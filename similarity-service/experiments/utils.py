from python_speech_features import mfcc
from bokeh.plotting import figure, show, output_file
import bokeh.layouts
import bokeh.models
import bokeh.embed
import bokeh.models.widgets
import bokeh.resources
import numpy as np
import sys
import os
import inspect
from jinja2 import Template
from bunch import Bunch
from pymongo import MongoClient
from tabulate import tabulate


def mfc(x_data, sample_rate):
    mfcc_data = []
    for amplitudes in x_data:
        mfcc_feat = mfcc(amplitudes, sample_rate)
        mfcc_data.append(mfcc_feat[0])
    return mfcc_data

def calculate_accuracy(actual_ratings, predicted_ratings, threshold=0.1):
    correct_predictions = 0
    for i, predicted in enumerate(predicted_ratings):
        actual = actual_ratings[i]
        if (compare(predicted, actual, threshold)):
            correct_predictions += 1
    accuracy = 100. * (correct_predictions)/len(predicted_ratings)
    return accuracy 

def compare(predicted, actual, threshold=0.2):
    if (predicted <= (actual + threshold) and predicted >= (actual - threshold)):
        return True
    return False

def plot(trained_data, title):
    # prepare some data
    predicted_ratings = trained_data.predicted
    actual_ratings = trained_data.actual

    # output to static HTML file
    output_file("log_lines.html")
    TOOLS_SM = "pan,save,box_select"
    TOOLS_LG = "pan,wheel_zoom,box_zoom,reset,save,box_select"
    plot_sm = figure(title=title, tools=TOOLS_SM, plot_width=500, plot_height=300, responsive=True, toolbar_location="above")
    plot_lg = figure(title=title, tools=TOOLS_LG, plot_width=1020, plot_height=700)

    x = []
    for (i, rating) in enumerate(predicted_ratings):
        x.append(i)
        plot_sm.add_layout(bokeh.models.Arrow(end=None, line_color="orange", x_start=i, y_start=rating, x_end=(i), y_end=(actual_ratings[i])))
        plot_lg.add_layout(bokeh.models.Arrow(end=None, line_color="orange", x_start=i, y_start=rating, x_end=(i), y_end=(actual_ratings[i])))

    plot_sm.square(x, predicted_ratings, legend="Predicted", color="red", alpha=0.5)
    plot_lg.square(x, predicted_ratings, legend="Predicted", color="red", alpha=0.5)
    plot_sm.circle(x, actual_ratings, legend="Actual", color="blue", alpha=0.3)
    plot_lg.circle(x, actual_ratings, legend="Actual", color="blue", alpha=0.3)

    template = get_report_template()
    html_sm = bokeh.embed.file_html(plot_sm, bokeh.resources.CDN, title, template=template)
    html_lg = bokeh.embed.file_html(plot_lg, bokeh.resources.CDN, title, template=template)

    return Bunch({
        "lg": html_lg,
        "sm": html_sm
    })


def generate_report(trained_data, original_data, train, title="", description=""):
    chart_html = plot(trained_data, title=title)
    YAML_headers = ('---\nlayout: default\ntitle: "{0}"\n---\n\n').format(title)
    path = os.path.realpath(__file__ + '../../../../docs/_experiments/')

    fullscreen_button = """<a href="{{site.url}}{{ site.baseurl }}/experiments/report_lg.html"> Full Screen </a>"""
    description = ("<p>{0}</p>").format(description)
    metrics = get_metrics(trained_data, original_data, train)
    train_code = "\n\n\n```python\n {0} \n```".format(''.join(inspect.getsourcelines(train)[0]))

    # Create the standard report
    report = open(path + "/report.md", "w")
    report.write(YAML_headers + description + metrics + train_code + chart_html.sm + fullscreen_button)
    report.close()
    # Create a seperate page for the fullscreen report
    YAML_headers = ('---\nlayout: fullscreen_graph\ntitle: "{0}"\n---').format(title + " __lg")
    fullscreen_graph = open(path + "/report_lg.md", "w")
    fullscreen_graph.write(YAML_headers + chart_html.lg)
    fullscreen_graph.close()

def get_report_template():
    with open('report_template.html', 'r') as f:
        template = Template(f.read())
    return template

def load_data():
    db = MongoClient()
    results = list(db.sqwaks.sounds.find())
    return results

def get_metrics(trained_data, original_data, train):
    predicted = trained_data.predicted
    actual = trained_data.actual
    reg = trained_data.reg
    
    x_data_test = trained_data.x_data_test
    y_data_test = trained_data.y_data_test

    mean_sqr_err = np.mean((predicted - actual) ** 2)
    variance = reg.score(x_data_test, y_data_test)
    accuracy = get_accuracy(original_data, train, num_iterations=1)
    
    headers = ["Mean Squared Error", "Variance", "Accuracy"]
    table = [[("%.2f" % mean_sqr_err), ("%.2f" % variance), ("%.2f" % accuracy)]]
    return "\n\n\n" + tabulate(table, headers, tablefmt="pipe")

#     return ("""
# | Mean Squared Error| Variance | Accuracy |\n
# |:------------------|:---------|:---------|\n
# |{0}                | {1}      | {2}%     |\n
#     """).format(("%.2f" % mean_sqr_err), ("%.2f" % variance), ("%.2f" % accuracy))

def get_accuracy(original_data, train, num_iterations=10):
    accuracy = 0
    for i in range(num_iterations):
        trained_data = train(original_data)
        predicted = trained_data.predicted
        actual = trained_data.actual

        accuracy += calculate_accuracy(predicted, actual)
    return accuracy/num_iterations
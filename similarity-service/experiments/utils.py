from python_speech_features import mfcc
from bokeh.plotting import figure, show, output_file
import bokeh.layouts
import bokeh.models
import bokeh.embed
import bokeh.models.widgets
import bokeh.resources
import sys
import os
from jinja2 import Template
from bunch import Bunch


def calculate_accuracy(actual_ratings, predicted_ratings, threshold=0.1):
    correct_predictions = 0
    for i, predicted in enumerate(predicted_ratings):
        actual = actual_ratings[i]
        if (compare(predicted, actual, threshold)):
            correct_predictions += 1
    accuracy = 100. * (correct_predictions)/len(predicted_ratings)
    return accuracy 
    
def mfc(amplitudes, sample_rate):
    mfcc_feat = mfcc(amplitudes, sample_rate)
    return mfcc_feat[0]

def compare(predicted, actual, threshold=0.2):
    if (predicted <= (actual + threshold) and predicted >= (actual - threshold)):
        return True
    return False

def plot(trained_data, title, will_show):
    # prepare some data
    predicted_ratings = trained_data.predicted
    actual_ratings = trained_data.actual

    # output to static HTML file
    output_file("log_lines.html")
    TOOLS = "pan,wheel_zoom,box_zoom,reset,save,box_select"
    plot_sm = figure(title=title, tools=TOOLS, plot_width=500, plot_height=300, responsive=True)
    plot_lg = figure(title=title, tools=TOOLS, plot_width=1020, plot_height=700)

    x = []
    for (i, rating) in enumerate(predicted_ratings):
        x.append(i)
        plot_sm.add_layout(bokeh.models.Arrow(end=None, line_color="orange", x_start=i, y_start=rating, x_end=(i), y_end=(actual_ratings[i])))
        plot_lg.add_layout(bokeh.models.Arrow(end=None, line_color="orange", x_start=i, y_start=rating, x_end=(i), y_end=(actual_ratings[i])))

    plot_sm.square(x, predicted_ratings, legend="Predicted", color="red", alpha=0.4)
    plot_lg.square(x, predicted_ratings, legend="Predicted", color="red", alpha=0.4)
    plot_sm.circle(x, actual_ratings, legend="Actual", color="blue", alpha=0.4)
    plot_lg.circle(x, actual_ratings, legend="Actual", color="blue", alpha=0.4)

    if(will_show):
        tab1 = bokeh.models.widgets.Panel(child=plot_sm, title="Data")
        show(bokeh.models.widgets.Tabs(tabs=[tab1]))
    template = get_report_template()
    html_sm = bokeh.embed.file_html(plot_sm, bokeh.resources.CDN, title, template=template)
    html_lg = bokeh.embed.file_html(plot_lg, bokeh.resources.CDN, title, template=template)

    return Bunch({
        "lg": html_lg,
        "sm": html_sm
    })


def generate_report(trained_data, title):
    html = plot(trained_data, title=title, will_show=False)
    YAML_headers = ('---\nlayout: default\ntitle: "{0}"\n---').format(title)
    path = os.path.realpath(__file__ + '../../../../docs/_experiments/')

    fullscreen_button = """<a href="{{site.url}}{{ site.baseurl }}/experiments/report_lg.html"> Full Screen </a>"""

    # Create the standard report
    report = open(path + "/report.md", "w")
    report.write(YAML_headers + html.sm + fullscreen_button)
    report.close()
    # Create a seperate page for the fullscreen report
    YAML_headers = ('---\nlayout: fullscreen_graph\ntitle: "{0}"\n---').format(title + " __lg")
    fullscreen_graph = open(path + "/report_lg.md", "w")
    fullscreen_graph.write(YAML_headers + html.lg)
    fullscreen_graph.close()

def get_report_template():
    with open('report_template.html', 'r') as f:
        template = Template(f.read())
    return template


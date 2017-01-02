from python_speech_features import mfcc
from bokeh.plotting import figure, show, output_file
import bokeh.layouts
import bokeh.models
import bokeh.models.widgets
from jinja2 import Template

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

def plot(trained_data, title):
    # prepare some data
    predicted_ratings = trained_data.predicted
    actual_ratings = trained_data.actual

    # output to static HTML file
    output_file("log_lines.html")
    TOOLS = "pan,wheel_zoom,box_zoom,reset,save,box_select"
    plot = figure(title=title, tools=TOOLS, plot_width=1020, plot_height=700)
    
    x = []
    for (i, rating) in enumerate(predicted_ratings):
        x.append(i)
        plot.add_layout(bokeh.models.Arrow(end=None, line_color="orange", x_start=i, y_start=rating, x_end=(i), y_end=(actual_ratings[i])))

    plot.square(x, predicted_ratings, legend="Predicted", color="red", alpha=0.4)
    plot.circle(x, actual_ratings, legend="Actual", color="blue", alpha=0.4)
    tab1 = bokeh.models.widgets.Panel(child=plot, title="Data")
    return show(bokeh.models.widgets.Tabs(tabs=[tab1]))


def get_report_template():
    with open('report_template.html', 'r') as f:
        template = Template(f.read())
    return template


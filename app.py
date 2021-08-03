import math
import bokeh.plotting.figure as bk_figure
from bokeh.io import curdoc, show
from bokeh.layouts import row, widgetbox
from bokeh.models import ColumnDataSource, Select
from bokeh.models.widgets import Slider, TextInput
import numpy as np
from bokeh.layouts import column, row

"""
Initialize global variables and functions
"""
M = 500
n = 0.375
R = 1
time1 = 5
time2 = 10
time3 = 20


def calculate_z(M, n):
    """
    Calculates z values for use in Bokeh plot curves

    :param M: mass (kg)
    :param n: porosity
    :return: x (range of curves), y/yy/y2 (concentration at different times)
    """
    x = np.arange(1.1, 400, 0.5)
    y = np.zeros([len(x)])
    yy = np.zeros([len(x)])
    y2 = np.zeros([len(x)])
    q = 1.667  # flow speed of groundwater in aquifer
    v = q / n
    D = v * 0.83 * (np.log10(x)) ** 2.414
    y = (M / (4 * math.pi * time1 * np.sqrt(D / R))) * np.exp(
        -((x - (((1.667 / n) * time1) / R)) ** 2) / (4 * D * time1 / R))
    yy = (M / (4 * math.pi * time2 * np.sqrt(D / R))) * np.exp(
        -((x - (((1.667 / n) * time2) / R)) ** 2) / (4 * D * time2 / R))
    y2 = (M / (4 * math.pi * time3 * np.sqrt(D / R))) * np.exp(
        -((x - (((1.667 / n) * time3) / R)) ** 2) / (4 * D * time3 / R))
    return x, y, yy, y2


x, y, yy, y2 = calculate_z(M, n)
source = ColumnDataSource(data=dict(x=x, y=y))
source1 = ColumnDataSource(data=dict(x=x, y=yy))
source2 = ColumnDataSource(data=dict(x=x, y=y2))

# Set up plotting function 
# set up the Bokeh figure first
plot = bk_figure(plot_height=400, plot_width=400, title="Concentration Signals (1 Dimension)",
                 tools="crosshair,pan,reset,save,wheel_zoom",
                 x_range=[-10, 350], y_range=[0, 15])
plot.xaxis.axis_label = 'Horizontal Distance (m)'
plot.yaxis.axis_label = 'Concentration (kg/m)'

# input three functions with 1, 5, 10 days
plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6, color='magenta', legend_label='5 days')
plot.line('x', 'y', source=source1, line_width=3, line_alpha=0.6, color='blue', legend_label='10 days')
plot.line('x', 'y', source=source2, line_width=3, line_alpha=0.6, color='green', legend_label='20 days')

# Set up widgets aka. sliders and text box
text = TextInput(title="title", value='Concentration Signals (1 Dimension)')
Mass = Slider(title="Pollution Mass (kg)", value=500, start=300, end=1000, step=5)
menu = Select(options=['Well Sorted Sand', 'Glacial Till', 'Silt'], value='Well Sorted Sand', title='Soil Type')

"""
Define Bokeh event handler callback functions
"""
def update_title(attrname, old, new):
    """
    Bokeh event handler callback that changes the title of the plot

    :param attrname: 'value' attribute of TextInput widget
    :param old: previous title value
    :param new: updated title value
    :return:
    """
    plot.title.text = text.value


def update_data(attrname, old, new):
    """
    Bokeh event handler callback that redraws the plot when the mass or menu are changed

    :param attrname: 'value' attribute of Mass and menu widgets
    :param old: previous values of mass and menu
    :param new: updated values of mass and menu
    """
    # Get the current slider values
    if menu.value == 'Well Sorted Sand':
        n = 0.375
    elif menu.value == 'Glacial Till':
        n = 0.15
    elif menu.value == 'Silt':
        n = 0.42
    M = Mass.value
    x, y, yy, y2 = calculate_z(M, n)
    # Generate the new curve
    source.data = dict(x=x, y=y)
    source1.data = dict(x=x, y=yy)
    source2.data = dict(x=x, y=y2)


for w in [Mass, menu]:
    w.on_change('value', update_data)

# Set up layouts and add to document
inputs = widgetbox(text, menu, Mass)
layout = row(plot, column(text, menu, Mass))

curdoc().add_root(layout)
curdoc().title = "Sliders"

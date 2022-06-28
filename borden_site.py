#!/usr/bin/env python
# coding: utf-8

# Author: Taylor Lithgow (git: tlithgow)
# Date: June-July 2022


#libraries from other scripts
import os
from bokeh.embed import components
from bokeh.models import Button, CustomJS
from bokeh.io import curdoc
from bokeh.io import output_notebook
import numpy as np
import pandas as pd
import math
import scipy.integrate as integrate
from bokeh.io import output_file, show
from bokeh.models import BasicTicker, ColorBar, LinearColorMapper, ColumnDataSource, PrintfTickFormatter
from bokeh.plotting import figure
from bokeh.transform import transform
from bokeh.palettes import Viridis256

np.set_printoptions(threshold=np.inf)
pd.options.display.max_seq_items = 2000

import timeit

start = timeit.timeit()
import bokeh.plotting.figure as bk_figure
from bokeh.io import curdoc, show
from bokeh.layouts import row, widgetbox
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Slider, TextInput

from bokeh.application import Application
from bokeh.application.handlers import FunctionHandler

print('The Borden Site - A Groundwater Contamination Study')






"""
Export bokeh objects for use in html - from one_dimension.py
"""
#from here on is changing python into html 
script, div = components({
    "Plot": plot,
    "Inputs": inputs
})

filename = "app/templates/bokeh_output/borden_site.html"
os.makedirs(os.path.dirname(filename), exist_ok=True)
with open(filename, "w") as f:
    f.write(script)

filename = "app/templates/bokeh_output/borden_site.html"
os.makedirs(os.path.dirname(filename), exist_ok=True)
f = open(filename, "w")
for key, value in div.items():
    f.write(str(value))
f.close()
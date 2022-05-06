# ***************************************
# Imports
# ***************************************
# Dash
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output

# Div.
import pandas as pd
import numpy as np
import calendar

# Plotly
import plotly.express as px
import plotly.graph_objects as go


#import datamodel.py file
import our_datamodel
all = our_datamodel.all_data()
attention = our_datamodel.attention()
meditation = our_datamodel.meditation()
stress = our_datamodel.stress()

#all_data = attention + meditation + stress

# Diagram - attention
fig_attention = px.bar(all)
fig_attention.show()

# Diagram - medication

# Diagram - stress



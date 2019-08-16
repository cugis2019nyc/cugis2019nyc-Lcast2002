# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 15:22:52 2019

@author: columbia
"""

import pandas

import plotly
dir(plotly)
from plotly.offline import plot
import plotly.graph_objs as go


studentbar= go.Bar(x=studentdf["Name"], y=studentdf["Age"])
print(studentbar)
go.Bar(studentbar)


agename = go.Bar(x=studentdf["Age"], y=studentdf["Name"])
agename
go.Bar(agename)
  

import pandas
wodf = pandas.read_excel("GISdata.xlsx", sheet_name= "womenOccupation")
wodf

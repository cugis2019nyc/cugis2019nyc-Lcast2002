# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 10:33:56 2019

@author: columbia
"""


import pandas
import plotly
from plotly.offline import plot
import plotly.graph_objs as go

wcdf = pandas.read_excel("GISdata.xlsx", sheet_name= "womenCEOs")
wodf

wcdf = pandas.read_excel("GISdata.xlsx",sheet_name = "womenCEOs")
wcdf
wcdfbar = go.Bar(x=wcdf["Year"], y = wcdf["CEOs"],
                 marker = {"color": wcdf["CEOs"],
                           "colorscale" : "Jet"})

layout = go.Layout(
                   #Title of the Graph
                   title = 'Share of CEOs',
                   
                   #Name of the X-axis
                   xaxis=go.layout.XAxis(
                            title=go.layout.xaxis.Title(
                            text='Year'
                            
                        )
                    ),
                  
                   #Name of Y-axis 
                   yaxis=go.layout.YAxis(
                            title=go.layout.yaxis.Title(
                            text='Percentages'
                        )
                    )
                  )

fig = go.Figure(data=[wcdfbar], layout=layout)
plot(fig)

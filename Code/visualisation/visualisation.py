# ****************************************************************************
#  * visualisation.py
#  *
#  * Algoritmen & Heuristieken
#  * DuraNett: Joey Bink, Jasper Claessen & Camiel de Kom
#  *
#  * This code makes visual representation of the SmartGrid model.
#  ***************************************************************************

from bokeh.plotting import figure, output_file, show
from bokeh.palettes import magma
import pandas as pd


def visualize(grid):
    graph = figure(title= "AmstelHaege")
    data = pd.read_csv(grid)
    color = magma(256)
    graph.scatter(data, color=color)
    show(graph)

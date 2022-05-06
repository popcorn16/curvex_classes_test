# Imports
import pandas as pd
import numpy as np
import calendar

# Plotly
import plotly.express as px
import plotly.graph_objects as go
import plotly
import matplotlib.pyplot as plt

#csv path
# ***************************************
# Get data
# ***************************************
githubpath = './data/'

plt.rcParams["figure.figsize"] = [10, 5]
plt.rcParams["figure.autolayout"] = True
plt.xlabel=("Sessions")
plt.ylabel=("Average")

# Import from csv file
#headers = ['id', 'Time', 'Stress', 'Attention', 'Mediation']



class all_data:
    def alldata(self):
        df = pd.read_csv(githubpath + "EEG_data.csv", index_col="id", sep=';')
        result = df.head(10)
        print(result)
        result.set_index('Sessions').plot(ylabel='Average reading', title='All measurements')
        #all_data()

        plt.show()


class stress_data(all_data):
    def stress():
        col_list = ["Sessions", "Stress"]
        df = pd.read_csv(githubpath + "EEG_data.csv", sep=';', usecols = col_list)
        result = df.head(10)
        print(result)
        result.set_index('Sessions').plot(ylabel='Average reading', title='Stress measurement')
        stress_data()
        
        plt.show()

stress1 = stress_data()

def test():
    if (info.Choice) == 1:
        stress1.stress()


class graph():
    def __init__ (self, Choice):
        self.Choice = Choice

info = graph (0)
info.Choice = ""    

# def attention():
#     col_list = ["Sessions", "Attention"]
#     df = pd.read_csv(githubpath + "EEG_data.csv", sep=';', usecols = col_list)
#     result = df.head(10)
#     print(result)
#     result.set_index('Sessions').plot(ylabel='Average reading', title='Attention measurement')
#     #result.plot(xlabel='Sessions', ylabel='Average', title='Plot Title')
#     attention()

#     plt.show()

# def meditation():
#     col_list = ["Sessions", "Meditation"]
#     df = pd.read_csv(githubpath + "EEG_data.csv", sep=';', usecols = col_list)
#     result = df.head(10)
#     print(result)
#     result.set_index('Sessions').plot(ylabel='Average reading', title='Meditation measurement')
#     meditation()

#     plt.show()











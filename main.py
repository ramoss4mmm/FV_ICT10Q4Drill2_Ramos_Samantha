from pyscript import display,document
import numpy as np
import matplotlib.pyplot as plt  # plt is a common alias

def graph(e):
    document.getElementById('output').innerHTML = " "

    days = np.array(['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun'])
    hours_slept = np.array([7, 6, 4, 8, 7, 6, 8]) #only sample data
    hours_graph = plt.plot(days, hours_slept)
    plt.show(hours_graph)
    plt.title("Hours of Sleep")
    plt.xlabel("Days")
    plt.ylabel("Hours Slept")
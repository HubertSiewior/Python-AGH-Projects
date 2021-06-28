#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import networkx as nx
from H1 import get_module_usage as gmu
import os
from random import randint


def draw_graph(files_array, show=True):
    MyGraph = nx.DiGraph()
    if not files_array or len(files_array) == 0:
        print("array is empty")
        exit(0)
    files_without_size = []
    correct_size = []
    for file_array_index, array_element in enumerate(files_array):
        file_size = files_array[file_array_index][1]
        file_name = files_array[file_array_index][0]

        if files_array[file_array_index][1] == None:
            files_without_size.append(file_name)

        MyGraph.add_node(file_name, size=file_size)
        dependence_array = array_element[len(array_element) - 1]
        if dependence_array == None:
            dependence_array = []

        for dependence_array_index, dependence_element in enumerate(dependence_array):
            if (dependence_element != 0) and (dependence_element != None):
                if dependence_element == -1:
                    MyGraph.add_edge(files_array[file_array_index][0], files_array[dependence_array_index][0],
                                     weight=True)
                else:
                    MyGraph.add_edge(files_array[file_array_index][0], files_array[dependence_array_index][0],
                                     weight=dependence_array[dependence_array_index])


    f = plt.figure()
    pos = nx.circular_layout(MyGraph)
    edge_labels = nx.get_edge_attributes(MyGraph, 'weight')
    for i, node in enumerate(MyGraph.nodes):
        for j in range(len(files_array)):
            if node == files_array[j][0]:
                if len(correct_size)==len(MyGraph.nodes):
                    break
                if node not in files_without_size:
                    correct_size.append(files_array[j][1])
                else:
                    correct_size.append(1000)


    nx.draw(MyGraph, pos, edge_color='black', node_size=correct_size, width=1, linewidths=1, alpha=0.75, \
            node_color='red', node_shape='o', arrowsize=25)
    nx.draw_networkx_labels(MyGraph, pos, labels={node: node for node in MyGraph.nodes()}, alpha=1)
    nx.draw_networkx_edge_labels(MyGraph, pos, edge_labels, label_pos=0.2, alpha=1)
    if show:
        plt.show()

    return f


def main(data):

    draw_graph(data)
    return 0


if __name__ == "__main__":
    module_data = [
        ["get_dependencies.py", 10024, [None, 20, 35, 0, 4]],
        ["draw_graphH3.py", 4048, True, [12, None, 38, 0, 3]],
        ["os.py", 1000, [32, -1, None, 9, 1]],
        ["test_h1.py", 2000, [43, 2, 32, None, 0]],
        ["os.py", 2000, [0, 9, 2, 0, None]]

    ]
    main(module_data)
    #main(gmu.main(os.path.dirname(os.getcwd()), False, False, False))

import matplotlib.pyplot as plt
import networkx as nx

import os
from random import randint


def draw_graphH3(files_array, show=True):
    if not files_array or len(files_array) == 0:
        print("array is empty")
        exit(0)
    colors = []
    colors_of_moduls = []
    correct_size = []
    names_of_files = []
    node_names = []
    MyGraph = nx.DiGraph()
    count = len(files_array)
    for files_array_index, modul in enumerate(files_array):
        count += len(modul)
    for count_index in range(count):
        colors.append('#%06X' % randint(0, 0xFFFFFF))

    for files_array_index, modul in enumerate(files_array):
        MyGraph.add_node(modul[0][2], size=20000)
        colors_of_moduls.append(colors[files_array_index])
        for modul_index, modul_element in enumerate(modul):
            MyGraph.add_edge(files_array[files_array_index][modul_index][0], modul[0][2])
            file_name = modul_element[0]
            file_size = modul_element[1]
            if file_size == None:
                file_size = 1000
            if file_name not in names_of_files:
                colors_of_moduls.append(colors[files_array_index])
                names_of_files.append(file_name)
            MyGraph.add_node(file_name, size=file_size)
            dependence_array = modul_element[-1]
            if dependence_array == None:
                dependence_array = []
            for dependence_array_index, dependence_array_element in enumerate(dependence_array):
                for z, dependence in enumerate(dependence_array_element):
                    if (dependence != None and dependence != None):
                        MyGraph.add_edge(files_array[files_array_index][modul_index][0],
                                         files_array[dependence_array_index][z][0], weight=dependence)

    for files_array_index, modul in enumerate(files_array):
        for nodes_index, nodeName in enumerate(MyGraph.nodes):
            for dependence_array_index, fileElement in enumerate(modul):
                if len(correct_size) == len(MyGraph.nodes):
                    break
                if nodeName == fileElement[2] and nodeName not in node_names:
                    correct_size.append(20000)
                    node_names.append(nodeName)
                if nodeName == fileElement[0] and nodeName not in node_names:
                    correct_size.append(fileElement[1])
                    node_names.append(nodeName)

    f = plt.figure()
    edge_labels = nx.get_edge_attributes(MyGraph, 'weight')
    pos = nx.circular_layout(MyGraph)
    nx.draw(MyGraph, pos, node_size=correct_size, width=1, linewidths=1, alpha=0.75, node_color=colors_of_moduls,
            node_shape='o', arrowsize=25)
    nx.draw_networkx_labels(MyGraph, pos, labels={node: node for node in MyGraph.nodes()}, alpha=1)
    nx.draw_networkx_edge_labels(MyGraph, pos, edge_labels, label_pos=0.2)
    if show:
        plt.show()

    return f


def main(data):
    draw_graphH3(data)
    return 0


if __name__ == "__main__":
    module_data = [

        [["jeden.py", 5000, "modul1", [[None, 20, 35, 4, 9], [12, None, 38, 2, 3], [None]]],
         ["dwa.py", 2000, "modul1", [[None, None, 35, 4, 9], [12, None, 800, 2, 3], [None]]],
         ["trzy.py", 3000, "modul1", [[None, 200, None, 4, 9], [12, None, 38, 2, 3], [None]]],
         ["cztery.py", 4000, "modul1", [[None, 20, 35, None, 9], [12, None, 38, 2, 3], [None]]],
         ["piec.py", 1000, "modul1", [[None, 20, 35, 4, None], [12, None, 38, 2, 3], [None]]]],

        [["szesc.py", 100, "modul2", [[None, 20, 35, 4, 9], [12, None, 38, 2, 3], [None]]],
         ["siedem.py", 2000, "modul2", [[None, None, 35, 4, 9], [12, None, 38, 2, 3], [None]]],
         ["osiem.py", 3000, "modul2", [[None, 20, None, 4, 9], [12, None, 38, 2, 3], [None]]],
         ["dziewiec.py", 4000, "modul2", [[None, 20, 35, None, 9], [12, None, 38, 2, 3], [None]]],
         ["dziesiec.py", 5000, "modul2", [[None, 20, 35, 4, 9], [12, None, 38, 2, 3], [None]]]],

        [["jedenascie.py", 1000, "modul3", [[None, 20, 35, 4, 9], [12, None, 38, 2, 3], [None]]]]

    ]

    main(module_data)
    # main(gmu.main(os.path.dirname(os.getcwd()), False, False, False))

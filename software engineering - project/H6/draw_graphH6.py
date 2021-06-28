import matplotlib.pyplot as plt
import networkx as nx
from random import randint


def draw_graphH6(files_array,show=True):
    if not files_array or len(files_array) == 0:
        print("array is empty")
        exit(0)

    colors = []
    colors_of_modules = []
    correct_size = []
    names_of_files = []
    names_of_functions = []
    my_graph = nx.DiGraph()

    count = len(files_array)
    for files_array_index, module in enumerate(files_array):
        count += len(module)
    for count_index in range(count):
        colors.append('#%06X' % randint(0, 0xFFFFFF))

    for files_array_index, module in enumerate(files_array):
        if module[0][1] not in names_of_files:
            my_graph.add_node(module[0][1])
            colors_of_modules.append(colors[files_array_index])
            names_of_files.append(module[0][1])
        for module_index, function in enumerate(module[1]):
            if function not in names_of_functions:
                my_graph.add_node(function)
                colors_of_modules.append(colors[names_of_files.index(module[0][1])])
                names_of_functions.append(function)
            my_graph.add_edge(function, module[0][1])

    for node_index, node in enumerate(my_graph.nodes):
        if len(correct_size) == len(my_graph.nodes):
            break
        if node not in names_of_files:
            correct_size.append(100)
        else:
            correct_size.append(3500)
    f = plt.figure()
    pos = nx.circular_layout(my_graph)
    nx.draw(my_graph, pos, node_size=correct_size, alpha=0.75, node_color=colors_of_modules, node_shape='o',
            arrowsize=25, width=1, linewidths=1)
    nx.draw_networkx_labels(my_graph, pos, labels={node: node for node in my_graph.nodes()})
    if show:
        plt.show()

    return f


def main(data):
    draw_graphH6(data)
    return 0


if __name__ == "__main__":
    # dane pomocnicze
    module_data = [
        [["H1", "jeden.py"], ["funkcja1", "funkcja2", "funkcja3", "funkcja4", "funkcja5", "funkcja6"]],
        [["H2", "dwa.py"], ["funkcja7", "funkcja8", "funkcja9"]],
        [["H2", "trzy.py"], ["funkcja10", "funkcja11", "funkcja12", "funkcja13", "funkcja14"]],
        [["H3", "cztery.py"], ["funkcja15", "funkcja166", "funkcja17", "funkcja18"]],
        [["H3", "piec.py"], ["funkcja19", "funkcja20", "funkcja21", "funkcja22", "funkcja23"]],
        [["H3", "szesc.py"], ["funkcja24", "funkcja25"]],
        [["H4", "siedem.py"], ["funkcja26"]],
        [["H4", "osiem.py"],
         ["funkcja27", "funkcja28", "funkcja29", "funkcja30", "funkcja31", "funkcja32", "funkcja33"]],
        [["H6", "dziewiec.py"], ["funkcja34", "funkcja35", "funkcja36"]],
        [["H6", "dziesiec.py"], ["funkcja37", "funkcja38"]],
        [["H6", "jeden.py"], ["funkcja222", "funkcja111"]]
    ]

    main(module_data)

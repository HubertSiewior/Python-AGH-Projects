from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QTabWidget, QVBoxLayout
import matplotlib.pyplot as plt
import sys
import networkx as nx
from H3 import draw_graphH3 as h3
from H1 import draw_graph as h1
from H6 import  draw_graphH6 as h6
from random import randint



class plotWindow():
    def __init__(self, parent=None):
        self.app = QApplication(sys.argv)
        self.MainWindow = QMainWindow()
        self.MainWindow.__init__()
        self.MainWindow.setWindowTitle("plot window")
        self.canvases = []
        self.figure_handles = []
        self.toolbar_handles = []
        self.tab_handles = []
        self.current_window = -1
        self.tabs = QTabWidget()
        self.MainWindow.setCentralWidget(self.tabs)
        self.MainWindow.resize(1280, 900)
        self.MainWindow.show()

    def addPlot(self, title, figure):
        new_tab = QWidget()
        layout = QVBoxLayout()
        new_tab.setLayout(layout)

        figure.subplots_adjust(left=0.05, right=0.99, bottom=0.05, top=0.91, wspace=0.2, hspace=0.2)
        new_canvas = FigureCanvas(figure)
        new_toolbar = NavigationToolbar(new_canvas, new_tab)

        layout.addWidget(new_canvas)
        layout.addWidget(new_toolbar)
        self.tabs.addTab(new_tab, title)

        self.toolbar_handles.append(new_toolbar)
        self.canvases.append(new_canvas)
        self.figure_handles.append(figure)
        self.tab_handles.append(new_tab)

    def show(self):
        self.app.exec_()


def draw_multiple_graph(files_array1, files_array2, files_array3,files_array6):
    pw = plotWindow()
    f1 = h1.draw_graph(files_array1, False)
    f2 = h1.draw_graph(files_array2, False)
    f3 = h3.draw_graphH3(files_array3, False)
    f6  = h6.draw_graphH6(files_array6,False)
    pw.addPlot("h1", f1)
    pw.addPlot("h2", f2)
    pw.addPlot("h3", f3)
    pw.addPlot("h6",f6)

    pw.show()


def main(data1, data2, data3,data6):
    draw_multiple_graph(data1, data2, data3,data6)

    return 0


if __name__ == "__main__":
    module_data3 = [

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

    module_data1 = [
        ["get_dependencies.py", 10024, [None, 20, 35, 0, 4]],
        ["draw_graphH3.py", 4048, True, [12, None, 38, 0, 3]],
        ["os.py", 1000, [32, -1, None, 9, 1]],
        ["test_h1.py", 2000, [43, 2, 32, None, 0]],
        ["plik4.py", 2000, [0, 9, 2, 0, None]]

    ]

    module_data2 = [
        ["funkcja1", 100, [None, 0, 35, 40, 4, 0]],
        ["funkcja2", 2008, [12, None, 38, 0, 3, 0]],
        ["funkcja3", 4000, [32, 0, None, 9, 3, 0]],
        ["funkcja4", 5000, [43, 2, 4, None, 7, 0]],
        ["funkcja5", 20000, [1, 0, 0, None, 0, 9]],
        ["funkcja5", 20000, [1, 0, 0, 0, None, 3]],
        ["funkcja6", 20000, [1, 0, 0, 0, 3, None]]

    ]

    module_data6 = [
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

    main(module_data1, module_data2, module_data3,module_data6)

import sys
import os
from easygui import buttonbox

from H1 import h1
from H2 import h2
from H3 import h3
from H4 import h4
from H5 import h5
from H6 import h6

H1 = "Historyjka 1 - graf dependencji plików"
H2 = "Historyjka 2 - graf dependencji funkcji"
H3 = "Historyjka 3 - graf dependencji modułów i funkcji"
H4 = "Historyjka 4 - generacja danych do formatu XML"
H5 = "Historyjka 5 - pokazanie historyjek 1-3 na jednym programie"
H6 = "Historyjka 6 - graf dependencji funkcji i plików"


def main():
    path = os.getcwd()
    image = "logo.png"
    msg = "Przedstawiamy program na IO - JD Team"
    choices = [H1, H2, H3, H4, H5, H6]
    while True:
        reply = buttonbox(msg, title="Program na IO - JD Team", image=image, choices=choices)
        if reply == H1:
            h1.main(path)
        elif reply == H2:
            h2.main(path)
        elif reply == H3:
            h3.main()
        elif reply == H4:
            h4.main("xml", path)
        elif reply == H5:
            h5.main(path)
        elif reply == H6:
            h6.main(path)
        else:
            exit()


if __name__ == '__main__':
    main()

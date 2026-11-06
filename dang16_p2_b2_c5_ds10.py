import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang16_p2_b2_c5_ds10(self):
            # Khai báo biến
            # Khai báo biến
            a = random.randint(1, 5) # Random cạnh khối lập phương nhỏ
            A = 2 * a                # Cạnh khối lập phương lớn
            hinhve=r'''\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-0.7,xscale=0.7]
            	\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (160,110) -- (315.07,110.13) ;
            	\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (160,110) -- (161.73,241.47) ;
            	\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (161.73,241.47) -- (316.8,241.6) ;
            	\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (316.8,241.6) -- (315.07,110.13) ;
            	\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (92.67,58) -- (247.73,58.13) ;
            	\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (247.73,58.13) -- (315.07,110.13) ;
            	\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (92.67,58) -- (160,110) ;
            	\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (92.67,58) -- (94.4,189.47) ;
            	\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (94.4,189.47) -- (161.73,241.47) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1]    (170.2,58.07) -- (237.53,110.07) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1]    (237.53,110.07) -- (239.27,241.53) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1]    (126.33,84) -- (281.4,84.13) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1]    (126.33,84) -- (128.07,215.47) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1]    (93.53,123.73) -- (160.87,175.73) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1]    (160.87,175.73) -- (315.93,175.87) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (247.73,58.13) -- (249.47,189.6) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (316.8,241.6) -- (250.4,185.47) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (94.4,189.47) -- (250.4,185.47) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (170.2,58.07) -- (171.93,189.53) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (171.93,189.53) -- (239.27,241.53) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (281.4,84.13) -- (283.13,215.6) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (128.07,215.47) -- (283.6,213.53) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (93.53,123.73) -- (248.6,123.87) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (248.6,123.87) -- (315.93,175.87) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (203.87,84.07) -- (205.6,215.53) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (127.2,149.73) -- (282.27,149.87) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (171.07,123.8) -- (238.4,175.8) ;
            	\draw [color={rgb, 255:red, 245; green, 166; blue, 35 }  ,draw opacity=1 ][line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (94.4,189.47) -- (316.8,241.6) ;
            	\draw [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (94.4,189.47) -- (315.07,110.13) ;
            	\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (86.1,58) .. controls (86.1,54.37) and (89.04,51.43) .. (92.67,51.43) .. controls (96.29,51.43) and (99.23,54.37) .. (99.23,58) .. controls (99.23,61.63) and (96.29,64.57) .. (92.67,64.57) .. controls (89.04,64.57) and (86.1,61.63) .. (86.1,58) -- cycle ;
            	\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (119.77,84) .. controls (119.77,80.37) and (122.71,77.43) .. (126.33,77.43) .. controls (129.96,77.43) and (132.9,80.37) .. (132.9,84) .. controls (132.9,87.63) and (129.96,90.57) .. (126.33,90.57) .. controls (122.71,90.57) and (119.77,87.63) .. (119.77,84) -- cycle ;
            	\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (153.43,110) .. controls (153.43,106.37) and (156.37,103.43) .. (160,103.43) .. controls (163.63,103.43) and (166.57,106.37) .. (166.57,110) .. controls (166.57,113.63) and (163.63,116.57) .. (160,116.57) .. controls (156.37,116.57) and (153.43,113.63) .. (153.43,110) -- cycle ;
            	\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (163.63,58.07) .. controls (163.63,54.44) and (166.57,51.5) .. (170.2,51.5) .. controls (173.83,51.5) and (176.77,54.44) .. (176.77,58.07) .. controls (176.77,61.69) and (173.83,64.63) .. (170.2,64.63) .. controls (166.57,64.63) and (163.63,61.69) .. (163.63,58.07) -- cycle ;
            	\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (241.17,58.13) .. controls (241.17,54.51) and (244.11,51.57) .. (247.73,51.57) .. controls (251.36,51.57) and (254.3,54.51) .. (254.3,58.13) .. controls (254.3,61.76) and (251.36,64.7) .. (247.73,64.7) .. controls (244.11,64.7) and (241.17,61.76) .. (241.17,58.13) -- cycle ;
            	\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (197.3,84.07) .. controls (197.3,80.44) and (200.24,77.5) .. (203.87,77.5) .. controls (207.49,77.5) and (210.43,80.44) .. (210.43,84.07) .. controls (210.43,87.69) and (207.49,90.63) .. (203.87,90.63) .. controls (200.24,90.63) and (197.3,87.69) .. (197.3,84.07) -- cycle ;
            	\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (274.83,84.13) .. controls (274.83,80.51) and (277.77,77.57) .. (281.4,77.57) .. controls (285.03,77.57) and (287.97,80.51) .. (287.97,84.13) .. controls (287.97,87.76) and (285.03,90.7) .. (281.4,90.7) .. controls (277.77,90.7) and (274.83,87.76) .. (274.83,84.13) -- cycle ;
            	\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (230.97,110.07) .. controls (230.97,106.44) and (233.91,103.5) .. (237.53,103.5) .. controls (241.16,103.5) and (244.1,106.44) .. (244.1,110.07) .. controls (244.1,113.69) and (241.16,116.63) .. (237.53,116.63) .. controls (233.91,116.63) and (230.97,113.69) .. (230.97,110.07) -- cycle ;
            	\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (308.5,110.13) .. controls (308.5,106.51) and (311.44,103.57) .. (315.07,103.57) .. controls (318.69,103.57) and (321.63,106.51) .. (321.63,110.13) .. controls (321.63,113.76) and (318.69,116.7) .. (315.07,116.7) .. controls (311.44,116.7) and (308.5,113.76) .. (308.5,110.13) -- cycle ;
            	\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (86.97,123.73) .. controls (86.97,120.11) and (89.91,117.17) .. (93.53,117.17) .. controls (97.16,117.17) and (100.1,120.11) .. (100.1,123.73) .. controls (100.1,127.36) and (97.16,130.3) .. (93.53,130.3) .. controls (89.91,130.3) and (86.97,127.36) .. (86.97,123.73) -- cycle ;
            	\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (87.83,189.47) .. controls (87.83,185.84) and (90.77,182.9) .. (94.4,182.9) .. controls (98.03,182.9) and (100.97,185.84) .. (100.97,189.47) .. controls (100.97,193.09) and (98.03,196.03) .. (94.4,196.03) .. controls (90.77,196.03) and (87.83,193.09) .. (87.83,189.47) -- cycle ;
            	\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (120.63,149.73) .. controls (120.63,146.11) and (123.57,143.17) .. (127.2,143.17) .. controls (130.83,143.17) and (133.77,146.11) .. (133.77,149.73) .. controls (133.77,153.36) and (130.83,156.3) .. (127.2,156.3) .. controls (123.57,156.3) and (120.63,153.36) .. (120.63,149.73) -- cycle ;
            	\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (121.5,215.47) .. controls (121.5,211.84) and (124.44,208.9) .. (128.07,208.9) .. controls (131.69,208.9) and (134.63,211.84) .. (134.63,215.47) .. controls (134.63,219.09) and (131.69,222.03) .. (128.07,222.03) .. controls (124.44,222.03) and (121.5,219.09) .. (121.5,215.47) -- cycle ;
            	\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (154.3,175.73) .. controls (154.3,172.11) and (157.24,169.17) .. (160.87,169.17) .. controls (164.49,169.17) and (167.43,172.11) .. (167.43,175.73) .. controls (167.43,179.36) and (164.49,182.3) .. (160.87,182.3) .. controls (157.24,182.3) and (154.3,179.36) .. (154.3,175.73) -- cycle ;
            	\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (155.17,241.47) .. controls (155.17,237.84) and (158.11,234.9) .. (161.73,234.9) .. controls (165.36,234.9) and (168.3,237.84) .. (168.3,241.47) .. controls (168.3,245.09) and (165.36,248.03) .. (161.73,248.03) .. controls (158.11,248.03) and (155.17,245.09) .. (155.17,241.47) -- cycle ;
            	\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (231.83,175.8) .. controls (231.83,172.17) and (234.77,169.23) .. (238.4,169.23) .. controls (242.03,169.23) and (244.97,172.17) .. (244.97,175.8) .. controls (244.97,179.43) and (242.03,182.37) .. (238.4,182.37) .. controls (234.77,182.37) and (231.83,179.43) .. (231.83,175.8) -- cycle ;
            	\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (198.17,149.8) .. controls (198.17,146.17) and (201.11,143.23) .. (204.73,143.23) .. controls (208.36,143.23) and (211.3,146.17) .. (211.3,149.8) .. controls (211.3,153.43) and (208.36,156.37) .. (204.73,156.37) .. controls (201.11,156.37) and (198.17,153.43) .. (198.17,149.8) -- cycle ;
            	\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (164.5,123.8) .. controls (164.5,120.17) and (167.44,117.23) .. (171.07,117.23) .. controls (174.69,117.23) and (177.63,120.17) .. (177.63,123.8) .. controls (177.63,127.43) and (174.69,130.37) .. (171.07,130.37) .. controls (167.44,130.37) and (164.5,127.43) .. (164.5,123.8) -- cycle ;
            	\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (165.83,187.47) .. controls (165.83,183.84) and (168.77,180.9) .. (172.4,180.9) .. controls (176.03,180.9) and (178.97,183.84) .. (178.97,187.47) .. controls (178.97,191.09) and (176.03,194.03) .. (172.4,194.03) .. controls (168.77,194.03) and (165.83,191.09) .. (165.83,187.47) -- cycle ;
            	\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (199.27,214.5) .. controls (199.27,210.87) and (202.21,207.93) .. (205.83,207.93) .. controls (209.46,207.93) and (212.4,210.87) .. (212.4,214.5) .. controls (212.4,218.13) and (209.46,221.07) .. (205.83,221.07) .. controls (202.21,221.07) and (199.27,218.13) .. (199.27,214.5) -- cycle ;
            	\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (232.7,241.53) .. controls (232.7,237.91) and (235.64,234.97) .. (239.27,234.97) .. controls (242.89,234.97) and (245.83,237.91) .. (245.83,241.53) .. controls (245.83,245.16) and (242.89,248.1) .. (239.27,248.1) .. controls (235.64,248.1) and (232.7,245.16) .. (232.7,241.53) -- cycle ;
            	\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (242.03,123.87) .. controls (242.03,120.24) and (244.97,117.3) .. (248.6,117.3) .. controls (252.23,117.3) and (255.17,120.24) .. (255.17,123.87) .. controls (255.17,127.49) and (252.23,130.43) .. (248.6,130.43) .. controls (244.97,130.43) and (242.03,127.49) .. (242.03,123.87) -- cycle ;
            	\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (275.7,149.87) .. controls (275.7,146.24) and (278.64,143.3) .. (282.27,143.3) .. controls (285.89,143.3) and (288.83,146.24) .. (288.83,149.87) .. controls (288.83,153.49) and (285.89,156.43) .. (282.27,156.43) .. controls (278.64,156.43) and (275.7,153.49) .. (275.7,149.87) -- cycle ;
            	\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (309.37,175.87) .. controls (309.37,172.24) and (312.31,169.3) .. (315.93,169.3) .. controls (319.56,169.3) and (322.5,172.24) .. (322.5,175.87) .. controls (322.5,179.49) and (319.56,182.43) .. (315.93,182.43) .. controls (312.31,182.43) and (309.37,179.49) .. (309.37,175.87) -- cycle ;
            	\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (310.23,241.6) .. controls (310.23,237.97) and (313.17,235.03) .. (316.8,235.03) .. controls (320.43,235.03) and (323.37,237.97) .. (323.37,241.6) .. controls (323.37,245.23) and (320.43,248.17) .. (316.8,248.17) .. controls (313.17,248.17) and (310.23,245.23) .. (310.23,241.6) -- cycle ;
            	\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (277.03,213.53) .. controls (277.03,209.91) and (279.97,206.97) .. (283.6,206.97) .. controls (287.23,206.97) and (290.17,209.91) .. (290.17,213.53) .. controls (290.17,217.16) and (287.23,220.1) .. (283.6,220.1) .. controls (279.97,220.1) and (277.03,217.16) .. (277.03,213.53) -- cycle ;
            	\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (243.83,185.47) .. controls (243.83,181.84) and (246.77,178.9) .. (250.4,178.9) .. controls (254.03,178.9) and (256.97,181.84) .. (256.97,185.47) .. controls (256.97,189.09) and (254.03,192.03) .. (250.4,192.03) .. controls (246.77,192.03) and (243.83,189.09) .. (243.83,185.47) -- cycle ;
            \end{tikzpicture}'''
            # Nội dung câu hỏi
            noidungcauhoi = (r'''\immini{Một khối lập phương cạnh $%s$ cm được chia thành $8$ khối lập phương nhỏ cạnh $%s$ cm. Xét các điểm là đỉnh của các khối lập phương nhỏ đó.}{%s}''' % (A, a, hinhve))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Có tất cả $27$ điểm là đỉnh của các khối lập phương nhỏ'
            nb_da_1_s = 'Có tất cả $24$ điểm là đỉnh của các khối lập phương nhỏ'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Các đỉnh của các khối lập phương nhỏ tạo thành một mạng điểm $3 \\times 3 \\times 3$ nên có tổng cộng $27$ điểm.''')

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Số bộ $3$ điểm thẳng hàng được tạo ra từ $27$ điểm trên là $49$'
            th_da_1_s = 'Số bộ $3$ điểm thẳng hàng được tạo ra từ $27$ điểm trên là $27$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Đếm số bộ $3$ điểm thẳng hàng: \\\\
            - Các đường thẳng song song với các cạnh của khối lập phương: $3$ hướng $\\times$ $3 \\times 3 = 27$ đường. \\\\
            - Các đường chéo trên các mặt: $3$ nhóm mặt $\\times$ $3$ mặt mỗi nhóm $\\times$ $2$ đường chéo $= 18$ đường. \\\\
            - Các đường chéo không gian: $4$ đường. \\\\
            Vậy số bộ $3$ điểm thẳng hàng là: $27 + 18 + 4 = 49$.''')

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Số cách chọn ra $3$ điểm bất kỳ từ $27$ điểm nói trên là $2925$'
            vd_da_1_s = 'Số cách chọn ra $3$ điểm bất kỳ từ $27$ điểm nói trên là $2876$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Mỗi cách chọn $3$ điểm ngẫu nhiên từ $27$ điểm là một tổ hợp chập $3$ của $27$. \\\\
            Số cách chọn là: $C_{27}^3 = \\frac{27!}{3! \\cdot 24!} = \\frac{27 \\cdot 26 \\cdot 25}{3 \\cdot 2 \\cdot 1} = 2925$.''')

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Số tam giác được tạo thành từ các đỉnh của các khối lập phương nhỏ là $2876$'
            vdc_da_1_s = 'Số tam giác được tạo thành từ các đỉnh của các khối lập phương nhỏ là $2925$'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Để $3$ điểm tạo thành một tam giác thì $3$ điểm đó phải không thẳng hàng. \\\\
            Do đó, số tam giác tạo thành bằng tổng số cách chọn $3$ điểm bất kỳ trừ đi số bộ $3$ điểm thẳng hàng. \\\\
            Vậy số tam giác là: $2925 - 49 = 2876$ (tam giác).''')

            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vdc)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 đúng
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán lại vào list
            list_nb_1 = [nb_da_1]
            list_th_1 = [th_da_1]
            list_vd_1 = [vd_da_1]
            list_vdc_1 = [vdc_da_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            combined_th = list(zip(list_th_1, list_th_2))
            combined_vd = list(zip(list_vd_1, list_vd_2))
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            random.shuffle(combined_nb)
            random.shuffle(combined_th)
            random.shuffle(combined_vd)
            random.shuffle(combined_vdc)

            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ '\n'
                '\\choiceTFn \n'
                '{'+str(shuffled_answers_nb[0])+'}\n'
                '{'+str(shuffled_answers_th[0])+'}\n'
                '{'+str(shuffled_answers_vd[0])+'}\n'
                '{'+str(shuffled_answers_vdc[0])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions_nb[0])+'\n'
                '\\item '+str(shuffled_solutions_th[0])+'\n'
                '\\item '+str(shuffled_solutions_vd[0])+'\n'
                '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


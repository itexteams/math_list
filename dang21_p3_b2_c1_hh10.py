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


def bt_dang21_p3_b2_c1_hh10(self):
    # (a, b, h) với a = AB = BC = CD, b là thông số phụ thuộc độ rộng giảm
    configs = [
        (2, 1, 4), # Bài gốc
        (3, 1, 5),
        (3, 2, 4),
        (4, 2, 6),
        (2, 1, 5),
        (4, 1, 5)
    ]
    a, b, h_val = random.choice(configs)

    k_val = Rational(2*(a-b), 3*a) # Độ rộng giảm đi k
    c = a - b
    d = a * b
    num = 2 * c * h_val * (h_val**2 + d)
    den = (h_val**2 + d)**2 - (c * h_val)**2
    T_val = Rational(num, den) # Giá trị của tan(alpha - theta)

    W1 = 3 * a
    W2 = 2 * b + a

    # Các đáp án trắc nghiệm
    da = h_val
    s = [h_val + 1, h_val + 2, h_val + 3, h_val - 1, h_val - 2, h_val + 4]
    if h_val - 1 <= 0:
        s.remove(h_val - 1)
    if h_val - 2 <= 0:
        s.remove(h_val - 2)

    das1 = random.choice(s)
    s.remove(das1)
    das2 = random.choice(s)
    s.remove(das2)
    das3 = random.choice(s)

    tikz_code = (''' \\begin{center}  
    	\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
    		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.56 ][fill={rgb, 255:red, 234; green, 238; blue, 244 }  ,fill opacity=1 ] (84.33,122.27) .. controls (87.98,115.82) and (117.23,116.07) .. (118.47,123.6) .. controls (119.13,144.6) and (118.47,160.6) .. (118.47,184.93) .. controls (117.13,192.93) and (89.8,194.93) .. (85.13,186.27) .. controls (83.8,159.6) and (83.47,147.6) .. (84.33,122.27) -- cycle ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.8 ] (88,135.93) .. controls (94.13,133.6) and (106.13,132.6) .. (115.13,136.27) .. controls (113.13,140.27) and (112.8,141.6) .. (111.13,145.27) .. controls (105.8,144.27) and (98.47,143.93) .. (91.13,144.93) .. controls (90.13,141.6) and (89.23,140.07) .. (88,135.93) -- cycle ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.8 ] (86.98,140.07) .. controls (91.23,147.07) and (91.73,172.07) .. (88.73,177.57) .. controls (87.73,174.23) and (85.73,145.07) .. (86.98,140.07) -- cycle ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.8 ] (115.14,140.48) .. controls (110.49,147.77) and (110.83,173.04) .. (114.73,178.32) .. controls (115.73,174.92) and (116.92,145.39) .. (115.14,140.48) -- cycle ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.8 ] (89.23,182.07) .. controls (95.37,184.48) and (104.73,186.1) .. (113.73,182.32) .. controls (112.23,178.07) and (112.8,176.3) .. (111.13,172.52) .. controls (105.8,173.55) and (98.57,174.1) .. (91.23,173.07) .. controls (90.23,176.51) and (90.47,177.8) .. (89.23,182.07) -- cycle ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.8 ] (91.73,147.07) .. controls (94.23,155.07) and (93.23,165.07) .. (92.23,171.07) .. controls (91.23,167.73) and (93.23,162.07) .. (91.73,147.07) -- cycle ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.8 ] (111.23,146.82) .. controls (108.45,154.82) and (109.56,164.82) .. (110.68,170.82) .. controls (111.79,167.48) and (109.56,161.82) .. (111.23,146.82) -- cycle ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.8 ] (87.73,123.07) .. controls (90.23,129.57) and (88.98,131.07) .. (88,135.93) .. controls (87,132.6) and (89.23,138.07) .. (87.73,123.07) -- cycle ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.8 ] (115.37,123.4) .. controls (113.17,129.9) and (114.27,131.4) .. (115.13,136.27) .. controls (116.01,132.93) and (114.05,138.4) .. (115.37,123.4) -- cycle ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.2 ] (84.33,122.27) .. controls (85.37,122.11) and (86.52,121.96) .. (86.73,125.57) .. controls (85.48,128.07) and (86.02,140.46) .. (85.48,144.82) .. controls (84.93,149.35) and (84.72,146.51) .. (83.73,148.32) .. controls (83.98,133.57) and (83.08,127.27) .. (84.33,122.27) -- cycle ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.2 ] (84.48,169.32) .. controls (85.52,169.16) and (88.27,169.46) .. (88.48,173.07) .. controls (87.23,175.57) and (89.77,181.71) .. (89.23,186.07) .. controls (88.68,190.6) and (86.12,184.46) .. (85.13,186.27) .. controls (85.38,171.52) and (83.23,174.32) .. (84.48,169.32) -- cycle ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.2 ] (89.58,119.27) .. controls (93.73,117.07) and (117.02,117.96) .. (117.23,121.57) .. controls (116.23,122.07) and (114.73,120.32) .. (115.37,122.4) .. controls (111.73,119.82) and (91.73,117.32) .. (87.73,122.07) .. controls (86.73,117.07) and (88.33,124.27) .. (89.58,119.27) -- cycle ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.2 ] (115.98,120.82) -- (118.47,123.6) -- (118.23,142.82) -- (115.14,140.48) -- (116.73,125.07) -- cycle ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.2 ] (115.98,171.32) -- (117.73,168.07) -- (117.73,186.07) -- (113.23,187.82) -- (114.98,175.07) -- cycle ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.2 ] (111.98,188.32) -- (113.98,189.82) -- (100.73,192.07) -- (89.23,189.57) -- (90.23,188.07) -- (100.23,190.07) -- cycle ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.2 ] (91.23,119.82) -- (88.98,132.07) -- (87.73,123.07) -- cycle ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.2 ] (115.37,122.4) -- (114.23,132.07) -- (112.23,120.82) -- cycle ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (91.23,189.07) -- (89.23,189.57) -- (85.13,186.27) -- (85.23,184.32) -- cycle ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (117.73,186.07) -- (113.98,189.82) -- (111.98,188.32) -- (115.73,186.32) -- cycle ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=0.33 ] (89.58,119.27) -- (84.33,122.27) -- (86.23,123.82) -- (89.73,121.07) -- cycle ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=0.33 ] (118.47,122.6) -- (112.23,119.82) -- (113.23,122.32) -- (116.73,124.07) -- cycle ;
    		\\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (81.74,142.06) .. controls (81.6,141.51) and (82.39,140.84) .. (83.51,140.55) .. controls (84.63,140.27) and (85.65,140.48) .. (85.79,141.03) .. controls (85.93,141.58) and (85.13,142.25) .. (84.01,142.54) .. controls (82.9,142.82) and (81.88,142.61) .. (81.74,142.06) -- cycle ;
    		\\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (116.62,141.14) .. controls (116.82,140.61) and (117.85,140.5) .. (118.94,140.89) .. controls (120.02,141.29) and (120.74,142.04) .. (120.55,142.57) .. controls (120.35,143.1) and (119.32,143.21) .. (118.23,142.82) .. controls (117.15,142.42) and (116.43,141.67) .. (116.62,141.14) -- cycle ;
    		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.19 ]   (91.23,189.07) .. controls (94.23,189.57) and (105.98,191.07) .. (113.23,187.82) ;
    		\\draw  [color={rgb, 255:red, 245; green, 166; blue, 35 }  ,draw opacity=0.36 ][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=0.25 ][line width=0.75]  (86.4,119) -- (118.53,55.07) -- (54.27,55.07) -- cycle ;
    		\\draw  [color={rgb, 255:red, 245; green, 166; blue, 35 }  ,draw opacity=0.36 ][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=0.25 ][line width=0.75]  (115.87,119) -- (146.27,55.07) -- (85.47,55.07) -- cycle ;
    		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.56 ][fill={rgb, 255:red, 234; green, 238; blue, 244 }  ,fill opacity=1 ] (271,122.6) .. controls (274.65,116.15) and (303.9,116.4) .. (305.13,123.93) .. controls (305.8,144.93) and (305.13,160.93) .. (305.13,185.27) .. controls (303.8,193.27) and (276.47,195.27) .. (271.8,186.6) .. controls (270.47,159.93) and (270.13,147.93) .. (271,122.6) -- cycle ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.8 ] (274.67,136.27) .. controls (280.8,133.93) and (292.8,132.93) .. (301.8,136.6) .. controls (299.8,140.6) and (299.47,141.93) .. (297.8,145.6) .. controls (292.47,144.6) and (285.13,144.27) .. (277.8,145.27) .. controls (276.8,141.93) and (275.9,140.4) .. (274.67,136.27) -- cycle ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.8 ] (273.65,140.4) .. controls (277.9,147.4) and (278.4,172.4) .. (275.4,177.9) .. controls (274.4,174.57) and (272.4,145.4) .. (273.65,140.4) -- cycle ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.8 ] (301.8,140.82) .. controls (297.16,148.11) and (297.5,173.37) .. (301.4,178.65) .. controls (302.39,175.25) and (303.59,145.72) .. (301.8,140.82) -- cycle ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.8 ] (275.9,182.4) .. controls (282.03,184.81) and (291.4,186.44) .. (300.4,182.65) .. controls (298.9,178.4) and (299.47,176.64) .. (297.8,172.85) .. controls (292.47,173.88) and (285.23,174.43) .. (277.9,173.4) .. controls (276.9,176.84) and (277.13,178.13) .. (275.9,182.4) -- cycle ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.8 ] (278.4,147.4) .. controls (280.9,155.4) and (279.9,165.4) .. (278.9,171.4) .. controls (277.9,168.07) and (279.9,162.4) .. (278.4,147.4) -- cycle ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.8 ] (297.9,147.15) .. controls (295.11,155.15) and (296.23,165.15) .. (297.34,171.15) .. controls (298.46,167.82) and (296.23,162.15) .. (297.9,147.15) -- cycle ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.8 ] (274.4,123.4) .. controls (276.9,129.9) and (275.65,131.4) .. (274.67,136.27) .. controls (273.67,132.93) and (275.9,138.4) .. (274.4,123.4) -- cycle ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.8 ] (302.03,123.73) .. controls (299.84,130.23) and (300.94,131.73) .. (301.8,136.6) .. controls (302.68,133.27) and (300.72,138.73) .. (302.03,123.73) -- cycle ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.2 ] (271,122.6) .. controls (272.03,122.44) and (273.19,122.29) .. (273.4,125.9) .. controls (272.15,128.4) and (272.68,140.79) .. (272.15,145.15) .. controls (271.59,149.68) and (271.38,146.84) .. (270.4,148.65) .. controls (270.65,133.9) and (269.75,127.6) .. (271,122.6) -- cycle ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.2 ] (271.15,169.65) .. controls (272.18,169.49) and (274.94,169.79) .. (275.15,173.4) .. controls (273.9,175.9) and (276.43,182.04) .. (275.9,186.4) .. controls (275.34,190.93) and (272.78,184.79) .. (271.8,186.6) .. controls (272.05,171.85) and (269.9,174.65) .. (271.15,169.65) -- cycle ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.2 ] (276.25,119.6) .. controls (280.4,117.4) and (303.69,118.29) .. (303.9,121.9) .. controls (302.9,122.4) and (301.4,120.65) .. (302.03,122.73) .. controls (298.4,120.15) and (278.4,117.65) .. (274.4,122.4) .. controls (273.4,117.4) and (275,124.6) .. (276.25,119.6) -- cycle ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.2 ] (302.65,121.15) -- (305.13,123.93) -- (304.9,143.15) -- (301.8,140.82) -- (303.4,125.4) -- cycle ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.2 ] (302.65,171.65) -- (304.4,168.4) -- (304.4,186.4) -- (299.9,188.15) -- (301.65,175.4) -- cycle ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.2 ] (298.65,188.65) -- (300.65,190.15) -- (287.4,192.4) -- (275.9,189.9) -- (276.9,188.4) -- (286.9,190.4) -- cycle ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.2 ] (277.9,120.15) -- (275.65,132.4) -- (274.4,123.4) -- cycle ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.2 ] (302.03,122.73) -- (300.9,132.4) -- (298.9,121.15) -- cycle ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (277.9,189.4) -- (275.9,189.9) -- (271.8,186.6) -- (271.9,184.65) -- cycle ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (304.4,186.4) -- (300.65,190.15) -- (298.65,188.65) -- (302.4,186.65) -- cycle ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=0.33 ] (276.25,119.6) -- (271,122.6) -- (272.9,124.15) -- (276.4,121.4) -- cycle ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=0.33 ] (305.13,122.93) -- (298.9,120.15) -- (299.9,122.65) -- (303.4,124.4) -- cycle ;
    		\\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (268.4,142.39) .. controls (268.26,141.84) and (269.06,141.17) .. (270.18,140.88) .. controls (271.3,140.6) and (272.32,140.81) .. (272.45,141.36) .. controls (272.59,141.91) and (271.8,142.58) .. (270.68,142.87) .. controls (269.56,143.15) and (268.54,142.94) .. (268.4,142.39) -- cycle ;
    		\\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (303.29,141.47) .. controls (303.48,140.94) and (304.52,140.83) .. (305.6,141.23) .. controls (306.69,141.62) and (307.41,142.37) .. (307.22,142.91) .. controls (307.02,143.44) and (305.98,143.55) .. (304.9,143.15) .. controls (303.82,142.75) and (303.09,142) .. (303.29,141.47) -- cycle ;
    		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.19 ]   (277.9,189.4) .. controls (280.9,189.9) and (292.65,191.4) .. (299.9,188.15) ;
    		\\draw  [color={rgb, 255:red, 245; green, 166; blue, 35 }  ,draw opacity=0.36 ][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=0.25 ][line width=0.75]  (305.03,119.33) -- (322.27,55.4) -- (287.8,55.4) -- cycle ;
    		\\draw  [color={rgb, 255:red, 245; green, 166; blue, 35 }  ,draw opacity=0.36 ][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=0.25 ][line width=0.75]  (270.7,119.33) -- (287.8,55.4) -- (253.6,55.4) -- cycle ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 174; blue, 196 }  ,fill opacity=1 ] (24.67,51.07) -- (179.07,51.07) -- (179.07,57.73) -- (24.67,57.73) -- cycle ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 174; blue, 196 }  ,fill opacity=1 ] (210.6,51.73) -- (365,51.73) -- (365,58.4) -- (210.6,58.4) -- cycle ;
    		\\draw (44.67,33) node [anchor=north west][inner sep=0.75pt]  [font=\\footnotesize]  {$A$};
    		\\draw (80,34.33) node [anchor=north west][inner sep=0.75pt]  [font=\\footnotesize]  {$B$};
    		\\draw (111.33,32.67) node [anchor=north west][inner sep=0.75pt]  [font=\\footnotesize]  {$C$};
    		\\draw (140.67,32.67) node [anchor=north west][inner sep=0.75pt]  [font=\\footnotesize]  {$D$};
    		\\draw (245.33,34.33) node [anchor=north west][inner sep=0.75pt]  [font=\\footnotesize]  {$K$};
    		\\draw (282,33.67) node [anchor=north west][inner sep=0.75pt]  [font=\\footnotesize]  {$L$};
    		\\draw (314.67,33.67) node [anchor=north west][inner sep=0.75pt]  [font=\\footnotesize]  {$M$};
    		\\draw (97,95) node [anchor=north west][inner sep=0.75pt]  [font=\\scriptsize]  {$\\alpha $};
    		\\draw (283,69) node [anchor=north west][inner sep=0.75pt]  [font=\\scriptsize]  {$\\theta $};
    		\\draw (83.33,209.67) node [anchor=north west][inner sep=0.75pt]  [font=\\scriptsize] [align=left] {Hình 1};
    		\\draw (270.67,209.67) node [anchor=north west][inner sep=0.75pt]  [font=\\scriptsize] [align=left] {Hình 2};
    	\\end{tikzpicture}
    \\end{center}''')

    # Câu hỏi
    noidungcauhoi = ('''Một ô tô giữ nguyên khoảng cách đến bức tường.''' + tikz_code + '''
    Ở Hình 1, xe bật đèn chiếu gần; ở Hình 2, xe bật đèn chiếu xa. Khi chuyển sang đèn chiếu xa, độ rộng vùng được chiếu sáng trên tường giảm đi $%s$. Biết $AB = BC = CD = %s$. Trong mỗi hình, hai chùm sáng tạo thành hai tam giác cân bằng nhau. Do các tia sáng giao nhau, xuất hiện các góc nhọn $\\alpha$ và $\\theta$. Biết $\\tan(\\alpha - \\theta) = %s$. Hỏi khoảng cách từ đèn xe đến bức tường bằng bao nhiêu?'''
                     % (latex(k_val).replace('.', ','), latex(a), latex(T_val).replace('.', ',')))

    # Các đáp án
    da_d = ('\\True $%s$' % latex(da))
    da_s1 = ('$%s$' % latex(das1))
    da_s2 = ('$%s$' % latex(das2))
    da_s3 = ('$%s$' % latex(das3))

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_1 = [da_d, da_s1, da_s2, da_s3]
    random.shuffle(list_1)

    # Nội dung lời giải
    loigiai = ('''Gọi $P, Q$ lần lượt là vị trí đèn bên trái và đèn bên phải của xe; $h > 0$ là khoảng cách từ đèn xe đến bức tường.\\\\
    Ở Hình 1, hai tam giác cân có đỉnh $P, Q$ và đáy tương ứng là $AC, BD$. Vì $AB = BC = CD = %s$ nên $B$ là trung điểm của $AC$, còn $C$ là trung điểm của $BD$. Do đó $PB$ và $QC$ cùng vuông góc với bức tường, đồng thời $PB = QC = h$. Suy ra tứ giác $BCQP$ là hình chữ nhật và $PQ = BC = %s$.\\\\
    Gọi $I$ là giao điểm của hai tia $PC$ và $QB$, $H$ là trung điểm của $PQ$. Hai đường chéo của hình chữ nhật $BCQP$ cắt nhau tại trung điểm mỗi đường nên $IH = \\frac{h}{2}$. Tam giác $PIQ$ cân tại $I$, vì vậy $IH$ đồng thời là đường phân giác của góc $\\alpha$. Trong tam giác vuông $IHP$, ta có $\\tan \\frac{\\alpha}{2} = \\frac{PH}{IH} = \\frac{%s/2}{h/2} = \\frac{%s}{h}$.\\\\
    Ở Hình 2, độ rộng vùng chiếu sáng ban đầu là $AD = 3 \\cdot %s = %s$. Khi chuyển sang đèn chiếu xa, độ rộng giảm đi $%s$, nên độ rộng vùng chiếu sáng lúc này là $W' = %s \\cdot (1 - %s) = %s$.\\\\
    Tương tự như trên, gọi $I'$ là giao điểm của các tia sáng bên trong. Bằng lập luận tương tự, ta có $\\tan \\frac{\\theta}{2} = \\frac{W'/2 - %s/2}{h} = \\frac{%s}{h}$.\\\\
    Ta có $\\tan \\frac{\\alpha - \\theta}{2} = \\frac{\\tan \\frac{\\alpha}{2} - \\tan \\frac{\\theta}{2}}{1 + \\tan \\frac{\\alpha}{2} \\tan \\frac{\\theta}{2}} = \\frac{\\frac{%s}{h} - \\frac{%s}{h}}{1 + \\frac{%s}{h} \\cdot \\frac{%s}{h}} = \\frac{%s h}{h^2 + %s}$.\\\\
    Suy ra $\\tan(\\alpha - \\theta) = \\frac{2 \\tan \\frac{\\alpha - \\theta}{2}}{1 - \\tan^2 \\frac{\\alpha - \\theta}{2}} = \\frac{2 \\cdot \\frac{%s h}{h^2 + %s}}{1 - \\left(\\frac{%s h}{h^2 + %s}\\right)^2} = \\frac{%s h (h^2 + %s)}{(h^2 + %s)^2 - %s h^2}$.\\\\
    Theo giả thiết $\\tan(\\alpha - \\theta) = %s$, ta có phương trình:\\\\
    $$\\frac{%s h (h^2 + %s)}{(h^2 + %s)^2 - %s h^2} = %s$$\\\\
    Giải phương trình trên ta thu được nghiệm thỏa mãn là $h = %s$. Vậy khoảng cách từ đèn xe đến bức tường là $%s$.'''
               % (latex(a), latex(a), latex(a), latex(a),
                  latex(a), latex(W1), latex(k_val), latex(W1), latex(k_val), latex(W2),
                  latex(a), latex(b),
                  latex(a), latex(b), latex(a), latex(b), latex(c), latex(d),
                  latex(c), latex(d), latex(c), latex(d), latex(2*c), latex(d), latex(d), latex(c**2),
                  latex(T_val), latex(2*c), latex(d), latex(d), latex(c**2), latex(T_val), latex(h_val), latex(h_val)))
    dapan='\\shortans[0]{$%s$}\n'%(latex(h_val))
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
               '\\loigiai{'+str(loigiai)+'}\n'
               '\\end{ex}\n\\end{minipage} \n\n')
    return content


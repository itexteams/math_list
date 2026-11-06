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


def bt_dang33_p2_b2_c3_ds12(self):
    # Khai báo các bộ số liệu để random
    configs = [
        {'v1': 45, 'v0_str': '12,5', 'v0_val': 12.5, 't1': 4, 't2': 10, 'D': 250, 'a_str': '1,5', 'a_val': 1.5, 'S1': 50, 'S_accel': 200, 'v0_t2': 125, 'vf_ms': '27,5', 'vf_kmh': 99, 'vmin': 60, 'vmax': 100},
        {'v1': 36, 'v0_str': '10', 'v0_val': 10.0, 't1': 4, 't2': 10, 'D': 200, 'a_str': '1,2', 'a_val': 1.2, 'S1': 40, 'S_accel': 160, 'v0_t2': 100, 'vf_ms': '22', 'vf_kmh': 79, 'vmin': 60, 'vmax': 100},
        {'v1': 54, 'v0_str': '15', 'v0_val': 15.0, 't1': 4, 't2': 10, 'D': 260, 'a_str': '1', 'a_val': 1.0, 'S1': 60, 'S_accel': 200, 'v0_t2': 150, 'vf_ms': '25', 'vf_kmh': 90, 'vmin': 60, 'vmax': 100}
    ]

    # Chọn ngẫu nhiên một bộ số liệu
    cf = random.choice(configs)

    v1 = cf['v1']
    v0_str = cf['v0_str']
    t1 = cf['t1']
    t2 = cf['t2']
    D = cf['D']
    a_str = cf['a_str']
    S1 = cf['S1']
    S_accel = cf['S_accel']
    v0_t2 = cf['v0_t2']
    vf_ms = cf['vf_ms']
    vf_kmh = cf['vf_kmh']
    vmin = cf['vmin']
    vmax = cf['vmax']

    # Lựa chọn sai cho Nhận biết (đổi v0_str)
    v0_str_sai = '10' if v0_str != '10' else '12,5'

    # Nội dung câu hỏi
    noidungcauhoi = ('''Một người đi ô tô từ đường dẫn muốn nhập vào đường cao tốc theo lối vào cao tốc. Ban đầu người đó đi với vận tốc $%s km/h$ thì quan sát thấy biển báo nhập làn cách xe của anh ta $%s m$. Sau $%s$ giây từ khi quan sát thấy biển báo anh ta bắt đầu tăng tốc xe để đạt được vận tốc yêu cầu khi nhập làn tối thiểu là $%s km/h$. Biết rằng xe tăng tốc nhanh dần đều với vận tốc biểu diễn theo thời gian $t$ (giây) là một hàm số bậc nhất và xe người đó nhập làn cao tốc sau khi tăng tốc được $%s$ giây.
                     \\begin{center}
                     	\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1.3,xscale=1.3]
                     		\\tikzset {_wwixfy0nw/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{-90 }  \\pgftransformscale{2 }  }}}
                     		\\pgfdeclarehorizontalshading{_euhpl5yiw}{150bp}{rgb(0bp)=(0.6,0.85,1);
                     			rgb(37.5bp)=(0.6,0.85,1);
                     			rgb(62.5bp)=(1,1,1);
                     			rgb(100bp)=(1,1,1)}
                     		\\tikzset{every picture/.style={line width=0.75pt}}  
                     		\\draw  [draw opacity=0][shading=_euhpl5yiw,_wwixfy0nw] (44.67,19) -- (327.2,19) -- (327.2,165.47) -- (44.67,165.47) -- cycle ;
                     		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.6 ] (75.93,113.29) .. controls (78.52,113.29) and (80.62,115.39) .. (80.62,117.98) .. controls (80.62,120.57) and (78.52,122.67) .. (75.93,122.67) -- (60.02,122.67) .. controls (57.43,122.67) and (55.33,120.57) .. (55.33,117.98) .. controls (55.33,115.39) and (57.43,113.29) .. (60.02,113.29) .. controls (60.02,110.7) and (62.12,108.6) .. (64.71,108.6) -- (67.81,108.6) .. controls (70.4,108.6) and (72.49,110.7) .. (72.49,113.29) -- (75.93,113.29) -- cycle ;
                     		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.6 ] (145.97,109.07) .. controls (148.86,109.07) and (151.2,111.07) .. (151.2,113.53) .. controls (151.2,116) and (148.86,118) .. (145.97,118) -- (128.24,118) .. controls (125.35,118) and (123.01,116) .. (123.01,113.53) .. controls (123.01,111.07) and (125.35,109.07) .. (128.24,109.07) .. controls (128.24,106.6) and (130.58,104.6) .. (133.47,104.6) -- (136.91,104.6) .. controls (139.8,104.6) and (142.14,106.6) .. (142.14,109.07) -- (145.97,109.07) -- cycle ;
                     		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.6 ] (199.24,119.42) .. controls (202.16,119.42) and (204.52,121.79) .. (204.52,124.71) .. controls (204.52,127.63) and (202.16,130) .. (199.24,130) -- (181.29,130) .. controls (178.37,130) and (176,127.63) .. (176,124.71) .. controls (176,121.79) and (178.37,119.42) .. (181.29,119.42) .. controls (181.29,116.5) and (183.66,114.13) .. (186.58,114.13) -- (190.07,114.13) .. controls (192.99,114.13) and (195.36,116.5) .. (195.36,119.42) -- (199.24,119.42) -- cycle ;
                     		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.6 ] (270.18,104.35) .. controls (273.08,104.35) and (275.44,106.71) .. (275.44,109.61) .. controls (275.44,112.51) and (273.08,114.86) .. (270.18,114.86) -- (252.35,114.86) .. controls (249.45,114.86) and (247.1,112.51) .. (247.1,109.61) .. controls (247.1,106.71) and (249.45,104.35) .. (252.35,104.35) .. controls (252.35,101.45) and (254.7,99.1) .. (257.61,99.1) -- (261.07,99.1) .. controls (263.98,99.1) and (266.33,101.45) .. (266.33,104.35) -- (270.18,104.35) -- cycle ;
                     		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.6 ] (282.05,40.99) .. controls (277.59,40.99) and (273.98,44.3) .. (273.98,48.38) .. controls (273.98,52.46) and (277.59,55.77) .. (282.05,55.77) -- (309.43,55.77) .. controls (313.89,55.77) and (317.5,52.46) .. (317.5,48.38) .. controls (317.5,44.3) and (313.89,40.99) .. (309.43,40.99) .. controls (309.43,36.91) and (305.82,33.6) .. (301.36,33.6) -- (296.03,33.6) .. controls (291.58,33.6) and (287.96,36.91) .. (287.96,40.99) -- (282.05,40.99) -- cycle ;
                     		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.6 ] (85.34,35.92) .. controls (89.53,35.92) and (92.93,39.32) .. (92.93,43.51) .. controls (92.93,47.7) and (89.53,51.1) .. (85.34,51.1) -- (59.59,51.1) .. controls (55.4,51.1) and (52,47.7) .. (52,43.51) .. controls (52,39.32) and (55.4,35.92) .. (59.59,35.92) .. controls (59.59,31.73) and (62.99,28.33) .. (67.18,28.33) -- (72.19,28.33) .. controls (76.38,28.33) and (79.78,31.73) .. (79.78,35.92) -- (85.34,35.92) -- cycle ;
                     		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.6 ] (286.74,118.09) .. controls (282.58,118.09) and (279.2,120.46) .. (279.2,123.38) .. controls (279.2,126.3) and (282.58,128.67) .. (286.74,128.67) -- (312.33,128.67) .. controls (316.49,128.67) and (319.87,126.3) .. (319.87,123.38) .. controls (319.87,120.46) and (316.49,118.09) .. (312.33,118.09) .. controls (312.33,115.17) and (308.95,112.8) .. (304.79,112.8) -- (299.81,112.8) .. controls (295.65,112.8) and (292.27,115.17) .. (292.27,118.09) -- (286.74,118.09) -- cycle ;
                     		\\draw  [draw opacity=0][fill={rgb, 255:red, 65; green, 117; blue, 5 }  ,fill opacity=1 ] (44.67,130.13) -- (329.2,130.13) -- (329.2,164.13) -- (44.67,164.13) -- cycle ;
                     		\\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (186.93,130.13) -- (329.7,156.4) -- (329.2,164.13) -- (44.67,164.13) -- (44.53,151.47) -- cycle ;
                     		\\draw  [draw opacity=0][fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (284.7,133.97) -- (286.4,133.97) -- (286.4,140.5) -- (284.7,140.5) -- cycle ;
                     		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (284.7,127.45) -- (286.4,127.45) -- (286.4,133.97) -- (284.7,133.97) -- cycle ;
                     		\\draw  [draw opacity=0][fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (284.7,120.92) -- (286.4,120.92) -- (286.4,127.45) -- (284.7,127.45) -- cycle ;
                     		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (284.7,114.4) -- (286.4,114.4) -- (286.4,120.92) -- (284.7,120.92) -- cycle ;
                     		\\draw  [draw opacity=0][fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (301.7,134.47) -- (303.4,134.47) -- (303.4,141) -- (301.7,141) -- cycle ;
                     		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (301.7,127.95) -- (303.4,127.95) -- (303.4,134.47) -- (301.7,134.47) -- cycle ;
                     		\\draw  [draw opacity=0][fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (301.7,121.42) -- (303.4,121.42) -- (303.4,127.95) -- (301.7,127.95) -- cycle ;
                     		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (301.7,114.9) -- (303.4,114.9) -- (303.4,121.42) -- (301.7,121.42) -- cycle ;
                     		\\draw  [draw opacity=0][fill={rgb, 255:red, 11; green, 103; blue, 81 }  ,fill opacity=1 ] (270.73,71) -- (317.53,71) -- (317.53,121.9) -- (270.73,121.9) -- cycle ;
                     		\\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ] (273.53,73.53) -- (315.23,73.53) -- (315.23,119.37) -- (273.53,119.37) -- cycle ;
                     		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (279.53,78.5) -- (298.73,78.5) -- (298.73,110.15) -- (279.53,110.15) -- cycle ;
                     		\\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (312.23,91.9) -- (312.23,100.4) -- (297.73,93.9) -- (297.53,84) -- cycle ;
                     		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (279.53,78.5) -- (279.53,110.15) ;
                     		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ] [dash pattern={on 4.5pt off 4.5pt}]  (289.13,78.5) -- (289.13,110.15) ;
                     		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (298.73,78.5) -- (298.73,84) ;
                     		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (298.73,84) -- (312.23,91.9) ;
                     		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (298.73,94.32) -- (299.2,108.9) ;
                     		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (298.73,93.9) -- (312.23,100.4) ;
                     		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (281.23,102.7) -- (284.73,98.23) -- (288.23,102.7) -- (286.48,102.7) -- (286.48,109.4) -- (282.98,109.4) -- (282.98,102.7) -- cycle ;
                     		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (290.23,102.7) -- (293.73,98.23) -- (297.23,102.7) -- (295.48,102.7) -- (295.48,109.4) -- (291.98,109.4) -- (291.98,102.7) -- cycle ;
                     		\\draw  [draw opacity=0][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (301.78,95.12) -- (299.63,89.96) -- (305.15,88.99) -- (304.3,90.52) -- (310.05,93.67) -- (308.37,96.74) -- (302.62,93.59) -- cycle ;
                     		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.46 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (256.72,50.67) -- (258.3,138.9) -- (255.53,138.53) -- (255.53,50.67) -- cycle ;
                     		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.46 ]   (256.01,34.27) -- (256.25,50.67) ;
                     		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.46 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (221.27,29.32) .. controls (221.42,28.26) and (222.39,27.6) .. (223.42,27.85) -- (230.83,29.61) .. controls (231.86,29.86) and (232.58,30.92) .. (232.43,31.98) -- (232.43,31.98) .. controls (232.28,33.04) and (231.32,33.69) .. (230.28,33.45) -- (222.88,31.68) .. controls (221.84,31.43) and (221.12,30.38) .. (221.27,29.32) -- cycle ;
                     		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.46 ]   (232.43,31.98) .. controls (248.11,34.89) and (253.85,38.29) .. (256.48,48.19) ;
                     		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.46 ]   (232.43,31.98) .. controls (261.27,37.06) and (268.21,42.31) .. (256.48,48.19) ;
                     		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.44 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (215.72,93.58) -- (216.41,132.4) -- (215.19,132.24) -- (215.19,93.58) -- cycle ;
                     		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.44 ]   (215.4,86.37) -- (215.51,93.58) ;
                     		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.44 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (200.12,84.19) .. controls (200.19,83.72) and (200.61,83.43) .. (201.07,83.54) -- (204.32,84.32) .. controls (204.78,84.43) and (205.09,84.89) .. (205.03,85.36) -- (205.03,85.36) .. controls (204.96,85.82) and (204.54,86.11) .. (204.08,86.01) -- (200.82,85.23) .. controls (200.37,85.12) and (200.05,84.65) .. (200.12,84.19) -- cycle ;
                     		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.44 ]   (205.03,85.36) .. controls (211.93,86.64) and (214.45,88.14) .. (215.61,92.49) ;
                     		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.44 ]   (205.03,85.36) .. controls (217.72,87.59) and (220.77,89.91) .. (215.61,92.49) ;
                     		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.45 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (93.26,94.08) -- (92.73,132.9) -- (93.67,132.74) -- (93.67,94.08) -- cycle ;
                     		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.45 ]   (93.51,86.87) -- (93.43,94.08) ;
                     		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.45 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (105.31,84.69) .. controls (105.26,84.22) and (104.86,83.96) .. (104.42,84.09) -- (102.22,84.77) .. controls (101.78,84.91) and (101.47,85.39) .. (101.52,85.86) -- (101.52,85.86) .. controls (101.57,86.32) and (101.97,86.59) .. (102.41,86.46) -- (104.6,85.78) .. controls (105.04,85.64) and (105.36,85.15) .. (105.31,84.69) -- cycle ;
                     		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.45 ]   (101.52,85.86) .. controls (96.19,87.14) and (94.24,88.64) .. (93.34,92.99) ;
                     		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.45 ]   (101.52,85.86) .. controls (91.72,88.09) and (89.36,90.41) .. (93.34,92.99) ;
                     		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.52 ][fill={rgb, 255:red, 205; green, 202; blue, 202 }  ,fill opacity=1 ] (328.9,152.4) -- (186.93,130.13) -- (328.65,145.12) -- cycle ;
                     		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.52 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (44.53,151.47) -- (186.93,130.13) -- (44.67,147.13) -- cycle ;
                     		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.38 ][fill={rgb, 255:red, 198; green, 195; blue, 195 }  ,fill opacity=1 ] (44.67,147.13) -- (186.93,130.13) -- (44.4,135.4) -- cycle ;
                     		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.38 ][fill={rgb, 255:red, 175; green, 225; blue, 213 }  ,fill opacity=1 ] (44.9,138.9) -- (186.93,130.13) -- (44.67,130.13) -- cycle ;
                     		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.24 ]   (186.93,130.13) -- (44.4,134.4) ;
                     		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.24 ]   (186.93,130.13) -- (44.4,132.4) ;
                     		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.24 ]   (186.93,130.13) -- (44.4,136.4) ;
                     		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (201.4,132.4) -- (329.2,164.13) -- (318.9,164.4) -- cycle ;
                     		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (198.4,133.4) -- (204.9,164.9) -- (192.9,163.4) -- cycle ;
                     		\\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (187.5,150.4) -- (210.4,150.4) -- (210.4,157) -- (187.5,157) -- cycle ;
                     		\\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (186.93,140.53) -- (209.83,140.53) -- (209.83,144.9) -- (186.93,144.9) -- cycle ;
                     		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ] [dash pattern={on 4.5pt off 4.5pt}]  (46.4,159.4) .. controls (91.4,152.4) and (167.4,134.4) .. (186.93,130.13) ;
                     		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (154.62,148.18) -- (158.96,152.19) -- (152.64,151.77) -- (140.25,157.2) -- (131.76,156.78) -- (145.54,150.93) -- (141.58,149.85) -- cycle ;
                     		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (57.76,152) -- (54.56,155.6) -- (45.2,154.84) -- cycle ;
                     		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (243.92,149.6) -- (258.72,159.04) -- (249.92,159.6) -- (239.12,152) -- (219.92,150.4) -- (219.12,147.6) -- cycle ;
                     		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (219.12,146.6) -- (222.72,151.56) -- (213.12,149.16) -- cycle ;
                     		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.46 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (145.04,118.8) -- (145.84,118.8) -- (145.84,129.2) -- (145.04,129.2) -- cycle ;
                     		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.46 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (145.04,117.6) -- (204.64,117.6) -- (204.64,118.8) -- (145.04,118.8) -- cycle ;
                     		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.46 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (203.44,118.2) -- (204.64,118.2) -- (204.64,132) -- (203.44,132) -- cycle ;
                     		\\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 177; green, 171; blue, 171 }  ,fill opacity=1 ] (149.84,113.2) -- (174.84,113.2) -- (174.84,123.19) -- (149.84,123.19) -- cycle ;
                     		\\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 11; green, 103; blue, 81 }  ,fill opacity=1 ] (180.79,113.13) -- (199.34,113.13) -- (199.34,123.12) -- (180.79,123.12) -- cycle ;
                     		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ] [dash pattern={on 0.84pt off 2.51pt}]  (152.64,116.3) -- (172.64,116.3)(152.64,119.3) -- (172.64,119.3) ;
                     		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ] [dash pattern={on 0.84pt off 2.51pt}]  (184.64,116.1) -- (196.24,116.1)(184.64,119.1) -- (196.24,119.1) ;
                     		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.47 ] (58.58,96) -- (60.18,130) -- (53.78,130) -- (56.25,96.15) -- cycle ;
                     		\\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ]   (54.98,102) -- (64.18,102.4) ;
                     		\\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ]   (58.58,104.8) -- (61.8,103.42) -- (64.18,102.4) ;
                     		\\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ]   (51.5,111.9) -- (65,112.4) ;
                     		\\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ]   (55.83,115.4) -- (65,112.4) ;
                     		\\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ]   (54.98,102) -- (58.58,96) ;
                     		\\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ]   (54.58,105.6) -- (58.58,102.4) ;
                     		\\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ]   (54.98,110.8) -- (58.98,107.6) ;
                     		\\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ]   (54.58,118.4) -- (59.38,115.2) ;
                     		\\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ]   (53.78,130) -- (60.58,124.8) ;
                     		\\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ]   (59.78,120) -- (54.58,123.2) ;
                     		\\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ]   (58.58,102.4) -- (56.25,96.15) ;
                     		\\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ]   (58.18,112) -- (54.58,105.6) ;
                     		\\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ]   (59.78,120) -- (54.38,113) ;
                     		\\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ]   (58.18,129.6) -- (54.58,123.2) ;
                     		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.47 ] (108.1,113.4) -- (108.86,129.5) -- (105.83,129.5) -- (107,113.47) -- cycle ;
                     		\\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ]   (106.4,116.24) -- (110.75,116.43) ;
                     		\\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ]   (108.1,117.57) -- (109.63,116.91) -- (110.75,116.43) ;
                     		\\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ]   (104.75,120.93) -- (111.14,121.17) ;
                     		\\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ]   (106.8,122.59) -- (111.14,121.17) ;
                     		\\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ]   (106.4,116.24) -- (108.1,113.4) ;
                     		\\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ]   (106.21,117.95) -- (108.1,116.43) ;
                     		\\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ]   (106.4,120.41) -- (108.29,118.89) ;
                     		\\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ]   (106.21,124.01) -- (108.48,122.49) ;
                     		\\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ]   (105.83,129.5) -- (109.05,127.04) ;
                     		\\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ]   (108.67,124.76) -- (106.21,126.28) ;
                     		\\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ]   (108.1,116.43) -- (107,113.47) ;
                     		\\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ]   (107.91,120.98) -- (106.21,117.95) ;
                     		\\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ]   (108.67,124.76) -- (106.11,121.45) ;
                     		\\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ]   (107.91,129.31) -- (106.21,126.28) ;
                     		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ]   (58.5,100.75) .. controls (70.25,112.4) and (86.5,118.4) .. (108.1,116.43) ;
                     		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ]   (55,103.75) .. controls (66.75,115.4) and (88.02,118.88) .. (109.63,116.91) ;
                     		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ]   (108.1,116.43) .. controls (119.85,128.08) and (123.9,128.87) .. (145.5,126.9) ;
                     		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ]   (106.21,117.95) .. controls (117.96,129.6) and (123.9,128.87) .. (145.5,126.9) ;
                     		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.6 ] (234.42,114.11) .. controls (236.29,114.11) and (237.8,115.62) .. (237.8,117.49) .. controls (237.8,119.35) and (236.29,120.86) .. (234.42,120.86) -- (222.97,120.86) .. controls (221.11,120.86) and (219.6,119.35) .. (219.6,117.49) .. controls (219.6,115.62) and (221.11,114.11) .. (222.97,114.11) .. controls (222.97,112.25) and (224.48,110.74) .. (226.35,110.74) -- (228.57,110.74) .. controls (230.44,110.74) and (231.95,112.25) .. (231.95,114.11) -- (234.42,114.11) -- cycle ;
                     		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.87 ] (94,47.99) .. controls (97.2,47.99) and (99.8,50.59) .. (99.8,53.8) .. controls (99.8,57) and (97.2,59.6) .. (94,59.6) -- (74.3,59.6) .. controls (71.1,59.6) and (68.5,57) .. (68.5,53.8) .. controls (68.5,50.59) and (71.1,47.99) .. (74.3,47.99) .. controls (74.3,44.79) and (76.9,42.19) .. (80.11,42.19) -- (83.94,42.19) .. controls (87.14,42.19) and (89.74,44.79) .. (89.74,47.99) -- (94,47.99) -- cycle ;
                     		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.15 ] (181.03,128.6) -- (44.67,164.13) -- (44.53,151.47) -- cycle ;
                     		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.08 ] (198.4,133.4) -- (219.1,165) -- (163.4,165.4) -- (195.6,132.5) -- cycle ;
                     	\\end{tikzpicture}
                     \\end{center}'''                
                     %(v1, D, t1, vmin, t2))

    ########################################################################
    # Nhận biết ############################################
    # Các đáp án
    nb_da_1_d = '\\True Hàm số vận tốc $v(t)$ được biểu thị theo thời gian của xe trong suốt quá trình tăng tốc là $v(t) = at + %s$ ($m/s$)' % (v0_str)
    nb_da_1_s = 'Hàm số vận tốc $v(t)$ được biểu thị theo thời gian của xe trong suốt quá trình tăng tốc là $v(t) = at + %s$ ($m/s$)' % (v0_str_sai)
    list_nb_da_1=[nb_da_1_d,nb_da_1_s]
    nb_da_1=random.choice(list_nb_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]

    # Nội dung lời giải
    loigiai_nb_1 = ('''Đổi $%s km/h = %s m/s$. \\\\
    Vì xe tăng tốc nhanh dần đều nên vận tốc là hàm số bậc nhất của thời gian: $v(t) = at + v_0$, trong đó $v_0 = %s m/s$ là vận tốc ban đầu khi bắt đầu tăng tốc. \\\\
    Vậy $v(t) = at + %s$ ($m/s$).'''
                %(v1, v0_str, v0_str, v0_str))

    # Đưa các lời giải vào danh sách lời giải
    list_nb_2 = [loigiai_nb_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_nb = list(zip(list_nb_1, list_nb_2))

    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_nb)

    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

    ########################################################################
    # Thông hiểu ############################################
    # Các đáp án
    th_da_1_d = '\\True Quãng đường xe đi được trong khoảng thời gian $0 \\le t \\le %s$ tính theo công thức: $S = \\int_0^{%s} v(t) \\text{d}t$' % (t2, t2)
    th_da_1_s = 'Quãng đường xe đi được trong khoảng thời gian $0 \\le t \\le %s$ tính theo công thức: $S = \\int_0^{%s} v\'(t) \\text{d}t$' % (t2, t2)
    list_th_da_1=[th_da_1_d,th_da_1_s]
    th_da_1=random.choice(list_th_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]

    # Nội dung lời giải
    loigiai_th_1 = ('''Quãng đường vật đi được trong khoảng thời gian từ $t_1$ đến $t_2$ được tính bằng tích phân của hàm vận tốc: $S = \\int_{t_1}^{t_2} v(t) \\text{d}t$. \\\\
    Áp dụng cho khoảng thời gian từ $0$ đến $%s$ giây, ta có: $S = \\int_0^{%s} v(t) \\text{d}t$.'''       
               %(t2, t2))

    # Đưa các lời giải vào danh sách lời giải
    list_th_2 = [loigiai_th_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_th = list(zip(list_th_1, list_th_2))

    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_th)

    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

    ######################################################################## 
    # Vận dụng ############################################
    # Các đáp án
    vd_da_1_d = '\\True Quãng đường từ khi tăng tốc đến khi nhập làn là $%sm$' % (S_accel)  
    vd_da_1_s = 'Quãng đường từ khi tăng tốc đến khi nhập làn là $%sm$' % (D)  
    list_vd_da_1=[vd_da_1_d,vd_da_1_s]
    vd_da_1=random.choice(list_vd_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]

    # Nội dung lời giải
    loigiai_vd_1 = ('''Quãng đường xe đi được trong $%s$ giây đầu (trước khi tăng tốc) là: $S_1 = %s \\cdot %s = %s m$. \\\\
    Quãng đường từ khi xe bắt đầu tăng tốc đến khi nhập làn là phần quãng đường còn lại: $S_2 = %s - %s = %s m$.'''  
               %(t1, v0_str, t1, S1, D, S1, S_accel))

    # Đưa các lời giải vào danh sách lời giải
    list_vd_2 = [loigiai_vd_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_vd = list(zip(list_vd_1, list_vd_2))

    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_vd)

    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

    ######################################################################## 
    # Vận dụng cao ############################################
    # Các đáp án
    vdc_da_1_d = '\\True Tốc độ bắt buộc trên cao tốc từ $%skm/h$ đến $%skm/h$ như vậy người lái xe không vi phạm tốc độ quy định khi nhập làn' % (vmin, vmax) 
    vdc_da_1_s = 'Tốc độ bắt buộc trên cao tốc từ $%skm/h$ đến $%skm/h$ như vậy người lái xe đã vi phạm tốc độ quy định khi nhập làn' % (vmin, vmax) 
    list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
    vdc_da_1=random.choice(list_vdc_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]

    # Nội dung lời giải
    loigiai_vdc_1 = ('''Ta có quãng đường khi tăng tốc: $S_2 = \\int_0^{%s} (at + %s) \\text{d}t = \\left( \\frac{at^2}{2} + %st \\right) \\Big|_0^{%s} = 50a + %s$. \\\\
    Mà $S_2 = %s \\Rightarrow 50a + %s = %s \\Rightarrow 50a = %s \\Rightarrow a = %s m/s^2$. \\\\
    Vận tốc của xe khi nhập làn (tại $t = %s$) là: $v(%s) = %s \\cdot %s + %s = %s m/s = %s km/h$. \\\\
    Vì $%s \\le %s \\le %s$ nên người lái xe không vi phạm tốc độ quy định khi nhập làn.'''
               %(t2, v0_str, v0_str, t2, v0_t2, S_accel, v0_t2, S_accel, S_accel - v0_t2, a_str, t2, t2, a_str, t2, v0_str, vf_ms, vf_kmh, vmin, vf_kmh, vmax))

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
    str(noidungcauhoi)+ 
        '\n\\choiceTFn \n'
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
        '\\end{ex}\n \\end{minipage}\n\n')
    return content


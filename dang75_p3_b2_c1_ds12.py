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


def bt_dang75_p3_b2_c1_ds12(self):
    # Khai báo biến và tạo bài toán ngẫu nhiên
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        t = symbols('t')

        t0 = randint(4, 7)       # Thời điểm đạt độ cao cực đại
        t1 = randint(1, 3)       # Nghiệm âm
        if (t0 - t1) % 2 != 0:
            t1 += 1

        k = t0 - t1              # Hệ số của t trong h'(t)
        b_val = Rational(k, 2)   # Hệ số của t^2 trong h(t)
        c_val = t0 * t1          # Hệ số tự do của h'(t) và hệ số của t trong h(t)

        # Hàm độ cao h(t)
        h = -Rational(1, 3) * t**3 + b_val * t**2 + c_val * t
        # Đạo hàm cấp 1: vận tốc v(t) = h'(t)
        dh1 = -t**2 + k * t + c_val

        # Thời gian kết thúc khảo sát t_end > t0
        t_end = t0 + randint(1, 2)

        # Tính giá trị tại các mốc
        h_0 = 0
        h_max = h.subs(t, t0)
        h_end = h.subs(t, t_end)

        # Xử lý làm tròn độ cao cực đại (h_max) thành số thập phân có dấu phẩy nếu lẻ
        number = Decimal(str(float(h_max)))
        kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)
        kq_str = str(kq).replace('.', ',')

        # Định dạng chuỗi hiển thị số
        h_max_latex = latex(h_max)
        h_end_latex = latex(h_end)
        hinhve='''\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-0.8,xscale=0.8]
        	\\tikzset {_wxnryw785/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{0 }  \\pgftransformscale{2 }  }}}
        	\\pgfdeclarehorizontalshading{_eucr6cs1h}{150bp}{rgb(0bp)=(0.22,0.35,0.49);
        		rgb(37.5bp)=(0.22,0.35,0.49);
        		rgb(62.5bp)=(0,0,0);
        		rgb(100bp)=(0,0,0)}
        	\\tikzset{every picture/.style={line width=0.75pt}} 
        	\\draw  [draw opacity=0][shading=_eucr6cs1h,_wxnryw785] (111.87,15.47) -- (358.53,15.47) -- (358.53,252.4) -- (111.87,252.4) -- cycle ;
        	\\draw  [draw opacity=0][fill={rgb, 255:red, 188; green, 213; blue, 242 }  ,fill opacity=1 ] (197.16,91.57) -- (209.56,178.14) -- (225.92,225.55) -- (166.48,222.11) -- (183.05,178.5) -- cycle ;
        	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (197.33,105.33) -- (209.73,191.9) -- (229.23,253.4) -- (120.53,252.4) -- (159.87,230.8) -- (183.21,192.26) -- cycle ;
        	\\draw  [draw opacity=0][fill={rgb, 255:red, 215; green, 190; blue, 220 }  ,fill opacity=1 ] (195.71,89.48) -- (199.31,89.57) -- (199.12,97.17) -- (195.53,97.08) -- cycle ;
        	\\draw  [draw opacity=0][fill={rgb, 255:red, 188; green, 213; blue, 242 }  ,fill opacity=1 ] (253.43,108.15) -- (267.93,194.4) -- (285.43,241.4) -- (225.93,239.4) -- (241.43,195.4) -- cycle ;
        	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (253.93,121.9) -- (268.43,208.15) -- (290.43,252.4) -- (224.93,243.9) -- (241.93,209.15) -- cycle ;
        	\\draw  [draw opacity=0][fill={rgb, 255:red, 215; green, 190; blue, 220 }  ,fill opacity=1 ] (251.93,106.1) -- (255.53,106.1) -- (255.53,113.7) -- (251.93,113.7) -- cycle ;
        	\\draw  [draw opacity=0][fill={rgb, 255:red, 188; green, 213; blue, 242 }  ,fill opacity=1 ] (288.93,108.15) -- (303.43,194.4) -- (320.93,241.4) -- (261.43,239.4) -- (276.93,195.4) -- cycle ;
        	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (289.43,121.9) -- (303.93,208.15) -- (322.53,238.13) -- (349.87,252.4) -- (258.93,252.4) -- (277.43,209.15) -- cycle ;
        	\\draw  [draw opacity=0][fill={rgb, 255:red, 215; green, 190; blue, 220 }  ,fill opacity=1 ] (287.43,106.1) -- (291.03,106.1) -- (291.03,113.7) -- (287.43,113.7) -- cycle ;
        	\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (244.93,61.4) -- (257.83,73.5) -- (229.93,66.4) -- (180.93,71.4) -- (221.93,61.9) -- cycle ;
        	\\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (233.93,102.9) .. controls (233.93,95.72) and (238.19,89.9) .. (243.43,89.9) .. controls (248.68,89.9) and (252.93,95.72) .. (252.93,102.9) .. controls (252.93,110.08) and (248.68,115.9) .. (243.43,115.9) .. controls (238.19,115.9) and (233.93,110.08) .. (233.93,102.9) -- cycle ;
        	\\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (177.93,88.4) .. controls (177.93,81.22) and (182.19,75.4) .. (187.43,75.4) .. controls (192.68,75.4) and (196.93,81.22) .. (196.93,88.4) .. controls (196.93,95.58) and (192.68,101.4) .. (187.43,101.4) .. controls (182.19,101.4) and (177.93,95.58) .. (177.93,88.4) -- cycle ;
        	\\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ][fill={rgb, 255:red, 206; green, 225; blue, 249 }  ,fill opacity=1 ] (285.93,82.4) -- (297.93,87.4) -- (295.43,95.4) -- (290.43,104.4) -- (206.93,78.4) -- (171.43,82.4) -- (170.43,76.9) -- (172.43,72.4) -- (207.43,65.9) -- (230.43,63.9) -- (247.93,59.9) -- (267.43,68.4) -- (280.93,79.9) -- cycle ;
        	\\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (171.43,82.4) -- (206.93,78.4) -- (290.43,104.4) -- (289.43,108.9) -- (206.43,83.4) -- (172.43,87.4) -- cycle ;
        	\\draw  [fill={rgb, 255:red, 104; green, 21; blue, 30 }  ,fill opacity=1 ] (206.43,83.4) -- (289.43,108.9) -- (253.93,110.9) -- (172.43,87.4) -- cycle ;
        	\\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (215.43,86.4) .. controls (215.43,79.22) and (219.69,73.4) .. (224.93,73.4) .. controls (230.18,73.4) and (234.43,79.22) .. (234.43,86.4) .. controls (234.43,93.58) and (230.18,99.4) .. (224.93,99.4) .. controls (219.69,99.4) and (215.43,93.58) .. (215.43,86.4) -- cycle ;
        	\\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (273.18,102.4) .. controls (273.18,95.22) and (277.44,89.4) .. (282.68,89.4) .. controls (287.93,89.4) and (292.18,95.22) .. (292.18,102.4) .. controls (292.18,109.58) and (287.93,115.4) .. (282.68,115.4) .. controls (277.44,115.4) and (273.18,109.58) .. (273.18,102.4) -- cycle ;
        	\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (264.93,69.9) -- (275.33,80.5) -- (247.43,73.4) -- (232.43,66.4) -- (247.43,62.9) -- cycle ;
        	\\draw  [draw opacity=0][fill={rgb, 255:red, 52; green, 89; blue, 130 }  ,fill opacity=1 ] (171.43,82.4) -- (206.93,78.4) -- (203.93,72.9) -- (170.43,76.9) -- cycle ;
        	\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (170.43,76.9) -- (203.93,72.9) ;
        	\\draw  [draw opacity=0][fill={rgb, 255:red, 65; green, 85; blue, 108 }  ,fill opacity=0.42 ] (172.43,72.4) -- (203.93,66.4) -- (227.93,63.4) -- (205.43,68.9) -- (205.43,68.9) -- cycle ;
        	\\draw  [draw opacity=0][fill={rgb, 255:red, 65; green, 85; blue, 108 }  ,fill opacity=0.42 ] (203.93,72.9) -- (220.43,74.4) -- (215.93,81.4) -- (206.93,78.4) -- cycle ;
        	\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.51 ]   (275.33,80.5) -- (277.43,85.4) ;
        	\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.31 ]   (264.93,95.4) -- (277.43,85.4) ;
        	\\draw  [draw opacity=0][fill={rgb, 255:red, 65; green, 85; blue, 108 }  ,fill opacity=0.22 ] (242.93,76.9) -- (277.43,85.4) -- (267.43,93.4) -- (238.93,85.4) -- cycle ;
        	\\draw  [draw opacity=0][fill={rgb, 255:red, 65; green, 85; blue, 108 }  ,fill opacity=0.22 ] (277.43,85.4) -- (295.43,91.4) -- (273.93,99.9) -- (264.93,95.4) -- cycle ;
        	\\draw  [draw opacity=0][fill={rgb, 255:red, 74; green, 144; blue, 226 }  ,fill opacity=0.38 ] (247.43,62.9) -- (264.93,69.9) -- (275.33,80.5) -- (247.43,73.4) -- cycle ;
        	\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.43 ]   (232.83,73.5) -- (237.93,74.9) ;
        	\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.43 ]   (265.93,82.9) -- (285.43,87.4) ;
        	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (187.43,90.9) -- (224.93,86.4) -- (224.43,89.9) -- (189.43,94.4) -- cycle ;
        	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (239.93,106.9) -- (277.93,103.4) -- (277.43,106.9) -- (241.43,110.4) -- cycle ;
        	\\draw    (193.33,85.5) -- (265.43,107.9) ;
        	\\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (235.93,95.9) -- (255.43,102.4) -- (243.43,102.9) -- (224.93,99.4) -- cycle ;
        	\\draw  [draw opacity=0][fill={rgb, 255:red, 188; green, 213; blue, 242 }  ,fill opacity=1 ] (235.93,90.65) -- (250.43,176.9) -- (267.93,223.9) -- (208.43,221.9) -- (223.93,177.9) -- cycle ;
        	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (236.43,104.4) -- (250.93,190.65) -- (278.43,252.4) -- (194.93,252.9) -- (224.43,191.65) -- cycle ;
        	\\draw  [draw opacity=0][fill={rgb, 255:red, 215; green, 190; blue, 220 }  ,fill opacity=1 ] (234.43,88.6) -- (238.03,88.6) -- (238.03,96.2) -- (234.43,96.2) -- cycle ;
        	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (111.87,252.4) .. controls (112.01,240.45) and (120.01,230.82) .. (129.87,230.82) .. controls (139.81,230.82) and (147.87,240.63) .. (147.87,252.73) .. controls (147.87,252.87) and (147.87,253.02) .. (147.86,253.16) -- cycle ;
        	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (137.2,243.51) .. controls (137.3,235.37) and (142.75,228.8) .. (149.47,228.8) .. controls (156.25,228.8) and (161.74,235.49) .. (161.74,243.73) .. controls (161.74,243.83) and (161.74,243.93) .. (161.74,244.03) -- cycle ;
        	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (322.54,251.64) .. controls (322.68,239.69) and (330.68,230.06) .. (340.54,230.06) .. controls (350.48,230.06) and (358.54,239.87) .. (358.54,251.97) .. controls (358.54,252.11) and (358.54,252.26) .. (358.53,252.4) -- cycle ;
        	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (309.21,241.19) .. controls (309.3,233.41) and (314.52,227.13) .. (320.93,227.13) .. controls (327.41,227.13) and (332.66,233.52) .. (332.66,241.4) .. controls (332.66,241.49) and (332.66,241.59) .. (332.66,241.68) -- cycle ;
        	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (190.53,229.77) .. controls (190.68,217.82) and (198.68,208.19) .. (208.53,208.19) .. controls (218.48,208.19) and (226.53,218) .. (226.53,230.09) .. controls (226.53,230.24) and (226.53,230.38) .. (226.53,230.53) -- cycle ;
        	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (250.18,230.45) .. controls (250.33,218.5) and (258.33,208.87) .. (268.18,208.87) .. controls (278.13,208.87) and (286.19,218.68) .. (286.19,230.77) .. controls (286.19,230.92) and (286.18,231.06) .. (286.18,231.21) -- cycle ;
        	\\draw  [draw opacity=0] (135.48,242.52) .. controls (135.47,242.46) and (135.47,242.39) .. (135.47,242.33) .. controls (135.47,234.7) and (141.66,228.52) .. (149.28,228.52) .. controls (156.88,228.52) and (163.04,234.65) .. (163.09,242.23) -- (149.28,242.33) -- cycle ; \\draw  [color={rgb, 255:red, 192; green, 215; blue, 242 }  ,draw opacity=1 ] (135.48,242.52) .. controls (135.47,242.46) and (135.47,242.39) .. (135.47,242.33) .. controls (135.47,234.7) and (141.66,228.52) .. (149.28,228.52) .. controls (156.88,228.52) and (163.04,234.65) .. (163.09,242.23) ;  
        	\\draw  [draw opacity=0] (163.09,242.23) .. controls (163.09,242.2) and (163.09,242.16) .. (163.09,242.13) .. controls (163.09,238.12) and (166.34,234.86) .. (170.35,234.86) .. controls (174.35,234.86) and (177.59,238.09) .. (177.62,242.08) -- (170.35,242.13) -- cycle ; \\draw  [color={rgb, 255:red, 192; green, 215; blue, 242 }  ,draw opacity=1 ] (163.09,242.23) .. controls (163.09,242.2) and (163.09,242.16) .. (163.09,242.13) .. controls (163.09,238.12) and (166.34,234.86) .. (170.35,234.86) .. controls (174.35,234.86) and (177.59,238.09) .. (177.62,242.08) ;  
        	\\draw  [draw opacity=0] (177.62,238.83) .. controls (177.62,238.78) and (177.62,238.73) .. (177.62,238.68) .. controls (177.62,232.85) and (182.34,228.12) .. (188.18,228.12) .. controls (193.98,228.12) and (198.7,232.81) .. (198.74,238.61) -- (188.18,238.68) -- cycle ; \\draw  [color={rgb, 255:red, 192; green, 215; blue, 242 }  ,draw opacity=1 ] (177.62,238.83) .. controls (177.62,238.78) and (177.62,238.73) .. (177.62,238.68) .. controls (177.62,232.85) and (182.34,228.12) .. (188.18,228.12) .. controls (193.98,228.12) and (198.7,232.81) .. (198.74,238.61) ;  
        	\\draw  [draw opacity=0] (195.41,246.5) .. controls (195.41,246.45) and (195.41,246.4) .. (195.41,246.35) .. controls (195.41,240.52) and (200.14,235.79) .. (205.97,235.79) .. controls (211.78,235.79) and (216.49,240.48) .. (216.53,246.28) -- (205.97,246.35) -- cycle ; \\draw  [color={rgb, 255:red, 192; green, 215; blue, 242 }  ,draw opacity=1 ] (195.41,246.5) .. controls (195.41,246.45) and (195.41,246.4) .. (195.41,246.35) .. controls (195.41,240.52) and (200.14,235.79) .. (205.97,235.79) .. controls (211.78,235.79) and (216.49,240.48) .. (216.53,246.28) ;  
        	\\draw  [draw opacity=0] (168.72,252.33) .. controls (168.72,252.28) and (168.72,252.23) .. (168.72,252.18) .. controls (168.72,246.35) and (173.45,241.62) .. (179.28,241.62) .. controls (185.09,241.62) and (189.8,246.31) .. (189.84,252.11) -- (179.28,252.18) -- cycle ; \\draw  [color={rgb, 255:red, 192; green, 215; blue, 242 }  ,draw opacity=1 ] (168.72,252.33) .. controls (168.72,252.28) and (168.72,252.23) .. (168.72,252.18) .. controls (168.72,246.35) and (173.45,241.62) .. (179.28,241.62) .. controls (185.09,241.62) and (189.8,246.31) .. (189.84,252.11) ;  
        	\\draw  [draw opacity=0] (124.53,252.94) .. controls (124.53,252.89) and (124.53,252.84) .. (124.53,252.79) .. controls (124.53,246.96) and (129.26,242.23) .. (135.09,242.23) .. controls (140.9,242.23) and (145.61,246.92) .. (145.65,252.72) -- (135.09,252.79) -- cycle ; \\draw  [color={rgb, 255:red, 192; green, 215; blue, 242 }  ,draw opacity=1 ] (124.53,252.94) .. controls (124.53,252.89) and (124.53,252.84) .. (124.53,252.79) .. controls (124.53,246.96) and (129.26,242.23) .. (135.09,242.23) .. controls (140.9,242.23) and (145.61,246.92) .. (145.65,252.72) ;  
        	\\draw  [draw opacity=0] (155.83,247.51) .. controls (155.83,247.48) and (155.83,247.45) .. (155.83,247.42) .. controls (155.83,244.22) and (158.43,241.62) .. (161.63,241.62) .. controls (164.83,241.62) and (167.42,244.2) .. (167.44,247.38) -- (161.63,247.42) -- cycle ; \\draw  [color={rgb, 255:red, 192; green, 215; blue, 242 }  ,draw opacity=1 ] (155.83,247.51) .. controls (155.83,247.48) and (155.83,247.45) .. (155.83,247.42) .. controls (155.83,244.22) and (158.43,241.62) .. (161.63,241.62) .. controls (164.83,241.62) and (167.42,244.2) .. (167.44,247.38) ;  
        	\\draw  [draw opacity=0] (189.84,252.11) .. controls (189.84,252.08) and (189.84,252.05) .. (189.84,252.02) .. controls (189.84,248.82) and (192.44,246.22) .. (195.64,246.22) .. controls (198.83,246.22) and (201.42,248.8) .. (201.44,251.99) -- (195.64,252.02) -- cycle ; \\draw  [color={rgb, 255:red, 192; green, 215; blue, 242 }  ,draw opacity=1 ] (189.84,252.11) .. controls (189.84,252.08) and (189.84,252.05) .. (189.84,252.02) .. controls (189.84,248.82) and (192.44,246.22) .. (195.64,246.22) .. controls (198.83,246.22) and (201.42,248.8) .. (201.44,251.99) ;  
        	\\draw  [draw opacity=0] (266.61,243.06) .. controls (266.61,243) and (266.61,242.93) .. (266.61,242.87) .. controls (266.61,235.32) and (272.73,229.19) .. (280.28,229.19) .. controls (287.8,229.19) and (293.9,235.27) .. (293.95,242.77) -- (280.28,242.87) -- cycle ; \\draw  [color={rgb, 255:red, 192; green, 215; blue, 242 }  ,draw opacity=1 ] (266.61,243.06) .. controls (266.61,243) and (266.61,242.93) .. (266.61,242.87) .. controls (266.61,235.32) and (272.73,229.19) .. (280.28,229.19) .. controls (287.8,229.19) and (293.9,235.27) .. (293.95,242.77) ;  
        	\\draw  [draw opacity=0] (293.95,242.77) .. controls (293.95,242.74) and (293.95,242.7) .. (293.95,242.67) .. controls (293.95,238.7) and (297.17,235.48) .. (301.14,235.48) .. controls (305.1,235.48) and (308.31,238.67) .. (308.34,242.62) -- (301.14,242.67) -- cycle ; \\draw  [color={rgb, 255:red, 192; green, 215; blue, 242 }  ,draw opacity=1 ] (293.95,242.77) .. controls (293.95,242.74) and (293.95,242.7) .. (293.95,242.67) .. controls (293.95,238.7) and (297.17,235.48) .. (301.14,235.48) .. controls (305.1,235.48) and (308.31,238.67) .. (308.34,242.62) ;  
        	\\draw  [draw opacity=0] (308.34,239.41) .. controls (308.33,239.36) and (308.33,239.31) .. (308.33,239.26) .. controls (308.33,233.48) and (313.02,228.8) .. (318.79,228.8) .. controls (324.54,228.8) and (329.21,233.44) .. (329.25,239.18) -- (318.79,239.26) -- cycle ; \\draw  [color={rgb, 255:red, 192; green, 215; blue, 242 }  ,draw opacity=1 ] (308.34,239.41) .. controls (308.33,239.36) and (308.33,239.31) .. (308.33,239.26) .. controls (308.33,233.48) and (313.02,228.8) .. (318.79,228.8) .. controls (324.54,228.8) and (329.21,233.44) .. (329.25,239.18) ;  
        	\\draw  [draw opacity=0] (325.96,247) .. controls (325.96,246.95) and (325.96,246.9) .. (325.96,246.85) .. controls (325.96,241.08) and (330.64,236.4) .. (336.41,236.4) .. controls (342.16,236.4) and (346.83,241.04) .. (346.87,246.78) -- (336.41,246.85) -- cycle ; \\draw  [color={rgb, 255:red, 192; green, 215; blue, 242 }  ,draw opacity=1 ] (325.96,247) .. controls (325.96,246.95) and (325.96,246.9) .. (325.96,246.85) .. controls (325.96,241.08) and (330.64,236.4) .. (336.41,236.4) .. controls (342.16,236.4) and (346.83,241.04) .. (346.87,246.78) ;  
        	\\draw  [draw opacity=0] (299.52,252.77) .. controls (299.52,252.72) and (299.52,252.67) .. (299.52,252.62) .. controls (299.52,246.85) and (304.21,242.17) .. (309.98,242.17) .. controls (315.73,242.17) and (320.4,246.81) .. (320.43,252.55) -- (309.98,252.62) -- cycle ; \\draw  [color={rgb, 255:red, 192; green, 215; blue, 242 }  ,draw opacity=1 ] (299.52,252.77) .. controls (299.52,252.72) and (299.52,252.67) .. (299.52,252.62) .. controls (299.52,246.85) and (304.21,242.17) .. (309.98,242.17) .. controls (315.73,242.17) and (320.4,246.81) .. (320.43,252.55) ;  
        	\\draw  [draw opacity=0] (255.78,253.38) .. controls (255.78,253.33) and (255.78,253.28) .. (255.78,253.23) .. controls (255.78,247.46) and (260.46,242.78) .. (266.23,242.78) .. controls (271.98,242.78) and (276.65,247.42) .. (276.69,253.16) -- (266.23,253.23) -- cycle ; \\draw  [color={rgb, 255:red, 192; green, 215; blue, 242 }  ,draw opacity=1 ] (255.78,253.38) .. controls (255.78,253.33) and (255.78,253.28) .. (255.78,253.23) .. controls (255.78,247.46) and (260.46,242.78) .. (266.23,242.78) .. controls (271.98,242.78) and (276.65,247.42) .. (276.69,253.16) ;  
        	\\draw  [draw opacity=0] (286.76,248) .. controls (286.76,247.97) and (286.76,247.94) .. (286.76,247.91) .. controls (286.76,244.74) and (289.34,242.17) .. (292.51,242.17) .. controls (295.67,242.17) and (298.24,244.72) .. (298.26,247.88) -- (292.51,247.91) -- cycle ; \\draw  [color={rgb, 255:red, 192; green, 215; blue, 242 }  ,draw opacity=1 ] (286.76,248) .. controls (286.76,247.97) and (286.76,247.94) .. (286.76,247.91) .. controls (286.76,244.74) and (289.34,242.17) .. (292.51,242.17) .. controls (295.67,242.17) and (298.24,244.72) .. (298.26,247.88) ;  
        	\\draw  [draw opacity=0] (320.43,252.55) .. controls (320.43,252.52) and (320.43,252.5) .. (320.43,252.47) .. controls (320.43,249.3) and (323.01,246.72) .. (326.18,246.72) .. controls (329.34,246.72) and (331.91,249.28) .. (331.93,252.43) -- (326.18,252.47) -- cycle ; \\draw  [color={rgb, 255:red, 192; green, 215; blue, 242 }  ,draw opacity=1 ] (320.43,252.55) .. controls (320.43,252.52) and (320.43,252.5) .. (320.43,252.47) .. controls (320.43,249.3) and (323.01,246.72) .. (326.18,246.72) .. controls (329.34,246.72) and (331.91,249.28) .. (331.93,252.43) ;  
        	\\draw  [draw opacity=0] (193.24,237.44) .. controls (193.24,237.35) and (193.23,237.26) .. (193.23,237.17) .. controls (193.23,226.95) and (201.52,218.67) .. (211.74,218.67) .. controls (221.92,218.67) and (230.18,226.88) .. (230.24,237.05) -- (211.74,237.17) -- cycle ; \\draw  [color={rgb, 255:red, 192; green, 215; blue, 242 }  ,draw opacity=1 ] (193.24,237.44) .. controls (193.24,237.35) and (193.23,237.26) .. (193.23,237.17) .. controls (193.23,226.95) and (201.52,218.67) .. (211.74,218.67) .. controls (221.92,218.67) and (230.18,226.88) .. (230.24,237.05) ;  
        	\\draw  [draw opacity=0] (230.24,237.05) .. controls (230.24,237) and (230.24,236.95) .. (230.24,236.91) .. controls (230.24,231.53) and (234.6,227.17) .. (239.98,227.17) .. controls (245.33,227.17) and (249.68,231.49) .. (249.71,236.84) -- (239.98,236.91) -- cycle ; \\draw  [color={rgb, 255:red, 192; green, 215; blue, 242 }  ,draw opacity=1 ] (230.24,237.05) .. controls (230.24,237) and (230.24,236.95) .. (230.24,236.91) .. controls (230.24,231.53) and (234.6,227.17) .. (239.98,227.17) .. controls (245.33,227.17) and (249.68,231.49) .. (249.71,236.84) ;  
        	\\draw  [draw opacity=0] (249.71,232.49) .. controls (249.71,232.42) and (249.71,232.35) .. (249.71,232.29) .. controls (249.71,224.47) and (256.05,218.13) .. (263.86,218.13) .. controls (271.65,218.13) and (277.96,224.42) .. (278.02,232.19) -- (263.86,232.29) -- cycle ; \\draw  [color={rgb, 255:red, 192; green, 215; blue, 242 }  ,draw opacity=1 ] (249.71,232.49) .. controls (249.71,232.42) and (249.71,232.35) .. (249.71,232.29) .. controls (249.71,224.47) and (256.05,218.13) .. (263.86,218.13) .. controls (271.65,218.13) and (277.96,224.42) .. (278.02,232.19) ;  
        	\\draw  [draw opacity=0] (273.56,242.77) .. controls (273.56,242.7) and (273.56,242.63) .. (273.56,242.57) .. controls (273.56,234.75) and (279.9,228.41) .. (287.71,228.41) .. controls (295.5,228.41) and (301.81,234.7) .. (301.87,242.47) -- (287.71,242.57) -- cycle ; \\draw  [color={rgb, 255:red, 192; green, 215; blue, 242 }  ,draw opacity=1 ] (273.56,242.77) .. controls (273.56,242.7) and (273.56,242.63) .. (273.56,242.57) .. controls (273.56,234.75) and (279.9,228.41) .. (287.71,228.41) .. controls (295.5,228.41) and (301.81,234.7) .. (301.87,242.47) ;  
        	\\draw  [draw opacity=0] (237.79,250.58) .. controls (237.79,250.51) and (237.79,250.45) .. (237.79,250.38) .. controls (237.79,242.56) and (244.12,236.23) .. (251.94,236.23) .. controls (259.72,236.23) and (266.04,242.51) .. (266.09,250.28) -- (251.94,250.38) -- cycle ; \\draw  [color={rgb, 255:red, 192; green, 215; blue, 242 }  ,draw opacity=1 ] (237.79,250.58) .. controls (237.79,250.51) and (237.79,250.45) .. (237.79,250.38) .. controls (237.79,242.56) and (244.12,236.23) .. (251.94,236.23) .. controls (259.72,236.23) and (266.04,242.51) .. (266.09,250.28) ;  
        	\\draw  [draw opacity=0] (178.57,251.4) .. controls (178.57,251.34) and (178.57,251.27) .. (178.57,251.2) .. controls (178.57,243.39) and (184.91,237.05) .. (192.72,237.05) .. controls (200.51,237.05) and (206.82,243.33) .. (206.88,251.1) -- (192.72,251.2) -- cycle ; \\draw  [color={rgb, 255:red, 192; green, 215; blue, 242 }  ,draw opacity=1 ] (178.57,251.4) .. controls (178.57,251.34) and (178.57,251.27) .. (178.57,251.2) .. controls (178.57,243.39) and (184.91,237.05) .. (192.72,237.05) .. controls (200.51,237.05) and (206.82,243.33) .. (206.88,251.1) ;  
        	\\draw  [draw opacity=0] (220.52,244.12) .. controls (220.52,244.08) and (220.52,244.04) .. (220.52,244) .. controls (220.52,239.71) and (224,236.23) .. (228.29,236.23) .. controls (232.57,236.23) and (236.04,239.68) .. (236.07,243.95) -- (228.29,244) -- cycle ; \\draw  [color={rgb, 255:red, 192; green, 215; blue, 242 }  ,draw opacity=1 ] (220.52,244.12) .. controls (220.52,244.08) and (220.52,244.04) .. (220.52,244) .. controls (220.52,239.71) and (224,236.23) .. (228.29,236.23) .. controls (232.57,236.23) and (236.04,239.68) .. (236.07,243.95) ;  
        	\\draw  [draw opacity=0] (266.09,250.28) .. controls (266.09,250.25) and (266.09,250.21) .. (266.09,250.17) .. controls (266.09,245.88) and (269.57,242.39) .. (273.87,242.39) .. controls (278.15,242.39) and (281.62,245.85) .. (281.65,250.12) -- (273.87,250.17) -- cycle ; \\draw  [color={rgb, 255:red, 192; green, 215; blue, 242 }  ,draw opacity=1 ] (266.09,250.28) .. controls (266.09,250.25) and (266.09,250.21) .. (266.09,250.17) .. controls (266.09,245.88) and (269.57,242.39) .. (273.87,242.39) .. controls (278.15,242.39) and (281.62,245.85) .. (281.65,250.12) ;  
        \\end{tikzpicture}'''    
        # Nội dung câu hỏi
        noidungcauhoi = ('''\\immini{Trong một buổi thử nghiệm nguyên mẫu ô tô bay của Tesla tích hợp gói đẩy phản lực khí nén của SpaceX, chiếc xe thực hiện một cú nhảy thử nghiệm cất cánh thẳng đứng từ mặt đất. Độ cao $h$ (tính bằng mét) của xe so với mặt đất tại thời điểm $t$ giây ($0 \\le t \\le %s$) được mô hình hóa bởi hàm số bậc ba: $h(t) = %s$. Chiếc xe đạt độ cao lớn nhất so với mặt đất là bao nhiêu mét? (Làm tròn kết quả đến hàng đơn vị).}{%s}'''
                         %(str(t_end),
                           latex(h), hinhve
                         ))

        # Nội dung lời giải kèm bảng biến thiên tkz-tab chuẩn LaTeX
        loigiai = ('''Vận tốc tức thời của ô tô bay tại thời điểm $t$ là đạo hàm cấp một của hàm độ cao:\\\\
    $v(t) = h'(t) = %s$.\\\\
    Xét phương trình $h'(t) = 0$ trên đoạn $[0; %s]$:\\\\
    $%s = 0 \\Leftrightarrow \\left[\\begin{array}{l} t = %s \\text{ (nhận)} \\\\ t = -%s \\text{ (loại do } t \\ge 0\\text{)} \\end{array}\\right.$\\\\
    Bảng biến thiên của hàm số $h(t)$ trên đoạn $[0; %s]$:
    \\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\tkzTabInit[lgt=1.5,espcl=3]{$t$/0.8,$h'(t)$/0.8,$h(t)$/2}{$0$,$%s$,$%s$}
    \\tkzTabLine{,+,$0$,-,}
    \\tkzTabVar{-/$0$, +/$%s$, -/$%s$}
    \\end{tikzpicture}
    \\end{center}
    Căn cứ vào bảng biến thiên, hàm số $h(t)$ đạt giá trị lớn nhất trên đoạn $[0; %s]$ tại $t = %s$.\\\\
    Độ cao lớn nhất đạt được là $h_{\\max} = h(%s) = %s \\approx %s$ mét.'''
                   %(latex(dh1),
                     str(t_end),
                     latex(dh1), str(t0), str(t1),
                     str(t_end),
                     str(t0), str(t_end),
                     h_max_latex, h_end_latex,
                     str(t_end), str(t0),
                     str(t0), h_max_latex, str(kq_str)
                   ))

        # Đáp án dạng câu hỏi điền số ngắn
        dapan = '\\shortans[0]{$%s$}\n'%(str(kq_str))

    # Xuất câu hỏi và lời giải ra định dạng minipage ex chuẩn
    content = ('\\begin{minipage}{\\textwidth}\n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               str(dapan) +
               '\\loigiai{\n' +
               str(loigiai) + '\n' +
               '}\n' +
               '\\end{ex}\n' +
               '\\end{minipage}\n\n')
    return content


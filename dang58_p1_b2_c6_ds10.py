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


def bt_dang58_p1_b2_c6_ds10(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':

        N = random.choice([4, 5, 6])
        m = N - 1
        k = random.randint(0, N - 2)

        r = N - k
        p_thua = Rational(1, 2**r)
        p_thang = 1 - p_thua

        # Các đáp án trắc nghiệm
        du = ['$%s$' % (latex(p_thang))]
        da = random.choice(du)

        s = [
            '$%s$' % (latex(p_thua)),
            '$%s$' % (latex(Rational(1, 2))),
            '$%s$' % (latex(Rational(m, m + k))),
            '$%s$' % (latex(1 - Rational(1, 2**(r - 1)))) if r > 1 else '$%s$' % (latex(Rational(2, 3))),
            '$%s$' % (latex(Rational(m, 2 * N - 1))),
            '$%s$' % (latex(Rational(2**r - 2, 2**r + 1))),
            '$%s$' % (latex(Rational(3, 4))),
            '$%s$' % (latex(Rational(7, 8)))
        ]
        # Lọc bỏ các phần tử trùng với đáp án đúng
        s = [ans for ans in set(s) if ans != da]
        while len(s) < 3:
            s.append('$%s$' % (latex(Rational(random.randint(1, 7), 8))))
            s = [ans for ans in set(s) if ans != da]

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        # Câu hỏi
        noidungcauhoi = ('''\\immini{Hai người ngang tài ngang sức tranh chức vô địch của một cuộc thi cờ tướng. Người giành chiến thắng là người đầu tiên thắng được %s ván cờ. Tại thời điểm người chơi thứ nhất đã thắng %s ván và người chơi thứ hai mới thắng %s ván. Xác suất để người chơi thứ nhất giành chiến thắng là}
                         {\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
                         	\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.34 ] (101.28,155.42) .. controls (101.28,144.05) and (130.65,134.84) .. (166.88,134.84) .. controls (203.11,134.84) and (232.48,144.05) .. (232.48,155.42) .. controls (232.48,166.79) and (203.11,176) .. (166.88,176) .. controls (130.65,176) and (101.28,166.79) .. (101.28,155.42) -- cycle ;
                         	\\draw  [fill={rgb, 255:red, 12; green, 62; blue, 4 }  ,fill opacity=1 ] (100.6,87.4) .. controls (120.6,77.4) and (167.6,52.9) .. (216.6,78.4) .. controls (253.1,81.9) and (251.6,140.9) .. (228.6,156.9) .. controls (201.1,180.9) and (114.6,174.9) .. (98.6,150.4) .. controls (85.1,132.9) and (86.6,89.9) .. (100.6,87.4) -- cycle ;
                         	\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.19 ][line width=3.75]    (92.88,96.64) .. controls (86.48,120.4) and (123.28,143.6) .. (194.88,135.2) ;
                         	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.29 ][fill={rgb, 255:red, 15; green, 89; blue, 5 }  ,fill opacity=1 ] (91.6,102.15) .. controls (91.6,82.54) and (124.95,66.65) .. (166.1,66.65) .. controls (207.25,66.65) and (240.6,82.54) .. (240.6,102.15) .. controls (240.6,121.76) and (207.25,137.65) .. (166.1,137.65) .. controls (124.95,137.65) and (91.6,121.76) .. (91.6,102.15) -- cycle ;
                         	\\draw  [color={rgb, 255:red, 245; green, 203; blue, 35 }  ,draw opacity=1 ] (98.35,102.15) .. controls (98.35,85.44) and (128.68,71.9) .. (166.1,71.9) .. controls (203.52,71.9) and (233.85,85.44) .. (233.85,102.15) .. controls (233.85,118.86) and (203.52,132.4) .. (166.1,132.4) .. controls (128.68,132.4) and (98.35,118.86) .. (98.35,102.15) -- cycle ;
                         	\\draw  [color={rgb, 255:red, 245; green, 203; blue, 35 }  ,draw opacity=1 ] (102.6,101.4) .. controls (102.6,86.49) and (131.14,74.4) .. (166.35,74.4) .. controls (201.56,74.4) and (230.1,86.49) .. (230.1,101.4) .. controls (230.1,116.31) and (201.56,128.4) .. (166.35,128.4) .. controls (131.14,128.4) and (102.6,116.31) .. (102.6,101.4) -- cycle ;
                         	\\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 203; blue, 35 }  ,fill opacity=1 ] (144.12,84.55) .. controls (155.75,85.6) and (180.42,76.05) .. (180.19,83.73) .. controls (174.6,88.16) and (161.8,82.57) .. (148.77,87.92) .. controls (146.44,87.92) and (141.09,85.13) .. (144.12,84.55) -- cycle ;
                         	\\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 203; blue, 35 }  ,fill opacity=1 ] (150.87,89.78) .. controls (162.04,89.32) and (179.72,86.29) .. (177.4,90.25) .. controls (171.81,91.65) and (162.5,90.02) .. (149,93.97) .. controls (146.68,93.97) and (147.84,90.37) .. (150.87,89.78) -- cycle ;
                         	\\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 203; blue, 35 }  ,fill opacity=1 ] (151.8,95.6) .. controls (162.97,95.14) and (180.42,90.25) .. (178.33,96.07) .. controls (175.3,96.3) and (163.2,96.3) .. (150.63,98.86) .. controls (148.31,98.86) and (148.77,96.18) .. (151.8,95.6) -- cycle ;
                         	\\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 203; blue, 35 }  ,fill opacity=1 ] (143.65,102.58) .. controls (157.85,100.49) and (194.62,95.37) .. (195.55,97.93) .. controls (198.57,97.93) and (201.39,100.58) .. (200.2,101.65) .. controls (199.73,102.08) and (196.55,107.87) .. (192.52,112.82) .. controls (189.2,116.91) and (184.82,121.29) .. (183.45,121.2) .. controls (182.54,121.14) and (168.51,115.47) .. (169.02,113.29) .. controls (184.61,116.08) and (185.44,109.98) .. (189.03,104.21) .. controls (189.69,101.09) and (186.09,100.57) .. (185.54,100.02) .. controls (173.35,101.67) and (154.34,103.15) .. (144.35,106.07) .. controls (142.02,106.07) and (140.63,103.17) .. (143.65,102.58) -- cycle ;
                         	\\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 203; blue, 35 }  ,fill opacity=1 ] (143.65,102.58) .. controls (148.77,86.99) and (150.17,81.64) .. (154.53,85.16) .. controls (152.96,87.69) and (154.42,90.34) .. (149.94,102.35) .. controls (148.7,104.33) and (142.54,105.46) .. (143.65,102.58) -- cycle ;
                         	\\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 203; blue, 35 }  ,fill opacity=1 ] (159.71,102.82) .. controls (162.95,97.52) and (163.9,93.51) .. (163.9,84.43) .. controls (164.76,82.3) and (167.41,83.6) .. (169.02,84.9) .. controls (167.45,87.43) and (167.62,93.74) .. (165.99,102.58) .. controls (164.76,104.56) and (160.41,105.61) .. (159.71,102.82) -- cycle ;
                         	\\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 203; blue, 35 }  ,fill opacity=1 ] (142.49,108.87) .. controls (138.77,107.24) and (135.04,110.26) .. (129.92,109.1) .. controls (128.53,111.66) and (141.09,120.5) .. (142.49,108.87) -- cycle ;
                         	\\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 203; blue, 35 }  ,fill opacity=1 ] (155.75,108.4) .. controls (152.03,106.77) and (151.8,108.87) .. (146.21,108.17) .. controls (144.82,110.73) and (154.59,116.78) .. (155.75,108.4) -- cycle ;
                         	\\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 203; blue, 35 }  ,fill opacity=1 ] (168.32,108.17) .. controls (164.6,106.54) and (162.73,107.7) .. (157.62,106.54) .. controls (156.22,109.1) and (165.06,114.92) .. (168.32,108.17) -- cycle ;
                         	\\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 203; blue, 35 }  ,fill opacity=1 ] (180.42,106.54) .. controls (176.7,104.91) and (173.21,104.68) .. (166.69,104.91) .. controls (171.11,110.26) and (178.79,114.92) .. (180.42,106.54) -- cycle ;
                         	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.09 ] (120.08,163.2) .. controls (100.48,167.2) and (83.68,132) .. (89.28,110.8) .. controls (96.48,126.4) and (118.08,159.2) .. (120.08,163.2) -- cycle ;
                         	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.09 ] (176.08,173.2) .. controls (215.28,146) and (236.88,133.6) .. (242.88,102.8) .. controls (250.08,117.6) and (252.08,172.4) .. (176.08,173.2) -- cycle ;
                         	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.22 ] (224.08,80.4) .. controls (288.88,124) and (139.68,165.2) .. (97.28,115.6) .. controls (129.28,112) and (222.08,76.4) .. (224.08,80.4) -- cycle ;
                         	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.69 ] (233.68,116.8) .. controls (227.28,131.2) and (206.48,139.2) .. (173.28,138) .. controls (208.28,134.5) and (226.08,125.6) .. (233.68,116.8) -- cycle ;
                         \\end{tikzpicture}}'''
                         % (m + 1, m, k))

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải
        loigiai = ('''Vì hai người ngang tài ngang sức nên trong mỗi ván cờ, xác suất thắng của mỗi người là bằng nhau và bằng $\\frac{1}{2}$.\\\\
    Để giành chiến thắng chung cuộc, mỗi người cần thắng đủ %s ván.\\\\
    Hiện tại người thứ nhất đã thắng %s ván, do đó người thứ nhất chỉ cần thắng thêm $1$ ván nữa là giành chiến thắng chung cuộc.\\\\
    Người chơi thứ hai đã thắng %s ván, nên cần phải thắng thêm $%s - %s = %s$ ván liên tiếp nữa thì mới giành chiến thắng chung cuộc.\\\\
    Do đó, người chơi thứ hai chỉ có thể giành chiến thắng nếu toàn bộ $%s$ ván tiếp theo người thứ hai đều thắng.\\\\
    Xác suất để người chơi thứ hai thắng liên tiếp $%s$ ván là:
    \\[
    P_2 = \\left(\\frac{1}{2}\\right)^{%s} = %s.
    \\]
    Vì giải đấu chắc chắn sẽ tìm được người thắng cuộc nên biến cố người chơi thứ nhất giành chiến thắng là biến cố đối của biến cố người chơi thứ hai giành chiến thắng.\\\\
    Vậy xác suất để người chơi thứ nhất giành chiến thắng là:
    \\[
    P = 1 - P_2 = 1 - %s = %s.
    \\]'''
                   % (m + 1, m, k, m + 1, k, r, r, r, r, latex(p_thua), latex(p_thua), latex(p_thang)))

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\choice \n' +
               '{' + str(list_1[0]) + '}\n' +
               '{' + str(list_1[1]) + '}\n' +
               '{' + str(list_1[2]) + '}\n' +
               '{' + str(list_1[3]) + '}\n' +
               '\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content


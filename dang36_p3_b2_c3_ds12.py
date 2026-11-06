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


def bt_dang36_p3_b2_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                t = symbols('t')

                # Random các thông số cho phương trình: v(t) = (1/k) * (a - t^2) * e^(-b*t)
                # Trong bài gốc: k=2, a=10, b=0.2 (hay 1/5)
                a = random.randint(30, 80) 
                k = random.randint(2, 5)

                # Random hệ số của số mũ e, sử dụng Rational để sympy tính toán tích phân chính xác
                b_choices = [Rational(1,10), Rational(1,5), Rational(1,4), Rational(3,10)] # Tương ứng 0.1, 0.2, 0.25, 0.3
                b_frac = random.choice(b_choices)
                b_float = float(b_frac)
                b_str = str(b_float).replace('.', ',')

                # Chuỗi hiển thị hàm số v(t)
                func_str = "\\frac{1}{%s}\\left(%s - t^2\\right)e^{-%st}" % (k, a, b_str)

                # Thiết lập biểu thức toán học để tính toán trong Sympy
                v_expr = Rational(1, k) * (a - t**2) * exp(-b_frac * t)

                # Tính tích phân từ 0 đến căn(a)
                integral_expr = integrate(v_expr, (t, 0, sqrt(a)))

                # Tính ra số thập phân và làm tròn đến hàng phần mười
                result_float = integral_expr.evalf()
                result_dec = Decimal(str(result_float)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Chuyển đổi định dạng dấu phẩy cho kết quả đúng
                kq = str(result_dec).replace('.', ',')
                kq4 = float(result_dec)

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(kq)]
                da = random.choice(du)

                # Sinh các đáp án sai không trùng lặp
                s_set = set()
                offsets = [1.2, -1.5, 2.3, -2.1, 3.4, -3.2, 0.8, -0.9, 4.1, 1.8, -2.5]
                random.shuffle(offsets)

                for offset in offsets:
                    wrong_val = Decimal(str(max(0.1, kq4 + offset))).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                    wrong_str = '$%s$' % str(wrong_val).replace('.', ',')
                    if wrong_str != da and wrong_str not in s_set:
                        s_set.add(wrong_str)
                    if len(s_set) == 3:
                        break

                s = list(s_set)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                hinhve=r'''\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (219.93,160.44) -- (213.27,171.36) -- (186.5,179.27) -- (174.98,173.71) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.2 ][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (180.42,88.86) .. controls (191.86,88.86) and (201.13,96.27) .. (201.13,105.41) .. controls (201.13,109.42) and (199.35,113.09) .. (196.37,115.96) -- (183.41,121.78) .. controls (182.43,121.89) and (181.43,121.95) .. (180.42,121.95) .. controls (168.97,121.95) and (159.7,114.54) .. (159.7,105.41) .. controls (159.7,101.44) and (161.44,97.81) .. (164.35,94.96) -- (177.59,89.01) .. controls (178.51,88.91) and (179.46,88.86) .. (180.42,88.86) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ] (161.24,107.11) .. controls (161.24,99.59) and (168.03,93.5) .. (176.4,93.5) .. controls (184.76,93.5) and (191.55,99.59) .. (191.55,107.11) .. controls (191.55,114.62) and (184.76,120.71) .. (176.4,120.71) .. controls (168.03,120.71) and (161.24,114.62) .. (161.24,107.11) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (164.95,105.71) .. controls (164.95,98.97) and (170.91,93.5) .. (178.25,93.5) .. controls (185.59,93.5) and (191.55,98.97) .. (191.55,105.71) .. controls (191.55,112.46) and (185.59,117.93) .. (178.25,117.93) .. controls (170.91,117.93) and (164.95,112.46) .. (164.95,105.71) -- cycle ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ]   (171.14,112.05) -- (176.33,106.74) -- (184.13,98.76) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ]   (169.28,105.25) -- (186.6,105.87) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ]   (180.42,112.05) -- (175.16,98.76) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (174.04,105.71) .. controls (174.04,103.58) and (175.93,101.85) .. (178.25,101.85) .. controls (180.57,101.85) and (182.46,103.58) .. (182.46,105.71) .. controls (182.46,107.85) and (180.57,109.58) .. (178.25,109.58) .. controls (175.93,109.58) and (174.04,107.85) .. (174.04,105.71) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 17; green, 242; blue, 247 }  ,fill opacity=1 ] (173.21,98.76) .. controls (173.21,97.77) and (174.08,96.97) .. (175.16,96.97) .. controls (176.23,96.97) and (177.11,97.77) .. (177.11,98.76) .. controls (177.11,99.75) and (176.23,100.55) .. (175.16,100.55) .. controls (174.08,100.55) and (173.21,99.75) .. (173.21,98.76) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 17; green, 242; blue, 247 }  ,fill opacity=1 ] (167.33,105.25) .. controls (167.33,104.26) and (168.21,103.46) .. (169.28,103.46) .. controls (170.36,103.46) and (171.23,104.26) .. (171.23,105.25) .. controls (171.23,106.24) and (170.36,107.04) .. (169.28,107.04) .. controls (168.21,107.04) and (167.33,106.24) .. (167.33,105.25) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 17; green, 242; blue, 247 }  ,fill opacity=1 ] (169.19,112.05) .. controls (169.19,111.06) and (170.06,110.26) .. (171.14,110.26) .. controls (172.21,110.26) and (173.09,111.06) .. (173.09,112.05) .. controls (173.09,113.04) and (172.21,113.84) .. (171.14,113.84) .. controls (170.06,113.84) and (169.19,113.04) .. (169.19,112.05) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 17; green, 242; blue, 247 }  ,fill opacity=1 ] (178.47,113.84) .. controls (178.47,112.86) and (179.34,112.05) .. (180.42,112.05) .. controls (181.49,112.05) and (182.36,112.86) .. (182.36,113.84) .. controls (182.36,114.83) and (181.49,115.63) .. (180.42,115.63) .. controls (179.34,115.63) and (178.47,114.83) .. (178.47,113.84) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 17; green, 242; blue, 247 }  ,fill opacity=1 ] (184.65,105.87) .. controls (184.65,104.88) and (185.52,104.08) .. (186.6,104.08) .. controls (187.68,104.08) and (188.55,104.88) .. (188.55,105.87) .. controls (188.55,106.86) and (187.68,107.66) .. (186.6,107.66) .. controls (185.52,107.66) and (184.65,106.86) .. (184.65,105.87) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 17; green, 242; blue, 247 }  ,fill opacity=1 ] (182.18,98.76) .. controls (182.18,97.77) and (183.05,96.97) .. (184.13,96.97) .. controls (185.2,96.97) and (186.08,97.77) .. (186.08,98.76) .. controls (186.08,99.75) and (185.2,100.55) .. (184.13,100.55) .. controls (183.05,100.55) and (182.18,99.75) .. (182.18,98.76) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.38 ] (161.86,106.95) .. controls (161.86,99.52) and (168.51,93.5) .. (176.7,93.5) .. controls (184.9,93.5) and (191.55,99.52) .. (191.55,106.95) .. controls (191.55,114.38) and (184.9,120.4) .. (176.7,120.4) .. controls (168.51,120.4) and (161.86,114.38) .. (161.86,106.95) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.45 ] (198.97,98.76) .. controls (201.13,102.78) and (202.68,106.18) .. (196.37,115.96) .. controls (191.55,119.78) and (185.05,120.71) .. (177.94,122.26) .. controls (188.76,116.38) and (190.93,115.92) .. (191.55,105.71) .. controls (194.64,101.08) and (201.75,95.36) .. (198.97,98.76) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.45 ] (180.42,88.86) .. controls (184.13,91.34) and (195.57,89.79) .. (188.15,94.12) .. controls (183.32,97.95) and (185.36,91.95) .. (178.25,93.5) .. controls (189.07,87.62) and (170.52,96.59) .. (168.36,95.05) .. controls (171.45,90.41) and (182.27,87.32) .. (180.42,88.86) -- cycle ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (175.16,91.95) -- (181.34,89.17) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.49 ]   (171.76,98.14) .. controls (175.78,94.43) and (180.11,95.05) .. (184.13,98.76) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.56 ] (172.96,98.76) .. controls (172.96,97.45) and (174.82,96.39) .. (177.11,96.39) .. controls (179.4,96.39) and (181.25,97.45) .. (181.25,98.76) .. controls (181.25,100.06) and (179.4,101.12) .. (177.11,101.12) .. controls (174.82,101.12) and (172.96,100.06) .. (172.96,98.76) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (246.47,163.36) -- (242.35,169.36) -- (224.96,173.02) -- (218.77,169.2) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (269.56,155.16) -- (265.44,161.16) -- (248.05,164.82) -- (241.86,160.99) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.13 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (168.23,111.74) .. controls (179.36,113.29) and (152.15,123.19) .. (142.88,128.75) .. controls (139.16,130.61) and (133.6,126.9) .. (115.97,138.96) .. controls (143.18,112.05) and (157.1,115.76) .. (168.23,111.74) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (170.44,114.02) -- (160.75,119.24) -- (152.62,119.39) -- (162.32,114.17) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.15 ][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (147.2,126.9) .. controls (164.52,100.92) and (274.6,88.55) .. (273.06,103.7) .. controls (246.16,117.93) and (201.01,120.4) .. (176.58,129.06) .. controls (162.97,124.42) and (153.38,124.63) .. (147.2,126.9) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.31 ] (162.97,125.04) .. controls (191.11,100.3) and (249.87,95.36) .. (269.04,104.01) .. controls (242.14,118.24) and (201.01,120.4) .. (176.58,129.06) .. controls (162.97,124.42) and (170.71,124.42) .. (162.97,125.04) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.42 ] (155.55,125.35) .. controls (183.69,100.61) and (234.1,93.19) .. (253.27,101.85) .. controls (226.37,116.07) and (195.75,117.93) .. (171.32,126.59) .. controls (157.72,121.95) and (163.28,124.73) .. (155.55,125.35) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (174.11,110.51) .. controls (210.9,89.48) and (234.1,91.95) .. (257.29,96.28) .. controls (229.46,99.68) and (229.15,100.92) .. (206.88,112.67) .. controls (195.44,109.89) and (181.84,109.89) .. (174.11,110.51) -- cycle ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.43 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.43 ]   (182.15,106.49) .. controls (187.71,104.94) and (198.23,104.94) .. (211.83,109.89) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.43 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.43 ]   (191.42,102.16) .. controls (196.99,100.61) and (205.65,100.61) .. (219.25,105.56) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.43 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.43 ]   (200.39,98.45) .. controls (205.96,96.9) and (213.69,97.21) .. (227.29,102.16) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.43 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.43 ]   (209.36,95.66) .. controls (214.92,94.12) and (220.49,94.43) .. (234.1,99.38) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.43 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.43 ]   (220.49,94.12) .. controls (226.06,92.57) and (229.46,92.26) .. (243.06,97.21) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.42 ] (174.11,110.51) .. controls (209.98,90.1) and (232.55,90.72) .. (257.29,96.28) .. controls (201.94,96.9) and (217.71,102.16) .. (193.28,110.82) .. controls (180.29,108.03) and (181.84,109.89) .. (174.11,110.51) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.14 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (178.25,128.75) .. controls (214.74,120.09) and (215.36,116.38) .. (284.62,106.8) .. controls (311.84,109.89) and (317.4,132.77) .. (275.97,154.42) .. controls (249.99,163.69) and (223.71,171.73) .. (195.26,170.81) .. controls (232.36,141.43) and (171.76,134.32) .. (178.25,128.75) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.21 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (304.41,118.24) .. controls (312.39,123.56) and (308.43,139.88) .. (303.49,139.88) .. controls (293.31,144.49) and (271.12,152.43) .. (256.79,152.56) .. controls (235.46,152.56) and (229.89,137.41) .. (304.41,118.24) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 8; green, 246; blue, 251 }  ,fill opacity=1 ] (249.34,145.51) .. controls (249.5,143.47) and (251.17,141.46) .. (253.06,141.02) -- (266.73,137.81) .. controls (268.62,137.36) and (270.03,138.65) .. (269.87,140.69) -- (269.87,140.69) .. controls (269.71,142.73) and (268.05,144.74) .. (266.15,145.18) -- (252.49,148.39) .. controls (250.59,148.84) and (249.18,147.55) .. (249.34,145.51) -- cycle ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.27 ]   (264.21,145.45) -- (265.14,138.34) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.27 ]   (259.27,147) -- (259.89,138.96) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.27 ]   (254.32,148.23) -- (254.94,140.19) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.34 ]   (252.49,148.39) .. controls (261.12,147.61) and (271.95,144.52) .. (269.47,138.34) ;
            	\draw [color={rgb, 255:red, 8; green, 246; blue, 251 }  ,draw opacity=0.4 ]   (252.46,150.09) .. controls (261.72,148.07) and (273.8,145.45) .. (271.33,139.27) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.4 ] (285.55,129.37) -- (302.56,123.49) -- (288.95,130.61) -- cycle ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1.5]    (286.17,131.23) .. controls (283.7,135.55) and (285.86,146.38) .. (292.04,148.23) ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.2 ][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (307.82,120.71) .. controls (319.26,120.71) and (328.53,128.12) .. (328.53,137.26) .. controls (328.53,141.27) and (326.75,144.94) .. (323.77,147.81) -- (310.81,153.63) .. controls (309.83,153.74) and (308.83,153.8) .. (307.82,153.8) .. controls (296.37,153.8) and (287.1,146.39) .. (287.1,137.26) .. controls (287.1,133.29) and (288.84,129.66) .. (291.75,126.81) -- (304.99,120.86) .. controls (305.91,120.76) and (306.86,120.71) .. (307.82,120.71) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ] (288.64,138.96) .. controls (288.64,131.44) and (295.43,125.35) .. (303.8,125.35) .. controls (312.16,125.35) and (318.95,131.44) .. (318.95,138.96) .. controls (318.95,146.47) and (312.16,152.56) .. (303.8,152.56) .. controls (295.43,152.56) and (288.64,146.47) .. (288.64,138.96) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (292.35,137.56) .. controls (292.35,130.82) and (298.31,125.35) .. (305.65,125.35) .. controls (312.99,125.35) and (318.95,130.82) .. (318.95,137.56) .. controls (318.95,144.31) and (312.99,149.78) .. (305.65,149.78) .. controls (298.31,149.78) and (292.35,144.31) .. (292.35,137.56) -- cycle ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ]   (298.54,143.9) -- (303.73,138.59) -- (311.53,130.61) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ]   (296.68,137.1) -- (314,137.72) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ]   (307.82,143.9) -- (302.56,130.61) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (301.44,137.56) .. controls (301.44,135.43) and (303.33,133.7) .. (305.65,133.7) .. controls (307.97,133.7) and (309.86,135.43) .. (309.86,137.56) .. controls (309.86,139.7) and (307.97,141.43) .. (305.65,141.43) .. controls (303.33,141.43) and (301.44,139.7) .. (301.44,137.56) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 17; green, 242; blue, 247 }  ,fill opacity=1 ] (300.61,130.61) .. controls (300.61,129.62) and (301.48,128.82) .. (302.56,128.82) .. controls (303.64,128.82) and (304.51,129.62) .. (304.51,130.61) .. controls (304.51,131.6) and (303.64,132.4) .. (302.56,132.4) .. controls (301.48,132.4) and (300.61,131.6) .. (300.61,130.61) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 17; green, 242; blue, 247 }  ,fill opacity=1 ] (294.73,137.1) .. controls (294.73,136.11) and (295.61,135.31) .. (296.68,135.31) .. controls (297.76,135.31) and (298.63,136.11) .. (298.63,137.1) .. controls (298.63,138.09) and (297.76,138.89) .. (296.68,138.89) .. controls (295.61,138.89) and (294.73,138.09) .. (294.73,137.1) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 17; green, 242; blue, 247 }  ,fill opacity=1 ] (296.59,143.9) .. controls (296.59,142.91) and (297.46,142.11) .. (298.54,142.11) .. controls (299.62,142.11) and (300.49,142.91) .. (300.49,143.9) .. controls (300.49,144.89) and (299.62,145.69) .. (298.54,145.69) .. controls (297.46,145.69) and (296.59,144.89) .. (296.59,143.9) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 17; green, 242; blue, 247 }  ,fill opacity=1 ] (305.87,145.69) .. controls (305.87,144.71) and (306.74,143.9) .. (307.82,143.9) .. controls (308.89,143.9) and (309.76,144.71) .. (309.76,145.69) .. controls (309.76,146.68) and (308.89,147.48) .. (307.82,147.48) .. controls (306.74,147.48) and (305.87,146.68) .. (305.87,145.69) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 17; green, 242; blue, 247 }  ,fill opacity=1 ] (312.05,137.72) .. controls (312.05,136.73) and (312.92,135.93) .. (314,135.93) .. controls (315.08,135.93) and (315.95,136.73) .. (315.95,137.72) .. controls (315.95,138.71) and (315.08,139.51) .. (314,139.51) .. controls (312.92,139.51) and (312.05,138.71) .. (312.05,137.72) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 17; green, 242; blue, 247 }  ,fill opacity=1 ] (309.58,130.61) .. controls (309.58,129.62) and (310.45,128.82) .. (311.53,128.82) .. controls (312.6,128.82) and (313.48,129.62) .. (313.48,130.61) .. controls (313.48,131.6) and (312.6,132.4) .. (311.53,132.4) .. controls (310.45,132.4) and (309.58,131.6) .. (309.58,130.61) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.38 ] (289.26,138.8) .. controls (289.26,131.37) and (295.91,125.35) .. (304.1,125.35) .. controls (312.3,125.35) and (318.95,131.37) .. (318.95,138.8) .. controls (318.95,146.23) and (312.3,152.25) .. (304.1,152.25) .. controls (295.91,152.25) and (289.26,146.23) .. (289.26,138.8) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.45 ] (326.37,130.61) .. controls (328.53,134.63) and (330.08,138.03) .. (323.77,147.81) .. controls (318.95,151.63) and (312.45,152.56) .. (305.34,154.11) .. controls (316.16,148.23) and (318.33,147.77) .. (318.95,137.56) .. controls (322.04,132.93) and (329.15,127.21) .. (326.37,130.61) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.45 ] (307.82,120.71) .. controls (311.53,123.19) and (322.97,121.64) .. (315.55,125.97) .. controls (310.72,129.8) and (312.76,123.8) .. (305.65,125.35) .. controls (316.47,119.47) and (297.92,128.44) .. (295.76,126.9) .. controls (298.85,122.26) and (309.67,119.17) .. (307.82,120.71) -- cycle ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (302.56,123.8) -- (308.74,121.02) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.49 ]   (299.16,129.99) .. controls (303.18,126.28) and (307.51,126.9) .. (311.53,130.61) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.56 ] (300.36,130.61) .. controls (300.36,129.3) and (302.22,128.24) .. (304.51,128.24) .. controls (306.8,128.24) and (308.65,129.3) .. (308.65,130.61) .. controls (308.65,131.91) and (306.8,132.97) .. (304.51,132.97) .. controls (302.22,132.97) and (300.36,131.91) .. (300.36,130.61) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (203.33,155.52) .. controls (203.9,153.58) and (205.79,151.74) .. (207.56,151.41) -- (233.61,146.56) .. controls (235.38,146.23) and (236.36,147.54) .. (235.8,149.47) -- (235.8,149.47) .. controls (235.24,151.41) and (233.35,153.25) .. (231.58,153.58) -- (205.52,158.43) .. controls (203.75,158.76) and (202.77,157.45) .. (203.33,155.52) -- cycle ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.46 ]   (207.69,157.14) .. controls (226.49,154.11) and (236.38,155.04) .. (235.15,147.61) ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.2 ][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (261.43,88.86) .. controls (272.87,88.86) and (282.15,96.27) .. (282.15,105.41) .. controls (282.15,109.42) and (280.36,113.09) .. (277.39,115.96) -- (264.43,121.78) .. controls (263.45,121.89) and (262.45,121.95) .. (261.43,121.95) .. controls (249.99,121.95) and (240.71,114.54) .. (240.71,105.41) .. controls (240.71,101.44) and (242.46,97.81) .. (245.37,94.96) -- (258.6,89.01) .. controls (259.53,88.91) and (260.47,88.86) .. (261.43,88.86) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ] (242.26,107.11) .. controls (242.26,99.59) and (249.04,93.5) .. (257.41,93.5) .. controls (265.78,93.5) and (272.56,99.59) .. (272.56,107.11) .. controls (272.56,114.62) and (265.78,120.71) .. (257.41,120.71) .. controls (249.04,120.71) and (242.26,114.62) .. (242.26,107.11) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (245.97,105.71) .. controls (245.97,98.97) and (251.92,93.5) .. (259.27,93.5) .. controls (266.61,93.5) and (272.56,98.97) .. (272.56,105.71) .. controls (272.56,112.46) and (266.61,117.93) .. (259.27,117.93) .. controls (251.92,117.93) and (245.97,112.46) .. (245.97,105.71) -- cycle ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ]   (252.16,112.05) -- (257.35,106.74) -- (265.14,98.76) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ]   (250.3,105.25) -- (267.62,105.87) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ]   (261.43,112.05) -- (256.17,98.76) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (255.06,105.71) .. controls (255.06,103.58) and (256.94,101.85) .. (259.27,101.85) .. controls (261.59,101.85) and (263.47,103.58) .. (263.47,105.71) .. controls (263.47,107.85) and (261.59,109.58) .. (259.27,109.58) .. controls (256.94,109.58) and (255.06,107.85) .. (255.06,105.71) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 17; green, 242; blue, 247 }  ,fill opacity=1 ] (254.23,98.76) .. controls (254.23,97.77) and (255.1,96.97) .. (256.17,96.97) .. controls (257.25,96.97) and (258.12,97.77) .. (258.12,98.76) .. controls (258.12,99.75) and (257.25,100.55) .. (256.17,100.55) .. controls (255.1,100.55) and (254.23,99.75) .. (254.23,98.76) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 17; green, 242; blue, 247 }  ,fill opacity=1 ] (248.35,105.25) .. controls (248.35,104.26) and (249.22,103.46) .. (250.3,103.46) .. controls (251.38,103.46) and (252.25,104.26) .. (252.25,105.25) .. controls (252.25,106.24) and (251.38,107.04) .. (250.3,107.04) .. controls (249.22,107.04) and (248.35,106.24) .. (248.35,105.25) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 17; green, 242; blue, 247 }  ,fill opacity=1 ] (250.21,112.05) .. controls (250.21,111.06) and (251.08,110.26) .. (252.16,110.26) .. controls (253.23,110.26) and (254.1,111.06) .. (254.1,112.05) .. controls (254.1,113.04) and (253.23,113.84) .. (252.16,113.84) .. controls (251.08,113.84) and (250.21,113.04) .. (250.21,112.05) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 17; green, 242; blue, 247 }  ,fill opacity=1 ] (259.48,113.84) .. controls (259.48,112.86) and (260.36,112.05) .. (261.43,112.05) .. controls (262.51,112.05) and (263.38,112.86) .. (263.38,113.84) .. controls (263.38,114.83) and (262.51,115.63) .. (261.43,115.63) .. controls (260.36,115.63) and (259.48,114.83) .. (259.48,113.84) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 17; green, 242; blue, 247 }  ,fill opacity=1 ] (265.67,105.87) .. controls (265.67,104.88) and (266.54,104.08) .. (267.62,104.08) .. controls (268.69,104.08) and (269.57,104.88) .. (269.57,105.87) .. controls (269.57,106.86) and (268.69,107.66) .. (267.62,107.66) .. controls (266.54,107.66) and (265.67,106.86) .. (265.67,105.87) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 17; green, 242; blue, 247 }  ,fill opacity=1 ] (263.19,98.76) .. controls (263.19,97.77) and (264.07,96.97) .. (265.14,96.97) .. controls (266.22,96.97) and (267.09,97.77) .. (267.09,98.76) .. controls (267.09,99.75) and (266.22,100.55) .. (265.14,100.55) .. controls (264.07,100.55) and (263.19,99.75) .. (263.19,98.76) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.38 ] (242.88,106.95) .. controls (242.88,99.52) and (249.52,93.5) .. (257.72,93.5) .. controls (265.92,93.5) and (272.56,99.52) .. (272.56,106.95) .. controls (272.56,114.38) and (265.92,120.4) .. (257.72,120.4) .. controls (249.52,120.4) and (242.88,114.38) .. (242.88,106.95) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.45 ] (279.99,98.76) .. controls (282.15,102.78) and (283.7,106.18) .. (277.39,115.96) .. controls (272.56,119.78) and (266.07,120.71) .. (258.96,122.26) .. controls (269.78,116.38) and (271.95,115.92) .. (272.56,105.71) .. controls (275.66,101.08) and (282.77,95.36) .. (279.99,98.76) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.45 ] (261.43,88.86) .. controls (265.14,91.34) and (276.58,89.79) .. (269.16,94.12) .. controls (264.34,97.95) and (266.38,91.95) .. (259.27,93.5) .. controls (270.09,87.62) and (251.54,96.59) .. (249.37,95.05) .. controls (252.46,90.41) and (263.29,87.32) .. (261.43,88.86) -- cycle ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (256.17,91.95) -- (262.36,89.17) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.49 ]   (252.77,98.14) .. controls (256.79,94.43) and (261.12,95.05) .. (265.14,98.76) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.56 ] (253.98,98.76) .. controls (253.98,97.45) and (255.84,96.39) .. (258.12,96.39) .. controls (260.41,96.39) and (262.27,97.45) .. (262.27,98.76) .. controls (262.27,100.06) and (260.41,101.12) .. (258.12,101.12) .. controls (255.84,101.12) and (253.98,100.06) .. (253.98,98.76) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (240.1,107.72) -- (246.74,118.7) -- (261.43,121.95) -- (279.06,115.76) -- (261.43,121.95) -- (232.06,115.46) -- (233.33,108.91) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.38 ] (240.1,107.72) -- (241.02,109.58) -- (237.62,110.2) -- (233.33,108.91) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.34 ] (189.49,129.57) .. controls (191.17,129.02) and (193.4,128.96) .. (194.48,129.44) -- (204.95,134.05) .. controls (206.02,134.53) and (205.54,135.36) .. (203.87,135.91) -- (203.87,135.91) .. controls (202.19,136.46) and (199.96,136.52) .. (198.88,136.04) -- (188.42,131.43) .. controls (187.34,130.96) and (187.82,130.12) .. (189.49,129.57) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (212.25,122.35) -- (224.3,118.97) -- (230.19,120.74) -- (218.14,124.11) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (233.76,132.28) .. controls (233.23,131.49) and (233.38,130.85) .. (234.09,130.85) .. controls (234.8,130.85) and (235.81,131.49) .. (236.35,132.28) .. controls (236.88,133.06) and (236.73,133.7) .. (236.02,133.7) .. controls (235.31,133.7) and (234.3,133.06) .. (233.76,132.28) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (210.4,161.31) .. controls (211.09,160.65) and (211.74,160.68) .. (211.86,161.39) .. controls (211.98,162.09) and (211.53,163.19) .. (210.85,163.85) .. controls (210.17,164.51) and (209.51,164.48) .. (209.39,163.78) .. controls (209.27,163.07) and (209.72,161.97) .. (210.4,161.31) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (242.87,158.52) .. controls (243.56,157.86) and (244.21,157.9) .. (244.33,158.6) .. controls (244.45,159.31) and (244,160.41) .. (243.32,161.07) .. controls (242.63,161.73) and (241.98,161.7) .. (241.86,160.99) .. controls (241.74,160.29) and (242.19,159.18) .. (242.87,158.52) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.34 ] (286.83,120.48) .. controls (287.89,121.91) and (287.45,123.55) .. (285.85,124.15) -- (276.93,127.49) .. controls (275.33,128.09) and (273.18,127.42) .. (272.12,125.99) -- (272.12,125.99) .. controls (271.06,124.57) and (271.5,122.93) .. (273.1,122.33) -- (282.02,118.99) .. controls (283.62,118.39) and (285.77,119.06) .. (286.83,120.48) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.25 ] (275.97,154.42) -- (235.02,166.17) -- (197.3,171.12) -- (208.12,161.53) -- (240.9,158.13) -- (287.59,147.31) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.25 ] (304.41,118.24) -- (267.49,129.06) -- (258.96,122.26) -- (297.49,110.51) -- cycle ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.11 ]   (204.1,146.07) -- (257.29,134.32) ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (213.06,96.4) -- (213.06,100.67) .. controls (213.06,101.08) and (211.95,101.41) .. (210.6,101.41) .. controls (209.24,101.41) and (208.13,101.08) .. (208.13,100.67) -- (208.13,96.4) .. controls (208.13,96) and (209.24,95.66) .. (210.6,95.66) .. controls (211.95,95.66) and (213.06,96) .. (213.06,96.4) .. controls (213.06,96.81) and (211.95,97.14) .. (210.6,97.14) .. controls (209.24,97.14) and (208.13,96.81) .. (208.13,96.4) ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (212.41,74.56) -- (211.25,95.68) .. controls (211.25,95.79) and (210.97,95.85) .. (210.62,95.83) .. controls (210.28,95.82) and (210.01,95.72) .. (210.02,95.61) -- (211.18,74.5) .. controls (211.18,74.39) and (211.46,74.33) .. (211.8,74.34) .. controls (212.14,74.36) and (212.42,74.46) .. (212.41,74.56) .. controls (212.41,74.67) and (212.12,74.73) .. (211.78,74.71) .. controls (211.44,74.7) and (211.17,74.6) .. (211.18,74.5) ;
            	\draw  [fill={rgb, 255:red, 52; green, 50; blue, 50 }  ,fill opacity=1 ] (113.81,148.02) .. controls (115.57,134.49) and (137.74,125.08) .. (163.33,126.99) .. controls (188.92,128.91) and (208.24,141.43) .. (206.49,154.96) .. controls (204.73,168.49) and (182.56,177.91) .. (156.97,175.99) .. controls (131.37,174.08) and (112.05,161.56) .. (113.81,148.02) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (110.75,149.92) .. controls (111.67,137.61) and (133.17,129.18) .. (158.76,131.09) .. controls (184.35,133.01) and (204.35,144.54) .. (203.43,156.86) .. controls (202.51,169.17) and (181.01,177.6) .. (155.42,175.68) .. controls (129.83,173.77) and (109.83,162.23) .. (110.75,149.92) -- cycle ;
            	\draw  [fill={rgb, 255:red, 38; green, 36; blue, 36 }  ,fill opacity=1 ] (127.47,152.87) .. controls (126.03,139.04) and (138.39,127.82) .. (155.08,127.82) .. controls (171.78,127.82) and (186.49,139.04) .. (187.93,152.87) .. controls (189.38,166.7) and (177.02,177.92) .. (160.32,177.92) .. controls (143.63,177.92) and (128.92,166.7) .. (127.47,152.87) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (129.85,155.19) .. controls (128.52,142.47) and (138.72,132.15) .. (152.64,132.15) .. controls (166.56,132.15) and (178.92,142.47) .. (180.25,155.19) .. controls (181.58,167.91) and (171.38,178.23) .. (157.46,178.23) .. controls (143.54,178.23) and (131.18,167.91) .. (129.85,155.19) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (137.44,154.57) .. controls (136.59,146.46) and (143.09,139.88) .. (151.97,139.88) .. controls (160.84,139.88) and (168.73,146.46) .. (169.57,154.57) .. controls (170.42,162.68) and (163.92,169.26) .. (155.04,169.26) .. controls (146.17,169.26) and (138.29,162.68) .. (137.44,154.57) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (191.35,151.79) .. controls (191.12,149.65) and (192.84,147.92) .. (195.17,147.92) .. controls (197.51,147.92) and (199.58,149.65) .. (199.8,151.79) .. controls (200.03,153.92) and (198.32,155.65) .. (195.98,155.65) .. controls (193.64,155.65) and (191.57,153.92) .. (191.35,151.79) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (189.8,160.45) .. controls (189.58,158.31) and (191.29,156.58) .. (193.63,156.58) .. controls (195.96,156.58) and (198.03,158.31) .. (198.26,160.45) .. controls (198.48,162.58) and (196.77,164.31) .. (194.43,164.31) .. controls (192.1,164.31) and (190.02,162.58) .. (189.8,160.45) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (113.42,146.53) .. controls (113.2,144.4) and (114.91,142.67) .. (117.25,142.67) .. controls (119.58,142.67) and (121.66,144.4) .. (121.88,146.53) .. controls (122.1,148.67) and (120.39,150.4) .. (118.06,150.4) .. controls (115.72,150.4) and (113.65,148.67) .. (113.42,146.53) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (114.04,155.19) .. controls (113.82,153.06) and (115.53,151.32) .. (117.87,151.32) .. controls (120.2,151.32) and (122.27,153.06) .. (122.5,155.19) .. controls (122.72,157.33) and (121.01,159.06) .. (118.67,159.06) .. controls (116.34,159.06) and (114.26,157.33) .. (114.04,155.19) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 80; green, 224; blue, 227 }  ,fill opacity=0.7 ] (136.99,151.85) .. controls (138.42,145.04) and (145.11,139.88) .. (153.14,139.88) .. controls (154.22,139.88) and (155.27,139.98) .. (156.29,140.15) -- (153.14,154.57) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 80; green, 224; blue, 227 }  ,fill opacity=0.7 ] (169.27,156.82) .. controls (168.16,162.17) and (163.83,166.73) .. (157.96,168.51) -- (153.14,154.57) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.73 ] (141.54,148.18) .. controls (140.91,146.89) and (142.43,144.84) .. (144.94,143.6) .. controls (147.46,142.37) and (150.01,142.41) .. (150.64,143.7) .. controls (151.28,144.99) and (149.75,147.03) .. (147.24,148.27) .. controls (144.73,149.51) and (142.18,149.47) .. (141.54,148.18) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.73 ] (157.22,166.2) .. controls (156.39,165.04) and (157.56,162.77) .. (159.83,161.14) .. controls (162.11,159.51) and (164.64,159.13) .. (165.47,160.3) .. controls (166.31,161.47) and (165.14,163.74) .. (162.86,165.37) .. controls (160.58,167) and (158.06,167.37) .. (157.22,166.2) -- cycle ;
            	\draw  [draw opacity=0] (142.76,161.06) .. controls (141.53,159.27) and (140.8,157.09) .. (140.8,154.75) .. controls (140.8,149.04) and (145.1,144.34) .. (150.64,143.7) -- (151.94,154.75) -- cycle ; \draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.57 ] (142.76,161.06) .. controls (141.53,159.27) and (140.8,157.09) .. (140.8,154.75) .. controls (140.8,149.04) and (145.1,144.34) .. (150.64,143.7) ;  
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.46 ] (161.48,165.7) .. controls (159.79,166.94) and (157.81,167.79) .. (155.63,168.13) .. controls (152.16,168.68) and (148.77,167.83) .. (145.97,165.97) -- (153.29,153.21) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.32 ] (144.01,154.75) .. controls (143.56,150.45) and (146.74,146.97) .. (151.12,146.97) .. controls (155.5,146.97) and (159.41,150.45) .. (159.86,154.75) .. controls (160.31,159.06) and (157.13,162.54) .. (152.75,162.54) .. controls (148.37,162.54) and (144.46,159.06) .. (144.01,154.75) -- cycle ;
            	\draw  [color={rgb, 255:red, 80; green, 227; blue, 222 }  ,draw opacity=0.32 ] (137.44,154.64) .. controls (136.59,146.49) and (143.13,139.88) .. (152.04,139.88) .. controls (160.95,139.88) and (168.87,146.49) .. (169.72,154.64) .. controls (170.57,162.8) and (164.04,169.4) .. (155.13,169.4) .. controls (146.21,169.4) and (138.3,162.8) .. (137.44,154.64) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 65; green, 62; blue, 62 }  ,fill opacity=0.08 ] (128.47,206.06) .. controls (134.69,202.95) and (145.37,200.85) .. (163.26,198.51) .. controls (176.38,196.8) and (194.42,197.67) .. (209.65,196.66) .. controls (224.25,195.68) and (240.75,195.28) .. (253.56,195.42) .. controls (281.61,195.73) and (299.59,196.11) .. (290,205.69) .. controls (281.07,207.86) and (265.28,213.23) .. (246.75,214.59) .. controls (233.25,215.59) and (218.29,212.76) .. (203.46,213.36) .. controls (187.54,213.99) and (173.06,216.26) .. (160.17,215.83) .. controls (142.27,215.23) and (128.57,211.18) .. (128.47,206.06) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 65; green, 62; blue, 62 }  ,fill opacity=0.08 ] (149.49,202.35) .. controls (155.71,199.24) and (166.4,197.14) .. (184.29,194.8) .. controls (197.41,193.09) and (215.44,193.96) .. (230.67,192.95) .. controls (245.28,191.97) and (261.78,191.57) .. (274.58,191.71) .. controls (302.64,192.02) and (320.61,192.39) .. (311.03,201.98) .. controls (302.1,204.15) and (286.31,209.52) .. (267.78,210.88) .. controls (254.27,211.88) and (239.31,209.05) .. (224.49,209.64) .. controls (208.56,210.28) and (194.09,212.55) .. (181.2,212.12) .. controls (163.3,211.52) and (149.59,207.47) .. (149.49,202.35) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 65; green, 62; blue, 62 }  ,fill opacity=0.08 ] (119.19,203.58) .. controls (125.41,200.47) and (136.09,198.38) .. (153.99,196.04) .. controls (167.1,194.32) and (185.14,195.2) .. (200.37,194.18) .. controls (214.98,193.21) and (231.47,192.8) .. (244.28,192.95) .. controls (272.34,193.26) and (290.31,193.63) .. (280.73,203.21) .. controls (271.79,205.39) and (256,210.75) .. (237.48,212.12) .. controls (223.97,213.11) and (209.01,210.29) .. (194.19,210.88) .. controls (178.26,211.52) and (163.79,213.79) .. (150.89,213.36) .. controls (133,212.75) and (119.29,208.7) .. (119.19,203.58) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.14 ][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (209.37,71.91) .. controls (209.37,70.57) and (210.46,69.48) .. (211.8,69.48) .. controls (213.15,69.48) and (214.23,70.57) .. (214.23,71.91) .. controls (214.23,73.26) and (213.15,74.34) .. (211.8,74.34) .. controls (210.46,74.34) and (209.37,73.26) .. (209.37,71.91) -- cycle ;
            \end{tikzpicture}'''

                # Câu hỏi
                noidungcauhoi = (r'''\immini{Một thiết bị lặn không người lái được thả xuống nước để thực hiện khảo sát. Vận tốc di chuyển theo phương thẳng đứng của thiết bị được mô tả bởi hàm $v(t)=%s$ (m/phút). Trong đó $t$ là thời gian tính bằng phút kể từ lúc bắt đầu lặn. Quy ước vận tốc dương $\left(v>0\right)$ ứng với chuyển động đi xuống, vận tốc âm $\left(v<0\right)$ ứng với chuyển động đi lên. Độ sâu lớn nhất mà thiết bị đạt được trong quá trình khảo sát là bao nhiêu mét? (Kết quả làm tròn đến hàng phần mười).}{%s}'''
                                 % (func_str,hinhve))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Thiết bị đạt độ sâu lớn nhất khi vận tốc đổi chiều từ đi xuống (vận tốc dương) sang đi lên (vận tốc âm). \\\\
                           Ta có $v(t)=0 \\Leftrightarrow %s = 0 \\Rightarrow t = \\sqrt{%s}$ (do $t \\ge 0$). \\\\
                           Với $0 \\le t < \\sqrt{%s}$ thì $v(t) > 0$, thiết bị chuyển động đi xuống.\\\\
                           Với $t > \\sqrt{%s}$ thì $v(t) < 0$, thiết bị chuyển động đi lên.\\\\
                           Độ sâu lớn nhất mà thiết bị đạt được là quãng đường thiết bị đi được từ thời điểm $t=0$ đến thời điểm $t=\\sqrt{%s}$.\\\\
                           Ta có: $h = \\int\\limits_0^{\\sqrt{%s}} v(t) \\mathrm{\\,d}t = \\int\\limits_0^{\\sqrt{%s}} \\left[%s\\right] \\mathrm{\\,d}t \\approx %s$ (m).'''
                           % (func_str, a, a, a, a, a, a, func_str, kq))
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content


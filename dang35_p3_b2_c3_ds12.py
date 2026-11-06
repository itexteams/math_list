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


def bt_dang35_p3_b2_c3_ds12(self):
            # Khai báo biến
            # B3: Suy nghĩ tìm cách random bài toán
            # Tạo các bộ tham số sao cho thời gian, vận tốc, và các hệ số tích phân ra số nguyên đẹp
            params_list = [
                {
                    'a': '0,04', 'b': '1,2', 't1': 20, 't2': 100,
                    'v_max': 160, 'S1': 1600, 'S2': 16000,
                    'v3_tex': '160 - \\frac{1}{6}t^2', 'v_end3': 10, 't3': 30, 'S3': 3300,
                    'v4_tex': '10 - 2t', 't4': 5, 'S4': 25,
                    'ans_m': 20925, 'ans_km': 20.925, 'ans_round': '20,9',
                    'v3_eq': '160 - \\frac{1}{6}t^2 = 10 \\Rightarrow \\frac{1}{6}t^2 = 150 \\Rightarrow t^2 = 900',
                    'v4_eq': '10 - 2t = 0'
                },
                {
                    'a': '0,02', 'b': '0,6', 't1': 20, 't2': 120,
                    'v_max': 80, 'S1': 800, 'S2': 9600,
                    'v3_tex': '80 - \\frac{1}{12}t^2', 'v_end3': 5, 't3': 30, 'S3': 1650,
                    'v4_tex': '5 - t', 't4': 5, 'S4': 12.5,
                    'ans_m': 12062.5, 'ans_km': 12.0625, 'ans_round': '12,1',
                    'v3_eq': '80 - \\frac{1}{12}t^2 = 5 \\Rightarrow \\frac{1}{12}t^2 = 75 \\Rightarrow t^2 = 900',
                    'v4_eq': '5 - t = 0'
                },
                {
                    'a': '0,08', 'b': '2,4', 't1': 20, 't2': 80,
                    'v_max': 320, 'S1': 3200, 'S2': 25600,
                    'v3_tex': '320 - \\frac{1}{3}t^2', 'v_end3': 20, 't3': 30, 'S3': 6600,
                    'v4_tex': '20 - 4t', 't4': 5, 'S4': 50,
                    'ans_m': 35450, 'ans_km': 35.45, 'ans_round': '35,5',
                    'v3_eq': '320 - \\frac{1}{3}t^2 = 20 \\Rightarrow \\frac{1}{3}t^2 = 300 \\Rightarrow t^2 = 900',
                    'v4_eq': '20 - 4t = 0'
                },
                {
                    'a': '0,04', 'b': '1,2', 't1': 20, 't2': 150,
                    'v_max': 160, 'S1': 1600, 'S2': 24000,
                    'v3_tex': '160 - \\frac{1}{6}t^2', 'v_end3': 10, 't3': 30, 'S3': 3300,
                    'v4_tex': '10 - 2t', 't4': 5, 'S4': 25,
                    'ans_m': 28925, 'ans_km': 28.925, 'ans_round': '28,9',
                    'v3_eq': '160 - \\frac{1}{6}t^2 = 10 \\Rightarrow \\frac{1}{6}t^2 = 150 \\Rightarrow t^2 = 900',
                    'v4_eq': '10 - 2t = 0'
                }
            ]

            # Chọn ngẫu nhiên 1 cấu hình bài toán
            p = random.choice(params_list)

            # Đảm bảo số thập phân làm tròn chính xác và hiển thị dấu phẩy
            kq_num = round(p['ans_km'], 1)
            kq = str(kq_num).replace('.', ',')

            du = ['$%s$' % (kq)]
            da = random.choice(du)

            # B4: Điều chỉnh các phương án sai không được phép trùng với đáp án đúng
            sai_options = [
                round(kq_num + 0.1, 1),
                round(kq_num - 0.1, 1),
                round(kq_num + 1.0, 1),
                round(kq_num - 1.0, 1),
                round(kq_num + 0.5, 1),
                round(kq_num - 0.5, 1)
            ]

            s = []
            for val in sai_options:
                val_str = str(val).replace('.', ',')
                # Kiểm tra điều kiện loại trừ trùng đáp án đúng
                if val_str != kq:
                    s.append('$%s$' % val_str)

            das1 = random.choice(s)
            s.remove(das1)
            das2 = random.choice(s)
            s.remove(das2)
            das3 = random.choice(s)

            hinhve=r'''\begin{center} \tikzset{every picture/.style={line width=0.75pt}} 
            \begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-0.7,xscale=0.7]
            	\draw  [draw opacity=0][fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ] (46.53,184.13) -- (476.07,114.72) -- (47.2,274.27) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (46.53,184.13) -- (476.07,114.72) -- (218.53,202.93) -- cycle ;
            	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (257.98,153.92) -- (316.53,157.39) -- (169.71,194.8) -- (169.74,173.13) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (169.74,173.13) -- (179.81,171) -- (221.58,181.77) -- (212.47,183.9) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (189.88,168.72) -- (199.04,166.68) -- (241.72,177.36) -- (232.61,179.49) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (208.35,164.66) -- (217.51,162.82) -- (259.47,173.46) -- (251.07,175.43) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (228.25,160.4) -- (236.45,158.37) -- (279.13,169.59) -- (270.98,171.17) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (247,156.24) -- (256.59,154.11) -- (299.03,164.94) -- (291.12,166.68) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (169.73,183.97) -- (169.55,179.45) -- (200.2,187.22) -- (191.09,189.35) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (169.71,194.8) -- (169.55,190.29) -- (178.82,192.67) -- (169.71,194.8) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (263.3,151.59) -- (272.89,149.47) -- (315.33,160.3) -- (307.42,162.04) -- cycle ;
            	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (138.75,185.45) -- (199.8,189.93) -- (46.72,238.28) -- (46.75,210.28) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (46.75,210.28) -- (57.25,207.53) -- (100.8,221.45) -- (91.3,224.2) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (67.75,204.58) -- (77.3,201.95) -- (121.8,215.75) -- (112.3,218.5) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (87,199.33) -- (96.55,196.95) -- (140.3,210.7) -- (131.55,213.25) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (107.75,193.83) -- (116.3,191.2) -- (160.8,205.7) -- (152.3,207.75) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (127.3,188.45) -- (137.3,185.7) -- (181.55,199.7) -- (173.3,201.95) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (46.73,224.28) -- (46.55,218.45) -- (78.51,228.49) -- (69.01,231.24) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (46.72,238.28) -- (46.55,232.45) -- (56.22,235.53) -- (46.72,238.28) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (144.3,182.45) -- (154.3,179.7) -- (198.55,193.7) -- (190.3,195.95) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (199.55,190.68) -- (46.47,239.03) -- (46.32,235.78) -- (183.32,193.53) -- cycle ;
            	\draw  [fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (213.5,177.7) -- (46.3,227.2) -- (46,224.28) -- (164,189.2) -- cycle ;
            	\draw  [fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (134.25,183.03) -- (138.5,186.2) -- (46.5,211.03) -- (46.5,206.28) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (172.93,186.33) -- (46,224.28) -- (45.85,221.03) -- (168.68,186.08) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (138.18,181.75) -- (46.5,206.28) -- (46.35,203.03) -- (135.18,181) -- cycle ;
            	\draw  [fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (46.97,257.28) -- (46.47,239.03) -- (443.55,115.68) -- cycle ;
            	\draw  [fill={rgb, 255:red, 173; green, 203; blue, 234 }  ,fill opacity=1 ] (181.43,101.05) .. controls (207.53,88.88) and (242.61,92.86) .. (288.05,97.99) .. controls (333.49,103.11) and (486.97,108.8) .. (474.07,114.05) .. controls (461.16,119.3) and (285.05,163.39) .. (265.11,170.11) .. controls (245.17,176.83) and (147.95,214.72) .. (132.2,193.02) .. controls (116.44,171.32) and (137.72,151.24) .. (144.21,141.78) .. controls (150.69,132.32) and (155.32,113.23) .. (181.43,101.05) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.71 ] (208.08,104.52) .. controls (227.88,94.13) and (256.88,93.57) .. (242.62,106.35) .. controls (228.37,119.13) and (231.04,112.68) .. (209.56,129) .. controls (188.07,145.31) and (172.83,169.21) .. (146.29,167.73) .. controls (119.76,166.24) and (188.28,114.9) .. (208.08,104.52) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (210.92,112.22) .. controls (209.39,116.1) and (206.46,120.48) .. (202.15,125) .. controls (189.21,138.58) and (168.72,148.33) .. (156.4,146.79) .. controls (146.73,145.58) and (144.95,137.77) .. (150.88,127.91) -- (179.83,122.2) -- cycle ; \draw   (210.92,112.22) .. controls (209.39,116.1) and (206.46,120.48) .. (202.15,125) .. controls (189.21,138.58) and (168.72,148.33) .. (156.4,146.79) .. controls (146.73,145.58) and (144.95,137.77) .. (150.88,127.91) ;  
            	\draw  [fill={rgb, 255:red, 62; green, 85; blue, 113 }  ,fill opacity=1 ] (151.15,135.4) .. controls (146.91,128.01) and (157.99,113.69) .. (175.89,103.4) .. controls (193.79,93.11) and (211.74,90.75) .. (215.99,98.13) .. controls (220.23,105.51) and (209.16,119.84) .. (191.25,130.13) .. controls (173.35,140.42) and (155.4,142.78) .. (151.15,135.4) -- cycle ;
            	\draw  [fill={rgb, 255:red, 26; green, 43; blue, 60 }  ,fill opacity=1 ] (154.85,121.47) .. controls (160.04,113.98) and (171.79,101.14) .. (186.53,104.52) .. controls (201.26,107.9) and (214.57,106.64) .. (201.17,120.57) .. controls (187.77,134.5) and (176.26,134.5) .. (164.39,132.29) .. controls (152.53,130.08) and (149.66,128.96) .. (154.85,121.47) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 139; green, 162; blue, 184 }  ,fill opacity=0.67 ] (188.58,107.48) -- (205.33,111.16) -- (187.91,129.53) -- (182.94,131.29) -- (200.02,112.59) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 172; green, 193; blue, 218 }  ,fill opacity=0.59 ] (168.28,109.21) -- (171.27,108.48) -- (156.67,129.44) -- (156.27,125.78) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 184; green, 208; blue, 237 }  ,fill opacity=0.4 ] (215.99,98.13) .. controls (223.46,94.21) and (209.15,89.26) .. (192.09,99.08) .. controls (175.03,108.89) and (190.11,95.6) .. (176.64,110.38) .. controls (163.17,125.16) and (154.5,148.99) .. (166.7,135.43) .. controls (178.91,121.86) and (189.17,112.72) .. (197.79,107.66) .. controls (206.4,102.61) and (208.52,102.05) .. (215.99,98.13) -- cycle ;
            	\draw  [fill={rgb, 255:red, 18; green, 39; blue, 64 }  ,fill opacity=1 ] (268.52,131.5) .. controls (271.76,129.8) and (237.33,135.11) .. (219.45,141.46) .. controls (201.57,147.8) and (196.99,154.43) .. (205.25,143.98) .. controls (213.5,133.54) and (215.39,129.99) .. (226.8,120.81) .. controls (238.21,111.63) and (243.15,112.74) .. (250.38,111.6) .. controls (257.61,110.46) and (265.35,110.31) .. (266.66,113.04) .. controls (267.96,115.76) and (265.27,133.2) .. (268.52,131.5) -- cycle ;
            	\draw  [fill={rgb, 255:red, 62; green, 92; blue, 125 }  ,fill opacity=0.58 ] (260.17,126.91) .. controls (260.98,129.9) and (246.68,127.18) .. (228.8,133.52) .. controls (210.92,139.87) and (210.08,146.17) .. (218.34,135.73) .. controls (226.6,125.28) and (222.49,130.39) .. (230.6,123.24) .. controls (238.71,116.08) and (244.49,117.47) .. (251.72,116.33) .. controls (258.95,115.19) and (258.45,115.2) .. (259.75,117.92) .. controls (261.05,120.65) and (259.37,123.93) .. (260.17,126.91) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 121; green, 154; blue, 193 }  ,fill opacity=0.46 ] (242.24,117.76) -- (248.47,116.39) -- (241.98,130.02) -- (234.76,131.66) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 217; green, 228; blue, 242 }  ,fill opacity=0.46 ] (254.97,116.51) -- (259.2,115.18) -- (252.71,128.81) -- (249.96,128.86) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 217; green, 228; blue, 242 }  ,fill opacity=0.46 ] (259.23,116.68) -- (260.07,121.42) -- (256.7,128.48) -- (253.71,128.79) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 87; green, 125; blue, 166 }  ,fill opacity=1 ] (470.19,112.94) -- (474.07,114.05) -- (267.03,132.13) -- (265.88,111.65) -- cycle ;
            	\draw  [fill={rgb, 255:red, 54; green, 80; blue, 109 }  ,fill opacity=1 ] (337.36,112.98) -- (337.85,125.27) -- (294.07,129.26) -- (293.26,112.87) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 92; green, 120; blue, 150 }  ,fill opacity=1 ] (305.15,119.39) -- (305.54,126.86) -- (299.43,127.71) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 84; green, 115; blue, 143 }  ,fill opacity=1 ] (312.39,113.71) -- (315.58,114.13) -- (311.17,126.76) -- (307.74,126.58) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 84; green, 115; blue, 143 }  ,fill opacity=1 ] (316.57,114.59) -- (316.95,121.58) -- (316.04,125.21) -- (312.63,126.49) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 84; green, 115; blue, 143 }  ,fill opacity=1 ] (324.14,113.48) -- (327.34,113.9) -- (322.93,126.53) -- (319.49,126.35) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 84; green, 115; blue, 143 }  ,fill opacity=1 ] (328.33,114.36) -- (328.71,121.35) -- (327.8,124.99) -- (324.39,126.26) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 84; green, 115; blue, 143 }  ,fill opacity=1 ] (334.17,112.56) -- (337.36,112.98) -- (332.95,125.61) -- (329.52,125.44) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 84; green, 115; blue, 143 }  ,fill opacity=1 ] (336.67,115.17) -- (337.05,122.15) -- (336.14,125.79) -- (332.74,127.06) -- cycle ;
            	\draw [color={rgb, 255:red, 24; green, 41; blue, 61 }  ,draw opacity=1 ][line width=1.5]    (293.26,112.87) -- (337.36,112.98) ;
            	\draw [color={rgb, 255:red, 24; green, 41; blue, 61 }  ,draw opacity=1 ][line width=1.5]    (294.07,129.26) -- (337.85,125.27) ;
            	\draw [color={rgb, 255:red, 24; green, 41; blue, 61 }  ,draw opacity=1 ][line width=0.75]    (305.76,113.35) -- (306.76,126.6) ;
            	\draw [color={rgb, 255:red, 24; green, 41; blue, 61 }  ,draw opacity=1 ][line width=0.75]    (317.28,113.37) -- (318.27,126.62) ;
            	\draw [color={rgb, 255:red, 24; green, 41; blue, 61 }  ,draw opacity=1 ][line width=0.75]    (328.55,113.15) -- (329.52,125.44) ;
            	\draw  [fill={rgb, 255:red, 54; green, 80; blue, 109 }  ,fill opacity=1 ] (381.75,113.27) -- (382.04,121.15) -- (358.74,123.6) -- (358.28,113.11) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 92; green, 120; blue, 150 }  ,fill opacity=1 ] (364.62,117.31) -- (364.84,122.1) -- (361.59,122.62) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 84; green, 115; blue, 143 }  ,fill opacity=1 ] (368.46,113.69) -- (370.16,113.96) -- (367.84,122.04) -- (366.01,121.92) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 84; green, 115; blue, 143 }  ,fill opacity=1 ] (370.69,114.26) -- (370.9,118.74) -- (370.43,121.06) -- (368.62,121.87) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 84; green, 115; blue, 143 }  ,fill opacity=1 ] (374.72,113.56) -- (376.42,113.84) -- (374.1,121.92) -- (372.27,121.8) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 84; green, 115; blue, 143 }  ,fill opacity=1 ] (376.94,114.14) -- (377.16,118.61) -- (376.68,120.94) -- (374.87,121.75) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 84; green, 115; blue, 143 }  ,fill opacity=1 ] (380.05,113) -- (381.75,113.27) -- (379.43,121.35) -- (377.6,121.23) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 84; green, 115; blue, 143 }  ,fill opacity=1 ] (381.39,114.67) -- (381.61,119.15) -- (381.13,121.47) -- (379.32,122.28) -- cycle ;
            	\draw [color={rgb, 255:red, 24; green, 41; blue, 61 }  ,draw opacity=1 ][line width=1.5]    (358.28,113.11) -- (381.75,113.27) ;
            	\draw [color={rgb, 255:red, 24; green, 41; blue, 61 }  ,draw opacity=1 ][line width=1.5]    (358.74,123.6) -- (382.04,121.15) ;
            	\draw [color={rgb, 255:red, 24; green, 41; blue, 61 }  ,draw opacity=1 ][line width=0.75]    (364.93,113.45) -- (365.49,121.93) ;
            	\draw [color={rgb, 255:red, 24; green, 41; blue, 61 }  ,draw opacity=1 ][line width=0.75]    (371.06,113.48) -- (371.62,121.96) ;
            	\draw [color={rgb, 255:red, 24; green, 41; blue, 61 }  ,draw opacity=1 ][line width=0.75]    (377.06,113.37) -- (377.6,121.23) ;
            	\draw  [fill={rgb, 255:red, 54; green, 80; blue, 109 }  ,fill opacity=1 ] (396.59,113.34) -- (396.75,119.34) -- (388.53,121.03) -- (388.28,113.03) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 92; green, 120; blue, 150 }  ,fill opacity=1 ] (390.56,116.28) -- (390.67,119.93) -- (389.53,120.3) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 84; green, 115; blue, 143 }  ,fill opacity=1 ] (391.89,113.55) -- (392.49,113.77) -- (391.74,119.91) -- (391.09,119.8) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 84; green, 115; blue, 143 }  ,fill opacity=1 ] (392.68,114) -- (392.79,117.41) -- (392.64,119.18) -- (392.01,119.78) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 84; green, 115; blue, 143 }  ,fill opacity=1 ] (394.1,113.51) -- (394.71,113.73) -- (393.95,119.86) -- (393.3,119.76) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 84; green, 115; blue, 143 }  ,fill opacity=1 ] (394.9,113.96) -- (395.01,117.37) -- (394.86,119.14) -- (394.22,119.74) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 84; green, 115; blue, 143 }  ,fill opacity=1 ] (395.99,113.12) -- (396.59,113.34) -- (395.83,119.47) -- (395.19,119.37) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 84; green, 115; blue, 143 }  ,fill opacity=1 ] (396.47,114.4) -- (396.59,117.81) -- (396.44,119.58) -- (395.8,120.18) -- cycle ;
            	\draw [color={rgb, 255:red, 24; green, 41; blue, 61 }  ,draw opacity=1 ][line width=1.5]    (388.28,113.03) -- (396.59,113.34) ;
            	\draw [color={rgb, 255:red, 24; green, 41; blue, 61 }  ,draw opacity=1 ][line width=1.5]    (388.53,121.03) -- (396.75,119.34) ;
            	\draw [color={rgb, 255:red, 24; green, 41; blue, 61 }  ,draw opacity=1 ][line width=0.75]    (390.64,113.34) -- (390.9,119.8) ;
            	\draw [color={rgb, 255:red, 24; green, 41; blue, 61 }  ,draw opacity=1 ][line width=0.75]    (392.81,113.41) -- (393.07,119.88) ;
            	\draw [color={rgb, 255:red, 24; green, 41; blue, 61 }  ,draw opacity=1 ][line width=0.75]    (394.93,113.37) -- (395.19,119.37) ;
            	\draw  [fill={rgb, 255:red, 54; green, 80; blue, 109 }  ,fill opacity=1 ] (414.8,113.19) -- (414.99,118.63) -- (400.09,120.3) -- (399.78,113.06) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 92; green, 120; blue, 150 }  ,fill opacity=1 ] (403.84,115.96) -- (403.99,119.27) -- (401.91,119.63) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 84; green, 115; blue, 143 }  ,fill opacity=1 ] (406.3,113.46) -- (407.39,113.66) -- (405.91,119.23) -- (404.74,119.15) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 84; green, 115; blue, 143 }  ,fill opacity=1 ] (407.72,113.86) -- (407.87,116.95) -- (407.57,118.56) -- (406.41,119.11) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 84; green, 115; blue, 143 }  ,fill opacity=1 ] (410.3,113.39) -- (411.39,113.58) -- (409.91,119.15) -- (408.74,119.07) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 84; green, 115; blue, 143 }  ,fill opacity=1 ] (411.73,113.79) -- (411.87,116.88) -- (411.57,118.48) -- (410.41,119.04) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 84; green, 115; blue, 143 }  ,fill opacity=1 ] (413.72,113) -- (414.8,113.19) -- (413.33,118.77) -- (412.16,118.68) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 84; green, 115; blue, 143 }  ,fill opacity=1 ] (414.57,114.16) -- (414.72,117.25) -- (414.41,118.85) -- (413.26,119.41) -- cycle ;
            	\draw [color={rgb, 255:red, 24; green, 41; blue, 61 }  ,draw opacity=1 ][line width=1.5]    (399.78,113.06) -- (414.8,113.19) ;
            	\draw [color={rgb, 255:red, 24; green, 41; blue, 61 }  ,draw opacity=1 ][line width=1.5]    (400.09,120.3) -- (414.99,118.63) ;
            	\draw [color={rgb, 255:red, 24; green, 41; blue, 61 }  ,draw opacity=1 ][line width=0.75]    (404.04,113.29) -- (404.41,119.15) ;
            	\draw [color={rgb, 255:red, 24; green, 41; blue, 61 }  ,draw opacity=1 ][line width=0.75]    (407.96,113.33) -- (408.33,119.18) ;
            	\draw [color={rgb, 255:red, 24; green, 41; blue, 61 }  ,draw opacity=1 ][line width=0.75]    (411.8,113.25) -- (412.16,118.68) ;
            	\draw  [fill={rgb, 255:red, 54; green, 80; blue, 109 }  ,fill opacity=1 ] (436.05,112.91) -- (436.21,116.85) -- (420.56,118.16) -- (420.28,112.91) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 92; green, 120; blue, 150 }  ,fill opacity=1 ] (424.53,114.99) -- (424.66,117.38) -- (422.48,117.66) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 84; green, 115; blue, 143 }  ,fill opacity=1 ] (427.12,113.16) -- (428.26,113.3) -- (426.68,117.34) -- (425.45,117.29) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 84; green, 115; blue, 143 }  ,fill opacity=1 ] (428.61,113.44) -- (428.75,115.68) -- (428.42,116.85) -- (427.2,117.25) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 84; green, 115; blue, 143 }  ,fill opacity=1 ] (431.32,113.08) -- (432.46,113.21) -- (430.88,117.26) -- (429.65,117.21) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 84; green, 115; blue, 143 }  ,fill opacity=1 ] (432.82,113.36) -- (432.95,115.6) -- (432.62,116.76) -- (431.4,117.17) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 84; green, 115; blue, 143 }  ,fill opacity=1 ] (434.91,112.78) -- (436.05,112.91) -- (434.46,116.96) -- (433.24,116.91) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 84; green, 115; blue, 143 }  ,fill opacity=1 ] (435.8,113.61) -- (435.93,115.85) -- (435.6,117.01) -- (434.38,117.42) -- cycle ;
            	\draw [color={rgb, 255:red, 24; green, 41; blue, 61 }  ,draw opacity=1 ][line width=1.5]    (420.28,112.91) -- (436.05,112.91) ;
            	\draw [color={rgb, 255:red, 24; green, 41; blue, 61 }  ,draw opacity=1 ][line width=1.5]    (420.56,118.16) -- (436.21,116.85) ;
            	\draw [color={rgb, 255:red, 24; green, 41; blue, 61 }  ,draw opacity=1 ][line width=0.75]    (424.75,113.06) -- (425.1,117.3) ;
            	\draw [color={rgb, 255:red, 24; green, 41; blue, 61 }  ,draw opacity=1 ][line width=0.75]    (428.87,113.05) -- (429.21,117.29) ;
            	\draw [color={rgb, 255:red, 24; green, 41; blue, 61 }  ,draw opacity=1 ][line width=0.75]    (432.9,112.97) -- (433.24,116.91) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 167; green, 191; blue, 220 }  ,fill opacity=0.6 ] (274.34,111.99) -- (283.1,112.32) -- (274.46,131.24) -- (269.97,131.83) -- (270.5,120.56) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 131; green, 162; blue, 200 }  ,fill opacity=1 ] (278.38,127.16) -- (283.2,117.82) -- (282.7,130.58) -- (277.96,130.92) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 131; green, 162; blue, 200 }  ,fill opacity=1 ] (347.14,113.83) -- (349.89,113.77) -- (350.06,122.77) -- (347.56,122.57) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 131; green, 162; blue, 200 }  ,fill opacity=1 ] (351.38,113.49) -- (354.13,113.44) -- (354.31,122.44) -- (351.8,122.24) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 131; green, 162; blue, 200 }  ,fill opacity=1 ] (381.75,113.27) -- (384.5,113.22) -- (384.68,122.22) -- (382.17,122.02) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 131; green, 162; blue, 200 }  ,fill opacity=1 ] (356.64,113.89) -- (356.64,113.89) -- (356.81,122.89) -- (355.55,122.17) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (216.96,144.6) .. controls (236.76,134.22) and (272.52,131.74) .. (317,129.25) .. controls (361.47,126.75) and (422.55,115.98) .. (442.26,119.49) .. controls (461.98,122.99) and (443.16,117) .. (417.27,120.22) .. controls (391.39,123.44) and (252.53,140.2) .. (243.12,142.1) .. controls (233.7,144) and (213.77,150.17) .. (186.47,160.95) .. controls (159.17,171.73) and (197.16,154.99) .. (216.96,144.6) -- cycle ;
            	\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ]   (192.17,160.84) .. controls (206.56,155.06) and (213.3,151.64) .. (230.42,147.59) .. controls (247.54,143.55) and (260.13,142.71) .. (287.06,138.75) .. controls (313.99,134.78) and (441.92,116.97) .. (452.67,117.28) ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.32 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (170.39,147.99) .. controls (173.77,145.57) and (177.62,145.16) .. (178.99,147.08) .. controls (180.36,148.99) and (178.73,152.5) .. (175.35,154.92) .. controls (171.98,157.33) and (168.13,157.74) .. (166.76,155.82) .. controls (165.39,153.91) and (167.02,150.4) .. (170.39,147.99) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.32 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (140.9,148.8) .. controls (140.96,146.38) and (142.13,144.45) .. (143.5,144.48) .. controls (144.87,144.52) and (145.93,146.51) .. (145.87,148.93) .. controls (145.81,151.35) and (144.65,153.29) .. (143.27,153.25) .. controls (141.9,153.21) and (140.84,151.22) .. (140.9,148.8) -- cycle ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.24 ]   (142.78,192.8) .. controls (135.54,180.44) and (131.91,174.01) .. (154.9,147.06) ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.26 ] (127.57,171.12) .. controls (129.19,162.54) and (141.98,157.75) .. (156.15,160.41) .. controls (170.32,163.07) and (180.51,172.18) .. (178.89,180.76) .. controls (177.28,189.34) and (164.49,194.13) .. (150.32,191.47) .. controls (136.14,188.81) and (125.96,179.7) .. (127.57,171.12) -- cycle ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.24 ]   (259.3,120.43) .. controls (260.3,115.51) and (268.55,102.25) .. (252.9,94.65) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.24 ]   (271.83,168.3) .. controls (271.12,105.8) and (277.55,102.17) .. (260.9,94.49) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.24 ]   (279.29,166.15) .. controls (278.58,103.65) and (285.58,103.52) .. (268.92,95.84) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.24 ]   (287.74,163.49) .. controls (287.03,100.99) and (295.09,104.33) .. (278.44,96.65) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.24 ]   (342.47,148.92) .. controls (343.3,114.4) and (347.1,104.33) .. (339.07,102.48) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.24 ]   (347.42,146.33) .. controls (348.25,111.81) and (352.61,104.72) .. (344.57,102.87) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.24 ]   (354.41,145.69) .. controls (355.24,111.17) and (359.11,104.59) .. (351.07,102.75) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.18 ]   (216.18,161.37) -- (459.36,116.65) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.18 ]   (212.92,173.44) -- (470.19,112.94) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.24 ]   (187.26,191.44) .. controls (208.13,184.43) and (220.04,179.8) .. (213.63,158.42) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 50; green, 77; blue, 108 }  ,fill opacity=1 ] (265.26,164.92) -- (474.07,114.05) -- (256.41,172.6) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 36; green, 61; blue, 91 }  ,fill opacity=1 ] (286.05,154.02) -- (300.99,150.73) -- (295.65,158.83) -- (283.2,161.57) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 36; green, 61; blue, 91 }  ,fill opacity=1 ] (326.62,146.48) -- (333.89,145.09) -- (331.02,151.65) -- (323.76,154.04) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 36; green, 61; blue, 91 }  ,fill opacity=1 ] (358.05,140.12) -- (364.52,138.5) -- (363.12,143.52) -- (356.64,144.65) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 36; green, 61; blue, 91 }  ,fill opacity=1 ] (387.91,132.54) -- (391.16,132.48) -- (389.98,136) -- (386.5,137.07) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 36; green, 61; blue, 91 }  ,fill opacity=1 ] (403.09,129) -- (406.34,128.93) -- (405.16,132.46) -- (401.68,133.52) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 36; green, 61; blue, 91 }  ,fill opacity=1 ] (414.79,126.27) -- (418.04,126.21) -- (416.86,129.73) -- (413.38,130.8) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 42; green, 72; blue, 108 }  ,fill opacity=1 ] (254.88,164.14) -- (250.69,175.03) -- (206.56,189.08) -- (223.81,171.15) -- cycle ;
            	\draw  [color={rgb, 255:red, 22; green, 42; blue, 67 }  ,draw opacity=1 ] (233.14,169.62) .. controls (233.26,170.29) and (233.33,170.98) .. (233.36,171.69) .. controls (233.61,177.98) and (230.02,183.23) .. (225.34,183.42) .. controls (222.28,183.54) and (219.52,181.46) .. (217.9,178.25) -- (219.33,176.97) .. controls (220.59,179.8) and (222.81,181.66) .. (225.27,181.56) .. controls (228.92,181.41) and (231.71,177.03) .. (231.5,171.76) .. controls (231.48,171.21) and (231.43,170.67) .. (231.34,170.14) -- cycle ;
            	\draw  [color={rgb, 255:red, 22; green, 42; blue, 67 }  ,draw opacity=1 ] (248.83,165.96) .. controls (248.74,171.87) and (245.27,176.67) .. (240.8,176.85) .. controls (237.74,176.97) and (234.98,174.9) .. (233.36,171.69) -- (234.79,170.41) .. controls (236.05,173.24) and (238.27,175.09) .. (240.73,175) .. controls (244.23,174.86) and (246.94,170.82) .. (246.97,165.85) -- cycle ;
            	\draw [line width=0.75]    (132.2,193.02) .. controls (145.43,200.75) and (158.92,199.79) .. (206.56,189.08) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.27 ]   (163.15,170.6) .. controls (188.82,168.65) and (196.77,165.75) .. (226.12,158.18) ;
            \end{tikzpicture} \end{center}'''

            # Nội dung câu hỏi (Không dùng raw string, quy đổi ngoặc đơn chuẩn LaTeX)
            noidungcauhoi = ('Một đoàn tàu đệm từ trường (Maglev) bắt đầu chuyển chạy thử nghiệm trên tuyến đường ray mới. Khi vừa rời ga, hệ thống động lực đẩy tàu tăng tốc êm ái, vận tốc của tàu thay đổi theo quy luật $v\\left(t\\right) = -%st^3 + %st^2$ (m/s) trong đúng $%s$ giây đầu tiên. Ngay khi đạt đến ngưỡng vận tốc tối đa ở cuối khoảng thời gian này, hệ thống tự động chuyển sang chế độ hành trình, duy trì cho tàu lướt đi với vận tốc không đổi trong suốt $%s$ giây tiếp theo. Khi tiến gần đến trạm đích, '
                             'hệ thống đệm từ bắt đầu can thiệp để hãm tốc độ, làm vận tốc của tàu giảm dần theo phương trình $v\\left(t\\right) = %s$ (m/s) (với $t$ là thời gian tính bằng giây kể từ lúc bắt đầu hãm). %s Hệ thống tiếp tục theo dõi cho đến khi vận tốc giảm xuống chỉ còn $%s$ (m/s). Lúc này, để đảm bảo dừng chính xác tại sân ga, hệ thống phanh cơ học được kích hoạt, tạo ra lực cản làm vận tốc giảm đều đặn theo công thức $v\\left(t\\right) = %s$ (m/s) (với $t$ tính từ lúc kích hoạt phanh cơ học) cho đến khi đoàn tàu đứng im hoàn toàn. Tổng chiều dài quãng đường mà đoàn tàu Maglev đã di chuyển trong toàn bộ chuyến thử nghiệm trên là bao nhiêu km? (Kết quả làm tròn đến hàng phần chục).'
                             % (p['a'], p['b'], p['t1'], p['t2'], p['v3_tex'], hinhve, p['v_end3'], p['v4_tex']))

            # Các đáp án
            da_d = ('\\True ' + str(da))
            da_s1 = str(das1)
            da_s2 = str(das2)
            da_s3 = str(das3)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Nội dung lời giải (Giải chi tiết không viết tắt, định dạng lại dấu ngoặc)
            loigiai = ('Chia quá trình chuyển động của tàu thành 4 giai đoạn:\\\\'
                       '+ Giai đoạn 1 (Tăng tốc): Quãng đường tàu đi được trong $%s$ giây đầu là \\\\'
                       '$S_1 = \\int_{0}^{%s} \\left(-%st^3 + %st^2\\right) \\text{d}t = %s$ (m). \\\\'
                       'Vận tốc tối đa tàu đạt được tại $t = %s$ là: $v_{max} = -%s \\cdot %s^3 + %s \\cdot %s^2 = %s$ (m/s). \\\\'
                       '+ Giai đoạn 2 (Hành trình): Tàu chạy với vận tốc không đổi $v = %s$ (m/s) trong $%s$ giây. \\\\'
                       'Quãng đường tàu đi được là: $S_2 = %s \\cdot %s = %s$ (m). \\\\'
                       '+ Giai đoạn 3 (Đệm từ hãm tốc): Thời gian đệm từ hãm tốc từ $%s$ (m/s) xuống $%s$ (m/s) thỏa mãn \\\\'
                       '$%s \\Rightarrow t = %s$ (s). \\\\\n'
                       'Quãng đường đi được trong giai đoạn này là: $S_3 = \\int_{0}^{%s} \\left(%s\\right) \\text{d}t = %s$ (m). \\\\'
                       '+ Giai đoạn 4 (Phanh cơ học): Thời gian phanh cơ học từ $%s$ (m/s) đến khi dừng hẳn $\\left(v=0\\right)$ thỏa mãn \\\\'
                       '$%s \\Rightarrow t = %s$ (s). \\\\'
                       'Quãng đường đi được là: $S_4 = \\int_{0}^{%s} \\left(%s\\right) \\text{d}t = %s$ (m). \\\\'
                       '+ Tổng quãng đường tàu đã di chuyển là: \\\\'
                       '$S = S_1 + S_2 + S_3 + S_4 = %s + %s + %s + %s = %s$ (m) $= %s$ (km). \\\\'
                       'Làm tròn đến hàng phần chục, ta được kết quả là $%s$ (km).'
                       % (p['t1'],
                          p['t1'], p['a'], p['b'], str(p['S1']).replace('.', ','),
                          p['t1'], p['a'], p['t1'], p['b'], p['t1'], p['v_max'],
                          p['v_max'], p['t2'],
                          p['v_max'], p['t2'], str(p['S2']).replace('.', ','),
                          p['v_max'], p['v_end3'],
                          p['v3_eq'], p['t3'],
                          p['t3'], p['v3_tex'], str(p['S3']).replace('.', ','),
                          p['v_end3'],
                          p['v4_eq'], p['t4'],
                          p['t4'], p['v4_tex'], str(p['S4']).replace('.', ','),
                          str(p['S1']).replace('.', ','), str(p['S2']).replace('.', ','), str(p['S3']).replace('.', ','), str(p['S4']).replace('.', ','), str(p['ans_m']).replace('.', ','), str(p['ans_km']).replace('.', ','),
                          kq))
            dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                       '\\loigiai{\n' + str(loigiai) + '\n}\n'
                       '\\end{ex}\n\\end{minipage} \n\n')
            return content


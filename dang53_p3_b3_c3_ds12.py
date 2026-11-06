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


def bt_dang53_p3_b3_c3_ds12(self):
            # Khai báo biến
            # Hàm hỗ trợ định dạng số thập phân dùng dấu phẩy
            def fmt(val):
                if val == int(val):
                    return str(int(val))
                return str(val).replace('.', ',')

            # Hàm định dạng hệ số để tránh trường hợp 1x
            def format_term(coef, var):
                if coef == 1: return var
                if coef == -1: return f"-{var}"
                return f"{coef}{var}"

            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Các bộ cấu hình cho bài toán để đảm bảo kết quả luôn tròn hoặc đẹp
                configs = [
                    {
                        'n': 5, 'h_cm': 15, 'c': 45,
                        'b': 3, 'd': 1, 'x0': 2, 'y0': 2,
                        'b_plus_d': 4, 'k': 2,
                        'x0_cubed': 8, 'x0_sq': 4,
                        'term1_str': r'-\frac{16}{3}', 'term2_str': '8',
                        'S1_str': r'\frac{8}{3}', 'S1_val': Rational(8, 3)
                    },
                    {
                        'n': 6, 'h_cm': 10, 'c': 50,
                        'b': 4, 'd': 2, 'x0': 3, 'y0': 3,
                        'b_plus_d': 6, 'k': 3,
                        'x0_cubed': 27, 'x0_sq': 9,
                        'term1_str': '-18', 'term2_str': '27',
                        'S1_str': '9', 'S1_val': Rational(9, 1)
                    },
                    {
                        'n': 10, 'h_cm': 12, 'c': 30,
                        'b': 3, 'd': 1, 'x0': 2, 'y0': 2,
                        'b_plus_d': 4, 'k': 2,
                        'x0_cubed': 8, 'x0_sq': 4,
                        'term1_str': r'-\frac{16}{3}', 'term2_str': '8',
                        'S1_str': r'\frac{8}{3}', 'S1_val': Rational(8, 3)
                    },
                    {
                        'n': 3, 'h_cm': 20, 'c': 75,
                        'b': 3, 'd': 1, 'x0': 2, 'y0': 2,
                        'b_plus_d': 4, 'k': 2,
                        'x0_cubed': 8, 'x0_sq': 4,
                        'term1_str': r'-\frac{16}{3}', 'term2_str': '8',
                        'S1_str': r'\frac{8}{3}', 'S1_val': Rational(8, 3)
                    }
                ]

                cfg = random.choice(configs)
                n = cfg['n']
                h_cm = cfg['h_cm']
                c_cost = cfg['c']
                b = cfg['b']
                d = cfg['d']
                x0 = cfg['x0']
                y0 = cfg['y0']
                b_plus_d = cfg['b_plus_d']
                k = cfg['k']
                x0_cubed = cfg['x0_cubed']
                x0_sq = cfg['x0_sq']
                term1_str = cfg['term1_str']
                term2_str = cfg['term2_str']
                S1_str = cfg['S1_str']
                S1_val = cfg['S1_val']

                # Tính toán (Sử dụng Rational để ra phân số)
                h_m_rat = Rational(h_cm, 100)
                V1_rat = S1_val * h_m_rat
                V_rat = n * V1_rat
                C_val = int(V_rat * c_cost) # Kết quả chi phí cuối cùng là số nguyên

                h_m_str = latex(h_m_rat)
                V1_str = latex(V1_rat)
                V_str = latex(V_rat)

                P1_term = f"-x^2 + {format_term(b, 'x')}"
                P2_term = f"x^2 - {format_term(d, 'x')}"
                b_plus_d_term = format_term(b_plus_d, 'x')

                # Xây dựng các đáp án trắc nghiệm
                da_correct = C_val
                distractors = [da_correct + 10, da_correct - 10, da_correct + 20, da_correct + 5]

                # Lọc ra các đáp án sai hợp lệ
                valid_distractors = list(set([dist for dist in distractors if dist != da_correct and dist > 0]))
                random.shuffle(valid_distractors)
                das1 = valid_distractors[0]
                das2 = valid_distractors[1]
                das3 = valid_distractors[2]

                # Các đáp án hoàn chỉnh
                da_d = '\\True $%s$' % fmt(da_correct)
                da_s1 = '$%s$' % fmt(das1)
                da_s2 = '$%s$' % fmt(das2)
                da_s3 = '$%s$' % fmt(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                hinhve=r'''\begin{center}
            	\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            		\draw  [draw opacity=0][fill={rgb, 255:red, 244; green, 155; blue, 196 }  ,fill opacity=1 ][line width=1]  (479.2,96.13) .. controls (459.47,208.73) and (392.47,211.73) .. (343.33,170.67) .. controls (362.97,21.23) and (459.47,31.23) .. (479.2,96.13) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.32 ] (150.37,164.13) -- (309.03,190.13) -- (155.03,246.13) -- (48.37,186.13) -- cycle ;
            		\draw  [fill={rgb, 255:red, 193; green, 188; blue, 167 }  ,fill opacity=1 ] (174.2,138.4) -- (290.7,181.9) -- (155.7,228.4) -- (54.64,177.36) -- cycle ;
            		\draw  [fill={rgb, 255:red, 194; green, 190; blue, 179 }  ,fill opacity=1 ] (157.2,189.4) -- (156.2,216.4) -- (74.2,176.4) -- (74,153.5) -- cycle ;
            		\draw  [fill={rgb, 255:red, 194; green, 190; blue, 179 }  ,fill opacity=1 ] (268.2,158.9) -- (267.87,181.07) -- (156.2,216.4) -- (157.2,189.4) -- cycle ;
            		\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (155.7,228.4) -- (155.53,235.4) -- (55.04,184.56) -- (54.64,177.36) -- cycle ;
            		\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (290.7,181.9) -- (290.53,187.73) -- (155.53,235.4) -- (155.7,228.4) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (192.63,155.68) .. controls (186.42,156.39) and (176.24,149.18) .. (177.44,142.56) .. controls (184.64,151.65) and (186.86,153.09) .. (192.63,155.68) -- cycle ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.21 ]   (157.04,198.16) -- (267.84,165.76) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.21 ]   (155.84,207.76) -- (266.64,173.36) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.21 ]   (157.04,198.16) -- (73.44,160.16) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.21 ]   (155.84,206.76) -- (74.24,168.96) ;
            		\draw  [fill={rgb, 255:red, 223; green, 215; blue, 190 }  ,fill opacity=1 ] (171.7,132.4) -- (268.2,158.9) -- (157.2,189.4) -- (74,153.5) -- cycle ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.21 ]   (115.2,196.4) -- (115.6,171.45) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.21 ]   (92.64,184.96) -- (92.8,161.85) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.21 ]   (141.2,208.4) -- (142.24,182.96) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.21 ]   (83.04,180.16) -- (82.8,157.85) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.21 ]   (103.44,189.76) -- (103.44,167.36) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.21 ]   (127.44,201.76) -- (128.4,177.05) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.21 ]   (171.6,210.8) -- (172.64,185.36) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.21 ]   (185.2,207.2) -- (186.24,181.76) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.21 ]   (198,203.6) -- (199.04,178.16) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.21 ]   (211.66,199.59) -- (212.7,174.15) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.21 ]   (225.44,194.56) -- (225.84,170.96) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.21 ]   (237.84,189.76) -- (238.64,167.36) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.21 ]   (249.84,186.56) -- (250.64,164.56) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.21 ]   (259.44,183.76) -- (259.84,162.16) ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.45 ] (120.64,156.2) .. controls (122.64,170.16) and (142.24,163.36) .. (167.84,161.36) .. controls (193.44,159.36) and (225.44,163.36) .. (216.64,154.96) .. controls (207.84,146.56) and (118.64,142.24) .. (120.64,156.2) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.37 ] (74,153.5) -- (127.44,201.76) -- (74.2,176.4) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.27 ] (268.2,158.9) -- (191.2,204.13) -- (268.4,181.8) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.27 ] (171.7,132.4) -- (74,153.5) -- (237.2,151.47) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 240; green, 117; blue, 161 }  ,fill opacity=1 ] (153.77,98.21) .. controls (153.77,89.09) and (161.17,81.69) .. (170.29,81.69) .. controls (179.42,81.69) and (186.81,89.09) .. (186.81,98.21) .. controls (186.81,107.34) and (179.42,114.73) .. (170.29,114.73) .. controls (161.17,114.73) and (153.77,107.34) .. (153.77,98.21) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.6 ] (170.57,91.69) -- (171.5,96.1) -- (175.14,95.84) -- (172.07,98.3) -- (173.39,102.55) -- (170.57,99.67) -- (167.75,102.55) -- (169.07,98.3) -- (166.01,95.84) -- (169.65,96.1) -- cycle ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.52 ][fill={rgb, 255:red, 240; green, 117; blue, 161 }  ,fill opacity=1 ] (147.23,67.8) .. controls (141.8,14.53) and (204.8,19.87) .. (191.93,68.8) .. controls (178.8,86.87) and (172.67,97.87) .. (166.67,91.2) .. controls (161.73,87.43) and (158.33,82.53) .. (147.23,67.8) -- cycle ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.52 ][fill={rgb, 255:red, 240; green, 117; blue, 161 }  ,fill opacity=1 ] (191.93,68.8) .. controls (249.8,39.87) and (257.47,111.53) .. (201.8,109.87) .. controls (180.8,102.25) and (175.13,101.2) .. (174.84,93.96) .. controls (177.09,88.17) and (180.85,83.55) .. (191.93,68.8) -- cycle ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.52 ][fill={rgb, 255:red, 240; green, 117; blue, 161 }  ,fill opacity=1 ] (201.8,109.87) .. controls (248.87,159.71) and (184.47,180.87) .. (170.47,129.53) .. controls (170.82,107.2) and (168.8,105.87) .. (172.8,103.2) .. controls (180.8,101.2) and (182.53,104.37) .. (201.8,109.87) -- cycle ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.52 ][fill={rgb, 255:red, 240; green, 117; blue, 161 }  ,fill opacity=1 ] (169.13,134.2) .. controls (141.8,198.53) and (94.47,138.2) .. (139.78,109.35) .. controls (159.13,102.53) and (170.7,100.65) .. (169.47,109.53) .. controls (169.76,115.73) and (171.8,117.2) .. (169.13,134.2) -- cycle ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.52 ][fill={rgb, 255:red, 240; green, 117; blue, 161 }  ,fill opacity=1 ] (136.8,109.87) .. controls (76.47,103.53) and (107.47,42.2) .. (147.23,67.8) .. controls (162.47,85.2) and (169.8,96.2) .. (163.13,101.2) .. controls (157.9,104.53) and (154.46,104.53) .. (136.8,109.87) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.39 ] (127.37,102.89) .. controls (88.57,86.09) and (111.91,55.09) .. (140.57,68.09) .. controls (153.91,77.09) and (166.8,94.2) .. (160.13,99.2) .. controls (154.9,102.53) and (137.77,105.23) .. (127.37,102.89) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.37 ] (152.57,59.29) .. controls (149.77,19.69) and (192.57,24.89) .. (188.97,60.09) .. controls (188.37,71.03) and (174.47,91.8) .. (167.94,86.62) .. controls (163.39,82.39) and (153.77,72.49) .. (152.57,59.29) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.25 ] (197,72.47) .. controls (236.48,53.07) and (249,89.13) .. (213.02,99.99) .. controls (197.24,103.11) and (177.25,101.48) .. (178.4,93.23) .. controls (184,84.13) and (188.02,78.2) .. (197,72.47) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.3 ] (163,136.13) .. controls (152.17,174.09) and (109.37,155.69) .. (130,124.8) .. controls (139.53,111.84) and (161.45,101.63) .. (166.17,108.49) .. controls (171.32,116.37) and (165.77,129.29) .. (163,136.13) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.28 ] (205.77,118.49) .. controls (233.56,147.78) and (202.96,167.28) .. (182.57,143.29) .. controls (174.35,129.47) and (169.67,103.8) .. (177.67,106.47) .. controls (186.93,104.8) and (199.96,112.18) .. (205.77,118.49) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (127.37,97.69) .. controls (100.17,85.69) and (105.77,56.89) .. (140.17,71.69) .. controls (153.51,80.69) and (166.8,94.2) .. (160.13,99.2) .. controls (154.9,102.53) and (137.37,102.09) .. (127.37,97.69) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (128.17,82.89) .. controls (108.97,73.69) and (121.37,64.09) .. (140.17,74.09) .. controls (153.51,83.09) and (158.17,90.89) .. (160.13,99.2) .. controls (149.37,91.29) and (138.17,87.29) .. (128.17,82.89) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (157.25,58.71) .. controls (152.92,33.22) and (186.56,23.05) .. (186.17,60.49) .. controls (183.01,76.27) and (175.36,93.52) .. (168.17,89.29) .. controls (163.08,85.75) and (157.05,69.64) .. (157.25,58.71) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (170.57,50.89) .. controls (171.65,29.63) and (184.95,37.69) .. (182.97,58.89) .. controls (179.81,74.67) and (179.48,76.28) .. (172.57,81.29) .. controls (175.72,68.32) and (170.37,61.82) .. (170.57,50.89) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (204.57,74.09) .. controls (232.75,64.61) and (242.17,86.89) .. (212.97,97.29) .. controls (197.06,99.64) and (178.19,101.33) .. (179.74,93.14) .. controls (181.36,87.15) and (194.22,77.59) .. (204.57,74.09) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (217.77,79.29) .. controls (225.77,77.69) and (230,69.6) .. (209.37,74.89) .. controls (193.77,79.29) and (187.77,88.89) .. (181.3,92.22) .. controls (197.77,84.49) and (209.37,74.49) .. (217.77,79.29) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (207,121.13) .. controls (218.17,139.69) and (209.37,160.49) .. (186.57,138.89) .. controls (180.17,129.29) and (169.55,108.33) .. (177.67,106.47) .. controls (183.8,105.55) and (199.65,113.05) .. (207,121.13) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (198.97,134.49) .. controls (208.17,144.68) and (212.57,135.29) .. (206.17,124.49) .. controls (197.63,110.86) and (182.17,110.09) .. (178.78,108.45) .. controls (193.37,119.29) and (198.57,125.08) .. (198.97,134.49) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (158.97,139.69) .. controls (148.17,165.29) and (114.97,146.49) .. (133.77,126.09) .. controls (141.46,113.6) and (158.62,102.99) .. (162.97,110.09) .. controls (165.8,115.62) and (163.37,131.69) .. (158.97,139.69) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (142.97,136.49) .. controls (141.42,142.03) and (131.46,142.4) .. (136.97,126.49) .. controls (148.97,114.09) and (149.77,111.69) .. (157.77,110.09) .. controls (148.9,120.07) and (148.29,126.95) .. (142.97,136.49) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 239; green, 240; blue, 165 }  ,fill opacity=0.5 ] (175.77,54.49) .. controls (176.85,33.23) and (183.37,42.89) .. (182.97,58.89) .. controls (179.81,74.67) and (183.88,66.68) .. (176.97,71.69) .. controls (180.12,58.72) and (176.97,64.89) .. (175.77,54.49) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 239; green, 240; blue, 165 }  ,fill opacity=0.5 ] (212.18,87.74) .. controls (232.14,80.35) and (225.83,90.15) .. (210.97,96.09) .. controls (195.23,99.41) and (204.18,100) .. (196.84,95.63) .. controls (210.01,93.4) and (203.09,92.95) .. (212.18,87.74) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 239; green, 240; blue, 165 }  ,fill opacity=0.5 ] (192.11,131.55) .. controls (205.71,147.93) and (194.37,145.23) .. (183.83,133.18) .. controls (175.49,119.43) and (177.9,128.06) .. (179.59,119.7) .. controls (186.06,131.38) and (184.19,124.7) .. (192.11,131.55) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 239; green, 240; blue, 165 }  ,fill opacity=0.5 ] (146.42,127.5) .. controls (132.95,143.98) and (133.43,132.34) .. (143.23,119.69) .. controls (155.13,108.86) and (147.12,112.88) .. (155.65,112.93) .. controls (145.43,121.52) and (151.62,118.41) .. (146.42,127.5) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 239; green, 240; blue, 165 }  ,fill opacity=0.5 ] (140.85,83.19) .. controls (124.41,69.67) and (136.05,70.18) .. (148.67,80.03) .. controls (159.46,91.96) and (155.46,83.94) .. (155.38,92.47) .. controls (146.83,82.22) and (149.92,88.42) .. (140.85,83.19) -- cycle ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.28 ]   (114.97,67.29) .. controls (94.17,81.29) and (108.57,106.89) .. (142.57,106.89) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.28 ]   (159.77,35.69) .. controls (143.37,52.09) and (146,72.77) .. (165.37,87.69) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.28 ]   (234.57,73.29) .. controls (242.57,96.49) and (208.97,113.29) .. (187.37,102.89) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.28 ]   (177.67,106.47) .. controls (211.67,112.07) and (219.77,140.09) .. (211.37,150.89) ;
            		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.28 ]   (156.57,105.69) .. controls (135.37,107.29) and (111.77,137.29) .. (131.77,156.49) ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (129.1,99.39) .. controls (121.87,101.08) and (109.58,93.84) .. (110.61,85.76) .. controls (119.53,95.66) and (122.2,97.08) .. (129.1,99.39) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (154.28,64.48) .. controls (149.35,60.46) and (147.71,48.2) .. (153.64,44.59) .. controls (151.74,55.96) and (152.19,58.54) .. (154.28,64.48) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (225.37,96.09) .. controls (223.22,100.9) and (213.47,105.61) .. (209.06,102.24) .. controls (218.93,100.41) and (220.96,99.34) .. (225.37,96.09) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (161.66,133.51) .. controls (164,140.56) and (157.89,153.45) .. (149.74,153.15) .. controls (158.8,143.38) and (159.98,140.59) .. (161.66,133.51) -- cycle ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (76.4,153.6) -- (157.2,188.4) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (157.2,188.4) -- (264,159.2) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (157.2,226.4) -- (286.8,182) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (56.8,177.6) -- (155.2,226) ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (191.47,115.57) .. controls (196.73,115.93) and (204.51,123.45) .. (202.87,128.75) .. controls (197.75,120.13) and (196.04,118.59) .. (191.47,115.57) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 225; green, 20; blue, 143 }  ,fill opacity=0.36 ] (146.77,104.05) .. controls (138.74,110.83) and (115.62,107.28) .. (109.45,94.61) .. controls (130.56,104.12) and (135.44,104.67) .. (146.77,104.05) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 225; green, 20; blue, 143 }  ,fill opacity=0.36 ] (169.21,113.29) .. controls (173.31,119.61) and (169.62,136.92) .. (160.77,141.09) .. controls (168.34,125.53) and (168.99,121.86) .. (169.21,113.29) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 225; green, 20; blue, 143 }  ,fill opacity=0.36 ] (225.87,102.09) .. controls (219.92,110.77) and (196.69,113.47) .. (187.37,102.89) .. controls (210.25,106.46) and (215.1,105.7) .. (225.87,102.09) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 225; green, 20; blue, 143 }  ,fill opacity=0.36 ] (182.57,143.29) .. controls (172.77,142.1) and (162.72,124.38) .. (169.26,112.4) .. controls (173.51,132.45) and (175.79,136.07) .. (182.57,143.29) -- cycle ;
            		\draw [line width=1]    (314.67,171.33) -- (529.87,170.81) ;
            		\draw [shift={(533.87,170.8)}, rotate = 179.86] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (13.4,-6.43) -- (0,0) -- (13.4,6.44) -- (8.9,0) -- cycle    ;
            		\draw [line width=1]    (342.47,206.73) -- (341.88,28.97) ;
            		\draw [shift={(341.87,24.97)}, rotate = 89.81] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (13.4,-6.43) -- (0,0) -- (13.4,6.44) -- (8.9,0) -- cycle    ;
            		\draw [line width=1]    (343.33,170.67) .. controls (353.87,38.13) and (480.53,-13.87) .. (495.2,170.13) ;
            		\draw [line width=1]    (343.33,170.67) .. controls (427.87,232.8) and (470.53,158.13) .. (479.2,96.13) ;
            		\draw (323.27,177) node [anchor=north west][inner sep=0.75pt]    {$O$};
            		\draw (517.77,181) node [anchor=north west][inner sep=0.75pt]    {$x$};
            		\draw (320.43,26) node [anchor=north west][inner sep=0.75pt]    {$y$};
            		\draw (478.77,72) node [anchor=north west][inner sep=0.75pt]    {$A$};
                    \draw (400.77,30) node [anchor=north west][inner sep=0.75pt]    {$(P_1)$};
            		\draw (400.77,200) node [anchor=north west][inner sep=0.75pt]    {$(P_2)$};
            	\end{tikzpicture}
            \end{center}'''

                # Nội dung câu hỏi
                noidungcauhoi = (r'''Hướng tới chuỗi sự kiện văn hóa và du lịch năm 2026 tại Điện Biên, một nhóm kỹ sư thiết kế một mô hình bông hoa Ban khổng lồ phát sáng đặt tại Quảng trường 7/5. Bông hoa được thiết kế gồm $%s$ cánh hoa có kích thước và hình dáng giống hệt nhau. Mỗi cánh hoa được đúc đặc nguyên khối từ nhựa mica tán sáng cao cấp với độ dày đồng nhất là $%s$ cm. Trên mặt phẳng tọa độ $Oxy$ (đơn vị đo trên mỗi trục tọa độ là mét), bề mặt của mỗi cánh hoa được mô tả là một hình phẳng giới hạn bởi hai parabol có phương trình là: $\left(P_1\right): y = %s$ và $\left(P_2\right): y = %s$. %s Biết chi phí vật liệu nhựa mica tán sáng này là $%s$ triệu đồng cho mỗi $\mathrm{m}^3$. Hỏi tổng chi phí vật liệu để đúc cả $%s$ cánh hoa trong mô hình biểu tượng này là bao nhiêu triệu đồng?''' % (n, h_cm, P1_term, P2_term, hinhve, c_cost, n))

                # Nội dung lời giải
                loigiai = ('''1) Giao điểm của hai parabol được xác định bởi\\\\
                $\\quad %s = %s$\\\\
                $\\Leftrightarrow 2x^2 - %s = 0$\\\\
                $\\Leftrightarrow 2x\\left(x - %s\\right) = 0$\\\\
                $\\Rightarrow x = 0$ hoặc $x = %s$.\\\\
                Từ đó các giao điểm là $O\\left(0,0\\right)$ và $A\\left(%s,%s\\right)$.\\\\
                2) Trên đoạn $\\left[0,%s\\right]$, đồ thị $P_1$ nằm trên $P_2$, nên diện tích một cánh hoa là\\\\
                $\\quad S_1 = \\int_0^{%s} \\left[ \\left( %s \\right) - \\left( %s \\right) \\right] \\mathrm{d}x$\\\\
                $\\quad = \\int_0^{%s} \\left( -2x^2 + %s \\right) \\mathrm{d}x$\\\\
                $\\quad = \\left[ -\\frac{2}{3}x^3 + %sx^2 \\right]_0^{%s}$\\\\
                $\\quad = \\left( -\\frac{2}{3} \\cdot %s + %s \\cdot %s \\right) - 0 = %s + %s = %s \\text{ } \\left(\\mathrm{m}^2\\right)$.\\\\
                3) Độ dày của bông hoa: $h = %s \\text{ cm} = %s \\text{ m}$.\\\\
                Thể tích một cánh hoa:\\\\
                $\\quad V_1 = S_1 \\cdot h = %s \\cdot %s = %s \\text{ } \\left(\\mathrm{m}^3\\right)$.\\\\
                4) Bông hoa có $%s$ cánh nên tổng thể tích là\\\\
                $\\quad V = %s V_1 = %s \\cdot %s = %s \\text{ } \\left(\\mathrm{m}^3\\right)$.\\\\
                5) Chi phí vật liệu:\\\\
                $\\quad C = %s \\cdot %s = %s \\text{ } \\left(\\text{triệu đồng}\\right)$.''' % (
                    P1_term, P2_term,
                    b_plus_d_term,
                    x0,
                    x0,
                    x0, y0,
                    x0,
                    x0, P1_term, P2_term,
                    x0, b_plus_d_term,
                    k, x0,
                    x0_cubed, k, x0_sq, term1_str, term2_str, S1_str,
                    h_cm, h_m_str,
                    S1_str, h_m_str, V1_str,
                    n,
                    n, n, V1_str, V_str,
                    V_str, c_cost, fmt(C_val)
                ))
                dapan='\\shortans[0]{$%s$}\n'%(fmt(C_val))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content  


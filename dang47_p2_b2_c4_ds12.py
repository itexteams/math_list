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


def bt_dang47_p2_b2_c4_ds12(self):
            # Khai báo biến
            # Khai báo biến
            pA_percent = random.randint(3, 8)
            pA = sp.Rational(pA_percent, 100)
            pA_bar = 1 - pA

            p_pos_A_percent = random.randint(92, 98)
            p_pos_A = sp.Rational(p_pos_A_percent, 100)

            p_pos_Abar_percent = random.randint(1, 4)
            p_pos_Abar = sp.Rational(p_pos_Abar_percent, 100)

            def fmt_dec(rat, max_places=5):
                f = float(rat)
                s = f"{f:.{max_places}f}".rstrip('0').rstrip('.')
                if s == '': s = '0'
                return s.replace('.', ',')

            def fmt_round(rat, places=2):
                f = float(rat)
                s = f"{f:.{places}f}"
                return s.replace('.', ',')

            str_p_pos_A = fmt_dec(p_pos_A)
            str_p_pos_Abar = fmt_dec(p_pos_Abar)
            str_pA_dec = fmt_dec(pA)
            str_pA_bar_dec = fmt_dec(pA_bar)

            # Tính toán các xác suất
            p_B1 = pA * p_pos_A + pA_bar * p_pos_Abar
            p_A_given_B1 = (pA * p_pos_A) / p_B1
            p_B1_B2 = pA * (p_pos_A**2) + pA_bar * (p_pos_Abar**2)
            p_B2_given_B1 = p_B1_B2 / p_B1
            p_A_given_B1_B2 = (pA * (p_pos_A**2)) / p_B1_B2

            str_p_B1 = fmt_dec(p_B1)

            # Các giá trị đúng sai cho từng mức độ
            a_correct_val = str_p_B1
            a_wrong_val = fmt_dec(p_B1 + sp.Rational(random.choice([-1, 1]) * random.randint(1, 5), 1000))

            num_b, den_b = p_A_given_B1.p, p_A_given_B1.q
            b_correct_latex = f"\\frac{{{num_b}}}{{{den_b}}}"
            wrong_num_b = num_b + random.choice([-2, -1, 1, 2])
            if wrong_num_b <= 0: wrong_num_b = num_b + 1
            if wrong_num_b == num_b: wrong_num_b += 1
            b_wrong_latex = f"\\frac{{{wrong_num_b}}}{{{den_b}}}"

            c_correct_val = fmt_round(p_B2_given_B1, 2)
            c_wrong_val = fmt_round(float(p_B2_given_B1) + random.choice([-0.12, 0.15]), 2)

            d_correct_val = fmt_round(p_A_given_B1_B2, 2)
            d_wrong_val = fmt_round(float(p_A_given_B1_B2) - random.choice([0.04, 0.05]), 2)
            num_d, den_d = p_A_given_B1_B2.p, p_A_given_B1_B2.q
            d_frac_latex = f"\\frac{{{num_d}}}{{{den_d}}}"

            hinhve=r'''\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-0.8,xscale=0.8]
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 80; green, 206; blue, 227 }  ,fill opacity=1 ] (201.76,120) .. controls (203.07,121.2) and (204.29,122.38) .. (205.41,123.52) .. controls (231.67,150.16) and (208.34,159.74) .. (218.96,177.16) .. controls (225.76,183.56) and (215.36,183.56) .. (218.96,183.56) .. controls (197.76,175.56) and (170.56,145.56) .. (201.76,120) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.22 ] (203.64,115.91) .. controls (204.96,117.12) and (206.17,118.29) .. (207.29,119.43) .. controls (233.55,146.07) and (205.54,156.18) .. (216.16,173.6) .. controls (222.96,180) and (213.36,179.2) .. (216.96,179.2) .. controls (195.76,171.2) and (172.44,141.47) .. (203.64,115.91) -- cycle ;
            	\draw  [fill={rgb, 255:red, 80; green, 206; blue, 227 }  ,fill opacity=1 ] (147.6,114.4) .. controls (138.3,42.1) and (233.8,42.1) .. (244.3,51.6) .. controls (271.8,28.6) and (310.03,41.78) .. (306.8,56.1) .. controls (277.8,62.6) and (285.8,75.1) .. (286.8,83.1) .. controls (331.3,135.1) and (308.3,269.1) .. (206.3,231.6) .. controls (198.3,241.6) and (195.3,248.6) .. (166.8,248.6) .. controls (162.88,250.36) and (159.59,250.88) .. (156.84,250.38) .. controls (151.51,250.23) and (160.39,240.51) .. (169.3,231.1) .. controls (176.34,223.66) and (182.93,215.94) .. (185.8,216.6) .. controls (182.56,212) and (183.4,220.78) .. (178.56,195.6) .. controls (176.02,190.76) and (170.65,190.03) .. (167.4,185.47) .. controls (164.78,181.78) and (207.07,176.47) .. (208.73,220.47) .. controls (253.07,228.47) and (241.4,173.8) .. (224.07,163.47) .. controls (203.73,142.47) and (163.36,156.8) .. (141.76,146.8) .. controls (126.76,138.8) and (127.6,124.4) .. (147.6,114.4) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 219; green, 236; blue, 240 }  ,fill opacity=1 ] (132.56,138.44) .. controls (152.96,152) and (174.96,129.2) .. (184.56,118) .. controls (251.76,68.8) and (336.96,246.8) .. (206.56,226) .. controls (259.36,227.2) and (247.05,176.53) .. (224.56,160.4) .. controls (204.25,143.33) and (168.56,153.6) .. (147.36,147.2) .. controls (140.2,145.5) and (134.56,140.8) .. (132.56,138.44) -- cycle ;
            	\draw    (134.56,138.64) .. controls (141.76,143.2) and (168.16,147.2) .. (184.96,111.6) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.4 ]   (150.8,113.2) .. controls (160.96,108.8) and (164.56,110) .. (168.96,112.8) ;
            	\draw    (182.16,112.8) -- (188.16,110.4) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (180.96,120.4) .. controls (191.76,108.4) and (223.36,105.6) .. (236.96,118.8) .. controls (216.96,138.8) and (195.76,138) .. (164.16,137.6) .. controls (174.56,129.6) and (174.16,130.4) .. (180.96,120.4) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (244.96,168) .. controls (242.56,150.8) and (236.96,147.6) .. (250.56,160.8) .. controls (286.56,214) and (241.36,226.8) .. (209.76,226.4) .. controls (273.36,224) and (238.16,178) .. (244.96,168) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 80; green, 206; blue, 227 }  ,fill opacity=1 ] (236.96,118.8) .. controls (238.27,120) and (239.49,121.18) .. (240.61,122.32) .. controls (266.87,148.96) and (243.54,158.54) .. (254.16,175.96) .. controls (260.96,182.36) and (250.56,182.36) .. (254.16,182.36) .. controls (232.96,174.36) and (205.76,144.36) .. (236.96,118.8) -- cycle ;
            	\draw    (224.16,136) .. controls (220.16,144) and (216.96,162.4) .. (254.16,182.36) ;
            	\draw    (246.96,129.64) .. controls (262.16,144) and (244.56,160.8) .. (256.22,180.68) .. controls (257.76,184) and (253.15,180.29) .. (254.16,182.36) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (190.09,103.67) .. controls (188.26,97.24) and (190.94,90.83) .. (196.09,89.37) .. controls (201.23,87.9) and (206.89,91.93) .. (208.72,98.37) .. controls (210.56,104.81) and (207.87,111.21) .. (202.72,112.68) .. controls (197.58,114.14) and (191.92,110.11) .. (190.09,103.67) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (192.89,102.88) .. controls (191.61,98.38) and (193.49,93.9) .. (197.09,92.88) .. controls (200.68,91.85) and (204.64,94.67) .. (205.92,99.17) .. controls (207.2,103.67) and (205.32,108.14) .. (201.73,109.17) .. controls (198.13,110.19) and (194.18,107.37) .. (192.89,102.88) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 240; green, 194; blue, 129 }  ,fill opacity=1 ] (198.45,117.39) .. controls (197.94,115.6) and (199.86,113.5) .. (202.72,112.68) .. controls (205.59,111.86) and (208.33,112.65) .. (208.84,114.43) .. controls (209.35,116.22) and (207.43,118.33) .. (204.56,119.14) .. controls (201.7,119.96) and (198.96,119.18) .. (198.45,117.39) -- cycle ;
            	\draw [color={rgb, 255:red, 60; green, 153; blue, 173 }  ,draw opacity=1 ][line width=2.25]    (132.56,135.44) .. controls (140.96,140.8) and (164.56,144.4) .. (182.16,112.8) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.52 ] (171.36,115.6) .. controls (163.36,129.2) and (148.16,129.6) .. (133.36,129.6) .. controls (142.56,110.4) and (166.96,108.8) .. (171.36,115.6) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.34 ] (166.56,113.6) .. controls (158.96,126.4) and (151.36,126) .. (136.56,126) .. controls (148.96,112) and (162.16,106.8) .. (166.56,113.6) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (135.56,132.15) .. controls (134.83,131.06) and (136.74,128.53) .. (139.8,126.49) .. controls (142.87,124.45) and (145.95,123.68) .. (146.67,124.77) .. controls (147.39,125.86) and (145.49,128.39) .. (142.42,130.43) .. controls (139.35,132.47) and (136.28,133.24) .. (135.56,132.15) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.3 ] (179.36,58) .. controls (194.96,46.8) and (225.5,41.6) .. (244.3,51.6) .. controls (224.3,71.6) and (182.16,89.6) .. (150.56,89.2) .. controls (154.16,71.6) and (168.16,60.4) .. (179.36,58) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.3 ] (179.36,58) .. controls (194.96,46.8) and (217.76,43.2) .. (233.76,49.2) .. controls (213.76,69.2) and (185.36,78) .. (154.56,81.2) .. controls (158.16,63.6) and (168.16,60.4) .. (179.36,58) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.16 ] (180.56,60) .. controls (196.16,48.8) and (252.16,36.8) .. (282.56,76.8) .. controls (225.36,106.8) and (179.36,113.2) .. (148.56,106) .. controls (144.16,78.4) and (169.36,62.4) .. (180.56,60) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (172.95,70.84) .. controls (171.68,68.93) and (173.72,65.34) .. (177.5,62.83) .. controls (181.29,60.31) and (185.39,59.82) .. (186.66,61.74) .. controls (187.93,63.65) and (185.89,67.24) .. (182.1,69.75) .. controls (178.32,72.27) and (174.22,72.76) .. (172.95,70.84) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (168.83,78.07) .. controls (168.15,77.05) and (168.62,75.55) .. (169.88,74.71) .. controls (171.14,73.88) and (172.71,74.02) .. (173.38,75.04) .. controls (174.06,76.06) and (173.58,77.56) .. (172.33,78.39) .. controls (171.07,79.23) and (169.5,79.08) .. (168.83,78.07) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (191.23,62.87) .. controls (190.55,61.85) and (191.02,60.35) .. (192.28,59.51) .. controls (193.54,58.68) and (195.11,58.82) .. (195.78,59.84) .. controls (196.46,60.86) and (195.98,62.36) .. (194.73,63.19) .. controls (193.47,64.03) and (191.9,63.88) .. (191.23,62.87) -- cycle ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.62 ][line width=1.5]    (149.76,111.44) .. controls (139.36,54.4) and (233.76,20.8) .. (283.36,82) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.46 ][line width=1.5]    (283.36,82) .. controls (321.76,118) and (320.96,263.2) .. (206.3,231.6) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.1 ] (260.16,64) .. controls (321.76,84.8) and (334.16,262.8) .. (207.76,230) .. controls (337.76,238) and (296.56,78) .. (260.16,64) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.19 ] (236.96,118.8) .. controls (238.27,120) and (239.49,121.18) .. (240.61,122.32) .. controls (266.87,148.96) and (245.36,159.2) .. (254.16,175.96) .. controls (260.96,182.36) and (250.56,182.36) .. (254.16,182.36) .. controls (237.36,166) and (256.16,140.8) .. (236.96,118.8) -- cycle ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (226.96,137.44) .. controls (222.16,150) and (236.96,171.2) .. (246.56,174.4) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (191.76,151.44) .. controls (194.56,164.4) and (204.96,176) .. (214.56,179.2) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.29 ] (251.76,54.8) .. controls (262.56,42.8) and (299.76,38.4) .. (306.8,56.1) .. controls (282.8,60.5) and (280.16,68.4) .. (286.8,83.1) .. controls (272.16,66.8) and (265.76,60) .. (251.76,54.8) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.14 ] (262.56,60.8) .. controls (273.36,48.8) and (293.36,45.6) .. (306.8,56.1) .. controls (282.8,60.5) and (280.16,68.4) .. (286.8,83.1) .. controls (272.16,66.8) and (276.56,66) .. (262.56,60.8) -- cycle ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (305.76,52.4) .. controls (278.96,28.4) and (249.36,48.4) .. (248.16,52.8) ;
            	\draw    (190.09,103.67) .. controls (187.36,78.4) and (208.96,90.4) .. (208.72,98.37) ;
            	\draw    (190.16,80.4) .. controls (192.96,74) and (199.76,74.4) .. (203.36,80) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (194.74,102.35) .. controls (193.82,99.13) and (195.16,95.91) .. (197.74,95.18) .. controls (200.32,94.45) and (203.16,96.47) .. (204.08,99.69) .. controls (204.99,102.92) and (203.65,106.13) .. (201.07,106.86) .. controls (198.49,107.6) and (195.66,105.58) .. (194.74,102.35) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (194.93,99.74) .. controls (193.84,98.1) and (194.09,96.03) .. (195.48,95.11) .. controls (196.87,94.19) and (198.87,94.76) .. (199.96,96.4) .. controls (201.04,98.03) and (200.79,100.1) .. (199.41,101.02) .. controls (198.02,101.94) and (196.01,101.37) .. (194.93,99.74) -- cycle ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (170.53,183.87) .. controls (196.53,184.53) and (201.87,199.2) .. (206.53,211.2) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.19 ] (206.56,226) .. controls (205.46,232.99) and (196.84,238.67) .. (186.87,240.73) .. controls (175.34,243.12) and (162.04,241.82) .. (156.84,250.38) .. controls (169.53,246.73) and (201.87,251.73) .. (206.56,226) -- cycle ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ]   (182.33,202.73) .. controls (185.53,211.07) and (184.2,214.73) .. (193.2,218.4) ;
            \end{tikzpicture}'''
            # Nội dung câu hỏi
            noidungcauhoi = (r'''\immini{Biết rằng $%s\%%$ cá heo trong một khu bảo tồn mắc một bệnh nhất định. Một xét nghiệm chẩn đoán có thể được áp dụng để xác định cá heo có mắc bệnh hay không. Nếu cá heo mắc bệnh thì xét nghiệm cho kết quả dương tính với xác suất $%s$ còn nếu cá heo không mắc bệnh thì xét nghiệm cho kết quả dương tính với xác suất $%s$. Xét nghiệm được áp dụng cho một cá heo được chọn ngẫu nhiên.}{%s}''' % (pA_percent, str_p_pos_A, str_p_pos_Abar, hinhve))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Xác suất để thu được kết quả dương tính bằng $%s$' % a_correct_val
            nb_da_1_s = 'Xác suất để thu được kết quả dương tính bằng $%s$' % a_wrong_val
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Gọi $A$ là biến cố: "Cá heo thực sự mắc một bệnh nhất định" và $B_i$ là biến cố: "Xét nghiệm cá heo cho kết quả dương tính lần thứ $i$"; với $i \\in \\mathbb{N}^*$.\\\\
            Xác suất để có kết quả dương tính là $P(B_1) = P(A).P(B_1|A) + P(\\overline{A}).P(B_1|\\overline{A})$;\\\\
            $P(B_1) = %s.%s + %s.%s = %s$.''' % (str_pA_dec, str_p_pos_A, str_pA_bar_dec, str_p_pos_Abar, str_p_B1))

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
            th_da_1_d = '\\True Biết rằng kết quả dương tính thu được thì xác suất để cá heo này thực sự mắc bệnh bằng $%s$' % b_correct_latex
            th_da_1_s = 'Biết rằng kết quả dương tính thu được thì xác suất để cá heo này thực sự mắc bệnh bằng $%s$' % b_wrong_latex
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Ta có: $P(A|B_1) = \\frac{P(AB_1)}{P(B_1)} = \\frac{%s.%s}{%s} = %s$.''' % (str_pA_dec, str_p_pos_A, str_p_B1, b_correct_latex))

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
            vd_da_1_d = '\\True Cá heo khi xét nghiệm đã cho kết quả dương tính lần đầu, xác suất để khi xét nghiệm lần tiếp theo vẫn cho kết quả dương tính bằng $%s$ (làm tròn đến hàng phần trăm)' % c_correct_val
            vd_da_1_s = 'Cá heo khi xét nghiệm đã cho kết quả dương tính lần đầu, xác suất để khi xét nghiệm lần tiếp theo vẫn cho kết quả dương tính bằng $%s$ (làm tròn đến hàng phần trăm)' % c_wrong_val
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Ta có: $P(B_2|B_1) = \\frac{P(B_1B_2)}{P(B_1)} = \\frac{%s.%s^2 + %s.%s^2}{%s} \\approx %s$.''' % (str_pA_dec, str_p_pos_A, str_pA_bar_dec, str_p_pos_Abar, str_p_B1, c_correct_val))

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
            vdc_da_1_d = '\\True Biết rằng kết quả xét nghiệm cả hai lần là dương tính thì xác suất để cá heo này thực sự mắc bệnh bằng $%s$ (làm tròn đến hàng phần trăm)' % d_correct_val
            vdc_da_1_s = 'Biết rằng kết quả xét nghiệm cả hai lần là dương tính thì xác suất để cá heo này thực sự mắc bệnh bằng $%s$ (làm tròn đến hàng phần trăm)' % d_wrong_val
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Ta có: $P(A|B_1B_2) = \\frac{P(AB_1B_2)}{P(B_1B_2)} = \\frac{%s.%s^2}{%s.%s^2 + %s.%s^2} = %s \\approx %s$.''' % (str_pA_dec, str_p_pos_A, str_pA_dec, str_p_pos_A, str_pA_bar_dec, str_p_pos_Abar, d_frac_latex, d_correct_val))

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
                '\\end{ex}\n\\end{minipage}\n\n')
            return content


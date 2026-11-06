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


def bt_dang11_p2_b3_c1_hh12(self):
    # Khai báo biến
    # random giá trị x_B, y_D, z_A
    xb = randint(6, 10)
    yd = randint(8, 12)
    za = randint(3, 6)

    # Các thông số cho câu d
    giam = randint(8, 12)
    tg = randint(10, 15)

    # Tính toán
    v_max = xb * yd * za
    cos_alpha = (xb * 0 + 0 * yd + za * za) / (sqrt(xb**2 + za**2) * sqrt(yd**2 + za**2))
    # simplify cos_alpha to print
    num = za**2
    den_sq = (xb**2 + za**2) * (yd**2 + za**2)
    g_num = num
    g_den = sqrt(den_sq)
    cos_val = Rational(num, 1) / sqrt(den_sq) # just to use sympy formatting

    v_xa = giam * tg
    v_con_lai = v_max - v_xa
    h_con_lai = v_con_lai / (xb * yd)
    cach_mieng = za - h_con_lai
    # Rounding for display
    cach_mieng_float = round(float(cach_mieng), 2)
    cach_mieng_str = f"{cach_mieng_float:.2f}".replace('.', ',')
    if cach_mieng_str.endswith(',00'):
        cach_mieng_str = cach_mieng_str[:-3]

    h_con_lai_float = round(float(h_con_lai), 2)
    h_con_lai_str = f"{h_con_lai_float:.2f}".replace('.', ',')
    if h_con_lai_str.endswith(',00'):
        h_con_lai_str = h_con_lai_str[:-3]

    # Nội dung câu hỏi
    noidungcauhoi = ('''Một bể nước bằng nhựa với phần chứa nước có dạng hình hộp chữ nhật được đặt trong một hệ trục tọa độ $Oxyz$ sao cho các tia $Ox, Oy, Oz$ dọc theo ba cạnh của hình hộp như hình vẽ, miệng bể là hình chữ nhật $ABCD$. Biết đơn vị trên mỗi trục là dm và $x_B = %s; y_D = %s; z_A = %s$. \\\\
    \\begin{center}
    	\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 80; green, 209; blue, 227 }  ,fill opacity=1 ] (193.73,69.47) -- (193.07,123.47) -- (58.4,170.13) -- (59.07,116.13) -- cycle ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 74; green, 144; blue, 226 }  ,fill opacity=1 ] (193.07,123.47) -- (301.07,150.13) -- (170,201) -- (58.4,170.13) -- cycle ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 103; green, 166; blue, 240 }  ,fill opacity=1 ] (193.73,69.47) -- (301.73,96.13) -- (301.07,150.13) -- (193.07,123.47) -- cycle ;
    		\\draw  [color={rgb, 255:red, 74; green, 144; blue, 226 }  ,draw opacity=1 ][fill={rgb, 255:red, 64; green, 215; blue, 223 }  ,fill opacity=0.5 ] (193.73,69.47) -- (301.73,96.13) -- (170.67,147) -- (59.07,116.13) -- cycle ;
    		\\draw  [color={rgb, 255:red, 74; green, 144; blue, 226 }  ,draw opacity=1 ][fill={rgb, 255:red, 74; green, 180; blue, 226 }  ,fill opacity=0.66 ] (301.73,96.13) -- (301.07,150.13) -- (170,201) -- (170.67,147) -- cycle ;
    		\\draw  [color={rgb, 255:red, 74; green, 144; blue, 226 }  ,draw opacity=1 ][fill={rgb, 255:red, 74; green, 180; blue, 226 }  ,fill opacity=0.66 ] (59.07,116.13) -- (170.67,147) -- (170,201) -- (58.4,170.13) -- cycle ;
    		\\draw  [color={rgb, 255:red, 74; green, 144; blue, 226 }  ,draw opacity=1 ][dash pattern={on 4.5pt off 4.5pt}] (193.73,35.47) -- (301.73,62.13) -- (170.67,113) -- (59.07,82.13) -- cycle ;
    		\\draw [color={rgb, 255:red, 74; green, 144; blue, 226 }  ,draw opacity=1 ][line width=1.5]    (59.07,82.13) -- (58.4,170.13) ;
    		\\draw [color={rgb, 255:red, 21; green, 109; blue, 210 }  ,draw opacity=1 ][line width=1.5]    (170.67,113) -- (170,201) ;
    		\\draw [color={rgb, 255:red, 21; green, 109; blue, 210 }  ,draw opacity=1 ][line width=1.5]    (301.73,62.13) -- (301.07,150.13) ;
    		\\draw [color={rgb, 255:red, 131; green, 182; blue, 239 }  ,draw opacity=1 ][line width=1.5]    (193.73,35.47) -- (193.07,123.47) ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 74; green, 144; blue, 226 }  ,fill opacity=0.1 ] (193.73,35.47) -- (193.73,69.47) -- (59.07,116.13) -- (59.07,82.13) -- cycle ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 74; green, 144; blue, 226 }  ,fill opacity=0.1 ] (301.73,62.13) -- (301.73,96.13) -- (193.73,69.47) -- (193.73,35.47) -- cycle ;
    		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ]   (82,89) -- (82.4,175.47) ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.4 ] (170.67,113) -- (168.87,144.9) -- (59.07,116.13) -- (59.07,82.13) -- cycle ;
    		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ]   (110,97.67) -- (110.4,184.13) ;
    		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ]   (136.67,104.33) -- (137.07,190.8) ;
    		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ]   (197.33,104.33) -- (197.73,190.8) ;
    		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ]   (223.33,92.33) -- (223.73,178.8) ;
    		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ]   (251.33,81.67) -- (251.73,168.13) ;
    		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ]   (278.67,70.33) -- (279.07,156.8) ;
    		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.44 ]   (157.33,86.35) .. controls (158.21,85.7) and (159.93,84.62) .. (163.82,85.15) .. controls (167.7,85.69) and (168.92,87.52) .. (171.04,87.44) .. controls (173.17,87.36) and (177.71,84.79) .. (182.56,84.94) .. controls (187.42,85.09) and (187.01,87.3) .. (190.86,87.44) .. controls (194.71,87.59) and (196.63,85.05) .. (200.45,84.65) .. controls (204.28,84.25) and (211.51,88.11) .. (212.4,87.44) ;
    		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.66 ]   (182.33,81.02) .. controls (183.21,80.37) and (184.93,79.28) .. (188.82,79.82) .. controls (192.7,80.35) and (193.92,82.19) .. (196.04,82.11) .. controls (198.17,82.03) and (202.71,79.45) .. (207.56,79.6) .. controls (212.42,79.76) and (212.01,81.96) .. (215.86,82.11) .. controls (219.71,82.25) and (221.63,79.72) .. (225.45,79.32) .. controls (229.28,78.92) and (236.51,82.77) .. (237.4,82.11) ;
    		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.66 ]   (203.57,87.53) .. controls (204.44,86.87) and (206.17,85.79) .. (210.05,86.33) .. controls (213.94,86.86) and (215.15,88.7) .. (217.28,88.62) .. controls (219.41,88.54) and (223.95,85.96) .. (228.8,86.11) .. controls (233.65,86.26) and (233.25,88.47) .. (237.1,88.62) .. controls (240.95,88.76) and (242.86,86.23) .. (246.69,85.83) .. controls (250.51,85.43) and (257.75,89.28) .. (258.64,88.62) ;
    		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.66 ]   (226.33,93.02) .. controls (227.21,92.37) and (228.93,91.28) .. (232.82,91.82) .. controls (236.7,92.35) and (237.92,94.19) .. (240.04,94.11) .. controls (242.17,94.03) and (246.71,91.45) .. (251.56,91.6) .. controls (256.42,91.76) and (256.01,93.96) .. (259.86,94.11) .. controls (263.71,94.25) and (265.63,91.72) .. (269.45,91.32) .. controls (273.28,90.92) and (280.51,94.77) .. (281.4,94.11) ;
    		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.66 ]   (230.67,99.69) .. controls (231.54,99.03) and (233.27,97.95) .. (237.15,98.49) .. controls (241.03,99.02) and (242.25,100.85) .. (244.38,100.77) .. controls (246.5,100.7) and (251.04,98.12) .. (255.9,98.27) .. controls (260.75,98.42) and (260.35,100.63) .. (264.2,100.77) .. controls (268.05,100.92) and (269.96,98.38) .. (273.78,97.98) .. controls (277.61,97.58) and (284.85,101.44) .. (285.73,100.77) ;
    		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.66 ]   (133,93.69) .. controls (133.87,93.03) and (135.6,91.95) .. (139.48,92.49) .. controls (143.37,93.02) and (144.58,94.85) .. (146.71,94.77) .. controls (148.84,94.7) and (153.38,92.12) .. (158.23,92.27) .. controls (163.08,92.42) and (162.68,94.63) .. (166.53,94.77) .. controls (170.38,94.92) and (172.29,92.38) .. (176.12,91.98) .. controls (179.94,91.58) and (187.18,95.44) .. (188.07,94.77) ;
    		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.44 ]   (144.52,91.18) .. controls (145.39,90.53) and (147.12,89.45) .. (151,89.98) .. controls (154.89,90.52) and (156.1,92.35) .. (158.23,92.27) .. controls (160.36,92.19) and (164.9,89.61) .. (169.75,89.77) .. controls (174.6,89.92) and (174.2,92.13) .. (178.05,92.27) .. controls (181.9,92.41) and (183.81,89.88) .. (187.64,89.48) .. controls (191.46,89.08) and (198.7,92.93) .. (199.59,92.27) ;
    		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.66 ]   (196.5,90.52) .. controls (197.37,89.86) and (199.1,88.78) .. (202.98,89.31) .. controls (206.86,89.85) and (208.08,91.68) .. (210.21,91.6) .. controls (212.33,91.52) and (216.87,88.95) .. (221.73,89.1) .. controls (226.58,89.25) and (226.18,91.46) .. (230.03,91.6) .. controls (233.88,91.75) and (235.79,89.21) .. (239.61,88.81) .. controls (243.44,88.41) and (250.68,92.27) .. (251.56,91.6) ;
    		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.66 ]   (216,105.29) .. controls (216.87,105.8) and (218.6,106.63) .. (222.48,106.22) .. controls (226.37,105.8) and (227.58,104.4) .. (229.71,104.46) .. controls (231.84,104.52) and (236.38,106.5) .. (241.23,106.38) .. controls (246.08,106.26) and (245.68,104.57) .. (249.53,104.46) .. controls (253.38,104.35) and (255.29,106.29) .. (259.12,106.6) .. controls (262.94,106.91) and (270.18,103.95) .. (271.07,104.46) ;
    		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.66 ]   (178.67,100.69) .. controls (179.54,100.03) and (181.27,98.95) .. (185.15,99.49) .. controls (189.03,100.02) and (190.25,101.85) .. (192.38,101.77) .. controls (194.5,101.7) and (199.04,99.12) .. (203.9,99.27) .. controls (208.75,99.42) and (208.35,101.63) .. (212.2,101.77) .. controls (216.05,101.92) and (217.96,99.38) .. (221.78,98.98) .. controls (225.61,98.58) and (232.85,102.44) .. (233.73,101.77) ;
    		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.44 ]   (142.33,98.02) .. controls (143.21,97.37) and (144.93,96.28) .. (148.82,96.82) .. controls (152.7,97.35) and (153.92,99.19) .. (156.04,99.11) .. controls (158.17,99.03) and (162.71,96.45) .. (167.56,96.6) .. controls (172.42,96.76) and (172.01,98.96) .. (175.86,99.11) .. controls (179.71,99.25) and (181.63,96.72) .. (185.45,96.32) .. controls (189.28,95.92) and (196.51,99.77) .. (197.4,99.11) ;
    		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.66 ]   (117.1,99.44) .. controls (117.98,98.78) and (119.7,97.7) .. (123.59,98.24) .. controls (127.47,98.77) and (128.69,100.6) .. (130.81,100.52) .. controls (132.94,100.45) and (137.48,97.87) .. (142.33,98.02) .. controls (147.19,98.17) and (146.78,100.38) .. (150.63,100.52) .. controls (154.48,100.67) and (156.4,98.13) .. (160.22,97.73) .. controls (164.05,97.33) and (171.29,101.19) .. (172.17,100.52) ;
    		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.66 ]   (104.33,105.02) .. controls (105.21,104.37) and (106.93,103.28) .. (110.82,103.82) .. controls (114.7,104.35) and (115.92,106.19) .. (118.04,106.11) .. controls (120.17,106.03) and (124.71,103.45) .. (129.56,103.6) .. controls (134.42,103.76) and (134.01,105.96) .. (137.86,106.11) .. controls (141.71,106.25) and (143.63,103.72) .. (147.45,103.32) .. controls (151.28,102.92) and (158.51,106.77) .. (159.4,106.11) ;
    		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.66 ]   (90.67,108.69) .. controls (91.54,108.03) and (93.27,106.95) .. (97.15,107.49) .. controls (101.03,108.02) and (102.25,109.85) .. (104.38,109.77) .. controls (106.5,109.7) and (111.04,107.12) .. (115.9,107.27) .. controls (120.75,107.42) and (120.35,109.63) .. (124.2,109.77) .. controls (128.05,109.92) and (129.96,107.38) .. (133.78,106.98) .. controls (137.61,106.58) and (144.85,110.44) .. (145.73,109.77) ;
    		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.66 ]   (78.33,113.69) .. controls (79.21,113.03) and (80.93,111.95) .. (84.82,112.49) .. controls (88.7,113.02) and (89.92,114.85) .. (92.04,114.77) .. controls (94.17,114.7) and (98.71,112.12) .. (103.56,112.27) .. controls (108.42,112.42) and (108.01,114.63) .. (111.86,114.77) .. controls (115.71,114.92) and (117.63,112.38) .. (121.45,111.98) .. controls (125.28,111.58) and (132.51,115.44) .. (133.4,114.77) ;
    		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.66 ]   (72,117.35) .. controls (72.87,116.7) and (74.6,115.62) .. (78.48,116.15) .. controls (82.37,116.69) and (83.58,118.52) .. (85.71,118.44) .. controls (87.84,118.36) and (92.38,115.79) .. (97.23,115.94) .. controls (102.08,116.09) and (101.68,118.3) .. (105.53,118.44) .. controls (109.38,118.59) and (111.29,116.05) .. (115.12,115.65) .. controls (118.94,115.25) and (126.18,119.11) .. (127.07,118.44) ;
    		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.66 ]   (131.67,113.02) .. controls (132.54,112.37) and (134.27,111.28) .. (138.15,111.82) .. controls (142.03,112.35) and (143.25,114.19) .. (145.38,114.11) .. controls (147.5,114.03) and (152.04,111.45) .. (156.9,111.6) .. controls (161.75,111.76) and (161.35,113.96) .. (165.2,114.11) .. controls (169.05,114.25) and (170.96,111.72) .. (174.78,111.32) .. controls (178.61,110.92) and (185.85,114.77) .. (186.73,114.11) ;
    		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.66 ]   (96.67,122.35) .. controls (97.54,121.7) and (99.27,120.62) .. (103.15,121.15) .. controls (107.03,121.69) and (108.25,123.52) .. (110.38,123.44) .. controls (112.5,123.36) and (117.04,120.79) .. (121.9,120.94) .. controls (126.75,121.09) and (126.35,123.3) .. (130.2,123.44) .. controls (134.05,123.59) and (135.96,121.05) .. (139.78,120.65) .. controls (143.61,120.25) and (150.85,124.11) .. (151.73,123.44) ;
    		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.66 ]   (116.33,125.35) .. controls (117.21,124.7) and (118.93,123.62) .. (122.82,124.15) .. controls (126.7,124.69) and (127.92,126.52) .. (130.04,126.44) .. controls (132.17,126.36) and (136.71,123.79) .. (141.56,123.94) .. controls (146.42,124.09) and (146.01,126.3) .. (149.86,126.44) .. controls (153.71,126.59) and (155.63,124.05) .. (159.45,123.65) .. controls (163.28,123.25) and (170.51,127.11) .. (171.4,126.44) ;
    		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.66 ]   (131.33,131.35) .. controls (132.21,130.7) and (133.93,129.62) .. (137.82,130.15) .. controls (141.7,130.69) and (142.92,132.52) .. (145.04,132.44) .. controls (147.17,132.36) and (151.71,129.79) .. (156.56,129.94) .. controls (161.42,130.09) and (161.01,132.3) .. (164.86,132.44) .. controls (168.71,132.59) and (170.63,130.05) .. (174.45,129.65) .. controls (178.28,129.25) and (185.51,133.11) .. (186.4,132.44) ;
    		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.66 ]   (147,119.02) .. controls (147.87,118.37) and (149.6,117.28) .. (153.48,117.82) .. controls (157.37,118.35) and (158.58,120.19) .. (160.71,120.11) .. controls (162.84,120.03) and (167.38,117.45) .. (172.23,117.6) .. controls (177.08,117.76) and (176.68,119.96) .. (180.53,120.11) .. controls (184.38,120.25) and (186.29,117.72) .. (190.12,117.32) .. controls (193.94,116.92) and (201.18,120.77) .. (202.07,120.11) ;
    		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.44 ]   (154.22,106.04) .. controls (155.09,105.38) and (156.82,104.3) .. (160.7,104.83) .. controls (164.58,105.37) and (165.8,107.2) .. (167.93,107.12) .. controls (170.05,107.04) and (174.59,104.47) .. (179.45,104.62) .. controls (184.3,104.77) and (183.9,106.98) .. (187.75,107.12) .. controls (191.6,107.27) and (193.51,104.73) .. (197.33,104.33) .. controls (201.16,103.93) and (208.4,107.79) .. (209.28,107.12) ;
    		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.66 ]   (202.33,111.35) .. controls (203.21,110.7) and (204.93,109.62) .. (208.82,110.15) .. controls (212.7,110.69) and (213.92,112.52) .. (216.04,112.44) .. controls (218.17,112.36) and (222.71,109.79) .. (227.56,109.94) .. controls (232.42,110.09) and (232.01,112.3) .. (235.86,112.44) .. controls (239.71,112.59) and (241.63,110.05) .. (245.45,109.65) .. controls (249.28,109.25) and (256.51,113.11) .. (257.4,112.44) ;
    		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.66 ]   (187.67,117.02) .. controls (188.54,116.37) and (190.27,115.28) .. (194.15,115.82) .. controls (198.03,116.35) and (199.25,118.19) .. (201.38,118.11) .. controls (203.5,118.03) and (208.04,115.45) .. (212.9,115.6) .. controls (217.75,115.76) and (217.35,117.96) .. (221.2,118.11) .. controls (225.05,118.25) and (226.96,115.72) .. (230.78,115.32) .. controls (234.61,114.92) and (241.85,118.77) .. (242.73,118.11) ;
    		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.66 ]   (169.67,122.69) .. controls (170.54,122.03) and (172.27,120.95) .. (176.15,121.49) .. controls (180.03,122.02) and (181.25,123.85) .. (183.38,123.77) .. controls (185.5,123.7) and (190.04,121.12) .. (194.9,121.27) .. controls (199.75,121.42) and (199.35,123.63) .. (203.2,123.77) .. controls (207.05,123.92) and (208.96,121.38) .. (212.78,120.98) .. controls (216.61,120.58) and (223.85,124.44) .. (224.73,123.77) ;
    		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.66 ]   (150.67,138.78) .. controls (151.26,138.24) and (152.44,137.35) .. (155.08,137.79) .. controls (157.72,138.23) and (158.55,139.74) .. (159.99,139.67) .. controls (161.44,139.6) and (164.53,137.49) .. (167.83,137.61) .. controls (171.13,137.74) and (170.86,139.55) .. (173.48,139.67) .. controls (176.1,139.79) and (177.4,137.71) .. (180,137.38) .. controls (182.61,137.05) and (187.53,140.22) .. (188.13,139.67) ;
    		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.66 ]   (173,127.98) .. controls (173.65,127.49) and (174.94,126.68) .. (177.84,127.08) .. controls (180.74,127.48) and (181.65,128.85) .. (183.24,128.79) .. controls (184.83,128.73) and (188.22,126.81) .. (191.85,126.92) .. controls (195.47,127.04) and (195.17,128.69) .. (198.05,128.79) .. controls (200.92,128.9) and (202.35,127.01) .. (205.21,126.71) .. controls (208.06,126.41) and (213.47,129.29) .. (214.13,128.79) ;
    		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.44 ]   (169.67,82.65) .. controls (170.32,82.16) and (171.61,81.35) .. (174.51,81.75) .. controls (177.41,82.15) and (178.32,83.52) .. (179.91,83.46) .. controls (181.5,83.4) and (184.89,81.48) .. (188.51,81.59) .. controls (192.14,81.7) and (191.84,83.35) .. (194.71,83.46) .. controls (197.59,83.57) and (199.02,81.68) .. (201.87,81.38) .. controls (204.73,81.08) and (210.14,83.96) .. (210.8,83.46) ;
    		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.66 ]   (183,76.2) .. controls (183.49,75.83) and (184.45,75.23) .. (186.63,75.53) .. controls (188.8,75.83) and (189.48,76.85) .. (190.67,76.81) .. controls (191.86,76.76) and (194.4,75.32) .. (197.11,75.41) .. controls (199.83,75.49) and (199.6,76.73) .. (201.75,76.81) .. controls (203.91,76.89) and (204.98,75.47) .. (207.12,75.25) .. controls (209.26,75.02) and (213.3,77.18) .. (213.8,76.81) ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.4 ] (303.53,64.23) -- (301.73,96.13) -- (170.67,147) -- (170.67,113) -- cycle ;
    		\\draw    (170,201) -- (170,66.47) ;
    		\\draw [shift={(170,63.47)}, rotate = 90] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (7.14,-3.43) -- (0,0) -- (7.14,3.43) -- (4.74,0) -- cycle    ;
    		\\draw    (170,201) -- (37.29,164.59) ;
    		\\draw [shift={(34.4,163.8)}, rotate = 15.34] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (7.14,-3.43) -- (0,0) -- (7.14,3.43) -- (4.74,0) -- cycle    ;
    		\\draw    (170,201) -- (323.61,140.57) ;
    		\\draw [shift={(326.4,139.47)}, rotate = 158.52] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (7.14,-3.43) -- (0,0) -- (7.14,3.43) -- (4.74,0) -- cycle    ;
    		\\draw  [fill={rgb, 255:red, 220; green, 230; blue, 242 }  ,fill opacity=1 ] (90.3,153.84) -- (96.3,152.07) .. controls (97.96,151.58) and (99.97,153.54) .. (100.79,156.44) .. controls (101.61,159.35) and (100.93,162.1) .. (99.27,162.58) -- (93.27,164.35) .. controls (91.61,164.84) and (89.6,162.88) .. (88.78,159.98) .. controls (87.96,157.08) and (88.64,154.33) .. (90.3,153.84) .. controls (91.95,153.35) and (93.96,155.31) .. (94.78,158.21) .. controls (95.6,161.12) and (94.92,163.86) .. (93.27,164.35) ;
    		\\draw  [fill={rgb, 255:red, 220; green, 230; blue, 242 }  ,fill opacity=1 ] (75.55,160.3) -- (90.39,155.93) .. controls (91.46,155.61) and (92.73,156.84) .. (93.25,158.66) .. controls (93.76,160.49) and (93.32,162.22) .. (92.26,162.53) -- (77.42,166.9) .. controls (76.36,167.21) and (75.08,165.99) .. (74.56,164.16) .. controls (74.05,162.34) and (74.49,160.61) .. (75.55,160.3) .. controls (76.61,159.98) and (77.89,161.21) .. (78.4,163.03) .. controls (78.92,164.86) and (78.48,166.59) .. (77.42,166.9) ;
    		\\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (89.56,151.21) .. controls (90.52,150.25) and (92.08,149.47) .. (93.05,149.47) -- (112.07,149.47) .. controls (113.03,149.47) and (113.04,150.25) .. (112.08,151.21) -- (112.08,151.21) .. controls (111.12,152.18) and (109.56,152.96) .. (108.6,152.96) -- (89.58,152.96) .. controls (88.61,152.96) and (88.61,152.18) .. (89.56,151.21) -- cycle ;
    		\\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (75.32,163.92) .. controls (75.02,162.59) and (75.29,161.4) .. (75.92,161.26) .. controls (76.55,161.12) and (77.3,162.08) .. (77.6,163.41) .. controls (77.9,164.73) and (77.63,165.92) .. (77,166.06) .. controls (76.37,166.21) and (75.62,165.25) .. (75.32,163.92) -- cycle ;
    		\\draw (159.33,205) node [anchor=north west][inner sep=0.75pt]  [font=\\footnotesize]  {$O$};
    		\\draw (34,149) node [anchor=north west][inner sep=0.75pt]    {$x$};
    		\\draw (312.67,125) node [anchor=north west][inner sep=0.75pt]    {$y$};
    		\\draw (153.33,51.33) node [anchor=north west][inner sep=0.75pt]    {$z$};
    		\\draw (150.67,111) node [anchor=north west][inner sep=0.75pt]  [font=\\footnotesize]  {$A$};
    		\\draw (44,71) node [anchor=north west][inner sep=0.75pt]  [font=\\footnotesize]  {$B$};
    		\\draw (186.67,16.33) node [anchor=north west][inner sep=0.75pt]  [font=\\footnotesize]  {$C$};
    		\\draw (303.33,49.67) node [anchor=north west][inner sep=0.75pt]  [font=\\footnotesize]  {$D$};	
    	\\end{tikzpicture}
    \\end{center} ''' 
                     %(xb, yd, za))

    ######################################################################## Nhận biết ############################################
    # Các đáp án
    nb_da_1_d = '\\True Tọa độ điểm $A(0;0;%s), B(%s;0;%s), C(%s;%s;%s), D(0;%s;%s)$' %(za, xb, za, xb, yd, za, yd, za)
    nb_da_1_s = 'Tọa độ điểm $A(%s;0;0), B(%s;%s;0), C(%s;%s;%s), D(0;0;%s)$' %(za, xb, za, xb, yd, za, yd)
    list_nb_da_1=[nb_da_1_d,nb_da_1_s]
    nb_da_1=random.choice(list_nb_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]

    # Nội dung lời giải
    loigiai_nb_1 = ('''Từ giả thiết ta có $A(0;0;%s), B(%s;0;%s), C(%s;%s;%s), D(0;%s;%s)$.''' %(za, xb, za, xb, yd, za, yd, za))

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
    th_da_1_d = '\\True Sức chứa tối đa của bể nước là $%s$ lít' %(v_max) 
    th_da_1_s = 'Sức chứa tối đa của bể nước là $%s$ lít' %(v_max + randint(10, 50))
    list_th_da_1=[th_da_1_d,th_da_1_s]
    th_da_1=random.choice(list_th_da_1)


    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]

    # Nội dung lời giải
    loigiai_th_1 = ('''Thể tích của bể là $V = %s \\cdot %s \\cdot %s = %s \\text{ (dm}^3\\text{)} = %s \\text{ (lít)}$. \\\\
    Sức chứa tối đa của bể nước là $%s$ lít.'''       
               %(xb, yd, za, v_max, v_max, v_max))

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
    # Formatting cos alpha
    if sqrt(den_sq).is_integer:
        cos_str = latex(Rational(num, sqrt(den_sq)))
    else:
        # try to simplify
        cos_str = "\\frac{%s}{\\sqrt{%s}}" %(num, den_sq)
        # better to just format directly as requested format doesn't need perfect simplification

    vd_da_1_d = '\\True Giả sử $\\alpha$ là góc giữa hai vectơ $\\overrightarrow{OB}, \\overrightarrow{OD}$ thì $\\cos \\alpha = %s$' %(cos_str)  
    vd_da_1_s = 'Giả sử $\\alpha$ là góc giữa hai vectơ $\\overrightarrow{OB}, \\overrightarrow{OD}$ thì $\\cos \\alpha = \\frac{%s}{\\sqrt{%s}}$' %(num+1, den_sq)  
    list_vd_da_1=[vd_da_1_d,vd_da_1_s]
    vd_da_1=random.choice(list_vd_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]

    # Nội dung lời giải
    loigiai_vd_1 = ('''Ta có $\\overrightarrow{OB} = (%s;0;%s), \\overrightarrow{OD} = (0;%s;%s)$. \\\\
                    $\\cos \\alpha = \\cos \\left(\\overrightarrow{OB}, \\overrightarrow{OD}\\right) = \\frac{\\overrightarrow{OB} \\cdot \\overrightarrow{OD}}{|\\overrightarrow{OB}| \\cdot |\\overrightarrow{OD}|} = \\frac{%s \\cdot 0 + 0 \\cdot %s + %s \\cdot %s}{\\sqrt{%s^2 + 0^2 + %s^2} \\cdot \\sqrt{0^2 + %s^2 + %s^2}} = %s$.'''  
               %(xb, za, yd, za, xb, yd, za, za, xb, za, yd, za, cos_str))

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
    cach_mieng_sai = round(float(cach_mieng) + 0.5, 2)
    cach_mieng_sai_str = f"{cach_mieng_sai:.2f}".replace('.', ',')
    if cach_mieng_sai_str.endswith(',00'):
        cach_mieng_sai_str = cach_mieng_sai_str[:-3]

    # Các đáp án
    vdc_da_1_d = '\\True Ban đầu nước đầy bể, người ta xả nước sao cho thể tích nước trong bể giảm $%s \\text{ dm}^3$/phút. Sau $%s$ phút thì mực nước trong bể cách miệng bể $%s$ dm' %(giam, tg, cach_mieng_str) 
    vdc_da_1_s = 'Ban đầu nước đầy bể, người ta xả nước sao cho thể tích nước trong bể giảm $%s \\text{ dm}^3$/phút. Sau $%s$ phút thì mực nước trong bể cách miệng bể $%s$ dm' %(giam, tg, cach_mieng_sai_str) 
    list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
    vdc_da_1=random.choice(list_vdc_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]

    # Nội dung lời giải
    loigiai_vdc_1 = ('''Thể tích nước đã xả là $V_1 = %s \\cdot %s = %s \\text{ (dm}^3\\text{)}$. \\\\
                        Thể tích nước còn lại trong bể là $V_2 = %s - %s = %s \\text{ (dm}^3\\text{)}$. \\\\
                        Chiều cao mực nước còn lại là $h = \\frac{V_2}{x_B \\cdot y_D} = \\frac{%s}{%s \\cdot %s} \\approx %s \\text{ (dm)}$. \\\\
                        Mực nước cách miệng bể là $d = %s - h \\approx %s - %s = %s \\text{ (dm)}$.'''
                %(giam, tg, v_xa, v_max, v_xa, v_con_lai, v_con_lai, xb, yd, h_con_lai_str, za, za, h_con_lai_str, cach_mieng_str))

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
        '\\end{ex}\n \\end{minipage}\n\n')
    return content


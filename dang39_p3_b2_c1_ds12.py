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


def bt_dang39_p3_b2_c1_ds12(self):
            # Khai báo biến
            # Các bộ dữ liệu được tính toán cẩn thận để đảm bảo kết quả ra số nguyên đẹp (P0, t1, P1, c, a, b)
            data_list = [
                (800, 3, 6000, 8000, 9, 3),   # Dữ liệu gốc của bài toán
                (1000, 1, 1800, 9000, 8, 2),
                (1000, 2, 3000, 9000, 8, 2),
                (500, 2, 1700, 8500, 16, 2),
                (1000, 1, 3400, 17000, 16, 4),
                (500, 2, 1500, 4500, 8, 2)
            ]

            P0, t1, P1, c, a, b = random.choice(data_list)

            # Các thông số phụ phục vụ quá trình giải chi tiết
            a_plus_1 = a + 1
            cp1_frac = Rational(c, P1)
            cp1_minus_1_frac = cp1_frac - 1
            b_pow_frac = cp1_minus_1_frac / a

            # t_m là thời điểm tốc độ tăng trưởng đạt cực đại
            t_m = int(math.log(a, b))

            # Tốc độ tăng trưởng tối đa: v_max = (c * ln(b)) / 4
            v_max = (c * math.log(b)) / 4
            kq = round(v_max)

            # Các đáp án trắc nghiệm
            du = ['$%s$'%(kq)]
            da = random.choice(du)

            # Tạo các phương án sai (đảm bảo không bao giờ trùng nhau và không trùng đáp án đúng)
            sai_set = set([kq + 1, kq + 2, kq + 3, kq - 1, kq - 2, kq - 3, kq + 10, kq - 10])
            s = ['$%s$'%(latex(val)).replace('.',',') for val in sai_set if val != kq]
            random.shuffle(s)

            das1 = s[0]
            das2 = s[1]
            das3 = s[2]

            hinhve=r'''\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.08 ] (249.4,187.4) .. controls (269.4,177.4) and (323.4,146.9) .. (303.4,166.9) .. controls (283.4,186.9) and (301.4,198.9) .. (271.4,209.4) .. controls (241.4,219.9) and (174.4,222.4) .. (177.9,204.9) .. controls (181.4,187.4) and (229.4,197.4) .. (249.4,187.4) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.22 ][fill={rgb, 255:red, 48; green, 84; blue, 83 }  ,fill opacity=1 ] (265.52,138) .. controls (270.72,132.4) and (283.92,118.8) .. (295.12,121.78) .. controls (292.72,132.4) and (279.52,139.6) .. (265.52,138) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.22 ][fill={rgb, 255:red, 48; green, 84; blue, 83 }  ,fill opacity=1 ] (245.2,91.2) .. controls (249.52,98) and (252.49,96.02) .. (259.52,96.18) .. controls (247.52,134.8) and (257.31,135.81) .. (241.12,152) .. controls (221.12,122) and (235.12,98.4) .. (245.2,91.2) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.22 ][fill={rgb, 255:red, 48; green, 84; blue, 83 }  ,fill opacity=1 ] (256.24,21.6) .. controls (271.44,32) and (271.84,39.2) .. (275.92,52.8) .. controls (264.64,56.4) and (269.44,63.6) .. (269.84,67.6) .. controls (257.44,58.8) and (251.84,64.8) .. (241.37,46.03) .. controls (248.17,44.66) and (254.55,45.2) .. (259.84,48.4) .. controls (254.24,40.8) and (253.44,29.6) .. (256.24,21.6) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.22 ][fill={rgb, 255:red, 198; green, 218; blue, 210 }  ,fill opacity=1 ] (268.32,66.4) .. controls (265.52,58.4) and (273.12,47.2) .. (275.92,52.8) .. controls (334.32,153.2) and (175.52,206) .. (155.52,176) .. controls (220.72,98.8) and (290.72,108.4) .. (268.32,66.4) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 106; green, 179; blue, 163 }  ,fill opacity=1 ] (275.92,52.8) .. controls (294.32,116.8) and (248.72,111.6) .. (228.72,131.6) .. controls (218,142.32) and (216.7,147.64) .. (219.72,153.9) .. controls (215.18,149.08) and (211.14,148.53) .. (207.92,150.39) .. controls (210.08,152.7) and (211.13,154.83) .. (211.41,156.82) .. controls (201.63,151.6) and (197.3,152.34) .. (195.9,155.65) .. controls (198.16,156.98) and (199.64,158.56) .. (200.57,160.26) .. controls (180.72,150.8) and (182.32,162) .. (164.72,166.4) .. controls (242.32,85.2) and (278.72,123.6) .. (275.92,52.8) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 244; green, 243; blue, 216 }  ,fill opacity=1 ] (285.92,83.2) .. controls (291.52,108.4) and (279.92,131.6) .. (256.72,152.4) .. controls (243.52,152.4) and (239.12,156.8) .. (229.52,158.8) .. controls (227.64,158.01) and (227.12,155.6) .. (223.52,152.4) .. controls (245.52,115.2) and (273.92,144.4) .. (285.92,83.2) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.22 ][fill={rgb, 255:red, 48; green, 84; blue, 83 }  ,fill opacity=1 ] (229.52,158.8) .. controls (234.72,153.2) and (260.32,150.4) .. (271.52,153.38) .. controls (269.7,161.44) and (243.51,169.88) .. (231.52,166.4) .. controls (227.72,165.3) and (230.87,162.56) .. (229.52,158.8) -- cycle ;
            	\draw [color={rgb, 255:red, 48; green, 84; blue, 83 }  ,draw opacity=0.82 ]   (219.52,151.6) .. controls (230.72,158.8) and (221.52,174.8) .. (205.92,176.8) ;
            	\draw [color={rgb, 255:red, 48; green, 84; blue, 83 }  ,draw opacity=0.61 ]   (209.12,155.2) .. controls (218.32,163.6) and (215.92,172.8) .. (205.92,176.8) ;
            	\draw [color={rgb, 255:red, 48; green, 84; blue, 83 }  ,draw opacity=0.63 ]   (200.57,160.26) .. controls (207.3,164.05) and (206.72,173.6) .. (193.52,178) ;
            	\draw [color={rgb, 255:red, 48; green, 84; blue, 83 }  ,draw opacity=0.59 ]   (186.72,177.6) .. controls (180.32,181.2) and (164,180.35) .. (158,173.55) ;
            	\draw [color={rgb, 255:red, 48; green, 84; blue, 83 }  ,draw opacity=0.67 ]   (186.72,177.6) .. controls (183.52,167.2) and (176.32,181.6) .. (170.32,174.8) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 244; green, 243; blue, 216 }  ,fill opacity=1 ] (193.52,178) .. controls (196.02,172) and (198.8,175.05) .. (195.57,166.9) .. controls (194.3,164.8) and (192.55,162.3) .. (197.51,160) .. controls (204.8,162.8) and (206.52,171.75) .. (193.52,178) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.36 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (181.21,162.58) .. controls (183.66,161.04) and (186.63,161.33) .. (187.84,163.25) .. controls (189.05,165.16) and (188.04,167.97) .. (185.59,169.52) .. controls (183.14,171.06) and (180.17,170.77) .. (178.96,168.85) .. controls (177.75,166.94) and (178.76,164.13) .. (181.21,162.58) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (183.59,161.93) .. controls (185.26,160.87) and (187.36,161.18) .. (188.26,162.61) .. controls (189.17,164.05) and (188.54,166.07) .. (186.86,167.13) .. controls (185.19,168.19) and (183.09,167.88) .. (182.19,166.45) .. controls (181.28,165.01) and (181.91,162.99) .. (183.59,161.93) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (182.04,163.9) .. controls (183.43,163.02) and (185.17,163.28) .. (185.91,164.46) .. controls (186.66,165.65) and (186.15,167.32) .. (184.76,168.2) .. controls (183.37,169.08) and (181.63,168.82) .. (180.89,167.64) .. controls (180.14,166.45) and (180.65,164.78) .. (182.04,163.9) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (181.77,164.07) .. controls (182.46,163.63) and (183.33,163.76) .. (183.7,164.35) .. controls (184.08,164.95) and (183.82,165.78) .. (183.13,166.22) .. controls (182.43,166.66) and (181.56,166.53) .. (181.19,165.94) .. controls (180.82,165.35) and (181.07,164.51) .. (181.77,164.07) -- cycle ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ][line width=1.5]    (194.33,143.33) .. controls (204.47,129.4) and (228.13,120.4) .. (240.8,113.07) ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0 ][fill={rgb, 255:red, 48; green, 84; blue, 83 }  ,fill opacity=1 ] (275.92,52.8) .. controls (282.32,95.2) and (276.72,100.8) .. (227.92,125.6) .. controls (197.12,145.2) and (225.12,149.6) .. (219.52,151.6) .. controls (198.72,135.2) and (191.52,153.2) .. (170.72,160.8) .. controls (237.12,95.2) and (285.52,116.8) .. (275.92,52.8) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ][fill={rgb, 255:red, 198; green, 218; blue, 210 }  ,fill opacity=1 ] (150.67,158.7) .. controls (150.67,156.51) and (152.44,154.73) .. (154.63,154.73) .. controls (156.82,154.73) and (158.6,156.51) .. (158.6,158.7) .. controls (158.6,160.89) and (156.82,162.67) .. (154.63,162.67) .. controls (152.44,162.67) and (150.67,160.89) .. (150.67,158.7) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.61 ] (151.13,158.31) .. controls (151.13,156.54) and (152.57,155.1) .. (154.34,155.1) .. controls (156.11,155.1) and (157.54,156.54) .. (157.54,158.31) .. controls (157.54,160.08) and (156.11,161.51) .. (154.34,161.51) .. controls (152.57,161.51) and (151.13,160.08) .. (151.13,158.31) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.61 ] (151.61,157.52) .. controls (151.61,156.27) and (152.62,155.26) .. (153.86,155.26) .. controls (155.11,155.26) and (156.11,156.27) .. (156.11,157.52) .. controls (156.11,158.76) and (155.11,159.77) .. (153.86,159.77) .. controls (152.62,159.77) and (151.61,158.76) .. (151.61,157.52) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.44 ] (151.34,160.61) .. controls (151.34,159.47) and (152.82,158.55) .. (154.63,158.55) .. controls (156.45,158.55) and (157.92,159.47) .. (157.92,160.61) .. controls (157.92,161.75) and (156.45,162.67) .. (154.63,162.67) .. controls (152.82,162.67) and (151.34,161.75) .. (151.34,160.61) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ][fill={rgb, 255:red, 198; green, 218; blue, 210 }  ,fill opacity=1 ] (156,149.87) .. controls (156,147.4) and (158,145.4) .. (160.47,145.4) .. controls (162.93,145.4) and (164.93,147.4) .. (164.93,149.87) .. controls (164.93,152.33) and (162.93,154.33) .. (160.47,154.33) .. controls (158,154.33) and (156,152.33) .. (156,149.87) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.61 ] (156.52,149.43) .. controls (156.52,147.43) and (158.14,145.82) .. (160.13,145.82) .. controls (162.13,145.82) and (163.74,147.43) .. (163.74,149.43) .. controls (163.74,151.42) and (162.13,153.04) .. (160.13,153.04) .. controls (158.14,153.04) and (156.52,151.42) .. (156.52,149.43) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.61 ] (157.06,148.53) .. controls (157.06,147.13) and (158.2,146) .. (159.6,146) .. controls (161,146) and (162.13,147.13) .. (162.13,148.53) .. controls (162.13,149.93) and (161,151.07) .. (159.6,151.07) .. controls (158.2,151.07) and (157.06,149.93) .. (157.06,148.53) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.44 ] (156.76,152.02) .. controls (156.76,150.74) and (158.42,149.7) .. (160.47,149.7) .. controls (162.51,149.7) and (164.17,150.74) .. (164.17,152.02) .. controls (164.17,153.3) and (162.51,154.33) .. (160.47,154.33) .. controls (158.42,154.33) and (156.76,153.3) .. (156.76,152.02) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ][fill={rgb, 255:red, 198; green, 218; blue, 210 }  ,fill opacity=1 ] (141.67,142.7) .. controls (141.67,139.96) and (143.89,137.73) .. (146.63,137.73) .. controls (149.38,137.73) and (151.6,139.96) .. (151.6,142.7) .. controls (151.6,145.44) and (149.38,147.67) .. (146.63,147.67) .. controls (143.89,147.67) and (141.67,145.44) .. (141.67,142.7) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.61 ] (142.25,142.21) .. controls (142.25,139.99) and (144.05,138.2) .. (146.26,138.2) .. controls (148.48,138.2) and (150.28,139.99) .. (150.28,142.21) .. controls (150.28,144.43) and (148.48,146.22) .. (146.26,146.22) .. controls (144.05,146.22) and (142.25,144.43) .. (142.25,142.21) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.61 ] (142.85,141.22) .. controls (142.85,139.66) and (144.11,138.4) .. (145.67,138.4) .. controls (147.22,138.4) and (148.49,139.66) .. (148.49,141.22) .. controls (148.49,142.77) and (147.22,144.04) .. (145.67,144.04) .. controls (144.11,144.04) and (142.85,142.77) .. (142.85,141.22) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.44 ] (142.51,145.09) .. controls (142.51,143.67) and (144.36,142.51) .. (146.63,142.51) .. controls (148.91,142.51) and (150.75,143.67) .. (150.75,145.09) .. controls (150.75,146.51) and (148.91,147.67) .. (146.63,147.67) .. controls (144.36,147.67) and (142.51,146.51) .. (142.51,145.09) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ][fill={rgb, 255:red, 198; green, 218; blue, 210 }  ,fill opacity=1 ] (158.67,135.27) .. controls (158.67,132.47) and (160.94,130.2) .. (163.73,130.2) .. controls (166.53,130.2) and (168.8,132.47) .. (168.8,135.27) .. controls (168.8,138.06) and (166.53,140.33) .. (163.73,140.33) .. controls (160.94,140.33) and (158.67,138.06) .. (158.67,135.27) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.61 ] (159.26,134.77) .. controls (159.26,132.51) and (161.09,130.67) .. (163.36,130.67) .. controls (165.62,130.67) and (167.45,132.51) .. (167.45,134.77) .. controls (167.45,137.03) and (165.62,138.86) .. (163.36,138.86) .. controls (161.09,138.86) and (159.26,137.03) .. (159.26,134.77) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.61 ] (159.87,133.75) .. controls (159.87,132.16) and (161.16,130.88) .. (162.75,130.88) .. controls (164.34,130.88) and (165.62,132.16) .. (165.62,133.75) .. controls (165.62,135.34) and (164.34,136.63) .. (162.75,136.63) .. controls (161.16,136.63) and (159.87,135.34) .. (159.87,133.75) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.44 ] (159.53,137.71) .. controls (159.53,136.25) and (161.41,135.08) .. (163.73,135.08) .. controls (166.05,135.08) and (167.94,136.25) .. (167.94,137.71) .. controls (167.94,139.16) and (166.05,140.33) .. (163.73,140.33) .. controls (161.41,140.33) and (159.53,139.16) .. (159.53,137.71) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ][fill={rgb, 255:red, 198; green, 218; blue, 210 }  ,fill opacity=1 ] (145.8,128.1) .. controls (145.8,125.21) and (148.14,122.87) .. (151.03,122.87) .. controls (153.92,122.87) and (156.27,125.21) .. (156.27,128.1) .. controls (156.27,130.99) and (153.92,133.33) .. (151.03,133.33) .. controls (148.14,133.33) and (145.8,130.99) .. (145.8,128.1) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.61 ] (146.41,127.58) .. controls (146.41,125.25) and (148.31,123.36) .. (150.64,123.36) .. controls (152.98,123.36) and (154.87,125.25) .. (154.87,127.58) .. controls (154.87,129.92) and (152.98,131.81) .. (150.64,131.81) .. controls (148.31,131.81) and (146.41,129.92) .. (146.41,127.58) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.61 ] (147.04,126.54) .. controls (147.04,124.9) and (148.37,123.56) .. (150.01,123.56) .. controls (151.66,123.56) and (152.99,124.9) .. (152.99,126.54) .. controls (152.99,128.18) and (151.66,129.51) .. (150.01,129.51) .. controls (148.37,129.51) and (147.04,128.18) .. (147.04,126.54) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.44 ] (146.69,130.62) .. controls (146.69,129.12) and (148.64,127.9) .. (151.03,127.9) .. controls (153.43,127.9) and (155.37,129.12) .. (155.37,130.62) .. controls (155.37,132.12) and (153.43,133.33) .. (151.03,133.33) .. controls (148.64,133.33) and (146.69,132.12) .. (146.69,130.62) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ][fill={rgb, 255:red, 198; green, 218; blue, 210 }  ,fill opacity=1 ] (150.67,168.4) .. controls (150.67,167.11) and (151.71,166.07) .. (153,166.07) .. controls (154.29,166.07) and (155.33,167.11) .. (155.33,168.4) .. controls (155.33,169.69) and (154.29,170.73) .. (153,170.73) .. controls (151.71,170.73) and (150.67,169.69) .. (150.67,168.4) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.61 ] (150.94,168.17) .. controls (150.94,167.13) and (151.78,166.28) .. (152.83,166.28) .. controls (153.87,166.28) and (154.71,167.13) .. (154.71,168.17) .. controls (154.71,169.21) and (153.87,170.06) .. (152.83,170.06) .. controls (151.78,170.06) and (150.94,169.21) .. (150.94,168.17) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.61 ] (151.22,167.7) .. controls (151.22,166.97) and (151.81,166.38) .. (152.55,166.38) .. controls (153.28,166.38) and (153.87,166.97) .. (153.87,167.7) .. controls (153.87,168.44) and (153.28,169.03) .. (152.55,169.03) .. controls (151.81,169.03) and (151.22,168.44) .. (151.22,167.7) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.44 ] (151.06,169.52) .. controls (151.06,168.85) and (151.93,168.31) .. (153,168.31) .. controls (154.07,168.31) and (154.94,168.85) .. (154.94,169.52) .. controls (154.94,170.19) and (154.07,170.73) .. (153,170.73) .. controls (151.93,170.73) and (151.06,170.19) .. (151.06,169.52) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.08 ] (243.9,187.9) .. controls (263.9,177.9) and (307.9,160.4) .. (287.9,180.4) .. controls (267.9,200.4) and (293.4,193.4) .. (263.4,203.9) .. controls (233.4,214.4) and (170.4,208.4) .. (185.4,202.4) .. controls (200.4,196.4) and (223.9,197.9) .. (243.9,187.9) -- cycle ;
            \end{tikzpicture}'''

            # Câu hỏi
            noidungcauhoi = (r'''\immini{Một hồ nước ở Bắc Ontario đã phục hồi sau một vụ tràn axít khiến tất cả cá hồi ở đó chết. Một chương trình tái thả cá đã thả $%s$ con cá hồi vào hồ. $%s$ năm sau, số lượng được ước tính là $%s$ con. Sức chứa của hồ được cho là $%s$ con. Để đánh giá khả năng tăng trưởng, người ta mô phỏng số lượng cá trong hồ qua từng năm thông qua hàm số $P(t) = \frac{c}{1 + a \cdot b^{-t}}$ ($a, b, c \in \mathbb{R}$) (trong đó $t$ tính theo năm kể từ lúc bắt đầu thả cá vào hồ). Sử dụng mô hình trên, hãy tính tốc độ tăng trưởng tối đa (đơn vị con/năm) của đàn cá (kết quả làm tròn đến hàng đơn vị).}{%s}'''
                             %(latex(P0), latex(t1), latex(P1), latex(c),hinhve))

            # Các đáp án
            da_d = ('\\True ' +str(da))
            da_s1 = str(das1)
            da_s2 = str(das2) 
            da_s3 = str(das3) 

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_d,da_s1,da_s2,da_s3]
            random.shuffle(list_1)

            # Nội dung lời giải sử dụng phương pháp Khảo sát hàm số (Đạo hàm)
            loigiai = ('''Ta có hàm số mô phỏng số lượng cá là $P(t) = \\frac{c}{1 + a \\cdot b^{-t}}$. \\\\
            Theo giả thiết, sức chứa của hồ là $c = %s$. Suy ra $P(t) = \\frac{%s}{1 + a \\cdot b^{-t}}$. \\\\
            Ban đầu thả $%s$ con cá, tức là $P(0) = %s \\Rightarrow \\frac{%s}{1 + a} = %s \\Rightarrow 1 + a = %s \\Rightarrow a = %s$. \\\\
            Sau $%s$ năm, số cá là $%s$, tức là $P(%s) = %s \\Rightarrow \\frac{%s}{1 + %s \\cdot b^{-%s}} = %s \\Rightarrow 1 + %s \\cdot b^{-%s} = %s \\Rightarrow %s \\cdot b^{-%s} = %s \\Rightarrow b^{-%s} = %s \\Rightarrow b = %s$. \\\\
            Vậy mô hình số lượng cá là $P(t) = \\frac{%s}{1 + %s \\cdot %s^{-t}}$. \\\\
            Tốc độ tăng trưởng của đàn cá là đạo hàm của số lượng cá theo thời gian $t$: \\\\
            $v(t) = P'(t) = \\frac{ %s \\cdot %s^{-t} \\cdot \\ln %s }{ \\left( 1 + %s \\cdot %s^{-t} \\right)^2 }$. \\\\
            Xét hàm số $v(t)$, ta tính đạo hàm $v'(t)$: \\\\
            $v'(t) = \\frac{ %s \\cdot (\\ln %s)^2 \\cdot %s^{-t} \\cdot (%s \\cdot %s^{-t} - 1) }{ \\left( 1 + %s \\cdot %s^{-t} \\right)^3 }$. \\\\
            Cho $v'(t) = 0 \\Leftrightarrow %s \\cdot %s^{-t} - 1 = 0 \\Leftrightarrow %s^{-t} = \\frac{1}{%s} \\Leftrightarrow t = \\log_{%s}(%s) = %s$. \\\\
            Dựa vào sự đổi dấu của $v'(t)$, ta có bảng biến thiên chỉ ra $v'(t)$ đổi dấu từ dương sang âm khi qua $t = %s$. Do đó $v(t)$ đạt giá trị lớn nhất tại $t = %s$. \\\\
            Tốc độ tăng trưởng tối đa là: \\\\
            $v_{max} = v(%s) = \\frac{ %s \\cdot \\frac{1}{%s} \\cdot \\ln %s }{ \\left( 1 + %s \\cdot \\frac{1}{%s} \\right)^2 } = \\frac{ %s \\ln %s }{ 4 } \\approx %s$ (con/năm).'''
            %(
            latex(c), latex(c), 
            latex(P0), latex(P0), latex(c), latex(P0), latex(a_plus_1), latex(a), 
            latex(t1), latex(P1), latex(t1), latex(P1), latex(c), latex(a), latex(t1), latex(P1), 
            latex(a), latex(t1), latex(cp1_frac), latex(a), latex(t1), latex(cp1_minus_1_frac), latex(t1), latex(b_pow_frac), latex(b), 
            latex(c), latex(a), latex(b), 
            latex(c * a), latex(b), latex(b), latex(a), latex(b), 
            latex(c * a), latex(b), latex(b), latex(a), latex(b), latex(a), latex(b), 
            latex(a), latex(b), latex(b), latex(a), latex(b), latex(a), latex(t_m), 
            latex(t_m), latex(t_m), 
            latex(t_m), latex(c * a), latex(a), latex(b), latex(a), latex(a), latex(c), latex(b), latex(kq)
            ))
            dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                       '\\loigiai{\n'+str(loigiai)+'\n}\n'
                       '\\end{ex}\n\\end{minipage} \n\n')
            return content


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


def bt_dang55_p3_b2_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random các số liệu của bài toán
                a = random.choice([3, 4, 5, 6, 7]) # Vận tốc dòng nước
                S = random.choice([40, 50, 60, 80, 100, 120]) # Quãng đường AB
                L0 = 10 # Cố định lượng nhiên liệu thử nghiệm 
                v0 = random.choice([10, 20]) # Cố định 2 mốc tốc độ thử nghiệm để k chẵn đẹp

                # Tính k_den tức là mẫu số của k = 1 / k_den
                k_den = (v0**2) // L0 

                # Tính các hệ số thu gọn cho phương trình
                M_val = S / k_den
                if int(M_val) == M_val:
                    M_str = str(int(M_val))
                else:
                    M_str = str(M_val).replace('.', ',')

                C_val = 2 * M_val
                if int(C_val) == C_val:
                    C_str = str(int(C_val))
                else:
                    C_str = str(C_val).replace('.', ',')

                a_sq = a**2
                three_a_sq = 3 * a_sq

                # Tính toán kết quả chính xác và xấp xỉ
                v_exact_latex = '%s\\sqrt{3}' % (a)
                v_approx = a * math.sqrt(3)
                v_approx_dec = Decimal(float(v_approx)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                v_approx_str = str(v_approx_dec).replace('.', ',')

                # Đáp án đúng
                du = ['$%s$' % (v_approx_str)]
                da = random.choice(du)

                # Tạo các phương án nhiễu
                s1_val = a * math.sqrt(2)
                s1_str = str(Decimal(float(s1_val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')

                s2_val = a * math.sqrt(5)
                s2_str = str(Decimal(float(s2_val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')

                s3_val = v_approx + random.choice([-2.5, -1.5, 1.5, 2.5])
                s3_str = str(Decimal(float(s3_val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')

                # Lọc đáp án sai, đảm bảo không trùng với đáp án đúng và không trùng nhau
                s_raw = ['$%s$' % s1_str, '$%s$' % s2_str, '$%s$' % s3_str]
                s = []
                for opt in s_raw:
                    if opt not in s and opt != da:
                        s.append(opt)

                # Bổ sung nhiễu nếu bị trùng
                while len(s) < 3:
                    s_val = v_approx + random.choice([-3.1, 4.2, 5.3, 6.1])
                    s_opt = '$' + str(Decimal(float(s_val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',') + '$'
                    if s_opt not in s and s_opt != da:
                        s.append(s_opt)

                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]
                hinhve=r'''\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-0.5,xscale=0.5]
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (280.15,108.18) .. controls (280.15,106.67) and (281.38,105.44) .. (282.89,105.44) -- (299.66,105.44) .. controls (301.18,105.44) and (302.4,106.67) .. (302.4,108.18) -- (302.4,110.92) .. controls (302.4,110.92) and (302.4,110.92) .. (302.4,110.92) -- (280.15,110.92) .. controls (280.15,110.92) and (280.15,110.92) .. (280.15,110.92) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (278.6,93.99) .. controls (278.6,90.85) and (281.04,88.31) .. (284.05,88.31) .. controls (287.06,88.31) and (289.5,90.85) .. (289.5,93.99) .. controls (289.5,97.14) and (287.06,99.68) .. (284.05,99.68) .. controls (281.04,99.68) and (278.6,97.14) .. (278.6,93.99) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (186.24,98.96) -- (180.5,110.65) -- (176.5,111.15) -- (182.24,98.56) -- (176.64,69.36) -- (179.04,68.16) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (217.55,83.45) -- (193.55,88.15) -- (162.85,83.45) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (193.3,68.15) -- (192.8,69.9) -- (188.3,70.9) -- (186.3,68.15) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ,even odd rule] (477.97,181.33) .. controls (477.97,180.21) and (478.88,179.31) .. (480,179.31) .. controls (481.12,179.31) and (482.03,180.21) .. (482.03,181.33) .. controls (482.03,182.45) and (481.12,183.36) .. (480,183.36) .. controls (478.88,183.36) and (477.97,182.45) .. (477.97,181.33)(476.67,181.33) .. controls (476.67,179.49) and (478.16,178) .. (480,178) .. controls (481.84,178) and (483.33,179.49) .. (483.33,181.33) .. controls (483.33,183.17) and (481.84,184.67) .. (480,184.67) .. controls (478.16,184.67) and (476.67,183.17) .. (476.67,181.33) ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (407.46,141.79) -- (494.37,134.07) -- (494.31,133.34) -- (407.4,141.07) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (138.9,121.9) .. controls (138.9,118.4) and (126.87,117.84) .. (124.26,115.91) .. controls (124.13,114.68) and (124.05,113.48) .. (124.04,112.33) .. controls (195.33,111.33) and (290,104) .. (326,113.67) .. controls (326.33,114.35) and (326.49,115.02) .. (326.51,115.67) .. controls (322.76,115.33) and (317.27,116.65) .. (310.7,117.4) .. controls (310.95,118.98) and (311.94,119.22) .. (312.2,119.9) .. controls (325.95,130.52) and (335.83,138.78) .. (341.55,145.65) .. controls (648.88,167.58) and (163.67,170.82) .. (122.7,167.15) .. controls (124.47,161.14) and (125.05,156.52) .. (126.7,151.65) .. controls (127.95,149.9) and (130.31,148.96) .. (130.67,147.89) .. controls (133.23,140.4) and (135.83,132.79) .. (138.9,121.9) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (29.5,179.5) .. controls (197.4,174.4) and (379.9,166.4) .. (497.4,161.4) .. controls (483.9,175.9) and (457.08,197.76) .. (445.4,207.4) .. controls (416.4,232.4) and (373.77,227.17) .. (311.4,226.9) .. controls (215.25,226.48) and (95.54,217.36) .. (36.4,211.9) .. controls (32.4,189.9) and (33.4,196.9) .. (29.5,179.5) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 22; green, 48; blue, 120 }  ,fill opacity=1 ] (33.9,200.4) .. controls (185.4,204.4) and (327.4,209.4) .. (445.4,207.4) .. controls (434.4,214.9) and (457.08,197.76) .. (445.4,207.4) .. controls (416.4,232.4) and (373.77,227.17) .. (311.4,226.9) .. controls (215.25,226.48) and (95.54,217.36) .. (36.4,211.9) .. controls (32.4,189.9) and (37.8,217.8) .. (33.9,200.4) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 22; green, 48; blue, 120 }  ,fill opacity=1 ] (326.5,168) -- (295.4,206.9) -- (286.9,206.9) -- (317.9,167.4) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 113; blue, 35 }  ,fill opacity=1 ] (376.4,167.9) -- (347.9,206.4) -- (301.4,205.9) -- (328.9,169.9) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (30.85,172.08) .. controls (58.75,172.48) and (375.25,146.48) .. (494.25,154.48) .. controls (495.74,156.15) and (498.64,157.26) .. (498.99,158.82) .. controls (346.25,162.48) and (136.25,171.98) .. (29.66,175.78) .. controls (30.06,174.6) and (30.46,173.37) .. (30.85,172.08) -- cycle ;
            	\draw  [fill={rgb, 255:red, 22; green, 48; blue, 120 }  ,fill opacity=1 ] (25.75,177.88) .. controls (25.71,176.95) and (26.44,176.16) .. (27.37,176.12) -- (500.77,157.61) .. controls (501.7,157.57) and (502.48,158.3) .. (502.52,159.23) -- (502.52,159.23) .. controls (502.56,160.16) and (501.83,160.95) .. (500.9,160.98) -- (27.5,179.5) .. controls (26.57,179.54) and (25.78,178.81) .. (25.75,177.88) -- cycle ;
            	\draw    (134,118.9) .. controls (169,117.3) and (272.5,110.4) .. (326.51,115.67) ;
            	\draw  [fill={rgb, 255:red, 174; green, 219; blue, 245 }  ,fill opacity=1 ][line width=1.5]  (313.25,120.95) -- (336.45,141.15) -- (275.7,139.4) -- (255.7,120.15) -- cycle ;
            	\draw [line width=1.5]    (300.7,121.4) -- (319.5,140.2) ;
            	\draw [line width=1.5]    (282.45,121.15) -- (299.7,139.9) ;
            	\draw  [fill={rgb, 255:red, 174; green, 219; blue, 245 }  ,fill opacity=1 ][line width=1.5]  (247.95,120.4) -- (266.45,140.4) -- (210.2,140.9) -- (211.2,121.9) -- cycle ;
            	\draw [line width=1.5]    (236.7,120.65) -- (236.7,140.9) ;
            	\draw  [fill={rgb, 255:red, 174; green, 219; blue, 245 }  ,fill opacity=1 ][line width=1.5]  (177.08,125.05) .. controls (177.17,123.42) and (178.57,122.1) .. (180.19,122.1) -- (200.77,122.1) .. controls (202.4,122.1) and (203.64,123.42) .. (203.55,125.05) -- (202.78,138.95) .. controls (202.69,140.58) and (201.3,141.9) .. (199.67,141.9) -- (179.09,141.9) .. controls (177.47,141.9) and (176.22,140.58) .. (176.31,138.95) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (270.92,116.87) .. controls (270.73,116.33) and (270.96,115.9) .. (271.44,115.9) .. controls (271.91,115.9) and (272.45,116.33) .. (272.64,116.87) .. controls (272.84,117.4) and (272.6,117.83) .. (272.13,117.83) .. controls (271.65,117.83) and (271.11,117.4) .. (270.92,116.87) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (291.67,117.37) .. controls (291.48,116.83) and (291.71,116.4) .. (292.19,116.4) .. controls (292.66,116.4) and (293.2,116.83) .. (293.39,117.37) .. controls (293.59,117.9) and (293.35,118.33) .. (292.88,118.33) .. controls (292.4,118.33) and (291.86,117.9) .. (291.67,117.37) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (303.67,117.37) .. controls (303.48,116.83) and (303.71,116.4) .. (304.19,116.4) .. controls (304.66,116.4) and (305.2,116.83) .. (305.39,117.37) .. controls (305.59,117.9) and (305.35,118.33) .. (304.88,118.33) .. controls (304.4,118.33) and (303.86,117.9) .. (303.67,117.37) -- cycle ;
            	\draw    (272.64,116.87) .. controls (275.55,117.4) and (280.8,123.65) .. (281.55,125.65) ;
            	\draw    (292.53,117.37) .. controls (296.8,117.4) and (299.3,123.65) .. (302.05,126.65) ;
            	\draw    (305.39,117.37) .. controls (309.3,119.15) and (315.55,125.9) .. (318.3,128.9) ;
            	\draw    (305.85,123.7) -- (315.3,132.4) ;
            	\draw    (287.35,122.7) -- (298.8,135.9) ;
            	\draw    (291.14,126.62) .. controls (294.05,127.15) and (315.55,141.15) .. (316.3,143.15) ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (315.44,143.15) .. controls (315.25,142.62) and (315.48,142.18) .. (315.96,142.18) .. controls (316.43,142.18) and (316.97,142.62) .. (317.16,143.15) .. controls (317.35,143.68) and (317.12,144.12) .. (316.64,144.12) .. controls (316.17,144.12) and (315.63,143.68) .. (315.44,143.15) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (193.05,126.15) -- (186.1,134.45) -- (187.3,131.4) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (199.05,127.15) -- (192.1,135.45) -- (192.8,132.9) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (224.8,125.4) -- (217.85,133.7) -- (219.3,129.9) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (229.8,124.9) -- (222.85,133.2) -- (225.3,129.15) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (248.3,126.15) -- (241.35,134.45) -- (245.3,127.9) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (250.55,128.9) -- (243.6,137.2) -- (246.3,132.65) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (281.55,125.65) -- (274.6,133.95) -- (277.3,128.9) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (281.55,131.9) -- (277.85,135.95) -- (281.8,129.4) -- cycle ;
            	\draw   (146.38,124.14) .. controls (146.51,122.81) and (147.68,121.69) .. (149,121.64) -- (166.95,120.97) .. controls (168.28,120.92) and (169.24,121.96) .. (169.11,123.28) -- (165.34,161.91) .. controls (165.21,163.24) and (164.04,164.36) .. (162.71,164.41) -- (144.76,165.08) .. controls (143.44,165.13) and (142.48,164.09) .. (142.61,162.77) -- cycle ;
            	\draw   (145.07,127.08) -- (146.59,127.19) -- (146.28,131.63) -- (144.77,131.53) -- cycle ;
            	\draw   (144.07,139.58) -- (145.59,139.69) -- (145.28,144.13) -- (143.77,144.03) -- cycle ;
            	\draw   (142.57,154.08) -- (144.09,154.19) -- (143.78,158.63) -- (142.27,158.53) -- cycle ;
            	\draw   (191.85,147.24) .. controls (191.85,147.05) and (192,146.9) .. (192.19,146.9) -- (200.96,146.9) .. controls (201.15,146.9) and (201.3,147.05) .. (201.3,147.24) -- (201.3,148.26) .. controls (201.3,148.45) and (201.15,148.6) .. (200.96,148.6) -- (192.19,148.6) .. controls (192,148.6) and (191.85,148.45) .. (191.85,148.26) -- cycle ;
            	\draw   (237.1,146.99) .. controls (237.1,146.8) and (237.25,146.65) .. (237.44,146.65) -- (246.21,146.65) .. controls (246.4,146.65) and (246.55,146.8) .. (246.55,146.99) -- (246.55,148.01) .. controls (246.55,148.2) and (246.4,148.35) .. (246.21,148.35) -- (237.44,148.35) .. controls (237.25,148.35) and (237.1,148.2) .. (237.1,148.01) -- cycle ;
            	\draw   (163.08,144.52) .. controls (163.1,144.3) and (163.3,144.13) .. (163.53,144.15) -- (164.74,144.26) .. controls (164.97,144.28) and (165.14,144.48) .. (165.12,144.7) -- (164.62,150.42) .. controls (164.6,150.65) and (164.4,150.81) .. (164.17,150.79) -- (162.96,150.69) .. controls (162.73,150.67) and (162.57,150.47) .. (162.59,150.24) -- cycle ;
            	\draw   (159.8,146.29) .. controls (159.8,146.2) and (159.87,146.13) .. (159.95,146.13) -- (163.7,146.13) .. controls (163.78,146.13) and (163.85,146.2) .. (163.85,146.29) -- (163.85,146.75) .. controls (163.85,146.83) and (163.78,146.9) .. (163.7,146.9) -- (159.95,146.9) .. controls (159.87,146.9) and (159.8,146.83) .. (159.8,146.75) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (223.1,156.6) .. controls (223.1,155.8) and (223.75,155.15) .. (224.55,155.15) -- (231.1,155.15) .. controls (231.9,155.15) and (232.55,155.8) .. (232.55,156.6) -- (232.55,158.15) .. controls (232.55,158.95) and (231.9,159.6) .. (231.1,159.6) -- (224.55,159.6) .. controls (223.75,159.6) and (223.1,158.95) .. (223.1,158.15) -- cycle ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ]   (248.1,115.45) -- (278.3,145.4) ;
            	\draw    (278.3,145.4) .. controls (306.3,144.4) and (331.55,145.4) .. (341.55,145.65) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ]   (244.8,153.4) -- (280.3,152.4) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ]   (278.05,157.4) -- (280.3,152.4) ;
            	\draw  [fill={rgb, 255:red, 174; green, 219; blue, 245 }  ,fill opacity=1 ][line width=0.75]  (154.51,125.95) .. controls (154.54,125.45) and (154.96,125.05) .. (155.46,125.05) -- (159.83,125.05) .. controls (160.33,125.05) and (160.71,125.45) .. (160.69,125.95) -- (160.45,130.2) .. controls (160.42,130.7) and (160,131.1) .. (159.5,131.1) -- (155.12,131.1) .. controls (154.63,131.1) and (154.24,130.7) .. (154.27,130.2) -- cycle ;
            	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (261.51,161.37) .. controls (261.87,160.84) and (262.6,160.4) .. (263.14,160.4) -- (266.88,160.4) .. controls (267.41,160.4) and (267.55,160.84) .. (267.19,161.37) -- (265.21,164.29) .. controls (264.85,164.83) and (264.11,165.27) .. (263.58,165.27) -- (259.84,165.27) .. controls (259.3,165.27) and (259.16,164.83) .. (259.53,164.29) -- cycle ;
            	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (65.16,159.18) .. controls (65.31,157.66) and (66.66,156.35) .. (68.18,156.27) -- (89,155.2) .. controls (90.52,155.12) and (91.63,156.3) .. (91.48,157.83) -- (90.67,166.14) .. controls (90.52,167.67) and (89.16,168.97) .. (87.65,169.05) -- (66.83,170.12) .. controls (65.31,170.2) and (64.2,169.02) .. (64.35,167.49) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (39.02,152.67) -- (124.33,149.07) -- (124.38,150.2) -- (39.06,153.81) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (37.73,163.79) -- (124.71,160.11) -- (124.65,158.72) -- (37.67,162.4) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (39.02,152.67) -- (34.36,171.32) -- (36,171.73) -- (40.65,153.08) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (51.68,152.26) -- (51.65,170.73) -- (53.33,170.73) -- (53.37,152.26) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (66.87,151.65) -- (66.83,170.12) -- (68.52,170.12) -- (68.55,151.65) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (81.7,150.44) -- (81.66,168.91) -- (83.35,168.92) -- (83.39,150.44) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (110.02,149.59) -- (109.98,168.06) -- (111.67,168.07) -- (111.71,149.59) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (124.27,149.33) -- (126.43,166.31) -- (128.49,166.05) -- (126.33,149.07) -- cycle ;
            	\draw  [fill={rgb, 255:red, 245; green, 113; blue, 35 }  ,fill opacity=1 ,even odd rule] (61.55,156.27) .. controls (61.55,152.61) and (64.52,149.64) .. (68.18,149.64) .. controls (71.84,149.64) and (74.81,152.61) .. (74.81,156.27) .. controls (74.81,159.94) and (71.84,162.91) .. (68.18,162.91) .. controls (64.52,162.91) and (61.55,159.94) .. (61.55,156.27)(55.21,156.27) .. controls (55.21,149.11) and (61.02,143.31) .. (68.18,143.31) .. controls (75.34,143.31) and (81.15,149.11) .. (81.15,156.27) .. controls (81.15,163.43) and (75.34,169.24) .. (68.18,169.24) .. controls (61.02,169.24) and (55.21,163.43) .. (55.21,156.27) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (68.18,149.64) -- (68.18,143.31) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (55.21,156.27) -- (61.55,156.27) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (81.15,156.27) -- (74.81,156.27) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (68.52,170.12) -- (68.52,163.79) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (59.33,147.07) -- (62.67,151.07) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (73.33,161.07) -- (76.67,165.07) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (76.67,147.73) -- (73,151.73) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (63.33,161.07) -- (59.67,165.07) ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.5 ][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (42.67,168.2) .. controls (42.67,166.84) and (43.77,165.73) .. (45.13,165.73) .. controls (46.5,165.73) and (47.6,166.84) .. (47.6,168.2) .. controls (47.6,169.56) and (46.5,170.67) .. (45.13,170.67) .. controls (43.77,170.67) and (42.67,169.56) .. (42.67,168.2) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (155.03,157.29) -- (472.53,129.07) -- (472.65,130.36) -- (155.14,158.59) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (155.03,157.29) -- (151.35,163.77) -- (152.47,164.4) -- (156.14,157.92) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (473.14,129.26) -- (463.36,152.71) -- (464.87,153.33) -- (474.64,129.89) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (415.06,134.45) -- (410.5,152.74) -- (411.8,153.07) -- (416.36,134.77) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (356.85,140.02) -- (351.14,153.51) -- (352.68,154.16) -- (358.39,140.67) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (312.3,143.18) -- (307.14,155.36) -- (308.8,156.07) -- (313.96,143.88) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (263.3,147.84) -- (259.08,157.81) -- (260.47,158.4) -- (264.69,148.43) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (230.63,150.84) -- (226.7,160.13) -- (228.13,160.73) -- (232.06,151.45) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (191.3,154.18) -- (187.85,162.33) -- (188.8,162.73) -- (192.25,154.58) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (406.56,140.71) -- (402.4,150.53) -- (403.24,150.89) -- (407.4,141.07) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (418.89,140.38) -- (414.02,151.9) -- (414.73,152.2) -- (419.61,140.68) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (450.89,137.57) -- (444.73,152.11) -- (445.73,152.53) -- (451.89,137.99) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (493.37,133.64) -- (484.95,153.53) -- (485.73,153.87) -- (494.15,133.97) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (443.05,147.91) .. controls (443.05,147.63) and (443.28,147.4) .. (443.56,147.4) -- (456.29,147.4) .. controls (456.57,147.4) and (456.8,147.63) .. (456.8,147.91) -- (456.8,149.43) .. controls (456.8,149.71) and (456.57,149.93) .. (456.29,149.93) -- (443.56,149.93) .. controls (443.28,149.93) and (443.05,149.71) .. (443.05,149.43) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (479.3,149.05) .. controls (479.3,148.83) and (479.48,148.65) .. (479.7,148.65) -- (490.65,148.65) .. controls (490.87,148.65) and (491.05,148.83) .. (491.05,149.05) -- (491.05,150.25) .. controls (491.05,150.47) and (490.87,150.65) .. (490.65,150.65) -- (479.7,150.65) .. controls (479.48,150.65) and (479.3,150.47) .. (479.3,150.25) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (447.19,149.4) -- (452.3,149.4) -- (452.3,152.9) -- (447.19,152.9) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (482.19,150.08) -- (487.3,150.08) -- (487.3,153.9) -- (482.19,153.9) -- cycle ;
            	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (363.21,145.72) .. controls (362.91,145.27) and (363.04,144.9) .. (363.5,144.9) -- (371.54,144.9) .. controls (372,144.9) and (372.61,145.27) .. (372.9,145.72) -- (374.51,148.19) .. controls (374.8,148.65) and (374.67,149.02) .. (374.22,149.02) -- (366.17,149.02) .. controls (365.72,149.02) and (365.11,148.65) .. (364.81,148.19) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.5 ][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (146.42,163.77) .. controls (146.42,162.41) and (147.53,161.3) .. (148.89,161.3) .. controls (150.25,161.3) and (151.35,162.41) .. (151.35,163.77) .. controls (151.35,165.13) and (150.25,166.24) .. (148.89,166.24) .. controls (147.53,166.24) and (146.42,165.13) .. (146.42,163.77) -- cycle ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.6 ]   (36.4,211.9) .. controls (131.04,220.16) and (339.04,210.96) .. (468.64,187.76) ;
            	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (138.24,103.76) .. controls (138.24,101.55) and (140.03,99.76) .. (142.24,99.76) -- (145.84,99.76) .. controls (148.05,99.76) and (149.84,101.55) .. (149.84,103.76) -- (149.84,111.36) .. controls (149.84,111.36) and (149.84,111.36) .. (149.84,111.36) -- (138.24,111.36) .. controls (138.24,111.36) and (138.24,111.36) .. (138.24,111.36) -- cycle ;
            	\draw    (143.24,99.76) -- (142.24,49.76) ;
            	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (142.24,94.52) -- (144.24,94.52) -- (144.24,99.76) -- (142.24,99.76) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (183.84,60.56) -- (207.3,109.9) -- (199.8,110.4) -- (188.64,85.76) -- (181.84,61.36) -- cycle ;
            	\draw [line width=1.5]    (186.24,98.96) -- (196.55,110.4) ;
            	\draw   (175.04,42.16) -- (176.35,42.4) -- (178.1,69.15) -- (176.64,69.36) -- cycle ;
            	\draw    (176.04,42.16) -- (175.6,34.65) ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.23 ][fill={rgb, 255:red, 255; green, 1; blue, 32 }  ,fill opacity=1 ] (151.84,48.4) .. controls (159.34,48.4) and (167.1,44.4) .. (174.6,44.15) .. controls (175.1,50.4) and (175.35,54.15) .. (175.6,58.4) .. controls (171.1,58.4) and (160.29,60.9) .. (151.04,62.4) .. controls (151.84,56.4) and (152.24,54) .. (151.84,48.4) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (164.08,48.9) -- (164.94,52.13) -- (168.86,52.1) -- (165.48,54.06) -- (166.42,57.27) -- (163.47,55.25) -- (160.14,57.27) -- (161.69,54.06) -- (158.69,52.1) -- (162.6,52.13) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (177.42,60.89) .. controls (177.35,60.34) and (179.67,59.61) .. (182.6,59.25) .. controls (185.52,58.9) and (187.95,59.05) .. (188.01,59.6) .. controls (188.08,60.15) and (185.76,60.88) .. (182.84,61.24) .. controls (179.91,61.59) and (177.49,61.44) .. (177.42,60.89) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (184.8,68.4) -- (185.55,71.4) -- (168.5,70.15) -- (168,68.9) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (162.85,83.45) .. controls (162.85,82.87) and (163.32,82.4) .. (163.9,82.4) -- (216.5,82.4) .. controls (217.08,82.4) and (217.55,82.87) .. (217.55,83.45) -- (217.55,83.45) .. controls (217.55,84.03) and (217.08,84.5) .. (216.5,84.5) -- (163.9,84.5) .. controls (163.32,84.5) and (162.85,84.03) .. (162.85,83.45) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (180.25,99.73) .. controls (180.25,99.13) and (180.73,98.65) .. (181.33,98.65) -- (196.86,98.65) .. controls (197.46,98.65) and (197.94,99.13) .. (197.94,99.73) -- (197.94,99.73) .. controls (197.94,100.33) and (197.46,100.81) .. (196.86,100.81) -- (181.33,100.81) .. controls (180.73,100.81) and (180.25,100.33) .. (180.25,99.73) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (202.5,99.85) .. controls (202.5,99.33) and (202.93,98.9) .. (203.45,98.9) -- (211.3,98.9) .. controls (211.82,98.9) and (212.25,99.33) .. (212.25,99.85) -- (212.25,99.85) .. controls (212.25,100.38) and (211.82,100.81) .. (211.3,100.81) -- (203.45,100.81) .. controls (202.93,100.81) and (202.5,100.38) .. (202.5,99.85) -- cycle ;
            	\draw    (205.25,105.65) -- (211.3,100.81) ;
            	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (207.14,96.17) .. controls (207.14,95.38) and (207.78,94.74) .. (208.57,94.74) -- (209.86,94.74) .. controls (210.65,94.74) and (211.3,95.38) .. (211.3,96.17) -- (211.3,98.9) .. controls (211.3,98.9) and (211.3,98.9) .. (211.3,98.9) -- (207.14,98.9) .. controls (207.14,98.9) and (207.14,98.9) .. (207.14,98.9) -- cycle ;
            	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (186.24,96.23) .. controls (186.24,95.44) and (186.88,94.8) .. (187.67,94.8) -- (188.97,94.8) .. controls (189.76,94.8) and (190.4,95.44) .. (190.4,96.23) -- (190.4,98.96) .. controls (190.4,98.96) and (190.4,98.96) .. (190.4,98.96) -- (186.24,98.96) .. controls (186.24,98.96) and (186.24,98.96) .. (186.24,98.96) -- cycle ;
            	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (163.9,79.67) .. controls (163.9,78.88) and (164.54,78.24) .. (165.33,78.24) -- (166.63,78.24) .. controls (167.42,78.24) and (168.06,78.88) .. (168.06,79.67) -- (168.06,82.4) .. controls (168.06,82.4) and (168.06,82.4) .. (168.06,82.4) -- (163.9,82.4) .. controls (163.9,82.4) and (163.9,82.4) .. (163.9,82.4) -- cycle ;
            	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (168,66.17) .. controls (168,65.38) and (168.64,64.74) .. (169.43,64.74) -- (170.73,64.74) .. controls (171.52,64.74) and (172.16,65.38) .. (172.16,66.17) -- (172.16,68.9) .. controls (172.16,68.9) and (172.16,68.9) .. (172.16,68.9) -- (168,68.9) .. controls (168,68.9) and (168,68.9) .. (168,68.9) -- cycle ;
            	\draw    (163.9,84.5) -- (159.25,110.9) ;
            	\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (181.5,55.92) .. controls (181.5,55.13) and (182.14,54.49) .. (182.93,54.49) -- (184.23,54.49) .. controls (185.02,54.49) and (185.66,55.13) .. (185.66,55.92) -- (185.66,58.65) .. controls (185.66,58.65) and (185.66,58.65) .. (185.66,58.65) -- (181.5,58.65) .. controls (181.5,58.65) and (181.5,58.65) .. (181.5,58.65) -- cycle ;
            	\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (189.14,65.42) .. controls (189.14,64.63) and (189.78,63.99) .. (190.57,63.99) -- (191.87,63.99) .. controls (192.66,63.99) and (193.3,64.63) .. (193.3,65.42) -- (193.3,68.15) .. controls (193.3,68.15) and (193.3,68.15) .. (193.3,68.15) -- (189.14,68.15) .. controls (189.14,68.15) and (189.14,68.15) .. (189.14,68.15) -- cycle ;
            	\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (212.34,79.67) .. controls (212.34,78.88) and (212.98,78.24) .. (213.77,78.24) -- (215.07,78.24) .. controls (215.86,78.24) and (216.5,78.88) .. (216.5,79.67) -- (216.5,82.4) .. controls (216.5,82.4) and (216.5,82.4) .. (216.5,82.4) -- (212.34,82.4) .. controls (212.34,82.4) and (212.34,82.4) .. (212.34,82.4) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 22; green, 48; blue, 120 }  ,fill opacity=1 ] (219.63,75.57) -- (211,80.51) -- (201.91,80.54) -- (193.25,75.65) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.5 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (200.8,80.51) -- (211,80.51) -- (211,82.4) -- (200.8,82.4) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (190.75,72.02) .. controls (190.75,70.02) and (192.37,68.4) .. (194.38,68.4) -- (217.92,68.4) .. controls (219.93,68.4) and (221.55,70.02) .. (221.55,72.02) -- (221.55,72.02) .. controls (221.55,74.03) and (219.93,75.65) .. (217.92,75.65) -- (194.38,75.65) .. controls (192.37,75.65) and (190.75,74.03) .. (190.75,72.02) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (221.25,97.65) -- (259.05,99.7) -- (260,101.4) -- (228.5,100.65) -- (233.25,108.9) -- (226.5,109.15) -- (228,105.65) -- (225.5,100.57) -- (222.25,100.65) -- (217.5,109.15) -- (213.75,109.65) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (260,101.4) -- (262.75,108.15) -- (259.5,108.4) -- (257.5,101.4) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (253.25,101.65) -- (256,108.4) -- (252.75,108.65) -- (250.75,101.65) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (244.25,105.89) .. controls (244.25,104.38) and (245.48,103.15) .. (246.99,103.15) -- (263.76,103.15) .. controls (265.27,103.15) and (266.5,104.38) .. (266.5,105.89) -- (266.5,108.62) .. controls (266.5,108.62) and (266.5,108.62) .. (266.5,108.62) -- (244.25,108.62) .. controls (244.25,108.62) and (244.25,108.62) .. (244.25,108.62) -- cycle ;
            	\draw  [fill={rgb, 255:red, 22; green, 48; blue, 120 }  ,fill opacity=1 ] (248.48,93.44) .. controls (253.39,93.85) and (258.13,94.16) .. (262.55,94.25) .. controls (263.88,95.01) and (264.15,96.39) .. (263.8,98.32) .. controls (259,99.4) and (254.75,98.15) .. (247.75,98.15) .. controls (251,95.9) and (251,96.65) .. (248.48,93.44) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (234.4,92.63) .. controls (239.32,93.04) and (244.05,93.35) .. (248.48,93.44) .. controls (249.8,94.2) and (249.85,95.97) .. (249.5,97.9) .. controls (244.7,98.98) and (240.68,97.34) .. (233.68,97.34) .. controls (236.93,95.09) and (235.5,95.4) .. (234.4,92.63) -- cycle ;
            	\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (219.75,91.9) .. controls (224.67,92.31) and (229.98,92.54) .. (234.4,92.63) .. controls (235.73,93.39) and (235.77,95.16) .. (235.43,97.09) .. controls (230.62,98.17) and (226.6,96.53) .. (219.6,96.53) .. controls (222.85,94.28) and (220.85,94.67) .. (219.75,91.9) -- cycle ;
            	\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (213.3,94.57) .. controls (213.3,93.24) and (214.39,92.15) .. (215.73,92.15) -- (224.32,92.15) .. controls (225.66,92.15) and (226.75,93.24) .. (226.75,94.57) -- (226.75,94.57) .. controls (226.75,95.91) and (225.66,97) .. (224.32,97) -- (215.73,97) .. controls (214.39,97) and (213.3,95.91) .. (213.3,94.57) -- cycle ;
            	\draw    (252.25,63.9) -- (252.5,93.15) ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (282.56,107.99) .. controls (282.58,107.25) and (283.2,106.67) .. (283.94,106.69) -- (294.69,106.99) .. controls (295.43,107.01) and (296.01,107.63) .. (295.99,108.37) -- (295.95,109.71) .. controls (295.95,109.71) and (295.95,109.71) .. (295.95,109.71) -- (282.52,109.33) .. controls (282.52,109.33) and (282.52,109.33) .. (282.52,109.33) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (294.53,100.18) -- (292.15,106.89) -- (286.12,106.59) -- (284.4,99.68) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (295.25,100.13) -- (283.76,99.66) .. controls (282.17,99.59) and (280.98,97) .. (281.11,93.86) .. controls (281.24,90.73) and (282.64,88.24) .. (284.23,88.31) -- (295.72,88.78) .. controls (297.31,88.85) and (298.49,91.44) .. (298.37,94.58) .. controls (298.24,97.71) and (296.84,100.2) .. (295.25,100.13) .. controls (293.66,100.07) and (292.47,97.47) .. (292.6,94.34) .. controls (292.73,91.2) and (294.13,88.71) .. (295.72,88.78) ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (294.5,102.64) -- (283.65,102.19) .. controls (283.3,102.18) and (283.03,101.6) .. (283.06,100.9) .. controls (283.09,100.2) and (283.4,99.64) .. (283.76,99.66) -- (294.6,100.1) .. controls (294.96,100.12) and (295.23,100.7) .. (295.2,101.4) .. controls (295.17,102.1) and (294.86,102.66) .. (294.5,102.64) .. controls (294.14,102.63) and (293.88,102.05) .. (293.91,101.35) .. controls (293.94,100.65) and (294.25,100.09) .. (294.6,100.1) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 161; green, 235; blue, 242 }  ,fill opacity=1 ] (293.35,94.78) .. controls (293.35,92.22) and (294.19,90.15) .. (295.22,90.15) .. controls (296.26,90.15) and (297.1,92.22) .. (297.1,94.78) .. controls (297.1,97.33) and (296.26,99.4) .. (295.22,99.4) .. controls (294.19,99.4) and (293.35,97.33) .. (293.35,94.78) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.43 ] (281.85,94.9) -- (291.35,95.15) -- (292.35,99.15) -- (283.76,99.66) -- cycle ;
            	\draw    (273.1,108.9) .. controls (276.1,103.9) and (282.1,104.4) .. (283.65,102.19) ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (314.22,104.59) .. controls (314.29,103.31) and (315.34,102.32) .. (316.56,102.39) .. controls (317.79,102.46) and (318.72,103.55) .. (318.65,104.83) .. controls (318.58,106.11) and (317.53,107.09) .. (316.31,107.02) .. controls (315.08,106.95) and (314.15,105.86) .. (314.22,104.59) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (315.52,110.37) .. controls (315.54,110.07) and (315.81,109.84) .. (316.11,109.87) -- (320.47,110.23) .. controls (320.77,110.25) and (321,110.52) .. (320.97,110.82) -- (320.93,111.36) .. controls (320.93,111.36) and (320.93,111.36) .. (320.93,111.36) -- (315.47,110.91) .. controls (315.47,110.91) and (315.47,110.91) .. (315.47,110.91) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (320.56,107.45) -- (319.44,110.13) -- (316.99,109.88) -- (316.45,107.03) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (320.85,107.45) -- (316.19,107) .. controls (315.54,106.94) and (315.12,105.86) .. (315.24,104.59) .. controls (315.36,103.31) and (315.99,102.33) .. (316.63,102.4) -- (321.3,102.84) .. controls (321.94,102.91) and (322.37,103.99) .. (322.25,105.26) .. controls (322.12,106.53) and (321.5,107.51) .. (320.85,107.45) .. controls (320.21,107.39) and (319.78,106.31) .. (319.91,105.04) .. controls (320.03,103.76) and (320.65,102.78) .. (321.3,102.84) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 161; green, 235; blue, 242 }  ,fill opacity=1 ] (320.2,105.23) .. controls (320.26,104.19) and (320.64,103.37) .. (321.07,103.39) .. controls (321.49,103.41) and (321.78,104.27) .. (321.73,105.31) .. controls (321.67,106.35) and (321.28,107.18) .. (320.86,107.15) .. controls (320.44,107.13) and (320.14,106.27) .. (320.2,105.23) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.43 ] (315.52,105.03) -- (319.38,105.34) -- (319.7,106.99) -- (316.19,107) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (263.72,101.59) .. controls (263.79,100.31) and (264.84,99.32) .. (266.06,99.39) .. controls (267.29,99.46) and (268.22,100.55) .. (268.15,101.83) .. controls (268.08,103.11) and (267.03,104.09) .. (265.81,104.02) .. controls (264.58,103.95) and (263.65,102.86) .. (263.72,101.59) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (265.02,107.37) .. controls (265.04,107.07) and (265.31,106.84) .. (265.61,106.87) -- (269.97,107.23) .. controls (270.27,107.25) and (270.5,107.52) .. (270.47,107.82) -- (270.43,108.36) .. controls (270.43,108.36) and (270.43,108.36) .. (270.43,108.36) -- (264.97,107.91) .. controls (264.97,107.91) and (264.97,107.91) .. (264.97,107.91) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (270.06,104.45) -- (268.94,107.13) -- (266.49,106.88) -- (265.95,104.03) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (270.35,104.45) -- (265.69,104) .. controls (265.04,103.94) and (264.62,102.86) .. (264.74,101.59) .. controls (264.86,100.31) and (265.49,99.33) .. (266.13,99.4) -- (270.8,99.84) .. controls (271.44,99.91) and (271.87,100.99) .. (271.75,102.26) .. controls (271.62,103.53) and (271,104.51) .. (270.35,104.45) .. controls (269.71,104.39) and (269.28,103.31) .. (269.41,102.04) .. controls (269.53,100.76) and (270.15,99.78) .. (270.8,99.84) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 161; green, 235; blue, 242 }  ,fill opacity=1 ] (269.7,102.23) .. controls (269.76,101.19) and (270.14,100.37) .. (270.57,100.39) .. controls (270.99,100.41) and (271.28,101.27) .. (271.23,102.31) .. controls (271.17,103.35) and (270.78,104.18) .. (270.36,104.15) .. controls (269.94,104.13) and (269.64,103.27) .. (269.7,102.23) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.43 ] (265.02,102.03) -- (268.88,102.34) -- (269.2,103.99) -- (265.69,104) -- cycle ;
            \end{tikzpicture}'''
                # Câu hỏi
                noidungcauhoi = (r'''\immini{Một đội CSGT đường thủy sử dụng một chiếc ca nô chuyên dụng để tuần tra trên một đoạn sông dài $%s$ km. Chuyến tuần tra bao gồm đi ngược dòng từ vị trí xuất phát $A$ đến $B$ dài $%s$ km, sau đó ngay lập tức quay về xuôi dòng từ $B$ về lại $A$. }{%s} Lượng xăng tiêu thụ của động cơ (tính bằng lít) được xác định theo công thức: $L = k.v^2.t$ trong đó $k$ là một hằng số phụ thuộc vào đặc tính của động cơ, $v$ là tốc độ của động cơ (tốc độ của ca nô so với mặt nước) có đơn vị là km/h và $t$ là thời gian động cơ hoạt động tính bằng giờ. Biết rằng vận tốc của dòng nước trên cả đoạn sông là $%s$ km/h. Để xác định hằng số $k$ thì các kỹ thuật viên đã chạy thử ca nô trong điều kiện mặt nước yên tĩnh. Kết quả cho thấy động cơ tiêu thụ $%s$ lít xăng mỗi giờ nếu chạy với tốc độ ổn định là $%s$ km/h. Hỏi để hoàn thành cả chuyến tuần tra với lượng xăng tiêu thụ ít nhất thì người lái ca nô phải cài đặt tốc độ $v$ của ca nô bằng bao nhiêu km/h? (Kết quả làm tròn đến hàng phần chục).''' 
                % (S, S, hinhve, a, L0, v0))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Khi thử nghiệm chạy với vận tốc $v = %s$ (km/h) trong thời gian $t = 1$ giờ và hết $L = %s$ lít, \\\\
                Ta có: $L = k.v^2.t \\Rightarrow %s = k.%s^2.1 \\Rightarrow k = \\frac{%s}{%s^2.1} = \\frac{1}{%s}$ \\\\
                Khi ca nô đi ngược dòng từ $A$ đến $B$ thì vận tốc thực của ca nô là: $v_{nguoc} = v - v_{nuoc} = v - %s$ (km/h) \\\\
                Lượng xăng ca nô tiêu thụ khi đi ngược dòng là: $L_1 = k.v^2.t_{nguoc} = \\frac{1}{%s}.v^2.\\left(\\frac{%s}{v - %s}\\right) = \\frac{%sv^2}{v - %s}$ \\\\
                Khi ca nô đi xuôi dòng từ $B$ về $A$ thì vận tốc thực của ca nô là: $v_{xuoi} = v + v_{nuoc} = v + %s$ (km/h) \\\\
                Lượng xăng ca nô tiêu thụ khi đi xuôi dòng là: $L_2 = k.v^2.t_{xuoi} = \\frac{1}{%s}.v^2.\\left(\\frac{%s}{v + %s}\\right) = \\frac{%sv^2}{v + %s}$ \\\\
                Hàm tổng lượng xăng tiêu thụ cho cả chuyến tuần tra là: \\\\
                $L(v) = L_1 + L_2 = \\frac{%sv^2}{v - %s} + \\frac{%sv^2}{v + %s} = %sv^2 \\left( \\frac{2v}{v^2 - %s} \\right)$ \\\\
                Xét hàm số $L(v) = \\frac{%sv^3}{v^2 - %s}$ với $v \\in (%s; +\\infty)$ có $L'(v) = \\frac{%sv^2(v^2 - %s)}{(v^2 - %s)^2} = 0 \\Leftrightarrow v = %s \\in (%s; +\\infty)$ \\\\
                Vậy người lái ca nô vẫn cần cài đặt tốc độ động cơ là $v = %s \\approx %s$ (km/h).'''
                % (v0, L0,
                   L0, v0, L0, v0, k_den,
                   a,
                   k_den, S, a, M_str, a,
                   a,
                   k_den, S, a, M_str, a,
                   M_str, a, M_str, a, M_str, a_sq,
                   C_str, a_sq, a, C_str, three_a_sq, a_sq, v_exact_latex, a,
                   v_exact_latex, v_approx_str))
                dapan='\\shortans[0]{$%s$}\n'%(v_approx_str)


            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


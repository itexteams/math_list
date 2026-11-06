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


def bt_dang46_p3_b2_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Các bộ tham số (xA, xB, xH, yH, m) được chọn cẩn thận để tạo ra hàm số đẹp và hợp logic
                configs = [
                    {'xA': 1, 'xB': 9, 'xH': 7, 'yH': 6, 'm': 10},
                    {'xA': 2, 'xB': 10, 'xH': 8, 'yH': 8, 'm': 11},
                    {'xA': 1, 'xB': 6, 'xH': 4, 'yH': 3, 'm': 10},
                    {'xA': 1, 'xB': 13, 'xH': 9, 'yH': 8, 'm': 17}
                ]
                config = random.choice(configs)
                xA = config['xA']
                xB = config['xB']
                xH = config['xH']
                yH = config['yH']
                m = config['m']

                sum_x = xA + xB
                prod_x = xA * xB

                # Tính a = yH(xH - m) / ((xH - xA)(xH - xB))
                num = yH * (xH - m)
                den = (xH - xA) * (xH - xB)
                a_frac = Rational(num, den)

                # Hệ số cho y = \alpha x + \beta + k / (x - m)
                alpha = a_frac
                beta = a_frac * (m - sum_x)
                k = a_frac * (m**2 - m*sum_x + prod_x)

                # PQ_min^2 = 8*k*(sqrt(1+alpha^2) - alpha)
                val = 8 * k * (sp.sqrt(1 + alpha**2) - alpha)
                pq_min_val = math.sqrt(float(val))

                # Làm tròn đáp án đúng 2 chữ số thập phân
                kq3 = Decimal(float(pq_min_val)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                kq = str(kq3).replace('.', ',')
                kq_val = float(kq3)

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (kq)]
                da = random.choice(du)

                # Tạo các đáp án sai lệch đi 1 chút
                s = [
                    '$%s$' % str(Decimal(float(pq_min_val + random.uniform(0.15, 0.45))).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ','),
                    '$%s$' % str(Decimal(float(pq_min_val - random.uniform(0.15, 0.45))).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ','),
                    '$%s$' % str(Decimal(float(pq_min_val + random.uniform(0.55, 1.05))).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ','),
                    '$%s$' % str(Decimal(float(pq_min_val - random.uniform(0.55, 1.05))).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ','),
                    '$%s$' % str(Decimal(float(pq_min_val + random.uniform(1.15, 1.55))).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ','),
                ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                hinhve=r'''\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-0.8,xscale=0.8]
            	\tikzset {_qgscni35r/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{0 }  \pgftransformscale{2 }  }}}
            	\pgfdeclarehorizontalshading{_3z74gkugh}{150bp}{rgb(0bp)=(1,1,1);
            		rgb(37.5bp)=(1,1,1);
            		rgb(44.17857033865793bp)=(0.29,0.29,0.29);
            		rgb(50bp)=(1,1,1);
            		rgb(58.01785605294364bp)=(0,0,0);
            		rgb(62.03571319580078bp)=(1,1,1);
            		rgb(100bp)=(1,1,1)}
            	\tikzset {_yrjsyg6bv/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{0 }  \pgftransformscale{2 }  }}}
            	\pgfdeclarehorizontalshading{_pgpucy6ds}{150bp}{rgb(0bp)=(1,1,1);
            		rgb(37.5bp)=(1,1,1);
            		rgb(44.17857033865793bp)=(0.29,0.29,0.29);
            		rgb(50bp)=(1,1,1);
            		rgb(58.01785605294364bp)=(0,0,0);
            		rgb(62.03571319580078bp)=(1,1,1);
            		rgb(100bp)=(1,1,1)}
            	\tikzset {_fp1uueb6g/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{0 }  \pgftransformscale{2 }  }}}
            	\pgfdeclarehorizontalshading{_65kcpozvd}{150bp}{rgb(0bp)=(1,1,1);
            		rgb(37.5bp)=(1,1,1);
            		rgb(44.17857033865793bp)=(0.29,0.29,0.29);
            		rgb(50bp)=(1,1,1);
            		rgb(58.01785605294364bp)=(0,0,0);
            		rgb(62.03571319580078bp)=(1,1,1);
            		rgb(100bp)=(1,1,1)}
            	\tikzset {_aren70hmg/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{0 }  \pgftransformscale{2 }  }}}
            	\pgfdeclarehorizontalshading{_usg9dx652}{150bp}{rgb(0bp)=(1,1,1);
            		rgb(37.5bp)=(1,1,1);
            		rgb(44.17857033865793bp)=(0.29,0.29,0.29);
            		rgb(50bp)=(1,1,1);
            		rgb(58.01785605294364bp)=(0,0,0);
            		rgb(62.03571319580078bp)=(1,1,1);
            		rgb(100bp)=(1,1,1)}
            	\tikzset{every picture/.style={line width=0.75pt}} 
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (192.31,94.92) -- (195.74,104.36) -- (150.1,142.65) -- (149.52,131.59) -- (131,126.9) -- (178.02,99.58) -- cycle ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (228,169.9) -- (234,168.9) -- (218.5,207.9) -- (213,206.9) -- cycle ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (63,113.9) -- (69,112.9) -- (77,142.9) -- (71,142.4) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (60.43,88.27) -- (61.58,75.22) -- (76.16,37.14) -- (80.42,34.91) -- (72.56,74.23) -- (64.79,82.25) -- (62.78,86.98) -- cycle ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (75.04,99.9) -- (76.76,108.97) .. controls (77.24,111.48) and (73.39,114.31) .. (68.17,115.31) .. controls (62.94,116.3) and (58.32,115.08) .. (57.84,112.57) -- (56.12,103.5) .. controls (55.64,101) and (59.49,98.16) .. (64.72,97.17) .. controls (69.94,96.17) and (74.56,97.4) .. (75.04,99.9) .. controls (75.52,102.41) and (71.67,105.24) .. (66.44,106.24) .. controls (61.22,107.23) and (56.59,106.01) .. (56.12,103.5) ;
            	\path  [shading=_3z74gkugh,_qgscni35r] (72.37,91.01) -- (74.09,100.09) .. controls (74.57,102.59) and (71.14,105.34) .. (66.44,106.24) .. controls (61.74,107.13) and (57.54,105.82) .. (57.07,103.32) -- (55.34,94.25) .. controls (54.87,91.75) and (58.29,88.99) .. (62.99,88.1) .. controls (67.7,87.2) and (71.89,88.51) .. (72.37,91.01) .. controls (72.84,93.52) and (69.42,96.27) .. (64.72,97.17) .. controls (60.02,98.06) and (55.82,96.75) .. (55.34,94.25) ;  
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.54 ] (72.37,91.01) -- (74.09,100.09) .. controls (74.57,102.59) and (71.14,105.34) .. (66.44,106.24) .. controls (61.74,107.13) and (57.54,105.82) .. (57.07,103.32) -- (55.34,94.25) .. controls (54.87,91.75) and (58.29,88.99) .. (62.99,88.1) .. controls (67.7,87.2) and (71.89,88.51) .. (72.37,91.01) .. controls (72.84,93.52) and (69.42,96.27) .. (64.72,97.17) .. controls (60.02,98.06) and (55.82,96.75) .. (55.34,94.25) ; 
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (55.34,94.25) .. controls (54.87,91.75) and (58.29,88.99) .. (62.99,88.1) .. controls (67.7,87.2) and (71.89,88.51) .. (72.37,91.01) .. controls (72.84,93.52) and (69.42,96.27) .. (64.72,97.17) .. controls (60.02,98.06) and (55.82,96.75) .. (55.34,94.25) -- cycle ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (68.38,88.27) -- (69.24,92.8) .. controls (69.48,94.05) and (67.36,95.51) .. (64.51,96.05) .. controls (61.65,96.59) and (59.15,96.02) .. (58.91,94.76) -- (58.05,90.23) .. controls (57.81,88.98) and (59.93,87.52) .. (62.78,86.98) .. controls (65.63,86.44) and (68.14,87.02) .. (68.38,88.27) .. controls (68.61,89.52) and (66.5,90.97) .. (63.64,91.52) .. controls (60.79,92.06) and (58.29,91.48) .. (58.05,90.23) ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (68.99,83.88) -- (70.12,89.82) .. controls (70.43,91.46) and (67.74,93.35) .. (64.12,94.03) .. controls (60.5,94.72) and (57.31,93.95) .. (57,92.31) -- (55.87,86.38) .. controls (55.56,84.74) and (58.24,82.85) .. (61.87,82.16) .. controls (65.49,81.47) and (68.68,82.24) .. (68.99,83.88) .. controls (69.3,85.52) and (66.62,87.41) .. (62.99,88.1) .. controls (59.37,88.79) and (56.18,88.01) .. (55.87,86.38) ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.51 ][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (52.5,98.91) -- (58.05,90.23) -- (63.73,100.94) -- (43.48,147.21) -- (40.58,143.65) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (145.55,42.65) -- (156.05,37.9) -- (191.55,32.65) -- (195.1,34.95) -- (161.55,45.9) -- (152.05,43.4) -- (147.55,43.9) -- cycle ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (150.15,55.51) -- (150.15,63.64) .. controls (150.15,65.88) and (146.36,67.7) .. (141.67,67.7) .. controls (136.99,67.7) and (133.2,65.88) .. (133.2,63.64) -- (133.2,55.51) .. controls (133.2,53.27) and (136.99,51.45) .. (141.67,51.45) .. controls (146.36,51.45) and (150.15,53.27) .. (150.15,55.51) .. controls (150.15,57.76) and (146.36,59.58) .. (141.67,59.58) .. controls (136.99,59.58) and (133.2,57.76) .. (133.2,55.51) ;
            	\path  [shading=_pgpucy6ds,_yrjsyg6bv] (149.3,47.39) -- (149.3,55.51) .. controls (149.3,57.76) and (145.89,59.58) .. (141.67,59.58) .. controls (137.46,59.58) and (134.05,57.76) .. (134.05,55.51) -- (134.05,47.39) .. controls (134.05,45.14) and (137.46,43.33) .. (141.67,43.33) .. controls (145.89,43.33) and (149.3,45.14) .. (149.3,47.39) .. controls (149.3,49.63) and (145.89,51.45) .. (141.67,51.45) .. controls (137.46,51.45) and (134.05,49.63) .. (134.05,47.39) ; 
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.54 ] (149.3,47.39) -- (149.3,55.51) .. controls (149.3,57.76) and (145.89,59.58) .. (141.67,59.58) .. controls (137.46,59.58) and (134.05,57.76) .. (134.05,55.51) -- (134.05,47.39) .. controls (134.05,45.14) and (137.46,43.33) .. (141.67,43.33) .. controls (145.89,43.33) and (149.3,45.14) .. (149.3,47.39) .. controls (149.3,49.63) and (145.89,51.45) .. (141.67,51.45) .. controls (137.46,51.45) and (134.05,49.63) .. (134.05,47.39) ;  
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (123.36,111.2) .. controls (143.36,101.2) and (144.56,110.8) .. (166.16,120.8) .. controls (161.2,125.76) and (165.8,129.73) .. (163.76,132.8) .. controls (140.88,126.79) and (137.46,127.5) .. (124.96,121.2) .. controls (123.8,120.15) and (121.87,113.36) .. (123.36,111.2) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (214.56,72.4) .. controls (216.16,85.6) and (206.96,97.6) .. (204.56,103.2) .. controls (186.96,118.8) and (176.24,131.61) .. (163.76,132.8) .. controls (163.9,127.16) and (164.59,123.39) .. (160.56,121.6) .. controls (172.56,104.4) and (194.42,84.2) .. (214.56,72.4) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (124.5,117.25) .. controls (124.06,115.15) and (124.9,113.45) .. (126.38,113.45) .. controls (127.86,113.45) and (129.42,115.15) .. (129.86,117.25) .. controls (130.3,119.35) and (129.46,121.05) .. (127.98,121.05) .. controls (126.5,121.05) and (124.94,119.35) .. (124.5,117.25) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (154.21,126.25) .. controls (153.77,124.15) and (154.85,122.45) .. (156.61,122.45) .. controls (158.38,122.45) and (160.17,124.15) .. (160.61,126.25) .. controls (161.05,128.35) and (159.98,130.05) .. (158.21,130.05) .. controls (156.45,130.05) and (154.66,128.35) .. (154.21,126.25) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.42 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (148.2,58.7) -- (176.65,82.15) -- (167.4,86.15) -- (142.9,60.15) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.42 ][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (142.9,60.15) -- (167.4,86.15) -- (162.65,87.4) -- (142.9,66.4) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.42 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (74.15,100.65) -- (145.15,92.65) -- (137.9,100.4) -- (74.15,103.65) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.42 ][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (74.15,103.65) -- (142.9,99.4) -- (135.9,109.4) -- (77.15,110.9) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.37 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (185.5,63) .. controls (196.16,63.2) and (209.36,64.8) .. (214.56,72.4) .. controls (186.96,90) and (168.56,130.4) .. (158.39,120.33) .. controls (144.84,117.09) and (132.61,113.86) .. (123.36,111.2) .. controls (135.36,94) and (165.36,74.8) .. (185.5,63) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.42 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (265.4,83.4) -- (265.9,87.15) -- (203.65,87.4) -- (208.9,81.65) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.42 ][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (265.9,87.15) -- (266.15,93.4) -- (204.4,97.4) -- (203.65,87.4) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.42 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (225.65,144.9) -- (218.9,146.9) -- (182.4,111.15) -- (188.15,104.4) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.42 ][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (218.9,146.9) -- (218.65,155.4) -- (182.9,120.4) -- (182.4,111.15) -- cycle ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (134.05,47.39) .. controls (134.05,45.14) and (137.46,43.33) .. (141.67,43.33) .. controls (145.89,43.33) and (149.3,45.14) .. (149.3,47.39) .. controls (149.3,49.63) and (145.89,51.45) .. (141.67,51.45) .. controls (137.46,51.45) and (134.05,49.63) .. (134.05,47.39) -- cycle ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (146.3,44.36) -- (146.3,48.42) .. controls (146.3,49.54) and (144.23,50.45) .. (141.67,50.45) .. controls (139.12,50.45) and (137.05,49.54) .. (137.05,48.42) -- (137.05,44.36) .. controls (137.05,43.23) and (139.12,42.33) .. (141.67,42.33) .. controls (144.23,42.33) and (146.3,43.23) .. (146.3,44.36) .. controls (146.3,45.48) and (144.23,46.39) .. (141.67,46.39) .. controls (139.12,46.39) and (137.05,45.48) .. (137.05,44.36) ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (147.55,40.67) -- (147.55,45.98) .. controls (147.55,47.45) and (144.92,48.64) .. (141.67,48.64) .. controls (138.43,48.64) and (135.8,47.45) .. (135.8,45.98) -- (135.8,40.67) .. controls (135.8,39.2) and (138.43,38.01) .. (141.67,38.01) .. controls (144.92,38.01) and (147.55,39.2) .. (147.55,40.67) .. controls (147.55,42.13) and (144.92,43.33) .. (141.67,43.33) .. controls (138.43,43.33) and (135.8,42.13) .. (135.8,40.67) ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.51 ][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (128,43.81) -- (137.05,44.36) -- (131.25,53.31) -- (87,57.56) -- (88.5,53.81) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (231.9,138.54) -- (246.01,131.64) -- (294.14,123.04) -- (299.06,126.03) -- (253.83,142.31) -- (240.79,139.3) -- (234.68,140.16) -- cycle ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (238.69,155.87) -- (239.03,166.93) .. controls (239.12,169.99) and (234.03,172.62) .. (227.65,172.81) .. controls (221.28,173) and (216.04,170.68) .. (215.95,167.62) -- (215.61,156.56) .. controls (215.52,153.5) and (220.61,150.87) .. (226.99,150.68) .. controls (233.36,150.49) and (238.6,152.81) .. (238.69,155.87) .. controls (238.79,158.92) and (233.69,161.55) .. (227.32,161.75) .. controls (220.95,161.94) and (215.71,159.62) .. (215.61,156.56) ;
            	\path  [shading=_65kcpozvd,_fp1uueb6g] (237.2,144.84) -- (237.54,155.9) .. controls (237.63,158.96) and (233.05,161.57) .. (227.32,161.75) .. controls (221.59,161.92) and (216.86,159.58) .. (216.77,156.53) -- (216.44,145.46) .. controls (216.35,142.41) and (220.92,139.79) .. (226.66,139.62) .. controls (232.39,139.45) and (237.11,141.78) .. (237.2,144.84) .. controls (237.3,147.89) and (232.72,150.51) .. (226.99,150.68) .. controls (221.25,150.85) and (216.53,148.52) .. (216.44,145.46) ; 
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.54 ] (237.2,144.84) -- (237.54,155.9) .. controls (237.63,158.96) and (233.05,161.57) .. (227.32,161.75) .. controls (221.59,161.92) and (216.86,159.58) .. (216.77,156.53) -- (216.44,145.46) .. controls (216.35,142.41) and (220.92,139.79) .. (226.66,139.62) .. controls (232.39,139.45) and (237.11,141.78) .. (237.2,144.84) .. controls (237.3,147.89) and (232.72,150.51) .. (226.99,150.68) .. controls (221.25,150.85) and (216.53,148.52) .. (216.44,145.46) ; 
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (216.44,145.46) .. controls (216.35,142.41) and (220.92,139.79) .. (226.66,139.62) .. controls (232.39,139.45) and (237.11,141.78) .. (237.2,144.84) .. controls (237.3,147.89) and (232.72,150.51) .. (226.99,150.68) .. controls (221.25,150.85) and (216.53,148.52) .. (216.44,145.46) -- cycle ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (233,140.83) -- (233.16,146.36) .. controls (233.21,147.89) and (230.43,149.22) .. (226.95,149.32) .. controls (223.47,149.42) and (220.61,148.27) .. (220.57,146.74) -- (220.4,141.21) .. controls (220.35,139.68) and (223.14,138.36) .. (226.61,138.26) .. controls (230.09,138.15) and (232.95,139.3) .. (233,140.83) .. controls (233.04,142.36) and (230.26,143.68) .. (226.78,143.79) .. controls (223.3,143.89) and (220.45,142.74) .. (220.4,141.21) ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (234.55,135.76) -- (234.76,143) .. controls (234.82,145) and (231.29,146.73) .. (226.87,146.86) .. controls (222.45,146.99) and (218.82,145.48) .. (218.76,143.48) -- (218.55,136.24) .. controls (218.49,134.24) and (222.02,132.51) .. (226.44,132.37) .. controls (230.86,132.24) and (234.49,133.76) .. (234.55,135.76) .. controls (234.61,137.76) and (231.07,139.48) .. (226.66,139.62) .. controls (222.24,139.75) and (218.61,138.24) .. (218.55,136.24) ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.51 ][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (208.05,140.83) -- (220.4,141.21) -- (212.87,153.64) -- (152.79,161.23) -- (154.67,156.06) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (278.76,73.02) -- (288.08,79.8) -- (310.19,108.07) -- (309.94,112.29) -- (283.84,88.54) -- (281.32,79.04) -- (278.67,75.38) -- cycle ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (282.62,84.17) -- (282.62,92.3) .. controls (282.62,94.54) and (278.83,96.36) .. (274.15,96.37) .. controls (269.47,96.37) and (265.67,94.55) .. (265.67,92.31) -- (265.67,84.18) .. controls (265.67,81.94) and (269.46,80.12) .. (274.14,80.12) .. controls (278.82,80.11) and (282.62,81.93) .. (282.62,84.17) .. controls (282.62,86.42) and (278.83,88.24) .. (274.15,88.24) .. controls (269.47,88.24) and (265.67,86.43) .. (265.67,84.18) ;
            	\path  [shading=_usg9dx652,_aren70hmg] (281.77,76.05) -- (281.77,84.17) .. controls (281.77,86.42) and (278.36,88.24) .. (274.15,88.24) .. controls (269.94,88.24) and (266.52,86.43) .. (266.52,84.18) -- (266.52,76.06) .. controls (266.51,73.81) and (269.93,71.99) .. (274.14,71.99) .. controls (278.35,71.99) and (281.76,73.81) .. (281.77,76.05) .. controls (281.77,78.29) and (278.35,80.11) .. (274.14,80.12) .. controls (269.93,80.12) and (266.52,78.3) .. (266.52,76.06) ; 
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.54 ] (281.77,76.05) -- (281.77,84.17) .. controls (281.77,86.42) and (278.36,88.24) .. (274.15,88.24) .. controls (269.94,88.24) and (266.52,86.43) .. (266.52,84.18) -- (266.52,76.06) .. controls (266.51,73.81) and (269.93,71.99) .. (274.14,71.99) .. controls (278.35,71.99) and (281.76,73.81) .. (281.77,76.05) .. controls (281.77,78.29) and (278.35,80.11) .. (274.14,80.12) .. controls (269.93,80.12) and (266.52,78.3) .. (266.52,76.06) ; 
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (266.52,76.06) .. controls (266.51,73.81) and (269.93,71.99) .. (274.14,71.99) .. controls (278.35,71.99) and (281.76,73.81) .. (281.77,76.05) .. controls (281.77,78.29) and (278.35,80.11) .. (274.14,80.12) .. controls (269.93,80.12) and (266.52,78.3) .. (266.52,76.06) -- cycle ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (278.76,73.02) -- (278.77,77.08) .. controls (278.77,78.2) and (276.7,79.12) .. (274.14,79.12) .. controls (271.59,79.12) and (269.52,78.21) .. (269.52,77.09) -- (269.51,73.03) .. controls (269.51,71.9) and (271.58,70.99) .. (274.14,70.99) .. controls (276.69,70.99) and (278.76,71.9) .. (278.76,73.02) .. controls (278.76,74.14) and (276.69,75.05) .. (274.14,75.05) .. controls (271.59,75.06) and (269.51,74.15) .. (269.51,73.03) ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (280.01,69.33) -- (280.01,74.65) .. controls (280.02,76.12) and (277.39,77.31) .. (274.14,77.31) .. controls (270.9,77.31) and (268.27,76.12) .. (268.26,74.65) -- (268.26,69.34) .. controls (268.26,67.87) and (270.89,66.67) .. (274.14,66.67) .. controls (277.38,66.67) and (280.01,67.86) .. (280.01,69.33) .. controls (280.01,70.8) and (277.38,71.99) .. (274.14,71.99) .. controls (270.89,71.99) and (268.26,70.8) .. (268.26,69.34) ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.51 ][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (267.93,61.54) -- (272.66,69.28) -- (262,69.64) -- (233.21,35.76) -- (237.15,34.85) -- cycle ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (131,126.9) -- (149.5,132.25) -- (150.1,142.65) -- (131.85,137.9) -- cycle ;
            	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (133.4,134.76) .. controls (132.16,132.49) and (134.02,130.65) .. (137.57,130.65) .. controls (141.11,130.65) and (144.99,132.49) .. (146.23,134.76) .. controls (147.47,137.03) and (145.6,138.87) .. (142.06,138.87) .. controls (138.51,138.87) and (134.64,137.03) .. (133.4,134.76) -- cycle ;
            	\draw  [fill={rgb, 255:red, 20; green, 118; blue, 96 }  ,fill opacity=1 ] (135.69,134.76) .. controls (134.9,133.3) and (136.1,132.12) .. (138.37,132.12) .. controls (140.64,132.12) and (143.13,133.3) .. (143.93,134.76) .. controls (144.72,136.22) and (143.53,137.4) .. (141.25,137.4) .. controls (138.98,137.4) and (136.49,136.22) .. (135.69,134.76) -- cycle ;
            	\draw  [fill={rgb, 255:red, 8; green, 166; blue, 131 }  ,fill opacity=1 ] (131.85,116.65) -- (151.6,121.4) -- (150.6,126.4) -- (132.1,121.15) -- cycle ;
            	\draw [color={rgb, 255:red, 248; green, 231; blue, 28 }  ,draw opacity=1 ]   (126.1,94.9) -- (116.1,101.15) ;
            	\draw [color={rgb, 255:red, 248; green, 231; blue, 28 }  ,draw opacity=1 ]   (116.1,101.15) -- (116.35,109.9) ;
            	\draw [color={rgb, 255:red, 248; green, 231; blue, 28 }  ,draw opacity=1 ]   (222.85,82.15) -- (219.6,86.9) ;
            	\draw [color={rgb, 255:red, 248; green, 231; blue, 28 }  ,draw opacity=1 ]   (219.6,86.9) -- (220.1,96.4) ;
            	\draw [color={rgb, 255:red, 248; green, 231; blue, 28 }  ,draw opacity=1 ]   (196.35,113.65) -- (191.1,119.4) ;
            	\draw [color={rgb, 255:red, 248; green, 231; blue, 28 }  ,draw opacity=1 ]   (191.1,119.4) -- (190.85,128.4) ;
            	\draw [color={rgb, 255:red, 248; green, 231; blue, 28 }  ,draw opacity=1 ]   (165.6,74.15) -- (159.6,76.9) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.7 ] (76.16,37.14) -- (65.85,74.9) -- (60.85,81.4) -- (61.58,75.22) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.7 ] (58.05,90.23) -- (56.1,101.65) -- (40.58,143.65) -- (52.5,98.91) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.7 ] (137.05,44.36) -- (127.1,47.4) -- (88.5,53.81) -- (128,43.81) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.7 ] (191.55,32.65) -- (158.85,39.65) -- (148.35,41.65) -- (156.05,37.9) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.7 ] (220.4,141.21) -- (212.87,153.64) -- (152.79,161.23) -- (209.05,149.4) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.7 ] (294.14,123.04) -- (250.3,136.4) -- (235.33,136.9) -- (246.01,131.64) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.7 ] (189.55,63.15) -- (163.8,81.65) -- (129.76,112.44) -- (123.36,111.2) -- (148.3,87.4) -- (185.5,63) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.33 ] (214.56,72.4) -- (194.3,90.15) -- (171.8,116.4) -- (163.3,122.9) -- (154.55,118.65) -- (176.3,96.4) -- (212.05,70.15) -- cycle ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (132.8,118.65) -- (150.3,122.9) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.7 ] (271.2,67.1) -- (260.2,61.6) -- (237.15,34.85) -- (267.93,61.54) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.7 ] (310.19,108.07) -- (288.7,86.1) -- (281.77,76.05) -- (288.08,79.8) -- cycle ;
            	\draw [color={rgb, 255:red, 80; green, 227; blue, 194 }  ,draw opacity=1 ]   (126.6,141.1) .. controls (126.1,149.6) and (132.6,152.1) .. (146.6,149.1) ;
            	\draw [color={rgb, 255:red, 80; green, 227; blue, 194 }  ,draw opacity=1 ]   (119.1,145.1) .. controls (120.1,152.1) and (124.6,160.6) .. (146.6,156.1) ;
            	\draw [color={rgb, 255:red, 80; green, 227; blue, 194 }  ,draw opacity=1 ]   (110.6,146.6) .. controls (108.1,154.1) and (123.6,170.6) .. (148.6,162.6) ;
            \end{tikzpicture}'''
                # Câu hỏi
                noidungcauhoi = (r'''\immini{Một thiết bị bay Drone D được lập trình xuất phát từ điểm $A(%s;0)$ trong mặt phẳng tọa độ $Oxy$ (đơn vị: km), bay lên theo quỹ đạo là một phần của đường cong $(C): y = \frac{ax^2+bx+c}{x-m}$ và hạ cánh tại điểm $B(%s;0)$. Biết Drone D đạt độ cao lớn nhất tại điểm $H(%s;%s)$. Nhằm bảo vệ chống nhiễu sóng, vùng bay của Drone D được thiết lập hành lang an toàn bởi hai tia nằm dọc theo hai đường tiệm cận của $(C)$, phát ra từ trạm điều khiển $E$ đặt tại giao điểm của 2 đường tiệm cận. Trong quá trình di chuyển từ A đến B, Drone D liên tục phát ra một tia laser là tiếp tuyến với quỹ đạo. Tia laser này cắt hai tia bảo vệ tại hai điểm $P$ và $Q$. Hỏi độ dài ngắn nhất của đoạn $PQ$ bằng bao nhiêu km? (Kết quả làm tròn đến hàng phần trăm).}{%s}'''
                                 % (xA, xB, xH, yH, hinhve))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Xử lý chuỗi cho phần lời giải
                str_beta = ""
                if beta < 0:
                    str_beta = latex(beta)
                elif beta > 0:
                    str_beta = "+ " + latex(beta)

                yP_base = latex(alpha * m + beta)
                str_yP = yP_base + " + \\frac{" + latex(2*k) + "}{t}"
                str_yQ = latex(alpha) + "(2x_0 - " + str(m) + ")" + str_beta

                val2 = Decimal(float(val)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                str_val2 = str(val2).replace('.', ',')

                # Nội dung lời giải
                loigiai = ('''Quỹ đạo là đường cong $(C): y = \\frac{ax^2+bx+c}{x-m} = f(x)$.\\\\
                Vì Drone xuất phát từ $A(%s; 0)$ và hạ cánh tại $B(%s; 0)$ nên $A, B \\in (C)$, suy ra $f(%s) = 0, f(%s) = 0$. Do đó $f(x) = \\frac{a(x-%s)(x-%s)}{x-m}$.\\\\
                Ta có $f'(x) = \\frac{a[x^2 - 2mx + m(%s+%s) - %s \\cdot %s]}{(x-m)^2}$.\\\\
                Đạt độ cao lớn nhất tại $H(%s; %s)$ nên $f'(%s) = 0 \\Rightarrow %s^2 - 2m \\cdot %s + m(%s+%s) - %s \\cdot %s = 0 \\Rightarrow m = %s$.\\\\
                Lại có $f(%s) = %s \\Rightarrow \\frac{a(%s-%s)(%s-%s)}{%s-%s} = %s \\Rightarrow a = %s$.\\\\
                Khi đó $y = \\frac{%s(x-%s)(x-%s)}{x-%s}$. Phân tích ta được $y = %s x %s + \\frac{%s}{x - %s}$.\\\\
                Hai đường tiệm cận của $(C)$ là $d_1: x = %s$ và $d_2: y = %s x %s$. Giao điểm hai tiệm cận $E(%s; %s)$.\\\\
                Gọi tiếp điểm là $M(x_0; y_0) \\in (C)$. Phương trình tiếp tuyến $\\Delta$ tại $M$ có dạng: \\\\ $y = f'(x_0)(x - x_0) + f(x_0)$.\\\\
                Giao điểm của $\\Delta$ với $d_1, d_2$ lần lượt là $P, Q$. Giả sử $t = x_0 - %s$. \\\\
                Theo tính chất tiếp tuyến, ta có $P\\left(%s; %s \\right)$ và $Q\\left(2x_0 - %s; %s \\right)$.\\\\
                Độ dài $PQ^2 = (x_Q - x_P)^2 + (y_Q - y_P)^2 = (2t)^2 + \\left(2 \\cdot %s t - \\frac{2 \\cdot %s}{t}\\right)^2 = 4\\left(1 + %s\\right)t^2 + \\frac{4 \\cdot %s}{t^2} - 8 \\cdot %s \\cdot %s$.\\\\
                Đặt $u = t^2 (u > 0)$, xét hàm số $g(u) = 4\\left(1 + %s\\right)u + \\frac{4 \\cdot %s}{u} - 8 \\cdot %s \\cdot %s$.\\\\
                Ta có đạo hàm $g'(u) = 4\\left(1 + %s\\right) - \\frac{4 \\cdot %s}{u^2}$. Cho $g'(u) = 0 \\Leftrightarrow u^2 = \\frac{%s}{1 + %s} \\Rightarrow u = \\frac{%s}{\\sqrt{1 + %s}}$.\\\\
                Lập bảng biến thiên, ta thấy hàm số $g(u)$ liên tục và đổi dấu từ âm sang dương qua điểm $u = \\frac{%s}{\\sqrt{1 + %s}}$ nên đạt giá trị nhỏ nhất tại đây.\\\\
                Suy ra $PQ^2 \\ge g_{min} = 8 \\cdot %s \\left(\\sqrt{1+%s} - %s \\right)$.\\\\
                Thay số ta tính được $PQ^2 \\ge %s \\Rightarrow PQ \\ge %s$.\\\\
                Vậy độ dài ngắn nhất của đoạn $PQ$ là khoảng $%s$ km.'''
                % (xA, xB, xA, xB, xA, xB,
                   xA, xB, xA, xB,
                   xH, yH, xH, xH, xH, xA, xB, xA, xB, m,
                   xH, yH, xH, xA, xH, xB, xH, m, yH, latex(alpha),
                   latex(alpha), xA, xB, m, latex(alpha), str_beta, latex(k), m,
                   m, latex(alpha), str_beta, m, latex(alpha*m + beta),
                   m, m, str_yP, m, str_yQ,
                   latex(alpha), latex(k), latex(alpha**2), latex(k**2), latex(alpha), latex(k),

                   # Phần thay mới cho Xét hàm số
                   latex(alpha**2), latex(k**2), latex(alpha), latex(k), 
                   latex(alpha**2), latex(k**2), latex(k**2), latex(alpha**2), latex(k), latex(alpha**2),
                   latex(k), latex(alpha**2),
                   latex(k), latex(alpha**2), latex(alpha),

                   str_val2, kq, kq
                ))
                dapan='\\shortans[0]{$%s$}\n'%(kq)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n\\end{minipage} \n\n')
            return content


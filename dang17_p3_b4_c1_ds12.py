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


def bt_dang17_p3_b4_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                c = random.choice([2, 3, 4])
                x1 = c - 1
                y1 = random.choice([1, 2, 3])
                u = random.choice([10, 20, 30])

                m = y1 - c + 2
                a = m - c
                b = 1 - m * c

                x_sym = symbols('x')
                poly_num = x_sym**2 + a*x_sym + b
                num_latex = latex(poly_num)
                poly_quo = x_sym + m
                quo_latex = latex(poly_quo)

                eq1_rhs = x1**2 - 2*c*x1
                eq2_rhs = y1*(x1 - c) - x1**2

                D0_sq = 2 * math.sqrt(2) + 2
                D0 = math.sqrt(D0_sq)
                L = 2 * D0 * u

                kq = Decimal(float(L)).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
                kq_str = str(kq).replace('.', ',')

                # Các đáp án trắc nghiệm
                s_vals = [
                    Decimal(float(L + random.uniform(1.0, 3.0))).quantize(Decimal('1'), rounding=ROUND_HALF_UP),
                    Decimal(float(L - random.uniform(1.0, 3.0))).quantize(Decimal('1'), rounding=ROUND_HALF_UP),
                    Decimal(float(L + 5)).quantize(Decimal('1'), rounding=ROUND_HALF_UP),
                    Decimal(float(L - 5)).quantize(Decimal('1'), rounding=ROUND_HALF_UP),
                    Decimal(float(D0 * u)).quantize(Decimal('1'), rounding=ROUND_HALF_UP),
                    Decimal(float(L * 1.5)).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
                ]

                s = []
                for val in s_vals:
                    if val != kq:
                        s.append('$%s$' % str(val).replace('.', ','))

                s = list(set(s))
                random.shuffle(s)

                da = '$%s$' % kq_str

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi (Đã điều chỉnh dạng x^2 + ax + b)
                noidungcauhoi = ('''\\immini{Hình dáng phần đất liền của hai xã thuộc tỉnh Đồng Tháp được mô hình hóa bởi đồ thị hàm số $y = \\frac{x^2 + ax + b}{x - %s}$; biết đồ thị có một điểm cực trị là $(%s; %s)$, với hệ trục tọa độ $Oxy$ như hình vẽ, đơn vị trên mỗi trục là $%s$ mét. Để thuận tiện cho giao thông hai xã, lãnh đạo tỉnh đã phê duyệt dự án xây một chiếc cầu nối phần đất liền của hai xã này. Nhằm tiết kiệm chi phí cho công trình, người kỹ sư trưởng thiết kế có nhiệm vụ nghiên cứu để chọn được hai vị trí $A$, $B$ trên phần đất liền hai xã sao cho độ dài chiếc cầu (đoạn $AB$) là ngắn nhất có thể. Hỏi độ dài ngắn nhất của chiếc cầu đó (tính theo đường chim bay) là bao nhiêu mét? (làm tròn đến hàng đơn vị).}
                                 {\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
                                 	\\tikzset {_s14f1969e/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{-91 }  \\pgftransformscale{2 }  }}}
                                 	\\pgfdeclarehorizontalshading{_zs9106glz}{150bp}{rgb(0bp)=(0.6,0.85,1);
                                 		rgb(37.5bp)=(0.6,0.85,1);
                                 		rgb(62.5bp)=(0.13,0.83,0.57);
                                 		rgb(100bp)=(0.13,0.83,0.57)}
                                 	\\tikzset{every picture/.style={line width=0.75pt}} 
                                 	\\draw  [draw opacity=0][shading=_zs9106glz,_s14f1969e] (18.4,33) -- (218.24,33) -- (218.24,232.32) -- (18.4,232.32) -- cycle ;
                                 	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.2 ] (83.44,53.92) .. controls (108.3,53.92) and (128.45,59.2) .. (128.45,65.72) .. controls (128.45,66.6) and (128.08,67.46) .. (127.39,68.29) .. controls (130.85,68.06) and (134.47,67.94) .. (138.2,67.94) .. controls (163.06,67.94) and (183.21,73.23) .. (183.21,79.75) .. controls (183.21,86.27) and (163.06,91.55) .. (138.2,91.55) .. controls (135.79,91.55) and (133.43,91.5) .. (131.12,91.41) .. controls (131.08,94.55) and (128.78,97.52) .. (124.74,100.11) .. controls (133.86,97.95) and (145.24,96.66) .. (157.57,96.66) .. controls (187.59,96.66) and (211.93,104.29) .. (211.93,113.69) .. controls (211.93,123.1) and (187.59,130.72) .. (157.57,130.72) .. controls (127.55,130.72) and (103.21,123.1) .. (103.21,113.69) .. controls (103.21,111.16) and (104.98,108.75) .. (108.15,106.59) .. controls (99.28,108.75) and (88.45,110.02) .. (76.76,110.02) .. controls (46.74,110.02) and (22.4,101.65) .. (22.4,91.32) .. controls (22.4,83.9) and (34.97,77.48) .. (53.19,74.46) .. controls (44.12,72.3) and (38.43,69.19) .. (38.43,65.72) .. controls (38.43,59.2) and (58.58,53.92) .. (83.44,53.92) -- cycle ;
                                 	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.2 ] (140.96,209.92) .. controls (118.61,209.92) and (100.49,205.85) .. (100.49,200.82) .. controls (100.49,200.14) and (100.82,199.48) .. (101.45,198.85) .. controls (98.34,199.02) and (95.08,199.11) .. (91.73,199.11) .. controls (69.38,199.11) and (51.26,195.04) .. (51.26,190.01) .. controls (51.26,184.99) and (69.38,180.91) .. (91.73,180.91) .. controls (93.89,180.91) and (96.02,180.95) .. (98.09,181.02) .. controls (98.13,178.6) and (100.2,176.31) .. (103.83,174.31) .. controls (95.63,175.98) and (85.4,176.97) .. (74.31,176.97) .. controls (47.32,176.97) and (25.44,171.1) .. (25.44,163.85) .. controls (25.44,156.6) and (47.32,150.72) .. (74.31,150.72) .. controls (101.31,150.72) and (123.19,156.6) .. (123.19,163.85) .. controls (123.19,165.8) and (121.6,167.66) .. (118.75,169.32) .. controls (126.72,167.66) and (136.45,166.68) .. (146.97,166.68) .. controls (173.96,166.68) and (195.84,173.13) .. (195.84,181.09) .. controls (195.84,186.81) and (184.54,191.76) .. (168.16,194.08) .. controls (176.31,195.75) and (181.43,198.15) .. (181.43,200.82) .. controls (181.43,205.85) and (163.31,209.92) .. (140.96,209.92) -- cycle ;
                                 	\\draw [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ][line width=1]    (128.64,33.12) .. controls (134.24,113.12) and (132.64,140.2) .. (218.24,33) ;
                                 	\\draw [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ][line width=1]    (118.32,232.32) .. controls (114.24,137.92) and (95.04,149.92) .. (20.72,233.52) ;
                                 	\\draw [line width=1]    (84.64,231.52) -- (84.64,37.12) ;
                                 	\\draw [shift={(84.64,33.12)}, rotate = 90] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (8.75,-4.2) -- (0,0) -- (8.75,4.2) -- (5.81,0) -- cycle    ;
                                 	\\draw [line width=1]    (19.04,189.12) -- (215.84,189.12) ;
                                 	\\draw [shift={(219.84,189.12)}, rotate = 180] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (8.75,-4.2) -- (0,0) -- (8.75,4.2) -- (5.81,0) -- cycle    ;
                                 	\\draw (68,193) node [anchor=north west][inner sep=0.75pt]    {$O$};
                                 	\\draw (205,193) node [anchor=north west][inner sep=0.75pt]    {$x$};
                                 	\\draw (68,32.8) node [anchor=north west][inner sep=0.75pt]    {$y$};
                                 \\end{tikzpicture}}'''
                                 % (latex(c), latex(x1), latex(y1), latex(u)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (Đã thay đổi sang xét hàm và lập BBT bằng TikZ)
                loigiai = ('''Ta có $y = \\frac{x^2 + ax + b}{x - %s} \\Rightarrow y' = \\frac{x^2 - %sx - %sa - b}{(x - %s)^2}$.\\\\
            Đồ thị hàm số có điểm cực trị $(%s; %s)$ nên: \\\\
            $\\begin{cases} y'(%s) = 0 \\\\ y(%s) = %s \\end{cases} \\Leftrightarrow \\begin{cases} %s - %s - %sa - b = 0 \\\\ \\frac{%s + %sa + b}{%s - %s} = %s \\end{cases} \\Leftrightarrow \\begin{cases} %sa + b = %s \\\\ %sa + b = %s \\end{cases} \\Leftrightarrow \\begin{cases} a = %s \\\\ b = %s \\end{cases}$.\\\\
            Khi đó $y = \\frac{%s}{x - %s} = %s + \\frac{1}{x - %s}$.\\\\
            Gọi $I(%s; %s)$ là giao điểm của hai đường tiệm cận.\\\\
            Lấy $A\\left(%s + \\alpha; %s + \\alpha + \\frac{1}{\\alpha}\\right)$ với $\\alpha > 0$ trên nhánh phải và $B\\left(%s - \\beta; %s - \\beta - \\frac{1}{\\beta}\\right)$ với $\\beta > 0$ trên nhánh trái.\\\\
            Để $AB$ ngắn nhất thì tiếp tuyến tại $A$ và $B$ song song và khoảng cách $AB$ ngắn nhất khi $A, B$ đối xứng nhau qua $I$, tức là $\\alpha = \\beta$ và $AB = 2IA$.\\\\
            Ta có $IA^2 = \\alpha^2 + \\left(\\alpha + \\frac{1}{\\alpha}\\right)^2 = 2\\alpha^2 + \\frac{1}{\\alpha^2} + 2$.\\\\
            Xét hàm số $f(t) = 2t^2 + \\frac{1}{t^2} + 2$ với $t > 0$ (ở đây $t = \\alpha$).\\\\
            Ta có $f'(t) = 4t - \\frac{2}{t^3} = \\frac{4t^4 - 2}{t^3}$.\\\\
            $f'(t) = 0 \\Leftrightarrow 4t^4 - 2 = 0 \\Leftrightarrow t = \\frac{1}{\\sqrt[4]{2}}$ (do $t > 0$).\\\\
            Bảng biến thiên:
            \\begin{center}
            \\begin{tikzpicture}
            \\tkzTabInit[nocadre=false,lgt=1.5,espcl=3,deltacl=0.5]{$t$ / 1, $f'(t)$ / 1, $f(t)$ / 2.5}{$0$, $\\frac{1}{\\sqrt[4]{2}}$, $+\\infty$}
            \\tkzTabLine{ , -, 0, +, }
            \\tkzTabVar{+/ $+\\infty$, -/ $2\\sqrt{2}+2$, +/ $+\\infty$}
            \\end{tikzpicture}
            \\end{center}
            Dựa vào bảng biến thiên, ta thấy $\\min_{(0; +\\infty)} f(t) = f\\left(\\frac{1}{\\sqrt[4]{2}}\\right) = 2\\sqrt{2} + 2$.\\\\
            Do đó $IA^2 \\ge 2\\sqrt{2} + 2 \\Rightarrow IA \\ge \\sqrt{2\\sqrt{2} + 2}$.\\\\
            Suy ra $AB = 2IA \\ge 2\\sqrt{2\\sqrt{2} + 2}$.\\\\
            Khoảng cách thực tế ngắn nhất là $2\\sqrt{2\\sqrt{2} + 2} \\cdot %s \\approx %s$ (m).'''
                           % (latex(c), latex(2*c), latex(c), latex(c),
                              latex(x1), latex(y1),
                              latex(x1), latex(x1), latex(y1),
                              latex(x1**2), latex(2*c*x1), latex(c),
                              latex(x1**2), latex(x1), latex(x1), latex(c), latex(y1),
                              latex(c), latex(eq1_rhs), latex(x1), latex(eq2_rhs),
                              latex(a), latex(b),
                              num_latex, latex(c), quo_latex, latex(c),
                              latex(c), latex(c+m),
                              latex(c), latex(c+m), latex(c), latex(c+m),
                              latex(u), kq_str
                             ))
            dapan='\\shortans[0]{$%s$}\n'%(kq_str)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


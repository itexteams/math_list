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


def bt_dang37_p4_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B3-Suy nghĩ tìm cách random bài toán
                # Trục lớn 2a, trục bé 2b. Để số đẹp, ta chọn a và b sao cho a chia hết cho 5 hoặc 10
                a_val = random.choice([70, 75, 80, 85, 90])
                b_val = random.choice([40, 45, 50, 55, 60])

                truc_lon = 2 * a_val
                truc_be = 2 * b_val


                v_numeric = (2/3) * a_val * (b_val**2) * (math.pi - 2)
                kq_val = int(Decimal(v_numeric).quantize(Decimal('1'), rounding=ROUND_HALF_UP))

                # Đáp án đúng
                da = f"${kq_val}$"

                # B4-Điều chỉnh các phương án sai không được phép trùng với đáp án đúng
                s = set()
                while len(s) < 3:
                    sai = kq_val + random.choice([-2000, -1500, -1000, 1000, 1500, 2000]) + random.randint(-500, 500)
                    if sai != kq_val:
                        s.add(f"${sai}$")

                list_sai = list(s)
                das1, das2, das3 = list_sai[0], list_sai[1], list_sai[2]

                # Nội dung câu hỏi
                noidungcauhoi = ('''Sân vận động Sport Hub (Singapore) là sân có mái vòm kỳ vĩ nhất thế giới. 
                                 Nền sân là một elip $(E)$ có trục lớn dài $%s$m, trục bé dài $%s$m. 
                                 Nếu cắt sân vận động theo một mặt phẳng vuông góc với trục lớn của $(E)$ và cắt elip ở $M, N$ 
                                 thì ta được thiết diện luôn là một phần của hình tròn có tâm $I$ với $MN$ là một dây cung 
                                 và góc $\\widehat{{MIN}} = 90^\\circ$.
                                 \\begin{center}
            	\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            		\\draw   (44.53,73.77) .. controls (44.53,45.05) and (87.53,21.77) .. (140.58,21.77) .. controls (193.62,21.77) and (236.63,45.05) .. (236.63,73.77) .. controls (236.63,102.5) and (193.62,125.78) .. (140.58,125.78) .. controls (87.53,125.78) and (44.53,102.5) .. (44.53,73.77) -- cycle ;
            		\\draw   (48.47,72.62) .. controls (48.47,44.79) and (90.13,22.23) .. (141.52,22.23) .. controls (192.91,22.23) and (234.57,44.79) .. (234.57,72.62) .. controls (234.57,100.44) and (192.91,123) .. (141.52,123) .. controls (90.13,123) and (48.47,100.44) .. (48.47,72.62) -- cycle ;
            		\\draw  [draw opacity=0] (48.74,71.71) .. controls (64.86,58.5) and (96.81,46.02) .. (134.73,39.54) .. controls (163.61,34.6) and (190.4,34.1) .. (210.18,37.28) -- (140.58,73.77) -- cycle ; \\draw   (48.74,71.71) .. controls (64.86,58.5) and (96.81,46.02) .. (134.73,39.54) .. controls (163.61,34.6) and (190.4,34.1) .. (210.18,37.28) ;  
            		\\draw  [draw opacity=0] (62.2,98.55) .. controls (77.56,84.48) and (108.78,70.25) .. (146.27,61.68) .. controls (179.58,54.07) and (210.37,52.64) .. (230.82,56.62) -- (154.01,95.54) -- cycle ; \\draw   (62.2,98.55) .. controls (77.56,84.48) and (108.78,70.25) .. (146.27,61.68) .. controls (179.58,54.07) and (210.37,52.64) .. (230.82,56.62) ;  
            		\\draw  [draw opacity=0] (48.86,71.37) .. controls (52.59,53.99) and (85.29,36.06) .. (127.11,29.58) .. controls (158.82,24.66) and (187.53,27.61) .. (203.4,36.06) -- (132.43,63.9) -- cycle ; \\draw   (48.86,71.37) .. controls (52.59,53.99) and (85.29,36.06) .. (127.11,29.58) .. controls (158.82,24.66) and (187.53,27.61) .. (203.4,36.06) ;  
            		\\draw  [draw opacity=0] (230.54,56.92) .. controls (228.12,74.96) and (189.33,94.16) .. (139.89,101.03) .. controls (109.28,105.29) and (81.31,103.88) .. (62.72,98.22) -- (135.11,66.63) -- cycle ; \\draw   (230.54,56.92) .. controls (228.12,74.96) and (189.33,94.16) .. (139.89,101.03) .. controls (109.28,105.29) and (81.31,103.88) .. (62.72,98.22) ;  
            		\\draw  [draw opacity=0] (63.04,47.14) .. controls (75.85,51.73) and (88.63,64.37) .. (96.38,81.8) .. controls (101.98,94.41) and (103.95,107.28) .. (102.66,118.21) -- (64.64,95.91) -- cycle ; \\draw   (63.04,47.14) .. controls (75.85,51.73) and (88.63,64.37) .. (96.38,81.8) .. controls (101.98,94.41) and (103.95,107.28) .. (102.66,118.21) ;  
            		\\draw  [draw opacity=0] (86.61,30.79) .. controls (101.26,34.42) and (117.06,49.61) .. (126.61,71.12) .. controls (134.96,89.89) and (136.54,108.97) .. (132.07,122.36) -- (94.87,85.22) -- cycle ; \\draw   (86.61,30.79) .. controls (101.26,34.42) and (117.06,49.61) .. (126.61,71.12) .. controls (134.96,89.89) and (136.54,108.97) .. (132.07,122.36) ;  
            		\\draw  [draw opacity=0] (107.95,25.35) .. controls (125.46,17.85) and (150.35,35.93) .. (163.67,65.9) .. controls (172.54,85.86) and (174.06,106.09) .. (168.97,119.74) -- (131.93,80.01) -- cycle ; \\draw   (107.95,25.35) .. controls (125.46,17.85) and (150.35,35.93) .. (163.67,65.9) .. controls (172.54,85.86) and (174.06,106.09) .. (168.97,119.74) ;  
            		\\draw  [draw opacity=0] (148.46,22.68) .. controls (165.46,18.79) and (186.73,34.08) .. (197.86,59.12) .. controls (206.4,78.35) and (206.67,98.16) .. (199.88,110.85) -- (166.12,73.23) -- cycle ; \\draw   (148.46,22.68) .. controls (165.46,18.79) and (186.73,34.08) .. (197.86,59.12) .. controls (206.4,78.35) and (206.67,98.16) .. (199.88,110.85) ;  
            		\\draw  [draw opacity=0] (197.03,33.79) .. controls (207.37,37.88) and (216.81,46.88) .. (222.29,59.22) .. controls (227.82,71.67) and (228.14,84.82) .. (224.14,95.27) -- (190.55,73.33) -- cycle ; \\draw   (197.03,33.79) .. controls (207.37,37.88) and (216.81,46.88) .. (222.29,59.22) .. controls (227.82,71.67) and (228.14,84.82) .. (224.14,95.27) ;  
            		\\draw    (94.45,79.19) -- (80.56,110.68) ;
            		\\draw    (94.45,79.19) -- (132.07,122.36) ;
            		\\draw    (102.66,118.21) -- (124.55,67.61) ;
            		\\draw    (168.97,119.74) -- (124.55,67.61) ;
            		\\draw    (160.68,59.28) -- (132.07,122.36) ;
            		\\draw    (160.68,59.28) -- (199.88,110.85) ;
            		\\draw    (194.95,55.11) -- (168.97,119.74) ;
            		\\draw    (194.95,55.11) -- (224.14,95.27) ;
            		\\draw    (220.88,56.5) -- (199.88,110.85) ;
            		\\draw    (220.88,56.5) -- (233.38,75.49) ;
            		\\draw    (77.32,55.57) -- (54.63,55.57) ;
            		\\draw    (86.61,30.79) -- (77.32,55.57) ;
            		\\draw    (119.92,23.62) -- (109.74,45.39) ;
            		\\draw    (160.68,23.16) -- (145.39,37.98) ;
            		\\draw    (186.61,27.79) -- (181.98,36.12) ; 
            		\\draw    (109.74,45.39) -- (63.04,47.14) ;
            		\\draw    (145.39,37.98) -- (86.61,30.79) ;
            		\\draw    (181.98,36.12) -- (119.92,23.62) ;
            		\\draw  [draw opacity=0] (82.04,60.48) .. controls (97.87,53.07) and (118.34,46.77) .. (141.08,42.87) .. controls (166.66,38.49) and (190.53,37.94) .. (208.92,40.59) -- (146.95,77.11) -- cycle ; \\draw   (82.04,60.48) .. controls (97.87,53.07) and (118.34,46.77) .. (141.08,42.87) .. controls (166.66,38.49) and (190.53,37.94) .. (208.92,40.59) ;  
            		\\draw  [draw opacity=0] (85.75,65.11) .. controls (101.58,57.7) and (122.04,51.4) .. (144.79,47.5) .. controls (170.37,43.12) and (194.24,42.57) .. (212.63,45.22) -- (150.65,81.74) -- cycle ; \\draw   (85.75,65.11) .. controls (101.58,57.7) and (122.04,51.4) .. (144.79,47.5) .. controls (170.37,43.12) and (194.24,42.57) .. (212.63,45.22) ;  
            		\\draw  [draw opacity=0] (88.72,70.14) .. controls (104.42,62.47) and (124.78,55.82) .. (147.46,51.54) .. controls (172.96,46.73) and (196.82,45.78) .. (215.25,48.12) -- (153.89,85.67) -- cycle ; \\draw   (88.72,70.14) .. controls (104.42,62.47) and (124.78,55.82) .. (147.46,51.54) .. controls (172.96,46.73) and (196.82,45.78) .. (215.25,48.12) ;  
            		\\draw  [draw opacity=0] (91.76,75.55) .. controls (107.41,67.74) and (127.75,60.92) .. (150.43,56.46) .. controls (175.89,51.45) and (199.75,50.31) .. (218.19,52.5) -- (157.14,90.54) -- cycle ; \\draw   (91.76,75.55) .. controls (107.41,67.74) and (127.75,60.92) .. (150.43,56.46) .. controls (175.89,51.45) and (199.75,50.31) .. (218.19,52.5) ;  
            	\\end{tikzpicture}
            	\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            		\\draw   (10.8,68.76) .. controls (10.8,40.37) and (45.97,17.36) .. (89.36,17.36) .. controls (132.75,17.36) and (167.92,40.37) .. (167.92,68.76) .. controls (167.92,97.15) and (132.75,120.16) .. (89.36,120.16) .. controls (45.97,120.16) and (10.8,97.15) .. (10.8,68.76) -- cycle ;
            		\\draw    (10.8,68.76) -- (167.92,68.76) ;
            		\\draw    (130.32,24.56) -- (130.72,112.56) ;
            		\\draw (120.8,0.8) node [anchor=north west][inner sep=0.75pt]    {$M$};
            		\\draw (123.2,111.4) node [anchor=north west][inner sep=0.75pt]    {$N$};
            	\\end{tikzpicture}
            	\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            		\\draw   (17.44,69.36) .. controls (17.44,39.98) and (41.26,16.16) .. (70.64,16.16) .. controls (100.02,16.16) and (123.84,39.98) .. (123.84,69.36) .. controls (123.84,98.74) and (100.02,122.56) .. (70.64,122.56) .. controls (41.26,122.56) and (17.44,98.74) .. (17.44,69.36) -- cycle ;
            		\\draw   (69,69.36) .. controls (69,68.91) and (69.37,68.54) .. (69.82,68.54) .. controls (70.27,68.54) and (70.64,68.91) .. (70.64,69.36) .. controls (70.64,69.81) and (70.27,70.18) .. (69.82,70.18) .. controls (69.37,70.18) and (69,69.81) .. (69,69.36) -- cycle ;
            		\\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (32.06,32.44) .. controls (38.7,22.61) and (53.85,15.89) .. (71.37,16.17) .. controls (88.4,16.44) and (102.98,23.25) .. (109.6,32.84) -- cycle ;
            		\\draw (113.6,18.4) node [anchor=north west][inner sep=0.75pt]    {$M$};
            		\\draw (12.8,17) node [anchor=north west][inner sep=0.75pt]    {$N$};
            	\\end{tikzpicture}
            \\end{center}
                                 Tính thể tích phần không gian bên dưới mái che và bên trên mặt sân 
                                 (coi mặt sân là một mặt phẳng và thể tích vật liệu là mái không đáng kể).''' %(truc_lon, truc_be))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (B2 - Viết lại y hệt cấu trúc logic của đề bài)
                b2 = b_val**2
                a2 = a_val**2

                loigiai = (r'''\begin{center}
            				\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            					\draw   (270.77,95.36) .. controls (270.77,65.98) and (294.59,42.16) .. (323.97,42.16) .. controls (353.35,42.16) and (377.17,65.98) .. (377.17,95.36) .. controls (377.17,124.74) and (353.35,148.56) .. (323.97,148.56) .. controls (294.59,148.56) and (270.77,124.74) .. (270.77,95.36) -- cycle ;
            					\draw   (322.33,95.36) .. controls (322.33,94.91) and (322.7,94.54) .. (323.15,94.54) .. controls (323.61,94.54) and (323.97,94.91) .. (323.97,95.36) .. controls (323.97,95.81) and (323.61,96.18) .. (323.15,96.18) .. controls (322.7,96.18) and (322.33,95.81) .. (322.33,95.36) -- cycle ;
            					\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (285.39,58.44) .. controls (292.03,48.61) and (307.19,41.89) .. (324.71,42.17) .. controls (341.74,42.44) and (356.32,49.25) .. (362.93,58.84) -- cycle ;
            					\draw   (43.73,99.25) .. controls (43.73,69.19) and (82.83,44.83) .. (131.07,44.83) .. controls (179.3,44.83) and (218.4,69.19) .. (218.4,99.25) .. controls (218.4,129.3) and (179.3,153.67) .. (131.07,153.67) .. controls (82.83,153.67) and (43.73,129.3) .. (43.73,99.25) -- cycle ;
            					\draw    (29.07,95.47) -- (239.73,96.79) ;
            					\draw [shift={(241.73,96.8)}, rotate = 180.36] [color={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.75]    (10.93,-3.29) .. controls (6.95,-1.4) and (3.31,-0.3) .. (0,0) .. controls (3.31,0.3) and (6.95,1.4) .. (10.93,3.29)   ;
            					\draw    (285.39,58.44) -- (323.15,96.18) ;
            					\draw    (362.93,58.84) -- (323.15,96.18) ;
            					\draw    (163.07,48.8) -- (163.07,150.8) ;
            					\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (128.8,95.98) .. controls (128.8,94.73) and (129.81,93.71) .. (131.07,93.71) .. controls (132.32,93.71) and (133.33,94.73) .. (133.33,95.98) .. controls (133.33,97.23) and (132.32,98.25) .. (131.07,98.25) .. controls (129.81,98.25) and (128.8,97.23) .. (128.8,95.98) -- cycle ;
            					\draw (366.93,44.4) node [anchor=north west][inner sep=0.75pt]    {$M$};
            					\draw (266.13,43) node [anchor=north west][inner sep=0.75pt]    {$N$};
            					\draw (155.6,23.07) node [anchor=north west][inner sep=0.75pt]    {$M$};
            					\draw (155.47,153.67) node [anchor=north west][inner sep=0.75pt]    {$N$};
            					\draw (224.67,98) node [anchor=north west][inner sep=0.75pt]    {$x$};
            					\draw (118.67,98.33) node [anchor=north west][inner sep=0.75pt]    {$O$};
            					\draw (315.6,95.07) node [anchor=north west][inner sep=0.75pt]    {$I$};
            					\draw (343.04,77.51) node [anchor=north west][inner sep=0.75pt]    {$R$};
            				\end{tikzpicture}
            			\end{center}'''
                    f"Chọn hệ trục tọa độ sao cho phương trình elip là $(E): \\frac{{x^2}}{{{a_val}^2}} + \\frac{{y^2}}{{{b_val}^2}} = 1$. "
                           f"Ta cần tìm diện tích $S(x)$ của thiết diện tại hoành độ $x \\in [-{a_val}; {a_val}]$. \\\\"
                           f"Tại vị trí $x$, độ dài dây cung $MN = 2y = 2 \\cdot {b_val}\\sqrt{{1 - \\frac{{x^2}}{{{a_val}^2}}}}$. \\\\"
                           f"Vì $\\triangle MIN$ vuông cân tại $I$ (do $\\widehat{{MIN}} = 90^\\circ$) nên bán kính thiết diện $R = \\frac{{MN}}{{\\sqrt{2}}}$. \\\\"
                           f"Diện tích thiết diện là phần hình tròn giới hạn bởi dây cung $MN$ (hình quạt $90^\\circ$ trừ diện tích tam giác): \\\\"
                           f"$S(x) = \\frac{{1}}{{4}}\\pi R^2 - \\frac{{1}}{{2}}R^2 = \\frac{{\\pi - 2}}{{4}}R^2 = \\frac{{\\pi - 2}}{{4}} \\cdot \\frac{{MN^2}}{{2}} = \\frac{{\\pi - 2}}{{2}}y^2$. \\\\"
                           f"Thay $y^2 = {b_val}^2\\left(1 - \\frac{{x^2}}{{{a_val}^2}}\\right)$, ta có $S(x) = \\frac{{\\pi - 2}}{{2}} \\cdot {b2} \\left(1 - \\frac{{x^2}}{{{a_val}^2}}\\right)$. \\\\"
                           f"Thể tích cần tìm là: \\\\"
                           f"$V = \\int_{{-{a_val}}}^{{{a_val}}} \\frac{{\\pi - 2}}{{2}} \\cdot {b2} \\left(1 - \\frac{{x^2}}{{{a_val}^2}}\\right) \\text{{d}}x \\approx {kq_val} \\text{{m}}^3$.")

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content


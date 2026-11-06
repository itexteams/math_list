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


def bt_dang53_p3_b2_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Sử dụng vòng lặp while để đảm bảo 0 < max_profit_trieu < 9999
                while True:
                    # Random các hệ số của bài toán
                    b_num = random.choice([2, 4, 5, 8])
                    b_val = b_num / 10.0 # Random b = 0.2, 0.4, 0.5, 0.8

                    # Chọn x_max (số lượng mô hình cho lợi nhuận cực đại)
                    x_max = random.choice([400, 500, 600, 750, 800, 1000])

                    # Random chi phí trên mỗi đơn vị (d) và chi phí cố định (c)
                    d = random.choice([100, 150, 200, 250, 300])
                    c_base = random.choice([50, 80, 100, 120, 150])
                    c = c_base * 1000

                    # Tính hệ số a sao cho lợi nhuận lớn nhất đạt được đúng tại x_max
                    # x_max = (a - d) / (2b) => a - d = 2b * x_max => a = 2b * x_max + d
                    a = int(2 * b_val * x_max + d)
                    a_minus_d = a - d

                    # Các giá trị tính toán trung gian dùng trong lời giải
                    term1 = int(b_val * (x_max**2))
                    term2 = int(a_minus_d * x_max)

                    # Lợi nhuận cực đại (đơn vị nghìn đồng) và (đơn vị triệu đồng)
                    max_profit_nghin = -term1 + term2 - c
                    max_profit_trieu = int(max_profit_nghin / 1000)

                    # Kiểm tra điều kiện bắt buộc
                    if 0 < max_profit_trieu < 9999:
                        break

                # Định dạng các số thập phân dùng dấu phẩy
                b_str = str(b_val).replace('.', ',')
                two_b_str = str(b_val * 2).replace('.', ',')

                # Khoảng giới hạn của x trong đề bài
                x_limit = x_max * 2 + random.choice([500, 1000])

                # Đáp án đúng
                da = '$%s$ triệu đồng' % latex(max_profit_trieu)

                # Tạo các đáp án nhiễu dựa trên sai lầm thường gặp
                s_vals = set()
                s_vals.add(max_profit_trieu + c_base * 2) # Lỗi: cộng thêm chi phí c thay vì trừ
                s_vals.add(x_max)                         # Lỗi: chọn nhầm giá trị x làm lợi nhuận
                s_vals.add(max_profit_trieu + random.choice([10, 15, 20, 30])) # Lỗi tính toán bù trừ
                s_vals.add(max_profit_trieu - random.choice([10, 15, 20, 30])) # Lỗi tính toán bù trừ

                # Đảm bảo loại bỏ đáp án đúng khỏi danh sách nhiễu (nếu bị trùng ngẫu nhiên)
                if max_profit_trieu in s_vals:
                    s_vals.remove(max_profit_trieu)

                s_list = list(s_vals)[:3]
                s = ['$%s$ triệu đồng' % latex(val) for val in s_list]

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Đã loại bỏ raw string (tiền tố r) và nhân đôi các dấu backslash để tuân thủ luật
                hinhve = ('''\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            \t\\tikzset {_mhnm7oucs/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{-41 }  \\pgftransformscale{2 }  }}}
            \t\\pgfdeclarehorizontalshading{_1pau0o0nc}{150bp}{rgb(0bp)=(0.6,0.52,0.12);
            \t\trgb(37.96428680419922bp)=(0.6,0.52,0.12);
            \t\trgb(48.44643184116909bp)=(0.82,0.72,0.25);
            \t\trgb(52.73214612688337bp)=(0.89,0.84,0.6);
            \t\trgb(55.94532012939453bp)=(0.82,0.72,0.25);
            \t\trgb(61.803572518484934bp)=(0.51,0.44,0.07);
            \t\trgb(100bp)=(0.51,0.44,0.07)}
            \t\\tikzset {_l4mkuqh53/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{80.52 bp } { -133.98 bp }  }  \\pgftransformscale{1.32 }  }}}
            \t\\pgfdeclareradialshading{_z1em4h3ab}{\\pgfpoint{-72bp}{104bp}}{rgb(0bp)=(0.95,0.93,0.61);
            \t\trgb(0bp)=(0.95,0.93,0.61);
            \t\trgb(6.123883383614676bp)=(0.82,0.72,0.25);
            \t\trgb(25bp)=(0.62,0.52,0.04);
            \t\trgb(400bp)=(0.62,0.52,0.04)}
            \t\\tikzset {_voq84wsu2/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{0 }  \\pgftransformscale{2 }  }}}
            \t\\pgfdeclarehorizontalshading{_ksnmg3bfu}{150bp}{rgb(0bp)=(0.05,0.31,0.05);
            \t\trgb(44.178575788225444bp)=(0.05,0.31,0.05);
            \t\trgb(48.464290073939736bp)=(0.29,0.64,0.15);
            \t\trgb(54.625004359654014bp)=(0.02,0.29,0.02);
            \t\trgb(100bp)=(0.02,0.29,0.02)}
            \t\\tikzset {_flmt02lqk/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{0 }  \\pgftransformscale{2 }  }}}
            \t\\pgfdeclarehorizontalshading{_p2gvjpsk6}{150bp}{rgb(0bp)=(0.07,0.22,0.07);
            \t\trgb(45.8749989100865bp)=(0.07,0.22,0.07);
            \t\trgb(50bp)=(0.11,0.64,0.11);
            \t\trgb(54.64174270629883bp)=(0.07,0.22,0.07);
            \t\trgb(62.5bp)=(0.02,0.29,0.02);
            \t\trgb(100bp)=(0.02,0.29,0.02)}
            \t\\tikzset{every picture/.style={line width=0.75pt}} 
            \t\\draw  [draw opacity=0][shading=_1pau0o0nc,_mhnm7oucs] (134.6,137.4) .. controls (126.58,126.74) and (121.6,110.4) .. (123.1,98.4) .. controls (117.86,89.8) and (116.02,82.09) .. (116.65,75.41) .. controls (117.94,75.73) and (119.3,75.73) .. (120.71,75.46) .. controls (111.6,31.4) and (184.6,21.4) .. (192.73,64.64) .. controls (194.51,64.94) and (196.27,65.31) .. (198.02,65.74) .. controls (199.05,74.7) and (195.67,88.9) .. (185.67,110.41) .. controls (184.78,119.22) and (182.38,129.8) .. (178.1,142.4) .. controls (164.6,168.9) and (177.1,188.9) .. (194.6,218.9) .. controls (169.1,220.4) and (153.1,219.9) .. (116.6,218.4) .. controls (139.2,171.8) and (139.1,176.4) .. (134.6,137.4) -- cycle ;
            \t\\draw  [draw opacity=0][shading=_z1em4h3ab,_l4mkuqh53] (116.76,65.01) .. controls (116.76,43.75) and (134,26.51) .. (155.26,26.51) .. controls (176.52,26.51) and (193.76,43.75) .. (193.76,65.01) .. controls (193.76,86.27) and (176.52,103.51) .. (155.26,103.51) .. controls (134,103.51) and (116.76,86.27) .. (116.76,65.01) -- cycle ;
            \t\\draw  [draw opacity=0][fill={rgb, 255:red, 186; green, 164; blue, 56 }  ,fill opacity=1 ] (152.1,50.4) .. controls (148.94,41.79) and (155.78,51.07) .. (156.6,52.9) .. controls (166.39,74.88) and (166.14,87.82) .. (170.76,103.51) .. controls (179.8,94.57) and (189.26,94.51) .. (193.76,65.01) .. controls (195.91,66.22) and (197.73,68.91) .. (199.29,72.7) .. controls (191.82,87.23) and (193.76,98.51) .. (185.67,110.41) .. controls (177.69,155.77) and (165.76,170.51) .. (132.66,187.61) .. controls (164.26,130.51) and (167.1,104.9) .. (152.1,50.4) -- cycle ;
            \t\\draw  [draw opacity=0][fill={rgb, 255:red, 186; green, 164; blue, 56 }  ,fill opacity=1 ] (169.6,93.4) .. controls (169.6,89.26) and (172.96,85.9) .. (177.1,85.9) .. controls (181.24,85.9) and (184.6,89.26) .. (184.6,93.4) .. controls (184.6,97.54) and (181.24,100.9) .. (177.1,100.9) .. controls (172.96,100.9) and (169.6,97.54) .. (169.6,93.4) -- cycle ;
            \t\\draw  [draw opacity=0][fill={rgb, 255:red, 217; green, 194; blue, 76 }  ,fill opacity=1 ] (116.65,75.41) .. controls (123.5,89.4) and (148.94,103.79) .. (152.1,50.4) .. controls (159.44,85.79) and (171.6,129.4) .. (135.6,176.9) .. controls (142.6,151.9) and (151.6,136.9) .. (144.6,122.4) .. controls (124.5,98.15) and (116.25,95.4) .. (116.65,75.41) -- cycle ;
            \t\\draw  [draw opacity=0][fill={rgb, 255:red, 186; green, 164; blue, 56 }  ,fill opacity=1 ] (172.1,164.4) .. controls (170.1,188.9) and (151.1,185.4) .. (131.6,192.9) .. controls (154.6,182.9) and (164.6,178.4) .. (172.1,164.4) -- cycle ;
            \t\\draw  [draw opacity=0][fill={rgb, 255:red, 113; green, 108; blue, 47 }  ,fill opacity=0.34 ] (168.6,116.9) .. controls (174.6,146.4) and (156.6,171.9) .. (133.6,183.9) .. controls (151.6,170.4) and (163.6,134.4) .. (168.6,116.9) -- cycle ;
            \t\\draw  [draw opacity=0][shading=_ksnmg3bfu,_voq84wsu2] (128.1,193.9) .. controls (151.6,190.9) and (166.6,188.9) .. (180.6,191.9) .. controls (184.2,197.3) and (181.6,194.4) .. (183.6,198.4) .. controls (168.1,196.9) and (153.6,197.4) .. (124.6,200.9) .. controls (127.1,196.9) and (126.6,198.4) .. (128.1,193.9) -- cycle ;
            \t\\draw  [draw opacity=0][shading=_p2gvjpsk6,_flmt02lqk] (120.6,209.4) .. controls (144.6,208.4) and (174.6,209.4) .. (189.1,208.4) .. controls (193.6,214.4) and (191.6,211.9) .. (193.6,215.9) .. controls (184.1,217.4) and (127.4,217.9) .. (117.9,215.9) .. controls (120.4,211.9) and (119.1,213.9) .. (120.6,209.4) -- cycle ;
            \t\\draw  [draw opacity=0][fill={rgb, 255:red, 113; green, 108; blue, 47 }  ,fill opacity=0.34 ] (129.44,106.07) .. controls (149.1,123.9) and (146.6,130.9) .. (144.6,142.4) .. controls (143.1,130.4) and (136.6,126.4) .. (129.44,106.07) -- cycle ;
            \t\\draw  [draw opacity=0][fill={rgb, 255:red, 113; green, 108; blue, 47 }  ,fill opacity=0.34 ] (134.6,137.4) .. controls (154.26,155.23) and (139.1,158.9) .. (137.1,170.4) .. controls (135.6,158.4) and (141.76,157.73) .. (134.6,137.4) -- cycle ;
            \t\\draw  [draw opacity=0][fill={rgb, 255:red, 113; green, 108; blue, 47 }  ,fill opacity=0.14 ] (156.6,96.4) .. controls (156.1,114.4) and (149.43,112.07) .. (133.1,102.4) .. controls (149.93,105.57) and (149.91,98.74) .. (156.6,96.4) -- cycle ;
            \t\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (116.67,231.11) -- (124.72,231.11) -- (124.72,254.67) -- (116.67,254.67) -- cycle ;
            \t\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (139.63,231.41) -- (147.68,231.41) -- (147.68,254.96) -- (139.63,254.96) -- cycle ;
            \t\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (153.35,231.11) -- (161.4,231.11) -- (161.4,254.67) -- (153.35,254.67) -- cycle ;
            \t\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (124.72,231.11) -- (136.91,230.81) -- (134.9,235.95) -- (120.84,236.48) -- cycle ;
            \t\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (121.14,241.17) -- (133.66,240.58) -- (131.28,245.35) -- (117.26,246.54) -- cycle ;
            \t\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (161.4,231.11) -- (173.59,230.81) -- (171.58,236.18) -- (157.52,236.48) -- cycle ;
            \t\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (156.92,241.17) -- (169.45,240.58) -- (167.06,245.35) -- (154.58,246.24) -- cycle ;
            \t\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (179.29,231.33) -- (187.01,230.59) -- (177.17,254.52) -- (170.01,254.29) -- cycle ;
            \t\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (179.29,231.33) -- (187.24,231.7) -- (197.3,254.96) -- (189.25,254.74) -- cycle ;
            \t\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (176.95,246.47) -- (192.83,246.02) -- (190.59,251.39) -- (176.5,251.16) -- cycle ;
            \t\\draw  [color={rgb, 255:red, 242; green, 238; blue, 146 }  ,draw opacity=1 ][fill={rgb, 255:red, 242; green, 238; blue, 146 }  ,fill opacity=1 ] (139.3,200.81) -- (142.45,200.81) -- (142.45,205.64) -- (139.3,205.64) -- cycle ;
            \t\\draw  [color={rgb, 255:red, 242; green, 238; blue, 146 }  ,draw opacity=1 ][fill={rgb, 255:red, 242; green, 238; blue, 146 }  ,fill opacity=1 ] (148.27,200.87) -- (151.42,200.87) -- (151.42,205.7) -- (148.27,205.7) -- cycle ;
            \t\\draw  [color={rgb, 255:red, 242; green, 238; blue, 146 }  ,draw opacity=1 ][fill={rgb, 255:red, 242; green, 238; blue, 146 }  ,fill opacity=1 ] (153.63,200.81) -- (156.77,200.81) -- (156.77,205.64) -- (153.63,205.64) -- cycle ;
            \t\\draw  [color={rgb, 255:red, 242; green, 238; blue, 146 }  ,draw opacity=1 ][fill={rgb, 255:red, 242; green, 238; blue, 146 }  ,fill opacity=1 ] (142.45,200.81) -- (147.21,200.75) -- (146.42,201.8) -- (140.93,201.91) -- cycle ;
            \t\\draw  [color={rgb, 255:red, 242; green, 238; blue, 146 }  ,draw opacity=1 ][fill={rgb, 255:red, 242; green, 238; blue, 146 }  ,fill opacity=1 ] (141.05,202.87) -- (145.94,202.75) -- (145.01,203.73) -- (139.53,203.97) -- cycle ;
            \t\\draw  [color={rgb, 255:red, 242; green, 238; blue, 146 }  ,draw opacity=1 ][fill={rgb, 255:red, 242; green, 238; blue, 146 }  ,fill opacity=1 ] (156.77,200.81) -- (161.54,200.75) -- (160.75,201.85) -- (155.26,201.91) -- cycle ;
            \t\\draw  [color={rgb, 255:red, 242; green, 238; blue, 146 }  ,draw opacity=1 ][fill={rgb, 255:red, 242; green, 238; blue, 146 }  ,fill opacity=1 ] (155.03,202.87) -- (159.92,202.75) -- (158.99,203.73) -- (154.11,203.91) -- cycle ;
            \t\\draw  [color={rgb, 255:red, 242; green, 238; blue, 146 }  ,draw opacity=1 ][fill={rgb, 255:red, 242; green, 238; blue, 146 }  ,fill opacity=1 ] (163.76,200.85) -- (166.78,200.7) -- (162.94,205.61) -- (160.14,205.56) -- cycle ;
            \t\\draw  [color={rgb, 255:red, 242; green, 238; blue, 146 }  ,draw opacity=1 ][fill={rgb, 255:red, 242; green, 238; blue, 146 }  ,fill opacity=1 ] (163.76,200.85) -- (166.87,200.93) -- (170.8,205.7) -- (167.65,205.65) -- cycle ;
            \t\\draw  [color={rgb, 255:red, 242; green, 238; blue, 146 }  ,draw opacity=1 ][fill={rgb, 255:red, 242; green, 238; blue, 146 }  ,fill opacity=1 ] (162.85,203.96) -- (169.05,203.87) -- (168.18,204.97) -- (162.67,204.92) -- cycle ;
            \\end{tikzpicture}''')

                # Câu hỏi
                noidungcauhoi = ('''\\immini{Một cơ sở sản xuất đồ lưu niệm chế tạo các mô hình cúp World Cup để bán cho người hâm mộ bóng đá. Qua khảo sát thị trường, người ta nhận thấy rằng nếu sản xuất và bán $x$ mô hình mỗi tháng ($0 < x < %s$) thì giá bán mỗi mô hình là $p(x) = %s - %s x$ (nghìn đồng/mô hình). Chi phí sản xuất $x$ mô hình mỗi tháng được cho bởi $C(x) = %s + %s x$ (nghìn đồng). Gọi $L(x)$ (nghìn đồng) là lợi nhuận thu được khi sản xuất và bán hết $x$ mô hình trong một tháng. Lợi nhuận lớn nhất đó bằng bao nhiêu triệu đồng?}{%s}'''
                % (latex(x_limit), latex(a), b_str, latex(c), latex(d), hinhve))

                # Gắn thẻ \True cho đáp án đúng và định dạng các phương án sai
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào danh sách và xáo trộn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Xây dựng bảng biến thiên bằng gói tkz-tab bên trong tikzpicture
                bang_bien_thien = ('''\\begin{center}
            \\begin{tikzpicture}
            \\tkzTabInit[lgt=1.5,espcl=3]{$x$ / 1, $L'(x)$ / 1, $L(x)$ / 2.5}{$0$, $%s$, $%s$}
            \\tkzTabLine{ , +, 0, -, }
            \\tkzTabVar{-/ , +/ $%s$, -/ }
            \\end{tikzpicture}
            \\end{center}''' % (latex(x_max), latex(x_limit), latex(max_profit_nghin)))

                # Nội dung lời giải
                loigiai = ('''Doanh thu: $R(x) = x \\cdot p(x) = x(%s - %s x) = %s x - %s x^2.$\\\\
            Lợi nhuận: $L(x) = R(x) - C(x)$\\\\
            $L(x) = %s x - %s x^2 - (%s + %s x)$\\\\
            $L(x) = -%s x^2 + %s x - %s.$\\\\
            Ta có:\\\\
            $L'(x) = -%s x + %s.$\\\\
            Cho $L'(x) = 0$ suy ra $-%s x + %s = 0 \\Leftrightarrow x = %s.$\\\\
            Ta có: $L(%s) = -%s(%s)^2 + %s \\cdot %s - %s = -%s + %s - %s = %s.$\\\\
            Bảng biến thiên:
            %s
            Dựa vào bảng biến thiên, ta thấy lợi nhuận đạt giá trị lớn nhất khi $x = %s$.\\\\
            Vậy lợi nhuận lớn nhất là $%s$ (nghìn đồng) $= %s$ triệu đồng.'''
                % (latex(a), b_str, latex(a), b_str,
                   latex(a), b_str, latex(c), latex(d),
                   b_str, latex(a_minus_d), latex(c),
                   two_b_str, latex(a_minus_d),
                   two_b_str, latex(a_minus_d), latex(x_max),
                   latex(x_max), b_str, latex(x_max), latex(a_minus_d), latex(x_max), latex(c),
                   latex(term1), latex(term2), latex(c), latex(max_profit_nghin),
                   bang_bien_thien,
                   latex(x_max),
                   latex(max_profit_nghin), latex(max_profit_trieu)))

                dapan='\\shortans[0]{$%s$}\n'%(latex(max_profit_trieu))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'+ dapan+
                       '\\loigiai{'+str(loigiai)+'}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content


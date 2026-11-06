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


def bt_dang67_p3_b2_c1_ds12(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)

    if dang=='1':
        # Các bộ số liệu (p0: Giá bán đầu, c: Giá nhập, q0: Số lượng đầu, dq: Tăng thêm mỗi 1tr giảm)
        # Các bộ số này được thiết kế để x_max luôn là số nguyên
        data = [
            (35, 25, 120, 20),
            (40, 28, 200, 25),
            (38, 26, 160, 20),
            (35, 25, 80, 20)
        ]
        p0, c, q0, dq = random.choice(data)

        # Tính toán
        # Hàm lợi nhuận: f(x) = (p0 - x - c)(q0 + dq*x) = (A - x)(q0 + dq*x)
        A = p0 - c

        # Rút gọn hàm bậc 2: f(x) = -dq*x^2 + (A*dq - q0)*x + A*q0
        a = -dq
        b = A * dq - q0
        c_val = A * q0

        # Đạo hàm: f'(x) = 2ax + b = 0 => x = -b/(2a)
        x_max = -b // (2 * a)
        max_profit = a * (x_max**2) + b * x_max + c_val

        kq = max_profit

        # Các đáp án trắc nghiệm
        du = ['$%s$ triệu đồng' % (kq)]
        da = random.choice(du)

        # Tạo các phương án sai (Nhiễu) - Đảm bảo không trùng với đáp án đúng
        s = [
            '$%s$ triệu đồng' % (kq + dq),
            '$%s$ triệu đồng' % (kq + 2*dq),
            '$%s$ triệu đồng' % (kq - dq),
            '$%s$ triệu đồng' % (kq - 2*dq),
            '$%s$ triệu đồng' % (kq + 15),
            '$%s$ triệu đồng' % (kq - 15),
            '$%s$ triệu đồng' % (c_val) # Phương án bẫy: lợi nhuận khi không giảm giá
        ]

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        # Câu hỏi
        noidungcauhoi = ('''\\immini{Một cửa hàng điện thoại di động nhập một lô hàng iPhone 18 Pro (màu Đỏ Burgundy) với giá $%s$ triệu đồng/chiếc. Hiện tại, cửa hàng đang bán với giá $%s$ triệu đồng/chiếc, với mức giá này mỗi tháng cửa hàng bán được $%s$ chiếc. Qua nghiên cứu thị trường, quản lý cửa hàng thấy rằng nếu cứ giảm giá bán đi $1$ triệu đồng/chiếc thì doanh số bán hàng hàng tháng sẽ tăng thêm $%s$ chiếc. Hỏi lợi nhuận lớn nhất trong tháng mà cửa hàng có thể đạt được từ việc bán dòng iPhone 18 Pro này là bao nhiêu? (Biết rằng các chi phí vận hành khác là không đổi).}
                         {\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
                         	\\tikzset {_ddr2vh0uk/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{-10.08 bp } { 0 bp }  }  \\pgftransformrotate{-48 }  \\pgftransformscale{2.52 }  }}}
                         	\\pgfdeclarehorizontalshading{_w8riifhnk}{150bp}{rgb(0bp)=(0.45,0.05,0.41);
                         		rgb(37.5bp)=(0.45,0.05,0.41);
                         		rgb(55.87499346051897bp)=(0.2,0.14,0.2);
                         		rgb(100bp)=(0.2,0.14,0.2)}
                         	\\tikzset {_w707st43p/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{0 }  \\pgftransformscale{2 }  }}}
                         	\\pgfdeclarehorizontalshading{_u6q4xkel7}{150bp}{rgb(0bp)=(0.31,0.16,0.31);
                         		rgb(37.5bp)=(0.31,0.16,0.31);
                         		rgb(62.5bp)=(0.2,0.14,0.2);
                         		rgb(100bp)=(0.2,0.14,0.2)}
                         	\\tikzset {_otogg9n7x/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{0 }  \\pgftransformscale{2 }  }}}
                         	\\pgfdeclarehorizontalshading{_1uhlx79qm}{150bp}{rgb(0bp)=(0.31,0.16,0.31);
                         		rgb(37.5bp)=(0.31,0.16,0.31);
                         		rgb(62.5bp)=(0.2,0.14,0.2);
                         		rgb(100bp)=(0.2,0.14,0.2)}
                         	\\tikzset {_kohc8uqh9/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{0 }  \\pgftransformscale{2 }  }}}
                         	\\pgfdeclarehorizontalshading{_oybpmecg8}{150bp}{rgb(0bp)=(0.31,0.16,0.31);
                         		rgb(37.5bp)=(0.31,0.16,0.31);
                         		rgb(62.5bp)=(0.2,0.14,0.2);
                         		rgb(100bp)=(0.2,0.14,0.2)}
                         	\\tikzset {_jftiu3yyy/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{0 }  \\pgftransformscale{2 }  }}}
                         	\\pgfdeclarehorizontalshading{_akkxvah79}{150bp}{rgb(0bp)=(0.31,0.16,0.31);
                         		rgb(37.5bp)=(0.31,0.16,0.31);
                         		rgb(62.5bp)=(0.2,0.14,0.2);
                         		rgb(100bp)=(0.2,0.14,0.2)}
                         	\\tikzset{every picture/.style={line width=0.75pt}} 
                         	\\path  [shading=_w8riifhnk,_ddr2vh0uk] (23.43,32.38) .. controls (23.43,22.6) and (31.36,14.67) .. (41.15,14.67) -- (94.28,14.67) .. controls (104.07,14.67) and (112,22.6) .. (112,32.38) -- (112,189.21) .. controls (112,199) and (104.07,206.93) .. (94.28,206.93) -- (41.15,206.93) .. controls (31.36,206.93) and (23.43,199) .. (23.43,189.21) -- cycle ; 
                         	\\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ] (23.43,32.38) .. controls (23.43,22.6) and (31.36,14.67) .. (41.15,14.67) -- (94.28,14.67) .. controls (104.07,14.67) and (112,22.6) .. (112,32.38) -- (112,189.21) .. controls (112,199) and (104.07,206.93) .. (94.28,206.93) -- (41.15,206.93) .. controls (31.36,206.93) and (23.43,199) .. (23.43,189.21) -- cycle ;  
                         	\\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.18 ][line width=0.75]  (25.19,33.08) .. controls (25.19,23.69) and (32.81,16.07) .. (42.2,16.07) -- (93.23,16.07) .. controls (102.62,16.07) and (110.24,23.69) .. (110.24,33.08) -- (110.24,188.51) .. controls (110.24,197.9) and (102.62,205.52) .. (93.23,205.52) -- (42.2,205.52) .. controls (32.81,205.52) and (25.19,197.9) .. (25.19,188.51) -- cycle ;
                         	\\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.08 ] (29.3,30.08) .. controls (29.3,24.85) and (33.54,20.61) .. (38.77,20.61) -- (96.66,20.61) .. controls (101.89,20.61) and (106.13,24.85) .. (106.13,30.08) -- (106.13,57.28) .. controls (106.13,62.51) and (101.89,66.75) .. (96.66,66.75) -- (38.77,66.75) .. controls (33.54,66.75) and (29.3,62.51) .. (29.3,57.28) -- cycle ;
                         	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.31 ] (31.06,31.21) .. controls (31.06,26.22) and (35.1,22.17) .. (40.09,22.17) -- (94.75,22.17) .. controls (99.74,22.17) and (103.79,26.22) .. (103.79,31.21) -- (103.79,57.13) .. controls (103.79,62.12) and (99.74,66.16) .. (94.75,66.16) -- (40.09,66.16) .. controls (35.1,66.16) and (31.06,62.12) .. (31.06,57.13) -- cycle ;
                         	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.2 ][fill={rgb, 255:red, 70; green, 10; blue, 82 }  ,fill opacity=1 ] (33.29,54.53) .. controls (33.29,49.47) and (37.39,45.36) .. (42.46,45.36) .. controls (47.52,45.36) and (51.63,49.47) .. (51.63,54.53) .. controls (51.63,59.59) and (47.52,63.7) .. (42.46,63.7) .. controls (37.39,63.7) and (33.29,59.59) .. (33.29,54.53) -- cycle ;
                         	\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (34.53,54.53) .. controls (34.53,50.15) and (38.08,46.61) .. (42.46,46.61) .. controls (46.83,46.61) and (50.38,50.15) .. (50.38,54.53) .. controls (50.38,58.91) and (46.83,62.45) .. (42.46,62.45) .. controls (38.08,62.45) and (34.53,58.91) .. (34.53,54.53) -- cycle ;
                         	\\draw  [draw opacity=0][fill={rgb, 255:red, 80; green, 227; blue, 194 }  ,fill opacity=0.17 ] (38.75,54.53) .. controls (38.75,52.48) and (40.41,50.83) .. (42.46,50.83) .. controls (44.5,50.83) and (46.16,52.48) .. (46.16,54.53) .. controls (46.16,56.58) and (44.5,58.23) .. (42.46,58.23) .. controls (40.41,58.23) and (38.75,56.58) .. (38.75,54.53) -- cycle ;
                         	\\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.67 ] (42.46,54.53) -- (39.01,52.84) -- (41.03,51.01) -- cycle ;
                         	\\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.67 ] (44.51,58.34) -- (42.46,54.53) -- (45.98,55.96) -- cycle ;
                         	\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (43.23,51.56) -- (42.46,54.53) ;
                         	\\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.12 ][fill={rgb, 255:red, 70; green, 10; blue, 82 }  ,fill opacity=1 ] (33.29,33.81) .. controls (33.29,28.74) and (37.39,24.64) .. (42.46,24.64) .. controls (47.52,24.64) and (51.63,28.74) .. (51.63,33.81) .. controls (51.63,38.87) and (47.52,42.98) .. (42.46,42.98) .. controls (37.39,42.98) and (33.29,38.87) .. (33.29,33.81) -- cycle ;
                         	\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (34.53,33.81) .. controls (34.53,29.43) and (38.08,25.88) .. (42.46,25.88) .. controls (46.83,25.88) and (50.38,29.43) .. (50.38,33.81) .. controls (50.38,38.18) and (46.83,41.73) .. (42.46,41.73) .. controls (38.08,41.73) and (34.53,38.18) .. (34.53,33.81) -- cycle ;
                         	\\draw  [draw opacity=0][fill={rgb, 255:red, 80; green, 227; blue, 194 }  ,fill opacity=0.17 ] (38.75,33.81) .. controls (38.75,31.76) and (40.41,30.1) .. (42.46,30.1) .. controls (44.5,30.1) and (46.16,31.76) .. (46.16,33.81) .. controls (46.16,35.85) and (44.5,37.51) .. (42.46,37.51) .. controls (40.41,37.51) and (38.75,35.85) .. (38.75,33.81) -- cycle ;
                         	\\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.67 ] (42.46,33.81) -- (39.01,32.12) -- (41.03,30.29) -- cycle ;
                         	\\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.67 ] (44.51,37.62) -- (42.46,33.81) -- (45.98,35.24) -- cycle ;
                         	\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (43.23,30.84) -- (42.46,33.81) ;
                         	\\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.14 ][fill={rgb, 255:red, 70; green, 10; blue, 82 }  ,fill opacity=1 ] (52.84,42.02) .. controls (52.84,36.95) and (56.94,32.85) .. (62.01,32.85) .. controls (67.07,32.85) and (71.18,36.95) .. (71.18,42.02) .. controls (71.18,47.08) and (67.07,51.19) .. (62.01,51.19) .. controls (56.94,51.19) and (52.84,47.08) .. (52.84,42.02) -- cycle ;
                         	\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (54.08,42.02) .. controls (54.08,37.64) and (57.63,34.1) .. (62.01,34.1) .. controls (66.38,34.1) and (69.93,37.64) .. (69.93,42.02) .. controls (69.93,46.39) and (66.38,49.94) .. (62.01,49.94) .. controls (57.63,49.94) and (54.08,46.39) .. (54.08,42.02) -- cycle ;
                         	\\draw  [draw opacity=0][fill={rgb, 255:red, 80; green, 227; blue, 194 }  ,fill opacity=0.17 ] (58.3,42.02) .. controls (58.3,39.97) and (59.96,38.31) .. (62.01,38.31) .. controls (64.05,38.31) and (65.71,39.97) .. (65.71,42.02) .. controls (65.71,44.06) and (64.05,45.72) .. (62.01,45.72) .. controls (59.96,45.72) and (58.3,44.06) .. (58.3,42.02) -- cycle ;
                         	\\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.67 ] (62.01,42.02) -- (58.56,40.33) -- (60.58,38.5) -- cycle ;
                         	\\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.67 ] (64.06,45.83) -- (62.01,42.02) -- (65.53,43.45) -- cycle ;
                         	\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (62.78,39.05) -- (62.01,42.02) ;
                         	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.22 ] (29.34,79.57) .. controls (29.34,74.61) and (33.36,70.58) .. (38.33,70.58) -- (97.37,70.58) .. controls (102.34,70.58) and (106.37,74.61) .. (106.37,79.57) -- (106.37,193.83) .. controls (106.37,198.79) and (102.34,202.82) .. (97.37,202.82) -- (38.33,202.82) .. controls (33.36,202.82) and (29.34,198.79) .. (29.34,193.83) -- cycle ;
                         	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.09 ] (68.48,122.41) .. controls (73.93,121.3) and (72.47,122.17) .. (77.16,123.35) .. controls (72.47,125.69) and (71.99,129.43) .. (76.86,133.91) .. controls (76.86,136.59) and (74.37,138.75) .. (71.47,140.36) .. controls (70.2,140.77) and (67.95,137.72) .. (64.72,138.89) .. controls (60.33,145.34) and (50.18,115.72) .. (68.48,122.41) -- cycle ;
                         	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.1 ] (72.03,118.12) .. controls (71.19,119.45) and (69.87,120.3) .. (68.44,120.58) .. controls (68.03,119.12) and (68.21,117.51) .. (69.08,116.13) .. controls (69.91,114.8) and (71.23,113.96) .. (72.66,113.68) .. controls (73.08,115.13) and (72.9,116.74) .. (72.03,118.12) -- cycle ;
                         	\\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=0.16 ][fill={rgb, 255:red, 52; green, 35; blue, 52 }  ,fill opacity=1 ] (81.3,32.86) .. controls (81.3,23.07) and (89.23,15.14) .. (99.02,15.14) -- (152.15,15.14) .. controls (161.94,15.14) and (169.87,23.07) .. (169.87,32.86) -- (169.87,189.69) .. controls (169.87,199.47) and (161.94,207.4) .. (152.15,207.4) -- (99.02,207.4) .. controls (89.23,207.4) and (81.3,199.47) .. (81.3,189.69) -- cycle ;
                         	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1.5]  (83.65,34.03) .. controls (83.65,24.83) and (91.11,17.37) .. (100.31,17.37) -- (150.28,17.37) .. controls (159.48,17.37) and (166.93,24.83) .. (166.93,34.03) -- (166.93,187.81) .. controls (166.93,197.01) and (159.48,204.47) .. (150.28,204.47) -- (100.31,204.47) .. controls (91.11,204.47) and (83.65,197.01) .. (83.65,187.81) -- cycle ;
                         	\\draw  [draw opacity=0][shading=_u6q4xkel7,_w707st43p] (120.01,25) -- (159.31,34.38) -- (90.69,71.33) -- (88.34,51.98) -- cycle ;
                         	\\draw  [draw opacity=0][shading=_1uhlx79qm,_otogg9n7x] (91.86,83.06) -- (91.27,103.59) -- (159.31,88.34) -- (134.68,54.91) -- cycle ;
                         	\\draw  [draw opacity=0][shading=_oybpmecg8,_kohc8uqh9] (90.1,120.01) -- (89.51,140.54) -- (162.83,155.79) -- (137.02,100.07) -- cycle ;
                         	\\draw  [draw opacity=0][shading=_akkxvah79,_jftiu3yyy] (91.86,154.03) -- (90.69,190.39) -- (144.06,196.26) -- (158.72,175.15) -- cycle ;
                         	\\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (117.37,27.64) .. controls (117.37,26.18) and (118.56,25) .. (120.01,25) -- (131.27,25) .. controls (132.73,25) and (133.91,26.18) .. (133.91,27.64) -- (133.91,27.64) .. controls (133.91,29.09) and (132.73,30.28) .. (131.27,30.28) -- (120.01,30.28) .. controls (118.56,30.28) and (117.37,29.09) .. (117.37,27.64) -- cycle ;
                         	\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.22 ]   (91.27,69.28) -- (131.16,49.04) ;
                         	\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.22 ]   (91.27,69.28) -- (91.86,52.56) ;
                         	\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.22 ]   (91.27,103.59) -- (140.54,92.45) ;
                         	\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.22 ]   (92.45,140.25) -- (145.23,151.68) ;
                         	\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.22 ]   (90.69,190.39) -- (128.81,195.67) ;
                         	\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.22 ]   (90.69,190.39) -- (91.27,162.24) ;
                         \\end{tikzpicture}}'''
                         %(latex(c), latex(p0), latex(q0), latex(dq)))

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2) 
        da_s3 = str(das3) 

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải
        loigiai = ('''Gọi $x$ (triệu đồng) là số tiền giảm giá cho mỗi chiếc điện thoại ($0 \\le x \\le %s$).\\\\
        Khi đó, giá bán mỗi chiếc điện thoại là: $%s - x$ (triệu đồng).\\\\
        Lợi nhuận thu được khi bán mỗi chiếc điện thoại là: $(%s - x) - %s = %s - x$ (triệu đồng).\\\\
        Số lượng điện thoại bán được trong tháng là: $%s + %s x$ (chiếc).\\\\
        Hàm lợi nhuận trong tháng là:
        $$f(x) = (%s - x)(%s + %s x) = -%s x^2 + %s x + %s$$
        Xét hàm số $f(x) = -%s x^2 + %s x + %s$ trên đoạn $[0; %s]$.\\\\
        Ta có $f'(x) = -%s x + %s$.\\\\
        Cho $f'(x) = 0 \\Leftrightarrow -%s x + %s = 0 \\Leftrightarrow x = %s$.\\\\
        Bảng biến thiên:
        \\begin{center}
        \\begin{tikzpicture}
        \\tkzTabInit[lgt=1.5,espcl=3]{$x$/1,$f'(x)$/1,$f(x)$/2}{$0$,$%s$,$%s$}
        \\tkzTabLine{,+,$0$,-,}
        \\tkzTabVar{-/ $%s$, +/ $%s$, -/ $0$}
        \\end{tikzpicture}
        \\end{center}
        Từ bảng biến thiên, ta thấy hàm số đạt giá trị lớn nhất tại $x = %s$ với $\\max f(x) = f(%s) = %s$.\\\\
        Vậy lợi nhuận lớn nhất trong tháng cửa hàng có thể đạt được là $%s$ triệu đồng (tương ứng với việc bán mỗi chiếc với giá $%s$ triệu đồng).'''

        % (latex(A), latex(p0), latex(p0), latex(c), latex(A), latex(q0), latex(dq), 
           latex(A), latex(q0), latex(dq), latex(-a), latex(b), latex(c_val), 
           latex(-a), latex(b), latex(c_val), latex(A), 
           latex(-2*a), latex(b), latex(-2*a), latex(b), latex(x_max), 
           latex(x_max), latex(A), latex(c_val), latex(max_profit), 
           latex(x_max), latex(x_max), latex(max_profit), latex(max_profit), latex(p0 - x_max)))
        dapan='\\shortans[0]{$%s$}\n'%(latex(max_profit))

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
        '\\loigiai{\n'+str(loigiai)+'\n}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content


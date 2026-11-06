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


def bt_dang35_p3_b3_c4_ds11(self):
            # Khai báo biến
            # Khai báo biến (Random các thông số đầu vào)
            T0 = random.randint(15, 30)          # Nhiệt độ ban đầu
            v1 = random.randint(3, 8)            # Tốc độ tăng
            t1 = random.choice([40, 50, 60, 70]) # Thời gian tăng
            v2 = random.randint(2, 5)            # Tốc độ giảm
            t2 = random.choice([30, 40, 50, 60]) # Thời gian giảm

            # Tính toán các giá trị
            ttotal = t1 + t2
            Tmid = T0 + v1 * t1                  # Nhiệt độ đạt đỉnh tại thời điểm t1
            a = Tmid + v2 * t1                   # Giá trị của a

            # Các đáp án trắc nghiệm
            du = ['$%s$' % a]
            da = random.choice(du)

            # Tạo các đáp án nhiễu sai khác logic
            s_list = [
                '$%s$' % (a + 10),
                '$%s$' % (a - 10),
                '$%s$' % (Tmid - v2 * t1),       # Sai dấu giới hạn
                '$%s$' % (Tmid + v2 * ttotal),   # Nhầm t1 với tổng thời gian
                '$%s$' % (a + 20),
                '$%s$' % (a - 20)
            ]

            # Lọc trùng lặp giữa các phương án và chọn 3 phương án ngẫu nhiên
            s_list = list(set(s_list) - set(du))
            random.shuffle(s_list)

            das1 = s_list[0]
            das2 = s_list[1]
            das3 = s_list[2]

            # Vẽ hình mô phỏng đèn cồn và ống nghiệm bằng TikZ
            tikz_pic = r'''\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\draw  [fill={rgb, 255:red, 139; green, 87; blue, 42 }  ,fill opacity=1 ] (260.3,43.6) -- (308.8,136.6) -- (291.3,145.1) -- (251.3,49.6) -- cycle ;
            	\draw    (260.3,43.6) -- (279.3,95.1) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 213; green, 234; blue, 234 }  ,fill opacity=1 ] (278.08,78.55) -- (197.23,138.57) .. controls (190.78,143.36) and (182.47,143.09) .. (178.66,137.96) .. controls (174.86,132.84) and (177,124.8) .. (183.45,120.01) -- (264.3,59.99) .. controls (270.75,55.2) and (279.06,55.48) .. (282.87,60.6) .. controls (286.67,65.72) and (284.53,73.76) .. (278.08,78.55) .. controls (271.63,83.33) and (263.32,83.06) .. (259.52,77.94) .. controls (255.71,72.81) and (257.86,64.78) .. (264.3,59.99) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 213; green, 234; blue, 234 }  ,fill opacity=1 ] (276.22,51.57) -- (289.61,69.75) -- (249.56,99.26) -- (236.17,81.08) -- cycle ;
            	\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.57 ][fill={rgb, 255:red, 174; green, 203; blue, 203 }  ,fill opacity=1 ] (276.22,51.57) .. controls (278.12,50.17) and (282.66,53.11) .. (286.36,58.13) .. controls (290.05,63.15) and (291.51,68.35) .. (289.61,69.75) .. controls (287.71,71.15) and (283.17,68.22) .. (279.47,63.2) .. controls (275.77,58.18) and (274.32,52.97) .. (276.22,51.57) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 191; green, 132; blue, 203 }  ,fill opacity=1 ] (232.22,111.68) -- (196.42,138.26) .. controls (190.18,142.89) and (182.13,142.63) .. (178.45,137.67) .. controls (174.76,132.71) and (176.84,124.92) .. (183.08,120.29) -- (218.88,93.71) .. controls (225.12,89.08) and (233.17,89.34) .. (236.85,94.31) .. controls (240.54,99.27) and (238.46,107.05) .. (232.22,111.68) .. controls (225.97,116.32) and (217.93,116.05) .. (214.24,111.09) .. controls (210.56,106.13) and (212.63,98.35) .. (218.88,93.71) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 191; green, 132; blue, 203 }  ,fill opacity=1 ] (260.28,91.73) -- (225.77,116.54) -- (214.19,97.27) -- (226.75,88.02) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.35 ] (275.24,55.56) -- (276.41,59.67) -- (176.99,131.67) -- (178.23,127.03) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.09 ] (281.35,68.14) -- (285.37,70.15) -- (188.96,141.17) -- (184.21,140.63) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 45; green, 87; blue, 138 }  ,fill opacity=1 ] (203.07,205.73) -- (185.29,235.26) -- (151.96,235.04) -- (134.58,205.28) -- cycle ;
            	\draw [line width=2.25]    (170.4,158.73) .. controls (172.4,193.73) and (160.07,202.4) .. (165.67,212.23) .. controls (171.27,222.07) and (179.77,226.07) .. (183.67,229.73) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 142; green, 210; blue, 235 }  ,fill opacity=1 ] (188.33,237.78) -- (186.2,234.14) -- (151.25,233.9) -- (149.08,237.52) -- cycle ;
            	\draw [color={rgb, 255:red, 142; green, 210; blue, 235 }  ,draw opacity=1 ][line width=2.25]    (158.73,177.07) .. controls (163.07,194.4) and (128.07,192.73) .. (133.07,206.4) .. controls (142.07,219.4) and (148.5,230.6) .. (152.4,235.07) ;
            	\draw [color={rgb, 255:red, 142; green, 210; blue, 235 }  ,draw opacity=1 ][line width=2.25]    (180.02,175.85) .. controls (175.84,193.18) and (209.65,191.51) .. (204.82,205.18) .. controls (196.12,218.18) and (188.17,231.26) .. (184.4,235.73) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 133; green, 228; blue, 207 }  ,fill opacity=0.31 ] (159.15,178.85) .. controls (164.88,175.98) and (168.1,178.73) .. (178.1,176.4) .. controls (178.1,185.07) and (182.71,187.07) .. (186.15,189.51) .. controls (199.15,196.85) and (208.13,204.02) .. (204.82,205.18) .. controls (193.15,226.51) and (193.48,221.18) .. (185.71,237.04) .. controls (183.11,237.28) and (178.34,237.15) .. (172.36,236.75) .. controls (166.31,236.35) and (159.03,235.68) .. (151.48,234.85) .. controls (142.73,221.71) and (137.15,214.85) .. (132.82,205.51) .. controls (133.24,199.25) and (146.8,193.4) .. (155.48,189.51) .. controls (159.94,185.81) and (159.15,182.18) .. (159.15,178.85) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.44 ] (159.15,178.85) .. controls (164.88,175.98) and (158.3,181.98) .. (168.3,179.65) .. controls (168.3,188.32) and (163.61,187.21) .. (167.05,189.65) .. controls (160.3,195.9) and (154.3,200.15) .. (150.8,206.65) .. controls (154.3,218.4) and (157.8,222.4) .. (164.05,233.9) .. controls (161.45,234.13) and (166.53,234.29) .. (160.55,233.9) .. controls (154.5,233.5) and (160.34,234.24) .. (152.8,233.4) .. controls (144.8,221.4) and (140.05,214.65) .. (134.58,205.28) .. controls (135,199.01) and (146.57,192.46) .. (155.25,188.57) .. controls (159.71,184.86) and (159.15,182.18) .. (159.15,178.85) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (157.25,171.99) .. controls (157.25,171.11) and (157.96,170.4) .. (158.84,170.4) -- (180.01,170.4) .. controls (180.89,170.4) and (181.6,171.11) .. (181.6,171.99) -- (181.6,178.35) .. controls (181.6,178.35) and (181.6,178.35) .. (181.6,178.35) -- (157.25,178.35) .. controls (157.25,178.35) and (157.25,178.35) .. (157.25,178.35) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (129.15,237.4) -- (206.55,237.4) -- (206.55,240.6) -- (129.15,240.6) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 94; blue, 35 }  ,fill opacity=1 ] (169.4,113.48) .. controls (183.9,124.23) and (185.65,156.23) .. (170.4,158.73) .. controls (159.88,156.16) and (155.29,147.35) .. (157.4,139.48) .. controls (159.6,131.27) and (168.76,123.83) .. (169.4,113.48) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (170.7,130.4) .. controls (180.45,146.15) and (177.2,152.15) .. (170.4,158.73) .. controls (165.7,154.15) and (163.2,153.4) .. (162.7,146.65) .. controls (164.9,138.43) and (167.7,136.15) .. (170.7,130.4) -- cycle ;
            	\draw  [fill={rgb, 255:red, 139; green, 87; blue, 42 }  ,fill opacity=1 ] (243.3,44.6) -- (301.3,140.6) -- (291.3,145.1) -- (234.3,50.6) -- cycle ;
            	\draw  [fill={rgb, 255:red, 139; green, 87; blue, 42 }  ,fill opacity=1 ] (251.3,49.6) -- (271.3,82.1) -- (301.3,140.6) -- (243.3,44.6) -- cycle ;
            	\draw    (308.8,136.6) -- (279.3,95.1) ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (276.29,96.56) .. controls (274.95,93.81) and (275.21,90.92) .. (276.87,90.11) .. controls (278.54,89.3) and (280.97,90.88) .. (282.31,93.64) .. controls (283.65,96.39) and (283.39,99.28) .. (281.73,100.09) .. controls (280.06,100.9) and (277.63,99.32) .. (276.29,96.56) -- cycle ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.53 ]   (160.6,172.5) -- (181.6,171.99) ;
            \end{tikzpicture}'''

            # Câu hỏi
            noidungcauhoi = (r'''\immini{Khi nung nóng một vật với nhiệt độ tăng từ $%s^\circ\mathrm{C}$, mỗi phút tăng $%s^\circ\mathrm{C}$ trong $%s$ phút, sau đó giảm mỗi phút $%s^\circ\mathrm{C}$ trong $%s$ phút. Hàm số biểu thị nhiệt độ ($^\circ\mathrm{C}$) trong tủ theo thời gian $t$ (phút) có dạng:
            \[ T(t) = \begin{cases} %s + %st & \text{khi } 0 \le t \le %s \\ a - %st & \text{khi } %s < t \le %s \end{cases} \]
            Biết rằng quá trình tăng giảm nhiệt độ diễn ra liên tục. Khi đó giá trị của $a$ bằng bao nhiêu?}
            {%s}''' % (T0, v1, t1, v2, t2, T0, v1, t1, v2, t1, ttotal, tikz_pic))

            # Các đáp án
            da_d = ('\\True ' + str(da))
            da_s1 = str(das1)
            da_s2 = str(das2)
            da_s3 = str(das3)

            # Đưa các đáp án vào danh sách chọn ngẫu nhiên
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Nội dung lời giải
            loigiai = ('''Do quá trình tăng giảm nhiệt độ diễn ra liên tục nên hàm $T(t) = \\begin{cases} %s + %st & \\text{khi } 0 \\le t \\le %s \\\\ a - %st & \\text{khi } %s < t \\le %s \\end{cases}$ là hàm liên tục trên tập xác định. \\\\  Suy ra hàm số liên tục tại $t_0 = %s \\Rightarrow \\lim\\limits_{t \\to %s} T(t) = T(%s)$.\\\\
            Ta có: $\\lim\\limits_{t \\to %s^+} T(t) = \\lim\\limits_{t \\to %s^+} (a - %st) = a - %s$ và $\\lim\\limits_{t \\to %s^-} T(t) = \\lim\\limits_{t \\to %s^-} (%s + %st) = %s + %s = %s$.\\\\
            $\\Leftrightarrow T(%s) = %s$ nên ta có $a - %s = %s \\Rightarrow a = %s$.'''
            % (T0, v1, t1, v2, t1, ttotal, 
               t1, t1, t1, 
               t1, t1, v2, v2 * t1, 
               t1, t1, T0, v1, T0, v1 * t1, Tmid, 
               t1, Tmid, v2 * t1, Tmid, a))
            dapan='\\shortans[0]{$%s$}\n'%(a)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content 


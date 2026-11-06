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


def bt_dang37_p3_b2_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Khởi tạo ngẫu nhiên thời gian T dừng/chạm cầu (chọn số chia hết cho 5 để số đẹp)
                T_val = random.choice([12, 15, 18, 21, 24])

                # Chọn vận tốc ban đầu v0 và vận tốc tại cầu vT sao cho phù hợp thực tế
                v0 = 35
                vT = 10

                # Tính toán các hệ số theo bài toán gốc:
                # b = v0
                # a * T^2 = v0 - vT => a = (v0 - vT) / T^2
                b = v0
                diff_v = v0 - vT # 35 - 10 = 25
                a = Rational(diff_v, T_val**2)

                # Quãng đường tổng S(T) = -1/3 * a * T^3 + v0 * T
                S_total = Rational(-1, 3) * a * T_val**3 + v0 * T_val
                S_total = int(S_total) # S_total luôn là số nguyên với các bộ số chọn trước

                # Chọn một thời gian t1 ngẫu nhiên nguyên dương nhỏ hơn T để làm câu hỏi quãng đường
                # Để t1 là số nguyên đẹp cho phương trình bậc 3: t^3 - 3*v0/a * t + 3*S_t1/a = 0
                # Ta chọn trước t1 ngẫu nhiên từ 5 đến T-3, sau đó tính ngược ra S_t1 tương ứng
                t1_val = random.choice([6, 9, 12])
                while t1_val >= T_val:
                    t1_val = random.choice([3, 6, 9])

                # Tính quãng đường S_t1 đi được tại thời điểm t1
                S_t1 = Rational(-1, 3) * a * t1_val**3 + b * t1_val
                S_t1_int = int(S_t1)

                # Tính độ lớn gia tốc tại t1: |a(t1)| = |-2 * a * t1| = 2 * a * t1
                gia_toc_t1 = Rational(2 * diff_v * t1_val, T_val**2)

                # Định dạng kết quả hiển thị dấu phẩy thập phân nếu không nguyên
                if gia_toc_t1.q == 1:
                    kq_chinh_xac = str(gia_toc_t1.p)
                    kq4 = int(gia_toc_t1)
                else:
                    val_float = float(gia_toc_t1)
                    kq_chinh_xac = str(round(val_float, 2)).replace('.', ',')
                    kq4 = round(val_float, 1)

                # Đáp án đúng
                da = '$%s$' % (kq_chinh_xac)

                # Các đáp án sai chạy nhiễu xung quanh đáp án đúng
                s = [
                    '$%s$' % (latex(round(kq4 + 1.2, 1))).replace('.', ','),
                    '$%s$' % (latex(round(kq4 + 2.5, 1))).replace('.', ','),
                    '$%s$' % (latex(round(kq4 + 3.1, 1))).replace('.', ','),
                    '$%s$' % (latex(round(max(0.2, kq4 - 0.8), 1))).replace('.', ','),
                    '$%s$' % (latex(round(max(0.5, kq4 - 1.5), 1))).replace('.', ','),
                    '$%s$' % (latex(round(max(0.1, kq4 - 2.3), 1))).replace('.', ','),
                ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                hinhve=r'''\begin{center}
            	\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            		\draw  [draw opacity=0][fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (13.84,163.59) -- (336.71,163.59) -- (336.71,169.13) -- (13.84,169.13) -- cycle ;
            		\draw  [color={rgb, 255:red, 95; green, 57; blue, 25 }  ,draw opacity=1 ][line width=5.25]  (549.18,168.25) .. controls (472.69,88.98) and (396.2,88.98) .. (319.7,168.25) ;
            		\draw [color={rgb, 255:red, 95; green, 57; blue, 25 }  ,draw opacity=1 ][line width=3]    (434.44,108.8) -- (434.44,165.34) ;
            		\draw [color={rgb, 255:red, 95; green, 57; blue, 25 }  ,draw opacity=1 ][line width=3]    (381.91,121.52) -- (381.91,164.87) ;
            		\draw [color={rgb, 255:red, 95; green, 57; blue, 25 }  ,draw opacity=1 ][line width=3]    (489.24,122.94) -- (489.24,165.34) ;
            		\draw [color={rgb, 255:red, 95; green, 57; blue, 25 }  ,draw opacity=1 ][line width=3]    (408.18,113.04) -- (408.18,166.76) ;
            		\draw [color={rgb, 255:red, 95; green, 57; blue, 25 }  ,draw opacity=1 ][line width=3]    (462.52,112.1) -- (462.52,166.29) ;
            		\draw [color={rgb, 255:red, 95; green, 57; blue, 25 }  ,draw opacity=1 ][line width=3]    (354.74,136.6) -- (354.74,164.87) ;
            		\draw [color={rgb, 255:red, 95; green, 57; blue, 25 }  ,draw opacity=1 ][line width=3]    (517.32,138.01) -- (517.32,166.29) ;
            		\draw [color={rgb, 255:red, 95; green, 57; blue, 25 }  ,draw opacity=1 ][line width=3]    (434.44,108.8) -- (408.18,166.76) ;
            		\draw [color={rgb, 255:red, 95; green, 57; blue, 25 }  ,draw opacity=1 ][line width=3]    (408.18,113.04) -- (381.91,164.87) ;
            		\draw [color={rgb, 255:red, 95; green, 57; blue, 25 }  ,draw opacity=1 ][line width=3]    (381.91,121.52) -- (354.74,164.87) ;
            		\draw [color={rgb, 255:red, 95; green, 57; blue, 25 }  ,draw opacity=1 ][line width=3]    (434.44,108.8) -- (462.52,166.29) ;
            		\draw [color={rgb, 255:red, 95; green, 57; blue, 25 }  ,draw opacity=1 ][line width=3]    (462.52,112.1) -- (489.24,165.34) ;
            		\draw [color={rgb, 255:red, 95; green, 57; blue, 25 }  ,draw opacity=1 ][line width=3]    (489.24,122.94) -- (517.32,166.29) ;
            		\draw  [color={rgb, 255:red, 95; green, 57; blue, 25 }  ,draw opacity=1 ][fill={rgb, 255:red, 139; green, 87; blue, 42 }  ,fill opacity=1 ] (316.53,163.15) -- (552.35,163.15) -- (552.35,171) -- (316.53,171) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (570.26,163.72) -- (640.79,163.72) -- (640.79,168.36) -- (570.26,168.36) -- cycle ;
            		\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (259.72,160.64) .. controls (259.72,157.89) and (261.87,155.67) .. (264.53,155.67) .. controls (267.19,155.67) and (269.35,157.89) .. (269.35,160.64) .. controls (269.35,163.38) and (267.19,165.61) .. (264.53,165.61) .. controls (261.87,165.61) and (259.72,163.38) .. (259.72,160.64) -- cycle ;
            		\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (269.35,160.64) .. controls (269.35,157.89) and (271.5,155.67) .. (274.16,155.67) .. controls (276.82,155.67) and (278.97,157.89) .. (278.97,160.64) .. controls (278.97,163.38) and (276.82,165.61) .. (274.16,165.61) .. controls (271.5,165.61) and (269.35,163.38) .. (269.35,160.64) -- cycle ;
            		\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (261.7,160.64) .. controls (261.7,159.02) and (262.97,157.71) .. (264.53,157.71) .. controls (266.1,157.71) and (267.37,159.02) .. (267.37,160.64) .. controls (267.37,162.26) and (266.1,163.57) .. (264.53,163.57) .. controls (262.97,163.57) and (261.7,162.26) .. (261.7,160.64) -- cycle ;
            		\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (271.32,160.64) .. controls (271.32,159.02) and (272.59,157.71) .. (274.16,157.71) .. controls (275.72,157.71) and (276.99,159.02) .. (276.99,160.64) .. controls (276.99,162.26) and (275.72,163.57) .. (274.16,163.57) .. controls (272.59,163.57) and (271.32,162.26) .. (271.32,160.64) -- cycle ;
            		\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (186.71,158.1) -- (249.39,158.1) -- (249.39,162.61) -- (186.71,162.61) -- cycle ;
            		\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (181.9,160.36) .. controls (181.9,157.61) and (184.05,155.39) .. (186.71,155.39) .. controls (189.37,155.39) and (191.52,157.61) .. (191.52,160.36) .. controls (191.52,163.1) and (189.37,165.33) .. (186.71,165.33) .. controls (184.05,165.33) and (181.9,163.1) .. (181.9,160.36) -- cycle ;
            		\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (191.52,160.36) .. controls (191.52,157.61) and (193.68,155.39) .. (196.34,155.39) .. controls (199,155.39) and (201.15,157.61) .. (201.15,160.36) .. controls (201.15,163.1) and (199,165.33) .. (196.34,165.33) .. controls (193.68,165.33) and (191.52,163.1) .. (191.52,160.36) -- cycle ;
            		\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (243.66,160.36) .. controls (243.66,157.61) and (245.82,155.39) .. (248.48,155.39) .. controls (251.13,155.39) and (253.29,157.61) .. (253.29,160.36) .. controls (253.29,163.1) and (251.13,165.33) .. (248.48,165.33) .. controls (245.82,165.33) and (243.66,163.1) .. (243.66,160.36) -- cycle ;
            		\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (234.03,160.36) .. controls (234.03,157.61) and (236.19,155.39) .. (238.85,155.39) .. controls (241.51,155.39) and (243.66,157.61) .. (243.66,160.36) .. controls (243.66,163.1) and (241.51,165.33) .. (238.85,165.33) .. controls (236.19,165.33) and (234.03,163.1) .. (234.03,160.36) -- cycle ;
            		\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (201.15,160.36) .. controls (201.15,157.61) and (203.31,155.39) .. (205.96,155.39) .. controls (208.62,155.39) and (210.78,157.61) .. (210.78,160.36) .. controls (210.78,163.1) and (208.62,165.33) .. (205.96,165.33) .. controls (203.31,165.33) and (201.15,163.1) .. (201.15,160.36) -- cycle ;
            		\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (224.41,160.36) .. controls (224.41,157.61) and (226.56,155.39) .. (229.22,155.39) .. controls (231.88,155.39) and (234.03,157.61) .. (234.03,160.36) .. controls (234.03,163.1) and (231.88,165.33) .. (229.22,165.33) .. controls (226.56,165.33) and (224.41,163.1) .. (224.41,160.36) -- cycle ;
            		\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (183.87,160.36) .. controls (183.87,158.74) and (185.14,157.43) .. (186.71,157.43) .. controls (188.28,157.43) and (189.54,158.74) .. (189.54,160.36) .. controls (189.54,161.97) and (188.28,163.28) .. (186.71,163.28) .. controls (185.14,163.28) and (183.87,161.97) .. (183.87,160.36) -- cycle ;
            		\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (193.5,160.36) .. controls (193.5,158.74) and (194.77,157.43) .. (196.34,157.43) .. controls (197.9,157.43) and (199.17,158.74) .. (199.17,160.36) .. controls (199.17,161.97) and (197.9,163.28) .. (196.34,163.28) .. controls (194.77,163.28) and (193.5,161.97) .. (193.5,160.36) -- cycle ;
            		\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (203.13,160.36) .. controls (203.13,158.74) and (204.4,157.43) .. (205.96,157.43) .. controls (207.53,157.43) and (208.8,158.74) .. (208.8,160.36) .. controls (208.8,161.97) and (207.53,163.28) .. (205.96,163.28) .. controls (204.4,163.28) and (203.13,161.97) .. (203.13,160.36) -- cycle ;
            		\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (226.38,160.36) .. controls (226.38,158.74) and (227.65,157.43) .. (229.22,157.43) .. controls (230.79,157.43) and (232.05,158.74) .. (232.05,160.36) .. controls (232.05,161.97) and (230.79,163.28) .. (229.22,163.28) .. controls (227.65,163.28) and (226.38,161.97) .. (226.38,160.36) -- cycle ;
            		\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (236.01,160.36) .. controls (236.01,158.74) and (237.28,157.43) .. (238.85,157.43) .. controls (240.41,157.43) and (241.68,158.74) .. (241.68,160.36) .. controls (241.68,161.97) and (240.41,163.28) .. (238.85,163.28) .. controls (237.28,163.28) and (236.01,161.97) .. (236.01,160.36) -- cycle ;
            		\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (245.64,160.36) .. controls (245.64,158.74) and (246.91,157.43) .. (248.48,157.43) .. controls (250.04,157.43) and (251.31,158.74) .. (251.31,160.36) .. controls (251.31,161.97) and (250.04,163.28) .. (248.48,163.28) .. controls (246.91,163.28) and (245.64,161.97) .. (245.64,160.36) -- cycle ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 50; green, 112; blue, 186 }  ,fill opacity=1 ] (177.57,143.79) .. controls (177.57,141.48) and (179.44,139.61) .. (181.75,139.61) -- (252.83,139.61) .. controls (255.13,139.61) and (257.01,141.48) .. (257.01,143.79) -- (257.01,160.51) .. controls (257.01,160.51) and (257.01,160.51) .. (257.01,160.51) -- (177.57,160.51) .. controls (177.57,160.51) and (177.57,160.51) .. (177.57,160.51) -- cycle ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (177.79,157.68) -- (256.85,157.4) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (177.79,155.14) -- (256.85,154.86) ;
            		\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.75 ] (181.54,143.84) -- (195.98,143.84) -- (195.98,152.26) -- (181.54,152.26) -- cycle ;
            		\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.75 ] (198.03,143.84) -- (212.48,143.84) -- (212.48,152.26) -- (198.03,152.26) -- cycle ;
            		\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.75 ] (214.53,143.84) -- (228.97,143.84) -- (228.97,152.26) -- (214.53,152.26) -- cycle ;
            		\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.75 ] (230.75,143.84) -- (245.19,143.84) -- (245.19,152.26) -- (230.75,152.26) -- cycle ;
            		\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.75 ] (247.24,143.84) -- (253.7,143.84) -- (253.7,152.26) -- (247.24,152.26) -- cycle ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (179.16,141.58) -- (265.74,141.58) ;
            		\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (175.82,143.56) -- (177.57,143.56) -- (177.57,160.51) -- (175.82,160.51) -- cycle ;
            		\draw  [fill={rgb, 255:red, 50; green, 112; blue, 186 }  ,fill opacity=1 ] (269.02,139.75) -- (281.87,154.72) -- (281.87,160.93) -- (257.01,160.51) -- (257.01,143.79) -- (254.52,139.47) -- cycle ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (256.85,154.86) -- (266.01,154.72) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (256.85,157.4) -- (266.01,157.26) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (266.01,154.72) -- (271.21,158.39) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (271.21,158.39) -- (281.87,158.67) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (266.01,157.26) -- (269.44,160.72) ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 74; green, 144; blue, 226 }  ,fill opacity=1 ] (271.75,143.14) -- (279.41,151.19) -- (265.46,151.05) -- (260.54,143.14) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.48 ] (271.75,143.14) -- (279.27,151.26) -- (266.83,150.76) -- (263.82,143.14) -- cycle ;
            		\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (24.09,158.24) -- (86.77,158.24) -- (86.77,162.75) -- (24.09,162.75) -- cycle ;
            		\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (19.28,160.5) .. controls (19.28,157.75) and (21.43,155.53) .. (24.09,155.53) .. controls (26.75,155.53) and (28.9,157.75) .. (28.9,160.5) .. controls (28.9,163.24) and (26.75,165.47) .. (24.09,165.47) .. controls (21.43,165.47) and (19.28,163.24) .. (19.28,160.5) -- cycle ;
            		\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (28.9,160.5) .. controls (28.9,157.75) and (31.06,155.53) .. (33.72,155.53) .. controls (36.38,155.53) and (38.53,157.75) .. (38.53,160.5) .. controls (38.53,163.24) and (36.38,165.47) .. (33.72,165.47) .. controls (31.06,165.47) and (28.9,163.24) .. (28.9,160.5) -- cycle ;
            		\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (81.04,160.5) .. controls (81.04,157.75) and (83.2,155.53) .. (85.86,155.53) .. controls (88.51,155.53) and (90.67,157.75) .. (90.67,160.5) .. controls (90.67,163.24) and (88.51,165.47) .. (85.86,165.47) .. controls (83.2,165.47) and (81.04,163.24) .. (81.04,160.5) -- cycle ;
            		\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (71.41,160.5) .. controls (71.41,157.75) and (73.57,155.53) .. (76.23,155.53) .. controls (78.89,155.53) and (81.04,157.75) .. (81.04,160.5) .. controls (81.04,163.24) and (78.89,165.47) .. (76.23,165.47) .. controls (73.57,165.47) and (71.41,163.24) .. (71.41,160.5) -- cycle ;
            		\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (38.53,160.5) .. controls (38.53,157.75) and (40.69,155.53) .. (43.35,155.53) .. controls (46,155.53) and (48.16,157.75) .. (48.16,160.5) .. controls (48.16,163.24) and (46,165.47) .. (43.35,165.47) .. controls (40.69,165.47) and (38.53,163.24) .. (38.53,160.5) -- cycle ;
            		\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (61.79,160.5) .. controls (61.79,157.75) and (63.94,155.53) .. (66.6,155.53) .. controls (69.26,155.53) and (71.41,157.75) .. (71.41,160.5) .. controls (71.41,163.24) and (69.26,165.47) .. (66.6,165.47) .. controls (63.94,165.47) and (61.79,163.24) .. (61.79,160.5) -- cycle ;
            		\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (21.26,160.5) .. controls (21.26,158.88) and (22.52,157.57) .. (24.09,157.57) .. controls (25.66,157.57) and (26.93,158.88) .. (26.93,160.5) .. controls (26.93,162.11) and (25.66,163.43) .. (24.09,163.43) .. controls (22.52,163.43) and (21.26,162.11) .. (21.26,160.5) -- cycle ;
            		\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (30.88,160.5) .. controls (30.88,158.88) and (32.15,157.57) .. (33.72,157.57) .. controls (35.28,157.57) and (36.55,158.88) .. (36.55,160.5) .. controls (36.55,162.11) and (35.28,163.43) .. (33.72,163.43) .. controls (32.15,163.43) and (30.88,162.11) .. (30.88,160.5) -- cycle ;
            		\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (40.51,160.5) .. controls (40.51,158.88) and (41.78,157.57) .. (43.35,157.57) .. controls (44.91,157.57) and (46.18,158.88) .. (46.18,160.5) .. controls (46.18,162.11) and (44.91,163.43) .. (43.35,163.43) .. controls (41.78,163.43) and (40.51,162.11) .. (40.51,160.5) -- cycle ;
            		\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (63.77,160.5) .. controls (63.77,158.88) and (65.03,157.57) .. (66.6,157.57) .. controls (68.17,157.57) and (69.44,158.88) .. (69.44,160.5) .. controls (69.44,162.11) and (68.17,163.43) .. (66.6,163.43) .. controls (65.03,163.43) and (63.77,162.11) .. (63.77,160.5) -- cycle ;
            		\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (73.39,160.5) .. controls (73.39,158.88) and (74.66,157.57) .. (76.23,157.57) .. controls (77.79,157.57) and (79.06,158.88) .. (79.06,160.5) .. controls (79.06,162.11) and (77.79,163.43) .. (76.23,163.43) .. controls (74.66,163.43) and (73.39,162.11) .. (73.39,160.5) -- cycle ;
            		\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (83.02,160.5) .. controls (83.02,158.88) and (84.29,157.57) .. (85.86,157.57) .. controls (87.42,157.57) and (88.69,158.88) .. (88.69,160.5) .. controls (88.69,162.11) and (87.42,163.43) .. (85.86,163.43) .. controls (84.29,163.43) and (83.02,162.11) .. (83.02,160.5) -- cycle ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 50; green, 112; blue, 186 }  ,fill opacity=1 ] (14.95,143.93) .. controls (14.95,141.62) and (16.83,139.75) .. (19.13,139.75) -- (90.21,139.75) .. controls (92.52,139.75) and (94.39,141.62) .. (94.39,143.93) -- (94.39,160.65) .. controls (94.39,160.65) and (94.39,160.65) .. (94.39,160.65) -- (14.95,160.65) .. controls (14.95,160.65) and (14.95,160.65) .. (14.95,160.65) -- cycle ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (15.17,157.82) -- (94.23,157.54) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (15.17,155.28) -- (94.23,155) ;
            		\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.75 ] (18.92,143.99) -- (33.36,143.99) -- (33.36,152.4) -- (18.92,152.4) -- cycle ;
            		\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.75 ] (35.42,143.99) -- (49.86,143.99) -- (49.86,152.4) -- (35.42,152.4) -- cycle ;
            		\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.75 ] (51.91,143.99) -- (66.35,143.99) -- (66.35,152.4) -- (51.91,152.4) -- cycle ;
            		\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.75 ] (68.13,143.99) -- (82.57,143.99) -- (82.57,152.4) -- (68.13,152.4) -- cycle ;
            		\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.75 ] (84.62,143.99) -- (91.08,143.99) -- (91.08,152.4) -- (84.62,152.4) -- cycle ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (16.54,141.73) -- (92.58,141.73) ;
            		\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (94.39,143.7) -- (96.14,143.7) -- (96.14,160.65) -- (94.39,160.65) -- cycle ;
            		\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (13.2,143.7) -- (14.95,143.7) -- (14.95,160.65) -- (13.2,160.65) -- cycle ;
            		\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (105.19,158.38) -- (167.88,158.38) -- (167.88,162.9) -- (105.19,162.9) -- cycle ;
            		\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (100.38,160.64) .. controls (100.38,157.89) and (102.54,155.67) .. (105.19,155.67) .. controls (107.85,155.67) and (110.01,157.89) .. (110.01,160.64) .. controls (110.01,163.38) and (107.85,165.61) .. (105.19,165.61) .. controls (102.54,165.61) and (100.38,163.38) .. (100.38,160.64) -- cycle ;
            		\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (110.01,160.64) .. controls (110.01,157.89) and (112.16,155.67) .. (114.82,155.67) .. controls (117.48,155.67) and (119.64,157.89) .. (119.64,160.64) .. controls (119.64,163.38) and (117.48,165.61) .. (114.82,165.61) .. controls (112.16,165.61) and (110.01,163.38) .. (110.01,160.64) -- cycle ;
            		\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (162.15,160.64) .. controls (162.15,157.89) and (164.3,155.67) .. (166.96,155.67) .. controls (169.62,155.67) and (171.77,157.89) .. (171.77,160.64) .. controls (171.77,163.38) and (169.62,165.61) .. (166.96,165.61) .. controls (164.3,165.61) and (162.15,163.38) .. (162.15,160.64) -- cycle ;
            		\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (152.52,160.64) .. controls (152.52,157.89) and (154.67,155.67) .. (157.33,155.67) .. controls (159.99,155.67) and (162.15,157.89) .. (162.15,160.64) .. controls (162.15,163.38) and (159.99,165.61) .. (157.33,165.61) .. controls (154.67,165.61) and (152.52,163.38) .. (152.52,160.64) -- cycle ;
            		\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (119.64,160.64) .. controls (119.64,157.89) and (121.79,155.67) .. (124.45,155.67) .. controls (127.11,155.67) and (129.26,157.89) .. (129.26,160.64) .. controls (129.26,163.38) and (127.11,165.61) .. (124.45,165.61) .. controls (121.79,165.61) and (119.64,163.38) .. (119.64,160.64) -- cycle ;
            		\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (142.89,160.64) .. controls (142.89,157.89) and (145.05,155.67) .. (147.7,155.67) .. controls (150.36,155.67) and (152.52,157.89) .. (152.52,160.64) .. controls (152.52,163.38) and (150.36,165.61) .. (147.7,165.61) .. controls (145.05,165.61) and (142.89,163.38) .. (142.89,160.64) -- cycle ;
            		\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (102.36,160.64) .. controls (102.36,159.02) and (103.63,157.71) .. (105.19,157.71) .. controls (106.76,157.71) and (108.03,159.02) .. (108.03,160.64) .. controls (108.03,162.26) and (106.76,163.57) .. (105.19,163.57) .. controls (103.63,163.57) and (102.36,162.26) .. (102.36,160.64) -- cycle ;
            		\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (111.99,160.64) .. controls (111.99,159.02) and (113.26,157.71) .. (114.82,157.71) .. controls (116.39,157.71) and (117.66,159.02) .. (117.66,160.64) .. controls (117.66,162.26) and (116.39,163.57) .. (114.82,163.57) .. controls (113.26,163.57) and (111.99,162.26) .. (111.99,160.64) -- cycle ;
            		\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (121.62,160.64) .. controls (121.62,159.02) and (122.88,157.71) .. (124.45,157.71) .. controls (126.02,157.71) and (127.29,159.02) .. (127.29,160.64) .. controls (127.29,162.26) and (126.02,163.57) .. (124.45,163.57) .. controls (122.88,163.57) and (121.62,162.26) .. (121.62,160.64) -- cycle ;
            		\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (144.87,160.64) .. controls (144.87,159.02) and (146.14,157.71) .. (147.7,157.71) .. controls (149.27,157.71) and (150.54,159.02) .. (150.54,160.64) .. controls (150.54,162.26) and (149.27,163.57) .. (147.7,163.57) .. controls (146.14,163.57) and (144.87,162.26) .. (144.87,160.64) -- cycle ;
            		\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (154.5,160.64) .. controls (154.5,159.02) and (155.77,157.71) .. (157.33,157.71) .. controls (158.9,157.71) and (160.17,159.02) .. (160.17,160.64) .. controls (160.17,162.26) and (158.9,163.57) .. (157.33,163.57) .. controls (155.77,163.57) and (154.5,162.26) .. (154.5,160.64) -- cycle ;
            		\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (164.13,160.64) .. controls (164.13,159.02) and (165.39,157.71) .. (166.96,157.71) .. controls (168.53,157.71) and (169.8,159.02) .. (169.8,160.64) .. controls (169.8,162.26) and (168.53,163.57) .. (166.96,163.57) .. controls (165.39,163.57) and (164.13,162.26) .. (164.13,160.64) -- cycle ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 50; green, 112; blue, 186 }  ,fill opacity=1 ] (96.06,144.07) .. controls (96.06,141.76) and (97.93,139.89) .. (100.24,139.89) -- (171.31,139.89) .. controls (173.62,139.89) and (175.49,141.76) .. (175.49,144.07) -- (175.49,160.79) .. controls (175.49,160.79) and (175.49,160.79) .. (175.49,160.79) -- (96.06,160.79) .. controls (96.06,160.79) and (96.06,160.79) .. (96.06,160.79) -- cycle ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (96.28,157.96) -- (175.33,157.68) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (96.28,155.42) -- (175.33,155.14) ;
            		\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.75 ] (100.03,144.13) -- (114.47,144.13) -- (114.47,152.54) -- (100.03,152.54) -- cycle ;
            		\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.75 ] (116.52,144.13) -- (130.96,144.13) -- (130.96,152.54) -- (116.52,152.54) -- cycle ;
            		\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.75 ] (133.01,144.13) -- (147.46,144.13) -- (147.46,152.54) -- (133.01,152.54) -- cycle ;
            		\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.75 ] (149.23,144.13) -- (163.68,144.13) -- (163.68,152.54) -- (149.23,152.54) -- cycle ;
            		\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.75 ] (165.73,144.13) -- (172.18,144.13) -- (172.18,152.54) -- (165.73,152.54) -- cycle ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (97.65,141.87) -- (173.69,141.87) ;
            		\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (175.49,143.84) -- (177.25,143.84) -- (177.25,160.79) -- (175.49,160.79) -- cycle ;
            		\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (94.3,143.84) -- (96.06,143.84) -- (96.06,160.79) -- (94.3,160.79) -- cycle ;
            		\draw  [fill={rgb, 255:red, 198; green, 174; blue, 139 }  ,fill opacity=1 ] (13.84,169.13) -- (641.87,169.13) -- (641.87,172.13) -- (13.84,172.13) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 65; green, 117; blue, 5 }  ,fill opacity=1 ] (13.97,166.36) -- (336.84,166.36) -- (336.84,169.15) -- (13.97,169.15) -- cycle ;
            		\draw  [color={rgb, 255:red, 139; green, 87; blue, 42 }  ,draw opacity=1 ][line width=5.25]  (569.36,168.48) .. controls (492.87,89.21) and (416.38,89.21) .. (339.88,168.48) ;
            		\draw [color={rgb, 255:red, 139; green, 87; blue, 42 }  ,draw opacity=1 ][line width=3]    (454.62,109.03) -- (454.62,165.57) ;
            		\draw [color={rgb, 255:red, 139; green, 87; blue, 42 }  ,draw opacity=1 ][line width=3]    (402.09,121.75) -- (402.09,165.1) ;
            		\draw [color={rgb, 255:red, 139; green, 87; blue, 42 }  ,draw opacity=1 ][line width=3]    (509.42,123.16) -- (509.42,165.57) ;
            		\draw [color={rgb, 255:red, 139; green, 87; blue, 42 }  ,draw opacity=1 ][line width=3]    (428.36,113.27) -- (428.36,166.98) ;
            		\draw [color={rgb, 255:red, 139; green, 87; blue, 42 }  ,draw opacity=1 ][line width=3]    (482.7,112.32) -- (482.7,166.51) ;
            		\draw [color={rgb, 255:red, 139; green, 87; blue, 42 }  ,draw opacity=1 ][line width=3]    (374.92,136.83) -- (374.92,165.1) ;
            		\draw [color={rgb, 255:red, 139; green, 87; blue, 42 }  ,draw opacity=1 ][line width=3]    (537.5,138.24) -- (537.5,166.51) ;
            		\draw [color={rgb, 255:red, 139; green, 87; blue, 42 }  ,draw opacity=1 ][line width=3]    (454.62,109.03) -- (428.36,166.98) ;
            		\draw [color={rgb, 255:red, 139; green, 87; blue, 42 }  ,draw opacity=1 ][line width=3]    (428.36,113.27) -- (402.09,165.1) ;
            		\draw [color={rgb, 255:red, 139; green, 87; blue, 42 }  ,draw opacity=1 ][line width=3]    (402.09,121.75) -- (374.92,165.1) ;
            		\draw [color={rgb, 255:red, 139; green, 87; blue, 42 }  ,draw opacity=1 ][line width=3]    (454.62,109.03) -- (482.7,166.51) ;
            		\draw [color={rgb, 255:red, 139; green, 87; blue, 42 }  ,draw opacity=1 ][line width=3]    (482.7,112.32) -- (509.42,165.57) ;
            		\draw [color={rgb, 255:red, 139; green, 87; blue, 42 }  ,draw opacity=1 ][line width=3]    (509.42,123.16) -- (537.5,166.51) ;
            		\draw  [color={rgb, 255:red, 139; green, 87; blue, 42 }  ,draw opacity=1 ][fill={rgb, 255:red, 139; green, 87; blue, 42 }  ,fill opacity=1 ] (336.71,163.37) -- (572.53,163.37) -- (572.53,171.22) -- (336.71,171.22) -- cycle ;
            		\draw  [fill={rgb, 255:red, 184; green, 193; blue, 205 }  ,fill opacity=1 ] (321.33,172.67) -- (349.2,172.67) -- (349.2,206.8) -- (321.33,206.8) -- cycle ;
            		\draw  [fill={rgb, 255:red, 184; green, 193; blue, 205 }  ,fill opacity=1 ] (542.39,171.28) -- (570.26,171.28) -- (570.26,205.41) -- (542.39,205.41) -- cycle ;
            		\draw  [fill={rgb, 255:red, 234; green, 204; blue, 179 }  ,fill opacity=1 ] (13.84,171.28) -- (321.33,172.67) -- (321.33,206.8) -- (14.53,180.8) -- cycle ;
            		\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ] (14.53,180.8) -- (321.2,206.67) -- (349.2,206.8) -- (396.53,246.8) -- (15.2,247.47) -- cycle ;
            		\draw  [fill={rgb, 255:red, 113; green, 118; blue, 126 }  ,fill opacity=1 ] (525.2,171.47) -- (542.39,171.28) -- (542.39,205.41) -- (524.53,196.13) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 97; green, 207; blue, 240 }  ,fill opacity=1 ] (349.2,206.8) -- (350.53,186.13) -- (525.2,186.13) -- (524.53,196.13) -- (542.39,205.41) -- (607.2,249.47) -- (396.53,246.8) -- cycle ;
            		\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (56.81,124.99) -- (58.05,124.99) -- (58.05,164.99) -- (56.81,164.99) -- cycle ;
            		\draw  [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ][line width=2.25]  (58.05,117.66) -- (67.65,132.33) -- (48.45,132.33) -- cycle ;
            		\draw    (56.81,124.99) -- (60.71,130.5) ;
            		\draw [shift={(61.87,132.13)}, rotate = 234.69] [color={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.75]    (10.93,-3.29) .. controls (6.95,-1.4) and (3.31,-0.3) .. (0,0) .. controls (3.31,0.3) and (6.95,1.4) .. (10.93,3.29)   ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 65; green, 117; blue, 5 }  ,fill opacity=1 ] (567.11,166.6) -- (641.87,166.6) -- (641.87,169.13) -- (567.11,169.13) -- cycle ;
            		\draw  [fill={rgb, 255:red, 234; green, 204; blue, 179 }  ,fill opacity=1 ] (641.87,172.13) -- (570.26,171.28) -- (570.26,205.41) -- (640.53,195.73) -- cycle ;
            		\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ] (640.53,195.73) -- (570.26,205.41) -- (542.39,205.41) -- (607.2,249.47) -- (641.87,249.73) -- cycle ;
            	\end{tikzpicture}
            \end{center}'''
                # Câu hỏi
                noidungcauhoi = (r'''Một đoàn tàu đang chạy thẳng đều với tốc độ $%s$ m/s thì phát hiện biển báo phía trước có một cây cầu yếu. Bắt đầu từ vị trí cách đầu cầu $%s$ m, lái tàu hãm phanh làm vận tốc của tàu giảm dần theo quy luật $v(t) = -at^2 + b$ (m/s), trong đó $t$ là thời gian tính bằng giây kể từ lúc bắt đầu hãm phanh. Biết rằng đúng lúc mũi tàu chạm đầu cầu thì vận tốc tàu giảm còn $%s$ m/s. Hỏi kể từ lúc bắt đầu hãm phanh, khi tàu đi được quãng đường $%s$ m thì độ lớn gia tốc thực tế của đoàn tàu lúc đó là bao nhiêu m/s$^2$? %s'''
                                 % (latex(v0), latex(S_total), latex(vT), latex(S_t1_int),hinhve))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Trộn ngẫu nhiên đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Các phân số trung gian phục vụ hiển thị lời giải
                ba_he_so = 3 * b
                pt_bac3_c = 3 * S_t1_int

                # Nội dung lời giải chi tiết từng bước
                loigiai = ('''Tại thời điểm $t = 0$ vận tốc của tàu là $%s$ m/s: $v(0) = -a \\cdot (0)^2 + b = %s \\Rightarrow b = %s$.\\\\
                           Vậy hàm vận tốc có dạng: $v(t) = -at^2 + %s$.\\\\
                           Gọi $T$ (giây) là thời gian kể từ lúc hãm phanh đến khi mũi tàu chạm đầu cầu.\\\\
                           Theo đề bài, ta có hệ phương trình:\\\\
                           Vận tốc tại $T$ là: $v(T) = -aT^2 + %s = %s \\Rightarrow aT^2 = %s \\Rightarrow a = \\frac{%s}{T^2}$ (1).\\\\
                           Quãng đường đi được sau thời gian $T$:\\\\
                           $S(T) = \\int\\limits_{0}^{T} (-at^2 + %s) \\, \\text{d}t = \\left. \\left( -\\frac{1}{3}at^3 + %st \\right) \\right|_{0}^{T} = -\\frac{1}{3}at^3 + %sT = %s$ (2).\\\\
                           Thay (1) vào (2) ta được: $-\\frac{1}{3} \\cdot \\frac{%s}{T^2} \\cdot T^3 + %sT = %s \\Rightarrow T = %s$ suy ra $a = \\frac{%s}{%s^2} = %s$.\\\\
                           Vậy hàm vận tốc là: $v(t) = -%st^2 + %s$.\\\\
                           Gọi $t_1$ là khoảng thời gian cần tìm, ta có phương trình quãng đường:\\\\
                           $S(t_1) = \\int\\limits_{0}^{t_1} \\left( -%st^2 + %s \\right) \\, \\text{d}t = %s \\Leftrightarrow \\left. \\left( -\\frac{%s}{3}t^3 + %st \\right) \\right|_{0}^{t_1} = %s \\Leftrightarrow t_1^3 - %st_1 + %s = 0 \\Rightarrow t_1 = %s$.\\\\
                           Gia tốc của đoàn tàu là: $a(t) = v'(t) = \\left( -%st^2 + %s \\right)' = -%st$.\\\\
                           Tại thời điểm $t_1 = %s$ gia tốc thực tế là: $a(%s) = -%s \\cdot %s = -%s$ (m/s$^2$).\\\\
                           Độ lớn gia tốc lúc này là: $|a(%s)| = %s$ (m/s$^2$).'''
                           % (latex(v0), latex(v0), latex(b), latex(b),
                              latex(b), latex(vT), latex(diff_v), latex(diff_v),
                              latex(b), latex(b), latex(b), latex(S_total),
                              latex(diff_v), latex(b), latex(S_total), latex(T_val), latex(diff_v), latex(T_val), latex(a),
                              latex(a), latex(b),
                              latex(a), latex(b), latex(S_t1_int), latex(a), latex(b), latex(S_t1_int), latex(Rational(ba_he_so, a)), latex(Rational(pt_bac3_c, a)), latex(t1_val),
                              latex(a), latex(b), latex(2*a),
                              latex(t1_val), latex(t1_val), latex(2*a), latex(t1_val), latex(gia_toc_t1),
                              latex(t1_val), latex(kq_chinh_xac)
                              ))
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq_chinh_xac))
            # Xuất câu trắc nghiệm định dạng mẫu ex
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) +dapan+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content


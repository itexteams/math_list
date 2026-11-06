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


def bt_dang3_p2_b3_c2_hh12(self):
            # Khai báo biến
            # Khai báo biến
            x, y, z = symbols('x y z')

            # Random các thông số sao cho kết quả đẹp (mẫu số nguyên)
            n_choices = [(2, 2, 1), (2, -2, 1), (1, 2, 2), (1, -2, 2)]
            A, B, C = random.choice(n_choices)
            Dp = random.randint(-8, -2)

            u_choices = [(1, -2, -2), (2, 1, 2), (2, 2, 1), (-1, -2, -2), (-2, 2, -1)]
            u1, u2, u3 = random.choice(u_choices)

            # Đảm bảo tia laser không song song với mặt phẳng
            while A*u1 + B*u2 + C*u3 == 0:
                u1, u2, u3 = random.choice(u_choices)

            xs = random.randint(1, 3)
            ys = random.randint(1, 3)
            zs = random.randint(4, 8)

            # Các thông số của bài toán
            mat_phang = A*x + B*y + C*z + Dp
            len_n = sp.sqrt(A**2 + B**2 + C**2)
            len_u = sp.sqrt(u1**2 + u2**2 + u3**2)

            # Tính toán Nhận biết (Khoảng cách)
            tu_so_d = abs(A*xs + B*ys + C*zs + Dp)
            dist_val = sp.Rational(tu_so_d, len_n)
            dist_false = dist_val + sp.Rational(1, 3)

            # Tính toán Thông hiểu (Giao điểm M)
            mau_so_t = A*u1 + B*u2 + C*u3
            tu_so_t = -(A*xs + B*ys + C*zs + Dp)
            t_val = sp.Rational(tu_so_t, mau_so_t)

            Mx = xs + u1*t_val
            My = ys + u2*t_val
            Mz = zs + u3*t_val

            Mx_false = Mx + 1
            My_false = My - 1
            Mz_false = Mz

            # Tính toán Vận dụng (Góc alpha)
            tich_vo_huong = abs(A*u1 + B*u2 + C*u3)
            sin_val = sp.Rational(tich_vo_huong, len_n * len_u)
            # Đảm bảo sin_false < 1
            sin_false = sp.Rational(tich_vo_huong + 1, len_n * len_u) if tich_vo_huong + 1 < len_n * len_u else sp.Rational(tich_vo_huong - 1, len_n * len_u)

            # Tính toán Vận dụng cao (Hướng dòng nước)
            ud1, ud2, ud3 = B, -A, 0
            c1, c2, c3 = -A*C, -B*C, A**2 + B**2
            v1, v2, v3 = -c1, -c2, -c3

            g = math.gcd(abs(v1), math.gcd(abs(v2), abs(v3)))
            v1, v2, v3 = v1//g, v2//g, v3//g
            v1_false, v2_false, v3_false = v1, v2, abs(v3)

            hinhve=r'''\begin{center} \scalebox{0.8}{ \begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\draw  [draw opacity=0][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=0.5 ] (403.67,127.87) -- (140.69,155.31) -- (64.43,136.91) -- (356.43,124.11) -- cycle ;
            	\draw  [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (226.73,128.28) -- (277.05,131.6) -- (267.65,132.34) -- cycle ;
            	\draw  [color={rgb, 255:red, 184; green, 233; blue, 134 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (230.05,127.64) -- (280.37,130.96) -- (270.97,131.7) -- cycle ;
            	\draw  [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (245.35,127.46) -- (295.67,130.77) -- (286.27,131.51) -- cycle ;
            	\draw  [color={rgb, 255:red, 184; green, 233; blue, 134 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (244.24,125.98) -- (294.56,129.3) -- (285.16,130.04) -- cycle ;
            	\draw  [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (267.46,119.9) -- (277.05,119.53) -- (277.42,132.06) -- (267.83,132.62) -- cycle ;
            	\draw  [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (285.9,119.16) -- (294.01,118.61) -- (294.56,131.14) -- (286.27,131.51) -- cycle ;
            	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (277.05,119.53) -- (285.9,119.16) ;
            	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (267.65,131.14) -- (277.05,130.4) ;
            	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (286.45,129.85) -- (294.56,129.3) ;
            	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (272.26,130.4) -- (271.52,115.66) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (277.05,119.53) -- (276.68,111.97) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (285.9,119.16) -- (285.53,112.34) ;
            	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (290.69,129.67) -- (289.95,114.92) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (226.36,117.13) -- (267.46,119.9) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (226.54,128.01) -- (267.83,132.62) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (226.73,127.09) -- (267.65,131.14) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (261.93,130.04) -- (261.75,119.71) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (256.59,129.85) -- (256.41,119.35) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (251.06,129.3) -- (250.88,118.79) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (246.08,128.56) -- (245.9,118.42) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (241.47,128.38) -- (241.29,118.24) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (237.6,128.01) -- (237.42,117.87) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (233.55,127.82) -- (233.36,117.69) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (226.54,128.01) -- (226.54,116.95) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (230.05,127.64) -- (229.86,117.5) ;
            	\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (288.29,118.44) .. controls (278.89,107.43) and (270.04,107.86) .. (261.75,119.71) ;
            	\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (282.03,118.44) .. controls (272.63,107.43) and (263.78,107.86) .. (255.48,119.71) ;
            	\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (277.42,117.52) .. controls (268.02,106.51) and (259.17,106.93) .. (250.88,118.79) ;
            	\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (272.44,117.15) .. controls (263.04,106.14) and (254.2,106.57) .. (245.9,118.42) ;
            	\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (267.83,116.96) .. controls (258.43,105.95) and (249.58,106.38) .. (241.29,118.24) ;
            	\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (263.96,116.6) .. controls (254.56,105.59) and (245.72,106.01) .. (237.42,117.87) ;
            	\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (259.91,116.41) .. controls (250.51,105.4) and (241.66,105.82) .. (233.36,117.69) ;
            	\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (256.41,116.23) .. controls (247.01,105.22) and (238.16,105.64) .. (229.86,117.5) ;
            	\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (252.9,115.86) .. controls (243.5,104.85) and (234.66,105.28) .. (226.36,117.13) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (252.9,115.86) -- (294.01,118.61) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (226.54,116.95) -- (252.9,115.86) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (235.94,126.9) -- (277.05,130.4) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (252.35,126.35) -- (286.45,129.85) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (252.17,127.46) -- (286.27,131.51) ;
            	\draw  [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (294.01,118.62) .. controls (284.61,107.61) and (275.76,108.04) .. (267.46,119.9) ;
            	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (272.26,130.4) -- (271.52,115.66) ;
            	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (267.83,132.62) -- (267.46,119.9) ;
            	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (277.42,132.06) -- (276.68,111.97) ;
            	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (286.27,131.51) -- (285.53,112.34) ;
            	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (277.05,130.4) -- (267.65,131.14) ;
            	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (294.01,118.62) -- (267.46,119.9) ;
            	\draw  [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (179.58,129.9) -- (236.72,133.67) -- (226.05,134.5) -- cycle ;
            	\draw  [color={rgb, 255:red, 184; green, 233; blue, 134 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (183.35,129.16) -- (240.49,132.93) -- (229.82,133.77) -- cycle ;
            	\draw  [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (200.72,128.96) -- (257.87,132.72) -- (247.19,133.56) -- cycle ;
            	\draw  [color={rgb, 255:red, 184; green, 233; blue, 134 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (199.46,127.28) -- (256.61,131.05) -- (245.94,131.89) -- cycle ;
            	\draw  [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (225.84,120.37) -- (236.72,119.95) -- (237.14,134.19) -- (226.26,134.82) -- cycle ;
            	\draw  [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (246.77,119.54) -- (255.98,118.91) -- (256.61,133.14) -- (247.19,133.56) -- cycle ;
            	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (236.72,119.95) -- (246.77,119.54) ;
            	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (226.05,133.14) -- (236.72,132.3) ;
            	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (247.4,131.68) -- (256.61,131.05) ;
            	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (231.28,132.3) -- (230.44,115.56) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (236.72,119.95) -- (236.31,111.37) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (246.77,119.54) -- (246.35,111.79) ;
            	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (252.21,131.47) -- (251.38,114.72) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (179.16,117.23) -- (225.84,120.37) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (179.37,129.58) -- (226.26,134.82) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (179.58,128.54) -- (226.05,133.14) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (219.56,131.89) -- (219.35,120.16) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (213.49,131.68) -- (213.28,119.75) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (207.21,131.05) -- (207,119.12) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (201.56,130.21) -- (201.35,118.7) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (196.32,130) -- (196.12,118.49) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (191.93,129.58) -- (191.72,118.07) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (187.32,129.37) -- (187.11,117.86) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (179.37,129.58) -- (179.37,117.02) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (183.35,129.16) -- (183.14,117.65) ;
            	\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (249.49,118.72) .. controls (238.82,106.21) and (228.77,106.69) .. (219.35,120.16) ;
            	\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (242.38,118.72) .. controls (231.71,106.21) and (221.66,106.69) .. (212.23,120.16) ;
            	\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (237.14,117.67) .. controls (226.47,105.16) and (216.42,105.65) .. (207,119.12) ;
            	\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (231.49,117.25) .. controls (220.82,104.75) and (210.77,105.23) .. (201.35,118.7) ;
            	\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (226.26,117.04) .. controls (215.59,104.54) and (205.54,105.02) .. (196.12,118.49) ;
            	\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (221.86,116.62) .. controls (211.19,104.12) and (201.14,104.6) .. (191.72,118.07) ;
            	\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (217.26,116.41) .. controls (206.59,103.91) and (196.54,104.4) .. (187.11,117.86) ;
            	\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (213.28,116.2) .. controls (202.6,103.7) and (192.57,104.19) .. (183.14,117.65) ;
            	\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (209.3,115.79) .. controls (198.63,103.28) and (188.58,103.76) .. (179.16,117.23) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (209.3,115.79) -- (255.98,118.91) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (179.37,117.02) -- (209.3,115.79) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (190.04,128.33) -- (236.72,132.3) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (208.67,127.7) -- (247.4,131.68) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (208.47,128.96) -- (247.19,133.56) ;
            	\draw  [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (255.98,118.93) .. controls (245.31,106.42) and (235.26,106.9) .. (225.84,120.37) ;
            	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (231.28,132.3) -- (230.44,115.56) ;
            	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (226.26,134.82) -- (225.84,120.37) ;
            	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (237.14,134.19) -- (236.31,111.37) ;
            	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (247.19,133.56) -- (246.35,111.79) ;
            	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (236.72,132.3) -- (226.05,133.14) ;
            	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (255.98,118.93) -- (225.84,120.37) ;
            	\draw  [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (124.5,134.41) -- (191.92,138.86) -- (179.33,139.85) -- cycle ;
            	\draw  [color={rgb, 255:red, 184; green, 233; blue, 134 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (128.94,133.55) -- (196.37,137.99) -- (183.77,138.98) -- cycle ;
            	\draw  [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (149.44,133.3) -- (216.87,137.75) -- (204.27,138.73) -- cycle ;
            	\draw  [color={rgb, 255:red, 184; green, 233; blue, 134 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (147.96,131.33) -- (215.38,135.77) -- (202.79,136.76) -- cycle ;
            	\draw  [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (179.08,123.17) -- (191.92,122.68) -- (192.42,139.48) -- (179.57,140.22) -- cycle ;
            	\draw  [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (203.78,122.19) -- (214.64,121.45) -- (215.38,138.24) -- (204.27,138.73) -- cycle ;
            	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (191.92,122.68) -- (203.78,122.19) ;
            	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (179.33,138.24) -- (191.92,137.25) ;
            	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (204.52,136.51) -- (215.38,135.77) ;
            	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (185.5,137.25) -- (184.51,117.49) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (191.92,122.68) -- (191.43,112.55) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (203.78,122.19) -- (203.28,113.05) ;
            	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (210.2,136.26) -- (209.21,116.51) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (124,119.47) -- (179.08,123.17) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (124.25,134.04) -- (179.57,140.22) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (124.5,132.81) -- (179.33,138.24) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (171.67,136.76) -- (171.42,122.93) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (164.51,136.51) -- (164.26,122.43) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (157.1,135.77) -- (156.85,121.69) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (150.43,134.78) -- (150.18,121.2) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (144.25,134.54) -- (144.01,120.95) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (139.07,134.04) -- (138.82,120.46) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (133.63,133.8) -- (133.39,120.21) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (124.25,134.04) -- (124.25,119.22) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (128.94,133.55) -- (128.69,119.96) ;
            	\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (206.99,121.22) .. controls (194.4,106.46) and (182.54,107.03) .. (171.42,122.93) ;
            	\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (198.59,121.22) .. controls (186,106.46) and (174.14,107.03) .. (163.02,122.93) ;
            	\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (192.42,119.98) .. controls (179.83,105.23) and (167.97,105.8) .. (156.85,121.69) ;
            	\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (185.75,119.49) .. controls (173.16,104.73) and (161.3,105.3) .. (150.18,121.2) ;
            	\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (179.57,119.24) .. controls (166.98,104.49) and (155.12,105.06) .. (144.01,120.95) ;
            	\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (174.39,118.75) .. controls (161.8,103.99) and (149.94,104.56) .. (138.82,120.46) ;
            	\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (168.95,118.5) .. controls (156.36,103.75) and (144.5,104.32) .. (133.39,120.21) ;
            	\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (164.26,118.26) .. controls (151.67,103.5) and (139.81,104.07) .. (128.69,119.96) ;
            	\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (159.57,117.76) .. controls (146.98,103.01) and (135.12,103.58) .. (124,119.47) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (159.57,117.76) -- (214.64,121.45) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (124.25,119.22) -- (159.57,117.76) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (136.84,132.56) -- (191.92,137.25) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (158.83,131.82) -- (204.52,136.51) ;
            	\draw [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (158.58,133.3) -- (204.27,138.73) ;
            	\draw  [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (214.64,121.47) .. controls (202.05,106.72) and (190.2,107.28) .. (179.08,123.17) ;
            	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (185.5,137.25) -- (184.51,117.49) ;
            	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (179.57,140.22) -- (179.08,123.17) ;
            	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (192.42,139.48) -- (191.43,112.55) ;
            	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (204.27,138.73) -- (203.28,113.05) ;
            	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (191.92,137.25) -- (179.33,138.24) ;
            	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ]   (214.64,121.47) -- (179.08,123.17) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.38 ] (427.07,203.82) -- (293.07,225.27) -- (417.57,255.27) -- (498.57,254.27) -- (498.07,203.27) -- (453.57,211.77) -- cycle ;
            	\draw  [fill={rgb, 255:red, 199; green, 194; blue, 194 }  ,fill opacity=1 ] (303.72,24.67) -- (305.97,169.92) -- (300.97,170.67) -- (299.97,24.67) -- cycle ;
            	\draw  [fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (307.72,24.42) -- (309.72,165.67) -- (305.97,169.92) -- (303.72,24.67) -- cycle ;
            	\draw  [fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (307.97,30.42) -- (308.22,41.42) -- (304.47,41.92) -- (304.22,30.17) -- cycle ;
            	\draw  [fill={rgb, 255:red, 199; green, 194; blue, 194 }  ,fill opacity=1 ] (309.22,31.17) -- (314.47,39.92) -- (310.72,44.67) -- (305.22,35.92) -- cycle ;
            	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (319.72,41.42) -- (315.22,46.67) -- (310.72,44.67) -- (314.47,39.92) -- cycle ;
            	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (313.72,31.67) -- (319.72,41.42) -- (314.47,39.92) -- (309.22,31.17) -- cycle ;
            	\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ]   (315.22,43.67) -- (340.07,81.66) ;
            	\draw [shift={(341.72,84.17)}, rotate = 236.8] [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ][line width=0.08]  [draw opacity=0] (10.72,-5.15) -- (0,0) -- (10.72,5.15) -- (7.12,0) -- cycle    ;
            	\draw  [fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (296.67,211.22) -- (280.42,216.97) -- (275.17,215.47) -- (290.17,210.22) -- cycle ;
            	\draw  [fill={rgb, 255:red, 7; green, 46; blue, 98 }  ,fill opacity=1 ] (343.47,115.87) -- (487.97,128.87) -- (405.47,229.37) -- (253.47,197.87) -- cycle ;
            	\draw  [fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (487.97,128.87) -- (489.02,132.57) -- (405.91,234.87) -- (405.47,229.37) -- cycle ;
            	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (405.47,229.37) -- (405.91,234.87) -- (255.27,202.07) -- (253.47,197.87) -- cycle ;
            	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (283.12,207.97) -- (282.62,214.47) -- (278.66,214.2) -- (279.12,207.47) -- cycle ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (286.37,208.97) -- (286.25,210.74) -- (286.12,212.72) -- (282.62,214.47) -- (283.12,207.97) -- cycle ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (302.92,212.47) -- (280.17,220.97) -- (280.42,216.97) -- (296.67,211.22) -- cycle ;
            	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (280.17,220.97) -- (275.13,219.8) -- (275.17,215.47) -- (280.42,216.97) -- cycle ;
            	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (407.92,239.72) -- (403.92,242.97) -- (284.42,215.97) -- (288.17,214.22) -- cycle ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (403.92,242.97) -- (404.92,247.22) -- (284.42,219.47) -- (284.42,215.97) -- cycle ;
            	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (455.92,216.22) -- (455.17,218.97) -- (423.42,213.47) -- (426.17,210.47) -- cycle ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (455.17,218.97) -- (455.67,222.72) -- (421.17,216.47) -- (423.42,213.47) -- cycle ;
            	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (467.17,219.22) -- (407.92,245.22) -- (402.42,243.22) -- (459.92,217.72) -- cycle ;
            	\draw  [fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (467.42,223.97) -- (407.92,250.22) -- (407.92,245.22) -- (467.17,219.22) -- cycle ;
            	\draw  [fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (417.77,221.32) -- (414.52,239.82) -- (411.02,241.82) -- (413.77,226.32) -- cycle ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (413.77,226.32) -- (411.02,241.82) -- (406.02,240.82) -- (407.16,233.87) -- cycle ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (444.52,187.32) -- (459.27,221.57) -- (454.02,220.07) -- (442.02,191.82) -- cycle ;
            	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (447.71,183.97) -- (461.77,219.82) -- (459.27,221.57) -- (444.52,187.32) -- cycle ;
            	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (407.67,249.47) -- (403.47,248.67) -- (403.92,242.97) -- (407.67,244.47) -- cycle ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.73 ]   (255.47,197.42) -- (405.47,228.37) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.73 ][line width=1.5]    (404.22,227.67) -- (485.22,129.67) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.73 ][line width=1.5]    (343.97,117.17) -- (485.22,129.67) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.73 ][line width=0.75]    (255.47,197.42) -- (343.97,117.17) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ][line width=0.75]    (268.97,199.67) -- (353.47,118.42) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ][line width=0.75]    (279.72,201.42) -- (364.72,119.67) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ][line width=0.75]    (290.22,203.67) -- (373.97,120.67) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ][line width=0.75]    (301.97,206.17) -- (383.97,121.42) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ][line width=0.75]    (311.47,207.92) -- (395.47,121.92) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ][line width=0.75]    (323.22,210.67) -- (406.72,122.92) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ][line width=0.75]    (335.72,212.67) -- (418.22,124.17) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ][line width=0.75]    (348.97,216.17) -- (430.97,125.42) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ][line width=0.75]    (362.22,218.92) -- (442.97,126.67) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ][line width=0.75]    (375.97,221.42) -- (456.47,127.17) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ][line width=0.75]    (389.97,224.67) -- (469.72,128.17) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ][line width=0.75]    (475.47,140.67) -- (333.97,126.92) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ][line width=0.75]    (467.72,149.92) -- (324.97,134.92) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ][line width=0.75]    (458.97,160.67) -- (315.97,143.17) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ][line width=0.75]    (450.97,170.42) -- (306.47,151.17) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ][line width=0.75]    (441.97,181.17) -- (296.97,159.92) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ][line width=0.75]    (432.97,192.67) -- (286.97,169.17) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ][line width=0.75]    (423.47,203.42) -- (277.22,177.92) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.5 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ][line width=0.75]    (414.22,215.67) -- (266.97,187.67) ;
            	\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ]   (341.72,84.17) -- (392.8,160.67) ;
            	\draw [shift={(394.47,163.17)}, rotate = 236.27] [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ][line width=0.08]  [draw opacity=0] (10.72,-5.15) -- (0,0) -- (10.72,5.15) -- (7.12,0) -- cycle    ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.3 ] (388.27,118.92) -- (307.27,147.17) -- (313.77,150.42) -- (399.77,119.92) -- cycle ;
            	\draw    (340,129.93) -- (145,151.93) ;
            	\draw    (84,138.93) -- (145,151.93) ;
            	\draw    (248.22,169.92) -- (277.22,177.92) ;
            	\draw [color={rgb, 255:red, 248; green, 231; blue, 28 }  ,draw opacity=1 ] [dash pattern={on 4.5pt off 4.5pt}]  (424.73,126.33) -- (342.73,215.33) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.14 ] (476.47,131.28) -- (329.47,213.62) -- (265.27,202.42) -- (306.8,167.28) -- cycle ;
            	\draw (95,160) node [anchor=north west][inner sep=0.75pt]    {$( P)$};
            	\draw (369,73) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize] [align=left] {(Tia laser)};
            	\draw (351.67,72.67) node [anchor=north west][inner sep=0.75pt]    {$\Delta $};
            	\draw (392.67,156.67) node [anchor=north west][inner sep=0.75pt]  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,opacity=1 ]  {$M$};
            	\draw (331.47,46.67) node [anchor=north west][inner sep=0.75pt]    {$\vec{u}$};
            	\draw (122,161.31) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize] [align=left] {(Mặt phẳng tấm pin)};
            \end{tikzpicture} } \end{center}'''

            # Nội dung câu hỏi
            noidungcauhoi = (r'''Trong một mô hình nông nghiệp công nghệ cao, một tấm pin năng lượng mặt trời phẳng được lắp đặt nghiêng sao cho bề mặt của nó nằm trên mặt phẳng $\left(P\right): %s = 0$ (xét trong hệ không gian tọa độ $Oxyz$ với đơn vị đo là mét, mặt phẳng $\left(Oxy\right)$ được xem là mặt đất phẳng). Người ta lắp đặt một robot cố định ở trên cao để kiểm tra bụi bẩn. Robot có mắt phát tia laser tại điểm $S\left(%s; %s; %s\right)$. Robot thực hiện quét tia laser trên bề mặt tấm pin. Tại một thời điểm tia laser được chiếu theo đường thẳng $\Delta$ có vectơ chỉ phương $\vec{u}=\left(%s; %s; %s\right)$ và chạm vào bề mặt tấm pin tại điểm $M$. %s'''               
                             %(latex(mat_phang), xs, ys, zs, u1, u2, u3, hinhve
                                 ))

            ########################################################################
            # Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Khoảng cách từ mắt phát tia laser $S$ đến mặt phẳng $\\left(P\\right)$ bằng $%s$ mét' % (latex(dist_val))
            nb_da_1_s = 'Khoảng cách từ mắt phát tia laser $S$ đến mặt phẳng $\\left(P\\right)$ bằng $%s$ mét' % (latex(dist_false))
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Ta có công thức tính khoảng cách từ điểm $S$ đến mặt phẳng $\\left(P\\right)$ là: \\\\
                            $d\\left(S, \\left(P\\right)\\right) = \\frac{\\left|%s\\cdot (%s) + (%s)\\cdot (%s) + (%s)\\cdot (%s) + \\left(%s\\right)\\right|}{\\sqrt{(%s)^2 + (%s)^2 + (%s)^2}} = \\frac{%s}{%s} = %s$ (mét).'''
                            % (A, xs, B, ys, C, zs, Dp, A, B, C, tu_so_d, len_n, latex(dist_val))
                        )

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Điểm $M$ có tọa độ là $\\left(%s; %s; %s\\right)$' % (latex(Mx), latex(My), latex(Mz))  
            th_da_1_s = 'Điểm $M$ có tọa độ là $\\left(%s; %s; %s\\right)$' % (latex(Mx_false), latex(My_false), latex(Mz_false))   
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Phương trình tham số của đường thẳng $\\Delta$ đi qua $S\\left(%s; %s; %s\\right)$ và có vectơ chỉ phương $\\vec{u}=\\left(%s; %s; %s\\right)$ là: $\\left\\{\\begin{matrix}x=%s%s\\\\y=%s%s\\\\z=%s%s\\end{matrix}\\right.$ (với $t \\in \\mathbb{R}$). \\\\
                            Vì điểm $M$ là giao điểm của đường thẳng $\\Delta$ và mặt phẳng $\\left(P\\right)$ nên tọa độ điểm $M$ thỏa mãn phương trình mặt phẳng $\\left(P\\right)$. Thay $x, y, z$ vào phương trình mặt phẳng $\\left(P\\right)$, ta được: \\\\
                            $%s\\left(%s%s\\right) + %s\\left(%s%s\\right) + %s\\left(%s%s\\right) + \\left(%s\\right) = 0 \\Leftrightarrow %s t + %s = 0 \\Leftrightarrow t = %s$. \\\\
                            Thay $t = %s$ vào phương trình tham số của $\\Delta$, ta tìm được tọa độ điểm $M$ là $M\\left(%s; %s; %s\\right)$.'''       
                       %(xs, ys, zs, u1, u2, u3, 
                         xs, '+'+str(u1)+'t' if u1>0 else str(u1)+'t', 
                         ys, '+'+str(u2)+'t' if u2>0 else str(u2)+'t', 
                         zs, '+'+str(u3)+'t' if u3>0 else str(u3)+'t',
                         A, xs, '+'+str(u1)+'t' if u1>0 else str(u1)+'t', 
                         B, ys, '+'+str(u2)+'t' if u2>0 else str(u2)+'t', 
                         C, zs, '+'+str(u3)+'t' if u3>0 else str(u3)+'t', 
                         Dp, mau_so_t, -tu_so_t, latex(t_val), latex(t_val), latex(Mx), latex(My), latex(Mz)
                            ))

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## 
            # Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Góc $\\alpha$ hợp bởi tia laser $\\Delta$ và mặt phẳng $\\left(P\\right)$ thỏa mãn hệ thức $\\sin\\alpha = %s$' % (latex(sin_val))  
            vd_da_1_s = 'Góc $\\alpha$ hợp bởi tia laser $\\Delta$ và mặt phẳng $\\left(P\\right)$ thỏa mãn hệ thức $\\sin\\alpha = %s$' % (latex(sin_false))  
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Mặt phẳng $\\left(P\\right)$ có vectơ pháp tuyến $\\vec{n}=\\left(%s; %s; %s\\right)$. Đường thẳng $\\Delta$ có vectơ chỉ phương $\\vec{u}=\\left(%s; %s; %s\\right)$. \\\\
                            Gọi $\\alpha$ là góc hợp bởi đường thẳng $\\Delta$ và mặt phẳng $\\left(P\\right)$. Ta có công thức: \\\\
                            $\\sin\\alpha = \\frac{\\left|\\vec{u}\\cdot \\vec{n}\\right|}{\\left|\\vec{u}\\right|\\cdot \\left|\\vec{n}\\right|} = \\frac{\\left|%s\\cdot (%s) + (%s) \\cdot (%s) + (%s) \\cdot (%s)\\right|}{\\sqrt{(%s)^2 + (%s)^2 + (%s)^2}\\cdot \\sqrt{(%s)^2 + (%s)^2 + (%s)^2}} = \\frac{%s}{%s\\cdot %s} = %s$.'''  
                       %(A, B, C, u1, u2, u3, u1, A, u2, B, u3, C, u1, u2, u3, A, B, C, tich_vo_huong, len_u, len_n, latex(sin_val)
                            ))

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## 
            # Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Khi vệ sinh, nước được phun trúng điểm chạm của tia laser trên tấm pin sẽ tạo thành dòng nước chảy trên bề mặt pin xuống đất theo hướng dốc nhất, quỹ đạo chảy của dòng nước nằm trên một đường thẳng. Đường thẳng đó có một vectơ chỉ phương là $\\vec{v}=\\left(%s; %s; %s\\right)$' % (v1, v2, v3) 
            vdc_da_1_s = 'Khi vệ sinh, nước được phun trúng điểm chạm của tia laser trên tấm pin sẽ tạo thành dòng nước chảy trên bề mặt pin xuống đất theo hướng dốc nhất, quỹ đạo chảy của dòng nước nằm trên một đường thẳng. Đường thẳng đó có một vectơ chỉ phương là $\\vec{v}=\\left(%s; %s; %s\\right)$' % (v1_false, v2_false, v3_false) 
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Mặt phẳng $\\left(P\\right)$ có vectơ pháp tuyến $\\vec{n}_{P}=\\left(%s; %s; %s\\right)$. Mặt đất là mặt phẳng $\\left(Oxy\\right)$ có phương trình $z=0$, nhận $\\vec{k}=\\left(0; 0; 1\\right)$ làm vectơ pháp tuyến. \\\\
                            Gọi $d$ là giao tuyến của mặt phẳng $\\left(P\\right)$ và mặt phẳng $\\left(Oxy\\right)$. Đường thẳng $d$ có một vectơ chỉ phương là $\\vec{u}_{d} = \\left[\\vec{n}_{P}, \\vec{k}\\right] = \\left(%s; %s; 0\\right)$. \\\\
                            Dòng nước chảy theo hướng dốc nhất trên mặt phẳng $\\left(P\\right)$ nên quỹ đạo của dòng nước là một đường thẳng nằm trong mặt phẳng $\\left(P\\right)$ và vuông góc với giao tuyến $d$. \\\\
                            Vectơ chỉ phương của hướng vuông góc này là $\\vec{u}_{1} = \\left[\\vec{u}_{d}, \\vec{n}_{P}\\right] = \\left(%s; %s; %s\\right)$. \\\\
                            Vì dòng nước chảy từ trên xuống dưới đất nên cao độ của vectơ chỉ phương hướng chảy phải nhận giá trị âm. Từ $\\vec{u}_{1}$, ta điều chỉnh dấu để cao độ âm và rút gọn vectơ, ta chọn được vectơ chỉ phương của dòng nước là $\\vec{v} = \\left(%s; %s; %s\\right)$.'''
                       %(A, B, C, ud1, ud2, c1, c2, c3, v1, v2, v3
                            ))

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
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


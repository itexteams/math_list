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


def bt_dang46_p3_b6_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random các thông số của chậu cây
                a_int = random.randint(10, 20)      # Cạnh đáy lớn (1.0 đến 2.0)
                b_int = random.randint(4, 9)        # Cạnh đáy nhỏ (0.4 đến 0.9)
                while a_int <= b_int:
                    a_int = random.randint(10, 20)
                h_int = random.choice([30, 45, 60, 75, 90]) # Chiều cao (đảm bảo chia hết cho 3 khi tính toán thể tích)
                d_int = random.randint(12, 18)      # Khối lượng riêng của đất (1.2 đến 1.8)

                a = a_int / 10.0
                b = b_int / 10.0
                h = h_int / 100.0
                d = d_int / 10.0

                # Tính toán chính xác Thể tích (V) và Khối lượng (M)
                V_val = (h / 3.0) * (a**2 + b**2 + a*b)
                M_val = V_val * d

                # Định dạng các số hiển thị sang dạng chuỗi dùng dấu phẩy
                a_str = str(Decimal(str(a)).normalize()).replace('.', ',')
                b_str = str(Decimal(str(b)).normalize()).replace('.', ',')
                h_str = str(Decimal(str(h)).normalize()).replace('.', ',')
                d_str = str(Decimal(str(d)).normalize()).replace('.', ',')

                # Định dạng các kết quả trung gian
                V_str = str(Decimal(str(V_val)).quantize(Decimal('0.000001')).normalize()).replace('.', ',')
                M_str = str(Decimal(str(M_val)).quantize(Decimal('0.000001')).normalize()).replace('.', ',')

                # Làm tròn kết quả cuối cùng đến hàng phần trăm theo yêu cầu đề bài
                kq3 = Decimal(str(M_val)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                kq = str(kq3).replace('.', ',')

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(kq)]
                da = random.choice(du)

                # Tạo các phương án sai (đảm bảo không trùng nhau và không trùng đáp án đúng)
                s = []
                for offset in [0.01, -0.01, 0.1, -0.1, 1.0, -1.0, 0.05, -0.05, 0.2, -0.2, 0.5, -0.5]:
                    distractor = Decimal(str(M_val + offset)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                    s.append('$%s$' % str(distractor).replace('.', ','))

                s = list(set(s))
                if '$%s$' % kq in s:
                    s.remove('$%s$' % kq)

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                hinhve=r'''\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.41 ] (299.87,162.8) -- (259.2,204.8) -- (168.82,207.31) -- (161.87,172.8) -- (249.87,156.8) -- cycle ;
            	\draw  [fill={rgb, 255:red, 225; green, 187; blue, 152 }  ,fill opacity=1 ] (176.37,100.81) -- (168.82,207.31) -- (109.21,190.62) -- (81,88.49) -- cycle ;
            	\draw  [fill={rgb, 255:red, 225; green, 187; blue, 152 }  ,fill opacity=1 ] (233.2,80.54) -- (212.54,181.48) -- (168.82,207.31) -- (176.37,100.81) -- cycle ;
            	\draw  [fill={rgb, 255:red, 225; green, 187; blue, 152 }  ,fill opacity=1 ] (149.75,68.22) -- (233.2,80.54) -- (176.37,100.81) -- (81,88.49) -- cycle ;
            	\draw  [fill={rgb, 255:red, 109; green, 81; blue, 56 }  ,fill opacity=1 ] (150.54,71.8) -- (220.88,81.73) -- (176.37,96.83) -- (97.29,87.3) -- cycle ;
            	\draw    (164.27,45.56) .. controls (165.91,56.51) and (162.62,71.45) .. (167.55,79.49) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (168.21,41.98) .. controls (167.86,44.26) and (166.53,46.09) .. (164.77,47.06) .. controls (163.66,45.56) and (163.13,43.58) .. (163.44,41.54) .. controls (163.8,39.26) and (165.13,37.42) .. (166.89,36.45) .. controls (167.99,37.95) and (168.53,39.93) .. (168.21,41.98) -- cycle ;
            	\draw    (164.77,47.06) -- (166.89,36.45) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (169.48,51.25) .. controls (168.36,52.84) and (166.66,53.66) .. (164.95,53.63) .. controls (164.67,52) and (165,50.24) .. (166,48.82) .. controls (167.12,47.23) and (168.82,46.41) .. (170.53,46.44) .. controls (170.82,48.07) and (170.49,49.83) .. (169.48,51.25) -- cycle ;
            	\draw    (164.95,53.63) -- (170.53,46.44) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (169.86,60.13) .. controls (168.55,61.54) and (166.76,62.1) .. (165.07,61.81) .. controls (164.99,60.15) and (165.54,58.46) .. (166.72,57.2) .. controls (168.03,55.79) and (169.82,55.24) .. (171.51,55.52) .. controls (171.59,57.18) and (171.04,58.87) .. (169.86,60.13) -- cycle ;
            	\draw    (165.07,61.81) -- (171.51,55.52) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (169.21,67.03) .. controls (168.09,68.62) and (166.39,69.44) .. (164.68,69.4) .. controls (164.39,67.77) and (164.72,66.02) .. (165.73,64.59) .. controls (166.85,63) and (168.55,62.18) .. (170.26,62.22) .. controls (170.54,63.85) and (170.21,65.6) .. (169.21,67.03) -- cycle ;
            	\draw    (164.68,69.4) -- (170.26,62.22) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (170.85,74.17) .. controls (169.73,75.76) and (168.03,76.58) .. (166.32,76.55) .. controls (166.04,74.91) and (166.37,73.16) .. (167.37,71.74) .. controls (168.49,70.15) and (170.19,69.33) .. (171.9,69.36) .. controls (172.19,70.99) and (171.86,72.75) .. (170.85,74.17) -- cycle ;
            	\draw    (166.32,76.55) -- (171.9,69.36) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (162.91,46.07) .. controls (164.09,47.6) and (164.46,49.58) .. (164.06,51.39) .. controls (162.53,51.34) and (161.03,50.61) .. (159.97,49.24) .. controls (158.78,47.71) and (158.41,45.72) .. (158.81,43.92) .. controls (160.34,43.97) and (161.84,44.7) .. (162.91,46.07) -- cycle ;
            	\draw    (164.06,51.39) -- (158.81,43.92) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (163.08,52.52) .. controls (164.36,53.96) and (164.85,55.91) .. (164.56,57.75) .. controls (163.03,57.8) and (161.48,57.18) .. (160.34,55.89) .. controls (159.06,54.44) and (158.57,52.49) .. (158.87,50.66) .. controls (160.4,50.6) and (161.94,51.22) .. (163.08,52.52) -- cycle ;
            	\draw    (164.56,57.75) -- (158.87,50.66) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (162.54,59.07) .. controls (163.81,60.51) and (164.3,62.46) .. (164.01,64.29) .. controls (162.48,64.35) and (160.93,63.73) .. (159.79,62.43) .. controls (158.51,60.99) and (158.03,59.04) .. (158.32,57.21) .. controls (159.85,57.15) and (161.39,57.77) .. (162.54,59.07) -- cycle ;
            	\draw    (164.01,64.29) -- (158.32,57.21) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (163.08,66.51) .. controls (164.36,67.95) and (164.85,69.9) .. (164.56,71.73) .. controls (163.03,71.79) and (161.48,71.17) .. (160.34,69.87) .. controls (159.06,68.43) and (158.57,66.48) .. (158.87,64.65) .. controls (160.4,64.59) and (161.94,65.21) .. (163.08,66.51) -- cycle ;
            	\draw    (164.56,71.73) -- (158.87,64.65) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (165.28,74.84) .. controls (166.55,76.28) and (167.04,78.24) .. (166.75,80.07) .. controls (165.22,80.13) and (163.67,79.5) .. (162.53,78.21) .. controls (161.25,76.76) and (160.77,74.81) .. (161.06,72.98) .. controls (162.59,72.92) and (164.13,73.55) .. (165.28,74.84) -- cycle ;
            	\draw    (166.75,80.07) -- (161.06,72.98) ;
            	\draw    (134.25,36.43) .. controls (136.63,51.05) and (131.87,71) .. (139.02,81.73) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (139.97,31.65) .. controls (139.46,34.7) and (137.53,37.15) .. (134.98,38.44) .. controls (133.38,36.44) and (132.6,33.79) .. (133.06,31.06) .. controls (133.57,28.02) and (135.5,25.56) .. (138.05,24.27) .. controls (139.66,26.27) and (140.43,28.92) .. (139.97,31.65) -- cycle ;
            	\draw    (134.98,38.44) -- (138.05,24.27) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (141.81,44.03) .. controls (140.19,46.16) and (137.72,47.25) .. (135.24,47.21) .. controls (134.83,45.03) and (135.31,42.69) .. (136.77,40.78) .. controls (138.39,38.66) and (140.86,37.57) .. (143.34,37.61) .. controls (143.75,39.79) and (143.27,42.13) .. (141.81,44.03) -- cycle ;
            	\draw    (135.24,47.21) -- (143.34,37.61) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (142.36,55.89) .. controls (140.46,57.77) and (137.87,58.52) .. (135.42,58.13) .. controls (135.31,55.92) and (136.1,53.66) .. (137.81,51.98) .. controls (139.7,50.1) and (142.3,49.35) .. (144.75,49.73) .. controls (144.86,51.95) and (144.06,54.21) .. (142.36,55.89) -- cycle ;
            	\draw    (135.42,58.13) -- (144.75,49.73) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (141.42,65.1) .. controls (139.79,67.22) and (137.33,68.31) .. (134.85,68.27) .. controls (134.43,66.09) and (134.91,63.75) .. (136.37,61.85) .. controls (137.99,59.72) and (140.46,58.63) .. (142.94,58.67) .. controls (143.35,60.85) and (142.87,63.19) .. (141.42,65.1) -- cycle ;
            	\draw    (134.85,68.27) -- (142.94,58.67) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (143.8,74.63) .. controls (142.18,76.76) and (139.71,77.85) .. (137.23,77.81) .. controls (136.82,75.63) and (137.3,73.29) .. (138.75,71.38) .. controls (140.37,69.26) and (142.84,68.17) .. (145.32,68.21) .. controls (145.74,70.39) and (145.26,72.73) .. (143.8,74.63) -- cycle ;
            	\draw    (137.23,77.81) -- (145.32,68.21) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (132.28,37.12) .. controls (134,39.16) and (134.54,41.81) .. (133.96,44.22) .. controls (131.74,44.15) and (129.56,43.18) .. (128.02,41.34) .. controls (126.3,39.3) and (125.76,36.65) .. (126.34,34.24) .. controls (128.56,34.31) and (130.74,35.29) .. (132.28,37.12) -- cycle ;
            	\draw    (133.96,44.22) -- (126.34,34.24) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (132.54,45.73) .. controls (134.39,47.65) and (135.09,50.26) .. (134.67,52.7) .. controls (132.45,52.78) and (130.21,51.95) .. (128.56,50.22) .. controls (126.71,48.29) and (126,45.69) .. (126.42,43.24) .. controls (128.64,43.17) and (130.88,44) .. (132.54,45.73) -- cycle ;
            	\draw    (134.67,52.7) -- (126.42,43.24) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (131.74,54.47) .. controls (133.59,56.4) and (134.3,59) .. (133.88,61.45) .. controls (131.66,61.52) and (129.42,60.69) .. (127.76,58.96) .. controls (125.91,57.03) and (125.21,54.43) .. (125.63,51.98) .. controls (127.85,51.91) and (130.09,52.74) .. (131.74,54.47) -- cycle ;
            	\draw    (133.88,61.45) -- (125.63,51.98) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (132.54,64.4) .. controls (134.39,66.33) and (135.09,68.94) .. (134.67,71.38) .. controls (132.45,71.46) and (130.21,70.63) .. (128.56,68.9) .. controls (126.71,66.97) and (126,64.36) .. (126.42,61.92) .. controls (128.64,61.84) and (130.88,62.67) .. (132.54,64.4) -- cycle ;
            	\draw    (134.67,71.38) -- (126.42,61.92) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (135.72,75.53) .. controls (137.57,77.46) and (138.27,80.06) .. (137.85,82.51) .. controls (135.63,82.58) and (133.39,81.75) .. (131.73,80.02) .. controls (129.89,78.1) and (129.18,75.49) .. (129.6,73.05) .. controls (131.82,72.97) and (134.06,73.8) .. (135.72,75.53) -- cycle ;
            	\draw    (137.85,82.51) -- (129.6,73.05) ;
            	\draw    (151.42,53.87) .. controls (156.33,61.68) and (158.82,74.19) .. (165.27,78.68) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (153.23,49.81) .. controls (153.73,51.67) and (153.33,53.52) .. (152.3,54.85) .. controls (150.96,54.07) and (149.89,52.73) .. (149.44,51.07) .. controls (148.95,49.21) and (149.35,47.36) .. (150.38,46.03) .. controls (151.72,46.81) and (152.79,48.15) .. (153.23,49.81) -- cycle ;
            	\draw    (152.3,54.85) -- (150.38,46.03) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (157.31,56.47) .. controls (156.98,58.06) and (155.96,59.26) .. (154.64,59.8) .. controls (153.87,58.65) and (153.54,57.2) .. (153.83,55.78) .. controls (154.16,54.19) and (155.18,52.99) .. (156.5,52.45) .. controls (157.26,53.6) and (157.6,55.05) .. (157.31,56.47) -- cycle ;
            	\draw    (154.64,59.8) -- (156.5,52.45) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (160.56,63.13) .. controls (160.03,64.64) and (158.85,65.67) .. (157.47,66.01) .. controls (156.85,64.77) and (156.71,63.3) .. (157.18,61.94) .. controls (157.71,60.43) and (158.89,59.4) .. (160.28,59.05) .. controls (160.89,60.3) and (161.04,61.77) .. (160.56,63.13) -- cycle ;
            	\draw    (157.47,66.01) -- (160.28,59.05) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (162.37,68.61) .. controls (162.05,70.2) and (161.02,71.4) .. (159.7,71.94) .. controls (158.94,70.79) and (158.61,69.34) .. (158.9,67.92) .. controls (159.22,66.33) and (160.25,65.13) .. (161.56,64.59) .. controls (162.33,65.74) and (162.66,67.19) .. (162.37,68.61) -- cycle ;
            	\draw    (159.7,71.94) -- (161.56,64.59) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (166.01,73.52) .. controls (165.69,75.11) and (164.67,76.3) .. (163.35,76.85) .. controls (162.58,75.7) and (162.25,74.25) .. (162.54,72.82) .. controls (162.86,71.23) and (163.89,70.04) .. (165.21,69.49) .. controls (165.97,70.64) and (166.31,72.09) .. (166.01,73.52) -- cycle ;
            	\draw    (163.35,76.85) -- (165.21,69.49) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (150.55,54.71) .. controls (151.97,55.49) and (152.91,56.88) .. (153.21,58.39) .. controls (152.03,58.86) and (150.63,58.81) .. (149.36,58.11) .. controls (147.94,57.34) and (147,55.95) .. (146.7,54.44) .. controls (147.89,53.96) and (149.28,54.02) .. (150.55,54.71) -- cycle ;
            	\draw    (153.21,58.39) -- (146.7,54.44) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (152.84,59.58) .. controls (154.3,60.25) and (155.32,61.58) .. (155.71,63.08) .. controls (154.56,63.63) and (153.18,63.67) .. (151.87,63.07) .. controls (150.41,62.39) and (149.39,61.06) .. (149,59.57) .. controls (150.15,59.01) and (151.54,58.97) .. (152.84,59.58) -- cycle ;
            	\draw    (155.71,63.08) -- (149,59.57) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (154.61,64.76) .. controls (156.07,65.44) and (157.09,66.77) .. (157.48,68.26) .. controls (156.33,68.82) and (154.95,68.86) .. (153.64,68.25) .. controls (152.18,67.58) and (151.16,66.25) .. (150.77,64.75) .. controls (151.92,64.2) and (153.31,64.16) .. (154.61,64.76) -- cycle ;
            	\draw    (157.48,68.26) -- (150.77,64.75) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (157.52,70.26) .. controls (158.98,70.94) and (160,72.27) .. (160.39,73.76) .. controls (159.24,74.32) and (157.85,74.36) .. (156.55,73.75) .. controls (155.09,73.08) and (154.06,71.75) .. (153.67,70.25) .. controls (154.82,69.7) and (156.21,69.66) .. (157.52,70.26) -- cycle ;
            	\draw    (160.39,73.76) -- (153.67,70.25) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (161.98,75.89) .. controls (163.44,76.57) and (164.46,77.9) .. (164.85,79.4) .. controls (163.7,79.95) and (162.31,79.99) .. (161.01,79.38) .. controls (159.55,78.71) and (158.53,77.38) .. (158.14,75.88) .. controls (159.29,75.33) and (160.67,75.29) .. (161.98,75.89) -- cycle ;
            	\draw    (164.85,79.39) -- (158.14,75.88) ;
            	\draw    (181.88,44.58) .. controls (176.94,55.62) and (176.31,72.32) .. (168.57,79.3) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (178.54,39.64) .. controls (178.28,42.14) and (179.23,44.47) .. (180.9,46.02) .. controls (182.54,44.77) and (183.7,42.84) .. (183.93,40.6) .. controls (184.19,38.09) and (183.25,35.76) .. (181.58,34.21) .. controls (179.93,35.46) and (178.78,37.39) .. (178.54,39.64) -- cycle ;
            	\draw    (180.9,46.02) -- (181.58,34.21) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (174.5,49.02) .. controls (175.28,51.02) and (176.92,52.4) .. (178.82,52.87) .. controls (179.6,51.24) and (179.73,49.3) .. (179.03,47.5) .. controls (178.25,45.49) and (176.61,44.12) .. (174.71,43.64) .. controls (173.93,45.27) and (173.8,47.22) .. (174.5,49.02) -- cycle ;
            	\draw    (178.82,52.87) -- (174.71,43.64) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (171.55,58.25) .. controls (172.59,60.12) and (174.41,61.24) .. (176.35,61.45) .. controls (176.91,59.72) and (176.79,57.78) .. (175.85,56.1) .. controls (174.81,54.23) and (172.99,53.11) .. (171.04,52.9) .. controls (170.49,54.63) and (170.61,56.57) .. (171.55,58.25) -- cycle ;
            	\draw    (176.35,61.45) -- (171.04,52.9) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (170.3,65.7) .. controls (171.08,67.71) and (172.73,69.08) .. (174.62,69.56) .. controls (175.41,67.92) and (175.54,65.98) .. (174.84,64.18) .. controls (174.06,62.17) and (172.41,60.8) .. (170.52,60.32) .. controls (169.73,61.95) and (169.6,63.9) .. (170.3,65.7) -- cycle ;
            	\draw    (174.63,69.56) -- (170.51,60.32) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (166.45,72.72) .. controls (167.23,74.73) and (168.88,76.1) .. (170.77,76.58) .. controls (171.55,74.95) and (171.69,73) .. (170.99,71.2) .. controls (170.2,69.2) and (168.56,67.82) .. (166.66,67.35) .. controls (165.88,68.98) and (165.75,70.92) .. (166.45,72.72) -- cycle ;
            	\draw    (170.77,76.58) -- (166.66,67.35) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (183.23,45.53) .. controls (181.48,46.79) and (180.51,48.76) .. (180.44,50.78) .. controls (182.14,51.19) and (184.01,50.87) .. (185.57,49.74) .. controls (187.32,48.49) and (188.29,46.51) .. (188.37,44.49) .. controls (186.66,44.09) and (184.79,44.41) .. (183.23,45.53) -- cycle ;
            	\draw    (180.44,50.78) -- (188.37,44.49) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (181.2,52.26) .. controls (179.38,53.4) and (178.28,55.31) .. (178.08,57.32) .. controls (179.75,57.84) and (181.64,57.65) .. (183.27,56.63) .. controls (185.09,55.49) and (186.18,53.58) .. (186.38,51.57) .. controls (184.71,51.05) and (182.83,51.24) .. (181.2,52.26) -- cycle ;
            	\draw    (178.08,57.32) -- (186.38,51.57) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (179.93,59.32) .. controls (178.11,60.46) and (177.02,62.36) .. (176.82,64.38) .. controls (178.49,64.9) and (180.37,64.7) .. (182.01,63.68) .. controls (183.83,62.54) and (184.92,60.63) .. (185.12,58.62) .. controls (183.45,58.1) and (181.56,58.3) .. (179.93,59.32) -- cycle ;
            	\draw    (176.82,64.38) -- (185.12,58.62) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (177.21,66.98) .. controls (175.39,68.12) and (174.29,70.03) .. (174.09,72.04) .. controls (175.77,72.56) and (177.65,72.37) .. (179.28,71.35) .. controls (181.1,70.21) and (182.19,68.3) .. (182.39,66.29) .. controls (180.72,65.77) and (178.84,65.96) .. (177.21,66.98) -- cycle ;
            	\draw    (174.09,72.04) -- (182.39,66.29) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (172.41,75.1) .. controls (170.59,76.24) and (169.5,78.14) .. (169.3,80.16) .. controls (170.97,80.67) and (172.85,80.48) .. (174.48,79.46) .. controls (176.3,78.32) and (177.4,76.41) .. (177.6,74.4) .. controls (175.93,73.88) and (174.04,74.08) .. (172.41,75.1) -- cycle ;
            	\draw    (169.3,80.16) -- (177.6,74.4) ;
            	\draw    (190.44,59.12) .. controls (186.24,65.3) and (184.05,75.39) .. (178.58,78.8) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (188.94,55.75) .. controls (188.51,57.24) and (188.84,58.76) .. (189.68,59.88) .. controls (190.82,59.3) and (191.73,58.25) .. (192.12,56.91) .. controls (192.55,55.42) and (192.23,53.9) .. (191.38,52.77) .. controls (190.24,53.36) and (189.33,54.41) .. (188.94,55.75) -- cycle ;
            	\draw    (189.68,59.88) -- (191.38,52.77) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (185.47,61.02) .. controls (185.73,62.32) and (186.58,63.33) .. (187.68,63.83) .. controls (188.33,62.92) and (188.62,61.75) .. (188.39,60.58) .. controls (188.13,59.28) and (187.28,58.26) .. (186.18,57.77) .. controls (185.53,58.68) and (185.23,59.84) .. (185.47,61.02) -- cycle ;
            	\draw    (187.68,63.83) -- (186.18,57.77) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (182.67,66.31) .. controls (183.1,67.56) and (184.09,68.44) .. (185.25,68.78) .. controls (185.78,67.79) and (185.91,66.6) .. (185.52,65.47) .. controls (185.09,64.22) and (184.11,63.34) .. (182.94,63.01) .. controls (182.42,64) and (182.28,65.19) .. (182.67,66.31) -- cycle ;
            	\draw    (185.25,68.78) -- (182.95,63.01) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (181.11,70.71) .. controls (181.37,72.02) and (182.22,73.03) .. (183.32,73.53) .. controls (183.97,72.62) and (184.27,71.45) .. (184.03,70.28) .. controls (183.77,68.97) and (182.92,67.96) .. (181.82,67.46) .. controls (181.17,68.37) and (180.88,69.54) .. (181.11,70.71) -- cycle ;
            	\draw    (183.32,73.53) -- (181.82,67.46) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (178,74.57) .. controls (178.26,75.87) and (179.11,76.89) .. (180.22,77.38) .. controls (180.87,76.47) and (181.16,75.31) .. (180.93,74.13) .. controls (180.67,72.83) and (179.82,71.82) .. (178.72,71.32) .. controls (178.06,72.23) and (177.77,73.4) .. (178,74.57) -- cycle ;
            	\draw    (180.22,77.38) -- (178.72,71.32) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (191.16,59.84) .. controls (189.96,60.41) and (189.15,61.51) .. (188.89,62.73) .. controls (189.88,63.16) and (191.05,63.17) .. (192.13,62.66) .. controls (193.33,62.08) and (194.13,60.98) .. (194.4,59.76) .. controls (193.4,59.33) and (192.23,59.32) .. (191.16,59.84) -- cycle ;
            	\draw    (188.89,62.73) -- (194.4,59.76) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (189.19,63.72) .. controls (187.96,64.21) and (187.09,65.25) .. (186.75,66.46) .. controls (187.71,66.95) and (188.88,67.04) .. (189.98,66.6) .. controls (191.21,66.1) and (192.08,65.06) .. (192.42,63.85) .. controls (191.46,63.36) and (190.29,63.27) .. (189.19,63.72) -- cycle ;
            	\draw    (186.75,66.46) -- (192.42,63.85) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (187.66,67.87) .. controls (186.43,68.37) and (185.56,69.41) .. (185.22,70.61) .. controls (186.18,71.11) and (187.35,71.2) .. (188.45,70.75) .. controls (189.68,70.26) and (190.55,69.21) .. (190.89,68.01) .. controls (189.93,67.51) and (188.76,67.43) .. (187.66,67.87) -- cycle ;
            	\draw    (185.22,70.61) -- (190.89,68.01) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (185.17,72.24) .. controls (183.94,72.74) and (183.07,73.78) .. (182.73,74.98) .. controls (183.69,75.48) and (184.86,75.56) .. (185.96,75.12) .. controls (187.19,74.62) and (188.06,73.58) .. (188.4,72.38) .. controls (187.44,71.88) and (186.27,71.8) .. (185.17,72.24) -- cycle ;
            	\draw    (182.73,74.98) -- (188.4,72.38) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (181.37,76.66) .. controls (180.14,77.15) and (179.27,78.2) .. (178.93,79.4) .. controls (179.89,79.9) and (181.06,79.98) .. (182.16,79.54) .. controls (183.39,79.04) and (184.26,78) .. (184.61,76.8) .. controls (183.64,76.3) and (182.48,76.21) .. (181.37,76.66) -- cycle ;
            	\draw    (178.93,79.4) -- (184.61,76.8) ;
            	\draw    (117.83,47.69) .. controls (119.2,58.93) and (126.16,72.89) .. (123.72,82.05) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (113.25,45.12) .. controls (114.18,47.29) and (115.89,48.78) .. (117.77,49.31) .. controls (118.39,47.55) and (118.36,45.46) .. (117.53,43.52) .. controls (116.61,41.35) and (114.9,39.86) .. (113.02,39.33) .. controls (112.4,41.09) and (112.43,43.18) .. (113.25,45.12) -- cycle ;
            	\draw    (117.77,49.31) -- (113.02,39.33) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (114.52,54.6) .. controls (115.97,55.9) and (117.76,56.29) .. (119.33,55.84) .. controls (119.16,54.16) and (118.39,52.51) .. (117.09,51.34) .. controls (115.64,50.05) and (113.86,49.65) .. (112.29,50.1) .. controls (112.45,51.79) and (113.22,53.44) .. (114.52,54.6) -- cycle ;
            	\draw    (119.32,55.84) -- (112.29,50.1) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (116.51,63.48) .. controls (118.08,64.55) and (119.88,64.66) .. (121.36,63.96) .. controls (121,62.3) and (120.05,60.77) .. (118.63,59.81) .. controls (117.06,58.74) and (115.26,58.62) .. (113.78,59.32) .. controls (114.14,60.98) and (115.09,62.52) .. (116.51,63.48) -- cycle ;
            	\draw    (121.36,63.96) -- (113.78,59.32) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (118.92,70.13) .. controls (120.37,71.43) and (122.16,71.82) .. (123.72,71.37) .. controls (123.56,69.69) and (122.79,68.04) .. (121.49,66.87) .. controls (120.04,65.58) and (118.26,65.18) .. (116.69,65.63) .. controls (116.85,67.32) and (117.62,68.97) .. (118.92,70.13) -- cycle ;
            	\draw    (123.72,71.37) -- (116.69,65.63) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (119.28,77.6) .. controls (120.73,78.9) and (122.52,79.29) .. (124.09,78.84) .. controls (123.92,77.15) and (123.15,75.5) .. (121.85,74.34) .. controls (120.4,73.04) and (118.62,72.65) .. (117.05,73.1) .. controls (117.22,74.78) and (117.98,76.44) .. (119.28,77.6) -- cycle ;
            	\draw    (124.09,78.84) -- (117.05,73.1) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (119.22,47.87) .. controls (118.53,49.67) and (118.71,51.72) .. (119.55,53.41) .. controls (120.95,52.99) and (122.15,51.9) .. (122.77,50.28) .. controls (123.46,48.47) and (123.28,46.42) .. (122.43,44.73) .. controls (121.04,45.16) and (119.84,46.25) .. (119.22,47.87) -- cycle ;
            	\draw    (119.55,53.41) -- (122.43,44.73) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (120.75,54.29) .. controls (119.96,56.03) and (120.02,58.08) .. (120.77,59.82) .. controls (122.2,59.5) and (123.46,58.5) .. (124.17,56.94) .. controls (124.97,55.2) and (124.9,53.15) .. (124.15,51.41) .. controls (122.73,51.73) and (121.47,52.73) .. (120.75,54.29) -- cycle ;
            	\draw    (120.77,59.82) -- (124.15,51.41) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (122.98,60.63) .. controls (122.18,62.37) and (122.25,64.42) .. (123,66.16) .. controls (124.42,65.84) and (125.68,64.84) .. (126.4,63.28) .. controls (127.19,61.54) and (127.13,59.49) .. (126.38,57.75) .. controls (124.96,58.07) and (123.69,59.07) .. (122.98,60.63) -- cycle ;
            	\draw    (123,66.16) -- (126.38,57.75) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (124.43,68.12) .. controls (123.63,69.86) and (123.7,71.91) .. (124.45,73.65) .. controls (125.87,73.33) and (127.13,72.33) .. (127.85,70.77) .. controls (128.65,69.03) and (128.58,66.98) .. (127.83,65.24) .. controls (126.41,65.56) and (125.14,66.56) .. (124.43,68.12) -- cycle ;
            	\draw    (124.45,73.65) -- (127.83,65.24) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (124.6,76.9) .. controls (123.8,78.64) and (123.87,80.69) .. (124.62,82.43) .. controls (126.04,82.11) and (127.3,81.11) .. (128.02,79.55) .. controls (128.81,77.81) and (128.75,75.76) .. (128,74.02) .. controls (126.57,74.34) and (125.31,75.34) .. (124.6,76.9) -- cycle ;
            	\draw    (124.62,82.42) -- (128,74.02) ;
            	\draw    (104.24,54.53) .. controls (108.72,63.68) and (118.76,73.49) .. (119.39,82) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (99.59,53.7) .. controls (101.01,55.27) and (102.91,56.03) .. (104.66,55.92) .. controls (104.67,54.25) and (104.03,52.47) .. (102.75,51.07) .. controls (101.33,49.5) and (99.43,48.74) .. (97.68,48.84) .. controls (97.67,50.52) and (98.31,52.29) .. (99.59,53.7) -- cycle ;
            	\draw    (104.66,55.92) -- (97.68,48.84) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (103.47,61.38) .. controls (105.08,62.06) and (106.71,61.87) .. (107.92,61.02) .. controls (107.28,59.64) and (106.14,58.46) .. (104.69,57.85) .. controls (103.07,57.18) and (101.44,57.37) .. (100.24,58.22) .. controls (100.88,59.6) and (102.02,60.78) .. (103.47,61.38) -- cycle ;
            	\draw    (107.92,61.02) -- (100.24,58.22) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (107.77,68.34) .. controls (109.43,68.78) and (110.99,68.35) .. (112.05,67.32) .. controls (111.25,66.01) and (109.98,64.99) .. (108.5,64.59) .. controls (106.84,64.15) and (105.28,64.58) .. (104.23,65.61) .. controls (105.03,66.92) and (106.29,67.94) .. (107.77,68.34) -- cycle ;
            	\draw    (112.05,67.32) -- (104.23,65.61) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (111.79,73.29) .. controls (113.41,73.96) and (115.04,73.77) .. (116.24,72.92) .. controls (115.6,71.54) and (114.46,70.36) .. (113.02,69.75) .. controls (111.4,69.08) and (109.77,69.27) .. (108.57,70.12) .. controls (109.2,71.5) and (110.34,72.68) .. (111.79,73.29) -- cycle ;
            	\draw    (116.24,72.92) -- (108.57,70.12) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (114.31,79.53) .. controls (115.92,80.2) and (117.55,80.01) .. (118.76,79.16) .. controls (118.12,77.78) and (116.98,76.6) .. (115.53,75.99) .. controls (113.91,75.32) and (112.28,75.51) .. (111.08,76.36) .. controls (111.72,77.74) and (112.86,78.92) .. (114.31,79.53) -- cycle ;
            	\draw    (118.76,79.16) -- (111.08,76.36) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (105.47,54.27) .. controls (105.42,56.01) and (106.18,57.7) .. (107.39,58.88) .. controls (108.45,58.11) and (109.15,56.83) .. (109.2,55.27) .. controls (109.25,53.53) and (108.49,51.84) .. (107.28,50.66) .. controls (106.21,51.43) and (105.52,52.71) .. (105.47,54.27) -- cycle ;
            	\draw    (107.39,58.88) -- (107.28,50.66) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (108.67,59.27) .. controls (108.51,60.99) and (109.17,62.71) .. (110.32,63.97) .. controls (111.44,63.28) and (112.21,62.06) .. (112.36,60.52) .. controls (112.52,58.81) and (111.86,57.08) .. (110.71,55.83) .. controls (109.59,56.52) and (108.82,57.74) .. (108.67,59.27) -- cycle ;
            	\draw    (110.32,63.97) -- (110.71,55.83) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (112.44,64.01) .. controls (112.27,65.72) and (112.93,67.44) .. (114.08,68.7) .. controls (115.2,68.01) and (115.98,66.79) .. (116.13,65.25) .. controls (116.29,63.54) and (115.63,61.82) .. (114.48,60.56) .. controls (113.36,61.25) and (112.58,62.47) .. (112.44,64.01) -- cycle ;
            	\draw    (114.08,68.7) -- (114.48,60.56) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (115.88,69.95) .. controls (115.72,71.66) and (116.38,73.38) .. (117.53,74.64) .. controls (118.65,73.95) and (119.43,72.73) .. (119.57,71.19) .. controls (119.73,69.48) and (119.07,67.76) .. (117.92,66.5) .. controls (116.81,67.19) and (116.03,68.41) .. (115.88,69.95) -- cycle ;
            	\draw    (117.53,74.64) -- (117.92,66.5) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (118.62,77.36) .. controls (118.46,79.07) and (119.12,80.8) .. (120.27,82.05) .. controls (121.38,81.36) and (122.16,80.14) .. (122.31,78.6) .. controls (122.47,76.89) and (121.81,75.17) .. (120.66,73.91) .. controls (119.54,74.6) and (118.76,75.82) .. (118.62,77.36) -- cycle ;
            	\draw    (120.27,82.05) -- (120.66,73.91) ;
            	\draw    (205.93,63.51) .. controls (205.32,69.97) and (201.1,77.89) .. (202.94,83.23) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (208.88,62.12) .. controls (208.33,63.35) and (207.24,64.17) .. (206.01,64.44) .. controls (205.56,63.42) and (205.52,62.21) .. (206.02,61.1) .. controls (206.57,59.87) and (207.66,59.04) .. (208.88,58.78) .. controls (209.34,59.8) and (209.37,61.01) .. (208.88,62.12) -- cycle ;
            	\draw    (206.01,64.44) -- (208.88,58.78) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (208.29,67.57) .. controls (207.37,68.29) and (206.2,68.48) .. (205.16,68.18) .. controls (205.22,67.22) and (205.68,66.28) .. (206.51,65.63) .. controls (207.43,64.91) and (208.6,64.72) .. (209.65,65.01) .. controls (209.58,65.98) and (209.12,66.92) .. (208.29,67.57) -- cycle ;
            	\draw    (205.16,68.18) -- (209.65,65.01) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (207.21,72.65) .. controls (206.2,73.24) and (205.02,73.27) .. (204.02,72.83) .. controls (204.22,71.88) and (204.81,71.01) .. (205.72,70.49) .. controls (206.73,69.9) and (207.91,69.87) .. (208.91,70.31) .. controls (208.71,71.26) and (208.12,72.12) .. (207.21,72.65) -- cycle ;
            	\draw    (204.02,72.83) -- (208.91,70.31) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (205.8,76.45) .. controls (204.87,77.17) and (203.71,77.36) .. (202.66,77.06) .. controls (202.73,76.09) and (203.19,75.16) .. (204.02,74.51) .. controls (204.94,73.79) and (206.1,73.6) .. (207.15,73.89) .. controls (207.08,74.86) and (206.62,75.8) .. (205.8,76.45) -- cycle ;
            	\draw    (202.66,77.06) -- (207.15,73.89) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (205.75,80.75) .. controls (204.83,81.47) and (203.66,81.66) .. (202.62,81.37) .. controls (202.68,80.4) and (203.14,79.46) .. (203.97,78.81) .. controls (204.89,78.09) and (206.06,77.9) .. (207.11,78.2) .. controls (207.04,79.17) and (206.58,80.1) .. (205.75,80.75) -- cycle ;
            	\draw    (202.62,81.37) -- (207.11,78.2) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (205.02,63.58) .. controls (205.52,64.64) and (205.45,65.82) .. (204.94,66.78) .. controls (204.01,66.5) and (203.19,65.85) .. (202.74,64.9) .. controls (202.24,63.85) and (202.31,62.66) .. (202.82,61.71) .. controls (203.75,61.98) and (204.57,62.64) .. (205.02,63.58) -- cycle ;
            	\draw    (204.94,66.78) -- (202.82,61.71) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (204.17,67.26) .. controls (204.74,68.28) and (204.76,69.46) .. (204.31,70.45) .. controls (203.36,70.24) and (202.5,69.64) .. (201.99,68.72) .. controls (201.42,67.7) and (201.41,66.52) .. (201.86,65.53) .. controls (202.81,65.74) and (203.66,66.34) .. (204.17,67.26) -- cycle ;
            	\draw    (204.31,70.45) -- (201.86,65.53) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (202.87,70.87) .. controls (203.44,71.89) and (203.45,73.08) .. (203,74.07) .. controls (202.06,73.85) and (201.2,73.25) .. (200.69,72.34) .. controls (200.12,71.32) and (200.11,70.13) .. (200.55,69.15) .. controls (201.5,69.36) and (202.36,69.96) .. (202.87,70.87) -- cycle ;
            	\draw    (203,74.07) -- (200.55,69.15) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (202.11,75.17) .. controls (202.68,76.19) and (202.69,77.37) .. (202.24,78.36) .. controls (201.29,78.15) and (200.44,77.55) .. (199.93,76.63) .. controls (199.36,75.61) and (199.34,74.43) .. (199.79,73.44) .. controls (200.74,73.66) and (201.6,74.26) .. (202.11,75.17) -- cycle ;
            	\draw    (202.24,78.36) -- (199.79,73.44) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (202.23,80.24) .. controls (202.8,81.26) and (202.81,82.44) .. (202.36,83.43) .. controls (201.41,83.22) and (200.55,82.62) .. (200.04,81.7) .. controls (199.47,80.68) and (199.46,79.5) .. (199.91,78.51) .. controls (200.86,78.72) and (201.72,79.32) .. (202.23,80.24) -- cycle ;
            	\draw    (202.36,83.43) -- (199.91,78.51) ;
            	\draw    (214.63,69.16) .. controls (213.23,74.21) and (208.75,79.9) .. (209.45,84.4) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (217.18,68.48) .. controls (216.56,69.38) and (215.58,69.88) .. (214.57,69.92) .. controls (214.35,69.04) and (214.49,68.07) .. (215.05,67.26) .. controls (215.66,66.36) and (216.64,65.86) .. (217.65,65.82) .. controls (217.87,66.7) and (217.73,67.67) .. (217.18,68.48) -- cycle ;
            	\draw    (214.57,69.92) -- (217.65,65.82) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (215.93,72.72) .. controls (215.1,73.16) and (214.14,73.15) .. (213.35,72.77) .. controls (213.54,72.01) and (214.05,71.33) .. (214.79,70.93) .. controls (215.63,70.49) and (216.58,70.51) .. (217.37,70.89) .. controls (217.18,71.65) and (216.68,72.33) .. (215.93,72.72) -- cycle ;
            	\draw    (213.35,72.77) -- (217.37,70.89) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (214.35,76.61) .. controls (213.47,76.93) and (212.52,76.78) .. (211.79,76.3) .. controls (212.09,75.57) and (212.67,74.97) .. (213.47,74.68) .. controls (214.36,74.36) and (215.3,74.5) .. (216.03,74.99) .. controls (215.74,75.71) and (215.15,76.32) .. (214.35,76.61) -- cycle ;
            	\draw    (211.79,76.3) -- (216.03,74.99) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (212.69,79.42) .. controls (211.85,79.86) and (210.9,79.85) .. (210.11,79.47) .. controls (210.3,78.7) and (210.8,78.02) .. (211.55,77.63) .. controls (212.38,77.19) and (213.34,77.2) .. (214.13,77.58) .. controls (213.93,78.35) and (213.43,79.03) .. (212.69,79.42) -- cycle ;
            	\draw    (210.11,79.47) -- (214.13,77.58) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (212.04,82.83) .. controls (211.2,83.27) and (210.25,83.26) .. (209.46,82.88) .. controls (209.65,82.12) and (210.15,81.44) .. (210.9,81.04) .. controls (211.73,80.6) and (212.69,80.62) .. (213.48,81) .. controls (213.29,81.76) and (212.79,82.44) .. (212.04,82.83) -- cycle ;
            	\draw    (209.46,82.88) -- (213.48,81) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (213.9,69.09) .. controls (214.15,70) and (213.93,70.93) .. (213.38,71.62) .. controls (212.68,71.27) and (212.13,70.63) .. (211.9,69.82) .. controls (211.66,68.91) and (211.88,67.98) .. (212.42,67.29) .. controls (213.12,67.64) and (213.68,68.28) .. (213.9,69.09) -- cycle ;
            	\draw    (213.38,71.62) -- (212.42,67.29) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (212.71,71.89) .. controls (213.01,72.78) and (212.85,73.72) .. (212.36,74.45) .. controls (211.63,74.14) and (211.04,73.54) .. (210.76,72.74) .. controls (210.45,71.85) and (210.61,70.91) .. (211.11,70.19) .. controls (211.83,70.49) and (212.43,71.09) .. (212.71,71.89) -- cycle ;
            	\draw    (212.36,74.45) -- (211.11,70.19) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (211.16,74.58) .. controls (211.46,75.47) and (211.3,76.41) .. (210.81,77.13) .. controls (210.08,76.83) and (209.49,76.23) .. (209.21,75.43) .. controls (208.91,74.54) and (209.06,73.6) .. (209.56,72.88) .. controls (210.28,73.18) and (210.88,73.78) .. (211.16,74.58) -- cycle ;
            	\draw    (210.81,77.13) -- (209.56,72.88) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (209.94,77.88) .. controls (210.25,78.78) and (210.09,79.72) .. (209.59,80.44) .. controls (208.87,80.13) and (208.27,79.54) .. (208,78.74) .. controls (207.69,77.84) and (207.85,76.9) .. (208.35,76.18) .. controls (209.07,76.48) and (209.66,77.08) .. (209.94,77.88) -- cycle ;
            	\draw    (209.59,80.44) -- (208.35,76.18) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (209.31,81.92) .. controls (209.62,82.82) and (209.46,83.76) .. (208.96,84.48) .. controls (208.24,84.17) and (207.64,83.58) .. (207.37,82.78) .. controls (207.06,81.88) and (207.22,80.94) .. (207.72,80.22) .. controls (208.44,80.53) and (209.04,81.12) .. (209.31,81.92) -- cycle ;
            	\draw    (208.96,84.48) -- (207.72,80.22) ;
            	\draw    (196.41,67.75) .. controls (195.47,72.68) and (197.67,79.33) .. (194.64,83) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (193.89,66.19) .. controls (194.14,67.21) and (194.99,68.02) .. (196.1,68.43) .. controls (196.78,67.74) and (197.1,66.85) .. (196.89,65.93) .. controls (196.64,64.92) and (195.79,64.11) .. (194.68,63.7) .. controls (194,64.38) and (193.68,65.28) .. (193.89,66.19) -- cycle ;
            	\draw    (196.1,68.43) -- (194.68,63.7) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (193.18,70.36) .. controls (193.9,71.06) and (194.97,71.41) .. (196.05,71.37) .. controls (196.21,70.64) and (195.99,69.86) .. (195.34,69.23) .. controls (194.63,68.53) and (193.55,68.19) .. (192.48,68.22) .. controls (192.31,68.96) and (192.54,69.74) .. (193.18,70.36) -- cycle ;
            	\draw    (196.05,71.37) -- (192.48,68.22) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (193.02,74.35) .. controls (193.86,74.96) and (194.98,75.19) .. (196.04,75.04) .. controls (196.08,74.3) and (195.72,73.55) .. (194.97,73) .. controls (194.13,72.38) and (193,72.15) .. (191.94,72.3) .. controls (191.91,73.05) and (192.27,73.8) .. (193.02,74.35) -- cycle ;
            	\draw    (196.04,75.04) -- (191.94,72.3) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (193.49,77.43) .. controls (194.21,78.13) and (195.29,78.48) .. (196.36,78.44) .. controls (196.52,77.71) and (196.3,76.92) .. (195.66,76.3) .. controls (194.94,75.6) and (193.86,75.25) .. (192.79,75.29) .. controls (192.62,76.03) and (192.85,76.81) .. (193.49,77.43) -- cycle ;
            	\draw    (196.36,78.44) -- (192.79,75.29) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (192.52,80.66) .. controls (193.24,81.35) and (194.32,81.7) .. (195.39,81.67) .. controls (195.56,80.93) and (195.33,80.15) .. (194.69,79.52) .. controls (193.97,78.82) and (192.89,78.48) .. (191.82,78.51) .. controls (191.66,79.25) and (191.88,80.03) .. (192.52,80.66) -- cycle ;
            	\draw    (195.39,81.67) -- (191.82,78.51) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (197.26,67.96) .. controls (196.53,68.66) and (196.32,69.55) .. (196.58,70.36) .. controls (197.54,70.32) and (198.48,69.97) .. (199.14,69.34) .. controls (199.87,68.64) and (200.09,67.75) .. (199.82,66.94) .. controls (198.86,66.99) and (197.92,67.33) .. (197.26,67.96) -- cycle ;
            	\draw    (196.58,70.36) -- (199.82,66.94) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (197.21,70.85) .. controls (196.42,71.52) and (196.13,72.4) .. (196.33,73.21) .. controls (197.29,73.22) and (198.26,72.92) .. (198.97,72.33) .. controls (199.75,71.66) and (200.04,70.78) .. (199.84,69.97) .. controls (198.88,69.96) and (197.92,70.26) .. (197.21,70.85) -- cycle ;
            	\draw    (196.33,73.21) -- (199.84,69.97) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (197.61,73.78) .. controls (196.82,74.44) and (196.54,75.33) .. (196.73,76.14) .. controls (197.7,76.15) and (198.66,75.85) .. (199.37,75.26) .. controls (200.16,74.59) and (200.44,73.71) .. (200.25,72.89) .. controls (199.28,72.89) and (198.32,73.19) .. (197.61,73.78) -- cycle ;
            	\draw    (196.73,76.14) -- (200.25,72.89) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (197.33,77.12) .. controls (196.55,77.79) and (196.26,78.67) .. (196.46,79.49) .. controls (197.42,79.49) and (198.38,79.19) .. (199.09,78.6) .. controls (199.88,77.94) and (200.17,77.05) .. (199.97,76.24) .. controls (199.01,76.23) and (198.04,76.53) .. (197.33,77.12) -- cycle ;
            	\draw    (196.46,79.49) -- (199.97,76.24) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (196.03,80.89) .. controls (195.24,81.55) and (194.95,82.43) .. (195.15,83.25) .. controls (196.11,83.26) and (197.08,82.96) .. (197.79,82.36) .. controls (198.58,81.7) and (198.86,80.82) .. (198.66,80) .. controls (197.7,79.99) and (196.74,80.29) .. (196.03,80.89) -- cycle ;
            	\draw    (195.15,83.25) -- (198.66,80) ;
            	\draw  [fill={rgb, 255:red, 112; green, 200; blue, 20 }  ,fill opacity=1 ] (159.91,71.42) .. controls (157.51,75.52) and (153.55,77.78) .. (149.64,77.74) .. controls (147.98,73.89) and (148.2,69) .. (150.59,64.91) .. controls (152.99,60.82) and (156.96,58.56) .. (160.86,58.59) .. controls (162.53,62.45) and (162.31,67.33) .. (159.91,71.42) -- cycle ;
            	\draw  [fill={rgb, 255:red, 112; green, 200; blue, 20 }  ,fill opacity=1 ] (153.92,66.48) .. controls (153.92,71.33) and (151.7,75.58) .. (148.39,77.85) .. controls (145.09,75.58) and (142.86,71.33) .. (142.86,66.48) .. controls (142.86,61.62) and (145.09,57.38) .. (148.39,55.11) .. controls (151.7,57.38) and (153.92,61.62) .. (153.92,66.48) -- cycle ;
            	\draw  [fill={rgb, 255:red, 112; green, 200; blue, 20 }  ,fill opacity=1 ] (145.17,66.21) .. controls (147.14,70.56) and (146.87,75.44) .. (144.83,79.08) .. controls (140.95,78.65) and (137.23,75.93) .. (135.25,71.57) .. controls (133.28,67.22) and (133.55,62.34) .. (135.59,58.7) .. controls (139.48,59.13) and (143.19,61.86) .. (145.17,66.21) -- cycle ;
            	\draw  [fill={rgb, 255:red, 112; green, 200; blue, 20 }  ,fill opacity=1 ] (138.33,70.44) .. controls (141.1,72.18) and (142.73,75.21) .. (142.84,78.27) .. controls (140.37,79.71) and (137.15,79.71) .. (134.38,77.97) .. controls (131.61,76.24) and (129.98,73.21) .. (129.87,70.15) .. controls (132.34,68.71) and (135.56,68.71) .. (138.33,70.44) -- cycle ;
            	\draw  [fill={rgb, 255:red, 112; green, 200; blue, 20 }  ,fill opacity=1 ] (162.03,77.35) .. controls (159.47,79.27) and (156.36,79.54) .. (153.86,78.36) .. controls (153.75,75.39) and (155.11,72.31) .. (157.67,70.4) .. controls (160.23,68.48) and (163.35,68.21) .. (165.85,69.39) .. controls (165.95,72.37) and (164.6,75.44) .. (162.03,77.35) -- cycle ;
            	\draw  [fill={rgb, 255:red, 112; green, 200; blue, 20 }  ,fill opacity=1 ] (142.39,83.55) .. controls (142.5,80.79) and (144.82,78.49) .. (148.17,77.36) .. controls (151.42,78.81) and (153.55,81.33) .. (153.44,84.08) .. controls (153.32,86.84) and (151,89.14) .. (147.65,90.27) .. controls (144.4,88.82) and (142.27,86.31) .. (142.39,83.55) -- cycle ;
            	\draw  [fill={rgb, 255:red, 112; green, 200; blue, 20 }  ,fill opacity=1 ] (134.38,77.97) .. controls (135.74,75.65) and (138.8,74.92) .. (142.22,75.78) .. controls (144.38,78.81) and (145.06,82.14) .. (143.7,84.47) .. controls (142.35,86.8) and (139.28,87.52) .. (135.86,86.67) .. controls (133.71,83.64) and (133.02,80.3) .. (134.38,77.97) -- cycle ;
            	\draw  [fill={rgb, 255:red, 112; green, 200; blue, 20 }  ,fill opacity=1 ] (151.02,86.08) .. controls (149.67,83.75) and (150.37,80.41) .. (152.53,77.39) .. controls (155.96,76.56) and (159.02,77.29) .. (160.37,79.63) .. controls (161.72,81.96) and (161.01,85.29) .. (158.85,88.31) .. controls (155.43,89.15) and (152.37,88.41) .. (151.02,86.08) -- cycle ;
            	\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ] (143.13,69.62) .. controls (143.23,67.25) and (144.85,65.25) .. (147.17,64.26) .. controls (149.39,65.47) and (150.84,67.62) .. (150.74,69.99) .. controls (150.65,72.36) and (149.03,74.36) .. (146.71,75.35) .. controls (144.48,74.14) and (143.04,71.99) .. (143.13,69.62) -- cycle ;
            	\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ] (150.87,69.22) .. controls (152.42,67.55) and (154.64,67.06) .. (156.66,67.72) .. controls (157.23,69.94) and (156.75,72.36) .. (155.21,74.02) .. controls (153.66,75.69) and (151.43,76.18) .. (149.42,75.52) .. controls (148.84,73.31) and (149.32,70.89) .. (150.87,69.22) -- cycle ;
            	\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ] (139.22,75.56) .. controls (137.53,74.06) and (136.83,71.72) .. (137.19,69.48) .. controls (139.12,68.63) and (141.37,68.89) .. (143.06,70.38) .. controls (144.75,71.87) and (145.45,74.22) .. (145.09,76.46) .. controls (143.16,77.31) and (140.91,77.05) .. (139.22,75.56) -- cycle ;
            	\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ] (148.39,80.7) .. controls (147.71,79.04) and (148.17,77.07) .. (149.42,75.52) .. controls (151.3,75.53) and (152.95,76.46) .. (153.64,78.12) .. controls (154.32,79.78) and (153.86,81.75) .. (152.61,83.29) .. controls (150.73,83.29) and (149.08,82.36) .. (148.39,80.7) -- cycle ;
            	\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ] (141.97,77.82) .. controls (142.89,76.07) and (144.74,75.2) .. (146.71,75.35) .. controls (147.83,77.15) and (148.06,79.33) .. (147.13,81.08) .. controls (146.21,82.83) and (144.36,83.7) .. (142.39,83.55) .. controls (141.28,81.76) and (141.04,79.57) .. (141.97,77.82) -- cycle ;
            	\draw  [fill={rgb, 255:red, 252; green, 193; blue, 241 }  ,fill opacity=1 ] (184.91,78.23) .. controls (182.97,81.26) and (179.76,82.94) .. (176.6,82.91) .. controls (175.26,80.06) and (175.43,76.44) .. (177.37,73.41) .. controls (179.31,70.38) and (182.52,68.71) .. (185.68,68.73) .. controls (187.02,71.59) and (186.85,75.2) .. (184.91,78.23) -- cycle ;
            	\draw  [fill={rgb, 255:red, 252; green, 193; blue, 241 }  ,fill opacity=1 ] (180.07,74.57) .. controls (180.07,78.17) and (178.27,81.31) .. (175.59,82.99) .. controls (172.92,81.31) and (171.12,78.17) .. (171.12,74.57) .. controls (171.12,70.97) and (172.92,67.83) .. (175.59,66.15) .. controls (178.27,67.83) and (180.07,70.97) .. (180.07,74.57) -- cycle ;
            	\draw  [fill={rgb, 255:red, 252; green, 193; blue, 241 }  ,fill opacity=1 ] (172.98,74.37) .. controls (174.58,77.6) and (174.36,81.21) .. (172.71,83.9) .. controls (169.57,83.58) and (166.56,81.57) .. (164.97,78.35) .. controls (163.37,75.12) and (163.59,71.51) .. (165.24,68.82) .. controls (168.38,69.14) and (171.39,71.15) .. (172.98,74.37) -- cycle ;
            	\draw  [fill={rgb, 255:red, 252; green, 193; blue, 241 }  ,fill opacity=1 ] (167.45,77.51) .. controls (169.7,78.79) and (171.01,81.03) .. (171.11,83.3) .. controls (169.1,84.37) and (166.5,84.37) .. (164.26,83.08) .. controls (162.02,81.8) and (160.7,79.56) .. (160.61,77.29) .. controls (162.61,76.22) and (165.21,76.22) .. (167.45,77.51) -- cycle ;
            	\draw  [fill={rgb, 255:red, 252; green, 193; blue, 241 }  ,fill opacity=1 ] (186.63,82.63) .. controls (184.55,84.04) and (182.04,84.25) .. (180.01,83.37) .. controls (179.93,81.17) and (181.03,78.89) .. (183.1,77.47) .. controls (185.17,76.06) and (187.69,75.85) .. (189.71,76.73) .. controls (189.8,78.93) and (188.7,81.21) .. (186.63,82.63) -- cycle ;
            	\draw  [fill={rgb, 255:red, 252; green, 193; blue, 241 }  ,fill opacity=1 ] (170.74,87.21) .. controls (170.83,85.17) and (172.7,83.47) .. (175.42,82.63) .. controls (178.04,83.7) and (179.76,85.57) .. (179.67,87.61) .. controls (179.58,89.65) and (177.7,91.35) .. (174.99,92.19) .. controls (172.36,91.12) and (170.64,89.25) .. (170.74,87.21) -- cycle ;
            	\draw  [fill={rgb, 255:red, 252; green, 193; blue, 241 }  ,fill opacity=1 ] (164.26,83.08) .. controls (165.36,81.36) and (167.83,80.82) .. (170.6,81.46) .. controls (172.34,83.7) and (172.9,86.17) .. (171.8,87.89) .. controls (170.7,89.62) and (168.22,90.15) .. (165.46,89.52) .. controls (163.72,87.28) and (163.16,84.81) .. (164.26,83.08) -- cycle ;
            	\draw  [fill={rgb, 255:red, 252; green, 193; blue, 241 }  ,fill opacity=1 ] (177.72,89.09) .. controls (176.62,87.36) and (177.19,84.89) .. (178.94,82.66) .. controls (181.71,82.03) and (184.18,82.58) .. (185.28,84.31) .. controls (186.37,86.03) and (185.8,88.5) .. (184.05,90.74) .. controls (181.28,91.36) and (178.81,90.81) .. (177.72,89.09) -- cycle ;
            	\draw  [fill={rgb, 255:red, 252; green, 193; blue, 241 }  ,fill opacity=1 ] (171.34,76.9) .. controls (171.42,75.14) and (172.72,73.66) .. (174.6,72.93) .. controls (176.4,73.83) and (177.57,75.42) .. (177.49,77.17) .. controls (177.42,78.93) and (176.11,80.41) .. (174.23,81.14) .. controls (172.43,80.24) and (171.26,78.65) .. (171.34,76.9) -- cycle ;
            	\draw  [fill={rgb, 255:red, 252; green, 193; blue, 241 }  ,fill opacity=1 ] (177.6,76.6) .. controls (178.85,75.37) and (180.65,75.01) .. (182.28,75.49) .. controls (182.74,77.13) and (182.35,78.93) .. (181.1,80.16) .. controls (179.85,81.39) and (178.05,81.76) .. (176.42,81.27) .. controls (175.96,79.63) and (176.34,77.84) .. (177.6,76.6) -- cycle ;
            	\draw  [fill={rgb, 255:red, 252; green, 193; blue, 241 }  ,fill opacity=1 ] (168.18,81.29) .. controls (166.81,80.19) and (166.24,78.45) .. (166.53,76.79) .. controls (168.09,76.16) and (169.91,76.36) .. (171.28,77.46) .. controls (172.64,78.57) and (173.21,80.3) .. (172.92,81.97) .. controls (171.36,82.59) and (169.54,82.4) .. (168.18,81.29) -- cycle ;
            	\draw  [fill={rgb, 255:red, 252; green, 193; blue, 241 }  ,fill opacity=1 ] (175.59,85.1) .. controls (175.04,83.87) and (175.41,82.41) .. (176.42,81.27) .. controls (177.95,81.27) and (179.28,81.96) .. (179.84,83.19) .. controls (180.39,84.42) and (180.02,85.88) .. (179.01,87.02) .. controls (177.48,87.02) and (176.14,86.33) .. (175.59,85.1) -- cycle ;
            	\draw  [fill={rgb, 255:red, 252; green, 193; blue, 241 }  ,fill opacity=1 ] (170.4,82.97) .. controls (171.14,81.68) and (172.64,81.03) .. (174.23,81.14) .. controls (175.13,82.47) and (175.32,84.09) .. (174.57,85.38) .. controls (173.83,86.68) and (172.33,87.33) .. (170.74,87.21) .. controls (169.84,85.89) and (169.65,84.27) .. (170.4,82.97) -- cycle ;
            	\draw  [fill={rgb, 255:red, 237; green, 134; blue, 147 }  ,fill opacity=1 ] (133.18,81.86) .. controls (131.45,84.56) and (128.6,86.05) .. (125.79,86.03) .. controls (124.59,83.49) and (124.75,80.27) .. (126.47,77.57) .. controls (128.2,74.88) and (131.05,73.38) .. (133.86,73.41) .. controls (135.06,75.95) and (134.9,79.17) .. (133.18,81.86) -- cycle ;
            	\draw  [fill={rgb, 255:red, 237; green, 134; blue, 147 }  ,fill opacity=1 ] (128.87,78.6) .. controls (128.87,81.8) and (127.27,84.6) .. (124.89,86.09) .. controls (122.51,84.6) and (120.91,81.8) .. (120.91,78.6) .. controls (120.91,75.4) and (122.51,72.61) .. (124.89,71.11) .. controls (127.27,72.61) and (128.87,75.4) .. (128.87,78.6) -- cycle ;
            	\draw  [fill={rgb, 255:red, 237; green, 134; blue, 147 }  ,fill opacity=1 ] (122.56,78.43) .. controls (123.99,81.3) and (123.79,84.51) .. (122.32,86.91) .. controls (119.53,86.62) and (116.85,84.83) .. (115.43,81.96) .. controls (114.01,79.09) and (114.2,75.88) .. (115.67,73.48) .. controls (118.47,73.77) and (121.14,75.56) .. (122.56,78.43) -- cycle ;
            	\draw  [fill={rgb, 255:red, 237; green, 134; blue, 147 }  ,fill opacity=1 ] (117.65,81.21) .. controls (119.64,82.36) and (120.81,84.35) .. (120.89,86.37) .. controls (119.11,87.32) and (116.8,87.32) .. (114.8,86.18) .. controls (112.81,85.03) and (111.64,83.04) .. (111.55,81.02) .. controls (113.34,80.07) and (115.65,80.07) .. (117.65,81.21) -- cycle ;
            	\draw  [fill={rgb, 255:red, 237; green, 134; blue, 147 }  ,fill opacity=1 ] (134.7,85.77) .. controls (132.86,87.03) and (130.62,87.21) .. (128.82,86.43) .. controls (128.74,84.47) and (129.72,82.45) .. (131.57,81.19) .. controls (133.41,79.92) and (135.65,79.74) .. (137.45,80.52) .. controls (137.53,82.48) and (136.55,84.51) .. (134.7,85.77) -- cycle ;
            	\draw  [fill={rgb, 255:red, 237; green, 134; blue, 147 }  ,fill opacity=1 ] (120.56,89.85) .. controls (120.65,88.03) and (122.31,86.52) .. (124.73,85.78) .. controls (127.07,86.73) and (128.6,88.39) .. (128.52,90.2) .. controls (128.44,92.02) and (126.77,93.53) .. (124.35,94.28) .. controls (122.01,93.32) and (120.48,91.67) .. (120.56,89.85) -- cycle ;
            	\draw  [fill={rgb, 255:red, 237; green, 134; blue, 147 }  ,fill opacity=1 ] (114.8,86.18) .. controls (115.78,84.64) and (117.98,84.17) .. (120.45,84.73) .. controls (122,86.73) and (122.49,88.93) .. (121.51,90.46) .. controls (120.53,91.99) and (118.33,92.47) .. (115.87,91.91) .. controls (114.32,89.91) and (113.82,87.71) .. (114.8,86.18) -- cycle ;
            	\draw  [fill={rgb, 255:red, 237; green, 134; blue, 147 }  ,fill opacity=1 ] (126.78,91.52) .. controls (125.8,89.98) and (126.31,87.79) .. (127.87,85.8) .. controls (130.33,85.24) and (132.53,85.73) .. (133.5,87.27) .. controls (134.48,88.8) and (133.97,91) .. (132.41,92.99) .. controls (129.95,93.54) and (127.75,93.06) .. (126.78,91.52) -- cycle ;
            	\draw  [fill={rgb, 255:red, 237; green, 134; blue, 147 }  ,fill opacity=1 ] (121.1,80.67) .. controls (121.17,79.11) and (122.33,77.8) .. (124,77.14) .. controls (125.61,77.94) and (126.65,79.35) .. (126.58,80.92) .. controls (126.51,82.48) and (125.35,83.79) .. (123.68,84.45) .. controls (122.07,83.65) and (121.03,82.24) .. (121.1,80.67) -- cycle ;
            	\draw  [fill={rgb, 255:red, 237; green, 134; blue, 147 }  ,fill opacity=1 ] (126.67,80.41) .. controls (127.78,79.31) and (129.38,78.99) .. (130.84,79.42) .. controls (131.25,80.88) and (130.9,82.48) .. (129.79,83.58) .. controls (128.68,84.67) and (127.08,85) .. (125.62,84.56) .. controls (125.21,83.1) and (125.56,81.51) .. (126.67,80.41) -- cycle ;
            	\draw  [fill={rgb, 255:red, 237; green, 134; blue, 147 }  ,fill opacity=1 ] (118.29,84.59) .. controls (117.07,83.6) and (116.56,82.06) .. (116.82,80.58) .. controls (118.21,80.02) and (119.83,80.19) .. (121.05,81.17) .. controls (122.26,82.16) and (122.77,83.7) .. (122.51,85.18) .. controls (121.12,85.74) and (119.5,85.57) .. (118.29,84.59) -- cycle ;
            	\draw  [fill={rgb, 255:red, 237; green, 134; blue, 147 }  ,fill opacity=1 ] (124.89,87.97) .. controls (124.39,86.88) and (124.72,85.58) .. (125.62,84.56) .. controls (126.98,84.57) and (128.17,85.18) .. (128.66,86.27) .. controls (129.15,87.37) and (128.82,88.66) .. (127.93,89.68) .. controls (126.57,89.68) and (125.38,89.07) .. (124.89,87.97) -- cycle ;
            	\draw  [fill={rgb, 255:red, 237; green, 134; blue, 147 }  ,fill opacity=1 ] (120.26,86.08) .. controls (120.93,84.93) and (122.26,84.35) .. (123.68,84.45) .. controls (124.48,85.63) and (124.65,87.07) .. (123.98,88.22) .. controls (123.31,89.38) and (121.99,89.95) .. (120.56,89.85) .. controls (119.76,88.67) and (119.6,87.23) .. (120.26,86.08) -- cycle ;
            	\draw  [fill={rgb, 255:red, 160; green, 237; blue, 220 }  ,fill opacity=1 ] (164.59,87.1) .. controls (163.34,89.05) and (161.27,90.13) .. (159.23,90.12) .. controls (158.36,88.28) and (158.48,85.94) .. (159.73,83.99) .. controls (160.98,82.03) and (163.05,80.95) .. (165.08,80.97) .. controls (165.95,82.81) and (165.84,85.14) .. (164.59,87.1) -- cycle ;
            	\draw  [fill={rgb, 255:red, 160; green, 237; blue, 220 }  ,fill opacity=1 ] (161.47,84.74) .. controls (161.47,87.06) and (160.31,89.08) .. (158.58,90.17) .. controls (156.86,89.08) and (155.7,87.06) .. (155.7,84.74) .. controls (155.7,82.42) and (156.86,80.39) .. (158.58,79.31) .. controls (160.31,80.39) and (161.47,82.42) .. (161.47,84.74) -- cycle ;
            	\draw  [fill={rgb, 255:red, 160; green, 237; blue, 220 }  ,fill opacity=1 ] (156.9,84.61) .. controls (157.93,86.69) and (157.79,89.02) .. (156.72,90.76) .. controls (154.69,90.55) and (152.76,89.25) .. (151.73,87.17) .. controls (150.7,85.09) and (150.84,82.76) .. (151.9,81.02) .. controls (153.93,81.23) and (155.87,82.53) .. (156.9,84.61) -- cycle ;
            	\draw  [fill={rgb, 255:red, 160; green, 237; blue, 220 }  ,fill opacity=1 ] (153.33,86.63) .. controls (154.78,87.46) and (155.63,88.91) .. (155.68,90.37) .. controls (154.39,91.06) and (152.72,91.06) .. (151.27,90.23) .. controls (149.82,89.4) and (148.97,87.95) .. (148.91,86.49) .. controls (150.21,85.8) and (151.88,85.8) .. (153.33,86.63) -- cycle ;
            	\draw  [fill={rgb, 255:red, 160; green, 237; blue, 220 }  ,fill opacity=1 ] (165.7,89.93) .. controls (164.36,90.85) and (162.74,90.98) .. (161.43,90.41) .. controls (161.38,88.99) and (162.08,87.52) .. (163.42,86.61) .. controls (164.76,85.69) and (166.38,85.56) .. (167.69,86.13) .. controls (167.74,87.55) and (167.03,89.02) .. (165.7,89.93) -- cycle ;
            	\draw  [fill={rgb, 255:red, 160; green, 237; blue, 220 }  ,fill opacity=1 ] (155.45,92.89) .. controls (155.5,91.57) and (156.71,90.47) .. (158.47,89.94) .. controls (160.16,90.63) and (161.27,91.83) .. (161.21,93.14) .. controls (161.15,94.46) and (159.94,95.56) .. (158.19,96.1) .. controls (156.5,95.41) and (155.39,94.21) .. (155.45,92.89) -- cycle ;
            	\draw  [fill={rgb, 255:red, 160; green, 237; blue, 220 }  ,fill opacity=1 ] (151.27,90.23) .. controls (151.98,89.12) and (153.58,88.77) .. (155.36,89.18) .. controls (156.48,90.62) and (156.84,92.22) .. (156.13,93.33) .. controls (155.42,94.44) and (153.83,94.79) .. (152.04,94.38) .. controls (150.92,92.93) and (150.56,91.34) .. (151.27,90.23) -- cycle ;
            	\draw  [fill={rgb, 255:red, 160; green, 237; blue, 220 }  ,fill opacity=1 ] (159.95,94.1) .. controls (159.24,92.98) and (159.61,91.39) .. (160.74,89.95) .. controls (162.53,89.55) and (164.12,89.9) .. (164.83,91.02) .. controls (165.53,92.13) and (165.16,93.72) .. (164.04,95.17) .. controls (162.25,95.57) and (160.65,95.21) .. (159.95,94.1) -- cycle ;
            	\draw  [fill={rgb, 255:red, 160; green, 237; blue, 220 }  ,fill opacity=1 ] (155.84,86.24) .. controls (155.89,85.1) and (156.73,84.15) .. (157.94,83.67) .. controls (159.1,84.26) and (159.86,85.28) .. (159.81,86.41) .. controls (159.76,87.55) and (158.91,88.5) .. (157.7,88.98) .. controls (156.54,88.39) and (155.79,87.37) .. (155.84,86.24) -- cycle ;
            	\draw  [fill={rgb, 255:red, 160; green, 237; blue, 220 }  ,fill opacity=1 ] (159.87,86.05) .. controls (160.68,85.25) and (161.84,85.02) .. (162.89,85.33) .. controls (163.19,86.39) and (162.94,87.55) .. (162.13,88.34) .. controls (161.33,89.14) and (160.17,89.37) .. (159.11,89.06) .. controls (158.81,88) and (159.06,86.84) .. (159.87,86.05) -- cycle ;
            	\draw  [fill={rgb, 255:red, 160; green, 237; blue, 220 }  ,fill opacity=1 ] (153.8,89.07) .. controls (152.91,88.36) and (152.55,87.24) .. (152.73,86.17) .. controls (153.74,85.76) and (154.91,85.89) .. (155.79,86.6) .. controls (156.68,87.31) and (157.04,88.43) .. (156.86,89.51) .. controls (155.85,89.91) and (154.68,89.79) .. (153.8,89.07) -- cycle ;
            	\draw  [fill={rgb, 255:red, 160; green, 237; blue, 220 }  ,fill opacity=1 ] (158.58,91.53) .. controls (158.22,90.73) and (158.46,89.79) .. (159.11,89.06) .. controls (160.1,89.06) and (160.96,89.5) .. (161.32,90.3) .. controls (161.67,91.09) and (161.43,92.03) .. (160.78,92.77) .. controls (159.8,92.76) and (158.94,92.32) .. (158.58,91.53) -- cycle ;
            	\draw  [fill={rgb, 255:red, 160; green, 237; blue, 220 }  ,fill opacity=1 ] (155.23,90.16) .. controls (155.71,89.32) and (156.67,88.9) .. (157.7,88.98) .. controls (158.28,89.83) and (158.4,90.87) .. (157.92,91.71) .. controls (157.44,92.55) and (156.48,92.96) .. (155.45,92.89) .. controls (154.87,92.03) and (154.75,90.99) .. (155.23,90.16) -- cycle ;
            	\draw  [fill={rgb, 255:red, 112; green, 200; blue, 20 }  ,fill opacity=1 ] (201.71,80.91) .. controls (200.12,83.4) and (197.49,84.77) .. (194.9,84.75) .. controls (193.79,82.41) and (193.94,79.44) .. (195.53,76.96) .. controls (197.12,74.47) and (199.75,73.1) .. (202.34,73.12) .. controls (203.45,75.46) and (203.3,78.43) .. (201.71,80.91) -- cycle ;
            	\draw  [fill={rgb, 255:red, 112; green, 200; blue, 20 }  ,fill opacity=1 ] (197.74,77.91) .. controls (197.74,80.86) and (196.26,83.43) .. (194.07,84.81) .. controls (191.88,83.43) and (190.4,80.86) .. (190.4,77.91) .. controls (190.4,74.96) and (191.88,72.38) .. (194.07,71) .. controls (196.26,72.38) and (197.74,74.96) .. (197.74,77.91) -- cycle ;
            	\draw  [fill={rgb, 255:red, 112; green, 200; blue, 20 }  ,fill opacity=1 ] (191.93,77.75) .. controls (193.24,80.39) and (193.06,83.35) .. (191.71,85.56) .. controls (189.13,85.3) and (186.66,83.65) .. (185.35,81) .. controls (184.05,78.36) and (184.22,75.4) .. (185.58,73.19) .. controls (188.15,73.45) and (190.62,75.1) .. (191.93,77.75) -- cycle ;
            	\draw  [fill={rgb, 255:red, 112; green, 200; blue, 20 }  ,fill opacity=1 ] (187.4,80.32) .. controls (189.23,81.37) and (190.31,83.21) .. (190.39,85.07) .. controls (188.75,85.94) and (186.61,85.94) .. (184.77,84.89) .. controls (182.94,83.84) and (181.86,82) .. (181.78,80.14) .. controls (183.42,79.26) and (185.56,79.26) .. (187.4,80.32) -- cycle ;
            	\draw  [fill={rgb, 255:red, 112; green, 200; blue, 20 }  ,fill opacity=1 ] (203.12,84.51) .. controls (201.42,85.68) and (199.36,85.84) .. (197.7,85.13) .. controls (197.63,83.32) and (198.53,81.45) .. (200.23,80.29) .. controls (201.92,79.13) and (203.99,78.96) .. (205.65,79.68) .. controls (205.72,81.48) and (204.82,83.35) .. (203.12,84.51) -- cycle ;
            	\draw  [fill={rgb, 255:red, 112; green, 200; blue, 20 }  ,fill opacity=1 ] (190.09,88.28) .. controls (190.16,86.6) and (191.7,85.2) .. (193.92,84.52) .. controls (196.08,85.4) and (197.49,86.93) .. (197.42,88.6) .. controls (197.34,90.28) and (195.8,91.67) .. (193.58,92.36) .. controls (191.42,91.48) and (190.01,89.95) .. (190.09,88.28) -- cycle ;
            	\draw  [fill={rgb, 255:red, 112; green, 200; blue, 20 }  ,fill opacity=1 ] (184.77,84.89) .. controls (185.68,83.48) and (187.71,83.04) .. (189.98,83.56) .. controls (191.4,85.4) and (191.86,87.42) .. (190.96,88.84) .. controls (190.06,90.25) and (188.03,90.69) .. (185.76,90.17) .. controls (184.33,88.33) and (183.87,86.3) .. (184.77,84.89) -- cycle ;
            	\draw  [fill={rgb, 255:red, 112; green, 200; blue, 20 }  ,fill opacity=1 ] (195.81,89.81) .. controls (194.92,88.4) and (195.38,86.37) .. (196.82,84.54) .. controls (199.09,84.03) and (201.12,84.48) .. (202.01,85.89) .. controls (202.91,87.31) and (202.44,89.34) .. (201.01,91.17) .. controls (198.74,91.68) and (196.71,91.23) .. (195.81,89.81) -- cycle ;
            	\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ] (190.58,79.82) .. controls (190.65,78.38) and (191.72,77.16) .. (193.26,76.56) .. controls (194.73,77.3) and (195.69,78.6) .. (195.63,80.04) .. controls (195.57,81.48) and (194.5,82.69) .. (192.96,83.3) .. controls (191.48,82.56) and (190.52,81.26) .. (190.58,79.82) -- cycle ;
            	\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ] (195.71,79.57) .. controls (196.74,78.56) and (198.21,78.26) .. (199.55,78.66) .. controls (199.93,80.01) and (199.62,81.48) .. (198.59,82.49) .. controls (197.56,83.5) and (196.09,83.8) .. (194.75,83.4) .. controls (194.37,82.06) and (194.69,80.59) .. (195.71,79.57) -- cycle ;
            	\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ] (187.99,83.42) .. controls (186.87,82.52) and (186.4,81.09) .. (186.63,79.73) .. controls (187.92,79.21) and (189.41,79.37) .. (190.53,80.28) .. controls (191.65,81.19) and (192.12,82.61) .. (191.88,83.97) .. controls (190.6,84.49) and (189.11,84.33) .. (187.99,83.42) -- cycle ;
            	\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ] (194.07,86.54) .. controls (193.62,85.54) and (193.92,84.34) .. (194.75,83.4) .. controls (196,83.4) and (197.1,83.97) .. (197.55,84.98) .. controls (198,85.99) and (197.7,87.18) .. (196.87,88.12) .. controls (195.62,88.12) and (194.52,87.55) .. (194.07,86.54) -- cycle ;
            	\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ] (189.81,84.8) .. controls (190.42,83.74) and (191.65,83.21) .. (192.96,83.3) .. controls (193.69,84.39) and (193.85,85.71) .. (193.23,86.78) .. controls (192.62,87.84) and (191.4,88.37) .. (190.09,88.28) .. controls (189.35,87.19) and (189.19,85.86) .. (189.81,84.8) -- cycle ;
            	\draw    (98.16,69.31) .. controls (100.49,75.28) and (107.61,80.77) .. (106.67,86.94) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (94.21,69.52) .. controls (95.19,70.43) and (96.72,70.66) .. (98.29,70.27) .. controls (98.59,69.03) and (98.34,67.83) .. (97.46,67.02) .. controls (96.48,66.11) and (94.95,65.88) .. (93.39,66.27) .. controls (93.08,67.51) and (93.33,68.7) .. (94.21,69.52) -- cycle ;
            	\draw    (98.29,70.27) -- (93.39,66.27) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (96.27,74.52) .. controls (97.58,74.73) and (99.05,74.3) .. (100.26,73.46) .. controls (99.94,72.55) and (99.14,71.88) .. (97.97,71.69) .. controls (96.67,71.48) and (95.19,71.91) .. (93.99,72.74) .. controls (94.31,73.65) and (95.1,74.32) .. (96.27,74.52) -- cycle ;
            	\draw    (100.26,73.46) -- (93.99,72.74) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (98.84,78.9) .. controls (100.22,78.93) and (101.67,78.34) .. (102.78,77.39) .. controls (102.31,76.57) and (101.38,76.03) .. (100.14,76) .. controls (98.76,75.96) and (97.31,76.56) .. (96.2,77.51) .. controls (96.67,78.33) and (97.6,78.86) .. (98.84,78.9) -- cycle ;
            	\draw    (102.78,77.39) -- (96.2,77.51) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (101.51,81.84) .. controls (102.81,82.06) and (104.29,81.63) .. (105.49,80.79) .. controls (105.17,79.88) and (104.38,79.21) .. (103.21,79.02) .. controls (101.9,78.81) and (100.43,79.24) .. (99.22,80.07) .. controls (99.54,80.98) and (100.34,81.65) .. (101.51,81.84) -- cycle ;
            	\draw    (105.49,80.79) -- (99.22,80.07) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (102.62,86.01) .. controls (103.93,86.23) and (105.4,85.8) .. (106.61,84.96) .. controls (106.29,84.05) and (105.49,83.38) .. (104.32,83.19) .. controls (103.02,82.97) and (101.54,83.4) .. (100.34,84.24) .. controls (100.66,85.15) and (101.45,85.82) .. (102.62,86.01) -- cycle ;
            	\draw    (106.61,84.96) -- (100.34,84.24) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (99.29,68.91) .. controls (98.94,70.2) and (99.31,71.31) .. (100.17,71.98) .. controls (101.24,71.22) and (102.08,70.15) .. (102.4,68.99) .. controls (102.75,67.69) and (102.38,66.58) .. (101.52,65.92) .. controls (100.45,66.68) and (99.61,67.74) .. (99.29,68.91) -- cycle ;
            	\draw    (100.17,71.98) -- (101.52,65.92) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (101.23,72.04) .. controls (100.78,73.33) and (101.06,74.49) .. (101.85,75.22) .. controls (102.96,74.51) and (103.86,73.47) .. (104.26,72.31) .. controls (104.7,71.01) and (104.43,69.86) .. (103.64,69.13) .. controls (102.53,69.84) and (101.63,70.88) .. (101.23,72.04) -- cycle ;
            	\draw    (101.85,75.22) -- (103.64,69.13) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (103.71,74.87) .. controls (103.26,76.17) and (103.54,77.32) .. (104.33,78.05) .. controls (105.44,77.34) and (106.34,76.3) .. (106.74,75.14) .. controls (107.19,73.85) and (106.91,72.69) .. (106.12,71.96) .. controls (105.01,72.67) and (104.11,73.71) .. (103.71,74.87) -- cycle ;
            	\draw    (104.33,78.05) -- (106.12,71.96) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (105.7,78.65) .. controls (105.25,79.95) and (105.53,81.11) .. (106.32,81.83) .. controls (107.43,81.13) and (108.33,80.09) .. (108.73,78.93) .. controls (109.18,77.63) and (108.9,76.47) .. (108.11,75.75) .. controls (107,76.45) and (106.1,77.49) .. (105.7,78.65) -- cycle ;
            	\draw    (106.32,81.83) -- (108.11,75.75) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (106.8,83.65) .. controls (106.36,84.95) and (106.63,86.1) .. (107.43,86.83) .. controls (108.53,86.12) and (109.43,85.08) .. (109.83,83.92) .. controls (110.28,82.62) and (110,81.47) .. (109.21,80.74) .. controls (108.1,81.45) and (107.2,82.49) .. (106.8,83.65) -- cycle ;
            	\draw    (107.43,86.83) -- (109.21,80.74) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.14 ] (173.99,130.61) .. controls (171.6,160.02) and (170.81,181.48) .. (168.82,207.31) .. controls (148.16,200.95) and (141.01,198.96) .. (109.21,190.62) .. controls (169.62,208.1) and (162.46,165.18) .. (173.99,130.61) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.14 ] (233.2,80.54) .. controls (230.82,109.95) and (214.52,155.65) .. (212.54,181.48) .. controls (195.05,190.62) and (191.87,195.39) .. (168.82,207.31) .. controls (170.73,199.12) and (165.94,195.69) .. (170.81,185.85) .. controls (196.57,181.81) and (216.11,145.31) .. (225.65,84.12) .. controls (230.82,81.73) and (225.65,83.72) .. (233.2,80.54) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.43 ] (176.37,100.81) .. controls (173.59,107.56) and (115.97,90.87) .. (87.76,94.85) .. controls (86.17,101.6) and (109.21,175.52) .. (109.21,190.62) .. controls (104.84,175.12) and (89.74,120.28) .. (81,88.49) .. controls (125.51,95.24) and (146.17,98.03) .. (176.37,100.81) -- cycle ;
            \end{tikzpicture}'''
                # Câu hỏi
                noidungcauhoi = (r'''\immini{Một chậu trồng cây có dạng hình chóp cụt tứ giác đều có cạnh đáy lớn là $%s$ m; cạnh đáy nhỏ là $%s$ m; chiều cao là $%s$ m. Người ta đổ đất vào chậu, biết rằng $1$ m$^3$ đất có khối lượng $%s$ tấn. Hỏi chậu chứa đầy sẽ có khối lượng đất bao nhiêu tấn (không làm tròn kết quả các phép tính trung gian, chỉ làm tròn kết quả cuối cùng đến hàng phần trăm)?}{%s}'''
                                 % (a_str, b_str, h_str, d_str, hinhve))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Thể tích của chậu trồng cây (hình chóp cụt tứ giác đều) là: \\\\
                         $V = \\frac{1}{3}h \\left( a^2 + b^2 + ab \\right) = \\frac{1}{3} \\cdot %s \\left( %s^2 + %s^2 + %s \\cdot %s \\right) = %s$ (m$^3$). \\\\
                         Khối lượng đất khi chậu chứa đầy là: \\\\
                         $m = V \\cdot d = %s \\cdot %s = %s$ (tấn). \\\\
                         Làm tròn kết quả đến hàng phần trăm, ta được $%s$ tấn.'''
                         % (h_str, a_str, b_str, a_str, b_str, V_str, V_str, d_str, M_str, kq))
                dapan='\\shortans[0]{$%s$}\n'%(kq)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content


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


def bt_dang62_p3_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random nửa trục lớn m (để đảm bảo tính toán ra số nguyên đẹp, m là bội của 4)
                m = random.choice([4, 8, 12]) 

                # Random chi phí nguyên vật liệu (đơn vị: nghìn đồng)
                c1 = random.choice([4, 5, 6, 8])
                c2 = random.choice([12, 15, 18, 20])

                # Format chi phí có dấu chấm phân cách hàng nghìn (VD: 5.000)
                c1_str = f"{c1 * 1000:,}".replace(',', '.')
                c2_str = f"{c2 * 1000:,}".replace(',', '.')

                # Tính diện tích (lưu giá trị thực để tính toán)
                S1 = math.pi * (m**2 / 2)
                S2 = math.pi * (4 * m**2 / (3 * math.sqrt(3)) - m**2 / 2)

                # Tổng chi phí (VND)
                T_val = c1 * 1000 * S1 + c2 * 1000 * S2
                T_rounded = round(T_val) # Làm tròn đến hàng đơn vị của đồng
                T_vnd_str = f"{T_rounded:,}".replace(',', '.')

                # Đổi sang đơn vị nghìn đồng
                T_nghin_val = T_val / 1000
                T_nghin_rounded = round(T_nghin_val)
                T_nghin_str = str(T_nghin_rounded)

                kq = T_nghin_str
                kq_num = T_nghin_rounded

                # Các đáp án trắc nghiệm
                du = [f'${kq}$']
                da = random.choice(du)

                # Tạo các phương án sai ngẫu nhiên
                offsets = [-3, -2, -1, 1, 2, 3, 4, 5, -4, -5]
                random.shuffle(offsets)
                s = []
                for off in offsets[:6]:
                    s.append(f'${kq_num + off}$')

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]
                hinhve=r'''\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\tikzset {_g49hp56bg/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-122 }  \pgftransformscale{2 }  }}}
            	\pgfdeclarehorizontalshading{_8ii25g4km}{150bp}{rgb(0bp)=(0.96,0.65,0.14);
            		rgb(37.5bp)=(0.96,0.65,0.14);
            		rgb(50bp)=(1,1,0);
            		rgb(62.5bp)=(0.96,0.65,0.14);
            		rgb(100bp)=(0.96,0.65,0.14)}
            	\tikzset{every picture/.style={line width=0.75pt}} 
            	\draw  [color={rgb, 255:red, 245; green, 166; blue, 35 }  ,draw opacity=1 ][fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (204.13,23.1) .. controls (225.6,23.1) and (243,62.19) .. (243,110.4) .. controls (243,158.61) and (225.6,197.7) .. (204.13,197.7) .. controls (182.67,197.7) and (165.27,158.61) .. (165.27,110.4) .. controls (165.27,62.19) and (182.67,23.1) .. (204.13,23.1) -- cycle ;
            	\draw  [color={rgb, 255:red, 245; green, 166; blue, 35 }  ,draw opacity=1 ][fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (204.13,33.1) .. controls (224.11,33.1) and (240.3,67.71) .. (240.3,110.4) .. controls (240.3,153.09) and (224.11,187.7) .. (204.13,187.7) .. controls (184.16,187.7) and (167.97,153.09) .. (167.97,110.4) .. controls (167.97,67.71) and (184.16,33.1) .. (204.13,33.1) -- cycle ;
            	\draw  [color={rgb, 255:red, 245; green, 166; blue, 35 }  ,draw opacity=1 ][fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (118.5,110.9) .. controls (118.5,90.47) and (157.59,73.9) .. (205.8,73.9) .. controls (254.01,73.9) and (293.1,90.47) .. (293.1,110.9) .. controls (293.1,131.33) and (254.01,147.9) .. (205.8,147.9) .. controls (157.59,147.9) and (118.5,131.33) .. (118.5,110.9) -- cycle ;
            	\draw  [color={rgb, 255:red, 245; green, 166; blue, 35 }  ,draw opacity=1 ][fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (128.5,110.9) .. controls (128.5,91.88) and (163.11,76.47) .. (205.8,76.47) .. controls (248.49,76.47) and (283.1,91.88) .. (283.1,110.9) .. controls (283.1,129.92) and (248.49,145.33) .. (205.8,145.33) .. controls (163.11,145.33) and (128.5,129.92) .. (128.5,110.9) -- cycle ;
            	\draw  [color={rgb, 255:red, 245; green, 166; blue, 35 }  ,draw opacity=1 ][fill={rgb, 255:red, 242; green, 238; blue, 191 }  ,fill opacity=1 ] (155.1,110.5) .. controls (155.1,83.49) and (176.99,61.6) .. (204,61.6) .. controls (231.01,61.6) and (252.9,83.49) .. (252.9,110.5) .. controls (252.9,137.51) and (231.01,159.4) .. (204,159.4) .. controls (176.99,159.4) and (155.1,137.51) .. (155.1,110.5) -- cycle ;
            	\path  [shading=_8ii25g4km,_g49hp56bg] (161.6,110.5) .. controls (161.6,87.08) and (180.58,68.1) .. (204,68.1) .. controls (227.42,68.1) and (246.4,87.08) .. (246.4,110.5) .. controls (246.4,133.92) and (227.42,152.9) .. (204,152.9) .. controls (180.58,152.9) and (161.6,133.92) .. (161.6,110.5) -- cycle ; 
            	\draw  [color={rgb, 255:red, 245; green, 166; blue, 35 }  ,draw opacity=1 ] (161.6,110.5) .. controls (161.6,87.08) and (180.58,68.1) .. (204,68.1) .. controls (227.42,68.1) and (246.4,87.08) .. (246.4,110.5) .. controls (246.4,133.92) and (227.42,152.9) .. (204,152.9) .. controls (180.58,152.9) and (161.6,133.92) .. (161.6,110.5) -- cycle ; 
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (257.67,106.08) -- (261.92,106.08) -- (261.92,110.33) -- (257.67,110.33) -- cycle ;
            	\draw [draw opacity=0]   (257.67,106.08) -- (261.92,110.33) ;
            	\draw [draw opacity=0]   (257.67,110.33) -- (261.92,106.08) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (257.67,106.08) -- (261.92,106.08) -- (259.8,108.2) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (259.8,108.2) -- (261.92,110.33) -- (257.67,110.33) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (257.67,106.08) -- (259.17,106.07) -- (259.8,108.2) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (259.8,108.2) -- (260.23,110.32) -- (261.92,110.33) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (259.8,108.2) -- (261.89,107.47) -- (261.93,108.71) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (257.72,107.6) -- (259.76,108.29) -- (257.68,108.41) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (252,130.41) -- (256.26,130.41) -- (256.26,134.67) -- (252,134.67) -- cycle ;
            	\draw [draw opacity=0]   (252,130.41) -- (256.26,134.67) ;
            	\draw [draw opacity=0]   (252,134.67) -- (256.26,130.41) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (252,130.41) -- (256.26,130.41) -- (254.13,132.54) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (254.13,132.54) -- (256.26,134.67) -- (252,134.67) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (252,130.41) -- (253.5,130.4) -- (254.13,132.54) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (254.13,132.54) -- (254.56,134.66) -- (256.26,134.67) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (254.13,132.54) -- (256.22,131.81) -- (256.27,133.04) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (252.05,131.93) -- (254.09,132.62) -- (252.01,132.74) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (251.33,87.41) -- (255.59,87.41) -- (255.59,91.67) -- (251.33,91.67) -- cycle ;
            	\draw [draw opacity=0]   (251.33,87.41) -- (255.59,91.67) ;
            	\draw [draw opacity=0]   (251.33,91.67) -- (255.59,87.41) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (251.33,87.41) -- (255.59,87.41) -- (253.46,89.54) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (253.46,89.54) -- (255.59,91.67) -- (251.33,91.67) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (251.33,87.41) -- (252.83,87.4) -- (253.46,89.54) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (253.46,89.54) -- (253.9,91.66) -- (255.59,91.67) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (253.46,89.54) -- (255.56,88.81) -- (255.6,90.04) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (251.38,88.93) -- (253.42,89.62) -- (251.34,89.74) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (256,96.41) -- (260.26,96.41) -- (260.26,100.67) -- (256,100.67) -- cycle ;
            	\draw [draw opacity=0]   (256,96.41) -- (260.26,100.67) ;
            	\draw [draw opacity=0]   (256,100.67) -- (260.26,96.41) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (256,96.41) -- (260.26,96.41) -- (258.13,98.54) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (258.13,98.54) -- (260.26,100.67) -- (256,100.67) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (256,96.41) -- (257.5,96.4) -- (258.13,98.54) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (258.13,98.54) -- (258.56,100.66) -- (260.26,100.67) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (258.13,98.54) -- (260.22,97.81) -- (260.27,99.04) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (256.05,97.93) -- (258.09,98.62) -- (256.01,98.74) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (256,118.41) -- (260.26,118.41) -- (260.26,122.67) -- (256,122.67) -- cycle ;
            	\draw [draw opacity=0]   (256,118.41) -- (260.26,122.67) ;
            	\draw [draw opacity=0]   (256,122.67) -- (260.26,118.41) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (256,118.41) -- (260.26,118.41) -- (258.13,120.54) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (258.13,120.54) -- (260.26,122.67) -- (256,122.67) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (256,118.41) -- (257.5,118.4) -- (258.13,120.54) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (258.13,120.54) -- (258.56,122.66) -- (260.26,122.67) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (258.13,120.54) -- (260.22,119.81) -- (260.27,121.04) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (256.05,119.93) -- (258.09,120.62) -- (256.01,120.74) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (261,90.08) -- (265.26,90.08) -- (265.26,94.33) -- (261,94.33) -- cycle ;
            	\draw [draw opacity=0]   (261,90.08) -- (265.26,94.33) ;
            	\draw [draw opacity=0]   (261,94.33) -- (265.26,90.08) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (261,90.08) -- (265.26,90.08) -- (263.13,92.2) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (263.13,92.2) -- (265.26,94.33) -- (261,94.33) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (261,90.08) -- (262.5,90.07) -- (263.13,92.2) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (263.13,92.2) -- (263.56,94.32) -- (265.26,94.33) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (263.13,92.2) -- (265.22,91.47) -- (265.27,92.71) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (261.05,91.6) -- (263.09,92.29) -- (261.01,92.41) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (262.67,100.41) -- (266.92,100.41) -- (266.92,104.67) -- (262.67,104.67) -- cycle ;
            	\draw [draw opacity=0]   (262.67,100.41) -- (266.92,104.67) ;
            	\draw [draw opacity=0]   (262.67,104.67) -- (266.92,100.41) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (262.67,100.41) -- (266.92,100.41) -- (264.8,102.54) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (264.8,102.54) -- (266.92,104.67) -- (262.67,104.67) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (262.67,100.41) -- (264.17,100.4) -- (264.8,102.54) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (264.8,102.54) -- (265.23,104.66) -- (266.92,104.67) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (264.8,102.54) -- (266.89,101.81) -- (266.93,103.04) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (262.72,101.93) -- (264.76,102.62) -- (262.68,102.74) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (262.67,112.41) -- (266.92,112.41) -- (266.92,116.67) -- (262.67,116.67) -- cycle ;
            	\draw [draw opacity=0]   (262.67,112.41) -- (266.92,116.67) ;
            	\draw [draw opacity=0]   (262.67,116.67) -- (266.92,112.41) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (262.67,112.41) -- (266.92,112.41) -- (264.8,114.54) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (264.8,114.54) -- (266.92,116.67) -- (262.67,116.67) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (262.67,112.41) -- (264.17,112.4) -- (264.8,114.54) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (264.8,114.54) -- (265.23,116.66) -- (266.92,116.67) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (264.8,114.54) -- (266.89,113.81) -- (266.93,115.04) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (262.72,113.93) -- (264.76,114.62) -- (262.68,114.74) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (260,124.74) -- (264.26,124.74) -- (264.26,129) -- (260,129) -- cycle ;
            	\draw [draw opacity=0]   (260,124.74) -- (264.26,129) ;
            	\draw [draw opacity=0]   (260,129) -- (264.26,124.74) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (260,124.74) -- (264.26,124.74) -- (262.13,126.87) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (262.13,126.87) -- (264.26,129) -- (260,129) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (260,124.74) -- (261.5,124.73) -- (262.13,126.87) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (262.13,126.87) -- (262.56,128.99) -- (264.26,129) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (262.13,126.87) -- (264.22,126.14) -- (264.27,127.37) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (260.05,126.27) -- (262.09,126.95) -- (260.01,127.08) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (267.33,95.41) -- (271.59,95.41) -- (271.59,99.67) -- (267.33,99.67) -- cycle ;
            	\draw [draw opacity=0]   (267.33,95.41) -- (271.59,99.67) ;
            	\draw [draw opacity=0]   (267.33,99.67) -- (271.59,95.41) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (267.33,95.41) -- (271.59,95.41) -- (269.46,97.54) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (269.46,97.54) -- (271.59,99.67) -- (267.33,99.67) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (267.33,95.41) -- (268.83,95.4) -- (269.46,97.54) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (269.46,97.54) -- (269.9,99.66) -- (271.59,99.67) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (269.46,97.54) -- (271.56,96.81) -- (271.6,98.04) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (267.38,96.93) -- (269.42,97.62) -- (267.34,97.74) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (269,106.74) -- (273.26,106.74) -- (273.26,111) -- (269,111) -- cycle ;
            	\draw [draw opacity=0]   (269,106.74) -- (273.26,111) ;
            	\draw [draw opacity=0]   (269,111) -- (273.26,106.74) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (269,106.74) -- (273.26,106.74) -- (271.13,108.87) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (271.13,108.87) -- (273.26,111) -- (269,111) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (269,106.74) -- (270.5,106.73) -- (271.13,108.87) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (271.13,108.87) -- (271.56,110.99) -- (273.26,111) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (271.13,108.87) -- (273.22,108.14) -- (273.27,109.37) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (269.05,108.27) -- (271.09,108.95) -- (269.01,109.08) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (267.67,118.74) -- (271.92,118.74) -- (271.92,123) -- (267.67,123) -- cycle ;
            	\draw [draw opacity=0]   (267.67,118.74) -- (271.92,123) ;
            	\draw [draw opacity=0]   (267.67,123) -- (271.92,118.74) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (267.67,118.74) -- (271.92,118.74) -- (269.8,120.87) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (269.8,120.87) -- (271.92,123) -- (267.67,123) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (267.67,118.74) -- (269.17,118.73) -- (269.8,120.87) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (269.8,120.87) -- (270.23,122.99) -- (271.92,123) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (269.8,120.87) -- (271.89,120.14) -- (271.93,121.37) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (267.72,120.27) -- (269.76,120.95) -- (267.68,121.08) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (273.67,101.08) -- (277.92,101.08) -- (277.92,105.33) -- (273.67,105.33) -- cycle ;
            	\draw [draw opacity=0]   (273.67,101.08) -- (277.92,105.33) ;
            	\draw [draw opacity=0]   (273.67,105.33) -- (277.92,101.08) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (273.67,101.08) -- (277.92,101.08) -- (275.8,103.2) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (275.8,103.2) -- (277.92,105.33) -- (273.67,105.33) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (273.67,101.08) -- (275.17,101.07) -- (275.8,103.2) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (275.8,103.2) -- (276.23,105.32) -- (277.92,105.33) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (275.8,103.2) -- (277.89,102.47) -- (277.93,103.71) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (273.72,102.6) -- (275.76,103.29) -- (273.68,103.41) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (274.33,112.41) -- (278.59,112.41) -- (278.59,116.67) -- (274.33,116.67) -- cycle ;
            	\draw [draw opacity=0]   (274.33,112.41) -- (278.59,116.67) ;
            	\draw [draw opacity=0]   (274.33,116.67) -- (278.59,112.41) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (274.33,112.41) -- (278.59,112.41) -- (276.46,114.54) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (276.46,114.54) -- (278.59,116.67) -- (274.33,116.67) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (274.33,112.41) -- (275.83,112.4) -- (276.46,114.54) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (276.46,114.54) -- (276.9,116.66) -- (278.59,116.67) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (276.46,114.54) -- (278.56,113.81) -- (278.6,115.04) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (274.38,113.93) -- (276.42,114.62) -- (274.34,114.74) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (151.25,106.74) -- (147.16,106.74) -- (147.16,111) -- (151.25,111) -- cycle ;
            	\draw [draw opacity=0]   (151.25,106.74) -- (147.16,111) ;
            	\draw [draw opacity=0]   (151.25,111) -- (147.16,106.74) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (151.25,106.74) -- (147.16,106.74) -- (149.2,108.87) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (149.2,108.87) -- (147.16,111) -- (151.25,111) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (151.25,106.74) -- (149.81,106.73) -- (149.2,108.87) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (149.2,108.87) -- (148.78,110.99) -- (147.16,111) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (149.2,108.87) -- (147.19,108.14) -- (147.15,109.37) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (151.2,108.27) -- (149.24,108.95) -- (151.24,109.08) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (156.69,131.08) -- (152.6,131.08) -- (152.6,135.33) -- (156.69,135.33) -- cycle ;
            	\draw [draw opacity=0]   (156.69,131.08) -- (152.6,135.33) ;
            	\draw [draw opacity=0]   (156.69,135.33) -- (152.6,131.08) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (156.69,131.08) -- (152.6,131.08) -- (154.65,133.2) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (154.65,133.2) -- (152.6,135.33) -- (156.69,135.33) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (156.69,131.08) -- (155.25,131.07) -- (154.65,133.2) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (154.65,133.2) -- (154.23,135.32) -- (152.6,135.33) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (154.65,133.2) -- (152.63,132.47) -- (152.59,133.71) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (156.64,132.6) -- (154.68,133.29) -- (156.68,133.41) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (157.33,88.08) -- (153.24,88.08) -- (153.24,92.33) -- (157.33,92.33) -- cycle ;
            	\draw [draw opacity=0]   (157.33,88.08) -- (153.24,92.33) ;
            	\draw [draw opacity=0]   (157.33,92.33) -- (153.24,88.08) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (157.33,88.08) -- (153.24,88.08) -- (155.29,90.2) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (155.29,90.2) -- (153.24,92.33) -- (157.33,92.33) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (157.33,88.08) -- (155.89,88.07) -- (155.29,90.2) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (155.29,90.2) -- (154.87,92.32) -- (153.24,92.33) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (155.29,90.2) -- (153.27,89.47) -- (153.23,90.71) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (157.28,89.6) -- (155.32,90.29) -- (157.33,90.41) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (152.85,97.08) -- (148.76,97.08) -- (148.76,101.33) -- (152.85,101.33) -- cycle ;
            	\draw [draw opacity=0]   (152.85,97.08) -- (148.76,101.33) ;
            	\draw [draw opacity=0]   (152.85,101.33) -- (148.76,97.08) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (152.85,97.08) -- (148.76,97.08) -- (150.8,99.2) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (150.8,99.2) -- (148.76,101.33) -- (152.85,101.33) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (152.85,97.08) -- (151.41,97.07) -- (150.8,99.2) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (150.8,99.2) -- (150.39,101.32) -- (148.76,101.33) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (150.8,99.2) -- (148.79,98.47) -- (148.75,99.71) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (152.8,98.6) -- (150.84,99.29) -- (152.84,99.41) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (152.85,119.08) -- (148.76,119.08) -- (148.76,123.33) -- (152.85,123.33) -- cycle ;
            	\draw [draw opacity=0]   (152.85,119.08) -- (148.76,123.33) ;
            	\draw [draw opacity=0]   (152.85,123.33) -- (148.76,119.08) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (152.85,119.08) -- (148.76,119.08) -- (150.8,121.2) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (150.8,121.2) -- (148.76,123.33) -- (152.85,123.33) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (152.85,119.08) -- (151.41,119.07) -- (150.8,121.2) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (150.8,121.2) -- (150.39,123.32) -- (148.76,123.33) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (150.8,121.2) -- (148.79,120.47) -- (148.75,121.71) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (152.8,120.6) -- (150.84,121.29) -- (152.84,121.41) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (148.04,90.74) -- (143.95,90.74) -- (143.95,95) -- (148.04,95) -- cycle ;
            	\draw [draw opacity=0]   (148.04,90.74) -- (143.95,95) ;
            	\draw [draw opacity=0]   (148.04,95) -- (143.95,90.74) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (148.04,90.74) -- (143.95,90.74) -- (146,92.87) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (146,92.87) -- (143.95,95) -- (148.04,95) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (148.04,90.74) -- (146.6,90.73) -- (146,92.87) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (146,92.87) -- (145.58,94.99) -- (143.95,95) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (146,92.87) -- (143.99,92.14) -- (143.95,93.37) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (148,92.27) -- (146.04,92.95) -- (148.04,93.08) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (146.44,101.08) -- (142.35,101.08) -- (142.35,105.33) -- (146.44,105.33) -- cycle ;
            	\draw [draw opacity=0]   (146.44,101.08) -- (142.35,105.33) ;
            	\draw [draw opacity=0]   (146.44,105.33) -- (142.35,101.08) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (146.44,101.08) -- (142.35,101.08) -- (144.4,103.2) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (144.4,103.2) -- (142.35,105.33) -- (146.44,105.33) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (146.44,101.08) -- (145,101.07) -- (144.4,103.2) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (144.4,103.2) -- (143.98,105.32) -- (142.35,105.33) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (144.4,103.2) -- (142.38,102.47) -- (142.34,103.71) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (146.39,102.6) -- (144.43,103.29) -- (146.44,103.41) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (146.44,113.08) -- (142.35,113.08) -- (142.35,117.33) -- (146.44,117.33) -- cycle ;
            	\draw [draw opacity=0]   (146.44,113.08) -- (142.35,117.33) ;
            	\draw [draw opacity=0]   (146.44,117.33) -- (142.35,113.08) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (146.44,113.08) -- (142.35,113.08) -- (144.4,115.2) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (144.4,115.2) -- (142.35,117.33) -- (146.44,117.33) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (146.44,113.08) -- (145,113.07) -- (144.4,115.2) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (144.4,115.2) -- (143.98,117.32) -- (142.35,117.33) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (144.4,115.2) -- (142.38,114.47) -- (142.34,115.71) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (146.39,114.6) -- (144.43,115.29) -- (146.44,115.41) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (149.01,125.41) -- (144.91,125.41) -- (144.91,129.67) -- (149.01,129.67) -- cycle ;
            	\draw [draw opacity=0]   (149.01,125.41) -- (144.91,129.67) ;
            	\draw [draw opacity=0]   (149.01,129.67) -- (144.91,125.41) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (149.01,125.41) -- (144.91,125.41) -- (146.96,127.54) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (146.96,127.54) -- (144.91,129.67) -- (149.01,129.67) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (149.01,125.41) -- (147.57,125.4) -- (146.96,127.54) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (146.96,127.54) -- (146.54,129.66) -- (144.91,129.67) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (146.96,127.54) -- (144.95,126.81) -- (144.91,128.04) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (148.96,126.93) -- (147,127.62) -- (149,127.74) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (141.96,96.08) -- (137.87,96.08) -- (137.87,100.33) -- (141.96,100.33) -- cycle ;
            	\draw [draw opacity=0]   (141.96,96.08) -- (137.87,100.33) ;
            	\draw [draw opacity=0]   (141.96,100.33) -- (137.87,96.08) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (141.96,96.08) -- (137.87,96.08) -- (139.91,98.2) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (139.91,98.2) -- (137.87,100.33) -- (141.96,100.33) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (141.96,96.08) -- (140.52,96.07) -- (139.91,98.2) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (139.91,98.2) -- (139.5,100.32) -- (137.87,100.33) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (139.91,98.2) -- (137.9,97.47) -- (137.86,98.71) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (141.91,97.6) -- (139.95,98.29) -- (141.95,98.41) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (140.36,107.41) -- (136.27,107.41) -- (136.27,111.67) -- (140.36,111.67) -- cycle ;
            	\draw [draw opacity=0]   (140.36,107.41) -- (136.27,111.67) ;
            	\draw [draw opacity=0]   (140.36,111.67) -- (136.27,107.41) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (140.36,107.41) -- (136.27,107.41) -- (138.31,109.54) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (138.31,109.54) -- (136.27,111.67) -- (140.36,111.67) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (140.36,107.41) -- (138.92,107.4) -- (138.31,109.54) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (138.31,109.54) -- (137.89,111.66) -- (136.27,111.67) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (138.31,109.54) -- (136.3,108.81) -- (136.26,110.04) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (140.31,108.93) -- (138.35,109.62) -- (140.35,109.74) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (141.64,119.41) -- (137.55,119.41) -- (137.55,123.67) -- (141.64,123.67) -- cycle ;
            	\draw [draw opacity=0]   (141.64,119.41) -- (137.55,123.67) ;
            	\draw [draw opacity=0]   (141.64,123.67) -- (137.55,119.41) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (141.64,119.41) -- (137.55,119.41) -- (139.59,121.54) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (139.59,121.54) -- (137.55,123.67) -- (141.64,123.67) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (141.64,119.41) -- (140.2,119.4) -- (139.59,121.54) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (139.59,121.54) -- (139.18,123.66) -- (137.55,123.67) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (139.59,121.54) -- (137.58,120.81) -- (137.54,122.04) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (141.59,120.93) -- (139.63,121.62) -- (141.63,121.74) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (135.87,101.74) -- (131.78,101.74) -- (131.78,106) -- (135.87,106) -- cycle ;
            	\draw [draw opacity=0]   (135.87,101.74) -- (131.78,106) ;
            	\draw [draw opacity=0]   (135.87,106) -- (131.78,101.74) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (135.87,101.74) -- (131.78,101.74) -- (133.83,103.87) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (133.83,103.87) -- (131.78,106) -- (135.87,106) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (135.87,101.74) -- (134.43,101.73) -- (133.83,103.87) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (133.83,103.87) -- (133.41,105.99) -- (131.78,106) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (133.83,103.87) -- (131.81,103.14) -- (131.77,104.37) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (135.82,103.27) -- (133.86,103.95) -- (135.87,104.08) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (135.23,113.08) -- (131.14,113.08) -- (131.14,117.33) -- (135.23,117.33) -- cycle ;
            	\draw [draw opacity=0]   (135.23,113.08) -- (131.14,117.33) ;
            	\draw [draw opacity=0]   (135.23,117.33) -- (131.14,113.08) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (135.23,113.08) -- (131.14,113.08) -- (133.19,115.2) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (133.19,115.2) -- (131.14,117.33) -- (135.23,117.33) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (135.23,113.08) -- (133.79,113.07) -- (133.19,115.2) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (133.19,115.2) -- (132.77,117.32) -- (131.14,117.33) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (133.19,115.2) -- (131.17,114.47) -- (131.13,115.71) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (135.18,114.6) -- (133.22,115.29) -- (135.22,115.41) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (200.64,57.98) -- (200.66,53.72) -- (204.92,53.74) -- (204.9,58) -- cycle ;
            	\draw [draw opacity=0]   (200.64,57.98) -- (204.92,53.74) ;
            	\draw [draw opacity=0]   (204.9,58) -- (200.66,53.72) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (200.64,57.98) -- (200.66,53.72) -- (202.78,55.86) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (202.78,55.86) -- (204.92,53.74) -- (204.9,58) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (200.64,57.98) -- (200.64,56.48) -- (202.78,55.86) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (202.78,55.86) -- (204.9,55.43) -- (204.92,53.74) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (202.78,55.86) -- (202.06,53.76) -- (203.29,53.72) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (202.17,57.93) -- (202.86,55.9) -- (202.98,57.98) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (224.95,63.75) -- (224.97,59.5) -- (229.23,59.52) -- (229.21,63.77) -- cycle ;
            	\draw [draw opacity=0]   (224.95,63.75) -- (229.23,59.52) ;
            	\draw [draw opacity=0]   (229.21,63.77) -- (224.97,59.5) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (224.95,63.75) -- (224.97,59.5) -- (227.09,61.64) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (227.09,61.64) -- (229.23,59.52) -- (229.21,63.77) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (224.95,63.75) -- (224.95,62.26) -- (227.09,61.64) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (227.09,61.64) -- (229.21,61.21) -- (229.23,59.52) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (227.09,61.64) -- (226.37,59.54) -- (227.6,59.5) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (226.47,63.71) -- (227.17,61.67) -- (227.28,63.76) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (181.95,64.23) -- (181.97,59.97) -- (186.22,59.99) -- (186.21,64.25) -- cycle ;
            	\draw [draw opacity=0]   (181.95,64.23) -- (186.22,59.99) ;
            	\draw [draw opacity=0]   (186.21,64.25) -- (181.97,59.97) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (181.95,64.23) -- (181.97,59.97) -- (184.09,62.11) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (184.09,62.11) -- (186.22,59.99) -- (186.21,64.25) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (181.95,64.23) -- (181.95,62.73) -- (184.09,62.11) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (184.09,62.11) -- (186.21,61.68) -- (186.22,59.99) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (184.09,62.11) -- (183.36,60.01) -- (184.6,59.97) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (183.47,64.18) -- (184.17,62.15) -- (184.28,64.23) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (190.97,59.6) -- (190.99,55.34) -- (195.25,55.36) -- (195.23,59.62) -- cycle ;
            	\draw [draw opacity=0]   (190.97,59.6) -- (195.25,55.36) ;
            	\draw [draw opacity=0]   (195.23,59.62) -- (190.99,55.34) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (190.97,59.6) -- (190.99,55.34) -- (193.11,57.48) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (193.11,57.48) -- (195.25,55.36) -- (195.23,59.62) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (190.97,59.6) -- (190.97,58.1) -- (193.11,57.48) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (193.11,57.48) -- (195.23,57.06) -- (195.25,55.36) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (193.11,57.48) -- (192.38,55.38) -- (193.62,55.35) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (192.49,59.56) -- (193.19,57.52) -- (193.3,59.6) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (212.97,59.7) -- (212.99,55.44) -- (217.25,55.46) -- (217.23,59.72) -- cycle ;
            	\draw [draw opacity=0]   (212.97,59.7) -- (217.25,55.46) ;
            	\draw [draw opacity=0]   (217.23,59.72) -- (212.99,55.44) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (212.97,59.7) -- (212.99,55.44) -- (215.11,57.58) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (215.11,57.58) -- (217.25,55.46) -- (217.23,59.72) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (212.97,59.7) -- (212.97,58.2) -- (215.11,57.58) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (215.11,57.58) -- (217.23,57.16) -- (217.25,55.46) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (215.11,57.58) -- (214.38,55.48) -- (215.62,55.45) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (214.49,59.66) -- (215.19,57.62) -- (215.3,59.7) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (184.66,54.57) -- (184.68,50.31) -- (188.93,50.33) -- (188.92,54.59) -- cycle ;
            	\draw [draw opacity=0]   (184.66,54.57) -- (188.93,50.33) ;
            	\draw [draw opacity=0]   (188.92,54.59) -- (184.68,50.31) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (184.66,54.57) -- (184.68,50.31) -- (186.8,52.45) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (186.8,52.45) -- (188.93,50.33) -- (188.92,54.59) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (184.66,54.57) -- (184.66,53.07) -- (186.8,52.45) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (186.8,52.45) -- (188.92,52.03) -- (188.93,50.33) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (186.8,52.45) -- (186.07,50.35) -- (187.31,50.32) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (186.18,54.53) -- (186.88,52.49) -- (186.99,54.57) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (195,52.95) -- (195.02,48.69) -- (199.28,48.71) -- (199.26,52.97) -- cycle ;
            	\draw [draw opacity=0]   (195,52.95) -- (199.28,48.71) ;
            	\draw [draw opacity=0]   (199.26,52.97) -- (195.02,48.69) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (195,52.95) -- (195.02,48.69) -- (197.14,50.83) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (197.14,50.83) -- (199.28,48.71) -- (199.26,52.97) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (195,52.95) -- (195,51.45) -- (197.14,50.83) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (197.14,50.83) -- (199.26,50.41) -- (199.28,48.71) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (197.14,50.83) -- (196.41,48.73) -- (197.65,48.7) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (196.52,52.91) -- (197.22,50.87) -- (197.33,52.95) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (207,53.01) -- (207.02,48.75) -- (211.28,48.77) -- (211.26,53.03) -- cycle ;
            	\draw [draw opacity=0]   (207,53.01) -- (211.28,48.77) ;
            	\draw [draw opacity=0]   (211.26,53.03) -- (207.02,48.75) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (207,53.01) -- (207.02,48.75) -- (209.14,50.89) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (209.14,50.89) -- (211.28,48.77) -- (211.26,53.03) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (207,53.01) -- (207,51.51) -- (209.14,50.89) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (209.14,50.89) -- (211.26,50.46) -- (211.28,48.77) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (209.14,50.89) -- (208.41,48.79) -- (209.65,48.75) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (208.52,52.96) -- (209.22,50.93) -- (209.33,53.01) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (219.32,55.73) -- (219.34,51.47) -- (223.6,51.49) -- (223.58,55.75) -- cycle ;
            	\draw [draw opacity=0]   (219.32,55.73) -- (223.6,51.49) ;
            	\draw [draw opacity=0]   (223.58,55.75) -- (219.34,51.47) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (219.32,55.73) -- (219.34,51.47) -- (221.46,53.61) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (221.46,53.61) -- (223.6,51.49) -- (223.58,55.75) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (219.32,55.73) -- (219.32,54.23) -- (221.46,53.61) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (221.46,53.61) -- (223.58,53.18) -- (223.6,51.49) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (221.46,53.61) -- (220.73,51.51) -- (221.97,51.47) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (220.84,55.68) -- (221.54,53.65) -- (221.65,55.73) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (190.02,48.26) -- (190.04,44) -- (194.3,44.02) -- (194.28,48.28) -- cycle ;
            	\draw [draw opacity=0]   (190.02,48.26) -- (194.3,44.02) ;
            	\draw [draw opacity=0]   (194.28,48.28) -- (190.04,44) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (190.02,48.26) -- (190.04,44) -- (192.16,46.14) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (192.16,46.14) -- (194.3,44.02) -- (194.28,48.28) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (190.02,48.26) -- (190.02,46.76) -- (192.16,46.14) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (192.16,46.14) -- (194.28,45.72) -- (194.3,44.02) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (192.16,46.14) -- (191.44,44.04) -- (192.67,44.01) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (191.54,48.22) -- (192.24,46.18) -- (192.35,48.26) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (201.36,46.65) -- (201.38,42.39) -- (205.64,42.41) -- (205.62,46.67) -- cycle ;
            	\draw [draw opacity=0]   (201.36,46.65) -- (205.64,42.41) ;
            	\draw [draw opacity=0]   (205.62,46.67) -- (201.38,42.39) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (201.36,46.65) -- (201.38,42.39) -- (203.5,44.53) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (203.5,44.53) -- (205.64,42.41) -- (205.62,46.67) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (201.36,46.65) -- (201.36,45.15) -- (203.5,44.53) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (203.5,44.53) -- (205.62,44.1) -- (205.64,42.41) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (203.5,44.53) -- (202.78,42.43) -- (204.01,42.39) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (202.88,46.6) -- (203.58,44.57) -- (203.69,46.65) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (213.35,48.04) -- (213.37,43.78) -- (217.63,43.8) -- (217.61,48.05) -- cycle ;
            	\draw [draw opacity=0]   (213.35,48.04) -- (217.63,43.8) ;
            	\draw [draw opacity=0]   (217.61,48.05) -- (213.37,43.78) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (213.35,48.04) -- (213.37,43.78) -- (215.49,45.92) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (215.49,45.92) -- (217.63,43.8) -- (217.61,48.05) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (213.35,48.04) -- (213.35,46.54) -- (215.49,45.92) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (215.49,45.92) -- (217.62,45.49) -- (217.63,43.8) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (215.49,45.92) -- (214.77,43.82) -- (216,43.78) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (214.88,47.99) -- (215.57,45.95) -- (215.69,48.04) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (195.71,41.95) -- (195.73,37.7) -- (199.99,37.72) -- (199.97,41.97) -- cycle ;
            	\draw [draw opacity=0]   (195.71,41.95) -- (199.99,37.72) ;
            	\draw [draw opacity=0]   (199.97,41.97) -- (195.73,37.7) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (195.71,41.95) -- (195.73,37.7) -- (197.85,39.84) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (197.85,39.84) -- (199.99,37.72) -- (199.97,41.97) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (195.71,41.95) -- (195.71,40.46) -- (197.85,39.84) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (197.85,39.84) -- (199.98,39.41) -- (199.99,37.72) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (197.85,39.84) -- (197.13,37.74) -- (198.37,37.7) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (197.24,41.91) -- (197.93,39.87) -- (198.05,41.96) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (207.05,41.34) -- (207.07,37.08) -- (211.33,37.1) -- (211.31,41.36) -- cycle ;
            	\draw [draw opacity=0]   (207.05,41.34) -- (211.33,37.1) ;
            	\draw [draw opacity=0]   (211.31,41.36) -- (207.07,37.08) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (207.05,41.34) -- (207.07,37.08) -- (209.19,39.22) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (209.19,39.22) -- (211.33,37.1) -- (211.31,41.36) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (207.05,41.34) -- (207.05,39.84) -- (209.19,39.22) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (209.19,39.22) -- (211.31,38.8) -- (211.33,37.1) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (209.19,39.22) -- (208.47,37.12) -- (209.7,37.08) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (208.58,41.3) -- (209.27,39.26) -- (209.38,41.34) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (208.25,162.18) -- (208.45,166.43) -- (204.19,166.63) -- (204,162.38) -- cycle ;
            	\draw [draw opacity=0]   (208.25,162.18) -- (204.19,166.63) ;
            	\draw [draw opacity=0]   (204,162.38) -- (208.45,166.43) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (208.25,162.18) -- (208.45,166.43) -- (206.22,164.4) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (206.22,164.4) -- (204.19,166.63) -- (204,162.38) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (208.25,162.18) -- (208.33,163.68) -- (206.22,164.4) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (206.22,164.4) -- (204.12,164.94) -- (204.19,166.63) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (206.22,164.4) -- (207.05,166.46) -- (205.82,166.56) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (206.73,162.3) -- (206.14,164.37) -- (205.92,162.3) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (183.68,157.64) -- (183.88,161.89) -- (179.63,162.09) -- (179.43,157.83) -- cycle ;
            	\draw [draw opacity=0]   (183.68,157.64) -- (179.63,162.09) ;
            	\draw [draw opacity=0]   (179.43,157.83) -- (183.88,161.89) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (183.68,157.64) -- (183.88,161.89) -- (181.65,159.86) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (181.65,159.86) -- (179.63,162.09) -- (179.43,157.83) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (183.68,157.64) -- (183.76,159.13) -- (181.65,159.86) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (181.65,159.86) -- (179.56,160.39) -- (179.63,162.09) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (181.65,159.86) -- (182.48,161.92) -- (181.25,162.02) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (182.16,157.76) -- (181.57,159.83) -- (181.35,157.75) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (227.61,157) -- (227.8,161.25) -- (223.55,161.45) -- (223.35,157.19) -- cycle ;
            	\draw [draw opacity=0]   (227.61,157) -- (223.55,161.45) ;
            	\draw [draw opacity=0]   (223.35,157.19) -- (227.8,161.25) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (227.61,157) -- (227.8,161.25) -- (225.58,159.22) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (225.58,159.22) -- (223.55,161.45) -- (223.35,157.19) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (227.61,157) -- (227.69,158.49) -- (225.58,159.22) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (225.58,159.22) -- (223.48,159.75) -- (223.55,161.45) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (225.58,159.22) -- (226.41,161.28) -- (225.17,161.38) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (226.09,157.12) -- (225.5,159.19) -- (225.28,157.11) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (217.83,160.07) -- (218.03,164.33) -- (213.77,164.52) -- (213.58,160.27) -- cycle ;
            	\draw [draw opacity=0]   (217.83,160.07) -- (213.77,164.52) ;
            	\draw [draw opacity=0]   (213.58,160.27) -- (218.03,164.33) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (217.83,160.07) -- (218.03,164.33) -- (215.8,162.3) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (215.8,162.3) -- (213.77,164.52) -- (213.58,160.27) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (217.83,160.07) -- (217.91,161.57) -- (215.8,162.3) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (215.8,162.3) -- (213.7,162.83) -- (213.77,164.52) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (215.8,162.3) -- (216.63,164.36) -- (215.4,164.45) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (216.31,160.19) -- (215.72,162.26) -- (215.5,160.19) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (195.85,161.08) -- (196.05,165.33) -- (191.8,165.53) -- (191.6,161.28) -- cycle ;
            	\draw [draw opacity=0]   (195.85,161.08) -- (191.8,165.53) ;
            	\draw [draw opacity=0]   (191.6,161.28) -- (196.05,165.33) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (195.85,161.08) -- (196.05,165.33) -- (193.83,163.31) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (193.83,163.31) -- (191.8,165.53) -- (191.6,161.28) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (195.85,161.08) -- (195.93,162.58) -- (193.83,163.31) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (193.83,163.31) -- (191.73,163.84) -- (191.8,165.53) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (193.83,163.31) -- (194.65,165.36) -- (193.42,165.46) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (194.33,161.2) -- (193.74,163.27) -- (193.52,161.2) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (224.39,164.78) -- (224.58,169.03) -- (220.33,169.22) -- (220.13,164.97) -- cycle ;
            	\draw [draw opacity=0]   (224.39,164.78) -- (220.33,169.22) ;
            	\draw [draw opacity=0]   (220.13,164.97) -- (224.58,169.03) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (224.39,164.78) -- (224.58,169.03) -- (222.36,167) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (222.36,167) -- (220.33,169.22) -- (220.13,164.97) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (224.39,164.78) -- (224.46,166.27) -- (222.36,167) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (222.36,167) -- (220.26,167.53) -- (220.33,169.22) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (222.36,167) -- (223.19,169.06) -- (221.95,169.16) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (222.87,164.9) -- (222.28,166.97) -- (222.06,164.89) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (214.14,166.91) -- (214.34,171.17) -- (210.08,171.36) -- (209.89,167.11) -- cycle ;
            	\draw [draw opacity=0]   (214.14,166.91) -- (210.08,171.36) ;
            	\draw [draw opacity=0]   (209.89,167.11) -- (214.34,171.17) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (214.14,166.91) -- (214.34,171.17) -- (212.11,169.14) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (212.11,169.14) -- (210.08,171.36) -- (209.89,167.11) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (214.14,166.91) -- (214.22,168.41) -- (212.11,169.14) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (212.11,169.14) -- (210.01,169.67) -- (210.08,171.36) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (212.11,169.14) -- (212.94,171.2) -- (211.71,171.3) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (212.62,167.04) -- (212.03,169.1) -- (211.81,167.03) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (202.15,167.47) -- (202.35,171.72) -- (198.1,171.91) -- (197.9,167.66) -- cycle ;
            	\draw [draw opacity=0]   (202.15,167.47) -- (198.1,171.91) ;
            	\draw [draw opacity=0]   (197.9,167.66) -- (202.35,171.72) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (202.15,167.47) -- (202.35,171.72) -- (200.12,169.69) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (200.12,169.69) -- (198.1,171.91) -- (197.9,167.66) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (202.15,167.47) -- (202.23,168.96) -- (200.12,169.69) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (200.12,169.69) -- (198.03,170.22) -- (198.1,171.91) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (200.12,169.69) -- (200.95,171.75) -- (199.72,171.85) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (200.63,167.59) -- (200.04,169.66) -- (199.82,167.58) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (189.38,164.7) -- (189.57,168.95) -- (185.32,169.15) -- (185.12,164.9) -- cycle ;
            	\draw [draw opacity=0]   (189.38,164.7) -- (185.32,169.15) ;
            	\draw [draw opacity=0]   (185.12,164.9) -- (189.57,168.95) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (189.38,164.7) -- (189.57,168.95) -- (187.35,166.93) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (187.35,166.93) -- (185.32,169.15) -- (185.12,164.9) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (189.38,164.7) -- (189.46,166.2) -- (187.35,166.93) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (187.35,166.93) -- (185.25,167.46) -- (185.32,169.15) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (187.35,166.93) -- (188.18,168.98) -- (186.95,169.08) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (187.86,164.82) -- (187.27,166.89) -- (187.05,164.82) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (219.35,171.35) -- (219.55,175.6) -- (215.29,175.8) -- (215.1,171.54) -- cycle ;
            	\draw [draw opacity=0]   (219.35,171.35) -- (215.29,175.8) ;
            	\draw [draw opacity=0]   (215.1,171.54) -- (219.55,175.6) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (219.35,171.35) -- (219.55,175.6) -- (217.32,173.57) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (217.32,173.57) -- (215.29,175.8) -- (215.1,171.54) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (219.35,171.35) -- (219.43,172.84) -- (217.32,173.57) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (217.32,173.57) -- (215.22,174.1) -- (215.29,175.8) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (217.32,173.57) -- (218.15,175.63) -- (216.92,175.73) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (217.83,171.47) -- (217.24,173.54) -- (217.02,171.46) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (208.11,173.53) -- (208.3,177.79) -- (204.05,177.98) -- (203.85,173.73) -- cycle ;
            	\draw [draw opacity=0]   (208.11,173.53) -- (204.05,177.98) ;
            	\draw [draw opacity=0]   (203.85,173.73) -- (208.3,177.79) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (208.11,173.53) -- (208.3,177.79) -- (206.08,175.76) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (206.08,175.76) -- (204.05,177.98) -- (203.85,173.73) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (208.11,173.53) -- (208.18,175.03) -- (206.08,175.76) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (206.08,175.76) -- (203.98,176.29) -- (204.05,177.98) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (206.08,175.76) -- (206.9,177.82) -- (205.67,177.91) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (206.58,173.65) -- (205.99,175.72) -- (205.77,173.65) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (196.06,172.75) -- (196.25,177) -- (192,177.2) -- (191.8,172.95) -- cycle ;
            	\draw [draw opacity=0]   (196.06,172.75) -- (192,177.2) ;
            	\draw [draw opacity=0]   (191.8,172.95) -- (196.25,177) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (196.06,172.75) -- (196.25,177) -- (194.03,174.98) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (194.03,174.98) -- (192,177.2) -- (191.8,172.95) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (196.06,172.75) -- (196.13,174.25) -- (194.03,174.98) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (194.03,174.98) -- (191.93,175.51) -- (192,177.2) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (194.03,174.98) -- (194.86,177.03) -- (193.62,177.13) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (194.54,172.87) -- (193.95,174.94) -- (193.73,172.87) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (213.98,177.93) -- (214.18,182.19) -- (209.92,182.38) -- (209.73,178.13) -- cycle ;
            	\draw [draw opacity=0]   (213.98,177.93) -- (209.92,182.38) ;
            	\draw [draw opacity=0]   (209.73,178.13) -- (214.18,182.19) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (213.98,177.93) -- (214.18,182.19) -- (211.95,180.16) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (211.95,180.16) -- (209.92,182.38) -- (209.73,178.13) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (213.98,177.93) -- (214.06,179.43) -- (211.95,180.16) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (211.95,180.16) -- (209.85,180.69) -- (209.92,182.38) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (211.95,180.16) -- (212.78,182.22) -- (211.55,182.32) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (212.46,178.05) -- (211.87,180.12) -- (211.65,178.05) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (202.69,179.12) -- (202.88,183.37) -- (198.63,183.57) -- (198.44,179.32) -- cycle ;
            	\draw [draw opacity=0]   (202.69,179.12) -- (198.63,183.57) ;
            	\draw [draw opacity=0]   (198.44,179.32) -- (202.88,183.37) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (202.69,179.12) -- (202.88,183.37) -- (200.66,181.34) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (200.66,181.34) -- (198.63,183.57) -- (198.44,179.32) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (202.69,179.12) -- (202.77,180.62) -- (200.66,181.34) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (200.66,181.34) -- (198.56,181.88) -- (198.63,183.57) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (200.66,181.34) -- (201.49,183.4) -- (200.26,183.5) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.66 ] (201.17,179.24) -- (200.58,181.31) -- (200.36,179.24) -- cycle ;
            \end{tikzpicture}'''
                # Câu hỏi
                noidungcauhoi = (r'''\immini{Để chuẩn bị quà tặng sinh nhật đặc biệt cho các thành viên trong câu lạc bộ nghệ thuật, người ta đặt hàng chế tác một vật phẩm chặn giấy bằng hợp kim cao cấp. Bề mặt của vật phẩm có dạng hai hình elip bằng nhau xếp chồng lên nhau. Biết mỗi elip có độ dài trục lớn bằng $%s$ cm, độ dài trục nhỏ bằng $\frac{%s}{\sqrt{3}}$ cm; trục lớn của elip này vuông góc với trục lớn của elip kia tại giao điểm $O$ của chúng. Đường tròn $(O)$ đi qua các giao điểm của hai elip được vẽ lên bề mặt để phân chia các khu vực trang trí (như hình vẽ). Phần lõi bên trong đường tròn được dát đồng để khắc tên và lời chúc sinh nhật với chi phí $%s$ đồng/cm$^2$. Các phần cánh hoa nằm phía ngoài đường tròn được đính đá Sapphire nhân tạo với chi phí $%s$ đồng/cm$^2$. Hỏi tổng chi phí nguyên vật liệu để chế tác một vật phẩm quà tặng này là bao nhiêu nghìn đồng? (Không làm tròn các kết quả trung gian, chỉ làm tròn kết quả cuối cùng đến hàng đơn vị).}{%s}'''
                                 %(2*m, 2*m, c1_str, c2_str, hinhve))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Chọn hệ trục tọa độ $Oxy$ sao cho tâm $O$ của hai elip trùng với gốc tọa độ, trục lớn của elip thứ nhất nằm trên trục $Ox$, trục lớn của elip thứ hai nằm trên trục $Oy$.\\\\
            Theo giả thiết, trục lớn $2a = %s \\Rightarrow a = %s$; trục nhỏ $2b = \\frac{%s}{\\sqrt{3}} \\Rightarrow b = \\frac{%s}{\\sqrt{3}}$.\\\\
            Phương trình hai elip là: \\\\
            $(E_1): \\frac{x^2}{%s} + \\frac{y^2}{\\frac{%s}{3}} = 1 \\Rightarrow x^2 + 3y^2 = %s$\\\\
            $(E_2): \\frac{x^2}{\\frac{%s}{3}} + \\frac{y^2}{%s} = 1 \\Rightarrow 3x^2 + y^2 = %s$\\\\
            Tọa độ giao điểm của $(E_1)$ và $(E_2)$ thỏa mãn hệ: $\\begin{cases} x^2 + 3y^2 = %s \\\\ 3x^2 + y^2 = %s \\end{cases} \\Rightarrow x^2 = y^2 = %s \\Rightarrow \\begin{cases} x = \\pm %s \\\\ y = \\pm %s \\end{cases}$\\\\
            Đường tròn $(O)$ đi qua các giao điểm có bán kính $R = \\sqrt{x^2 + y^2} = \\sqrt{%s + %s} = \\sqrt{%s}$.\\\\
            Diện tích phần lõi (hình tròn) là $S_1 = \\pi R^2 = %s\\pi$.\\\\
            Diện tích của một elip là $S_E = \\pi a b = \\pi \\cdot %s \\cdot \\frac{%s}{\\sqrt{3}} = \\frac{%s\\pi}{\\sqrt{3}}$.\\\\
            Do tính đối xứng, diện tích phần giao nhau của hai elip bằng 8 lần diện tích phần giao nhau nằm trong góc phần tư thứ nhất và được giới hạn bởi $(E_1)$ và đường phân giác $y=x$.\\\\
            Diện tích này là: $S_g = 8 \\int_0^{%s} \\left( \\frac{1}{\\sqrt{3}}\\sqrt{%s-x^2} - x \\right) \\mathrm{d}x$\\\\
            $= 8 \\left[ \\frac{1}{\\sqrt{3}} \\left( \\frac{x}{2}\\sqrt{%s-x^2} + \\frac{%s}{2}\\arcsin \\frac{x}{%s} \\right) - \\frac{x^2}{2} \\right]_0^{%s} = 8 \\left( \\frac{1}{\\sqrt{3}} \\left( %s\\sqrt{%s} + %s\\arcsin\\frac{1}{2} \\right) - %s \\right) = \\frac{%s\\pi}{3\\sqrt{3}}$.\\\\
            Tổng diện tích bề mặt của vật phẩm (hợp của hai elip) là $S_t = 2S_E - S_g = 2 \\cdot \\frac{%s\\pi}{\\sqrt{3}} - \\frac{%s\\pi}{3\\sqrt{3}} = \\frac{%s\\pi}{3\\sqrt{3}}$.\\\\
            Diện tích các phần cánh hoa là $S_2 = S_t - S_1 = \\frac{%s\\pi}{3\\sqrt{3}} - %s\\pi$.\\\\
            Tổng chi phí chế tác là: \\\\
            $T = %s \\cdot S_1 + %s \\cdot S_2 = %s \\cdot %s\\pi + %s \\cdot \\left( \\frac{%s\\pi}{3\\sqrt{3}} - %s\\pi \\right) \\approx %s$ (đồng).\\\\
            Làm tròn kết quả thu được, ta có tổng chi phí nguyên vật liệu là $%s$ nghìn đồng.'''
                % (2*m, m, 2*m, m, m**2, m**2, m**2, m**2, m**2, m**2, m**2, m**2, m**2//4, m//2, m//2, m**2//4, m**2//4, m**2//2, m**2//2, m, m, m**2, m//2, m**2, m**2, m**2, m, m//2, m//4, 3*m**2//4, m**2//2, m**2//8, 2*m**2, m**2, 2*m**2, 4*m**2, 4*m**2, m**2//2, c1_str, c2_str, c1_str, m**2//2, c2_str, 4*m**2, m**2//2, T_vnd_str, T_nghin_str))
                dapan='\\shortans[0]{$%s$}\n'%(T_nghin_str)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                       '\\loigiai{\n'+str(loigiai)+'\n}\n'
                       '\\end{ex}\n\\end{minipage} \n\n')
            return content


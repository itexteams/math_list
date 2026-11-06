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


def bt_dang34_p3_b2_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Vòng lặp để đảm bảo thông số ngẫu nhiên sinh ra hợp lý về mặt vật lý (y1 > 0)
                while True:
                    a = random.choice([-1, -2]) # Hệ số a âm vì parabol bề lõm hướng xuống
                    xv = random.choice([2, 3])  # Thời gian đạt đỉnh (hoành độ đỉnh d)
                    yv = random.choice([3, 4, 5, 6, 7]) # Độ cao tối đa (tung độ đỉnh)

                    b = -2 * a * xv
                    c = yv + a * (xv**2)
                    y1 = a + b + c # Độ cao sau 1 giây

                    if y1 > 0 and y1 < yv:
                        break

                N = random.choice([2024, 2025, 2026])
                d = xv
                kq_num = N + d

                # Xử lý chuỗi đa thức f(x) hiển thị đẹp trong LaTeX
                term_a = "-x^2" if a == -1 else f"{a}x^2"
                term_b = ""
                if b == 1: term_b = "+ x"
                elif b == -1: term_b = "- x"
                elif b > 0: term_b = f"+ {b}x"
                elif b < 0: term_b = f"- {-b}x"

                term_c = ""
                if c > 0: term_c = f"+ {c}"
                elif c < 0: term_c = f"- {-c}"

                fx_str = f"{term_a} {term_b} {term_c}".strip()

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(kq_num)]
                da = du[0]

                # Tạo các phương án nhiễu (sai) không trùng nhau
                s = ['$%s$'%(kq_num + 1),
                     '$%s$'%(kq_num + 2),
                     '$%s$'%(kq_num + 3),
                     '$%s$'%(kq_num - 1),
                     '$%s$'%(kq_num - 2),
                     '$%s$'%(kq_num - 3),
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                hinhve=r'''\begin{center}
            	\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            		\draw  [fill={rgb, 255:red, 237; green, 195; blue, 127 }  ,fill opacity=1 ][line width=0.75]  (412.42,129.6) -- (528.38,192.69) -- (178.25,194.4) -- (107.2,126.76) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.25 ] (163.76,158.88) .. controls (167.78,156.87) and (171.7,160.19) .. (175.76,160.24) .. controls (191.94,160.45) and (204.45,169.68) .. (176.96,170.64) .. controls (170.56,167.04) and (143.76,168.88) .. (163.76,158.88) -- cycle ;
            		\draw [color={rgb, 255:red, 139; green, 87; blue, 42 }  ,draw opacity=0.57 ][line width=0.75]    (124.82,141.09) -- (430.04,140.97) ;
            		\draw [color={rgb, 255:red, 139; green, 87; blue, 42 }  ,draw opacity=0.57 ][line width=0.75]    (266.35,151.2) -- (445.96,150.07) ;
            		\draw [color={rgb, 255:red, 139; green, 87; blue, 42 }  ,draw opacity=0.57 ][line width=0.75]    (152.1,165.41) -- (331.71,164.28) ;
            		\draw [color={rgb, 255:red, 139; green, 87; blue, 42 }  ,draw opacity=0.57 ][line width=0.75]    (243.04,174.51) -- (422.66,173.37) ;
            		\draw [color={rgb, 255:red, 139; green, 87; blue, 42 }  ,draw opacity=0.57 ][line width=0.75]    (318.64,184.17) -- (498.25,183.03) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.61 ][line width=0.75]    (199.28,136.99) -- (416.4,135.86) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.61 ][line width=0.75]    (244.18,149.5) -- (423.22,147.79) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.61 ][line width=0.75]    (153.81,161.43) -- (322.62,161.43) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.61 ][line width=0.75]    (240.2,175.64) -- (409.01,175.64) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.61 ][line width=0.75]    (286.24,186.44) -- (455.05,186.44) ;
            		\draw [color={rgb, 255:red, 17; green, 57; blue, 105 }  ,draw opacity=1 ][line width=0.75]    (160.9,127.59) -- (238.13,194.33) ;
            		\draw [color={rgb, 255:red, 17; green, 57; blue, 105 }  ,draw opacity=1 ][line width=0.75]    (348.76,129.6) -- (452.13,193.33) ;
            		\draw  [fill={rgb, 255:red, 11; green, 69; blue, 137 }  ,fill opacity=1 ][line width=0.75]  (422.66,173.37) -- (377.13,147.67) -- (297.04,148.64) -- (332.85,173.94) -- cycle ;
            		\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ][line width=0.75]  (287.81,161.86) .. controls (281.76,157.35) and (288,153.69) .. (301.73,153.69) .. controls (315.46,153.69) and (331.5,157.35) .. (337.54,161.86) .. controls (343.58,166.37) and (337.35,170.03) .. (323.61,170.03) .. controls (309.88,170.03) and (293.85,166.37) .. (287.81,161.86) -- cycle ;
            		\draw [color={rgb, 255:red, 14; green, 56; blue, 105 }  ,draw opacity=1 ][line width=0.75]    (362.97,139.27) .. controls (111.75,150.63) and (361.27,194.97) .. (426.07,183.6) ;
            		\draw  [fill={rgb, 255:red, 14; green, 57; blue, 108 }  ,fill opacity=1 ][line width=0.75]  (420.16,108.42) -- (407.44,107.36) -- (399.93,103.5) -- (415.41,102.46) -- (420.22,105.88) -- cycle ;
            		\draw  [fill={rgb, 255:red, 20; green, 74; blue, 138 }  ,fill opacity=1 ][line width=0.75]  (447.57,152.38) -- (447.24,165.95) -- (433.84,159.47) -- (434.52,147.1) -- cycle ;
            		\draw  [fill={rgb, 255:red, 14; green, 57; blue, 108 }  ,fill opacity=1 ][line width=0.75]  (448.96,151.93) -- (447.57,152.38) -- (434.52,147.1) -- (435.54,146.5) -- cycle ;
            		\draw  [fill={rgb, 255:red, 18; green, 73; blue, 138 }  ,fill opacity=1 ][line width=0.75]  (444.23,135.19) -- (448.34,151.62) -- (435.54,146.5) -- (439.1,134.13) -- (440.46,119.65) -- (444.83,120.86) -- cycle ;
            		\draw  [fill={rgb, 255:red, 14; green, 57; blue, 108 }  ,fill opacity=1 ][line width=0.75]  (448.23,135.64) -- (452.97,150.44) -- (448.53,152.04) -- (444.23,135.19) -- (444.78,112.41) -- (448.31,112.11) -- cycle ;
            		\draw  [fill={rgb, 255:red, 14; green, 57; blue, 108 }  ,fill opacity=1 ][line width=0.75]  (452.97,150.44) -- (452.33,163.39) -- (447.24,165.95) -- (447.57,152.38) -- cycle ;
            		\draw  [fill={rgb, 255:red, 14; green, 57; blue, 108 }  ,fill opacity=1 ][line width=0.75]  (443.11,120.18) -- (441.32,119.8) -- (441.51,111.98) -- (443.39,112.17) -- cycle ;
            		\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=0.75]  (441.93,101.83) -- (448.61,105.9) -- (448.28,109.62) -- (446.72,109.53) -- (446.81,107.41) -- (441.85,104.84) -- (435.7,104.84) -- (430.88,101.98) -- cycle ;
            		\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=0.75]  (448.28,109.62) -- (448.31,112.11) -- (445.71,112.26) -- (445.77,109.72) -- cycle ;
            		\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=0.75]  (445.59,110.85) -- (445.71,112.26) -- (444.78,112.41) -- (444.41,120.56) -- (443.11,120.18) -- (443.64,110.28) -- cycle ;
            		\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=0.75]  (441.85,104.84) -- (446.81,107.41) -- (446.72,109.53) -- (445.77,109.72) -- (445.59,110.85) -- (443.64,110.28) -- (438.37,107.36) -- (435.64,107.39) -- (435.7,104.84) -- cycle ;
            		\draw [line width=0.75]    (438.37,107.36) -- (441.14,107.36) ;
            		\draw [line width=0.75]    (441.14,107.36) -- (446.09,110) ;
            		\draw  [fill={rgb, 255:red, 14; green, 57; blue, 108 }  ,fill opacity=1 ][line width=0.75]  (435.64,107.39) -- (415.28,108.89) -- (415.41,102.46) -- (430.89,101.42) -- (435.7,104.84) -- cycle ;
            		\draw [line width=0.75]    (415.84,77.81) -- (430.88,101.98) ;
            		\draw [line width=0.75]    (395.14,75.12) -- (430.89,101.42) ;
            		\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ][line width=0.75]  (428.02,101.59) -- (430.94,101.59) -- (430.98,99.9) -- (428.06,99.9) -- cycle ;
            		\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=0.75]  (416.37,74.18) -- (414.95,109.72) -- (413.32,109.7) -- (414.34,74.26) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=0.75]  (414.34,74.26) -- (413.32,109.7) -- (412.04,109.91) -- (413.23,74.09) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=0.75]  (413.23,74.09) -- (413.32,76.82) -- (393.49,75.97) -- (393.38,73.99) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=0.75]  (394.49,74.16) -- (393.62,105.85) -- (392.24,104.53) -- (393.38,73.99) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=0.75]  (412.19,106.98) -- (412.83,109.72) -- (392.95,104.72) -- (393.16,102.46) -- cycle ;
            		\draw  [line width=0.75]  (393.24,73.33) -- (414.34,74.26) -- (413.32,109.7) -- (392.24,104.53) -- cycle ;
            		\draw  [line width=0.75]  (394.59,76.07) -- (412.94,77.08) -- (412.19,106.98) -- (393.78,102.55) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 177; green, 175; blue, 175 }  ,fill opacity=1 ][line width=0.75]  (395.37,76.16) -- (394.64,102.84) -- (393.78,102.55) -- (394.59,76.07) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.29 ][line width=0.75]  (412.94,77.08) -- (412.19,106.98) -- (393.78,102.55) -- (394.59,76.07) -- cycle ;
            		\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=0.75]  (407.18,90.05) -- (406.58,104.34) -- (399.08,102.65) -- (399.42,88.89) -- cycle ;
            		\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ][line width=0.75]  (405.94,91.42) -- (405.56,102.48) -- (400.05,101.23) -- (400.29,90.55) -- cycle ;
            		\draw  [fill={rgb, 255:red, 14; green, 57; blue, 108 }  ,fill opacity=1 ][line width=0.75]  (392.73,103.74) -- (412.8,108.64) -- (413.17,96.95) -- (415.68,96.95) -- (416.25,99.47) -- (416.09,111.03) -- (413.58,111.69) -- (391.44,105.25) -- (391.72,93.81) -- (392.87,93.69) -- cycle ;
            		\draw  [fill={rgb, 255:red, 245; green, 120; blue, 35 }  ,fill opacity=1 ][line width=0.75]  (403.49,101.83) -- (403.68,106.86) -- (401.89,107.49) -- (399.49,106.86) -- (398.7,105.12) -- (398.24,102.61) -- (401.38,102.61) -- (401.2,101.45) -- cycle ;
            		\draw  [fill={rgb, 255:red, 245; green, 120; blue, 35 }  ,fill opacity=1 ,even odd rule][line width=0.75]  (382.9,103.28) .. controls (382.91,102.78) and (386.44,102.37) .. (390.78,102.37) .. controls (395.13,102.37) and (398.64,102.78) .. (398.62,103.28) .. controls (398.61,103.78) and (395.08,104.18) .. (390.74,104.18) .. controls (386.4,104.18) and (382.89,103.78) .. (382.9,103.28)(382.11,103.28) .. controls (382.13,102.34) and (386.03,101.58) .. (390.8,101.58) .. controls (395.58,101.58) and (399.44,102.34) .. (399.41,103.28) .. controls (399.39,104.21) and (395.5,104.97) .. (390.72,104.97) .. controls (385.94,104.97) and (382.09,104.21) .. (382.11,103.28) ;
            		\draw  [fill={rgb, 255:red, 245; green, 120; blue, 35 }  ,fill opacity=1 ][line width=0.75]  (399.33,105.22) -- (393.25,105.73) -- (392.02,104.47) -- (399.41,103.28) -- cycle ;
            		\draw [line width=0.75]    (382.11,103.28) .. controls (383.81,111.76) and (385.99,110.6) .. (385.46,119.65) ;
            		\draw [line width=0.75]    (399.55,104.47) .. controls (396.61,112.87) and (395.51,110.64) .. (396.14,119.31) ;
            		\draw [line width=0.75]    (388.21,110.44) .. controls (391.4,113.77) and (393.11,112.14) .. (395.81,117.42) ;
            		\draw [line width=0.75]    (385.9,110.69) .. controls (389.09,114.02) and (391.56,113.81) .. (394.26,119.09) ;
            		\draw [line width=0.75]    (384.95,112.14) .. controls (388.13,115.47) and (388.89,114) .. (391.59,119.28) ;
            		\draw [line width=0.75]    (385.21,114.27) .. controls (388.39,117.6) and (386.57,115.97) .. (388.68,119.24) ;
            		\draw [line width=0.75]    (391.79,110.5) .. controls (394.97,113.83) and (393.96,111.63) .. (395.97,114.78) ;
            		\draw [line width=0.75]    (394.73,109.87) .. controls (397.92,113.2) and (394.84,109.87) .. (395.94,111.76) ;
            		\draw [line width=0.75]    (388.21,110.44) .. controls (386.59,113.39) and (386.84,113.39) .. (385.6,116.79) ;
            		\draw [line width=0.75]    (389.99,110.57) .. controls (388.37,113.52) and (387.79,116.03) .. (386.56,119.43) ;
            		\draw [line width=0.75]    (391.79,110.5) .. controls (390.17,113.46) and (389.36,116.26) .. (388.12,119.65) ;
            		\draw [line width=0.75]    (393.85,110.82) .. controls (392.23,113.77) and (392.32,114.75) .. (390.31,120.03) ;
            		\draw [line width=0.75]    (395.79,110.69) .. controls (394.17,113.64) and (393.91,116.07) .. (392.68,119.46) ;
            		\draw [line width=0.75]    (395.97,114.78) .. controls (394.88,117.92) and (395.49,115.69) .. (394.26,119.09) ;
            		\draw [line width=0.75]    (387.82,105) .. controls (387.52,107.93) and (387.27,108.49) .. (385.18,111.73) ;
            		\draw [line width=0.75]    (383.6,104.25) .. controls (383.3,107.17) and (385.6,109.06) .. (385.9,110.69) ;
            		\draw [line width=0.75]    (385.66,105) .. controls (385.35,107.93) and (385.69,108.59) .. (385.99,110.22) ;
            		\draw [line width=0.75]    (389.5,104.88) .. controls (389.2,107.8) and (389.54,108.46) .. (389.84,110.09) ;
            		\draw [line width=0.75]    (393.42,105.1) .. controls (393.12,108.02) and (393.46,108.68) .. (393.76,110.31) ;
            		\draw [line width=0.75]    (392,105.38) .. controls (391.7,108.3) and (392.08,107.32) .. (389.99,110.57) ;
            		\draw [line width=0.75]    (387.82,105) .. controls (387.52,107.93) and (389.69,108.93) .. (389.99,110.57) ;
            		\draw [line width=0.75]    (392,105.38) .. controls (391.7,108.3) and (393.55,109.18) .. (393.85,110.82) ;
            		\draw [line width=0.75]    (395.66,105.48) .. controls (395.35,108.4) and (397.16,108.46) .. (397.46,110.09) ;
            		\draw [line width=0.75]    (395.66,105.48) .. controls (395.35,108.4) and (395.73,107.42) .. (393.64,110.66) ;
            		\draw [line width=0.75]    (397.81,105.51) .. controls (397.5,108.43) and (397.88,107.45) .. (395.79,110.69) ;
            		\draw [line width=0.75]    (387,104.82) .. controls (386.11,108.77) and (387.91,108.81) .. (388.21,110.44) ;
            		\draw [line width=0.75]    (390.67,105.48) .. controls (389.79,109.43) and (391.58,109.47) .. (391.88,111.1) ;
            		\draw [line width=0.75]    (384.78,104.6) .. controls (383.9,108.55) and (383.99,107.8) .. (384.29,109.43) ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.46 ][fill={rgb, 255:red, 208; green, 80; blue, 2 }  ,fill opacity=1 ][line width=0.75]  (268.42,52.98) .. controls (268.42,49.98) and (270.85,47.55) .. (273.85,47.55) .. controls (276.85,47.55) and (279.28,49.98) .. (279.28,52.98) .. controls (279.28,55.98) and (276.85,58.41) .. (273.85,58.41) .. controls (270.85,58.41) and (268.42,55.98) .. (268.42,52.98) -- cycle ;
            		\draw [line width=0.75]    (268.82,51.5) .. controls (270.34,54.14) and (275.54,55.99) .. (278.51,55.25) ;
            		\draw [line width=0.75]    (271.42,48.53) .. controls (272.94,51.17) and (270.34,55.62) .. (269.23,55.25) ;
            		\draw [line width=0.75]    (275.35,48.38) .. controls (272.75,51.91) and (271.27,56.18) .. (272.38,57.85) ;
            		\draw [line width=0.75]    (275.17,58.22) .. controls (273.13,55.81) and (273.68,53.77) .. (278.14,50.79) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.6 ][line width=0.75]    (271.42,48.53) .. controls (273.13,47.57) and (277.4,47.95) .. (278.51,51.85) ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.81 ][line width=0.75]  (268.42,52.98) .. controls (268.42,49.98) and (270.85,47.55) .. (273.85,47.55) .. controls (276.85,47.55) and (279.28,49.98) .. (279.28,52.98) .. controls (279.28,55.98) and (276.85,58.41) .. (273.85,58.41) .. controls (270.85,58.41) and (268.42,55.98) .. (268.42,52.98) -- cycle ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 247; green, 214; blue, 158 }  ,fill opacity=1 ][line width=0.75]  (172.39,122.67) .. controls (172.85,120.9) and (177.59,119.16) .. (178.47,118.78) .. controls (178.76,117.57) and (180.89,115.98) .. (180.04,113.51) .. controls (179.88,113.06) and (180.65,110.66) .. (180.47,110.23) .. controls (181.03,110.19) and (179.67,110.73) .. (180.47,111.17) .. controls (182.72,111.42) and (182.5,119.1) .. (181.09,121.14) .. controls (179.99,122.75) and (169.76,130.7) .. (172.39,122.67) -- cycle ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.46 ][fill={rgb, 255:red, 208; green, 80; blue, 2 }  ,fill opacity=1 ][line width=0.75]  (176.78,107.32) .. controls (176.78,104.4) and (179.15,102.04) .. (182.06,102.04) .. controls (184.98,102.04) and (187.34,104.4) .. (187.34,107.32) .. controls (187.34,110.23) and (184.98,112.59) .. (182.06,112.59) .. controls (179.15,112.59) and (176.78,110.23) .. (176.78,107.32) -- cycle ;
            		\draw [line width=0.75]    (177.17,105.88) .. controls (178.65,108.44) and (183.71,110.25) .. (186.59,109.52) ;
            		\draw [line width=0.75]    (179.7,102.99) .. controls (181.18,105.55) and (178.65,109.89) .. (177.57,109.52) ;
            		\draw [line width=0.75]    (183.52,102.84) .. controls (181,106.27) and (179.55,110.43) .. (180.64,112.05) ;
            		\draw [line width=0.75]    (183.34,112.41) .. controls (181.36,110.07) and (181.9,108.08) .. (186.23,105.19) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.6 ][line width=0.75]    (179.7,102.99) .. controls (181.36,102.06) and (185.51,102.42) .. (186.59,106.21) ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=0.75] [line join = round][line cap = round] (173.97,122.58) .. controls (173.84,122.66) and (173.72,122.74) .. (173.59,122.83) ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 247; green, 214; blue, 158 }  ,fill opacity=1 ][line width=0.75]  (170.31,121.48) .. controls (169.62,121.44) and (169.24,120.71) .. (169.12,120.72) .. controls (167.97,120.73) and (170.25,115.83) .. (173.95,116.02) .. controls (174.54,116.25) and (174.94,116.69) .. (175.26,117.2) .. controls (175.42,117.46) and (175.31,117.77) .. (175.04,118.1) .. controls (176.01,118.78) and (176.14,118.54) .. (176.21,118.78) .. controls (176.13,119.1) and (175.89,119.39) .. (175.56,119.66) .. controls (175.56,120.89) and (175.92,121.39) .. (175.18,121.7) .. controls (174.84,121.68) and (174.33,121.66) .. (173.81,121.63) .. controls (173.3,121.6) and (174.13,123.99) .. (170.94,123.99) .. controls (167.36,124.24) and (169.81,121.54) .. (170.31,121.48) -- cycle ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ][line width=0.75]  (172.57,118.91) .. controls (170.52,117.76) and (170.06,119.28) .. (171.31,120.35) .. controls (170.68,121.1) and (170.62,121.1) .. (170.12,121.16) .. controls (168.97,121.17) and (166.73,117.34) .. (168.8,115.83) .. controls (170.04,114.81) and (171.81,114.83) .. (173.95,114.58) .. controls (174.01,115.04) and (174.22,115.36) .. (174.51,115.58) .. controls (174.25,115.84) and (173.48,116.05) .. (172.62,116.19) .. controls (172.76,116.54) and (172.89,116.86) .. (173.01,117.15) .. controls (172.44,118.66) and (172.12,119.13) .. (172.57,118.91) -- cycle ;
            		\draw [line width=0.75]    (173.95,117.71) -- (175.07,117.59) ;
            		\draw [line width=0.75]    (174.57,118.28) ;
            		\draw [line width=0.75]    (174.12,118.5) -- (174.57,118.28) ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 74; green, 144; blue, 226 }  ,fill opacity=1 ][line width=0.75]  (167.3,136.94) .. controls (166.82,136.94) and (165.29,135.94) .. (167.3,132.61) .. controls (165.92,126.41) and (167.13,123.36) .. (168.93,122.46) .. controls (169.18,124.53) and (171.06,123.9) .. (171.94,123.96) .. controls (169.37,128.41) and (172.5,129.27) .. (173.44,129.48) .. controls (175.22,129.87) and (176.33,125.83) .. (176.58,126.16) .. controls (178.02,128.8) and (176.59,135.34) .. (176.2,137.07) .. controls (175.88,138.51) and (167.37,136.85) .. (167.3,136.94) -- cycle ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 247; green, 214; blue, 158 }  ,fill opacity=1 ][line width=0.75]  (171.94,123.96) .. controls (172.52,123.7) and (174.01,121.64) .. (177.39,122.14) .. controls (178.54,120.81) and (179.9,121.14) .. (180.78,120.76) .. controls (181.07,119.55) and (182.32,116.58) .. (181.47,114.12) .. controls (181.31,113.66) and (179.39,113.61) .. (179.21,113.17) .. controls (178.76,112.07) and (177.45,110.98) .. (177.33,110.23) .. controls (177.14,109.01) and (179.83,110.16) .. (179.9,109.66) .. controls (179.96,109.28) and (180.67,111.56) .. (180.96,111.54) .. controls (181.53,111.5) and (182.42,111.99) .. (183.23,112.42) .. controls (183.28,112.88) and (185.26,120.35) .. (183.85,122.39) .. controls (182.75,124) and (178.27,125.65) .. (176.58,126.16) .. controls (174.45,131.67) and (169.18,129.1) .. (171.94,123.96) -- cycle ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 247; green, 214; blue, 158 }  ,fill opacity=1 ][line width=0.75]  (179.73,157.6) .. controls (179.41,155.47) and (179.16,152.79) .. (180.65,150.34) .. controls (180.13,149.74) and (177.03,149.16) .. (179.66,149.09) .. controls (177.03,148.41) and (180.34,147.59) .. (180.17,147.15) .. controls (180.33,147.14) and (182.86,145.37) .. (183.87,147.56) .. controls (184.32,147.79) and (184.79,148.3) .. (185.23,148.98) .. controls (185.88,149.98) and (183.05,156.6) .. (182.8,157.91) .. controls (181.04,164.12) and (179.38,157.41) .. (179.73,157.6) -- cycle ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 247; green, 214; blue, 158 }  ,fill opacity=1 ][line width=0.75]  (167.56,156.6) .. controls (168.17,154.53) and (169.19,151.83) .. (171.32,150.39) .. controls (171.1,149.62) and (170.91,148.36) .. (170.91,148.14) .. controls (170.96,147.66) and (172.16,147.06) .. (172.18,146.59) .. controls (172.33,146.64) and (175.37,146.1) .. (175.37,148.51) .. controls (175.68,148.9) and (175.9,149.57) .. (176.01,150.37) .. controls (176.19,151.55) and (170.84,156.37) .. (170.06,157.46) .. controls (165.86,162.36) and (167.33,156.28) .. (167.56,156.6) -- cycle ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 74; green, 144; blue, 226 }  ,fill opacity=1 ][line width=0.75]  (168.05,136.98) .. controls (170.51,138.25) and (175.15,137.49) .. (176.03,137.56) .. controls (180.61,141.38) and (182.92,146.13) .. (183.87,146.34) .. controls (184.87,147.4) and (182.24,147.33) .. (182.49,147.65) .. controls (182.45,147.81) and (180.53,146.98) .. (180.17,147.15) .. controls (179.78,147.34) and (180.27,148.87) .. (179.66,149.09) .. controls (178.88,149.65) and (177.78,150.07) .. (176.54,150.39) .. controls (175.4,150.69) and (176.13,149.51) .. (174.9,149.66) .. controls (173.34,150.19) and (172.16,150.52) .. (170.87,150.79) .. controls (169.13,151.29) and (163.8,137.62) .. (168.05,136.98) -- cycle ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=0.75]  (167.56,156.6) .. controls (167.45,156.21) and (168.37,157.71) .. (170.06,157.46) .. controls (168.13,161.42) and (163.42,163.68) .. (167.56,156.6) -- cycle ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=0.75]  (179.73,157.6) .. controls (179.35,156.47) and (181.54,158.1) .. (182.93,157.1) .. controls (182.05,164.06) and (177.91,166.5) .. (179.73,157.6) -- cycle ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ][line width=0.75]  (165.87,159.1) .. controls (165.76,158.72) and (166.12,162.05) .. (168.88,159.67) .. controls (168.38,162.11) and (172.52,162.62) .. (172.39,163.56) .. controls (171.26,165.31) and (166.37,164.43) .. (164.06,163.01) .. controls (163.6,162.17) and (163.97,160.91) .. (165.87,159.1) -- cycle ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ][line width=0.75]  (178.91,161.17) .. controls (178.73,160.82) and (180.07,163.87) .. (182.3,160.98) .. controls (182.3,163.48) and (187.94,163.31) .. (187.94,164.25) .. controls (187.19,166.19) and (180.92,166.33) .. (178.37,165.4) .. controls (177.75,164.67) and (177.41,163.32) .. (178.91,161.17) -- cycle ;
            		\draw [line width=0.75]    (172.01,120.72) .. controls (172.83,121.04) and (172.95,121.54) .. (173.81,121.63) ;
            		\draw [line width=0.75]    (179.48,110) .. controls (179.73,110.63) and (179.78,111.96) .. (180.64,112.05) ;
            		\draw [line width=0.75]    (178.6,109.75) .. controls (178.85,110.38) and (178.9,111.71) .. (179.76,111.8) ;
            		\draw [line width=0.75]    (177.85,109.94) .. controls (178.1,110.57) and (178.54,111.69) .. (179.01,111.99) ;
            		\draw [line width=0.75]    (168.25,135.51) .. controls (168.5,136.14) and (171.64,135.65) .. (173.83,131.89) ;
            		\draw [line width=0.75]    (171.95,136.58) .. controls (172.2,137.21) and (174.33,135.65) .. (175.02,133.64) ;
            		\draw [line width=0.75]    (167.56,141.86) .. controls (170.26,145.12) and (172.89,147.94) .. (175.49,149.54) ;
            		\draw [line width=0.75]    (170.32,144.18) .. controls (173.27,146) and (173.39,145.75) .. (176.03,146.44) ;
            		\draw [line width=0.75]    (175.21,126.87) .. controls (175.46,126.81) and (175.53,126.18) .. (176.58,126.16) ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=0.75]  (172.39,163.56) .. controls (170.82,165.3) and (166.37,163.98) .. (164.06,163.01) .. controls (163.23,159.59) and (167.31,165.11) .. (172.39,163.56) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=0.75]  (187.94,164.25) .. controls (186.56,166.18) and (180.68,166.37) .. (178.37,165.4) .. controls (176.47,162.6) and (182.55,166.18) .. (187.94,164.25) -- cycle ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ][line width=0.75]    (168.93,122.46) .. controls (168.38,123.28) and (169,124.98) .. (171.94,123.96) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ][line width=0.75]    (171.94,123.96) .. controls (168.06,127.48) and (174.27,133.38) .. (176.58,126.16) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ][line width=0.75]    (170.51,150.31) .. controls (169.96,151.14) and (172.83,149.81) .. (175.09,149.31) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ][line width=0.75]    (176.03,149.87) .. controls (175.76,150.27) and (178.66,149.56) .. (179.29,148.81) .. controls (179.92,148.05) and (179.23,147.12) .. (179.92,146.8) .. controls (180.6,146.48) and (181.43,147.21) .. (182.05,147.24) .. controls (182.66,147.26) and (183.3,146.84) .. (183.74,146.74) ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.32 ][line width=0.75]  (163.94,161.95) .. controls (165.62,158.92) and (165.06,159.11) .. (167.25,160.5) .. controls (165.74,161.17) and (164.43,164.94) .. (163.94,161.95) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.32 ][line width=0.75]  (177.59,163.74) .. controls (179.28,160.71) and (178.54,161.3) .. (180.74,162.69) .. controls (179.29,163.93) and (179.29,167.95) .. (177.59,163.74) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.22 ][line width=0.75]  (165.87,159.1) .. controls (167.75,156.53) and (166.56,155.89) .. (168.75,157.28) .. controls (167.24,157.96) and (166.36,162.09) .. (165.87,159.1) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.22 ][line width=0.75]  (178.91,161.17) .. controls (180.23,158.54) and (178.85,156.27) .. (181.04,157.66) .. controls (180.17,158.05) and (180.62,161.37) .. (180.1,162.05) .. controls (179.72,162.55) and (179.12,162.44) .. (178.91,161.17) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.22 ][line width=0.75]  (167.56,156.6) .. controls (169,152.77) and (171.01,149.37) .. (173.21,150.76) .. controls (171.69,151.44) and (168.05,159.58) .. (167.56,156.6) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.22 ][line width=0.75]  (179.6,157.03) .. controls (179.25,154.17) and (180.1,151.84) .. (180.23,150.51) .. controls (178.66,148.63) and (179.69,148.86) .. (182.05,150.51) .. controls (181.19,150.89) and (180.85,154.73) .. (180.48,156.72) .. controls (180.19,158.26) and (179.82,158.34) .. (179.6,157.03) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.22 ][line width=0.75]  (170.07,156.34) .. controls (175.4,152.41) and (173.21,149.01) .. (176.03,149.87) .. controls (175.84,151.7) and (172.08,155.78) .. (170.07,156.34) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.22 ][line width=0.75]  (181.29,157.47) .. controls (182.86,153.77) and (182.24,154.02) .. (183.49,150.83) .. controls (183.3,152.66) and (182.74,156.34) .. (181.29,157.47) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.22 ][line width=0.75]  (184.74,149.7) .. controls (183.55,148) and (183.3,149.57) .. (183.36,147.44) .. controls (183.68,149.57) and (184.81,148.44) .. (184.74,149.7) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.4 ][line width=0.75]  (167.62,137.22) .. controls (168.59,136.73) and (170.13,138.15) .. (173.06,137.8) .. controls (172.75,138.79) and (170.09,138.76) .. (171.05,139.73) .. controls (171.53,140.2) and (173.38,140.79) .. (174.15,141.31) .. controls (174.59,141.62) and (171.52,141.33) .. (171.97,141.65) .. controls (173.13,142.46) and (174.59,142.63) .. (176.07,143.57) .. controls (176.5,143.85) and (173.66,143.85) .. (174.06,144.16) .. controls (174.92,144.82) and (176.26,145.6) .. (177.44,146.37) .. controls (177.87,146.66) and (176.3,147.06) .. (176.65,147.33) .. controls (177.6,148.07) and (180.14,148.61) .. (179.66,149.09) .. controls (178.52,148.79) and (177.55,150.66) .. (176.54,150.39) .. controls (175.79,150.19) and (176.15,149.72) .. (175.49,149.54) .. controls (171.55,150.51) and (170.05,150.89) .. (169.97,150.51) .. controls (166.37,143.07) and (165.37,138.64) .. (167.62,137.22) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.41 ][line width=0.75]  (167.3,136.94) .. controls (166.82,136.94) and (165.29,135.94) .. (167.3,132.61) .. controls (165.92,126.41) and (167.13,123.36) .. (168.93,122.46) .. controls (169.18,124.53) and (171.06,123.9) .. (171.94,123.96) .. controls (169.37,128.41) and (172.5,129.27) .. (173.44,129.48) .. controls (175.22,129.87) and (170.72,134.67) .. (170.97,134.99) .. controls (171.24,135.48) and (174.32,132.11) .. (174.73,132.32) .. controls (175.31,132.61) and (171.7,136.05) .. (171.95,136.58) .. controls (172.49,137.68) and (176.42,136.11) .. (176.2,137.07) .. controls (175.88,138.51) and (167.37,136.85) .. (167.3,136.94) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.22 ][line width=0.75]  (171.94,123.96) .. controls (169.05,130.65) and (175.9,132.82) .. (176.49,124.37) .. controls (174.97,125.05) and (172.43,126.95) .. (171.94,123.96) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.22 ][line width=0.75]  (176.09,125.91) .. controls (177.82,124.21) and (179.83,124.04) .. (183.85,122.39) .. controls (183.01,122.87) and (176.58,128.9) .. (176.09,125.91) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.22 ][line width=0.75]  (180.78,120.76) .. controls (182.09,123.37) and (182.84,117.35) .. (181.92,114.26) .. controls (181.08,114.73) and (181.27,123.75) .. (180.78,120.76) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.22 ][line width=0.75]  (178.47,118.78) .. controls (180.21,117.08) and (177.23,115.15) .. (181.25,113.5) .. controls (182.09,115.34) and (182.34,124.04) .. (178.47,118.78) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.22 ][line width=0.75]  (175.18,121.7) .. controls (177.41,120.86) and (179.75,119.52) .. (180.75,120.19) .. controls (179.41,121.2) and (177.41,122.2) .. (175.18,121.7) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.22 ][line width=0.75]  (170.05,118.86) .. controls (167.04,125.46) and (171.72,125.38) .. (173.81,121.63) .. controls (172.3,122.3) and (172.72,121.03) .. (170.05,118.86) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.22 ][line width=0.75]  (177.17,105.88) .. controls (174.28,112.56) and (186.75,115.76) .. (187.34,107.32) .. controls (183.85,113.84) and (177.66,108.87) .. (177.17,105.88) -- cycle ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.46 ][fill={rgb, 255:red, 208; green, 80; blue, 2 }  ,fill opacity=1 ][line width=0.75]  (215.13,70.74) .. controls (215.13,67.74) and (217.57,65.31) .. (220.56,65.31) .. controls (223.56,65.31) and (225.99,67.74) .. (225.99,70.74) .. controls (225.99,73.74) and (223.56,76.17) .. (220.56,76.17) .. controls (217.57,76.17) and (215.13,73.74) .. (215.13,70.74) -- cycle ;
            		\draw [line width=0.75]    (215.53,69.26) .. controls (217.05,71.9) and (222.25,73.76) .. (225.23,73.01) ;
            		\draw [line width=0.75]    (218.13,66.29) .. controls (219.65,68.93) and (217.05,73.38) .. (215.94,73.01) ;
            		\draw [line width=0.75]    (222.07,66.14) .. controls (219.47,69.67) and (217.98,73.94) .. (219.1,75.61) ;
            		\draw [line width=0.75]    (221.88,75.98) .. controls (219.84,73.57) and (220.4,71.53) .. (224.85,68.56) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.6 ][line width=0.75]    (218.13,66.29) .. controls (219.84,65.34) and (224.11,65.71) .. (225.23,69.61) ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.81 ][line width=0.75]  (215.13,70.74) .. controls (215.13,67.74) and (217.57,65.31) .. (220.56,65.31) .. controls (223.56,65.31) and (225.99,67.74) .. (225.99,70.74) .. controls (225.99,73.74) and (223.56,76.17) .. (220.56,76.17) .. controls (217.57,76.17) and (215.13,73.74) .. (215.13,70.74) -- cycle ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.46 ][fill={rgb, 255:red, 208; green, 80; blue, 2 }  ,fill opacity=1 ][line width=0.75]  (332.72,63.64) .. controls (332.72,60.64) and (335.15,58.21) .. (338.15,58.21) .. controls (341.15,58.21) and (343.58,60.64) .. (343.58,63.64) .. controls (343.58,66.64) and (341.15,69.07) .. (338.15,69.07) .. controls (335.15,69.07) and (332.72,66.64) .. (332.72,63.64) -- cycle ;
            		\draw [line width=0.75]    (333.12,62.16) .. controls (334.64,64.79) and (339.84,66.65) .. (342.81,65.91) ;
            		\draw [line width=0.75]    (335.72,59.19) .. controls (337.24,61.82) and (334.64,66.28) .. (333.52,65.91) ;
            		\draw [line width=0.75]    (339.65,59.04) .. controls (337.05,62.57) and (335.57,66.84) .. (336.68,68.51) ;
            		\draw [line width=0.75]    (339.47,68.88) .. controls (337.42,66.47) and (337.98,64.42) .. (342.44,61.45) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.6 ][line width=0.75]    (335.72,59.19) .. controls (337.42,58.23) and (341.7,58.6) .. (342.81,62.5) ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.81 ][line width=0.75]  (332.72,63.64) .. controls (332.72,60.64) and (335.15,58.21) .. (338.15,58.21) .. controls (341.15,58.21) and (343.58,60.64) .. (343.58,63.64) .. controls (343.58,66.64) and (341.15,69.07) .. (338.15,69.07) .. controls (335.15,69.07) and (332.72,66.64) .. (332.72,63.64) -- cycle ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.46 ][fill={rgb, 255:red, 208; green, 80; blue, 2 }  ,fill opacity=1 ][line width=0.75]  (186.72,94.54) .. controls (186.72,91.54) and (189.15,89.11) .. (192.14,89.11) .. controls (195.14,89.11) and (197.57,91.54) .. (197.57,94.54) .. controls (197.57,97.54) and (195.14,99.97) .. (192.14,99.97) .. controls (189.15,99.97) and (186.72,97.54) .. (186.72,94.54) -- cycle ;
            		\draw [line width=0.75]    (187.11,93.06) .. controls (188.63,95.7) and (193.83,97.56) .. (196.81,96.81) ;
            		\draw [line width=0.75]    (189.71,90.09) .. controls (191.23,92.73) and (188.63,97.19) .. (187.52,96.81) ;
            		\draw [line width=0.75]    (193.65,89.94) .. controls (191.05,93.47) and (189.56,97.74) .. (190.68,99.41) ;
            		\draw [line width=0.75]    (193.46,99.79) .. controls (191.42,97.37) and (191.98,95.33) .. (196.43,92.36) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.6 ][line width=0.75]    (189.71,90.09) .. controls (191.42,89.14) and (195.69,89.51) .. (196.81,93.41) ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.81 ][line width=0.75]  (186.72,94.54) .. controls (186.72,91.54) and (189.15,89.11) .. (192.14,89.11) .. controls (195.14,89.11) and (197.57,91.54) .. (197.57,94.54) .. controls (197.57,97.54) and (195.14,99.97) .. (192.14,99.97) .. controls (189.15,99.97) and (186.72,97.54) .. (186.72,94.54) -- cycle ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.46 ][fill={rgb, 255:red, 208; green, 80; blue, 2 }  ,fill opacity=1 ][line width=0.75]  (240.71,59.37) .. controls (240.71,56.38) and (243.14,53.94) .. (246.14,53.94) .. controls (249.14,53.94) and (251.57,56.38) .. (251.57,59.37) .. controls (251.57,62.37) and (249.14,64.8) .. (246.14,64.8) .. controls (243.14,64.8) and (240.71,62.37) .. (240.71,59.37) -- cycle ;
            		\draw [line width=0.75]    (241.11,57.89) .. controls (242.63,60.53) and (247.83,62.39) .. (250.8,61.65) ;
            		\draw [line width=0.75]    (243.71,54.92) .. controls (245.23,57.56) and (242.63,62.02) .. (241.52,61.65) ;
            		\draw [line width=0.75]    (247.65,54.77) .. controls (245.05,58.3) and (243.56,62.57) .. (244.67,64.25) ;
            		\draw [line width=0.75]    (247.46,64.62) .. controls (245.42,62.2) and (245.97,60.16) .. (250.43,57.19) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.6 ][line width=0.75]    (243.71,54.92) .. controls (245.42,53.97) and (249.69,54.34) .. (250.8,58.24) ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.81 ][line width=0.75]  (240.71,59.37) .. controls (240.71,56.38) and (243.14,53.94) .. (246.14,53.94) .. controls (249.14,53.94) and (251.57,56.38) .. (251.57,59.37) .. controls (251.57,62.37) and (249.14,64.8) .. (246.14,64.8) .. controls (243.14,64.8) and (240.71,62.37) .. (240.71,59.37) -- cycle ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.46 ][fill={rgb, 255:red, 208; green, 80; blue, 2 }  ,fill opacity=1 ][line width=0.75]  (302.17,54.4) .. controls (302.17,51.4) and (304.6,48.97) .. (307.6,48.97) .. controls (310.6,48.97) and (313.03,51.4) .. (313.03,54.4) .. controls (313.03,57.4) and (310.6,59.83) .. (307.6,59.83) .. controls (304.6,59.83) and (302.17,57.4) .. (302.17,54.4) -- cycle ;
            		\draw [line width=0.75]    (302.56,52.92) .. controls (304.09,55.56) and (309.29,57.42) .. (312.26,56.67) ;
            		\draw [line width=0.75]    (305.17,49.95) .. controls (306.69,52.59) and (304.09,57.04) .. (302.97,56.67) ;
            		\draw [line width=0.75]    (309.1,49.8) .. controls (306.5,53.33) and (305.02,57.6) .. (306.13,59.27) ;
            		\draw [line width=0.75]    (308.92,59.64) .. controls (306.87,57.23) and (307.43,55.19) .. (311.89,52.21) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.6 ][line width=0.75]    (305.17,49.95) .. controls (306.87,49) and (311.15,49.37) .. (312.26,53.27) ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.81 ][line width=0.75]  (302.17,54.4) .. controls (302.17,51.4) and (304.6,48.97) .. (307.6,48.97) .. controls (310.6,48.97) and (313.03,51.4) .. (313.03,54.4) .. controls (313.03,57.4) and (310.6,59.83) .. (307.6,59.83) .. controls (304.6,59.83) and (302.17,57.4) .. (302.17,54.4) -- cycle ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.46 ][fill={rgb, 255:red, 208; green, 80; blue, 2 }  ,fill opacity=1 ][line width=0.75]  (355.81,76.43) .. controls (355.81,73.43) and (358.24,71) .. (361.24,71) .. controls (364.24,71) and (366.67,73.43) .. (366.67,76.43) .. controls (366.67,79.42) and (364.24,81.85) .. (361.24,81.85) .. controls (358.24,81.85) and (355.81,79.42) .. (355.81,76.43) -- cycle ;
            		\draw [line width=0.75]    (356.21,74.95) .. controls (357.73,77.58) and (362.93,79.44) .. (365.9,78.7) ;
            		\draw [line width=0.75]    (358.81,71.97) .. controls (360.33,74.61) and (357.73,79.07) .. (356.62,78.7) ;
            		\draw [line width=0.75]    (362.74,71.83) .. controls (360.14,75.35) and (358.66,79.63) .. (359.77,81.3) ;
            		\draw [line width=0.75]    (362.56,81.67) .. controls (360.52,79.25) and (361.07,77.21) .. (365.53,74.24) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.6 ][line width=0.75]    (358.81,71.97) .. controls (360.52,71.02) and (364.79,71.39) .. (365.9,75.29) ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.81 ][line width=0.75]  (355.81,76.43) .. controls (355.81,73.43) and (358.24,71) .. (361.24,71) .. controls (364.24,71) and (366.67,73.43) .. (366.67,76.43) .. controls (366.67,79.42) and (364.24,81.85) .. (361.24,81.85) .. controls (358.24,81.85) and (355.81,79.42) .. (355.81,76.43) -- cycle ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.46 ][fill={rgb, 255:red, 208; green, 80; blue, 2 }  ,fill opacity=1 ][line width=0.75]  (382.45,96.67) .. controls (382.45,93.68) and (384.88,91.24) .. (387.88,91.24) .. controls (390.88,91.24) and (393.31,93.68) .. (393.31,96.67) .. controls (393.31,99.67) and (390.88,102.1) .. (387.88,102.1) .. controls (384.88,102.1) and (382.45,99.67) .. (382.45,96.67) -- cycle ;
            		\draw [line width=0.75]    (382.85,95.19) .. controls (384.37,97.83) and (389.57,99.69) .. (392.54,98.95) ;
            		\draw [line width=0.75]    (385.45,92.22) .. controls (386.97,94.86) and (384.37,99.32) .. (383.26,98.95) ;
            		\draw [line width=0.75]    (389.39,92.07) .. controls (386.79,95.6) and (385.3,99.87) .. (386.42,101.55) ;
            		\draw [line width=0.75]    (389.2,101.92) .. controls (387.16,99.5) and (387.72,97.46) .. (392.17,94.49) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.6 ][line width=0.75]    (385.45,92.22) .. controls (387.16,91.27) and (391.43,91.64) .. (392.54,95.54) ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.81 ][line width=0.75]  (382.45,96.67) .. controls (382.45,93.68) and (384.88,91.24) .. (387.88,91.24) .. controls (390.88,91.24) and (393.31,93.68) .. (393.31,96.67) .. controls (393.31,99.67) and (390.88,102.1) .. (387.88,102.1) .. controls (384.88,102.1) and (382.45,99.67) .. (382.45,96.67) -- cycle ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.46 ][fill={rgb, 255:red, 208; green, 80; blue, 2 }  ,fill opacity=1 ][line width=0.75]  (371.09,86.37) .. controls (371.09,83.37) and (373.52,80.94) .. (376.51,80.94) .. controls (379.51,80.94) and (381.94,83.37) .. (381.94,86.37) .. controls (381.94,89.37) and (379.51,91.8) .. (376.51,91.8) .. controls (373.52,91.8) and (371.09,89.37) .. (371.09,86.37) -- cycle ;
            		\draw [line width=0.75]    (371.48,84.89) .. controls (373,87.53) and (378.21,89.39) .. (381.18,88.64) ;
            		\draw [line width=0.75]    (374.08,81.92) .. controls (375.6,84.56) and (373,89.02) .. (371.89,88.64) ;
            		\draw [line width=0.75]    (378.02,81.77) .. controls (375.42,85.3) and (373.93,89.57) .. (375.05,91.24) ;
            		\draw [line width=0.75]    (377.83,91.62) .. controls (375.79,89.2) and (376.35,87.16) .. (380.81,84.19) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.6 ][line width=0.75]    (374.08,81.92) .. controls (375.79,80.97) and (380.06,81.34) .. (381.18,85.24) ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.81 ][line width=0.75]  (371.09,86.37) .. controls (371.09,83.37) and (373.52,80.94) .. (376.51,80.94) .. controls (379.51,80.94) and (381.94,83.37) .. (381.94,86.37) .. controls (381.94,89.37) and (379.51,91.8) .. (376.51,91.8) .. controls (373.52,91.8) and (371.09,89.37) .. (371.09,86.37) -- cycle ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.46 ][fill={rgb, 255:red, 208; green, 80; blue, 2 }  ,fill opacity=1 ][line width=0.75]  (198.44,84.24) .. controls (198.44,81.24) and (200.87,78.81) .. (203.87,78.81) .. controls (206.87,78.81) and (209.3,81.24) .. (209.3,84.24) .. controls (209.3,87.24) and (206.87,89.67) .. (203.87,89.67) .. controls (200.87,89.67) and (198.44,87.24) .. (198.44,84.24) -- cycle ;
            		\draw [line width=0.75]    (198.83,82.76) .. controls (200.36,85.4) and (205.56,87.26) .. (208.53,86.51) ;
            		\draw [line width=0.75]    (201.43,79.79) .. controls (202.96,82.43) and (200.36,86.88) .. (199.24,86.51) ;
            		\draw [line width=0.75]    (205.37,79.64) .. controls (202.77,83.17) and (201.29,87.44) .. (202.4,89.11) ;
            		\draw [line width=0.75]    (205.19,89.48) .. controls (203.14,87.07) and (203.7,85.03) .. (208.16,82.06) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.6 ][line width=0.75]    (201.43,79.79) .. controls (203.14,78.84) and (207.41,79.21) .. (208.53,83.11) ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.81 ][line width=0.75]  (198.44,84.24) .. controls (198.44,81.24) and (200.87,78.81) .. (203.87,78.81) .. controls (206.87,78.81) and (209.3,81.24) .. (209.3,84.24) .. controls (209.3,87.24) and (206.87,89.67) .. (203.87,89.67) .. controls (200.87,89.67) and (198.44,87.24) .. (198.44,84.24) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.25 ] (393.76,161.44) .. controls (397.78,159.43) and (420.96,164.24) .. (434.56,157.04) .. controls (444.96,160.24) and (474.73,164.99) .. (447.24,165.95) .. controls (424.96,163.44) and (397.36,167.44) .. (393.76,161.44) -- cycle ;
            	\end{tikzpicture}
            \end{center}'''
                # Câu hỏi
                noidungcauhoi = (r'''Một vận động viên bóng rổ đứng ném bóng vào rổ. Quỹ đạo chuyển động của quả bóng là hình parabol có phương trình $y= ax^2+ bx + c \left(a \neq 0\right)$. Biết quả bóng đạt vị trí cao nhất là $%s$ mét sau khi vận động viên ném $%s$ giây. Sau một giây ném ra, quả bóng cao hơn đầu vận động viên $%s$ mét. %s Biết rằng hàm số $y = ax^2+ bx +c$ đồng biến trên $\left( - \infty; d \right)$ và nghịch biến trên $\left(d; +\infty\right)$. Giá trị của $%s + d$ bằng bao nhiêu?'''
                                 %(yv, xv, y1,hinhve, N))

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                hinhve1=r'''\begin{center}
            	\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            		\draw  [fill={rgb, 255:red, 237; green, 195; blue, 127 }  ,fill opacity=1 ][line width=0.75]  (412.42,129.6) -- (528.38,192.69) -- (178.25,194.4) -- (107.2,126.76) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.25 ] (163.76,158.88) .. controls (167.78,156.87) and (171.7,160.19) .. (175.76,160.24) .. controls (191.94,160.45) and (204.45,169.68) .. (176.96,170.64) .. controls (170.56,167.04) and (143.76,168.88) .. (163.76,158.88) -- cycle ;
            		\draw [color={rgb, 255:red, 139; green, 87; blue, 42 }  ,draw opacity=0.57 ][line width=0.75]    (124.82,141.09) -- (430.04,140.97) ;
            		\draw [color={rgb, 255:red, 139; green, 87; blue, 42 }  ,draw opacity=0.57 ][line width=0.75]    (266.35,151.2) -- (445.96,150.07) ;
            		\draw [color={rgb, 255:red, 139; green, 87; blue, 42 }  ,draw opacity=0.57 ][line width=0.75]    (152.1,165.41) -- (331.71,164.28) ;
            		\draw [color={rgb, 255:red, 139; green, 87; blue, 42 }  ,draw opacity=0.57 ][line width=0.75]    (243.04,174.51) -- (422.66,173.37) ;
            		\draw [color={rgb, 255:red, 139; green, 87; blue, 42 }  ,draw opacity=0.57 ][line width=0.75]    (318.64,184.17) -- (498.25,183.03) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.61 ][line width=0.75]    (199.28,136.99) -- (416.4,135.86) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.61 ][line width=0.75]    (244.18,149.5) -- (423.22,147.79) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.61 ][line width=0.75]    (153.81,161.43) -- (322.62,161.43) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.61 ][line width=0.75]    (240.2,175.64) -- (409.01,175.64) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.61 ][line width=0.75]    (286.24,186.44) -- (455.05,186.44) ;
            		\draw [color={rgb, 255:red, 17; green, 57; blue, 105 }  ,draw opacity=1 ][line width=0.75]    (160.9,127.59) -- (238.13,194.33) ;
            		\draw [color={rgb, 255:red, 17; green, 57; blue, 105 }  ,draw opacity=1 ][line width=0.75]    (348.76,129.6) -- (452.13,193.33) ;
            		\draw  [fill={rgb, 255:red, 11; green, 69; blue, 137 }  ,fill opacity=1 ][line width=0.75]  (422.66,173.37) -- (377.13,147.67) -- (297.04,148.64) -- (332.85,173.94) -- cycle ;
            		\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ][line width=0.75]  (287.81,161.86) .. controls (281.76,157.35) and (288,153.69) .. (301.73,153.69) .. controls (315.46,153.69) and (331.5,157.35) .. (337.54,161.86) .. controls (343.58,166.37) and (337.35,170.03) .. (323.61,170.03) .. controls (309.88,170.03) and (293.85,166.37) .. (287.81,161.86) -- cycle ;
            		\draw [color={rgb, 255:red, 14; green, 56; blue, 105 }  ,draw opacity=1 ][line width=0.75]    (362.97,139.27) .. controls (111.75,150.63) and (371.36,195.21) .. (436.16,183.84) ;
            		\draw  [fill={rgb, 255:red, 14; green, 57; blue, 108 }  ,fill opacity=1 ][line width=0.75]  (420.16,108.42) -- (407.44,107.36) -- (399.93,103.5) -- (415.41,102.46) -- (420.22,105.88) -- cycle ;
            		\draw  [fill={rgb, 255:red, 20; green, 74; blue, 138 }  ,fill opacity=1 ][line width=0.75]  (447.57,152.38) -- (447.24,165.95) -- (433.84,159.47) -- (434.52,147.1) -- cycle ;
            		\draw  [fill={rgb, 255:red, 14; green, 57; blue, 108 }  ,fill opacity=1 ][line width=0.75]  (448.96,151.93) -- (447.57,152.38) -- (434.52,147.1) -- (435.54,146.5) -- cycle ;
            		\draw  [fill={rgb, 255:red, 18; green, 73; blue, 138 }  ,fill opacity=1 ][line width=0.75]  (444.23,135.19) -- (448.34,151.62) -- (435.54,146.5) -- (439.1,134.13) -- (440.46,119.65) -- (444.83,120.86) -- cycle ;
            		\draw  [fill={rgb, 255:red, 14; green, 57; blue, 108 }  ,fill opacity=1 ][line width=0.75]  (448.23,135.64) -- (452.97,150.44) -- (448.53,152.04) -- (444.23,135.19) -- (444.78,112.41) -- (448.31,112.11) -- cycle ;
            		\draw  [fill={rgb, 255:red, 14; green, 57; blue, 108 }  ,fill opacity=1 ][line width=0.75]  (452.97,150.44) -- (452.33,163.39) -- (447.24,165.95) -- (447.57,152.38) -- cycle ;
            		\draw  [fill={rgb, 255:red, 14; green, 57; blue, 108 }  ,fill opacity=1 ][line width=0.75]  (443.11,120.18) -- (441.32,119.8) -- (441.51,111.98) -- (443.39,112.17) -- cycle ;
            		\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=0.75]  (441.93,101.83) -- (448.61,105.9) -- (448.28,109.62) -- (446.72,109.53) -- (446.81,107.41) -- (441.85,104.84) -- (435.7,104.84) -- (430.88,101.98) -- cycle ;
            		\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=0.75]  (448.28,109.62) -- (448.31,112.11) -- (445.71,112.26) -- (445.77,109.72) -- cycle ;
            		\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=0.75]  (445.59,110.85) -- (445.71,112.26) -- (444.78,112.41) -- (444.41,120.56) -- (443.11,120.18) -- (443.64,110.28) -- cycle ;
            		\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=0.75]  (441.85,104.84) -- (446.81,107.41) -- (446.72,109.53) -- (445.77,109.72) -- (445.59,110.85) -- (443.64,110.28) -- (438.37,107.36) -- (435.64,107.39) -- (435.7,104.84) -- cycle ;
            		\draw [line width=0.75]    (438.37,107.36) -- (441.14,107.36) ;
            		\draw [line width=0.75]    (441.14,107.36) -- (446.09,110) ;
            		\draw  [fill={rgb, 255:red, 14; green, 57; blue, 108 }  ,fill opacity=1 ][line width=0.75]  (435.64,107.39) -- (415.28,108.89) -- (415.41,102.46) -- (430.89,101.42) -- (435.7,104.84) -- cycle ;
            		\draw [line width=0.75]    (415.84,77.81) -- (430.88,101.98) ;
            		\draw [line width=0.75]    (395.14,75.12) -- (430.89,101.42) ;
            		\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ][line width=0.75]  (428.02,101.59) -- (430.94,101.59) -- (430.98,99.9) -- (428.06,99.9) -- cycle ;
            		\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=0.75]  (416.37,74.18) -- (414.95,109.72) -- (413.32,109.7) -- (414.34,74.26) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=0.75]  (414.34,74.26) -- (413.32,109.7) -- (412.04,109.91) -- (413.23,74.09) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=0.75]  (413.23,74.09) -- (413.32,76.82) -- (393.49,75.97) -- (393.38,73.99) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=0.75]  (394.49,74.16) -- (393.62,105.85) -- (392.24,104.53) -- (393.38,73.99) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=0.75]  (412.19,106.98) -- (412.83,109.72) -- (392.95,104.72) -- (393.16,102.46) -- cycle ;
            		\draw  [line width=0.75]  (393.24,73.33) -- (414.34,74.26) -- (413.32,109.7) -- (392.24,104.53) -- cycle ;
            		\draw  [line width=0.75]  (394.59,76.07) -- (412.94,77.08) -- (412.19,106.98) -- (393.78,102.55) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 177; green, 175; blue, 175 }  ,fill opacity=1 ][line width=0.75]  (395.37,76.16) -- (394.64,102.84) -- (393.78,102.55) -- (394.59,76.07) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.29 ][line width=0.75]  (412.94,77.08) -- (412.19,106.98) -- (393.78,102.55) -- (394.59,76.07) -- cycle ;
            		\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=0.75]  (407.18,90.05) -- (406.58,104.34) -- (399.08,102.65) -- (399.42,88.89) -- cycle ;
            		\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ][line width=0.75]  (405.94,91.42) -- (405.56,102.48) -- (400.05,101.23) -- (400.29,90.55) -- cycle ;
            		\draw  [fill={rgb, 255:red, 14; green, 57; blue, 108 }  ,fill opacity=1 ][line width=0.75]  (392.73,103.74) -- (412.8,108.64) -- (413.17,96.95) -- (415.68,96.95) -- (416.25,99.47) -- (416.09,111.03) -- (413.58,111.69) -- (391.44,105.25) -- (391.72,93.81) -- (392.87,93.69) -- cycle ;
            		\draw  [fill={rgb, 255:red, 245; green, 120; blue, 35 }  ,fill opacity=1 ][line width=0.75]  (403.49,101.83) -- (403.68,106.86) -- (401.89,107.49) -- (399.49,106.86) -- (398.7,105.12) -- (398.24,102.61) -- (401.38,102.61) -- (401.2,101.45) -- cycle ;
            		\draw  [fill={rgb, 255:red, 245; green, 120; blue, 35 }  ,fill opacity=1 ,even odd rule][line width=0.75]  (382.9,103.28) .. controls (382.91,102.78) and (386.44,102.37) .. (390.78,102.37) .. controls (395.13,102.37) and (398.64,102.78) .. (398.62,103.28) .. controls (398.61,103.78) and (395.08,104.18) .. (390.74,104.18) .. controls (386.4,104.18) and (382.89,103.78) .. (382.9,103.28)(382.11,103.28) .. controls (382.13,102.34) and (386.03,101.58) .. (390.8,101.58) .. controls (395.58,101.58) and (399.44,102.34) .. (399.41,103.28) .. controls (399.39,104.21) and (395.5,104.97) .. (390.72,104.97) .. controls (385.94,104.97) and (382.09,104.21) .. (382.11,103.28) ;
            		\draw  [fill={rgb, 255:red, 245; green, 120; blue, 35 }  ,fill opacity=1 ][line width=0.75]  (399.33,105.22) -- (393.25,105.73) -- (392.02,104.47) -- (399.41,103.28) -- cycle ;
            		\draw [line width=0.75]    (382.11,103.28) .. controls (383.81,111.76) and (385.99,110.6) .. (385.46,119.65) ;
            		\draw [line width=0.75]    (399.55,104.47) .. controls (396.61,112.87) and (395.51,110.64) .. (396.14,119.31) ;
            		\draw [line width=0.75]    (388.21,110.44) .. controls (391.4,113.77) and (393.11,112.14) .. (395.81,117.42) ;
            		\draw [line width=0.75]    (385.9,110.69) .. controls (389.09,114.02) and (391.56,113.81) .. (394.26,119.09) ;
            		\draw [line width=0.75]    (384.95,112.14) .. controls (388.13,115.47) and (388.89,114) .. (391.59,119.28) ;
            		\draw [line width=0.75]    (385.21,114.27) .. controls (388.39,117.6) and (386.57,115.97) .. (388.68,119.24) ;
            		\draw [line width=0.75]    (391.79,110.5) .. controls (394.97,113.83) and (393.96,111.63) .. (395.97,114.78) ;
            		\draw [line width=0.75]    (394.73,109.87) .. controls (397.92,113.2) and (394.84,109.87) .. (395.94,111.76) ;
            		\draw [line width=0.75]    (388.21,110.44) .. controls (386.59,113.39) and (386.84,113.39) .. (385.6,116.79) ;
            		\draw [line width=0.75]    (389.99,110.57) .. controls (388.37,113.52) and (387.79,116.03) .. (386.56,119.43) ;
            		\draw [line width=0.75]    (391.79,110.5) .. controls (390.17,113.46) and (389.36,116.26) .. (388.12,119.65) ;
            		\draw [line width=0.75]    (393.85,110.82) .. controls (392.23,113.77) and (392.32,114.75) .. (390.31,120.03) ;
            		\draw [line width=0.75]    (395.79,110.69) .. controls (394.17,113.64) and (393.91,116.07) .. (392.68,119.46) ;
            		\draw [line width=0.75]    (395.97,114.78) .. controls (394.88,117.92) and (395.49,115.69) .. (394.26,119.09) ;
            		\draw [line width=0.75]    (387.82,105) .. controls (387.52,107.93) and (387.27,108.49) .. (385.18,111.73) ;
            		\draw [line width=0.75]    (383.6,104.25) .. controls (383.3,107.17) and (385.6,109.06) .. (385.9,110.69) ;
            		\draw [line width=0.75]    (385.66,105) .. controls (385.35,107.93) and (385.69,108.59) .. (385.99,110.22) ;
            		\draw [line width=0.75]    (389.5,104.88) .. controls (389.2,107.8) and (389.54,108.46) .. (389.84,110.09) ;
            		\draw [line width=0.75]    (393.42,105.1) .. controls (393.12,108.02) and (393.46,108.68) .. (393.76,110.31) ;
            		\draw [line width=0.75]    (392,105.38) .. controls (391.7,108.3) and (392.08,107.32) .. (389.99,110.57) ;
            		\draw [line width=0.75]    (387.82,105) .. controls (387.52,107.93) and (389.69,108.93) .. (389.99,110.57) ;
            		\draw [line width=0.75]    (392,105.38) .. controls (391.7,108.3) and (393.55,109.18) .. (393.85,110.82) ;
            		\draw [line width=0.75]    (395.66,105.48) .. controls (395.35,108.4) and (397.16,108.46) .. (397.46,110.09) ;
            		\draw [line width=0.75]    (395.66,105.48) .. controls (395.35,108.4) and (395.73,107.42) .. (393.64,110.66) ;
            		\draw [line width=0.75]    (397.81,105.51) .. controls (397.5,108.43) and (397.88,107.45) .. (395.79,110.69) ;
            		\draw [line width=0.75]    (387,104.82) .. controls (386.11,108.77) and (387.91,108.81) .. (388.21,110.44) ;
            		\draw [line width=0.75]    (390.67,105.48) .. controls (389.79,109.43) and (391.58,109.47) .. (391.88,111.1) ;
            		\draw [line width=0.75]    (384.78,104.6) .. controls (383.9,108.55) and (383.99,107.8) .. (384.29,109.43) ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.46 ][fill={rgb, 255:red, 208; green, 80; blue, 2 }  ,fill opacity=1 ][line width=0.75]  (268.42,52.98) .. controls (268.42,49.98) and (270.85,47.55) .. (273.85,47.55) .. controls (276.85,47.55) and (279.28,49.98) .. (279.28,52.98) .. controls (279.28,55.98) and (276.85,58.41) .. (273.85,58.41) .. controls (270.85,58.41) and (268.42,55.98) .. (268.42,52.98) -- cycle ;
            		\draw [line width=0.75]    (268.82,51.5) .. controls (270.34,54.14) and (275.54,55.99) .. (278.51,55.25) ;
            		\draw [line width=0.75]    (271.42,48.53) .. controls (272.94,51.17) and (270.34,55.62) .. (269.23,55.25) ;
            		\draw [line width=0.75]    (275.35,48.38) .. controls (272.75,51.91) and (271.27,56.18) .. (272.38,57.85) ;
            		\draw [line width=0.75]    (275.17,58.22) .. controls (273.13,55.81) and (273.68,53.77) .. (278.14,50.79) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.6 ][line width=0.75]    (271.42,48.53) .. controls (273.13,47.57) and (277.4,47.95) .. (278.51,51.85) ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.81 ][line width=0.75]  (268.42,52.98) .. controls (268.42,49.98) and (270.85,47.55) .. (273.85,47.55) .. controls (276.85,47.55) and (279.28,49.98) .. (279.28,52.98) .. controls (279.28,55.98) and (276.85,58.41) .. (273.85,58.41) .. controls (270.85,58.41) and (268.42,55.98) .. (268.42,52.98) -- cycle ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 247; green, 214; blue, 158 }  ,fill opacity=1 ][line width=0.75]  (172.39,122.67) .. controls (172.85,120.9) and (177.59,119.16) .. (178.47,118.78) .. controls (178.76,117.57) and (180.89,115.98) .. (180.04,113.51) .. controls (179.88,113.06) and (180.65,110.66) .. (180.47,110.23) .. controls (181.03,110.19) and (179.67,110.73) .. (180.47,111.17) .. controls (182.72,111.42) and (182.5,119.1) .. (181.09,121.14) .. controls (179.99,122.75) and (169.76,130.7) .. (172.39,122.67) -- cycle ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.46 ][fill={rgb, 255:red, 208; green, 80; blue, 2 }  ,fill opacity=1 ][line width=0.75]  (176.78,107.32) .. controls (176.78,104.4) and (179.15,102.04) .. (182.06,102.04) .. controls (184.98,102.04) and (187.34,104.4) .. (187.34,107.32) .. controls (187.34,110.23) and (184.98,112.59) .. (182.06,112.59) .. controls (179.15,112.59) and (176.78,110.23) .. (176.78,107.32) -- cycle ;
            		\draw [line width=0.75]    (177.17,105.88) .. controls (178.65,108.44) and (183.71,110.25) .. (186.59,109.52) ;
            		\draw [line width=0.75]    (179.7,102.99) .. controls (181.18,105.55) and (178.65,109.89) .. (177.57,109.52) ;
            		\draw [line width=0.75]    (183.52,102.84) .. controls (181,106.27) and (179.55,110.43) .. (180.64,112.05) ;
            		\draw [line width=0.75]    (183.34,112.41) .. controls (181.36,110.07) and (181.9,108.08) .. (186.23,105.19) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.6 ][line width=0.75]    (179.7,102.99) .. controls (181.36,102.06) and (185.51,102.42) .. (186.59,106.21) ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=0.75] [line join = round][line cap = round] (173.97,122.58) .. controls (173.84,122.66) and (173.72,122.74) .. (173.59,122.83) ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 247; green, 214; blue, 158 }  ,fill opacity=1 ][line width=0.75]  (170.31,121.48) .. controls (169.62,121.44) and (169.24,120.71) .. (169.12,120.72) .. controls (167.97,120.73) and (170.25,115.83) .. (173.95,116.02) .. controls (174.54,116.25) and (174.94,116.69) .. (175.26,117.2) .. controls (175.42,117.46) and (175.31,117.77) .. (175.04,118.1) .. controls (176.01,118.78) and (176.14,118.54) .. (176.21,118.78) .. controls (176.13,119.1) and (175.89,119.39) .. (175.56,119.66) .. controls (175.56,120.89) and (175.92,121.39) .. (175.18,121.7) .. controls (174.84,121.68) and (174.33,121.66) .. (173.81,121.63) .. controls (173.3,121.6) and (174.13,123.99) .. (170.94,123.99) .. controls (167.36,124.24) and (169.81,121.54) .. (170.31,121.48) -- cycle ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ][line width=0.75]  (172.57,118.91) .. controls (170.52,117.76) and (170.06,119.28) .. (171.31,120.35) .. controls (170.68,121.1) and (170.62,121.1) .. (170.12,121.16) .. controls (168.97,121.17) and (166.73,117.34) .. (168.8,115.83) .. controls (170.04,114.81) and (171.81,114.83) .. (173.95,114.58) .. controls (174.01,115.04) and (174.22,115.36) .. (174.51,115.58) .. controls (174.25,115.84) and (173.48,116.05) .. (172.62,116.19) .. controls (172.76,116.54) and (172.89,116.86) .. (173.01,117.15) .. controls (172.44,118.66) and (172.12,119.13) .. (172.57,118.91) -- cycle ;
            		\draw [line width=0.75]    (173.95,117.71) -- (175.07,117.59) ;
            		\draw [line width=0.75]    (174.57,118.28) ;
            		\draw [line width=0.75]    (174.12,118.5) -- (174.57,118.28) ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 74; green, 144; blue, 226 }  ,fill opacity=1 ][line width=0.75]  (167.3,136.94) .. controls (166.82,136.94) and (165.29,135.94) .. (167.3,132.61) .. controls (165.92,126.41) and (167.13,123.36) .. (168.93,122.46) .. controls (169.18,124.53) and (171.06,123.9) .. (171.94,123.96) .. controls (169.37,128.41) and (172.5,129.27) .. (173.44,129.48) .. controls (175.22,129.87) and (176.33,125.83) .. (176.58,126.16) .. controls (178.02,128.8) and (176.59,135.34) .. (176.2,137.07) .. controls (175.88,138.51) and (167.37,136.85) .. (167.3,136.94) -- cycle ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 247; green, 214; blue, 158 }  ,fill opacity=1 ][line width=0.75]  (171.94,123.96) .. controls (172.52,123.7) and (174.01,121.64) .. (177.39,122.14) .. controls (178.54,120.81) and (179.9,121.14) .. (180.78,120.76) .. controls (181.07,119.55) and (182.32,116.58) .. (181.47,114.12) .. controls (181.31,113.66) and (179.39,113.61) .. (179.21,113.17) .. controls (178.76,112.07) and (177.45,110.98) .. (177.33,110.23) .. controls (177.14,109.01) and (179.83,110.16) .. (179.9,109.66) .. controls (179.96,109.28) and (180.67,111.56) .. (180.96,111.54) .. controls (181.53,111.5) and (182.42,111.99) .. (183.23,112.42) .. controls (183.28,112.88) and (185.26,120.35) .. (183.85,122.39) .. controls (182.75,124) and (178.27,125.65) .. (176.58,126.16) .. controls (174.45,131.67) and (169.18,129.1) .. (171.94,123.96) -- cycle ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 247; green, 214; blue, 158 }  ,fill opacity=1 ][line width=0.75]  (179.73,157.6) .. controls (179.41,155.47) and (179.16,152.79) .. (180.65,150.34) .. controls (180.13,149.74) and (177.03,149.16) .. (179.66,149.09) .. controls (177.03,148.41) and (180.34,147.59) .. (180.17,147.15) .. controls (180.33,147.14) and (182.86,145.37) .. (183.87,147.56) .. controls (184.32,147.79) and (184.79,148.3) .. (185.23,148.98) .. controls (185.88,149.98) and (183.05,156.6) .. (182.8,157.91) .. controls (181.04,164.12) and (179.38,157.41) .. (179.73,157.6) -- cycle ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 247; green, 214; blue, 158 }  ,fill opacity=1 ][line width=0.75]  (167.56,156.6) .. controls (168.17,154.53) and (169.19,151.83) .. (171.32,150.39) .. controls (171.1,149.62) and (170.91,148.36) .. (170.91,148.14) .. controls (170.96,147.66) and (172.16,147.06) .. (172.18,146.59) .. controls (172.33,146.64) and (175.37,146.1) .. (175.37,148.51) .. controls (175.68,148.9) and (175.9,149.57) .. (176.01,150.37) .. controls (176.19,151.55) and (170.84,156.37) .. (170.06,157.46) .. controls (165.86,162.36) and (167.33,156.28) .. (167.56,156.6) -- cycle ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 74; green, 144; blue, 226 }  ,fill opacity=1 ][line width=0.75]  (168.05,136.98) .. controls (170.51,138.25) and (175.15,137.49) .. (176.03,137.56) .. controls (180.61,141.38) and (182.92,146.13) .. (183.87,146.34) .. controls (184.87,147.4) and (182.24,147.33) .. (182.49,147.65) .. controls (182.45,147.81) and (180.53,146.98) .. (180.17,147.15) .. controls (179.78,147.34) and (180.27,148.87) .. (179.66,149.09) .. controls (178.88,149.65) and (177.78,150.07) .. (176.54,150.39) .. controls (175.4,150.69) and (176.13,149.51) .. (174.9,149.66) .. controls (173.34,150.19) and (172.16,150.52) .. (170.87,150.79) .. controls (169.13,151.29) and (163.8,137.62) .. (168.05,136.98) -- cycle ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=0.75]  (167.56,156.6) .. controls (167.45,156.21) and (168.37,157.71) .. (170.06,157.46) .. controls (168.13,161.42) and (163.42,163.68) .. (167.56,156.6) -- cycle ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=0.75]  (179.73,157.6) .. controls (179.35,156.47) and (181.54,158.1) .. (182.93,157.1) .. controls (182.05,164.06) and (177.91,166.5) .. (179.73,157.6) -- cycle ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ][line width=0.75]  (165.87,159.1) .. controls (165.76,158.72) and (166.12,162.05) .. (168.88,159.67) .. controls (168.38,162.11) and (172.52,162.62) .. (172.39,163.56) .. controls (171.26,165.31) and (166.37,164.43) .. (164.06,163.01) .. controls (163.6,162.17) and (163.97,160.91) .. (165.87,159.1) -- cycle ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ][line width=0.75]  (178.91,161.17) .. controls (178.73,160.82) and (180.07,163.87) .. (182.3,160.98) .. controls (182.3,163.48) and (187.94,163.31) .. (187.94,164.25) .. controls (187.19,166.19) and (180.92,166.33) .. (178.37,165.4) .. controls (177.75,164.67) and (177.41,163.32) .. (178.91,161.17) -- cycle ;
            		\draw [line width=0.75]    (172.01,120.72) .. controls (172.83,121.04) and (172.95,121.54) .. (173.81,121.63) ;
            		\draw [line width=0.75]    (179.48,110) .. controls (179.73,110.63) and (179.78,111.96) .. (180.64,112.05) ;
            		\draw [line width=0.75]    (178.6,109.75) .. controls (178.85,110.38) and (178.9,111.71) .. (179.76,111.8) ;
            		\draw [line width=0.75]    (177.85,109.94) .. controls (178.1,110.57) and (178.54,111.69) .. (179.01,111.99) ;
            		\draw [line width=0.75]    (168.25,135.51) .. controls (168.5,136.14) and (171.64,135.65) .. (173.83,131.89) ;
            		\draw [line width=0.75]    (171.95,136.58) .. controls (172.2,137.21) and (174.33,135.65) .. (175.02,133.64) ;
            		\draw [line width=0.75]    (167.56,141.86) .. controls (170.26,145.12) and (172.89,147.94) .. (175.49,149.54) ;
            		\draw [line width=0.75]    (170.32,144.18) .. controls (173.27,146) and (173.39,145.75) .. (176.03,146.44) ;
            		\draw [line width=0.75]    (175.21,126.87) .. controls (175.46,126.81) and (175.53,126.18) .. (176.58,126.16) ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=0.75]  (172.39,163.56) .. controls (170.82,165.3) and (166.37,163.98) .. (164.06,163.01) .. controls (163.23,159.59) and (167.31,165.11) .. (172.39,163.56) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=0.75]  (187.94,164.25) .. controls (186.56,166.18) and (180.68,166.37) .. (178.37,165.4) .. controls (176.47,162.6) and (182.55,166.18) .. (187.94,164.25) -- cycle ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ][line width=0.75]    (168.93,122.46) .. controls (168.38,123.28) and (169,124.98) .. (171.94,123.96) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ][line width=0.75]    (171.94,123.96) .. controls (168.06,127.48) and (174.27,133.38) .. (176.58,126.16) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ][line width=0.75]    (170.51,150.31) .. controls (169.96,151.14) and (172.83,149.81) .. (175.09,149.31) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ][line width=0.75]    (176.03,149.87) .. controls (175.76,150.27) and (178.66,149.56) .. (179.29,148.81) .. controls (179.92,148.05) and (179.23,147.12) .. (179.92,146.8) .. controls (180.6,146.48) and (181.43,147.21) .. (182.05,147.24) .. controls (182.66,147.26) and (183.3,146.84) .. (183.74,146.74) ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.32 ][line width=0.75]  (163.94,161.95) .. controls (165.62,158.92) and (165.06,159.11) .. (167.25,160.5) .. controls (165.74,161.17) and (164.43,164.94) .. (163.94,161.95) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.32 ][line width=0.75]  (177.59,163.74) .. controls (179.28,160.71) and (178.54,161.3) .. (180.74,162.69) .. controls (179.29,163.93) and (179.29,167.95) .. (177.59,163.74) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.22 ][line width=0.75]  (165.87,159.1) .. controls (167.75,156.53) and (166.56,155.89) .. (168.75,157.28) .. controls (167.24,157.96) and (166.36,162.09) .. (165.87,159.1) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.22 ][line width=0.75]  (178.91,161.17) .. controls (180.23,158.54) and (178.85,156.27) .. (181.04,157.66) .. controls (180.17,158.05) and (180.62,161.37) .. (180.1,162.05) .. controls (179.72,162.55) and (179.12,162.44) .. (178.91,161.17) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.22 ][line width=0.75]  (167.56,156.6) .. controls (169,152.77) and (171.01,149.37) .. (173.21,150.76) .. controls (171.69,151.44) and (168.05,159.58) .. (167.56,156.6) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.22 ][line width=0.75]  (179.6,157.03) .. controls (179.25,154.17) and (180.1,151.84) .. (180.23,150.51) .. controls (178.66,148.63) and (179.69,148.86) .. (182.05,150.51) .. controls (181.19,150.89) and (180.85,154.73) .. (180.48,156.72) .. controls (180.19,158.26) and (179.82,158.34) .. (179.6,157.03) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.22 ][line width=0.75]  (170.07,156.34) .. controls (175.4,152.41) and (173.21,149.01) .. (176.03,149.87) .. controls (175.84,151.7) and (172.08,155.78) .. (170.07,156.34) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.22 ][line width=0.75]  (181.29,157.47) .. controls (182.86,153.77) and (182.24,154.02) .. (183.49,150.83) .. controls (183.3,152.66) and (182.74,156.34) .. (181.29,157.47) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.22 ][line width=0.75]  (184.74,149.7) .. controls (183.55,148) and (183.3,149.57) .. (183.36,147.44) .. controls (183.68,149.57) and (184.81,148.44) .. (184.74,149.7) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.4 ][line width=0.75]  (167.62,137.22) .. controls (168.59,136.73) and (170.13,138.15) .. (173.06,137.8) .. controls (172.75,138.79) and (170.09,138.76) .. (171.05,139.73) .. controls (171.53,140.2) and (173.38,140.79) .. (174.15,141.31) .. controls (174.59,141.62) and (171.52,141.33) .. (171.97,141.65) .. controls (173.13,142.46) and (174.59,142.63) .. (176.07,143.57) .. controls (176.5,143.85) and (173.66,143.85) .. (174.06,144.16) .. controls (174.92,144.82) and (176.26,145.6) .. (177.44,146.37) .. controls (177.87,146.66) and (176.3,147.06) .. (176.65,147.33) .. controls (177.6,148.07) and (180.14,148.61) .. (179.66,149.09) .. controls (178.52,148.79) and (177.55,150.66) .. (176.54,150.39) .. controls (175.79,150.19) and (176.15,149.72) .. (175.49,149.54) .. controls (171.55,150.51) and (170.05,150.89) .. (169.97,150.51) .. controls (166.37,143.07) and (165.37,138.64) .. (167.62,137.22) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.41 ][line width=0.75]  (167.3,136.94) .. controls (166.82,136.94) and (165.29,135.94) .. (167.3,132.61) .. controls (165.92,126.41) and (167.13,123.36) .. (168.93,122.46) .. controls (169.18,124.53) and (171.06,123.9) .. (171.94,123.96) .. controls (169.37,128.41) and (172.5,129.27) .. (173.44,129.48) .. controls (175.22,129.87) and (170.72,134.67) .. (170.97,134.99) .. controls (171.24,135.48) and (174.32,132.11) .. (174.73,132.32) .. controls (175.31,132.61) and (171.7,136.05) .. (171.95,136.58) .. controls (172.49,137.68) and (176.42,136.11) .. (176.2,137.07) .. controls (175.88,138.51) and (167.37,136.85) .. (167.3,136.94) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.22 ][line width=0.75]  (171.94,123.96) .. controls (169.05,130.65) and (175.9,132.82) .. (176.49,124.37) .. controls (174.97,125.05) and (172.43,126.95) .. (171.94,123.96) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.22 ][line width=0.75]  (176.09,125.91) .. controls (177.82,124.21) and (179.83,124.04) .. (183.85,122.39) .. controls (183.01,122.87) and (176.58,128.9) .. (176.09,125.91) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.22 ][line width=0.75]  (180.78,120.76) .. controls (182.09,123.37) and (182.84,117.35) .. (181.92,114.26) .. controls (181.08,114.73) and (181.27,123.75) .. (180.78,120.76) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.22 ][line width=0.75]  (178.47,118.78) .. controls (180.21,117.08) and (177.23,115.15) .. (181.25,113.5) .. controls (182.09,115.34) and (182.34,124.04) .. (178.47,118.78) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.22 ][line width=0.75]  (175.18,121.7) .. controls (177.41,120.86) and (179.75,119.52) .. (180.75,120.19) .. controls (179.41,121.2) and (177.41,122.2) .. (175.18,121.7) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.22 ][line width=0.75]  (170.05,118.86) .. controls (167.04,125.46) and (171.72,125.38) .. (173.81,121.63) .. controls (172.3,122.3) and (172.72,121.03) .. (170.05,118.86) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.22 ][line width=0.75]  (177.17,105.88) .. controls (174.28,112.56) and (186.75,115.76) .. (187.34,107.32) .. controls (183.85,113.84) and (177.66,108.87) .. (177.17,105.88) -- cycle ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.46 ][fill={rgb, 255:red, 208; green, 80; blue, 2 }  ,fill opacity=1 ][line width=0.75]  (215.13,70.74) .. controls (215.13,67.74) and (217.57,65.31) .. (220.56,65.31) .. controls (223.56,65.31) and (225.99,67.74) .. (225.99,70.74) .. controls (225.99,73.74) and (223.56,76.17) .. (220.56,76.17) .. controls (217.57,76.17) and (215.13,73.74) .. (215.13,70.74) -- cycle ;
            		\draw [line width=0.75]    (215.53,69.26) .. controls (217.05,71.9) and (222.25,73.76) .. (225.23,73.01) ;
            		\draw [line width=0.75]    (218.13,66.29) .. controls (219.65,68.93) and (217.05,73.38) .. (215.94,73.01) ;
            		\draw [line width=0.75]    (222.07,66.14) .. controls (219.47,69.67) and (217.98,73.94) .. (219.1,75.61) ;
            		\draw [line width=0.75]    (221.88,75.98) .. controls (219.84,73.57) and (220.4,71.53) .. (224.85,68.56) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.6 ][line width=0.75]    (218.13,66.29) .. controls (219.84,65.34) and (224.11,65.71) .. (225.23,69.61) ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.81 ][line width=0.75]  (215.13,70.74) .. controls (215.13,67.74) and (217.57,65.31) .. (220.56,65.31) .. controls (223.56,65.31) and (225.99,67.74) .. (225.99,70.74) .. controls (225.99,73.74) and (223.56,76.17) .. (220.56,76.17) .. controls (217.57,76.17) and (215.13,73.74) .. (215.13,70.74) -- cycle ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.46 ][fill={rgb, 255:red, 208; green, 80; blue, 2 }  ,fill opacity=1 ][line width=0.75]  (332.72,63.64) .. controls (332.72,60.64) and (335.15,58.21) .. (338.15,58.21) .. controls (341.15,58.21) and (343.58,60.64) .. (343.58,63.64) .. controls (343.58,66.64) and (341.15,69.07) .. (338.15,69.07) .. controls (335.15,69.07) and (332.72,66.64) .. (332.72,63.64) -- cycle ;
            		\draw [line width=0.75]    (333.12,62.16) .. controls (334.64,64.79) and (339.84,66.65) .. (342.81,65.91) ;
            		\draw [line width=0.75]    (335.72,59.19) .. controls (337.24,61.82) and (334.64,66.28) .. (333.52,65.91) ;
            		\draw [line width=0.75]    (339.65,59.04) .. controls (337.05,62.57) and (335.57,66.84) .. (336.68,68.51) ;
            		\draw [line width=0.75]    (339.47,68.88) .. controls (337.42,66.47) and (337.98,64.42) .. (342.44,61.45) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.6 ][line width=0.75]    (335.72,59.19) .. controls (337.42,58.23) and (341.7,58.6) .. (342.81,62.5) ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.81 ][line width=0.75]  (332.72,63.64) .. controls (332.72,60.64) and (335.15,58.21) .. (338.15,58.21) .. controls (341.15,58.21) and (343.58,60.64) .. (343.58,63.64) .. controls (343.58,66.64) and (341.15,69.07) .. (338.15,69.07) .. controls (335.15,69.07) and (332.72,66.64) .. (332.72,63.64) -- cycle ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.46 ][fill={rgb, 255:red, 208; green, 80; blue, 2 }  ,fill opacity=1 ][line width=0.75]  (186.72,94.54) .. controls (186.72,91.54) and (189.15,89.11) .. (192.14,89.11) .. controls (195.14,89.11) and (197.57,91.54) .. (197.57,94.54) .. controls (197.57,97.54) and (195.14,99.97) .. (192.14,99.97) .. controls (189.15,99.97) and (186.72,97.54) .. (186.72,94.54) -- cycle ;
            		\draw [line width=0.75]    (187.11,93.06) .. controls (188.63,95.7) and (193.83,97.56) .. (196.81,96.81) ;
            		\draw [line width=0.75]    (189.71,90.09) .. controls (191.23,92.73) and (188.63,97.19) .. (187.52,96.81) ;
            		\draw [line width=0.75]    (193.65,89.94) .. controls (191.05,93.47) and (189.56,97.74) .. (190.68,99.41) ;
            		\draw [line width=0.75]    (193.46,99.79) .. controls (191.42,97.37) and (191.98,95.33) .. (196.43,92.36) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.6 ][line width=0.75]    (189.71,90.09) .. controls (191.42,89.14) and (195.69,89.51) .. (196.81,93.41) ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.81 ][line width=0.75]  (186.72,94.54) .. controls (186.72,91.54) and (189.15,89.11) .. (192.14,89.11) .. controls (195.14,89.11) and (197.57,91.54) .. (197.57,94.54) .. controls (197.57,97.54) and (195.14,99.97) .. (192.14,99.97) .. controls (189.15,99.97) and (186.72,97.54) .. (186.72,94.54) -- cycle ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.46 ][fill={rgb, 255:red, 208; green, 80; blue, 2 }  ,fill opacity=1 ][line width=0.75]  (240.71,59.37) .. controls (240.71,56.38) and (243.14,53.94) .. (246.14,53.94) .. controls (249.14,53.94) and (251.57,56.38) .. (251.57,59.37) .. controls (251.57,62.37) and (249.14,64.8) .. (246.14,64.8) .. controls (243.14,64.8) and (240.71,62.37) .. (240.71,59.37) -- cycle ;
            		\draw [line width=0.75]    (241.11,57.89) .. controls (242.63,60.53) and (247.83,62.39) .. (250.8,61.65) ;
            		\draw [line width=0.75]    (243.71,54.92) .. controls (245.23,57.56) and (242.63,62.02) .. (241.52,61.65) ;
            		\draw [line width=0.75]    (247.65,54.77) .. controls (245.05,58.3) and (243.56,62.57) .. (244.67,64.25) ;
            		\draw [line width=0.75]    (247.46,64.62) .. controls (245.42,62.2) and (245.97,60.16) .. (250.43,57.19) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.6 ][line width=0.75]    (243.71,54.92) .. controls (245.42,53.97) and (249.69,54.34) .. (250.8,58.24) ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.81 ][line width=0.75]  (240.71,59.37) .. controls (240.71,56.38) and (243.14,53.94) .. (246.14,53.94) .. controls (249.14,53.94) and (251.57,56.38) .. (251.57,59.37) .. controls (251.57,62.37) and (249.14,64.8) .. (246.14,64.8) .. controls (243.14,64.8) and (240.71,62.37) .. (240.71,59.37) -- cycle ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.46 ][fill={rgb, 255:red, 208; green, 80; blue, 2 }  ,fill opacity=1 ][line width=0.75]  (302.17,54.4) .. controls (302.17,51.4) and (304.6,48.97) .. (307.6,48.97) .. controls (310.6,48.97) and (313.03,51.4) .. (313.03,54.4) .. controls (313.03,57.4) and (310.6,59.83) .. (307.6,59.83) .. controls (304.6,59.83) and (302.17,57.4) .. (302.17,54.4) -- cycle ;
            		\draw [line width=0.75]    (302.56,52.92) .. controls (304.09,55.56) and (309.29,57.42) .. (312.26,56.67) ;
            		\draw [line width=0.75]    (305.17,49.95) .. controls (306.69,52.59) and (304.09,57.04) .. (302.97,56.67) ;
            		\draw [line width=0.75]    (309.1,49.8) .. controls (306.5,53.33) and (305.02,57.6) .. (306.13,59.27) ;
            		\draw [line width=0.75]    (308.92,59.64) .. controls (306.87,57.23) and (307.43,55.19) .. (311.89,52.21) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.6 ][line width=0.75]    (305.17,49.95) .. controls (306.87,49) and (311.15,49.37) .. (312.26,53.27) ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.81 ][line width=0.75]  (302.17,54.4) .. controls (302.17,51.4) and (304.6,48.97) .. (307.6,48.97) .. controls (310.6,48.97) and (313.03,51.4) .. (313.03,54.4) .. controls (313.03,57.4) and (310.6,59.83) .. (307.6,59.83) .. controls (304.6,59.83) and (302.17,57.4) .. (302.17,54.4) -- cycle ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.46 ][fill={rgb, 255:red, 208; green, 80; blue, 2 }  ,fill opacity=1 ][line width=0.75]  (355.81,76.43) .. controls (355.81,73.43) and (358.24,71) .. (361.24,71) .. controls (364.24,71) and (366.67,73.43) .. (366.67,76.43) .. controls (366.67,79.42) and (364.24,81.85) .. (361.24,81.85) .. controls (358.24,81.85) and (355.81,79.42) .. (355.81,76.43) -- cycle ;
            		\draw [line width=0.75]    (356.21,74.95) .. controls (357.73,77.58) and (362.93,79.44) .. (365.9,78.7) ;
            		\draw [line width=0.75]    (358.81,71.97) .. controls (360.33,74.61) and (357.73,79.07) .. (356.62,78.7) ;
            		\draw [line width=0.75]    (362.74,71.83) .. controls (360.14,75.35) and (358.66,79.63) .. (359.77,81.3) ;
            		\draw [line width=0.75]    (362.56,81.67) .. controls (360.52,79.25) and (361.07,77.21) .. (365.53,74.24) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.6 ][line width=0.75]    (358.81,71.97) .. controls (360.52,71.02) and (364.79,71.39) .. (365.9,75.29) ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.81 ][line width=0.75]  (355.81,76.43) .. controls (355.81,73.43) and (358.24,71) .. (361.24,71) .. controls (364.24,71) and (366.67,73.43) .. (366.67,76.43) .. controls (366.67,79.42) and (364.24,81.85) .. (361.24,81.85) .. controls (358.24,81.85) and (355.81,79.42) .. (355.81,76.43) -- cycle ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.46 ][fill={rgb, 255:red, 208; green, 80; blue, 2 }  ,fill opacity=1 ][line width=0.75]  (382.45,96.67) .. controls (382.45,93.68) and (384.88,91.24) .. (387.88,91.24) .. controls (390.88,91.24) and (393.31,93.68) .. (393.31,96.67) .. controls (393.31,99.67) and (390.88,102.1) .. (387.88,102.1) .. controls (384.88,102.1) and (382.45,99.67) .. (382.45,96.67) -- cycle ;
            		\draw [line width=0.75]    (382.85,95.19) .. controls (384.37,97.83) and (389.57,99.69) .. (392.54,98.95) ;
            		\draw [line width=0.75]    (385.45,92.22) .. controls (386.97,94.86) and (384.37,99.32) .. (383.26,98.95) ;
            		\draw [line width=0.75]    (389.39,92.07) .. controls (386.79,95.6) and (385.3,99.87) .. (386.42,101.55) ;
            		\draw [line width=0.75]    (389.2,101.92) .. controls (387.16,99.5) and (387.72,97.46) .. (392.17,94.49) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.6 ][line width=0.75]    (385.45,92.22) .. controls (387.16,91.27) and (391.43,91.64) .. (392.54,95.54) ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.81 ][line width=0.75]  (382.45,96.67) .. controls (382.45,93.68) and (384.88,91.24) .. (387.88,91.24) .. controls (390.88,91.24) and (393.31,93.68) .. (393.31,96.67) .. controls (393.31,99.67) and (390.88,102.1) .. (387.88,102.1) .. controls (384.88,102.1) and (382.45,99.67) .. (382.45,96.67) -- cycle ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.46 ][fill={rgb, 255:red, 208; green, 80; blue, 2 }  ,fill opacity=1 ][line width=0.75]  (371.09,86.37) .. controls (371.09,83.37) and (373.52,80.94) .. (376.51,80.94) .. controls (379.51,80.94) and (381.94,83.37) .. (381.94,86.37) .. controls (381.94,89.37) and (379.51,91.8) .. (376.51,91.8) .. controls (373.52,91.8) and (371.09,89.37) .. (371.09,86.37) -- cycle ;
            		\draw [line width=0.75]    (371.48,84.89) .. controls (373,87.53) and (378.21,89.39) .. (381.18,88.64) ;
            		\draw [line width=0.75]    (374.08,81.92) .. controls (375.6,84.56) and (373,89.02) .. (371.89,88.64) ;
            		\draw [line width=0.75]    (378.02,81.77) .. controls (375.42,85.3) and (373.93,89.57) .. (375.05,91.24) ;
            		\draw [line width=0.75]    (377.83,91.62) .. controls (375.79,89.2) and (376.35,87.16) .. (380.81,84.19) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.6 ][line width=0.75]    (374.08,81.92) .. controls (375.79,80.97) and (380.06,81.34) .. (381.18,85.24) ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.81 ][line width=0.75]  (371.09,86.37) .. controls (371.09,83.37) and (373.52,80.94) .. (376.51,80.94) .. controls (379.51,80.94) and (381.94,83.37) .. (381.94,86.37) .. controls (381.94,89.37) and (379.51,91.8) .. (376.51,91.8) .. controls (373.52,91.8) and (371.09,89.37) .. (371.09,86.37) -- cycle ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.46 ][fill={rgb, 255:red, 208; green, 80; blue, 2 }  ,fill opacity=1 ][line width=0.75]  (198.44,84.24) .. controls (198.44,81.24) and (200.87,78.81) .. (203.87,78.81) .. controls (206.87,78.81) and (209.3,81.24) .. (209.3,84.24) .. controls (209.3,87.24) and (206.87,89.67) .. (203.87,89.67) .. controls (200.87,89.67) and (198.44,87.24) .. (198.44,84.24) -- cycle ;
            		\draw [line width=0.75]    (198.83,82.76) .. controls (200.36,85.4) and (205.56,87.26) .. (208.53,86.51) ;
            		\draw [line width=0.75]    (201.43,79.79) .. controls (202.96,82.43) and (200.36,86.88) .. (199.24,86.51) ;
            		\draw [line width=0.75]    (205.37,79.64) .. controls (202.77,83.17) and (201.29,87.44) .. (202.4,89.11) ;
            		\draw [line width=0.75]    (205.19,89.48) .. controls (203.14,87.07) and (203.7,85.03) .. (208.16,82.06) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.6 ][line width=0.75]    (201.43,79.79) .. controls (203.14,78.84) and (207.41,79.21) .. (208.53,83.11) ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.81 ][line width=0.75]  (198.44,84.24) .. controls (198.44,81.24) and (200.87,78.81) .. (203.87,78.81) .. controls (206.87,78.81) and (209.3,81.24) .. (209.3,84.24) .. controls (209.3,87.24) and (206.87,89.67) .. (203.87,89.67) .. controls (200.87,89.67) and (198.44,87.24) .. (198.44,84.24) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.25 ] (393.76,161.44) .. controls (397.78,159.43) and (420.96,164.24) .. (434.56,157.04) .. controls (444.96,160.24) and (474.73,164.99) .. (447.24,165.95) .. controls (424.96,163.44) and (397.36,167.44) .. (393.76,161.44) -- cycle ;
            		\draw    (182.06,107.32) -- (374.96,105.06) ;
            		\draw [shift={(376.96,105.04)}, rotate = 179.33] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (12,-3) -- (0,0) -- (12,3) -- cycle    ;
            		\draw    (182.06,107.32) -- (181.38,31.44) ;
            		\draw [shift={(181.36,29.44)}, rotate = 89.48] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (12,-3) -- (0,0) -- (12,3) -- cycle    ;
            		\draw (159,99) node [anchor=north west][inner sep=0.75pt]    {$O$};
            		\draw (363.76,111) node [anchor=north west][inner sep=0.75pt]    {$x$};
            		\draw (165.36,29) node [anchor=north west][inner sep=0.75pt]    {$y$};
            	\end{tikzpicture}
            \end{center}'''
                # Nội dung lời giải
                loigiai = ('''Chọn hệ trục tọa độ $Oxy$ như hình vẽ. %s Theo giả thiết ta có \\\\
            $\\begin{cases} -\\frac{b}{2a} = %s \\\\ %sa + %sb + c = %s \\\\ a + b + c = %s \\end{cases} \\Leftrightarrow \\begin{cases} %sa + b = 0 \\\\ %sa + %sb + c = %s \\\\ a + b + c = %s \\end{cases} \\Leftrightarrow \\begin{cases} a = %s \\\\ b = %s \\\\ c = %s \\end{cases}$ \\\\
            $\\Rightarrow f\\left(x\\right) = %s$ \\\\
            Lại có: $a = %s < 0$; $-\\frac{b}{2a} = %s \\Rightarrow$ hàm số đồng biến trên $\\left(-\\infty; %s\\right)$ và nghịch biến trên $\\left(%s; +\\infty\\right)$ \\\\
            Suy ra $d = %s \\Rightarrow %s + d = %s$'''
                           %(hinhve1, xv, xv**2, xv, yv, y1,
                             2*xv, xv**2, xv, yv, y1,
                             a, b, c,
                             fx_str,
                             a, xv, xv, xv,
                             xv, N, kq_num))
                dapan='\\shortans[0]{$%s$}\n'%(kq_num)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                       '\\loigiai{'+str(loigiai)+'}\n'
                       '\\end{ex}\n\\end{minipage} \n\n')
            return content


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


def bt_dang9_p3_b4_c3_hh10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Thiết lập các thông số ngẫu nhiên cho bài toán elip
                # cao = b, rong = 2a
                cao = randint(6, 12)
                rong = randint(16, 30)
                if rong % 2 != 0: rong += 1 # Đảm bảo chiều rộng chẵn để a là số nguyên

                a_val = Rational(rong, 2)
                b_val = cao

                # Khoảng cách từ điểm đến chân tường (phải nhỏ hơn a)
                dist_wall = randint(3, int(a_val) - 2)

                # Tọa độ x của điểm đó (x = a - khoảng cách từ tường)
                x_val = a_val - dist_wall

                # Tính y dựa trên phương trình elip: x^2/a^2 + y^2/b^2 = 1
                # y = sqrt(b^2 * (1 - x^2/a^2))
                y_squared = b_val**2 * (1 - Rational(x_val**2, a_val**2))
                y_result = sqrt(y_squared)

                # Chuyển đổi sang số thập phân để làm tròn
                val_float = float(y_result.evalf())
                kq_dec = Decimal(str(val_float)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq = str(kq_dec).replace('.', ',')

                # Đáp án đúng
                du = ['$%s$ m' % (kq)]
                da = random.choice(du)

                # Tạo các phương án sai (không trùng đáp án đúng)
                kq_float = float(kq_dec)
                s = []
                offsets = [1.2, 2.5, 3.1, -1.5, -2.2, -0.8]
                for offset in offsets:
                    sai_val = round(kq_float + offset, 1)
                    sai_str = ('$%s$ m' % (str(sai_val).replace('.', ',')))
                    if sai_str != da:
                        s.append(sai_str)

                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                hinhve=r'''\begin{center}
            	\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
                \tikzset {_hojs09dfs/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 14.5 bp }  }  \pgftransformrotate{-89 }  \pgftransformscale{2 }  }}}
            	\pgfdeclarehorizontalshading{_q5ugmfv2m}{150bp}{rgb(0bp)=(0.15,0.71,0.98);
            		rgb(37.5bp)=(0.15,0.71,0.98);
            		rgb(62.5bp)=(1,1,1);
            		rgb(100bp)=(1,1,1)}
            	\tikzset{every picture/.style={line width=0.75pt}} 
            		\draw  [draw opacity=0][shading=_q5ugmfv2m,_hojs09dfs] (115.4,28.4) -- (490.53,28.4) -- (490.53,205.83) -- (115.4,205.83) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 235; green, 216; blue, 183 }  ,fill opacity=1 ] (115.87,163.73) -- (115.4,205.83) -- (251.01,160.23) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 235; green, 216; blue, 183 }  ,fill opacity=1 ] (490.53,162.4) -- (490.53,205.83) -- (361.36,160.71) -- cycle ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (373.12,165.4) -- (378.55,151.9) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (226.45,168.23) -- (233.7,156.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (372.5,154.48) -- (380.49,167.11) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (404.25,144.98) -- (401.1,164.9) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (396.35,147.4) -- (406.5,161.23) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (233.35,168.42) -- (227.95,155.98) ;
            		\draw  [fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (356.8,159.98) -- (489.8,205.53) -- (115.4,205.83) -- (254.67,159.73) -- cycle ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ][line width=1.5]    (254.8,158.43) -- (156.13,192.92) ;
            		\draw  [draw opacity=0][line width=0.75]  (214.58,173.43) .. controls (214.33,170.77) and (214.2,168.08) .. (214.2,165.36) .. controls (214.2,117.65) and (253.71,78.98) .. (302.45,78.98) .. controls (351.19,78.98) and (390.7,117.65) .. (390.7,165.36) .. controls (390.7,167.48) and (390.62,169.58) .. (390.47,171.67) -- (302.45,165.36) -- cycle ; \draw  [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ][line width=0.75]  (214.58,173.43) .. controls (214.33,170.77) and (214.2,168.08) .. (214.2,165.36) .. controls (214.2,117.65) and (253.71,78.98) .. (302.45,78.98) .. controls (351.19,78.98) and (390.7,117.65) .. (390.7,165.36) .. controls (390.7,167.48) and (390.62,169.58) .. (390.47,171.67) ;  
            		\draw  [draw opacity=0][line width=0.75]  (219.27,172.01) .. controls (219.22,170.81) and (219.2,169.61) .. (219.2,168.41) .. controls (219.2,120.7) and (256.58,82.03) .. (302.7,82.03) .. controls (348.82,82.03) and (386.2,120.7) .. (386.2,168.41) .. controls (386.2,169.19) and (386.19,169.97) .. (386.17,170.74) -- (302.7,168.41) -- cycle ; \draw  [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ][line width=0.75]  (219.27,172.01) .. controls (219.22,170.81) and (219.2,169.61) .. (219.2,168.41) .. controls (219.2,120.7) and (256.58,82.03) .. (302.7,82.03) .. controls (348.82,82.03) and (386.2,120.7) .. (386.2,168.41) .. controls (386.2,169.19) and (386.19,169.97) .. (386.17,170.74) ;  
            		\draw  [draw opacity=0][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=0.73 ] (352.6,160.98) -- (356.8,159.98) -- (489.8,205.53) -- (466.3,205.73) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=0.74 ] (245.11,162.03) -- (250.26,162.36) -- (135.9,205.83) -- (115.4,205.83) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (261.85,160.48) -- (160.9,205.33) -- (150.4,205.33) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (352.6,160.98) -- (451.3,205.03) -- (443.3,205.03) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (306.13,159.32) -- (309.3,204.03) -- (303.3,203.53) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=0.63 ] (315.8,178.23) -- (387.55,178.98) -- (359.96,182.47) -- (358.45,184.15) -- (355.53,183.02) -- (347.01,184.1) -- (343.2,187.15) -- (340.45,187.65) -- (336.7,185.4) -- (314.53,187.04) -- (309.5,189.23) -- (302.5,189.23) -- (297.5,186.48) -- (276.19,183.47) -- (272.7,185.4) -- (267.95,185.15) -- (265.69,181.99) -- (256.73,180.72) -- (254.7,181.4) -- (252.35,180.1) -- (230.3,176.98) -- (296.55,177.98) -- (306.05,174.23) -- cycle ;
            		\draw  [draw opacity=0][line width=1.5]  (254.67,159.73) .. controls (254.67,159.73) and (254.67,159.73) .. (254.67,159.73) .. controls (254.67,129.54) and (276.71,105.07) .. (303.9,105.07) .. controls (331.09,105.07) and (353.13,129.54) .. (353.13,159.73) .. controls (353.13,159.97) and (353.13,160.2) .. (353.13,160.43) -- (303.9,159.73) -- cycle ; \draw  [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ][line width=1.5]  (254.67,159.73) .. controls (254.67,159.73) and (254.67,159.73) .. (254.67,159.73) .. controls (254.67,129.54) and (276.71,105.07) .. (303.9,105.07) .. controls (331.09,105.07) and (353.13,129.54) .. (353.13,159.73) .. controls (353.13,159.97) and (353.13,160.2) .. (353.13,160.43) ;  
            		\draw  [draw opacity=0][line width=1.5]  (251.01,160.23) .. controls (251,159.9) and (251,159.57) .. (251,159.23) .. controls (251,127.11) and (274.68,101.07) .. (303.9,101.07) .. controls (333.12,101.07) and (356.8,127.11) .. (356.8,159.23) .. controls (356.8,159.48) and (356.8,159.73) .. (356.8,159.98) -- (303.9,159.23) -- cycle ; \draw  [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ][line width=1.5]  (251.01,160.23) .. controls (251,159.9) and (251,159.57) .. (251,159.23) .. controls (251,127.11) and (274.68,101.07) .. (303.9,101.07) .. controls (333.12,101.07) and (356.8,127.11) .. (356.8,159.23) .. controls (356.8,159.48) and (356.8,159.73) .. (356.8,159.98) ;  
            		\draw  [draw opacity=0][line width=1.5]  (233.35,168.42) .. controls (233.34,167.8) and (233.33,167.19) .. (233.33,166.57) .. controls (233.33,125.24) and (264.63,91.73) .. (303.23,91.73) .. controls (341.47,91.73) and (372.54,124.61) .. (373.12,165.4) -- (303.23,166.57) -- cycle ; \draw  [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ][line width=1.5]  (233.35,168.42) .. controls (233.34,167.8) and (233.33,167.19) .. (233.33,166.57) .. controls (233.33,125.24) and (264.63,91.73) .. (303.23,91.73) .. controls (341.47,91.73) and (372.54,124.61) .. (373.12,165.4) ;  
            		\draw  [draw opacity=0][line width=1.5]  (226.27,170.45) .. controls (226.26,169.77) and (226.25,169.08) .. (226.25,168.4) .. controls (226.25,122.38) and (260.78,85.07) .. (303.38,85.07) .. controls (345.57,85.07) and (379.85,121.68) .. (380.49,167.11) -- (303.38,168.4) -- cycle ; \draw  [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ][line width=1.5]  (226.27,170.45) .. controls (226.26,169.77) and (226.25,169.08) .. (226.25,168.4) .. controls (226.25,122.38) and (260.78,85.07) .. (303.38,85.07) .. controls (345.57,85.07) and (379.85,121.68) .. (380.49,167.11) ;  
            		\draw  [draw opacity=0][line width=2.25]  (206.85,178.8) .. controls (206.83,177.95) and (206.82,177.09) .. (206.82,176.23) .. controls (206.82,120.73) and (250.1,75.73) .. (303.48,75.73) .. controls (356.86,75.73) and (400.13,120.73) .. (400.13,176.23) .. controls (400.13,176.47) and (400.13,176.71) .. (400.13,176.94) -- (303.48,176.23) -- cycle ; \draw  [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ][line width=2.25]  (206.85,178.8) .. controls (206.83,177.95) and (206.82,177.09) .. (206.82,176.23) .. controls (206.82,120.73) and (250.1,75.73) .. (303.48,75.73) .. controls (356.86,75.73) and (400.13,120.73) .. (400.13,176.23) .. controls (400.13,176.47) and (400.13,176.71) .. (400.13,176.94) ;  
            		\draw  [draw opacity=0][line width=2.25]  (198.71,179.49) .. controls (198.55,177.1) and (198.47,174.69) .. (198.47,172.26) .. controls (198.47,114.53) and (245.49,67.73) .. (303.49,67.73) .. controls (361.49,67.73) and (408.52,114.53) .. (408.52,172.26) .. controls (408.52,174.11) and (408.47,175.94) .. (408.37,177.77) -- (303.49,172.26) -- cycle ; \draw  [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ][line width=2.25]  (198.71,179.49) .. controls (198.55,177.1) and (198.47,174.69) .. (198.47,172.26) .. controls (198.47,114.53) and (245.49,67.73) .. (303.49,67.73) .. controls (361.49,67.73) and (408.52,114.53) .. (408.52,172.26) .. controls (408.52,174.11) and (408.47,175.94) .. (408.37,177.77) ;  
            		\draw  [draw opacity=0][line width=3]  (172.1,194.12) .. controls (171.68,190.1) and (171.47,186.02) .. (171.47,181.9) .. controls (171.47,113.14) and (230.94,57.4) .. (304.3,57.4) .. controls (377.66,57.4) and (437.13,113.14) .. (437.13,181.9) .. controls (437.13,185.07) and (437.01,188.21) .. (436.76,191.33) -- (304.3,181.9) -- cycle ; \draw  [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ][line width=3]  (172.1,194.12) .. controls (171.68,190.1) and (171.47,186.02) .. (171.47,181.9) .. controls (171.47,113.14) and (230.94,57.4) .. (304.3,57.4) .. controls (377.66,57.4) and (437.13,113.14) .. (437.13,181.9) .. controls (437.13,185.07) and (437.01,188.21) .. (436.76,191.33) ;  
            		\draw  [draw opacity=0][line width=3]  (156.13,192.92) .. controls (156.17,111.26) and (222.2,45.07) .. (303.63,45.07) .. controls (384.8,45.07) and (450.66,110.83) .. (451.13,192.12) -- (303.63,193) -- cycle ; \draw  [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ][line width=3]  (156.13,192.92) .. controls (156.17,111.26) and (222.2,45.07) .. (303.63,45.07) .. controls (384.8,45.07) and (450.66,110.83) .. (451.13,192.12) ;  
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ][line width=1.5]    (251.2,147.73) -- (158,173.33) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ][line width=1.5]    (258.8,127.73) -- (176.4,118.93) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ][line width=1.5]    (271.6,112.53) -- (212.8,77.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ][line width=1.5]    (290.8,101.73) -- (268.4,49.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ][line width=1.5]    (316.4,101.33) -- (338.8,50.13) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ][line width=1.5]    (335.2,112.13) -- (394.8,77.33) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ][line width=1.5]    (348.3,127.48) -- (430,118.93) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ][line width=1.5]    (356.4,147.73) -- (448,171.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ][line width=1.5]    (303.25,105.98) -- (302.5,160.48) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ][line width=1.5]    (325.2,111.33) -- (324,160.13) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ][line width=1.5]    (281.2,110.93) -- (281.6,161.33) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ][line width=1.5]    (324.8,118.93) -- (281.6,118.93) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ][line width=1.5]    (348,137.33) -- (325.3,137.23) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ][line width=1.5]    (282,138.13) -- (258.3,138.48) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (448.75,172.73) -- (437.6,176.93) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (437.75,131.73) -- (428.6,136.93) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (414.5,95.23) -- (407.85,103.78) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (382.75,68.48) -- (377.35,77.28) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (343.5,51.23) -- (341.6,61.78) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (304.25,45.23) -- (303.85,57.03) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (407.75,161.73) -- (399.75,165.48) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (400.75,132.73) -- (393.5,136.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (384.25,105.73) -- (378.25,112.23) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (361.5,85.23) -- (357.25,92.23) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (333.25,72.73) -- (332,79.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (376.75,152.73) -- (372.5,154.48) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (373,132.98) -- (367.5,136.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (360.75,113.23) -- (356.5,117.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (345.25,98.73) -- (342,104.23) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (325,88.98) -- (323.5,94.23) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (303.75,68.23) -- (303.75,74.98) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (304,85.73) -- (303.75,91.48) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (303.25,101.73) -- (303.45,104.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (317.75,103.48) -- (317.25,106.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (331,109.73) -- (329.5,112.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (342.5,119.73) -- (340,122.23) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (350.25,132.98) -- (347.25,134.98) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (355,147.48) -- (352.25,147.98) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (408.25,176.73) -- (400.13,176.74) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (380.49,167.11) -- (372.85,166.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (263.75,51.23) -- (264.9,62.23) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (274.25,71.73) -- (275.15,79.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (282.5,87.73) -- (283.15,94.98) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (289.5,103.23) -- (290.15,106.98) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (224.75,67.73) -- (230.4,77.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (246,84.48) -- (249.65,91.98) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (262,98.23) -- (264.9,102.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (275.5,110.48) -- (277.4,113.48) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (193.75,94.73) -- (201.15,104.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (223,105.23) -- (228.65,111.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (245.75,113.73) -- (249.9,117.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (170,131.23) -- (180.7,138.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (206.3,133.73) -- (213.7,137.98) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (233.75,133.23) -- (238.95,135.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (158,173.33) -- (171.45,178.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (199.45,164.48) -- (207.45,166.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (227.95,155.98) -- (233.7,156.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (265.5,120.48) -- (267.7,122.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (257,133.73) -- (260.2,134.98) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (251.2,147.73) -- (255.95,148.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (198.7,178.73) -- (206.85,178.8) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (226.45,168.23) -- (233.35,168.42) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ][line width=1.5]    (451.13,191.61) -- (356.8,159.98) ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.5 ][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (306.45,105.43) -- (308.28,153.82) -- (303.95,151.82) -- cycle ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.5 ][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (350.7,152.82) -- (315.7,158.82) -- (313.37,155.15) -- cycle ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.5 ][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (261.37,153.15) -- (297.37,159.15) -- (298.37,155.82) -- cycle ;
            		\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (395.7,158.82) -- (405.03,154.15) -- (397.03,160.82) -- (314.7,170.82) -- (317.03,163.82) -- cycle ;
            		\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (217.7,159.15) -- (299.03,164.15) -- (298.37,169.82) -- (218.7,162.48) -- (208.03,154.48) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.55 ] (397.03,160.82) -- (314.7,170.82) -- (316.9,167.75) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.55 ] (218.7,162.48) -- (298.37,169.82) -- (297.6,166.73) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.88 ] (218.92,159.53) -- (298.6,165.48) -- (299.03,164.15) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.88 ] (369.6,161.23) -- (317.35,166.23) -- (317.78,164.9) -- cycle ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.46 ][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (264.6,174.85) .. controls (264.6,170.92) and (267.57,167.73) .. (271.22,167.73) .. controls (274.88,167.73) and (277.85,170.92) .. (277.85,174.85) .. controls (277.85,178.79) and (274.88,181.98) .. (271.22,181.98) .. controls (267.57,181.98) and (264.6,178.79) .. (264.6,174.85) -- cycle ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (266.06,174.48) .. controls (266.06,171.63) and (268.37,169.31) .. (271.22,169.31) .. controls (274.08,169.31) and (276.39,171.63) .. (276.39,174.48) .. controls (276.39,177.34) and (274.08,179.65) .. (271.22,179.65) .. controls (268.37,179.65) and (266.06,177.34) .. (266.06,174.48) -- cycle ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.46 ][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (333.85,175.73) .. controls (333.85,171.59) and (336.82,168.23) .. (340.47,168.23) .. controls (344.13,168.23) and (347.1,171.59) .. (347.1,175.73) .. controls (347.1,179.88) and (344.13,183.23) .. (340.47,183.23) .. controls (336.82,183.23) and (333.85,179.88) .. (333.85,175.73) -- cycle ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (335.31,175.73) .. controls (335.31,172.88) and (337.62,170.56) .. (340.47,170.56) .. controls (343.33,170.56) and (345.64,172.88) .. (345.64,175.73) .. controls (345.64,178.59) and (343.33,180.9) .. (340.47,180.9) .. controls (337.62,180.9) and (335.31,178.59) .. (335.31,175.73) -- cycle ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.46 ][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (249.6,170.58) .. controls (249.6,167.76) and (251.61,165.48) .. (254.1,165.48) .. controls (256.59,165.48) and (258.6,167.76) .. (258.6,170.58) .. controls (258.6,173.39) and (256.59,175.67) .. (254.1,175.67) .. controls (251.61,175.67) and (249.6,173.39) .. (249.6,170.58) -- cycle ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (250.59,170.58) .. controls (250.59,168.64) and (252.16,167.07) .. (254.1,167.07) .. controls (256.04,167.07) and (257.61,168.64) .. (257.61,170.58) .. controls (257.61,172.52) and (256.04,174.09) .. (254.1,174.09) .. controls (252.16,174.09) and (250.59,172.52) .. (250.59,170.58) -- cycle ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.46 ][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (353.1,170.33) .. controls (353.1,167.51) and (355.11,165.23) .. (357.6,165.23) .. controls (360.09,165.23) and (362.1,167.51) .. (362.1,170.33) .. controls (362.1,173.14) and (360.09,175.42) .. (357.6,175.42) .. controls (355.11,175.42) and (353.1,173.14) .. (353.1,170.33) -- cycle ;
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (354.09,170.33) .. controls (354.09,168.39) and (355.66,166.82) .. (357.6,166.82) .. controls (359.54,166.82) and (361.11,168.39) .. (361.11,170.33) .. controls (361.11,172.27) and (359.54,173.84) .. (357.6,173.84) .. controls (355.66,173.84) and (354.09,172.27) .. (354.09,170.33) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 252; green, 247; blue, 183 }  ,fill opacity=1 ] (267.77,168.34) -- (268.62,165.88) -- (273.97,166.08) -- (274.62,168.6) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 252; green, 247; blue, 183 }  ,fill opacity=1 ] (337.1,169.61) -- (337.75,167.09) -- (343.1,166.89) -- (343.95,169.35) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 252; green, 247; blue, 183 }  ,fill opacity=1 ] (252.06,166.41) -- (252.74,164.43) -- (255.54,164.53) -- (256.06,166.56) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 252; green, 247; blue, 183 }  ,fill opacity=1 ] (355.91,165.91) -- (356.5,163.9) -- (359.29,163.87) -- (359.91,165.88) -- cycle ;
            		\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (307.1,175.7) .. controls (307.1,175.66) and (307.07,175.63) .. (307.03,175.63) -- (306.83,175.63) .. controls (306.79,175.63) and (306.76,175.66) .. (306.76,175.7) -- (306.76,181.79) .. controls (306.76,181.83) and (306.79,181.86) .. (306.83,181.86) -- (307.03,181.86) .. controls (307.07,181.86) and (307.1,181.83) .. (307.1,181.79) -- cycle ;
            		\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (305.87,180.18) .. controls (305.87,180.04) and (305.76,179.93) .. (305.62,179.93) -- (304.85,179.93) .. controls (304.71,179.93) and (304.6,180.04) .. (304.6,180.18) -- (304.6,183.48) .. controls (304.6,183.62) and (304.71,183.73) .. (304.85,183.73) -- (305.62,183.73) .. controls (305.76,183.73) and (305.87,183.62) .. (305.87,183.48) -- cycle ;
            		\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (309.1,180.18) .. controls (309.1,180.04) and (308.99,179.93) .. (308.85,179.93) -- (308.08,179.93) .. controls (307.94,179.93) and (307.83,180.04) .. (307.83,180.18) -- (307.83,183.48) .. controls (307.83,183.62) and (307.94,183.73) .. (308.08,183.73) -- (308.85,183.73) .. controls (308.99,183.73) and (309.1,183.62) .. (309.1,183.48) -- cycle ;
            		\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (307.72,181.06) .. controls (307.72,180.86) and (307.56,180.7) .. (307.36,180.7) -- (306.29,180.7) .. controls (306.1,180.7) and (305.94,180.86) .. (305.94,181.06) -- (305.94,182.66) .. controls (305.94,182.86) and (306.1,183.02) .. (306.29,183.02) -- (307.36,183.02) .. controls (307.56,183.02) and (307.72,182.86) .. (307.72,182.66) -- cycle ;
            		\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (285.61,169.53) .. controls (285.61,169.47) and (285.56,169.42) .. (285.5,169.42) -- (285.19,169.42) .. controls (285.13,169.42) and (285.09,169.47) .. (285.09,169.53) -- (285.09,179.74) .. controls (285.09,179.8) and (285.13,179.85) .. (285.19,179.85) -- (285.5,179.85) .. controls (285.56,179.85) and (285.61,179.8) .. (285.61,179.74) -- cycle ;
            		\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (283.75,176.99) .. controls (283.75,176.78) and (283.58,176.61) .. (283.37,176.61) -- (282.23,176.61) .. controls (282.02,176.61) and (281.85,176.78) .. (281.85,176.99) -- (281.85,182.6) .. controls (281.85,182.81) and (282.02,182.98) .. (282.23,182.98) -- (283.37,182.98) .. controls (283.58,182.98) and (283.75,182.81) .. (283.75,182.6) -- cycle ;
            		\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (288.6,176.99) .. controls (288.6,176.78) and (288.43,176.61) .. (288.22,176.61) -- (287.08,176.61) .. controls (286.87,176.61) and (286.7,176.78) .. (286.7,176.99) -- (286.7,182.6) .. controls (286.7,182.81) and (286.87,182.98) .. (287.08,182.98) -- (288.22,182.98) .. controls (288.43,182.98) and (288.6,182.81) .. (288.6,182.6) -- cycle ;
            		\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (286.52,178.44) .. controls (286.52,178.15) and (286.28,177.91) .. (285.99,177.91) -- (284.39,177.91) .. controls (284.1,177.91) and (283.86,178.15) .. (283.86,178.44) -- (283.86,181.25) .. controls (283.86,181.55) and (284.1,181.79) .. (284.39,181.79) -- (285.99,181.79) .. controls (286.28,181.79) and (286.52,181.55) .. (286.52,181.25) -- cycle ;
            		\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (329.11,170.28) .. controls (329.11,170.22) and (329.06,170.17) .. (329,170.17) -- (328.69,170.17) .. controls (328.63,170.17) and (328.59,170.22) .. (328.59,170.28) -- (328.59,180.49) .. controls (328.59,180.55) and (328.63,180.6) .. (328.69,180.6) -- (329,180.6) .. controls (329.06,180.6) and (329.11,180.55) .. (329.11,180.49) -- cycle ;
            		\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (327.25,177.74) .. controls (327.25,177.53) and (327.08,177.36) .. (326.87,177.36) -- (325.73,177.36) .. controls (325.52,177.36) and (325.35,177.53) .. (325.35,177.74) -- (325.35,183.35) .. controls (325.35,183.56) and (325.52,183.73) .. (325.73,183.73) -- (326.87,183.73) .. controls (327.08,183.73) and (327.25,183.56) .. (327.25,183.35) -- cycle ;
            		\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (332.1,177.74) .. controls (332.1,177.53) and (331.93,177.36) .. (331.72,177.36) -- (330.58,177.36) .. controls (330.37,177.36) and (330.2,177.53) .. (330.2,177.74) -- (330.2,183.35) .. controls (330.2,183.56) and (330.37,183.73) .. (330.58,183.73) -- (331.72,183.73) .. controls (331.93,183.73) and (332.1,183.56) .. (332.1,183.35) -- cycle ;
            		\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (330.02,179.19) .. controls (330.02,178.9) and (329.78,178.66) .. (329.49,178.66) -- (327.89,178.66) .. controls (327.6,178.66) and (327.36,178.9) .. (327.36,179.19) -- (327.36,182) .. controls (327.36,182.3) and (327.6,182.54) .. (327.89,182.54) -- (329.49,182.54) .. controls (329.78,182.54) and (330.02,182.3) .. (330.02,182) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ][line width=0.75]  (294,157.36) .. controls (294,154.23) and (299.11,151.69) .. (305.41,151.69) .. controls (311.72,151.69) and (316.83,154.23) .. (316.83,157.36) .. controls (316.83,160.49) and (311.72,163.03) .. (305.41,163.03) .. controls (299.11,163.03) and (294,160.49) .. (294,157.36) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ][line width=0.75]  (293.66,153.69) .. controls (295.57,148.46) and (300.58,144.73) .. (306.46,144.73) .. controls (312.59,144.73) and (317.77,148.78) .. (319.47,154.35) -- (306.46,158.34) -- cycle ; \draw  [line width=0.75]  (293.66,153.69) .. controls (295.57,148.46) and (300.58,144.73) .. (306.46,144.73) .. controls (312.59,144.73) and (317.77,148.78) .. (319.47,154.35) ;  
            		\draw  [draw opacity=0][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ][line width=0.75]  (319.02,153.44) .. controls (321.5,155.91) and (323.01,159.11) .. (323.03,162.63) .. controls (323.08,170.48) and (315.67,176.89) .. (306.49,176.95) .. controls (297.3,177.01) and (289.81,170.69) .. (289.76,162.84) .. controls (289.74,159.12) and (291.38,155.73) .. (294.1,153.18) -- (306.4,162.73) -- cycle ; \draw  [line width=0.75]  (319.02,153.44) .. controls (321.5,155.91) and (323.01,159.11) .. (323.03,162.63) .. controls (323.08,170.48) and (315.67,176.89) .. (306.49,176.95) .. controls (297.3,177.01) and (289.81,170.69) .. (289.76,162.84) .. controls (289.74,159.12) and (291.38,155.73) .. (294.1,153.18) ;  
            		\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (305.48,154.52) -- (317.19,153.48) -- (318.82,157.19) -- (305.48,158.52) -- (294,157.36) -- (295.69,153.33) -- cycle ;
            		\draw [color={rgb, 255:red, 248; green, 231; blue, 28 }  ,draw opacity=1 ]   (305.48,154.52) -- (305.48,158.52) ;
            		\draw [color={rgb, 255:red, 248; green, 231; blue, 28 }  ,draw opacity=1 ]   (311.33,154) -- (312.15,157.86) ;
            		\draw [color={rgb, 255:red, 248; green, 231; blue, 28 }  ,draw opacity=1 ]   (300.58,153.93) -- (299.74,157.94) ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.22 ] (306.05,169.15) .. controls (309.91,170.63) and (309.63,168.46) .. (321.05,169.2) .. controls (316.45,176.47) and (302.01,181.36) .. (291.84,169.94) .. controls (296.67,169.05) and (297.15,173.6) .. (306.05,169.15) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.39 ] (300.58,158.38) .. controls (304.44,159.86) and (309.78,157.19) .. (321.2,157.93) .. controls (316.15,162.08) and (316.73,164.11) .. (306.05,169.15) .. controls (305.61,167.22) and (302.96,163.27) .. (300.58,158.38) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.39 ] (296.43,152.59) .. controls (303.99,154.08) and (307.26,153.93) .. (318.38,152.59) .. controls (316.75,151.26) and (316.15,144.59) .. (307.85,145.47) .. controls (307.4,143.55) and (298.8,157.49) .. (296.43,152.59) -- cycle ;
            		\draw [line width=1.5]    (285.35,174.64) -- (290.35,169.23) ;
            		\draw [line width=1.5]    (328.85,175.39) -- (323.85,169.73) ;
            		\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (269.02,174.48) .. controls (269.02,173.27) and (270.01,172.28) .. (271.22,172.28) .. controls (272.44,172.28) and (273.42,173.27) .. (273.42,174.48) .. controls (273.42,175.7) and (272.44,176.68) .. (271.22,176.68) .. controls (270.01,176.68) and (269.02,175.7) .. (269.02,174.48) -- cycle ;
            		\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (338.27,175.73) .. controls (338.27,174.52) and (339.26,173.53) .. (340.47,173.53) .. controls (341.69,173.53) and (342.67,174.52) .. (342.67,175.73) .. controls (342.67,176.95) and (341.69,177.93) .. (340.47,177.93) .. controls (339.26,177.93) and (338.27,176.95) .. (338.27,175.73) -- cycle ;
            		\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (252.69,170.58) .. controls (252.69,169.8) and (253.32,169.16) .. (254.1,169.16) .. controls (254.88,169.16) and (255.51,169.8) .. (255.51,170.58) .. controls (255.51,171.36) and (254.88,171.99) .. (254.1,171.99) .. controls (253.32,171.99) and (252.69,171.36) .. (252.69,170.58) -- cycle ;
            		\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (356.19,170.33) .. controls (356.19,169.55) and (356.82,168.91) .. (357.6,168.91) .. controls (358.38,168.91) and (359.01,169.55) .. (359.01,170.33) .. controls (359.01,171.11) and (358.38,171.74) .. (357.6,171.74) .. controls (356.82,171.74) and (356.19,171.11) .. (356.19,170.33) -- cycle ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.43 ]   (266.16,174.47) -- (269.6,175.04) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.43 ]   (266.1,175.54) -- (269.6,175.04) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.43 ]   (266.33,176.61) -- (269.6,175.04) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.43 ]   (267,177.45) -- (269.6,175.04) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.43 ]   (266.66,173.48) -- (269.6,175.04) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.43 ]   (269.6,175.04) -- (267.91,177.98) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.43 ]   (335.91,175.97) -- (339.35,176.54) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.43 ]   (335.85,177.04) -- (339.35,176.54) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.43 ]   (336.08,178.11) -- (339.35,176.54) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.43 ]   (336.75,178.95) -- (339.35,176.54) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.43 ]   (336.41,174.98) -- (339.35,176.54) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.43 ]   (339.35,176.54) -- (337.66,179.48) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.43 ]   (250.15,170.36) -- (253.1,170.86) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.43 ]   (250.1,171.31) -- (253.1,170.86) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.43 ]   (250.29,172.26) -- (253.1,170.86) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.43 ]   (250.87,173.01) -- (253.1,170.86) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.43 ]   (250.58,169.48) -- (253.1,170.86) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.43 ]   (253.1,170.86) -- (251.65,173.48) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.43 ]   (353.65,169.81) -- (356.6,170.28) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.43 ]   (353.6,170.7) -- (356.6,170.28) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.43 ]   (353.79,171.59) -- (356.6,170.28) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.43 ]   (354.37,172.29) -- (356.6,170.28) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.43 ]   (354.08,168.98) -- (356.6,170.28) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.43 ]   (356.6,170.28) -- (355.15,172.73) ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (316.83,157.36) -- (308.35,158.48) -- (313.35,153.73) -- cycle ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (161.5,150.38) -- (174.95,155.78) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (178.5,112.88) -- (189.5,120.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (208.5,79.63) -- (215,88.48) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (242.75,57.88) -- (246.75,68.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (283.25,46.73) -- (283.5,58.23) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (322.75,46.23) -- (321.75,58.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (362.25,58.23) -- (360,68.23) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (397.5,80.23) -- (392.75,88.23) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (425.25,110.48) -- (419.5,116.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (443.5,148.48) -- (434.75,152.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (404.25,144.98) -- (397.5,148.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (393,118.98) -- (386.75,123.98) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (373.75,93.73) -- (368,100.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (347.75,76.98) -- (345,84.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (317.75,68.73) -- (317.5,75.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (288.5,68.73) -- (289,76.48) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (259.5,77.48) -- (261.5,84.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (233.25,94.48) -- (237.8,101.23) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (214.5,118.23) -- (221.05,122.98) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (202.05,149.73) -- (209.8,152.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (272,92.73) -- (273.55,98.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (252.75,104.73) -- (256.8,110.23) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (239.5,122.48) -- (243.55,125.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (229.75,145.48) -- (235.8,146.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (293.5,86.23) -- (293.8,92.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (314.5,85.98) -- (313.55,91.98) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (335.25,92.98) -- (333.3,98.48) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (354,106.23) -- (350.3,110.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (367.5,123.23) -- (363.3,127.23) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (376.25,141.98) -- (370.8,144.73) ;
            		\draw  [draw opacity=0][line width=0.75]  (177.8,184.47) .. controls (177.73,182.9) and (177.7,181.32) .. (177.7,179.73) .. controls (177.7,114.01) and (234.75,60.73) .. (305.12,60.73) .. controls (375.49,60.73) and (432.54,114.01) .. (432.54,179.73) .. controls (432.54,181.47) and (432.5,183.2) .. (432.42,184.91) -- (305.12,179.73) -- cycle ; \draw  [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ][line width=0.75]  (177.8,184.47) .. controls (177.73,182.9) and (177.7,181.32) .. (177.7,179.73) .. controls (177.7,114.01) and (234.75,60.73) .. (305.12,60.73) .. controls (375.49,60.73) and (432.54,114.01) .. (432.54,179.73) .. controls (432.54,181.47) and (432.5,183.2) .. (432.42,184.91) ;  
            		\draw  [draw opacity=0][line width=0.75]  (183.22,182.96) .. controls (183.21,182.34) and (183.2,181.71) .. (183.2,181.08) .. controls (183.2,115.99) and (237.49,63.23) .. (304.45,63.23) .. controls (371.41,63.23) and (425.7,115.99) .. (425.7,181.08) .. controls (425.7,181.62) and (425.7,182.17) .. (425.69,182.71) -- (304.45,181.08) -- cycle ; \draw  [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ][line width=0.75]  (183.22,182.96) .. controls (183.21,182.34) and (183.2,181.71) .. (183.2,181.08) .. controls (183.2,115.99) and (237.49,63.23) .. (304.45,63.23) .. controls (371.41,63.23) and (425.7,115.99) .. (425.7,181.08) .. controls (425.7,181.62) and (425.7,182.17) .. (425.69,182.71) ;  
            		\draw  [draw opacity=0][line width=0.75]  (189.7,181.73) .. controls (190.1,117.32) and (241.1,65.23) .. (303.95,65.23) .. controls (366.48,65.23) and (417.27,116.79) .. (418.19,180.74) -- (303.95,182.49) -- cycle ; \draw  [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ][line width=0.75]  (189.7,181.73) .. controls (190.1,117.32) and (241.1,65.23) .. (303.95,65.23) .. controls (366.48,65.23) and (417.27,116.79) .. (418.19,180.74) ;  
            		\draw  [draw opacity=0][line width=0.75]  (241.07,160.25) .. controls (240.92,158.64) and (240.85,157.01) .. (240.85,155.37) .. controls (240.85,123.24) and (268.97,97.2) .. (303.65,97.2) .. controls (338.33,97.2) and (366.45,123.24) .. (366.45,155.37) .. controls (366.45,157.05) and (366.37,158.72) .. (366.22,160.37) -- (303.65,155.37) -- cycle ; \draw  [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ][line width=0.75]  (241.07,160.25) .. controls (240.92,158.64) and (240.85,157.01) .. (240.85,155.37) .. controls (240.85,123.24) and (268.97,97.2) .. (303.65,97.2) .. controls (338.33,97.2) and (366.45,123.24) .. (366.45,155.37) .. controls (366.45,157.05) and (366.37,158.72) .. (366.22,160.37) ;  
            		\draw  [draw opacity=0][line width=0.75]  (246.45,160.75) .. controls (246.38,159.63) and (246.35,158.5) .. (246.35,157.37) .. controls (246.35,125.24) and (272.12,99.2) .. (303.9,99.2) .. controls (335.68,99.2) and (361.45,125.24) .. (361.45,157.37) .. controls (361.45,158.49) and (361.42,159.6) .. (361.36,160.71) -- (303.9,157.37) -- cycle ; \draw  [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ][line width=0.75]  (246.45,160.75) .. controls (246.38,159.63) and (246.35,158.5) .. (246.35,157.37) .. controls (246.35,125.24) and (272.12,99.2) .. (303.9,99.2) .. controls (335.68,99.2) and (361.45,125.24) .. (361.45,157.37) .. controls (361.45,158.49) and (361.42,159.6) .. (361.36,160.71) ;  
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (156.13,192.92) -- (171.45,178.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (169.95,191.43) -- (158,173.33) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (171.45,178.73) -- (161.5,150.38) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (158,173.33) -- (174.95,155.78) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (173.7,155.18) -- (170,131.23) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (161.5,150.38) -- (180.7,138.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (180.7,138.73) -- (178.5,112.88) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (170,131.23) -- (189.5,120.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (178.5,112.88) -- (201.15,104.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (189.2,119.18) -- (193.75,94.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (193.75,94.73) -- (215,88.48) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (201.15,104.73) -- (208.5,79.63) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (208.5,79.63) -- (230.4,77.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (215,88.48) -- (224.75,67.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (231.7,77.68) -- (242.75,57.88) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (224.75,67.73) -- (246.75,68.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (246.75,68.73) -- (263.75,51.23) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (242.75,57.88) -- (264.9,62.23) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (264.9,62.23) -- (283.25,46.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (263.45,49.93) -- (283.5,58.23) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (283.5,58.23) -- (304.25,45.23) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (283.25,46.73) -- (303.85,57.03) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (303.85,57.03) -- (322.75,46.23) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (304.25,45.23) -- (321.75,58.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (321.75,58.73) -- (343.5,51.23) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (322.75,46.23) -- (341.6,61.78) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (341.6,61.78) -- (362.25,58.23) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (343.5,51.23) -- (360,68.23) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (360,68.23) -- (382.75,68.48) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (362.25,58.23) -- (377.35,77.28) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (377.35,77.28) -- (397.5,80.23) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (382.75,68.48) -- (392.75,88.23) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (392.75,88.23) -- (414.5,95.23) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (397.5,80.23) -- (407.85,103.78) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (414.5,95.23) -- (419.5,116.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (407.85,103.78) -- (425.25,110.48) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (419.5,116.73) -- (437.75,131.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (425.25,110.48) -- (428.6,136.93) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (437.75,131.73) -- (434.75,152.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (428.6,136.93) -- (443.5,148.48) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (443.5,148.48) -- (437.6,176.93) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (434.75,152.73) -- (448,171.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (437.6,176.93) -- (451.7,190.43) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (448.75,172.73) -- (436.76,191.33) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ][line width=0.75]    (281.3,127.48) -- (264.5,127.63) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ][line width=0.75]    (281.05,150.73) -- (256,150.63) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ][line width=0.75]    (343.3,127.23) -- (325.3,127.23) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ][line width=0.75]    (351.3,149.73) -- (325.05,149.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (206.85,178.8) -- (199.45,164.48) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (207.5,165.4) -- (202.05,149.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (209.5,151.4) -- (206.3,133.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (213.7,137.98) -- (214.5,118.23) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (221.05,122.98) -- (223,105.23) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (228.65,111.73) -- (233.25,94.48) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (239,102.15) -- (246,84.48) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (233.7,156.73) -- (229.15,145.32) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (235.8,146.73) -- (233.75,133.23) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (238.95,135.73) -- (239.5,122.48) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (243.55,125.73) -- (245.75,113.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (249.9,117.73) -- (252.75,104.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (249.65,91.98) -- (259.5,77.48) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (261.5,84.73) -- (274.25,71.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (275.15,79.73) -- (288.5,68.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (288.35,77.65) -- (303.75,66.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (303.75,74.98) -- (317.75,68.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (318.85,76.4) -- (333.25,72.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (332,79.73) -- (347.75,76.98) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (256.8,110.23) -- (262,98.23) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (264.9,102.73) -- (272,92.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (273.55,98.73) -- (282.5,87.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (283.15,94.98) -- (293.5,86.23) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (293.8,92.73) -- (304,85.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (303.75,91.48) -- (314.5,85.98) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (313.55,91.98) -- (325,88.98) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (323.5,94.23) -- (335.25,92.98) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (345,84.73) -- (361.5,85.23) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (357.25,92.23) -- (373.75,93.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (368,100.73) -- (384.25,105.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (378.25,112.23) -- (393,118.98) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (386.75,123.98) -- (400.75,132.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (393.5,136.73) -- (404.25,144.98) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (399.75,165.48) -- (408.37,177.77) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (407.75,161.73) -- (400.6,175.4) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (400.75,132.73) -- (397.5,148.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (393,118.98) -- (393.5,136.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (384.25,105.73) -- (386.75,123.98) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (373.75,93.73) -- (378.25,112.23) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (361.5,85.23) -- (368,100.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (347.75,76.98) -- (357.25,92.23) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (333.25,72.73) -- (345,84.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (317.75,68.73) -- (332,79.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (303.75,68.23) -- (318.85,76.4) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (288.5,68.73) -- (303.75,74.98) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (274.25,71.73) -- (289,76.48) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (259.5,77.48) -- (275.15,79.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (246,84.48) -- (261.5,84.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (233.25,94.48) -- (249.65,91.98) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (223,105.23) -- (237.8,101.23) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (214.5,118.23) -- (228.65,111.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (206.3,133.73) -- (221.05,122.98) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (201.25,148.73) -- (213.7,137.98) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (199.45,164.48) -- (209.8,152.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (198.71,179.49) -- (207.45,166.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (333.3,98.48) -- (345.25,98.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (342,104.23) -- (354,106.23) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (350.3,110.73) -- (360.75,113.23) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (356.5,117.73) -- (367.5,123.23) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (363.3,127.23) -- (373,132.98) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (367.5,136.73) -- (376.25,141.98) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (370.8,144.73) -- (378.55,151.9) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (227.95,155.98) -- (235.8,146.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (229.15,145.32) -- (238.95,135.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (233.75,133.23) -- (243.55,125.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (239.5,122.48) -- (249.9,117.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (245.75,113.73) -- (256.8,110.23) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (252.75,104.73) -- (264.9,102.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (262,98.23) -- (273.55,98.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (272,92.73) -- (283.15,94.98) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (293.8,92.73) -- (282.5,87.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (303.75,91.48) -- (292.45,86.48) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (313.55,91.98) -- (304,85.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (323.5,94.23) -- (314.5,85.98) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (333.3,98.48) -- (325,88.98) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (342,104.23) -- (335.25,92.98) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (350.3,110.73) -- (345.25,98.73) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (356.5,117.73) -- (354,106.23) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (363.3,127.23) -- (360.75,113.23) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (367.5,136.73) -- (367.5,123.23) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (370.8,144.73) -- (373,132.98) ;
            		\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ]   (372.5,154.48) -- (376.25,141.98) ;
            		\draw  [draw opacity=0][line width=0.75]  (157.63,190.98) .. controls (159.09,111.25) and (224.03,47.07) .. (303.93,47.07) .. controls (384.46,47.07) and (449.8,112.27) .. (450.26,192.87) -- (303.93,193.74) -- cycle ; \draw  [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][line width=0.75]  (157.63,190.98) .. controls (159.09,111.25) and (224.03,47.07) .. (303.93,47.07) .. controls (384.46,47.07) and (449.8,112.27) .. (450.26,192.87) ;  
            		\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.36 ] (306.05,169.15) .. controls (309.91,170.63) and (284.38,172.16) .. (295.8,172.9) .. controls (291.2,180.17) and (293.3,172.15) .. (290.3,164.15) .. controls (293.8,168.4) and (296.3,172.4) .. (306.05,169.15) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.51 ] (312.15,157.86) .. controls (316.01,159.34) and (306.13,157.91) .. (317.55,158.65) .. controls (312.51,162.8) and (316.48,165.36) .. (305.8,170.4) .. controls (306.55,169.15) and (314.52,162.75) .. (312.15,157.86) -- cycle ;
            	\end{tikzpicture}
            \end{center}'''

                # Nội dung câu hỏi
                noidungcauhoi = (r'''Một nhà vòm chứa máy bay có mặt cắt hình nửa elip cao $%s$ m, rộng $%s$ m. Khoảng cách theo phương thẳng đứng từ một điểm cách chân tường $%s$ m đến nóc nhà vòm bằng bao nhiêu mét? (làm tròn kết quả đến hàng phần chục).%s'''
                                % (latex(cao), latex(rong), latex(dist_wall),hinhve))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào danh sách và xáo trộn
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                # Phương trình elip: x^2/a^2 + y^2/b^2 = 1
                loigiai = ('''Chọn hệ trục tọa độ $Oxy$ sao cho gốc tọa độ $O$ là trung điểm của chiều rộng mặt cắt, trục $Ox$ nằm trên mặt đất. \\\\
                            Vì chiều rộng là $%s$ m nên ta có $2a = %s \\Rightarrow a = %s$. \\\\
                            Vì chiều cao của nhà vòm là $%s$ m nên ta có $b = %s$. \\\\
                            Phương trình elip của mặt cắt nhà vòm là: $\\frac{x^2}{%s^2} + \\frac{y^2}{%s^2} = 1$ với $y \\ge 0$. \\\\
                            Điểm cách chân tường $%s$ m tương ứng với điểm có hoành độ $x = %s - %s = %s$ (hoặc $x = -%s$). \\\\
                            Thay $x = %s$ vào phương trình elip ta có: \\\\
                            $\\frac{%s^2}{%s^2} + \\frac{y^2}{%s^2} = 1 \\Rightarrow \\frac{y^2}{%s} = 1 - \\frac{%s}{%s} = \\frac{%s}{%s}$. \\\\
                            $\\Rightarrow y^2 = %s \\cdot \\frac{%s}{%s} = %s \\Rightarrow y = \\sqrt{%s} \\approx %s$ m. \\\\
                            Vậy khoảng cách cần tìm là khoảng $%s$ m.'''
                            % (latex(rong), latex(rong), latex(a_val),
                               latex(cao), latex(b_val),
                               latex(a_val), latex(b_val),
                               latex(dist_wall), latex(a_val), latex(dist_wall), latex(x_val), latex(x_val),
                               latex(x_val),
                               latex(x_val), latex(a_val), latex(b_val),
                               latex(b_val**2), latex(x_val**2), latex(a_val**2), latex(a_val**2 - x_val**2), latex(a_val**2),
                               latex(b_val**2), latex(a_val**2 - x_val**2), latex(a_val**2), latex(y_squared), latex(y_squared),
                               kq, kq))
                dapan='\\shortans[0]{$%s$}\n'%(kq)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 


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


def bt_dang36_p3_b1_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B3 - Thiết lập random bài toán đảm bảo tính thực tế của đu quay
                # Bán kính R thường nhỏ hơn độ cao tâm h
                r1 = randint(60, 85)        # Bán kính đu quay (m)
                h1 = r1 + randint(10, 20)   # Độ cao của tâm vòng quay (m)
                t_vong = 30                 # Thời gian thực hiện mỗi vòng quay (phút)
                t_quay = 20                 # Thời gian quay của người đó (phút)

                # Tính toán các giá trị hình học trong lời giải
                # Góc quay: beta = (t_quay / t_vong) * 360
                goc_beta = int((t_quay / t_vong) * 360) 
                # Góc nhọn phụ với trục Ox hoặc Oy tùy thuộc góc quay (ở đây beta = 240 độ -> góc alpha với Ox là 30 độ)
                goc_alpha = goc_beta - 210 

                # Đoạn HJ = sin(alpha) * R = sin(30) * R = 0.5 * R
                # Với alpha = 30 độ thì sin(30) = 1/2
                hj_val = Rational(r1, 2)
                hj_float = float(hj_val)
                hj_str = str(hj_float).replace('.', ',') if hj_float % 1 != 0 else str(int(hj_float))

                # Độ cao cuối cùng = h1 + hj_val
                kq_chinhxac = h1 + hj_val
                kq_float = float(kq_chinhxac)

                # Làm tròn đến hàng đơn vị theo quy tắc ROUND_HALF_UP
                kq_tron = Decimal(str(kq_float)).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
                da_dung = int(kq_tron)

                # B4 - Điều chỉnh các phương án sai không trùng với đáp án đúng
                s = set()
                while len(s) < 3:
                    sai = da_dung + random.choice([-15, -10, -5, 5, 10, 15, 20, -25])
                    if sai != da_dung and sai > 0:
                        s.add(sai)

                list_sai = list(s)
                das1 = list_sai[0]
                das2 = list_sai[1]
                das3 = list_sai[2]

                # Đưa các đáp án vào định dạng LaTeX và chọn ngẫu nhiên vị trí
                da = '$%d\\text{ m}$' % da_dung
                du = [da]
                da_chon = random.choice(du)

                s_da = [
                    '$%d\\text{ m}$' % das1,
                    '$%d\\text{ m}$' % das2,
                    '$%d\\text{ m}$' % das3
                ]
                hinhve=r'''\scalebox{0.7}{ \begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (234.11,250) -- (240.06,250) -- (240.06,262.88) -- (234.11,262.88) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (148.69,250) -- (154.63,250) -- (154.63,262.88) -- (148.69,262.88) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ,even odd rule] (99.21,118.4) .. controls (99.21,66.73) and (141.09,24.85) .. (192.76,24.85) .. controls (244.43,24.85) and (286.32,66.73) .. (286.32,118.4) .. controls (286.32,170.07) and (244.43,211.95) .. (192.76,211.95) .. controls (141.09,211.95) and (99.21,170.07) .. (99.21,118.4)(95.95,118.4) .. controls (95.95,64.93) and (139.29,21.59) .. (192.76,21.59) .. controls (246.23,21.59) and (289.58,64.93) .. (289.58,118.4) .. controls (289.58,171.87) and (246.23,215.22) .. (192.76,215.22) .. controls (139.29,215.22) and (95.95,171.87) .. (95.95,118.4) ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (190,115.64) -- (195.52,115.64) -- (195.52,121.16) -- (190,121.16) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (192.76,121.16) -- (190,121.16) -- (167.35,252) -- (171.94,252) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (195.52,121.16) -- (192.76,121.16) -- (220.44,251.58) -- (225.87,251.17) -- cycle ;
            	\draw    (192.76,118.4) -- (192.76,24.85) ;
            	\draw    (192.76,118.4) -- (192.76,211.95) ;
            	\draw    (192.76,118.4) -- (286.32,118.4) ;
            	\draw    (192.76,118.4) -- (99.21,118.4) ;
            	\draw    (192.76,118.4) -- (254.29,49.32) ;
            	\draw    (192.76,118.4) -- (266.05,174.36) ;
            	\draw    (192.76,118.4) -- (116.87,171.26) ;
            	\draw    (192.76,118.4) -- (126.16,53.03) ;
            	\draw    (192.76,115.64) -- (225.82,31.37) ;
            	\draw    (192.76,118.4) -- (276.58,79.03) ;
            	\draw    (192.76,118.4) -- (280.91,147.74) ;
            	\draw    (236.34,200.36) -- (192.76,118.4) ;
            	\draw    (144.11,196.64) -- (192.76,118.4) ;
            	\draw    (103.87,143.41) -- (195.52,118.4) ;
            	\draw    (105.11,84.6) -- (192.76,118.4) ;
            	\draw    (192.76,118.4) -- (154.63,33.22) ;
            	\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (293.66,73.39) -- (292,78.93) -- (281.58,78.93) -- (279.92,73.39) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (279.93,73.82) .. controls (279.92,73.72) and (279.92,73.62) .. (279.92,73.52) .. controls (279.92,69.73) and (283,66.65) .. (286.79,66.65) .. controls (290.59,66.65) and (293.66,69.73) .. (293.66,73.52) .. controls (293.66,73.53) and (293.66,73.55) .. (293.66,73.56) -- cycle ;
            	\draw    (286.8,66.75) .. controls (286.67,69.24) and (286.67,71.2) .. (286.79,73.52) ;
            	\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (269.21,39.03) -- (267.55,44.57) -- (257.13,44.57) -- (255.47,39.03) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (255.48,39.46) .. controls (255.47,39.36) and (255.47,39.27) .. (255.47,39.17) .. controls (255.47,35.37) and (258.55,32.29) .. (262.34,32.29) .. controls (266.13,32.29) and (269.21,35.37) .. (269.21,39.17) .. controls (269.21,39.18) and (269.21,39.19) .. (269.21,39.2) -- cycle ;
            	\draw    (262.35,32.4) .. controls (262.22,34.89) and (262.22,36.85) .. (262.34,39.17) ;
            	\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (236.4,20.46) -- (234.74,26) -- (224.32,26) -- (222.66,20.46) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (222.67,20.89) .. controls (222.66,20.79) and (222.66,20.69) .. (222.66,20.59) .. controls (222.66,16.8) and (225.74,13.72) .. (229.53,13.72) .. controls (233.33,13.72) and (236.4,16.8) .. (236.4,20.59) .. controls (236.4,20.61) and (236.4,20.62) .. (236.4,20.63) -- cycle ;
            	\draw    (229.54,13.83) .. controls (229.41,16.31) and (229.41,18.28) .. (229.53,20.59) ;
            	\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (199.26,14.27) -- (197.6,19.81) -- (187.18,19.81) -- (185.52,14.27) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (185.53,14.7) .. controls (185.52,14.6) and (185.52,14.5) .. (185.52,14.4) .. controls (185.52,10.61) and (188.6,7.53) .. (192.39,7.53) .. controls (196.19,7.53) and (199.26,10.61) .. (199.26,14.4) .. controls (199.26,14.42) and (199.26,14.43) .. (199.26,14.44) -- cycle ;
            	\draw    (192.4,7.64) .. controls (192.27,10.12) and (192.27,12.09) .. (192.39,14.4) ;
            	\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (154.69,23.56) -- (153.03,29.1) -- (142.61,29.1) -- (140.95,23.56) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (140.96,23.99) .. controls (140.95,23.89) and (140.95,23.79) .. (140.95,23.69) .. controls (140.95,19.89) and (144.03,16.82) .. (147.82,16.82) .. controls (151.62,16.82) and (154.69,19.89) .. (154.69,23.69) .. controls (154.69,23.7) and (154.69,23.72) .. (154.69,23.73) -- cycle ;
            	\draw    (147.83,16.92) .. controls (147.7,19.41) and (147.7,21.37) .. (147.82,23.69) ;
            	\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (124.36,43.37) -- (122.7,48.9) -- (112.28,48.9) -- (110.62,43.37) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (110.62,43.8) .. controls (110.62,43.7) and (110.62,43.6) .. (110.62,43.5) .. controls (110.62,39.7) and (113.69,36.63) .. (117.49,36.63) .. controls (121.28,36.63) and (124.36,39.7) .. (124.36,43.5) .. controls (124.36,43.51) and (124.36,43.52) .. (124.36,43.54) -- cycle ;
            	\draw    (117.5,36.73) .. controls (117.37,39.22) and (117.37,41.18) .. (117.49,43.5) ;
            	\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (101.46,78.65) -- (99.8,84.19) -- (89.37,84.19) -- (87.71,78.65) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (87.72,79.08) .. controls (87.72,78.98) and (87.71,78.88) .. (87.71,78.78) .. controls (87.71,74.99) and (90.79,71.91) .. (94.59,71.91) .. controls (98.38,71.91) and (101.46,74.99) .. (101.46,78.78) .. controls (101.46,78.8) and (101.46,78.81) .. (101.46,78.82) -- cycle ;
            	\draw    (94.6,72.02) .. controls (94.47,74.5) and (94.47,76.47) .. (94.59,78.78) ;
            	\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (93.41,116.41) -- (91.75,121.95) -- (81.33,121.95) -- (79.67,116.41) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (79.67,116.84) .. controls (79.67,116.74) and (79.67,116.64) .. (79.67,116.54) .. controls (79.67,112.75) and (82.74,109.67) .. (86.54,109.67) .. controls (90.33,109.67) and (93.41,112.75) .. (93.41,116.54) .. controls (93.41,116.56) and (93.41,116.57) .. (93.41,116.58) -- cycle ;
            	\draw    (86.55,109.78) .. controls (86.42,112.26) and (86.42,114.23) .. (86.54,116.54) ;
            	\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (97.12,144.89) -- (95.46,150.42) -- (85.04,150.42) -- (83.38,144.89) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (83.39,145.32) .. controls (83.38,145.22) and (83.38,145.12) .. (83.38,145.02) .. controls (83.38,141.22) and (86.46,138.15) .. (90.25,138.15) .. controls (94.05,138.15) and (97.12,141.22) .. (97.12,145.02) .. controls (97.12,145.03) and (97.12,145.04) .. (97.12,145.06) -- cycle ;
            	\draw    (90.27,138.25) .. controls (90.13,140.74) and (90.13,142.7) .. (90.25,145.02) ;
            	\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (113.22,178.93) -- (111.56,184.47) -- (101.14,184.47) -- (99.48,178.93) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (99.48,179.36) .. controls (99.48,179.26) and (99.48,179.16) .. (99.48,179.06) .. controls (99.48,175.27) and (102.55,172.19) .. (106.35,172.19) .. controls (110.14,172.19) and (113.22,175.27) .. (113.22,179.06) .. controls (113.22,179.08) and (113.22,179.09) .. (113.22,179.1) -- cycle ;
            	\draw    (106.36,172.3) .. controls (106.23,174.78) and (106.23,176.75) .. (106.35,179.06) ;
            	\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (146.64,206.79) -- (144.98,212.33) -- (134.56,212.33) -- (132.9,206.79) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (132.91,207.22) .. controls (132.9,207.12) and (132.9,207.02) .. (132.9,206.92) .. controls (132.9,203.13) and (135.98,200.05) .. (139.77,200.05) .. controls (143.57,200.05) and (146.64,203.13) .. (146.64,206.92) .. controls (146.64,206.93) and (146.64,206.95) .. (146.64,206.96) -- cycle ;
            	\draw    (139.79,200.15) .. controls (139.66,202.64) and (139.66,204.6) .. (139.77,206.92) ;
            	\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (199.26,222.88) -- (197.6,228.42) -- (187.18,228.42) -- (185.52,222.88) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (185.53,223.31) .. controls (185.52,223.21) and (185.52,223.11) .. (185.52,223.01) .. controls (185.52,219.22) and (188.6,216.14) .. (192.39,216.14) .. controls (196.19,216.14) and (199.26,219.22) .. (199.26,223.01) .. controls (199.26,223.03) and (199.26,223.04) .. (199.26,223.05) -- cycle ;
            	\draw    (192.4,216.25) .. controls (192.27,218.73) and (192.27,220.7) .. (192.39,223.01) ;
            	\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (250.64,209.88) -- (248.98,215.42) -- (238.56,215.42) -- (236.9,209.88) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (236.9,210.31) .. controls (236.9,210.21) and (236.9,210.12) .. (236.9,210.02) .. controls (236.9,206.22) and (239.97,203.14) .. (243.77,203.14) .. controls (247.56,203.14) and (250.64,206.22) .. (250.64,210.02) .. controls (250.64,210.03) and (250.64,210.04) .. (250.64,210.05) -- cycle ;
            	\draw    (243.78,203.25) .. controls (243.65,205.74) and (243.65,207.7) .. (243.77,210.02) ;
            	\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (283.45,182.65) -- (281.79,188.18) -- (271.37,188.18) -- (269.71,182.65) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (269.71,183.08) .. controls (269.71,182.98) and (269.71,182.88) .. (269.71,182.78) .. controls (269.71,178.98) and (272.78,175.91) .. (276.58,175.91) .. controls (280.37,175.91) and (283.45,178.98) .. (283.45,182.78) .. controls (283.45,182.79) and (283.45,182.8) .. (283.45,182.82) -- cycle ;
            	\draw    (276.59,176.01) .. controls (276.46,178.5) and (276.46,180.46) .. (276.58,182.78) ;
            	\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (298.92,150.46) -- (297.26,155.99) -- (286.84,155.99) -- (285.18,150.46) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (285.19,150.89) .. controls (285.18,150.79) and (285.18,150.69) .. (285.18,150.59) .. controls (285.18,146.79) and (288.26,143.72) .. (292.05,143.72) .. controls (295.85,143.72) and (298.92,146.79) .. (298.92,150.59) .. controls (298.92,150.6) and (298.92,150.62) .. (298.92,150.63) -- cycle ;
            	\draw    (292.07,143.82) .. controls (291.94,146.31) and (291.94,148.27) .. (292.05,150.59) ;
            	\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (305.73,118.27) -- (304.07,123.81) -- (293.65,123.81) -- (291.99,118.27) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (292,118.7) .. controls (291.99,118.6) and (291.99,118.5) .. (291.99,118.4) .. controls (291.99,114.61) and (295.07,111.53) .. (298.86,111.53) .. controls (302.66,111.53) and (305.73,114.61) .. (305.73,118.4) .. controls (305.73,118.41) and (305.73,118.43) .. (305.73,118.44) -- cycle ;
            	\draw    (298.88,111.63) .. controls (298.74,114.12) and (298.74,116.08) .. (298.86,118.4) ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (139.45,248.02) -- (251.2,248.02) -- (251.2,252.36) -- (139.45,252.36) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (107.33,257.13) -- (284.32,257.13) -- (284.32,272.28) -- (107.33,272.28) -- cycle ;
            	\draw  [fill={rgb, 255:red, 33; green, 172; blue, 184 }  ,fill opacity=1 ] (110.48,262.6) -- (133.7,262.6) -- (133.7,269.38) -- (110.48,269.38) -- cycle ;
            	\draw  [fill={rgb, 255:red, 33; green, 172; blue, 184 }  ,fill opacity=1 ] (137.64,262.6) -- (160.86,262.6) -- (160.86,269.38) -- (137.64,269.38) -- cycle ;
            	\draw  [fill={rgb, 255:red, 33; green, 172; blue, 184 }  ,fill opacity=1 ] (164.8,262.6) -- (188.01,262.6) -- (188.01,269.38) -- (164.8,269.38) -- cycle ;
            	\draw  [fill={rgb, 255:red, 33; green, 172; blue, 184 }  ,fill opacity=1 ] (191.96,262.6) -- (215.17,262.6) -- (215.17,269.38) -- (191.96,269.38) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (83.67,272.12) -- (308.01,272.12) -- (308.01,287.26) -- (83.67,287.26) -- cycle ;
            	\draw  [fill={rgb, 255:red, 33; green, 172; blue, 184 }  ,fill opacity=1 ] (86.82,277.59) -- (110.04,277.59) -- (110.04,284.37) -- (86.82,284.37) -- cycle ;
            	\draw  [fill={rgb, 255:red, 33; green, 172; blue, 184 }  ,fill opacity=1 ] (113.98,277.59) -- (137.19,277.59) -- (137.19,284.37) -- (113.98,284.37) -- cycle ;
            	\draw  [fill={rgb, 255:red, 33; green, 172; blue, 184 }  ,fill opacity=1 ] (141.14,277.59) -- (164.35,277.59) -- (164.35,284.37) -- (141.14,284.37) -- cycle ;
            	\draw  [fill={rgb, 255:red, 33; green, 172; blue, 184 }  ,fill opacity=1 ] (168.3,277.59) -- (191.51,277.59) -- (191.51,284.37) -- (168.3,284.37) -- cycle ;
            	\draw  [fill={rgb, 255:red, 33; green, 172; blue, 184 }  ,fill opacity=1 ] (195.45,277.59) -- (218.67,277.59) -- (218.67,284.37) -- (195.45,284.37) -- cycle ;
            	\draw  [fill={rgb, 255:red, 33; green, 172; blue, 184 }  ,fill opacity=1 ] (222.61,277.59) -- (245.83,277.59) -- (245.83,284.37) -- (222.61,284.37) -- cycle ;
            	\draw    (107.67,261.42) -- (283.95,261.02) ;
            	\draw    (84.01,276.4) -- (308.4,276.4) ;
            \end{tikzpicture} }'''
                # Câu hỏi
                noidungcauhoi = (r'''\immini{Một chiếc đu quay có bán kính $%s\text{ m}$, tâm của vòng quay ở độ cao $%s\text{ m}$, thời gian thực hiện mỗi vòng quay của đu quay là $%s$ phút. Nếu một người vào cabin tại vị trí thấp nhất của vòng quay, thì sau $%s$ phút quay, người đó ở độ cao bao nhiêu mét? (kết quả làm tròn đến hàng đơn vị).}{%s}'''
                                 % (latex(r1), latex(h1), latex(t_vong), latex(t_quay),hinhve))

                # Các đáp án
                da_d = ('\\True ' + str(da_chon))
                da_s1 = str(s_da[0])
                da_s2 = str(s_da[1]) 
                da_s3 = str(s_da[2]) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = ('''\\begin{center}
            	\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            		\\draw  [line width=1]  (136.52,156.22) .. controls (136.52,109.15) and (174.68,71) .. (221.74,71) .. controls (268.81,71) and (306.97,109.15) .. (306.97,156.22) .. controls (306.97,203.29) and (268.81,241.45) .. (221.74,241.45) .. controls (174.68,241.45) and (136.52,203.29) .. (136.52,156.22) -- cycle ;
            		\\draw [line width=1]    (103.73,156.22) -- (345.07,156.22) ;
            		\\draw [shift={(349.07,156.22)}, rotate = 180] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (8.75,-4.2) -- (0,0) -- (8.75,4.2) -- (5.81,0) -- cycle    ;
            		\\draw [line width=1]    (226.4,267.19) -- (226.4,30.4) ;
            		\\draw [shift={(226.4,26.4)}, rotate = 90] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (8.75,-4.2) -- (0,0) -- (8.75,4.2) -- (5.81,0) -- cycle    ;
            		\\draw [line width=1]    (226.4,156.22) -- (293.03,111.21) ;
            		\\draw [line width=1]    (293.03,156.64) -- (293.03,111.21) ;
            		\\draw    (238.13,148.07) .. controls (242.8,149.4) and (243.27,152.47) .. (244.13,155.73) ;
            		\\draw (205.28,161) node [anchor=north west][inner sep=0.75pt]    {$O$};
            		\\draw (293.11,91) node [anchor=north west][inner sep=0.75pt]    {$H$};
            		\\draw (285.07,161) node [anchor=north west][inner sep=0.75pt]    {$J$};
            		\\draw (242.67,145) node [anchor=north west][inner sep=0.75pt]    {$\\alpha $};
            		\\draw (329.33,162) node [anchor=north west][inner sep=0.75pt]    {$x$};
            		\\draw (208.67,25.67) node [anchor=north west][inner sep=0.75pt]    {$y$};
            	\\end{tikzpicture}
            \\end{center} Do tính đối xứng, dù đu quay chuyển động theo chiều kim đồng hồ hay ngược chiều kim đồng hồ, ta đều thấy rằng độ cao của người đó là như nhau sau cùng một khoảng thời gian. Ở đây ta xét đu quay chuyển động theo chiều kim đồng hồ. Gắn đu quay có bán kính $%s\\text{ m}$, tâm của vòng quay ở độ cao $%s\\text{ m}$ vào hệ trục tọa độ $Oxy$ như hình vẽ. \\\\
            Sau $%s$ phút quay cabin đi được một góc là $\\frac{%s}{%s} \\cdot 360^\\circ = %s^\\circ$ tức là đến vị trí điểm $H$. \\\\
            Khi đó góc $\\widehat{HOJ} = %s^\\circ$ và $HJ = \\sin %s^\\circ \\cdot OH = %s\\text{ m}$. \\\\
            Vậy sau $%s$ phút quay, người đó ở độ cao là: $%s + %s = %s\\text{ m}$ (làm tròn thành $%d\\text{ m}$).'''
                           % (latex(r1), latex(h1), latex(t_quay), latex(t_quay), latex(t_vong), latex(goc_beta),
                              latex(goc_alpha), latex(goc_alpha), hj_str,
                              latex(t_quay), latex(h1), hj_str, str(kq_float).replace('.', ','), da_dung))
                dapan='\\shortans[0]{$%s$}\n'%(da_dung)
            # Xuất câu trắc nghiệm định dạng minipage
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) +dapan+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content


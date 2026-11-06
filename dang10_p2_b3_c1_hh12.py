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


def bt_dang10_p2_b3_c1_hh12(self):
    def custom_round(val):
        d = Decimal(str(val))
        return int(d.quantize(Decimal('1'), rounding=ROUND_HALF_UP))

    # Sinh ngẫu nhiên tọa độ ban đầu (dựa trên bộ số Pythagore để ra số đẹp)
    xy_triples = [(30, 40, 50), (40, 30, 50), (50, 120, 130), (120, 50, 130), (60, 80, 100), (80, 60, 100)]
    x0, y0, d_xy = random.choice(xy_triples)
    z0 = random.choice([2, 4, 6])

    # Sinh vectơ vận tốc ban đầu
    v_triples = [(300, 400), (400, 300), (600, 800), (800, 600)]
    vx, vy = random.choice(v_triples)
    vz = random.choice([2, 3, 4])

    # Tính toán cho Câu a (Khoảng cách lúc 8h)
    dist_M0_sq = x0**2 + y0**2 + z0**2
    dist_M0 = math.sqrt(dist_M0_sq)
    dist_M0_round = custom_round(dist_M0)
    dist_M0_wrong = dist_M0_round + random.randint(15, 30)

    # Tính toán cho Câu b (Độ cao lúc 9h - sau 1 giờ)
    h_9am = z0 + vz * 1
    h_9am_wrong = h_9am + random.choice([-1, 1]) * random.randint(1, 2)

    # Tính toán cho Câu c (Khoảng cách tháp truyền hình lúc 10h - sau 2 giờ)
    x2 = x0 + vx * 2
    y2 = y0 + vy * 2
    z2 = z0 + vz * 2

    dx_F, dy_F = random.choice(v_triples)
    xF = x2 + dx_F
    yF = y2 + dy_F
    zF = 0

    dist_F_sq = (x2 - xF)**2 + (y2 - yF)**2 + (z2 - zF)**2
    dist_F = math.sqrt(dist_F_sq)
    dist_F_round = custom_round(dist_F)
    dist_F_wrong = dist_F_round + random.randint(100, 300)

    # Tính toán cho Câu d (Hạ cánh)
    v2x = random.choice([300, 400, 500])
    v2y = random.choice([200, 300, 400])
    t_descend = 2
    v2z = -int(z2 / t_descend) # z2 luôn chẵn vì z0 chẵn
    v2z_str = "- " + str(abs(v2z))

    xB = x2 + v2x * t_descend
    yB = y2 + v2y * t_descend
    xB_wrong = xB + random.choice([-100, 100])
    yB_wrong = yB + random.choice([-100, 100])


    # Nội dung câu hỏi
    noidungcauhoi = ('''Trong một ca trực tại Trạm kiểm soát không lưu sân bay, các kỹ sư ra-đa thiết lập hệ trục tọa độ $Oxyz$ (đơn vị trên các trục tính bằng ki-lô-mét) với gốc $O(0;0;0)$ là vị trí đặt tháp điều hành không lưu. Lúc 8 giờ sáng, hệ thống theo dõi một máy bay trực thăng đang ở vị trí $M_0(%s;%s;%s)$ (nghĩa là cách tháp điều hành %s km về hướng Đông, %s km về hướng Bắc và ở độ cao %s km). Máy bay đang bay ổn định với vectơ vận tốc không đổi là $\\vec{v} = (%s;%s;%s)$ (đơn vị: km/h).
    \\begin{center}
    	\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
    		\\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.42 ][dash pattern={on 5.63pt off 4.5pt}][line width=1]  (174.49,188.8) -- (327.13,188.8) -- (261.71,223.07) -- (109.07,223.07) -- cycle ;
    		\\draw [line width=1]    (174.49,188.8) -- (174.49,49.8) ;
    		\\draw [shift={(174.49,46.8)}, rotate = 90] [color={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=1]    (5.68,-1.71) .. controls (3.61,-0.72) and (1.72,-0.15) .. (0,0) .. controls (1.72,0.15) and (3.61,0.72) .. (5.68,1.71)   ;
    		\\draw [line width=1]    (174.49,188.8) -- (74.39,241.4) ;
    		\\draw [shift={(71.73,242.8)}, rotate = 332.28] [color={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=1]    (5.68,-1.71) .. controls (3.61,-0.72) and (1.72,-0.15) .. (0,0) .. controls (1.72,0.15) and (3.61,0.72) .. (5.68,1.71)   ;
    		\\draw [line width=1]    (174.49,188.8) -- (389.4,188.8) ;
    		\\draw [shift={(392.4,188.8)}, rotate = 180] [color={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=1]    (5.68,-1.71) .. controls (3.61,-0.72) and (1.72,-0.15) .. (0,0) .. controls (1.72,0.15) and (3.61,0.72) .. (5.68,1.71)   ;
    		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (174.49,188.8) -- (143.73,204.75) ;
    		\\draw [shift={(141.07,206.13)}, rotate = 332.59] [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (5.68,-1.71) .. controls (3.61,-0.72) and (1.72,-0.15) .. (0,0) .. controls (1.72,0.15) and (3.61,0.72) .. (5.68,1.71)   ;
    		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (174.49,188.8) -- (212.73,188.8) ;
    		\\draw [shift={(215.73,188.8)}, rotate = 180] [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (5.68,-1.71) .. controls (3.61,-0.72) and (1.72,-0.15) .. (0,0) .. controls (1.72,0.15) and (3.61,0.72) .. (5.68,1.71)   ;
    		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (174.49,188.8) -- (175.02,152.47) ;
    		\\draw [shift={(175.07,149.47)}, rotate = 90.84] [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (5.68,-1.71) .. controls (3.61,-0.72) and (1.72,-0.15) .. (0,0) .. controls (1.72,0.15) and (3.61,0.72) .. (5.68,1.71)   ;
    		\\draw [color={rgb, 255:red, 74; green, 144; blue, 226 }  ,draw opacity=1 ][line width=1]    (174.49,188.8) -- (259.42,118.71) ;
    		\\draw [shift={(261.73,116.8)}, rotate = 140.47] [color={rgb, 255:red, 74; green, 144; blue, 226 }  ,draw opacity=1 ][line width=1]    (5.68,-1.71) .. controls (3.61,-0.72) and (1.72,-0.15) .. (0,0) .. controls (1.72,0.15) and (3.61,0.72) .. (5.68,1.71)   ;
    		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (261.73,116.8) -- (261.71,223.07) ;
    		\\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (262.25,96.53) .. controls (262.25,95.88) and (263.43,95.36) .. (264.89,95.36) .. controls (266.34,95.36) and (267.52,95.88) .. (267.52,96.53) .. controls (267.52,97.17) and (266.34,97.7) .. (264.89,97.7) .. controls (263.43,97.7) and (262.25,97.17) .. (262.25,96.53) -- cycle ;
    		\\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (262.84,101.48) -- (263.14,99.26) -- (267.03,99.26) -- (267.33,101.48) -- cycle ;
    		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.55 ][fill={rgb, 255:red, 228; green, 224; blue, 224 }  ,fill opacity=1 ] (223.19,103.86) -- (226.11,103.67) -- (230.21,110.5) -- (226.31,117.23) -- (223.28,116.94) -- (226.6,110.69) -- cycle ;
    		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.57 ][fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (253.82,106.69) -- (254.8,113.62) -- (229.04,111.67) -- (226.6,110.69) -- (230.11,109.33) -- cycle ;
    		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (277.51,111.12) -- (282.51,118.2) -- (281.81,118.69) -- (276.81,111.62) -- cycle ;
    		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (271.55,110.61) -- (271.06,119.26) -- (270.21,119.21) -- (270.7,110.56) -- cycle ;
    		\\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (288.05,116.23) -- (289.01,116.73) -- (285.05,118.93) -- (262.82,119.93) -- (262.46,119.21) -- (284.87,118.05) -- cycle ;
    		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (275.2,112.54) -- (275.03,121.2) -- (274.17,121.18) -- (274.34,112.52) -- cycle ;
    		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (263.02,113.54) -- (259.22,121.33) -- (258.45,120.96) -- (262.24,113.17) -- cycle ;
    		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.58 ][fill={rgb, 255:red, 228; green, 224; blue, 224 }  ,fill opacity=1 ] (252.26,106.71) .. controls (252.4,105.52) and (253.16,104.56) .. (253.84,103.75) .. controls (257.88,100.85) and (265.39,100.01) .. (269.38,100.82) .. controls (270.89,101.48) and (272.66,102.16) .. (273.07,103.65) .. controls (274.92,107.36) and (251.85,110.15) .. (252.26,106.71) -- cycle ;
    		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (260.74,102.67) .. controls (260.84,102.15) and (261.33,101.69) .. (261.82,101.63) -- (265.29,101.22) .. controls (265.79,101.16) and (266.11,101.53) .. (266.01,102.04) -- (265.71,103.58) .. controls (265.61,104.09) and (265.13,104.56) .. (264.63,104.62) -- (261.16,105.03) .. controls (260.67,105.08) and (260.35,104.71) .. (260.45,104.2) -- cycle ;
    		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.45 ][fill={rgb, 255:red, 230; green, 226; blue, 226 }  ,fill opacity=1 ] (252.26,106.71) .. controls (259.99,103.45) and (270.72,103.16) .. (281.03,102.77) .. controls (282.73,103.84) and (284.09,103.94) .. (287.41,107.65) .. controls (288.68,108.14) and (293.13,109.13) .. (292.77,111.45) .. controls (292.77,116.63) and (258.82,118.38) .. (256.19,116.53) .. controls (254.33,114.48) and (251.31,111.45) .. (252.26,106.71) -- cycle ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (280.19,103.16) -- (282.43,103.26) -- (287.12,107.65) -- (284.29,108.33) -- (280.38,109.31) -- (277.36,103.94) -- cycle ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (276.87,104.33) -- (279.31,109.02) -- (275.31,109.6) -- (274.63,104.62) -- cycle ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (273.85,104.72) -- (274.43,109.5) -- (270.33,109.89) -- (269.94,105.01) -- cycle ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (268.97,105.21) -- (269.46,109.89) -- (265.85,110.19) -- (265.26,105.6) -- cycle ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (264.38,105.7) -- (264.77,109.02) -- (261.36,109.41) -- (260.97,106.28) -- cycle ;
    		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.48 ][fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (252.09,107.75) .. controls (253.43,107.08) and (254.56,107.29) .. (257.16,106.67) .. controls (258.53,108.04) and (259.5,110.87) .. (260.87,111.36) .. controls (266.04,110.97) and (270.14,110.48) .. (281.46,109.8) .. controls (283.58,108.52) and (285.88,107.96) .. (288.09,107.89) .. controls (291.7,108.82) and (293.85,109.7) .. (292.58,112.04) .. controls (281.72,113.89) and (268.47,114.31) .. (259.74,114.76) .. controls (258.82,114.81) and (257.94,114.85) .. (257.13,114.9) .. controls (254.62,114.19) and (252.19,112.04) .. (252.09,107.75) -- cycle ;
    		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.47 ]   (256.5,107.34) .. controls (257.45,109.8) and (259.02,111.06) .. (260.09,112.04) ;
    		\\draw    (265.85,110.97) -- (266.53,114.48) ;
    		\\draw    (266.72,110.97) -- (267.31,114.48) ;
    		\\draw    (275.21,110.19) -- (275.9,113.7) ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (281.16,110.87) .. controls (282.14,109.89) and (285.65,110.97) .. (288.77,112.14) .. controls (288.38,114.77) and (284.87,115.65) .. (282.63,114.19) .. controls (280.87,112.14) and (280.77,111.55) .. (281.16,110.87) -- cycle ;
    		\\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.4 ]   (256.09,115.46) -- (281.65,113.99) ;
    		\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (256.48,115.85) -- (282.04,114.38) ;
    		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (254.48,108.56) .. controls (254.45,108.31) and (254.63,108.07) .. (254.89,108.04) -- (256.82,107.81) .. controls (257.07,107.78) and (257.31,107.97) .. (257.34,108.23) -- (257.43,108.99) .. controls (257.46,109.25) and (257.27,109.48) .. (257.02,109.51) -- (255.09,109.74) .. controls (254.83,109.77) and (254.6,109.59) .. (254.57,109.33) -- cycle ;
    		\\draw  [fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (280.2,118.32) -- (281.3,118.83) -- (276.75,121.09) -- (251.24,122.2) -- (250.83,121.47) -- (276.55,120.2) -- cycle ;
    		\\draw [color={rgb, 255:red, 100; green, 7; blue, 7 }  ,draw opacity=1 ]   (233.33,110.11) -- (251.97,108.55) ;
    		\\draw [color={rgb, 255:red, 146; green, 21; blue, 21 }  ,draw opacity=1 ]   (242.31,110.99) -- (252.26,111.18) ;
    		\\draw  [color={rgb, 255:red, 100; green, 12; blue, 12 }  ,draw opacity=1 ][fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (225.04,104.74) -- (228.46,109.23) -- (230.6,106.69) -- (231.48,107.47) -- (229.14,110.3) -- (232.65,112.94) -- (231.19,114.11) -- (228.07,110.99) -- (225.24,115.28) -- (223.77,114.69) -- (227.77,110.3) -- (222.99,106.01) -- cycle ;
    		\\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (227.21,110.1) .. controls (227.21,109.35) and (227.81,108.74) .. (228.56,108.74) .. controls (229.31,108.74) and (229.92,109.35) .. (229.92,110.1) .. controls (229.92,110.85) and (229.31,111.45) .. (228.56,111.45) .. controls (227.81,111.45) and (227.21,110.85) .. (227.21,110.1) -- cycle ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (227.88,110.1) .. controls (227.88,109.72) and (228.19,109.42) .. (228.56,109.42) .. controls (228.94,109.42) and (229.25,109.72) .. (229.25,110.1) .. controls (229.25,110.48) and (228.94,110.78) .. (228.56,110.78) .. controls (228.19,110.78) and (227.88,110.48) .. (227.88,110.1) -- cycle ;
    		\\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (264.26,97.21) -- (265.47,97.21) -- (265.47,100.37) -- (264.26,100.37) -- cycle ;
    		\\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (288.77,90.98) -- (292.37,91.84) -- (266.12,97.5) -- (264.26,97.21) -- cycle ;
    		\\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (299,99.28) -- (296.48,100.53) -- (265.94,97.89) -- (264.87,97.21) -- cycle ;
    		\\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (264.26,97.21) -- (264.56,97.7) -- (240.75,101.99) -- (237.33,101.21) -- cycle ;
    		\\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (264.87,97.21) -- (263.91,97.78) -- (224.01,95.24) -- (226.84,94.07) -- cycle ;
    		\\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (268.42,95.77) -- (269.77,97.4) -- (268.6,98.48) -- (265.18,97.79) -- (262.74,98.67) -- (261.28,98.09) -- (260.99,96.14) -- (264.79,96.62) -- cycle ;
    		\\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (264.26,97.21) .. controls (264.26,96.86) and (264.57,96.58) .. (264.95,96.58) .. controls (265.32,96.58) and (265.63,96.86) .. (265.63,97.21) .. controls (265.63,97.56) and (265.32,97.84) .. (264.95,97.84) .. controls (264.57,97.84) and (264.26,97.56) .. (264.26,97.21) -- cycle ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.22 ] (252.48,110.48) -- (253.18,113.11) -- (231.62,111.75) -- (230.21,110.5) -- cycle ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.22 ] (257.43,108.99) -- (261.28,113.31) -- (255.62,113.8) -- (253.77,112.14) -- (252.79,109.89) -- cycle ;
    		\\draw [color={rgb, 255:red, 220; green, 128; blue, 128 }  ,draw opacity=1 ]   (268.11,111.55) -- (280.01,110.67) ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.26 ] (275.76,104.46) -- (260.97,106.28) -- (269.46,109.89) -- (271.6,109.8) -- cycle ;
    		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.46 ] (281.74,103.16) -- (277.46,104.37) -- (283.82,107.84) -- (286.04,107.19) -- cycle ;
    		\\draw (68,219) node [anchor=north west][inner sep=0.75pt]    {$x$};
    		\\draw (373.33,168) node [anchor=north west][inner sep=0.75pt]    {$y$};
    		\\draw (158,38.67) node [anchor=north west][inner sep=0.75pt]    {$z$};
    		\\draw (130,178.67) node [anchor=north west][inner sep=0.75pt]  [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,opacity=1 ]  {$\\vec{i}$};
    		\\draw (210.67,159.33) node [anchor=north west][inner sep=0.75pt]  [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,opacity=1 ]  {$\\vec{j}$};
    		\\draw (155.33,130) node [anchor=north west][inner sep=0.75pt]  [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,opacity=1 ]  {$\\vec{k}$};
    		\\draw (207.33,122) node [anchor=north west][inner sep=0.75pt]  [color={rgb, 255:red, 74; green, 144; blue, 226 }  ,opacity=1 ]  {$\\vec{r}$};
    		\\draw (154,171.33) node [anchor=north west][inner sep=0.75pt]    {$O$};
    	\\end{tikzpicture}
    \\end{center}'''
    % (x0, y0, z0, x0, y0, z0, vx, vy, vz))

    ########################################################################
    # Nhận biết ############################################
    # Các đáp án
    nb_da_1_d = '\\True Tại thời điểm 8 giờ sáng, khoảng cách từ máy bay đến tháp điều hành không lưu xấp xỉ $%s$ km (sai số không quá 1 km)' % (dist_M0_round)
    nb_da_1_s = 'Tại thời điểm 8 giờ sáng, khoảng cách từ máy bay đến tháp điều hành không lưu xấp xỉ $%s$ km (sai số không quá 1 km)' % (dist_M0_wrong)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]

    # Nội dung lời giải
    loigiai_nb_1 = ('''Lúc 8 giờ sáng, máy bay ở vị trí $M_0(%s; %s; %s)$. \\\\
    Khoảng cách từ máy bay đến tháp điều hành (gốc tọa độ $O$) là: \\\\
    $OM_0 = \\sqrt{x_0^2 + y_0^2 + z_0^2} = \\sqrt{%s^2 + %s^2 + %s^2} = \\sqrt{%s} \\approx %s$ (km).'''
    % (x0, y0, z0, x0, y0, z0, dist_M0_sq, dist_M0_round))

    # Đưa các lời giải vào danh sách lời giải
    list_nb_2 = [loigiai_nb_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)


    ########################################################################
    # Thông hiểu ############################################
    # Các đáp án
    th_da_1_d = '\\True Tại thời điểm 9 giờ sáng, độ cao của máy bay so với mặt đất là $%s$ km' % (h_9am)
    th_da_1_s = 'Tại thời điểm 9 giờ sáng, độ cao của máy bay so với mặt đất là $%s$ km' % (h_9am_wrong)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)

    list_th_1 = [th_da_1]

    # Nội dung lời giải
    loigiai_th_1 = ('''Sau 1 giờ bay (từ 8 giờ đến 9 giờ), cao độ $z$ của máy bay thay đổi theo phương trình $z(t) = z_0 + v_z \\cdot t$. \\\\
    Tại $t = 1$, ta có độ cao máy bay là: $z = %s + %s \\cdot 1 = %s$ (km).'''
    % (z0, vz, h_9am))

    list_th_2 = [loigiai_th_1]
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)


    ########################################################################
    # Vận dụng ############################################
    # Các đáp án
    vd_da_1_d = '\\True Tại thời điểm 10 giờ sáng, khoảng cách từ máy bay đến tháp truyền hình $F(%s;%s;0)$ xấp xỉ $%s$ km (sai số không quá 10 km)' % (xF, yF, dist_F_round)
    vd_da_1_s = 'Tại thời điểm 10 giờ sáng, khoảng cách từ máy bay đến tháp truyền hình $F(%s;%s;0)$ xấp xỉ $%s$ km (sai số không quá 10 km)' % (xF, yF, dist_F_wrong)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)

    list_vd_1 = [vd_da_1]

    # Nội dung lời giải
    loigiai_vd_1 = ('''Tại thời điểm 10 giờ sáng (sau $t = 2$ giờ bay), vị trí của máy bay là $M_2(x_2; y_2; z_2)$ với: \\\\
    $x_2 = %s + %s \\cdot 2 = %s$ \\\\
    $y_2 = %s + %s \\cdot 2 = %s$ \\\\
    $z_2 = %s + %s \\cdot 2 = %s$. \\\\
    Tọa độ máy bay lúc 10 giờ là $M_2(%s; %s; %s)$. \\\\
    Khoảng cách từ máy bay đến tháp truyền hình $F(%s; %s; 0)$ là: \\\\
    $M_2F = \\sqrt{(%s - %s)^2 + (%s - %s)^2 + (0 - %s)^2} = \\sqrt{%s} \\approx %s$ (km).'''
    % (x0, vx, x2, y0, vy, y2, z0, vz, z2, x2, y2, z2, xF, yF, xF, x2, yF, y2, z2, dist_F_sq, dist_F_round))

    list_vd_2 = [loigiai_vd_1]
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)


    ########################################################################
    # Vận dụng cao ############################################
    # Các đáp án
    vdc_da_1_d = '\\True Khi đạt độ cao $%s$ km, máy bay nhận lệnh hạ cánh và đổi sang vận tốc mới là $\\vec{v}_2 = (%s;%s;%s)$ km/h để hướng về đường băng B. Tọa độ của máy bay ngay khi chạm đất tại đường băng B là $(%s;%s;0)$' % (z2, v2x, v2y, v2z, xB, yB)
    vdc_da_1_s = 'Khi đạt độ cao $%s$ km, máy bay nhận lệnh hạ cánh và đổi sang vận tốc mới là $\\vec{v}_2 = (%s;%s;%s)$ km/h để hướng về đường băng B. Tọa độ của máy bay ngay khi chạm đất tại đường băng B là $(%s;%s;0)$' % (z2, v2x, v2y, v2z, xB_wrong, yB_wrong)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)

    list_vdc_1 = [vdc_da_1]

    # Nội dung lời giải
    loigiai_vdc_1 = ('''Máy bay đạt độ cao $z = %s$ km khi $z(t) = %s + %s t = %s \\Leftrightarrow t = 2$ (giờ). \\\\
    Lúc này máy bay đang ở vị trí $M_2(%s; %s; %s)$. \\\\
    Máy bay chuyển hướng với vectơ vận tốc mới $\\vec{v}_2 = (%s; %s; %s)$. \\\\
    Phương trình chuyển động theo trục $Oz$ là $z' = %s %s t'$. \\\\
    Máy bay chạm đất khi độ cao $z' = 0 \\Leftrightarrow %s %s t' = 0 \\Leftrightarrow t' = %s$ (giờ). \\\\
    Tọa độ máy bay khi chạm đất (tại đường băng B) là: \\\\
    $x_B = %s + %s \\cdot %s = %s$ \\\\
    $y_B = %s + %s \\cdot %s = %s$. \\\\
    Vậy tọa độ đường băng B là $(%s; %s; 0)$.'''
    % (z2, z0, vz, z2, x2, y2, z2, v2x, v2y, v2z, z2, v2z_str, z2, v2z_str, t_descend, x2, v2x, t_descend, xB, y2, v2y, t_descend, yB, xB, yB))

    list_vdc_2 = [loigiai_vdc_1]
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))
    random.shuffle(combined_vdc)
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


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


def bt_dang14_p3_b2_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random các thông số của bài toán: chiều cao BD, CD và khoảng cách AD
                while True:
                    bd = randint(12, 20)
                    cd = randint(6, bd - 3)
                    ad = randint(10, 20)

                    # Tính tan(BAD) và tan(CAD)
                    tan_bad = Rational(bd, ad)
                    tan_cad = Rational(cd, ad)

                    # Tính tan(alpha) = tan(BAD - CAD) = (tan_bad - tan_cad) / (1 + tan_bad * tan_cad)
                    tan_alpha = (tan_bad - tan_cad) / (1 + tan_bad * tan_cad)

                    # Đảm bảo phân số khác 1 hoặc quá đặc biệt để kết quả làm tròn có ý nghĩa
                    if tan_alpha > 0:
                        break

                # Tính góc alpha bằng radian rồi chuyển sang độ
                alpha_rad = float(math.atan(tan_alpha))
                alpha_deg = math.degrees(alpha_rad)

                # Làm tròn đến hàng phần chục
                kq_num = Decimal(str(alpha_deg)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq = str(kq_num).replace('.', ',')

                # Các đáp án trắc nghiệm
                du = ['$%s^\\circ$' % kq]
                da = random.choice(du)

                kq_float = float(kq_num)
                # Tạo các phương án nhiễu (cộng/trừ một vài độ)
                s = []
                cac_phuong_an_nhieu = [kq_float + 1.5, kq_float - 1.5, kq_float + 2.5, kq_float - 2.5, kq_float + 3.0, kq_float - 3.0]
                for phan_tu in cac_phuong_an_nhieu:
                    if phan_tu > 0:
                        val_sai = '$%s^\\circ$' % str(Decimal(str(phan_tu)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')
                        if val_sai != da and val_sai not in s:
                            s.append(val_sai)

                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Rút gọn phân số tan_bad và tan_cad để hiển thị trong lời giải
                tan_bad_p = tan_bad.p
                tan_bad_q = tan_bad.q
                tan_cad_p = tan_cad.p
                tan_cad_q = tan_cad.q

                # Rút gọn phân số tan_alpha để hiển thị
                tan_alpha_p = tan_alpha.p
                tan_alpha_q = tan_alpha.q
                hinhve=r'''\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (150.26,176.14) .. controls (156.71,173.58) and (167.53,171.9) .. (179.8,171.9) .. controls (191.87,171.9) and (202.54,173.53) .. (209.02,176.02) -- cycle ;
            	\draw  [fill={rgb, 255:red, 210; green, 224; blue, 240 }  ,fill opacity=1 ] (144.5,175) -- (380.6,175) -- (380.6,202.4) -- (144.5,202.4) -- cycle ;
            	\draw  [draw opacity=0] (144.5,175) -- (379.6,175) -- (379.6,202.4) -- (144.5,202.4) -- cycle ; \draw   (144.5,175) -- (144.5,202.4)(150.5,175) -- (150.5,202.4)(156.5,175) -- (156.5,202.4)(162.5,175) -- (162.5,202.4)(168.5,175) -- (168.5,202.4)(174.5,175) -- (174.5,202.4)(180.5,175) -- (180.5,202.4)(186.5,175) -- (186.5,202.4)(192.5,175) -- (192.5,202.4)(198.5,175) -- (198.5,202.4)(204.5,175) -- (204.5,202.4)(210.5,175) -- (210.5,202.4)(216.5,175) -- (216.5,202.4)(222.5,175) -- (222.5,202.4)(228.5,175) -- (228.5,202.4)(234.5,175) -- (234.5,202.4)(240.5,175) -- (240.5,202.4)(246.5,175) -- (246.5,202.4)(252.5,175) -- (252.5,202.4)(258.5,175) -- (258.5,202.4)(264.5,175) -- (264.5,202.4)(270.5,175) -- (270.5,202.4)(276.5,175) -- (276.5,202.4)(282.5,175) -- (282.5,202.4)(288.5,175) -- (288.5,202.4)(294.5,175) -- (294.5,202.4)(300.5,175) -- (300.5,202.4)(306.5,175) -- (306.5,202.4)(312.5,175) -- (312.5,202.4)(318.5,175) -- (318.5,202.4)(324.5,175) -- (324.5,202.4)(330.5,175) -- (330.5,202.4)(336.5,175) -- (336.5,202.4)(342.5,175) -- (342.5,202.4)(348.5,175) -- (348.5,202.4)(354.5,175) -- (354.5,202.4)(360.5,175) -- (360.5,202.4)(366.5,175) -- (366.5,202.4)(372.5,175) -- (372.5,202.4)(378.5,175) -- (378.5,202.4) ; \draw   (144.5,175) -- (379.6,175)(144.5,181) -- (379.6,181)(144.5,187) -- (379.6,187)(144.5,193) -- (379.6,193)(144.5,199) -- (379.6,199) ; \draw    ;
            	\draw  [fill={rgb, 255:red, 139; green, 87; blue, 42 }  ,fill opacity=1 ] (180.1,137.4) -- (172.6,119.4) -- (176.6,122.4) -- (183.6,134.4) -- (181.1,161.4) -- (186.5,175) -- (171.6,174.4) -- (178.6,166.9) -- cycle ;
            	\draw    (183.6,134.4) -- (191.6,115.4) ;
            	\draw    (190.1,109.4) -- (191.6,115.4) ;
            	\draw    (191.6,115.4) -- (198.6,110.4) ;
            	\draw    (158.6,113.4) -- (172.6,119.4) ;
            	\draw    (172.6,119.4) -- (166.1,108.4) ;
            	\draw    (176.6,122.4) -- (178.1,115.9) ;
            	\draw    (173.1,103.9) -- (178.1,115.9) ;
            	\draw    (178.1,115.9) -- (184.6,106.9) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (178.92,97.23) .. controls (178.75,95.75) and (179.31,94.29) .. (180.36,93.47) .. controls (181.41,92.64) and (182.76,92.59) .. (183.85,93.35) .. controls (184.23,92.49) and (184.94,91.9) .. (185.75,91.75) .. controls (186.56,91.6) and (187.39,91.92) .. (187.97,92.6) .. controls (188.3,91.82) and (188.94,91.3) .. (189.68,91.22) .. controls (190.41,91.13) and (191.12,91.5) .. (191.57,92.19) .. controls (192.16,91.37) and (193.11,91.02) .. (193.99,91.3) .. controls (194.88,91.58) and (195.55,92.44) .. (195.71,93.51) .. controls (196.44,93.74) and (197.04,94.33) .. (197.37,95.14) .. controls (197.7,95.94) and (197.71,96.87) .. (197.42,97.69) .. controls (198.13,98.79) and (198.3,100.26) .. (197.86,101.54) .. controls (197.41,102.82) and (196.43,103.73) .. (195.26,103.93) .. controls (195.25,105.14) and (194.7,106.24) .. (193.8,106.82) .. controls (192.9,107.4) and (191.81,107.37) .. (190.95,106.73) .. controls (190.58,108.17) and (189.54,109.24) .. (188.28,109.46) .. controls (187.02,109.68) and (185.76,109.02) .. (185.06,107.77) .. controls (184.19,108.38) and (183.15,108.56) .. (182.17,108.26) .. controls (181.19,107.96) and (180.35,107.2) .. (179.85,106.16) .. controls (178.96,106.28) and (178.11,105.74) .. (177.7,104.8) .. controls (177.3,103.86) and (177.44,102.73) .. (178.05,101.96) .. controls (177.26,101.41) and (176.85,100.32) .. (177.05,99.25) .. controls (177.24,98.19) and (177.99,97.4) .. (178.9,97.28) ; \draw   (178.05,101.96) .. controls (178.42,102.22) and (178.85,102.34) .. (179.28,102.3)(179.85,106.16) .. controls (180.03,106.13) and (180.22,106.08) .. (180.39,106)(185.06,107.77) .. controls (184.93,107.54) and (184.82,107.29) .. (184.73,107.03)(190.95,106.73) .. controls (191.01,106.47) and (191.06,106.19) .. (191.08,105.92)(195.26,103.93) .. controls (195.27,102.65) and (194.65,101.47) .. (193.68,100.91)(197.42,97.69) .. controls (197.26,98.13) and (197.02,98.51) .. (196.71,98.82)(195.71,93.51) .. controls (195.74,93.68) and (195.75,93.86) .. (195.75,94.04)(191.57,92.19) .. controls (191.42,92.4) and (191.3,92.63) .. (191.21,92.88)(187.97,92.6) .. controls (187.89,92.78) and (187.83,92.98) .. (187.8,93.19)(183.85,93.35) .. controls (184.08,93.51) and (184.29,93.7) .. (184.48,93.92)(178.92,97.23) .. controls (178.94,97.43) and (178.98,97.63) .. (179.03,97.83) ;
            	\draw  [fill={rgb, 255:red, 65; green, 117; blue, 5 }  ,fill opacity=1 ] (180.39,99.1) .. controls (180.24,97.86) and (180.72,96.63) .. (181.61,95.94) .. controls (182.5,95.24) and (183.65,95.2) .. (184.58,95.84) .. controls (184.91,95.11) and (185.51,94.62) .. (186.2,94.49) .. controls (186.89,94.37) and (187.59,94.63) .. (188.08,95.21) .. controls (188.36,94.55) and (188.91,94.11) .. (189.53,94.04) .. controls (190.16,93.97) and (190.76,94.28) .. (191.14,94.87) .. controls (191.65,94.17) and (192.45,93.88) .. (193.2,94.12) .. controls (193.96,94.35) and (194.53,95.07) .. (194.66,95.97) .. controls (195.28,96.17) and (195.8,96.67) .. (196.08,97.34) .. controls (196.35,98.02) and (196.37,98.8) .. (196.12,99.49) .. controls (196.72,100.42) and (196.87,101.65) .. (196.49,102.73) .. controls (196.11,103.81) and (195.27,104.58) .. (194.29,104.74) .. controls (194.28,105.76) and (193.8,106.69) .. (193.04,107.18) .. controls (192.28,107.67) and (191.35,107.64) .. (190.61,107.1) .. controls (190.3,108.31) and (189.42,109.21) .. (188.35,109.39) .. controls (187.27,109.58) and (186.21,109.03) .. (185.6,107.97) .. controls (184.87,108.49) and (183.98,108.64) .. (183.15,108.39) .. controls (182.31,108.13) and (181.6,107.5) .. (181.18,106.62) .. controls (180.42,106.72) and (179.69,106.27) .. (179.35,105.48) .. controls (179.01,104.69) and (179.13,103.73) .. (179.64,103.08) .. controls (178.97,102.62) and (178.63,101.7) .. (178.79,100.81) .. controls (178.96,99.91) and (179.59,99.24) .. (180.37,99.15) ; \draw   (179.64,103.08) .. controls (179.96,103.3) and (180.33,103.4) .. (180.7,103.37)(181.18,106.62) .. controls (181.33,106.6) and (181.49,106.55) .. (181.64,106.48)(185.6,107.97) .. controls (185.49,107.78) and (185.4,107.57) .. (185.33,107.35)(190.61,107.1) .. controls (190.67,106.88) and (190.71,106.65) .. (190.73,106.42)(194.28,104.74) .. controls (194.29,103.66) and (193.77,102.67) .. (192.94,102.2)(196.12,99.49) .. controls (195.98,99.86) and (195.78,100.18) .. (195.52,100.44)(194.66,95.97) .. controls (194.69,96.12) and (194.7,96.27) .. (194.7,96.42)(191.14,94.87) .. controls (191.02,95.04) and (190.91,95.23) .. (190.84,95.44)(188.08,95.21) .. controls (188.02,95.36) and (187.97,95.53) .. (187.93,95.7)(184.58,95.84) .. controls (184.77,95.97) and (184.95,96.13) .. (185.12,96.32)(180.39,99.1) .. controls (180.41,99.27) and (180.44,99.44) .. (180.48,99.61) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (221.45,113.4) .. controls (221.33,115.51) and (220.2,117.43) .. (218.53,118.35) .. controls (216.86,119.26) and (214.94,119) .. (213.59,117.68) .. controls (212.84,118.8) and (211.71,119.46) .. (210.54,119.48) .. controls (209.36,119.49) and (208.28,118.86) .. (207.61,117.76) .. controls (206.97,118.77) and (205.94,119.36) .. (204.89,119.3) .. controls (203.84,119.24) and (202.92,118.55) .. (202.46,117.47) .. controls (201.43,118.49) and (200.02,118.75) .. (198.84,118.15) .. controls (197.66,117.54) and (196.92,116.18) .. (196.95,114.64) .. controls (195.98,114.14) and (195.27,113.16) .. (195,111.95) .. controls (194.73,110.75) and (194.93,109.43) .. (195.54,108.35) .. controls (194.79,106.63) and (194.91,104.53) .. (195.84,102.83) .. controls (196.76,101.13) and (198.37,100.08) .. (200.05,100.08) .. controls (200.35,98.39) and (201.4,96.97) .. (202.8,96.36) .. controls (204.19,95.76) and (205.72,96.07) .. (206.79,97.17) .. controls (207.65,95.23) and (209.36,93.98) .. (211.19,93.97) .. controls (213.01,93.96) and (214.62,95.18) .. (215.32,97.11) .. controls (216.69,96.45) and (218.19,96.45) .. (219.5,97.1) .. controls (220.81,97.76) and (221.8,99.03) .. (222.26,100.61) .. controls (223.54,100.65) and (224.62,101.62) .. (224.96,103.03) .. controls (225.3,104.45) and (224.84,106.01) .. (223.8,106.95) .. controls (224.78,107.91) and (225.09,109.54) .. (224.56,110.99) .. controls (224.04,112.44) and (222.79,113.38) .. (221.49,113.32) ; \draw   (223.8,106.95) .. controls (223.33,106.49) and (222.75,106.22) .. (222.14,106.18)(222.26,100.61) .. controls (222,100.6) and (221.73,100.64) .. (221.46,100.71)(215.32,97.11) .. controls (215.45,97.47) and (215.54,97.84) .. (215.6,98.23)(206.79,97.17) .. controls (206.63,97.53) and (206.5,97.9) .. (206.41,98.28)(200.05,100.08) .. controls (199.73,101.89) and (200.32,103.69) .. (201.56,104.71)(195.54,108.35) .. controls (195.87,107.77) and (196.3,107.29) .. (196.8,106.93)(196.95,114.64) .. controls (196.95,114.39) and (196.98,114.13) .. (197.02,113.88)(202.46,117.47) .. controls (202.71,117.21) and (202.94,116.92) .. (203.13,116.6)(207.61,117.76) .. controls (207.77,117.51) and (207.9,117.25) .. (208,116.97)(213.59,117.68) .. controls (213.31,117.4) and (213.05,117.08) .. (212.83,116.73)(221.45,113.4) .. controls (221.46,113.1) and (221.46,112.81) .. (221.43,112.52) ;
            	\draw  [fill={rgb, 255:red, 65; green, 117; blue, 5 }  ,fill opacity=1 ] (219.26,112.6) .. controls (219.12,114.56) and (218.18,116.36) .. (216.83,117.25) .. controls (215.49,118.13) and (213.97,117.94) .. (212.93,116.75) .. controls (212.32,117.8) and (211.41,118.44) .. (210.47,118.48) .. controls (209.54,118.52) and (208.7,117.96) .. (208.2,116.96) .. controls (207.66,117.91) and (206.83,118.48) .. (206,118.45) .. controls (205.17,118.42) and (204.46,117.8) .. (204.12,116.81) .. controls (203.28,117.78) and (202.16,118.05) .. (201.24,117.52) .. controls (200.32,116.99) and (199.77,115.74) .. (199.82,114.32) .. controls (199.07,113.88) and (198.53,112.99) .. (198.34,111.88) .. controls (198.16,110.76) and (198.34,109.54) .. (198.85,108.53) .. controls (198.3,106.95) and (198.44,105) .. (199.22,103.41) .. controls (199.99,101.81) and (201.29,100.8) .. (202.62,100.76) .. controls (202.89,99.19) and (203.76,97.85) .. (204.88,97.26) .. controls (206,96.66) and (207.2,96.91) .. (208.02,97.91) .. controls (208.75,96.09) and (210.14,94.9) .. (211.58,94.84) .. controls (213.03,94.79) and (214.28,95.88) .. (214.78,97.66) .. controls (215.88,97.01) and (217.08,96.97) .. (218.1,97.55) .. controls (219.12,98.13) and (219.87,99.28) .. (220.2,100.73) .. controls (221.21,100.74) and (222.04,101.61) .. (222.28,102.92) .. controls (222.52,104.22) and (222.12,105.68) .. (221.27,106.57) .. controls (222.03,107.44) and (222.23,108.94) .. (221.78,110.29) .. controls (221.33,111.65) and (220.33,112.55) .. (219.29,112.52) ; \draw   (221.27,106.57) .. controls (220.91,106.16) and (220.46,105.92) .. (219.97,105.89)(220.2,100.73) .. controls (219.99,100.73) and (219.78,100.77) .. (219.57,100.85)(214.78,97.66) .. controls (214.88,97.98) and (214.94,98.33) .. (214.98,98.68)(208.02,97.91) .. controls (207.89,98.24) and (207.78,98.59) .. (207.7,98.95)(202.62,100.76) .. controls (202.33,102.44) and (202.75,104.1) .. (203.71,105.01)(198.85,108.53) .. controls (199.12,107.98) and (199.48,107.52) .. (199.89,107.18)(199.82,114.32) .. controls (199.83,114.08) and (199.86,113.85) .. (199.9,113.61)(204.12,116.81) .. controls (204.33,116.57) and (204.51,116.29) .. (204.67,115.99)(208.2,116.96) .. controls (208.33,116.73) and (208.44,116.48) .. (208.52,116.22)(212.93,116.75) .. controls (212.72,116.5) and (212.52,116.21) .. (212.36,115.88)(219.26,112.6) .. controls (219.28,112.32) and (219.28,112.05) .. (219.27,111.79) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (143.24,102.49) .. controls (143,100.39) and (143.79,98.31) .. (145.29,97.13) .. controls (146.79,95.95) and (148.72,95.88) .. (150.27,96.96) .. controls (150.82,95.73) and (151.83,94.89) .. (152.98,94.68) .. controls (154.14,94.47) and (155.32,94.92) .. (156.15,95.89) .. controls (156.62,94.78) and (157.54,94.03) .. (158.58,93.92) .. controls (159.63,93.8) and (160.65,94.33) .. (161.28,95.31) .. controls (162.13,94.14) and (163.48,93.64) .. (164.74,94.04) .. controls (166,94.44) and (166.96,95.67) .. (167.19,97.18) .. controls (168.23,97.52) and (169.09,98.37) .. (169.56,99.51) .. controls (170.02,100.65) and (170.05,101.98) .. (169.62,103.15) .. controls (170.64,104.72) and (170.88,106.81) .. (170.25,108.64) .. controls (169.62,110.48) and (168.21,111.78) .. (166.55,112.06) .. controls (166.54,113.77) and (165.74,115.35) .. (164.47,116.18) .. controls (163.19,117.01) and (161.63,116.96) .. (160.4,116.05) .. controls (159.87,118.11) and (158.39,119.62) .. (156.59,119.94) .. controls (154.79,120.26) and (153,119.32) .. (151.99,117.53) .. controls (150.76,118.41) and (149.27,118.66) .. (147.87,118.23) .. controls (146.47,117.8) and (145.28,116.72) .. (144.56,115.24) .. controls (143.3,115.41) and (142.08,114.64) .. (141.5,113.3) .. controls (140.93,111.96) and (141.13,110.34) .. (142,109.24) .. controls (140.87,108.46) and (140.29,106.9) .. (140.57,105.39) .. controls (140.85,103.87) and (141.91,102.73) .. (143.21,102.57) ; \draw   (142,109.24) .. controls (142.53,109.61) and (143.14,109.78) .. (143.76,109.72)(144.56,115.24) .. controls (144.83,115.2) and (145.09,115.12) .. (145.34,115.01)(151.99,117.53) .. controls (151.81,117.2) and (151.65,116.85) .. (151.53,116.48)(160.4,116.05) .. controls (160.49,115.67) and (160.55,115.28) .. (160.58,114.89)(166.55,112.06) .. controls (166.56,110.22) and (165.68,108.55) .. (164.29,107.75)(169.62,103.15) .. controls (169.4,103.77) and (169.05,104.33) .. (168.62,104.77)(167.19,97.18) .. controls (167.23,97.43) and (167.24,97.69) .. (167.24,97.95)(161.28,95.31) .. controls (161.07,95.61) and (160.9,95.93) .. (160.77,96.29)(156.15,95.89) .. controls (156.04,96.15) and (155.95,96.44) .. (155.9,96.73)(150.27,96.96) .. controls (150.6,97.18) and (150.9,97.46) .. (151.17,97.77)(143.24,102.49) .. controls (143.27,102.78) and (143.33,103.07) .. (143.4,103.35) ;
            	\draw  [fill={rgb, 255:red, 65; green, 117; blue, 5 }  ,fill opacity=1 ] (145.24,104.14) .. controls (145.04,102.24) and (145.69,100.37) .. (146.91,99.31) .. controls (148.14,98.25) and (149.72,98.19) .. (150.99,99.15) .. controls (151.43,98.05) and (152.26,97.29) .. (153.2,97.1) .. controls (154.15,96.91) and (155.11,97.31) .. (155.79,98.19) .. controls (156.17,97.19) and (156.93,96.52) .. (157.78,96.41) .. controls (158.63,96.31) and (159.47,96.79) .. (159.99,97.67) .. controls (160.68,96.61) and (161.78,96.17) .. (162.81,96.53) .. controls (163.84,96.89) and (164.62,97.99) .. (164.81,99.36) .. controls (165.66,99.66) and (166.36,100.42) .. (166.75,101.45) .. controls (167.13,102.48) and (167.15,103.68) .. (166.8,104.73) .. controls (167.64,106.14) and (167.83,108.03) .. (167.32,109.68) .. controls (166.8,111.33) and (165.65,112.49) .. (164.29,112.75) .. controls (164.28,114.29) and (163.63,115.72) .. (162.59,116.46) .. controls (161.54,117.21) and (160.27,117.16) .. (159.26,116.34) .. controls (158.83,118.2) and (157.62,119.56) .. (156.15,119.85) .. controls (154.68,120.13) and (153.22,119.28) .. (152.39,117.67) .. controls (151.38,118.47) and (150.17,118.7) .. (149.03,118.31) .. controls (147.88,117.92) and (146.91,116.95) .. (146.32,115.61) .. controls (145.29,115.77) and (144.29,115.07) .. (143.82,113.87) .. controls (143.35,112.66) and (143.51,111.2) .. (144.22,110.22) .. controls (143.3,109.51) and (142.83,108.11) .. (143.06,106.74) .. controls (143.28,105.38) and (144.15,104.35) .. (145.22,104.21) ; \draw   (144.22,110.22) .. controls (144.66,110.55) and (145.16,110.7) .. (145.66,110.65)(146.32,115.61) .. controls (146.54,115.58) and (146.75,115.51) .. (146.95,115.4)(152.39,117.67) .. controls (152.24,117.38) and (152.11,117.06) .. (152.01,116.73)(159.26,116.34) .. controls (159.34,116) and (159.39,115.65) .. (159.41,115.3)(164.29,112.75) .. controls (164.3,111.1) and (163.58,109.59) .. (162.44,108.87)(166.8,104.73) .. controls (166.62,105.29) and (166.34,105.79) .. (165.98,106.18)(164.81,99.36) .. controls (164.84,99.58) and (164.86,99.81) .. (164.86,100.04)(159.99,97.67) .. controls (159.81,97.94) and (159.67,98.23) .. (159.56,98.55)(155.79,98.19) .. controls (155.7,98.43) and (155.63,98.68) .. (155.59,98.95)(150.99,99.15) .. controls (151.25,99.36) and (151.5,99.6) .. (151.72,99.89)(145.24,104.14) .. controls (145.27,104.4) and (145.31,104.66) .. (145.37,104.91) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (156.83,85.71) .. controls (156.54,83.15) and (157.5,80.62) .. (159.32,79.19) .. controls (161.14,77.76) and (163.49,77.67) .. (165.38,78.98) .. controls (166.05,77.49) and (167.27,76.47) .. (168.68,76.21) .. controls (170.09,75.95) and (171.52,76.5) .. (172.53,77.68) .. controls (173.1,76.33) and (174.22,75.43) .. (175.49,75.28) .. controls (176.76,75.14) and (178,75.78) .. (178.77,76.98) .. controls (179.8,75.55) and (181.44,74.95) .. (182.97,75.44) .. controls (184.51,75.92) and (185.67,77.41) .. (185.95,79.26) .. controls (187.21,79.66) and (188.26,80.69) .. (188.83,82.09) .. controls (189.4,83.48) and (189.43,85.09) .. (188.91,86.51) .. controls (190.15,88.42) and (190.44,90.96) .. (189.68,93.19) .. controls (188.91,95.42) and (187.2,97) .. (185.18,97.34) .. controls (185.16,99.43) and (184.19,101.35) .. (182.64,102.36) .. controls (181.09,103.36) and (179.2,103.3) .. (177.69,102.19) .. controls (177.05,104.7) and (175.25,106.54) .. (173.06,106.93) .. controls (170.88,107.31) and (168.7,106.17) .. (167.47,103.99) .. controls (165.97,105.07) and (164.16,105.37) .. (162.46,104.85) .. controls (160.76,104.33) and (159.32,103.01) .. (158.44,101.21) .. controls (156.9,101.42) and (155.42,100.48) .. (154.72,98.85) .. controls (154.02,97.22) and (154.26,95.25) .. (155.32,93.92) .. controls (153.95,92.97) and (153.25,91.07) .. (153.58,89.23) .. controls (153.92,87.38) and (155.22,86.01) .. (156.8,85.81) ; \draw   (155.32,93.92) .. controls (155.97,94.37) and (156.71,94.58) .. (157.46,94.51)(158.44,101.21) .. controls (158.76,101.16) and (159.08,101.07) .. (159.38,100.93)(167.47,103.99) .. controls (167.25,103.59) and (167.06,103.16) .. (166.91,102.72)(177.69,102.19) .. controls (177.81,101.74) and (177.88,101.27) .. (177.92,100.79)(185.18,97.34) .. controls (185.19,95.11) and (184.12,93.07) .. (182.43,92.1)(188.91,86.51) .. controls (188.64,87.27) and (188.22,87.94) .. (187.69,88.48)(185.95,79.26) .. controls (186,79.56) and (186.02,79.87) .. (186.02,80.18)(178.77,76.98) .. controls (178.52,77.34) and (178.31,77.74) .. (178.15,78.17)(172.53,77.68) .. controls (172.39,78) and (172.29,78.35) .. (172.23,78.7)(165.38,78.98) .. controls (165.78,79.26) and (166.15,79.59) .. (166.48,79.97)(156.83,85.71) .. controls (156.87,86.07) and (156.94,86.41) .. (157.02,86.75) ;
            	\draw  [fill={rgb, 255:red, 65; green, 117; blue, 5 }  ,fill opacity=1 ] (159.43,87.79) .. controls (159.18,85.61) and (160,83.46) .. (161.54,82.24) .. controls (163.09,81.02) and (165.08,80.95) .. (166.68,82.06) .. controls (167.25,80.8) and (168.29,79.92) .. (169.49,79.7) .. controls (170.68,79.49) and (171.89,79.95) .. (172.75,80.96) .. controls (173.24,79.81) and (174.19,79.04) .. (175.26,78.92) .. controls (176.34,78.8) and (177.4,79.34) .. (178.05,80.36) .. controls (178.93,79.15) and (180.31,78.63) .. (181.62,79.05) .. controls (182.92,79.46) and (183.91,80.73) .. (184.15,82.3) .. controls (185.22,82.64) and (186.11,83.52) .. (186.59,84.7) .. controls (187.07,85.89) and (187.1,87.26) .. (186.66,88.47) .. controls (187.71,90.09) and (187.96,92.26) .. (187.31,94.15) .. controls (186.66,96.05) and (185.2,97.39) .. (183.49,97.68) .. controls (183.48,99.46) and (182.65,101.09) .. (181.34,101.95) .. controls (180.02,102.81) and (178.41,102.75) .. (177.14,101.81) .. controls (176.59,103.94) and (175.06,105.51) .. (173.21,105.84) .. controls (171.35,106.16) and (169.51,105.19) .. (168.46,103.34) .. controls (167.19,104.25) and (165.65,104.52) .. (164.21,104.07) .. controls (162.77,103.63) and (161.54,102.51) .. (160.8,100.97) .. controls (159.49,101.15) and (158.23,100.35) .. (157.64,98.97) .. controls (157.04,97.58) and (157.25,95.91) .. (158.14,94.77) .. controls (156.98,93.96) and (156.39,92.35) .. (156.67,90.78) .. controls (156.96,89.21) and (158.06,88.04) .. (159.4,87.87) ; \draw   (158.14,94.77) .. controls (158.69,95.16) and (159.33,95.33) .. (159.96,95.27)(160.8,100.97) .. controls (161.07,100.93) and (161.34,100.85) .. (161.59,100.73)(168.46,103.34) .. controls (168.27,103) and (168.11,102.64) .. (167.98,102.25)(177.14,101.81) .. controls (177.23,101.42) and (177.3,101.02) .. (177.33,100.62)(183.49,97.68) .. controls (183.5,95.79) and (182.59,94.05) .. (181.16,93.22)(186.66,88.47) .. controls (186.43,89.12) and (186.07,89.69) .. (185.62,90.14)(184.15,82.3) .. controls (184.19,82.56) and (184.2,82.82) .. (184.2,83.09)(178.05,80.36) .. controls (177.83,80.67) and (177.66,81) .. (177.52,81.37)(172.75,80.96) .. controls (172.64,81.23) and (172.55,81.52) .. (172.5,81.82)(166.68,82.06) .. controls (167.02,82.3) and (167.34,82.58) .. (167.62,82.9)(159.43,87.79) .. controls (159.46,88.09) and (159.52,88.39) .. (159.59,88.68) ;
            	\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1.5]    (204.5,175) -- (323.1,34.4) ;
            	\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1.5]    (204.5,175) -- (322.6,90.9) ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (323.1,34.4) -- (329.6,34.4) -- (329.6,175) -- (323.1,175) -- cycle ;
            	\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (323.1,34.4) -- (329.6,34.4) -- (329.6,53.4) -- (323.1,53.4) -- cycle ;
            	\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (323.6,71.9) -- (330.1,71.9) -- (330.1,90.9) -- (323.6,90.9) -- cycle ;
            	\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (323.1,106.7) -- (329.6,106.7) -- (329.6,125.7) -- (323.1,125.7) -- cycle ;
            	\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (323.1,142.4) -- (329.6,142.4) -- (329.6,161.4) -- (323.1,161.4) -- cycle ;
            	\draw (191,150.5) node [anchor=north west][inner sep=0.75pt]    {$A$};
            	\draw (332,23) node [anchor=north west][inner sep=0.75pt]    {$B$};
            	\draw (332.5,78) node [anchor=north west][inner sep=0.75pt]    {$C$};
            	\draw (332.5,155) node [anchor=north west][inner sep=0.75pt]    {$D$};
            \end{tikzpicture}'''
                # Câu hỏi
                noidungcauhoi = (r'''\immini{Từ một vị trí $A$, người ta buộc hai sợi cáp $AB$ và $AC$ đến một cái trụ cao $%s$m, được dựng vuông góc với mặt đất, chân trụ ở vị trí $D$. Biết $CD = %s$m và $AD = %s$m. Góc nhọn $\alpha = \widehat{BAC}$ tạo bởi hai sợi dây cáp đó, giá trị $\alpha$ bằng bao nhiêu? (làm tròn đến hàng phần chục, đơn vị độ).}{%s}''' 
                                 % (bd, cd, ad, hinhve))

                # Các đáp án
                da_d = ('\\True $\\alpha \\approx ' + str(da)[1:])
                da_s1 = '$\\alpha \\approx ' + str(das1)[1:]
                da_s2 = '$\\alpha \\approx ' + str(das2)[1:]
                da_s3 = '$\\alpha \\approx ' + str(das3)[1:]

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết y hệt mẫu gốc
                loigiai = ('''Ta có: \\\\
                           $\\tan \\alpha = \\tan(\\widehat{BAD} - \\widehat{CAD})$ \\\\
                           $= \\frac{\\tan \\widehat{BAD} - \\tan \\widehat{CAD}}{1 + \\tan \\widehat{BAD} \\tan \\widehat{CAD}} = \\frac{\\frac{%s}{%s} - \\frac{%s}{%s}}{1 + \\frac{%s}{%s} \\cdot \\frac{%s}{%s}} = \\frac{%s}{%s}$. \\\\
                           Vì vậy $\\alpha \\approx %s^\\circ$.'''
                           % (latex(bd), latex(ad), latex(cd), latex(ad),
                              latex(bd), latex(ad), latex(cd), latex(ad),
                              latex(tan_alpha_p), latex(tan_alpha_q), kq))
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content  


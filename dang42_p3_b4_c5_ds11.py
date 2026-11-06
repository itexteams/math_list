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


def bt_dang42_p3_b4_c5_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random thời gian nạp (phút)
                T_min = random.choice([30, 40, 45, 50, 60, 80, 90, 100, 120])
                t_val = Rational(T_min, 60) # thời gian nạp tính bằng giờ

                # Tính toán kết quả
                # t = -2/3 * ln(1 - Q/Q0) => ln(1 - Q/Q0) = -3/2 * t => 1 - Q/Q0 = e^(-3/2 * t)
                exponent = -Rational(3, 2) * t_val
                exp_val = float(exponent)
                ratio = 1 - math.exp(exp_val)
                percentage = ratio * 100

                # Làm tròn đến hàng phần chục
                kq_dec = Decimal(str(percentage)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq_str = str(kq_dec).replace('.', ',')
                kq_float = float(kq_dec)

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(kq_str)]
                da = random.choice(du)

                # Tạo các đáp án sai (dao động ngẫu nhiên xung quanh đáp án đúng)
                s_raw = [
                    kq_float + 1.2,
                    kq_float - 1.2,
                    kq_float + 2.5,
                    kq_float - 2.5,
                    kq_float + 10.5,
                    kq_float - 10.5,
                    kq_float + 5.0,
                    kq_float - 5.0
                ]
                s = []
                for val in s_raw:
                    # Làm tròn và đổi dấu chấm thành phẩy
                    val_dec = Decimal(str(abs(val))).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                    s.append('$%s$' % str(val_dec).replace('.', ','))

                s = list(set(s)) # Loại bỏ các đáp án sai bị trùng nhau
                if da in s:
                    s.remove(da) # Đảm bảo đáp án sai không trùng với đáp án đúng

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                hinhve=r'''\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-0.75,xscale=0.75]
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.09 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (231.07,114.73) .. controls (231.07,113.63) and (231.96,112.73) .. (233.07,112.73) -- (239.07,112.73) .. controls (240.17,112.73) and (241.07,113.63) .. (241.07,114.73) -- (241.07,124.07) .. controls (241.07,125.17) and (240.17,126.07) .. (239.07,126.07) -- (233.07,126.07) .. controls (231.96,126.07) and (231.07,125.17) .. (231.07,124.07) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.09 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.48 ] (236.07,113.73) .. controls (236.07,113.18) and (236.51,112.73) .. (237.07,112.73) -- (240.07,112.73) .. controls (240.62,112.73) and (241.07,113.18) .. (241.07,113.73) -- (241.07,125.07) .. controls (241.07,125.62) and (240.62,126.07) .. (240.07,126.07) -- (237.07,126.07) .. controls (236.51,126.07) and (236.07,125.62) .. (236.07,125.07) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.09 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (231.73,87.73) .. controls (231.73,86.63) and (232.63,85.73) .. (233.73,85.73) -- (239.73,85.73) .. controls (240.84,85.73) and (241.73,86.63) .. (241.73,87.73) -- (241.73,97.07) .. controls (241.73,98.17) and (240.84,99.07) .. (239.73,99.07) -- (233.73,99.07) .. controls (232.63,99.07) and (231.73,98.17) .. (231.73,97.07) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.09 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.48 ] (236.73,86.73) .. controls (236.73,86.18) and (237.18,85.73) .. (237.73,85.73) -- (240.73,85.73) .. controls (241.29,85.73) and (241.73,86.18) .. (241.73,86.73) -- (241.73,98.07) .. controls (241.73,98.62) and (241.29,99.07) .. (240.73,99.07) -- (237.73,99.07) .. controls (237.18,99.07) and (236.73,98.62) .. (236.73,98.07) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.26 ][fill={rgb, 255:red, 235; green, 232; blue, 232 }  ,fill opacity=1 ] (191,81.4) .. controls (191,76.61) and (194.88,72.73) .. (199.67,72.73) -- (225.67,72.73) .. controls (230.45,72.73) and (234.33,76.61) .. (234.33,81.4) -- (234.33,213.07) .. controls (234.33,217.85) and (230.45,221.73) .. (225.67,221.73) -- (199.67,221.73) .. controls (194.88,221.73) and (191,217.85) .. (191,213.07) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.46 ] (197.79,215.7) -- (191.91,210.98) -- (191.12,78.5) -- (196.95,73.71) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.46 ] (229.82,74.93) -- (234.99,79.16) -- (234.33,213.07) -- (229.12,217.25) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.09 ][fill={rgb, 255:red, 235; green, 232; blue, 232 }  ,fill opacity=1 ] (200.07,133.71) .. controls (200.07,130.78) and (202.44,128.4) .. (205.37,128.4) -- (221.29,128.4) .. controls (224.22,128.4) and (226.6,130.78) .. (226.6,133.71) -- (226.6,216.43) .. controls (226.6,219.36) and (224.22,221.73) .. (221.29,221.73) -- (205.37,221.73) .. controls (202.44,221.73) and (200.07,219.36) .. (200.07,216.43) -- cycle ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ]   (193,76.73) -- (193.27,206.73) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ]   (232,79.07) -- (232.27,209.07) ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (206,142.4) .. controls (206,141.48) and (206.75,140.73) .. (207.67,140.73) -- (217.27,140.73) .. controls (218.19,140.73) and (218.93,141.48) .. (218.93,142.4) -- (218.93,147.4) .. controls (218.93,148.32) and (218.19,149.07) .. (217.27,149.07) -- (207.67,149.07) .. controls (206.75,149.07) and (206,148.32) .. (206,147.4) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.09 ][fill={rgb, 255:red, 247; green, 183; blue, 76 }  ,fill opacity=1 ] (225.67,126.58) .. controls (225.67,130.71) and (222.53,134.07) .. (218.67,134.07) -- (209.67,134.07) .. controls (205.8,134.07) and (202.67,130.71) .. (202.67,126.58) -- (202.67,72.73) -- (225.67,72.73) -- (225.67,126.58) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.09 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (206.4,97.17) .. controls (206.4,94.53) and (208.53,92.4) .. (211.17,92.4) -- (217.63,92.4) .. controls (220.27,92.4) and (222.4,94.53) .. (222.4,97.17) -- (222.4,117.3) .. controls (222.4,119.93) and (220.27,122.07) .. (217.63,122.07) -- (211.17,122.07) .. controls (208.53,122.07) and (206.4,119.93) .. (206.4,117.3) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.24 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.62 ] (209,82.57) .. controls (209,79.53) and (211.46,77.07) .. (214.5,77.07) .. controls (217.54,77.07) and (220,79.53) .. (220,82.57) .. controls (220,85.6) and (217.54,88.07) .. (214.5,88.07) .. controls (211.46,88.07) and (209,85.6) .. (209,82.57) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 80; green, 227; blue, 194 }  ,fill opacity=1 ] (209.67,113.73) -- (218.4,113.73) -- (218.4,118.4) -- (209.67,118.4) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 80; green, 227; blue, 194 }  ,fill opacity=1 ] (209.67,107.07) -- (218.4,107.07) -- (218.4,111.73) -- (209.67,111.73) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 80; green, 227; blue, 194 }  ,fill opacity=1 ] (209.67,100.73) -- (218.4,100.73) -- (218.4,105.4) -- (209.67,105.4) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (183.93,207.73) -- (242.73,207.73) -- (242.73,223.4) -- (183.93,223.4) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.33 ] (194.7,207.73) -- (205.43,207.73) -- (205.43,223.59) -- (194.7,223.59) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.33 ] (226.6,207.73) -- (237.77,207.73) -- (237.77,223.59) -- (226.6,223.59) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.33 ] (207.97,207.64) -- (209.73,207.64) -- (209.73,223.5) -- (207.97,223.5) -- cycle ;
            	\draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ][line width=1.5]    (212.67,147.23) .. controls (212.16,191.93) and (230.93,184.47) .. (238.53,173.47) .. controls (246.13,162.47) and (266.47,139.13) .. (299.47,147.47) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (370.39,200.01) -- (365.12,204.24) -- (351.08,205.75) -- (345.03,202.73) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 182; blue, 35 }  ,fill opacity=1 ] (335.02,97.18) .. controls (339.31,95.04) and (342.02,98.43) .. (350.77,93.18) .. controls (353.65,92.47) and (354.15,103.17) .. (348.77,108.68) .. controls (342.64,114.96) and (333.77,106.63) .. (337.77,105.43) .. controls (333.77,102.18) and (331.82,98.78) .. (335.02,97.18) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 182; blue, 35 }  ,fill opacity=1 ] (323.27,86.18) .. controls (327.56,84.04) and (335.02,83.43) .. (343.77,78.18) .. controls (360.02,86.93) and (350.02,94.68) .. (357.52,92.43) .. controls (363.27,96.43) and (368.52,95.68) .. (364.27,100.68) .. controls (359.52,95.68) and (332.27,104.18) .. (327.52,99.93) .. controls (323.52,96.68) and (320.07,87.78) .. (323.27,86.18) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.79 ] (323.57,87.39) .. controls (325.17,86.41) and (328.22,88.5) .. (330.38,92.06) .. controls (332.53,95.61) and (332.97,99.28) .. (331.37,100.25) .. controls (329.76,101.23) and (326.71,99.14) .. (324.56,95.58) .. controls (322.41,92.03) and (321.96,88.36) .. (323.57,87.39) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.44 ] (330.38,92.06) .. controls (333.05,90.72) and (331.07,91.71) .. (336.27,90.43) .. controls (339.4,89.66) and (344.73,85.91) .. (348.02,83.93) .. controls (354.19,82.41) and (348.52,92.18) .. (356.02,89.93) .. controls (361.77,93.93) and (337.77,98.68) .. (332.77,97.93) .. controls (331.02,94.18) and (331.63,94.56) .. (330.38,92.06) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 182; blue, 35 }  ,fill opacity=1 ] (351.61,87.36) -- (350.38,91.75) .. controls (350.26,92.17) and (349.03,92.19) .. (347.64,91.8) .. controls (346.24,91.41) and (345.2,90.75) .. (345.32,90.33) -- (346.55,85.94) .. controls (346.67,85.52) and (347.9,85.5) .. (349.29,85.89) .. controls (350.69,86.29) and (351.73,86.94) .. (351.61,87.36) .. controls (351.49,87.78) and (350.26,87.8) .. (348.87,87.41) .. controls (347.47,87.02) and (346.44,86.36) .. (346.55,85.94) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (354.29,73.43) -- (350.37,87.38) .. controls (350.31,87.61) and (349.64,87.63) .. (348.87,87.41) .. controls (348.1,87.19) and (347.53,86.83) .. (347.6,86.6) -- (351.52,72.65) .. controls (351.58,72.42) and (352.25,72.41) .. (353.02,72.62) .. controls (353.79,72.84) and (354.36,73.2) .. (354.29,73.43) .. controls (354.23,73.66) and (353.55,73.67) .. (352.79,73.46) .. controls (352.02,73.24) and (351.45,72.88) .. (351.52,72.65) ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (351.46,76.96) .. controls (349.15,76.03) and (348.3,72.73) .. (349.56,69.57) .. controls (350.82,66.42) and (353.72,64.61) .. (356.03,65.54) .. controls (358.34,66.46) and (359.18,69.77) .. (357.92,72.92) .. controls (356.66,76.07) and (353.76,77.88) .. (351.46,76.96) -- cycle ;
            	\draw [color={rgb, 255:red, 220; green, 143; blue, 13 }  ,draw opacity=1 ]   (332.47,101.13) .. controls (337.47,98.73) and (339.42,99.38) .. (347.72,99.73) ;
            	\draw [line width=1.5]    (312.2,189.73) .. controls (316.53,193.73) and (315.13,188.07) .. (324.47,187.73) ;
            	\draw [line width=1.5]    (393.4,205.07) .. controls (412.6,210.73) and (413.6,212.4) .. (433.6,211.07) ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (432.57,196.57) .. controls (432.57,180.92) and (445.25,168.23) .. (460.9,168.23) .. controls (476.55,168.23) and (489.23,180.92) .. (489.23,196.57) .. controls (489.23,212.21) and (476.55,224.9) .. (460.9,224.9) .. controls (445.25,224.9) and (432.57,212.21) .. (432.57,196.57) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.76 ] (439.57,196.57) .. controls (439.57,184.78) and (449.12,175.23) .. (460.9,175.23) .. controls (472.68,175.23) and (482.23,184.78) .. (482.23,196.57) .. controls (482.23,208.35) and (472.68,217.9) .. (460.9,217.9) .. controls (449.12,217.9) and (439.57,208.35) .. (439.57,196.57) -- cycle ;
            	\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.27 ][line width=2.25]  (436.9,196.57) .. controls (436.9,183.31) and (447.65,172.57) .. (460.9,172.57) .. controls (474.15,172.57) and (484.9,183.31) .. (484.9,196.57) .. controls (484.9,209.82) and (474.15,220.57) .. (460.9,220.57) .. controls (447.65,220.57) and (436.9,209.82) .. (436.9,196.57) -- cycle ;
            	\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ][line width=1.5]  (441.23,196.57) .. controls (441.23,185.71) and (450.04,176.9) .. (460.9,176.9) .. controls (471.76,176.9) and (480.57,185.71) .. (480.57,196.57) .. controls (480.57,207.43) and (471.76,216.23) .. (460.9,216.23) .. controls (450.04,216.23) and (441.23,207.43) .. (441.23,196.57) -- cycle ;
            	\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.34 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (456.6,196.57) .. controls (456.6,193.99) and (458.69,191.9) .. (461.27,191.9) .. controls (463.84,191.9) and (465.93,193.99) .. (465.93,196.57) .. controls (465.93,199.14) and (463.84,201.23) .. (461.27,201.23) .. controls (458.69,201.23) and (456.6,199.14) .. (456.6,196.57) -- cycle ;
            	\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.34 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (458.93,189.57) .. controls (458.93,188.28) and (459.98,187.23) .. (461.27,187.23) .. controls (462.56,187.23) and (463.6,188.28) .. (463.6,189.57) .. controls (463.6,190.86) and (462.56,191.9) .. (461.27,191.9) .. controls (459.98,191.9) and (458.93,190.86) .. (458.93,189.57) -- cycle ;
            	\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.34 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (458.93,203.57) .. controls (458.93,202.28) and (459.98,201.23) .. (461.27,201.23) .. controls (462.56,201.23) and (463.6,202.28) .. (463.6,203.57) .. controls (463.6,204.86) and (462.56,205.9) .. (461.27,205.9) .. controls (459.98,205.9) and (458.93,204.86) .. (458.93,203.57) -- cycle ;
            	\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.34 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (464.93,193.57) .. controls (464.93,192.28) and (465.98,191.23) .. (467.27,191.23) .. controls (468.56,191.23) and (469.6,192.28) .. (469.6,193.57) .. controls (469.6,194.86) and (468.56,195.9) .. (467.27,195.9) .. controls (465.98,195.9) and (464.93,194.86) .. (464.93,193.57) -- cycle ;
            	\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.34 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (465.18,200.07) .. controls (465.18,198.78) and (466.23,197.73) .. (467.52,197.73) .. controls (468.81,197.73) and (469.85,198.78) .. (469.85,200.07) .. controls (469.85,201.36) and (468.81,202.4) .. (467.52,202.4) .. controls (466.23,202.4) and (465.18,201.36) .. (465.18,200.07) -- cycle ;
            	\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.34 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (452.93,200.07) .. controls (452.93,198.78) and (453.98,197.73) .. (455.27,197.73) .. controls (456.56,197.73) and (457.6,198.78) .. (457.6,200.07) .. controls (457.6,201.36) and (456.56,202.4) .. (455.27,202.4) .. controls (453.98,202.4) and (452.93,201.36) .. (452.93,200.07) -- cycle ;
            	\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.34 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (452.93,192.57) .. controls (452.93,191.28) and (453.98,190.23) .. (455.27,190.23) .. controls (456.56,190.23) and (457.6,191.28) .. (457.6,192.57) .. controls (457.6,193.86) and (456.56,194.9) .. (455.27,194.9) .. controls (453.98,194.9) and (452.93,193.86) .. (452.93,192.57) -- cycle ;
            	\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.34 ][line width=2.25]  (442.85,196.57) .. controls (442.85,186.4) and (451.1,178.15) .. (461.27,178.15) .. controls (471.44,178.15) and (479.68,186.4) .. (479.68,196.57) .. controls (479.68,206.74) and (471.44,214.98) .. (461.27,214.98) .. controls (451.1,214.98) and (442.85,206.74) .. (442.85,196.57) -- cycle ;
            	\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=0.75 ][line width=3]  (447.1,196.57) .. controls (447.1,188.74) and (453.44,182.4) .. (461.27,182.4) .. controls (469.09,182.4) and (475.43,188.74) .. (475.43,196.57) .. controls (475.43,204.39) and (469.09,210.73) .. (461.27,210.73) .. controls (453.44,210.73) and (447.1,204.39) .. (447.1,196.57) -- cycle ;
            	\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ] (458.52,176.32) -- (463.52,176.32) -- (463.52,216.32) -- (458.52,216.32) -- cycle ;
            	\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ] (476.94,183.96) -- (479.49,188.26) -- (445.09,208.67) -- (442.54,204.37) -- cycle ;
            	\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ] (442.6,188.12) -- (445.19,183.84) -- (479.43,204.52) -- (476.84,208.8) -- cycle ;
            	\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.45 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (456.35,196.32) .. controls (456.35,193.74) and (458.44,191.65) .. (461.02,191.65) .. controls (463.59,191.65) and (465.68,193.74) .. (465.68,196.32) .. controls (465.68,198.89) and (463.59,200.98) .. (461.02,200.98) .. controls (458.44,200.98) and (456.35,198.89) .. (456.35,196.32) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (413.27,187.73) .. controls (433.27,177.73) and (460.27,165.4) .. (440.27,185.4) .. controls (437.6,196.07) and (443.27,193.4) .. (475.27,189.73) .. controls (475.6,191.07) and (484.06,195.24) .. (482.27,197.4) .. controls (475.1,206.03) and (475.27,203.73) .. (428.07,213.44) .. controls (425.15,212.08) and (423.21,210.67) .. (422.63,209.28) .. controls (413.29,207.06) and (405.59,205.28) .. (401.27,204.73) .. controls (381.27,174.73) and (393.27,197.73) .. (413.27,187.73) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.23 ] (441.91,192.54) .. controls (447.67,193.68) and (459.07,191.58) .. (475.27,189.73) .. controls (475.6,191.07) and (484.06,195.24) .. (482.27,197.4) .. controls (475.1,206.03) and (486.8,201.36) .. (439.6,211.07) .. controls (436.68,209.71) and (435.27,208.4) .. (434.27,203.07) .. controls (437.27,187.73) and (446.23,193.08) .. (441.91,192.54) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (443.65,200.89) .. controls (443.39,199.62) and (444.21,198.39) .. (445.47,198.14) -- (472.2,192.75) .. controls (473.47,192.5) and (474.7,193.32) .. (474.95,194.58) -- (474.95,194.58) .. controls (475.21,195.84) and (474.39,197.07) .. (473.13,197.33) -- (446.4,202.71) .. controls (445.13,202.97) and (443.9,202.15) .. (443.65,200.89) -- cycle ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (445.47,199.14) -- (472.2,193.75) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.29 ]   (439.27,194.73) -- (475.27,189.73) ;
            	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (415,197.9) .. controls (415,194.13) and (418.06,191.07) .. (421.83,191.07) .. controls (425.61,191.07) and (428.67,194.13) .. (428.67,197.9) .. controls (428.67,201.67) and (425.61,204.73) .. (421.83,204.73) .. controls (418.06,204.73) and (415,201.67) .. (415,197.9) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.77 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.58 ] (417.33,197.9) .. controls (417.33,195.41) and (419.35,193.4) .. (421.83,193.4) .. controls (424.32,193.4) and (426.33,195.41) .. (426.33,197.9) .. controls (426.33,200.39) and (424.32,202.4) .. (421.83,202.4) .. controls (419.35,202.4) and (417.33,200.39) .. (417.33,197.9) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (488.15,171.73) -- (501.27,190.53) -- (495.97,190.06) -- (492.52,186.25) -- (488.61,183.87) -- (482.17,174.35) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.41 ] (489.99,175.06) -- (501.27,190.53) -- (496.2,188.87) -- (493.9,185.77) -- (486.77,176.49) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (462.63,154.37) .. controls (480.17,140.98) and (484.92,145.98) .. (491.92,154.98) .. controls (495.17,158.48) and (446.17,161.23) .. (462.63,154.37) -- cycle ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.43 ]   (483.67,147.73) -- (490.42,155.23) ;
            	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.43 ]   (490.42,155.23) -- (484.67,156.23) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (483.67,147.73) -- (478.17,147.23) ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (259.07,197.57) .. controls (259.07,181.92) and (271.75,169.23) .. (287.4,169.23) .. controls (303.05,169.23) and (315.73,181.92) .. (315.73,197.57) .. controls (315.73,213.21) and (303.05,225.9) .. (287.4,225.9) .. controls (271.75,225.9) and (259.07,213.21) .. (259.07,197.57) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.76 ] (266.07,197.57) .. controls (266.07,185.78) and (275.62,176.23) .. (287.4,176.23) .. controls (299.18,176.23) and (308.73,185.78) .. (308.73,197.57) .. controls (308.73,209.35) and (299.18,218.9) .. (287.4,218.9) .. controls (275.62,218.9) and (266.07,209.35) .. (266.07,197.57) -- cycle ;
            	\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.27 ][line width=2.25]  (263.4,197.57) .. controls (263.4,184.31) and (274.15,173.57) .. (287.4,173.57) .. controls (300.65,173.57) and (311.4,184.31) .. (311.4,197.57) .. controls (311.4,210.82) and (300.65,221.57) .. (287.4,221.57) .. controls (274.15,221.57) and (263.4,210.82) .. (263.4,197.57) -- cycle ;
            	\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ][line width=1.5]  (267.73,197.57) .. controls (267.73,186.71) and (276.54,177.9) .. (287.4,177.9) .. controls (298.26,177.9) and (307.07,186.71) .. (307.07,197.57) .. controls (307.07,208.43) and (298.26,217.23) .. (287.4,217.23) .. controls (276.54,217.23) and (267.73,208.43) .. (267.73,197.57) -- cycle ;
            	\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.34 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (283.1,197.57) .. controls (283.1,194.99) and (285.19,192.9) .. (287.77,192.9) .. controls (290.34,192.9) and (292.43,194.99) .. (292.43,197.57) .. controls (292.43,200.14) and (290.34,202.23) .. (287.77,202.23) .. controls (285.19,202.23) and (283.1,200.14) .. (283.1,197.57) -- cycle ;
            	\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.34 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (285.43,190.57) .. controls (285.43,189.28) and (286.48,188.23) .. (287.77,188.23) .. controls (289.06,188.23) and (290.1,189.28) .. (290.1,190.57) .. controls (290.1,191.86) and (289.06,192.9) .. (287.77,192.9) .. controls (286.48,192.9) and (285.43,191.86) .. (285.43,190.57) -- cycle ;
            	\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.34 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (285.43,204.57) .. controls (285.43,203.28) and (286.48,202.23) .. (287.77,202.23) .. controls (289.06,202.23) and (290.1,203.28) .. (290.1,204.57) .. controls (290.1,205.86) and (289.06,206.9) .. (287.77,206.9) .. controls (286.48,206.9) and (285.43,205.86) .. (285.43,204.57) -- cycle ;
            	\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.34 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (291.43,194.57) .. controls (291.43,193.28) and (292.48,192.23) .. (293.77,192.23) .. controls (295.06,192.23) and (296.1,193.28) .. (296.1,194.57) .. controls (296.1,195.86) and (295.06,196.9) .. (293.77,196.9) .. controls (292.48,196.9) and (291.43,195.86) .. (291.43,194.57) -- cycle ;
            	\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.34 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (291.68,201.07) .. controls (291.68,199.78) and (292.73,198.73) .. (294.02,198.73) .. controls (295.31,198.73) and (296.35,199.78) .. (296.35,201.07) .. controls (296.35,202.36) and (295.31,203.4) .. (294.02,203.4) .. controls (292.73,203.4) and (291.68,202.36) .. (291.68,201.07) -- cycle ;
            	\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.34 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (279.43,201.07) .. controls (279.43,199.78) and (280.48,198.73) .. (281.77,198.73) .. controls (283.06,198.73) and (284.1,199.78) .. (284.1,201.07) .. controls (284.1,202.36) and (283.06,203.4) .. (281.77,203.4) .. controls (280.48,203.4) and (279.43,202.36) .. (279.43,201.07) -- cycle ;
            	\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.34 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (279.43,193.57) .. controls (279.43,192.28) and (280.48,191.23) .. (281.77,191.23) .. controls (283.06,191.23) and (284.1,192.28) .. (284.1,193.57) .. controls (284.1,194.86) and (283.06,195.9) .. (281.77,195.9) .. controls (280.48,195.9) and (279.43,194.86) .. (279.43,193.57) -- cycle ;
            	\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.34 ][line width=2.25]  (269.35,197.57) .. controls (269.35,187.4) and (277.6,179.15) .. (287.77,179.15) .. controls (297.94,179.15) and (306.18,187.4) .. (306.18,197.57) .. controls (306.18,207.74) and (297.94,215.98) .. (287.77,215.98) .. controls (277.6,215.98) and (269.35,207.74) .. (269.35,197.57) -- cycle ;
            	\draw  [color={rgb, 255:red, 155; green, 155; blue, 155 }  ,draw opacity=0.75 ][line width=3]  (273.6,197.57) .. controls (273.6,189.74) and (279.94,183.4) .. (287.77,183.4) .. controls (295.59,183.4) and (301.93,189.74) .. (301.93,197.57) .. controls (301.93,205.39) and (295.59,211.73) .. (287.77,211.73) .. controls (279.94,211.73) and (273.6,205.39) .. (273.6,197.57) -- cycle ;
            	\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ] (285.02,177.32) -- (290.02,177.32) -- (290.02,217.32) -- (285.02,217.32) -- cycle ;
            	\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ] (303.44,184.96) -- (305.99,189.26) -- (271.59,209.67) -- (269.04,205.37) -- cycle ;
            	\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ] (269.1,189.12) -- (271.69,184.84) -- (305.93,205.52) -- (303.34,209.8) -- cycle ;
            	\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.45 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (282.85,197.32) .. controls (282.85,194.74) and (284.94,192.65) .. (287.52,192.65) .. controls (290.09,192.65) and (292.18,194.74) .. (292.18,197.32) .. controls (292.18,199.89) and (290.09,201.98) .. (287.52,201.98) .. controls (284.94,201.98) and (282.85,199.89) .. (282.85,197.32) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 182; blue, 35 }  ,fill opacity=1 ] (292.92,153.68) .. controls (312.92,143.68) and (312.92,171.18) .. (334.92,194.43) .. controls (329.97,191.2) and (315.84,190.57) .. (312.92,186.18) .. controls (289.67,154.43) and (259.88,180.78) .. (263.44,174.06) .. controls (268.36,164.78) and (281.31,159.48) .. (292.92,153.68) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.33 ] (296.92,154.68) .. controls (290.42,164.43) and (293.67,162.18) .. (291.67,166.68) .. controls (285.42,162.18) and (277.92,165.93) .. (269.21,172.85) .. controls (273.92,163.18) and (284.89,160.7) .. (296.92,154.68) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 182; blue, 35 }  ,fill opacity=1 ] (333.37,101.4) .. controls (340.7,106.07) and (344.7,103.07) .. (347.7,109.73) .. controls (349.7,110.73) and (340.07,122.44) .. (337.03,130.73) .. controls (333.98,139.09) and (331.03,138.73) .. (330.37,155.4) .. controls (330.09,158.56) and (334.39,175.87) .. (346.37,181.07) .. controls (357.6,185.93) and (376.3,178.83) .. (383.37,177.73) .. controls (384.32,177.59) and (389.98,170.71) .. (389.7,164.07) .. controls (389.47,158.59) and (383.17,153.27) .. (384.75,152.04) .. controls (388.24,149.34) and (391.77,146.63) .. (393.68,146.29) .. controls (410.7,143.26) and (430.36,139.45) .. (444.37,140.4) .. controls (450.08,140.79) and (465.09,138.57) .. (469.7,141.07) .. controls (482.64,148.07) and (490.89,159.19) .. (497.03,168.4) .. controls (500.04,172.91) and (461.37,184.4) .. (431.37,187.4) .. controls (426.37,189.73) and (422.37,187.73) .. (416.99,189.71) .. controls (412.89,197.39) and (405,204.08) .. (393.37,207.4) .. controls (388.98,208.65) and (371.46,201.94) .. (366.97,202.67) .. controls (358.99,203.98) and (351.07,204.42) .. (344.03,203.73) .. controls (331.9,202.56) and (324.37,197.07) .. (319.7,188.4) .. controls (314.38,180.42) and (309.18,168) .. (302.37,160.07) .. controls (296.37,153.09) and (293.37,156.41) .. (293.37,151.73) .. controls (293.37,146.73) and (299.53,138.15) .. (302.03,134.4) .. controls (304.53,130.65) and (328.37,103.9) .. (333.37,101.4) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.34 ] (340.7,105.07) .. controls (341.81,104.24) and (346.07,104.65) .. (343.7,109.73) .. controls (341.02,115.48) and (331.47,126.49) .. (329.37,135.07) .. controls (325.95,148.98) and (327.92,162.85) .. (332.7,171.73) .. controls (341.87,188.76) and (349.03,185.4) .. (375.37,182.73) .. controls (378.03,180.07) and (397.37,180.4) .. (390.37,153.73) .. controls (401.03,172.4) and (389.64,176.2) .. (387.7,181.73) .. controls (391.7,187.4) and (420.32,188.88) .. (415.67,190.31) .. controls (399.89,195.16) and (380.17,188.08) .. (378.17,189.58) .. controls (375.58,191.52) and (358.79,193.8) .. (354.37,195.73) .. controls (349.94,197.67) and (331.7,196.4) .. (319.7,171.73) .. controls (307.7,147.07) and (309.43,155.4) .. (311.7,145.73) .. controls (313.97,136.06) and (332.42,111.22) .. (340.7,105.07) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.44 ] (405.03,157.73) .. controls (418.7,145.73) and (455.7,135.07) .. (479.37,153.73) .. controls (464.37,144.4) and (399.37,145.73) .. (419.37,175.73) .. controls (404.03,174.73) and (399.7,163.07) .. (405.03,157.73) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.67 ] (304.17,141.29) .. controls (302.5,139.82) and (304.5,134.81) .. (308.64,130.1) .. controls (312.78,125.39) and (317.49,122.77) .. (319.16,124.24) .. controls (320.84,125.71) and (318.83,130.72) .. (314.7,135.43) .. controls (310.56,140.13) and (305.85,142.76) .. (304.17,141.29) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 230; green, 209; blue, 82 }  ,fill opacity=0.67 ] (310.3,135.78) .. controls (309.01,134.65) and (310.13,131.28) .. (312.79,128.24) .. controls (315.46,125.21) and (318.66,123.67) .. (319.95,124.8) .. controls (321.24,125.93) and (320.12,129.31) .. (317.46,132.34) .. controls (314.79,135.37) and (311.58,136.91) .. (310.3,135.78) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 247; green, 242; blue, 242 }  ,fill opacity=0.27 ] (329.97,111.4) .. controls (333.63,108.4) and (312.3,131.07) .. (300.63,153.07) .. controls (282.63,163.73) and (309.97,121.4) .. (329.97,111.4) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 244; green, 199; blue, 77 }  ,fill opacity=1 ] (343.7,109.73) .. controls (313.63,159.73) and (325.23,167.07) .. (339.97,193.4) .. controls (328.3,186.4) and (292.3,157.07) .. (343.7,109.73) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 240; green, 129; blue, 6 }  ,fill opacity=1 ] (324.63,163.73) .. controls (312.97,154.4) and (314.3,150.4) .. (322.3,138.07) .. controls (329.4,135) and (326.63,143.73) .. (324.97,150.4) .. controls (325.63,155.4) and (331.14,161.33) .. (324.63,163.73) -- cycle ;
            	\draw [color={rgb, 255:red, 245; green, 182; blue, 35 }  ,draw opacity=1 ]   (317.43,146.4) -- (325.63,146.4) ;
            	\draw [color={rgb, 255:red, 245; green, 182; blue, 35 }  ,draw opacity=1 ]   (316.77,152.4) -- (324.97,152.4) ;
            	\draw [color={rgb, 255:red, 245; green, 182; blue, 35 }  ,draw opacity=1 ]   (318.77,157.07) -- (326.97,157.07) ;
            	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=0.37 ]   (317.43,147.4) -- (324.72,147.4) ;
            	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=0.37 ]   (317.77,153.4) -- (325.05,153.4) ;
            	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=0.37 ]   (319.68,158.07) -- (326.97,158.07) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (382.35,136.15) .. controls (400.6,128.65) and (398.35,142.4) .. (428.1,127.15) .. controls (438.6,127.65) and (447.85,125.4) .. (453.35,128.9) .. controls (461.35,137.9) and (449.1,138.15) .. (450.6,142.15) .. controls (444.1,145.15) and (393.35,144.65) .. (385.85,152.65) .. controls (372.35,158.15) and (373.6,138.9) .. (382.35,136.15) -- cycle ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.31 ]   (384.4,152.6) .. controls (389.18,147.57) and (394.14,142.42) .. (400.85,139.9) .. controls (407.56,137.38) and (442.35,136.15) .. (456.1,132.15) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.44 ] (417.85,136.15) .. controls (422.6,133.9) and (426.35,132.15) .. (430.6,129.65) .. controls (441.35,129.15) and (443.6,128.9) .. (453.35,130.15) .. controls (447.6,134.15) and (438.6,132.9) .. (417.85,136.15) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.32 ] (381.6,152.65) .. controls (379.6,146.4) and (380.35,141.4) .. (384.6,138.9) .. controls (388.6,137.9) and (393.85,136.9) .. (401.1,137.9) .. controls (394.1,141.65) and (388.6,143.4) .. (381.6,152.65) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.38 ] (398.03,224.65) .. controls (398.03,223.33) and (419.4,222.25) .. (445.77,222.25) .. controls (472.14,222.25) and (493.52,223.33) .. (493.52,224.65) .. controls (493.52,225.98) and (472.14,227.05) .. (445.77,227.05) .. controls (419.4,227.05) and (398.03,225.98) .. (398.03,224.65) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.38 ] (260.43,225.65) .. controls (260.43,224.66) and (285.14,223.85) .. (315.63,223.85) .. controls (346.11,223.85) and (370.83,224.66) .. (370.83,225.65) .. controls (370.83,226.65) and (346.11,227.45) .. (315.63,227.45) .. controls (285.14,227.45) and (260.43,226.65) .. (260.43,225.65) -- cycle ;
            	\draw [color={rgb, 255:red, 144; green, 98; blue, 19 }  ,draw opacity=0.34 ]   (334.97,101.73) .. controls (339.97,99.33) and (344.72,103.23) .. (348.77,108.68) ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (360.55,94.97) -- (367.75,97.31) .. controls (368.59,97.58) and (368.97,98.72) .. (368.6,99.85) .. controls (368.23,100.99) and (367.25,101.69) .. (366.41,101.41) -- (359.21,99.07) .. controls (358.38,98.8) and (358,97.66) .. (358.36,96.53) .. controls (358.73,95.39) and (359.71,94.69) .. (360.55,94.97) .. controls (361.39,95.24) and (361.77,96.38) .. (361.4,97.51) .. controls (361.03,98.65) and (360.05,99.35) .. (359.21,99.07) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.79 ] (324.95,87.71) .. controls (326.25,86.92) and (328.8,88.75) .. (330.64,91.78) .. controls (332.48,94.82) and (332.92,97.92) .. (331.62,98.71) .. controls (330.32,99.5) and (327.78,97.67) .. (325.93,94.63) .. controls (324.09,91.6) and (323.65,88.5) .. (324.95,87.71) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (295.15,211.57) -- (296.07,210.93) -- (297.68,213.24) -- (296.77,213.88) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (467.9,210.81) -- (468.82,210.17) -- (470.43,212.48) -- (469.52,213.12) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.69 ] (284.4,197.32) .. controls (284.4,195.6) and (285.8,194.2) .. (287.52,194.2) .. controls (289.24,194.2) and (290.63,195.6) .. (290.63,197.32) .. controls (290.63,199.04) and (289.24,200.43) .. (287.52,200.43) .. controls (285.8,200.43) and (284.4,199.04) .. (284.4,197.32) -- cycle ;
            	\draw [color={rgb, 255:red, 144; green, 98; blue, 19 }  ,draw opacity=0.2 ]   (298.27,156.73) .. controls (303.27,154.33) and (315.65,182.95) .. (319.7,188.4) ;
            	\draw [color={rgb, 255:red, 149; green, 101; blue, 22 }  ,draw opacity=0.32 ]   (450.6,142.15) -- (465.6,142.15) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.29 ] (175.2,224.07) .. controls (175.2,222.26) and (192.36,220.8) .. (213.53,220.8) .. controls (234.7,220.8) and (251.87,222.26) .. (251.87,224.07) .. controls (251.87,225.87) and (234.7,227.33) .. (213.53,227.33) .. controls (192.36,227.33) and (175.2,225.87) .. (175.2,224.07) -- cycle ;
            	\draw    (450.27,137.13) .. controls (457.13,134.8) and (466.8,136.47) .. (465.6,142.15) ;
            \end{tikzpicture}'''

            # Câu hỏi (đã sửa % thành %%)
                noidungcauhoi = (r'''\immini{Một chiếc xe máy điện đang nạp pin, thời gian pin nạp được tính theo dung lượng pin nạp $Q$ (mAh) theo công thức như sau: $t=-\frac{2}{3}\ln \left(1-\frac{Q}{Q_0}\right)$, với $t$ là khoảng thời gian (đơn vị: giờ) tính từ lúc bắt đầu nạp từ lúc cạn sạch pin và $Q_0$ là dung lượng nạp tối đa. Số $\%%$ dung lượng pin của xe $\left(\frac{Q}{Q_0} \cdot 100\%%\right)$ bằng bao nhiêu khi đã nạp được thời gian $%s$ phút? (Kết quả làm tròn đến hàng phần chục). }{%s}'''
                                 %(T_min, hinhve))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (đã sửa % thành %%)
                loigiai = ('''Đổi $%s$ phút $= \\frac{%s}{60}$ giờ $= %s$ giờ. \\\\
                         Thay $t = %s$ vào công thức $t=-\\frac{2}{3}\\ln \\left(1-\\frac{Q}{Q_0}\\right)$, ta được: \\\\
                         $$ %s = -\\frac{2}{3}\\ln \\left(1-\\frac{Q}{Q_0}\\right) $$
                         $$ \\Leftrightarrow \\ln \\left(1-\\frac{Q}{Q_0}\\right) = %s \\cdot \\left( -\\frac{3}{2} \\right) $$
                         $$ \\Leftrightarrow \\ln \\left(1-\\frac{Q}{Q_0}\\right) = %s $$
                         $$ \\Leftrightarrow 1-\\frac{Q}{Q_0} = e^{%s} $$
                         $$ \\Leftrightarrow \\frac{Q}{Q_0} = 1 - e^{%s} $$
                         Số phần trăm dung lượng pin đã nạp được là: \\\\
                         $$ \\frac{Q}{Q_0} \\cdot 100\\%% = \\left( 1 - e^{%s} \\right) \\cdot 100\\%% \\approx %s\\%% .$$'''
                         %(T_min, T_min, latex(t_val),
                           latex(t_val),
                           latex(t_val),
                           latex(t_val),
                           latex(exponent),
                           latex(exponent),
                           latex(exponent),
                           latex(exponent),
                           kq_str))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(kq_str)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 


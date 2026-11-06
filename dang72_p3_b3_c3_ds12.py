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


def bt_dang72_p3_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random bán kính R (chọn số chẵn để quá trình chia 2 ra số đẹp)
                R = random.choice([10, 12, 14, 16, 18, 20])

                # Tính diện tích chính xác dựa trên công thức tổng quát đã chứng minh: 5*sqrt(3)*R^2 / 12
                exact_area = 5 * math.sqrt(3) * (R**2) / 12
                ans_correct = round(exact_area)

                # Hàm hỗ trợ định dạng phân số LaTeX
                def tex_frac(num, den):
                    f = frac(num, den)
                    if f.denominator == 1:
                        return str(f.numerator)
                    return "\\frac{%s}{%s}" % (f.numerator, f.denominator)

                # Các thông số tính toán điền vào lời giải
                R2 = R**2
                R_half = R // 2
                M_y_sq = 3 * R_half**2
                two_R = 2 * R
                five_R_4 = tex_frac(5 * R, 4)
                four_R_3 = tex_frac(4 * R, 3)
                eight_R2_3 = tex_frac(8 * R**2, 3)

                # Đoạn code TikZ vẽ hình Spinner và Lục giác (đã xóa các ký tự % gây lỗi)
                hinhve=r'''\begin{center}
            	\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            		\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.19 ] (106.53,231.2) .. controls (111.2,227.87) and (249.47,216.13) .. (241.33,226.67) .. controls (233.2,237.2) and (160.53,243.87) .. (136.53,245.2) .. controls (112.53,246.53) and (101.87,234.53) .. (106.53,231.2) -- cycle ;
            		\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ][line width=1]  (528.08,199.57) -- (449.52,244.92) -- (370.96,199.57) -- (370.96,108.86) -- (449.52,63.5) -- (528.08,108.86) -- cycle ;
            		\draw  [fill={rgb, 255:red, 213; green, 225; blue, 235 }  ,fill opacity=1 ][line width=1]  (392.53,122.27) .. controls (439.2,36.27) and (475.2,68.27) .. (505.2,119.6) .. controls (544.53,182.93) and (535.2,222.93) .. (449.52,219.41) .. controls (366.53,223.6) and (353.87,180.93) .. (392.53,122.27) -- cycle ;
            		\draw  [line width=1]  (384.32,154.21) .. controls (384.32,118.2) and (413.51,89.01) .. (449.52,89.01) .. controls (485.53,89.01) and (514.72,118.2) .. (514.72,154.21) .. controls (514.72,190.22) and (485.53,219.41) .. (449.52,219.41) .. controls (413.51,219.41) and (384.32,190.22) .. (384.32,154.21) -- cycle ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (449.52,154.21) -- (571.2,225.2) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (449.52,154.21) -- (333.2,219.87) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (449.52,154.21) -- (451.2,29.87) ;
            		\draw  [fill={rgb, 255:red, 155; green, 164; blue, 174 }  ,fill opacity=1 ] (137.88,93.96) .. controls (142.99,83.28) and (154.6,63.76) .. (185.28,61.87) .. controls (190.21,62.83) and (198.46,63.57) .. (204.78,65.16) .. controls (190.85,79.1) and (130.91,214.31) .. (144.85,235.22) .. controls (136.95,232.43) and (136.48,231.5) .. (123.94,225.92) .. controls (94.74,199.28) and (101.63,172.02) .. (117.9,138.57) .. controls (126.26,120.51) and (135.55,100) .. (137.88,93.96) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 218; green, 226; blue, 235 }  ,fill opacity=1 ] (163.43,67.02) .. controls (171.82,68.45) and (186.34,71.01) .. (191.31,75.84) .. controls (205.56,89.69) and (211.29,112.55) .. (140.2,92.11) .. controls (144.85,80.95) and (151.82,74.45) .. (163.43,67.02) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 104; green, 111; blue, 118 }  ,fill opacity=1 ] (104.28,176.02) .. controls (130.67,191.54) and (165.06,188.29) .. (151.12,202.23) .. controls (137.18,216.17) and (153.07,196.93) .. (167.01,217.84) .. controls (180.95,238.75) and (172.26,249.62) .. (123.94,225.92) .. controls (110.46,211.98) and (102.1,197.12) .. (104.28,176.02) -- cycle ;
            		\draw  [fill={rgb, 255:red, 218; green, 226; blue, 235 }  ,fill opacity=1 ] (160.64,89.78) .. controls (168.54,70.73) and (214.77,46.11) .. (236.15,88.39) .. controls (257.52,130.67) and (263.79,142.29) .. (268.67,157.16) .. controls (275.41,188.29) and (256.59,224.99) .. (216.63,231.5) .. controls (180.39,235.68) and (144.61,254.73) .. (128.35,214.77) .. controls (113.95,182.71) and (128.82,157.62) .. (141.36,131.14) .. controls (150.5,113.03) and (156.79,97.49) .. (160.64,89.78) -- cycle ;
            		\draw  [fill={rgb, 255:red, 104; green, 111; blue, 118 }  ,fill opacity=1 ] (155.53,134.39) .. controls (155.53,43.32) and (247.07,59.58) .. (238.7,125.1) .. controls (239.57,126.99) and (240.11,127.55) .. (240.79,128.91) .. controls (299.95,173.2) and (234.86,247.55) .. (201.42,217.94) .. controls (199.06,219.27) and (196.18,220.36) .. (193.92,221.43) .. controls (156.29,267.43) and (88.16,194.79) .. (152.89,138.66) .. controls (153.74,137.26) and (154.63,135.84) .. (155.53,134.39) -- cycle ;
            		\draw  [color={rgb, 255:red, 155; green, 164; blue, 174 }  ,draw opacity=1 ][line width=1]  (159.71,114.87) .. controls (159.71,92.55) and (175.73,74.45) .. (195.49,74.45) .. controls (215.25,74.45) and (231.27,92.55) .. (231.27,114.87) .. controls (231.27,137.2) and (215.25,155.3) .. (195.49,155.3) .. controls (175.73,155.3) and (159.71,137.2) .. (159.71,114.87) -- cycle ;
            		\draw  [color={rgb, 255:red, 155; green, 164; blue, 174 }  ,draw opacity=1 ][line width=1]  (162.97,114.87) .. controls (162.97,94.58) and (177.53,78.12) .. (195.49,78.12) .. controls (213.45,78.12) and (228.02,94.58) .. (228.02,114.87) .. controls (228.02,135.17) and (213.45,151.62) .. (195.49,151.62) .. controls (177.53,151.62) and (162.97,135.17) .. (162.97,114.87) -- cycle ;
            		\draw  [color={rgb, 255:red, 155; green, 164; blue, 174 }  ,draw opacity=1 ][line width=1]  (166.7,114.87) .. controls (166.7,96.91) and (179.59,82.35) .. (195.49,82.35) .. controls (211.39,82.35) and (224.28,96.91) .. (224.28,114.87) .. controls (224.28,132.84) and (211.39,147.4) .. (195.49,147.4) .. controls (179.59,147.4) and (166.7,132.84) .. (166.7,114.87) -- cycle ;
            		\draw  [color={rgb, 255:red, 155; green, 164; blue, 174 }  ,draw opacity=1 ][line width=1]  (170.87,114.87) .. controls (170.87,99.51) and (181.89,87.05) .. (195.49,87.05) .. controls (209.09,87.05) and (220.12,99.51) .. (220.12,114.87) .. controls (220.12,130.24) and (209.09,142.7) .. (195.49,142.7) .. controls (181.89,142.7) and (170.87,130.24) .. (170.87,114.87) -- cycle ;
            		\draw  [color={rgb, 255:red, 155; green, 164; blue, 174 }  ,draw opacity=1 ][line width=1]  (174.52,114.87) .. controls (174.52,101.79) and (183.91,91.18) .. (195.49,91.18) .. controls (207.07,91.18) and (216.46,101.79) .. (216.46,114.87) .. controls (216.46,127.96) and (207.07,138.57) .. (195.49,138.57) .. controls (183.91,138.57) and (174.52,127.96) .. (174.52,114.87) -- cycle ;
            		\draw  [color={rgb, 255:red, 155; green, 164; blue, 174 }  ,draw opacity=1 ][line width=1]  (178.22,114.87) .. controls (178.22,104.1) and (185.95,95.36) .. (195.49,95.36) .. controls (205.03,95.36) and (212.76,104.1) .. (212.76,114.87) .. controls (212.76,125.65) and (205.03,134.39) .. (195.49,134.39) .. controls (185.95,134.39) and (178.22,125.65) .. (178.22,114.87) -- cycle ;
            		\draw  [color={rgb, 255:red, 155; green, 164; blue, 174 }  ,draw opacity=1 ][line width=1]  (182.02,114.87) .. controls (182.02,106.46) and (188.05,99.65) .. (195.49,99.65) .. controls (202.93,99.65) and (208.97,106.46) .. (208.97,114.87) .. controls (208.97,123.28) and (202.93,130.1) .. (195.49,130.1) .. controls (188.05,130.1) and (182.02,123.28) .. (182.02,114.87) -- cycle ;
            		\draw  [color={rgb, 255:red, 155; green, 164; blue, 174 }  ,draw opacity=1 ][line width=1]  (185.73,114.87) .. controls (185.73,108.78) and (190.1,103.85) .. (195.49,103.85) .. controls (200.88,103.85) and (205.25,108.78) .. (205.25,114.87) .. controls (205.25,120.96) and (200.88,125.9) .. (195.49,125.9) .. controls (190.1,125.9) and (185.73,120.96) .. (185.73,114.87) -- cycle ;
            		\draw  [color={rgb, 255:red, 155; green, 164; blue, 174 }  ,draw opacity=1 ][line width=1]  (188.99,114.87) .. controls (188.99,110.81) and (191.9,107.52) .. (195.49,107.52) .. controls (199.08,107.52) and (202,110.81) .. (202,114.87) .. controls (202,118.93) and (199.08,122.22) .. (195.49,122.22) .. controls (191.9,122.22) and (188.99,118.93) .. (188.99,114.87) -- cycle ;
            		\draw  [color={rgb, 255:red, 155; green, 164; blue, 174 }  ,draw opacity=1 ][line width=1]  (191.38,114.87) .. controls (191.38,112.31) and (193.22,110.23) .. (195.49,110.23) .. controls (197.76,110.23) and (199.6,112.31) .. (199.6,114.87) .. controls (199.6,117.44) and (197.76,119.52) .. (195.49,119.52) .. controls (193.22,119.52) and (191.38,117.44) .. (191.38,114.87) -- cycle ;
            		\draw  [color={rgb, 255:red, 155; green, 164; blue, 174 }  ,draw opacity=1 ][line width=1]  (129.05,188.29) .. controls (129.05,165.96) and (145.07,147.86) .. (164.83,147.86) .. controls (184.58,147.86) and (200.6,165.96) .. (200.6,188.29) .. controls (200.6,210.61) and (184.58,228.71) .. (164.83,228.71) .. controls (145.07,228.71) and (129.05,210.61) .. (129.05,188.29) -- cycle ;
            		\draw  [color={rgb, 255:red, 155; green, 164; blue, 174 }  ,draw opacity=1 ][line width=1]  (132.3,188.29) .. controls (132.3,167.99) and (146.86,151.54) .. (164.83,151.54) .. controls (182.79,151.54) and (197.35,167.99) .. (197.35,188.29) .. controls (197.35,208.58) and (182.79,225.04) .. (164.83,225.04) .. controls (146.86,225.04) and (132.3,208.58) .. (132.3,188.29) -- cycle ;
            		\draw  [color={rgb, 255:red, 155; green, 164; blue, 174 }  ,draw opacity=1 ][line width=1]  (136.04,188.29) .. controls (136.04,170.32) and (148.93,155.76) .. (164.83,155.76) .. controls (180.72,155.76) and (193.61,170.32) .. (193.61,188.29) .. controls (193.61,206.25) and (180.72,220.81) .. (164.83,220.81) .. controls (148.93,220.81) and (136.04,206.25) .. (136.04,188.29) -- cycle ;
            		\draw  [color={rgb, 255:red, 155; green, 164; blue, 174 }  ,draw opacity=1 ][line width=1]  (140.2,188.29) .. controls (140.2,172.92) and (151.22,160.46) .. (164.83,160.46) .. controls (178.43,160.46) and (189.45,172.92) .. (189.45,188.29) .. controls (189.45,203.65) and (178.43,216.11) .. (164.83,216.11) .. controls (151.22,216.11) and (140.2,203.65) .. (140.2,188.29) -- cycle ;
            		\draw  [color={rgb, 255:red, 155; green, 164; blue, 174 }  ,draw opacity=1 ][line width=1]  (143.85,188.29) .. controls (143.85,175.2) and (153.24,164.59) .. (164.83,164.59) .. controls (176.41,164.59) and (185.8,175.2) .. (185.8,188.29) .. controls (185.8,201.37) and (176.41,211.98) .. (164.83,211.98) .. controls (153.24,211.98) and (143.85,201.37) .. (143.85,188.29) -- cycle ;
            		\draw  [color={rgb, 255:red, 155; green, 164; blue, 174 }  ,draw opacity=1 ][line width=1]  (147.55,188.29) .. controls (147.55,177.51) and (155.29,168.77) .. (164.83,168.77) .. controls (174.36,168.77) and (182.1,177.51) .. (182.1,188.29) .. controls (182.1,199.06) and (174.36,207.8) .. (164.83,207.8) .. controls (155.29,207.8) and (147.55,199.06) .. (147.55,188.29) -- cycle ;
            		\draw  [color={rgb, 255:red, 155; green, 164; blue, 174 }  ,draw opacity=1 ][line width=1]  (151.35,188.29) .. controls (151.35,179.88) and (157.38,173.06) .. (164.83,173.06) .. controls (172.27,173.06) and (178.3,179.88) .. (178.3,188.29) .. controls (178.3,196.7) and (172.27,203.51) .. (164.83,203.51) .. controls (157.38,203.51) and (151.35,196.7) .. (151.35,188.29) -- cycle ;
            		\draw  [color={rgb, 255:red, 155; green, 164; blue, 174 }  ,draw opacity=1 ][line width=1]  (155.07,188.29) .. controls (155.07,182.2) and (159.44,177.26) .. (164.83,177.26) .. controls (170.21,177.26) and (174.58,182.2) .. (174.58,188.29) .. controls (174.58,194.38) and (170.21,199.31) .. (164.83,199.31) .. controls (159.44,199.31) and (155.07,194.38) .. (155.07,188.29) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 164; blue, 174 }  ,fill opacity=1 ] (179.46,91.95) .. controls (179.46,84.04) and (185.44,77.62) .. (192.82,77.62) .. controls (200.2,77.62) and (206.18,84.04) .. (206.18,91.95) .. controls (206.18,99.86) and (200.2,106.28) .. (192.82,106.28) .. controls (185.44,106.28) and (179.46,99.86) .. (179.46,91.95) -- cycle ;
            		\draw  [fill={rgb, 255:red, 104; green, 111; blue, 118 }  ,fill opacity=1 ] (181.86,92.34) .. controls (181.86,85.71) and (186.79,80.33) .. (192.86,80.33) .. controls (198.93,80.33) and (203.86,85.71) .. (203.86,92.34) .. controls (203.86,98.97) and (198.93,104.34) .. (192.86,104.34) .. controls (186.79,104.34) and (181.86,98.97) .. (181.86,92.34) -- cycle ;
            		\draw  [fill={rgb, 255:red, 155; green, 164; blue, 174 }  ,fill opacity=1 ] (181.4,91.85) .. controls (181.4,85.81) and (185.82,80.92) .. (191.27,80.92) .. controls (196.72,80.92) and (201.14,85.81) .. (201.14,91.85) .. controls (201.14,97.9) and (196.72,102.79) .. (191.27,102.79) .. controls (185.82,102.79) and (181.4,97.9) .. (181.4,91.85) -- cycle ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (188.44,101.28) .. controls (179.07,100.86) and (180.62,76.85) .. (196.11,82.66) ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 164; blue, 174 }  ,fill opacity=1 ] (154.6,147.94) .. controls (154.6,140.03) and (160.58,133.61) .. (167.96,133.61) .. controls (175.34,133.61) and (181.32,140.03) .. (181.32,147.94) .. controls (181.32,155.85) and (175.34,162.27) .. (167.96,162.27) .. controls (160.58,162.27) and (154.6,155.85) .. (154.6,147.94) -- cycle ;
            		\draw  [fill={rgb, 255:red, 104; green, 111; blue, 118 }  ,fill opacity=1 ] (157,148.33) .. controls (157,141.7) and (161.93,136.32) .. (168,136.32) .. controls (174.07,136.32) and (179,141.7) .. (179,148.33) .. controls (179,154.96) and (174.07,160.33) .. (168,160.33) .. controls (161.93,160.33) and (157,154.96) .. (157,148.33) -- cycle ;
            		\draw  [fill={rgb, 255:red, 155; green, 164; blue, 174 }  ,fill opacity=1 ] (156.54,147.84) .. controls (156.54,141.8) and (160.96,136.91) .. (166.41,136.91) .. controls (171.87,136.91) and (176.29,141.8) .. (176.29,147.84) .. controls (176.29,153.88) and (171.87,158.78) .. (166.41,158.78) .. controls (160.96,158.78) and (156.54,153.88) .. (156.54,147.84) -- cycle ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (163.59,157.27) .. controls (154.22,156.85) and (155.76,132.84) .. (171.25,138.65) ;
            		\draw  [color={rgb, 255:red, 155; green, 164; blue, 174 }  ,draw opacity=1 ][line width=1]  (201.07,169.24) .. controls (201.07,150.5) and (214.9,135.32) .. (231.97,135.32) .. controls (249.03,135.32) and (262.86,150.5) .. (262.86,169.24) .. controls (262.86,187.97) and (249.03,203.16) .. (231.97,203.16) .. controls (214.9,203.16) and (201.07,187.97) .. (201.07,169.24) -- cycle ;
            		\draw  [color={rgb, 255:red, 155; green, 164; blue, 174 }  ,draw opacity=1 ][line width=1]  (203.88,169.24) .. controls (203.88,152.21) and (216.45,138.4) .. (231.97,138.4) .. controls (247.48,138.4) and (260.06,152.21) .. (260.06,169.24) .. controls (260.06,186.27) and (247.48,200.07) .. (231.97,200.07) .. controls (216.45,200.07) and (203.88,186.27) .. (203.88,169.24) -- cycle ;
            		\draw  [color={rgb, 255:red, 155; green, 164; blue, 174 }  ,draw opacity=1 ][line width=1]  (207.1,169.24) .. controls (207.1,154.16) and (218.24,141.95) .. (231.97,141.95) .. controls (245.7,141.95) and (256.83,154.16) .. (256.83,169.24) .. controls (256.83,184.31) and (245.7,196.53) .. (231.97,196.53) .. controls (218.24,196.53) and (207.1,184.31) .. (207.1,169.24) -- cycle ;
            		\draw  [color={rgb, 255:red, 155; green, 164; blue, 174 }  ,draw opacity=1 ][line width=1]  (210.7,169.24) .. controls (210.7,156.34) and (220.22,145.89) .. (231.97,145.89) .. controls (243.71,145.89) and (253.23,156.34) .. (253.23,169.24) .. controls (253.23,182.13) and (243.71,192.58) .. (231.97,192.58) .. controls (220.22,192.58) and (210.7,182.13) .. (210.7,169.24) -- cycle ;
            		\draw  [color={rgb, 255:red, 155; green, 164; blue, 174 }  ,draw opacity=1 ][line width=1]  (213.85,169.24) .. controls (213.85,158.26) and (221.96,149.35) .. (231.97,149.35) .. controls (241.97,149.35) and (250.08,158.26) .. (250.08,169.24) .. controls (250.08,180.22) and (241.97,189.12) .. (231.97,189.12) .. controls (221.96,189.12) and (213.85,180.22) .. (213.85,169.24) -- cycle ;
            		\draw  [color={rgb, 255:red, 155; green, 164; blue, 174 }  ,draw opacity=1 ][line width=1]  (217.05,169.24) .. controls (217.05,160.19) and (223.73,152.86) .. (231.97,152.86) .. controls (240.2,152.86) and (246.88,160.19) .. (246.88,169.24) .. controls (246.88,178.28) and (240.2,185.61) .. (231.97,185.61) .. controls (223.73,185.61) and (217.05,178.28) .. (217.05,169.24) -- cycle ;
            		\draw  [color={rgb, 255:red, 155; green, 164; blue, 174 }  ,draw opacity=1 ][line width=1]  (220.33,169.24) .. controls (220.33,162.18) and (225.54,156.46) .. (231.97,156.46) .. controls (238.39,156.46) and (243.6,162.18) .. (243.6,169.24) .. controls (243.6,176.29) and (238.39,182.01) .. (231.97,182.01) .. controls (225.54,182.01) and (220.33,176.29) .. (220.33,169.24) -- cycle ;
            		\draw  [color={rgb, 255:red, 155; green, 164; blue, 174 }  ,draw opacity=1 ][line width=1]  (223.54,169.24) .. controls (223.54,164.13) and (227.31,159.99) .. (231.97,159.99) .. controls (236.62,159.99) and (240.39,164.13) .. (240.39,169.24) .. controls (240.39,174.35) and (236.62,178.49) .. (231.97,178.49) .. controls (227.31,178.49) and (223.54,174.35) .. (223.54,169.24) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 164; blue, 174 }  ,fill opacity=1 ] (207.57,139.11) .. controls (207.57,131.2) and (213.55,124.79) .. (220.93,124.79) .. controls (228.31,124.79) and (234.29,131.2) .. (234.29,139.11) .. controls (234.29,147.02) and (228.31,153.44) .. (220.93,153.44) .. controls (213.55,153.44) and (207.57,147.02) .. (207.57,139.11) -- cycle ;
            		\draw  [fill={rgb, 255:red, 104; green, 111; blue, 118 }  ,fill opacity=1 ] (209.97,139.5) .. controls (209.97,132.87) and (214.9,127.5) .. (220.97,127.5) .. controls (227.04,127.5) and (231.97,132.87) .. (231.97,139.5) .. controls (231.97,146.13) and (227.04,151.5) .. (220.97,151.5) .. controls (214.9,151.5) and (209.97,146.13) .. (209.97,139.5) -- cycle ;
            		\draw  [fill={rgb, 255:red, 155; green, 164; blue, 174 }  ,fill opacity=1 ] (209.51,139.02) .. controls (209.51,132.97) and (213.93,128.08) .. (219.38,128.08) .. controls (224.83,128.08) and (229.26,132.97) .. (229.26,139.02) .. controls (229.26,145.06) and (224.83,149.95) .. (219.38,149.95) .. controls (213.93,149.95) and (209.51,145.06) .. (209.51,139.02) -- cycle ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (216.56,148.44) .. controls (207.18,148.02) and (208.73,124.01) .. (224.22,129.82) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (144.85,235.22) .. controls (129.48,222.25) and (121,199.58) .. (124.05,177.17) .. controls (127.1,154.76) and (142.28,130.96) .. (142.99,128.35) .. controls (143.7,125.74) and (149.96,117.66) .. (156,101.4) .. controls (162.04,85.14) and (169.94,72.59) .. (193.73,66.6) ;
            		\draw  [fill={rgb, 255:red, 155; green, 164; blue, 174 }  ,fill opacity=1 ] (207.11,144.7) .. controls (221.05,137.73) and (229.41,135.41) .. (247.62,143.5) .. controls (264.44,154.37) and (233.69,164.4) .. (247.62,185.31) .. controls (261.56,206.22) and (188.99,195.81) .. (166.68,225.55) .. controls (114.64,212.54) and (144.85,143.77) .. (169.48,146.19) .. controls (178.76,143.77) and (197.5,150.41) .. (207.11,144.7) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 104; green, 111; blue, 118 }  ,fill opacity=1 ] (166.68,225.55) .. controls (140.13,218.91) and (134.99,197.75) .. (139.6,178.94) .. controls (154.6,184.2) and (167.61,188.84) .. (178.76,192.1) .. controls (188.04,189.68) and (157.07,231.26) .. (166.68,225.55) -- cycle ;
            		\draw  [fill={rgb, 255:red, 218; green, 226; blue, 235 }  ,fill opacity=1 ] (218.94,147.15) .. controls (232.88,140.18) and (242.88,136.8) .. (252.17,145.06) .. controls (277.27,171.19) and (261.01,210.22) .. (241.01,217.54) .. controls (232.2,221.12) and (222.97,217.22) .. (215.47,216.26) .. controls (210.33,215.6) and (205.43,217.99) .. (204.3,218.45) .. controls (196.42,220.9) and (188.99,231.13) .. (179.22,229.62) .. controls (131.37,217.65) and (152.73,145.52) .. (181.32,148.64) .. controls (190.6,146.22) and (209.33,152.85) .. (218.94,147.15) -- cycle ;
            		\draw  [fill={rgb, 255:red, 104; green, 111; blue, 118 }  ,fill opacity=1 ] (158.92,184.43) .. controls (159.13,172.94) and (168.36,162.18) .. (179.53,160.4) -- (237.98,151.08) .. controls (249.15,149.3) and (258.03,157.17) .. (257.82,168.66) -- (257.54,183.66) .. controls (257.33,195.15) and (248.1,205.91) .. (236.93,207.69) -- (178.48,217.01) .. controls (167.31,218.79) and (158.43,210.92) .. (158.64,199.43) -- cycle ;
            		\draw  [fill={rgb, 255:red, 155; green, 164; blue, 174 }  ,fill opacity=1 ] (158.92,184.43) .. controls (159.13,172.94) and (168.36,162.18) .. (179.53,160.4) -- (233.38,151.81) .. controls (244.55,150.03) and (253.43,157.9) .. (253.22,169.39) -- (252.94,184.4) .. controls (252.73,195.89) and (243.5,206.64) .. (232.33,208.43) -- (178.48,217.01) .. controls (167.31,218.79) and (158.43,210.92) .. (158.64,199.43) -- cycle ;
            		\draw  [fill={rgb, 255:red, 155; green, 164; blue, 174 }  ,fill opacity=1 ] (160.27,185.23) .. controls (160.46,175.3) and (168.43,166) .. (178.08,164.46) -- (232.37,155.81) .. controls (242.02,154.27) and (249.7,161.07) .. (249.51,171) -- (249.27,183.97) .. controls (249.09,193.9) and (241.12,203.19) .. (231.46,204.73) -- (177.18,213.39) .. controls (167.52,214.93) and (159.85,208.13) .. (160.03,198.2) -- cycle ;
            		\draw  [fill={rgb, 255:red, 155; green, 164; blue, 174 }  ,fill opacity=1 ] (163.53,185.55) .. controls (163.69,176.9) and (170.63,168.81) .. (179.03,167.47) -- (231.3,159.13) .. controls (239.7,157.79) and (246.39,163.72) .. (246.23,172.36) -- (246.02,183.65) .. controls (245.86,192.29) and (238.92,200.39) .. (230.51,201.73) -- (178.24,210.06) .. controls (169.84,211.4) and (163.16,205.48) .. (163.32,196.84) -- cycle ;
            		\draw  [fill={rgb, 255:red, 155; green, 164; blue, 174 }  ,fill opacity=1 ] (167.23,185.84) .. controls (167.36,178.55) and (173.22,171.72) .. (180.31,170.59) -- (229.9,162.68) .. controls (236.99,161.55) and (242.63,166.55) .. (242.49,173.84) -- (242.32,183.36) .. controls (242.18,190.65) and (236.33,197.47) .. (229.24,198.6) -- (179.64,206.51) .. controls (172.55,207.64) and (166.92,202.65) .. (167.05,195.36) -- cycle ;
            		\draw  [fill={rgb, 255:red, 155; green, 164; blue, 174 }  ,fill opacity=1 ] (170.88,186.03) .. controls (171,179.93) and (175.9,174.21) .. (181.83,173.27) -- (228.27,165.86) .. controls (234.2,164.92) and (238.92,169.09) .. (238.81,175.2) -- (238.66,183.17) .. controls (238.55,189.27) and (233.65,194.98) .. (227.72,195.93) -- (181.27,203.33) .. controls (175.34,204.28) and (170.62,200.1) .. (170.74,194) -- cycle ;
            		\draw  [fill={rgb, 255:red, 155; green, 164; blue, 174 }  ,fill opacity=1 ] (173.22,186.42) .. controls (173.31,181.5) and (177.26,176.9) .. (182.04,176.13) -- (227.95,168.81) .. controls (232.73,168.05) and (236.54,171.42) .. (236.45,176.34) -- (236.33,182.77) .. controls (236.24,187.69) and (232.29,192.3) .. (227.5,193.06) -- (181.6,200.38) .. controls (176.81,201.14) and (173.01,197.77) .. (173.1,192.85) -- cycle ;
            		\draw  [fill={rgb, 255:red, 155; green, 164; blue, 174 }  ,fill opacity=1 ] (175.06,186.97) .. controls (175.13,183.33) and (178.05,179.93) .. (181.59,179.37) -- (228.29,171.92) .. controls (231.82,171.35) and (234.64,173.84) .. (234.57,177.48) -- (234.48,182.23) .. controls (234.41,185.86) and (231.49,189.27) .. (227.96,189.83) -- (181.25,197.28) .. controls (177.72,197.84) and (174.91,195.35) .. (174.98,191.72) -- cycle ;
            		\draw  [fill={rgb, 255:red, 200; green, 215; blue, 234 }  ,fill opacity=1 ] (177.58,187.23) .. controls (177.63,184.61) and (179.73,182.15) .. (182.28,181.75) -- (227.5,174.53) .. controls (230.05,174.13) and (232.08,175.92) .. (232.03,178.54) -- (231.97,181.97) .. controls (231.92,184.59) and (229.81,187.04) .. (227.26,187.45) -- (182.04,194.66) .. controls (179.49,195.07) and (177.47,193.27) .. (177.52,190.65) -- cycle ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (152.28,199.53) .. controls (151.82,167.47) and (163.43,145.17) .. (192.24,149.35) .. controls (209.9,151.21) and (200.07,151.58) .. (216.56,148.44) .. controls (230.8,142.38) and (235.45,139.13) .. (247.62,143.5) ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.36 ] (208.16,159.93) -- (211.59,161.07) -- (213.01,158.26) -- (215.83,160.49) -- (218.25,158.64) -- (219.6,160.69) -- (222.87,159.61) -- (224.06,162.31) -- (226.96,161.72) -- (228.14,164.46) -- (230.57,164.22) -- (230.7,167.07) -- (233.34,167.93) -- (232.97,170.96) -- (235.34,172.33) -- (234.35,175.44) -- (236.2,177.24) -- (234.72,179.84) -- (236.12,182.01) -- (234.31,184.21) -- (235.38,186.7) -- (233.19,188.63) -- (233.45,191.87) -- (231.3,192.68) -- (230.96,196.09) -- (228.31,196.4) -- (228.15,199.41) -- (225.71,199.41) -- (224.43,202.67) -- (221.72,201.95) -- (219.56,204.59) -- (217.95,203.6) -- (215.33,206.01) -- (213.45,204.09) -- (211,206.13) -- (209.34,203.3) -- (206.28,204.87) -- (205.47,201.83) -- (201.64,202.99) -- (201.08,199.46) -- (197.56,199.54) -- (198.29,196.18) -- (194.85,195.26) -- (196.07,191.91) -- (192.79,190.41) -- (195.16,187.38) -- (192.43,185.15) -- (195.47,183) -- (192.01,179.89) -- (195.91,177.96) -- (193.95,174.44) -- (197.35,173.45) -- (196.42,169.84) -- (199.94,169.25) -- (199.89,165.37) -- (203.08,165.51) -- (204.14,162.18) -- (207.55,162.54) -- cycle ;
            		\draw  [fill={rgb, 255:red, 155; green, 164; blue, 174 }  ,fill opacity=1 ] (213.82,159.54) -- (217.59,160.72) -- (219.14,157.79) -- (222.25,160.12) -- (224.9,158.18) -- (226.39,160.33) -- (229.97,159.2) -- (231.28,162.02) -- (234.47,161.4) -- (235.76,164.26) -- (238.43,164.01) -- (238.57,166.98) -- (241.48,167.89) -- (241.07,171.04) -- (243.67,172.48) -- (242.59,175.72) -- (244.62,177.59) -- (242.99,180.31) -- (244.52,182.58) -- (242.54,184.87) -- (243.71,187.47) -- (241.31,189.48) -- (241.59,192.87) -- (239.24,193.71) -- (238.86,197.26) -- (235.95,197.59) -- (235.78,200.73) -- (233.09,200.72) -- (231.69,204.13) -- (228.72,203.38) -- (226.34,206.14) -- (224.57,205.1) -- (221.69,207.62) -- (219.64,205.61) -- (216.94,207.74) -- (215.12,204.79) -- (211.76,206.43) -- (210.87,203.25) -- (206.66,204.46) -- (206.05,200.78) -- (202.18,200.87) -- (202.98,197.35) -- (199.2,196.39) -- (200.55,192.91) -- (196.95,191.34) -- (199.55,188.18) -- (196.54,185.85) -- (199.88,183.61) -- (196.09,180.36) -- (200.37,178.35) -- (198.22,174.67) -- (201.96,173.64) -- (200.93,169.88) -- (204.8,169.25) -- (204.74,165.21) -- (208.24,165.36) -- (209.41,161.88) -- (213.16,162.26) -- cycle ;
            		\draw  [fill={rgb, 255:red, 218; green, 226; blue, 235 }  ,fill opacity=1 ] (218.34,161.16) -- (221.8,162.31) -- (223.22,159.46) -- (226.07,161.73) -- (228.5,159.85) -- (229.87,161.93) -- (233.16,160.83) -- (234.36,163.57) -- (237.28,162.97) -- (238.47,165.75) -- (240.92,165.51) -- (241.05,168.39) -- (243.71,169.27) -- (243.34,172.33) -- (245.73,173.73) -- (244.73,176.88) -- (246.59,178.7) -- (245.1,181.33) -- (246.51,183.54) -- (244.69,185.76) -- (245.76,188.29) -- (243.56,190.23) -- (243.82,193.53) -- (241.66,194.35) -- (241.31,197.8) -- (238.64,198.12) -- (238.48,201.16) -- (236.02,201.16) -- (234.73,204.47) -- (232.01,203.73) -- (229.83,206.41) -- (228.2,205.41) -- (225.56,207.86) -- (223.67,205.91) -- (221.2,207.97) -- (219.53,205.11) -- (216.45,206.7) -- (215.63,203.61) -- (211.77,204.79) -- (211.21,201.21) -- (207.65,201.3) -- (208.39,197.89) -- (204.92,196.95) -- (206.16,193.57) -- (202.86,192.04) -- (205.25,188.98) -- (202.49,186.71) -- (205.55,184.54) -- (202.07,181.39) -- (205.99,179.43) -- (204.03,175.86) -- (207.45,174.86) -- (206.51,171.2) -- (210.06,170.6) -- (210,166.67) -- (213.22,166.81) -- (214.29,163.44) -- (217.73,163.8) -- cycle ;
            		\draw    (201.14,169.92) -- (207.1,171.32) ;
            		\draw    (205.11,165.26) -- (211.08,166.65) ;
            		\draw    (198.31,174.71) -- (204.28,176.11) ;
            		\draw    (200.63,178.22) -- (206.6,179.62) ;
            		\draw    (202.21,173.68) -- (208.18,175.08) ;
            		\draw    (205.17,169.29) -- (210.6,170.7) ;
            		\draw    (208.76,165.4) -- (213.71,166.88) ;
            		\draw    (209.98,161.93) -- (214.77,163.48) ;
            		\draw    (200.19,183.38) -- (206.16,184.77) ;
            		\draw    (199.7,188.2) -- (205.67,189.6) ;
            		\draw    (197.54,190.95) -- (203.51,192.35) ;
            		\draw    (200.74,192.92) -- (206.7,194.32) ;
            		\draw    (199.57,195.91) -- (205.54,197.31) ;
            		\draw    (202.44,200.87) -- (208.41,202.27) ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 164; blue, 174 }  ,fill opacity=1 ] (213.22,166.81) -- (214.29,163.44) -- (224.81,183.97) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 164; blue, 174 }  ,fill opacity=1 ] (210.6,170.7) -- (210,166.67) -- (224.81,183.97) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 164; blue, 174 }  ,fill opacity=1 ] (207.45,174.86) -- (207.1,171.32) -- (223.56,182.69) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 164; blue, 174 }  ,fill opacity=1 ] (206.6,179.62) -- (204.28,176.11) -- (224.81,183.97) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 164; blue, 174 }  ,fill opacity=1 ] (206.16,184.77) -- (202.07,181.39) -- (224.81,183.97) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 164; blue, 174 }  ,fill opacity=1 ] (205.25,188.98) -- (203.14,186.97) -- (224.81,183.97) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 164; blue, 174 }  ,fill opacity=1 ] (206.16,193.57) -- (203.51,192.35) -- (224.26,183.86) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 164; blue, 174 }  ,fill opacity=1 ] (208.39,197.89) -- (205.54,197.31) -- (224.81,183.97) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 164; blue, 174 }  ,fill opacity=1 ] (207.65,201.3) -- (223.9,184.04) -- (211.21,201.21) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 164; blue, 174 }  ,fill opacity=1 ] (211.77,204.79) -- (224.81,183.97) -- (215.63,203.61) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 164; blue, 174 }  ,fill opacity=1 ] (216.45,206.7) -- (223.9,184.04) -- (219.53,205.11) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 164; blue, 174 }  ,fill opacity=1 ] (221.2,207.97) -- (223.9,184.04) -- (223.67,205.91) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 164; blue, 174 }  ,fill opacity=1 ] (225.56,207.86) -- (224.81,183.97) -- (228.2,205.41) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 164; blue, 174 }  ,fill opacity=1 ] (229.83,206.41) -- (224.26,183.86) -- (232.01,203.73) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 164; blue, 174 }  ,fill opacity=1 ] (234.73,204.47) -- (224.26,183.86) -- (236.02,201.16) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 164; blue, 174 }  ,fill opacity=1 ] (238.64,198.12) -- (224.81,183.97) -- (238.48,201.16) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 164; blue, 174 }  ,fill opacity=1 ] (241.31,197.8) -- (224.81,183.97) -- (241.66,194.35) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 164; blue, 174 }  ,fill opacity=1 ] (243.82,193.53) -- (224.81,183.97) -- (243.56,190.23) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 164; blue, 174 }  ,fill opacity=1 ] (244.69,185.76) -- (224.81,183.97) -- (245.76,188.29) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 164; blue, 174 }  ,fill opacity=1 ] (246.51,183.54) -- (224.23,183.34) -- (245.1,181.33) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 164; blue, 174 }  ,fill opacity=1 ] (246.59,178.7) -- (224.18,183.44) -- (244.73,176.88) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 164; blue, 174 }  ,fill opacity=1 ] (245.73,173.73) -- (224.44,183.12) -- (243.67,172.48) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 164; blue, 174 }  ,fill opacity=1 ] (243.71,169.27) -- (224.44,183.12) -- (241.05,168.39) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 164; blue, 174 }  ,fill opacity=1 ] (240.92,165.51) -- (224.44,183.12) -- (238.47,165.75) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 164; blue, 174 }  ,fill opacity=1 ] (237.28,162.97) -- (224.26,183.86) -- (234.36,163.57) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 164; blue, 174 }  ,fill opacity=1 ] (233.16,160.83) -- (224.18,183.44) -- (229.87,161.93) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 164; blue, 174 }  ,fill opacity=1 ] (228.5,159.85) -- (223.9,184.04) -- (226.07,161.73) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 164; blue, 174 }  ,fill opacity=1 ] (223.22,159.46) -- (224.8,182.97) -- (222.16,162.17) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 164; blue, 174 }  ,fill opacity=1 ] (219.6,160.69) -- (224.8,182.97) -- (217.73,163.8) -- cycle ;
            		\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ][fill={rgb, 255:red, 218; green, 226; blue, 235 }  ,fill opacity=1 ] (218.26,183.97) .. controls (218.26,178.55) and (221.64,174.15) .. (225.81,174.15) .. controls (229.98,174.15) and (233.36,178.55) .. (233.36,183.97) .. controls (233.36,189.38) and (229.98,193.78) .. (225.81,193.78) .. controls (221.64,193.78) and (218.26,189.38) .. (218.26,183.97) -- cycle ;
            		\draw (546.67,222.67) node [anchor=north west][inner sep=0.75pt]    {$d_{3}$};
            		\draw (333.2,219.87) node [anchor=north west][inner sep=0.75pt]    {$d_{2}$};
            		\draw (428.67,23.67) node [anchor=north west][inner sep=0.75pt]    {$d_{1}$};
            	\end{tikzpicture}
            \end{center}'''

                # Câu hỏi
                noidungcauhoi = (r'''Để thiết kế một chiếc khuôn con quay Fidget Spinner từ một miếng nhựa hình lục giác tâm $O$, người ta vẽ một đường tròn tâm $O$ trên tấm nhựa bán kính bằng $%s$ cm cùng với ba đường thẳng $d_1, d_2, d_3$ cùng đi qua tâm sao cho chia đường tròn thành ba phần bằng nhau. Tiếp đến dựng ba parabol có trục trùng với $d_1, d_2, d_3$ và tiếp xúc với hai bên của cạnh lục giác trên sao cho mỗi hai giao điểm của parabol cắt đường tròn cũng trùng với giao điểm kia của parabol với đường tròn đã cho (gọi là điểm đặc biệt). %s Biết rằng điểm đặc biệt này là tiếp điểm chung của đường tròn và hai đường cong parabol tương ứng. Khi đó, diện tích của phần còn lại của lục giác đều cần phải cắt bỏ (phần màu xanh) là bao nhiêu $\text{cm}^2$? (Kết quả làm tròn đến hàng đơn vị).''' % (R, hinhve))

                # Đáp án đúng
                da = str(ans_correct)

                # Tập hợp các đáp án nhiễu
                distractors = set()
                distractors.add(round(5 * math.sqrt(3) * ((R-2)**2) / 12)) 
                distractors.add(round(5 * math.sqrt(3) * ((R+2)**2) / 12)) 
                distractors.add(ans_correct + random.choice([5, 10, 15]))   
                distractors.add(ans_correct - random.choice([4, 8, 12]))    
                distractors.discard(ans_correct)

                wrong_choices = random.sample(list(distractors), 3)

                # Gắn đáp án
                da_d = ('\\True $%s$' % da)
                da_s1 = '$%s$' % wrong_choices[0]
                da_s2 = '$%s$' % wrong_choices[1] 
                da_s3 = '$%s$' % wrong_choices[2] 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai = ('''\\begin{center}
                	\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
                		\\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ][line width=1]  (548.53,158.53) .. controls (511.64,91.6) and (474.76,91.6) .. (437.87,158.53) ;
                		\\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ][line width=1]  (292.74,197.57) -- (214.19,242.92) -- (135.63,197.57) -- (135.63,106.86) -- (214.19,61.5) -- (292.74,106.86) -- cycle ;
                		\\draw  [fill={rgb, 255:red, 213; green, 225; blue, 235 }  ,fill opacity=1 ][line width=1]  (157.2,120.27) .. controls (203.87,34.27) and (239.87,66.27) .. (269.87,117.6) .. controls (309.2,180.93) and (299.87,220.93) .. (214.19,217.41) .. controls (131.2,221.6) and (118.53,178.93) .. (157.2,120.27) -- cycle ;
                		\\draw  [line width=1]  (148.98,152.21) .. controls (148.98,116.2) and (178.18,87.01) .. (214.19,87.01) .. controls (250.2,87.01) and (279.39,116.2) .. (279.39,152.21) .. controls (279.39,188.22) and (250.2,217.41) .. (214.19,217.41) .. controls (178.18,217.41) and (148.98,188.22) .. (148.98,152.21) -- cycle ;
                		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (214.19,152.21) -- (335.87,223.2) ;
                		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (214.19,152.21) -- (97.87,217.87) ;
                		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (214.19,152.21) -- (215.87,27.87) ;
                		\\draw [line width=1]    (388.53,195.2) -- (608.53,194.55) ;
                		\\draw [shift={(612.53,194.53)}, rotate = 179.83] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (13.4,-6.43) -- (0,0) -- (13.4,6.44) -- (8.9,0) -- cycle    ;
                		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=1]  (427.67,195.17) .. controls (427.66,194.63) and (427.65,194.09) .. (427.65,193.54) .. controls (427.65,157.53) and (456.84,128.34) .. (492.85,128.34) .. controls (528.86,128.34) and (558.05,157.53) .. (558.05,193.54) .. controls (558.05,193.87) and (558.05,194.2) .. (558.05,194.52) -- (492.85,193.54) -- cycle ; \\draw  [line width=1]  (427.67,195.17) .. controls (427.66,194.63) and (427.65,194.09) .. (427.65,193.54) .. controls (427.65,157.53) and (456.84,128.34) .. (492.85,128.34) .. controls (528.86,128.34) and (558.05,157.53) .. (558.05,193.54) .. controls (558.05,193.87) and (558.05,194.2) .. (558.05,194.52) ;  
                		\\draw  [line width=1]  (579.2,228.53) .. controls (521.87,68.27) and (464.53,68.27) .. (407.2,228.53) ;
                		\\draw [line width=1]    (442.53,226.53) -- (586.53,134.53) ;
                		\\draw [line width=1]    (588.53,225.2) -- (483.87,51.2) ;
                		\\draw [line width=1]    (492.2,231.87) -- (492.53,28.53) ;
                		\\draw [shift={(492.53,24.53)}, rotate = 90.09] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (13.4,-6.43) -- (0,0) -- (13.4,6.44) -- (8.9,0) -- cycle    ;
                		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (512.67,114.33) -- (513.87,195.2) ;
                		\\draw [line width=1]    (604.53,173.2) -- (429.2,59.87) ;
                		\\draw (473.33,25) node [anchor=north west][inner sep=0.75pt]    {$y$};
                		\\draw (471.87,175) node [anchor=north west][inner sep=0.75pt]    {$O$};
                		\\draw (600.67,200) node [anchor=north west][inner sep=0.75pt]    {$x$};
                		\\draw (425.87,216.53) node [anchor=north west][inner sep=0.75pt]    {$d$};
                		\\draw (587.2,220.53) node [anchor=north west][inner sep=0.75pt]    {$d'$};
                		\\draw (379.87,208.53) node [anchor=north west][inner sep=0.75pt]    {$(P)$};
                		\\draw (505.2,199) node [anchor=north west][inner sep=0.75pt]    {$m$};
                		\\draw (417.2,60.53) node [anchor=north west][inner sep=0.75pt]    {$\\Delta $};
                		\\draw (491.2,83.2) node [anchor=north west][inner sep=0.75pt]    {$E$};
                		\\draw (430.53,158.53) node [anchor=north west][inner sep=0.75pt]    {$( C)$};
                		\\draw (436.53,104.53) node [anchor=north west][inner sep=0.75pt]    {$S_{0}$};
                		\\draw (311.33,220.67) node [anchor=north west][inner sep=0.75pt]    {$d_{3}$};
                		\\draw (97.87,217.87) node [anchor=north west][inner sep=0.75pt]    {$d_{2}$};
                		\\draw (193.33,21.67) node [anchor=north west][inner sep=0.75pt]    {$d_{1}$};
                	\\end{tikzpicture}
                \\end{center} Gọi $d$ là đường thẳng đi qua $O$ và cắt $(C): y = \\sqrt{%s - x^2}$ tại điểm đặc biệt $M$. \\\\
            Khi ấy $k_d = \\tan 30^\\circ \\Rightarrow d: y = \\frac{x}{\\sqrt{3}}$ với ta có phương trình hoành độ điểm $M$ là: $\\left(\\frac{x}{\\sqrt{3}}\\right)^2 + x^2 = %s$. \\\\
            Suy ra tọa độ $M\\left(%s\\sqrt{3}; %s\\right)$ gọi parabol đề cho có phương trình $(P): y = -ax^2 + c, (a>0)$. \\\\
            Do $M\\left(%s\\sqrt{3}; %s\\right) \\in (P)$ nên ta có phương trình: $%s = -%sa + c \\Rightarrow (P): y = -ax^2 + %s + %sa$. \\\\
            Gọi $d'$ là pháp tuyến của $d$ tại $M$ thì dễ dàng có được $d': y = -x\\sqrt{3} + %s$. \\\\
            Khi đó với $d'$ là tiếp tuyến của $(P)$ tại tiếp điểm $M$ ta có phương trình tiếp xúc như sau: \\\\
            $\\begin{cases} -ax^2 + c = -\\sqrt{3}x + %s \\\\ -2ax = -\\sqrt{3} \\end{cases}$. \\\\
            Suy ra: $a = \\frac{1}{%s} \\Rightarrow (P): y = -\\frac{1}{%s}x^2 + %s$. \\\\
            Tiếp đến gọi $\\Delta$ là tiếp tuyến của $(P)$ tại tiếp điểm $x=m$ sao cho $(\\Delta; Oy) = 60^\\circ$. \\\\
            Hệ số góc: $k_\\Delta = \\tan 150^\\circ = -\\frac{1}{\\sqrt{3}}$. \\\\
            Suy ra: $-\\frac{2m}{%s} = -\\frac{1}{\\sqrt{3}} \\Rightarrow m = \\frac{%s}{\\sqrt{3}} \\Rightarrow \\Delta \\cap Oy = E\\left(0; %s\\right) \\Rightarrow OE = %s \\ (\\text{cm})$. \\\\
            $\\Rightarrow S_{\\text{lục giác}} = 6 \\cdot \\frac{OE^2\\sqrt{3}}{4} = %s\\sqrt{3} \\ (\\text{cm}^2)$. \\\\
            Gọi $S_0$ là diện tích hình giới hạn bởi cong $(P)$ và $(C)$, vậy diện tích cần tìm là: \\\\
            $S = S_{\\text{lục giác}} - (3S_0 + S_{\\text{tròn}}) = %s\\sqrt{3} - \\left[ 3 \\int\\limits_{-%s\\sqrt{3}}^{%s\\sqrt{3}} \\left( -\\frac{1}{%s}x^2 + %s \\right) - \\sqrt{%s - x^2} \\mathrm{d}x + \\pi \\cdot %s^2 \\right] \\approx %s \\ (\\text{cm}^2)$.'''
                % (R2, R2, R_half, R_half, R_half, R_half, R_half, M_y_sq, R_half, M_y_sq, two_R, two_R, R, R, five_R_4, R, R_half, four_R_3, four_R_3, eight_R2_3, eight_R2_3, R_half, R_half, R, five_R_4, R2, R, ans_correct))
                dapan='\\shortans[0]{$%s$}\n'%(ans_correct)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) +dapan+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content


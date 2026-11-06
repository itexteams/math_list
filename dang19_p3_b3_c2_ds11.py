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


def bt_dang19_p3_b3_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random các thông số của bài toán
                a = random.choice([30, 40, 50, 60]) # Kích thước cạnh viên gạch (cm)
                n = random.choice([4, 5, 6, 7]) # Số tầng tháp
                p = random.choice([40, 50, 60, 75, 80]) # Tỉ lệ %
                S1 = random.choice([40, 45, 50, 60, 80]) # Diện tích mặt đáy (m2)

                # Tính toán chính xác phân số của tỉ lệ phần trăm
                r_frac = Rational(p, 100)
                tu = r_frac.p # Tử số
                mau = r_frac.q # Mẫu số

                # Tính tổng diện tích (m2)
                S_total_expr = S1 * (1 - r_frac**n) / (1 - r_frac)
                S_total_float = float(S_total_expr)

                # Tính diện tích 1 viên gạch (m2)
                a_m = a / 100
                S_tile_m2 = a_m**2

                # Số viên gạch tối thiểu cần dùng
                num_tiles = S_total_float / S_tile_m2
                num_tiles_final = math.ceil(num_tiles)

                # Xử lý chuỗi số thập phân để hiển thị đúng chuẩn VN (dùng dấu phẩy)
                s_total_dec = Decimal(str(S_total_float)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)
                s_total_str = str(s_total_dec).replace('.', ',')
                # Xóa các số 0 thừa ở đuôi phần thập phân
                if s_total_str.endswith(',000'):
                    s_total_str = s_total_str[:-4]
                elif s_total_str.endswith('00'):
                    s_total_str = s_total_str[:-2]
                elif s_total_str.endswith('0'):
                    s_total_str = s_total_str[:-1]

                a_m_str = str(a_m).replace('.', ',')

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (num_tiles_final)]
                da = du[0]
                s_options = set([
                    '$%s$' % (num_tiles_final + 1),
                    '$%s$' % (num_tiles_final + 2),
                    '$%s$' % (num_tiles_final + 3),
                    '$%s$' % (num_tiles_final - 1),
                    '$%s$' % (num_tiles_final - 2),
                    '$%s$' % (num_tiles_final - 3),
                    '$%s$' % (math.floor(num_tiles))
                ])
                # Đảm bảo không trùng với đáp án đúng
                if da in s_options:
                    s_options.remove(da)
                s = list(s_options)

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                hinhve=r'''\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-0.8,xscale=0.8]
                	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.32 ] (301.3,185.3) -- (197.61,274.26) -- (105.37,241.73) -- (177.8,203.8) -- (278.3,181.8) -- (296.3,179.3) -- cycle ;
                	\draw  [fill={rgb, 255:red, 208; green, 78; blue, 2 }  ,fill opacity=1 ] (245.8,212.29) -- (197.61,274.26) -- (105.37,241.73) -- (158.95,185.95) -- cycle ;
                	\draw  [fill={rgb, 255:red, 179; green, 78; blue, 19 }  ,fill opacity=1 ] (197.61,274.26) -- (197.47,279.3) -- (105.72,247.93) -- (105.37,241.73) -- cycle ;
                	\draw  [fill={rgb, 255:red, 179; green, 78; blue, 19 }  ,fill opacity=1 ] (245.8,212.29) -- (244.75,217.33) -- (197.47,279.3) -- (197.61,274.26) -- cycle ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (132.16,213.84) -- (221.71,243.28) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (119.2,228.95) -- (208.75,258.38) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (145.47,197.96) -- (235.01,227.4) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (153.7,190.99) -- (240.97,219.26) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (140.04,205.71) -- (226.61,234.37) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (124.28,221.2) -- (214,250.25) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (112.37,234.76) -- (202.09,266.13) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (151.49,258) -- (200.62,198.35) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (174.6,265.74) -- (223.74,206.1) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (128.03,250.25) -- (177.86,191.76) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (185.81,270) -- (234.94,209.58) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (117.17,245.6) -- (166.3,188.67) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (140.98,252.57) -- (188.72,195.25) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (163.4,261.1) -- (211.48,201.45) ;
                	\draw  [fill={rgb, 255:red, 111; green, 96; blue, 68 }  ,fill opacity=1 ] (217.29,206.87) -- (228.31,206.88) -- (223.74,226.74) -- (221.76,229.83) -- (217.29,228.34) -- cycle ;
                	\draw  [fill={rgb, 255:red, 174; green, 151; blue, 110 }  ,fill opacity=1 ] (151.1,215.27) -- (150.33,242.4) -- (148.34,245.49) -- (130.02,210.7) -- cycle ;
                	\draw  [fill={rgb, 255:red, 240; green, 207; blue, 147 }  ,fill opacity=1 ] (148.21,226.83) .. controls (148.89,218.07) and (161.98,218.83) .. (164.39,233.68) .. controls (163.82,244.72) and (164.33,239.01) .. (164.39,251.2) .. controls (177.28,254.97) and (187.39,258.26) .. (195.14,261.08) .. controls (195.03,249.29) and (195.37,236.73) .. (194.7,227.15) .. controls (127.89,206.27) and (144.42,210.46) .. (120.15,203.47) .. controls (119.98,214.26) and (120.32,224.54) .. (121.35,236.73) .. controls (128.72,238.32) and (137.01,242.85) .. (148.34,245.49) .. controls (147.55,237.87) and (147.55,233.3) .. (148.21,226.83) -- cycle ;
                	\draw  [fill={rgb, 255:red, 140; green, 117; blue, 78 }  ,fill opacity=1 ] (195.56,226.77) .. controls (209.19,212.15) and (207.12,213.52) .. (234.39,181.53) .. controls (234.39,198.44) and (235.22,197.98) .. (235.22,211.23) .. controls (231.55,216.48) and (226.78,223.11) .. (221.76,229.83) .. controls (221.97,225.37) and (221.96,221.8) .. (221.76,219) .. controls (221.64,217.3) and (221.46,215.89) .. (221.22,214.73) .. controls (219.14,204.52) and (212.9,213.65) .. (210.27,223.86) .. controls (210.27,226.15) and (209.4,234.61) .. (210.23,241.93) .. controls (202.86,251.28) and (198.72,258.64) .. (195.14,261.08) .. controls (194.73,250.53) and (195.56,244.13) .. (195.56,226.77) -- cycle ;
                	\draw  [fill={rgb, 255:red, 208; green, 78; blue, 2 }  ,fill opacity=1 ] (238.36,172.48) -- (195.39,227.75) -- (113.12,198.73) -- (160.9,148.99) -- cycle ;
                	\draw  [fill={rgb, 255:red, 179; green, 78; blue, 19 }  ,fill opacity=1 ] (195.39,227.75) -- (195.26,232.24) -- (113.43,204.26) -- (113.12,198.73) -- cycle ;
                	\draw  [fill={rgb, 255:red, 179; green, 78; blue, 19 }  ,fill opacity=1 ] (238.36,172.48) -- (237.43,176.97) -- (195.26,232.24) -- (195.39,227.75) -- cycle ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (137.01,173.86) -- (216.88,200.11) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (125.45,187.33) -- (205.32,213.58) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (148.88,159.7) -- (228.74,185.95) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (156.22,153.48) -- (234.05,178.7) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (144.04,166.6) -- (221.25,192.17) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (129.98,180.42) -- (210,206.33) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (119.36,192.51) -- (199.38,220.49) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (154.25,213.24) -- (198.07,160.04) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (174.87,220.15) -- (218.69,166.95) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (133.33,206.33) -- (177.77,154.17) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (184.86,223.95) -- (228.68,170.06) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (123.64,202.19) -- (167.46,151.41) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (144.88,208.4) -- (187.45,157.28) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (164.87,216) -- (207.76,162.8) ;
                	\draw  [fill={rgb, 255:red, 111; green, 96; blue, 68 }  ,fill opacity=1 ] (212.94,167.64) -- (222.76,167.65) -- (218.69,185.36) -- (216.92,188.11) -- (212.94,186.79) -- cycle ;
                	\draw  [fill={rgb, 255:red, 174; green, 151; blue, 110 }  ,fill opacity=1 ] (153.91,175.13) -- (153.22,199.33) -- (151.45,202.08) -- (135.1,171.06) -- cycle ;
                	\draw  [fill={rgb, 255:red, 240; green, 207; blue, 147 }  ,fill opacity=1 ] (151.32,185.44) .. controls (151.94,177.63) and (163.6,178.31) .. (165.75,191.55) .. controls (165.25,201.4) and (165.71,196.31) .. (165.75,207.18) .. controls (177.25,210.54) and (186.27,213.48) .. (193.19,215.99) .. controls (193.08,205.48) and (193.39,194.27) .. (192.79,185.73) .. controls (133.21,167.1) and (147.95,170.84) .. (126.3,164.61) .. controls (126.15,174.24) and (126.45,183.4) .. (127.37,194.27) .. controls (133.94,195.69) and (141.34,199.73) .. (151.45,202.08) .. controls (150.74,195.29) and (150.74,191.21) .. (151.32,185.44) -- cycle ;
                	\draw  [fill={rgb, 255:red, 140; green, 117; blue, 78 }  ,fill opacity=1 ] (193.55,185.39) .. controls (205.71,172.35) and (203.87,173.57) .. (228.19,145.05) .. controls (228.19,160.12) and (228.92,159.72) .. (228.92,171.53) .. controls (225.66,176.21) and (221.4,182.13) .. (216.92,188.11) .. controls (217.11,184.14) and (217.1,180.96) .. (216.93,178.46) .. controls (216.82,176.95) and (216.66,175.69) .. (216.44,174.65) .. controls (214.59,165.55) and (209.02,173.69) .. (206.68,182.8) .. controls (206.68,184.83) and (205.9,192.39) .. (206.64,198.91) .. controls (200.07,207.25) and (196.38,213.81) .. (193.19,215.99) .. controls (192.82,206.58) and (193.55,200.87) .. (193.55,185.39) -- cycle ;
                	\draw  [fill={rgb, 255:red, 208; green, 78; blue, 2 }  ,fill opacity=1 ] (231.34,137.37) -- (193.35,186.23) -- (120.62,160.58) -- (162.87,116.61) -- cycle ;
                	\draw  [fill={rgb, 255:red, 179; green, 78; blue, 19 }  ,fill opacity=1 ] (193.35,186.23) -- (193.24,190.2) -- (120.9,165.47) -- (120.62,160.58) -- cycle ;
                	\draw  [fill={rgb, 255:red, 179; green, 78; blue, 19 }  ,fill opacity=1 ] (231.34,137.37) -- (230.51,141.34) -- (193.24,190.2) -- (193.35,186.23) -- cycle ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (141.75,138.6) -- (212.35,161.8) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (131.53,150.51) -- (202.13,173.71) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (152.24,126.08) -- (222.84,149.28) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (158.73,120.58) -- (227.53,142.87) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (147.96,132.18) -- (216.21,154.78) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (135.53,144.4) -- (206.27,167.3) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (126.15,155.09) -- (196.88,179.82) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (156.99,173.41) -- (195.72,126.38) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (175.21,179.51) -- (213.95,132.49) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (138.49,167.3) -- (177.78,121.19) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (184.04,182.87) -- (222.78,135.24) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (129.93,163.64) -- (168.67,118.75) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (148.7,169.13) -- (186.34,123.94) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (166.37,175.85) -- (204.28,128.82) ;
                	\draw  [fill={rgb, 255:red, 111; green, 96; blue, 68 }  ,fill opacity=1 ] (208.87,133.1) -- (217.55,133.11) -- (213.95,148.77) -- (212.38,151.2) -- (208.87,150.03) -- cycle ;
                	\draw  [fill={rgb, 255:red, 174; green, 151; blue, 110 }  ,fill opacity=1 ] (156.68,139.72) -- (156.07,161.11) -- (154.51,163.54) -- (140.06,136.12) -- cycle ;
                	\draw  [fill={rgb, 255:red, 240; green, 207; blue, 147 }  ,fill opacity=1 ] (154.4,148.84) .. controls (154.94,141.93) and (165.25,142.53) .. (167.15,154.24) .. controls (166.71,162.94) and (167.11,158.44) .. (167.15,168.05) .. controls (177.32,171.02) and (185.29,173.62) .. (191.4,175.84) .. controls (191.31,166.55) and (191.58,156.64) .. (191.05,149.09) .. controls (138.38,132.63) and (151.41,135.93) .. (132.28,130.42) .. controls (132.14,138.93) and (132.41,147.03) .. (133.23,156.64) .. controls (139.03,157.9) and (145.57,161.47) .. (154.51,163.54) .. controls (153.88,157.54) and (153.88,153.94) .. (154.4,148.84) -- cycle ;
                	\draw  [fill={rgb, 255:red, 140; green, 117; blue, 78 }  ,fill opacity=1 ] (191.73,148.79) .. controls (202.48,137.26) and (200.85,138.34) .. (222.34,113.13) .. controls (222.34,126.45) and (223,126.09) .. (223,136.54) .. controls (220.11,140.68) and (216.35,145.9) .. (212.38,151.2) .. controls (212.56,147.69) and (212.54,144.87) .. (212.39,142.66) .. controls (212.3,141.33) and (212.15,140.21) .. (211.96,139.29) .. controls (210.32,131.25) and (205.4,138.44) .. (203.33,146.5) .. controls (203.33,148.3) and (202.65,154.97) .. (203.3,160.74) .. controls (197.49,168.11) and (194.23,173.92) .. (191.4,175.84) .. controls (191.08,167.52) and (191.73,162.48) .. (191.73,148.79) -- cycle ;
                	\draw  [fill={rgb, 255:red, 208; green, 78; blue, 2 }  ,fill opacity=1 ] (224.32,106.54) -- (191.15,149.2) -- (127.65,126.8) -- (164.53,88.41) -- cycle ;
                	\draw  [fill={rgb, 255:red, 179; green, 78; blue, 19 }  ,fill opacity=1 ] (191.15,149.2) -- (191.05,152.66) -- (127.89,131.07) -- (127.65,126.8) -- cycle ;
                	\draw  [fill={rgb, 255:red, 179; green, 78; blue, 19 }  ,fill opacity=1 ] (224.32,106.54) -- (223.59,110) -- (191.05,152.66) -- (191.15,149.2) -- cycle ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (146.09,107.6) -- (207.73,127.87) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (137.17,118) -- (198.81,138.27) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (155.25,96.67) -- (216.89,116.94) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (160.92,91.87) -- (220.99,111.34) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (151.51,102) -- (211.11,121.73) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (140.67,112.67) -- (202.43,132.67) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (132.47,122) -- (194.23,143.6) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (159.4,138) -- (193.22,96.94) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (175.31,143.33) -- (209.13,102.27) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (143.25,132.67) -- (177.55,92.41) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (183.02,146.26) -- (216.84,104.67) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (135.77,129.47) -- (169.59,90.27) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (152.16,134.27) -- (185.02,94.81) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (167.59,140.13) -- (200.69,99.07) ;
                	\draw  [fill={rgb, 255:red, 111; green, 96; blue, 68 }  ,fill opacity=1 ] (204.7,102.8) -- (212.28,102.81) -- (209.13,116.48) -- (207.77,118.61) -- (204.7,117.58) -- cycle ;
                	\draw  [fill={rgb, 255:red, 174; green, 151; blue, 110 }  ,fill opacity=1 ] (159.13,108.59) -- (158.6,127.26) -- (157.23,129.39) -- (144.62,105.44) -- cycle ;
                	\draw  [fill={rgb, 255:red, 240; green, 207; blue, 147 }  ,fill opacity=1 ] (157.14,116.54) .. controls (157.61,110.52) and (166.62,111.04) .. (168.27,121.26) .. controls (167.88,128.86) and (168.24,124.93) .. (168.27,133.32) .. controls (177.15,135.92) and (184.11,138.18) .. (189.45,140.12) .. controls (189.37,132.01) and (189.6,123.36) .. (189.14,116.76) .. controls (143.15,102.39) and (154.53,105.27) .. (137.83,100.46) .. controls (137.7,107.89) and (137.94,114.97) .. (138.65,123.36) .. controls (143.72,124.46) and (149.43,127.57) .. (157.23,129.39) .. controls (156.69,124.14) and (156.69,121) .. (157.14,116.54) -- cycle ;
                	\draw  [fill={rgb, 255:red, 140; green, 117; blue, 78 }  ,fill opacity=1 ] (189.73,116.5) .. controls (199.12,106.44) and (197.69,107.38) .. (216.46,85.36) .. controls (216.46,97) and (217.03,96.69) .. (217.03,105.81) .. controls (214.51,109.42) and (211.23,113.98) .. (207.77,118.61) .. controls (207.92,115.54) and (207.9,113.08) .. (207.77,111.15) .. controls (207.69,109.99) and (207.56,109.01) .. (207.4,108.21) .. controls (205.97,101.19) and (201.67,107.47) .. (199.86,114.5) .. controls (199.86,116.07) and (199.26,121.9) .. (199.83,126.94) .. controls (194.76,133.38) and (191.91,138.44) .. (189.45,140.12) .. controls (189.16,132.86) and (189.73,128.45) .. (189.73,116.5) -- cycle ;
                	\draw  [fill={rgb, 255:red, 208; green, 78; blue, 2 }  ,fill opacity=1 ] (218.53,79.75) -- (189.76,116.76) -- (134.67,97.33) -- (166.67,64.02) -- cycle ;
                	\draw  [fill={rgb, 255:red, 179; green, 78; blue, 19 }  ,fill opacity=1 ] (189.76,116.76) -- (189.67,119.77) -- (134.88,101.03) -- (134.67,97.33) -- cycle ;
                	\draw  [fill={rgb, 255:red, 179; green, 78; blue, 19 }  ,fill opacity=1 ] (218.53,79.75) -- (217.91,82.76) -- (189.67,119.77) -- (189.76,116.76) -- cycle ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (150.67,80.68) -- (204.15,98.25) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (142.93,89.7) -- (196.41,107.28) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (158.62,71.19) -- (212.09,88.77) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (163.53,67.03) -- (215.65,83.91) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (155.38,75.82) -- (207.07,92.93) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (145.96,85.07) -- (199.54,102.42) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (138.85,93.17) -- (192.43,111.9) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (162.21,107.04) -- (191.56,71.42) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (176.02,111.67) -- (205.36,76.05) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (148.2,102.42) -- (177.96,67.49) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (182.71,114.21) -- (212.05,78.13) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (141.72,99.64) -- (171.06,65.64) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (155.94,103.81) -- (184.44,69.57) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (169.32,108.89) -- (198.04,73.27) ;
                	\draw  [fill={rgb, 255:red, 111; green, 96; blue, 68 }  ,fill opacity=1 ] (201.51,76.51) -- (208.09,76.52) -- (205.36,88.38) -- (204.18,90.22) -- (201.51,89.33) -- cycle ;
                	\draw  [fill={rgb, 255:red, 174; green, 151; blue, 110 }  ,fill opacity=1 ] (161.98,81.53) -- (161.52,97.73) -- (160.34,99.57) -- (149.39,78.8) -- cycle ;
                	\draw  [fill={rgb, 255:red, 240; green, 207; blue, 147 }  ,fill opacity=1 ] (160.25,88.43) .. controls (160.66,83.2) and (168.48,83.66) .. (169.92,92.52) .. controls (169.58,99.12) and (169.88,95.71) .. (169.92,102.98) .. controls (177.62,105.24) and (183.65,107.2) .. (188.28,108.89) .. controls (188.21,101.85) and (188.42,94.34) .. (188.02,88.62) .. controls (148.12,76.15) and (157.99,78.65) .. (143.5,74.48) .. controls (143.39,80.93) and (143.6,87.07) .. (144.22,94.34) .. controls (148.61,95.3) and (153.57,98) .. (160.34,99.57) .. controls (159.86,95.03) and (159.86,92.3) .. (160.25,88.43) -- cycle ;
                	\draw  [fill={rgb, 255:red, 140; green, 117; blue, 78 }  ,fill opacity=1 ] (188.53,88.39) .. controls (196.67,79.66) and (195.44,80.48) .. (211.72,61.38) .. controls (211.72,71.48) and (212.21,71.2) .. (212.21,79.12) .. controls (210.03,82.25) and (207.18,86.21) .. (204.18,90.22) .. controls (204.3,87.56) and (204.3,85.43) .. (204.18,83.75) .. controls (204.11,82.74) and (204,81.9) .. (203.86,81.2) .. controls (202.61,75.11) and (198.89,80.56) .. (197.32,86.66) .. controls (197.32,88.02) and (196.8,93.08) .. (197.29,97.45) .. controls (192.89,103.03) and (190.42,107.43) .. (188.28,108.89) .. controls (188.04,102.58) and (188.53,98.76) .. (188.53,88.39) -- cycle ;
                	\draw  [fill={rgb, 255:red, 208; green, 78; blue, 2 }  ,fill opacity=1 ] (213.16,57.21) -- (188.5,88.93) -- (141.28,72.28) -- (168.71,43.73) -- cycle ;
                	\draw  [fill={rgb, 255:red, 179; green, 78; blue, 19 }  ,fill opacity=1 ] (188.5,88.93) -- (188.43,91.51) -- (141.46,75.45) -- (141.28,72.28) -- cycle ;
                	\draw  [fill={rgb, 255:red, 179; green, 78; blue, 19 }  ,fill opacity=1 ] (213.16,57.21) -- (212.63,59.79) -- (188.43,91.51) -- (188.5,88.93) -- cycle ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (154.99,58) -- (200.83,73.07) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (148.36,65.74) -- (194.2,80.8) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (161.81,49.88) -- (207.64,64.94) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (166.02,46.31) -- (210.69,60.78) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (159.03,53.84) -- (203.34,68.51) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (150.96,61.77) -- (196.89,76.64) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (144.87,68.71) -- (190.79,84.77) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (164.89,80.61) -- (190.04,50.07) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (176.72,84.57) -- (201.87,54.04) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (152.88,76.64) -- (178.39,46.7) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (182.46,86.75) -- (207.61,55.82) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (147.32,74.26) -- (172.47,45.12) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (159.51,77.83) -- (183.94,48.49) ;
                	\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.33 ]   (170.98,82.19) -- (195.6,51.66) ;
                	\draw  [fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (204.07,55.28) -- (186.07,78.44) -- (151.61,66.28) -- (171.63,45.44) -- cycle ;
                	\draw  [fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (186.07,78.44) -- (186.02,80.32) -- (151.74,68.59) -- (151.61,66.28) -- cycle ;
                	\draw  [fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (204.07,55.28) -- (203.68,57.16) -- (186.02,80.32) -- (186.07,78.44) -- cycle ;
                	\draw  [fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (198.08,53.56) -- (184.26,71.33) -- (157.81,62) -- (173.17,46) -- cycle ;
                	\draw  [fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (184.26,71.33) -- (184.22,72.78) -- (157.91,63.78) -- (157.81,62) -- cycle ;
                	\draw  [fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (198.08,53.56) -- (197.78,55) -- (184.22,72.78) -- (184.26,71.33) -- cycle ;
                	\draw  [fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (178.87,27.3) -- (183.29,66.93) -- (163.18,59.74) -- cycle ;
                	\draw  [fill={rgb, 255:red, 169; green, 115; blue, 26 }  ,fill opacity=1 ] (178.87,27.3) -- (192.51,54.71) -- (183.29,66.93) -- cycle ;
                	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.55 ] (148.21,226.83) .. controls (149.86,216.78) and (164.83,222.86) .. (164.39,233.68) .. controls (163.59,240.22) and (164.13,235.72) .. (163.97,243.67) .. controls (158.63,244.33) and (154.09,245.25) .. (148.34,245.49) .. controls (147.89,237.93) and (146.55,236.88) .. (148.21,226.83) -- cycle ;
                	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.55 ] (151.32,185.44) .. controls (152.98,175.39) and (166.2,180.73) .. (165.75,191.55) .. controls (164.96,198.09) and (165.55,192.51) .. (165.39,200.46) .. controls (160.04,201.12) and (157.19,201.84) .. (151.45,202.08) .. controls (150.99,194.53) and (149.67,195.49) .. (151.32,185.44) -- cycle ;
                	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.55 ] (154.4,148.84) .. controls (156.98,141.53) and (164.81,143.56) .. (167.15,154.24) .. controls (165.22,163.21) and (166.89,161.17) .. (168.46,163.85) .. controls (163.12,164.52) and (160.25,163.3) .. (154.51,163.54) .. controls (154.05,155.99) and (152.75,158.89) .. (154.4,148.84) -- cycle ;
                	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.55 ] (157.14,116.54) .. controls (159.72,109.24) and (165.93,110.58) .. (168.27,121.26) .. controls (166.34,130.23) and (166.15,128.34) .. (167.72,131.02) .. controls (162.38,131.68) and (162.98,129.15) .. (157.23,129.39) .. controls (156.78,121.84) and (155.48,126.6) .. (157.14,116.54) -- cycle ;
                	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.55 ] (160.24,86.73) .. controls (163.18,83.96) and (166.26,85.95) .. (169.92,92.52) .. controls (168.32,100.57) and (169.26,98.53) .. (170.82,101.2) .. controls (165.48,101.87) and (166.08,99.33) .. (160.34,99.57) .. controls (159.88,92.02) and (158.59,96.78) .. (160.24,86.73) -- cycle ;
                	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.55 ] (221.76,219) -- (221.76,229.83) -- (210.23,241.93) -- (209.86,229.25) -- (210.68,221.03) -- (212.75,213.72) -- (217.71,210.98) -- (221.22,214.73) -- cycle ;
                	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.55 ] (216.06,179.42) -- (216.05,189.24) -- (206.45,200.21) -- (206.14,188.72) -- (206.83,181.26) -- (208.55,174.63) -- (212.68,172.14) -- (215.61,175.54) -- cycle ;
                	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.55 ] (211.92,143.12) -- (211.92,151.44) -- (203.52,160.74) -- (203.25,151) -- (203.85,144.68) -- (205.36,139.06) -- (208.97,136.96) -- (211.53,139.84) -- cycle ;
                	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.55 ] (207.79,112.02) -- (207.79,119.07) -- (199.79,126.94) -- (199.53,118.7) -- (200.1,113.34) -- (201.54,108.59) -- (204.98,106.8) -- (207.42,109.24) -- cycle ;
                	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.55 ] (204.07,83.4) -- (204.07,89.43) -- (197.29,96.17) -- (197.07,89.11) -- (197.56,84.53) -- (198.77,80.46) -- (201.69,78.93) -- (203.76,81.02) -- cycle ;
                	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.3 ] (119.8,205.95) -- (195.26,232.24) -- (195.4,235.65) -- (120.21,209.15) -- cycle ;
                	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.3 ] (126.82,168.03) -- (193,190.09) -- (193.14,193.5) -- (126.41,170.77) -- cycle ;
                	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.3 ] (133.43,133.3) -- (191.05,152.66) -- (191.19,156.07) -- (132.61,136.04) -- cycle ;
                	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.3 ] (137.83,100.46) -- (189.67,119.77) -- (189.81,123.18) -- (138.8,105.43) -- cycle ;
                	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.3 ] (143.5,74.48) -- (188.13,90.51) -- (188.26,93.93) -- (144.59,78.47) -- cycle ;
                	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.39 ] (245.8,212.29) -- (237.54,210.06) -- (195.4,260.42) -- (218.53,248.44) -- cycle ;
                	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.39 ] (238.36,172.48) -- (230.1,170.25) -- (193.19,215.99) -- (211.1,208.63) -- cycle ;
                	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.39 ] (232.74,136.11) -- (224.48,133.88) -- (191.4,175.84) -- (214.4,161.17) -- cycle ;
                	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.39 ] (224.32,106.54) -- (219.91,103.81) -- (189.45,140.12) -- (210.27,127.36) -- cycle ;
                	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.39 ] (218.53,79.75) -- (214.4,77.56) -- (188.28,108.89) -- (206.14,99.03) -- cycle ;
                	\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.39 ] (212.34,57.51) -- (195.6,51.66) -- (183.29,66.93) -- (203.34,68.51) -- cycle ;
                	\draw  [fill={rgb, 255:red, 208; green, 93; blue, 2 }  ,fill opacity=1 ] (56.38,228.3) -- (92.03,228.3) -- (76.75,240.49) -- (41.1,240.49) -- cycle ;
                	\draw  [fill={rgb, 255:red, 174; green, 80; blue, 6 }  ,fill opacity=1 ] (41.1,240.49) -- (77.91,240.49) -- (77.91,243.3) -- (41.1,243.3) -- cycle ;
                	\draw  [fill={rgb, 255:red, 137; green, 64; blue, 6 }  ,fill opacity=1 ] (92.03,228.3) -- (92.1,232.45) -- (77.91,243.3) -- (76.75,240.49) -- cycle ;
                \end{tikzpicture}'''
                # Câu hỏi
                noidungcauhoi = (r'''\immini{Một đội thợ công nhân dùng gạch cỡ $%s \text{ cm} \times %s \text{ cm}$ để lát nền cho một toà tháp gồm $%s$ tầng theo cấu trúc diện tích mặt sàn của tầng trên bằng $%s\%%$ diện tích mặt sàn của tầng dưới. Biết diện tích mặt đáy của tháp là $%s \text{ m}^2$. Hỏi đội công nhân dự định dùng tối thiểu bao nhiêu viên gạch để hoàn thành công trình?}{%s}'''
                                 %(latex(a), latex(a), latex(n), latex(p), latex(S1), hinhve))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Giả sử diện tích mặt sàn tầng 1 là $S_1 \\text{ (m}^2)$ nên diện tích mặt sàn tầng 2 là $S_2 = \\frac{%s}{%s}S_1$. \\\\
                            Diện tích mặt sàn tầng 3 là $S_3 = \\frac{%s}{%s}S_2 = \\left(\\frac{%s}{%s}\\right)^2 S_1$, nên diện tích mặt sàn tầng $%s$ là $S_{%s} = \\left(\\frac{%s}{%s}\\right)^{%s} S_1$. \\\\
                            Tổng diện tích mặt sàn của toà tháp là: $S = S_1 + S_2 + \\dots + S_{%s} = %s \\cdot \\frac{1 - \\left(\\frac{%s}{%s}\\right)^{%s}}{1 - \\frac{%s}{%s}} = %s \\text{ (m}^2)$. \\\\
                            Số viên gạch cần dùng là: $\\frac{%s}{(%s \\cdot %s)} = %s$ viên.'''
                           %(latex(tu), latex(mau),
                             latex(tu), latex(mau), latex(tu), latex(mau), latex(n), latex(n), latex(tu), latex(mau), latex(n-1),
                             latex(n), latex(S1), latex(tu), latex(mau), latex(n), latex(tu), latex(mau), s_total_str,
                             s_total_str, a_m_str, a_m_str, latex(num_tiles_final)))
                dapan='\\shortans[0]{$%s$}\n'%(latex(num_tiles_final))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                       '\\loigiai{\n'+str(loigiai)+'\n}\n'
                       '\\end{ex}\n\\end{minipage} \n\n') 
            return content 


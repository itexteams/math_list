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


def bt_dang10_p3_b4_c2_hh12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random cạnh hình lập phương (L) và khoảng cách (d)
                L = random.choice([4, 6, 8, 10, 12])
                d = random.choice([1, 2])

                # Tính toán tọa độ tâm
                toado = Rational(L, 2)
                tong_S = 3 * toado

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(latex(tong_S))]
                da = random.choice(du)

                # Tạo các phương án sai (đảm bảo không trùng)
                s = [
                    '$%s$'%(latex(tong_S + 1)),
                    '$%s$'%(latex(tong_S + 2)),
                    '$%s$'%(latex(tong_S - 1)),
                    '$%s$'%(latex(tong_S - 2)),
                    '$%s$'%(latex(tong_S + toado)),
                    '$%s$'%(latex(tong_S * 2))
                ]

                # Lọc bỏ phương án sai nếu vô tình trùng đáp án đúng
                if da in s:
                    s.remove(da)

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                hinhve=r'''\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.33 ] (132,160.56) -- (238.4,170.96) -- (149.85,195.52) -- (119.85,175.52) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.3 ] (131.52,74.75) -- (209.62,87.87) -- (209.6,175.36) -- (132,160.56) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.3 ] (67.98,90.85) -- (131.52,74.75) -- (132,160.56) -- (68,178.96) -- cycle ;
            	\draw  [fill={rgb, 255:red, 10; green, 107; blue, 220 }  ,fill opacity=1 ] (97.7,136.91) .. controls (97.7,111.51) and (118.29,90.92) .. (143.69,90.92) .. controls (169.09,90.92) and (189.68,111.51) .. (189.68,136.91) .. controls (189.68,162.31) and (169.09,182.9) .. (143.69,182.9) .. controls (118.29,182.9) and (97.7,162.31) .. (97.7,136.91) -- cycle ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=0.75] [line join = round][line cap = round] (125.88,118.77) .. controls (125.88,118.77) and (125.88,118.77) .. (125.88,118.77) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (116.16,110.14) .. controls (115.08,112.66) and (114,115.17) .. (112.92,117.69) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (113.82,119.13) .. controls (118.89,114.22) and (120.3,110.36) .. (120.3,116.25) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (121.02,117.87) .. controls (119.88,118.83) and (116.73,119.88) .. (117.78,120.93) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (120.3,120.93) .. controls (120.3,120.93) and (120.3,120.93) .. (120.3,120.93) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (123.36,120.39) .. controls (124.08,118.83) and (126.1,117.33) .. (125.52,115.71) .. controls (124.63,113.28) and (121.82,112.06) .. (119.76,110.5) .. controls (119.18,110.05) and (120.6,111.7) .. (121.02,112.3) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (116.7,107.26) .. controls (117.3,106.9) and (117.9,106.54) .. (118.5,106.18) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (117.06,106.18) .. controls (116.4,105.94) and (115.74,105.7) .. (115.08,105.46) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (114.18,108.52) .. controls (113.7,108.04) and (113.22,107.56) .. (112.74,107.08) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (112.92,110.14) .. controls (112.26,110.38) and (111.6,110.62) .. (110.94,110.86) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (111.3,113.02) .. controls (110.82,113.26) and (110.34,113.5) .. (109.86,113.74) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (110.22,115.89) .. controls (109.5,116.13) and (108.78,116.37) .. (108.06,116.61) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (108.6,117.69) .. controls (107.76,118.17) and (106.92,118.65) .. (106.08,119.13) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (106.8,119.49) .. controls (106.74,120.03) and (106.68,120.57) .. (106.62,121.11) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (110.22,119.49) .. controls (110.22,120.51) and (110.22,121.53) .. (110.22,122.55) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (112.38,121.47) .. controls (112.68,121.77) and (112.98,122.07) .. (113.28,122.37) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (114.9,122.19) .. controls (115.14,122.19) and (115.38,122.19) .. (115.62,122.19) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (108.6,124.53) .. controls (109.02,124.71) and (109.44,124.89) .. (109.86,125.07) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (136.85,154.4) .. controls (135.29,152) and (133.73,149.6) .. (132.17,147.2) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (132.17,146.66) .. controls (131.09,144.68) and (130.02,142.7) .. (128.94,140.72) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (133.97,155.84) .. controls (131.51,152.06) and (129.06,148.28) .. (126.6,144.5) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (128.22,153.86) .. controls (127.26,152.24) and (126.3,150.62) .. (125.34,149) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (140.81,153.68) .. controls (138.29,149.48) and (135.77,145.28) .. (133.25,141.08) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (143.69,157.64) .. controls (144.47,155.24) and (145.25,152.84) .. (146.03,150.44) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (145.49,152.6) .. controls (143.51,149.72) and (141.53,146.84) .. (139.55,143.96) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (145.49,151.16) .. controls (146.33,151.4) and (147.17,151.64) .. (148.01,151.88) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (146.93,154.04) .. controls (146.93,154.52) and (146.93,155) .. (146.93,155.48) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (146.03,157.64) .. controls (146.03,158) and (146.03,158.36) .. (146.03,158.72) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (142.97,159.08) .. controls (142.61,159.62) and (142.25,160.16) .. (141.89,160.7) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (140.45,160.7) .. controls (140.57,161.54) and (140.69,162.38) .. (140.81,163.22) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (138.83,164.12) .. controls (139.25,164.24) and (139.67,164.36) .. (140.09,164.48) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (136.49,165.19) .. controls (136.79,165.79) and (137.09,166.39) .. (137.39,166.99) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (136.67,166.99) .. controls (136.49,167.65) and (136.31,168.31) .. (136.13,168.97) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (133.97,168.61) .. controls (133.97,169.21) and (133.97,169.81) .. (133.97,170.41) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (133.43,167.53) .. controls (133.43,164) and (133.43,160.46) .. (133.43,156.92) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (135.59,161.6) .. controls (136.77,159.6) and (137.72,157.17) .. (139.73,156.02) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (134.33,158.54) .. controls (133.43,157.82) and (132.53,157.1) .. (131.63,156.38) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (173.56,126.69) .. controls (170.41,129.84) and (167.27,133) .. (164.02,136.05) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (164.2,134.25) .. controls (163.73,132.99) and (163.06,131.56) .. (163.48,130.29) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (164.2,129.03) .. controls (165.28,127.95) and (166.36,126.87) .. (167.44,125.79) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (167.98,125.25) .. controls (169.48,124.71) and (170.98,124.17) .. (172.48,123.63) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (173.56,124.89) .. controls (174.52,125.55) and (175.48,126.21) .. (176.44,126.87) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (178.6,128.31) .. controls (179.62,128.25) and (180.64,128.19) .. (181.66,128.13) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (182.37,128.13) .. controls (183.27,127.65) and (184.17,127.17) .. (185.07,126.69) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (185.43,126.87) .. controls (185.37,129.69) and (185.31,132.51) .. (185.25,135.33) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (186.51,132.09) .. controls (185.97,137.07) and (185.43,142.04) .. (184.89,147.02) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (183.09,135.15) .. controls (181.72,133.53) and (180.86,131.24) .. (178.96,130.29) .. controls (177.19,129.4) and (173.26,128.14) .. (173.02,130.11) .. controls (172.85,131.47) and (179.99,137.61) .. (181.66,139.11) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (178.6,135.33) .. controls (177.94,136.77) and (177.28,138.21) .. (176.62,139.64) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (175.36,138.75) .. controls (173.77,136.86) and (172.03,135.04) .. (169.96,133.71) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (169.24,134.43) .. controls (169.54,135.87) and (169.84,137.31) .. (170.14,138.75) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (166.54,137.13) .. controls (166.78,138.15) and (167.02,139.17) .. (167.26,140.18) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (180.22,139.64) .. controls (180.1,141.32) and (179.98,143) .. (179.86,144.68) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (183.09,144.86) .. controls (182.67,145.52) and (182.25,146.18) .. (181.83,146.84) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (180.4,139.11) .. controls (181.06,139.88) and (181.72,140.66) .. (182.37,141.44) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (184.71,149.36) .. controls (184.47,150.26) and (184.23,151.16) .. (183.99,152.06) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (183.09,150.08) .. controls (183.03,150.38) and (182.97,150.68) .. (182.91,150.98) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (182.91,151.16) .. controls (182.43,152.9) and (181.95,154.64) .. (181.48,156.38) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (176.26,112.12) .. controls (176.56,111.94) and (176.86,111.76) .. (177.16,111.58) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (177.7,112.48) .. controls (177.76,112.54) and (177.82,112.6) .. (177.88,112.66) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=6] [line join = round][line cap = round] (174.28,112.3) .. controls (173.26,112.3) and (172.24,112.3) .. (171.22,112.3) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=5.25] [line join = round][line cap = round] (144.77,98.8) .. controls (144.47,98.62) and (144.17,98.44) .. (143.87,98.26) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=2.25] [line join = round][line cap = round] (118.86,104.74) .. controls (119.76,104.56) and (120.66,104.38) .. (121.56,104.2) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=2.25] [line join = round][line cap = round] (120.66,105.82) .. controls (120.96,105.58) and (121.26,105.34) .. (121.56,105.1) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (116.34,103.48) .. controls (116.58,103.48) and (116.82,103.48) .. (117.06,103.48) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (117.42,103.84) .. controls (117.36,103.54) and (117.3,103.24) .. (117.24,102.94) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (121.74,104.38) .. controls (123.06,103.84) and (124.38,103.3) .. (125.7,102.76) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (123.36,105.1) .. controls (123.96,104.62) and (124.56,104.14) .. (125.16,103.66) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (122.82,104.74) .. controls (122.1,105.58) and (121.38,106.42) .. (120.66,107.26) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (103.57,120.93) .. controls (103.87,122.85) and (104.17,124.77) .. (104.47,126.69) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (116.7,124.53) .. controls (117.9,124.29) and (119.1,124.05) .. (120.3,123.81) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (120.3,124.35) .. controls (120.66,124.47) and (121.02,124.59) .. (121.38,124.71) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (122.82,123.09) .. controls (122.52,123.57) and (122.22,124.05) .. (121.92,124.53) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (121.92,124.17) .. controls (122.22,125.31) and (122.52,126.45) .. (122.82,127.59) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (112.38,125.25) .. controls (112.14,126.75) and (111.9,128.25) .. (111.66,129.75) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (109.68,127.05) .. controls (110.28,128.31) and (110.88,129.57) .. (111.48,130.83) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (109.86,127.59) .. controls (110.22,128.85) and (110.58,130.11) .. (110.94,131.37) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (108.6,127.41) .. controls (108.96,128.37) and (109.32,129.33) .. (109.68,130.29) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (108.24,127.59) .. controls (108.84,128.85) and (109.44,130.11) .. (110.04,131.37) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (113.46,124.17) .. controls (113.22,124.89) and (112.98,125.61) .. (112.74,126.33) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (110.58,127.41) .. controls (110.7,127.89) and (110.82,128.37) .. (110.94,128.85) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (108.06,129.21) .. controls (109.5,130.53) and (110.94,131.85) .. (112.38,133.17) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (108.96,131.19) .. controls (110.1,131.79) and (111.24,132.39) .. (112.38,132.99) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (112.02,130.29) .. controls (113.28,131.61) and (114.54,132.93) .. (115.8,134.25) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (113.1,132.63) .. controls (113.82,133.29) and (114.54,133.95) .. (115.26,134.61) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (112.38,131.37) .. controls (113.58,132.21) and (114.52,134.04) .. (115.98,133.89) .. controls (117.13,133.77) and (117.06,131.85) .. (117.6,130.83) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (116.34,132.81) .. controls (116.46,132.45) and (116.58,132.09) .. (116.7,131.73) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (116.34,134.61) .. controls (117.3,135.33) and (118.26,136.05) .. (119.22,136.77) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (117.24,135.33) .. controls (118.14,135.39) and (119.04,135.45) .. (119.94,135.51) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (119.94,136.41) .. controls (119.94,137.13) and (119.94,137.85) .. (119.94,138.57) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (120.3,138.39) .. controls (121.02,138.63) and (121.74,138.87) .. (122.46,139.11) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (123.18,139.64) .. controls (124.32,140.54) and (125.46,141.44) .. (126.6,142.34) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (124.44,141.08) .. controls (124.44,141.56) and (124.44,142.04) .. (124.44,142.52) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (124.98,140.36) .. controls (126,139.59) and (127.02,138.81) .. (128.04,138.03) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (129.84,138.57) .. controls (130.85,138.39) and (131.87,138.21) .. (132.89,138.03) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (136.13,141.62) .. controls (136.85,141.62) and (137.57,141.62) .. (138.29,141.62) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (147.65,149) .. controls (148.98,150.33) and (151.46,152.23) .. (150.53,153.86) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (149.81,149.18) .. controls (150.53,149.96) and (151.25,150.74) .. (151.97,151.52) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (150.17,151.16) .. controls (149.81,150.44) and (149.45,149.72) .. (149.09,149) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (149.09,157.64) .. controls (148.55,158.42) and (148.01,159.2) .. (147.47,159.98) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (143.51,164.12) .. controls (143.39,164.72) and (143.27,165.31) .. (143.15,165.91) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (135.77,171.13) .. controls (136.37,171.61) and (136.97,172.09) .. (137.57,172.57) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (138.11,168.97) .. controls (138.83,169.21) and (139.55,169.45) .. (140.27,169.69) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (139.19,168.97) .. controls (139.85,168.19) and (140.51,167.41) .. (141.17,166.63) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (131.45,170.77) .. controls (132.35,172.39) and (133.25,174.01) .. (134.15,175.63) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (134.15,173.29) .. controls (134.33,173.83) and (134.51,174.37) .. (134.69,174.91) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (133.97,175.63) .. controls (134.87,176.77) and (135.77,177.91) .. (136.67,179.05) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (125.16,102.94) .. controls (126,102.7) and (126.84,102.46) .. (127.68,102.22) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (127.5,102.94) .. controls (127.26,102.1) and (127.02,101.26) .. (126.78,100.42) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (126.78,100.06) .. controls (128.76,100) and (130.74,99.94) .. (132.71,99.88) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (131.09,100.06) .. controls (130.8,100.66) and (130.5,101.26) .. (130.2,101.86) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (131.81,99.88) .. controls (133.07,100.6) and (134.33,101.32) .. (135.59,102.04) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (133.43,101.32) .. controls (133.67,102.34) and (133.91,103.36) .. (134.15,104.38) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (133.97,102.58) .. controls (133.91,103.18) and (133.85,103.78) .. (133.79,104.38) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (133.43,102.94) .. controls (132.89,103.36) and (132.35,103.78) .. (131.81,104.2) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (132.35,103.66) .. controls (132.95,103.96) and (133.55,104.26) .. (134.15,104.56) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (120.12,100.78) .. controls (120.6,101.08) and (121.08,101.38) .. (121.56,101.68) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (121.74,101.68) .. controls (122.64,101.32) and (123.54,100.96) .. (124.44,100.6) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (122.46,100.78) .. controls (122.28,100.36) and (122.1,99.94) .. (121.92,99.52) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (121.56,100.06) .. controls (121.38,100.18) and (121.2,100.3) .. (121.02,100.42) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (124.98,98.8) .. controls (125.34,98.68) and (125.7,98.56) .. (126.06,98.44) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (128.22,98.26) .. controls (128.52,98.02) and (128.82,97.78) .. (129.12,97.54) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (131.27,98.26) .. controls (132.05,97.96) and (132.83,97.66) .. (133.61,97.36) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (133.07,97.18) .. controls (132.71,96.94) and (132.35,96.7) .. (131.99,96.46) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (133.61,97.18) .. controls (134.51,96.64) and (135.41,96.1) .. (136.31,95.56) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (134.87,96.46) .. controls (136.31,96.16) and (137.75,95.86) .. (139.19,95.56) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (136.13,95.38) .. controls (135.77,95.38) and (135.41,95.38) .. (135.05,95.38) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (123,109.42) .. controls (123.9,110.02) and (124.8,110.62) .. (125.7,111.22) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (115.8,102.22) .. controls (117.42,102.64) and (119.04,103.06) .. (120.66,103.48) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (121.02,103.48) .. controls (122.4,103.06) and (123.78,102.64) .. (125.16,102.22) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (127.68,114.63) .. controls (129.6,112.31) and (131,109.1) .. (133.79,107.98) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (131.99,107.62) .. controls (131.75,107.02) and (131.51,106.42) .. (131.27,105.82) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (131.09,105.46) .. controls (130.56,106.78) and (130.02,108.1) .. (129.48,109.42) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (129.12,108.16) .. controls (129.12,108.94) and (129.12,109.72) .. (129.12,110.5) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (129.12,110.5) .. controls (129.12,110.62) and (129.12,110.74) .. (129.12,110.86) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (129.3,109.24) .. controls (128.46,110.26) and (127.62,111.28) .. (126.78,112.3) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (127.5,113.38) .. controls (128.71,111.19) and (132.68,108.48) .. (130.91,106.72) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (130.2,106.54) .. controls (129.9,106.9) and (129.6,107.26) .. (129.3,107.62) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (128.76,110.14) .. controls (128.52,110.62) and (128.28,111.1) .. (128.04,111.58) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (133.25,108.52) .. controls (134.07,108) and (135.62,107.88) .. (136.13,108.7) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (135.95,108.7) .. controls (136.67,109.48) and (137.39,110.26) .. (138.11,111.04) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (138.29,111.94) .. controls (138.05,112.54) and (137.81,113.14) .. (137.57,113.74) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (138.11,112.3) .. controls (138.16,112.78) and (137.81,113.8) .. (137.39,113.56) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (137.03,113.38) .. controls (137.21,112.54) and (137.39,111.7) .. (137.57,110.86) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (136.49,110.86) .. controls (134.75,111.22) and (133.01,111.58) .. (131.27,111.94) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (131.81,110.86) .. controls (133.25,110.32) and (134.69,109.78) .. (136.13,109.24) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (135.05,109.42) .. controls (134.15,109.84) and (133.25,110.26) .. (132.35,110.68) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (132.71,109.78) .. controls (133.37,108.88) and (134.03,107.98) .. (134.69,107.08) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (130.74,112.12) .. controls (130.74,112.12) and (130.74,112.12) .. (130.74,112.12) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (131.45,111.94) .. controls (132.05,112.96) and (132.65,113.98) .. (133.25,114.99) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (131.81,113.38) .. controls (131.51,113.98) and (131.21,114.57) .. (130.91,115.17) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (130.91,112.48) .. controls (130.38,113.92) and (129.84,115.35) .. (129.3,116.79) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (129.66,113.2) .. controls (129.42,114.69) and (129.18,116.19) .. (128.94,117.69) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (131.63,114.81) .. controls (132.23,115.29) and (132.83,115.77) .. (133.43,116.25) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (133.43,115.71) .. controls (133.79,115.53) and (134.15,115.35) .. (134.51,115.17) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (136.49,97.9) .. controls (139.49,97) and (142.49,96.1) .. (145.49,95.2) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (145.49,95.2) .. controls (148.25,95.62) and (151.01,96.04) .. (153.77,96.46) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (146.21,95.74) .. controls (148.15,96.41) and (150.16,97.86) .. (152.15,97.36) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (147.65,97) .. controls (149.33,97.48) and (151.01,97.96) .. (152.69,98.44) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (146.93,96.46) .. controls (148.37,97.42) and (149.81,98.38) .. (151.25,99.34) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (147.83,97) .. controls (147.71,98.74) and (147.59,100.48) .. (147.47,102.22) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (147.65,101.5) .. controls (149.03,101.14) and (150.41,100.78) .. (151.79,100.42) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (149.81,100.06) .. controls (149.57,99.58) and (149.33,99.1) .. (149.09,98.62) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (148.91,100.06) .. controls (147.83,98.62) and (146.75,97.18) .. (145.67,95.74) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (140.81,97.36) .. controls (140.57,97.54) and (140.33,97.72) .. (140.09,97.9) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (139.91,98.44) .. controls (140.39,99.22) and (140.87,100) .. (141.35,100.78) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (140.99,98.8) .. controls (141.47,99.52) and (141.95,100.24) .. (142.43,100.96) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (139.01,97.9) .. controls (140.51,99.76) and (142.01,101.62) .. (143.51,103.48) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (141.53,101.5) .. controls (141.83,102.7) and (142.13,103.9) .. (142.43,105.1) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (143.51,101.14) .. controls (144.17,101.5) and (144.83,101.86) .. (145.49,102.22) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (146.93,100.06) .. controls (146.81,100.9) and (146.69,101.74) .. (146.57,102.58) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (146.75,102.22) .. controls (145.67,103.24) and (144.59,104.26) .. (143.51,105.28) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (145.49,101.32) .. controls (144.95,102.1) and (144.41,102.88) .. (143.87,103.66) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (141.35,101.5) .. controls (141.29,102.1) and (141.23,102.7) .. (141.17,103.3) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (143.51,101.14) .. controls (143.45,102.4) and (143.39,103.66) .. (143.33,104.92) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (141.17,102.22) .. controls (141.65,103.24) and (142.13,104.26) .. (142.61,105.28) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (140.99,103.66) .. controls (141.77,104.62) and (142.55,105.58) .. (143.33,106.54) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (168.7,111.94) .. controls (168.04,112.54) and (167.38,113.14) .. (166.72,113.74) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (167.44,114.27) .. controls (167.8,115.05) and (168.16,115.83) .. (168.52,116.61) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (168.34,113.74) .. controls (168.88,114.45) and (169.42,115.17) .. (169.96,115.89) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (171.94,115.35) .. controls (170.5,116.25) and (169.06,117.15) .. (167.62,118.05) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (168.52,115.89) .. controls (167.8,116.37) and (167.08,116.85) .. (166.36,117.33) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (166.72,116.61) .. controls (165.7,116.55) and (164.68,116.49) .. (163.66,116.43) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (163.66,116.79) .. controls (164.08,117.87) and (164.5,118.95) .. (164.92,120.03) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (165.64,120.21) .. controls (166.6,119.49) and (167.56,118.77) .. (168.52,118.05) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (167.08,119.49) .. controls (166.78,119.13) and (166.48,118.77) .. (166.18,118.41) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (165.46,118.41) .. controls (165.95,118.06) and (166.9,117.75) .. (167.26,118.23) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (166.54,118.59) .. controls (167.26,117.93) and (167.98,117.27) .. (168.7,116.61) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (174.28,109.06) .. controls (174.7,108.52) and (175.12,107.98) .. (175.54,107.44) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (175.54,107.26) .. controls (175.6,106.9) and (175.66,106.54) .. (175.72,106.18) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (176.62,106.54) .. controls (177.22,107.5) and (177.82,108.46) .. (178.42,109.42) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (176.98,108.7) .. controls (177.28,109.24) and (177.58,109.78) .. (177.88,110.32) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (178.6,108.52) .. controls (179.92,110.74) and (181.24,112.96) .. (182.55,115.17) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (179.86,111.94) .. controls (181.12,113.86) and (182.37,115.77) .. (183.63,117.69) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (182.37,114.45) .. controls (183.15,116.01) and (183.93,117.57) .. (184.71,119.13) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (181.12,115.71) .. controls (181.72,116.85) and (182.31,117.99) .. (182.91,119.13) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (180.58,113.92) .. controls (180.46,115.05) and (180.34,116.19) .. (180.22,117.33) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (177.88,114.45) .. controls (179.57,117.09) and (179.94,117.87) .. (179.32,116.61) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (174.1,114.99) .. controls (174.94,116.19) and (175.78,117.39) .. (176.62,118.59) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (174.1,115.89) .. controls (174.28,116.31) and (174.46,116.73) .. (174.64,117.15) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (173.74,115.53) .. controls (174.64,116.55) and (175.54,117.57) .. (176.44,118.59) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (175,117.69) .. controls (175.36,117.87) and (175.72,118.05) .. (176.08,118.23) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (175.54,117.33) .. controls (174.34,116.85) and (173.14,116.37) .. (171.94,115.89) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (180.58,125.07) .. controls (180.94,124.41) and (181.3,123.75) .. (181.66,123.09) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (181.48,125.61) .. controls (182.25,125.07) and (183.03,124.53) .. (183.81,123.99) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (182.19,123.27) .. controls (183.27,123.69) and (184.35,124.11) .. (185.43,124.53) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (183.99,123.99) .. controls (186.77,122.88) and (187.38,123.6) .. (186.51,122.73) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (187.23,124.71) .. controls (186.99,124.05) and (186.75,123.39) .. (186.51,122.73) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (185.43,120.03) .. controls (185.85,120.81) and (186.27,121.59) .. (186.69,122.37) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (179.32,157.46) .. controls (179.8,158.66) and (180.28,159.86) .. (180.76,161.06) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (184.98,154.08) .. controls (183.96,156.33) and (182.95,158.58) .. (181.93,160.84) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (180.94,159.62) .. controls (180.64,161.12) and (180.34,162.62) .. (180.04,164.12) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (180.58,161.6) .. controls (180.58,162.44) and (180.58,163.28) .. (180.58,164.12) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (174.1,103.48) .. controls (172.9,102.4) and (171.7,101.32) .. (170.5,100.24) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (170.32,99.88) .. controls (169.72,100.18) and (169.12,100.48) .. (168.52,100.78) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (168.34,101.32) .. controls (167.74,102.58) and (167.14,103.84) .. (166.54,105.1) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (166.54,105.1) .. controls (167.2,105.7) and (167.86,106.3) .. (168.52,106.9) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (168.52,106.9) .. controls (169.48,106.84) and (170.44,106.78) .. (171.4,106.72) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (171.4,106.54) .. controls (171.04,104.8) and (170.68,103.06) .. (170.32,101.32) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (169.96,101.5) .. controls (169.78,102.82) and (169.6,104.14) .. (169.42,105.46) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (169.24,102.22) .. controls (168.94,103.3) and (168.64,104.38) .. (168.34,105.46) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (168.52,105.46) .. controls (169.12,105.64) and (169.72,105.82) .. (170.32,106) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (171.76,102.76) .. controls (172.84,103.72) and (173.92,104.68) .. (175,105.64) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (169.96,104.74) .. controls (169.78,105.04) and (169.6,105.34) .. (169.42,105.64) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (167.8,104.92) .. controls (168.04,105.22) and (168.28,105.52) .. (168.52,105.82) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (171.4,107.44) .. controls (171.34,107.62) and (171.28,107.8) .. (171.22,107.98) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (162.76,107.08) .. controls (164.02,108.16) and (165.28,109.24) .. (166.54,110.32) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (163.48,107.8) .. controls (162.7,108.16) and (161.92,108.52) .. (161.14,108.88) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (161.14,109.24) .. controls (161.2,109.78) and (161.26,110.32) .. (161.32,110.86) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (161.68,110.86) .. controls (162.4,110.14) and (163.12,109.42) .. (163.84,108.7) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (164.2,109.24) .. controls (164.8,109.72) and (165.4,110.2) .. (166,110.68) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (166,110.86) .. controls (165.64,111.1) and (165.28,111.34) .. (164.92,111.58) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (124.08,130.83) .. controls (125.46,130.83) and (126.84,130.83) .. (128.22,130.83) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (126.78,131.19) .. controls (127.86,131.37) and (128.94,131.55) .. (130.02,131.73) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (126.78,131.19) .. controls (126.66,131.19) and (126.54,131.19) .. (126.42,131.19) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (132.53,131.91) .. controls (132.59,131.91) and (132.65,131.91) .. (132.71,131.91) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=1.5] [line join = round][line cap = round] (123.54,132.27) .. controls (123.66,132.27) and (123.78,132.27) .. (123.9,132.27) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=4.5] [line join = round][line cap = round] (121.02,114.45) .. controls (123.54,114.63) and (126.06,114.81) .. (128.58,114.99) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=4.5] [line join = round][line cap = round] (133.25,110.32) .. controls (134.03,110.26) and (134.81,110.2) .. (135.59,110.14) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=4.5] [line join = round][line cap = round] (120.12,120.93) .. controls (120.48,121.47) and (120.84,122.01) .. (121.2,122.55) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=4.5] [line join = round][line cap = round] (171.4,114.81) .. controls (172.12,114.93) and (172.84,115.05) .. (173.56,115.17) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=4.5] [line join = round][line cap = round] (166.9,117.69) .. controls (166.48,117.63) and (166.06,117.57) .. (165.64,117.51) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=4.5] [line join = round][line cap = round] (168.88,103.66) .. controls (168.52,103.66) and (168.16,103.66) .. (167.8,103.66) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=4.5] [line join = round][line cap = round] (168.88,103.84) .. controls (169.18,103.6) and (169.48,103.36) .. (169.78,103.12) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=4.5] [line join = round][line cap = round] (179.14,113.02) .. controls (179.5,113.68) and (179.86,114.33) .. (180.22,114.99) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=4.5] [line join = round][line cap = round] (186.69,135.69) .. controls (186.81,137.37) and (186.93,139.05) .. (187.05,140.72) ;
            	\draw  [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=4.5] [line join = round][line cap = round] (186.51,142.52) .. controls (186.45,143.84) and (186.39,145.16) .. (186.33,146.48) ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.21 ] (113.62,135.42) .. controls (107.98,124.41) and (114.42,109.85) .. (128,102.89) .. controls (141.59,95.92) and (157.17,99.21) .. (162.82,110.22) .. controls (168.46,121.23) and (162.02,135.8) .. (148.44,142.76) .. controls (134.85,149.72) and (119.27,146.44) .. (113.62,135.42) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.2 ] (102.86,149.61) .. controls (93.23,130.82) and (102.66,106.76) .. (123.91,95.87) .. controls (145.17,84.98) and (170.2,91.38) .. (179.83,110.17) .. controls (189.46,128.95) and (180.03,153.01) .. (158.77,163.9) .. controls (137.52,174.79) and (112.48,168.39) .. (102.86,149.61) -- cycle ;
            	\draw  [line width=0.75]  (97.7,136.91) .. controls (97.7,111.51) and (118.29,90.92) .. (143.69,90.92) .. controls (169.09,90.92) and (189.68,111.51) .. (189.68,136.91) .. controls (189.68,162.31) and (169.09,182.9) .. (143.69,182.9) .. controls (118.29,182.9) and (97.7,162.31) .. (97.7,136.91) -- cycle ;
            	\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.24 ] (131.52,74.75) -- (209.62,87.87) -- (146.08,103.97) -- (67.98,90.85) -- cycle ;
            	\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.19 ] (67.98,90.85) -- (146.08,103.97) -- (147.2,196.56) -- (68,178.96) -- cycle ;
            	\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.27 ] (146.08,103.97) -- (209.62,87.87) -- (209.6,175.36) -- (147.2,196.56) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.38 ] (67.98,90.85) -- (81.2,93.36) -- (107.6,187.76) -- (79.2,180.96) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.38 ] (99.2,96.96) -- (104.4,98.16) -- (127.2,191.36) -- (111.2,187.76) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.38 ] (118.38,98.85) -- (131.6,101.36) -- (146.4,159.76) -- (146.4,180.16) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.38 ] (157.43,101.01) -- (177.85,95.92) -- (157.05,192.32) -- (149.85,195.52) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.38 ] (185.6,95.76) -- (191.88,92.42) -- (178.4,185.96) -- (165.6,188.96) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.38 ] (203.35,91.2) -- (209.62,87.87) -- (209.6,175.36) -- (187.2,182.56) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.38 ] (131.52,74.75) -- (144.74,77.26) -- (146.08,103.97) -- (71.6,90.56) -- cycle ;
            \end{tikzpicture}'''
                # Câu hỏi
                noidungcauhoi = (r'''\immini{Trong khối pha lê hình lập phương $ABCD.A'B'C'D'$ cạnh $%s$ cm có mặt cầu cách đều các mặt của hình lập phương $ABCD.A'B'C'D'$ một khoảng $%s$ cm. Chọn hệ trục tọa độ $Oxyz$ sao cho đỉnh $A$ trùng với gốc tọa độ $O$, đỉnh $B$ thuộc tia $Ox$, đỉnh $D$ thuộc tia $Oy$, đỉnh $A'$ thuộc tia $Oz$. Gọi $I\left(a; b; c\right)$ là tọa độ tâm của mặt cầu nói trên. Tổng $S = a + b + c$ bằng bao nhiêu?}{%s}'''
                                 %(latex(L), latex(d),hinhve))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Theo giả thiết, hình lập phương $ABCD.A'B'C'D'$ có cạnh bằng $%s$. \\\\
                            Chọn hệ trục tọa độ $Oxyz$ với $A\\left(0; 0; 0\\right)$, $B\\left(%s; 0; 0\\right)$, $D\\left(0; %s; 0\\right)$, $A'\\left(0; 0; %s\\right)$. \\\\
                            Vì mặt cầu nằm trong và cách đều các mặt của hình lập phương nên tâm $I$ của mặt cầu trùng với tâm của hình lập phương. \\\\
                            Tâm của hình lập phương có tọa độ là $I\\left(\\frac{%s}{2}; \\frac{%s}{2}; \\frac{%s}{2}\\right)$ hay $I\\left(%s; %s; %s\\right)$. \\\\
                            Suy ra $a = %s$, $b = %s$, $c = %s$. \\\\
                            Vậy tổng $S = a + b + c = %s + %s + %s = %s$.'''
                           %(latex(L),
                             latex(L), latex(L), latex(L),
                             latex(L), latex(L), latex(L),
                             latex(toado), latex(toado), latex(toado),
                             latex(toado), latex(toado), latex(toado),
                             latex(toado), latex(toado), latex(toado), latex(tong_S)))
                dapan='\\shortans[0]{$%s$}\n'%(latex(tong_S))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+dapan+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content


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


def bt_dang44_p4_b6_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # --- B3: Ngẫu nhiên hóa bài toán ---
                # h1: Chiều cao thân (20-30m), a: cạnh đáy dưới (50-60m), b: cạnh đáy trên (20-30m)
                h1 = randint(20, 30)
                a = randint(50, 60)
                b = randint(20, 30)

                # h2: Chiều cao đền (5-8m), c: cạnh đáy đền (10-15m)
                h2 = randint(5, 8)
                c = randint(10, 18) 
                # Đảm bảo đền nhỏ hơn mặt bằng đáy trên
                if c >= b: c = b - 5

                # --- Tính toán giải thuật ---
                s1 = a * a
                s2 = b * b
                # Thể tích hình chóp cụt V1 = 1/3 * h1 * (s1 + s2 + sqrt(s1*s2))
                # Vì đáy là hình vuông nên sqrt(s1*s2) = a*b
                v1 = Rational(h1, 3) * (s1 + s2 + a * b)

                # Thể tích khối đền V2 = s_den * h2
                s_den = c * c
                v2 = s_den * h2

                # Tổng thể tích
                v_tong = v1 + v2

                # Chuyển sang số thập phân để làm đáp án trắc nghiệm
                v_val = float(v_tong)
                kq_float = Decimal(str(v_val)).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
                kq = str(kq_float).replace('.', ',')

                # --- B4: Tạo các phương án sai không trùng đáp án đúng ---
                da = '$%s$' % kq

                s = set()
                while len(s) < 3:
                    # Tạo sai số ngẫu nhiên từ 100 đến 500 đơn vị
                    sai_so = random.choice([100, 150, 200, 250, 300, -100, -150, -200])
                    phuong_an_sai = float(kq_float) + sai_so
                    if phuong_an_sai > 0 and phuong_an_sai != float(kq_float):
                        val_sai = Decimal(str(phuong_an_sai)).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
                        s.add('$%s$' % str(val_sai).replace('.', ','))

                list_s = list(s)
                das1, das2, das3 = list_s[0], list_s[1], list_s[2]

                hinhve=r'''\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-0.8,xscale=0.8]
            	\draw  [draw opacity=0][fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (341.39,211.44) -- (314.27,198.11) -- (60.05,197.44) -- (50.72,204.11) -- (29.39,213.44) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 65; green, 117; blue, 5 }  ,fill opacity=1 ] (139.39,212.11) -- (224.17,197.93) -- (60.05,197.44) -- (50.72,204.11) -- (29.39,213.44) -- cycle ;
            	\draw  [fill={rgb, 255:red, 179; green, 177; blue, 177 }  ,fill opacity=1 ] (207.43,97.07) -- (208.43,114.57) -- (177.93,109.07) -- (177.93,90.57) -- cycle ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (177.93,90.57) -- (177.93,109.07) -- (155.93,114.07) -- (155.43,102.57) -- cycle ;
            	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (208.43,114.57) -- (208.08,118.07) -- (177.83,113.57) -- (177.93,109.07) -- cycle ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (177.93,109.07) -- (177.83,113.57) -- (155.58,117.82) -- (155.93,114.07) -- cycle ;
            	\draw  [fill={rgb, 255:red, 179; green, 177; blue, 177 }  ,fill opacity=1 ] (295.83,194.07) -- (300.08,202.07) -- (267.33,201.62) -- (261.33,193.82) -- cycle ;
            	\draw  [fill={rgb, 255:red, 179; green, 177; blue, 177 }  ,fill opacity=1 ] (285.83,185.32) -- (290.83,193.82) -- (261.33,193.82) -- (255.83,185.07) -- cycle ;
            	\draw  [fill={rgb, 255:red, 179; green, 177; blue, 177 }  ,fill opacity=1 ] (274.58,176.57) -- (279.58,185.07) -- (255.83,185.07) -- (249.08,176.07) -- cycle ;
            	\draw  [fill={rgb, 255:red, 179; green, 177; blue, 177 }  ,fill opacity=1 ] (264.58,167.57) -- (269.58,176.07) -- (249.08,176.07) -- (243.58,167.07) -- cycle ;
            	\draw  [fill={rgb, 255:red, 179; green, 177; blue, 177 }  ,fill opacity=1 ] (255.08,157.82) -- (259.58,167.07) -- (243.58,167.07) -- (237.08,158.07) -- cycle ;
            	\draw  [fill={rgb, 255:red, 179; green, 177; blue, 177 }  ,fill opacity=1 ] (244.33,148.82) -- (248.83,158.07) -- (237.08,158.07) -- (230.58,149.07) -- cycle ;
            	\draw  [fill={rgb, 255:red, 179; green, 177; blue, 177 }  ,fill opacity=1 ] (235.08,139.07) -- (239.58,148.32) -- (230.58,149.07) -- (223.58,139.07) -- cycle ;
            	\draw  [fill={rgb, 255:red, 179; green, 177; blue, 177 }  ,fill opacity=1 ] (224.58,129.07) -- (229.83,138.57) -- (223.58,139.07) -- (216.83,129.07) -- cycle ;
            	\draw  [fill={rgb, 255:red, 179; green, 177; blue, 177 }  ,fill opacity=1 ] (215.08,120.32) -- (219.58,129.57) -- (216.83,129.07) -- (210.33,120.57) -- cycle ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (182.08,114.37) -- (237.33,203.62) -- (214.33,201.32) -- (180.08,113.82) -- cycle ;
            	\draw  [fill={rgb, 255:red, 179; green, 177; blue, 177 }  ,fill opacity=1 ] (218.83,190.57) -- (221.08,202.07) -- (149.08,202.07) -- (152.58,190.32) -- cycle ;
            	\draw  [fill={rgb, 255:red, 179; green, 177; blue, 177 }  ,fill opacity=1 ] (214.33,180.62) -- (216.33,190.37) -- (153.83,190.07) -- (156.83,180.57) -- cycle ;
            	\draw  [fill={rgb, 255:red, 179; green, 177; blue, 177 }  ,fill opacity=1 ] (207.83,170.87) -- (209.83,180.62) -- (156.83,180.57) -- (159.83,168.82) -- cycle ;
            	\draw  [fill={rgb, 255:red, 179; green, 177; blue, 177 }  ,fill opacity=1 ] (202.83,160.37) -- (204.58,170.32) -- (159.83,168.82) -- (162.33,157.32) -- cycle ;
            	\draw  [fill={rgb, 255:red, 179; green, 177; blue, 177 }  ,fill opacity=1 ] (198.33,151.12) -- (199.83,159.57) -- (162.33,157.32) -- (164.83,148.07) -- cycle ;
            	\draw  [fill={rgb, 255:red, 179; green, 177; blue, 177 }  ,fill opacity=1 ] (194.33,141.62) -- (195.08,150.57) -- (164.83,148.07) -- (167.08,138.32) -- cycle ;
            	\draw  [fill={rgb, 255:red, 179; green, 177; blue, 177 }  ,fill opacity=1 ] (189.83,131.87) -- (190.58,140.82) -- (167.08,138.32) -- (170.08,129.07) -- cycle ;
            	\draw  [fill={rgb, 255:red, 179; green, 177; blue, 177 }  ,fill opacity=1 ] (185.33,122.12) -- (186.08,131.07) -- (170.08,129.07) -- (172.33,120.82) -- cycle ;
            	\draw  [fill={rgb, 255:red, 179; green, 177; blue, 177 }  ,fill opacity=1 ] (180.08,113.82) -- (182.58,121.82) -- (172.33,120.82) -- (174.83,114.07) -- cycle ;
            	\draw  [fill={rgb, 255:red, 102; green, 100; blue, 100 }  ,fill opacity=1 ] (166.71,115.69) -- (111.33,202.57) -- (91.33,204.32) -- (164.83,116.07) -- cycle ;
            	\draw  [fill={rgb, 255:red, 143; green, 142; blue, 142 }  ,fill opacity=1 ] (174.83,114.07) -- (172.33,120.82) -- (161.08,124.07) -- (166.71,115.69) -- cycle ;
            	\draw  [fill={rgb, 255:red, 143; green, 141; blue, 141 }  ,fill opacity=1 ] (172.33,120.82) -- (170.08,129.07) -- (155.08,134.07) -- (159.33,124.57) -- cycle ;
            	\draw  [fill={rgb, 255:red, 153; green, 150; blue, 150 }  ,fill opacity=1 ] (170.08,129.07) -- (167.08,138.32) -- (148.33,144.57) -- (152.83,133.82) -- cycle ;
            	\draw  [fill={rgb, 255:red, 141; green, 140; blue, 140 }  ,fill opacity=1 ] (167.08,138.32) -- (164.83,148.07) -- (141.33,154.82) -- (144.83,145.07) -- cycle ;
            	\draw  [fill={rgb, 255:red, 138; green, 136; blue, 136 }  ,fill opacity=1 ] (164.83,148.07) -- (162.33,157.32) -- (135.83,163.07) -- (137.83,154.82) -- cycle ;
            	\draw  [fill={rgb, 255:red, 138; green, 136; blue, 136 }  ,fill opacity=1 ] (162.33,157.32) -- (159.83,168.82) -- (130.08,172.82) -- (131.58,163.07) -- cycle ;
            	\draw  [fill={rgb, 255:red, 138; green, 136; blue, 136 }  ,fill opacity=1 ] (159.83,168.82) -- (156.83,180.57) -- (122.83,184.07) -- (124.83,173.07) -- cycle ;
            	\draw  [fill={rgb, 255:red, 138; green, 137; blue, 137 }  ,fill opacity=1 ] (156.83,180.57) -- (153.83,190.07) -- (117.33,192.07) -- (119.33,182.32) -- cycle ;
            	\draw  [fill={rgb, 255:red, 157; green, 155; blue, 155 }  ,fill opacity=1 ] (152.58,190.32) -- (149.08,202.07) -- (111.33,202.57) -- (113.08,192.57) -- cycle ;
            	\draw  [fill={rgb, 255:red, 179; green, 177; blue, 177 }  ,fill opacity=1 ] (155.58,119.07) -- (150.08,129.07) -- (142.58,130.07) -- (144.33,121.07) -- cycle ;
            	\draw  [fill={rgb, 255:red, 179; green, 177; blue, 177 }  ,fill opacity=1 ] (146.83,129.07) -- (141.33,139.07) -- (133.83,140.07) -- (135.58,131.07) -- cycle ;
            	\draw  [fill={rgb, 255:red, 179; green, 177; blue, 177 }  ,fill opacity=1 ] (137.83,140.07) -- (132.33,150.07) -- (124.08,152.32) -- (126.58,142.07) -- cycle ;
            	\draw  [fill={rgb, 255:red, 179; green, 177; blue, 177 }  ,fill opacity=1 ] (128.83,149.57) -- (123.33,159.57) -- (115.08,161.82) -- (117.58,151.57) -- cycle ;
            	\draw  [fill={rgb, 255:red, 179; green, 177; blue, 177 }  ,fill opacity=1 ] (121.08,158.57) -- (115.58,168.57) -- (107.33,170.82) -- (109.83,160.57) -- cycle ;
            	\draw  [fill={rgb, 255:red, 179; green, 177; blue, 177 }  ,fill opacity=1 ] (112.08,168.07) -- (106.58,178.07) -- (98.33,180.32) -- (100.83,170.07) -- cycle ;
            	\draw  [fill={rgb, 255:red, 179; green, 177; blue, 177 }  ,fill opacity=1 ] (103.83,178.07) -- (101.08,185.57) -- (91.33,186.82) -- (92.58,180.07) -- cycle ;
            	\draw  [fill={rgb, 255:red, 179; green, 177; blue, 177 }  ,fill opacity=1 ] (95.58,185.82) -- (94.33,192.32) -- (83.08,193.32) -- (84.33,187.82) -- cycle ;
            	\draw  [fill={rgb, 255:red, 179; green, 177; blue, 177 }  ,fill opacity=1 ] (88.83,193.07) -- (84.33,202.07) -- (74.83,202.07) -- (75.83,194.07) -- cycle ;
            	\draw [color={rgb, 255:red, 222; green, 216; blue, 216 }  ,draw opacity=1 ]   (178.93,106.4) -- (208.27,112.07) ;
            	\draw [color={rgb, 255:red, 222; green, 216; blue, 216 }  ,draw opacity=1 ]   (178.6,94.73) -- (207.93,100.4) ;
            	\draw [color={rgb, 255:red, 147; green, 145; blue, 145 }  ,draw opacity=1 ]   (155.83,105.07) -- (178.6,94.73) ;
            	\draw [color={rgb, 255:red, 222; green, 216; blue, 216 }  ,draw opacity=1 ]   (153.83,190.07) -- (218.83,190.57) ;
            	\draw [color={rgb, 255:red, 89; green, 87; blue, 87 }  ,draw opacity=1 ]   (152.27,193.07) -- (218.6,193.07) ;
            	\draw [color={rgb, 255:red, 222; green, 216; blue, 216 }  ,draw opacity=1 ]   (156.83,180.57) -- (214.33,180.62) ;
            	\draw [color={rgb, 255:red, 222; green, 216; blue, 216 }  ,draw opacity=1 ]   (159.83,168.82) -- (207.83,170.87) ;
            	\draw [color={rgb, 255:red, 222; green, 216; blue, 216 }  ,draw opacity=1 ]   (162.33,157.32) -- (202.83,160.37) ;
            	\draw [color={rgb, 255:red, 222; green, 216; blue, 216 }  ,draw opacity=1 ]   (164.83,148.07) -- (198.33,151.12) ;
            	\draw [color={rgb, 255:red, 222; green, 216; blue, 216 }  ,draw opacity=1 ]   (167.08,138.32) -- (194.33,141.62) ;
            	\draw [color={rgb, 255:red, 222; green, 216; blue, 216 }  ,draw opacity=1 ]   (170.08,129.07) -- (189.83,131.87) ;
            	\draw [color={rgb, 255:red, 222; green, 216; blue, 216 }  ,draw opacity=1 ]   (172.33,120.82) -- (185.33,122.12) ;
            	\draw [color={rgb, 255:red, 222; green, 216; blue, 216 }  ,draw opacity=1 ]   (174.83,114.07) -- (180.08,113.82) ;
            	\draw [color={rgb, 255:red, 89; green, 87; blue, 87 }  ,draw opacity=1 ]   (156.83,182.57) -- (214.85,182.82) ;
            	\draw [color={rgb, 255:red, 89; green, 87; blue, 87 }  ,draw opacity=1 ]   (159.58,170.82) -- (208.1,172.82) ;
            	\draw [color={rgb, 255:red, 89; green, 87; blue, 87 }  ,draw opacity=1 ]   (162.33,159.82) -- (202.83,162.57) ;
            	\draw [color={rgb, 255:red, 89; green, 87; blue, 87 }  ,draw opacity=1 ]   (165.08,150.07) -- (199.08,153.07) ;
            	\draw [color={rgb, 255:red, 89; green, 87; blue, 87 }  ,draw opacity=1 ]   (166.83,140.57) -- (194.1,143.32) ;
            	\draw [color={rgb, 255:red, 89; green, 87; blue, 87 }  ,draw opacity=1 ]   (170.08,131.57) -- (189.83,133.82) ;
            	\draw [color={rgb, 255:red, 89; green, 87; blue, 87 }  ,draw opacity=1 ]   (172.58,123.07) -- (184.58,124.07) ;
            	\draw [color={rgb, 255:red, 89; green, 87; blue, 87 }  ,draw opacity=1 ]   (175.08,116.07) -- (179.83,115.82) ;
            	\draw [color={rgb, 255:red, 89; green, 87; blue, 87 }  ,draw opacity=1 ]   (178.58,97.07) -- (207.83,102.57) ;
            	\draw [color={rgb, 255:red, 50; green, 48; blue, 48 }  ,draw opacity=1 ]   (155.33,107.07) -- (178.58,97.07) ;
            	\draw [color={rgb, 255:red, 147; green, 145; blue, 145 }  ,draw opacity=1 ]   (156.08,111.57) -- (178.27,106.07) ;
            	\draw [color={rgb, 255:red, 222; green, 216; blue, 216 }  ,draw opacity=1 ]   (261.33,193.82) -- (295.83,194.07) ;
            	\draw [color={rgb, 255:red, 222; green, 216; blue, 216 }  ,draw opacity=1 ]   (231.78,166.82) -- (264.58,167.57) ;
            	\draw [color={rgb, 255:red, 222; green, 216; blue, 216 }  ,draw opacity=1 ]   (247.78,185.07) -- (285.83,185.32) ;
            	\draw [color={rgb, 255:red, 222; green, 216; blue, 216 }  ,draw opacity=1 ]   (236.53,176.32) -- (274.58,176.57) ;
            	\draw [color={rgb, 255:red, 222; green, 216; blue, 216 }  ,draw opacity=1 ]   (222.28,158.32) -- (255.08,157.82) ;
            	\draw [color={rgb, 255:red, 222; green, 216; blue, 216 }  ,draw opacity=1 ]   (223.53,148.82) -- (244.33,148.82) ;
            	\draw [color={rgb, 255:red, 222; green, 216; blue, 216 }  ,draw opacity=1 ]   (217.53,138.82) -- (235.08,139.07) ;
            	\draw [color={rgb, 255:red, 222; green, 216; blue, 216 }  ,draw opacity=1 ]   (211.03,128.82) -- (224.58,129.07) ;
            	\draw [color={rgb, 255:red, 89; green, 87; blue, 87 }  ,draw opacity=1 ]   (259.03,195.57) -- (296.35,196.07) ;
            	\draw [color={rgb, 255:red, 89; green, 87; blue, 87 }  ,draw opacity=1 ]   (249.53,187.07) -- (286.85,187.57) ;
            	\draw [color={rgb, 255:red, 89; green, 87; blue, 87 }  ,draw opacity=1 ]   (237.78,178.57) -- (275.1,179.07) ;
            	\draw [color={rgb, 255:red, 89; green, 87; blue, 87 }  ,draw opacity=1 ]   (228.03,169.07) -- (265.35,169.57) ;
            	\draw [color={rgb, 255:red, 89; green, 87; blue, 87 }  ,draw opacity=1 ]   (227.03,160.32) -- (256.28,160.07) ;
            	\draw [color={rgb, 255:red, 89; green, 87; blue, 87 }  ,draw opacity=1 ]   (221.28,151.07) -- (245.78,151.07) ;
            	\draw [color={rgb, 255:red, 89; green, 87; blue, 87 }  ,draw opacity=1 ]   (215.78,140.57) -- (235.78,140.82) ;
            	\draw [color={rgb, 255:red, 89; green, 87; blue, 87 }  ,draw opacity=1 ]   (213.03,131.07) -- (225.53,131.07) ;
            	\draw [color={rgb, 255:red, 222; green, 216; blue, 216 }  ,draw opacity=1 ]   (113.08,192.57) -- (153.83,190.07) ;
            	\draw [color={rgb, 255:red, 222; green, 216; blue, 216 }  ,draw opacity=1 ]   (119.33,182.32) -- (156.83,180.57) ;
            	\draw [color={rgb, 255:red, 222; green, 216; blue, 216 }  ,draw opacity=1 ]   (126.03,173.57) -- (159.83,168.82) ;
            	\draw [color={rgb, 255:red, 222; green, 216; blue, 216 }  ,draw opacity=1 ]   (131.58,163.07) -- (162.33,157.32) ;
            	\draw [color={rgb, 255:red, 222; green, 216; blue, 216 }  ,draw opacity=1 ]   (137.83,154.82) -- (164.83,148.07) ;
            	\draw [color={rgb, 255:red, 222; green, 216; blue, 216 }  ,draw opacity=1 ]   (144.83,145.07) -- (167.08,138.32) ;
            	\draw [color={rgb, 255:red, 222; green, 216; blue, 216 }  ,draw opacity=1 ]   (152.83,133.82) -- (170.08,129.07) ;
            	\draw [color={rgb, 255:red, 222; green, 216; blue, 216 }  ,draw opacity=1 ]   (159.33,124.57) -- (172.33,120.82) ;
            	\draw [color={rgb, 255:red, 222; green, 216; blue, 216 }  ,draw opacity=1 ]   (166.71,115.69) -- (174.83,114.07) ;
            	\draw [color={rgb, 255:red, 89; green, 87; blue, 87 }  ,draw opacity=1 ]   (113.03,195.32) -- (152.27,193.07) ;
            	\draw [color={rgb, 255:red, 89; green, 87; blue, 87 }  ,draw opacity=1 ]   (119.03,184.32) -- (156.83,182.57) ;
            	\draw [color={rgb, 255:red, 89; green, 87; blue, 87 }  ,draw opacity=1 ]   (126.03,143.82) -- (141.53,140.82) ;
            	\draw [color={rgb, 255:red, 89; green, 87; blue, 87 }  ,draw opacity=1 ]   (131.53,165.07) -- (162.33,159.82) ;
            	\draw [color={rgb, 255:red, 89; green, 87; blue, 87 }  ,draw opacity=1 ][fill={rgb, 255:red, 138; green, 136; blue, 136 }  ,fill opacity=1 ]   (138.53,156.57) -- (165.08,150.07) ;
            	\draw [color={rgb, 255:red, 89; green, 87; blue, 87 }  ,draw opacity=1 ][fill={rgb, 255:red, 138; green, 136; blue, 136 }  ,fill opacity=1 ]   (144.78,147.07) -- (166.83,140.57) ;
            	\draw [color={rgb, 255:red, 89; green, 87; blue, 87 }  ,draw opacity=1 ][fill={rgb, 255:red, 138; green, 136; blue, 136 }  ,fill opacity=1 ]   (152.53,135.82) -- (170.08,131.57) ;
            	\draw [color={rgb, 255:red, 89; green, 87; blue, 87 }  ,draw opacity=1 ][fill={rgb, 255:red, 138; green, 136; blue, 136 }  ,fill opacity=1 ]   (158.53,126.32) -- (172.58,123.07) ;
            	\draw [color={rgb, 255:red, 89; green, 87; blue, 87 }  ,draw opacity=1 ][fill={rgb, 255:red, 138; green, 136; blue, 136 }  ,fill opacity=1 ]   (166.03,117.57) -- (175.08,116.07) ;
            	\draw [color={rgb, 255:red, 89; green, 87; blue, 87 }  ,draw opacity=1 ]   (75.78,196.07) -- (90.28,195.07) ;
            	\draw [color={rgb, 255:red, 89; green, 87; blue, 87 }  ,draw opacity=1 ]   (84.28,189.32) -- (98.53,187.07) ;
            	\draw [color={rgb, 255:red, 89; green, 87; blue, 87 }  ,draw opacity=1 ]   (92.28,181.57) -- (107.53,179.07) ;
            	\draw [color={rgb, 255:red, 89; green, 87; blue, 87 }  ,draw opacity=1 ]   (100.28,172.07) -- (118.03,169.07) ;
            	\draw [color={rgb, 255:red, 89; green, 87; blue, 87 }  ,draw opacity=1 ]   (109.53,162.57) -- (124.53,160.07) ;
            	\draw [color={rgb, 255:red, 89; green, 87; blue, 87 }  ,draw opacity=1 ]   (118.03,153.07) -- (133.53,150.57) ;
            	\draw [color={rgb, 255:red, 89; green, 87; blue, 87 }  ,draw opacity=1 ]   (135.03,133.07) -- (150.03,130.07) ;
            	\draw [color={rgb, 255:red, 89; green, 87; blue, 87 }  ,draw opacity=1 ]   (143.78,122.82) -- (158.03,120.82) ;
            	\draw [color={rgb, 255:red, 222; green, 216; blue, 216 }  ,draw opacity=1 ]   (75.83,194.07) -- (88.83,193.07) ;
            	\draw [color={rgb, 255:red, 222; green, 216; blue, 216 }  ,draw opacity=1 ]   (84.33,187.82) -- (95.58,185.82) ;
            	\draw [color={rgb, 255:red, 222; green, 216; blue, 216 }  ,draw opacity=1 ]   (92.58,180.07) -- (103.83,178.07) ;
            	\draw [color={rgb, 255:red, 222; green, 216; blue, 216 }  ,draw opacity=1 ]   (100.83,170.07) -- (112.08,168.07) ;
            	\draw [color={rgb, 255:red, 222; green, 216; blue, 216 }  ,draw opacity=1 ]   (109.83,160.57) -- (121.08,158.57) ;
            	\draw [color={rgb, 255:red, 222; green, 216; blue, 216 }  ,draw opacity=1 ]   (117.58,151.57) -- (128.83,149.57) ;
            	\draw [color={rgb, 255:red, 222; green, 216; blue, 216 }  ,draw opacity=1 ]   (126.58,142.07) -- (137.83,140.07) ;
            	\draw [color={rgb, 255:red, 222; green, 216; blue, 216 }  ,draw opacity=1 ]   (135.58,131.07) -- (146.83,129.07) ;
            	\draw [color={rgb, 255:red, 222; green, 216; blue, 216 }  ,draw opacity=1 ]   (144.33,121.07) -- (157.03,118.82) ;
            	\draw  [fill={rgb, 255:red, 140; green, 137; blue, 137 }  ,fill opacity=1 ] (164.83,116.07) -- (91.33,204.32) -- (77.83,204.57) -- (150.83,119.07) -- cycle ;
            	\draw [color={rgb, 255:red, 222; green, 216; blue, 216 }  ,draw opacity=1 ]   (152.58,118.07) -- (79.58,203.57) ;
            	\draw [color={rgb, 255:red, 222; green, 216; blue, 216 }  ,draw opacity=1 ]   (161.35,116.73) -- (88.35,204.4) ; 
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (191.96,115.82) -- (191.97,112.57) .. controls (191.97,110.78) and (193.08,109.31) .. (194.44,109.28) .. controls (195.81,109.26) and (196.91,110.69) .. (196.9,112.48) -- (196.89,115.72) -- cycle ;
            	\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ] (211.58,118.62) -- (268.58,203.62) -- (237.58,203.87) -- (182.33,114.62) -- cycle ;
            	\draw [color={rgb, 255:red, 222; green, 216; blue, 216 }  ,draw opacity=1 ]   (185.33,114.62) -- (240.58,203.87) ;
            	\draw [color={rgb, 255:red, 222; green, 216; blue, 216 }  ,draw opacity=1 ]   (208.33,118.32) -- (264.96,202.94) ; 
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (106.4,202.66) -- (106.41,199.42) .. controls (106.41,197.63) and (107.52,196.16) .. (108.88,196.13) .. controls (110.25,196.1) and (111.35,197.53) .. (111.34,199.32) -- (111.33,202.57) -- cycle ;
            	\draw  [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (221.08,201.43) -- (221.09,197.61) .. controls (221.1,195.5) and (222.48,193.94) .. (224.18,194.11) .. controls (225.88,194.28) and (227.25,196.13) .. (227.24,198.24) -- (227.23,202.06) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.51 ] (180.08,113.82) -- (221.08,201.43) -- (203.6,202.11) -- cycle ;
            \end{tikzpicture}'''

                # --- Nội dung câu hỏi ---
                noidungcauhoi = (r'''\immini{Tháp Kukulkan tại khu di tích Chichen Itza, đất nước Mexico có cấu trúc gồm hai phần: Phần thân là một hình chóp cụt tứ giác đều có chiều cao $%s$ m, cạnh đáy dưới là $%s$ m và cạnh đáy trên là $%s$ m. Phần đỉnh là một ngôi đền hình hộp chữ nhật đặt chính giữa mặt đáy trên, có chiều cao $%s$ m và đáy là hình vuông cạnh $%s$ m. Tính thể tích của toàn bộ tháp Kukulkan. (làm tròn đến hàng đơn vị).}{%s}'''
                                 % (latex(h1), latex(a), latex(b), latex(h2), latex(c),hinhve))

                # --- Nội dung lời giải ---
                loigiai = (r'''Diện tích đáy dưới của phần thân: $S_1 = %s^2 = %s$ m$^2$. \\
                           Diện tích đáy trên của phần thân: $S_2 = %s^2 = %s$ m$^2$. \\
                           Thể tích phần thân chính ($V_1$): \\
                           $V_1 = \frac{1}{3} \cdot %s \cdot (%s + %s + \sqrt{%s \cdot %s}) = %s$ m$^3$. \\
                           Diện tích đáy ngôi đền: $S_\text{đáy} = %s^2 = %s$ m$^2$. \\
                           Thể tích phần đền thờ ($V_2$): \\
                           $V_2 = %s \cdot %s = %s$ m$^3$. \\
                           Tổng thể tích của tháp: \\
                           $V = V_1 + V_2 = %s + %s \approx %s$ m$^3$.'''
                           % (latex(a), latex(s1), latex(b), latex(s2), 
                              latex(h1), latex(s1), latex(s2), latex(s1), latex(s2), latex(v1),
                              latex(c), latex(s_den), latex(s_den), latex(h2), latex(v2),
                              latex(v1), latex(v2), kq))

                # --- Đóng gói các đáp án ---
                da_d = '\\True ' + str(da)
                list_1 = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + 
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


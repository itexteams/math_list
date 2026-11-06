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


def bt_dang37_p1_b4_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random phương trình lượng giác: cos(a*x) - cos(b*x) = 0
                # Để giữ nguyên cấu trúc giải như bài mẫu (gộp về 1 họ nghiệm x = k*2pi/c), ta chọn a = 2, b = 1 (bài mẫu) hoặc a = 3, b = 1
                a = random.choice([2, 3])
                b = 1

                # cos(ax) = cos(x) <=> ax = x + k2pi hoặc ax = -x + k2pi
                # TH1: (a-1)x = k2pi <=> x = k2pi / (a-1)
                # TH2: (a+1)x = k2pi <=> x = k2pi / (a+1)
                # Họ nghiệm chung bao quát tất cả các nghiệm phân biệt trên khoảng (0, 2pi) là x = k2pi / (a+1) 
                # (Vì với k chia hết cho tỉ số tương ứng sẽ trùng nhau, gộp lại thành x = k2pi / (a+1))
                c_mau = a + 1

                # Tìm tập giá trị k nguyên sao cho 0 < k*2pi/c_mau < 2pi <=> 0 < k < c_mau
                list_k = list(range(1, c_mau))
                k_min = 0
                k_max = c_mau

                # Tính tổng các nghiệm T
                tong_nghiem = sum([Rational(k * 2, c_mau) for k in list_k]) * pi

                kq = 'T = ' + latex(tong_nghiem)

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(kq)]
                da = random.choice(du)

                # Tạo các phương án nhiễu (sai) không trùng đáp án đúng
                s = [
                    '$T = \\pi$',
                    '$T = 2\\pi$',
                    '$T = 3\\pi$',
                    '$T = \\frac{4\\pi}{3}$',
                    '$T = \\frac{7\\pi}{6}$',
                    '$T = \\frac{5\\pi}{2}$'
                ]
                # Lọc bỏ giá trị trùng với đáp án đúng
                s = [item for item in s if item != da]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Tổng tất cả các nghiệm của phương trình $\\cos %sx-\\cos x=0$ trên khoảng $\\left( 0;2\\pi  \\right)$ bằng $T$. Khi đó $T$ có giá trị là'''
                                 %(latex(a)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Xử lý chuỗi danh sách nghiệm phục vụ phần lời giải chi tiết
                str_list_k = '{' + ';'.join([str(k) for k in list_k]) + '}'
                str_list_x = '; '.join(['x = ' + latex(Rational(k * 2, c_mau)*pi) for k in list_k])
                str_tong_bnd = ' + '.join([latex(Rational(k * 2, c_mau)*pi) for k in list_k])

                # Nội dung lời giải chi tiết từng bước y hệt ảnh gốc
                loigiai = ('''Ta có: $\\cos %sx-\\cos x=0 \\Leftrightarrow \\cos %sx=\\cos x$ \\\\
                           $\\Leftrightarrow \\left[ \\begin{aligned} & %sx=x+k2\\pi  \\\\ & %sx=-x+k2\\pi  \\end{aligned} \\right. \\Leftrightarrow \\left[ \\begin{aligned} & x=k2\\pi  \\\\ & x=\\frac{k2\\pi }{%s} \\end{aligned} \\right. \\Leftrightarrow x=\\frac{k2\\pi }{%s};\\left( k\\in \\mathbb{Z} \\right)$. \\\\
                           Vì $x\\in \\left( 0;2\\pi  \\right)$ nên $0<\\frac{k2\\pi }{%s}<2\\pi  \\Leftrightarrow %s<k<%s$. \\\\
                           Do $k\\in \\mathbb{Z}$ nên $k\\in %s \\Rightarrow %s$. \\\\
                           Vậy $T=%s=%s$.'''
                           %(latex(a), latex(a), latex(a), latex(a), latex(c_mau), latex(c_mau),
                             latex(c_mau), latex(k_min), latex(k_max),
                             str_list_k, str_list_x, str_tong_bnd, latex(tong_nghiem)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


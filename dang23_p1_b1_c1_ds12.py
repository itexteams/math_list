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


def bt_dang23_p1_b1_c1_ds12(self):
            # Khai báo biến
            x = symbols('x')

            # Hàm hỗ trợ ẩn số 0 nếu trùng gốc tọa độ
            lz = lambda v: "" if v == 0 else latex(v)

            while True:
                x0 = randint(1,3)
                x1 = x0**2
                a = randint(1,9)
                c = randint(-3,3)

                hs_a = a / 4
                hs_b = -(a / 2) * x1
                hs_c = c

                f = Rational(a, 4) * x**4 - Rational(a, 2) * (x1) * x**2 +c
                f1 = round((a/4) * x0**4 - (a/2) * (x1) * x0**2 +c,1)
                y1 = Rational(a, 4) * x0**4 - Rational(a, 2) * (x1) * x0**2 +c

                if -4 <= f1 <= 4:
                    break
            while True:
                zx0 = randint(1,3)
                zx1 = zx0**2
                za = randint(-9,-1)
                zc = randint(-3, 3)

                zhs_a = za / 4
                zhs_b = -(za / 2) * zx1
                zhs_c = zc

                zf = Rational(za, 4) * x**4 - Rational(za, 2) * (zx1) * x**2 +zc
                zf1 = round((za/4) * zx0**4 - (za/2) * (zx1) * zx0**2 +zc,1)
                zy1 = Rational(za, 4) * zx0**4 - Rational(za, 2) * (zx1) * zx0**2 +zc

                if -4 <= zf1 <= 4:
                    break

            lisdang=['1','2','3','4','5','6','7','8','1','1','1','1']
            dang=random.choice(lisdang)
            if dang=='8':
                d = ['$(0;%s)$'%(latex(zc)),
                    ]
                da= random.choice(d)
                s = ['$x=%s$'%(latex(-zx0)),
                    '$x=%s$'%(latex(zy1)),
                    '$x=%s$'%(latex(zx0)),
                    '$y=%s$'%(latex(zx0)),
                    '$y=%s$'%(latex(-zx0)),
                    '$x=%s$'%(latex(zy1)),
                    '$y=%s$'%(latex(zy1)),
                    '$(%s;%s)$'%(latex(zx0),latex(zy1)),
                    '$(%s;%s)$ và $(%s;%s)$'%(latex(-zx0),latex(zy1),latex(zx0),latex(zy1)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ có đồ thị như hình vẽ bên. Điểm cực tiểu của đồ thị hàm số là  \n')
                hinhve = (      '\\scalebox{0.6}{ \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,line width=1pt] \n'
                                '\\tikzset{every node/.style={scale=0.9}} \n'
                                '\\draw[->] (%s-2.1,0)--(%s+2.1,0) node[below left] {$x$}; \n'   #1
                                '\\draw[->] (0,%s-3.1)--(0,%s+3.1) node[below left] {$y$}; \n'   #2
                                '\\draw (0,0) node [below left] {$O$}; \n'
                                '\\draw (0,%s) node [below left] {$%s$}; \n'  #3
                                '\\foreach \\x/\\nx in {%s/%s,%s/%s} \n' #4
                                '\\draw[thin] (\\x,1pt)--(\\x,-1pt) node [below] {$\\nx$}; \n'
                                '\\draw[thin] (1pt,%s)--(-1pt,%s) node [left] {$%s$}; \n'  #5
                                '\\draw[dashed,thin](%s,0)--(%s,%s)--(0,%s); \n'  #6
                                '\\draw[dashed,thin](%s,0)--(%s,%s)--(0,%s); \n'  #7
                                '\\begin{scope} \n'
                                    '\\clip (%s,%s) rectangle (%s,%s); \n'  #8
                                    '\\draw[samples=200,domain=-4:4,smooth,variable=\\x] plot (\\x,{%s*((\\x)^4)+0*((\\x)^3)+%s*((\\x)^2)+0*(\\x)+%s}); \n' #9
                                '\\end{scope} \n'
                            '\\end{tikzpicture} } \n'

                                %(latex(-zx0), latex(zx0), #1
                                latex(zc), latex(zf1), #2
                                latex(zf1), lz(zy1), #3
                                latex(-zx0), lz(-zx0),latex(zx0),lz(zx0), #4
                                latex(zc),latex(zc), lz(zc), #5
                                latex(zx0), latex(zx0),latex(zf1),latex(zf1), #6
                                latex(-zx0), latex(-zx0),latex(zf1),latex(zf1), #7
                                latex(-zx0-2.1), latex(zc-3.1),latex(zx0+2.1),latex(zf1+3.1), #8
                                latex(zhs_a), latex(zhs_b),latex(zc), #9
                                )) 

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        'Từ bảng biến thiên ta có \\\\ \n'
                        '\\hspace*{1cm} Điểm cực tiểu của đồ thị hàm số là $(0;%s)$. \\\\ \n'
                        %(latex(zc),
                            )) 
            if dang=='7':
                d = ['$(%s;%s)$ và $(%s;%s)$'%(latex(-zx0),latex(zy1),latex(zx0),latex(zy1)),
                    ]
                da= random.choice(d)
                s = ['$x=%s$'%(latex(-zx0)),
                    '$x=%s$'%(latex(zy1)),
                    '$x=%s$'%(latex(zx0)),
                    '$y=%s$'%(latex(zx0)),
                    '$y=%s$'%(latex(-zx0)),
                    '$x=%s$'%(latex(zy1)),
                    '$y=%s$'%(latex(zy1)),
                    '$(%s;%s)$'%(latex(zx0),latex(zy1)),
                    '$(0;%s)$'%(latex(zc)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ có đồ thị như hình vẽ bên. Điểm cực đại của đồ thị hàm số là  \n')
                hinhve = (      '\\scalebox{0.6}{ \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,line width=1pt] \n'
                                '\\tikzset{every node/.style={scale=0.9}} \n'
                                '\\draw[->] (%s-2.1,0)--(%s+2.1,0) node[below left] {$x$}; \n'   #1
                                '\\draw[->] (0,%s-3.1)--(0,%s+3.1) node[below left] {$y$}; \n'   #2
                                '\\draw (0,0) node [below left] {$O$}; \n'
                                '\\draw (0,%s) node [below left] {$%s$}; \n'  #3
                                '\\foreach \\x/\\nx in {%s/%s,%s/%s} \n' #4
                                '\\draw[thin] (\\x,1pt)--(\\x,-1pt) node [below] {$\\nx$}; \n'
                                '\\draw[thin] (1pt,%s)--(-1pt,%s) node [left] {$%s$}; \n'  #5
                                '\\draw[dashed,thin](%s,0)--(%s,%s)--(0,%s); \n'  #6
                                '\\draw[dashed,thin](%s,0)--(%s,%s)--(0,%s); \n'  #7
                                '\\begin{scope} \n'
                                    '\\clip (%s,%s) rectangle (%s,%s); \n'  #8
                                    '\\draw[samples=200,domain=-4:4,smooth,variable=\\x] plot (\\x,{%s*((\\x)^4)+0*((\\x)^3)+%s*((\\x)^2)+0*(\\x)+%s}); \n' #9
                                '\\end{scope} \n'
                            '\\end{tikzpicture} } \n'

                                %(latex(-zx0), latex(zx0), #1
                                latex(zc), latex(zf1), #2
                                latex(zf1), lz(zy1), #3
                                latex(-zx0), lz(-zx0),latex(zx0),lz(zx0), #4
                                latex(zc),latex(zc), lz(zc), #5
                                latex(zx0), latex(zx0),latex(zf1),latex(zf1), #6
                                latex(-zx0), latex(-zx0),latex(zf1),latex(zf1), #7
                                latex(-zx0-2.1), latex(zc-3.1),latex(zx0+2.1),latex(zf1+3.1), #8
                                latex(zhs_a), latex(zhs_b),latex(zc), #9
                                )) 

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        'Từ bảng biến thiên ta có \\\\ \n'
                        '\\hspace*{1cm} Điểm cực đại của đồ thị hàm số là $(%s;%s)$ và $(%s;%s)$. \\\\ \n'
                        %(latex(-zx0),latex(zy1),latex(zx0),latex(zy1),
                            )) 
            if dang=='6':
                d = ['$y=%s$'%(latex(zc)),
                    ]
                da= random.choice(d)
                s = ['$x=%s$'%(latex(-zx0)),
                    '$x=%s$'%(latex(zy1)),
                    '$x=%s$'%(latex(zx0)),
                    '$y=%s$'%(latex(zx0)),
                    '$y=%s$'%(latex(-zx0)),
                    '$x=%s$'%(latex(zy1)),
                    '$y=%s$'%(latex(zy1)),
                    '$(%s;%s)$'%(latex(zx0),latex(zy1)),
                    '$(0;%s)$'%(latex(zc)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ có đồ thị như hình vẽ bên. Giá trị cực tiểu của hàm số là  \n')
                hinhve = (      '\\scalebox{0.6}{ \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,line width=1pt] \n'
                                '\\tikzset{every node/.style={scale=0.9}} \n'
                                '\\draw[->] (%s-2.1,0)--(%s+2.1,0) node[below left] {$x$}; \n'   #1
                                '\\draw[->] (0,%s-3.1)--(0,%s+3.1) node[below left] {$y$}; \n'   #2
                                '\\draw (0,0) node [below left] {$O$}; \n'
                                '\\draw (0,%s) node [below left] {$%s$}; \n'  #3
                                '\\foreach \\x/\\nx in {%s/%s,%s/%s} \n' #4
                                '\\draw[thin] (\\x,1pt)--(\\x,-1pt) node [below] {$\\nx$}; \n'
                                '\\draw[thin] (1pt,%s)--(-1pt,%s) node [left] {$%s$}; \n'  #5
                                '\\draw[dashed,thin](%s,0)--(%s,%s)--(0,%s); \n'  #6
                                '\\draw[dashed,thin](%s,0)--(%s,%s)--(0,%s); \n'  #7
                                '\\begin{scope} \n'
                                    '\\clip (%s,%s) rectangle (%s,%s); \n'  #8
                                    '\\draw[samples=200,domain=-4:4,smooth,variable=\\x] plot (\\x,{%s*((\\x)^4)+0*((\\x)^3)+%s*((\\x)^2)+0*(\\x)+%s}); \n' #9
                                '\\end{scope} \n'
                            '\\end{tikzpicture} } \n'

                                %(latex(-zx0), latex(zx0), #1
                                latex(zc), latex(zf1), #2
                                latex(zf1), lz(zy1), #3
                                latex(-zx0), lz(-zx0),latex(zx0),lz(zx0), #4
                                latex(zc),latex(zc), lz(zc), #5
                                latex(zx0), latex(zx0),latex(zf1),latex(zf1), #6
                                latex(-zx0), latex(-zx0),latex(zf1),latex(zf1), #7
                                latex(-zx0-2.1), latex(zc-3.1),latex(zx0+2.1),latex(zf1+3.1), #8
                                latex(zhs_a), latex(zhs_b),latex(zc), #9
                                )) 

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        'Từ bảng biến thiên ta có \\\\ \n'
                        '\\hspace*{1cm} Giá trị cực tiểu của hàm số là $y=%s$. \\\\ \n'
                        %(latex(zc),
                            )) 
            if dang=='5':
                d = ['$y=%s$'%(latex(zy1)),
                    ]
                da= random.choice(d)
                s = ['$x=%s$'%(latex(-zx0)),
                    '$x=%s$'%(latex(zy1)),
                    '$x=%s$'%(latex(zx0)),
                    '$y=%s$'%(latex(zx0)),
                    '$y=%s$'%(latex(-zx0)),
                    '$x=%s$'%(latex(zy1)),
                    '$y=%s$'%(latex(zc)),
                    '$(%s;%s)$'%(latex(zx0),latex(zy1)),
                    '$(0;%s)$'%(latex(zc)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ có đồ thị như hình vẽ bên. Giá trị cực đại của hàm số là \n')
                hinhve = (      '\\scalebox{0.6}{ \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,line width=1pt] \n'
                                '\\tikzset{every node/.style={scale=0.9}} \n'
                                '\\draw[->] (%s-2.1,0)--(%s+2.1,0) node[below left] {$x$}; \n'   #1
                                '\\draw[->] (0,%s-3.1)--(0,%s+3.1) node[below left] {$y$}; \n'   #2
                                '\\draw (0,0) node [below left] {$O$}; \n'
                                '\\draw (0,%s) node [below left] {$%s$}; \n'  #3
                                '\\foreach \\x/\\nx in {%s/%s,%s/%s} \n' #4
                                '\\draw[thin] (\\x,1pt)--(\\x,-1pt) node [below] {$\\nx$}; \n'
                                '\\draw[thin] (1pt,%s)--(-1pt,%s) node [left] {$%s$}; \n'  #5
                                '\\draw[dashed,thin](%s,0)--(%s,%s)--(0,%s); \n'  #6
                                '\\draw[dashed,thin](%s,0)--(%s,%s)--(0,%s); \n'  #7
                                '\\begin{scope} \n'
                                    '\\clip (%s,%s) rectangle (%s,%s); \n'  #8
                                    '\\draw[samples=200,domain=-4:4,smooth,variable=\\x] plot (\\x,{%s*((\\x)^4)+0*((\\x)^3)+%s*((\\x)^2)+0*(\\x)+%s}); \n' #9
                                '\\end{scope} \n'
                            '\\end{tikzpicture} } \n'

                                %(latex(-zx0), latex(zx0), #1
                                latex(zc), latex(zf1), #2
                                latex(zf1), lz(zy1), #3
                                latex(-zx0), lz(-zx0),latex(zx0),lz(zx0), #4
                                latex(zc),latex(zc), lz(zc), #5
                                latex(zx0), latex(zx0),latex(zf1),latex(zf1), #6
                                latex(-zx0), latex(-zx0),latex(zf1),latex(zf1), #7
                                latex(-zx0-2.1), latex(zc-3.1),latex(zx0+2.1),latex(zf1+3.1), #8
                                latex(zhs_a), latex(zhs_b),latex(zc), #9
                                )) 

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        'Từ bảng biến thiên ta có \\\\ \n'
                        '\\hspace*{1cm} Giá trị cực đại của hàm số là $y=%s$. \\\\ \n'
                        %(latex(zy1),
                            )) 
            if dang=='4':
                d = ['$x=0$',
                    ]
                da= random.choice(d)
                s = ['$x=%s$'%(latex(-zx0)),
                    '$x=%s$'%(latex(zx0)),
                    '$x=%s$'%(latex(zy1)),
                    '$x=%s$'%(latex(zc)),
                    '$y=%s$'%(latex(-zx0)),
                    '$y=%s$'%(latex(zx0)),
                    '$y=%s$'%(latex(zc)),
                    '$y=%s$'%(latex(zy1)),
                    '$(0;%s)$'%(latex(zc)),
                    '$(%s;%s)$'%(latex(-zx0),latex(zy1)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ có đồ thị như hình vẽ bên. Điểm cực tiểu của hàm số là  \n')
                hinhve = (      '\\scalebox{0.6}{ \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,line width=1pt] \n'
                                '\\tikzset{every node/.style={scale=0.9}} \n'
                                '\\draw[->] (%s-2.1,0)--(%s+2.1,0) node[below left] {$x$}; \n'   #1
                                '\\draw[->] (0,%s-3.1)--(0,%s+3.1) node[below left] {$y$}; \n'   #2
                                '\\draw (0,0) node [below left] {$O$}; \n'
                                '\\draw (0,%s) node [below left] {$%s$}; \n'  #3
                                '\\foreach \\x/\\nx in {%s/%s,%s/%s} \n' #4
                                '\\draw[thin] (\\x,1pt)--(\\x,-1pt) node [below] {$\\nx$}; \n'
                                '\\draw[thin] (1pt,%s)--(-1pt,%s) node [left] {$%s$}; \n'  #5
                                '\\draw[dashed,thin](%s,0)--(%s,%s)--(0,%s); \n'  #6
                                '\\draw[dashed,thin](%s,0)--(%s,%s)--(0,%s); \n'  #7
                                '\\begin{scope} \n'
                                    '\\clip (%s,%s) rectangle (%s,%s); \n'  #8
                                    '\\draw[samples=200,domain=-4:4,smooth,variable=\\x] plot (\\x,{%s*((\\x)^4)+0*((\\x)^3)+%s*((\\x)^2)+0*(\\x)+%s}); \n' #9
                                '\\end{scope} \n'
                            '\\end{tikzpicture} } \n'

                                %(latex(-zx0), latex(zx0), #1
                                latex(zc), latex(zf1), #2
                                latex(zf1), lz(zy1), #3
                                latex(-zx0), lz(-zx0),latex(zx0),lz(zx0), #4
                                latex(zc),latex(zc), lz(zc), #5
                                latex(zx0), latex(zx0),latex(zf1),latex(zf1), #6
                                latex(-zx0), latex(-zx0),latex(zf1),latex(zf1), #7
                                latex(-zx0-2.1), latex(zc-3.1),latex(zx0+2.1),latex(zf1+3.1), #8
                                latex(zhs_a), latex(zhs_b),latex(zc), #9
                                )) 

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        'Từ bảng biến thiên ta có \\\\ \n'
                        '\\hspace*{1cm} Điểm cực tiểu của hàm số là $x=0$. \\\\ \n'
                            )
            if dang=='3':
                d = ['$x=%s$ và $x=%s$'%(latex(-zx0),latex(zx0)),
                    ]
                da= random.choice(d)
                s = ['$x=0$',
                    '$x=%s$'%(latex(zy1)),
                    '$x=%s$'%(latex(zc)),
                    '$y=%s$'%(latex(-zx0)),
                    '$y=%s$'%(latex(zx0)),
                    '$y=%s$'%(latex(zc)),
                    '$y=%s$'%(latex(zy1)),
                    '$(0;%s)$'%(latex(zc)),
                    '$(%s;%s)$'%(latex(-zx0),latex(zy1)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ có đồ thị như hình vẽ bên. Điểm cực đại của hàm số là  \n')
                hinhve = (      '\\scalebox{0.6}{ \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,line width=1pt] \n'
                                '\\tikzset{every node/.style={scale=0.9}} \n'
                                '\\draw[->] (%s-2.1,0)--(%s+2.1,0) node[below left] {$x$}; \n'   #1
                                '\\draw[->] (0,%s-3.1)--(0,%s+3.1) node[below left] {$y$}; \n'   #2
                                '\\draw (0,0) node [below left] {$O$}; \n'
                                '\\draw (0,%s) node [below left] {$%s$}; \n'  #3
                                '\\foreach \\x/\\nx in {%s/%s,%s/%s} \n' #4
                                '\\draw[thin] (\\x,1pt)--(\\x,-1pt) node [below] {$\\nx$}; \n'
                                '\\draw[thin] (1pt,%s)--(-1pt,%s) node [left] {$%s$}; \n'  #5
                                '\\draw[dashed,thin](%s,0)--(%s,%s)--(0,%s); \n'  #6
                                '\\draw[dashed,thin](%s,0)--(%s,%s)--(0,%s); \n'  #7
                                '\\begin{scope} \n'
                                    '\\clip (%s,%s) rectangle (%s,%s); \n'  #8
                                    '\\draw[samples=200,domain=-4:4,smooth,variable=\\x] plot (\\x,{%s*((\\x)^4)+0*((\\x)^3)+%s*((\\x)^2)+0*(\\x)+%s}); \n' #9
                                '\\end{scope} \n'
                            '\\end{tikzpicture}} \n'

                                %(latex(-zx0), latex(zx0), #1
                                latex(zc), latex(zf1), #2
                                latex(zf1), lz(zy1), #3
                                latex(-zx0), lz(-zx0),latex(zx0),lz(zx0), #4
                                latex(zc),latex(zc), lz(zc), #5
                                latex(zx0), latex(zx0),latex(zf1),latex(zf1), #6
                                latex(-zx0), latex(-zx0),latex(zf1),latex(zf1), #7
                                latex(-zx0-2.1), latex(zc-3.1),latex(zx0+2.1),latex(zf1+3.1), #8
                                latex(zhs_a), latex(zhs_b),latex(zc), #9
                                )) 

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        'Từ bảng biến thiên ta có \\\\ \n'
                        '\\hspace*{1cm} Điểm cực đại của hàm số là $x=%s$ và $x=%s$. \\\\ \n'
                        %(latex(-zx0),latex(zx0),
                            )) 

            if dang=='2':
                d = ['$3$',
                    ]
                da= random.choice(d)
                s = ['$0$',
                    '$1$',
                    '$2$',
                    '$4$',
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ có đồ thị như hình vẽ bên. Số điểm cực trị của hàm số là')
                hinhve = (      '\\scalebox{0.6}{ \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,line width=1pt] \n'
                                '\\tikzset{every node/.style={scale=0.9}} \n'
                                '\\draw[->] (%s-2.1,0)--(%s+2.1,0) node[below left] {$x$}; \n'   #1
                                '\\draw[->] (0,%s-3.1)--(0,%s+3.1) node[below left] {$y$}; \n'   #2
                                '\\draw (0,0) node [below left] {$O$}; \n'
                                '\\draw (0,%s) node [below left] {$%s$}; \n'  #3
                                '\\foreach \\x/\\nx in {%s/%s,%s/%s} \n' #4
                                '\\draw[thin] (\\x,1pt)--(\\x,-1pt) node [below] {$\\nx$}; \n'
                                '\\draw[thin] (1pt,%s)--(-1pt,%s) node [left] {$%s$}; \n'  #5
                                '\\draw[dashed,thin](%s,0)--(%s,%s)--(0,%s); \n'  #6
                                '\\draw[dashed,thin](%s,0)--(%s,%s)--(0,%s); \n'  #7
                                '\\begin{scope} \n'
                                    '\\clip (%s,%s) rectangle (%s,%s); \n'  #8
                                    '\\draw[samples=200,domain=-4:4,smooth,variable=\\x] plot (\\x,{%s*((\\x)^4)+0*((\\x)^3)+%s*((\\x)^2)+0*(\\x)+%s}); \n' #9
                                '\\end{scope} \n'
                            '\\end{tikzpicture}} \n'

                                %(latex(-x0), latex(x0), #1
                                latex(f1), latex(c), #2
                                latex(f1), lz(y1), #3
                                latex(-x0), lz(-x0),latex(x0),lz(x0), #4
                                latex(c),latex(c), lz(c), #5
                                latex(x0), latex(x0),latex(f1),latex(f1), #6
                                latex(-x0), latex(-x0),latex(f1),latex(f1), #7
                                latex(-x0-2.1), latex(y1-3.1),latex(x0+2.1),latex(c+3.1), #8
                                latex(hs_a), latex(hs_b),latex(c), #9
                                ))  

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        'Từ bảng biến thiên ta có \\\\ \n'
                        '\\hspace*{1cm} Số điểm cực trị của hàm số là $3$. \\\\ \n'
                        )
            if dang=='1':
                d = [
                    'Số điểm cực trị của hàm số là $3$',
                    'Hàm số đạt cực tiểu tại các điểm $x=%s$ và $x=%s$'%(latex(-x0),latex(x0)),
                    'Điểm cực đại của hàm số là $x=0$',
                    'Giá trị cực tiểu của hàm số là $y_{\\text{CT}}=%s$'%(latex(y1)),
                    'Giá trị cực đại của hàm số là $y_{\\text{CĐ}}=%s$'%(latex(c)),
                    'Số điểm cực tiểu của hàm số là $2$',
                    'Điểm cực đại của đồ thị hàm số là $\\left(0;%s\\right)$'%(latex(c)),
                    ]
                da= random.choice(d)
                s = ['Số điểm cực trị của hàm số là $2$',
                    'Hàm số đạt cực tiểu tại các điểm $x=%s$ và $x=%s$'%(latex(-x0),latex(x0+2)),
                    'Điểm cực đại của hàm số là $x=%s$'%(latex(c+3)),
                    'Giá trị cực tiểu của hàm số là $y_{\\text{CT}}=%s$'%(latex(y1-11)),
                    'Giá trị cực đại của hàm số là $y_{\\text{CĐ}}=%s$'%(latex(c+1)),
                    'Số điểm cực tiểu của hàm số là $3$',
                    'Điểm cực đại của đồ thị hàm số là $\\left(0;%s\\right)$'%(latex(c-1)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ có đồ thị như hình vẽ bên. Khẳng định nào sau đây là đúng?')
                hinhve = (      '\\scalebox{0.6}{ \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,line width=1pt] \n'
                                '\\tikzset{every node/.style={scale=0.9}} \n'
                                '\\draw[->] (%s-2.1,0)--(%s+2.1,0) node[below left] {$x$}; \n'   #1
                                '\\draw[->] (0,%s-3.1)--(0,%s+3.1) node[below left] {$y$}; \n'   #2
                                '\\draw (0,0) node [below left] {$O$}; \n'
                                '\\draw (0,%s) node [below left] {$%s$}; \n'  #3
                                '\\foreach \\x/\\nx in {%s/%s,%s/%s} \n' #4
                                '\\draw[thin] (\\x,1pt)--(\\x,-1pt) node [below] {$\\nx$}; \n'
                                '\\draw[thin] (1pt,%s)--(-1pt,%s) node [left] {$%s$}; \n'  #5
                                '\\draw[dashed,thin](%s,0)--(%s,%s)--(0,%s); \n'  #6
                                '\\draw[dashed,thin](%s,0)--(%s,%s)--(0,%s); \n'  #7
                                '\\begin{scope} \n'
                                    '\\clip (%s,%s) rectangle (%s,%s); \n'  #8
                                    '\\draw[samples=200,domain=-4:4,smooth,variable=\\x] plot (\\x,{%s*((\\x)^4)+0*((\\x)^3)+%s*((\\x)^2)+0*(\\x)+%s}); \n' #9
                                '\\end{scope} \n'
                            '\\end{tikzpicture}} \n'

                                %(latex(-x0), latex(x0), #1
                                latex(f1), latex(c), #2
                                latex(f1), lz(y1), #3
                                latex(-x0), lz(-x0),latex(x0),lz(x0), #4
                                latex(c),latex(c), lz(c), #5
                                latex(x0), latex(x0),latex(f1),latex(f1), #6
                                latex(-x0), latex(-x0),latex(f1),latex(f1), #7
                                latex(-x0-2.1), latex(y1-3.1),latex(x0+2.1),latex(c+3.1), #8
                                latex(hs_a), latex(hs_b),latex(c), #9
                                )) 

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        'Từ bảng biến thiên ta có \\\\ \n'
                        '\\hspace*{1cm} Số điểm cực trị của hàm số là $3$. \\\\ \n'
                        '\\hspace*{1cm} Hàm số đạt cực tiểu tại các điểm $x=%s$ và $x=%s$. \\\\ \n'
                        '\\hspace*{1cm} Điểm cực đại của hàm số là $x=0$. \\\\ \n'
                        '\\hspace*{1cm} Giá trị cực tiểu của hàm số là $y_{\\text{CT}}=%s$. \\\\ \n'
                        '\\hspace*{1cm} Giá trị cực đại của hàm số là $y_{\\text{CĐ}}=%s$. \\\\ \n'
                        '\\hspace*{1cm} Số điểm cực tiểu của hàm số là $2$. \\\\ \n'
                        '\\hspace*{1cm} Điểm cực đại của đồ thị hàm số là $\\left(0;%s\\right)$. \\\\ \n'
                        %(latex(-x0),latex(x0),
                        latex(y1),
                        latex(c),
                        latex(c),
                        ))


            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n \\immini{'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n }{'+hinhve+ '} \n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content


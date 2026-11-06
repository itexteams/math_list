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


def bt_dang29_p1_b1_c1_ds12(self):
            # Khai báo biến
            lisdang=['1','2','3','4','5','6','7','1','1','1','1']
            dang=random.choice(lisdang)
            if dang=='7':
                # Khai báo biến
                a = randint(1,9)
                b = randint(1,9)
                c = randint(-20,20)
                while a<=0 or b==0:
                    a = randint(1,9)
                    b = randint(1,9)
                    c = randint(-20,20)
                x1 = Rational(-b,a)
                x2 = Rational(b,a)
                y=Rational(a**2,2)*x**4-b**2*x**2+c
                y1=Rational(a**2,2)*x1**4-b**2*x1**2+c
                y2=Rational(a**2,2)*x2**4-b**2*x2**2+c
                du = ['$\\left(0;%s\\right)$'%(latex(c)),
                    ]
                da= random.choice(du)
                s = ['$x=%s$'%(latex(x1)),
                    '$x=%s$'%(latex(x2)),
                    '$x=%s$'%(latex(y1)),
                    '$x=%s$'%(latex(c)),
                    '$y=%s$'%(latex(x1)),
                    '$y=%s$'%(latex(x2)),
                    '$y=%s$'%(latex(y1)),
                    '$y=%s$'%(latex(c)),
                    '$y=0$',
                    '$\\left(%s;%s\\right)$'%(latex(x1),latex(y1)),
                    '$\\left(%s;%s\\right)$'%(latex(x2),latex(y2)),
                    '$x=0$',
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = '''Cho hàm số $y=%sx^4+%sx^2+%s$. Điểm cực đại của đồ thị hàm số là \n'''%(latex(Rational(a**2,2)),latex(-b**2),latex(c))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Tập xác định: $\\mathscr{D}=\\mathbb{R}$.\\\\ \n'
                        '''Ta có $y'=%sx^3+%sx.\\\\ \n''' 
                        '''\\hspace*{1.1cm}y'=0 \\Leftrightarrow \\hoac{& x=0 \\\\& x=%s \\\\& x=%s.}$\\\\ \n'''
                        '''Bảng xét dấu\\\\ \n'''
                        '\\hspace*{2cm} \\begin{tikzpicture} \n'
                        '\\tkzTabInit[espcl=2.5,lgt=1.5] \n'
                        '{$x$/1,$y\'$/0.7,$y$/2.1}  \n'
                        '{$-\\infty$,$%s$,0,$%s$,$+\\infty$}  \n'
                        '\\tkzTabLine{,-,0,+,0,-,0,+}  \n'
                        '\\tkzTabVar{+/$+\\infty$,-/$%s$,+/$%s$,-/$%s$,+/$+\\infty$}  \n'
                        '\\end{tikzpicture}  \\\\ \n'
                        '''Từ bảng xét dấu ta thấy\\\\ \n'''
                        '''\\hspace*{1cm} Hàm số đạt cực tiểu tại các điểm $x=%s$ và $x=%s$, giá trị cực đại lại $y_{\\text{CĐ}}=%s$\\\\ \n'''
                        '''\\hspace*{1cm} Hàm số đạt cực đại tại điểm $x=0$, giá trị cực đại lại $y_{\\text{CT}}=%s$\\\\ \n'''
                        %(latex(2*(a**2)),latex(-2*(b**2)),
                        latex(x1),latex(x2),
                        latex(x1),latex(x2),
                        latex(y1),latex(c),latex(y2),
                        latex(x1),latex(x2),latex(y1),
                        latex(c)))
            if dang=='6':
                # Khai báo biến
                a = randint(1,9)
                b = randint(1,9)
                c = randint(-20,20)
                while a<=0 or b==0:
                    a = randint(1,9)
                    b = randint(1,9)
                    c = randint(-20,20)
                x1 = Rational(-b,a)
                x2 = Rational(b,a)
                y=Rational(a**2,2)*x**4-(b**2)*x**2+c
                y1=Rational(a**2,2)*x1**4-(b**2)*x1**2+c
                y2=Rational(a**2,2)*x2**4-(b**2)*x2**2+c
                du = ['$y=%s$'%(latex(y1)),
                    ]
                da= random.choice(du)
                s = ['$x=%s$'%(latex(x1)),
                    '$x=%s$'%(latex(x2)),
                    '$x=%s$'%(latex(y1)),
                    '$x=%s$'%(latex(c)),
                    '$y=%s$'%(latex(x1)),
                    '$y=%s$'%(latex(x2)),
                    '$y=%s$'%(latex(c)),
                    '$y=0$',
                    '$\\left(%s;%s\\right)$'%(latex(x1),latex(y1)),
                    '$\\left(%s;%s\\right)$'%(latex(x2),latex(y2)),
                    '$\\left(0;%s\\right)$'%(latex(c)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = '''Cho hàm số $y=%sx^4+%sx^2+%s$. Giá trị cực tiểu của hàm số là \n'''%(latex(Rational(a**2,2)),latex(-b**2),latex(c))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Tập xác định: $\\mathscr{D}=\\mathbb{R}$.\\\\ \n'
                        '''Ta có $y'=%sx^3+%sx.\\\\ \n''' 
                        '''\\hspace*{1.1cm}y'=0 \\Leftrightarrow \\hoac{& x=0 \\\\& x=%s \\\\& x=%s.}$\\\\ \n'''
                        '''Bảng xét dấu\\\\ \n'''
                        '\\hspace*{2cm} \\begin{tikzpicture} \n'
                        '\\tkzTabInit[espcl=2.5,lgt=1.5] \n'
                        '{$x$/1,$y\'$/0.7,$y$/2.1}  \n'
                        '{$-\\infty$,$%s$,0,$%s$,$+\\infty$}  \n'
                        '\\tkzTabLine{,-,0,+,0,-,0,+}  \n'
                        '\\tkzTabVar{+/$+\\infty$,-/$%s$,+/$%s$,-/$%s$,+/$+\\infty$}  \n'
                        '\\end{tikzpicture}  \\\\ \n'
                        '''Từ bảng xét dấu ta thấy\\\\ \n'''
                        '''\\hspace*{1cm} Hàm số đạt cực tiểu tại các điểm $x=%s$ và $x=%s$, giá trị cực đại lại $y_{\\text{CĐ}}=%s$\\\\ \n'''
                        '''\\hspace*{1cm} Hàm số đạt cực đại tại điểm $x=0$, giá trị cực đại lại $y_{\\text{CT}}=%s$\\\\ \n'''
                        %(latex(2*(a**2)),latex(-2*(b**2)),
                        latex(x1),latex(x2),
                        latex(x1),latex(x2),
                        latex(y1),latex(c),latex(y2),
                        latex(x1),latex(x2),latex(y1),
                        latex(c)))
            if dang=='5':
                # Khai báo biến
                a = randint(1,9)
                b = randint(1,9)
                c = randint(-20,20)
                while a<=0 or b==0:
                    a = randint(1,9)
                    b = randint(1,9)
                    c = randint(-20,20)
                x1 = Rational(-b,a)
                x2 = Rational(b,a)
                y=Rational(a**2,2)*x**4-b**2*x**2+c
                y1=Rational(a**2,2)*x1**4-b**2*x1**2+c
                y2=Rational(a**2,2)*x2**4-b**2*x2**2+c
                du = ['$y=%s$'%(latex(c)),
                    ]
                da= random.choice(du)
                s = ['$x=%s$'%(latex(x1)),
                    '$x=%s$'%(latex(x2)),
                    '$x=%s$'%(latex(y1)),
                    '$x=%s$'%(latex(c)),
                    '$y=%s$'%(latex(x1)),
                    '$y=%s$'%(latex(x2)),
                    '$y=%s$'%(latex(y1)),
                    '$x=0$',
                    '$y=0$',
                    '$\\left(%s;%s\\right)$'%(latex(x1),latex(y1)),
                    '$\\left(%s;%s\\right)$'%(latex(x2),latex(y2)),
                    '$\\left(0;%s\\right)$'%(latex(c)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = '''Cho hàm số $y=%sx^4+%sx^2+%s$. Giá trị cực đại của hàm số là \n'''%(latex(Rational(a**2,2)),latex(-b**2),latex(c))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Tập xác định: $\\mathscr{D}=\\mathbb{R}$.\\\\ \n'
                        '''Ta có $y'=%sx^3+%sx.\\\\ \n''' 
                        '''\\hspace*{1.1cm}y'=0 \\Leftrightarrow \\hoac{& x=0 \\\\& x=%s \\\\& x=%s.}$\\\\ \n'''
                        '''Bảng xét dấu\\\\ \n'''
                        '\\hspace*{2cm} \\begin{tikzpicture} \n'
                        '\\tkzTabInit[espcl=2.5,lgt=1.5] \n'
                        '{$x$/1,$y\'$/0.7,$y$/2.1}  \n'
                        '{$-\\infty$,$%s$,0,$%s$,$+\\infty$}  \n'
                        '\\tkzTabLine{,-,0,+,0,-,0,+}  \n'
                        '\\tkzTabVar{+/$+\\infty$,-/$%s$,+/$%s$,-/$%s$,+/$+\\infty$}  \n'
                        '\\end{tikzpicture}  \\\\ \n'
                        '''Từ bảng xét dấu ta thấy\\\\ \n'''
                        '''\\hspace*{1cm} Hàm số đạt cực tiểu tại các điểm $x=%s$ và $x=%s$, giá trị cực đại lại $y_{\\text{CĐ}}=%s$\\\\ \n'''
                        '''\\hspace*{1cm} Hàm số đạt cực đại tại điểm $x=0$, giá trị cực đại lại $y_{\\text{CT}}=%s$\\\\ \n'''
                        %(latex(2*(a**2)),latex(-2*(b**2)),
                        latex(x1),latex(x2),
                        latex(x1),latex(x2),
                        latex(y1),latex(c),latex(y2),
                        latex(x1),latex(x2),latex(y1),
                        latex(c)))
            if dang=='4':
                # Khai báo biến
                a = randint(1,9)
                b = randint(1,9)
                c = randint(-20,20)
                while a<=0 or b==0:
                    a = randint(1,9)
                    b = randint(1,9)
                    c = randint(-20,20)
                x1 = Rational(-b,a)
                x2 = Rational(b,a)
                y=Rational(a**2,2)*x**4-b**2*x**2+c
                y1=Rational(a**2,2)*x1**4-b**2*x1**2+c
                y2=Rational(a**2,2)*x2**4-b**2*x2**2+c
                du = ['$x=%s$ và $x=%s$'%(latex(x1),latex(x2)),
                    ]
                da= random.choice(du)
                s = ['$x=%s$'%(latex(x1)),
                    '$x=%s$'%(latex(x2)),
                    '$x=%s$'%(latex(y1)),
                    '$x=%s$'%(latex(c)),
                    '$y=%s$'%(latex(x1)),
                    '$y=%s$'%(latex(x2)),
                    '$y=%s$'%(latex(y1)),
                    '$y=%s$'%(latex(c)),
                    '$y=0$',
                    '$\\left(%s;%s\\right)$'%(latex(x1),latex(y1)),
                    '$\\left(%s;%s\\right)$'%(latex(x2),latex(y2)),
                    '$\\left(0;%s\\right)$'%(latex(c)),
                    '$x=0$ và $x=%s$'%(latex(x1)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = '''Cho hàm số $y=%sx^4+%sx^2+%s$. Điểm cực tiểu của hàm số là \n'''%(latex(Rational(a**2,2)),latex(-b**2),latex(c))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Tập xác định: $\\mathscr{D}=\\mathbb{R}$.\\\\ \n'
                        '''Ta có $y'=%sx^3+%sx.\\\\ \n''' 
                        '''\\hspace*{1.1cm}y'=0 \\Leftrightarrow \\hoac{& x=0 \\\\& x=%s \\\\& x=%s.}$\\\\ \n'''
                        '''Bảng xét dấu\\\\ \n'''
                        '\\hspace*{2cm} \\begin{tikzpicture} \n'
                        '\\tkzTabInit[espcl=2.5,lgt=1.5] \n'
                        '{$x$/1,$y\'$/0.7,$y$/2.1}  \n'
                        '{$-\\infty$,$%s$,0,$%s$,$+\\infty$}  \n'
                        '\\tkzTabLine{,-,0,+,0,-,0,+}  \n'
                        '\\tkzTabVar{+/$+\\infty$,-/$%s$,+/$%s$,-/$%s$,+/$+\\infty$}  \n'
                        '\\end{tikzpicture}  \\\\ \n'
                        '''Từ bảng xét dấu ta thấy\\\\ \n'''
                        '''\\hspace*{1cm} Hàm số đạt cực tiểu tại các điểm $x=%s$ và $x=%s$, giá trị cực đại lại $y_{\\text{CĐ}}=%s$\\\\ \n'''
                        '''\\hspace*{1cm} Hàm số đạt cực đại tại điểm $x=0$, giá trị cực đại lại $y_{\\text{CT}}=%s$\\\\ \n'''
                        %(latex(2*(a**2)),latex(-2*(b**2)),
                        latex(x1),latex(x2),
                        latex(x1),latex(x2),
                        latex(y1),latex(c),latex(y2),
                        latex(x1),latex(x2),latex(y1),
                        latex(c)))
            if dang=='3':
                # Khai báo biến
                a = randint(1,9)
                b = randint(1,9)
                c = randint(-20,20)
                while a<=0 or b==0:
                    a = randint(1,9)
                    b = randint(1,9)
                    c = randint(-20,20)
                x1 = Rational(-b,a)
                x2 = Rational(b,a)
                y=Rational(a**2,2)*x**4-b**2*x**2+c
                y1=Rational(a**2,2)*x1**4-b**2*x1**2+c
                y2=Rational(a**2,2)*x2**4-b**2*x2**2+c
                du = ['$x=0$',
                    ]
                da= random.choice(du)
                s = ['$x=%s$'%(latex(x1)),
                    '$x=%s$'%(latex(x2)),
                    '$x=%s$'%(latex(y1)),
                    '$x=%s$'%(latex(c)),
                    '$y=%s$'%(latex(x1)),
                    '$y=%s$'%(latex(x2)),
                    '$y=%s$'%(latex(y1)),
                    '$y=%s$'%(latex(c)),
                    '$y=0$',
                    '$\\left(%s;%s\\right)$'%(latex(x1),latex(y1)),
                    '$\\left(%s;%s\\right)$'%(latex(x2),latex(y2)),
                    '$\\left(0;%s\\right)$'%(latex(c)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = '''Cho hàm số $y=%sx^4+%sx^2+%s$. Điểm cực đại của hàm số là \n'''%(latex(Rational(a**2,2)),latex(-b**2),latex(c))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Tập xác định: $\\mathscr{D}=\\mathbb{R}$.\\\\ \n'
                        '''Ta có $y'=%sx^3+%sx.\\\\ \n''' 
                        '''\\hspace*{1.1cm}y'=0 \\Leftrightarrow \\hoac{& x=0 \\\\& x=%s \\\\& x=%s.}$\\\\ \n'''
                        '''Bảng xét dấu\\\\ \n'''
                        '\\hspace*{2cm} \\begin{tikzpicture} \n'
                        '\\tkzTabInit[espcl=2.5,lgt=1.5] \n'
                        '{$x$/1,$y\'$/0.7,$y$/2.1}  \n'
                        '{$-\\infty$,$%s$,0,$%s$,$+\\infty$}  \n'
                        '\\tkzTabLine{,-,0,+,0,-,0,+}  \n'
                        '\\tkzTabVar{+/$+\\infty$,-/$%s$,+/$%s$,-/$%s$,+/$+\\infty$}  \n'
                        '\\end{tikzpicture}  \\\\ \n'
                        '''Từ bảng xét dấu ta thấy\\\\ \n'''
                        '''\\hspace*{1cm} Hàm số đạt cực tiểu tại các điểm $x=%s$ và $x=%s$, giá trị cực đại lại $y_{\\text{CĐ}}=%s$\\\\ \n'''
                        '''\\hspace*{1cm} Hàm số đạt cực đại tại điểm $x=0$, giá trị cực đại lại $y_{\\text{CT}}=%s$\\\\ \n'''
                        %(latex(2*(a**2)),latex(-2*(b**2)),
                        latex(x1),latex(x2),
                        latex(x1),latex(x2),
                        latex(y1),latex(c),latex(y2),
                        latex(x1),latex(x2),latex(y1),
                        latex(c)))
            if dang=='2':
                # Khai báo biến
                a = randint(1,9)
                b = randint(1,9)
                c = randint(-20,20)
                while a<=0 or b==0:
                    a = randint(1,9)
                    b = randint(1,9)
                    c = randint(-20,20)
                x1 = Rational(-b,a)
                x2 = Rational(b,a)
                y=Rational(a**2,2)*x**4-b**2*x**2+c
                y1=Rational(a**2,2)*x1**4-b**2*x1**2+c
                y2=Rational(a**2,2)*x2**4-b**2*x2**2+c
                du = ['$3$',
                    ]
                da= random.choice(du)
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
                noidungcauhoi = '''Cho hàm số $y=%sx^4+%sx^2+%s$. Số điểm cực trị của hàm số là \n'''%(latex(Rational(a**2,2)),latex(-b**2),latex(c))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Tập xác định: $\\mathscr{D}=\\mathbb{R}$.\\\\ \n'
                        '''Ta có $y'=%sx^3+%sx.\\\\ \n''' 
                        '''\\hspace*{1.1cm}y'=0 \\Leftrightarrow \\hoac{& x=0 \\\\& x=%s \\\\& x=%s.}$\\\\ \n'''
                        '''Bảng xét dấu\\\\ \n'''
                        '\\hspace*{2cm} \\begin{tikzpicture} \n'
                        '\\tkzTabInit[espcl=2.5,lgt=1.5] \n'
                        '{$x$/1,$y\'$/0.7,$y$/2.1}  \n'
                        '{$-\\infty$,$%s$,0,$%s$,$+\\infty$}  \n'
                        '\\tkzTabLine{,-,0,+,0,-,0,+}  \n'
                        '\\tkzTabVar{+/$+\\infty$,-/$%s$,+/$%s$,-/$%s$,+/$+\\infty$}  \n'
                        '\\end{tikzpicture}  \\\\ \n'
                        '''Từ bảng xét dấu ta thấy\\\\ \n'''
                        '''\\hspace*{1cm} Hàm số đạt cực tiểu tại các điểm $x=%s$ và $x=%s$, giá trị cực đại lại $y_{\\text{CĐ}}=%s$\\\\ \n'''
                        '''\\hspace*{1cm} Hàm số đạt cực đại tại điểm $x=0$, giá trị cực đại lại $y_{\\text{CT}}=%s$\\\\ \n'''
                        %(latex(2*(a**2)),latex(-2*(b**2)),
                        latex(x1),latex(x2),
                        latex(x1),latex(x2),
                        latex(y1),latex(c),latex(y2),
                        latex(x1),latex(x2),latex(y1),
                        latex(c)))

            if dang=='1':
                # Khai báo biến
                a = randint(1,9)
                b = randint(1,8)
                c = randint(-20,20)
                while a<=0 or b==0:
                    a = randint(1,9)
                    b = randint(1,8)
                    c = randint(-20,20)
                x1 = Rational(-b,a)
                x2 = Rational(b,a)
                y=Rational(a**2,-2)*x**4+b**2*x**2+c
                y1=Rational(a**2,-2)*x1**4+b**2*x1**2+c
                y2=Rational(a**2,-2)*x2**4+b**2*x2**2+c
                du = ['Điểm cực đại của hàm số là $x=%s$ và $x=%s$'%(latex(x1),latex(x2)),
                    'Điểm cực tiểu của hàm số là $x=0$',
                    'Số điểm cực trị của hàm số là $3$',
                    'Giá trị cực đại của hàm số là $y_{\\text{CĐ}}=%s$'%(latex(y1)),
                    'Giá trị cực tiểu của hàm số là $y_{\\text{CT}}=%s$'%(latex(c)),
                    'Điểm cực đại của đồ thị hàm số là $\\left(%s;%s\\right)$ và $\\left(%s;%s\\right)$'%(latex(x1),latex(y1),latex(x2),latex(y1)),
                    'Điểm cực tiểu của đồ thị hàm số là $\\left(0;%s\\right)$'%(latex(c)),
                    ]
                da= random.choice(du)
                s = ['Điểm cực đại của hàm số là $x=%s$'%(latex(x2)),
                    'Điểm cực tiểu của hàm số là $x=%s$'%(latex(x1)),
                    'Số điểm cực trị của hàm số là $2$',
                    'Giá trị cực đại của hàm số là $y_{\\text{CĐ}}=%s$'%(latex(x1)),
                    'Giá trị cực tiểu của hàm số là $y_{\\text{CT}}=%s$'%(latex(c+9)),
                    'Điểm cực đại của đồ thị hàm số là $x=%s$ và $x=%s$'%(latex(x1),latex(x2)),
                    'Điểm cực tiểu của đồ thị hàm số là $x=0$',
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = '''Cho hàm số $y=%sx^4+%sx^2+%s$. Khẳng định nào dưới đây đúng? \n'''%(latex(Rational(a**2,-2)),latex(b**2),latex(c))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Tập xác định: $\\mathscr{D}=\\mathbb{R}$.\\\\ \n'
                        '''Ta có $y'=%sx^3+%sx.\\\\ \n''' 
                        '''\\hspace*{1.1cm}y'=0 \\Leftrightarrow \\hoac{& x=0 \\\\& x=%s \\\\& x=%s.}$\\\\ \n'''
                        '''Bảng xét dấu\\\\ \n'''
                        '\\hspace*{2cm} \\begin{tikzpicture} \n'
                        '\\tkzTabInit[espcl=2.5,lgt=1.5] \n'
                        '{$x$/1,$y\'$/0.7,$y$/2.1} \n'
                        '{$-\\infty$,$%s$,0,$%s$,$+\\infty$} \n'
                        '\\tkzTabLine{,+,0,-,0,+,0,-} \n'
                        '\\tkzTabVar{-/$-\\infty$,+/$%s$,-/$%s$,+/$%s$,-/$-\\infty$} \n'
                        '\\end{tikzpicture} \\\\ \n'
                        '''Từ bảng xét dấu ta thấy\\\\ \n'''
                        '''\\hspace*{1cm} Hàm số đạt cực đại tại các điểm $x=%s$ và $x=%s$, giá trị cực đại lại $y_{\\text{CĐ}}=%s$\\\\ \n'''
                        '''\\hspace*{1cm} Hàm số tiểu cực đại tại điểm $x=0$, giá trị cực đại lại $y_{\\text{CT}}=%s$\\\\ \n'''
                        %(latex(-2*(a**2)),latex(2*(b**2)),
                        latex(x1),latex(x2),
                        latex(x1),latex(x2),
                        latex(y1),latex(c),latex(y2),
                        latex(x1),latex(x2),latex(y1),
                        latex(c)))


            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-').replace('1x', 'x').replace('+0x^2', '').replace('+0x', '').replace('+0', '')
            return content


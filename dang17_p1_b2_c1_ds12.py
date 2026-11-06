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


def bt_dang17_p1_b2_c1_ds12(self):
            # Khai báo biến
            lisdang=['1','2','3','4','5','6','7','8']
            dang=random.choice(lisdang)
            if dang=='8':
                # Khai báo biến
                x = symbols('x')
                t = symbols('t')
                a=randint(-9,9)
                while a==0:
                    a=randint(-9,9)
                b=randint(-9,9)
                c=randint(1,9)
                while a*c-b<=0:
                    a=randint(-9,9)
                    while a==0:
                        a=randint(-9,9)
                    b=randint(-9,9)
                    c=randint(1,9)

                f=(a*t+b)/(t+c)
                ff=(a*cos(x)+b)/(cos(x)+c)
                daoham=(a*c-b)/(t+c)**2

                m=0
                n=1
                fm=Rational(b,c)
                fn=Rational(a+b,1+c)
                gtnn=fm
                gtln=fn

                du = ['$%s$'%(latex(gtln)),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(gtln+1)),
                    '$%s$'%(latex(gtln+3)),
                    '$%s$'%(latex(gtln+2)),
                    '$%s$'%(latex(gtln-2)),
                    '$%s$'%(latex(gtln-1)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('''Cho hàm số $y=%s$ trên đoạn $\\left[ 0;\\dfrac{\\pi}{2} \\right]$. Giá trị lớn nhất của hàm số là'''
                                %(latex(ff)
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
                        'Đặt $\\cos x=t$ với $t \\in [0;1]$, khi đó $y=%s$. \\\\ \n'
                        'Xét hàm số $f(t)=%s$ trên đoạn $[0;1]$. \\\\ \n'
                        '\\hspace*{1cm} $f\'(t)=%s >0$ Hàm số luông đồng biến. \\\\ \n'
                        'Ta có $f(0)=%s, f(1)=%s$.\\\\ \n'
                        'Ta thấy \\\\ \n'
                        '\\hspace*{1cm} $\\underset{[0;1]}{\\mathop{\\max }}\\,f(t)=%s$ suy ra giá trị lớn nhất của hàm số là $%s$. \\\\ \n'
                        '\\hspace*{1cm} $\\underset{[0;1]}{\\mathop{\\min }}\\,f(t)=%s$ suy ra giá trị nhỏ nhất của hàm số là $%s$.'

                        %(latex(f),latex(f),
                        latex(daoham),
                        latex(fm),latex(fn),
                        latex(gtln),latex(gtln),
                        latex(gtnn),latex(gtnn),
                        ))
            if dang=='7':
                # Khai báo biến
                x = symbols('x')
                t = symbols('t')
                a=randint(-9,9)
                while a==0:
                    a=randint(-9,9)
                b=randint(-9,9)
                c=randint(1,9)
                while a*c-b<=0:
                    a=randint(-9,9)
                    while a==0:
                        a=randint(-9,9)
                    b=randint(-9,9)
                    c=randint(1,9)

                f=(a*t+b)/(t+c)
                ff=(a*cos(x)+b)/(cos(x)+c)
                daoham=(a*c-b)/(t+c)**2

                m=0
                n=1
                fm=Rational(b,c)
                fn=Rational(a+b,1+c)
                gtnn=fm
                gtln=fn

                du = ['$%s$'%(latex(gtnn)),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(gtnn+1)),
                    '$%s$'%(latex(gtnn+2)),
                    '$%s$'%(latex(gtnn-1)),
                    '$%s$'%(latex(gtnn-2)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('''Cho hàm số $y=%s$ trên đoạn $\\left[ 0;\\dfrac{\\pi}{2} \\right]$. Giá trị nhỏ nhất của hàm số là'''
                                %(latex(ff)
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
                        'Đặt $\\cos x=t$ với $t \\in [0;1]$, khi đó $y=%s$. \\\\ \n'
                        'Xét hàm số $f(t)=%s$ trên đoạn $[0;1]$. \\\\ \n'
                        '\\hspace*{1cm} $f\'(t)=%s >0$ Hàm số luông đồng biến. \\\\ \n'
                        'Ta có $f(0)=%s, f(1)=%s$.\\\\ \n'
                        'Ta thấy \\\\ \n'
                        '\\hspace*{1cm} $\\underset{[0;1]}{\\mathop{\\max }}\\,f(t)=%s$ suy ra giá trị lớn nhất của hàm số là $%s$. \\\\ \n'
                        '\\hspace*{1cm} $\\underset{[0;1]}{\\mathop{\\min }}\\,f(t)=%s$ suy ra giá trị nhỏ nhất của hàm số là $%s$. '

                        %(latex(f),latex(f),
                        latex(daoham),
                        latex(fm),latex(fn),
                        latex(gtln),latex(gtln),
                        latex(gtnn),latex(gtnn),
                        ))
            if dang=='6':
                # Khai báo biến
                x = symbols('x')
                t = symbols('t')
                a=randint(-9,9)
                while a==0:
                    a=randint(-9,9)
                b=randint(-9,9)
                c=randint(1,9)
                while a*c-b<=0:
                    a=randint(-9,9)
                    while a==0:
                        a=randint(-9,9)
                    b=randint(-9,9)
                    c=randint(1,9)

                f=(a*t+b)/(t+c)
                ff=(a*sin(x)+b)/(sin(x)+c)
                daoham=(a*c-b)/(t+c)**2

                m=0
                n=1
                fm=Rational(b,c)
                fn=Rational(a+b,1+c)
                gtnn=fm
                gtln=fn

                du = ['$%s$'%(latex(gtln)),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(gtln+1)),
                    '$%s$'%(latex(gtln+2)),
                    '$%s$'%(latex(gtln-1)),
                    '$%s$'%(latex(gtln-2)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('''Cho hàm số $y=%s$ trên đoạn $\\left[ 0;\\dfrac{\\pi}{2} \\right]$. Giá trị lớn nhất của hàm số là'''
                                %(latex(ff)
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
                        'Đặt $\\sin x=t$ với $t \\in [0;1]$, khi đó $y=%s$. \\\\ \n'
                        'Xét hàm số $f(t)=%s$ trên đoạn $[0;1]$. \\\\ \n'
                        '\\hspace*{1cm} $f\'(t)=%s >0$ Hàm số luông đồng biến. \\\\ \n'
                        'Ta có $f(0)=%s, f(1)=%s$.\\\\ \n'
                        'Ta thấy \\\\ \n'
                        '\\hspace*{1cm} $\\underset{[0;1]}{\\mathop{\\max }}\\,f(t)=%s$ suy ra giá trị lớn nhất của hàm số là $%s$. \\\\ \n'
                        '\\hspace*{1cm} $\\underset{[0;1]}{\\mathop{\\min }}\\,f(t)=%s$ suy ra giá trị nhỏ nhất của hàm số là $%s$. '

                        %(latex(f),latex(f),
                        latex(daoham),
                        latex(fm),latex(fn),
                        latex(gtln),latex(gtln),
                        latex(gtnn),latex(gtnn),
                        ))
            if dang=='5':
                # Khai báo biến
                x = symbols('x')
                t = symbols('t')
                a=randint(-9,9)
                while a==0:
                    a=randint(-9,9)
                b=randint(-9,9)
                c=randint(1,9)
                while a*c-b<=0:
                    a=randint(-9,9)
                    while a==0:
                        a=randint(-9,9)
                    b=randint(-9,9)
                    c=randint(1,9)

                f=(a*t+b)/(t+c)
                ff=(a*sin(x)+b)/(sin(x)+c)
                daoham=(a*c-b)/(t+c)**2

                m=0
                n=1
                fm=Rational(b,c)
                fn=Rational(a+b,1+c)
                gtnn=fm
                gtln=fn

                du = ['$%s$'%(latex(gtnn)),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(gtnn-1)),
                    '$%s$'%(latex(gtnn-2)),
                    '$%s$'%(latex(gtnn-3)),
                    '$%s$'%(latex(gtnn+1)),
                    '$%s$'%(latex(gtnn+2)),
                    '$%s$'%(latex(gtnn+3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('''Cho hàm số $y=%s$ trên đoạn $\\left[ 0;\\dfrac{\\pi}{2} \\right]$. Giá trị nhỏ nhất của hàm số là'''
                                %(latex(ff)
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
                        'Đặt $\\sin x=t$ với $t \\in [0;1]$, khi đó $y=%s$. \\\\ \n'
                        'Xét hàm số $f(t)=%s$ trên đoạn $[0;1]$. \\\\ \n'
                        '\\hspace*{1cm} $f\'(t)=%s >0$ Hàm số luông đồng biến. \\\\ \n'
                        'Ta có $f(0)=%s, f(1)=%s$.\\\\ \n'
                        'Ta thấy \\\\ \n'
                        '\\hspace*{1cm} $\\underset{[0;1]}{\\mathop{\\max }}\\,f(t)=%s$ suy ra giá trị lớn nhất của hàm số là $%s$. \\\\ \n'
                        '\\hspace*{1cm} $\\underset{[0;1]}{\\mathop{\\min }}\\,f(t)=%s$ suy ra giá trị nhỏ nhất của hàm số là $%s$.'

                        %(latex(f),latex(f),
                        latex(daoham),
                        latex(fm),latex(fn),
                        latex(gtln),latex(gtln),
                        latex(gtnn),latex(gtnn),
                        ))
            if dang=='4':
                # Khai báo biến
                x = symbols('x')
                t = symbols('t')
                a=randint(-9,9)
                while a==0:
                    a=randint(-9,9)
                b=randint(-9,9)
                c=randint(-9,9)
                f=a*t**2+b*t+c
                ff=a*(cos(x))**2+b*cos(x)+c
                daoham=2*a*t+b
                x0=-Rational(b,2*a)

                m=-1
                n=1
                fm=a*(-1)**2+b*(-1)+c
                fn=a*1**2+b*1+c
                f0=a*x0**2+b*x0+c

                if m<=x0<=n:
                    gtln=max(fm,fn,f0)
                    gtnn=min(fm,fn,f0)
                if x0<=m<n:
                    gtln=max(fm,fn)
                    gtnn=min(fm,fn)
                if m<n<=x0:
                    gtln=max(fm,fn)
                    gtnn=min(fm,fn)

                du = ['$%s$'%(latex(gtnn)),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(gtnn+1)),
                    '$%s$'%(latex(gtnn+2)),
                    '$%s$'%(latex(gtnn-1)),
                    '$%s$'%(latex(gtnn-2)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('''Cho hàm số $y=%s$. Giá trị nhỏ nhất của hàm số là'''
                                %(latex(ff)
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
                        'Đặt $\\cos x=t$ với $t \\in [-1;1]$, khi đó $y=%s$. \\\\ \n'
                        'Xét hàm số $f(t)=%s$ trên đoạn $[-1;1]$. \\\\ \n'
                        '\\hspace*{1cm} $f\'(t)=%s$. \\\\ \n'
                        '\\hspace*{1cm} $f\'(t)=0 \\Leftrightarrow t=%s$. \\\\ \n'
                        'Ta có $f(-1)=%s, f(1)=%s$ và $f\\left(%s \\right)=%s$\\\\ \n'
                        'Ta thấy \\\\ \n'
                        '\\hspace*{1cm} $\\underset{[-1;1]}{\\mathop{\\max }}\\,f(t)=%s$ suy ra giá trị lớn nhất của hàm số là $%s$. \\\\ \n'
                        '\\hspace*{1cm} $\\underset{[-1;1]}{\\mathop{\\min }}\\,f(t)=%s$ suy ra giá trị nhỏ nhất của hàm số là $%s$.'

                        %(latex(f),latex(f),
                        latex(daoham),latex(x0),
                        latex(fm),latex(fn),latex(x0),latex(f0),
                        latex(gtln),latex(gtln),
                        latex(gtnn),latex(gtnn),
                        ))
            if dang=='3':
                # Khai báo biến
                x = symbols('x')
                t = symbols('t')
                a=randint(-9,9)
                while a==0:
                    a=randint(-9,9)
                b=randint(-9,9)
                c=randint(-9,9)
                f=a*t**2+b*t+c
                ff=a*(cos(x))**2+b*cos(x)+c
                daoham=2*a*t+b
                x0=-Rational(b,2*a)

                m=-1
                n=1
                fm=a*(-1)**2+b*(-1)+c
                fn=a*1**2+b*1+c
                f0=a*x0**2+b*x0+c

                if m<=x0<=n:
                    gtln=max(fm,fn,f0)
                    gtnn=min(fm,fn,f0)
                if x0<=m<n:
                    gtln=max(fm,fn)
                    gtnn=min(fm,fn)
                if m<n<=x0:
                    gtln=max(fm,fn)
                    gtnn=min(fm,fn)

                du = ['$%s$'%(latex(gtln)),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(gtln+1)),
                    '$%s$'%(latex(gtln+2)),
                    '$%s$'%(latex(gtln-1)),
                    '$%s$'%(latex(gtln-2)),
                    '$%s$'%(latex(gtln+3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('''Cho hàm số $y=%s$. Giá trị lớn nhất của hàm số là'''
                                %(latex(ff)
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
                        'Đặt $\\cos x=t$ với $t \\in [-1;1]$, khi đó $y=%s$. \\\\ \n'
                        'Xét hàm số $f(t)=%s$ trên đoạn $[-1;1]$. \\\\ \n'
                        '\\hspace*{1cm} $f\'(t)=%s$. \\\\ \n'
                        '\\hspace*{1cm} $f\'(t)=0 \\Leftrightarrow t=%s$. \\\\ \n'
                        'Ta có $f(-1)=%s, f(1)=%s$ và $f\\left(%s \\right)=%s$\\\\ \n'
                        'Ta thấy \\\\ \n'
                        '\\hspace*{1cm} $\\underset{[-1;1]}{\\mathop{\\max }}\\,f(t)=%s$ suy ra giá trị lớn nhất của hàm số là $%s$. \\\\ \n'
                        '\\hspace*{1cm} $\\underset{[-1;1]}{\\mathop{\\min }}\\,f(t)=%s$ suy ra giá trị nhỏ nhất của hàm số là $%s$. '

                        %(latex(f),latex(f),
                        latex(daoham),latex(x0),
                        latex(fm),latex(fn),latex(x0),latex(f0),
                        latex(gtln),latex(gtln),
                        latex(gtnn),latex(gtnn),
                        ))
            if dang=='2':
                # Khai báo biến
                x = symbols('x')
                t = symbols('t')
                a=randint(-9,9)
                while a==0:
                    a=randint(-9,9)
                b=randint(-9,9)
                c=randint(-9,9)
                f=a*t**2+b*t+c
                ff=a*(sin(x))**2+b*sin(x)+c
                daoham=2*a*t+b
                x0=-Rational(b,2*a)

                m=-1
                n=1
                fm=a*(-1)**2+b*(-1)+c
                fn=a*1**2+b*1+c
                f0=a*x0**2+b*x0+c

                if m<=x0<=n:
                    gtln=max(fm,fn,f0)
                    gtnn=min(fm,fn,f0)
                if x0<=m<n:
                    gtln=max(fm,fn)
                    gtnn=min(fm,fn)
                if m<n<=x0:
                    gtln=max(fm,fn)
                    gtnn=min(fm,fn)

                du = ['$%s$'%(latex(gtnn)),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(gtnn+1)),
                    '$%s$'%(latex(gtnn+2)),
                    '$%s$'%(latex(gtnn-1)),
                    '$%s$'%(latex(gtnn-2)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('''Cho hàm số $y=%s$. Giá trị nhỏ nhất của hàm số là'''
                                %(latex(ff)
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
                        'Đặt $\\sin x=t$ với $t \\in [-1;1]$, khi đó $y=%s$. \\\\ \n'
                        'Xét hàm số $f(t)=%s$ trên đoạn $[-1;1]$. \\\\ \n'
                        '\\hspace*{1cm} $f\'(t)=%s$. \\\\ \n'
                        '\\hspace*{1cm} $f\'(t)=0 \\Leftrightarrow t=%s$. \\\\ \n'
                        'Ta có $f(-1)=%s, f(1)=%s$ và $f\\left(%s \\right)=%s$\\\\ \n'
                        'Ta thấy \\\\ \n'
                        '\\hspace*{1cm} $\\underset{[-1;1]}{\\mathop{\\max }}\\,f(t)=%s$ suy ra giá trị lớn nhất của hàm số là $%s$. \\\\ \n'
                        '\\hspace*{1cm} $\\underset{[-1;1]}{\\mathop{\\min }}\\,f(t)=%s$ suy ra giá trị nhỏ nhất của hàm số là $%s$. '

                        %(latex(f),latex(f),
                        latex(daoham),latex(x0),
                        latex(fm),latex(fn),latex(x0),latex(f0),
                        latex(gtln),latex(gtln),
                        latex(gtnn),latex(gtnn),
                        ))
            if dang=='1':
                # Khai báo biến
                x = symbols('x')
                t = symbols('t')
                a=randint(-9,9)
                while a==0:
                    a=randint(-9,9)
                b=randint(-9,9)
                c=randint(-9,9)
                f=a*t**2+b*t+c
                ff=a*(sin(x))**2+b*sin(x)+c
                daoham=2*a*t+b
                x0=-Rational(b,2*a)

                m=-1
                n=1
                fm=a*(-1)**2+b*(-1)+c
                fn=a*1**2+b*1+c
                f0=a*x0**2+b*x0+c

                if m<=x0<=n:
                    gtln=max(fm,fn,f0)
                    gtnn=min(fm,fn,f0)
                if x0<=m<n:
                    gtln=max(fm,fn)
                    gtnn=min(fm,fn)
                if m<n<=x0:
                    gtln=max(fm,fn)
                    gtnn=min(fm,fn)

                du = ['$%s$'%(latex(gtln)),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(gtln+1)),
                    '$%s$'%(latex(gtln+2)),
                    '$%s$'%(latex(gtln+3)),
                    '$%s$'%(latex(gtln-1)),
                    '$%s$'%(latex(gtln-2)),
                    '$%s$'%(latex(gtln-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('''Cho hàm số $y=%s$. Giá trị lớn nhất của hàm số là'''
                                %(latex(ff)
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
                        'Đặt $\\sin x=t$ với $t \\in [-1;1]$, khi đó $y=%s$. \\\\ \n'
                        'Xét hàm số $f(t)=%s$ trên đoạn $[-1;1]$. \\\\ \n'
                        '\\hspace*{1cm} $f\'(t)=%s$. \\\\ \n'
                        '\\hspace*{1cm} $f\'(t)=0 \\Leftrightarrow t=%s$. \\\\ \n'
                        'Ta có $f(-1)=%s, f(1)=%s$ và $f\\left(%s \\right)=%s$\\\\ \n'
                        'Ta thấy \\\\ \n'
                        '\\hspace*{1cm} $\\underset{[-1;1]}{\\mathop{\\max }}\\,f(t)=%s$ suy ra giá trị lớn nhất của hàm số là $%s$. \\\\ \n'
                        '\\hspace*{1cm} $\\underset{[-1;1]}{\\mathop{\\min }}\\,f(t)=%s$ suy ra giá trị nhỏ nhất của hàm số là $%s$. '

                        %(latex(f),latex(f),
                        latex(daoham),latex(x0),
                        latex(fm),latex(fn),latex(x0),latex(f0),
                        latex(gtln),latex(gtln),
                        latex(gtnn),latex(gtnn),
                        ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-').replace('+1x', 'x').replace('-1x', '-x').replace('{\\left(x \\right)}', ' x')
            return content


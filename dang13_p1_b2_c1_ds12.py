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


def bt_dang13_p1_b2_c1_ds12(self):
            # Khai báo biến
            lisdang=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25']
            dang=random.choice(lisdang)
            if dang=='11':
                # Khai báo biến
                a = randint(-8,8)
                b = randint(1,9)
                c = randint(-15,15)
                g = randint(-4,8)
                h = randint(-3,9)
                x1= -sqrt(b)
                x2= sqrt (b)
                while a==0 or b==0 or x2>=h or g>=x1 or g>=h:
                    a = randint(-8,8)
                    b = randint(1,9)
                    c = randint(-15,15)
                    g = randint(-4,8)
                    h = randint(-3,9)
                    x1= -sqrt(b)
                    x2= sqrt (b)
                A = Rational(a,4)
                B = Rational (a*b,-2)
                C = c
                m1=A*g**4+B*g**2+C
                m2=A*h**4+B*h**2+C
                m3=A*x1**4+B*x1**2+C
                m4=A*0**4+B*0**2+C
                m5=A*x2**4+B*x2**2+C
                listmm=(m1,m2,m3,m4,m5)
                ln=max(listmm)
                nn=min(listmm)
                du = ['$\\underset{[%s;%s]}{\\mathop{\\min y}}\\,=%s$'%(latex(g),latex(h),latex(nn)),
                    '$\\underset{[%s;%s]}{\\mathop{\\max y}}\\,=%s$'%(latex(g),latex(h),latex(ln)),
                    '$\\underset{[%s;%s]}{\\mathop{\\max y}}\\,+\\underset{[%s;%s]}{\\mathop{\\min y}}\\,=%s$'%(latex(g),latex(h),latex(g),latex(h),latex(ln+nn)),
                    '$\\underset{[%s;%s]}{\\mathop{\\max y}}\\,-\\underset{%s;%s]}{\\mathop{\\min y}}\\,=%s$'%(latex(g),latex(h),latex(g),latex(h),latex(ln-nn)),
                    '$\\underset{[%s;%s]}{\\mathop{\\max y}}\\,\\cdot\\underset{[%s;%s]}{\\mathop{\\min y}}\\,=%s$'%(latex(g),latex(h),latex(g),latex(h),latex(nn*ln)),
                    ]
                da= random.choice(du)
                s = ['$\\underset{[%s;%s]}{\\mathop{\\min y}}\\,=%s$'%(latex(g),latex(h),latex(ln)),
                    '$\\underset{[%s;%s]}{\\mathop{\\max y}}\\,=%s$'%(latex(g),latex(h),latex(nn)),
                    '$\\underset{[%s;%s]}{\\mathop{\\max y}}\\,+\\underset{[%s;%s]}{\\mathop{\\min y}}\\,=%s$'%(latex(g),latex(h),latex(g),latex(h),latex(ln-nn)),
                    '$\\underset{[%s;%s]}{\\mathop{\\max y}}\\,-\\underset{[%s;%s]}{\\mathop{\\min y}}\\,=%s$'%(latex(g),latex(h),latex(g),latex(h),latex(nn-ln)),
                    '$\\underset{[%s;%s]}{\\mathop{\\max y}}\\,\\cdot\\underset{[%s;%s]}{\\mathop{\\min y}}\\,=%s$'%(latex(g),latex(h),latex(g),latex(h),latex(nn*ln+1)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = '''Cho hàm số $y=%sx^4+%sx^2+%s$. Mệnh đề nào dưới đây đúng? '''%(latex(A),latex(B),latex(C))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=( '''$y'= %sx^3+%s x.\\\\ \n'''
                        '''y'=0 \\Leftrightarrow \\hoac{& x=0 \\in\\left( %s;%s\\right) \\\\& x=%s \\in\\left( %s;%s\\right) \\\\& x=%s \\in\\left( %s;%s\\right).}$\\\\ \n'''
                        '''Ta có: ${y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm} {y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm} {y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm}{y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm} {y}{\\left(%s\\right)}=%s.$\\\\ \n'''
                        '''Vậy\\\\ \n'''
                        '''\\hspace*{1cm}$\\underset{[%s;%s]}{\\mathop{\\max y}}\\,=%s$;\\\\ \n'''
                        '''\\hspace*{1cm}$\\underset{[%s;%s]}{\\mathop{\\min y}}\\,=%s$;\\\\ \n'''
                        '''\\hspace*{1cm}$\\underset{[%s;%s]}{\\mathop{\\max y}}\\,+\\underset{[%s;%s]}{\\mathop{\\min y}}\\,=\\left(%s\\right)+\\left(%s\\right)=%s$;\\\\ \n'''
                        '''\\hspace*{1cm}$\\underset{[%s;%s]}{\\mathop{\\max y}}\\,-\\underset{[%s;%s]}{\\mathop{\\min y}}\\,=\\left(%s\\right)-\\left(%s\\right)=%s$;\\\\ \n''' 
                        '''\\hspace*{1cm}$\\underset{[%s;%s]}{\\mathop{\\max y}}\\,\\cdot\\underset{[%s;%s]}{\\mathop{\\min y}}\\,=\\left(%s\\right)\\cdot\\left(%s\\right)=%s$.'''
                        %(latex(4*A),latex(2*B),
                        latex(g),latex(h),latex(x1),latex(g),latex(h),latex(x2),latex(g),latex(h),
                        latex(g),latex(m1),latex(h),latex(m2),latex(x1),latex(m3),latex(0),latex(m4),latex(x2),latex(m5),
                        latex(g),latex(h),latex(ln),
                        latex(g),latex(h),latex(nn),
                        latex(g),latex(h),latex(g),latex(h),latex(ln),latex(nn),latex(ln+nn),
                        latex(g),latex(h),latex(g),latex(h),latex(ln),latex(nn),latex(ln-nn),
                        latex(g),latex(h),latex(g),latex(h),latex(ln),latex(nn),latex(ln*nn)))

            if dang=='12':
                # Khai báo biến
                a = randint(-8,8)
                b = randint(1,9)
                c = randint(-15,15)
                g = randint(-4,8)
                h = randint(-3,9)
                x1= -sqrt(b)
                x2= sqrt (b)
                while a==0 or b==0 or x2>=h or g>=x1 or g>=h:
                    a = randint(-8,8)
                    b = randint(1,9)
                    c = randint(-15,15)
                    g = randint(-4,8)
                    h = randint(-3,9)
                    x1= -sqrt(b)
                    x2= sqrt (b)
                A = Rational(a,4)
                B = Rational (a*b,-2)
                C = c
                m1=A*g**4+B*g**2+C
                m2=A*h**4+B*h**2+C
                m3=A*x1**4+B*x1**2+C
                m4=A*0**4+B*0**2+C
                m5=A*x2**4+B*x2**2+C
                listmm=(m1,m2,m3,m4,m5)
                ln=max(listmm)
                nn=min(listmm)
                du = ['$%s$'%(latex(nn)),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(nn+1)),
                '$%s$'%(latex(nn+2)),
                '$%s$'%(latex(nn+3)),
                '$%s$'%(latex(nn-1)),
                '$%s$'%(latex(nn-2)),
                '$%s$'%(latex(nn-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = '''Giá trị nhỏ nhất của hàm số $y=%sx^4+%sx^2+%s$ trên đoạn [%s;%s] bằng '''%(latex(A),latex(B),latex(C),latex(g),latex(h))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=( '''$y'= %sx^3+%s x.\\\\ \n'''
                        '''y'=0 \\Leftrightarrow \\hoac{& x=0 \\in\\left( %s;%s\\right) \\\\& x=%s \\in\\left( %s;%s\\right) \\\\& x=%s \\in\\left( %s;%s\\right).}$\\\\ \n'''
                        '''Ta có: ${y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm} {y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm} {y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm}{y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm} {y}{\\left(%s\\right)}=%s.$\\\\ \n'''
                        '''Vậy\\\\ \n'''
                        '''\\hspace*{1cm}$\\underset{[%s;%s]}{\\mathop{\\min y}}\\,=%s$.'''
                        %(latex(4*A),latex(2*B),
                        latex(g),latex(h),latex(x1),latex(g),latex(h),latex(x2),latex(g),latex(h),
                        latex(g),latex(m1),latex(h),latex(m2),latex(x1),latex(m3),latex(0),latex(m4),latex(x2),latex(m5),
                        latex(g),latex(h),latex(nn)
                        ))

            if dang=='13':
                # Khai báo biến
                a = randint(-8,8)
                b = randint(1,9)
                c = randint(-15,15)
                g = randint(-4,8)
                h = randint(-3,9)
                x1= -sqrt(b)
                x2= sqrt (b)
                while a==0 or b==0 or x2>=h or g>=x1 or g>=h:
                    a = randint(-8,8)
                    b = randint(1,9)
                    c = randint(-15,15)
                    g = randint(-4,8)
                    h = randint(-3,9)
                    x1= -sqrt(b)
                    x2= sqrt (b)
                A = Rational(a,4)
                B = Rational (a*b,-2)
                C = c
                m1=A*g**4+B*g**2+C
                m2=A*h**4+B*h**2+C
                m3=A*x1**4+B*x1**2+C
                m4=A*0**4+B*0**2+C
                m5=A*x2**4+B*x2**2+C
                listmm=(m1,m2,m3,m4,m5)
                ln=max(listmm)
                nn=min(listmm)
                du = ['$%s$'%(latex(ln)),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(ln+1)),
                '$%s$'%(latex(ln+2)),
                '$%s$'%(latex(ln+3)),
                '$%s$'%(latex(ln-1)),
                '$%s$'%(latex(ln-2)),
                '$%s$'%(latex(ln-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = '''Giá trị lớn nhất của hàm số $y=%sx^4+%sx^2+%s$ trên đoạn [%s;%s] bằng '''%(latex(A),latex(B),latex(C),latex(g),latex(h))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=( '''$y'= %sx^3+%s x.\\\\ \n'''
                        '''y'=0 \\Leftrightarrow \\hoac{& x=0 \\in\\left( %s;%s\\right) \\\\& x=%s \\in\\left( %s;%s\\right) \\\\& x=%s \\in\\left( %s;%s\\right).}$\\\\ \n'''
                        '''Ta có: ${y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm} {y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm} {y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm}{y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm} {y}{\\left(%s\\right)}=%s.$\\\\ \n'''
                        '''Vậy\\\\ \n'''
                        '''\\hspace*{1cm}$\\underset{[%s;%s]}{\\mathop{\\max y}}\\,=%s$.'''
                        %(latex(4*A),latex(2*B),
                        latex(g),latex(h),latex(x1),latex(g),latex(h),latex(x2),latex(g),latex(h),
                        latex(g),latex(m1),latex(h),latex(m2),latex(x1),latex(m3),latex(0),latex(m4),latex(x2),latex(m5),
                        latex(g),latex(h),latex(ln)
                        ))

            if dang=='14':
                # Khai báo biến
                a = randint(-8,8)
                b = randint(1,9)
                c = randint(-15,15)
                g = randint(-4,8)
                h = randint(-3,9)
                x1= -sqrt(b)
                x2= sqrt (b)
                while a==0 or b==0 or x2>=h or g>=x1 or g>=h:
                    a = randint(-8,8)
                    b = randint(1,9)
                    c = randint(-15,15)
                    g = randint(-4,8)
                    h = randint(-3,9)
                    x1= -sqrt(b)
                    x2= sqrt (b)
                A = Rational(a,4)
                B = Rational (a*b,-2)
                C = c
                m1=A*g**4+B*g**2+C
                m2=A*h**4+B*h**2+C
                m3=A*x1**4+B*x1**2+C
                m4=A*0**4+B*0**2+C
                m5=A*x2**4+B*x2**2+C
                listmm=(m1,m2,m3,m4,m5)
                ln=max(listmm)
                nn=min(listmm)
                du = ['$%s$'%(latex(ln+nn))
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(ln+nn+1)),
                '$%s$'%(latex(ln+nn+2)),
                '$%s$'%(latex(ln+nn+3)),
                '$%s$'%(latex(ln+nn-1)),
                '$%s$'%(latex(ln+nn-2)),
                '$%s$'%(latex(ln+nn-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = '''Cho hàm số $y=%sx^4+%sx^2+%s$ khi đó $\\underset{[%s;%s]}{\\mathop{\\max y}}\\,+\\underset{[%s;%s]}{\\mathop{\\min y}}\\,$ bằng '''%(latex(A),latex(B),latex(C),latex(g),latex(h),latex(g),latex(h))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=( '''$y'= %sx^3+%s x.\\\\ \n'''
                        '''y'=0 \\Leftrightarrow \\hoac{& x=0 \\in\\left( %s;%s\\right) \\\\& x=%s \\in\\left( %s;%s\\right) \\\\& x=%s \\in\\left( %s;%s\\right).}$\\\\ \n'''
                        '''Ta có: ${y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm} {y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm} {y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm}{y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm} {y}{\\left(%s\\right)}=%s.$\\\\ \n'''
                        '''Vậy\\\\ \n'''
                        '''$\\underset{[%s;%s]}{\\mathop{\\max y}}\\,+\\underset{[%s;%s]}{\\mathop{\\min y}}\\,=\\left(%s\\right)+\\left(%s\\right)=%s$.'''
                        %(latex(4*A),latex(2*B),
                        latex(g),latex(h),latex(x1),latex(g),latex(h),latex(x2),latex(g),latex(h),
                        latex(g),latex(m1),latex(h),latex(m2),latex(x1),latex(m3),latex(0),latex(m4),latex(x2),latex(m5),
                        latex(g),latex(h),latex(g),latex(h),latex(ln),latex(nn),latex(ln+nn)
                        ))

            if dang=='15':
                # Khai báo biến
                a = randint(-8,8)
                b = randint(1,9)
                c = randint(-15,15)
                g = randint(-4,8)
                h = randint(-3,9)
                x1= -sqrt(b)
                x2= sqrt (b)
                while a==0 or b==0 or x2>=h or g>=x1 or g>=h:
                    a = randint(-8,8)
                    b = randint(1,9)
                    c = randint(-15,15)
                    g = randint(-4,8)
                    h = randint(-3,9)
                    x1= -sqrt(b)
                    x2= sqrt (b)
                A = Rational(a,4)
                B = Rational (a*b,-2)
                C = c
                m1=A*g**4+B*g**2+C
                m2=A*h**4+B*h**2+C
                m3=A*x1**4+B*x1**2+C
                m4=A*0**4+B*0**2+C
                m5=A*x2**4+B*x2**2+C
                listmm=(m1,m2,m3,m4,m5)
                ln=max(listmm)
                nn=min(listmm)
                du = ['$%s$'%(latex(ln-nn))
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(ln-nn+1)),
                '$%s$'%(latex(ln-nn+2)),
                '$%s$'%(latex(ln-nn+3)),
                '$%s$'%(latex(ln-nn-1)),
                '$%s$'%(latex(ln-nn-2)),
                '$%s$'%(latex(ln-nn-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = '''Cho hàm số $y=%sx^4+%sx^2+%s$ khi đó $\\underset{[%s;%s]}{\\mathop{\\max y}}\\,-\\underset{[%s;%s]}{\\mathop{\\min y}}\\,$ bằng '''%(latex(A),latex(B),latex(C),latex(g),latex(h),latex(g),latex(h))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=( '''$y'= %sx^3+%s x.\\\\ \n'''
                        '''y'=0 \\Leftrightarrow \\hoac{& x=0 \\in\\left( %s;%s\\right) \\\\& x=%s \\in\\left( %s;%s\\right) \\\\& x=%s \\in\\left( %s;%s\\right).}$\\\\ \n'''
                        '''Ta có: ${y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm} {y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm} {y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm}{y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm} {y}{\\left(%s\\right)}=%s.$\\\\ \n'''
                        '''Vậy\\\\ \n'''
                        '''$\\underset{[%s;%s]}{\\mathop{\\max y}}\\,-\\underset{[%s;%s]}{\\mathop{\\min y}}\\,=\\left(%s\\right)-\\left(%s\\right)=%s$.'''
                        %(latex(4*A),latex(2*B),
                        latex(g),latex(h),latex(x1),latex(g),latex(h),latex(x2),latex(g),latex(h),
                        latex(g),latex(m1),latex(h),latex(m2),latex(x1),latex(m3),latex(0),latex(m4),latex(x2),latex(m5),
                        latex(g),latex(h),latex(g),latex(h),latex(ln),latex(nn),latex(ln-nn)
                        ))

            if dang=='16':
                # Khai báo biến
                a = randint(-8,8)
                b = randint(1,9)
                c = randint(-15,15)
                g = randint(-4,8)
                h = randint(-3,9)
                x1= -sqrt(b)
                x2= sqrt (b)
                while a==0 or b==0 or x2>=h or g>=x1 or g>=h:
                    a = randint(-8,8)
                    b = randint(1,9)
                    c = randint(-15,15)
                    g = randint(-4,8)
                    h = randint(-3,9)
                    x1= -sqrt(b)
                    x2= sqrt (b)
                A = Rational(a,4)
                B = Rational (a*b,-2)
                C = c
                m1=A*g**4+B*g**2+C
                m2=A*h**4+B*h**2+C
                m3=A*x1**4+B*x1**2+C
                m4=A*0**4+B*0**2+C
                m5=A*x2**4+B*x2**2+C
                listmm=(m1,m2,m3,m4,m5)
                ln=max(listmm)
                nn=min(listmm)
                du = ['$%s$'%(latex(ln*nn))
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(ln*nn+1)),
                '$%s$'%(latex(ln*nn+2)),
                '$%s$'%(latex(ln*nn+3)),
                '$%s$'%(latex(ln*nn-1)),
                '$%s$'%(latex(ln*nn-2)),
                '$%s$'%(latex(ln*nn-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = '''Cho hàm số $y=%sx^4+%sx^2+%s$ khi đó $\\underset{[%s;%s]}{\\mathop{\\max y}}\\,\\cdot\\underset{[%s;%s]}{\\mathop{\\min y}}\\,$ bằng '''%(latex(A),latex(B),latex(C),latex(g),latex(h),latex(g),latex(h))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=( '''$y'= %sx^3+%s x.\\\\ \n'''
                        '''y'=0 \\Leftrightarrow \\hoac{& x=0 \\in\\left( %s;%s\\right) \\\\& x=%s \\in\\left( %s;%s\\right) \\\\& x=%s \\in\\left( %s;%s\\right).}$\\\\ \n'''
                        '''Ta có: ${y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm} {y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm} {y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm}{y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm} {y}{\\left(%s\\right)}=%s.$\\\\ \n'''
                        '''Vậy\\\\ \n'''
                        '''$\\underset{[%s;%s]}{\\mathop{\\max y}}\\,\\cdot\\underset{[%s;%s]}{\\mathop{\\min y}}\\,=\\left(%s\\right)\\cdot\\left(%s\\right)=%s$.'''
                        %(latex(4*A),latex(2*B),
                        latex(g),latex(h),latex(x1),latex(g),latex(h),latex(x2),latex(g),latex(h),
                        latex(g),latex(m1),latex(h),latex(m2),latex(x1),latex(m3),latex(0),latex(m4),latex(x2),latex(m5),
                        latex(g),latex(h),latex(g),latex(h),latex(ln),latex(nn),latex(ln*nn)
                        ))

            if dang=='17':
                # Khai báo biến
                a = randint(-8,8)
                b = randint(1,9)
                c = randint(-15,15)
                g = randint(-4,8)
                h = randint(-3,9)
                x1= -sqrt(b)
                x2= sqrt (b)
                while a==0 or b==0 or x2>=h or g<=x1 or g>=0 or g>=h:
                    a = randint(-8,8)
                    b = randint(1,9)
                    c = randint(-15,15)
                    g = randint(-4,8)
                    h = randint(-3,9)
                    x1= -sqrt(b)
                    x2= sqrt (b)
                A = Rational(a,4)
                B = Rational (a*b,-2)
                C = c
                m1=A*g**4+B*g**2+C
                m2=A*h**4+B*h**2+C
                m3=A*x1**4+B*x1**2+C
                m4=A*0**4+B*0**2+C
                m5=A*x2**4+B*x2**2+C
                listmm=(m1,m2,m4,m5)
                ln=max(listmm)
                nn=min(listmm)
                du = ['$\\underset{[%s;%s]}{\\mathop{\\min y}}\\,=%s$'%(latex(g),latex(h),latex(nn)),
                    '$\\underset{[%s;%s]}{\\mathop{\\max y}}\\,=%s$'%(latex(g),latex(h),latex(ln)),
                    '$\\underset{[%s;%s]}{\\mathop{\\max y}}\\,+\\underset{[%s;%s]}{\\mathop{\\min y}}\\,=%s$'%(latex(g),latex(h),latex(g),latex(h),latex(ln+nn)),
                    '$\\underset{[%s;%s]}{\\mathop{\\max y}}\\,-\\underset{%s;%s]}{\\mathop{\\min y}}\\,=%s$'%(latex(g),latex(h),latex(g),latex(h),latex(ln-nn)),
                    '$\\underset{[%s;%s]}{\\mathop{\\max y}}\\,\\cdot\\underset{[%s;%s]}{\\mathop{\\min y}}\\,=%s$'%(latex(g),latex(h),latex(g),latex(h),latex(nn*ln)),
                    ]
                da= random.choice(du)
                s = ['$\\underset{[%s;%s]}{\\mathop{\\min y}}\\,=%s$'%(latex(g),latex(h),latex(ln)),
                    '$\\underset{[%s;%s]}{\\mathop{\\max y}}\\,=%s$'%(latex(g),latex(h),latex(nn)),
                    '$\\underset{[%s;%s]}{\\mathop{\\max y}}\\,+\\underset{[%s;%s]}{\\mathop{\\min y}}\\,=%s$'%(latex(g),latex(h),latex(g),latex(h),latex(ln-nn)),
                    '$\\underset{[%s;%s]}{\\mathop{\\max y}}\\,-\\underset{[%s;%s]}{\\mathop{\\min y}}\\,=%s$'%(latex(g),latex(h),latex(g),latex(h),latex(nn-ln)),
                    '$\\underset{[%s;%s]}{\\mathop{\\max y}}\\,\\cdot\\underset{[%s;%s]}{\\mathop{\\min y}}\\,=%s$'%(latex(g),latex(h),latex(g),latex(h),latex(nn*ln+1)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = '''Cho hàm số $y=%sx^4+%sx^2+%s$. Mệnh đề nào dưới đây đúng? '''%(latex(A),latex(B),latex(C))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=( '''$y'= %sx^3+%s x.\\\\ \n'''
                        '''y'=0 \\Leftrightarrow \\hoac{& x=0 \\in\\left( %s;%s\\right) \\\\& x=%s \\notin\\left( %s;%s\\right) \\\\& x=%s \\in\\left( %s;%s\\right).}$\\\\ \n'''
                        '''Ta có: ${y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm} {y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm}{y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm} {y}{\\left(%s\\right)}=%s.$\\\\ \n'''
                        '''Vậy\\\\ \n'''
                        '''\\hspace*{1cm}$\\underset{[%s;%s]}{\\mathop{\\max y}}\\,=%s$;\\\\ \n'''
                        '''\\hspace*{1cm}$\\underset{[%s;%s]}{\\mathop{\\min y}}\\,=%s$;\\\\ \n'''
                        '''\\hspace*{1cm}$\\underset{[%s;%s]}{\\mathop{\\max y}}\\,+\\underset{[%s;%s]}{\\mathop{\\min y}}\\,=\\left(%s\\right)+\\left(%s\\right)=%s$;\\\\ \n'''
                        '''\\hspace*{1cm}$\\underset{[%s;%s]}{\\mathop{\\max y}}\\,-\\underset{[%s;%s]}{\\mathop{\\min y}}\\,=\\left(%s\\right)-\\left(%s\\right)=%s$;\\\\ \n''' 
                        '''\\hspace*{1cm}$\\underset{[%s;%s]}{\\mathop{\\max y}}\\,\\cdot\\underset{[%s;%s]}{\\mathop{\\min y}}\\,=\\left(%s\\right)\\cdot\\left(%s\\right)=%s$.'''
                        %(latex(4*A),latex(2*B),
                        latex(g),latex(h),latex(x1),latex(g),latex(h),latex(x2),latex(g),latex(h),
                        latex(g),latex(m1),latex(h),latex(m2),latex(0),latex(m4),latex(x2),latex(m5),
                        latex(g),latex(h),latex(ln),
                        latex(g),latex(h),latex(nn),
                        latex(g),latex(h),latex(g),latex(h),latex(ln),latex(nn),latex(ln+nn),
                        latex(g),latex(h),latex(g),latex(h),latex(ln),latex(nn),latex(ln-nn),
                        latex(g),latex(h),latex(g),latex(h),latex(ln),latex(nn),latex(ln*nn)))

            if dang=='18':
                # Khai báo biến
                a = randint(-8,8)
                b = randint(1,9)
                c = randint(-15,15)
                g = randint(-4,8)
                h = randint(-3,9)
                x1= -sqrt(b)
                x2= sqrt (b)
                while a==0 or b==0 or x2>=h or g<=x1 or g>=0 or g>=h:
                    a = randint(-8,8)
                    b = randint(1,9)
                    c = randint(-15,15)
                    g = randint(-4,8)
                    h = randint(-3,9)
                    x1= -sqrt(b)
                    x2= sqrt (b)
                A = Rational(a,4)
                B = Rational (a*b,-2)
                C = c
                m1=A*g**4+B*g**2+C
                m2=A*h**4+B*h**2+C
                m3=A*x1**4+B*x1**2+C
                m4=A*0**4+B*0**2+C
                m5=A*x2**4+B*x2**2+C
                listmm=(m1,m2,m4,m5)
                ln=max(listmm)
                nn=min(listmm)
                du = ['$%s$'%(latex(ln+nn)),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(ln+nn-3)),
                '$%s$'%(latex(ln+nn+1)),
                '$%s$'%(latex(ln+nn+2)),
                '$%s$'%(latex(ln+nn+3)),
                '$%s$'%(latex(ln+nn-1)),
                '$%s$'%(latex(ln+nn-2)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = '''Cho hàm số $y=%sx^4+%sx^2+%s$. Gọi $M;m$ lần lượt là giá trị lớn nhất và giá trị nhỏ nhất của hàm số trên đoạn [%s;%s]. Khi đó $M+m$ bằng '''%(latex(A),latex(B),latex(C),latex(g),latex(h))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=( '''$y'= %sx^3+%s x.\\\\ \n'''
                        '''y'=0 \\Leftrightarrow \\hoac{& x=0 \\in\\left( %s;%s\\right) \\\\& x=%s \\notin\\left( %s;%s\\right) \\\\& x=%s \\in\\left( %s;%s\\right).}$\\\\ \n'''
                        '''Ta có: ${y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm} {y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm}{y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm} {y}{\\left(%s\\right)}=%s.$\\\\ \n'''
                        '''Khi đó $M=\\underset{[%s;%s]}{\\mathop{\\max y}}\\,=%s$;\\hspace*{1cm}$m=\\underset{[%s;%s]}{\\mathop{\\min y}}\\,=%s$.\\\\ \n'''
                        '''Vậy\\\\ \n'''
                        '''\\hspace*{1cm}$M+m=\\left(%s\\right)+\\left(%s\\right)=%s$.'''
                        %(latex(4*A),latex(2*B),
                        latex(g),latex(h),latex(x1),latex(g),latex(h),latex(x2),latex(g),latex(h),
                        latex(g),latex(m1),latex(h),latex(m2),latex(0),latex(m4),latex(x2),latex(m5),
                        latex(g),latex(h),latex(ln),latex(g),latex(h),latex(nn),
                        latex(ln),latex(nn),latex(ln+nn)
                        ))
            if dang=='19':
                # Khai báo biến
                a = randint(-8,8)
                b = randint(1,9)
                c = randint(-15,15)
                g = randint(-4,8)
                h = randint(-3,9)
                x1= -sqrt(b)
                x2= sqrt (b)
                while a==0 or b==0 or x2>=h or g<=x1 or g>=0 or g>=h or c==0:
                    a = randint(-8,8)
                    b = randint(1,9)
                    c = randint(-15,15)
                    g = randint(-4,8)
                    h = randint(-3,9)
                    x1= -sqrt(b)
                    x2= sqrt (b)
                A = Rational(a,4)
                B = Rational (a*b,-2)
                C = c
                m1=A*g**4+B*g**2+C
                m2=A*h**4+B*h**2+C
                m3=A*x1**4+B*x1**2+C
                m4=A*0**4+B*0**2+C
                m5=A*x2**4+B*x2**2+C
                listmm=(m1,m2,m4,m5)
                ln=max(listmm)
                nn=min(listmm)
                du = ['$%s$'%(latex(ln-nn)),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(ln-nn+1)),
                '$%s$'%(latex(ln-nn+2)),
                '$%s$'%(latex(ln-nn+3)),
                '$%s$'%(latex(ln-nn-1)),
                '$%s$'%(latex(ln-nn-2)),
                '$%s$'%(latex(ln-nn-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = '''Cho hàm số $y=%sx^4+%sx^2+%s$. Gọi $M;m$ lần lượt là giá trị lớn nhất và giá trị nhỏ nhất của hàm số trên đoạn [%s;%s]. Khi đó $M-m$ bằng '''%(latex(A),latex(B),latex(C),latex(g),latex(h))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=( '''$y'= %sx^3+%s x.\\\\ \n'''
                        '''y'=0 \\Leftrightarrow \\hoac{& x=0 \\in\\left( %s;%s\\right) \\\\& x=%s \\notin\\left( %s;%s\\right) \\\\& x=%s \\in\\left( %s;%s\\right).}$\\\\ \n'''
                        '''Ta có: ${y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm} {y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm}{y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm} {y}{\\left(%s\\right)}=%s.$\\\\ \n'''
                        '''Khi đó $M=\\underset{[%s;%s]}{\\mathop{\\max y}}\\,=%s$;\\hspace*{1cm}$m=\\underset{[%s;%s]}{\\mathop{\\min y}}\\,=%s$.'''
                        '''Vậy\\\\ \n'''
                        '''\\hspace*{1cm}$M-m=\\left(%s\\right)-\\left(%s\\right)=%s$.\\\\ \n'''
                        %(latex(4*A),latex(2*B),
                        latex(g),latex(h),latex(x1),latex(g),latex(h),latex(x2),latex(g),latex(h),
                        latex(g),latex(m1),latex(h),latex(m2),latex(0),latex(m4),latex(x2),latex(m5),
                        latex(g),latex(h),latex(ln),latex(g),latex(h),latex(nn),
                        latex(ln),latex(nn),latex(ln-nn)
                        ))

            if dang=='20':
                # Khai báo biến
                a = randint(-8,8)
                b = randint(1,9)
                c = randint(-15,15)
                g = randint(-4,8)
                h = randint(-3,9)
                x1= -sqrt(b)
                x2= sqrt (b)
                while a==0 or b==0 or x2>=h or g<=x1 or g>=0 or g>=h or c==0:
                    a = randint(-8,8)
                    b = randint(1,9)
                    c = randint(-15,15)
                    g = randint(-4,8)
                    h = randint(-3,9)
                    x1= -sqrt(b)
                    x2= sqrt (b)
                A = Rational(a,4)
                B = Rational (a*b,-2)
                C = c
                m1=A*g**4+B*g**2+C
                m2=A*h**4+B*h**2+C
                m3=A*x1**4+B*x1**2+C
                m4=A*0**4+B*0**2+C
                m5=A*x2**4+B*x2**2+C
                listmm=(m1,m2,m4,m5)
                ln=max(listmm)
                nn=min(listmm)
                du = ['$%s$'%(latex(ln*nn)),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(ln*nn+1)),
                '$%s$'%(latex(ln*nn+2)),
                '$%s$'%(latex(ln*nn+3)),
                '$%s$'%(latex(ln*nn-1)),
                '$%s$'%(latex(ln*nn-2)),
                '$%s$'%(latex(ln*nn-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = '''Cho hàm số $y=%sx^4+%sx^2+%s$. Gọi $M;m$ lần lượt là giá trị lớn nhất và giá trị nhỏ nhất của hàm số trên đoạn [%s;%s]. Khi đó $M\\cdot m$ bằng '''%(latex(A),latex(B),latex(C),latex(g),latex(h))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=( '''$y'= %sx^3+%s x.\\\\ \n'''
                        '''y'=0 \\Leftrightarrow \\hoac{& x=0 \\in\\left( %s;%s\\right) \\\\& x=%s \\notin\\left( %s;%s\\right) \\\\& x=%s \\in\\left( %s;%s\\right).}$\\\\ \n'''
                        '''Ta có: ${y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm} {y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm}{y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm} {y}{\\left(%s\\right)}=%s.$\\\\ \n'''
                        '''Khi đó $M=\\underset{[%s;%s]}{\\mathop{\\max y}}\\,=%s$;\\hspace*{1cm}$m=\\underset{[%s;%s]}{\\mathop{\\min y}}\\,=%s$.\\\\ \n'''
                        '''Vậy\\\\ \n'''
                        '''\\hspace*{1cm}$M\\cdot m=\\left(%s\\right)\\cdot\\left(%s\\right)=%s$.'''
                        %(latex(4*A),latex(2*B),
                        latex(g),latex(h),latex(x1),latex(g),latex(h),latex(x2),latex(g),latex(h),
                        latex(g),latex(m1),latex(h),latex(m2),latex(0),latex(m4),latex(x2),latex(m5),
                        latex(g),latex(h),latex(ln),latex(g),latex(h),latex(nn),
                        latex(ln),latex(nn),latex(ln*nn)
                        ))

            if dang=='21':
                # Khai báo biến
                a = randint(-8,8)
                b = randint(1,9)
                c = randint(-15,15)
                g = randint(-4,8)
                h = randint(-3,9)
                x1= -sqrt(b)
                x2= sqrt (b)
                while a==0 or b==0 or x2>=h or g<=x1 or g>=0 or g>=h or c==0:
                    a = randint(-8,8)
                    b = randint(1,9)
                    c = randint(-15,15)
                    g = randint(-4,8)
                    h = randint(-3,9)
                    x1= -sqrt(b)
                    x2= sqrt (b)
                A = Rational(a,4)
                B = Rational (a*b,-2)
                C = c
                m1=A*g**4+B*g**2+C
                m2=A*h**4+B*h**2+C
                m3=A*x1**4+B*x1**2+C
                m4=A*0**4+B*0**2+C
                m5=A*x2**4+B*x2**2+C
                listmm=(m1,m2,m4,m5)
                ln=max(listmm)
                nn=min(listmm)
                du = ['$%s$'%(latex(ln)),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(ln+1)),
                '$%s$'%(latex(ln+2)),
                '$%s$'%(latex(ln+3)),
                '$%s$'%(latex(ln-1)),
                '$%s$'%(latex(ln-2)),
                '$%s$'%(latex(ln-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = '''Cho hàm số $y=%sx^4+%sx^2+%s$. Giá trị lớn nhất của hàm số trên đoạn [%s;%s] bằng '''%(latex(A),latex(B),latex(C),latex(g),latex(h))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=( '''$y'= %sx^3+%s x.\\\\ \n'''
                        '''y'=0 \\Leftrightarrow \\hoac{& x=0 \\in\\left( %s;%s\\right) \\\\& x=%s \\notin\\left( %s;%s\\right) \\\\& x=%s \\in\\left( %s;%s\\right).}$\\\\ \n'''
                        '''Ta có: ${y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm} {y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm}{y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm} {y}{\\left(%s\\right)}=%s.$\\\\ \n'''
                        '''Vậy\\\\ \n'''
                        '''\\hspace*{1cm}$\\underset{[%s;%s]}{\\mathop{\\max y}}\\,=%s$.'''
                        %(latex(4*A),latex(2*B),
                        latex(g),latex(h),latex(x1),latex(g),latex(h),latex(x2),latex(g),latex(h),
                        latex(g),latex(m1),latex(h),latex(m2),latex(0),latex(m4),latex(x2),latex(m5),
                        latex(g),latex(h),latex(ln)
                        ))

            if dang=='22':
                # Khai báo biến
                a = randint(-8,8)
                b = randint(1,9)
                c = randint(-15,15)
                g = randint(-4,8)
                h = randint(-3,9)
                x1= -sqrt(b)
                x2= sqrt (b)
                while a==0 or b==0 or x2>=h or g<=x1 or g>=0 or g>=h or c==0:
                    a = randint(-8,8)
                    b = randint(1,9)
                    c = randint(-15,15)
                    g = randint(-4,8)
                    h = randint(-3,9)
                    x1= -sqrt(b)
                    x2= sqrt (b)
                A = Rational(a,4)
                B = Rational (a*b,-2)
                C = c
                m1=A*g**4+B*g**2+C
                m2=A*h**4+B*h**2+C
                m3=A*x1**4+B*x1**2+C
                m4=A*0**4+B*0**2+C
                m5=A*x2**4+B*x2**2+C
                listmm=(m1,m2,m4,m5)
                ln=max(listmm)
                nn=min(listmm)
                du = ['$%s$'%(latex(nn)),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(nn+1)),
                '$%s$'%(latex(nn+2)),
                '$%s$'%(latex(nn+3)),
                '$%s$'%(latex(nn-1)),
                '$%s$'%(latex(nn-2)),
                '$%s$'%(latex(nn-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = '''Cho hàm số $y=%sx^4+%sx^2+%s$. Giá trị nhỏ nhất của hàm số trên đoạn [%s;%s] bằng '''%(latex(A),latex(B),latex(C),latex(g),latex(h))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=( '''$y'= %sx^3+%s x.\\\\ \n'''
                        '''y'=0 \\Leftrightarrow \\hoac{& x=0 \\in\\left( %s;%s\\right) \\\\& x=%s \\notin\\left( %s;%s\\right) \\\\& x=%s \\in\\left( %s;%s\\right).}$\\\\ \n'''
                        '''Ta có: ${y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm} {y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm}{y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm} {y}{\\left(%s\\right)}=%s.$\\\\ \n'''
                        '''Vậy\\\\ \n'''
                        '''\\hspace*{1cm}$\\underset{[%s;%s]}{\\mathop{\\min y}}\\,=%s$.'''
                        %(latex(4*A),latex(2*B),
                        latex(g),latex(h),latex(x1),latex(g),latex(h),latex(x2),latex(g),latex(h),
                        latex(g),latex(m1),latex(h),latex(m2),latex(0),latex(m4),latex(x2),latex(m5),
                        latex(g),latex(h),latex(nn)
                        ))

            if dang=='23':
                # Khai báo biến
                a = randint(-8,8)
                b = randint(1,9)
                c = randint(-15,15)
                g = randint(-4,8)
                h = randint(-3,9)
                x1= -sqrt(b)
                x2= sqrt (b)
                while a==0 or b==0 or x2>=h or g<=0 or g>=x2 or g>=h:
                    a = randint(-8,8)
                    b = randint(1,9)
                    c = randint(-15,15)
                    g = randint(-4,8)
                    h = randint(-3,9)
                    x1= -sqrt(b)
                    x2= sqrt (b)
                A = Rational(a,4)
                B = Rational (a*b,-2)
                C = c
                m1=A*g**4+B*g**2+C
                m2=A*h**4+B*h**2+C
                m3=A*x1**4+B*x1**2+C
                m4=A*0**4+B*0**2+C
                m5=A*x2**4+B*x2**2+C
                listmm=(m1,m2,m5)
                ln=max(listmm)
                nn=min(listmm)
                du = ['$\\underset{[%s;%s]}{\\mathop{\\min y}}\\,=%s$'%(latex(g),latex(h),latex(nn)),
                    '$\\underset{[%s;%s]}{\\mathop{\\max y}}\\,=%s$'%(latex(g),latex(h),latex(ln)),
                    '$\\underset{[%s;%s]}{\\mathop{\\max y}}\\,+\\underset{[%s;%s]}{\\mathop{\\min y}}\\,=%s$'%(latex(g),latex(h),latex(g),latex(h),latex(ln+nn)),
                    '$\\underset{[%s;%s]}{\\mathop{\\max y}}\\,-\\underset{%s;%s]}{\\mathop{\\min y}}\\,=%s$'%(latex(g),latex(h),latex(g),latex(h),latex(ln-nn)),
                    '$\\underset{[%s;%s]}{\\mathop{\\max y}}\\,\\cdot\\underset{[%s;%s]}{\\mathop{\\min y}}\\,=%s$'%(latex(g),latex(h),latex(g),latex(h),latex(nn*ln)),
                    ]
                da= random.choice(du)
                s = ['$\\underset{[%s;%s]}{\\mathop{\\min y}}\\,=%s$'%(latex(g),latex(h),latex(ln)),
                    '$\\underset{[%s;%s]}{\\mathop{\\max y}}\\,=%s$'%(latex(g),latex(h),latex(nn)),
                    '$\\underset{[%s;%s]}{\\mathop{\\max y}}\\,+\\underset{[%s;%s]}{\\mathop{\\min y}}\\,=%s$'%(latex(g),latex(h),latex(g),latex(h),latex(ln-nn)),
                    '$\\underset{[%s;%s]}{\\mathop{\\max y}}\\,-\\underset{[%s;%s]}{\\mathop{\\min y}}\\,=%s$'%(latex(g),latex(h),latex(g),latex(h),latex(nn-ln)),
                    '$\\underset{[%s;%s]}{\\mathop{\\max y}}\\,\\cdot\\underset{[%s;%s]}{\\mathop{\\min y}}\\,=%s$'%(latex(g),latex(h),latex(g),latex(h),latex(nn*ln+1)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = '''Cho hàm số $y=%sx^4+%sx^2+%s$. Mệnh đề nào dưới đây đúng? '''%(latex(A),latex(B),latex(C))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=( '''$y'= %sx^3+%s x.\\\\ \n'''
                        '''y'=0 \\Leftrightarrow \\hoac{& x=0 \\notin\\left( %s;%s\\right) \\\\& x=%s \\notin\\left( %s;%s\\right) \\\\& x=%s \\in\\left( %s;%s\\right).}$\\\\ \n'''
                        '''Ta có: ${y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm} {y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm} {y}{\\left(%s\\right)}=%s.$\\\\ \n'''
                        '''Vậy\\\\ \n'''
                        '''\\hspace*{1cm}$\\underset{[%s;%s]}{\\mathop{\\max y}}\\,=%s$;\\\\ \n'''
                        '''\\hspace*{1cm}$\\underset{[%s;%s]}{\\mathop{\\min y}}\\,=%s$;\\\\ \n'''
                        '''\\hspace*{1cm}$\\underset{[%s;%s]}{\\mathop{\\max y}}\\,+\\underset{[%s;%s]}{\\mathop{\\min y}}\\,=\\left(%s\\right)+\\left(%s\\right)=%s$;\\\\ \n'''
                        '''\\hspace*{1cm}$\\underset{[%s;%s]}{\\mathop{\\max y}}\\,-\\underset{[%s;%s]}{\\mathop{\\min y}}\\,=\\left(%s\\right)-\\left(%s\\right)=%s$;\\\\ \n''' 
                        '''\\hspace*{1cm}$\\underset{[%s;%s]}{\\mathop{\\max y}}\\,\\cdot\\underset{[%s;%s]}{\\mathop{\\min y}}\\,=\\left(%s\\right)\\cdot\\left(%s\\right)=%s$.'''
                        %(latex(4*A),latex(2*B),
                        latex(g),latex(h),latex(x1),latex(g),latex(h),latex(x2),latex(g),latex(h),
                        latex(g),latex(m1),latex(h),latex(m2),latex(x2),latex(m5),
                        latex(g),latex(h),latex(ln),
                        latex(g),latex(h),latex(nn),
                        latex(g),latex(h),latex(g),latex(h),latex(ln),latex(nn),latex(ln+nn),
                        latex(g),latex(h),latex(g),latex(h),latex(ln),latex(nn),latex(ln-nn),
                        latex(g),latex(h),latex(g),latex(h),latex(ln),latex(nn),latex(ln*nn)))

            if dang=='24':
                # Khai báo biến
                a = randint(1,8)
                b = randint(1,9)
                c = randint(-15,15)
                g = randint(-4,8)
                h = randint(-3,9)
                x1= -sqrt(b)
                x2= sqrt (b)
                while a==0 or b==0 or x2>=h or g<=0 or g>=x2 or g>=h:
                    a = randint(1,8)
                    b = randint(1,9)
                    c = randint(-15,15)
                    g = randint(-4,8)
                    h = randint(-3,9)
                    x1= -sqrt(b)
                    x2= sqrt (b)
                A = Rational(a,4)
                B = Rational (a*b,-2)
                C = c
                m1=A*g**4+B*g**2+C
                m2=A*h**4+B*h**2+C
                m3=A*x1**4+B*x1**2+C
                m4=A*0**4+B*0**2+C
                m5=A*x2**4+B*x2**2+C
                listmm=(m1,m2,m5)
                ln=max(listmm)
                nn=min(listmm)
                du = ['$x=%s$'%(latex(x2)),
                    ]
                da= random.choice(du)
                s = ['$x=%s$'%(latex(x2+1)),
                '$x=%s$'%(latex(x2+2)),
                '$x=%s$'%(latex(x2+3)),
                '$x=%s$'%(latex(x2-1)),
                '$x=%s$'%(latex(x2-2)),
                '$x=%s$'%(latex(x2-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = '''Trên đoạn [%s;%s], hàm số $y=%sx^4+%sx^2+%s$ đạt giá trị nhỏ nhất tại điểm'''%(latex(g),latex(h),latex(A),latex(B),latex(C))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=( '''$y'= %sx^3+%s x.\\\\ \n'''
                        '''y'=0 \\Leftrightarrow \\hoac{& x=0 \\notin\\left( %s;%s\\right) \\\\& x=%s \\notin\\left( %s;%s\\right) \\\\& x=%s \\in\\left( %s;%s\\right).}$\\\\ \n'''
                        '''Ta có: ${y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm} {y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm} {y}{\\left(%s\\right)}=%s.$\\\\ \n'''
                        '''Vậy\\\\ \n'''
                        '''\\hspace*{1cm}$\\underset{[%s;%s]}{\\mathop{\\min y}}\\,=%s$ khi $x=%s$'''
                        %(latex(4*A),latex(2*B),
                        latex(g),latex(h),latex(x1),latex(g),latex(h),latex(x2),latex(g),latex(h),
                        latex(g),latex(m1),latex(h),latex(m2),latex(x2),latex(m5),
                        latex(g),latex(h),latex(nn),latex(x2)
            ))

            if dang=='25':
                # Khai báo biến
                a = randint(-8,-1)
                b = randint(1,9)
                c = randint(-15,15)
                g = randint(-4,8)
                h = randint(-3,9)
                x1= -sqrt(b)
                x2= sqrt (b)
                while a==0 or b==0 or x2>=h or g<=0 or g>=x2 or g>=h:
                    a = randint(-8,-1)
                    b = randint(1,9)
                    c = randint(-15,15)
                    g = randint(-4,8)
                    h = randint(-3,9)
                    x1= -sqrt(b)
                    x2= sqrt (b)
                A = Rational(a,4)
                B = Rational (a*b,-2)
                C = c
                m1=A*g**4+B*g**2+C
                m2=A*h**4+B*h**2+C
                m3=A*x1**4+B*x1**2+C
                m4=A*0**4+B*0**2+C
                m5=A*x2**4+B*x2**2+C
                listmm=(m1,m2,m5)
                ln=max(listmm)
                nn=min(listmm)
                du = ['$x=%s$'%(latex(x2)),
                    ]
                da= random.choice(du)
                s = ['$x=%s$'%(latex(x2+1)),
                '$x=%s$'%(latex(x2+2)),
                '$x=%s$'%(latex(x2+3)),
                '$x=%s$'%(latex(x2-1)),
                '$x=%s$'%(latex(x2-2)),
                '$x=%s$'%(latex(x2-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = '''Trên đoạn [%s;%s], hàm số $y=%sx^4+%sx^2+%s$ đạt giá trị lớn nhất tại điểm'''%(latex(g),latex(h),latex(A),latex(B),latex(C))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=( '''$y'= %sx^3+%s x.\\\\ \n'''
                        '''y'=0 \\Leftrightarrow \\hoac{& x=0 \\notin\\left( %s;%s\\right) \\\\& x=%s \\notin\\left( %s;%s\\right) \\\\& x=%s \\in\\left( %s;%s\\right).}$\\\\ \n'''
                        '''Ta có: ${y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm} {y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm} {y}{\\left(%s\\right)}=%s.$\\\\ \n'''
                        '''Vậy\\\\ \n'''
                        '''\\hspace*{1cm}$\\underset{[%s;%s]}{\\mathop{\\max y}}\\,=%s$ khi $x=%s$'''
                        %(latex(4*A),latex(2*B),
                        latex(g),latex(h),latex(x1),latex(g),latex(h),latex(x2),latex(g),latex(h),
                        latex(g),latex(m1),latex(h),latex(m2),latex(x2),latex(m5),
                        latex(g),latex(h),latex(ln),latex(x2)
            ))
            if dang=='10':
                # Khai báo biến
                x=symbols('x')
                i=randint(1,3)

                t1=randint(-10,-6)
                x1=randint(-5,-3)
                t2=randint(-2,-1)
                t3=randint(1,2)
                x2=-x1
                t4=x2+i  

                lisa=[t1,t2,t3,t4]    
                a=random.choice(lisa)
                b=random.choice(lisa)
                while a>=b:
                    a=random.choice(lisa)
                    b=random.choice(lisa) 

                m=randint(-9,9)
                hs_a=Rational(m,4)
                hs_b=-Rational(m*x1**2,2)
                hs_c=randint(-9,9)

                f=hs_a*x**4+hs_b*x**2+hs_c
                daoham=4*hs_a*x**3+2*hs_b*x
                fa=hs_a*a**4+hs_b*a**2+hs_c
                fb=hs_a*b**4+hs_b*b**2+hs_c
                f1=hs_a*x1**4+hs_b*x1**2+hs_c
                f2=hs_a*x2**4+hs_b*x2**2+hs_c
                f0=hs_c
                if a<x1<0<x2<b:
                    gtln=max(fa,fb,f1,f2,f0)
                    gtnn=min(fa,fb,f1,f2,f0)
                if a<x1<0<b<x2:
                    gtln=max(fa,fb,f1,f0)
                    gtnn=min(fa,fb,f1,f0)
                if a<x1<b<0<x2:
                    gtln=max(fa,fb,f1)
                    gtnn=min(fa,fb,f1)
                if x1<a<0<x2<b:
                    gtln=max(fa,fb,f2,f0)
                    gtnn=min(fa,fb,f2,f0)
                if x1<0<a<x2<b:
                    gtln=max(fa,fb,f2)
                    gtnn=min(fa,fb,f2)
                if x1<a<0<b<x2:
                    gtln=max(fa,fb,f0)
                    gtnn=min(fa,fb,f0) 

                du = ['$%s$'%(latex(gtln*gtnn)),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(gtln*gtnn+1)),
                '$%s$'%(latex(gtln*gtnn+2)),
                '$%s$'%(latex(gtln*gtnn+3)),
                '$%s$'%(latex(gtln*gtnn-1)),
                '$%s$'%(latex(gtln*gtnn-2)),
                '$%s$'%(latex(gtln*gtnn-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('''Cho hàm số $y=%s$. Tích giá trị lớn nhất và giá trị nhỏ nhấtcủa hàm số trên đoạn $[%s;%s]$ là'''
                                %(latex(f),latex(a),latex(b)
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
                loigiai=('Tập xác định: $\\mathscr{D}=\\mathbb{R}$.\\\\ \n'
                        '''Ta có $y'=%s.\\\\ \n''' 
                        '''\\hspace*{1.1cm}y'=0 \\Leftrightarrow \\hoac{& x=0 \\\\& x=%s \\\\& x=%s.}$.\\\\ \n'''
                        '''Bảng biến thiên\\\\ \n'''
                        '\\hspace*{3cm} \\begin{tikzpicture} \n'
                        '\\tkzTabInit[espcl=2.5,lgt=1.5] \n'
                        '{$x$/0.7,$y\'$/0.7,$y$/2.1} \n'
                        '{$-\\infty$,$%s$,0,$%s$,$+\\infty$} \n'
                        '\\tkzTabLine{,+,0,-,0,+,0,-} \n'
                        '\\tkzTabVar{-/$-\\infty$,+/$%s$,-/$%s$,+/$%s$,-/$-\\infty$}  \n'
                        '\\end{tikzpicture} \\\\ \n'

                        'Mặt khác $y(%s)=%s$ và $y(%s)=%s$.\\\\ \n'
                        '''\\hspace*{1cm} Hàm số có giá trị lớn nhất trên đoạn $[%s;%s]$ là $%s$. \\\\ \n'''
                        '''\\hspace*{1cm} Hàm số có giá trị nhỏ nhất trên đoạn $[%s;%s]$ là $%s$. '''
                        %(latex(daoham),
                        latex(x1),latex(x2),
                        latex(x1),latex(x2),
                        latex(f1),latex(f0),latex(f2),

                        latex(a),latex(fa), latex(b),latex(fb),
                        latex(a),latex(b), latex(gtln),
                        latex(a),latex(b), latex(gtnn),

                        ))
            if dang=='9':
                # Khai báo biến
                x=symbols('x')
                i=randint(1,3)

                t1=randint(-10,-6)
                x1=randint(-5,-3)
                t2=randint(-2,-1)
                t3=randint(1,2)
                x2=-x1
                t4=x2+i  

                lisa=[t1,t2,t3,t4]    
                a=random.choice(lisa)
                b=random.choice(lisa)
                while a>=b:
                    a=random.choice(lisa)
                    b=random.choice(lisa) 

                m=randint(-9,9)
                hs_a=Rational(m,4)
                hs_b=-Rational(m*x1**2,2)
                hs_c=randint(-9,9)

                f=hs_a*x**4+hs_b*x**2+hs_c
                daoham=4*hs_a*x**3+2*hs_b*x
                fa=hs_a*a**4+hs_b*a**2+hs_c
                fb=hs_a*b**4+hs_b*b**2+hs_c
                f1=hs_a*x1**4+hs_b*x1**2+hs_c
                f2=hs_a*x2**4+hs_b*x2**2+hs_c
                f0=hs_c
                if a<x1<0<x2<b:
                    gtln=max(fa,fb,f1,f2,f0)
                    gtnn=min(fa,fb,f1,f2,f0)
                if a<x1<0<b<x2:
                    gtln=max(fa,fb,f1,f0)
                    gtnn=min(fa,fb,f1,f0)
                if a<x1<b<0<x2:
                    gtln=max(fa,fb,f1)
                    gtnn=min(fa,fb,f1)
                if x1<a<0<x2<b:
                    gtln=max(fa,fb,f2,f0)
                    gtnn=min(fa,fb,f2,f0)
                if x1<0<a<x2<b:
                    gtln=max(fa,fb,f2)
                    gtnn=min(fa,fb,f2)
                if x1<a<0<b<x2:
                    gtln=max(fa,fb,f0)
                    gtnn=min(fa,fb,f0) 

                du = ['$%s$'%(latex(gtln-gtnn)),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(gtln-gtnn+1)),
                '$%s$'%(latex(gtln-gtnn+2)),
                '$%s$'%(latex(gtln-gtnn+3)),
                '$%s$'%(latex(gtln-gtnn-1)),
                '$%s$'%(latex(gtln-gtnn-2)),
                '$%s$'%(latex(gtln-gtnn-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('''Cho hàm số $y=%s$. Hiệu giá trị lớn nhất và giá trị nhỏ nhấtcủa hàm số trên đoạn $[%s;%s]$ là'''
                                %(latex(f),latex(a),latex(b)
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
                loigiai=('Tập xác định: $\\mathscr{D}=\\mathbb{R}$.\\\\ \n'
                        '''Ta có $y'=%s.\\\\ \n''' 
                        '''\\hspace*{1.1cm}y'=0 \\Leftrightarrow \\hoac{& x=0 \\\\& x=%s \\\\& x=%s.}$.\\\\ \n'''
                        '''Bảng biến thiên\\\\ \n'''
                        '\\hspace*{3cm} \\begin{tikzpicture} \n'
                        '\\tkzTabInit[espcl=2.5,lgt=1.5] \n'
                        '{$x$/0.7,$y\'$/0.7,$y$/2.1} \n'
                        '{$-\\infty$,$%s$,0,$%s$,$+\\infty$} \n'
                        '\\tkzTabLine{,+,0,-,0,+,0,-} \n'
                        '\\tkzTabVar{-/$-\\infty$,+/$%s$,-/$%s$,+/$%s$,-/$-\\infty$}  \n'
                        '\\end{tikzpicture} \\\\ \n'

                        'Mặt khác $y(%s)=%s$ và $y(%s)=%s$.\\\\ \n'
                        '''\\hspace*{1cm} Hàm số có giá trị lớn nhất trên đoạn $[%s;%s]$ là $%s$. \\\\ \n'''
                        '''\\hspace*{1cm} Hàm số có giá trị nhỏ nhất trên đoạn $[%s;%s]$ là $%s$. '''
                        %(latex(daoham),
                        latex(x1),latex(x2),
                        latex(x1),latex(x2),
                        latex(f1),latex(f0),latex(f2),

                        latex(a),latex(fa), latex(b),latex(fb),
                        latex(a),latex(b), latex(gtln),
                        latex(a),latex(b), latex(gtnn),

                        ))
            if dang=='8':
                # Khai báo biến
                x=symbols('x')
                i=randint(1,3)

                t1=randint(-10,-6)
                x1=randint(-5,-3)
                t2=randint(-2,-1)
                t3=randint(1,2)
                x2=-x1
                t4=x2+i  

                lisa=[t1,t2,t3,t4]    
                a=random.choice(lisa)
                b=random.choice(lisa)
                while a>=b:
                    a=random.choice(lisa)
                    b=random.choice(lisa) 

                m=randint(-9,9)
                hs_a=Rational(m,4)
                hs_b=-Rational(m*x1**2,2)
                hs_c=randint(-9,9)

                f=hs_a*x**4+hs_b*x**2+hs_c
                daoham=4*hs_a*x**3+2*hs_b*x
                fa=hs_a*a**4+hs_b*a**2+hs_c
                fb=hs_a*b**4+hs_b*b**2+hs_c
                f1=hs_a*x1**4+hs_b*x1**2+hs_c
                f2=hs_a*x2**4+hs_b*x2**2+hs_c
                f0=hs_c
                if a<x1<0<x2<b:
                    gtln=max(fa,fb,f1,f2,f0)
                    gtnn=min(fa,fb,f1,f2,f0)
                if a<x1<0<b<x2:
                    gtln=max(fa,fb,f1,f0)
                    gtnn=min(fa,fb,f1,f0)
                if a<x1<b<0<x2:
                    gtln=max(fa,fb,f1)
                    gtnn=min(fa,fb,f1)
                if x1<a<0<x2<b:
                    gtln=max(fa,fb,f2,f0)
                    gtnn=min(fa,fb,f2,f0)
                if x1<0<a<x2<b:
                    gtln=max(fa,fb,f2)
                    gtnn=min(fa,fb,f2)
                if x1<a<0<b<x2:
                    gtln=max(fa,fb,f0)
                    gtnn=min(fa,fb,f0) 

                du = ['$%s$'%(latex(gtln+gtnn)),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(gtln+gtnn+1)),
                '$%s$'%(latex(gtln+gtnn+2)),
                '$%s$'%(latex(gtln+gtnn+3)),
                '$%s$'%(latex(gtln+gtnn-1)),
                '$%s$'%(latex(gtln+gtnn-2)),
                '$%s$'%(latex(gtln+gtnn-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('''Cho hàm số $y=%s$. Tổng giá trị lớn nhất và giá trị nhỏ nhấtcủa hàm số trên đoạn $[%s;%s]$ là '''
                                %(latex(f),latex(a),latex(b)
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
                loigiai=('Tập xác định: $\\mathscr{D}=\\mathbb{R}$.\\\\ \n'
                        '''Ta có $y'=%s.\\\\ \n''' 
                        '''\\hspace*{1.1cm}y'=0 \\Leftrightarrow \\hoac{& x=0 \\\\& x=%s \\\\& x=%s.}$.\\\\ \n'''
                        '''Bảng biến thiên\\\\ \n'''
                        '\\hspace*{3cm} \\begin{tikzpicture} \n'
                        '\\tkzTabInit[espcl=2.5,lgt=1.5] \n'
                        '{$x$/0.7,$y\'$/0.7,$y$/2.1} \n'
                        '{$-\\infty$,$%s$,0,$%s$,$+\\infty$} \n'
                        '\\tkzTabLine{,+,0,-,0,+,0,-} \n'
                        '\\tkzTabVar{-/$-\\infty$,+/$%s$,-/$%s$,+/$%s$,-/$-\\infty$}  \n'
                        '\\end{tikzpicture} \\\\ \n'

                        'Mặt khác $y(%s)=%s$ và $y(%s)=%s$.\\\\ \n'
                        '''\\hspace*{1cm} Hàm số có giá trị lớn nhất trên đoạn $[%s;%s]$ là $%s$. \\\\ \n'''
                        '''\\hspace*{1cm} Hàm số có giá trị nhỏ nhất trên đoạn $[%s;%s]$ là $%s$. '''
                        %(latex(daoham),
                        latex(x1),latex(x2),
                        latex(x1),latex(x2),
                        latex(f1),latex(f0),latex(f2),

                        latex(a),latex(fa), latex(b),latex(fb),
                        latex(a),latex(b), latex(gtln),
                        latex(a),latex(b), latex(gtnn),

                        ))
            if dang=='7':
                # Khai báo biến
                x=symbols('x')
                i=randint(1,3)

                t1=randint(-10,-6)
                x1=randint(-5,-3)
                t2=randint(-2,-1)
                t3=randint(1,2)
                x2=-x1
                t4=x2+i  

                lisa=[t1,t2,t3,t4]    
                a=random.choice(lisa)
                b=random.choice(lisa)
                while a>=b:
                    a=random.choice(lisa)
                    b=random.choice(lisa) 

                m=randint(-9,9)
                hs_a=Rational(m,4)
                hs_b=-Rational(m*x1**2,2)
                hs_c=randint(-9,9)

                f=hs_a*x**4+hs_b*x**2+hs_c
                daoham=4*hs_a*x**3+2*hs_b*x
                fa=hs_a*a**4+hs_b*a**2+hs_c
                fb=hs_a*b**4+hs_b*b**2+hs_c
                f1=hs_a*x1**4+hs_b*x1**2+hs_c
                f2=hs_a*x2**4+hs_b*x2**2+hs_c
                f0=hs_c
                if a<x1<0<x2<b:
                    gtln=max(fa,fb,f1,f2,f0)
                    gtnn=min(fa,fb,f1,f2,f0)
                if a<x1<0<b<x2:
                    gtln=max(fa,fb,f1,f0)
                    gtnn=min(fa,fb,f1,f0)
                if a<x1<b<0<x2:
                    gtln=max(fa,fb,f1)
                    gtnn=min(fa,fb,f1)
                if x1<a<0<x2<b:
                    gtln=max(fa,fb,f2,f0)
                    gtnn=min(fa,fb,f2,f0)
                if x1<0<a<x2<b:
                    gtln=max(fa,fb,f2)
                    gtnn=min(fa,fb,f2)
                if x1<a<0<b<x2:
                    gtln=max(fa,fb,f0)
                    gtnn=min(fa,fb,f0) 

                du = ['$%s$'%(latex(gtnn)),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(gtnn+1)),
                '$%s$'%(latex(gtnn+2)),
                '$%s$'%(latex(gtnn+3)),
                '$%s$'%(latex(gtnn-1)),
                '$%s$'%(latex(gtnn-2)),
                '$%s$'%(latex(gtnn-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('''Cho hàm số $y=%s$. Giá trị nhỏ nhất của hàm số trên đoạn $[%s;%s]$ là '''
                                %(latex(f),latex(a),latex(b)
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
                loigiai=('Tập xác định: $\\mathscr{D}=\\mathbb{R}$.\\\\ \n'
                        '''Ta có $y'=%s.\\\\ \n''' 
                        '''\\hspace*{1.1cm}y'=0 \\Leftrightarrow \\hoac{& x=0 \\\\& x=%s \\\\& x=%s.}$.'''
                        '''Bảng biến thiên\\\\ \n'''
                        '\\hspace*{3cm} \\begin{tikzpicture} \n'
                        '\\tkzTabInit[espcl=2.5,lgt=1.5] \n'
                        '{$x$/0.7,$y\'$/0.7,$y$/2.1} \n'
                        '{$-\\infty$,$%s$,0,$%s$,$+\\infty$} \n'
                        '\\tkzTabLine{,+,0,-,0,+,0,-} \n'
                        '\\tkzTabVar{-/$-\\infty$,+/$%s$,-/$%s$,+/$%s$,-/$-\\infty$}  \n'
                        '\\end{tikzpicture} \\\\ \n'

                        'Mặt khác $y(%s)=%s$ và $y(%s)=%s$.\\\\ \n'
                        '''\\hspace*{1cm} Hàm số có giá trị lớn nhất trên đoạn $[%s;%s]$ là $%s$. \\\\ \n'''
                        '''\\hspace*{1cm} Hàm số có giá trị nhỏ nhất trên đoạn $[%s;%s]$ là $%s$. \\\\ \n'''
                        %(latex(daoham),
                        latex(x1),latex(x2),
                        latex(x1),latex(x2),
                        latex(f1),latex(f0),latex(f2),

                        latex(a),latex(fa), latex(b),latex(fb),
                        latex(a),latex(b), latex(gtln),
                        latex(a),latex(b), latex(gtnn),

                        ))
            if dang=='6':
                # Khai báo biến
                x=symbols('x')
                i=randint(1,3)

                t1=randint(-10,-6)
                x1=randint(-5,-3)
                t2=randint(-2,-1)
                t3=randint(1,2)
                x2=-x1
                t4=x2+i  

                lisa=[t1,t2,t3,t4]    
                a=random.choice(lisa)
                b=random.choice(lisa)
                while a>=b:
                    a=random.choice(lisa)
                    b=random.choice(lisa) 

                m=randint(-9,9)
                hs_a=Rational(m,4)
                hs_b=-Rational(m*x1**2,2)
                hs_c=randint(-9,9)

                f=hs_a*x**4+hs_b*x**2+hs_c
                daoham=4*hs_a*x**3+2*hs_b*x
                fa=hs_a*a**4+hs_b*a**2+hs_c
                fb=hs_a*b**4+hs_b*b**2+hs_c
                f1=hs_a*x1**4+hs_b*x1**2+hs_c
                f2=hs_a*x2**4+hs_b*x2**2+hs_c
                f0=hs_c
                if a<x1<0<x2<b:
                    gtln=max(fa,fb,f1,f2,f0)
                    gtnn=min(fa,fb,f1,f2,f0)
                if a<x1<0<b<x2:
                    gtln=max(fa,fb,f1,f0)
                    gtnn=min(fa,fb,f1,f0)
                if a<x1<b<0<x2:
                    gtln=max(fa,fb,f1)
                    gtnn=min(fa,fb,f1)
                if x1<a<0<x2<b:
                    gtln=max(fa,fb,f2,f0)
                    gtnn=min(fa,fb,f2,f0)
                if x1<0<a<x2<b:
                    gtln=max(fa,fb,f2)
                    gtnn=min(fa,fb,f2)
                if x1<a<0<b<x2:
                    gtln=max(fa,fb,f0)
                    gtnn=min(fa,fb,f0) 

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
                noidungcauhoi = ('''Cho hàm số $y=%s$. Giá trị lớn nhất của hàm số trên đoạn $[%s;%s]$ là '''
                                %(latex(f),latex(a),latex(b)
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
                loigiai=('Tập xác định: $\\mathscr{D}=\\mathbb{R}$.\\\\ \n'
                        '''Ta có $y'=%s.\\\\ \n''' 
                        '''\\hspace*{1.1cm}y'=0 \\Leftrightarrow \\hoac{& x=0 \\\\& x=%s \\\\& x=%s.}$.\\\\ \n'''
                        '''Bảng biến thiên\\\\ \n'''
                        '\\hspace*{3cm} \\begin{tikzpicture} \n'
                        '\\tkzTabInit[espcl=2.5,lgt=1.5] \n'
                        '{$x$/0.7,$y\'$/0.7,$y$/2.1} \n'
                        '{$-\\infty$,$%s$,0,$%s$,$+\\infty$} \n'
                        '\\tkzTabLine{,+,0,-,0,+,0,-} \n'
                        '\\tkzTabVar{-/$-\\infty$,+/$%s$,-/$%s$,+/$%s$,-/$-\\infty$}  \n'
                        '\\end{tikzpicture} \\\\ \n'

                        'Mặt khác $y(%s)=%s$ và $y(%s)=%s$.\\\\ \n'
                        '''\\hspace*{1cm} Hàm số có giá trị lớn nhất trên đoạn $[%s;%s]$ là $%s$. \\\\ \n'''
                        '''\\hspace*{1cm} Hàm số có giá trị nhỏ nhất trên đoạn $[%s;%s]$ là $%s$. '''
                        %(latex(daoham),
                        latex(x1),latex(x2),
                        latex(x1),latex(x2),
                        latex(f1),latex(f0),latex(f2),

                        latex(a),latex(fa), latex(b),latex(fb),
                        latex(a),latex(b), latex(gtln),
                        latex(a),latex(b), latex(gtnn),

                        ))
            if dang=='5':
                # Khai báo biến
                x=symbols('x')
                i=randint(1,3)

                t1=randint(-10,-6)
                x1=randint(-5,-3)
                t2=randint(-2,-1)
                t3=randint(1,2)
                x2=-x1
                t4=x2+i  

                lisa=[t1,t2,t3,t4]    
                a=random.choice(lisa)
                b=random.choice(lisa)
                while a>=b:
                    a=random.choice(lisa)
                    b=random.choice(lisa) 

                m=randint(1,9)
                hs_a=Rational(m,4)
                hs_b=-Rational(m*x1**2,2)
                hs_c=randint(-9,9)

                f=hs_a*x**4+hs_b*x**2+hs_c
                daoham=4*hs_a*x**3+2*hs_b*x
                fa=hs_a*a**4+hs_b*a**2+hs_c
                fb=hs_a*b**4+hs_b*b**2+hs_c
                f1=hs_a*x1**4+hs_b*x1**2+hs_c
                f2=hs_a*x2**4+hs_b*x2**2+hs_c
                f0=hs_c
                if a<x1<0<x2<b:
                    gtln=max(fa,fb,f1,f2,f0)
                    gtnn=min(fa,fb,f1,f2,f0)
                if a<x1<0<b<x2:
                    gtln=max(fa,fb,f1,f0)
                    gtnn=min(fa,fb,f1,f0)
                if a<x1<b<0<x2:
                    gtln=max(fa,fb,f1)
                    gtnn=min(fa,fb,f1)
                if x1<a<0<x2<b:
                    gtln=max(fa,fb,f2,f0)
                    gtnn=min(fa,fb,f2,f0)
                if x1<0<a<x2<b:
                    gtln=max(fa,fb,f2)
                    gtnn=min(fa,fb,f2)
                if x1<a<0<b<x2:
                    gtln=max(fa,fb,f0)
                    gtnn=min(fa,fb,f0) 

                du = ['$%s$'%(latex(gtln*gtnn)),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(gtln*gtnn+1)),
                '$%s$'%(latex(gtln*gtnn+2)),
                '$%s$'%(latex(gtln*gtnn+3)),
                '$%s$'%(latex(gtln*gtnn-1)),
                '$%s$'%(latex(gtln*gtnn-2)),
                '$%s$'%(latex(gtln*gtnn-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('''Cho hàm số $y=%s$. Tích giá trị lớn nhất và giá trị nhỏ nhất của hàm số trên đoạn $[%s;%s]$ là'''
                                %(latex(f),latex(a),latex(b)
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
                loigiai=('Tập xác định: $\\mathscr{D}=\\mathbb{R}$.\\\\ \n'
                        '''Ta có $y'=%s.\\\\ \n''' 
                        '''\\hspace*{1.1cm}y'=0 \\Leftrightarrow \\hoac{& x=0 \\\\& x=%s \\\\& x=%s.}$.\\\\ \n'''
                        '''Bảng biến thiên\\\\ \n'''
                        '\\hspace*{3cm} \\begin{tikzpicture} \n'
                        '\\tkzTabInit[espcl=2.5,lgt=1.5] \n'
                        '{$x$/0.7,$y\'$/0.7,$y$/2.1} \n'
                        '{$-\\infty$,$%s$,0,$%s$,$+\\infty$} \n'
                        '\\tkzTabLine{,-,0,+,0,-,0,+} \n'
                        '\\tkzTabVar{+/$+\\infty$,-/$%s$,+/$%s$,-/$%s$,+/$+\\infty$}  \n'
                        '\\end{tikzpicture} \\\\ \n'

                        'Mặt khác $y(%s)=%s$ và $y(%s)=%s$.\\\\ \n'
                        '''\\hspace*{1cm} Hàm số có giá trị lớn nhất trên đoạn $[%s;%s]$ là $%s$. \\\\ \n'''
                        '''\\hspace*{1cm} Hàm số có giá trị nhỏ nhất trên đoạn $[%s;%s]$ là $%s$. '''
                        %(latex(daoham),
                        latex(x1),latex(x2),
                        latex(x1),latex(x2),
                        latex(f1),latex(f0),latex(f2),

                        latex(a),latex(fa), latex(b),latex(fb),
                        latex(a),latex(b), latex(gtln),
                        latex(a),latex(b), latex(gtnn),

                        ))
            if dang=='4':
                # Khai báo biến
                x=symbols('x')
                i=randint(1,3)

                t1=randint(-10,-6)
                x1=randint(-5,-3)
                t2=randint(-2,-1)
                t3=randint(1,2)
                x2=-x1
                t4=x2+i  

                lisa=[t1,t2,t3,t4]    
                a=random.choice(lisa)
                b=random.choice(lisa)
                while a>=b:
                    a=random.choice(lisa)
                    b=random.choice(lisa) 

                m=randint(1,9)
                hs_a=Rational(m,4)
                hs_b=-Rational(m*x1**2,2)
                hs_c=randint(-9,9)

                f=hs_a*x**4+hs_b*x**2+hs_c
                daoham=4*hs_a*x**3+2*hs_b*x
                fa=hs_a*a**4+hs_b*a**2+hs_c
                fb=hs_a*b**4+hs_b*b**2+hs_c
                f1=hs_a*x1**4+hs_b*x1**2+hs_c
                f2=hs_a*x2**4+hs_b*x2**2+hs_c
                f0=hs_c
                if a<x1<0<x2<b:
                    gtln=max(fa,fb,f1,f2,f0)
                    gtnn=min(fa,fb,f1,f2,f0)
                if a<x1<0<b<x2:
                    gtln=max(fa,fb,f1,f0)
                    gtnn=min(fa,fb,f1,f0)
                if a<x1<b<0<x2:
                    gtln=max(fa,fb,f1)
                    gtnn=min(fa,fb,f1)
                if x1<a<0<x2<b:
                    gtln=max(fa,fb,f2,f0)
                    gtnn=min(fa,fb,f2,f0)
                if x1<0<a<x2<b:
                    gtln=max(fa,fb,f2)
                    gtnn=min(fa,fb,f2)
                if x1<a<0<b<x2:
                    gtln=max(fa,fb,f0)
                    gtnn=min(fa,fb,f0) 

                du = ['$%s$'%(latex(gtln-gtnn)),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(gtln-gtnn+1)),
                    '$%s$'%(latex(gtln-gtnn-1)),
                    '$%s$'%(latex(gtln-gtnn+2)),
                    '$%s$'%(latex(gtln-gtnn-2)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('''Cho hàm số $y=%s$. Hiệu giá trị lớn nhất và giá trị nhỏ nhất của hàm số trên đoạn $[%s;%s]$ là '''
                                %(latex(f),latex(a),latex(b)
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
                loigiai=('Tập xác định: $\\mathscr{D}=\\mathbb{R}$.\\\\ \n'
                        '''Ta có $y'=%s.\\\\ \n''' 
                        '''\\hspace*{1.1cm}y'=0 \\Leftrightarrow \\hoac{& x=0 \\\\& x=%s \\\\& x=%s.}$.\\\\ \n'''
                        '''Bảng biến thiên\\\\ \n'''
                        '\\hspace*{3cm} \\begin{tikzpicture} \n'
                        '\\tkzTabInit[espcl=2.5,lgt=1.5] \n'
                        '{$x$/0.7,$y\'$/0.7,$y$/2.1} \n'
                        '{$-\\infty$,$%s$,0,$%s$,$+\\infty$} \n'
                        '\\tkzTabLine{,-,0,+,0,-,0,+} \n'
                        '\\tkzTabVar{+/$+\\infty$,-/$%s$,+/$%s$,-/$%s$,+/$+\\infty$}  \n'
                        '\\end{tikzpicture} \\\\ \n'
                        'Mặt khác $y(%s)=%s$ và $y(%s)=%s$.\\\\ \n'
                        '''\\hspace*{1cm} Hàm số có giá trị lớn nhất trên đoạn $[%s;%s]$ là $%s$. \\\\ \n'''
                        '''\\hspace*{1cm} Hàm số có giá trị nhỏ nhất trên đoạn $[%s;%s]$ là $%s$. '''
                        %(latex(daoham),
                        latex(x1),latex(x2),
                        latex(x1),latex(x2),
                        latex(f1),latex(f0),latex(f2),

                        latex(a),latex(fa), latex(b),latex(fb),
                        latex(a),latex(b), latex(gtln),
                        latex(a),latex(b), latex(gtnn),

                        ))

            if dang=='3':
                # Khai báo biến
                x=symbols('x')
                i=randint(1,3)

                t1=randint(-10,-6)
                x1=randint(-5,-3)
                t2=randint(-2,-1)
                t3=randint(1,2)
                x2=-x1
                t4=x2+i  

                lisa=[t1,t2,t3,t4]    
                a=random.choice(lisa)
                b=random.choice(lisa)
                while a>=b:
                    a=random.choice(lisa)
                    b=random.choice(lisa) 

                m=randint(1,9)
                hs_a=Rational(m,4)
                hs_b=-Rational(m*x1**2,2)
                hs_c=randint(-9,9)

                f=hs_a*x**4+hs_b*x**2+hs_c
                daoham=4*hs_a*x**3+2*hs_b*x
                fa=hs_a*a**4+hs_b*a**2+hs_c
                fb=hs_a*b**4+hs_b*b**2+hs_c
                f1=hs_a*x1**4+hs_b*x1**2+hs_c
                f2=hs_a*x2**4+hs_b*x2**2+hs_c
                f0=hs_c
                if a<x1<0<x2<b:
                    gtln=max(fa,fb,f1,f2,f0)
                    gtnn=min(fa,fb,f1,f2,f0)
                if a<x1<0<b<x2:
                    gtln=max(fa,fb,f1,f0)
                    gtnn=min(fa,fb,f1,f0)
                if a<x1<b<0<x2:
                    gtln=max(fa,fb,f1)
                    gtnn=min(fa,fb,f1)
                if x1<a<0<x2<b:
                    gtln=max(fa,fb,f2,f0)
                    gtnn=min(fa,fb,f2,f0)
                if x1<0<a<x2<b:
                    gtln=max(fa,fb,f2)
                    gtnn=min(fa,fb,f2)
                if x1<a<0<b<x2:
                    gtln=max(fa,fb,f0)
                    gtnn=min(fa,fb,f0) 

                du = ['$%s$'%(latex(gtln+gtnn)),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(gtln+gtnn+1)),
                '$%s$'%(latex(gtln+gtnn+2)),
                '$%s$'%(latex(gtln+gtnn+3)),
                '$%s$'%(latex(gtln+gtnn-1)),
                '$%s$'%(latex(gtln+gtnn-2)),
                '$%s$'%(latex(gtln+gtnn-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('''Cho hàm số $y=%s$. Tổng giá trị lớn nhất và giá trị nhỏ nhất của hàm số trên đoạn $[%s;%s]$ là'''
                                %(latex(f),latex(a),latex(b)
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
                loigiai=('Tập xác định: $\\mathscr{D}=\\mathbb{R}$.\\\\ \n'
                        '''Ta có $y'=%s.\\\\ \n''' 
                        '''\\hspace*{1.1cm}y'=0 \\Leftrightarrow \\hoac{& x=0 \\\\& x=%s \\\\& x=%s.}$.\\\\ \n'''
                        '''Bảng biến thiên\\\\ \n'''
                        '\\hspace*{3cm} \\begin{tikzpicture} \n'
                        '\\tkzTabInit[espcl=2.5,lgt=1.5] \n'
                        '{$x$/0.7,$y\'$/0.7,$y$/2.1} \n'
                        '{$-\\infty$,$%s$,0,$%s$,$+\\infty$} \n'
                        '\\tkzTabLine{,-,0,+,0,-,0,+} \n'
                        '\\tkzTabVar{+/$+\\infty$,-/$%s$,+/$%s$,-/$%s$,+/$+\\infty$}  \n'
                        '\\end{tikzpicture} \\\\ \n'
                        'Mặt khác $y(%s)=%s$ và $y(%s)=%s$.\\\\ \n'
                        '''\\hspace*{1cm} Hàm số có giá trị lớn nhất trên đoạn $[%s;%s]$ là $%s$. \\\\ \n'''
                        '''\\hspace*{1cm} Hàm số có giá trị nhỏ nhất trên đoạn $[%s;%s]$ là $%s$. '''
                        %(latex(daoham),
                        latex(x1),latex(x2),
                        latex(x1),latex(x2),
                        latex(f1),latex(f0),latex(f2),

                        latex(a),latex(fa), latex(b),latex(fb),
                        latex(a),latex(b), latex(gtln),
                        latex(a),latex(b), latex(gtnn),

                        ))

            if dang=='2':
                # Khai báo biến
                x=symbols('x')
                i=randint(1,3)

                t1=randint(-10,-6)
                x1=randint(-5,-3)
                t2=randint(-2,-1)
                t3=randint(1,2)
                x2=-x1
                t4=x2+i  

                lisa=[t1,t2,t3,t4]    
                a=random.choice(lisa)
                b=random.choice(lisa)
                while a>=b:
                    a=random.choice(lisa)
                    b=random.choice(lisa) 

                m=randint(1,9)
                hs_a=Rational(m,4)
                hs_b=-Rational(m*x1**2,2)
                hs_c=randint(-9,9)

                f=hs_a*x**4+hs_b*x**2+hs_c
                daoham=4*hs_a*x**3+2*hs_b*x
                fa=hs_a*a**4+hs_b*a**2+hs_c
                fb=hs_a*b**4+hs_b*b**2+hs_c
                f1=hs_a*x1**4+hs_b*x1**2+hs_c
                f2=hs_a*x2**4+hs_b*x2**2+hs_c
                f0=hs_c
                if a<x1<0<x2<b:
                    gtln=max(fa,fb,f1,f2,f0)
                    gtnn=min(fa,fb,f1,f2,f0)
                if a<x1<0<b<x2:
                    gtln=max(fa,fb,f1,f0)
                    gtnn=min(fa,fb,f1,f0)
                if a<x1<b<0<x2:
                    gtln=max(fa,fb,f1)
                    gtnn=min(fa,fb,f1)
                if x1<a<0<x2<b:
                    gtln=max(fa,fb,f2,f0)
                    gtnn=min(fa,fb,f2,f0)
                if x1<0<a<x2<b:
                    gtln=max(fa,fb,f2)
                    gtnn=min(fa,fb,f2)
                if x1<a<0<b<x2:
                    gtln=max(fa,fb,f0)
                    gtnn=min(fa,fb,f0) 

                du = ['$%s$'%(latex(gtnn)),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(gtnn+1)),
                '$%s$'%(latex(gtnn+2)),
                '$%s$'%(latex(gtnn+3)),
                '$%s$'%(latex(gtnn-1)),
                '$%s$'%(latex(gtnn-2)),
                '$%s$'%(latex(gtnn-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('''Cho hàm số $y=%s$. Giá trị nhỏ nhất của hàm số trên đoạn $[%s;%s]$ là'''
                                %(latex(f),latex(a),latex(b)
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
                loigiai=('Tập xác định: $\\mathscr{D}=\\mathbb{R}$.\\\\ \n'
                        '''Ta có $y'=%s.\\\\ \n''' 
                        '''\\hspace*{1.1cm}y'=0 \\Leftrightarrow \\hoac{& x=0 \\\\& x=%s \\\\& x=%s.}$.\\\\ \n'''
                        '''Bảng biến thiên\\\\ \n'''
                        '\\hspace*{3cm} \\begin{tikzpicture} \n'
                        '\\tkzTabInit[espcl=2.5,lgt=1.5] \n'
                        '{$x$/0.7,$y\'$/0.7,$y$/2.1} \n'
                        '{$-\\infty$,$%s$,0,$%s$,$+\\infty$} \n'
                        '\\tkzTabLine{,-,0,+,0,-,0,+} \n'
                        '\\tkzTabVar{+/$+\\infty$,-/$%s$,+/$%s$,-/$%s$,+/$+\\infty$}  \n'
                        '\\end{tikzpicture} \\\\ \n'

                        'Mặt khác $y(%s)=%s$ và $y(%s)=%s$.\\\\ \n'
                        '''\\hspace*{1cm} Hàm số có giá trị lớn nhất trên đoạn $[%s;%s]$ là $%s$. \\\\ \n'''
                        '''\\hspace*{1cm} Hàm số có giá trị nhỏ nhất trên đoạn $[%s;%s]$ là $%s$. '''
                        %(latex(daoham),
                        latex(x1),latex(x2),
                        latex(x1),latex(x2),
                        latex(f1),latex(f0),latex(f2),

                        latex(a),latex(fa), latex(b),latex(fb),
                        latex(a),latex(b), latex(gtln),
                        latex(a),latex(b), latex(gtnn),

                        ))
            if dang=='1':
                # Khai báo biến
                x=symbols('x')
                i=randint(1,3)

                t1=randint(-10,-6)
                x1=randint(-5,-3)
                t2=randint(-2,-1)
                t3=randint(1,2)
                x2=-x1
                t4=x2+i  

                lisa=[t1,t2,t3,t4]    
                a=random.choice(lisa)
                b=random.choice(lisa)
                while a>=b:
                    a=random.choice(lisa)
                    b=random.choice(lisa) 

                m=randint(1,9)
                hs_a=Rational(m,4)
                hs_b=-Rational(m*x1**2,2)
                hs_c=randint(-9,9)

                f=hs_a*x**4+hs_b*x**2+hs_c
                daoham=4*hs_a*x**3+2*hs_b*x
                fa=hs_a*a**4+hs_b*a**2+hs_c
                fb=hs_a*b**4+hs_b*b**2+hs_c
                f1=hs_a*x1**4+hs_b*x1**2+hs_c
                f2=hs_a*x2**4+hs_b*x2**2+hs_c
                f0=hs_c
                if a<x1<0<x2<b:
                    gtln=max(fa,fb,f1,f2,f0)
                    gtnn=min(fa,fb,f1,f2,f0)
                if a<x1<0<b<x2:
                    gtln=max(fa,fb,f1,f0)
                    gtnn=min(fa,fb,f1,f0)
                if a<x1<b<0<x2:
                    gtln=max(fa,fb,f1)
                    gtnn=min(fa,fb,f1)
                if x1<a<0<x2<b:
                    gtln=max(fa,fb,f2,f0)
                    gtnn=min(fa,fb,f2,f0)
                if x1<0<a<x2<b:
                    gtln=max(fa,fb,f2)
                    gtnn=min(fa,fb,f2)
                if x1<a<0<b<x2:
                    gtln=max(fa,fb,f0)
                    gtnn=min(fa,fb,f0) 

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
                noidungcauhoi = ('''Cho hàm số $y=%s$. Giá trị lớn nhất của hàm số trên đoạn $[%s;%s]$ là'''
                                %(latex(f),latex(a),latex(b)
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
                loigiai=('Tập xác định: $\\mathscr{D}=\\mathbb{R}$.\\\\ \n'
                        '''Ta có $y'=%s.\\\\ \n''' 
                        '''\\hspace*{1.1cm}y'=0 \\Leftrightarrow \\hoac{& x=0 \\\\& x=%s \\\\& x=%s.}$.\\\\ \n'''
                        '''Bảng biến thiên\\\\ \n'''
                        '\\hspace*{3cm} \\begin{tikzpicture} \n'
                        '\\tkzTabInit[espcl=2.5,lgt=1.5] \n'
                        '{$x$/0.7,$y\'$/0.7,$y$/2.1} \n'
                        '{$-\\infty$,$%s$,0,$%s$,$+\\infty$} \n'
                        '\\tkzTabLine{,-,0,+,0,-,0,+} \n'
                        '\\tkzTabVar{+/$+\\infty$,-/$%s$,+/$%s$,-/$%s$,+/$+\\infty$}  \n'
                        '\\end{tikzpicture} \\\\ \n'
                        'Mặt khác $y(%s)=%s$ và $y(%s)=%s$.\\\\ \n'
                        '''\\hspace*{1cm} Hàm số có giá trị lớn nhất trên đoạn $[%s;%s]$ là $%s$. \\\\ \n'''
                        '''\\hspace*{1cm} Hàm số có giá trị nhỏ nhất trên đoạn $[%s;%s]$ là $%s$. '''
                        %(latex(daoham),
                        latex(x1),latex(x2),
                        latex(x1),latex(x2),
                        latex(f1),latex(f0),latex(f2),

                        latex(a),latex(fa), latex(b),latex(fb),
                        latex(a),latex(b), latex(gtln),
                        latex(a),latex(b), latex(gtnn),               
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-').replace('+1x', 'x').replace('-1x', '-x').replace('+0x^2', '').replace('+0x', '').replace('+0', '')
            return content


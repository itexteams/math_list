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


def bt_dang16_p1_b2_c1_ds12(self):
            # Khai báo biến
            lisdang=['1','2','3','4','5','6','7','8']
            dang=random.choice(lisdang)
            if dang=='8':
                # Khai báo biến
                x = symbols('x')
                a=randint(-9,9)
                b=randint(-9,9)
                c=randint(-9,9)
                d=randint(-9,9)
                while a==0 or c==0 or a*d-b*c>=0:
                    a=randint(-9,9)
                    b=randint(-9,9)
                    c=randint(-9,9)
                    d=randint(-9,9)

                f=(a*x+b)/(c*x+d)
                daoham=(a*d-b*c)/(c*x+d)**2

                i=randint(1,5)
                j=randint(1,5)

                m=Rational(-d,c)+i
                n=m+j

                fm=(a*m+b)/(c*m+d)
                fn=(a*n+b)/(c*n+d)

                gtln=fm
                gtnn=fn

                du = ['$x=%s$'%(latex(n)),
                    ]
                da= random.choice(du)
                s = ['$x=%s$'%(latex(gtnn)),
                    '$x=%s$'%(latex(gtln)),
                    '$x=%s$'%(latex(m)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('''Cho hàm số $y=%s$. Hàm số đạt giá trị nhỏ nhất trên đoạn $\\left[ %s;%s \\right]$ tại điểm '''
                                %(latex(f),latex(m),latex(n)
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
                        'Tập xác định $\\mathscr{D}=\\mathbb{R}\\backslash \\left\\{%s\\right\\}$. \\\\ \n' #1
                        '$y\'=%s$. \\\\ \n' #2
                        '\\hspace*{1cm} Ta thấy $y\'<0 \\, \\forall x \\in \\mathscr{D} $ nên hàm số luôn nghịch biến. \\\\ \n' #3
                        'Ta có \\\\ \n'
                        '\\hspace*{1cm} $y\\left( %s \\right)=%s$ và $y\\left( %s \\right)=%s$. \\\\ \n' #3
                        'Vậy \\\\ \n' #3
                        '\\hspace*{1cm} $\\underset{\\left[ %s;%s \\right]}{\\mathop{\\max }}\\,y=%s$. \\\\ \n' #3
                        '\\hspace*{1cm} $\\underset{\\left[ %s;%s \\right]}{\\mathop{\\min }}\\,y=%s$. ' #3

                        %(latex(-Rational(d,c)), #1
                        latex(daoham),
                        latex(m),latex(fm),latex(n),latex(fn),
                        latex(m),latex(n),latex(fm),
                        latex(m),latex(n),latex(fn),
                        ))
            if dang=='7':
                # Khai báo biến
                x = symbols('x')
                a=randint(-9,9)
                b=randint(-9,9)
                c=randint(-9,9)
                d=randint(-9,9)
                while a==0 or c==0 or a*d-b*c>=0:
                    a=randint(-9,9)
                    b=randint(-9,9)
                    c=randint(-9,9)
                    d=randint(-9,9)

                f=(a*x+b)/(c*x+d)
                daoham=(a*d-b*c)/(c*x+d)**2

                i=randint(1,5)
                j=randint(1,5)

                m=Rational(-d,c)+i
                n=m+j

                fm=(a*m+b)/(c*m+d)
                fn=(a*n+b)/(c*n+d)

                gtln=fm
                gtnn=fn

                du = ['$x=%s$'%(latex(m)),
                    ]
                da= random.choice(du)
                s = ['$x=%s$'%(latex(gtnn)),
                    '$x=%s$'%(latex(gtln)),
                    '$x=%s$'%(latex(n)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('''Cho hàm số $y=%s$. Hàm số đạt giá trị lớn nhất trên đoạn $\\left[ %s;%s \\right]$ tại điểm '''
                                %(latex(f),latex(m),latex(n)
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
                        'Tập xác định $\\mathscr{D}=\\mathbb{R}\\backslash \\left\\{%s\\right\\}$. \\\\ \n' #1
                        '$y\'=%s$. \\\\ \n' #2
                        '\\hspace*{1cm} Ta thấy $y\'<0 \\, \\forall x \\in \\mathscr{D} $ nên hàm số luôn nghịch biến. \\\\ \n' #3
                        'Ta có \\\\ \n'
                        '\\hspace*{1cm} $y\\left( %s \\right)=%s$ và $y\\left( %s \\right)=%s$. \\\\ \n' #3
                        'Vậy \\\\ \n' #3
                        '\\hspace*{1cm} $\\underset{\\left[ %s;%s \\right]}{\\mathop{\\max }}\\,y=%s$. \\\\ \n' #3
                        '\\hspace*{1cm} $\\underset{\\left[ %s;%s \\right]}{\\mathop{\\min }}\\,y=%s$. ' #3

                        %(latex(-Rational(d,c)), #1
                        latex(daoham),
                        latex(m),latex(fm),latex(n),latex(fn),
                        latex(m),latex(n),latex(fm),
                        latex(m),latex(n),latex(fn),
                        ))
            if dang=='6':
                # Khai báo biến
                x = symbols('x')
                a=randint(-9,9)
                b=randint(-9,9)
                c=randint(-9,9)
                d=randint(-9,9)
                while a==0 or c==0 or a*d-b*c>=0:
                    a=randint(-9,9)
                    b=randint(-9,9)
                    c=randint(-9,9)
                    d=randint(-9,9)

                f=(a*x+b)/(c*x+d)
                daoham=(a*d-b*c)/(c*x+d)**2

                i=randint(1,5)
                j=randint(1,5)

                m=Rational(-d,c)+i
                n=m+j

                fm=(a*m+b)/(c*m+d)
                fn=(a*n+b)/(c*n+d)

                gtln=fm
                gtnn=fn

                du = ['$%s$'%(latex(gtnn)),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(gtln)),
                    '$%s$'%(latex(m)),
                    '$%s$'%(latex(n)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('''Cho hàm số $y=%s$. Giá trị nhỏ nhất của hàm số trên đoạn $\\left[ %s;%s \\right]$ là '''
                                %(latex(f),latex(m),latex(n)
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
                        'Tập xác định $\\mathscr{D}=\\mathbb{R}\\backslash \\left\\{%s\\right\\}$. \\\\ \n' #1
                        '$y\'=%s$. \\\\ \n' #2
                        '\\hspace*{1cm} Ta thấy $y\'<0 \\, \\forall x \\in \\mathscr{D} $ nên hàm số luôn nghịch biến. \\\\ \n' #3
                        'Ta có \\\\ \n'
                        '\\hspace*{1cm} $y\\left( %s \\right)=%s$ và $y\\left( %s \\right)=%s$. \\\\ \n' #3
                        'Vậy \\\\ \n' #3
                        '\\hspace*{1cm} $\\underset{\\left[ %s;%s \\right]}{\\mathop{\\max }}\\,y=%s$. \\\\ \n' #3
                        '\\hspace*{1cm} $\\underset{\\left[ %s;%s \\right]}{\\mathop{\\min }}\\,y=%s$. ' #3

                        %(latex(-Rational(d,c)), #1
                        latex(daoham),
                        latex(m),latex(fm),latex(n),latex(fn),
                        latex(m),latex(n),latex(fm),
                        latex(m),latex(n),latex(fn),
                        ))
            if dang=='5':
                # Khai báo biến
                x = symbols('x')
                a=randint(-9,9)
                b=randint(-9,9)
                c=randint(-9,9)
                d=randint(-9,9)
                while a==0 or c==0 or a*d-b*c>=0:
                    a=randint(-9,9)
                    b=randint(-9,9)
                    c=randint(-9,9)
                    d=randint(-9,9)

                f=(a*x+b)/(c*x+d)
                daoham=(a*d-b*c)/(c*x+d)**2

                i=randint(1,5)
                j=randint(1,5)

                m=Rational(-d,c)+i
                n=m+j

                fm=(a*m+b)/(c*m+d)
                fn=(a*n+b)/(c*n+d)

                gtln=fm
                gtnn=fn

                du = ['$%s$'%(latex(gtln)),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(gtnn)),
                    '$%s$'%(latex(m)),
                    '$%s$'%(latex(n)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('''Cho hàm số $y=%s$. Giá trị lớn nhất của hàm số trên đoạn $\\left[ %s;%s \\right]$ là '''
                                %(latex(f),latex(m),latex(n)
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
                        'Tập xác định $\\mathscr{D}=\\mathbb{R}\\backslash \\left\\{%s\\right\\}$. \\\\ \n' #1
                        '$y\'=%s$. \\\\ \n' #2
                        '\\hspace*{1cm} Ta thấy $y\'<0 \\, \\forall x \\in \\mathscr{D} $ nên hàm số luôn nghịch biến. \\\\ \n' #3
                        'Ta có \\\\ \n'
                        '\\hspace*{1cm} $y\\left( %s \\right)=%s$ và $y\\left( %s \\right)=%s$. \\\\ \n' #3
                        'Vậy \\\\ \n' #3
                        '\\hspace*{1cm} $\\underset{\\left[ %s;%s \\right]}{\\mathop{\\max }}\\,y=%s$. \\\\ \n' #3
                        '\\hspace*{1cm} $\\underset{\\left[ %s;%s \\right]}{\\mathop{\\min }}\\,y=%s$. ' #3

                        %(latex(-Rational(d,c)), #1
                        latex(daoham),
                        latex(m),latex(fm),latex(n),latex(fn),
                        latex(m),latex(n),latex(fm),
                        latex(m),latex(n),latex(fn),
                        ))
            if dang=='4':
                # Khai báo biến
                x = symbols('x')
                a=randint(-9,9)
                b=randint(-9,9)
                c=randint(-9,9)
                d=randint(-9,9)
                while a==0 or c==0 or a*d-b*c<=0:
                    a=randint(-9,9)
                    b=randint(-9,9)
                    c=randint(-9,9)
                    d=randint(-9,9)

                f=(a*x+b)/(c*x+d)
                daoham=(a*d-b*c)/(c*x+d)**2

                i=randint(1,5)
                j=randint(1,5)

                m=Rational(-d,c)+i
                n=m+j

                fm=(a*m+b)/(c*m+d)
                fn=(a*n+b)/(c*n+d)

                gtln=fn
                gtnn=fm

                du = ['$x=%s$'%(latex(m)),
                    ]
                da= random.choice(du)
                s = ['$x=%s$'%(latex(gtnn)),
                    '$x=%s$'%(latex(n)),
                    '$x=%s$'%(latex(gtln)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('''Cho hàm số $y=%s$. Hàm số đạt giá trị nhỏ nhất của hàm số trên đoạn $\\left[ %s;%s \\right]$ tại điểm'''
                                %(latex(f),latex(m),latex(n)
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
                        'Tập xác định $\\mathscr{D}=\\mathbb{R}\\backslash \\left\\{%s\\right\\}$. \\\\ \n' #1
                        '$y\'=%s$. \\\\ \n' #2
                        '\\hspace*{1cm} Ta thấy $y\'>0 \\, \\forall x \\in \\mathscr{D} $ nên hàm số luôn đồng biến. \\\\ \n' #3
                        'Ta có \\\\ \n'
                        '\\hspace*{1cm} $y\\left( %s \\right)=%s$ và $y\\left( %s \\right)=%s$. \\\\ \n' #3
                        'Vậy \\\\ \n' #3
                        '\\hspace*{1cm} $\\underset{\\left[ %s;%s \\right]}{\\mathop{\\max }}\\,y=%s$. \\\\ \n' #3
                        '\\hspace*{1cm} $\\underset{\\left[ %s;%s \\right]}{\\mathop{\\min }}\\,y=%s$. ' #3

                        %(latex(-Rational(d,c)), #1
                        latex(daoham),
                        latex(m),latex(fm),latex(n),latex(fn),
                        latex(m),latex(n),latex(fn),
                        latex(m),latex(n),latex(fm),
                        ))
            if dang=='3':
                # Khai báo biến
                x = symbols('x')
                a=randint(-9,9)
                b=randint(-9,9)
                c=randint(-9,9)
                d=randint(-9,9)
                while a==0 or c==0 or a*d-b*c<=0:
                    a=randint(-9,9)
                    b=randint(-9,9)
                    c=randint(-9,9)
                    d=randint(-9,9)

                f=(a*x+b)/(c*x+d)
                daoham=(a*d-b*c)/(c*x+d)**2

                i=randint(1,5)
                j=randint(1,5)

                m=Rational(-d,c)+i
                n=m+j

                fm=(a*m+b)/(c*m+d)
                fn=(a*n+b)/(c*n+d)

                gtln=fn
                gtnn=fm

                du = ['$x=%s$'%(latex(n)),
                    ]
                da= random.choice(du)
                s = ['$x=%s$'%(latex(gtnn)),
                    '$x=%s$'%(latex(m)),
                    '$x=%s$'%(latex(gtln)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('''Cho hàm số $y=%s$. Hàm số đạt giá trị lớn nhất của hàm số trên đoạn $\\left[ %s;%s \\right]$ tại điểm'''
                                %(latex(f),latex(m),latex(n)
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
                        'Tập xác định $\\mathscr{D}=\\mathbb{R}\\backslash \\left\\{%s\\right\\}$. \\\\ \n' #1
                        '$y\'=%s$. \\\\ \n' #2
                        '\\hspace*{1cm} Ta thấy $y\'>0 \\, \\forall x \\in \\mathscr{D} $ nên hàm số luôn đồng biến. \\\\ \n' #3
                        'Ta có \\\\ \n'
                        '\\hspace*{1cm} $y\\left( %s \\right)=%s$ và $y\\left( %s \\right)=%s$. \\\\ \n' #3
                        'Vậy \\\\ \n' #3
                        '\\hspace*{1cm} $\\underset{\\left[ %s;%s \\right]}{\\mathop{\\max }}\\,y=%s$. \\\\ \n' #3
                        '\\hspace*{1cm} $\\underset{\\left[ %s;%s \\right]}{\\mathop{\\min }}\\,y=%s$. ' #3

                        %(latex(-Rational(d,c)), #1
                        latex(daoham),
                        latex(m),latex(fm),latex(n),latex(fn),
                        latex(m),latex(n),latex(fn),
                        latex(m),latex(n),latex(fm),
                        ))

            if dang=='2':
                # Khai báo biến
                x = symbols('x')
                a=randint(-9,9)
                b=randint(-9,9)
                c=randint(-9,9)
                d=randint(-9,9)
                while a==0 or c==0 or a*d-b*c<=0:
                    a=randint(-9,9)
                    b=randint(-9,9)
                    c=randint(-9,9)
                    d=randint(-9,9)

                f=(a*x+b)/(c*x+d)
                daoham=(a*d-b*c)/(c*x+d)**2

                i=randint(1,5)
                j=randint(1,5)

                m=Rational(-d,c)+i
                n=m+j

                fm=(a*m+b)/(c*m+d)
                fn=(a*n+b)/(c*n+d)

                gtln=fn
                gtnn=fm

                du = ['$%s$'%(latex(gtnn)),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(gtln)),
                    '$%s$'%(latex(m)),
                    '$%s$'%(latex(n)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('''Cho hàm số $y=%s$. Giá trị nhỏ nhất của hàm số trên đoạn $\\left[ %s;%s \\right]$ là'''
                                %(latex(f),latex(m),latex(n)
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
                        'Tập xác định $\\mathscr{D}=\\mathbb{R}\\backslash \\left\\{%s\\right\\}$. \\\\ \n' #1
                        '$y\'=%s$. \\\\ \n' #2
                        '\\hspace*{1cm} Ta thấy $y\'>0 \\, \\forall x \\in \\mathscr{D} $ nên hàm số luôn đồng biến. \\\\ \n' #3
                        'Ta có \\\\ \n'
                        '\\hspace*{1cm} $y\\left( %s \\right)=%s$ và $y\\left( %s \\right)=%s$. \\\\ \n' #3
                        'Vậy \\\\ \n' #3
                        '\\hspace*{1cm} $\\underset{\\left[ %s;%s \\right]}{\\mathop{\\max }}\\,y=%s$. \\\\ \n' #3
                        '\\hspace*{1cm} $\\underset{\\left[ %s;%s \\right]}{\\mathop{\\min }}\\,y=%s$. ' #3

                        %(latex(-Rational(d,c)), #1
                        latex(daoham),
                        latex(m),latex(fm),latex(n),latex(fn),
                        latex(m),latex(n),latex(fn),
                        latex(m),latex(n),latex(fm),
                        ))

            if dang=='1':
                # Khai báo biến
                x = symbols('x')
                a=randint(-9,9)
                b=randint(-9,9)
                c=randint(-9,9)
                d=randint(-9,9)
                while a==0 or c==0 or a*d-b*c<=0:
                    a=randint(-9,9)
                    b=randint(-9,9)
                    c=randint(-9,9)
                    d=randint(-9,9)

                f=(a*x+b)/(c*x+d)
                daoham=(a*d-b*c)/(c*x+d)**2

                i=randint(1,5)
                j=randint(1,5)

                m=Rational(-d,c)+i
                n=m+j

                fm=(a*m+b)/(c*m+d)
                fn=(a*n+b)/(c*n+d)

                gtln=fn
                gtnn=fm

                du = ['$%s$'%(latex(gtln)),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(gtnn)),
                    '$%s$'%(latex(m)),
                    '$%s$'%(latex(n)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('''Cho hàm số $y=%s$. Giá trị lớn nhất của hàm số trên đoạn $\\left[ %s;%s \\right]$ là '''
                                %(latex(f),latex(m),latex(n)
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
                        'Tập xác định $\\mathscr{D}=\\mathbb{R}\\backslash \\left\\{%s\\right\\}$. \\\\ \n' #1
                        '$y\'=%s$. \\\\ \n' #2
                        '\\hspace*{1cm} Ta thấy $y\'>0 \\, \\forall x \\in \\mathscr{D} $ nên hàm số luôn đồng biến. \\\\ \n' #3
                        'Ta có \\\\ \n'
                        '\\hspace*{1cm} $y\\left( %s \\right)=%s$ và $y\\left( %s \\right)=%s$. \\\\ \n' #3
                        'Vậy \\\\ \n' #3
                        '\\hspace*{1cm} $\\underset{\\left[ %s;%s \\right]}{\\mathop{\\max }}\\,y=%s$. \\\\ \n' #3
                        '\\hspace*{1cm} $\\underset{\\left[ %s;%s \\right]}{\\mathop{\\min }}\\,y=%s$.' #3

                        %(latex(-Rational(d,c)), #1
                        latex(daoham),
                        latex(m),latex(fm),latex(n),latex(fn),
                        latex(m),latex(n),latex(fn),
                        latex(m),latex(n),latex(fm),
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-').replace('+1x', 'x').replace('-1x', '-x').replace('+0x^2', '').replace('+0x', '').replace('.0', '').replace('+0', '')
            return content


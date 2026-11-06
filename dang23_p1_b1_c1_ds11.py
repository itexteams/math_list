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


def bt_dang23_p1_b1_c1_ds11(self):
            #Khai báo biến
            a=random.choice([1/2,sqrt(2)/2,sqrt(3)/2]) # a là số bất kỳ từ 1 đến 25
            b= sqrt(1-a**2)
            u=randint(-9,9)
            v=randint(-9,9)
            k=randint(-9,9)
            t=randint(-9,9)
            while u==0 or v==0 or t==0 or k==0 or k+t*b**3==0:
                u=randint(-9,9)
                v=randint(-9,9)
                k=randint(-9,9)
                t=randint(-9,9)

            x1 = 1-a**2
            x2= (b**2-a**2)/(b**2)
            p1=(u*a+v*b)/(k+t*b**3)
            p10=(u*a+v*b)//(k+t*b**3)
            p2=(u*b+v*a)/(k+t*a**2)
            p20=(u*b+v*a)//(k+t*a**2)
            p3=(u*a-v*b)/(k+t*b**2)
            p30=(u*a-v*b)//(k+t*b**2)
            p4=(u*b-v*a)/(k+t*b**3)
            p40=(u*b-v*a)//(k+t*b**3)
            list1=['dang1','dang2','dang3','dang4']
            rd = random.choice(list1)
            #Nội ung câu hỏi
            if rd=='dang1':
                noidungcauhoi = ('''Cho $\\sin\\alpha=%s$, với $0 <\\alpha<\\dfrac{\\pi}{2} $.'''
                                ''' Giá trị của $P=\\dfrac{%s\\sin\\alpha+%s\\cos\\alpha}{%s+%s\\cos^3\\alpha}$ thuộc khoảng nào sau đây\n'''
                            %(latex(a),latex(u),latex(v),latex(k),latex(t)))
            # Các đáp án
                da_d = '\\True $\\left( %s;%s \\right)$'%(latex(p10-1),latex(p10+1))
                da_s1 = '$\\left( %s;%s \\right)$'%(latex(p10-3),latex(p10-2))
                da_s2 = '$\\left( %s;%s \\right)$'%(latex(p10+2),latex(p10+3))
                da_s3 = '$\\left( %s;%s \\right)$'%(latex(p10+4),latex(p10+5))
            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
            # Nội dung lời giải
                loigiai=('Ta có: $\\cos^2\\alpha=1-\\sin^2\\alpha\\Leftrightarrow \\cos^2\\alpha=1-\\left(%s\\right)^2=%s\\Leftrightarrow \\cos\\alpha=\\pm %s$.\\\\ \n'
                    'Vì $0 <\\alpha<\\dfrac{\\pi}{2} $ nên $\\cos\\alpha>0 \\Rightarrow \\cos\\alpha=%s$.\\\\ \n'
                    'Vậy $P=\\dfrac{%s\\sin\\alpha+%s\\cos\\alpha}{%s+%s\\cos^3\\alpha} \\\\ \n'
                    '=\\dfrac{%s\\left(%s\\right)+%s\\left(%s\\right)}{%s+%s\\left(%s\\right)^3}=%s\\in \\left( %s;%s \\right)$.\\\\ \n'
                    %(latex(a),latex(x1),latex(b),
                    latex(b),
                    latex(u),latex(v),latex(k),latex(t),
                    latex(u),latex(a),latex(v),latex(b),latex(k),latex(t),latex(b),latex(p1),latex(p10-1),latex(p10+1)))
            if rd=='dang2':
                noidungcauhoi = ('''Cho $\\cos\\alpha=%s$, với $0 <\\alpha<\\dfrac{\\pi}{2} $.'''
                                ''' Giá trị của $P=\\dfrac{%s\\sin\\alpha+%s\\cos\\alpha}{%s+%s\\sin^2\\alpha}$ thuộc khoảng nào sau đây\n'''
                            %(latex(a),latex(u),latex(v),latex(k),latex(t)))
            # Các đáp án
                da_d = '\\True $\\left( %s;%s \\right)$'%(latex(p20-1),latex(p20+1))
                da_s1 = '$\\left( %s;%s \\right)$'%(latex(p20-3),latex(p20-2))
                da_s2 = '$\\left( %s;%s \\right)$'%(latex(p20+2),latex(p20+3))
                da_s3 = '$\\left( %s;%s \\right)$'%(latex(p20+4),latex(p20+5))
            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
            # Nội dung lời giải
                loigiai=('Ta có: $\\sin^2\\alpha=1-\\cos^2\\alpha\\Leftrightarrow \\sin^2\\alpha=1-\\left(%s\\right)^2=%s\\Leftrightarrow \\sin\\alpha=\\pm %s$.\\\\ \n'
                    'Vì $0 <\\alpha<\\dfrac{\\pi}{2} $ nên $\\sin\\alpha>0 \\Rightarrow \\sin\\alpha=%s$.\\\\ \n'
                    'Vậy $P=\\dfrac{%s\\sin\\alpha+%s\\cos\\alpha}{%s+%s\\cos^2\\alpha} \\\\ \n'
                    '=\\dfrac{%s\\left(%s\\right)+%s\\left(%s\\right)}{%s+%s\\left(%s\\right)^2}=%s\\in \\left( %s;%s \\right)$.\\\\ \n'
                    %(latex(a),latex(x1),latex(b),
                    latex(b),
                    latex(u),latex(v),latex(k),latex(t),
                    latex(u),latex(b),latex(v),latex(a),latex(k),latex(t),latex(b),latex(p2),latex(p20-1),latex(p20+1)))
            if rd=='dang3':
                noidungcauhoi = ('''Cho $\\sin\\alpha=%s$, với $\\dfrac{\\pi}{2} <\\alpha<\\pi $.'''
                                ''' Giá trị của $P=\\dfrac{%s\\sin\\alpha+%s\\cos\\alpha}{%s\\cos^2\\alpha+%s}$ thuộc khoảng nào sau đây\n'''
                            %(latex(a),latex(u),latex(v),latex(t),latex(k)))
            # Các đáp án
                da_d = '\\True $\\left( %s;%s \\right)$'%(latex(p30-1),latex(p30+1))
                da_s1 = '$\\left( %s;%s \\right)$'%(latex(p30-3),latex(p30-2))
                da_s2 = '$\\left( %s;%s \\right)$'%(latex(p30+2),latex(p30+3))
                da_s3 = '$\\left( %s;%s \\right)$'%(latex(p30-5),latex(p30-4))
            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
            # Nội dung lời giải
                loigiai=('Ta có: $\\cos^2\\alpha=1-\\sin^2\\alpha\\Leftrightarrow \\cos^2\\alpha=1-\\left(%s\\right)^2=%s\\Leftrightarrow \\cos\\alpha=\\pm %s$.\\\\ \n'
                    'Vì $\\dfrac{\\pi}{2} <\\alpha<\\pi $ nên $\\cos\\alpha<0 \\Rightarrow \\cos\\alpha=-%s$.\\\\ \n'
                    'Vậy $P=\\dfrac{%s\\sin\\alpha+%s\\cos\\alpha}{%s\\cos^2\\alpha+%s} \\\\ \n'
                    '=\\dfrac{%s\\left(%s\\right)+%s\\left(-%s\\right)}{%s\\left(-%s\\right)^2+%s}=%s\\in \\left( %s;%s \\right)$.\\\\ \n'
                    %(latex(a),latex(x1),latex(b),
                    latex(b),
                    latex(u),latex(v),latex(t),latex(k),
                    latex(u),latex(a),latex(v),latex(b),latex(t),latex(b),latex(k),latex(p3),latex(p30-1),latex(p30+1)))
            if rd=='dang4':
                noidungcauhoi = ('''Cho $\\cos\\alpha=-%s$, với $\\dfrac{\\pi}{2} <\\alpha<\\pi $.'''
                                ''' Giá trị của $P=\\dfrac{%s\\sin\\alpha+%s\\cos\\alpha}{%s\\sin^3\\alpha+%s}$ thuộc khoảng nào sau đây\n'''
                            %(latex(a),latex(u),latex(v),latex(t),latex(k)))
            # Các đáp án
                da_d = '\\True $\\left( %s;%s \\right)$'%(latex(p40-1),latex(p40+1))
                da_s1 = '$\\left( %s;%s \\right)$'%(latex(p40-3),latex(p40-2))
                da_s2 = '$\\left( %s;%s \\right)$'%(latex(p40+2),latex(p40+3))
                da_s3 = '$\\left( %s;%s \\right)$'%(latex(p40-5),latex(p40-4))
            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
            # Nội dung lời giải
                loigiai=('Ta có: $\\sin^2\\alpha=1-\\cos^2\\alpha\\Leftrightarrow \\sin^2\\alpha=1-\\left(-%s\\right)^2=%s\\Leftrightarrow \\sin\\alpha=\\pm %s$.\\\\ \n'
                    'Vì $\\dfrac{\\pi}{2} <\\alpha<\\pi $ nên $\\sin\\alpha>0 \\Rightarrow \\sin\\alpha=%s$.\\\\ \n'
                    'Vậy $P=\\dfrac{%s\\sin\\alpha+%s\\cos\\alpha}{%s\\sin^3\\alpha+%s} \\\\ \n'
                    '=\\dfrac{%s\\left(%s\\right)+%s\\left(-%s\\right)}{%s\\left(%s\\right)^3+%s}=%s\\in \\left( %s;%s \\right)$.\\\\ \n'
                    %(latex(a),latex(x1),latex(b),
                    latex(b),
                    latex(u),latex(v),latex(t),latex(k),
                    latex(u),latex(b),latex(v),latex(a),latex(t),latex(b),latex(k),latex(p4),latex(p40-1),latex(p40+1)))
            # Xuất câu hỏi
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n {'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n }'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n') .replace('--','').replace('\\frac','\\dfrac').replace('+-','-').replace('++','+').replace('1\\cos','\\cos').replace('1\\sin','\\sin').replace('-1\\cos','-\\cos').replace('-1\\sin','-\\sin')   
            return content


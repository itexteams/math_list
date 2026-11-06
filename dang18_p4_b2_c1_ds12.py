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


def bt_dang18_p4_b2_c1_ds12(self):
            # Khai báo biến
            lisdang=['1','2','3']
            dang=random.choice(lisdang)
            if dang=='1':
                a = 1
                b = randint(-5,-1)
                c = randint(-6,6)
                d = randint(4,8)
                e = randint(-20,20)
                g = randint(-5,5)
                h = randint(-4,10)
                i= Rational(d,c)
                while a==0 or c==0 or b>=i or h<=i or g>=b:
                    a = 1
                    b = randint(-5,-1)
                    c = randint(-6,6)
                    d = randint(4,8)
                    e = randint(-20,20)
                    g = randint(-5,5)
                    h = randint(-4,10)
                    i= Rational(d,c)
                A = Rational(a*c,3)
                B = Rational (a*d+b*c,-2)
                C = b*d
                D = e
                m1=A*g**3+B*g**2+C*g+D
                m2=A*h**3+B*h**2+C*h+D
                m3=A*i**3+B*i**2+C*i+D
                m4=A*b**3+B*b**2+C*b+D
                listmm=(m1,m2,m3,m4)
                ln=max(listmm)
                nn=min(listmm)
                while ln+nn>=99 or ln+nn<=-9.9 or (ln+nn)%1==0:
                    a = 1
                    b = randint(-5,-1)
                    c = randint(-6,6)
                    d = randint(4,8)
                    e = randint(-20,20)
                    g = randint(-5,5)
                    h = randint(-4,10)
                    i= Rational(d,c)
                    while a==0 or c==0 or b>=i or h<=i or g>=b:
                        a = 1
                        b = randint(-5,-1)
                        c = randint(-6,6)
                        d = randint(4,8)
                        e = randint(-20,20)
                        g = randint(-5,5)
                        h = randint(-4,10)
                        i= Rational(d,c)
                    A = Rational(a*c,3)
                    B = Rational (a*d+b*c,-2)
                    C = b*d
                    D = e
                    m1=A*g**3+B*g**2+C*g+D
                    m2=A*h**3+B*h**2+C*h+D
                    m3=A*i**3+B*i**2+C*i+D
                    m4=A*b**3+B*b**2+C*b+D
                    listmm=(m1,m2,m3,m4)
                    ln=max(listmm)
                    nn=min(listmm)
                x0=ln+nn
                number = Decimal(float(x0))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                # Nội dung câu hỏi
                noidungcauhoi = ('Tính tổng giá trị lớn nhất và giá trị nhỏ nhất của hàm số $y=%sx^3+%sx^2+%sx+%s$ trên đoạn $[%s;%s]$ (Kết quả làm tròn đến hàng phần chục)$zz$'
                            %(latex(A),latex(B),latex(C),latex(D),latex(g),latex(h))
                                )

                # Nội dung lời giải
                loigiai = ( '''$y'=%sx^2+%sx+%s$zz$\\\\ \n'''
                        '''y'=0 \\Leftrightarrow \\hoac{& x=%s \\in\\left( %s;%s\\right) \\\\& x=%s \\in\\left( %s;%s\\right)}$\\\\ \n'''
                        '''Ta có: ${y}{\\left(%s\\right)}=%s;\\hspace*{0.5cm} {y}{\\left(%s\\right)}=%s;\\hspace*{0.5cm} {y}{\\left(%s\\right)}=%s;\\hspace*{0.5cm} {y}{\\left(%s\\right)}=%s$$zz$\\\\ \n'''
                        '''Vậy $\\underset{[%s;%s]}{\\mathop{\\max y}}\\,+\\underset{[%s;%s]}{\\mathop{\\min y}}\\,=%s+\\left(%s\\right)=%s\\approx %s$$zz$'''
                        %(latex(3*A),latex(2*B),latex(C),
                        latex(b),latex(g),latex(h),latex(i),latex(g),latex(h),
                        latex(g),latex(m1),latex(h),latex(m2),latex(b),latex(m4),latex(i),latex(m3),
                        latex(g),latex(h),latex(g),latex(h),latex(ln),latex(nn),latex(ln+nn),latex(kq)))

                #Đáp án


            if dang=='2':
                a = 1
                b = randint(-5,-1)
                c = randint(-6,6)
                d = randint(4,8)
                e = randint(-20,20)
                g = randint(-5,5)
                h = randint(-4,10)
                i= Rational(d,c)
                while a==0 or c==0 or b>=i or h<=i or g>=b:
                    a = 1
                    b = randint(-5,-1)
                    c = randint(-6,6)
                    d = randint(4,8)
                    e = randint(-20,20)
                    g = randint(-5,5)
                    h = randint(-4,10)
                    i= Rational(d,c)
                A = Rational(a*c,3)
                B = Rational (a*d+b*c,-2)
                C = b*d
                D = e
                m1=A*g**3+B*g**2+C*g+D
                m2=A*h**3+B*h**2+C*h+D
                m3=A*i**3+B*i**2+C*i+D
                m4=A*b**3+B*b**2+C*b+D
                listmm=(m1,m2,m3,m4)
                ln=max(listmm)
                nn=min(listmm)
                while ln-nn>=99 or ln-nn<=-9.9 or (ln-nn)%1==0:
                    a = 1
                    b = randint(-5,-1)
                    c = randint(-6,6)
                    d = randint(4,8)
                    e = randint(-20,20)
                    g = randint(-5,5)
                    h = randint(-4,10)
                    i= Rational(d,c)
                    while a==0 or c==0 or b>=i or h<=i or g>=b:
                        a = 1
                        b = randint(-5,-1)
                        c = randint(-6,6)
                        d = randint(4,8)
                        e = randint(-20,20)
                        g = randint(-5,5)
                        h = randint(-4,10)
                        i= Rational(d,c)
                    A = Rational(a*c,3)
                    B = Rational (a*d+b*c,-2)
                    C = b*d
                    D = e
                    m1=A*g**3+B*g**2+C*g+D
                    m2=A*h**3+B*h**2+C*h+D
                    m3=A*i**3+B*i**2+C*i+D
                    m4=A*b**3+B*b**2+C*b+D
                    listmm=(m1,m2,m3,m4)
                    ln=max(listmm)
                    nn=min(listmm)
                x0=ln-nn
                number = Decimal(float(x0))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                # Nội dung câu hỏi
                noidungcauhoi = ('Tính hiệu giá trị lớn nhất và giá trị nhỏ nhất của hàm số $y=%sx^3+%sx^2+%sx+%s$ trên đoạn $[%s;%s]$ (Kết quả làm tròn đến hàng phần chục)$zz$'
                            %(latex(A),latex(B),latex(C),latex(D),latex(g),latex(h))
                                )

                # Nội dung lời giải
                loigiai = ( '''$y'=%sx^2+%sx+%s$zz$\\\\ \n'''
                        '''y'=0 \\Leftrightarrow \\hoac{& x=%s \\in\\left( %s;%s\\right) \\\\& x=%s \\in\\left( %s;%s\\right)}$\\\\ \n'''
                        '''Ta có: ${y}{\\left(%s\\right)}=%s;\\hspace*{0.5cm} {y}{\\left(%s\\right)}=%s;\\hspace*{0.5cm} {y}{\\left(%s\\right)}=%s;\\hspace*{0.5cm} {y}{\\left(%s\\right)}=%s$$zz$\\\\ \n'''
                        '''Vậy $\\underset{[%s;%s]}{\\mathop{\\max y}}\\,-\\underset{[%s;%s]}{\\mathop{\\min y}}\\,=%s-\\left(%s\\right)=%s \\approx %s$$zz$'''
                        %(latex(3*A),latex(2*B),latex(C),
                        latex(b),latex(g),latex(h),latex(i),latex(g),latex(h),
                        latex(g),latex(m1),latex(h),latex(m2),latex(b),latex(m4),latex(i),latex(m3),
                        latex(g),latex(h),latex(g),latex(h),latex(ln),latex(nn),latex(ln-nn),latex(kq)))

                #Đáp án


            if dang=='3':
                a = 1
                b = randint(-5,-1)
                c = randint(-6,6)
                d = randint(4,8)
                e = randint(-20,20)
                g = randint(-5,5)
                h = randint(-4,10)
                i= Rational(d,c)
                while a==0 or c==0 or b>=i or h<=i or g>=b:
                    a = 1
                    b = randint(-5,-1)
                    c = randint(-6,6)
                    d = randint(4,8)
                    e = randint(-20,20)
                    g = randint(-5,5)
                    h = randint(-4,10)
                    i= Rational(d,c)
                A = Rational(a*c,3)
                B = Rational (a*d+b*c,-2)
                C = b*d
                D = e
                m1=A*g**3+B*g**2+C*g+D
                m2=A*h**3+B*h**2+C*h+D
                m3=A*i**3+B*i**2+C*i+D
                m4=A*b**3+B*b**2+C*b+D
                listmm=(m1,m2,m3,m4)
                ln=max(listmm)
                nn=min(listmm)
                while ln*nn>=99 or ln*nn<=-9.9 or (ln*nn)%1==0:
                    a = 1
                    b = randint(-5,-1)
                    c = randint(-6,6)
                    d = randint(4,8)
                    e = randint(-20,20)
                    g = randint(-5,5)
                    h = randint(-4,10)
                    i= Rational(d,c)
                    while a==0 or c==0 or b>=i or h<=i or g>=b:
                        a = 1
                        b = randint(-5,-1)
                        c = randint(-6,6)
                        d = randint(4,8)
                        e = randint(-20,20)
                        g = randint(-5,5)
                        h = randint(-4,10)
                        i= Rational(d,c)
                    A = Rational(a*c,3)
                    B = Rational (a*d+b*c,-2)
                    C = b*d
                    D = e
                    m1=A*g**3+B*g**2+C*g+D
                    m2=A*h**3+B*h**2+C*h+D
                    m3=A*i**3+B*i**2+C*i+D
                    m4=A*b**3+B*b**2+C*b+D
                    listmm=(m1,m2,m3,m4)
                    ln=max(listmm)
                    nn=min(listmm)
                x0=ln*nn
                number = Decimal(float(x0))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                # Nội dung câu hỏi
                noidungcauhoi = ('Tính tích giá trị lớn nhất và giá trị nhỏ nhất của hàm số $y=%sx^3+%sx^2+%sx+%s$ trên đoạn $[%s;%s]$ (Kết quả làm tròn đến hàng phần chục)$zz$'
                            %(latex(A),latex(B),latex(C),latex(D),latex(g),latex(h))
                                )

                # Nội dung lời giải
                loigiai = ( '''$y'=%sx^2+%sx+%s$zz$\\\\ \n'''
                        '''y'=0 \\Leftrightarrow \\hoac{& x=%s \\in\\left( %s;%s\\right) \\\\& x=%s \\in\\left( %s;%s\\right)}$\\\\ \n'''
                        '''Ta có: ${y}{\\left(%s\\right)}=%s;\\hspace*{0.5cm} {y}{\\left(%s\\right)}=%s;\\hspace*{0.5cm} {y}{\\left(%s\\right)}=%s;\\hspace*{0.5cm} {y}{\\left(%s\\right)}=%s$$zz$\\\\ \n'''
                        '''Vậy $\\underset{[%s;%s]}{\\mathop{\\max y}}\\,\\cdot\\underset{[%s;%s]}{\\mathop{\\min y}}\\,=%s\\cdot \\left(%s\\right)=%s \\approx %s$$zz$'''
                        %(latex(3*A),latex(2*B),latex(C),
                        latex(b),latex(g),latex(h),latex(i),latex(g),latex(h),
                        latex(g),latex(m1),latex(h),latex(m2),latex(b),latex(m4),latex(i),latex(m3),
                        latex(g),latex(h),latex(g),latex(h),latex(ln),latex(nn),latex(ln*nn),latex(kq)))

                #Đáp án





            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.', ',').replace('$zz$', '.').replace('+-', '-').replace('+1x', '+x').replace('+0x^2', '').replace('+0x', '').replace('+0', '').replace('-1x', '-x').replace('+1x^2', '+x^2').replace('-1x^2', '-x^2').replace('1x^3', 'x^3').replace('-1x^3', '-x^3')
            return content


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


def bt_dang19_p4_b2_c1_ds12(self):
            # Khai báo biến
            lisdang=['1','2','3','4','5','6']
            dang=random.choice(lisdang)
            if dang=='1':
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
                while ln+nn>=9999 or ln+nn<=-1000 or int(ln+nn)!=ln+nn:
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

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho hàm số $y=%sx^4+%sx^2+%s$. Tính $\\underset{[%s;%s]}{\\mathop{\\max y}}\\,+\\underset{[%s;%s]}{\\mathop{\\min y}}\\,$.'
                                %(latex(A),latex(B),latex(C),latex(g),latex(h),latex(g),latex(h))
                                )

                # Nội dung lời giải
                loigiai = ( '''$y'= %sx^3+%s x.\\\\ \n'''
                        '''y'=0 \\Leftrightarrow \\hoac{& x=0 \\in\\left( %s;%s\\right) \\\\& x=%s \\in\\left( %s;%s\\right) \\\\& x=%s \\in\\left( %s;%s\\right).}$\\\\ \n'''
                        '''Ta có: ${y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm} {y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm} {y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm}{y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm} {y}{\\left(%s\\right)}=%s.$\\\\ \n'''
                        '''Vậy\\\\ \n'''
                        '''$\\underset{[%s;%s]}{\\mathop{\\max y}}\\,+\\underset{[%s;%s]}{\\mathop{\\min y}}\\,=%s+\\left(%s\\right)=%s$.\\\\ \n'''
                        %(latex(4*A),latex(2*B),
                        latex(g),latex(h),latex(x1),latex(g),latex(h),latex(x2),latex(g),latex(h),
                        latex(g),latex(m1),latex(h),latex(m2),latex(x1),latex(m3),latex(0),latex(m4),latex(x2),latex(m5),
                        latex(g),latex(h),latex(g),latex(h),latex(ln),latex(nn),latex(ln+nn)
                        ))

                #Đáp án


            if dang=='2':
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
                while ln-nn>=9999 or ln-nn<=-1000 or int(ln-nn)!=ln-nn:
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

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho hàm số $y=%sx^4+%sx^2+%s$. Tính $\\underset{[%s;%s]}{\\mathop{\\max y}}\\,-\\underset{[%s;%s]}{\\mathop{\\min y}}\\,$.'
                                %(latex(A),latex(B),latex(C),latex(g),latex(h),latex(g),latex(h))
                                )

                # Nội dung lời giải
                loigiai = ( '''$y'= %sx^3+%s x.\\\\ \n'''
                        '''y'=0 \\Leftrightarrow \\hoac{& x=0 \\in\\left( %s;%s\\right) \\\\& x=%s \\in\\left( %s;%s\\right) \\\\& x=%s \\in\\left( %s;%s\\right).}$\\\\ \n'''
                        '''Ta có: ${y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm} {y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm} {y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm}{y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm} {y}{\\left(%s\\right)}=%s.$\\\\ \n'''
                        '''Vậy\\\\ \n'''
                        '''$\\underset{[%s;%s]}{\\mathop{\\max y}}\\,-\\underset{[%s;%s]}{\\mathop{\\min y}}\\,=%s-\\left(%s\\right)=%s$.\\\\ \n'''
                        %(latex(4*A),latex(2*B),
                        latex(g),latex(h),latex(x1),latex(g),latex(h),latex(x2),latex(g),latex(h),
                        latex(g),latex(m1),latex(h),latex(m2),latex(x1),latex(m3),latex(0),latex(m4),latex(x2),latex(m5),
                        latex(g),latex(h),latex(g),latex(h),latex(ln),latex(nn),latex(ln-nn)
                        ))

                #Đáp án


            if dang=='3':
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
                while ln*nn>=9999 or ln*nn<=-1000 or int(ln*nn)!=ln*nn:
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

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho hàm số $y=%sx^4+%sx^2+%s$. Tính $\\underset{[%s;%s]}{\\mathop{\\max y}}\\,\\cdot\\underset{[%s;%s]}{\\mathop{\\min y}}\\,$.'
                                %(latex(A),latex(B),latex(C),latex(g),latex(h),latex(g),latex(h))
                                )

                # Nội dung lời giải
                loigiai = ( '''$y'= %sx^3+%s x.\\\\ \n'''
                        '''y'=0 \\Leftrightarrow \\hoac{& x=0 \\in\\left( %s;%s\\right) \\\\& x=%s \\in\\left( %s;%s\\right) \\\\& x=%s \\in\\left( %s;%s\\right).}$\\\\ \n'''
                        '''Ta có: ${y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm} {y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm} {y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm}{y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm} {y}{\\left(%s\\right)}=%s.$\\\\ \n'''
                        '''Vậy\\\\ \n'''
                        '''$\\underset{[%s;%s]}{\\mathop{\\max y}}\\,\\cdot\\underset{[%s;%s]}{\\mathop{\\min y}}\\,=%s \\cdot\\left(%s\\right)=%s$.\\\\ \n'''
                        %(latex(4*A),latex(2*B),
                        latex(g),latex(h),latex(x1),latex(g),latex(h),latex(x2),latex(g),latex(h),
                        latex(g),latex(m1),latex(h),latex(m2),latex(x1),latex(m3),latex(0),latex(m4),latex(x2),latex(m5),
                        latex(g),latex(h),latex(g),latex(h),latex(ln),latex(nn),latex(ln*nn)
                        ))

                #Đáp án


            if dang=='4':
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
                while ln+nn>=9999 or ln+nn<=-1000 or int(ln+nn)!=ln+nn:
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

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho hàm số $y=%sx^4+%sx^2+%s$. Gọi $M;m$ lần lượt là giá trị lớn nhất và giá trị nhỏ nhất của hàm số trên đoạn [%s;%s]. Tính giá trị của biểu thức $M+m$.'
                                %(latex(A),latex(B),latex(C),latex(g),latex(h))
                                )

                # Nội dung lời giải
                loigiai = ( '''$y'= %sx^3+%s x.\\\\ \n'''
                        '''y'=0 \\Leftrightarrow \\hoac{& x=0 \\in\\left( %s;%s\\right) \\\\& x=%s \\notin\\left( %s;%s\\right) \\\\& x=%s \\in\\left( %s;%s\\right).}$\\\\ \n'''
                        '''Ta có: ${y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm} {y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm}{y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm} {y}{\\left(%s\\right)}=%s.$\\\\ \n'''
                        '''Khi đó $M=\\underset{[%s;%s]}{\\mathop{\\max y}}\\,=%s$;\\hspace*{1cm}$m=\\underset{[%s;%s]}{\\mathop{\\min y}}\\,=%s$.\\\\ \n'''
                        '''Vậy\\\\ \n'''
                        '''\\hspace*{1cm}$M+m=%s +\\left(%s\\right)=%s$.\\\\ \n'''
                        %(latex(4*A),latex(2*B),
                        latex(g),latex(h),latex(x1),latex(g),latex(h),latex(x2),latex(g),latex(h),
                        latex(g),latex(m1),latex(h),latex(m2),latex(0),latex(m4),latex(x2),latex(m5),
                        latex(g),latex(h),latex(ln),latex(g),latex(h),latex(nn),
                        latex(ln),latex(nn),latex(ln+nn)
                        ))

                #Đáp án


            if dang=='5':
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
                while ln-nn>=9999 or ln-nn<=-1000 or int(ln-nn)!=ln-nn:
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

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho hàm số $y=%sx^4+%sx^2+%s$. Gọi $M;m$ lần lượt là giá trị lớn nhất và giá trị nhỏ nhất của hàm số trên đoạn [%s;%s]. Tính giá trị của biểu thức $M-m$.'
                                %(latex(A),latex(B),latex(C),latex(g),latex(h))
                                )

                # Nội dung lời giải
                loigiai = ( '''$y'= %sx^3+%s x.\\\\ \n'''
                        '''y'=0 \\Leftrightarrow \\hoac{& x=0 \\in\\left( %s;%s\\right) \\\\& x=%s \\notin\\left( %s;%s\\right) \\\\& x=%s \\in\\left( %s;%s\\right).}$\\\\ \n'''
                        '''Ta có: ${y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm} {y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm}{y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm} {y}{\\left(%s\\right)}=%s.$\\\\ \n'''
                        '''Khi đó $M=\\underset{[%s;%s]}{\\mathop{\\max y}}\\,=%s$;\\hspace*{1cm}$m=\\underset{[%s;%s]}{\\mathop{\\min y}}\\,=%s$.\\\\ \n'''
                        '''Vậy\\\\ \n'''
                        '''\\hspace*{1cm}$M-m=%s -\\left(%s\\right)=%s$.\\\\ \n'''
                        %(latex(4*A),latex(2*B),
                        latex(g),latex(h),latex(x1),latex(g),latex(h),latex(x2),latex(g),latex(h),
                        latex(g),latex(m1),latex(h),latex(m2),latex(0),latex(m4),latex(x2),latex(m5),
                        latex(g),latex(h),latex(ln),latex(g),latex(h),latex(nn),
                        latex(ln),latex(nn),latex(ln-nn)
                        ))

                #Đáp án


            if dang=='6':
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
                while ln*nn>=9999 or ln*nn<=-1000 or int(ln*nn)!=ln*nn:
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

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho hàm số $y=%sx^4+%sx^2+%s$. Gọi $M;m$ lần lượt là giá trị lớn nhất và giá trị nhỏ nhất của hàm số trên đoạn [%s;%s]. Tính tích $M\\cdot m$.'
                                %(latex(A),latex(B),latex(C),latex(g),latex(h))
                                )

                # Nội dung lời giải
                loigiai = ( '''$y'= %sx^3+%s x.\\\\ \n'''
                        '''y'=0 \\Leftrightarrow \\hoac{& x=0 \\in\\left( %s;%s\\right) \\\\& x=%s \\notin\\left( %s;%s\\right) \\\\& x=%s \\in\\left( %s;%s\\right).}$\\\\ \n'''
                        '''Ta có: ${y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm} {y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm}{y}{\\left(%s\\right)}=%s;\\hspace*{0.4cm} {y}{\\left(%s\\right)}=%s.$\\\\ \n'''
                        '''Khi đó $M=\\underset{[%s;%s]}{\\mathop{\\max y}}\\,=%s$;\\hspace*{1cm}$m=\\underset{[%s;%s]}{\\mathop{\\min y}}\\,=%s$.\\\\ \n'''
                        '''Vậy\\\\ \n'''
                        '''\\hspace*{1cm}$M\\cdot m=%s \\cdot\\left(%s\\right)=%s$.\\\\ \n'''
                        %(latex(4*A),latex(2*B),
                        latex(g),latex(h),latex(x1),latex(g),latex(h),latex(x2),latex(g),latex(h),
                        latex(g),latex(m1),latex(h),latex(m2),latex(0),latex(m4),latex(x2),latex(m5),
                        latex(g),latex(h),latex(ln),latex(g),latex(h),latex(nn),
                        latex(ln),latex(nn),latex(ln*nn)
                        ))

                #Đáp án


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-').replace('11x', '11fx').replace('21x', '21fx').replace('31x', '31fx').replace('41x', '41fx').replace('51x', '51fx').replace('61x', '61fx').replace('71x', '71fx').replace('81x', '81fx').replace('91x', '91fx').replace('101x', '101fx').replace('1x', 'x').replace('11fx', '11x').replace('21fx', '21x').replace('31fx', '31x').replace('41fx', '41x').replace('51fx', '51x').replace('61fx', '61x').replace('71fx', '71x').replace('81fx', '81x').replace('91fx', '91x').replace('101fx', '101x').replace('+0x^2', '').replace('+0x', '').replace('+0', '')
            return content


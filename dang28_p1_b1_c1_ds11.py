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


def bt_dang28_p1_b1_c1_ds11(self):
            # Khai báo biến  
            lis=[1,2,3,4,5,6,7,8,9]
            k=random.choice(lis)
            lis0=[3*k,4*k,5*k,12*k,8*k,15*k,7*k,24*k]
            a=random.choice(lis0)
            if a==3*k or a==4*k:
                b=5*k
            if a==5*k or a==12*k:
                b=13*k
            if a==8*k or a==15*k:
                b=17*k
            if a==7*k or a==24*k:
                b=25*k

            x1=Rational(a,b)
            lis1=[2,3,4,5,6,7,8,9,-2,-3,-4,-5,-6,-7,-8,-9]

            sin=Rational(a,b)
            can=sqrt(b**2-a**2)
            cos=Rational(can,b)
            tan=Rational(sin,cos)
            cot=Rational(cos,sin)

            m=random.choice(lis1)
            n=random.choice(lis1)
            p=m*sin+n*cos

            a1=n**2+m**2
            b1=-2*p*m
            c1=p**2-n**2
            delta=b1**2-4*a1*c1
            can_delta=sqrt(delta)
            x_1=Rational(-b1+can_delta,2*a1)
            x_2=Rational(-b1-can_delta,2*a1)
            #Dang 1
            t=randint(50,100)
            kq1=Rational(t*(t+1)*sin,2)
            #Dang 2
            a21=random.choice(lis1)
            b21=random.choice(lis1)
            c21=random.choice(lis1)
            a22=random.choice(lis1)
            b22=random.choice(lis1)
            c22=random.choice(lis1)
            kq2=Rational(a21*sin+b21*cos+c21,a22*sin+b22*cos+c22)
            #Dang 3
            kq3=Rational(a21*sin+b21*cos,a22*tan+b22)
            #Dang 4
            kq4=Rational(a21*tan+b21*cot+a22*tan**2+b22*cot**2,1)
            lis=['1','2','3','4']
            dang=random.choice(lis)
            if dang=='1':
                # Câu hỏi
                noidungcauhoi=('''Cho $%s \\sin a +%s \\cos a =%s$. Giá trị biểu thức $P=\\sin a + 2 \\sin a + 3 \\sin a + \\cdots + %s \\sin a$ là  \n'''
                            %(latex(m),latex(n),latex(p),latex(t)
                                ))
                # Các đáp án
                da_d = '\\True $%s$'%(latex(kq1))
                da_s1 = '$%s$'%(latex(kq1+1))
                da_s2 = '$%s$'%(latex(kq1-1))
                da_s3 = '$%s$'%(latex(kq1+2))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Theo giả thiết \\\\ \n'
                        '$%s \\sin a +%s \\cos a =%s \\Leftrightarrow \\cos a = \\dfrac{%s -%s \\sin a}{%s}$.\\\\ \n'
                        'Ta có \\\\ \n'
                        '$\\sin^{2}a + \\cos^{2}a =1 \\Leftrightarrow \\sin^{2}a + \\left( \\dfrac{%s -%s \\sin a}{%s} \\right)^2 -1=0$\\\\ \n'
                        '$\\Leftrightarrow %s \\sin^{2}a +%s -%s \\sin a +%s \\sin^{2}a -%s =0$\\\\ \n'
                        '$\\Leftrightarrow %s \\sin^{2}a -%s \\sin a +%s =0 \\Leftrightarrow \\hoac{& \\sin a =%s \\\\ & \\sin a =%s.}$\\\\ \n'
                        'Với $\\sin a = %s$ ta có\\\\ \n'
                        '$P=\\sin a + 2 \\sin a + 3 \\sin a + \\cdots + %s \\sin a$ \\\\ \n'
                        '$P=(1+2+3+ \\cdots +%s) \\sin a$ \\\\ \n'
                        '$P=\\dfrac{%s(%s+1)}{2} \\sin a = \\dfrac{%s(%s+1)}{2} \\left( %s \\right) =%s$. \\\\ \n'
                        %(latex(m),latex(n),latex(p),latex(p),latex(m),latex(n),
                            latex(p),latex(m),latex(n),
                            latex(n**2), latex(p**2), latex(2*p*m), latex(m**2), latex(n**2),
                            latex(n**2+m**2), latex(2*p*m), latex(p**2-n**2),
                            latex(x_1),latex(x_2),
                            latex(sin),
                            latex(t),
                            latex(t),
                            latex(t),
                            latex(t),
                            latex(t),latex(t),latex(sin),
                            latex(kq1)


                            ))
            if dang=='2':
                # Câu hỏi
                noidungcauhoi=('''Cho $%s \\sin a +%s \\cos a =%s$. Giá trị biểu thức $P=\\dfrac{%s \\sin a +%s \\cos a +%s}{%s \\sin a +%s \\cos a +%s}$ là  \n'''
                            %(latex(m),latex(n),latex(p),latex(a21),latex(b21),latex(c21),latex(a22),latex(b22),latex(c22)
                                ))
                # Các đáp án
                da_d = '\\True $%s$'%(latex(kq2))
                da_s1 = '$%s$'%(latex(kq2+1))
                da_s2 = '$%s$'%(latex(kq2-1))
                da_s3 = '$%s$'%(latex(kq2-2))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Theo giả thiết \\\\ \n'
                        '$%s \\sin a +%s \\cos a =%s \\Leftrightarrow \\cos a = \\dfrac{%s -%s \\sin a}{%s}$.\\\\ \n'
                        'Ta có \\\\ \n'
                        '$\\sin^{2}a + \\cos^{2}a =1 \\Leftrightarrow \\sin^{2}a + \\left( \\dfrac{%s -%s \\sin a}{%s} \\right)^2 -1=0$\\\\ \n'
                        '$\\Leftrightarrow %s \\sin^{2}a +%s -%s \\sin a +%s \\sin^{2}a -%s =0$\\\\ \n'
                        '$\\Leftrightarrow %s \\sin^{2}a -%s \\sin a +%s =0 \\Leftrightarrow \\hoac{& \\sin a =%s \\\\ & \\sin a =%s.}$\\\\ \n'
                        'Với $\\sin a = %s$ suy ra $\\cos a = \\dfrac{%s -%s \\sin a}{%s} = \\dfrac{%s -%s \\cdot \\left( %s \\right)}{%s} = %s$.\\\\ \n'
                        'Ta có \\\\ \n'
                        '$P=\\dfrac{%s \\sin a +%s \\cos a +%s}{%s \\sin a +%s \\cos a +%s}$ \\\\ \n'
                        '$P=\\dfrac{%s \\left( %s \\right) +%s \\left( %s \\right) +%s}{%s \\left( %s \\right) +%s \\left( %s \\right) +%s} =%s$. \\\\ \n'
                        %(latex(m),latex(n),latex(p),latex(p),latex(m),latex(n),
                            latex(p),latex(m),latex(n),
                            latex(n**2), latex(p**2), latex(2*p*m), latex(m**2), latex(n**2),
                            latex(n**2+m**2), latex(2*p*m), latex(p**2-n**2),
                            latex(x_1),latex(x_2),
                            latex(Rational(a,b)),latex(p),latex(m),latex(n),latex(p),latex(m),latex(Rational(a,b)), latex(n),latex(Rational(can,b)),
                            latex(a21),latex(b21),latex(c21),latex(a22),latex(b22),latex(c22),
                            latex(a21),latex(sin),latex(b21),latex(cos),latex(c21),latex(a22),latex(sin),latex(b22),latex(cos),latex(c22),latex(kq2)
                            ))
            if dang=='3':
                # Câu hỏi
                noidungcauhoi=('''Cho $%s \\sin a +%s \\cos a =%s$. Giá trị biểu thức $P=\\dfrac{%s \\sin a +%s \\cos a}{%s \\tan a +%s}$ là  \n'''
                            %(latex(m),latex(n),latex(p),latex(a21),latex(b21),latex(a22),latex(b22)
                                ))
                # Các đáp án
                da_d = '\\True $%s$'%(latex(kq3))
                da_s1 = '$%s$'%(latex(kq3+1))
                da_s2 = '$%s$'%(latex(kq3-1))
                da_s3 = '$%s$'%(latex(kq3-2))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Theo giả thiết \\\\ \n'
                        '$%s \\sin a +%s \\cos a =%s \\Leftrightarrow \\cos a = \\dfrac{%s -%s \\sin a}{%s}$.\\\\ \n'
                        'Ta có \\\\ \n'
                        '$\\sin^{2}a + \\cos^{2}a =1 \\Leftrightarrow \\sin^{2}a + \\left( \\dfrac{%s -%s \\sin a}{%s} \\right)^2 -1=0$\\\\ \n'
                        '$\\Leftrightarrow %s \\sin^{2}a +%s -%s \\sin a +%s \\sin^{2}a -%s =0$\\\\ \n'
                        '$\\Leftrightarrow %s \\sin^{2}a -%s \\sin a +%s =0 \\Leftrightarrow \\hoac{& \\sin a =%s \\\\ & \\sin a =%s.}$\\\\ \n'
                        'Với $\\sin a = %s$ suy ra $\\cos a = \\dfrac{%s -%s \\sin a}{%s} = \\dfrac{%s -%s \\cdot \\left( %s \\right)}{%s} = %s$.\\\\ \n'
                        'và $\\tan a = \\dfrac{\\sin a}{\\cos a} = \\dfrac{%s}{%s} = %s$.\\\\ \n'
                        'Ta có \\\\ \n'
                        '$P=\\dfrac{%s \\sin a +%s \\cos a}{%s \\tan a +%s}$ \\\\ \n'
                        '$P=\\dfrac{%s \\left( %s \\right) +%s \\left( %s \\right)}{%s \\left( %s \\right) +%s}=%s$. \\\\ \n'

                        %(latex(m),latex(n),latex(p),latex(p),latex(m),latex(n),
                            latex(p),latex(m),latex(n),
                            latex(n**2), latex(p**2), latex(2*p*m), latex(m**2), latex(n**2),
                            latex(n**2+m**2), latex(2*p*m), latex(p**2-n**2),
                            latex(x_1),latex(x_2),
                            latex(Rational(a,b)),latex(p),latex(m),latex(n),latex(p),latex(m),latex(Rational(a,b)), latex(n),latex(Rational(can,b)),
                            latex(Rational(a,b)), latex(Rational(can,b)),latex(tan),
                            latex(a21),latex(b21),latex(a22),latex(b22),
                            latex(a21),latex(sin),latex(b21),latex(cos),latex(a22),latex(tan),latex(b22),latex(kq3)
                            ))
            if dang=='4':
                # Câu hỏi
                noidungcauhoi=('''Cho $%s \\sin a +%s \\cos a =%s$. Giá trị biểu thức $P= %s \\tan a +%s \\cot a +%s \\tan^{2}a +%s \\cot^{2}a$ là  \n'''
                            %(latex(m),latex(n),latex(p),latex(a21),latex(b21),latex(a22),latex(b22)
                                ))
                # Các đáp án
                da_d = '\\True $%s$'%(latex(kq4))
                da_s1 = '$%s$'%(latex(kq4+1))
                da_s2 = '$%s$'%(latex(kq4-1))
                da_s3 = '$%s$'%(latex(kq4-2))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Theo giả thiết \\\\ \n'
                        '$%s \\sin a +%s \\cos a =%s \\Leftrightarrow \\cos a = \\dfrac{%s -%s \\sin a}{%s}$.\\\\ \n'
                        'Ta có \\\\ \n'
                        '$\\sin^{2}a + \\cos^{2}a =1 \\Leftrightarrow \\sin^{2}a + \\left( \\dfrac{%s -%s \\sin a}{%s} \\right)^2 -1=0$\\\\ \n'
                        '$\\Leftrightarrow %s \\sin^{2}a +%s -%s \\sin a +%s \\sin^{2}a -%s =0$\\\\ \n'
                        '$\\Leftrightarrow %s \\sin^{2}a -%s \\sin a +%s =0 \\Leftrightarrow \\hoac{& \\sin a =%s \\\\ & \\sin a =%s.}$\\\\ \n'
                        'Với $\\sin a = %s$ suy ra $\\cos a = \\dfrac{%s -%s \\sin a}{%s} = \\dfrac{%s -%s \\cdot \\left( %s \\right)}{%s} = %s$.\\\\ \n'
                        'Do đó $\\tan a = \\dfrac{\\sin a}{\\cos a} = \\dfrac{%s}{%s} = %s$.\\\\ \n'
                        'Và $\\cot a = \\dfrac{\\cos a}{\\sin a} = \\dfrac{%s}{%s} = %s$.\\\\ \n'
                        'Ta có \\\\ \n'
                        '$P= %s \\tan a +%s \\cot a +%s \\tan^{2}a +%s \\cot^{2}a$\\\\ \n'
                        '$P= %s \\left( %s \\right) +%s \\left( %s \\right) +%s \\left( %s \\right)^2 +%s \\left( %s \\right)^2 =%s$.\\\\ \n'
                        %(latex(m),latex(n),latex(p),latex(p),latex(m),latex(n),
                            latex(p),latex(m),latex(n),
                            latex(n**2), latex(p**2), latex(2*p*m), latex(m**2), latex(n**2),
                            latex(n**2+m**2), latex(2*p*m), latex(p**2-n**2),
                            latex(x_1),latex(x_2),
                            latex(Rational(a,b)),latex(p),latex(m),latex(n),latex(p),latex(m),latex(Rational(a,b)), latex(n),latex(Rational(can,b)),
                            latex(Rational(a,b)), latex(Rational(can,b)),latex(tan),
                            latex(Rational(can,b)), latex(Rational(a,b)), latex(cot),
                            latex(a21),latex(b21),latex(a22),latex(b22),
                            latex(a21),latex(tan),latex(b21),latex(cot),latex(a22),latex(tan),latex(b22),latex(cot),latex(kq4)
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac').replace('+-','-').replace('--','+')
            return content


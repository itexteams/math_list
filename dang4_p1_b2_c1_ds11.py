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


def bt_dang4_p1_b2_c1_ds11(self):
            # Khai báo biến
            lisdang=['1','2','3','4','5','6','7','8','9','10']
            dang=random.choice(lisdang)
            if dang=='10':
                a=randint(-20,20)
                while a==1 or a==-1:
                    a=randint(-20,20)

                lisgoc=[45,3*45,5*45,7*45,9*45,11*45,13*45,15*45,17*45,19*45]
                goc=random.choice(lisgoc)
                g=goc*pi/180

                kq=(a-tan(g))/(1+a*tan(g))
                i=randint(-5,5)
                j=randint(-5,5)
                k=randint(-5,5)
                while i==j or j==k or i==k or i==0 or j==0 or k==0:
                    i=randint(-5,5)
                    j=randint(-5,5)
                    k=randint(-5,5)

                d = [
                    '$%s$'%(latex(kq)),
                    ]
                da= random.choice(d)
                s = [
                    '$%s$'%(latex(kq+i)),
                    '$%s$'%(latex(kq+j)),
                    '$%s$'%(latex(kq+k)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho $\\tan a = %s$. Giá trị $\\tan \\left(a-%s\\right)$ bằng \n'
                                %(latex(a),latex(g))
                            ) 

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
                        'Ta có \\\\ \n'
                        '\\hspace*{1cm} $\\tan \\left(a+%s\\right) =\\dfrac{\\tan a-\\tan %s}{1+\\tan a \\tan %s}'
                        '=\\dfrac{%s-\\left( %s \\right)}{1+\\left( %s \\right) \\cdot \\left( %s \\right)}'
                        '=%s$. \\\\ \n'

                        %(latex(g),latex(g),latex(g),
                        latex(a),latex(tan(g)),
                        latex(a),latex(tan(g)),
                        latex(kq)
                        ))
            if dang=='9':
                a=randint(-20,20)
                while a==1 or a==-1:
                    a=randint(-20,20)

                lisgoc=[45,3*45,5*45,7*45,9*45,11*45,13*45,15*45,17*45,19*45]
                goc=random.choice(lisgoc)
                g=goc*pi/180

                kq=(a+tan(g))/(1-a*tan(g))
                i=randint(-5,5)
                j=randint(-5,5)
                k=randint(-5,5)
                while i==j or j==k or i==k or i==0 or j==0 or k==0:
                    i=randint(-5,5)
                    j=randint(-5,5)
                    k=randint(-5,5)

                d = [
                    '$%s$'%(latex(kq)),
                    ]
                da= random.choice(d)
                s = [
                    '$%s$'%(latex(kq+i)),
                    '$%s$'%(latex(kq+j)),
                    '$%s$'%(latex(kq+k)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho $\\tan a = %s$. Giá trị $\\tan \\left(a+%s\\right)$ bằng \n'
                                %(latex(a),latex(g))
                            ) 

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
                        'Ta có \\\\ \n'
                        '\\hspace*{1cm} $\\tan \\left(a+%s\\right) =\\dfrac{\\tan a+\\tan %s}{1-\\tan a \\tan %s}'
                        '=\\dfrac{%s+\\left( %s \\right)}{1-\\left( %s \\right) \\cdot \\left( %s \\right)}'
                        '=%s$. \\\\ \n'

                        %(latex(g),latex(g),latex(g),
                        latex(a),latex(tan(g)),
                        latex(a),latex(tan(g)),
                        latex(kq)
                        ))
            if dang=='8':
                m=randint(1,20)
                n=randint(1,20)
                while n<m:
                    m=randint(1,20)
                    n=randint(1,20)
                a=Rational(m,n)

                lisgoc=[30,45,60,90,120,135,150,180]
                goc=random.choice(lisgoc)
                g=goc*pi/180

                kq=a*cos(g)-sqrt(1-a**2)*sin(g)
                i=randint(-5,5)
                j=randint(-5,5)
                k=randint(-5,5)
                while i==j or j==k or i==k or i==0 or j==0 or k==0:
                    i=randint(-5,5)
                    j=randint(-5,5)
                    k=randint(-5,5)

                d = [
                    '$%s$'%(latex(kq)),
                    ]
                da= random.choice(d)
                s = [
                    '$%s$'%(latex(kq+i)),
                    '$%s$'%(latex(kq+j)),
                    '$%s$'%(latex(kq+k)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho $\\cos a = %s$ với $a \\in \\left(\\dfrac{3\\pi}{2};2\\pi \\right)$. Giá trị $\\cos \\left(a-%s\\right)$ bằng \n'
                                %(latex(a),latex(g))
                            ) 

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
                        'Ta có \\\\ \n'
                        '\\hspace*{1cm} $\\sin^2 a +\\cos^2 a =1 \\Leftrightarrow \\sin^2 a=1-\\cos^2 a =1-\\left(%s \\right)^2 =%s \\Leftrightarrow \\sin a =\\pm %s$. \\\\ \n'
                        '\\hspace*{1cm} Vì $a \\in \\left(\\dfrac{3\\pi}{2};2\\pi \\right)$, $\\sin a <0$ nên $\\sin a =%s$. \\\\ \n'
                        'Suy ra \\\\ \n'
                        '\\hspace*{1cm} $\\cos \\left(a-%s\\right) =\\cos a \\cos %s + \\sin a \\sin %s$'
                        '$=%s \\cdot \\left(%s \\right) + \\left(%s \\right) \\cdot \\left(%s \\right)$'
                        '$=%s$. \\\\ \n'

                        %(latex(a),latex(1-a**2),latex(-sqrt(1-a**2)),
                        latex(-sqrt(1-a**2)),
                        latex(g),latex(g),latex(g),
                        latex(a),latex(cos(g)),latex(-sqrt(1-a**2)),latex(sin(g)),
                        latex(kq)
                        ))
            if dang=='7':
                m=randint(1,20)
                n=randint(1,20)
                while n<m:
                    m=randint(1,20)
                    n=randint(1,20)
                a=Rational(m,n)

                lisgoc=[30,45,60,90,120,135,150,180]
                goc=random.choice(lisgoc)
                g=goc*pi/180

                kq=a*cos(g)+sqrt(1-a**2)*sin(g)
                i=randint(-5,5)
                j=randint(-5,5)
                k=randint(-5,5)
                while i==j or j==k or i==k or i==0 or j==0 or k==0:
                    i=randint(-5,5)
                    j=randint(-5,5)
                    k=randint(-5,5)

                d = [
                    '$%s$'%(latex(kq)),
                    ]
                da= random.choice(d)
                s = [
                    '$%s$'%(latex(kq+i)),
                    '$%s$'%(latex(kq+j)),
                    '$%s$'%(latex(kq+k)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho $\\cos a = %s$ với $a \\in \\left(\\dfrac{3\\pi}{2};2\\pi \\right)$. Giá trị $\\cos \\left(a+%s\\right)$ bằng  \n'
                                %(latex(a),latex(g))
                            ) 

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
                        'Ta có \\\\ \n'
                        '\\hspace*{1cm} $\\sin^2 a +\\cos^2 a =1 \\Leftrightarrow \\sin^2 a=1-\\cos^2 a =1-\\left(%s \\right)^2 =%s \\Leftrightarrow \\sin a =\\pm %s$. \\\\ \n'
                        '\\hspace*{1cm} Vì $a \\in \\left(\\dfrac{3\\pi}{2};2\\pi \\right)$, $\\sin a <0$ nên $\\sin a =%s$. \\\\ \n'
                        'Suy ra \\\\ \n'
                        '\\hspace*{1cm} $\\cos \\left(a+%s\\right) =\\cos a \\cos %s - \\sin a \\sin %s$'
                        '$=%s \\cdot \\left(%s \\right) - \\left(%s \\right) \\cdot \\left(%s \\right)$'
                        '$=%s$. \\\\ \n'

                        %(latex(a),latex(1-a**2),latex(-sqrt(1-a**2)),
                        latex(-sqrt(1-a**2)),
                        latex(g),latex(g),latex(g),
                        latex(a),latex(cos(g)),latex(-sqrt(1-a**2)),latex(sin(g)),
                        latex(kq)
                        ))
            if dang=='6':
                m=randint(1,20)
                n=randint(1,20)
                while n<m:
                    m=randint(1,20)
                    n=randint(1,20)
                a=Rational(m,n)

                lisgoc=[30,45,60,90,120,135,150,180]
                goc=random.choice(lisgoc)
                g=goc*pi/180

                kq=a*cos(g)+sqrt(1-a**2)*sin(g)
                i=randint(-5,5)
                j=randint(-5,5)
                k=randint(-5,5)
                while i==j or j==k or i==k or i==0 or j==0 or k==0:
                    i=randint(-5,5)
                    j=randint(-5,5)
                    k=randint(-5,5)

                d = [
                    '$%s$'%(latex(kq)),
                    ]
                da= random.choice(d)
                s = [
                    '$%s$'%(latex(kq+i)),
                    '$%s$'%(latex(kq+j)),
                    '$%s$'%(latex(kq+k)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho $\\cos a = %s$ với $a \\in \\left(0;\\dfrac{\\pi}{2} \\right)$. Giá trị $\\cos \\left(a-%s\\right)$ bằng  \n'
                                %(latex(a),latex(g))
                            ) 

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
                        'Ta có \\\\ \n'
                        '\\hspace*{1cm} $\\sin^2 a +\\cos^2 a =1 \\Leftrightarrow \\sin^2 a=1-\\cos^2 a =1-\\left(%s \\right)^2 =%s \\Leftrightarrow \\sin a =\\pm %s$. \\\\ \n'
                        '\\hspace*{1cm} Vì $a \\in \\left(0;\\dfrac{\\pi}{2} \\right)$, $\\sin a >0$ nên $\\sin a =%s$. \\\\ \n'
                        'Suy ra \\\\ \n'
                        '\\hspace*{1cm} $\\cos \\left(a-%s\\right) =\\cos a \\cos %s + \\sin a \\sin %s$'
                        '$=%s \\cdot \\left(%s \\right) + %s \\cdot \\left(%s \\right)$'
                        '$=%s$. \\\\ \n'

                        %(latex(a),latex(1-a**2),latex(-sqrt(1-a**2)),
                        latex(sqrt(1-a**2)),
                        latex(g),latex(g),latex(g),
                        latex(a),latex(cos(g)),latex(sqrt(1-a**2)),latex(sin(g)),
                        latex(kq)
                        ))
            if dang=='5':
                m=randint(1,20)
                n=randint(1,20)
                while n<m:
                    m=randint(1,20)
                    n=randint(1,20)
                a=Rational(m,n)

                lisgoc=[30,45,60,90,120,135,150,180]
                goc=random.choice(lisgoc)
                g=goc*pi/180

                kq=a*cos(g)-sqrt(1-a**2)*sin(g)
                i=randint(-5,5)
                j=randint(-5,5)
                k=randint(-5,5)
                while i==j or j==k or i==k or i==0 or j==0 or k==0:
                    i=randint(-5,5)
                    j=randint(-5,5)
                    k=randint(-5,5)

                d = [
                    '$%s$'%(latex(kq)),
                    ]
                da= random.choice(d)
                s = [
                    '$%s$'%(latex(kq+i)),
                    '$%s$'%(latex(kq+j)),
                    '$%s$'%(latex(kq+k)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho $\\cos a = %s$ với $a \\in \\left(0;\\dfrac{\\pi}{2} \\right)$. Giá trị $\\cos \\left(a+%s\\right)$ bằng \n'
                                %(latex(a),latex(g))
                            ) 

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
                        'Ta có \\\\ \n'
                        '\\hspace*{1cm} $\\sin^2 a +\\cos^2 a =1 \\Leftrightarrow \\sin^2 a=1-\\cos^2 a =1-\\left(%s \\right)^2 =%s \\Leftrightarrow \\sin a =\\pm %s$. \\\\ \n'
                        '\\hspace*{1cm} Vì $a \\in \\left(0;\\dfrac{\\pi}{2} \\right)$, $\\sin a >0$ nên $\\sin a =%s$. \\\\ \n'
                        'Suy ra \\\\ \n'
                        '\\hspace*{1cm} $\\cos \\left(a+%s\\right) =\\cos a \\cos %s - \\sin a \\sin %s$'
                        '$=%s \\cdot \\left(%s \\right) - %s \\cdot \\left(%s \\right)$'
                        '$=%s$. \\\\ \n'

                        %(latex(a),latex(1-a**2),latex(-sqrt(1-a**2)),
                        latex(sqrt(1-a**2)),
                        latex(g),latex(g),latex(g),
                        latex(a),latex(cos(g)),latex(sqrt(1-a**2)),latex(sin(g)),
                        latex(kq)
                        ))
            if dang=='4':
                m=randint(1,20)
                n=randint(1,20)
                while n<m:
                    m=randint(1,20)
                    n=randint(1,20)
                a=Rational(m,n)

                lisgoc=[30,45,60,90,120,135,150,180]
                goc=random.choice(lisgoc)
                g=goc*pi/180

                kq=a*cos(g)+sqrt(1-a**2)*sin(g)
                i=randint(-5,5)
                j=randint(-5,5)
                k=randint(-5,5)
                while i==j or j==k or i==k or i==0 or j==0 or k==0:
                    i=randint(-5,5)
                    j=randint(-5,5)
                    k=randint(-5,5)

                d = [
                    '$%s$'%(latex(kq)),
                    ]
                da= random.choice(d)
                s = [
                    '$%s$'%(latex(kq+i)),
                    '$%s$'%(latex(kq+j)),
                    '$%s$'%(latex(kq+k)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho $\\sin a = %s$ với $a \\in \\left(\\dfrac{\\pi}{2};\\pi \\right)$. Giá trị $\\sin \\left(a-%s\\right)$ bằng  \n'
                                %(latex(a),latex(g))
                            ) 

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
                        'Ta có \\\\ \n'
                        '\\hspace*{1cm} $\\sin^2 a +\\cos^2 a =1 \\Leftrightarrow \\cos^2 a=1-\\sin^2 a =1-\\left(%s \\right)^2 =%s \\Leftrightarrow \\cos a =\\pm %s$. \\\\ \n'
                        '\\hspace*{1cm} Vì $a \\in \\left(\\dfrac{\\pi}{2};\\pi \\right)$, $\\cos a <0$ nên $\\cos a =%s$. \\\\ \n'
                        'Suy ra \\\\ \n'
                        '\\hspace*{1cm} $\\sin \\left(a-%s\\right) =\\sin a \\cos %s - \\cos a \\sin %s$'
                        '$=%s \\cdot \\left(%s \\right) - \\left(%s \\right) \\cdot \\left(%s \\right)$'
                        '$=%s$. \\\\ \n'

                        %(latex(a),latex(1-a**2),latex(-sqrt(1-a**2)),
                        latex(-sqrt(1-a**2)),
                        latex(g),latex(g),latex(g),
                        latex(a),latex(cos(g)),latex(-sqrt(1-a**2)),latex(sin(g)),
                        latex(kq)
                        ))

            if dang=='3':
                m=randint(1,20)
                n=randint(1,20)
                while n<m:
                    m=randint(1,20)
                    n=randint(1,20)
                a=Rational(m,n)

                lisgoc=[30,45,60,90,120,135,150,180]
                goc=random.choice(lisgoc)
                g=goc*pi/180

                kq=a*cos(g)-sqrt(1-a**2)*sin(g)
                i=randint(-5,5)
                j=randint(-5,5)
                k=randint(-5,5)
                while i==j or j==k or i==k or i==0 or j==0 or k==0:
                    i=randint(-5,5)
                    j=randint(-5,5)
                    k=randint(-5,5)

                d = [
                    '$%s$'%(latex(kq)),
                    ]
                da= random.choice(d)
                s = [
                    '$%s$'%(latex(kq+i)),
                    '$%s$'%(latex(kq+j)),
                    '$%s$'%(latex(kq+k)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho $\\sin a = %s$ với $a \\in \\left(\\dfrac{\\pi}{2};\\pi \\right)$. Giá trị $\\sin \\left(a+%s\\right)$ bằng \n'
                                %(latex(a),latex(g))
                            ) 

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
                        'Ta có \\\\ \n'
                        '\\hspace*{1cm} $\\sin^2 a +\\cos^2 a =1 \\Leftrightarrow \\cos^2 a=1-\\sin^2 a =1-\\left(%s \\right)^2 =%s \\Leftrightarrow \\cos a =\\pm %s$. \\\\ \n'
                        '\\hspace*{1cm} Vì $a \\in \\left(\\dfrac{\\pi}{2};\\pi \\right)$, $\\cos a <0$ nên $\\cos a =%s$. \\\\ \n'
                        'Suy ra \\\\ \n'
                        '\\hspace*{1cm} $\\sin \\left(a+%s\\right) =\\sin a \\cos %s + \\cos a \\sin %s$'
                        '$=%s \\cdot \\left(%s \\right) + \\left(%s \\right) \\cdot \\left(%s \\right)$'
                        '$=%s$. \\\\ \n'

                        %(latex(a),latex(1-a**2),latex(-sqrt(1-a**2)),
                        latex(-sqrt(1-a**2)),
                        latex(g),latex(g),latex(g),
                        latex(a),latex(cos(g)),latex(-sqrt(1-a**2)),latex(sin(g)),
                        latex(kq)
                        ))
            if dang=='2':
                m=randint(1,20)
                n=randint(1,20)
                while n<m:
                    m=randint(1,20)
                    n=randint(1,20)
                a=Rational(m,n)

                lisgoc=[30,45,60,90,120,135,150,180]
                goc=random.choice(lisgoc)
                g=goc*pi/180

                kq=a*cos(g)-sqrt(1-a**2)*sin(g)
                i=randint(-5,5)
                j=randint(-5,5)
                k=randint(-5,5)
                while i==j or j==k or i==k or i==0 or j==0 or k==0:
                    i=randint(-5,5)
                    j=randint(-5,5)
                    k=randint(-5,5)

                d = [
                    '$%s$'%(latex(kq)),
                    ]
                da= random.choice(d)
                s = [
                    '$%s$'%(latex(kq+i)),
                    '$%s$'%(latex(kq+j)),
                    '$%s$'%(latex(kq+k)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho $\\sin a = %s$ với $a \\in \\left(0;\\dfrac{\\pi}{2} \\right)$. Giá trị $\\sin \\left(a-%s\\right)$ bằng  \n'
                                %(latex(a),latex(g))
                            ) 

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
                        'Ta có \\\\ \n'
                        '\\hspace*{1cm} $\\sin^2 a +\\cos^2 a =1 \\Leftrightarrow \\cos^2 a=1-\\sin^2 a =1-\\left(%s \\right)^2 =%s \\Leftrightarrow \\cos a =\\pm %s$. \\\\ \n'
                        '\\hspace*{1cm} Vì $a \\in \\left(0;\\dfrac{\\pi}{2} \\right)$, $\\cos a >0$ nên $\\cos a =%s$. \\\\ \n'
                        'Suy ra \\\\ \n'
                        '\\hspace*{1cm} $\\sin \\left(a-%s\\right) =\\sin a \\cos %s - \\cos a \\sin %s$'
                        '$=%s \\cdot \\left(%s \\right) - %s \\cdot \\left(%s \\right)$'
                        '$=%s$. \\\\ \n'

                        %(latex(a),latex(1-a**2),latex(sqrt(1-a**2)),
                        latex(sqrt(1-a**2)),
                        latex(g),latex(g),latex(g),
                        latex(a),latex(cos(g)),latex(sqrt(1-a**2)),latex(sin(g)),
                        latex(kq)
                        ))

            if dang=='1':
                m=randint(1,20)
                n=randint(1,20)
                while n<m:
                    m=randint(1,20)
                    n=randint(1,20)
                a=Rational(m,n)

                lisgoc=[30,45,60,90,120,135,150,180]
                goc=random.choice(lisgoc)
                g=goc*pi/180

                kq=a*cos(g)+sqrt(1-a**2)*sin(g)
                i=randint(-5,5)
                j=randint(-5,5)
                k=randint(-5,5)
                while i==j or j==k or i==k or i==0 or j==0 or k==0:
                    i=randint(-5,5)
                    j=randint(-5,5)
                    k=randint(-5,5)

                d = [
                    '$%s$'%(latex(kq)),
                    ]
                da= random.choice(d)
                s = [
                    '$%s$'%(latex(kq+i)),
                    '$%s$'%(latex(kq+j)),
                    '$%s$'%(latex(kq+k)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho $\\sin a = %s$ với $a \\in \\left(0;\\dfrac{\\pi}{2} \\right)$. Giá trị $\\sin \\left(a+%s\\right)$ bằng \n'
                                %(latex(a),latex(g))
                            ) 

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
                        'Ta có \\\\ \n'
                        '\\hspace*{1cm} $\\sin^2 a +\\cos^2 a =1 \\Leftrightarrow \\cos^2 a=1-\\sin^2 a =1-\\left(%s \\right)^2 =%s \\Leftrightarrow \\cos a =\\pm %s$. \\\\ \n'
                        '\\hspace*{1cm} Vì $a \\in \\left(0;\\dfrac{\\pi}{2} \\right)$, $\\cos a >0$ nên $\\cos a =%s$. \\\\ \n'
                        'Suy ra \\\\ \n'
                        '\\hspace*{1cm} $\\sin \\left(a+%s\\right) =\\sin a \\cos %s + \\cos a \\sin %s$'
                        '$=%s \\cdot \\left(%s \\right) + %s \\cdot \\left(%s \\right)$'
                        '$=%s$. \\\\ \n'

                        %(latex(a),latex(1-a**2),latex(sqrt(1-a**2)),
                        latex(sqrt(1-a**2)),
                        latex(g),latex(g),latex(g),
                        latex(a),latex(cos(g)),latex(sqrt(1-a**2)),latex(sin(g)),
                        latex(kq)
                        ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n '+ str(noidungcauhoi)+ 
                '\\choice[2] \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content


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


def bt_dang5_p1_b2_c1_ds11(self):
            # Khai báo biến
            lisdang=['1','2','3','4','5','6','7']
            dang=random.choice(lisdang)
            if dang=='7':
                m=randint(-9,9)
                n=randint(-9,9)
                while abs(n)<=abs(m):
                    m=randint(-9,9)
                    n=randint(-9,9)
                a=Rational(m,n)

                m1=randint(-9,9)
                n1=randint(-9,9)
                while abs(n1)<=abs(m1):
                    m1=randint(-9,9)
                    n1=randint(-9,9)
                b=Rational(m1,n1)

                kq=((1/a**2-1)-(1/(1-b**2)-1))/(1-((1/a**2-1))*((1/(1-b**2)-1)))

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
                noidungcauhoi = ('Cho $\\cos a = %s, \\sin b =%s$. Giá trị $\\tan (a+b) \\tan (a-b)$ bằng \n'
                                %(latex(a),latex(b))
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
                        '\\hspace*{1cm} $1 +\\tan^2 a =\\dfrac{1}{\\cos^2 a} \\Leftrightarrow \\tan^2 a=\\dfrac{1}{\\cos^2 a} -1 =\\dfrac{1}{\\left(%s\\right)^2}-1 =%s$. \\\\ \n'
                        '\\hspace*{1cm} $\\sin^2 b +\\cos^2 b =1 \\Leftrightarrow \\cos^2 b=1-\\sin^2 b =1-\\left(%s \\right)^2 =%s$. \\\\ \n'
                        '\\hspace*{1cm} $1 +\\tan^2 b =\\dfrac{1}{\\cos^2 b} \\Leftrightarrow \\tan^2 b=\\dfrac{1}{\\cos^2 b} -1 =\\dfrac{1}{%s}-1 =%s$. \\\\ \n'
                        'Suy ra \\\\ \n'
                        '\\hspace*{1cm} $\\tan (a+b) \\tan (a-b) = \\dfrac{\\tan a + \\tan b}{1-\\tan a \\tan b} \\cdot \\dfrac{\\tan a - \\tan b}{1+\\tan a \\tan b}$ \\\\ \n'
                        '\\hspace*{4.8cm} $= \\dfrac{\\tan^2 a - \\tan^2 b}{1-\\tan^2 a \\tan^2 b}$ \\\\ \n'
                        '\\hspace*{4.8cm} $= \\dfrac{%s - %s}{1-%s \\cdot %s} =%s$. \\\\ \n'

                        %(latex(a),latex(1/a**2-1),
                        latex(b),latex(1-b**2),
                        latex(1-b**2),latex(1/(1-b**2)-1),
                        latex(1/a**2-1),latex(1/(1-b**2)-1),latex(1/a**2-1),latex(1/(1-b**2)-1),
                        latex(kq)

                        ))
            if dang=='6':
                m=randint(-9,9)
                n=randint(-9,9)
                while abs(n)<abs(m):
                    m=randint(-9,9)
                    n=randint(-9,9)
                a=Rational(m,n)

                m1=randint(-9,9)
                n1=randint(-9,9)
                while abs(n1)<abs(m1):
                    m1=randint(-9,9)
                    n1=randint(-9,9)
                b=Rational(m1,n1)

                kq=(1-a**2)*(1-b**2)-(a**2)*(b**2)
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
                noidungcauhoi = ('Cho $\\cos a = %s, \\sin b =%s$. Giá trị $\\sin (a+b) \\sin (a-b)$ bằng \n'
                                %(latex(a),latex(b))
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
                        '\\hspace*{1cm} $\\sin^2 a +\\cos^2 a =1 \\Leftrightarrow \\sin^2 a=1-\\cos^2 a =1-\\left(%s \\right)^2 =%s$. \\\\ \n'
                        '\\hspace*{1cm} $\\sin^2 b +\\cos^2 b =1 \\Leftrightarrow \\cos^2 b=1-\\sin^2 b =1-\\left(%s \\right)^2 =%s$. \\\\ \n'
                        'Suy ra \\\\ \n'
                        '\\hspace*{1cm} $\\sin (a+b) \\sin (a-b) = (\\sin a \\cos b + \\cos a \\sin b) (\\sin a \\cos b - \\cos a \\sin b)$ \\\\ \n'
                        '\\hspace*{4.75cm} $= \\sin^2 a \\cos^2 b - \\cos^2 a \\sin^2 b$ \\\\ \n'
                        '\\hspace*{4.75cm} $= \\left( %s \\right) \\cdot \\left( %s \\right) -\\left( %s \\right)^2 \\cdot \\left( %s \\right)^2=%s$. \\\\ \n'

                        %(latex(a),latex(1-a**2),
                        latex(b),latex(1-b**2),
                        latex(1-a**2),latex(1-b**2),latex(a),latex(b),
                        latex(kq)

                        ))
            if dang=='5':
                m=randint(-9,9)
                n=randint(-9,9)
                while abs(n)<abs(m):
                    m=randint(-9,9)
                    n=randint(-9,9)
                a=Rational(m,n)

                m1=randint(-9,9)
                n1=randint(-9,9)
                while abs(n1)<abs(m1):
                    m1=randint(-9,9)
                    n1=randint(-9,9)
                b=Rational(m1,n1)

                kq=(1-a**2)*(b**2)-(a**2)*(1-b**2)
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
                noidungcauhoi = ('Cho $\\cos a = %s, \\cos b =%s$. Giá trị $\\sin (a+b) \\sin (a-b)$ bằng  \n'
                                %(latex(a),latex(b))
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
                        '\\hspace*{1cm} $\\sin^2 a +\\cos^2 a =1 \\Leftrightarrow \\sin^2 a=1-\\cos^2 a =1-\\left(%s \\right)^2 =%s$. \\\\ \n'
                        '\\hspace*{1cm} $\\sin^2 b +\\cos^2 b =1 \\Leftrightarrow \\sin^2 b=1-\\cos^2 b =1-\\left(%s \\right)^2 =%s$. \\\\ \n'
                        'Suy ra \\\\ \n'
                        '\\hspace*{1cm} $\\sin (a+b) \\sin (a-b) = (\\sin a \\cos b + \\cos a \\sin b) (\\sin a \\cos b - \\cos a \\sin b)$ \\\\ \n'
                        '\\hspace*{4.75cm} $= \\sin^2 a \\cos^2 b - \\cos^2 a \\sin^2 b$ \\\\ \n'
                        '\\hspace*{4.75cm} $= \\left( %s \\right) \\cdot \\left( %s \\right)^2 -\\left( %s \\right)^2 \\cdot \\left( %s \\right)=%s$. \\\\ \n'

                        %(latex(a),latex(1-a**2),
                        latex(b),latex(1-b**2),
                        latex(1-a**2),latex(b),latex(a),latex(1-b**2),
                        latex(kq)

                        ))
            if dang=='4':
                m=randint(-9,9)
                n=randint(-9,9)
                while abs(n)<abs(m):
                    m=randint(-9,9)
                    n=randint(-9,9)
                a=Rational(m,n)

                m1=randint(-9,9)
                n1=randint(-9,9)
                while abs(n1)<abs(m1):
                    m1=randint(-9,9)
                    n1=randint(-9,9)
                b=Rational(m1,n1)

                kq=(a**2)*(1-b**2)-(1-a**2)*(b**2)
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
                noidungcauhoi = ('Cho $\\sin a = %s, \\sin b =%s$. Giá trị $\\sin (a+b) \\sin (a-b)$ bằng  \n'
                                %(latex(a),latex(b))
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
                        '\\hspace*{1cm} $\\sin^2 a +\\cos^2 a =1 \\Leftrightarrow \\cos^2 a=1-\\sin^2 a =1-\\left(%s \\right)^2 =%s$. \\\\ \n'
                        '\\hspace*{1cm} $\\sin^2 b +\\cos^2 b =1 \\Leftrightarrow \\cos^2 b=1-\\sin^2 b =1-\\left(%s \\right)^2 =%s$. \\\\ \n'
                        'Suy ra \\\\ \n'
                        '\\hspace*{1cm} $\\sin (a+b) \\sin (a-b) = (\\sin a \\cos b + \\cos a \\sin b) (\\sin a \\cos b - \\cos a \\sin b)$ \\\\ \n'
                        '\\hspace*{4.75cm} $= \\sin^2 a \\cos^2 b - \\cos^2 a \\sin^2 b$ \\\\ \n'
                        '\\hspace*{4.75cm} $= \\left( %s \\right)^2 \\cdot \\left( %s \\right) -\\left( %s \\right) \\cdot \\left( %s \\right)^2=%s$. \\\\ \n'

                        %(latex(a),latex(1-a**2),
                        latex(b),latex(1-b**2),
                        latex(a),latex(1-b**2),latex(1-a**2),latex(b),
                        latex(kq)

                        ))

            if dang=='3':
                m=randint(-9,9)
                n=randint(-9,9)
                while abs(n)<abs(m):
                    m=randint(-9,9)
                    n=randint(-9,9)
                a=Rational(m,n)

                m1=randint(-9,9)
                n1=randint(-9,9)
                while abs(n1)<abs(m1):
                    m1=randint(-9,9)
                    n1=randint(-9,9)
                b=Rational(m1,n1)

                kq=(1-a**2)*(b**2)-(a**2)*(1-b**2)
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
                noidungcauhoi = ('Cho $\\sin a = %s, \\cos b =%s$. Giá trị $\\cos (a+b) \\cos (a-b)$ bằng  \n'
                                %(latex(a),latex(b))
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
                        '\\hspace*{1cm} $\\sin^2 a +\\cos^2 a =1 \\Leftrightarrow \\cos^2 a=1-\\sin^2 a =1-\\left(%s \\right)^2 =%s$. \\\\ \n'
                        '\\hspace*{1cm} $\\sin^2 b +\\cos^2 b =1 \\Leftrightarrow \\sin^2 b=1-\\cos^2 b =1-\\left(%s \\right)^2 =%s$. \\\\ \n'
                        'Suy ra \\\\ \n'
                        '\\hspace*{1cm} $\\cos (a+b) \\cos (a-b) = (\\cos a \\cos b - \\sin a \\sin b) (\\cos a \\cos b + \\sin a \\sin b)$ \\\\ \n'
                        '\\hspace*{4.75cm} $= \\cos^2 a \\cos^2 b - \\sin^2 a \\sin^2 b$ \\\\ \n'
                        '\\hspace*{4.75cm} $= \\left( %s \\right) \\cdot \\left( %s \\right)^2 -\\left( %s \\right)^2 \\cdot \\left( %s \\right)=%s$. \\\\ \n'

                        %(latex(a),latex(1-a**2),
                        latex(b),latex(1-b**2),
                        latex(1-a**2),latex(b),latex(a),latex(1-b**2),
                        latex(kq)
                        ))

            if dang=='2':
                m=randint(-9,9)
                n=randint(-9,9)
                while abs(n)<abs(m):
                    m=randint(-9,9)
                    n=randint(-9,9)
                a=Rational(m,n)

                m1=randint(-9,9)
                n1=randint(-9,9)
                while abs(n1)<abs(m1):
                    m1=randint(-9,9)
                    n1=randint(-9,9)
                b=Rational(m1,n1)

                kq=(a**2)*(b**2)-(1-a**2)*(1-b**2)
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
                noidungcauhoi = ('Cho $\\cos a = %s, \\cos b =%s$. Giá trị $\\cos (a+b) \\cos (a-b)$ bằng  \n'
                                %(latex(a),latex(b))
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
                        '\\hspace*{1cm} $\\sin^2 a +\\cos^2 a =1 \\Leftrightarrow \\sin^2 a=1-\\cos^2 a =1-\\left(%s \\right)^2 =%s$. \\\\ \n'
                        '\\hspace*{1cm} $\\sin^2 b +\\cos^2 b =1 \\Leftrightarrow \\sin^2 b=1-\\cos^2 b =1-\\left(%s \\right)^2 =%s$. \\\\ \n'
                        'Suy ra \\\\ \n'
                        '\\hspace*{1cm} $\\cos (a+b) \\cos (a-b) = (\\cos a \\cos b - \\sin a \\sin b) (\\cos a \\cos b + \\sin a \\sin b)$ \\\\ \n'
                        '\\hspace*{4.75cm} $= \\cos^2 a \\cos^2 b - \\sin^2 a \\sin^2 b$ \\\\ \n'
                        '\\hspace*{4.75cm} $= \\left( %s \\right) \\cdot \\left( %s \\right) -\\left( %s \\right)^2 \\cdot \\left( %s \\right)^2=%s$. \\\\ \n'

                        %(latex(a),latex(1-a**2),
                        latex(b),latex(1-b**2),
                        latex(a),latex(b),latex(1-a**2),latex(1-b**2),
                        latex(kq)
                        ))

            if dang=='1':
                m=randint(-9,9)
                n=randint(-9,9)
                while abs(n)<abs(m):
                    m=randint(-9,9)
                    n=randint(-9,9)
                a=Rational(m,n)

                m1=randint(-9,9)
                n1=randint(-9,9)
                while abs(n1)<abs(m1):
                    m1=randint(-9,9)
                    n1=randint(-9,9)
                b=Rational(m1,n1)

                kq=(1-a**2)*(1-b**2)-(a**2)*(b**2)
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
                noidungcauhoi = ('Cho $\\sin a = %s, \\sin b =%s$. Giá trị $\\cos (a+b) \\cos (a-b)$ bằng  \n'
                                %(latex(a),latex(b))
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
                        '\\hspace*{1cm} $\\sin^2 a +\\cos^2 a =1 \\Leftrightarrow \\cos^2 a=1-\\sin^2 a =1-\\left(%s \\right)^2 =%s$. \\\\ \n'
                        '\\hspace*{1cm} $\\sin^2 b +\\cos^2 b =1 \\Leftrightarrow \\cos^2 b=1-\\sin^2 b =1-\\left(%s \\right)^2 =%s$. \\\\ \n'
                        'Suy ra \\\\ \n'
                        '\\hspace*{1cm} $\\cos (a+b) \\cos (a-b) = (\\cos a \\cos b - \\sin a \\sin b) (\\cos a \\cos b + \\sin a \\sin b)$ \\\\ \n'
                        '\\hspace*{4.75cm} $= \\cos^2 a \\cos^2 b - \\sin^2 a \\sin^2 b$ \\\\ \n'
                        '\\hspace*{4.75cm} $= \\left( %s \\right) \\cdot \\left( %s \\right) -\\left( %s \\right)^2 \\cdot \\left( %s \\right)^2=%s$. \\\\ \n'

                        %(latex(a),latex(1-a**2),
                        latex(b),latex(1-b**2),
                        latex(1-a**2),latex(1-b**2),latex(a),latex(b),
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


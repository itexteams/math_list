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


def bt_dang1_p2_b1_c1_ds12(self):
            # Khai báo biến
            lisdang=['1','2']
            dang=random.choice(lisdang)
            if dang=='2':
                a = randint(-3,3)
                b = randint(-9,9)
                c = randint(-3,3)
                d = randint(-9,9)
                e = randint(-20,20)
                while a==0 or c==0 or b==0 or a*c<=0 or b/a>=d/c:
                    a = randint(-3,3)
                    b = randint(-9,9)
                    c = randint(-3,3)
                    d = randint(-9,9)
                    e = randint(-20,20)
                x1 = Rational(b,a)
                x2 = Rational(d,c)
                y=Rational(a*c,3)*x**3+Rational(a*d+b*c,-2)*x**2+b*d*x+e
                y1=Rational(a*c,3)*x1**3+Rational(a*d+b*c,-2)*x1**2+b*d*x1+e
                y2=Rational(a*c,3)*x2**3+Rational(a*d+b*c,-2)*x2**2+b*d*x2+e
                daoham=(a*c)*x**2+(-a*d-b*c)*x+(b*d)
                du = ['\\True Đạo hàm của hàm số là $y\'=%s$'%(latex(daoham)),
                    '\\True Hàm số đạt cực đại tại điểm $x=%s$'%(latex(x1)),
                    '\\True Hàm số đạt cực tiểu tại điểm $x=%s$'%(latex(x2)),
                    '\\True Giá trị cực đại của hàm số là $y_{\\text{CĐ}}=%s$'%(latex(y1)),
                    '\\True Giá trị cực tiểu của hàm số là $y_{\\text{CT}}=%s$'%(latex(y2)),
                    '\\True Điểm cực đại của đồ thị hàm số là $\\left(%s;%s\\right)$'%(latex(x1),latex(y1)),
                    '\\True Điểm cực tiểu của đồ thị hàm số là $\\left(%s;%s\\right)$'%(latex(x2),latex(y2)),
                    '\\True Hàm số có hai điểm cực trị',
                    '\\True Hàm số nghịch biến trên khoảng $\\left(%s;%s \\right)$'%(latex(x1),latex(x2)),
                    '\\True Hàm số đồng biến trên các khoảng $\\left(-\\infty;%s \\right)$ và $\\left(%s;+\\infty \\right)$'%(latex(x1),latex(x2)),
                    '\\True Phương trình $y\'=0$ có nghiệm là $x=%s$ hoặc $x=%s$'%(latex(x1),latex(x2)),          
                    ]

                da1= random.choice(du)
                du.remove(da1)
                da2= random.choice(du)
                du.remove(da2)
                da3= random.choice(du)
                du.remove(da3)
                da4= random.choice(du)
                s = ['  Đạo hàm của hàm số là $y\'=%s$'%(latex(daoham+1)),
                    '  Hàm số đạt cực đại tại điểm $x=%s$'%(latex(x1+1)),
                    '  Hàm số đạt cực tiểu tại điểm $x=%s$'%(latex(x2-1)),
                    '  Giá trị cực đại của hàm số là $y_{\\text{CĐ}}=%s$'%(latex(y1+1)),
                    '  Giá trị cực tiểu của hàm số là $y_{\\text{CT}}=%s$'%(latex(y2+1)),
                    '  Điểm cực đại của đồ thị hàm số là $x=%s$'%(latex(x1)),
                    '  Điểm cực tiểu của đồ thị hàm số là $x=%s$'%(latex(x2)),
                    '  Hàm số có một điểm cực trị',
                    '  Hàm số nghịch biến trên khoảng $\\left(%s;%s \\right)$'%(latex(x1),latex(x2+1)),
                    '  Hàm số đồng biến trên các khoảng $\\left(-\\infty;%s \\right)$ và $\\left(%s;+\\infty \\right)$'%(latex(x1+1),latex(x2)),
                    '  Phương trình $y\'=0$ có nghiệm là $x=%s$ hoặc $x=%s$'%(latex(-x1),latex(-x2)),  
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                s.remove(das3)
                das4 = random.choice(s)
                list_dapan = [da1,da2,da3,da4,das1,das2,das3,das4]
                # Câu hỏi
                noidungcauhoi = '''Cho hàm số $y=%sx^3+%sx^2+%sx+%s$. \n'''%(latex(Rational(a*c,3)),latex(Rational(a*d+b*c,-2)),latex(b*d),latex(e))
                # Các đáp án
                da_d = random.choice(list_dapan)
                list_dapan.remove(da_d)
                da_s1 = random.choice(list_dapan)
                list_dapan.remove(da_s1)
                da_s2 = random.choice(list_dapan) 
                list_dapan.remove(da_s2)
                da_s3 = random.choice(list_dapan)
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Tập xác định: $D=\\mathbb{R}$.\\\\ \n'
                        '''Ta có $y'=%sx^2+%sx+%s.\\\\ \n''' 
                        '''\\hspace*{1.1cm}y'=0 \\Leftrightarrow \\hoac{& x=%s \\\\& x=%s.}$.\\\\ \n'''
                        '''Bảng biến thiên\\\\ \n'''
                        '\\hspace*{3cm} \\begin{tikzpicture} \n'
                            '\\tkzTabInit[espcl=2.5,lgt=1.5]  \n'
                            '{$x$/1,$y\'$/0.7,$y$/2.1} \n'
                            '{$-\\infty$,$%s$,$%s$,$+\\infty$}  \n'
                            '\\tkzTabLine{,+,0,-,0,+,}  \n'
                            '\\tkzTabVar{-/$-\\infty$,+/$%s$,-/$%s$,+/$+\\infty$} \n'
                        '\\end{tikzpicture}  \\\\ \n'
                        '''Từ bảng biến thiên ta thấy\\\\ \n'''
                        '''\\hspace*{1cm} Hàm số nghịch biến trên khoảng $\\left(%s;%s \\right)$.\\\\ \n'''
                        '''\\hspace*{1cm} Hàm số đồng biến trên các khoảng $\\left(-\\infty;%s \\right)$ và $\\left(%s;+\\infty \\right)$.\\\\ \n'''
                        '''\\hspace*{1cm} Hàm số đạt cực đại tại điểm $x=%s$, giá trị cực đại là $y_{\\text{CĐ}}=%s$;\\\\ \n'''
                        '''\\hspace*{1cm} Hàm số đạt cực tiểu tại điểm $x=%s$, giá trị cực đại là $y_{\\text{CT}}=%s$;\\\\ \n'''
                        %(latex(a*c),latex(-a*d-b*c),latex(b*d),latex(x1),latex(x2),
                        latex(x1),latex(x2),
                        latex(y1),latex(y2),
                        latex(x1),latex(x2),
                        latex(x1),latex(x2),
                        latex(x1),latex(y1),
                        latex(x2),latex(y2)))
            if dang=='1':
                # Khai báo biến
                a = randint(-3,3)
                b = randint(-9,9)
                c = randint(-3,3)
                d = randint(-9,9)
                e = randint(-20,20)
                while a==0 or c==0 or b==0 or a*c>=0 or b/a>=d/c:
                    a = randint(-3,3)
                    b = randint(-9,9)
                    c = randint(-3,3)
                    d = randint(-9,9)
                    e = randint(-20,20)
                x1 = Rational(b,a)
                x2 = Rational(d,c)
                y=Rational(a*c,3)*x**3+Rational(a*d+b*c,-2)*x**2+b*d*x+e
                y1=Rational(a*c,3)*x1**3+Rational(a*d+b*c,-2)*x1**2+b*d*x1+e
                y2=Rational(a*c,3)*x2**3+Rational(a*d+b*c,-2)*x2**2+b*d*x2+e
                daoham=(a*c)*x**2+(-a*d-b*c)*x+(b*d)
                du = ['\\True Đạo hàm của hàm số là $y\'=%s$'%(latex(daoham)),
                    '\\True Hàm số đạt cực tiểu tại điểm $x=%s$'%(latex(x1)),
                    '\\True Hàm số đạt cực đại tại điểm $x=%s$'%(latex(x2)),
                    '\\True Giá trị cực tiểu của hàm số là $y_{\\text{CT}}=%s$'%(latex(y1)),
                    '\\True Giá trị cực đại của hàm số là $y_{\\text{CĐ}}=%s$'%(latex(y2)),
                    '\\True Điểm cực tiểu của đồ thị hàm số là $\\left(%s;%s\\right)$'%(latex(x1),latex(y1)),
                    '\\True Điểm cực đại của đồ thị hàm số là $\\left(%s;%s\\right)$'%(latex(x2),latex(y2)),
                    '\\True Hàm số có hai điểm cực trị',
                    '\\True Hàm số đồng biến trên khoảng $\\left(%s;%s \\right)$'%(latex(x1),latex(x2)),
                    '\\True Hàm số nghịch biến trên các khoảng $\\left(-\\infty;%s \\right)$ và $\\left(%s;+\\infty \\right)$'%(latex(x1),latex(x2)),
                    '\\True Phương trình $y\'=0$ có nghiệm là $x=%s$ hoặc $x=%s$'%(latex(x1),latex(x2)),          
                    ]

                da1= random.choice(du)
                du.remove(da1)
                da2= random.choice(du)
                du.remove(da2)
                da3= random.choice(du)
                du.remove(da3)
                da4= random.choice(du)
                s = ['  Đạo hàm của hàm số là $y\'=%s$'%(latex(daoham+1)),
                    '  Hàm số đạt cực tiểu tại điểm $x=%s$'%(latex(y1)),
                    '  Hàm số đạt cực đại tại điểm $x=%s$'%(latex(y2)),
                    '  Giá trị cực tiểu của hàm số là $y_{\\text{CT}}=%s$'%(latex(y1-9)),
                    '  Giá trị cực đại của hàm số là $y_{\\text{CĐ}}=%s$'%(latex(x2)),
                    '  Điểm cực tiểu của đồ thị hàm số là $x=%s$'%(latex(x1)),
                    '  Điểm cực đại của đồ thị hàm số là $x=%s$'%(latex(x2)),
                    '  Hàm số có một điểm cực trị',
                    '  Hàm số đồng biến trên khoảng $\\left(%s;%s \\right)$'%(latex(x1),latex(x2+1)),
                    '  Hàm số nghịch biến trên các khoảng $\\left(-\\infty;%s \\right)$ và $\\left(%s;+\\infty \\right)$'%(latex(x1+1),latex(x2)),
                    '  Phương trình $y\'=0$ có nghiệm là $x=%s$ hoặc $x=%s$'%(latex(-x1),latex(-x2)),  
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                s.remove(das3)
                das4 = random.choice(s)
                list_dapan = [da1,da2,da3,da4,das1,das2,das3,das4]
                # Câu hỏi
                noidungcauhoi = '''Cho hàm số $y=%sx^3+%sx^2+%sx+%s$. \n'''%(latex(Rational(a*c,3)),latex(Rational(a*d+b*c,-2)),latex(b*d),latex(e))
                # Các đáp án
                da_d = random.choice(list_dapan)
                list_dapan.remove(da_d)
                da_s1 = random.choice(list_dapan)
                list_dapan.remove(da_s1)
                da_s2 = random.choice(list_dapan) 
                list_dapan.remove(da_s2)
                da_s3 = random.choice(list_dapan)
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Tập xác định: $D=\\mathbb{R}$.\\\\ \n'
                        '''Ta có $y'=%sx^2+%sx+%s.\\\\ \n''' 
                        '''\\hspace*{1.1cm}y'=0 \\Leftrightarrow \\hoac{& x=%s \\\\& x=%s.}$.\\\\ \n'''
                        '''Bảng xét dấu\\\\ \n'''
                        '\\hspace*{3cm} \\begin{tikzpicture} \n'
                            '\\tkzTabInit[espcl=2.5,lgt=1.5]  \n'
                            '{$x$/1,$y\'$/0.7,$y$/2.1} \n'
                            '{$-\\infty$,$%s$,$%s$,$+\\infty$}  \n'
                            '\\tkzTabLine{,-,0,+,0,-,}  \n'
                            '\\tkzTabVar{+/$+\\infty$,-/$%s$,+/$%s$,-/$-\\infty$} \n'
                        '\\end{tikzpicture}  \\\\ \n'
                        '''Từ bảng biến thiên ta thấy\\\\ \n'''
                        '''\\hspace*{1cm} Hàm số đồng biến trên khoảng $\\left(%s;%s \\right)$.\\\\ \n'''
                        '''\\hspace*{1cm} Hàm số nghịch biến trên các khoảng $\\left(-\\infty;%s \\right)$ và $\\left(%s;+\\infty \\right)$.\\\\ \n'''
                        '''\\hspace*{1cm} Hàm số đạt cực đại tại điểm $x=%s$, giá trị cực đại là $y_{\\text{CĐ}}=%s$.\\\\ \n'''
                        '''\\hspace*{1cm} Hàm số đạt cực tiểu tại điểm $x=%s$, giá trị cực đại là $y_{\\text{CT}}=%s$.'''
                        %(latex(a*c),latex(-a*d-b*c),latex(b*d),latex(x1),latex(x2),
                        latex(x1),latex(x2),
                        latex(y1),latex(y2),
                        latex(x1),latex(x2),
                        latex(x1),latex(x2),
                        latex(x2),latex(y2),
                        latex(x1),latex(y1)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choiceTFn \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-').replace('+1x', 'x').replace('-1x', '-x').replace('+0x^2', '').replace('+0x', '').replace('+0', '')
            return content


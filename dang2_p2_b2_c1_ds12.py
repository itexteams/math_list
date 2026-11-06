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


def bt_dang2_p2_b2_c1_ds12(self):
            # Khai báo biến
            lisdang=['1','2']
            dang=random.choice(lisdang)
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

                m=randint(-9,-1)
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

                du = ['\\True Hàm số có ba điểm cực trị',
                    '\\True Hàm số đạt cực đại tại các điểm $x=%s$ và $x=%s$'%(latex(x1),latex(x2)),
                    '\\True Hàm số đạt cực tiểu tại điểm $x=0$',
                    '\\True Giá trị cực đại của hàm số là $y_{\\text{CĐ}}=%s$'%(latex(f2)),
                    '\\True Giá trị cực tiểu của hàm số là $y_{\\text{CT}}=%s$'%(latex(f0)),
                    '\\True Điểm cực tiểu của đồ thị hàm số là $\\left(0;%s\\right)$'%(latex(f0)),
                    '\\True Điểm cực đại của đồ thị hàm số là $\\left(%s;%s\\right)$ và $\\left(%s;%s\\right)$'%(latex(x1),latex(f1),latex(x2),latex(f2)),
                    '\\True Hàm số nghịch biến trên các khoảng $(%s;0)$ và $(%s;+\\infty)$'%(latex(x1),latex(x2)),
                    '\\True Hàm số đồng biến trên các khoảng $(-\\infty;%s)$ và $(0;%s)$'%(latex(x1),latex(x2)),
                    '\\True Giá trị nhỏ nhất của hàm số trên đoạn $[%s;%s]$ là $%s$'%(latex(a),latex(b),latex(gtnn)),
                    '\\True Giá trị lớn nhất của hàm số trên đoạn $[%s;%s]$ là $%s$'%(latex(a),latex(b),latex(gtln)),
                    ]

                da1= random.choice(du)
                du.remove(da1)
                da2= random.choice(du)
                du.remove(da2)
                da3= random.choice(du)
                du.remove(da3)
                da4= random.choice(du)
                s = ['  Hàm số có hai điểm cực trị',
                    '  Hàm số đạt cực tiểu tại các điểm $x=%s$ và $x=%s$'%(latex(x1),latex(x2)),
                    '  Hàm số đạt cực đại tại điểm $x=0$',
                    '  Giá trị cực tiểu của hàm số là $y_{\\text{CT}}=%s$'%(latex(f0-11)),
                    '  Giá trị cực đại của hàm số là $y_{\\text{CĐ}}=%s$'%(latex(f0)),
                    '  Điểm cực đại của đồ thị hàm số là $\\left(0;%s\\right)$'%(latex(f0)),
                    '  Điểm cực tiểu của đồ thị hàm số là $\\left(%s;%s\\right)$ và $\\left(%s;%s\\right)$'%(latex(x1),latex(f1),latex(x2),latex(f2)),
                    '  Hàm số đồng biến trên các khoảng $(%s;0)$ và $(%s;+\\infty)$'%(latex(x1),latex(x2)),
                    '  Hàm số nghịch biến trên các khoảng $(-\\infty;%s)$ và $(0;%s)$'%(latex(x1),latex(x2)),
                    ' Giá trị nhỏ nhất của hàm số trên đoạn $[%s;%s]$ là $%s$'%(latex(a),latex(b),latex(gtln)),
                    ' Giá trị lớn nhất của hàm số trên đoạn $[%s;%s]$ là $%s$'%(latex(a),latex(b),latex(gtnn)),
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
                noidungcauhoi = '''Cho hàm số $y=%s$. \n'''%(latex(f))
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
                        '''Từ bảng biến thiên ta thấy\\\\ \n'''
                        '''\\hspace*{1cm} Hàm số nghịch biến trên các khoảng $(%s;0)$ và $(%s;+\\infty)$. \\\\ \n'''
                        '''\\hspace*{1cm} Hàm số đồng biến trên các khoảng $(-\\infty;%s)$ và $(0;%s)$. \\\\ \n'''
                        '''\\hspace*{1cm} Hàm số đạt cực tiểu tại điểm $x=0$, giá trị cực tiểu là $y_{\\text{CT}}=%s$;\\\\ \n'''
                        '''\\hspace*{1cm} Hàm số đạt cực đại tại điểm $x=\\pm %s$, giá trị cực đại là $y_{\\text{CĐ}}=%s$;\\\\ \n'''
                        'Mặt khác $y(%s)=%s$ và $y(%s)=%s$.\\\\ \n'
                        '''\\hspace*{1cm} Hàm số có giá trị lớn nhất trên đoạn $[%s;%s]$ là $%s$. \\\\ \n'''
                        '''\\hspace*{1cm} Hàm số có giá trị nhỏ nhất trên đoạn $[%s;%s]$ là $%s$. \\\\ \n'''
                        %(latex(daoham),
                        latex(x1),latex(x2),
                        latex(x1),latex(x2),
                        latex(f1),latex(f0),latex(f2),
                        latex(x1),latex(x2),
                        latex(x1),latex(x2),
                        latex(f0),
                        latex(x2),latex(f2),
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

                du = ['\\True Hàm số có ba điểm cực trị',
                    '\\True Hàm số đạt cực tiểu tại các điểm $x=%s$ và $x=%s$'%(latex(x1),latex(x2)),
                    '\\True Hàm số đạt cực đại tại điểm $x=0$',
                    '\\True Giá trị cực tiểu của hàm số là $y_{\\text{CT}}=%s$'%(latex(f2)),
                    '\\True Giá trị cực đại của hàm số là $y_{\\text{CĐ}}=%s$'%(latex(f0)),
                    '\\True Điểm cực đại của đồ thị hàm số là $\\left(0;%s\\right)$'%(latex(f0)),
                    '\\True Điểm cực tiểu của đồ thị hàm số là $\\left(%s;%s\\right)$ và $\\left(%s;%s\\right)$'%(latex(x1),latex(f1),latex(x2),latex(f2)),
                    '\\True Hàm số đồng biến trên các khoảng $(%s;0)$ và $(%s;+\\infty)$'%(latex(x1),latex(x2)),
                    '\\True Hàm số nghịch biến trên các khoảng $(-\\infty;%s)$ và $(0;%s)$'%(latex(x1),latex(x2)),
                    '\\True Giá trị lớn nhất của hàm số trên đoạn $[%s;%s]$ là $%s$'%(latex(a),latex(b),latex(gtln)),
                    '\\True Giá trị nhỏ nhất của hàm số trên đoạn $[%s;%s]$ là $%s$'%(latex(a),latex(b),latex(gtnn)),
                    ]

                da1= random.choice(du)
                du.remove(da1)
                da2= random.choice(du)
                du.remove(da2)
                da3= random.choice(du)
                du.remove(da3)
                da4= random.choice(du)
                s = ['  Hàm số có hai điểm cực trị',
                    '  Hàm số đạt cực đại tại các điểm $x=%s$ và $x=%s$'%(latex(x1),latex(x2)),
                    '  Hàm số đạt cực tiểu tại điểm $x=0$',
                    '  Giá trị cực đại của hàm số là $y_{\\text{CĐ}}=%s$'%(latex(f2)),
                    '  Giá trị cực tiểu của hàm số là $y_{\\text{CT}}=%s$'%(latex(f2-11)),
                    '  Điểm cực tiểu của đồ thị hàm số là $\\left(0;%s\\right)$'%(latex(f0)),
                    '  Điểm cực đại của đồ thị hàm số là $\\left(%s;%s\\right)$ và $\\left(%s;%s\\right)$'%(latex(x1),latex(f1),latex(x2),latex(f2)),
                    '  Hàm số nghịch biến trên các khoảng $(%s;0)$ và $(%s;+\\infty)$'%(latex(x1),latex(x2)),
                    '  Hàm số đồng biến trên các khoảng $(-\\infty;%s)$ và $(0;%s)$'%(latex(x1),latex(x2)),
                    '  Giá trị nhỏ nhất của hàm số trên đoạn $[%s;%s]$ là $%s$'%(latex(a),latex(b),latex(gtln)),
                    '  Giá trị lớn nhất của hàm số trên đoạn $[%s;%s]$ là $%s$'%(latex(a),latex(b),latex(gtnn)),
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
                noidungcauhoi = '''Cho hàm số $y=%s$. \n'''%(latex(f))
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
                        '''Từ bảng biến thiên ta thấy\\\\ \n'''
                        '''\\hspace*{1cm} Hàm số đồng biến trên các khoảng $(%s;0)$ và $(%s;+\\infty)$. \\\\ \n'''
                        '''\\hspace*{1cm} Hàm số nghịch biến trên các khoảng $(-\\infty;%s)$ và $(0;%s)$. \\\\ \n'''
                        '''\\hspace*{1cm} Hàm số đạt cực đại tại điểm $x=0$, giá trị cực đại là $y_{\\text{CĐ}}=%s$;\\\\ \n'''
                        '''\\hspace*{1cm} Hàm số đạt cực tiểu tại điểm $x=\\pm %s$, giá trị cực tiểu là $y_{\\text{CT}}=%s$;\\\\ \n'''
                        'Mặt khác $y(%s)=%s$ và $y(%s)=%s$.\\\\ \n'
                        '''\\hspace*{1cm} Hàm số có giá trị lớn nhất trên đoạn $[%s;%s]$ là $%s$. \\\\ \n'''
                        '''\\hspace*{1cm} Hàm số có giá trị nhỏ nhất trên đoạn $[%s;%s]$ là $%s$.'''
                        %(latex(daoham),
                        latex(x1),latex(x2),
                        latex(x1),latex(x2),
                        latex(f1),latex(f0),latex(f2),
                        latex(x1),latex(x2),
                        latex(x1),latex(x2),
                        latex(f0),
                        latex(x2),latex(f2),
                        latex(a),latex(fa), latex(b),latex(fb),
                        latex(a),latex(b), latex(gtln),
                        latex(a),latex(b), latex(gtnn),

                        ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choiceTFn \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-').replace('1x', 'x').replace('+0x^2', '').replace('+0x', '').replace('+0', '')
            return content


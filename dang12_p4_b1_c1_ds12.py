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


def bt_dang12_p4_b1_c1_ds12(self):
            # Khai báo biến    
            lisdang=['1','2','3','4']
            dang=random.choice(lisdang)
            if dang=='4':
                x = symbols('x')

                x1=randint(-9,-1)
                n=randint(-9,9)
                while x1+n==0:
                    x1=randint(-9,-1)
                    n=randint(-9,9)                
                x2=-2*n-x1
                ##############################
                a = -1
                b=randint(-5,5)
                m=1

                c=(b*n+x1*x2)

                f=(a*x**2+b*x+c)/(x+n)
                daoham=(a*x**2+2*a*n*x+b*n-c)/((m*x+n)**2)
                tu=a*m*x**2+2*a*n*x+b*n-c*m
                x_nho=min(x1,x2)
                x_lon=max(x1,x2)
                f_nho=(a*x_nho**2+b*x_nho+c)/(m*x_nho+n)
                y_nho=Rational(a*x_nho**2+b*x_nho+c,m*x_nho+n)
                f_lon=(a*x_lon**2+b*x_lon+c)/(m*x_lon+n)
                y_lon=Rational(a*x_lon**2+b*x_lon+c,m*x_lon+n)

                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=%s$. Xét tính đơn điệu và tìm cực trị của hàm số.'
                                %(latex(f)
                                    ))

                # Nội dung lời giải
                loigiai=(
                        'Tập xác định $\\mathscr{D}=\\mathbb{R}\\backslash \\left\\{%s\\right\\}$. \\\\ \n' #1
                        'Ta có $y\'=%s$. \\\\ \n' #2
                        '\\hspace*{1cm} $y\'=0 \\Leftrightarrow %s=0 \\Leftrightarrow \\hoac{& x=%s \\\\& x=%s.}$ \\\\ \n' #3
                        '\\hspace*{1cm} $y\'$ không xác định tại $x=%s$. \\\\ \n' #6
                        'Bảng biến thiên \\\\ \n'
                        '\\hspace*{1cm} \\begin{tikzpicture}  \n'
                            '\\tkzTabInit[espcl=3,lgt=1.5]  \n'
                            '{$x$/1,$y\'$/0.7,$y$/2.1}  \n'
                            '{$-\\infty$,$%s$,$%s$,$%s$,$+\\infty$}  \n' #4
                            '\\tkzTabLine{,-,0,+,d,+,0,-,}  \n'
                            '\\tkzTabVar{+/$+\\infty$,-/$%s$,+D-/$+\\infty$/$-\\infty$,+/$%s$,-/$-\\infty$}  \n' #5
                        '\\end{tikzpicture}  \\\\ \n'
                        'Từ bảng biến thiên ta thấy \\\\ \n'
                        '\\hspace*{1cm} Hàm số nghịch biến trên các khoảng $(-\\infty;%s)$ và $(%s;+\\infty)$. \\\\ \n' #7
                        '\\hspace*{1cm} Hàm số đồng biến trên các khoảng $\\left( %s;%s \\right)$ và $\\left( %s;%s \\right)$. \\\\ \n' #8
                        '\\hspace*{1cm} Hàm số đạt cực tiểu tại điểm $x=%s$, giá trị cực tiểu là $y_{CT}=%s$. \\\\ \n' #9
                        '\\hspace*{1cm} Hàm số đạt cực đại tại điểm $x=%s$, giá trị cực đại là $y_{\\text{CĐ}}=%s$.' #10
                        %(latex(-Rational(n,m)), #1
                        latex(daoham),latex(daoham), #2
                        latex(x1),latex(x2), #3
                        latex(-Rational(n,m)), #6
                        latex(x_nho),latex(-Rational(n,m)),latex(x_lon), #4
                        latex(y_nho),latex(y_lon), #5
                        latex(x_nho),latex(x_lon), #7
                        latex(x_nho),latex(-Rational(n,m)),latex(-Rational(n,m)),latex(x_lon), #8
                        latex(x_nho), latex(y_nho), #9
                        latex(x_lon), latex(y_lon) #10
                        ))
            if dang=='3':
                x = symbols('x')

                x1=randint(-9,-1)
                n=randint(-9,9)
                while x1+n==0:
                    x1=randint(-9,-1)
                    n=randint(-9,9)                
                x2=-2*n-x1
                ##############################
                a = -1
                b=randint(-5,5)
                m=1

                c=(b*n+x1*x2)

                f=(a*x**2+b*x+c)/(x+n)
                daoham=(a*x**2+2*a*n*x+b*n-c)/((m*x+n)**2)
                tu=a*m*x**2+2*a*n*x+b*n-c*m
                x_nho=min(x1,x2)
                x_lon=max(x1,x2)
                f_nho=(a*x_nho**2+b*x_nho+c)/(m*x_nho+n)
                y_nho=Rational(a*x_nho**2+b*x_nho+c,m*x_nho+n)
                f_lon=(a*x_lon**2+b*x_lon+c)/(m*x_lon+n)
                y_lon=Rational(a*x_lon**2+b*x_lon+c,m*x_lon+n)

                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=%s$. Xét tính đơn điệu và tìm cực trị của hàm số.  \n'
                                %(latex(f)
                                    ))


                # Nội dung lời giải
                loigiai=(
                        'Tập xác định $\\mathscr{D}=\\mathbb{R}\\backslash \\left\\{%s\\right\\}$. \\\\ \n' #1
                        'Ta có $y\'=%s$. \\\\ \n' #2
                        '\\hspace*{1cm} $y\'=0 \\Leftrightarrow %s=0 \\Leftrightarrow \\hoac{& x=%s \\\\& x=%s.}$ \\\\ \n' #3
                        '\\hspace*{1cm} $y\'$ không xác định tại $x=%s$. \\\\ \n' #6
                        'Bảng biến thiên \\\\ \n'
                        '\\hspace*{1cm} \\begin{tikzpicture}  \n'
                            '\\tkzTabInit[espcl=3,lgt=1.5]  \n'
                            '{$x$/1,$y\'$/0.7,$y$/2.1}  \n'
                            '{$-\\infty$,$%s$,$%s$,$%s$,$+\\infty$}  \n' #4
                            '\\tkzTabLine{,-,0,+,d,+,0,-,}  \n'
                            '\\tkzTabVar{+/$+\\infty$,-/$%s$,+D-/$+\\infty$/$-\\infty$,+/$%s$,-/$-\\infty$}  \n' #5
                        '\\end{tikzpicture}  \\\\ \n'
                        'Từ bảng biến thiên ta thấy \\\\ \n'
                        '\\hspace*{1cm} Hàm số nghịch biến trên các khoảng $(-\\infty;%s)$ và $(%s;+\\infty)$. \\\\ \n' #7
                        '\\hspace*{1cm} Hàm số đồng biến trên các khoảng $\\left( %s;%s \\right)$ và $\\left( %s;%s \\right)$. \\\\ \n' #8
                        '\\hspace*{1cm} Hàm số đạt cực tiểu tại điểm $x=%s$, giá trị cực tiểu là $y_{CT}=%s$. \\\\ \n' #9
                        '\\hspace*{1cm} Hàm số đạt cực đại tại điểm $x=%s$, giá trị cực đại là $y_{\\text{CĐ}}=%s$.' #10
                        %(latex(-Rational(n,m)), #1
                        latex(daoham),latex(daoham), #2
                        latex(x1),latex(x2), #3
                        latex(-Rational(n,m)), #6
                        latex(x_nho),latex(-Rational(n,m)),latex(x_lon), #4
                        latex(y_nho),latex(y_lon), #5
                        latex(x_nho),latex(x_lon), #7
                        latex(x_nho),latex(-Rational(n,m)),latex(-Rational(n,m)),latex(x_lon), #8
                        latex(x_nho), latex(y_nho), #9
                        latex(x_lon), latex(y_lon) #10
                        ))
            if dang=='2':
                x = symbols('x')

                x1=randint(-9,-1)
                n=randint(-9,9)
                while x1+n==0:
                    x1=randint(-9,-1)
                    n=randint(-9,9)                
                x2=-2*n-x1
                ##############################
                a = 1
                b=randint(-5,5)
                m=1

                c=(b*n-x1*x2)

                f=(x**2+b*x+c)/(x+n)
                daoham=(x**2+2*n*x+b*n-c)/((m*x+n)**2)
                tu=a*m*x**2+2*a*n*x+b*n-c*m
                x_nho=min(x1,x2)
                x_lon=max(x1,x2)
                f_nho=(a*x_nho**2+b*x_nho+c)/(m*x_nho+n)
                y_nho=Rational(a*x_nho**2+b*x_nho+c,m*x_nho+n)
                f_lon=(a*x_lon**2+b*x_lon+c)/(m*x_lon+n)
                y_lon=Rational(a*x_lon**2+b*x_lon+c,m*x_lon+n)

                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=%s$. Xét tính đơn điệu và tìm cực trị của hàm số.'
                                %(latex(f)
                                    ))


                # Nội dung lời giải
                loigiai=(
                        'Tập xác định $\\mathscr{D}=\\mathbb{R}\\backslash \\left\\{%s\\right\\}$. \\\\ \n' #1
                        'Ta có $y\'=%s$. \\\\ \n' #2
                        '\\hspace*{1cm} $y\'=0 \\Leftrightarrow %s=0 \\Leftrightarrow \\hoac{& x=%s \\\\& x=%s.}$ \\\\ \n' #3
                        '\\hspace*{1cm} $y\'$ không xác định tại $x=%s$. \\\\ \n' #6
                        'Bảng biến thiên \\\\ \n'
                        '\\hspace*{1cm} \\begin{tikzpicture}  \n'
                            '\\tkzTabInit[espcl=3,lgt=1.5]  \n'
                            '{$x$/1,$y\'$/0.7,$y$/2.1}  \n'
                            '{$-\\infty$,$%s$,$%s$,$%s$,$+\\infty$}  \n' #4
                            '\\tkzTabLine{,+,0,-,d,-,0,+,}  \n'
                            '\\tkzTabVar{-/$-\\infty$,+/$%s$,-D+/$-\\infty$/$+\\infty$,-/$%s$,+/$+\\infty$}  \n' #5
                        '\\end{tikzpicture}  \\\\ \n'
                        'Từ bảng biến thiên ta thấy \\\\ \n'
                        '\\hspace*{1cm} Hàm số đồng biến trên các khoảng $(-\\infty;%s)$ và $(%s;+\\infty)$. \\\\ \n' #7
                        '\\hspace*{1cm} Hàm số nghịch biến trên các khoảng $\\left( %s;%s \\right)$ và $\\left( %s;%s \\right)$. \\\\ \n' #8
                        '\\hspace*{1cm} Hàm số đạt cực đại tại điểm $x=%s$, giá trị cực đại là $y_{\\text{CĐ}}=%s$. \\\\ \n' #9
                        '\\hspace*{1cm} Hàm số đạt cực tiểu tại điểm $x=%s$, giá trị cực tiểu là $y_{CT}=%s$.' #10
                        %(latex(-Rational(n,m)), #1
                        latex(daoham),latex(daoham), #2
                        latex(x1),latex(x2), #3
                        latex(-Rational(n,m)), #6
                        latex(x_nho),latex(-Rational(n,m)),latex(x_lon), #4
                        latex(y_nho),latex(y_lon), #5
                        latex(x_nho),latex(x_lon), #7
                        latex(x_nho),latex(-Rational(n,m)),latex(-Rational(n,m)),latex(x_lon), #8
                        latex(x_nho), latex(y_nho), #9
                        latex(x_lon), latex(y_lon) #10
                        ))
            if dang=='1':
                x = symbols('x')

                x1=randint(-9,-1)
                n=randint(-9,9)
                while x1+n==0:
                    x1=randint(-9,-1)
                    n=randint(-9,9)                
                x2=-2*n-x1
                ##############################
                a = 1
                b=randint(-5,5)
                m=1

                c=(b*n-x1*x2)

                f=(x**2+b*x+c)/(x+n)
                daoham=(x**2+2*n*x+b*n-c)/((m*x+n)**2)
                tu=a*m*x**2+2*a*n*x+b*n-c*m
                x_nho=min(x1,x2)
                x_lon=max(x1,x2)
                f_nho=(a*x_nho**2+b*x_nho+c)/(m*x_nho+n)
                y_nho=Rational(a*x_nho**2+b*x_nho+c,m*x_nho+n)
                f_lon=(a*x_lon**2+b*x_lon+c)/(m*x_lon+n)
                y_lon=Rational(a*x_lon**2+b*x_lon+c,m*x_lon+n)

                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=%s$. Xét tính đơn điệu và tìm cực trị của hàm số.  \n'
                                %(latex(f)
                                    ))


                # Nội dung lời giải
                loigiai=(
                        'Tập xác định $\\mathscr{D}=\\mathbb{R}\\backslash \\left\\{%s\\right\\}$. \\\\ \n' #1
                        'Ta có $y\'=%s$. \\\\ \n' #2
                        '\\hspace*{1cm} $y\'=0 \\Leftrightarrow %s=0 \\Leftrightarrow \\hoac{& x=%s \\\\& x=%s.}$ \\\\ \n' #3
                        '\\hspace*{1cm} $y\'$ không xác định tại $x=%s$. \\\\ \n' #6
                        'Bảng biến thiên \\\\ \n'
                        '\\hspace*{1cm} \\begin{tikzpicture}  \n'
                            '\\tkzTabInit[espcl=3,lgt=1.5]  \n'
                            '{$x$/1,$y\'$/0.7,$y$/2.1}  \n'
                            '{$-\\infty$,$%s$,$%s$,$%s$,$+\\infty$}  \n' #4
                            '\\tkzTabLine{,+,0,-,d,-,0,+,}  \n'
                            '\\tkzTabVar{-/$-\\infty$,+/$%s$,-D+/$-\\infty$/$+\\infty$,-/$%s$,+/$+\\infty$}  \n' #5
                        '\\end{tikzpicture}  \\\\ \n'
                        'Từ bảng biến thiên ta thấy \\\\ \n'
                        '\\hspace*{1cm} Hàm số đồng biến trên các khoảng $(-\\infty;%s)$ và $(%s;+\\infty)$. \\\\ \n' #7
                        '\\hspace*{1cm} Hàm số nghịch biến trên các khoảng $\\left( %s;%s \\right)$ và $\\left( %s;%s \\right)$. \\\\ \n' #8
                        '\\hspace*{1cm} Hàm số đạt cực đại tại điểm $x=%s$, giá trị cực đại là $y_{\\text{CĐ}}=%s$. \\\\ \n' #9
                        '\\hspace*{1cm} Hàm số đạt cực tiểu tại điểm $x=%s$, giá trị cực tiểu là $y_{CT}=%s$.' #10
                        %(latex(-Rational(n,m)), #1
                        latex(daoham),latex(daoham), #2
                        latex(x1),latex(x2), #3
                        latex(-Rational(n,m)), #6
                        latex(x_nho),latex(-Rational(n,m)),latex(x_lon), #4
                        latex(y_nho),latex(y_lon), #5
                        latex(x_nho),latex(x_lon), #7
                        latex(x_nho),latex(-Rational(n,m)),latex(-Rational(n,m)),latex(x_lon), #8
                        latex(x_nho), latex(y_nho), #9
                        latex(x_lon), latex(y_lon) #10
                        ))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+                  
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-').replace('.0', '').replace('1x', 'x')
            return content


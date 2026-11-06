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


def bt_dang9_p1_b1_c1_ds12(self):
            # Khai báo biến
            x = symbols('x')

            # Hàm hỗ trợ ẩn số 0 nếu giá trị bằng 0 để tránh đè lên chữ O gốc tọa độ
            lz = lambda v: "" if v == 0 else latex(v)

            while True:
                x1=randint(-3,-1)
                x2=randint(1,3)

                a = 1
                b=randint(-5,5)
                m=1
                #n=Rational(-x1-x2,2*a)
                n=(-x1-x2)/(2*a)
                #c=Rational(b*n-x1*x2,m)
                c=(b*n-x1*x2)/(m)

                f=(a*x**2+b*x+c)/(m*x+n)
                f1=(a*x1**2+b*x1+c)/(m*x1+n)
                y1=Rational(a*x1**2+b*x1+c,m*x1+n)
                f2=(a*x2**2+b*x2+c)/(m*x2+n)
                y2=Rational(a*x2**2+b*x2+c,m*x2+n)

                tcx=(a/m)*x+b/m-a*n/m**2
                tcd=-n/m


                if -4 <= f1 <= 4 and -4 <= f2 <= 4:
                    break
            while True:
                zx1=randint(-3,-1)
                zx2=randint(1,3)

                za = 1
                zb=randint(-5,5)
                zm=1
                #n=Rational(-x1-x2,2*a)
                zn=(-zx1-zx2)/(2*za)
                #c=Rational(b*n-x1*x2,m)
                zc=(zb*zn-zx1*zx2)/(zm)

                zf=(za*x**2+zb*x+zc)/(zm*x+zn)
                zf1=(za*zx1**2+zb*zx1+zc)/(zm*zx1+zn)
                zy1=Rational(za*zx1**2+zb*zx1+zc,zm*zx1+zn)
                zf2=(za*zx2**2+zb*zx2+zc)/(zm*zx2+zn)
                zy2=Rational(za*zx2**2+zb*zx2+zc,zm*zx2+zn)

                ztcx=(za/zm)*x+zb/zm-za*zn/zm**2
                ztcd=-zn/zm


                if -4 <= zf1 <= 4 and -4 <= zf2 <= 4:
                    break

            lisdang=['1','2','3','4','5','6','7','8']
            dang=random.choice(lisdang)

            if dang=='8':
                #Nội ung câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ có đồ thị như hình vẽ bên. Hàm số đồng biến trên khoảng nào dưới đây?  \n')
                hinhve = (      '\\scalebox{0.6}{ \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,line width=1pt] \n'
                                '\\tikzset{every node/.style={scale=0.9}} \n'
                                '\\draw[->] (-5.1,0)--(5.1,0) node[below left] {$x$}; \n'
                                '\\draw[->] (0,%s)--(0,%s) node[below left] {$y$}; \n' #11
                                '\\draw (0,0) node [below left] {$O$}; \n'
                                '\\draw (%s,0) node [below] {$%s$}; \n' #5
                                '\\draw (0,%s) node [right] {$%s$}; \n' #6
                                '\\draw (%s,0) node [below] {$%s$}; \n' #7
                                '\\draw (0,%s) node [left] {$%s$}; \n' #8
                                '\\draw[dashed,thin](%s,0)--(%s,%s)--(0,%s); \n' #9
                                '\\draw[dashed,thin](%s,0)--(%s,%s)--(0,%s); \n' #10
                                '\\begin{scope} \n'
                                    '\\clip (-5,%s) rectangle (5,%s); \n' #12
                                    '\\draw[samples=200,domain=-5:%s,smooth,variable=\\x] plot (\\x,{-(%s*((\\x)^2)+%s*(\\x)+%s)/(%s*(\\x)+%s)}); \n' #1
                                    '\\draw[samples=200,domain=%s:5,smooth,variable=\\x] plot (\\x,{-(%s*((\\x)^2)+%s*(\\x)+%s)/(%s*(\\x)+%s)}); \n' #2
                                    '\\draw [line width=1.pt,domain=-5:5] plot(\\x,{-%s*\\x-%s}); \n' #3
                                    '\\draw [line width=1.pt] (%s,%s) -- (%s,%s); \n'  #4
                                '\\end{scope}	 \n'
                                '\\draw (%s,0) node [below left] {$%s$}; \n' #13
                            '\\end{tikzpicture} }\n'

                                %(latex(-zf2-2),latex(-zf1+2), #11
                                latex(zx2),lz(zx2), #5
                                latex(zf2),lz(zy2), #6
                                latex(zx1),lz(zx1), #7
                                    latex(zf1),lz(zy1), #8
                                    latex(zx2),latex(zx2),latex(-zf2),latex(-zf2), #9
                                    latex(zx1),latex(zx1),latex(-zf1),latex(-zf1), #10
                                    latex(-zf2-2),latex(-zf1+2), #12
                                    latex(-zn/zm-0.1),latex(za),latex(zb),latex(zc),latex(zm),latex(zn), #1
                                latex(-zn/zm+0.1),latex(za),latex(zb),latex(zc),latex(zm),latex(zn), #2
                                latex(za/zm),latex(zb/zm-za*zn/zm**2), #3
                                latex(-zn/zm),latex(-zf2-2), latex(-zn/zm),latex(-zf1+2), #4
                                latex(-zn/zm),lz(-Rational(zn,zm)), #13

                                ))

                # Các đáp án
                da_d = '\\True $\\left( %s;%s \\right)$' %(latex(-Rational(zn,zm)),latex(zx2))
                da_s1 = '$(-\\infty;%s)$' %(latex(zx2))
                da_s2 = '$(%s;%s)$' %(latex(zx1),latex(zx2))
                da_s3 = '$\\left( %s;+\\infty \\right)$' %(latex(-Rational(zn,zm)))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        'Từ đồ thị ta thấy hàm số đồng biến trên khoảng $\\left( %s;%s \\right)$. \\\\ \n'
                        %(latex(-Rational(zn,zm)),latex(zx2))
                        )

            if dang=='7':
                #Nội ung câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ có đồ thị như hình vẽ bên. Hàm số đồng biến trên khoảng nào dưới đây?  \n')
                hinhve = (      '\\scalebox{0.6}{ \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,line width=1pt] \n'
                                '\\tikzset{every node/.style={scale=0.9}} \n'
                                '\\draw[->] (-5.1,0)--(5.1,0) node[below left] {$x$}; \n'
                                '\\draw[->] (0,%s)--(0,%s) node[below left] {$y$}; \n' #11
                                '\\draw (0,0) node [below left] {$O$}; \n'
                                '\\draw (%s,0) node [below] {$%s$}; \n' #5
                                '\\draw (0,%s) node [right] {$%s$}; \n' #6
                                '\\draw (%s,0) node [below] {$%s$}; \n' #7
                                '\\draw (0,%s) node [left] {$%s$}; \n' #8
                                '\\draw[dashed,thin](%s,0)--(%s,%s)--(0,%s); \n' #9
                                '\\draw[dashed,thin](%s,0)--(%s,%s)--(0,%s); \n' #10
                                '\\begin{scope} \n'
                                    '\\clip (-5,%s) rectangle (5,%s); \n' #12
                                    '\\draw[samples=200,domain=-5:%s,smooth,variable=\\x] plot (\\x,{-(%s*((\\x)^2)+%s*(\\x)+%s)/(%s*(\\x)+%s)}); \n' #1
                                    '\\draw[samples=200,domain=%s:5,smooth,variable=\\x] plot (\\x,{-(%s*((\\x)^2)+%s*(\\x)+%s)/(%s*(\\x)+%s)}); \n' #2
                                    '\\draw [line width=1.pt,domain=-5:5] plot(\\x,{-%s*\\x-%s}); \n' #3
                                    '\\draw [line width=1.pt] (%s,%s) -- (%s,%s); \n'  #4
                                '\\end{scope}	 \n'
                                '\\draw (%s,0) node [below left] {$%s$}; \n' #13
                            '\\end{tikzpicture} } \n'

                                %(latex(-zf2-2),latex(-zf1+2), #11
                                latex(zx2),lz(zx2), #5
                                latex(zf2),lz(zy2), #6
                                latex(zx1),lz(zx1), #7
                                    latex(zf1),lz(zy1), #8
                                    latex(zx2),latex(zx2),latex(-zf2),latex(-zf2), #9
                                    latex(zx1),latex(zx1),latex(-zf1),latex(-zf1), #10
                                    latex(-zf2-2),latex(-zf1+2), #12
                                    latex(-zn/zm-0.1),latex(za),latex(zb),latex(zc),latex(zm),latex(zn), #1
                                latex(-zn/zm+0.1),latex(za),latex(zb),latex(zc),latex(zm),latex(zn), #2
                                latex(za/zm),latex(zb/zm-za*zn/zm**2), #3
                                latex(-zn/zm),latex(-zf2-2), latex(-zn/zm),latex(-zf1+2), #4
                                latex(-zn/zm),lz(-Rational(zn,zm)), #13
                                ))

                # Các đáp án
                da_d = '\\True $\\left( %s;%s \\right)$' %(latex(zx1),latex(-Rational(zn,zm)))
                da_s1 = '$(-\\infty;%s)$' %(latex(zx2))
                da_s2 = '$(%s;%s)$' %(latex(zx1),latex(zx2))
                da_s3 = '$\\left( %s;+\\infty \\right)$' %(latex(-Rational(zn,zm)))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        'Từ đồ thị ta thấy hàm số đồng biến trên khoảng $\\left( %s;%s \\right)$. \\\\ \n'
                        %(latex(zx1),latex(-Rational(zn,zm)))
                        )

            if dang=='6':
                #Nội ung câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ có đồ thị như hình vẽ bên. Hàm số nghịch biến trên khoảng nào dưới đây?  \n')
                hinhve = (      '\\scalebox{0.6}{ \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,line width=1pt] \n'
                                '\\tikzset{every node/.style={scale=0.9}} \n'
                                '\\draw[->] (-5.1,0)--(5.1,0) node[below left] {$x$}; \n'
                                '\\draw[->] (0,%s)--(0,%s) node[below left] {$y$}; \n' #11
                                '\\draw (0,0) node [below left] {$O$}; \n'
                                '\\draw (%s,0) node [below] {$%s$}; \n' #5
                                '\\draw (0,%s) node [right] {$%s$}; \n' #6
                                '\\draw (%s,0) node [below] {$%s$}; \n' #7
                                '\\draw (0,%s) node [left] {$%s$}; \n' #8
                                '\\draw[dashed,thin](%s,0)--(%s,%s)--(0,%s); \n' #9
                                '\\draw[dashed,thin](%s,0)--(%s,%s)--(0,%s); \n' #10
                                '\\begin{scope} \n'
                                    '\\clip (-5,%s) rectangle (5,%s); \n' #12
                                    '\\draw[samples=200,domain=-5:%s,smooth,variable=\\x] plot (\\x,{-(%s*((\\x)^2)+%s*(\\x)+%s)/(%s*(\\x)+%s)}); \n' #1
                                    '\\draw[samples=200,domain=%s:5,smooth,variable=\\x] plot (\\x,{-(%s*((\\x)^2)+%s*(\\x)+%s)/(%s*(\\x)+%s)}); \n' #2
                                    '\\draw [line width=1.pt,domain=-5:5] plot(\\x,{-%s*\\x-%s}); \n' #3
                                    '\\draw [line width=1.pt] (%s,%s) -- (%s,%s); \n'  #4
                                '\\end{scope}	 \n'
                                '\\draw (%s,0) node [below left] {$%s$}; \n' #13
                            '\\end{tikzpicture} } \n'

                                %(latex(-zf2-2),latex(-zf1+2), #11
                                latex(zx2),lz(zx2), #5
                                latex(zf2),lz(zy2), #6
                                latex(zx1),lz(zx1), #7
                                    latex(zf1),lz(zy1), #8
                                    latex(zx2),latex(zx2),latex(-zf2),latex(-zf2), #9
                                    latex(zx1),latex(zx1),latex(-zf1),latex(-zf1), #10
                                    latex(-zf2-2),latex(-zf1+2), #12
                                    latex(-zn/zm-0.1),latex(za),latex(zb),latex(zc),latex(zm),latex(zn), #1
                                latex(-zn/zm+0.1),latex(za),latex(zb),latex(zc),latex(zm),latex(zn), #2
                                latex(za/zm),latex(zb/zm-za*zn/zm**2), #3
                                latex(-zn/zm),latex(-zf2-2), latex(-zn/zm),latex(-zf1+2), #4
                                latex(-zn/zm),lz(-Rational(zn,zm)), #13
                                ))

                # Các đáp án
                da_d = '\\True $(%s;+\\infty)$' %(latex(zx2))
                da_s1 = '$(-\\infty;%s)$' %(latex(zx2))
                da_s2 = '$(%s;%s)$' %(latex(zx1),latex(zx2))
                da_s3 = '$\\left( %s;+\\infty \\right)$' %(latex(-Rational(zn,zm)))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        'Từ đồ thị ta thấy hàm số nghịch biến trên khoảng $(%s;+\\infty)$. \\\\ \n'
                        %(latex(zx2))
                        )

            if dang=='5':
                #Nội ung câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ có đồ thị như hình vẽ bên. Hàm số nghịch biến trên khoảng nào dưới đây?  \n')
                hinhve = (      '\\scalebox{0.6}{ \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,line width=1pt] \n'
                                '\\tikzset{every node/.style={scale=0.9}} \n'
                                '\\draw[->] (-5.1,0)--(5.1,0) node[below left] {$x$}; \n'
                                '\\draw[->] (0,%s)--(0,%s) node[below left] {$y$}; \n' #11
                                '\\draw (0,0) node [below left] {$O$}; \n'
                                '\\draw (%s,0) node [below] {$%s$}; \n' #5
                                '\\draw (0,%s) node [right] {$%s$}; \n' #6
                                '\\draw (%s,0) node [below] {$%s$}; \n' #7
                                '\\draw (0,%s) node [left] {$%s$}; \n' #8
                                '\\draw[dashed,thin](%s,0)--(%s,%s)--(0,%s); \n' #9
                                '\\draw[dashed,thin](%s,0)--(%s,%s)--(0,%s); \n' #10
                                '\\begin{scope} \n'
                                    '\\clip (-5,%s) rectangle (5,%s); \n' #12
                                    '\\draw[samples=200,domain=-5:%s,smooth,variable=\\x] plot (\\x,{-(%s*((\\x)^2)+%s*(\\x)+%s)/(%s*(\\x)+%s)}); \n' #1
                                    '\\draw[samples=200,domain=%s:5,smooth,variable=\\x] plot (\\x,{-(%s*((\\x)^2)+%s*(\\x)+%s)/(%s*(\\x)+%s)}); \n' #2
                                    '\\draw [line width=1.pt,domain=-5:5] plot(\\x,{-%s*\\x-%s}); \n' #3
                                    '\\draw [line width=1.pt] (%s,%s) -- (%s,%s); \n'  #4
                                '\\end{scope}	 \n'
                                '\\draw (%s,0) node [below left] {$%s$}; \n' #13
                            '\\end{tikzpicture} } \n'

                                %(latex(-zf2-2),latex(-zf1+2), #11
                                latex(zx2),lz(zx2), #5
                                latex(zf2),lz(zy2), #6
                                latex(zx1),lz(zx1), #7
                                    latex(zf1),lz(zy1), #8
                                    latex(zx2),latex(zx2),latex(-zf2),latex(-zf2), #9
                                    latex(zx1),latex(zx1),latex(-zf1),latex(-zf1), #10
                                    latex(-zf2-2),latex(-zf1+2), #12
                                    latex(-zn/zm-0.1),latex(za),latex(zb),latex(zc),latex(zm),latex(zn), #1
                                latex(-zn/zm+0.1),latex(za),latex(zb),latex(zc),latex(zm),latex(zn), #2
                                latex(za/zm),latex(zb/zm-za*zn/zm**2), #3
                                latex(-zn/zm),latex(-zf2-2), latex(-zn/zm),latex(-zf1+2), #4
                                latex(-zn/zm),lz(-Rational(zn,zm)), #13
                                ))

                # Các đáp án
                da_d = '\\True $(-\\infty;%s)$' %(latex(zx1))
                da_s1 = '$(-\\infty;%s)$' %(latex(zx2))
                da_s2 = '$(%s;%s)$' %(latex(zx1),latex(zx2))
                da_s3 = '$\\left( %s;+\\infty \\right)$' %(latex(-Rational(zn,zm)))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        'Từ đồ thị ta thấy hàm số nghịch biến trên khoảng $(-\\infty;%s)$. \\\\ \n'
                        %(latex(zx1))
                        )

            if dang=='4':
                #Nội ung câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ có đồ thị như hình vẽ bên. Hàm số nghịch biến trên khoảng nào dưới đây?  \n')
                hinhve = (      '\\scalebox{0.6}{ \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,line width=1pt] \n'
                                '\\tikzset{every node/.style={scale=0.9}} \n'
                                '\\draw[->] (-5.1,0)--(5.1,0) node[below left] {$x$}; \n'
                                '\\draw[->] (0,%s)--(0,%s) node[below left] {$y$}; \n' #11
                                '\\draw (0,0) node [below left] {$O$}; \n'
                                '\\draw (%s,0) node [below] {$%s$}; \n' #5
                                '\\draw (0,%s) node [right] {$%s$}; \n' #6
                                '\\draw (%s,0) node [below] {$%s$}; \n' #7
                                '\\draw (0,%s) node [left] {$%s$}; \n' #8
                                '\\draw[dashed,thin](%s,0)--(%s,%s)--(0,%s); \n' #9
                                '\\draw[dashed,thin](%s,0)--(%s,%s)--(0,%s); \n' #10
                                '\\begin{scope} \n'
                                    '\\clip (-5,%s) rectangle (5,%s); \n' #12
                                    '\\draw[samples=200,domain=-5:%s,smooth,variable=\\x] plot (\\x,{(%s*((\\x)^2)+%s*(\\x)+%s)/(%s*(\\x)+%s)}); \n' #1
                                    '\\draw[samples=200,domain=%s:5,smooth,variable=\\x] plot (\\x,{(%s*((\\x)^2)+%s*(\\x)+%s)/(%s*(\\x)+%s)}); \n' #2
                                    '\\draw [line width=1.pt,domain=-5:5] plot(\\x,{%s*\\x+%s}); \n' #3
                                    '\\draw [line width=1.pt] (%s,%s) -- (%s,%s); \n'  #4
                                '\\end{scope}	 \n'
                                '\\draw (%s,0) node [below left] {$%s$}; \n' #13
                            '\\end{tikzpicture} } \n'

                                %(latex(f1-2),latex(f2+2), #11
                                latex(x2),lz(x2), #5
                                latex(f2),lz(y2), #6
                                latex(x1),lz(x1), #7
                                    latex(f1),lz(y1), #8
                                    latex(x2),latex(x2),latex(f2),latex(f2), #9
                                    latex(x1),latex(x1),latex(f1),latex(f1), #10
                                    latex(f1-2),latex(f2+2), #12
                                    latex(-n/m-0.1),latex(a),latex(b),latex(c),latex(m),latex(n), #1
                                latex(-n/m+0.1),latex(a),latex(b),latex(c),latex(m),latex(n), #2
                                latex(a/m),latex(b/m-a*n/m**2), #3
                                latex(-n/m),latex(f1-2), latex(-n/m),latex(f2+2), #4
                                latex(-n/m),lz(-Rational(n,m)), #13
                                ))

                # Các đáp án
                da_d = '\\True $\\left( %s;%s \\right)$' %(latex(-Rational(n,m)),latex(x2))
                da_s1 = '$(-\\infty;%s)$' %(latex(x2))
                da_s2 = '$(%s;%s)$' %(latex(x1),latex(x2))
                da_s3 = '$\\left( %s;+\\infty \\right)$' %(latex(-Rational(n,m)))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        'Từ đồ thị ta thấy hàm số nghịch biến trên khoảng $\\left( %s;%s \\right)$. \\\\ \n'
                        %(latex(-Rational(n,m)),latex(x2))
                        )

            if dang=='3':
                #Nội ung câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ có đồ thị như hình vẽ bên. Hàm số nghịch biến trên khoảng nào dưới đây?  \n')
                hinhve = (      '\\scalebox{0.6}{ \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,line width=1pt] \n'
                                '\\tikzset{every node/.style={scale=0.9}} \n'
                                '\\draw[->] (-5.1,0)--(5.1,0) node[below left] {$x$}; \n'
                                '\\draw[->] (0,%s)--(0,%s) node[below left] {$y$}; \n' #11
                                '\\draw (0,0) node [below left] {$O$}; \n'
                                '\\draw (%s,0) node [below] {$%s$}; \n' #5
                                '\\draw (0,%s) node [right] {$%s$}; \n' #6
                                '\\draw (%s,0) node [below] {$%s$}; \n' #7
                                '\\draw (0,%s) node [left] {$%s$}; \n' #8
                                '\\draw[dashed,thin](%s,0)--(%s,%s)--(0,%s); \n' #9
                                '\\draw[dashed,thin](%s,0)--(%s,%s)--(0,%s); \n' #10
                                '\\begin{scope} \n'
                                    '\\clip (-5,%s) rectangle (5,%s); \n' #12
                                    '\\draw[samples=200,domain=-5:%s,smooth,variable=\\x] plot (\\x,{(%s*((\\x)^2)+%s*(\\x)+%s)/(%s*(\\x)+%s)}); \n' #1
                                    '\\draw[samples=200,domain=%s:5,smooth,variable=\\x] plot (\\x,{(%s*((\\x)^2)+%s*(\\x)+%s)/(%s*(\\x)+%s)}); \n' #2
                                    '\\draw [line width=1.pt,domain=-5:5] plot(\\x,{%s*\\x+%s}); \n' #3
                                    '\\draw [line width=1.pt] (%s,%s) -- (%s,%s); \n'  #4
                                '\\end{scope}	 \n'
                                '\\draw (%s,0) node [below left] {$%s$}; \n' #13
                            '\\end{tikzpicture} } \n'

                                %(latex(f1-2),latex(f2+2), #11
                                latex(x2),lz(x2), #5
                                latex(f2),lz(y2), #6
                                latex(x1),lz(x1), #7
                                    latex(f1),lz(y1), #8
                                    latex(x2),latex(x2),latex(f2),latex(f2), #9
                                    latex(x1),latex(x1),latex(f1),latex(f1), #10
                                    latex(f1-2),latex(f2+2), #12
                                    latex(-n/m-0.1),latex(a),latex(b),latex(c),latex(m),latex(n), #1
                                latex(-n/m+0.1),latex(a),latex(b),latex(c),latex(m),latex(n), #2
                                latex(a/m),latex(b/m-a*n/m**2), #3
                                latex(-n/m),latex(f1-2), latex(-n/m),latex(f2+2), #4
                                latex(-n/m),lz(-Rational(n,m)), #13
                                ))

                # Các đáp án
                da_d = '\\True $\\left( %s;%s \\right)$' %(latex(x1),latex(-Rational(n,m)))
                da_s1 = '$(-\\infty;%s)$' %(latex(x2))
                da_s2 = '$(%s;%s)$' %(latex(x1),latex(x2))
                da_s3 = '$\\left( %s;+\\infty \\right)$' %(latex(-Rational(n,m)))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        'Từ đồ thị ta thấy hàm số nghịch biến trên khoảng $\\left( %s;%s \\right)$. \\\\ \n'
                        %(latex(x1),latex(-Rational(n,m)))
                        )

            if dang=='2':
                #Nội ung câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ có đồ thị như hình vẽ bên. Hàm số đồng biến trên khoảng nào dưới đây?  \n')
                hinhve = (      '\\scalebox{0.6}{ \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,line width=1pt] \n'
                                '\\tikzset{every node/.style={scale=0.9}} \n'
                                '\\draw[->] (-5.1,0)--(5.1,0) node[below left] {$x$}; \n'
                                '\\draw[->] (0,%s)--(0,%s) node[below left] {$y$}; \n' #11
                                '\\draw (0,0) node [below left] {$O$}; \n'
                                '\\draw (%s,0) node [below] {$%s$}; \n' #5
                                '\\draw (0,%s) node [right] {$%s$}; \n' #6
                                '\\draw (%s,0) node [below] {$%s$}; \n' #7
                                '\\draw (0,%s) node [left] {$%s$}; \n' #8
                                '\\draw[dashed,thin](%s,0)--(%s,%s)--(0,%s); \n' #9
                                '\\draw[dashed,thin](%s,0)--(%s,%s)--(0,%s); \n' #10
                                '\\begin{scope} \n'
                                    '\\clip (-5,%s) rectangle (5,%s); \n' #12
                                    '\\draw[samples=200,domain=-5:%s,smooth,variable=\\x] plot (\\x,{(%s*((\\x)^2)+%s*(\\x)+%s)/(%s*(\\x)+%s)}); \n' #1
                                    '\\draw[samples=200,domain=%s:5,smooth,variable=\\x] plot (\\x,{(%s*((\\x)^2)+%s*(\\x)+%s)/(%s*(\\x)+%s)}); \n' #2
                                    '\\draw [line width=1.pt,domain=-5:5] plot(\\x,{%s*\\x+%s}); \n' #3
                                    '\\draw [line width=1.pt] (%s,%s) -- (%s,%s); \n'  #4
                                '\\end{scope}	 \n'
                                '\\draw (%s,0) node [below left] {$%s$}; \n' #13
                            '\\end{tikzpicture} } \n'

                                %(latex(f1-2),latex(f2+2), #11
                                latex(x2),lz(x2), #5
                                latex(f2),lz(y2), #6
                                latex(x1),lz(x1), #7
                                    latex(f1),lz(y1), #8
                                    latex(x2),latex(x2),latex(f2),latex(f2), #9
                                    latex(x1),latex(x1),latex(f1),latex(f1), #10
                                    latex(f1-2),latex(f2+2), #12
                                    latex(-n/m-0.1),latex(a),latex(b),latex(c),latex(m),latex(n), #1
                                latex(-n/m+0.1),latex(a),latex(b),latex(c),latex(m),latex(n), #2
                                latex(a/m),latex(b/m-a*n/m**2), #3
                                latex(-n/m),latex(f1-2), latex(-n/m),latex(f2+2), #4
                                latex(-n/m),lz(-Rational(n,m)), #13
                                ))

                # Các đáp án
                da_d = '\\True $(%s;+\\infty)$' %(latex(x2))
                da_s1 = '$(-\\infty;%s)$' %(latex(x2))
                da_s2 = '$(%s;%s)$' %(latex(x1),latex(x2))
                da_s3 = '$\\left( %s;+\\infty \\right)$' %(latex(-Rational(n,m)))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        'Từ đồ thị ta thấy hàm số đồng biến trên khoảng $(%s;+\\infty)$. \\\\ \n'
                        %(latex(x2))
                        )

            if dang=='1':
                #Nội ung câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ có đồ thị như hình vẽ bên. Hàm số đồng biến trên khoảng nào dưới đây?  \n')
                hinhve = (      '\\scalebox{0.6}{ \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,line width=1pt] \n'
                                '\\tikzset{every node/.style={scale=0.9}} \n'
                                '\\draw[->] (-5.1,0)--(5.1,0) node[below left] {$x$}; \n'
                                '\\draw[->] (0,%s)--(0,%s) node[below left] {$y$}; \n' #11
                                '\\draw (0,0) node [below left] {$O$}; \n'
                                '\\draw (%s,0) node [below] {$%s$}; \n' #5
                                '\\draw (0,%s) node [right] {$%s$}; \n' #6
                                '\\draw (%s,0) node [below] {$%s$}; \n' #7
                                '\\draw (0,%s) node [left] {$%s$}; \n' #8
                                '\\draw[dashed,thin](%s,0)--(%s,%s)--(0,%s); \n' #9
                                '\\draw[dashed,thin](%s,0)--(%s,%s)--(0,%s); \n' #10
                                '\\begin{scope} \n'
                                    '\\clip (-5,%s) rectangle (5,%s); \n' #12
                                    '\\draw[samples=200,domain=-5:%s,smooth,variable=\\x] plot (\\x,{(%s*((\\x)^2)+%s*(\\x)+%s)/(%s*(\\x)+%s)}); \n' #1
                                    '\\draw[samples=200,domain=%s:5,smooth,variable=\\x] plot (\\x,{(%s*((\\x)^2)+%s*(\\x)+%s)/(%s*(\\x)+%s)}); \n' #2
                                    '\\draw [line width=1.pt,domain=-5:5] plot(\\x,{%s*\\x+%s}); \n' #3
                                    '\\draw [line width=1.pt] (%s,%s) -- (%s,%s); \n'  #4
                                '\\end{scope}	 \n'
                                '\\draw (%s,0) node [below left] {$%s$}; \n' #13
                            '\\end{tikzpicture} } \n'

                                %(latex(f1-2),latex(f2+2), #11
                                latex(x2),lz(x2), #5
                                latex(f2),lz(y2), #6
                                latex(x1),lz(x1), #7
                                    latex(f1),lz(y1), #8
                                    latex(x2),latex(x2),latex(f2),latex(f2), #9
                                    latex(x1),latex(x1),latex(f1),latex(f1), #10
                                    latex(f1-2),latex(f2+2), #12
                                    latex(-n/m-0.1),latex(a),latex(b),latex(c),latex(m),latex(n), #1
                                latex(-n/m+0.1),latex(a),latex(b),latex(c),latex(m),latex(n), #2
                                latex(a/m),latex(b/m-a*n/m**2), #3
                                latex(-n/m),latex(f1-2), latex(-n/m),latex(f2+2), #4
                                latex(-n/m),lz(-Rational(n,m)), #13
                                ))

                # Các đáp án
                da_d = '\\True $(-\\infty;%s)$' %(latex(x1))
                da_s1 = '$(-\\infty;%s)$' %(latex(x2))
                da_s2 = '$(%s;%s)$' %(latex(x1),latex(x2))
                da_s3 = '$\\left( %s;+\\infty \\right)$' %(latex(-Rational(n,m)))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        'Từ đồ thị ta thấy hàm số đồng biến trên khoảng $(-\\infty;%s)$. \\\\ \n'
                        %(latex(x1))
                        )


            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n \\immini{'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n }{'+hinhve+ '} \n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} ').replace('\\frac', '\\dfrac')
            return content


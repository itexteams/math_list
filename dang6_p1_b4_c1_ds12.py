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


def bt_dang6_p1_b4_c1_ds12(self):
            # Khai báo biến
            x = symbols('x')
            while True:
                x1=randint(-9,-1)
                n=randint(-9,-1)
                while x1+n==0:
                    x1=randint(-9,-1)
                    n=randint(-9,-1)                
                x2=-2*n-x1

                a = 1
                b=randint(-5,5)
                m=1

                c=(b*n-x1*x2)

                f=(a*x**2+b*x+c)/(m*x+n)
                f1=(a*x1**2+b*x1+c)/(m*x1+n)
                y1=Rational(a*x1**2+b*x1+c,m*x1+n)
                f2=(a*x2**2+b*x2+c)/(m*x2+n)
                y2=Rational(a*x2**2+b*x2+c,m*x2+n)                    
                tcx=Rational(a,m)*x+b/m-a*n/m**2
                tcd=-n/m
                if -4 <= f1 <= 4 and -4 <= f2 <= 4:
                    break
            while True:
                zx1=randint(-3,-1)
                zx2=randint(1,3)
                while (zx1+zx2)%2!=0:
                    zx1=randint(-3,-1)
                    zx2=randint(1,3)

                za = -1
                zb=randint(-5,5)
                zm=1
                #n=Rational(-x1-x2,2*a)
                zn=(zx1+zx2)/(-2)
                #c=Rational(b*n-x1*x2,m)
                zc=(zb*zn+zx1*zx2)/(zm)

                zf=(za*x**2+zb*x+zc)/(zm*x+zn)
                zf1=(za*zx1**2+zb*zx1+zc)/(zm*zx1+zn)
                zy1=Rational(za*zx1**2+zb*zx1+zc,zm*zx1+zn)
                zf2=(za*zx2**2+zb*zx2+zc)/(zm*zx2+zn)
                zy2=Rational(za*zx2**2+zb*zx2+zc,zm*zx2+zn)

                ztcx=(za/zm)*x+zb/zm-za*zn/zm**2
                ztcd=-zn/zm


                if -4 <= zf1 <= 4 and -4 <= zf2 <= 4:
                    break

            lisdang=['1','2']
            dang=random.choice(lisdang)

            if dang=='2':
                #Nội ung câu hỏi
                noidungcauhoi = ('Hình vẽ bên là đồ thị của hàm số nào dưới đây?  \n')
                hinhve = (      '\\scalebox{0.5}{ \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] \n'
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

                                %(latex(zf2-2),latex(zf1+2), #11
                                latex(zx2),latex(zx2), #5
                                latex(zf2),latex(zy2), #6
                                latex(zx1),latex(zx1), #7
                                latex(zf1),latex(zy1), #8
                                latex(zx2),latex(zx2),latex(zf2),latex(zf2), #9
                                latex(zx1),latex(zx1),latex(zf1),latex(zf1), #10
                                latex(zf2-2),latex(zf1+2), #12
                                latex(-zn/zm-0.1),latex(za),latex(zb),latex(zc),latex(zm),latex(zn), #1
                                latex(-zn/zm+0.1),latex(za),latex(zb),latex(zc),latex(zm),latex(zn), #2
                                latex(za/zm),latex(zb/zm-za*zn/zm**2), #3
                                latex(-zn/zm),latex(zf2-2), latex(-zn/zm),latex(zf1+2), #4
                                latex(-zn/zm),latex(-Rational(zn,zm)), #13

                                )) 
                # Các đáp án
                da_d = '\\True $y=%s$' %(latex(zf))
                da_s1 = '$y=%s$' %(latex((za*x**2+zb*x-zc)/(zm*x-zn)))
                da_s2 = '$y=%s$' %(latex((za*x+zb)/(zm*x+zn)))
                da_s3 = '$y=%s$' %(latex((za*x+zb+1)/(zm*x-zn)))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        'Từ hình vẽ ta thấy \\\\ \n'
                        '\\hspace*{1cm} Hình vẽ là đồ thị hàm phân thức bậc hai trên bậc nhất. \\\\ \n'
                        '\\hspace*{1cm} Đồ thị hàm số có tiệm cận đứng là $x=%s$. \\\\ \n'
                        '\\hspace*{1cm} Đồ thị hàm số có tiệm cận xiên là $y=%s$. '
                        %(latex(ztcd),latex(ztcx)
                            ))
            if dang=='1':
                #Nội ung câu hỏi
                noidungcauhoi = ('Hình vẽ bên là đồ thị của hàm số nào dưới đây?  \n')
                hinhve = (      '\\scalebox{0.6}{ \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] \n'
                                '\\tikzset{every node/.style={scale=0.9}} \n'
                                '\\draw[->] (-5.1,0)--(5.1,0) node[below left] {$x$}; \n'
                                '\\draw[->] (0,%s)--(0,%s) node[below left] {$y$}; \n' #11
                                '\\draw (0,0) node [below left] {$O$}; \n'
                                '\\draw (%s,0) node [below] {$%s$}; \n' #5
                                '\\draw (0,%s) node [left] {$%s$}; \n' #6
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
                                latex(x2),latex(x2), #5
                                latex(f2),latex(y2), #6
                                latex(x1),latex(x1), #7
                                    latex(f1),latex(y1), #8
                                    latex(x2),latex(x2),latex(f2),latex(f2), #9
                                    latex(x1),latex(x1),latex(f1),latex(f1), #10
                                    latex(f1-2),latex(f2+2), #12
                                    latex(-n/m-0.1),latex(a),latex(b),latex(c),latex(m),latex(n), #1
                                latex(-n/m+0.1),latex(a),latex(b),latex(c),latex(m),latex(n), #2
                                latex(a/m),latex(b/m-a*n/m**2), #3
                                latex(-n/m),latex(f1-2), latex(-n/m),latex(f2+2), #4
                                latex(-n/m),latex(-Rational(n,m)), #13
                                ))                    
                # Các đáp án
                da_d = '\\True $y=%s$' %(latex(f))
                da_s1 = '$y=%s$' %(latex((a*x**2+b*x-c)/(m*x-n)))
                da_s2 = '$y=%s$' %(latex((a*x+b)/(m*x+n)))
                da_s3 = '$y=%s$' %(latex((a*x+b+1)/(m*x-n)))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        'Từ hình vẽ ta thấy \\\\ \n'
                        '\\hspace*{1cm} Hình vẽ là đồ thị hàm phân thức bậc hai trên bậc nhất. \\\\ \n'
                        '\\hspace*{1cm} Đồ thị hàm số có tiệm cận đứng là $x=%s$. \\\\ \n'
                        '\\hspace*{1cm} Đồ thị hàm số có tiệm cận xiên là $y=%s$. '
                        %(latex(tcd),latex(tcx)
                            ))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n \\immini{'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n }{'+hinhve+ '} \n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.0', '')      
            return content


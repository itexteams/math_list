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


def bt_dang26_p1_b1_c1_ds12(self):
            # Khai báo biến
            x = symbols('x')
            x2=randint(-1,1)
            i1=randint(1,2)
            x1=x2-i1
            i2=randint(1,2)
            x3=x2+i2
            a=1
            b=-x1-x2-x3
            c=x1*x2+x2*x3+x1*x3
            e=-x1*x2*x3

            f=a*x**3+b*x**2+c*x+e
            n1=(x1+x2)/2
            n2=(x2+x3)/2
            f1=a*n1**3+b*n1**2+c*n1+e
            f2=a*n2**3+b*n2**2+c*n2+e
            lisdang=['1','2','3','4','5','6','7','8']
            dang=random.choice(lisdang)
            if dang=='8':
                d = ['$2$',
                    ]
                da= random.choice(d)
                s = ['$0$',
                    '$1$',
                    '$3$',
                    '$4$',
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ có đồ thị của đạo hàm $f\'(x)$ như hình vẽ bên. Số điểm cực đại của hàm số là   \n'
                                )
                hinhve = (      '\\scalebox{0.7}{ \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,line width=1pt]  \n'
                                '\\tikzset{every node/.style={scale=0.9}} \n'
                                '\\draw[->] (%s-2.1,0)--(%s+2.1,0) node[below left] {$x$}; \n' #3
                                '\\draw[->] (0,-4.1)--(0,4.1) node[below left] {$y$}; \n' #4
                                '\\draw (0,0) node [below left] {$O$}; \n'
                                '\\foreach \\x/\\nx in {%s/%s,%s/%s,%s/%s} { \n'  #1
                                    '\\ifnum \\x=0 \n'
                                        '\\draw[thin] (\\x,1pt)--(\\x,-1pt); \n'
                                    '\\else \n'
                                        '\\draw[thin] (\\x,1pt)--(\\x,-1pt) node [below] {$\\nx$}; \n'
                                    '\\fi \n'
                                '} \n'
                                '\\begin{scope} \n'
                                '\\clip (%s-2.1,-4.1) rectangle (%s+2.1,4.1); \n'  #5
                                '\\draw[samples=200,domain=-5:5,smooth,variable=\\x] plot (\\x,{%s*((\\x)^3)+%s*((\\x)^2)+%s*(\\x)+%s}); \n' #2
                                '\\end{scope} \n'
                                '\\end{tikzpicture} }\n'

                                %(latex(x1),latex(x3), #3
                                #latex(f1),latex(f2), #4
                                latex(x1),latex(x1), latex(x2),latex(x2),latex(x3),latex(x3), #1
                                latex(x1),latex(x3), #5
                                latex(-a),latex(-b),latex(-c),latex(-e), #2
                                )) 
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
                        'Từ đồ thị ta có \\\\ \n'
                        '\\hspace*{1cm} $f\'(x)=0 \\Leftrightarrow \\hoac{& x=%s \\\\& x=%s \\\\& x=%s.}$ \\\\ \n'
                        'Bảng xét dấu \\\\ \n'
                        '\\hspace*{1cm} \\begin{tikzpicture} \n'
                        '\\tkzTabInit[deltacl=0.5,espcl=2.5,lgt=2]  \n'
                        '{$x$/1,$y\'$/1}  \n'
                        '{$-\\infty$,$%s$,$%s$,$%s$,$+\\infty$}  \n'
                        '\\tkzTabLine{,+,0,-,0,+,0,-,}  \n'
                        '\\end{tikzpicture}  \\\\ \n'
                        'Từ bảng xét dấu ta thấy số điểm cực đại của hàm số là $2$. \\\\ \n'
                        %(latex(x1),latex(x2),latex(x3),
                        latex(x1),latex(x2),latex(x3),
                        ))
            if dang=='7':
                d = ['$x=%s$ và $x=%s$'%(latex(x1),latex(x3)),
                    ]
                da= random.choice(d)
                s = ['$x=%s$ và $x=%s$'%(latex(x1),latex(x2)),
                    '$x=%s$ và $x=%s$'%(latex(x2),latex(x3)),
                    '$y=%s$ và $y=%s$'%(latex(x1),latex(x3)),
                    '$y=%s$ và $y=%s$'%(latex(x1),latex(x2)),
                    '$y=%s$ và $y=%s$'%(latex(x2),latex(x3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ có đồ thị của đạo hàm $f\'(x)$ như hình vẽ bên. Điểm cực đại của hàm số là   \n'
                                )
                hinhve = (      '\\scalebox{0.7}{  \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,line width=1pt]  \n'
                                '\\tikzset{every node/.style={scale=0.9}} \n'
                                '\\draw[->] (%s-2.1,0)--(%s+2.1,0) node[below left] {$x$}; \n' #3
                                '\\draw[->] (0,-4.1)--(0,4.1) node[below left] {$y$}; \n' #4
                                '\\draw (0,0) node [below left] {$O$}; \n'
                                '\\foreach \\x/\\nx in {%s/%s,%s/%s,%s/%s} { \n'  #1
                                    '\\ifnum \\x=0 \n'
                                        '\\draw[thin] (\\x,1pt)--(\\x,-1pt); \n'
                                    '\\else \n'
                                        '\\draw[thin] (\\x,1pt)--(\\x,-1pt) node [below] {$\\nx$}; \n'
                                    '\\fi \n'
                                '} \n'
                                '\\begin{scope} \n'
                                '\\clip (%s-2.1,-4.1) rectangle (%s+2.1,4.1); \n'  #5
                                '\\draw[samples=200,domain=-5:5,smooth,variable=\\x] plot (\\x,{%s*((\\x)^3)+%s*((\\x)^2)+%s*(\\x)+%s}); \n' #2
                                '\\end{scope} \n'
                                '\\end{tikzpicture} } \n'

                                %(latex(x1),latex(x3), #3
                                #latex(f1),latex(f2), #4
                                latex(x1),latex(x1), latex(x2),latex(x2),latex(x3),latex(x3), #1
                                latex(x1),latex(x3), #5
                                latex(-a),latex(-b),latex(-c),latex(-e), #2
                                )) 
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
                        'Từ đồ thị ta có \\\\ \n'
                        '\\hspace*{1cm} $f\'(x)=0 \\Leftrightarrow \\hoac{& x=%s \\\\& x=%s \\\\& x=%s.}$ \\\\ \n'
                        'Bảng xét dấu \\\\ \n'
                        '\\hspace*{1cm} \\begin{tikzpicture} \n'
                        '\\tkzTabInit[deltacl=0.5,espcl=2.5,lgt=2]  \n'
                        '{$x$/1,$y\'$/1}  \n'
                        '{$-\\infty$,$%s$,$%s$,$%s$,$+\\infty$}  \n'
                        '\\tkzTabLine{,+,0,-,0,+,0,-,}  \n'
                        '\\end{tikzpicture}  \\\\ \n'
                        'Từ bảng xét dấu ta thấy điểm cực đại của hàm số là $x=%s$ và $x=%s$. \\\\ \n'
                        %(latex(x1),latex(x2),latex(x3),
                        latex(x1),latex(x2),latex(x3),
                        latex(x1),latex(x3)
                        ))
            if dang=='6':
                d = ['$x=%s$'%(latex(x2)),
                    ]
                da= random.choice(d)
                s = ['$x=%s$'%(latex(x1)),
                    '$x=%s$'%(latex(x3)),
                    '$y=%s$'%(latex(x1)),
                    '$y=%s$'%(latex(x3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ có đồ thị của đạo hàm $f\'(x)$ như hình vẽ bên. Điểm cực tiểu của hàm số là  \n'
                                )
                hinhve = (      '\\scalebox{0.7}{ \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,line width=1pt]  \n'
                                '\\tikzset{every node/.style={scale=0.9}} \n'
                                '\\draw[->] (%s-2.1,0)--(%s+2.1,0) node[below left] {$x$}; \n' #3
                                '\\draw[->] (0,-4.1)--(0,4.1) node[below left] {$y$}; \n' #4
                                '\\draw (0,0) node [below left] {$O$}; \n'
                                '\\foreach \\x/\\nx in {%s/%s,%s/%s,%s/%s} { \n'  #1
                                    '\\ifnum \\x=0 \n'
                                        '\\draw[thin] (\\x,1pt)--(\\x,-1pt); \n'
                                    '\\else \n'
                                        '\\draw[thin] (\\x,1pt)--(\\x,-1pt) node [below] {$\\nx$}; \n'
                                    '\\fi \n'
                                '} \n'
                                '\\begin{scope} \n'
                                '\\clip (%s-2.1,-4.1) rectangle (%s+2.1,4.1); \n'  #5
                                '\\draw[samples=200,domain=-5:5,smooth,variable=\\x] plot (\\x,{%s*((\\x)^3)+%s*((\\x)^2)+%s*(\\x)+%s}); \n' #2
                                '\\end{scope} \n'
                                '\\end{tikzpicture} }\n'

                                %(latex(x1),latex(x3), #3
                                #latex(f1),latex(f2), #4
                                latex(x1),latex(x1), latex(x2),latex(x2),latex(x3),latex(x3), #1
                                latex(x1),latex(x3), #5
                                latex(-a),latex(-b),latex(-c),latex(-e), #2
                                )) 
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
                        'Từ đồ thị ta có \\\\ \n'
                        '\\hspace*{1cm} $f\'(x)=0 \\Leftrightarrow \\hoac{& x=%s \\\\& x=%s \\\\& x=%s.}$ \\\\ \n'
                        'Bảng xét dấu \\\\ \n'
                        '\\hspace*{1cm} \\begin{tikzpicture} \n'
                        '\\tkzTabInit[deltacl=0.5,espcl=2.5,lgt=2]  \n'
                        '{$x$/1,$y\'$/1}  \n'
                        '{$-\\infty$,$%s$,$%s$,$%s$,$+\\infty$}  \n'
                        '\\tkzTabLine{,+,0,-,0,+,0,-,}  \n'
                        '\\end{tikzpicture}  \\\\ \n'
                        'Từ bảng xét dấu ta thấy điểm cực tiểu của hàm số là $x=%s$. \\\\ \n'
                        %(latex(x1),latex(x2),latex(x3),
                        latex(x1),latex(x2),latex(x3),
                        latex(x2)
                        ))
            if dang=='5':
                d = ['$3$',
                    ]
                da= random.choice(d)
                s = ['$0$',
                    '$1$',
                    '$2$',
                    '$4$',
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ có đồ thị của đạo hàm $f\'(x)$ như hình vẽ bên. Số điểm cực trị của hàm số là   \n'
                                )
                hinhve = (      '\\scalebox{0.7}{ \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,line width=1pt]  \n'
                                '\\tikzset{every node/.style={scale=0.9}} \n'
                                '\\draw[->] (%s-2.1,0)--(%s+2.1,0) node[below left] {$x$}; \n' #3
                                '\\draw[->] (0,-4.1)--(0,4.1) node[below left] {$y$}; \n' #4
                                '\\draw (0,0) node [below left] {$O$}; \n'
                                '\\foreach \\x/\\nx in {%s/%s,%s/%s,%s/%s} { \n'  #1
                                    '\\ifnum \\x=0 \n'
                                        '\\draw[thin] (\\x,1pt)--(\\x,-1pt); \n'
                                    '\\else \n'
                                        '\\draw[thin] (\\x,1pt)--(\\x,-1pt) node [below] {$\\nx$}; \n'
                                    '\\fi \n'
                                '} \n'
                                '\\begin{scope} \n'
                                '\\clip (%s-2.1,-4.1) rectangle (%s+2.1,4.1); \n'  #5
                                '\\draw[samples=200,domain=-5:5,smooth,variable=\\x] plot (\\x,{%s*((\\x)^3)+%s*((\\x)^2)+%s*(\\x)+%s}); \n' #2
                                '\\end{scope} \n'
                                '\\end{tikzpicture} }\n'

                                %(latex(x1),latex(x3), #3
                                #latex(f1),latex(f2), #4
                                latex(x1),latex(x1), latex(x2),latex(x2),latex(x3),latex(x3), #1
                                latex(x1),latex(x3), #5
                                latex(-a),latex(-b),latex(-c),latex(-e), #2
                                ))  
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
                        'Từ đồ thị ta có \\\\ \n'
                        '\\hspace*{1cm} $f\'(x)=0 \\Leftrightarrow \\hoac{& x=%s \\\\& x=%s \\\\& x=%s.}$ \\\\ \n'
                        'Bảng xét dấu \\\\ \n'
                        '\\hspace*{1cm} \\begin{tikzpicture} \n'
                        '\\tkzTabInit[deltacl=0.5,espcl=2.5,lgt=2]  \n'
                        '{$x$/1,$y\'$/1}  \n'
                        '{$-\\infty$,$%s$,$%s$,$%s$,$+\\infty$}  \n'
                        '\\tkzTabLine{,+,0,-,0,+,0,-,}  \n'
                        '\\end{tikzpicture}  \\\\ \n'
                        'Từ bảng xét dấu ta thấy số điểm cực trị của hàm số là $3$. \\\\ \n'
                        %(latex(x1),latex(x2),latex(x3),
                        latex(x1),latex(x2),latex(x3),
                        ))
            if dang=='4':
                d = ['$2$',
                    ]
                da= random.choice(d)
                s = ['$0$',
                    '$1$',
                    '$3$',
                    '$4$',
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ có đồ thị của đạo hàm $f\'(x)$ như hình vẽ bên. Số điểm cực tiểu của hàm số là   \n'
                                )
                hinhve = (      '\\scalebox{0.7}{  \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,line width=1pt]  \n'
                                '\\tikzset{every node/.style={scale=0.9}} \n'
                                '\\draw[->] (%s-2.1,0)--(%s+2.1,0) node[below left] {$x$}; \n' #3
                                '\\draw[->] (0,-4.1)--(0,4.1) node[below left] {$y$}; \n' #4
                                '\\draw (0,0) node [below left] {$O$}; \n'
                                '\\foreach \\x/\\nx in {%s/%s,%s/%s,%s/%s} { \n'  #1
                                    '\\ifnum \\x=0 \n'
                                        '\\draw[thin] (\\x,1pt)--(\\x,-1pt); \n'
                                    '\\else \n'
                                        '\\draw[thin] (\\x,1pt)--(\\x,-1pt) node [below] {$\\nx$}; \n'
                                    '\\fi \n'
                                '} \n'
                                '\\begin{scope} \n'
                                '\\clip (%s-2.1,-4.1) rectangle (%s+2.1,4.1); \n'  #5
                                '\\draw[samples=200,domain=-5:5,smooth,variable=\\x] plot (\\x,{%s*((\\x)^3)+%s*((\\x)^2)+%s*(\\x)+%s}); \n' #2
                                '\\end{scope} \n'
                                '\\end{tikzpicture} }\n'

                                %(latex(x1),latex(x3), #3
                                #latex(f1),latex(f2), #4
                                latex(x1),latex(x1), latex(x2),latex(x2),latex(x3),latex(x3), #1
                                latex(x1),latex(x3), #5
                                latex(a),latex(b),latex(c),latex(e), #2
                                )) 
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
                        'Từ đồ thị ta có \\\\ \n'
                        '\\hspace*{1cm} $f\'(x)=0 \\Leftrightarrow \\hoac{& x=%s \\\\& x=%s \\\\& x=%s.}$ \\\\ \n'
                        'Bảng xét dấu \\\\ \n'
                        '\\hspace*{1cm} \\begin{tikzpicture} \n'
                        '\\tkzTabInit[deltacl=0.5,espcl=2.5,lgt=2]  \n'
                        '{$x$/1,$y\'$/1}  \n'
                        '{$-\\infty$,$%s$,$%s$,$%s$,$+\\infty$}  \n'
                        '\\tkzTabLine{,-,0,+,0,-,0,+,}  \n'
                        '\\end{tikzpicture}  \\\\ \n'
                        'Từ bảng xét dấu ta thấy số điểm cực tiểu của hàm số là $2$. \\\\ \n'
                        %(latex(x1),latex(x2),latex(x3),
                        latex(x1),latex(x2),latex(x3),
                        ))
            if dang=='3':
                d = ['$x=%s$ và $x=%s$'%(latex(x1),latex(x3)),
                    ]
                da= random.choice(d)
                s = ['$x=%s$ và $x=%s$'%(latex(x1),latex(x2)),
                    '$x=%s$ và $x=%s$'%(latex(x2),latex(x3)),
                    '$y=%s$ và $y=%s$'%(latex(x1),latex(x3)),
                    '$y=%s$ và $y=%s$'%(latex(x1),latex(x2)),
                    '$y=%s$ và $y=%s$'%(latex(x2),latex(x3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ có đồ thị của đạo hàm $f\'(x)$ như hình vẽ bên. Điểm cực tiểu của hàm số là   \n'
                                )
                hinhve = (      '\\scalebox{0.7}{ \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,line width=1pt]  \n'
                                '\\tikzset{every node/.style={scale=0.9}} \n'
                                '\\draw[->] (%s-2.1,0)--(%s+2.1,0) node[below left] {$x$}; \n' #3
                                '\\draw[->] (0,-4.1)--(0,4.1) node[below left] {$y$}; \n' #4
                                '\\draw (0,0) node [below left] {$O$}; \n'
                                '\\foreach \\x/\\nx in {%s/%s,%s/%s,%s/%s} { \n'  #1
                                    '\\ifnum \\x=0 \n'
                                        '\\draw[thin] (\\x,1pt)--(\\x,-1pt); \n'
                                    '\\else \n'
                                        '\\draw[thin] (\\x,1pt)--(\\x,-1pt) node [below] {$\\nx$}; \n'
                                    '\\fi \n'
                                '} \n'
                                '\\begin{scope} \n'
                                '\\clip (%s-2.1,-4.1) rectangle (%s+2.1,4.1); \n'  #5
                                '\\draw[samples=200,domain=-5:5,smooth,variable=\\x] plot (\\x,{%s*((\\x)^3)+%s*((\\x)^2)+%s*(\\x)+%s}); \n' #2
                                '\\end{scope} \n'
                                '\\end{tikzpicture} }\n'

                                %(latex(x1),latex(x3), #3
                                #latex(f1),latex(f2), #4
                                latex(x1),latex(x1), latex(x2),latex(x2),latex(x3),latex(x3), #1
                                latex(x1),latex(x3), #5
                                latex(a),latex(b),latex(c),latex(e), #2
                                )) 
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
                        'Từ đồ thị ta có \\\\ \n'
                        '\\hspace*{1cm} $f\'(x)=0 \\Leftrightarrow \\hoac{& x=%s \\\\& x=%s \\\\& x=%s.}$ \\\\ \n'
                        'Bảng xét dấu \\\\ \n'
                        '\\hspace*{1cm} \\begin{tikzpicture} \n'
                        '\\tkzTabInit[deltacl=0.5,espcl=2.5,lgt=2]  \n'
                        '{$x$/1,$y\'$/1}  \n'
                        '{$-\\infty$,$%s$,$%s$,$%s$,$+\\infty$}  \n'
                        '\\tkzTabLine{,-,0,+,0,-,0,+,}  \n'
                        '\\end{tikzpicture}  \\\\ \n'
                        'Từ bảng xét dấu ta thấy điểm cực tiểu của hàm số là $x=%s$ và $x=%s$. \\\\ \n'
                        %(latex(x1),latex(x2),latex(x3),
                        latex(x1),latex(x2),latex(x3),
                        latex(x1),latex(x3)
                        ))
            if dang=='2':
                d = ['$x=%s$'%(latex(x2)),
                    ]
                da= random.choice(d)
                s = ['$x=%s$'%(latex(x1)),
                    '$x=%s$'%(latex(x3)),
                    '$y=%s$'%(latex(x1)),
                    '$y=%s$'%(latex(x3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ có đồ thị của đạo hàm $f\'(x)$ như hình vẽ bên. Điểm cực đại của hàm số là  \n'
                                )
                hinhve = (      '\\scalebox{0.7}{ \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,line width=1pt]  \n'
                                '\\tikzset{every node/.style={scale=0.9}} \n'
                                '\\draw[->] (%s-2.1,0)--(%s+2.1,0) node[below left] {$x$}; \n' #3
                                '\\draw[->] (0,-4.1)--(0,4.1) node[below left] {$y$}; \n' #4
                                '\\draw (0,0) node [below left] {$O$}; \n'
                                '\\foreach \\x/\\nx in {%s/%s,%s/%s,%s/%s} { \n'  #1
                                    '\\ifnum \\x=0 \n'
                                        '\\draw[thin] (\\x,1pt)--(\\x,-1pt); \n'
                                    '\\else \n'
                                        '\\draw[thin] (\\x,1pt)--(\\x,-1pt) node [below] {$\\nx$}; \n'
                                    '\\fi \n'
                                '} \n'
                                '\\begin{scope} \n'
                                '\\clip (%s-2.1,-4.1) rectangle (%s+2.1,4.1); \n'  #5
                                '\\draw[samples=200,domain=-5:5,smooth,variable=\\x] plot (\\x,{%s*((\\x)^3)+%s*((\\x)^2)+%s*(\\x)+%s}); \n' #2
                                '\\end{scope} \n'
                                '\\end{tikzpicture} }\n'

                                %(latex(x1),latex(x3), #3
                                #latex(f1),latex(f2), #4
                                latex(x1),latex(x1), latex(x2),latex(x2),latex(x3),latex(x3), #1
                                latex(x1),latex(x3), #5
                                latex(a),latex(b),latex(c),latex(e), #2
                                )) 
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
                        'Từ đồ thị ta có \\\\ \n'
                        '\\hspace*{1cm} $f\'(x)=0 \\Leftrightarrow \\hoac{& x=%s \\\\& x=%s \\\\& x=%s.}$ \\\\ \n'
                        'Bảng xét dấu \\\\ \n'
                        '\\hspace*{1cm} \\begin{tikzpicture} \n'
                        '\\tkzTabInit[deltacl=0.5,espcl=2.5,lgt=2]  \n'
                        '{$x$/1,$y\'$/1}  \n'
                        '{$-\\infty$,$%s$,$%s$,$%s$,$+\\infty$}  \n'
                        '\\tkzTabLine{,-,0,+,0,-,0,+,}  \n'
                        '\\end{tikzpicture}  \\\\ \n'
                        'Từ bảng xét dấu ta thấy điểm cực đại của hàm số là $x=%s$. \\\\ \n'
                        %(latex(x1),latex(x2),latex(x3),
                        latex(x1),latex(x2),latex(x3),
                        latex(x2)
                        ))
            if dang=='1':
                d = ['$3$',
                    ]
                da= random.choice(d)
                s = ['$0$',
                    '$1$',
                    '$2$',
                    '$4$',
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ có đồ thị của đạo hàm $f\'(x)$ như hình vẽ bên. Số điểm cực trị của hàm số là   \n'
                                )
                hinhve = (      '\\scalebox{0.7}{ \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,line width=1pt]  \n'
                                '\\tikzset{every node/.style={scale=0.9}} \n'
                                '\\draw[->] (%s-2.1,0)--(%s+2.1,0) node[below left] {$x$}; \n' #3
                                '\\draw[->] (0,-4.1)--(0,4.1) node[below left] {$y$}; \n' #4
                                '\\draw (0,0) node [below left] {$O$}; \n'
                                '\\foreach \\x/\\nx in {%s/%s,%s/%s,%s/%s} { \n'  #1
                                    '\\ifnum \\x=0 \n'
                                        '\\draw[thin] (\\x,1pt)--(\\x,-1pt); \n'
                                    '\\else \n'
                                        '\\draw[thin] (\\x,1pt)--(\\x,-1pt) node [below] {$\\nx$}; \n'
                                    '\\fi \n'
                                '} \n'
                                '\\begin{scope} \n'
                                '\\clip (%s-2.1,-4.1) rectangle (%s+2.1,4.1); \n'  #5
                                '\\draw[samples=200,domain=-5:5,smooth,variable=\\x] plot (\\x,{%s*((\\x)^3)+%s*((\\x)^2)+%s*(\\x)+%s}); \n' #2
                                '\\end{scope} \n'
                                '\\end{tikzpicture} }\n'

                                %(latex(x1),latex(x3), #3
                                #latex(f1),latex(f2), #4
                                latex(x1),latex(x1), latex(x2),latex(x2),latex(x3),latex(x3), #1
                                latex(x1),latex(x3), #5
                                latex(a),latex(b),latex(c),latex(e), #2
                                )) 
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
                        'Từ đồ thị ta có \\\\ \n'
                        '\\hspace*{1cm} $f\'(x)=0 \\Leftrightarrow \\hoac{& x=%s \\\\& x=%s \\\\& x=%s.}$ \\\\ \n'
                        'Bảng xét dấu \\\\ \n'
                        '\\hspace*{1cm} \\begin{tikzpicture} \n'
                        '\\tkzTabInit[deltacl=0.5,espcl=2.5,lgt=2]  \n'
                        '{$x$/1,$y\'$/1}  \n'
                        '{$-\\infty$,$%s$,$%s$,$%s$,$+\\infty$}  \n'
                        '\\tkzTabLine{,-,0,+,0,-,0,+,}  \n'
                        '\\end{tikzpicture}  \\\\ \n'
                        'Từ bảng xét dấu ta thấy số điểm cực trị của hàm số là $3$. \\\\ \n'
                        %(latex(x1),latex(x2),latex(x3),
                        latex(x1),latex(x2),latex(x3),
                        ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n \\immini{'+ str(noidungcauhoi)+ 
                '\\choice[2] \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n }{'+hinhve+ '} \n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content


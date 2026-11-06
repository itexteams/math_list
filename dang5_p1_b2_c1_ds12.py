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


def bt_dang5_p1_b2_c1_ds12(self):
            # Khai báo biến
            x = symbols('x')
            i=randint(1,9)
            a=-2*i
            b=4*i
            gtnn=-4*i
            gtln=i

            lisdang=['1','2','3','4','5','6','7']
            dang=random.choice(lisdang)
            if dang=='7':
                d = ['$x=%s$'%(latex(-a)),
                    ]
                da= random.choice(d)
                s = ['$x=%s$'%(latex(-a+1)),
                    '$x=%s$'%(latex(-a-1)),
                    '$x=%s$'%(latex(-a+2)),
                    '$x=%s$'%(latex(-a-2)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ liên tục trên đoạn $[%s;%s]$ và có đồ thị như hình vẽ bên. Hàm số đạt giá trị nhỏ nhất trên đoạn $[%s;%s]$ tại điểm'
                                %(latex(a),latex(b),latex(a),latex(b))
                                )
                hinhve = (      '\\scalebox{0.5}{ \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                                '\\tikzset{every node/.style={scale=0.9}} \n'
                                '\\draw[->] (-3.1,0)--(5.1,0) node[below left] {$x$}; \n'
                                '\\draw[->] (0,-5.1)--(0,2.1) node[below left] {$y$}; \n'
                                '\\draw (0,0) node [below left] {$O$}; \n'
                                '\\draw (-2,0) node [below] {$%s$}; \n'
                                '\\draw (1,0) node [above] {$%s$}; \n'
                                '\\draw (2,0) node [above] {$%s$}; \n'
                                '\\draw (4,0) node [above] {$%s$}; \n'
                                '\\draw (0,-4) node [left] {$%s$}; \n'
                                '\\draw (0,-3) node [below left] {$%s$}; \n'
                                '\\draw (0,-2) node [left] {$%s$}; \n'
                                '\\draw (0,1) node [right] {$%s$}; \n'
                                '\\draw[dashed,thin](-2,0)--(-2,1)--(0,1); \n'
                                '\\draw[dashed,thin](1,0)--(1,-2)--(0,-2); \n'
                                '\\draw[dashed,thin](2,0)--(2,-4)--(0,-4); \n'
                                '\\begin{scope} \n'
                                '\\clip (-3,-5) rectangle (5,2); \n'
                                '\\draw[samples=200,domain=-2:1,smooth,variable=\\x] plot (\\x,{1*(\\x)^2+0*(\\x)+-3}); \n'
                                '\\draw[samples=200,domain=1:2,smooth,variable=\\x] plot (\\x,{0*(\\x)^2+-2*(\\x)}); \n'
                                '\\draw[samples=200,domain=2:4,smooth,variable=\\x] plot (\\x,{0*(\\x)^2+2*(\\x)-8}); \n'
                                '\\end{scope} \n'
                                '\\end{tikzpicture}} \n'
                            %(latex(a),
                            latex(i),
                            latex(2*i),
                            latex(b),
                            latex(gtnn),
                            latex(-3*i),
                            latex(-2*i),
                            latex(i)
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
                        'Từ đồ thị hàm số ta có trên đoạn $[%s;%s]$ \\\\ \n'
                        '\\hspace*{1cm} Giá trị lớn nhất của hàm số là $%s$. \\\\ \n'
                        '\\hspace*{1cm} Giá trị nhỏ nhất của hàm số là $%s$.'
                        %(latex(a),latex(b),latex(gtln),latex(gtnn))
                            )
            if dang=='6':
                d = ['$x=%s$'%(latex(a)),
                    ]
                da= random.choice(d)
                s = ['$x=%s$'%(latex(a+1)),
                    '$x=%s$'%(latex(a-1)),
                    '$x=%s$'%(latex(a+2)),
                    '$x=%s$'%(latex(a-2)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ liên tục trên đoạn $[%s;%s]$ và có đồ thị như hình vẽ bên. Hàm số đạt giá trị lớn nhất trên đoạn $[%s;%s]$ tại điểm'
                                %(latex(a),latex(b),latex(a),latex(b))
                                )
                hinhve = (      '\\scalebox{0.5}{ \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                                '\\tikzset{every node/.style={scale=0.9}} \n'
                                '\\draw[->] (-3.1,0)--(5.1,0) node[below left] {$x$}; \n'
                                '\\draw[->] (0,-5.1)--(0,2.1) node[below left] {$y$}; \n'
                                '\\draw (0,0) node [below left] {$O$}; \n'
                                '\\draw (-2,0) node [below] {$%s$}; \n'
                                '\\draw (1,0) node [above] {$%s$}; \n'
                                '\\draw (2,0) node [above] {$%s$}; \n'
                                '\\draw (4,0) node [above] {$%s$}; \n'
                                '\\draw (0,-4) node [left] {$%s$}; \n'
                                '\\draw (0,-3) node [below left] {$%s$}; \n'
                                '\\draw (0,-2) node [left] {$%s$}; \n'
                                '\\draw (0,1) node [right] {$%s$}; \n'
                                '\\draw[dashed,thin](-2,0)--(-2,1)--(0,1); \n'
                                '\\draw[dashed,thin](1,0)--(1,-2)--(0,-2); \n'
                                '\\draw[dashed,thin](2,0)--(2,-4)--(0,-4); \n'
                                '\\begin{scope} \n'
                                '\\clip (-3,-5) rectangle (5,2); \n'
                                '\\draw[samples=200,domain=-2:1,smooth,variable=\\x] plot (\\x,{1*(\\x)^2+0*(\\x)+-3}); \n'
                                '\\draw[samples=200,domain=1:2,smooth,variable=\\x] plot (\\x,{0*(\\x)^2+-2*(\\x)}); \n'
                                '\\draw[samples=200,domain=2:4,smooth,variable=\\x] plot (\\x,{0*(\\x)^2+2*(\\x)-8}); \n'
                                '\\end{scope} \n'
                                '\\end{tikzpicture} }\n'
                            %(latex(a),
                            latex(i),
                            latex(2*i),
                            latex(b),
                            latex(gtnn),
                            latex(-3*i),
                            latex(-2*i),
                            latex(i)
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
                        'Từ đồ thị hàm số ta có trên đoạn $[%s;%s]$ \\\\ \n'
                        '\\hspace*{1cm} Giá trị lớn nhất của hàm số là $%s$. \\\\ \n'
                        '\\hspace*{1cm} Giá trị nhỏ nhất của hàm số là $%s$.'
                        %(latex(a),latex(b),latex(gtln),latex(gtnn))
                            )
            if dang=='5':
                d = ['$%s$'%(latex(gtln*gtnn)),
                    ]
                da= random.choice(d)
                s = ['$%s$'%(latex(gtln*gtnn+1)),
                    '$%s$'%(latex(gtln*gtnn-1)),
                    '$%s$'%(latex(gtln*gtnn+2)),
                    '$%s$'%(latex(gtln*gtnn-2)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ liên tục trên đoạn $[%s;%s]$ và có đồ thị như hình vẽ bên. Tích giá trị lớn nhất và giá trị nhỏ nhất của hàm số trên đoạn $[%s;%s]$ là'
                                %(latex(a),latex(b),latex(a),latex(b))
                                )
                hinhve = (      '\\scalebox{0.5}{ \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                                '\\tikzset{every node/.style={scale=0.9}} \n'
                                '\\draw[->] (-3.1,0)--(5.1,0) node[below left] {$x$}; \n'
                                '\\draw[->] (0,-5.1)--(0,2.1) node[below left] {$y$}; \n'
                                '\\draw (0,0) node [below left] {$O$}; \n'
                                '\\draw (-2,0) node [below] {$%s$}; \n'
                                '\\draw (1,0) node [above] {$%s$}; \n'
                                '\\draw (2,0) node [above] {$%s$}; \n'
                                '\\draw (4,0) node [above] {$%s$}; \n'
                                '\\draw (0,-4) node [left] {$%s$}; \n'
                                '\\draw (0,-3) node [below left] {$%s$}; \n'
                                '\\draw (0,-2) node [left] {$%s$}; \n'
                                '\\draw (0,1) node [right] {$%s$}; \n'
                                '\\draw[dashed,thin](-2,0)--(-2,1)--(0,1); \n'
                                '\\draw[dashed,thin](1,0)--(1,-2)--(0,-2); \n'
                                '\\draw[dashed,thin](2,0)--(2,-4)--(0,-4); \n'
                                '\\begin{scope} \n'
                                '\\clip (-3,-5) rectangle (5,2); \n'
                                '\\draw[samples=200,domain=-2:1,smooth,variable=\\x] plot (\\x,{1*(\\x)^2+0*(\\x)+-3}); \n'
                                '\\draw[samples=200,domain=1:2,smooth,variable=\\x] plot (\\x,{0*(\\x)^2+-2*(\\x)}); \n'
                                '\\draw[samples=200,domain=2:4,smooth,variable=\\x] plot (\\x,{0*(\\x)^2+2*(\\x)-8}); \n'
                                '\\end{scope} \n'
                                '\\end{tikzpicture} }\n'
                            %(latex(a),
                            latex(i),
                            latex(2*i),
                            latex(b),
                            latex(gtnn),
                            latex(-3*i),
                            latex(-2*i),
                            latex(i)
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
                        'Từ đồ thị hàm số ta có trên đoạn $[%s;%s]$ \\\\ \n'
                        '\\hspace*{1cm} Giá trị lớn nhất của hàm số là $%s$. \\\\ \n'
                        '\\hspace*{1cm} Giá trị nhỏ nhất của hàm số là $%s$.'
                        %(latex(a),latex(b),latex(gtln),latex(gtnn))
                            )
            if dang=='4':
                d = ['$%s$'%(latex(gtln-gtnn)),
                    ]
                da= random.choice(d)
                s = ['$%s$'%(latex(gtln-gtnn+3)),
                    '$%s$'%(latex(gtln-gtnn-1)),
                    '$%s$'%(latex(gtln-gtnn+1)),
                    '$%s$'%(latex(gtln-gtnn-2)),
                    '$%s$'%(latex(gtln-gtnn+2)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ liên tục trên đoạn $[%s;%s]$ và có đồ thị như hình vẽ bên. Hiệu giá trị lớn nhất và giá trị nhỏ nhất của hàm số trên đoạn $[%s;%s]$ là'
                                %(latex(a),latex(b),latex(a),latex(b))
                                )
                hinhve = (      '\\scalebox{0.5}{ \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                                '\\tikzset{every node/.style={scale=0.9}} \n'
                                '\\draw[->] (-3.1,0)--(5.1,0) node[below left] {$x$}; \n'
                                '\\draw[->] (0,-5.1)--(0,2.1) node[below left] {$y$}; \n'
                                '\\draw (0,0) node [below left] {$O$}; \n'
                                '\\draw (-2,0) node [below] {$%s$}; \n'
                                '\\draw (1,0) node [above] {$%s$}; \n'
                                '\\draw (2,0) node [above] {$%s$}; \n'
                                '\\draw (4,0) node [above] {$%s$}; \n'
                                '\\draw (0,-4) node [left] {$%s$}; \n'
                                '\\draw (0,-3) node [below left] {$%s$}; \n'
                                '\\draw (0,-2) node [left] {$%s$}; \n'
                                '\\draw (0,1) node [right] {$%s$}; \n'
                                '\\draw[dashed,thin](-2,0)--(-2,1)--(0,1); \n'
                                '\\draw[dashed,thin](1,0)--(1,-2)--(0,-2); \n'
                                '\\draw[dashed,thin](2,0)--(2,-4)--(0,-4); \n'
                                '\\begin{scope} \n'
                                '\\clip (-3,-5) rectangle (5,2); \n'
                                '\\draw[samples=200,domain=-2:1,smooth,variable=\\x] plot (\\x,{1*(\\x)^2+0*(\\x)+-3}); \n'
                                '\\draw[samples=200,domain=1:2,smooth,variable=\\x] plot (\\x,{0*(\\x)^2+-2*(\\x)}); \n'
                                '\\draw[samples=200,domain=2:4,smooth,variable=\\x] plot (\\x,{0*(\\x)^2+2*(\\x)-8}); \n'
                                '\\end{scope} \n'
                                '\\end{tikzpicture} }\n'
                            %(latex(a),
                            latex(i),
                            latex(2*i),
                            latex(b),
                            latex(gtnn),
                            latex(-3*i),
                            latex(-2*i),
                            latex(i)
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
                        'Từ đồ thị hàm số ta có trên đoạn $[%s;%s]$ \\\\ \n'
                        '\\hspace*{1cm} Giá trị lớn nhất của hàm số là $%s$. \\\\ \n'
                        '\\hspace*{1cm} Giá trị nhỏ nhất của hàm số là $%s$.'
                        %(latex(a),latex(b),latex(gtln),latex(gtnn))
                            )
            if dang=='3':
                d = ['$%s$'%(latex(gtln+gtnn)),
                    ]
                da= random.choice(d)
                s = ['$%s$'%(latex(gtln+gtnn+1)),
                    '$%s$'%(latex(gtln+gtnn-1)),
                    '$%s$'%(latex(gtln+gtnn+2)),
                    '$%s$'%(latex(gtln+gtnn-2)),
                    '$%s$'%(latex(gtln-gtnn)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ liên tục trên đoạn $[%s;%s]$ và có đồ thị như hình vẽ bên. Tổng giá trị lớn nhất và giá trị nhỏ nhất của hàm số trên đoạn $[%s;%s]$ là'
                                %(latex(a),latex(b),latex(a),latex(b))
                                )
                hinhve = (      '\\scalebox{0.5}{ \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                                '\\tikzset{every node/.style={scale=0.9}} \n'
                                '\\draw[->] (-3.1,0)--(5.1,0) node[below left] {$x$}; \n'
                                '\\draw[->] (0,-5.1)--(0,2.1) node[below left] {$y$}; \n'
                                '\\draw (0,0) node [below left] {$O$}; \n'
                                '\\draw (-2,0) node [below] {$%s$}; \n'
                                '\\draw (1,0) node [above] {$%s$}; \n'
                                '\\draw (2,0) node [above] {$%s$}; \n'
                                '\\draw (4,0) node [above] {$%s$}; \n'
                                '\\draw (0,-4) node [left] {$%s$}; \n'
                                '\\draw (0,-3) node [below left] {$%s$}; \n'
                                '\\draw (0,-2) node [left] {$%s$}; \n'
                                '\\draw (0,1) node [right] {$%s$}; \n'
                                '\\draw[dashed,thin](-2,0)--(-2,1)--(0,1); \n'
                                '\\draw[dashed,thin](1,0)--(1,-2)--(0,-2); \n'
                                '\\draw[dashed,thin](2,0)--(2,-4)--(0,-4); \n'
                                '\\begin{scope} \n'
                                '\\clip (-3,-5) rectangle (5,2); \n'
                                '\\draw[samples=200,domain=-2:1,smooth,variable=\\x] plot (\\x,{1*(\\x)^2+0*(\\x)+-3}); \n'
                                '\\draw[samples=200,domain=1:2,smooth,variable=\\x] plot (\\x,{0*(\\x)^2+-2*(\\x)}); \n'
                                '\\draw[samples=200,domain=2:4,smooth,variable=\\x] plot (\\x,{0*(\\x)^2+2*(\\x)-8}); \n'
                                '\\end{scope} \n'
                                '\\end{tikzpicture}} \n'
                            %(latex(a),
                            latex(i),
                            latex(2*i),
                            latex(b),
                            latex(gtnn),
                            latex(-3*i),
                            latex(-2*i),
                            latex(i)
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
                        'Từ đồ thị hàm số ta có trên đoạn $[%s;%s]$ \\\\ \n'
                        '\\hspace*{1cm} Giá trị lớn nhất của hàm số là $%s$. \\\\ \n'
                        '\\hspace*{1cm} Giá trị nhỏ nhất của hàm số là $%s$.'
                        %(latex(a),latex(b),latex(gtln),latex(gtnn))
                            )
            if dang=='2':
                d = ['$%s$'%(latex(gtnn)),
                    ]
                da= random.choice(d)
                s = ['$2$',
                    '$1$',
                    '$0$',
                    '$%s$'%(latex(gtln)),
                    '$-1$',
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ liên tục trên đoạn $[%s;%s]$ và có đồ thị như hình vẽ bên. Giá trị nhỏ nhất của hàm số trên đoạn $[%s;%s]$ là'
                                %(latex(a),latex(b),latex(a),latex(b))
                                )
                hinhve = (      '\\scalebox{0.5}{ \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                                '\\tikzset{every node/.style={scale=0.9}} \n'
                                '\\draw[->] (-3.1,0)--(5.1,0) node[below left] {$x$}; \n'
                                '\\draw[->] (0,-5.1)--(0,2.1) node[below left] {$y$}; \n'
                                '\\draw (0,0) node [below left] {$O$}; \n'
                                '\\draw (-2,0) node [below] {$%s$}; \n'
                                '\\draw (1,0) node [above] {$%s$}; \n'
                                '\\draw (2,0) node [above] {$%s$}; \n'
                                '\\draw (4,0) node [above] {$%s$}; \n'
                                '\\draw (0,-4) node [left] {$%s$}; \n'
                                '\\draw (0,-3) node [below left] {$%s$}; \n'
                                '\\draw (0,-2) node [left] {$%s$}; \n'
                                '\\draw (0,1) node [right] {$%s$}; \n'
                                '\\draw[dashed,thin](-2,0)--(-2,1)--(0,1); \n'
                                '\\draw[dashed,thin](1,0)--(1,-2)--(0,-2); \n'
                                '\\draw[dashed,thin](2,0)--(2,-4)--(0,-4); \n'
                                '\\begin{scope} \n'
                                '\\clip (-3,-5) rectangle (5,2); \n'
                                '\\draw[samples=200,domain=-2:1,smooth,variable=\\x] plot (\\x,{1*(\\x)^2+0*(\\x)+-3}); \n'
                                '\\draw[samples=200,domain=1:2,smooth,variable=\\x] plot (\\x,{0*(\\x)^2+-2*(\\x)}); \n'
                                '\\draw[samples=200,domain=2:4,smooth,variable=\\x] plot (\\x,{0*(\\x)^2+2*(\\x)-8}); \n'
                                '\\end{scope} \n'
                                '\\end{tikzpicture} }\n'
                            %(latex(a),
                            latex(i),
                            latex(2*i),
                            latex(b),
                            latex(gtnn),
                            latex(-3*i),
                            latex(-2*i),
                            latex(i)
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
                        'Từ đồ thị hàm số ta có trên đoạn $[%s;%s]$ \\\\ \n'
                        '\\hspace*{1cm} Giá trị lớn nhất của hàm số là $%s$. \\\\ \n'
                        '\\hspace*{1cm} Giá trị nhỏ nhất của hàm số là $%s$.'
                        %(latex(a),latex(b),latex(gtln),latex(gtnn))
                            )
            if dang=='1':
                d = ['$%s$'%(latex(gtln)),
                    ]
                da= random.choice(d)
                s = ['$2$',
                    '$1$',
                    '$0$',
                    '$%s$'%(latex(gtnn)),
                    '$-1$',
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ liên tục trên đoạn $[%s;%s]$ và có đồ thị như hình vẽ bên. Giá trị lớn nhất của hàm số trên đoạn $[%s;%s]$ là'
                                %(latex(a),latex(b),latex(a),latex(b))
                                )
                hinhve = (      '\\scalebox{0.5}{ \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                                '\\tikzset{every node/.style={scale=0.9}} \n'
                                '\\draw[->] (-3.1,0)--(5.1,0) node[below left] {$x$}; \n'
                                '\\draw[->] (0,-5.1)--(0,2.1) node[below left] {$y$}; \n'
                                '\\draw (0,0) node [below left] {$O$}; \n'
                                '\\draw (-2,0) node [below] {$%s$}; \n'
                                '\\draw (1,0) node [above] {$%s$}; \n'
                                '\\draw (2,0) node [above] {$%s$}; \n'
                                '\\draw (4,0) node [above] {$%s$}; \n'
                                '\\draw (0,-4) node [left] {$%s$}; \n'
                                '\\draw (0,-3) node [below left] {$%s$}; \n'
                                '\\draw (0,-2) node [left] {$%s$}; \n'
                                '\\draw (0,1) node [right] {$%s$}; \n'
                                '\\draw[dashed,thin](-2,0)--(-2,1)--(0,1); \n'
                                '\\draw[dashed,thin](1,0)--(1,-2)--(0,-2); \n'
                                '\\draw[dashed,thin](2,0)--(2,-4)--(0,-4); \n'
                                '\\begin{scope} \n'
                                '\\clip (-3,-5) rectangle (5,2); \n'
                                '\\draw[samples=200,domain=-2:1,smooth,variable=\\x] plot (\\x,{1*(\\x)^2+0*(\\x)+-3}); \n'
                                '\\draw[samples=200,domain=1:2,smooth,variable=\\x] plot (\\x,{0*(\\x)^2+-2*(\\x)}); \n'
                                '\\draw[samples=200,domain=2:4,smooth,variable=\\x] plot (\\x,{0*(\\x)^2+2*(\\x)-8}); \n'
                                '\\end{scope} \n'
                                '\\end{tikzpicture}} \n'
                            %(latex(a),
                            latex(i),
                            latex(2*i),
                            latex(b),
                            latex(gtnn),
                            latex(-3*i),
                            latex(-2*i),
                            latex(i)
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
                        'Từ đồ thị hàm số ta có trên đoạn $[%s;%s]$ \\\\ \n'
                        '\\hspace*{1cm} Giá trị lớn nhất của hàm số là $%s$. \\\\ \n'
                        '\\hspace*{1cm} Giá trị nhỏ nhất của hàm số là $%s$.'
                        %(latex(a),latex(b),latex(gtln),latex(gtnn))
                            )


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


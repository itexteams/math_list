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


def bt_dang16_p1_b4_c1_ds12(self):
            # Khai báo biến
            lisdang=['1','2','3','4','5','6','7','8']
            dang=random.choice(lisdang)

            if dang=='1':
                tcd=randint(-9,-1)
                tcn=-tcd
                c=randint(1,9)
                m=randint(-9,9)
                n=randint(-9,9)
                p=randint(-9,9)
                while m==0 or n==0 or p==0:
                    m=randint(-9,9)
                    n=randint(-9,9)
                    p=randint(-9,9)
                d=-c*tcd
                a=c*tcn
                b=2*d*tcn
                gox=2*tcd
                goy=-2*tcd
                x0=m*a+n*b+p*d

                S1=(x0+1,x0-1)
                S2=(x0+2,x0-2)
                S3=(x0+3,x0-3)
                s1=random.choice(S1)
                s2=random.choice(S2)
                s3=random.choice(S3)
                #Nội ung câu hỏi
                noidungcauhoi = ('Cho hàm số $y=\\dfrac{ax+b}{%sx+d}$ có đồ thị như hình vẽ bên. Giá trị biểu thức $T=%sa+%sb+%sd$ bằng '
                                %(latex(c),latex(m),latex(n),latex(p)))
                hinhve = (      '\\scalebox{0.8}{\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]'
                                '\\tikzset{every node/.style={scale=1}}'
                                '\\draw[->] (-6.1,0)--(2.1,0) node[below left] {$x$};'
                                '\\draw[->] (0,-3.1)--(0,5.1) node[below left] {$y$};'
                                '\\draw (0,1) node [below left] {$%s$};'#Tiệm cận ngang
                                '\\draw (-1,0) node [below left] {$%s$};'#Tiệm cận đứng
                                '\\draw (0,0) node [below left] {$O$};'
                                '\\draw (0,2) node [below left] {$%s$};'#Giao oy
                                '\\draw (-2,0) node [below left] {$%s$};'#Giao ox
                                '\\draw[thin] (-6,1)--(2,1);'
                                '\\begin{scope}'
                                '\\clip (-6,-3) rectangle (2,5);'
                                '\\draw[samples=200,domain=-6:5,smooth,variable=\\x] plot (\\x,{(1*(\\x)+2)/(1*(\\x)+1)});'
                                '\\end{scope}'
                                '\\end{tikzpicture}}'%(latex(tcn),latex(tcd),latex(goy),latex(gox))
                                )

                # Các đáp án
                da_d = '\\True $%s$'%(latex(x0))
                da_s1 = '$%s$'%(latex(s1))
                da_s2 = '$%s$'%(latex(s2))
                da_s3 = '$%s$'%(latex(s3))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        'Dựa vào hàm số và đồ thị ta có \\\\ \n'
                        'Tiệm cận ngang $y=\\dfrac{a}{%s}\\Rightarrow\\dfrac{a}{%s}= %s \\Leftrightarrow a=%s$.\\hspace {1 cm}$(1)$ \\\\ \n'
                        'Giao trục $Ox$ tại điểm có hoành độ $x_0=\\dfrac{-b}{a} \\Rightarrow \\dfrac{-b}{a}=%s\\Leftrightarrow b=%s\\cdot %s\\Leftrightarrow b=%s$.\\hspace {1 cm} $(2)$\\\\ \n'
                        'Tiệm cận đứng $x=\\dfrac{-d}{%s} \\Rightarrow \\dfrac{-d}{%s}=%s\\Leftrightarrow d=%s$.\\hspace {1 cm}$(3)$\\\\ \n'
                        'Thay $(1);(2);(3)$ vào $T$ ta được $T=%s\\cdot%s+%s\\cdot %s+%s\\cdot%s=%s$. \\\\ \n'
                        %(latex(c),latex(c),latex(tcn),latex(a),
                        latex(gox),latex(-gox),latex(a),latex(b),
                        latex(c),latex(c),latex(tcd),latex(d),
                                        latex(m),latex(a),latex(n),latex(b),latex(p),latex(d),latex(x0))
                        )

            if dang=='2':
                tcd=randint(-9,-1)
                tcn=-tcd
                c=randint(1,9)
                m=randint(-9,9)
                n=randint(-9,9)
                p=randint(-9,9)
                while m==0 or n==0 or p==0:
                    m=randint(-9,9)
                    n=randint(-9,9)
                    p=randint(-9,9)
                d=-c*tcd
                a=c*tcn
                b=Rational(3*tcd*a,4)
                gox=Rational(-3*tcd,4)
                goy=Rational(3*tcd,4)
                x0=m*a+n*b+p*d

                S1=(x0+1,x0-1)
                S2=(x0+2,x0-2)
                S3=(x0+3,x0-3)
                s1=random.choice(S1)
                s2=random.choice(S2)
                s3=random.choice(S3)
                #Nội ung câu hỏi
                noidungcauhoi = ('Cho hàm số $y=\\dfrac{ax+b}{%sx+d}$ có đồ thị như hình vẽ bên. Giá trị biểu thức $T=%sa+%sb+%sd$ bằng '
                                %(latex(c),latex(m),latex(n),latex(p)))
                hinhve = (      '\\scalebox{0.6}{\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]'
                                '\\tikzset{every node/.style={scale=1}}'
                                '\\draw[->] (-7,0)--(4,0) node[below left] {$x$};'
                                '\\draw[->] (0,-4)--(0,7) node[below left] {$y$};'
                                '\\draw (0,2) node [below left] {$%s$};'#Tiệm cận ngang
                                '\\draw (1.7,-0.1) node [below left] {$%s$};'#Tiệm cận đứng
                                '\\draw (0,0) node [below left] {$O$};'
                                '\\draw (0,-1) node [below left] {$%s$};'#Giao oy
                                '\\draw (-2,0) node [below left] {$%s$};'#Giao ox
                                '\\draw[thin] (-7,2)--(4,2);'
                                '\\begin{scope}'
                                '\\clip (-7,-4) rectangle (4,7);'
                                '\\draw[samples=200,domain=-7:4,smooth,variable=\\x] plot (\\x,{(2*(\\x)-3)/(1*(\\x)+2)});'
                                '\\end{scope}'
                                '\\end{tikzpicture}}'%(latex(tcn),latex(gox),latex(goy),latex(tcd))
                                )

                # Các đáp án
                da_d = '\\True $%s$'%(latex(x0))
                da_s1 = '$%s$'%(latex(s1))
                da_s2 = '$%s$'%(latex(s2))
                da_s3 = '$%s$'%(latex(s3))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        'Dựa vào hàm số và đồ thị ta có \\\\ \n'
                        'Tiệm cận ngang $y=\\dfrac{a}{%s}\\Rightarrow\\dfrac{a}{%s}= %s \\Leftrightarrow a=%s$.\\hspace {1 cm}$(1)$ \\\\ \n'
                        'Giao trục $Ox$ tại điểm có hoành độ $x_0=\\dfrac{-b}{a} \\Rightarrow \\dfrac{-b}{a}=%s\\Leftrightarrow b=%s\\cdot %s\\Leftrightarrow b=%s$.\\hspace {1 cm} $(2)$\\\\ \n'
                        'Tiệm cận đứng $x=\\dfrac{-d}{%s} \\Rightarrow \\dfrac{-d}{%s}=%s\\Leftrightarrow d=%s$.\\hspace {1 cm}$(3)$\\\\ \n'
                        'Thay $(1);(2);(3)$ vào $T$ ta được $T=%s\\cdot%s+%s\\cdot\\left(%s\\right)+%s\\cdot%s=%s$. \\\\ \n'
                        %(latex(c),latex(c),latex(tcn),latex(a),
                        latex(gox),latex(-gox),latex(a),latex(b),
                        latex(c),latex(c),latex(tcd),latex(d),
                                        latex(m),latex(a),latex(n),latex(b),latex(p),latex(d),latex(x0))
                        )

            if dang=='3':
                tcd=randint(1,9)
                tcn=2*tcd
                a=randint(1,9)
                m=randint(-9,9)
                n=randint(-9,9)
                p=randint(-9,9)
                while m==0 or n==0 or p==0:
                    m=randint(-9,9)
                    n=randint(-9,9)
                    p=randint(-9,9)
                b=Rational(a*tcd,2)
                c=Rational(a,2*tcd)
                d=-c*tcd
                gox=Rational(-tcd,2)
                x0=m*b+n*c+p*d

                S1=(x0+1,x0-1)
                S2=(x0+2,x0-2)
                S3=(x0+3,x0-3)
                s1=random.choice(S1)
                s2=random.choice(S2)
                s3=random.choice(S3)
                #Nội ung câu hỏi
                noidungcauhoi = ('Cho hàm số $y=\\dfrac{%sx+b}{cx+d}$ có đồ thị như hình vẽ bên. Giá trị biểu thức $T=%sb+%sc+%sd$ bằng '
                                %(latex(a),latex(m),latex(n),latex(p)))
                hinhve = (      '\\scalebox{0.6}{\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]'
                                '\\tikzset{every node/.style={scale=1.2}}'
                                '\\draw[->] (-4,0)--(5,0) node[below left] {$x$};'
                                '\\draw[->] (0,-3.1)--(0,5.1) node[below left] {$y$};'
                                '\\draw (0,2) node [below left] {$%s$};'#Tiệm cận ngang
                                '\\draw (1,0) node [below left] {$%s$};'#Tiệm cận đứng
                                '\\draw (0.7,0.7) node [below left] {$O$};'
                                '\\draw (0,-1) node [below left] {$%s$};'#Giao oy
                                '\\draw (-0.5,0) node [below left] {$%s$};'#Giao ox
                                '\\draw[thin] (-4,2)--(5,2);'
                                '\\begin{scope}'
                                '\\clip (-4,-3) rectangle (7,5);'
                                '\\draw[samples=200,domain=-4:5,smooth,variable=\\x] plot (\\x,{(2*(\\x)+1)/(1*(\\x)-1)});'
                                '\\end{scope}'
                                '\\end{tikzpicture}}'%(latex(tcn),latex(tcd),latex(-tcd),latex(gox))
                                )

                # Các đáp án
                da_d = '\\True $%s$'%(latex(x0))
                da_s1 = '$%s$'%(latex(s1))
                da_s2 = '$%s$'%(latex(s2))
                da_s3 = '$%s$'%(latex(s3))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        'Dựa vào hàm số và đồ thị ta có \\\\ \n'
                        'Giao trục $Ox$ tại điểm có hoành độ $x_0=\\dfrac{-b}{a} \\Rightarrow \\dfrac{-b}{%s}=%s\\Leftrightarrow b=%s$.\\hspace {1 cm} $(1)$\\\\ \n'
                        'Tiệm cận ngang $y=\\dfrac{%s}{c}\\Rightarrow\\dfrac{%s}{c}= %s \\Leftrightarrow c=%s$.\\hspace {1 cm}$(2)$ \\\\ \n'
                        'Tiệm cận đứng $x=\\dfrac{-d}{c} \\Rightarrow \\dfrac{-d}{%s}=%s\\Leftrightarrow d=%s$.\\hspace {1 cm}$(3)$\\\\ \n'
                        'Thay $(1);(2);(3)$ vào $T$ ta được $T=%s\\cdot%s+%s\\cdot %s+%s\\cdot \\left(%s\\right)=%s$. \\\\ \n'
                        %(latex(a),latex(gox),latex(b),
                        latex(a),latex(a),latex(tcn),latex(c),
                        latex(c),latex(tcd),latex(d),
                        latex(m),latex(b),latex(n),latex(c),latex(p),latex(d),latex(x0))
                        )

            if dang=='4':
                tcn=randint(1,9)
                tcd=-2*tcn
                a=randint(1,9)
                m=randint(-9,9)
                n=randint(-9,9)
                p=randint(-9,9)
                while m==0 or n==0 or p==0:
                    m=randint(-9,9)
                    n=randint(-9,9)
                    p=randint(-9,9)
                b=a*tcd
                c=Rational(a,tcn)
                d=-c*tcd
                gox=2*tcn
                goy=-tcn
                x0=m*b+n*c+p*d

                S1=(x0+1,x0-1)
                S2=(x0+2,x0-2)
                S3=(x0+3,x0-3)
                s1=random.choice(S1)
                s2=random.choice(S2)
                s3=random.choice(S3)
                #Nội ung câu hỏi
                noidungcauhoi = ('Cho hàm số $y=\\dfrac{%sx+b}{cx+d}$ có đồ thị như hình vẽ bên. Giá trị biểu thức $T=%sb+%sc+%sd$ bằng '
                                %(latex(a),latex(m),latex(n),latex(p)))
                hinhve = (      '\\scalebox{0.6}{\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]'
                                '\\tikzset{every node/.style={scale=1.2}}'
                                '\\draw[->] (-6,0)--(4,0) node[below left] {$x$};'
                                '\\draw[->] (0,-3.1)--(0,5.1) node[below left] {$y$};'
                                '\\draw (0,1) node [below left] {$%s$};'#Tiệm cận ngang
                                '\\draw (-2,0) node [below left] {$%s$};'#Tiệm cận đứng
                                '\\draw (0,0) node [below left] {$O$};'
                                '\\draw (0,-0.7) node [below left] {$%s$};'#Giao oy
                                '\\draw (2,0) node [below left] {$%s$};'#Giao ox
                                '\\draw[thin] (-6,1)--(4,1);'
                                '\\begin{scope}'
                                '\\clip (-6,-3) rectangle (5,5);'
                                '\\draw[samples=200,domain=-6:4,smooth,variable=\\x] plot (\\x,{(-1*(\\x)+2)/(-1*(\\x)-2)});'
                                '\\end{scope}'
                                '\\end{tikzpicture}}'%(latex(tcn),latex(tcd),latex(goy),latex(gox))
                                )

                # Các đáp án
                da_d = '\\True $%s$'%(latex(x0))
                da_s1 = '$%s$'%(latex(s1))
                da_s2 = '$%s$'%(latex(s2))
                da_s3 = '$%s$'%(latex(s3))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        'Dựa vào hàm số và đồ thị ta có \\\\ \n'
                        'Giao trục $Ox$ tại điểm có hoành độ $x_0=\\dfrac{-b}{a} \\Rightarrow \\dfrac{-b}{%s}=%s\\Leftrightarrow b=%s$.\\hspace {1 cm} $(1)$\\\\ \n'
                        'Tiệm cận ngang $y=\\dfrac{%s}{c}\\Rightarrow\\dfrac{%s}{c}= %s \\Leftrightarrow c=%s$.\\hspace {1 cm}$(2)$ \\\\ \n'
                        'Tiệm cận đứng $x=\\dfrac{-d}{c} \\Rightarrow \\dfrac{-d}{%s}=%s\\Leftrightarrow d=%s$.\\hspace {1 cm}$(3)$\\\\ \n'
                        'Thay $(1);(2);(3)$ vào $T$ ta được $T=%s\\cdot\\left(%s\\right)+%s\\cdot %s+%s\\cdot %s=%s$.'
                        %(latex(a),latex(gox),latex(b),
                        latex(a),latex(a),latex(tcn),latex(c),
                        latex(c),latex(tcd),latex(d),
                        latex(m),latex(b),latex(n),latex(c),latex(p),latex(d),latex(x0))
                        )

            if dang=='5':
                tcd=randint(1,9)
                tcn=-2*tcd
                b=randint(1,9)
                m=randint(-9,9)
                n=randint(-9,9)
                p=randint(-9,9)
                while m==0 or n==0 or p==0:
                    m=randint(-9,9)
                    n=randint(-9,9)
                    p=randint(-9,9)
                gox=-tcd
                goy=2*tcd
                a=Rational(-b,gox)
                c=Rational(a,tcn)
                d=-c*tcd
                x0=m*a+n*c+p*d

                S1=(x0+1,x0-1)
                S2=(x0+2,x0-2)
                S3=(x0+3,x0-3)
                s1=random.choice(S1)
                s2=random.choice(S2)
                s3=random.choice(S3)
                #Nội ung câu hỏi
                noidungcauhoi = ('Cho hàm số $y=\\dfrac{ax+%s}{cx+d}$ có đồ thị như hình vẽ bên. Giá trị biểu thức $T=%sa+%sc+%sd$ bằng '
                                %(latex(b),latex(m),latex(n),latex(p)))
                hinhve = (      '\\scalebox{0.6}{\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]'
                                '\\tikzset{every node/.style={scale=1.2}}\\\\ \n'
                                '\\draw[->] (-4,0)--(6,0) node[below left] {$x$};\\\\ \n'
                                '\\draw[->] (0,-6)--(0,4) node[below left] {$y$};\\\\ \n'
                                '\\draw (0,-2) node [below left] {$%s$};\\\\ \n'#Tiệm cận ngang
                                '\\draw (1,0) node [below left] {$%s$};\\\\ \n'#Tiệm cận đứng
                                '\\draw (0,0) node [below left] {$O$};\\\\ \n'
                                '\\draw (0,2) node [below left] {$%s$};\\\\ \n'#Giao oy
                                '\\draw (-0.7,0) node [below left] {$%s$};\\\\ \n'#Giao ox
                                '\\draw[thin] (-4,-2)--(6,-2);\\\\ \n'
                                '\\begin{scope}\\\\ \n'
                                '\\clip (-4,-6) rectangle (6,4);\\\\ \n'
                                '\\draw[samples=200,domain=-4:6,smooth,variable=\\x] plot (\\x,{(-2*(\\x)-2)/(1*(\\x)-1)});\\\\ \n'
                                '\\end{scope}\\\\'
                                '\\end{tikzpicture}}'%(latex(tcn),latex(tcd),latex(goy),latex(gox))
                                )

                # Các đáp án
                da_d = '\\True $%s$'%(latex(x0))
                da_s1 = '$%s$'%(latex(s1))
                da_s2 = '$%s$'%(latex(s2))
                da_s3 = '$%s$'%(latex(s3))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        'Dựa vào hàm số và đồ thị ta có \\\\ \n'
                        'Giao trục $Ox$ tại điểm có hoành độ $x_0=\\dfrac{-b}{a} \\Rightarrow \\dfrac{-%s}{a}=%s\\Leftrightarrow a=%s.$\\hspace {1 cm} $(1)$\\\\ \n'
                        'Tiệm cận ngang $y=\\dfrac{a}{c}\\Rightarrow\\dfrac{a}{c}= %s \\Leftrightarrow c= \\dfrac{%s}{%s} \\Leftrightarrow c=%s.$\\hspace {1 cm}$(2)$ \\\\ \n'
                        'Tiệm cận đứng $x=\\dfrac{-d}{c} \\Rightarrow \\dfrac{-d}{%s}=%s\\Leftrightarrow d=%s.$\\hspace {1 cm}$(3)$\\\\ \n'
                        'Thay $(1);(2);(3)$ vào $T$ ta được $T=%s\\cdot %s+%s\\cdot \\left(%s\\right)+%s\\cdot %s=%s.$ \\\\ \n'
                        %(latex(b),latex(gox),latex(a),
                        latex(tcn),latex(a),latex(tcn),latex(c),
                        latex(c),latex(tcd),latex(d),
                        latex(m),latex(b),latex(n),latex(c),latex(p),latex(d),latex(x0))
                        )

            if dang=='6':
                tcd=randint(1,9)
                tcn=2*tcd
                b=randint(1,9)
                m=randint(-9,9)
                n=randint(-9,9)
                p=randint(-9,9)
                while m==0 or n==0 or p==0:
                    m=randint(-9,9)
                    n=randint(-9,9)
                    p=randint(-9,9)
                gox=Rational(-3*tcd,2)
                goy=-3*tcd
                a=Rational(-b,gox)
                c=Rational(a,tcn)
                d=-c*tcd
                x0=m*a+n*c+p*d

                S1=(x0+1,x0-1)
                S2=(x0+2,x0-2)
                S3=(x0+3,x0-3)
                s1=random.choice(S1)
                s2=random.choice(S2)
                s3=random.choice(S3)
                #Nội ung câu hỏi
                noidungcauhoi = ('Cho hàm số $y=\\dfrac{ax+%s}{cx+d}$ có đồ thị như hình vẽ bên. Giá trị biểu thức $T=%sa+%sc+%sd$ bằng '
                                %(latex(b),latex(m),latex(n),latex(p)))
                hinhve = (      '\\scalebox{0.6}{\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]'
                                '\\tikzset{every node/.style={scale=1.2}}\\\\ \n'
                                '\\draw[->] (-4,0)--(6,0) node[below left] {$x$};\\\\ \n'
                                '\\draw[->] (0,-5)--(0,6) node[below left] {$y$};\\\\ \n'
                                '\\draw (0,2) node [below left] {$%s$};\\\\ \n'#Tiệm cận ngang
                                '\\draw (1,0) node [below left] {$%s$};\\\\ \n'#Tiệm cận đứng
                                '\\draw (0,0) node [below left] {$O$};\\\\ \n'
                                '\\draw (0,-3) node [below left] {$%s$};\\\\ \n'#Giao oy
                                '\\draw (-1.5,0) node [below left] {$%s$};\\\\ \n'#Giao ox
                                '\\draw[thin] (-4,2)--(6,2);\\\\ \n'
                                '\\begin{scope}\\\\ \n'
                                '\\clip (-4,-5) rectangle (6,6);\\\\ \n'
                                '\\draw[samples=200,domain=-4:6,smooth,variable=\\x] plot (\\x,{(2*(\\x)+3)/(1*(\\x)-1)});\\\\ \n'
                                '\\end{scope}\\\\'
                                '\\end{tikzpicture}}'%(latex(tcn),latex(tcd),latex(goy),latex(gox))
                                )

                # Các đáp án
                da_d = '\\True $%s$'%(latex(x0))
                da_s1 = '$%s$'%(latex(s1))
                da_s2 = '$%s$'%(latex(s2))
                da_s3 = '$%s$'%(latex(s3))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        'Dựa vào hàm số và đồ thị ta có \\\\ \n'
                        'Giao trục $Ox$ tại điểm có hoành độ $x_0=\\dfrac{-b}{a} \\Rightarrow \\dfrac{-%s}{a}=%s\\Leftrightarrow a=%s.$\\hspace {1 cm} $(1)$\\\\ \n'
                        'Tiệm cận ngang $y=\\dfrac{a}{c}\\Rightarrow\\dfrac{a}{c}= %s \\Leftrightarrow c= \\dfrac{%s}{%s} \\Leftrightarrow c=%s.$\\hspace {1 cm}$(2)$ \\\\ \n'
                        'Tiệm cận đứng $x=\\dfrac{-d}{c} \\Rightarrow \\dfrac{-d}{%s}=%s\\Leftrightarrow d=%s.$\\hspace {1 cm}$(3)$\\\\ \n'
                        'Thay $(1);(2);(3)$ vào $T$ ta được $T=%s\\cdot %s+%s\\cdot %s+%s\\cdot \\left(%s\\right)=%s.$ \\\\ \n'
                        %(latex(b),latex(gox),latex(a),
                        latex(tcn),latex(a),latex(tcn),latex(c),
                        latex(c),latex(tcd),latex(d),
                        latex(m),latex(a),latex(n),latex(c),latex(p),latex(d),latex(x0))
                        )

            if dang=='7':
                tcd=randint(1,9)
                tcn=tcd
                d=randint(1,9)
                m=randint(-9,9)
                n=randint(-9,9)
                p=randint(-9,9)
                while m==0 or n==0 or p==0:
                    m=randint(-9,9)
                    n=randint(-9,9)
                    p=randint(-9,9)
                gox=2*tcd
                goy=2*tcd
                c=Rational(-d,tcd)
                a=c*tcd
                b=-a*gox
                x0=m*a+n*b+p*c

                S1=(x0+1,x0-1)
                S2=(x0+2,x0-2)
                S3=(x0+3,x0-3)
                s1=random.choice(S1)
                s2=random.choice(S2)
                s3=random.choice(S3)
                #Nội ung câu hỏi
                noidungcauhoi = ('Cho hàm số $y=\\dfrac{ax+b}{cx+%s}$ có đồ thị như hình vẽ bên. Giá trị biểu thức $T=%sa+%sb+%sc$ bằng '
                                %(latex(d),latex(m),latex(n),latex(p)))
                hinhve = (      '\\scalebox{0.8}{\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]'
                                '\\tikzset{every node/.style={scale=1}}\\\\ \n'
                                '\\draw[->] (-3,0)--(5,0) node[below left] {$x$};\\\\ \n'
                                '\\draw[->] (0,-4)--(0,5) node[below left] {$y$};\\\\ \n'
                                '\\draw (0,1) node [below left] {$%s$};\\\\ \n'#Tiệm cận ngang
                                '\\draw (1,0) node [below left] {$%s$};\\\\ \n'#Tiệm cận đứng
                                '\\draw (0,0) node [below left] {$O$};\\\\ \n'
                                '\\draw (0,2.4) node [below left] {$%s$};\\\\ \n'#Giao oy
                                '\\draw (2.4,0) node [below left] {$%s$};\\\\ \n'#Giao ox
                                '\\draw[thin] (-3,1)--(5,1);\\\\ \n'
                                '\\begin{scope}\\\\ \n'
                                '\\clip (-3,-4) rectangle (5,5);\\\\ \n'
                                '\\draw[samples=200,domain=-4:6,smooth,variable=\\x] plot (\\x,{(1*(\\x)-2)/(1*(\\x)-1)});\\\\ \n'
                                '\\end{scope}\\\\'
                                '\\end{tikzpicture}}'%(latex(tcn),latex(tcd),latex(goy),latex(gox))
                                )

                # Các đáp án
                da_d = '\\True $%s$'%(latex(x0))
                da_s1 = '$%s$'%(latex(s1))
                da_s2 = '$%s$'%(latex(s2))
                da_s3 = '$%s$'%(latex(s3))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        'Dựa vào hàm số và đồ thị ta có \\\\ \n'
                        'Tiệm cận đứng $x=\\dfrac{-d}{c} \\Rightarrow \\dfrac{-%s}{c}=%s\\Leftrightarrow c=%s.$\\hspace {1 cm}$(1)$\\\\ \n'
                        'Tiệm cận ngang $y=\\dfrac{a}{c}\\Rightarrow\\dfrac{a}{c}= %s \\Leftrightarrow a= %s\\cdot \\left(%s\\right) \\Leftrightarrow a=%s.$\\hspace {1 cm}$(2)$ \\\\ \n'
                        'Giao trục $Ox$ tại điểm có hoành độ $x_0=\\dfrac{-b}{a} \\Rightarrow \\dfrac{-b}{%s}=%s\\Leftrightarrow b=%s.$\\hspace {1 cm} $(3)$\\\\ \n'
                        'Thay $(1);(2);(3)$ vào $T$ ta được $T=%s\\cdot \\left(%s\\right)+%s\\cdot %s+%s\\cdot \\left(%s\\right)=%s.$ \\\\ \n'
                        %(latex(d),latex(tcd),latex(c),
                        latex(tcn),latex(tcn),latex(c),latex(a),
                        latex(a),latex(gox),latex(b),
                        latex(m),latex(a),latex(n),latex(b),latex(p),latex(c),latex(x0))
                        )

            if dang=='8':
                tcn=randint(1,9)
                tcd=3*tcn
                d=randint(1,9)
                m=randint(-9,9)
                n=randint(-9,9)
                p=randint(-9,9)
                while m==0 or n==0 or p==0:
                    m=randint(-9,9)
                    n=randint(-9,9)
                    p=randint(-9,9)
                gox=2*tcn
                goy=Rational(2*tcn,3)
                c=Rational(-d,tcd)
                a=c*tcn
                b=-a*gox
                x0=m*a+n*b+p*c

                S1=(x0+1,x0-1)
                S2=(x0+2,x0-2)
                S3=(x0+3,x0-3)
                s1=random.choice(S1)
                s2=random.choice(S2)
                s3=random.choice(S3)
                #Nội ung câu hỏi
                noidungcauhoi = ('Cho hàm số $y=\\dfrac{ax+b}{cx+%s}$ có đồ thị như hình vẽ bên. Giá trị biểu thức $T=%sa+%sb+%sc$ bằng '
                                %(latex(d),latex(m),latex(n),latex(p)))
                hinhve = (      '\\scalebox{0.8}{\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]'
                                '\\tikzset{every node/.style={scale=1}}\\\\ \n'
                                '\\draw[->] (-2,0)--(6,0) node[below left] {$x$};\\\\ \n'
                                '\\draw[->] (0,-3)--(0,5) node[below left] {$y$};\\\\ \n'
                                '\\draw (0,1.5) node [below left] {$%s$};\\\\ \n'#Tiệm cận ngang
                                '\\draw (3,0) node [below left] {$%s$};\\\\ \n'#Tiệm cận đứng
                                '\\draw (0,0) node [below left] {$O$};\\\\ \n'
                                '\\draw (0,0.7) node [below left] {$%s$};\\\\ \n'#Giao oy
                                '\\draw (2,0) node [below left] {$%s$};\\\\ \n'#Giao ox
                                '\\draw[thin] (-2,1)--(6,1);\\\\ \n'
                                '\\begin{scope}\\\\ \n'
                                '\\clip (-2,-3) rectangle (6,5);\\\\ \n'
                                '\\draw[samples=200,domain=-2:6,smooth,variable=\\x] plot (\\x,{(1*(\\x)-2)/(1*(\\x)-3)});\\\\ \n'
                                '\\end{scope}\\\\'
                                '\\end{tikzpicture}}'%(latex(tcn),latex(tcd),latex(goy),latex(gox))
                                )

                # Các đáp án
                da_d = '\\True $%s$'%(latex(x0))
                da_s1 = '$%s$'%(latex(s1))
                da_s2 = '$%s$'%(latex(s2))
                da_s3 = '$%s$'%(latex(s3))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        'Dựa vào hàm số và đồ thị ta có \\\\ \n'
                        'Tiệm cận đứng $x=\\dfrac{-d}{c} \\Rightarrow \\dfrac{-%s}{c}=%s\\Leftrightarrow c=%s.$\\hspace {1 cm}$(1)$\\\\ \n'
                        'Tiệm cận ngang $y=\\dfrac{a}{c}\\Rightarrow\\dfrac{a}{c}= %s \\Leftrightarrow a= %s\\cdot \\left(%s\\right) \\Leftrightarrow a=%s.$\\hspace {1 cm}$(2)$ \\\\ \n'
                        'Giao trục $Ox$ tại điểm có hoành độ $x_0=\\dfrac{-b}{a} \\Rightarrow \\dfrac{-b}{%s}=%s\\Leftrightarrow b=%s.$\\hspace {1 cm} $(3)$\\\\ \n'
                        'Thay $(1);(2);(3)$ vào $T$ ta được $T=%s\\cdot \\left(%s\\right)+%s\\cdot %s+%s\\cdot \\left(%s\\right)=%s.$ \\\\ \n'
                        %(latex(d),latex(tcd),latex(c),
                        latex(tcn),latex(tcn),latex(c),latex(a),
                        latex(a),latex(gox),latex(b),
                        latex(m),latex(a),latex(n),latex(b),latex(p),latex(c),latex(x0))
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-').replace('+0', '').replace('1x', 'x').replace('.0', '').replace('1a', 'a').replace('1b', 'b').replace('1c', 'c').replace('1d', 'd')
            return content


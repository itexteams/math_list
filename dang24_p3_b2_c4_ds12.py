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


def bt_dang24_p3_b2_c4_ds12(self):
            # Khai báo biến
            lisdang=['1','2','3']
            dang=random.choice(lisdang)

            if dang=='1':
                # Khai báo biến
                a1=randint(3,10)
                a2=randint(3,10)
                b=randint(65,95)
                c=randint(65,95)
                b1=b/100
                b12=round(1-b1,2)
                c1=c/100
                c12=round(1-c1,2)
                n=a1+a2
                while a1==a2 or b<=c:
                    a1=randint(3,10)
                    a2=randint(3,10)
                    b=randint(65,95)
                    c=randint(65,95)
                    b1=b/100
                    b12=round(1-b1,2)
                    c1=c/100
                    c12=round(1-c1,2)
                    n=a1+a2
                p1=nsimplify(a1/n)
                p11=1-p1
                p21=2*b1*(1-b1)
                p22=1-p21
                q21=2*c1*(1-c1)
                q22=1-q21
                pb=nsimplify(p1*p21+p11*q21)
                pab=(p1*p21)/pb

                number = Decimal(float(pab))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)


                # Nội dung câu hỏi
                noidungcauhoi = ('Xác suất bắn trúng đích của xạ thủ hạng I là $%s$ và của xạ thủ hạng II là $%s$$zz$ Chọn ngẫu nhiên $1$ xạ thủ từ một nhóm gồm '
                            '$%s$ xạ thủ hạng I và $%s$ xạ thủ hạng II$zz$ Biết rằng xạ thủ này bắn $2$ viên đạn một cách độc lập và chỉ có một viên bắn trúng đích$zz$ Tính xác suất để xạ thủ đó là xạ thủ hạng I '
                            '(kết quả làm tròn đến hàng phần trăm)$zz$'
                            %(latex(b1),latex(c1),latex(a1),latex(a2)
                            )
                            )
                # Nội dung lời giải
                loigiai = ('Xét các biến cố:\\\\ \n'
                        '\\hspace*{1cm} $A$: "Xạ thủ bắn $2$ viên đạn và chỉ có $1$ viên trúng đích"\\\\ \n'
                    '\\hspace*{1cm} $B$: "Chọn được xạ thủ hạng I"$zz$\\\\ \n'
                    'Theo bài ta có: $\\mathrm{P}(A|B)=2\\cdot %s\\cdot %s=%s$, $\\mathrm{P}(A|\\overline{B})=2\\cdot %s\\cdot %s=%s$$zz$ \\\\ \n'
                    'Ta có sơ đồ hình cây\\\\ \n'
                    '\\begin{center}'
                        '\\begin{tikzpicture}[line join = round, line cap = round, >=stealth, font=\\footnotesize, scale=1]\n'
                        '\\begin{scope}[every node/$zz$style={draw, rounded corners=5pt}]\n'
                        '\\node (A) at (0,0){Chọn $1$ xạ thủ};\n'
                        '\\def \\gocA{30}\n'
                        '\\def \\kcA{4}\n'
                        '\\node (B1) at ($(A)+(\\gocA:\\kcA)$){$B$};\n'
                        '\\node (B2) at ($(A)+(-\\gocA:\\kcA)$){$\\overline{B}$};\n'
                        '\\def \\gocB{15}\n'
                        '\\def \\kcB{4}\n'
                        '\\node (B11) at ($(B1)+(\\gocB:\\kcB)$){$A$};\n'
                        '\\node (B12) at ($(B1)+(-\\gocB:\\kcB)$){$\\overline{A}$};\n'
                        '\\node (B21) at ($(B2)+(\\gocB:\\kcB)$){$A$};\n'
                        '\\node (B22) at ($(B2)+(-\\gocB:\\kcB)$){$\\overline{A}$};\n'
                        '\\end{scope}\n'
                        '\\begin{scope}[every node/$zz$style={midway,sloped},every path/$zz$style={->}]\n'
                            '\\draw (A)--(B1) node[above]{$\\mathrm{P}(B)=$\\fbox{$%s$}};\n'
                            '\\draw (A)--(B2) node[below]{$\\mathrm{P}(\\overline{B})=$\\fbox{$%s$}};\n'
                            '\\draw (B1)--(B11) node[above]{$\\mathrm{P}(A|B)=$\\fbox{$%s$}};\n'
                            '\\draw (B1)--(B12) node[below]{$\\mathrm{P}(\\overline{A}|B)=$\\fbox{$%s$}};\n'
                            '\\draw (B2)--(B21) node[above]{$\\mathrm{P}(A|\\overline{B})=$\\fbox{$%s$}};\n'
                            '\\draw (B2)--(B22) node[below]{$\\mathrm{P}(\\overline{A}|\\overline{B})=$\\fbox{$%s$}};\n'
                        '\\end{scope}\n'
                        '\\end{tikzpicture}\n'
                        '\\end{center}\n'
                        'Xác suất xạ thủ bắn $2$ viên đạn và chỉ có $1$ viên trúng đích là\\\\ \n'
                        '\\hspace*{1cm}$\\mathrm{P}(A)=\\mathrm{P}(B)\\cdot\\mathrm{P}(A|B)+\\mathrm{P}(\\overline{B})\\cdot\\mathrm{P}(A|\\overline{B})=%s\\cdot %s+%s\\cdot %s=%s$$zz$\\\\ \n'
                        'Áp dụng công thức Bayes ta được\\\\ \n'
                        '\\hspace*{1cm}$\\mathrm{P}(B|A)=\\dfrac{\\mathrm{P}(B)}{\\mathrm{P}(A)}\\cdot\\mathrm{P}(A|B)=\\dfrac{%s}{%s}\\cdot %s\\approx %s$$zz$'
                        %(latex(b1),latex(b12),latex(p21),latex(c1),latex(c12),latex(q21),
                            latex(p1),latex(p11),latex(p21),latex(p22),latex(q21),latex(q22),
                        latex(p1),latex(p21),latex(p11),latex(q21),latex(pb),
                        latex(p1),latex(pb),latex(p21),latex(kq))
                        )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))
            if dang=='2':
                # Khai báo biến
                a1=randint(3,10)
                a2=randint(3,10)
                b=randint(65,95)
                c=randint(65,95)
                b1=b/100
                b12=round(1-b1,2)
                c1=c/100
                c12=round(1-c1,2)
                n=a1+a2
                while a1==a2 or b<=c:
                    a1=randint(3,10)
                    a2=randint(3,10)
                    b=randint(65,95)
                    c=randint(65,95)
                    b1=b/100
                    b12=round(1-b1,2)
                    c1=c/100
                    c12=round(1-c1,2)
                    n=a1+a2
                p1=nsimplify(a1/n)
                p11=1-p1
                p21=b1*b1
                p22=1-p21
                q21=c1*c1
                q22=1-q21
                pb=nsimplify(p1*p21+p11*q21)
                pab=(p1*p21)/pb

                number = Decimal(float(pab))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)


                # Nội dung câu hỏi
                noidungcauhoi = ('Xác suất bắn trúng đích của xạ thủ hạng I là $%s$ và của xạ thủ hạng II là $%s$$zz$ Chọn ngẫu nhiên $1$ xạ thủ từ một nhóm gồm '
                            '$%s$ xạ thủ hạng I và $%s$ xạ thủ hạng II$zz$ Biết rằng xạ thủ này bắn $2$ viên đạn một cách độc lập và cả hai viên đều bắn trúng đích$zz$ Tính xác suất để xạ thủ đó là xạ thủ hạng I '
                            '(kết quả làm tròn đến hàng phần trăm)$zz$'
                            %(latex(b1),latex(c1),latex(a1),latex(a2)
                            )
                            )
                # Nội dung lời giải
                loigiai = ('Xét các biến cố:\\\\ \n'
                        '\\hspace*{1cm} $A$: "Xạ thủ bắn $2$ viên đạn và cả hai viên đều bắn trúng đích"\\\\ \n'
                    '\\hspace*{1cm} $B$: "Chọn được xạ thủ hạng I"$zz$\\\\ \n'
                    'Theo bài ta có: $\\mathrm{P}(A|B)=%s\\cdot %s=%s$, $\\mathrm{P}(A|\\overline{B})=%s\\cdot %s=%s$$zz$ \\\\ \n'
                    'Ta có sơ đồ hình cây\\\\ \n'
                    '\\begin{center}'
                        '\\begin{tikzpicture}[line join = round, line cap = round, >=stealth, font=\\footnotesize, scale=1]\n'
                        '\\begin{scope}[every node/$zz$style={draw, rounded corners=5pt}]\n'
                        '\\node (A) at (0,0){Chọn $1$ xạ thủ};\n'
                        '\\def \\gocA{30}\n'
                        '\\def \\kcA{4}\n'
                        '\\node (B1) at ($(A)+(\\gocA:\\kcA)$){$B$};\n'
                        '\\node (B2) at ($(A)+(-\\gocA:\\kcA)$){$\\overline{B}$};\n'
                        '\\def \\gocB{15}\n'
                        '\\def \\kcB{4}\n'
                        '\\node (B11) at ($(B1)+(\\gocB:\\kcB)$){$A$};\n'
                        '\\node (B12) at ($(B1)+(-\\gocB:\\kcB)$){$\\overline{A}$};\n'
                        '\\node (B21) at ($(B2)+(\\gocB:\\kcB)$){$A$};\n'
                        '\\node (B22) at ($(B2)+(-\\gocB:\\kcB)$){$\\overline{A}$};\n'
                        '\\end{scope}\n'
                        '\\begin{scope}[every node/$zz$style={midway,sloped},every path/$zz$style={->}]\n'
                            '\\draw (A)--(B1) node[above]{$\\mathrm{P}(B)=$\\fbox{$%s$}};\n'
                            '\\draw (A)--(B2) node[below]{$\\mathrm{P}(\\overline{B})=$\\fbox{$%s$}};\n'
                            '\\draw (B1)--(B11) node[above]{$\\mathrm{P}(A|B)=$\\fbox{$%s$}};\n'
                            '\\draw (B1)--(B12) node[below]{$\\mathrm{P}(\\overline{A}|B)=$\\fbox{$%s$}};\n'
                            '\\draw (B2)--(B21) node[above]{$\\mathrm{P}(A|\\overline{B})=$\\fbox{$%s$}};\n'
                            '\\draw (B2)--(B22) node[below]{$\\mathrm{P}(\\overline{A}|\\overline{B})=$\\fbox{$%s$}};\n'
                        '\\end{scope}\n'
                        '\\end{tikzpicture}\n'
                        '\\end{center}\n'
                        'Xác suất xạ thủ bắn $2$ viên đạn và cả hai viên đều bắn trúng đích là\\\\ \n'
                        '\\hspace*{1cm}$\\mathrm{P}(A)=\\mathrm{P}(B)\\cdot\\mathrm{P}(A|B)+\\mathrm{P}(\\overline{B})\\cdot\\mathrm{P}(A|\\overline{B})=%s\\cdot %s+%s\\cdot %s=%s$$zz$\\\\ \n'
                        'Áp dụng công thức Bayes ta được\\\\ \n'
                        '\\hspace*{1cm}$\\mathrm{P}(B|A)=\\dfrac{\\mathrm{P}(B)}{\\mathrm{P}(A)}\\cdot\\mathrm{P}(A|B)=\\dfrac{%s}{%s}\\cdot %s\\approx %s$$zz$'
                        %(latex(b1),latex(b1),latex(p21),latex(c1),latex(c1),latex(q21),
                            latex(p1),latex(p11),latex(p21),latex(p22),latex(q21),latex(q22),
                        latex(p1),latex(p21),latex(p11),latex(q21),latex(pb),
                        latex(p1),latex(pb),latex(p21),latex(kq))
                        )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))


            if dang=='3':
                # Khai báo biến
                a1=randint(3,10)
                a2=randint(3,10)
                b=randint(65,95)
                c=randint(65,95)
                b1=b/100
                b12=round(1-b1,2)
                c1=c/100
                c12=round(1-c1,2)
                n=a1+a2
                while a1==a2 or b<=c:
                    a1=randint(3,10)
                    a2=randint(3,10)
                    b=randint(65,95)
                    c=randint(65,95)
                    b1=b/100
                    b12=round(1-b1,2)
                    c1=c/100
                    c12=round(1-c1,2)
                    n=a1+a2
                p1=nsimplify(a1/n)
                p11=1-p1
                p21=(1-b1)**2
                p22=1-p21
                q21=(1-c1)**2
                q22=1-q21
                pb=nsimplify(p1*p21+p11*q21)
                pab=(p1*p21)/pb

                number = Decimal(float(pab))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)


                # Nội dung câu hỏi
                noidungcauhoi = ('Xác suất bắn trúng đích của xạ thủ hạng I là $%s$ và của xạ thủ hạng II là $%s$$zz$ Chọn ngẫu nhiên $1$ xạ thủ từ một nhóm gồm '
                            '$%s$ xạ thủ hạng I và $%s$ xạ thủ hạng II$zz$ Biết rằng xạ thủ này bắn $2$ viên đạn một cách độc lập và cả hai viên đều bắn trượt đích$zz$ Tính xác suất để xạ thủ đó là xạ thủ hạng I '
                            '(kết quả làm tròn đến hàng phần trăm)$zz$'
                            %(latex(b1),latex(c1),latex(a1),latex(a2)
                            )
                            )
                # Nội dung lời giải
                loigiai = ('Xét các biến cố:\\\\ \n'
                        '\\hspace*{1cm} $A$: "Xạ thủ bắn $2$ viên đạn và cả hai viên đều bắn trượt đích"\\\\ \n'
                    '\\hspace*{1cm} $B$: "Chọn được xạ thủ hạng I"$zz$\\\\ \n'
                    'Theo bài ta có: $\\mathrm{P}(A|B)= (1-%s)\\cdot (1-%s)=%s$, $\\mathrm{P}(A|\\overline{B})=(1-%s)\\cdot (1-%s)=%s$$zz$ \\\\ \n'
                    'Ta có sơ đồ hình cây\\\\ \n'
                    '\\begin{center}'
                        '\\begin{tikzpicture}[line join = round, line cap = round, >=stealth, font=\\footnotesize, scale=1]\n'
                        '\\begin{scope}[every node/$zz$style={draw, rounded corners=5pt}]\n'
                        '\\node (A) at (0,0){Chọn $1$ xạ thủ};\n'
                        '\\def \\gocA{30}\n'
                        '\\def \\kcA{4}\n'
                        '\\node (B1) at ($(A)+(\\gocA:\\kcA)$){$B$};\n'
                        '\\node (B2) at ($(A)+(-\\gocA:\\kcA)$){$\\overline{B}$};\n'
                        '\\def \\gocB{15}\n'
                        '\\def \\kcB{4}\n'
                        '\\node (B11) at ($(B1)+(\\gocB:\\kcB)$){$A$};\n'
                        '\\node (B12) at ($(B1)+(-\\gocB:\\kcB)$){$\\overline{A}$};\n'
                        '\\node (B21) at ($(B2)+(\\gocB:\\kcB)$){$A$};\n'
                        '\\node (B22) at ($(B2)+(-\\gocB:\\kcB)$){$\\overline{A}$};\n'
                        '\\end{scope}\n'
                        '\\begin{scope}[every node/$zz$style={midway,sloped},every path/$zz$style={->}]\n'
                            '\\draw (A)--(B1) node[above]{$\\mathrm{P}(B)=$\\fbox{$%s$}};\n'
                            '\\draw (A)--(B2) node[below]{$\\mathrm{P}(\\overline{B})=$\\fbox{$%s$}};\n'
                            '\\draw (B1)--(B11) node[above]{$\\mathrm{P}(A|B)=$\\fbox{$%s$}};\n'
                            '\\draw (B1)--(B12) node[below]{$\\mathrm{P}(\\overline{A}|B)=$\\fbox{$%s$}};\n'
                            '\\draw (B2)--(B21) node[above]{$\\mathrm{P}(A|\\overline{B})=$\\fbox{$%s$}};\n'
                            '\\draw (B2)--(B22) node[below]{$\\mathrm{P}(\\overline{A}|\\overline{B})=$\\fbox{$%s$}};\n'
                        '\\end{scope}\n'
                        '\\end{tikzpicture}\n'
                        '\\end{center}\n'
                        'Xác suất xạ thủ bắn $2$ viên đạn và cả hai viên đều bắn trượt đích là\\\\ \n'
                        '\\hspace*{1cm}$\\mathrm{P}(A)=\\mathrm{P}(B)\\cdot\\mathrm{P}(A|B)+\\mathrm{P}(\\overline{B})\\cdot\\mathrm{P}(A|\\overline{B})=%s\\cdot %s+%s\\cdot %s=%s$$zz$\\\\ \n'
                        'Áp dụng công thức Bayes ta được\\\\ \n'
                        '\\hspace*{1cm}$\\mathrm{P}(B|A)=\\dfrac{\\mathrm{P}(B)}{\\mathrm{P}(A)}\\cdot\\mathrm{P}(A|B)=\\dfrac{%s}{%s}\\cdot %s\\approx %s$$zz$'
                        %(latex(b1),latex(b1),latex(p21),latex(c1),latex(c1),latex(q21),
                            latex(p1),latex(p11),latex(p21),latex(p22),latex(q21),latex(q22),
                        latex(p1),latex(p21),latex(p11),latex(q21),latex(pb),
                        latex(p1),latex(pb),latex(p21),latex(kq))
                        )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))
            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('.',',').replace('$zz$','.').replace('\\frac','\\dfrac')
            return content 


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


def bt_dang13_p1_b2_c2_hh10(self):
            #Khai báo biến
            a = randint(2,50) # b là số bất kỳ từ 1 đến 30
            b = randint(4,50)# b là số bất kỳ từ 1 đến 30
            while a<=b:
                a = randint(2,30) # b là số bất kỳ từ 1 đến 30
                b = randint(2,30)# b là số bất kỳ từ 1 đến 30
            x1=round(sqrt(b**2+(a**2)/4),1)
            x0 =2*x1
            S = {x0+1,x0+2,x0+3,x0-1,x0-2,x0-3}
            S2 = {a/2+1,a/2+2,a/2+3,a/2-1,a/2-2,a/2-3,}
            s1=S.pop()
            s2=S.pop()
            s3=S.pop()
            s4=S2.pop()
            s5=S2.pop()
            s6=S2.pop()
            list1=['1','2']
            rd = random.choice(list1)
            #Nội ung câu hỏi
            if rd=='1':
                noidungcauhoi = ('''Cho hình chữ nhật $ABCD$ có $AB=%s$, $AD=%s$$zzz$ Gọi $I$ là trung điểm $CD$$zzz$ Độ dài vectơ $\\vec{x}=\\overrightarrow{AB}+\\overrightarrow{AD}+\\overrightarrow{BC}$ là\n'''
                            %(latex(a),latex(b)))
            # Các đáp án
                da_d = '\\True $\\left|\\vec{x}\\right|\\approx%s$'%(latex(x0))
                da_s1 = '$\\left|\\vec{x}\\right|\\approx%s$'%(latex(s1))
                da_s2 = '$\\left|\\vec{x}\\right|\\approx%s$'%(latex(s2))
                da_s3 = '$\\left|\\vec{x}\\right|\\approx%s$'%(latex(s3))
            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
            # Nội dung lời giải
                loigiai =('Ta thực hiện biến đổi:\\\\\n'
                        '$\\left|\\vec{x}\\right|=\\left| \\overrightarrow{AB}+\\overrightarrow{AD}+\\overrightarrow{BC} \\right|=\\left| \\overrightarrow{AB}+\\overrightarrow{BC}+\\overrightarrow{AD} \\right|=\\left| \\overrightarrow{AC}+\\overrightarrow{AD} \\right|$$zzz$\\\\\n' 
                        'Dựng điểm $E$ sao cho: $\\overrightarrow{CE}=\\overrightarrow{AD}$$zzz$\\\\\n' 
                        'Suy ra $ACED$ là hình bình hành$zzz$\\\\\n' 
                        'Theo quy tắc hình bình hành: $\\left| \\overrightarrow{AC}+\\overrightarrow{AD} \\right|=\\left| \\overrightarrow{AE} \\right|=AE=2AI$$zzz$\\\\\n'
                        'Xét tam giác vuông $ADI$ có \\\\\n' 
                        '$AI=\\sqrt{DA^2+DI^2}=\\sqrt{DA^2+\\frac{AB^2}{4}}=\\sqrt{%s^2+\\dfrac{%s^2}{4}}\\approx%s$\\\\\n'
                        'Vậy $\\left|\\vec{x}\\right|=\\left| \\overrightarrow{AB}+\\overrightarrow{AD}+\\overrightarrow{BC} \\right|=AE=2AI=2\\cdot(%s)\\approx%s$$zzz$'
                        %(latex(b),latex(a),latex(x1),latex(x1),latex(x0)))
                hinhve = (    '\\begin{center}\n'
                        '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick, scale=0$zzz$5]\n'
                '\\clip(4$zzz$5,-7) rectangle (17$zzz$16,3$zzz$3);\n'
                '\\draw (6,2)-- (15,2);\n'
                '\\draw (15,2)-- (15,-2);\n'
                '\\draw (15,-2)-- (6,-2);\n'
                '\\draw (6,-2)-- (6,2);\n'
                '\\draw (15,-6)-- (6,2);\n'
                '\\draw (15,-2)-- (15,-6);\n'
                '\\draw (6,2)-- (15,-2);\n'
                '\\draw (6,-2)-- (15,-6);\n'
                '\\draw (5$zzz$58,3$zzz$2) node[anchor=north west] {A};\n'
                '\\draw (15$zzz$14,2$zzz$46) node[anchor=north west] {B};\n'
                '\\draw (15$zzz$24,-1$zzz$88) node[anchor=north west] {C};\n'
                '\\draw (5$zzz$48,-2) node[anchor=north west] {D};\n'
                '\\draw (15$zzz$12,-5$zzz$6) node[anchor=north west] {E};\n'
                '\\draw (10$zzz$34,-2$zzz$34) node[anchor=north west] {I};\n'
            '\\end{tikzpicture}\n'
                        '\\end{center}')
            if rd=='2':
                noidungcauhoi = ('''Cho hình chữ nhật $ABCD$ có $AB=%s$, $AD=%s$$zzz$ Gọi $I$ là trung điểm $CD$$zzz$ Độ dài vectơ $\\vec{x}=\\overrightarrow{AC}-\\overrightarrow{AB}-\\overrightarrow{AI}$ là\n'''
                            %(latex(a),latex(b)))
            # Các đáp án
                da_d = '\\True $\\left|\\vec{x}\\right|=%s$'%(latex(a/2))
                da_s1 = '$\\left|\\vec{x}\\right|=%s$'%(latex(s4))
                da_s2 = '$\\left|\\vec{x}\\right|=%s$'%(latex(s5))
                da_s3 = '$\\left|\\vec{x}\\right|=%s$'%(latex(s6))
            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
            # Nội dung lời giải
                loigiai =('Ta thực hiện biến đổi:\\\\\n'
                        '$\\left|\\vec{x}\\right|=\\left|\\overrightarrow{AC}-\\overrightarrow{AB}-\\overrightarrow{AI}\\right|=\\left| \\overrightarrow{BC}-\\overrightarrow{AI}\\right|=\\left|\\overrightarrow{AD}-\\overrightarrow{AI}\\right|=\\left|\\overrightarrow{ID}\\right|=ID=\\dfrac{CD}{2}=%s$$zzz$\\\\\n'
                        'Vậy $\\left|\\vec{x}\\right|=%s$$zzz$\\\\\n'
                        %(latex(a/2),latex(a/2)))
                hinhve = (    '\\begin{center}\n'
                        '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick, scale=0$zzz$5]\n'
                '\\clip(4$zzz$5,-7) rectangle (17$zzz$16,3$zzz$3);\n'
                '\\draw (6,2)-- (15,2);\n'
                '\\draw (15,2)-- (15,-2);\n'
                '\\draw (15,-2)-- (6,-2);\n'
                '\\draw (6,-2)-- (6,2);\n'
                '\\draw (15,-6)-- (6,2);\n'
                '\\draw (15,-2)-- (15,-6);\n'
                '\\draw (6,2)-- (15,-2);\n'
                '\\draw (6,-2)-- (15,-6);\n'
                '\\draw (5$zzz$58,3$zzz$2) node[anchor=north west] {A};\n'
                '\\draw (15$zzz$14,2$zzz$46) node[anchor=north west] {B};\n'
                '\\draw (15$zzz$24,-1$zzz$88) node[anchor=north west] {C};\n'
                '\\draw (5$zzz$48,-2) node[anchor=north west] {D};\n'
                '\\draw (15$zzz$12,-5$zzz$6) node[anchor=north west] {E};\n'
                '\\draw (10$zzz$34,-2$zzz$34) node[anchor=north west] {I};\n'
            '\\end{tikzpicture}\n'
                        '\\end{center}')
            # Xuất câu hỏi
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'
                +hinhve+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('.',',').replace('$zzz$','.').replace('\\frac','\\dfrac'). replace('1x','x').replace('-1x','-x'). replace('1y','y'). replace('{,}0',''). replace('+-','-')
            return content


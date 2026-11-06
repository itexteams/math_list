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


def bt_dang7_p1_b1_c3_ds12(self):
            # Khai báo biến
            lisdang=['1','2','3','4','5','6','7']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                x=symbols('x')
                a=randint(-9,9)
                b=randint(-9,9)
                c=randint(-10,10)
                while a==0 or b==0 or c==0:
                    x=symbols('x')
                    a=randint(-9,9)
                    b=randint(-9,9)
                    c=randint(-10,10)
                k=nsimplify(a/b)

                du = ['$%s\\ln\\abs{%sx+%s}+\\text{C}$'%(latex(k),latex(b),latex(c))
                    ]
                da= random.choice(du)
                s = ['$%s\\ln\\abs{%sx+%s}+\\text{C}$'%(latex(k*2),latex(b),latex(c)),
                    '$%s\\ln\\abs{%sx+%s}+\\text{C}$'%(latex(k*3),latex(b),latex(c)),
                    '$%s\\ln\\abs{%sx+%s}+\\text{C}$'%(latex(-k),latex(b),latex(c)),
                    '$%s\\ln\\abs{%sx+%s}+\\text{C}$'%(latex(-2*k),latex(b),latex(c)),
                    '$%s\\ln\\abs{%sx+%s}+\\text{C}$'%(latex(-3*k),latex(b),latex(c))
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('$\\displaystyle \\int{ \\dfrac{%s}{%sx+%s} \\text{d}x}$ bằng'
                                %(latex(a),latex(b),
                                latex(c)
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
                loigiai=('Ta có\\\\ \n'
                        '\\hspace*{1cm} $\\displaystyle \\int{ \\dfrac{%s}{%sx+%s} \\text{d}x}=%s\\displaystyle \\int{ \\dfrac{(%sx+%s)\'}{%sx+%s} \\text{d}x}=%s\\ln\\abs{%sx+%s}+\\text{C}$ . \\\\ \n'
                        %(latex(a),latex(b),
                        latex(c),latex(k),latex(b),latex(c),latex(b),latex(c),latex(k),latex(b),latex(c))

                        )
            if dang=='2':
                # Khai báo biến
                x=symbols('x')
                a=randint(1,9)
                b=randint(-9,9)
                c=randint(-10,10)
                while a==0 or b==0 or c==0:
                    x=symbols('x')
                    a=randint(1,9)
                    b=randint(-9,9)
                    c=randint(-10,10)
                k=nsimplify(a/b)

                du = ['$%se^{%sx+%s}+\\text{C}$'%(latex(k),latex(b),latex(c))
                    ]
                da= random.choice(du)
                s = ['$%se^{%sx+%s}+\\text{C}$'%(latex(k*2),latex(b),latex(c)),
                    '$%se^{%sx+%s}+\\text{C}$'%(latex(k*3),latex(b),latex(c)),
                    '$%se^{%sx+%s}+\\text{C}$'%(latex(-k),latex(b),latex(c)),
                    '$%se^{%sx+%s}+\\text{C}$'%(latex(-2*k),latex(b),latex(c)),
                    '$%se^{%sx+%s}+\\text{C}$'%(latex(-3*k),latex(b),latex(c))
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('$\\displaystyle \\int{%se^{%sx+%s} \\text{d}x}$ bằng'
                                %(latex(a),latex(b),
                                latex(c)
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
                loigiai=('Ta có\\\\ \n'
                        '\\hspace*{1cm} $\\displaystyle \\int{%se^{%sx+%s} \\text{d}x}=%s\\displaystyle \\int{ (%sx+%s)\'e^{%sx+%s} \\text{d}x}=%se^{%sx+%s}+\\text{C}$ . \\\\ \n'
                        %(latex(a),latex(b),
                        latex(c),latex(k),latex(b),latex(c),latex(b),latex(c),latex(k),latex(b),latex(c))

                        )
            if dang=='3':
                # Khai báo biến
                x=symbols('x')
                a=randint(1,9)
                b=randint(-9,9)
                c=randint(-10,10)
                e=randint(2,9)
                while a==0 or b==0 or c==0:
                    x=symbols('x')
                    a=randint(1,9)
                    b=randint(-9,9)
                    c=randint(-10,10)
                    e=randint(2,9)
                k=nsimplify(a/b)

                du = ['$%s\\cdot\\dfrac{%s^{%sx+%s}}{\\ln %s}+\\text{C}$'%(latex(k),latex(e),latex(b),latex(c),latex(e))
                    ]
                da= random.choice(du)
                s = ['$%s\\cdot\\dfrac{%s^{%sx+%s}}{\\ln %s}+\\text{C}$'%(latex(-k),latex(e),latex(b),latex(c),latex(e)),
                    '$%s\\cdot\\dfrac{%s^{%sx-%s}}{\\ln %s}+\\text{C}$'%(latex(k),latex(e),latex(b),latex(c),latex(e+1)),
                    '$\\dfrac{%s^{%sx+%s}}{\\ln %s}+\\text{C}$'%(latex(e),latex(b),latex(c+1),latex(e)),
                    '$\\dfrac{%s^{%sx-%s}}{\\ln %s}+\\text{C}$'%(latex(e),latex(b+1),latex(c),latex(e))
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('$\\displaystyle \\int{%s\\cdot%s^{%sx+%s} \\text{d}x}$ bằng'
                                %(latex(a),latex(e),latex(b),
                                latex(c)
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
                loigiai=('Ta có\\\\ \n'
                        '\\hspace*{1cm} $\\displaystyle \\int{%s\\cdot%s^{%sx+%s} \\text{d}x}=%s\\displaystyle \\int{ (%sx+%s)\'%s^{%sx+%s} \\text{d}x}=%s\\cdot\\dfrac{%s^{%sx+%s}}{\\ln %s}+\\text{C}$ . \\\\ \n'
                        %(latex(a),latex(e),latex(b),
                        latex(c),latex(k),latex(b),latex(c),latex(e),latex(b),latex(c),latex(k),latex(e),latex(b),latex(c),latex(e))

                        )
            if dang=='4':
                # Khai báo biến
                x=symbols('x')
                a=randint(-9,9)
                b=randint(-9,9)
                c=randint(-10,10)

                while a==0 or b==0 or c==0:
                    x=symbols('x')
                    a=randint(-9,9)
                    b=randint(-9,9)
                    c=randint(-10,10)

                k=nsimplify(a/b)

                du = ['$%s\\sin (%sx+%s)+\\text{C}$'%(latex(k),latex(b),latex(c))
                    ]
                da= random.choice(du)
                s = ['$%s\\sin (%sx+%s)+\\text{C}$'%(latex(k*2),latex(b),latex(c)),
                    '$%s\\cos (%sx+%s)+\\text{C}$'%(latex(k*3),latex(b),latex(c)),
                    '$%s\\sin (%sx+%s)+\\text{C}$'%(latex(-k),latex(b),latex(c)),
                    '$%s\\sin (%sx+%s)+\\text{C}$'%(latex(-2*k),latex(b),latex(c)),
                    '$%s\\cos (%sx+%s)+\\text{C}$'%(latex(-3*k),latex(b),latex(c))
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('$\\displaystyle \\int{%s\\cos (%sx+%s) \\text{d}x}$ bằng'
                                %(latex(a),latex(b),
                                latex(c)
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
                loigiai=('Ta có\\\\ \n'
                        '\\hspace*{1cm} $\\displaystyle \\int{%s\\cos (%sx+%s) \\text{d}x}=%s\\displaystyle \\int{  (%sx+%s)\' \\cos (%sx+%s) \\text{d}x}=%s\\sin (%sx+%s)+\\text{C}$ . \\\\ \n'
                        %(latex(a),latex(b),
                        latex(c),latex(k),latex(b),latex(c),latex(b),latex(c),latex(k),latex(b),latex(c))

                        )
            if dang=='5':
                # Khai báo biến
                x=symbols('x')
                a=randint(-9,9)
                b=randint(-9,9)
                c=randint(-10,10)

                while a==0 or b==0 or c==0:
                    x=symbols('x')
                    a=randint(-9,9)
                    b=randint(-9,9)
                    c=randint(-10,10)

                k=-nsimplify(a/b)

                du = ['$%s\\cos (%sx+%s)+\\text{C}$'%(latex(k),latex(b),latex(c))
                    ]
                da= random.choice(du)
                s = ['$%s\\sin (%sx+%s)+\\text{C}$'%(latex(k),latex(b),latex(c)),
                    '$%s\\cos (%sx+%s)+\\text{C}$'%(latex(-k),latex(b),latex(c)),
                    '$%s\\sin (%sx+%s)+\\text{C}$'%(latex(-k),latex(b),latex(c)),
                    '$%s\\cos (%sx+%s)+\\text{C}$'%(latex(-2*k),latex(b),latex(c)),
                    '$%s\\cos (%sx+%s)+\\text{C}$'%(latex(2*k),latex(b),latex(c))
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('$\\displaystyle \\int{%s\\sin (%sx+%s) \\text{d}x}$ bằng'
                                %(latex(a),latex(b),
                                latex(c)
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
                loigiai=('Ta có\\\\ \n'
                        '\\hspace*{1cm} $\\displaystyle \\int{%s\\sin (%sx+%s) \\text{d}x}=%s\\displaystyle \\int{ (%sx+%s)\' \\sin (%sx+%s) \\text{d}x}=%s\\cos (%sx+%s)+\\text{C}$ . \\\\ \n'
                        %(latex(a),latex(b),
                        latex(c),latex(-k),latex(b),latex(c),latex(b),latex(c),latex(k),latex(b),latex(c))

                        )
            if dang=='6':
                # Khai báo biến
                x=symbols('x')
                a=randint(-9,9)
                b=randint(-9,9)
                c=randint(-10,10)

                while a==0 or b==0 or c==0:
                    x=symbols('x')
                    a=randint(-9,9)
                    b=randint(-9,9)
                    c=randint(-10,10)

                k=nsimplify(a/b)

                du = ['$%s\\tan (%sx+%s)+\\text{C}$'%(latex(k),latex(b),latex(c))
                    ]
                da= random.choice(du)
                s = ['$%s\\cot (%sx+%s)+\\text{C}$'%(latex(k),latex(b),latex(c)),
                    '$%s\\tan (%sx+%s)+\\text{C}$'%(latex(-k),latex(b),latex(c)),
                    '$%s\\cot (%sx+%s)+\\text{C}$'%(latex(-k),latex(b),latex(c)),
                    '$%s\\tan (%sx+%s)+\\text{C}$'%(latex(-2*k),latex(b),latex(c)),
                    '$%s\\tan (%sx+%s)+\\text{C}$'%(latex(2*k),latex(b),latex(c))
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('$\\displaystyle \\int{\\dfrac{%s}{\\cos^2 (%sx+%s)} \\text{d}x}$ bằng'
                                %(latex(a),latex(b),
                                latex(c)
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
                loigiai=('Ta có\\\\ \n'
                        '\\hspace*{1cm} $\\displaystyle \\int{\\dfrac{%s}{\\cos^2 (%sx+%s)} \\text{d}x}=%s\\displaystyle \\int{\\dfrac{(%sx+%s)\'}{\\cos^2 (%sx+%s)} \\text{d}x}=%s\\tan (%sx+%s)+\\text{C}$ . \\\\ \n'
                        %(latex(a),latex(b),
                        latex(c),latex(k),latex(b),latex(c),latex(b),latex(c),latex(k),latex(b),latex(c))

                        )
            if dang=='7':
                # Khai báo biến
                x=symbols('x')
                a=randint(-9,9)
                b=randint(-9,9)
                c=randint(-10,10)

                while a==0 or b==0 or c==0:
                    x=symbols('x')
                    a=randint(-9,9)
                    b=randint(-9,9)
                    c=randint(-10,10)

                k=-nsimplify(a/b)

                du = ['$%s\\cot (%sx+%s)+\\text{C}$'%(latex(k),latex(b),latex(c))
                    ]
                da= random.choice(du)
                s = ['$%s\\tan (%sx+%s)+\\text{C}$'%(latex(k),latex(b),latex(c)),
                    '$%s\\tan (%sx+%s)+\\text{C}$'%(latex(-k),latex(b),latex(c)),
                    '$%s\\cot (%sx+%s)+\\text{C}$'%(latex(-k),latex(b),latex(c)),
                    '$%s\\cot (%sx+%s)+\\text{C}$'%(latex(-2*k),latex(b),latex(c)),
                    '$%s\\cot (%sx+%s)+\\text{C}$'%(latex(2*k),latex(b),latex(c))
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('$\\displaystyle \\int{\\dfrac{%s}{\\sin^2 (%sx+%s)} \\text{d}x}$ bằng'
                                %(latex(a),latex(b),
                                latex(c)
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
                loigiai=('Ta có\\\\ \n'
                        '\\hspace*{1cm} $\\displaystyle \\int{\\dfrac{%s}{\\sin^2 (%sx+%s)} \\text{d}x}=%s\\displaystyle \\int{\\dfrac{(%sx+%s)\'}{\\sin^2 (%sx+%s)} \\text{d}x}=%s\\cot (%sx+%s)+\\text{C}$ . \\\\ \n'
                        %(latex(a),latex(b),
                        latex(c),latex(-k),latex(b),latex(c),latex(b),latex(c),latex(k),latex(b),latex(c))

                        )
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('--', '+').replace('+-', '-').replace('1x', 'x').replace('-1x', '-x').replace('1\\displaystyle', '\\displaystyle').replace('-1\\displaystyle', '-\\displaystyle').replace('1\\sin', '\\sin').replace('-1\\sin', '-\\sin').replace('1\\tan', '\\tan').replace('-1\\tan', '-\\tan').replace('1\\cos', '\\cos').replace('-1\\cos', '-\\cos').replace('1\\cot', '\\cot').replace('-1\\cot', '-\\cot').replace('1\\cdot', '').replace('-1\\cdot', '-').replace('1e', 'e').replace('-1e', '-e').replace('1\\ln', '\\ln').replace('-1\\ln', '-\\ln')
            return content


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


def bt_dang12_p1_b3_c1_ds11(self):
            # Khai báo biến
            lisdang=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                a = randint(-20,-1)
                b = randint(-10,10)
                c = randint(2,10)
                d = randint(-10,10)

                while b==0 or d==0:

                    a = randint(-20,-1)
                    b = randint(1,10)
                    c = randint(2,10)
                    d = randint(-10,10)
                M = -a+d
                m = a+d
                kq = M+m

                du = ['$%s$'%(latex(kq))

                                ]
                da= random.choice(du)

                da= random.choice(du)
                s = ['$%s$'%(latex(kq+1)),
                    '$%s$'%(latex(kq+2)),
                    '$%s$'%(latex(kq-1)),
                    '$%s$'%(latex(kq-2)),
                    '$%s$'%(latex(kq-3)),
                    '$%s$'%(latex(kq+3)),
                    '$%s$'%(latex(kq*2)),
                    '$%s$'%(latex(kq*3)),

                            ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                    # Câu hỏi
                noidungcauhoi = '''Tổng giá trị lớn nhất và giá trị nhỏ nhất của hàm số $y = %s\\sin(%sx+\\dfrac{\\pi}{%s}) +%s$ bằng \n''' %(latex(a),latex(b),latex(c),latex(d))
                    # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Tập xác định của hàm số $\\mathscr{D}=\\mathbb{R}$.\\\\ \n'
                            '''Ta có \\\\ \n'''
                            '''\\hspace*{1cm} $-1 \\leq \\sin(%sx+\\dfrac{\\pi}{%s}) \\leq 1 \\Leftrightarrow %s \\geq %s\\sin(%sx+\\dfrac{\\pi}{%s}) \\geq %s$\\\\ \n'''
                            '''\\hspace*{1cm} $\\Leftrightarrow %s +%s \\geq %s\\sin(%sx+\\dfrac{\\pi}{%s}) +%s \\geq %s +%s \\Leftrightarrow %s \\geq y \\geq %s$.\\\\ \n'''
                            '''Vậy tổng giá trị lớn nhất và nhỏ nhất của hàm số là $%s+%s=%s$.\\\\ \n'''
                            %(latex(b),latex(c),latex(-a),latex(a),latex(b),latex(c),latex(a),
                                latex(-a),latex(d),latex(a),latex(b),latex(c),latex(d),latex(a),latex(d),latex(M),latex(m),
                                latex(M),latex(m),latex(kq),

                            ))
            if dang=='2':
                # Khai báo biến
                a = randint(-20,-1)
                b = randint(-10,10)
                c = randint(2,10)
                d = randint(-10,10)

                while b==0 or d==0:

                    a = randint(-20,-1)
                    b = randint(1,10)
                    c = randint(2,10)
                    d = randint(-10,10)
                M = -a+d
                m = a+d

                du = ['$T=[%s;%s]$'%(latex(m),latex(M))

                                ]
                da= random.choice(du)


                da= random.choice(du)
                s = ['$T=[%s;%s]$'%(latex(m+1),latex(M+1)),
                    '$T=[%s;%s]$'%(latex(m-1),latex(M-1)),
                    '$T=[%s;%s]$'%(latex(m*2),latex(M*2)),
                    '$T=[%s;%s]$'%(latex(m*3),latex(M*3)),
                    '$T=[%s;%s]$'%(latex(m+2),latex(M+2)),
                    '$T=[%s;%s]$'%(latex(m-2),latex(M-2)),
                    '$T=[%s;%s]$'%(latex(m-3),latex(M-3)),

                            ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                    # Câu hỏi
                noidungcauhoi = '''Tập giá trị của hàm số $y = %s\\sin(%sx+\\dfrac{\\pi}{%s}) +%s$ là \n''' %(latex(a),latex(b),latex(c),latex(d))
                    # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Tập xác định của hàm số $\\mathscr{D}=\\mathbb{R}$.\\\\ \n'
                            '''Ta có \\\\ \n'''
                            '''\\hspace*{1cm} $-1 \\leq \\sin(%sx+\\dfrac{\\pi}{%s}) \\leq 1 \\Leftrightarrow %s \\geq %s\\sin(%sx+\\dfrac{\\pi}{%s}) \\geq %s$\\\\ \n'''
                            '''\\hspace*{1cm} $\\Leftrightarrow %s +%s \\geq %s\\sin(%sx+\\dfrac{\\pi}{%s}) +%s \\geq %s +%s \\Leftrightarrow %s \\geq y \\geq %s$.\\\\ \n'''
                            '''Vậy tập giá trị của hàm số là $T=[%s;%s]$.\\\\ \n'''
                            %(latex(b),latex(c),latex(-a),latex(a),latex(b),latex(c),latex(a),
                                latex(-a),latex(d),latex(a),latex(b),latex(c),latex(d),latex(a),latex(d),latex(M),latex(m),
                                latex(m),latex(M),

                            ))
            if dang=='3':
                # Khai báo biến
                a = randint(-20,-1)
                b = randint(-10,10)
                c = randint(2,10)
                d = randint(-10,10)

                while b==0 or d==0:

                    a = randint(-20,-1)
                    b = randint(1,10)
                    c = randint(2,10)
                    d = randint(-10,10)
                M = -a+d
                m = a+d
                kq = m

                du = ['$%s$'%(latex(kq))

                                ]
                da= random.choice(du)


                da= random.choice(du)
                s = ['$%s$'%(latex(kq+1)),
                    '$%s$'%(latex(kq+2)),
                    '$%s$'%(latex(kq-1)),
                    '$%s$'%(latex(kq-2)),
                    '$%s$'%(latex(kq-3)),
                    '$%s$'%(latex(kq+3)),
                    '$%s$'%(latex(kq*2)),
                    '$%s$'%(latex(kq*3)),

                            ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                    # Câu hỏi
                noidungcauhoi = '''Giá trị nhỏ nhất của hàm số $y = %s\\sin(%sx+\\dfrac{\\pi}{%s}) +%s$ bằng \n''' %(latex(a),latex(b),latex(c),latex(d))
                    # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Tập xác định của hàm số $\\mathscr{D}=\\mathbb{R}$.\\\\ \n'
                            '''Ta có \\\\ \n'''
                            '''\\hspace*{1cm} $-1 \\leq \\sin(%sx+\\dfrac{\\pi}{%s}) \\leq 1 \\Leftrightarrow %s \\geq %s\\sin(%sx+\\dfrac{\\pi}{%s}) \\geq %s$\\\\ \n'''
                            '''\\hspace*{1cm} $\\Leftrightarrow %s +%s \\geq %s\\sin(%sx+\\dfrac{\\pi}{%s}) +%s \\geq %s +%s \\Leftrightarrow %s \\geq y \\geq %s$.\\\\ \n'''
                            '''Vậy giá trị nhỏ nhất của hàm số là $%s$.\\\\ \n'''
                            %(latex(b),latex(c),latex(-a),latex(a),latex(b),latex(c),latex(a),
                                latex(-a),latex(d),latex(a),latex(b),latex(c),latex(d),latex(a),latex(d),latex(M),latex(m),
                                latex(kq),

                            ))
            if dang=='4':
                # Khai báo biến
                a = randint(-20,-1)
                b = randint(-10,10)
                c = randint(2,10)
                d = randint(-10,10)

                while b==0 or d==0:

                    a = randint(-20,-1)
                    b = randint(1,10)
                    c = randint(2,10)
                    d = randint(-10,10)
                M = -a+d
                m = a+d
                kq = M

                du = ['$%s$'%(latex(kq))

                                ]
                da= random.choice(du)


                da= random.choice(du)
                s = ['$%s$'%(latex(kq+1)),
                    '$%s$'%(latex(kq+2)),
                    '$%s$'%(latex(kq-1)),
                    '$%s$'%(latex(kq-2)),
                    '$%s$'%(latex(kq-3)),
                    '$%s$'%(latex(kq+3)),
                    '$%s$'%(latex(kq*2)),
                    '$%s$'%(latex(kq*3)),

                            ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                    # Câu hỏi
                noidungcauhoi = '''Giá trị lớn nhất của hàm số $y = %s\\sin(%sx+\\dfrac{\\pi}{%s}) +%s$ bằng \n''' %(latex(a),latex(b),latex(c),latex(d))
                    # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Tập xác định của hàm số $\\mathscr{D}=\\mathbb{R}$.\\\\ \n'
                            '''Ta có \\\\ \n'''
                            '''\\hspace*{1cm} $-1 \\leq \\sin(%sx+\\dfrac{\\pi}{%s}) \\leq 1 \\Leftrightarrow %s \\geq %s\\sin(%sx+\\dfrac{\\pi}{%s}) \\geq %s$\\\\ \n'''
                            '''\\hspace*{1cm} $\\Leftrightarrow %s +%s \\geq %s\\sin(%sx+\\dfrac{\\pi}{%s}) +%s \\geq %s +%s \\Leftrightarrow %s \\geq y \\geq %s$.\\\\ \n'''
                            '''Vậy giá trị lớn nhất của hàm số là $%s$.\\\\ \n'''
                            %(latex(b),latex(c),latex(-a),latex(a),latex(b),latex(c),latex(a),
                                latex(-a),latex(d),latex(a),latex(b),latex(c),latex(d),latex(a),latex(d),latex(M),latex(m),
                                latex(kq),

                            ))
            if dang=='5':
                # Khai báo biến
                a = randint(-20,-2)
                b = randint(-10,10)
                c = randint(2,10)
                d = randint(-10,10)
                e = randint(1,20)
                f = randint(-5,10)
                while b==0 or d==0:

                    a = randint(-20,-2)
                    b = randint(1,10)
                    c = randint(2,10)
                    d = randint(-10,10)
                    e = randint(1,20)
                    f = randint(-5,10)
                M = -a+d
                m = a+d
                kq = e*M + f*m

                du = ['$P=%s$'%(latex(kq))

                                ]
                da= random.choice(du)


                da= random.choice(du)
                s = ['$P=%s$'%(latex(kq+1)),
                    '$P=%s$'%(latex(kq+2)),
                    '$P=%s$'%(latex(kq-1)),
                    '$P=%s$'%(latex(kq-2)),
                    '$P=%s$'%(latex(kq-3)),
                    '$P=%s$'%(latex(kq+3)),
                    '$P=%s$'%(latex(kq*2)),
                    '$P=%s$'%(latex(kq*3)),

                            ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                    # Câu hỏi
                noidungcauhoi = '''Cho hàm số $y = %s\\sin(%sx+\\dfrac{\\pi}{%s}) +%s$. Gọi $M, m$ lần lượt là giá trị lớn nhất và giá trị nhỏ nhất của hàm số. Giá trị của biểu thức $P=%sM+%sm$ bằng \n''' %(latex(a),latex(b),latex(c),latex(d),latex(e),latex(f))
                    # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Tập xác định của hàm số $\\mathscr{D}=\\mathbb{R}$.\\\\ \n'
                        '''Ta có \\\\ \n'''
                        '''\\hspace*{1cm} $-1 \\leq \\sin(%sx+\\dfrac{\\pi}{%s}) \\leq 1 \\Leftrightarrow %s \\geq %s\\sin(%sx+\\dfrac{\\pi}{%s}) \\geq %s$\\\\ \n'''
                        '''\\hspace*{1cm} $\\Leftrightarrow %s +%s \\geq %s\\sin(%sx+\\dfrac{\\pi}{%s}) +%s \\geq %s +%s \\Leftrightarrow %s \\geq y \\geq %s$.\\\\ \n'''
                        '''Suy ra\\\\ \n'''
                        '''\\hspace*{1cm} Giá trị lớn nhất của hàm số là $M=%s$.\\\\ \n'''
                        '''\\hspace*{1cm} Giá trị nhỏ nhất của hàm số là $m=%s$.\\\\ \n'''
                            '''Vậy giá trị $P=%s\\cdot(%s)+%s\\cdot(%s)=%s$.\\\\ \n'''
                            %(latex(b),latex(c),latex(-a),latex(a),latex(b),latex(c),latex(a),
                                latex(-a),latex(d),latex(a),latex(b),latex(c),latex(d),latex(a),latex(d),latex(M),latex(m),
                                latex(M),latex(m),
                                latex(e),latex(M),latex(f),latex(m),latex(kq),

                            ))
            if dang=='6':
                # Khai báo biến
                a = randint(1,20)
                b = randint(-5,10)
                c = randint(2,10)
                d = randint(-10,10)
                e = randint(1,20)
                f = randint(-5,10)

                while b==0 or d==0:

                    a = randint(1,20)
                    b = randint(-5,10)
                    c = randint(2,10)
                    d = randint(-10,10)
                    e = randint(1,20)
                    f = randint(-5,10)
                m = -a+d
                M = a+d
                kq = e*M + f*m

                du = ['$P=%s$'%(latex(kq))

                                ]
                da= random.choice(du)


                da= random.choice(du)
                s = ['$P=%s$'%(latex(kq+1)),
                    '$P=%s$'%(latex(kq+2)),
                    '$P=%s$'%(latex(kq-1)),
                    '$P=%s$'%(latex(kq-2)),
                    '$P=%s$'%(latex(kq-3)),
                    '$P=%s$'%(latex(kq+3)),
                    '$P=%s$'%(latex(kq*2)),
                    '$P=%s$'%(latex(kq*3)),

                            ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                    # Câu hỏi
                noidungcauhoi = '''Cho hàm số $y = %s\\sin(%sx+\\dfrac{\\pi}{%s}) +%s$. Gọi $M, m$ lần lượt là giá trị lớn nhất và giá trị nhỏ nhất của hàm số. Giá trị của biểu thức $P=%sM+%sm$ bằng \n''' %(latex(a),latex(b),latex(c),latex(d),latex(e),latex(f))
                    # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Tập xác định của hàm số $\\mathscr{D}=\\mathbb{R}$.\\\\ \n'
                            '''Ta có \\\\ \n'''
                            '''\\hspace*{1cm} $-1 \\leq \\sin(%sx+\\dfrac{\\pi}{%s}) \\leq 1 \\Leftrightarrow -%s \\leq %s\\sin(%sx+\\dfrac{\\pi}{%s}) \\leq %s$\\\\ \n'''
                            '''\\hspace*{1cm} $\\Leftrightarrow -%s +%s \\leq %s\\sin(%sx+\\dfrac{\\pi}{%s}) +%s \\leq %s +%s \\Leftrightarrow %s \\leq y \\leq %s$.\\\\ \n'''
                            '''Suy ra\\\\ \n'''
                            '''\\hspace*{1cm} Giá trị lớn nhất của hàm số là $M=%s$.\\\\ \n'''
                            '''\\hspace*{1cm} Giá trị nhỏ nhất của hàm số là $m=%s$.\\\\ \n'''
                            '''Vậy giá trị $P=%s\\cdot(%s)+%s\\cdot(%s)=%s$.\\\\ \n'''
                            %(latex(b),latex(c),latex(a),latex(a),latex(b),latex(c),latex(a),
                                latex(a),latex(d),latex(a),latex(b),latex(c),latex(d),latex(a),latex(d),latex(m),latex(M),
                                latex(M),latex(m),
                                latex(e),latex(M),latex(f),latex(m),latex(kq),

                            ))
            if dang=='7':
                # Khai báo biến
                a = randint(1,20)
                b = randint(-5,10)
                c = randint(2,10)
                d = randint(-10,10)


                while b==0 or d==0:

                    a = randint(1,20)
                    b = randint(-5,10)
                    c = randint(2,10)
                    d = randint(-10,10)

                m = -a+d
                M = a+d
                kq = M+m

                du = ['$%s$'%(latex(kq))

                                ]
                da= random.choice(du)


                da= random.choice(du)
                s = ['$%s$'%(latex(kq+1)),
                    '$%s$'%(latex(kq+2)),
                    '$%s$'%(latex(kq-1)),
                    '$%s$'%(latex(kq-2)),
                    '$%s$'%(latex(kq-3)),
                    '$%s$'%(latex(kq+3)),
                    '$%s$'%(latex(kq*2)),
                    '$%s$'%(latex(kq*3)),

                            ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                    # Câu hỏi
                noidungcauhoi = '''Tổng giá trị lớn nhất và giá trị nhỏ nhất của hàm số $y = %s\\sin(%sx+\\dfrac{\\pi}{%s}) +%s$ bằng \n''' %(latex(a),latex(b),latex(c),latex(d))
                    # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Tập xác định của hàm số $\\mathscr{D}=\\mathbb{R}$.\\\\ \n'
                            '''Ta có \\\\ \n'''
                            '''\\hspace*{1cm} $-1 \\leq \\sin(%sx+\\dfrac{\\pi}{%s}) \\leq 1 \\Leftrightarrow -%s \\leq %s\\sin(%sx+\\dfrac{\\pi}{%s}) \\leq %s$\\\\ \n'''
                            '''\\hspace*{1cm} $\\Leftrightarrow -%s +%s \\leq %s\\sin(%sx+\\dfrac{\\pi}{%s}) +%s \\leq %s +%s \\Leftrightarrow %s \\leq y \\leq %s$.\\\\ \n'''
                            '''Vậy tổng giá trị lớn nhất và nhỏ nhất của hàm số là $%s+%s=%s$.\\\\ \n'''
                            %(latex(b),latex(c),latex(a),latex(a),latex(b),latex(c),latex(a),
                                latex(a),latex(d),latex(a),latex(b),latex(c),latex(d),latex(a),latex(d),latex(m),latex(M),
                                latex(M),latex(m),latex(kq),

                            ))
            if dang=='8':
                # Khai báo biến
                a = randint(1,20)
                b = randint(-5,10)
                c = randint(2,10)
                d = randint(-10,10)

                while b==0 or d==0:

                    a = randint(1,20)
                    b = randint(-5,10)
                    c = randint(2,10)
                    d = randint(-10,10)
                m = -a+d
                M = a+d

                du = ['$T=[%s;%s]$'%(latex(m),latex(M))

                                ]
                da= random.choice(du)


                da= random.choice(du)
                s = ['$T=[%s;%s]$'%(latex(m+1),latex(M+1)),
                    '$T=[%s;%s]$'%(latex(m-1),latex(M-1)),
                    '$T=[%s;%s]$'%(latex(m*2),latex(M*2)),
                    '$T=[%s;%s]$'%(latex(m*3),latex(M*3)),
                    '$T=[%s;%s]$'%(latex(m+2),latex(M+2)),
                    '$T=[%s;%s]$'%(latex(m-2),latex(M-2)),
                    '$T=[%s;%s]$'%(latex(m-3),latex(M-3)),

                            ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                    # Câu hỏi
                noidungcauhoi = '''Tập giá trị của hàm số $y = %s\\sin(%sx+\\dfrac{\\pi}{%s}) +%s$ là \n''' %(latex(a),latex(b),latex(c),latex(d))
                    # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Tập xác định của hàm số $\\mathscr{D}=\\mathbb{R}$.\\\\ \n'
                            '''Ta có \\\\ \n'''
                            '''\\hspace*{1cm} $-1 \\leq \\sin(%sx+\\dfrac{\\pi}{%s}) \\leq 1 \\Leftrightarrow -%s \\leq %s\\sin(%sx+\\dfrac{\\pi}{%s}) \\leq %s$\\\\ \n'''
                            '''\\hspace*{1cm} $\\Leftrightarrow -%s + %s \\leq %s\\sin(%sx+\\dfrac{\\pi}{%s}) + %s \\leq %s + %s \\Leftrightarrow %s \\leq y \\leq %s$.\\\\ \n'''
                            '''Vậy tập giá trị của hàm số là $T=[%s;%s]$.\\\\ \n'''
                            %(latex(b),latex(c),latex(a),latex(a),latex(b),latex(c),latex(a),
                                latex(a),latex(d),latex(a),latex(b),latex(c),latex(d),latex(a),latex(d),latex(m),latex(M),
                                latex(m),latex(M),

                            ))
            if dang=='9':
                # Khai báo biến
                a = randint(1,20)
                b = randint(-5,10)
                c = randint(2,10)
                d = randint(-10,10)


                while b==0 or d==0:

                    a = randint(1,20)
                    b = randint(-5,10)
                    c = randint(2,10)
                    d = randint(-10,10)

                m = -a+d
                M = a+d
                kq = m

                du = ['$%s$'%(latex(kq))

                                ]
                da= random.choice(du)


                da= random.choice(du)
                s = ['$%s$'%(latex(kq+1)),
                    '$%s$'%(latex(kq+2)),
                    '$%s$'%(latex(kq-1)),
                    '$%s$'%(latex(kq-2)),
                    '$%s$'%(latex(kq-3)),
                    '$%s$'%(latex(kq+3)),
                    '$%s$'%(latex(kq*2)),
                    '$%s$'%(latex(kq*3)),

                            ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                    # Câu hỏi
                noidungcauhoi = '''Giá trị nhỏ nhất của hàm số $y = %s\\sin(%sx+\\dfrac{\\pi}{%s}) +%s$ bằng \n''' %(latex(a),latex(b),latex(c),latex(d))
                    # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Tập xác định của hàm số $\\mathscr{D}=\\mathbb{R}$.\\\\ \n'
                            '''Ta có \\\\ \n'''
                            '''\\hspace*{1cm} $-1 \\leq \\sin(%sx+\\dfrac{\\pi}{%s}) \\leq 1 \\Leftrightarrow -%s \\leq %s\\sin(%sx+\\dfrac{\\pi}{%s}) \\leq %s$\\\\ \n'''
                            '''\\hspace*{1cm} $\\Leftrightarrow -%s +%s \\leq %s\\sin(%sx+\\dfrac{\\pi}{%s}) +%s \\leq %s +%s \\Leftrightarrow %s \\leq y \\leq %s$.\\\\ \n'''
                            '''Vậy giá trị nhỏ nhất của hàm số là $%s$.\\\\ \n'''
                            %(latex(b),latex(c),latex(a),latex(a),latex(b),latex(c),latex(a),
                                latex(a),latex(d),latex(a),latex(b),latex(c),latex(d),latex(a),latex(d),latex(m),latex(M),
                                latex(kq),

                            ))
            if dang=='10':
                # Khai báo biến
                a = randint(1,20)
                b = randint(-5,10)
                c = randint(2,10)
                d = randint(-10,10)


                while b==0 or d==0:

                    a = randint(1,20)
                    b = randint(-5,10)
                    c = randint(2,10)
                    d = randint(-10,10)

                m = -a+d
                M = a+d
                kq = M

                du = ['$%s$'%(latex(kq))

                                ]
                da= random.choice(du)


                da= random.choice(du)
                s = ['$%s$'%(latex(kq+1)),
                    '$%s$'%(latex(kq+2)),
                    '$%s$'%(latex(kq-1)),
                    '$%s$'%(latex(kq-2)),
                    '$%s$'%(latex(kq-3)),
                    '$%s$'%(latex(kq+3)),
                    '$%s$'%(latex(kq*2)),
                    '$%s$'%(latex(kq*3)),

                            ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                    # Câu hỏi
                noidungcauhoi = '''Giá trị lớn nhất của hàm số $y = %s\\sin(%sx+\\dfrac{\\pi}{%s}) +%s$ bằng \n''' %(latex(a),latex(b),latex(c),latex(d))
                    # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Tập xác định của hàm số $\\mathscr{D}=\\mathbb{R}$.\\\\ \n'
                            '''Ta có \\\\ \n'''
                            '''\\hspace*{1cm} $-1 \\leq \\sin(%sx+\\dfrac{\\pi}{%s}) \\leq 1 \\Leftrightarrow -%s \\leq %s\\sin(%sx+\\dfrac{\\pi}{%s}) \\leq %s$\\\\ \n'''
                            '''\\hspace*{1cm} $\\Leftrightarrow -%s +%s \\leq %s\\sin(%sx+\\dfrac{\\pi}{%s}) +%s \\leq %s +%s \\Leftrightarrow %s \\leq y \\leq %s$.\\\\ \n'''
                            '''Vậy giá trị lớn nhất của hàm số là $%s$.\\\\ \n'''
                            %(latex(b),latex(c),latex(a),latex(a),latex(b),latex(c),latex(a),
                                latex(a),latex(d),latex(a),latex(b),latex(c),latex(d),latex(a),latex(d),latex(m),latex(M),
                                latex(kq),

                            ))
            if dang=='11':
                # Khai báo biến
                a = randint(-20,-1)
                b = randint(-10,10)
                c = randint(2,10)
                d = randint(-10,10)

                while b==0 or d==0:

                    a = randint(-20,-1)
                    b = randint(1,10)
                    c = randint(2,10)
                    d = randint(-10,10)
                M = -a+d
                m = a+d
                kq = M+m

                du = ['$%s$'%(latex(kq))

                                ]
                da= random.choice(du)


                da= random.choice(du)
                s = ['$%s$'%(latex(kq+1)),
                    '$%s$'%(latex(kq+2)),
                    '$%s$'%(latex(kq-1)),
                    '$%s$'%(latex(kq-2)),
                    '$%s$'%(latex(kq-3)),
                    '$%s$'%(latex(kq+3)),
                    '$%s$'%(latex(kq*2)),
                    '$%s$'%(latex(kq*3)),

                            ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                    # Câu hỏi
                noidungcauhoi = '''Tổng giá trị lớn nhất và giá trị nhỏ nhất của hàm số $y = %s\\cos(%sx+\\dfrac{\\pi}{%s}) +%s$ bằng \n''' %(latex(a),latex(b),latex(c),latex(d))
                    # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Tập xác định của hàm số $\\mathscr{D}=\\mathbb{R}$.\\\\ \n'
                            '''Ta có \\\\ \n'''
                            '''\\hspace*{1cm} $-1 \\leq \\cos(%sx+\\dfrac{\\pi}{%s}) \\leq 1 \\Leftrightarrow %s \\geq %s\\cos(%sx+\\dfrac{\\pi}{%s}) \\geq %s$\\\\ \n'''
                            '''\\hspace*{1cm} $\\Leftrightarrow %s +%s \\geq %s\\cos(%sx+\\dfrac{\\pi}{%s}) +%s \\geq %s +%s \\Leftrightarrow %s \\geq y \\geq %s$.\\\\ \n'''
                            '''Vậy tổng giá trị lớn nhất và nhỏ nhất của hàm số là $%s+%s=%s$.\\\\ \n'''

                            %(latex(b),latex(c),latex(-a),latex(a),latex(b),latex(c),latex(a),
                                latex(-a),latex(d),latex(a),latex(b),latex(c),latex(d),latex(a),latex(d),latex(M),latex(m),
                                latex(M),latex(m),latex(kq),

                            ))
            if dang=='12':
                # Khai báo biến
                a = randint(-20,-1)
                b = randint(-10,10)
                c = randint(2,10)
                d = randint(-10,10)

                while b==0 or d==0:

                    a = randint(-20,-1)
                    b = randint(1,10)
                    c = randint(2,10)
                    d = randint(-10,10)
                M = -a+d
                m = a+d

                du = ['$T=[%s;%s]$'%(latex(m),latex(M))

                                ]
                da= random.choice(du)


                da= random.choice(du)
                s = ['$T=[%s;%s]$'%(latex(m+1),latex(M+1)),
                    '$T=[%s;%s]$'%(latex(m-1),latex(M-1)),
                    '$T=[%s;%s]$'%(latex(m*2),latex(M*2)),
                    '$T=[%s;%s]$'%(latex(m*3),latex(M*3)),
                    '$T=[%s;%s]$'%(latex(m+2),latex(M+2)),
                    '$T=[%s;%s]$'%(latex(m-2),latex(M-2)),
                    '$T=[%s;%s]$'%(latex(m-3),latex(M-3)),

                            ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                    # Câu hỏi
                noidungcauhoi = '''Tập giá trị của hàm số $y = %s\\cos(%sx+\\dfrac{\\pi}{%s}) +%s$ là \n''' %(latex(a),latex(b),latex(c),latex(d))
                    # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Tập xác định của hàm số $\\mathscr{D}=\\mathbb{R}$.\\\\ \n'
                            '''Ta có \\\\ \n'''
                            '''\\hspace*{1cm} $-1 \\leq \\cos(%sx+\\dfrac{\\pi}{%s}) \\leq 1 \\Leftrightarrow %s \\geq %s\\cos(%sx+\\dfrac{\\pi}{%s}) \\geq %s$\\\\ \n'''
                            '''\\hspace*{1cm} $\\Leftrightarrow %s +%s \\geq %s\\cos(%sx+\\dfrac{\\pi}{%s}) +%s \\geq %s +%s \\Leftrightarrow %s \\geq y \\geq %s$.\\\\ \n'''
                            '''Vậy tập giá trị của hàm số là $T=[%s;%s]$.\\\\ \n'''
                            %(latex(b),latex(c),latex(-a),latex(a),latex(b),latex(c),latex(a),
                                latex(-a),latex(d),latex(a),latex(b),latex(c),latex(d),latex(a),latex(d),latex(M),latex(m),
                                latex(m),latex(M),

                            ))
            if dang=='13':
                # Khai báo biến
                a = randint(-20,-1)
                b = randint(-10,10)
                c = randint(2,10)
                d = randint(-10,10)

                while b==0 or d==0:

                    a = randint(-20,-1)
                    b = randint(1,10)
                    c = randint(2,10)
                    d = randint(-10,10)
                M = -a+d
                m = a+d
                kq = m

                du = ['$%s$'%(latex(kq))

                                ]
                da= random.choice(du)


                da= random.choice(du)
                s = ['$%s$'%(latex(kq+1)),
                    '$%s$'%(latex(kq+2)),
                    '$%s$'%(latex(kq-1)),
                    '$%s$'%(latex(kq-2)),
                    '$%s$'%(latex(kq-3)),
                    '$%s$'%(latex(kq+3)),
                    '$%s$'%(latex(kq*2)),
                    '$%s$'%(latex(kq*3)),

                            ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                    # Câu hỏi
                noidungcauhoi = '''Giá trị nhỏ nhất của hàm số $y = %s\\cos(%sx+\\dfrac{\\pi}{%s}) +%s$ bằng \n''' %(latex(a),latex(b),latex(c),latex(d))
                    # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Tập xác định của hàm số $\\mathscr{D}=\\mathbb{R}$.\\\\ \n'
                            '''Ta có \\\\ \n'''
                            '''\\hspace*{1cm} $-1 \\leq \\cos(%sx+\\dfrac{\\pi}{%s}) \\leq 1 \\Leftrightarrow %s \\geq %s\\cos(%sx+\\dfrac{\\pi}{%s}) \\geq %s$\\\\ \n'''
                            '''\\hspace*{1cm} $\\Leftrightarrow %s +%s \\geq %s\\cos(%sx+\\dfrac{\\pi}{%s}) +%s \\geq %s +%s \\Leftrightarrow %s \\geq y \\geq %s$.\\\\ \n'''
                            '''Vậy giá trị nhỏ nhất của hàm số là $%s$.\\\\ \n'''
                            %(latex(b),latex(c),latex(-a),latex(a),latex(b),latex(c),latex(a),
                                latex(-a),latex(d),latex(a),latex(b),latex(c),latex(d),latex(a),latex(d),latex(M),latex(m),
                                latex(kq),

                            ))
            if dang=='14':
                # Khai báo biến
                a = randint(-20,-1)
                b = randint(-10,10)
                c = randint(2,10)
                d = randint(-10,10)

                while b==0 or d==0:

                    a = randint(-20,-1)
                    b = randint(1,10)
                    c = randint(2,10)
                    d = randint(-10,10)
                M = -a+d
                m = a+d
                kq = M

                du = ['$%s$'%(latex(kq))

                                ]
                da= random.choice(du)


                da= random.choice(du)
                s = ['$%s$'%(latex(kq+1)),
                    '$%s$'%(latex(kq+2)),
                    '$%s$'%(latex(kq-1)),
                    '$%s$'%(latex(kq-2)),
                    '$%s$'%(latex(kq-3)),
                    '$%s$'%(latex(kq+3)),
                    '$%s$'%(latex(kq*2)),
                    '$%s$'%(latex(kq*3)),

                            ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                    # Câu hỏi
                noidungcauhoi = '''Giá trị lớn nhất của hàm số $y = %s\\cos(%sx+\\dfrac{\\pi}{%s}) +%s$ bằng \n''' %(latex(a),latex(b),latex(c),latex(d))
                    # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Tập xác định của hàm số $\\mathscr{D}=\\mathbb{R}$.\\\\ \n'
                            '''Ta có \\\\ \n'''
                            '''\\hspace*{1cm} $-1 \\leq \\cos(%sx+\\dfrac{\\pi}{%s}) \\leq 1 \\Leftrightarrow %s \\geq %s\\cos(%sx+\\dfrac{\\pi}{%s}) \\geq %s$\\\\ \n'''
                            '''\\hspace*{1cm} $\\Leftrightarrow %s +%s \\geq %s\\cos(%sx+\\dfrac{\\pi}{%s}) +%s \\geq %s +%s \\Leftrightarrow %s \\geq y \\geq %s$.\\\\ \n'''
                            '''Vậy giá trị lớn nhất của hàm số là $%s$.\\\\ \n'''
                            %(latex(b),latex(c),latex(-a),latex(a),latex(b),latex(c),latex(a),
                                latex(-a),latex(d),latex(a),latex(b),latex(c),latex(d),latex(a),latex(d),latex(M),latex(m),
                                latex(kq),

                            ))
            if dang=='15':
                # Khai báo biến
                a = randint(-20,-1)
                b = randint(-10,10)
                c = randint(2,10)
                d = randint(-10,10)
                e = randint(1,20)
                f = randint(-5,10)
                while b==0 or d==0:

                    a = randint(-20,-1)
                    b = randint(1,10)
                    c = randint(2,10)
                    d = randint(-10,10)
                    e = randint(1,20)
                    f = randint(-5,10)
                M = -a+d
                m = a+d
                kq = e*M + f*m

                du = ['$P=%s$'%(latex(kq))

                                ]
                da= random.choice(du)


                da= random.choice(du)
                s = ['$P=%s$'%(latex(kq+1)),
                    '$P=%s$'%(latex(kq+2)),
                    '$P=%s$'%(latex(kq-1)),
                    '$P=%s$'%(latex(kq-2)),
                    '$P=%s$'%(latex(kq-3)),
                    '$P=%s$'%(latex(kq+3)),
                    '$P=%s$'%(latex(kq*2)),
                    '$P=%s$'%(latex(kq*3)),

                            ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                    # Câu hỏi
                noidungcauhoi = '''Cho hàm số $y = %s\\cos(%sx+\\dfrac{\\pi}{%s}) +%s$. Gọi $M, m$ lần lượt là giá trị lớn nhất và giá trị nhỏ nhất của hàm số. Giá trị của biểu thức $P=%sM+%sm$ bằng \n''' %(latex(a),latex(b),latex(c),latex(d),latex(e),latex(f))
                    # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Tập xác định của hàm số $\\mathscr{D}=\\mathbb{R}$.\\\\ \n'
                        '''Ta có \\\\ \n'''
                        '''\\hspace*{1cm} $-1 \\leq \\cos(%sx+\\dfrac{\\pi}{%s}) \\leq 1 \\Leftrightarrow %s \\geq %s\\cos(%sx+\\dfrac{\\pi}{%s}) \\geq %s$\\\\ \n'''
                        '''\\hspace*{1cm} $\\Leftrightarrow %s +%s \\geq %s\\cos(%sx+\\dfrac{\\pi}{%s}) +%s \\geq %s +%s \\Leftrightarrow %s \\geq y \\geq %s$.\\\\ \n'''
                        '''Suy ra\\\\ \n'''
                        '''\\hspace*{1cm} Giá trị lớn nhất của hàm số là $M=%s$.\\\\ \n'''
                        '''\\hspace*{1cm} Giá trị nhỏ nhất của hàm số là $m=%s$.\\\\ \n'''
                            '''Vậy giá trị $P=%s\\cdot(%s)+%s\\cdot(%s)=%s$.\\\\ \n'''
                            %(latex(b),latex(c),latex(-a),latex(a),latex(b),latex(c),latex(a),
                                latex(-a),latex(d),latex(a),latex(b),latex(c),latex(d),latex(a),latex(d),latex(M),latex(m),
                                latex(M),latex(m),
                                latex(e),latex(M),latex(f),latex(m),latex(kq),

                            ))
            if dang=='16':
                # Khai báo biến
                a = randint(1,20)
                b = randint(-5,10)
                c = randint(2,10)
                d = randint(-10,10)
                e = randint(1,20)
                f = randint(-5,10)

                while b==0 or d==0:

                    a = randint(1,20)
                    b = randint(-5,10)
                    c = randint(2,10)
                    d = randint(-10,10)
                    e = randint(1,20)
                    f = randint(-5,10)
                m = -a+d
                M = a+d
                kq = e*M + f*m

                du = ['$P=%s$'%(latex(kq))

                                ]
                da= random.choice(du)


                da= random.choice(du)
                s = ['$P=%s$'%(latex(kq+1)),
                    '$P=%s$'%(latex(kq+2)),
                    '$P=%s$'%(latex(kq-1)),
                    '$P=%s$'%(latex(kq-2)),
                    '$P=%s$'%(latex(kq-3)),
                    '$P=%s$'%(latex(kq+3)),
                    '$P=%s$'%(latex(kq*2)),
                    '$P=%s$'%(latex(kq*3)),

                            ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                    # Câu hỏi
                noidungcauhoi = '''Cho hàm số $y = %s\\cos(%sx+\\dfrac{\\pi}{%s}) +%s$. Gọi $M, m$ lần lượt là giá trị lớn nhất và giá trị nhỏ nhất của hàm số. Giá trị của biểu thức $P=%sM+%sm$ bằng \n''' %(latex(a),latex(b),latex(c),latex(d),latex(e),latex(f))
                    # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Tập xác định của hàm số $\\mathscr{D}=\\mathbb{R}$.\\\\ \n'
                            '''Ta có \\\\ \n'''
                            '''\\hspace*{1cm} $-1 \\leq \\cos(%sx+\\dfrac{\\pi}{%s}) \\leq 1 \\Leftrightarrow -%s \\leq %s\\cos(%sx+\\dfrac{\\pi}{%s}) \\leq %s$\\\\ \n'''
                            '''\\hspace*{1cm} $\\Leftrightarrow -%s +%s \\leq %s\\cos(%sx+\\dfrac{\\pi}{%s}) +%s \\leq %s +%s \\Leftrightarrow %s \\leq y \\leq %s$.\\\\ \n'''
                            '''Suy ra\\\\ \n'''
                            '''\\hspace*{1cm} Giá trị lớn nhất của hàm số là $M=%s$.\\\\ \n'''
                            '''\\hspace*{1cm} Giá trị nhỏ nhất của hàm số là $m=%s$.\\\\ \n'''
                            '''Vậy giá trị $P=%s\\cdot(%s)+%s\\cdot(%s)=%s$.\\\\ \n'''
                            %(latex(b),latex(c),latex(a),latex(a),latex(b),latex(c),latex(a),
                                latex(a),latex(d),latex(a),latex(b),latex(c),latex(d),latex(a),latex(d),latex(m),latex(M),
                                latex(M),latex(m),
                                latex(e),latex(M),latex(f),latex(m),latex(kq),

                            ))
            if dang=='17':
                # Khai báo biến
                a = randint(1,20)
                b = randint(-5,10)
                c = randint(2,10)
                d = randint(-10,10)


                while b==0 or d==0:

                    a = randint(1,20)
                    b = randint(-5,10)
                    c = randint(2,10)
                    d = randint(-10,10)

                m = -a+d
                M = a+d
                kq = M+m

                du = ['$%s$'%(latex(kq))

                                ]
                da= random.choice(du)


                da= random.choice(du)
                s = ['$%s$'%(latex(kq+1)),
                    '$%s$'%(latex(kq+2)),
                    '$%s$'%(latex(kq-1)),
                    '$%s$'%(latex(kq-2)),
                    '$%s$'%(latex(kq-3)),
                    '$%s$'%(latex(kq+3)),
                    '$%s$'%(latex(kq*2)),
                    '$%s$'%(latex(kq*3)),

                            ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                    # Câu hỏi
                noidungcauhoi = '''Tổng giá trị lớn nhất và giá trị nhỏ nhất của hàm số $y = %s\\cos(%sx+\\dfrac{\\pi}{%s}) +%s$ bằng \n''' %(latex(a),latex(b),latex(c),latex(d))
                    # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Tập xác định của hàm số $\\mathscr{D}=\\mathbb{R}$.\\\\ \n'
                            '''Ta có \\\\ \n'''
                            '''\\hspace*{1cm} $-1 \\leq \\cos(%sx+\\dfrac{\\pi}{%s}) \\leq 1 \\Leftrightarrow -%s \\leq %s\\cos(%sx+\\dfrac{\\pi}{%s}) \\leq %s$\\\\ \n'''
                            '''\\hspace*{1cm} $\\Leftrightarrow -%s +%s \\leq %s\\cos(%sx+\\dfrac{\\pi}{%s}) +%s \\leq %s +%s \\Leftrightarrow %s \\leq y \\leq %s$.\\\\ \n'''
                            '''Vậy tổng giá trị lớn nhất và nhỏ nhất của hàm số là $%s+%s=%s$.\\\\ \n'''
                            %(latex(b),latex(c),latex(a),latex(a),latex(b),latex(c),latex(a),
                                latex(a),latex(d),latex(a),latex(b),latex(c),latex(d),latex(a),latex(d),latex(m),latex(M),
                                latex(M),latex(m),latex(kq),

                            ))
            if dang=='18':
                # Khai báo biến
                a = randint(1,20)
                b = randint(-5,10)
                c = randint(2,10)
                d = randint(-10,10)

                while b==0 or d==0:

                    a = randint(1,20)
                    b = randint(-5,10)
                    c = randint(2,10)
                    d = randint(-10,10)
                m = -a+d
                M = a+d

                du = ['$T=[%s;%s]$'%(latex(m),latex(M))

                                ]
                da= random.choice(du)


                da= random.choice(du)
                s = ['$T=[%s;%s]$'%(latex(m+1),latex(M+1)),
                    '$T=[%s;%s]$'%(latex(m-1),latex(M-1)),
                    '$T=[%s;%s]$'%(latex(m*2),latex(M*2)),
                    '$T=[%s;%s]$'%(latex(m*3),latex(M*3)),
                    '$T=[%s;%s]$'%(latex(m+2),latex(M+2)),
                    '$T=[%s;%s]$'%(latex(m-2),latex(M-2)),
                    '$T=[%s;%s]$'%(latex(m-3),latex(M-3)),

                            ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                    # Câu hỏi
                noidungcauhoi = '''Tập giá trị của hàm số $y = %s\\cos(%sx+\\dfrac{\\pi}{%s}) +%s$ là \n''' %(latex(a),latex(b),latex(c),latex(d))
                    # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Tập xác định của hàm số $\\mathscr{D}=\\mathbb{R}$.\\\\ \n'
                            '''Ta có \\\\ \n'''
                            '''\\hspace*{1cm} $-1 \\leq \\cos(%sx+\\dfrac{\\pi}{%s}) \\leq 1 \\Leftrightarrow -%s \\leq %s\\cos(%sx+\\dfrac{\\pi}{%s}) \\leq %s$\\\\ \n'''
                            '''\\hspace*{1cm} $\\Leftrightarrow -%s + %s \\leq %s\\cos(%sx+\\dfrac{\\pi}{%s}) + %s \\leq %s + %s \\Leftrightarrow %s \\leq y \\leq %s$.\\\\ \n'''
                            '''Vậy tập giá trị của hàm số là $T=[%s;%s]$.\\\\ \n'''
                            %(latex(b),latex(c),latex(a),latex(a),latex(b),latex(c),latex(a),
                                latex(a),latex(d),latex(a),latex(b),latex(c),latex(d),latex(a),latex(d),latex(m),latex(M),
                                latex(m),latex(M),

                            ))
            if dang=='19':
                # Khai báo biến
                a = randint(1,20)
                b = randint(-5,10)
                c = randint(2,10)
                d = randint(-10,10)


                while b==0 or d==0:

                    a = randint(1,20)
                    b = randint(-5,10)
                    c = randint(2,10)
                    d = randint(-10,10)

                m = -a+d
                M = a+d
                kq = m

                du = ['$%s$'%(latex(kq))

                                ]
                da= random.choice(du)


                da= random.choice(du)
                s = ['$%s$'%(latex(kq+1)),
                    '$%s$'%(latex(kq+2)),
                    '$%s$'%(latex(kq-1)),
                    '$%s$'%(latex(kq-2)),
                    '$%s$'%(latex(kq-3)),
                    '$%s$'%(latex(kq+3)),
                    '$%s$'%(latex(kq*2)),
                    '$%s$'%(latex(kq*3)),

                            ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                    # Câu hỏi
                noidungcauhoi = '''Giá trị nhỏ nhất của hàm số $y = %s\\cos(%sx+\\dfrac{\\pi}{%s}) +%s$ bằng \n''' %(latex(a),latex(b),latex(c),latex(d))
                    # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Tập xác định của hàm số $\\mathscr{D}=\\mathbb{R}$.\\\\ \n'
                            '''Ta có \\\\ \n'''
                            '''\\hspace*{1cm} $-1 \\leq \\cos(%sx+\\dfrac{\\pi}{%s}) \\leq 1 \\Leftrightarrow -%s \\leq %s\\cos(%sx+\\dfrac{\\pi}{%s}) \\leq %s$\\\\ \n'''
                            '''\\hspace*{1cm} $\\Leftrightarrow -%s +%s \\leq %s\\cos(%sx+\\dfrac{\\pi}{%s}) +%s \\leq %s +%s \\Leftrightarrow %s \\leq y \\leq %s$.\\\\ \n'''
                            '''Vậy giá trị nhỏ nhất của hàm số là $%s$.\\\\ \n'''
                            %(latex(b),latex(c),latex(a),latex(a),latex(b),latex(c),latex(a),
                                latex(a),latex(d),latex(a),latex(b),latex(c),latex(d),latex(a),latex(d),latex(m),latex(M),
                                latex(kq),

                            ))
            if dang=='20':
                # Khai báo biến
                a = randint(1,20)
                b = randint(-5,10)
                c = randint(2,10)
                d = randint(-10,10)


                while b==0 or d==0:

                    a = randint(1,20)
                    b = randint(-5,10)
                    c = randint(2,10)
                    d = randint(-10,10)

                m = -a+d
                M = a+d
                kq = M

                du = ['$%s$'%(latex(kq))

                                ]
                da= random.choice(du)


                da= random.choice(du)
                s = ['$%s$'%(latex(kq+1)),
                    '$%s$'%(latex(kq+2)),
                    '$%s$'%(latex(kq-1)),
                    '$%s$'%(latex(kq-2)),
                    '$%s$'%(latex(kq-3)),
                    '$%s$'%(latex(kq+3)),
                    '$%s$'%(latex(kq*2)),
                    '$%s$'%(latex(kq*3)),

                            ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                    # Câu hỏi
                noidungcauhoi = '''Giá trị lớn nhất của hàm số $y = %s\\cos(%sx+\\dfrac{\\pi}{%s}) +%s$ bằng \n''' %(latex(a),latex(b),latex(c),latex(d))
                    # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Tập xác định của hàm số $\\mathscr{D}=\\mathbb{R}$.\\\\ \n'
                            '''Ta có \\\\ \n'''
                            '''\\hspace*{1cm} $-1 \\leq \\cos(%sx+\\dfrac{\\pi}{%s}) \\leq 1 \\Leftrightarrow -%s \\leq %s\\cos(%sx+\\dfrac{\\pi}{%s}) \\leq %s$\\\\ \n'''
                            '''\\hspace*{1cm} $\\Leftrightarrow -%s +%s \\leq %s\\cos(%sx+\\dfrac{\\pi}{%s}) +%s \\leq %s +%s \\Leftrightarrow %s \\leq y \\leq %s$.\\\\ \n'''
                            '''Vậy giá trị lớn nhất của hàm số là $%s$.\\\\ \n'''
                            %(latex(b),latex(c),latex(a),latex(a),latex(b),latex(c),latex(a),
                                latex(a),latex(d),latex(a),latex(b),latex(c),latex(d),latex(a),latex(d),latex(m),latex(M),
                                latex(kq),

                            ))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-').replace('1x', 'x').replace('-1x', '-x').replace('+ 0', '').replace('-1\\cos','-\\cos').replace('-1\\sin','-\\sin').replace('1M','M').replace('1m','m').replace('-1M','-M').replace('-1m','-m')

            return content


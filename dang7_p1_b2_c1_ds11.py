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


def bt_dang7_p1_b2_c1_ds11(self):
            lisdang=['1','2','3','4']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                a = randint(1,10)
                b = randint(1,10)
                c = randint(1,10)
                d = randint(1,10)


                while a>=b or c>=d:
                    a = randint(1,10)
                    b = randint(1,10)
                    c = randint(1,10)
                    d = randint(1,10)
                m = nsimplify(a/b)
                n = nsimplify(-c/d)
                ca = -nsimplify( sqrt(1-(a/b)**2))
                ca2 = nsimplify(1 - (a/b)**2)
                cb = nsimplify(sqrt(1-(c/d)**2))
                cb2 = nsimplify( 1 - (c/d)**2)
                kq1 = ca*cb+m*n
                kq2 = ca*cb-m*n
                kq3 = m*cb-ca*n
                kq4 = m*cb+ca*n

                du = ['$\\cos(a-b)=%s$'%(latex(kq1)),
                        '$\\cos(a+b)=%s$'%(latex(kq2)),
                        '$\\sin(a-b)=%s$'%(latex(kq3)),
                        '$\\sin(a+b)=%s$'%(latex(kq4)),
                                ]
                da= random.choice(du)


                da= random.choice(du)
                s = ['$\\cos(a-b)=%s$'%(latex(nsimplify(kq1*1/2))),
                        '$\\cos(a+b)=%s$'%(latex(nsimplify(kq2*1/2))),
                        '$\\sin(a-b)=%s$'%(latex(nsimplify(kq3*1/2))),
                        '$\\sin(a+b)=%s$'%(latex(nsimplify(kq4*1/2))),
                        '$\\cos(a-b)=%s$'%(latex(-kq1)),
                        '$\\cos(a+b)=%s$'%(latex(-kq2)),
                        '$\\sin(a-b)=%s$'%(latex(-kq3)),
                        '$\\sin(a+b)=%s$'%(latex(-kq4)),
                        '$\\cos(a-b)=%s$'%(latex(nsimplify(kq1*1/3))),
                        '$\\cos(a+b)=%s$'%(latex(nsimplify(kq2*1/3))),
                        '$\\sin(a-b)=%s$'%(latex(nsimplify(kq3*1/3))),
                        '$\\sin(a+b)=%s$'%(latex(nsimplify(kq4*1/3))),

                            ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                    # Câu hỏi
                noidungcauhoi = '''Cho $\\sin a = %s$ với $a \\in \\left(\\dfrac{\\pi}{2};\\pi \\right)$ và $\\sin b = %s$ với $ b \\in \\left(\\dfrac{3\\pi}{2};2\\pi \\right) $. Mệnh đề nào sau đây là đúng? \n''' %(latex(m),latex(n))
                    # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có \\\\ \n'
                            '''\\hspace*{1cm} $\\sin^2a+\\cos^2a=1 \\Leftrightarrow \\cos^2a = 1 - \\sin^2a = 1-\\left(%s \\right)^2 = %s \\Leftrightarrow \\cos a = \\pm %s$.\\\\ \n'''
                            '''\\hspace*{1cm} Vì $a \\in \\left(\\dfrac{\\pi}{2};\\pi \\right)$  nên $ \\cos a <0$. Do đó $ \\cos a = %s$.\\\\ \n'''
                            '''Tương tự ta có\\\\ \n'''
                            '''\\hspace*{1cm} $\\sin^2b+\\cos^2b=1 \\Leftrightarrow \\cos^2b = 1 - \\sin^2b = 1-\\left( %s \\right)^2 = %s \\Leftrightarrow \\cos b = \\pm %s$.\\\\ \n'''
                            '''\\hspace*{1cm} Vì $ b \\in \\left(\\dfrac{3\\pi}{2};2\\pi \\right) $  nên $ \\cos b > 0$. Do đó $ \\cos b = %s$.\\\\ \n'''
                            '''Suy ra\\\\ \n'''
                            '''\\hspace*{1cm} $\\cos(a+b) = \\cos a\\cos b -\\sin a\\sin b = %s\\cdot%s - %s\\cdot \\left(%s \\right) = %s$.\\\\ \n'''
                            '''\\hspace*{1cm} $\\cos(a-b) = \\cos a\\cos b +\\sin a\\sin b = %s\\cdot%s + %s\\cdot \\left(%s \\right) = %s$.\\\\ \n'''
                            '''\\hspace*{1cm} $\\sin(a-b) = \\sin a\\cos b -\\cos a\\sin b = %s\\cdot%s - \\left( %s\\right)\\cdot \\left(%s \\right) = %s$.\\\\ \n'''
                            '''\\hspace*{1cm} $\\sin(a+b) = \\sin a\\cos b +\\cos a\\sin b = %s\\cdot%s + \\left(%s\\right)\\cdot \\left(%s \\right) = %s$.\\\\ \n'''
                            %(latex(m),latex(ca2),latex(-ca),
                            latex(ca),
                            latex(n),latex(cb2),latex(cb),
                            latex(cb),
                            latex(ca),latex(cb),latex(m),latex(n),latex(kq2),
                            latex(ca),latex(cb),latex(m),latex(n),latex(kq1),
                            latex(m),latex(cb),latex(ca),latex(n),latex(kq3),
                            latex(m),latex(cb),latex(ca),latex(n),latex(kq4),
                            ))
            if dang=='2':
                # Khai báo biến
                a = randint(1,10)
                b = randint(1,10)
                c = randint(1,10)
                d = randint(1,10)

                while a>=b or c>=d:
                        a = randint(1,10)
                        b = randint(1,10)
                        c = randint(1,10)
                        d = randint(1,10)
                m = nsimplify(a/b)
                n = nsimplify(-c/d)
                ca = nsimplify( sqrt(1-(a/b)**2))
                ca2 = nsimplify(1 - (a/b)**2)
                cb = -nsimplify(sqrt(1-(c/d)**2))
                cb2 = nsimplify( 1 - (c/d)**2)
                kq1 = ca*cb+m*n
                kq2 = ca*cb-m*n
                kq3 = m*cb-ca*n
                kq4 = m*cb+ca*n

                du = ['$\\cos(a-b)=%s$'%(latex(kq1)),
                            '$\\cos(a+b)=%s$'%(latex(kq2)),
                            '$\\sin(a-b)=%s$'%(latex(kq3)),
                            '$\\sin(a+b)=%s$'%(latex(kq4)),
                                ]
                da= random.choice(du)


                da= random.choice(du)
                s = ['$\\cos(a-b)=%s$'%(latex(nsimplify(kq1*1/2))),
                        '$\\cos(a+b)=%s$'%(latex(nsimplify(kq2*1/2))),
                        '$\\sin(a-b)=%s$'%(latex(nsimplify(kq3*1/2))),
                        '$\\sin(a+b)=%s$'%(latex(nsimplify(kq4*1/4))),
                        '$\\cos(a-b)=%s$'%(latex(-kq1)),
                        '$\\cos(a+b)=%s$'%(latex(-kq2)),
                        '$\\sin(a-b)=%s$'%(latex(-kq3)),
                        '$\\sin(a+b)=%s$'%(latex(-kq4)),
                        '$\\cos(a-b)=%s$'%(latex(nsimplify(kq1*1/3))),
                        '$\\cos(a+b)=%s$'%(latex(nsimplify(kq2*1/3))),
                        '$\\sin(a-b)=%s$'%(latex(nsimplify(kq3*1/3))),
                        '$\\sin(a+b)=%s$'%(latex(nsimplify(kq4*1/3))),
                        ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = '''Cho $\\sin a = %s$ với $a \\in \\left(0;\\dfrac{\\pi}{2}\\right)$ và $\\sin b = %s$ với $ b \\in \\left(\\pi ;\\dfrac{3\\pi}{2}\\right) $. Mệnh đề nào sau đây là đúng? \n''' %(latex(m),latex(n))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có \\\\ \n'
                        '''\\hspace*{1cm} $\\sin^2a+\\cos^2a=1 \\Leftrightarrow \\cos^2a = 1 - \\sin^2a = 1-\\left(%s \\right)^2 = %s \\Leftrightarrow \\cos a = \\pm %s$.\\\\ \n'''
                        '''\\hspace*{1cm} Vì $a \\in \\left(0;\\dfrac{\\pi}{2}\\right)$  nên $ \\cos a >0$. Do đó $ \\cos a = %s$.\\\\ \n'''
                        '''Tương tự ta có\\\\ \n'''
                        '''\\hspace*{1cm} $\\sin^2b+\\cos^2b=1 \\Leftrightarrow \\cos^2b = 1 - \\sin^2b = 1-\\left( %s \\right)^2 = %s \\Leftrightarrow \\cos b = \\pm %s$.\\\\ \n'''
                        '''\\hspace*{1cm} Vì $b \\in \\left(\\pi ;\\dfrac{3\\pi}{2}\\right) $  nên $ \\cos b < 0$. Do đó $ \\cos b = %s$.\\\\ \n'''
                        '''Suy ra\\\\ \n'''
                        '''\\hspace*{1cm} $\\cos(a+b) = \\cos a\\cos b -\\sin a\\sin b = %s\\cdot\\left(%s \\right) - %s\\cdot \\left(%s \\right) = %s$.\\\\ \n'''
                        '''\\hspace*{1cm} $\\cos(a-b) = \\cos a\\cos b +\\sin a\\sin b = %s\\cdot\\left(%s \\right) + %s\\cdot \\left(%s \\right) = %s$.\\\\ \n'''
                        '''\\hspace*{1cm} $\\sin(a-b) = \\sin a\\cos b -\\cos a\\sin b = %s\\cdot\\left(%s \\right) - %s\\cdot \\left(%s \\right) = %s$.\\\\ \n'''
                        '''\\hspace*{1cm} $\\sin(a+b) = \\sin a\\cos b +\\cos a\\sin b = %s\\cdot\\left(%s \\right) + %s\\cdot \\left(%s \\right) = %s$.\\\\ \n'''
                        %(latex(m),latex(ca2),latex(ca),
                            latex(ca),
                            latex(n),latex(cb2),latex(-cb),
                            latex(cb),
                            latex(ca),latex(cb),latex(m),latex(n),latex(kq2),
                            latex(ca),latex(cb),latex(m),latex(n),latex(kq1),
                            latex(m),latex(cb),latex(ca),latex(n),latex(kq3),
                            latex(m),latex(cb),latex(ca),latex(n),latex(kq4),
                            ))
            if dang=='3':
                # Khai báo biến
                a = randint(1,10)
                b = randint(1,10)
                c = randint(1,10)
                d = randint(1,10)


                while a>=b or c>=d or a*d-b*c==0 or b**2+c**2-a**2-d**2!=0:
                    a = randint(1,10)
                    b = randint(1,10)
                    c = randint(1,10)
                    d = randint(1,10)
                m = nsimplify(a/b)
                n = nsimplify(-c/d)
                ca = -nsimplify( sqrt(1-(a/b)**2))
                ca2 = nsimplify(1 - (a/b)**2)
                cb = nsimplify(sqrt(1-(c/d)**2))
                cb2 = nsimplify( 1 - (c/d)**2)
                kq1 = ca*cb+m*n
                kq2 = ca*cb-m*n
                kq3 = m*cb-ca*n
                kq4 = m*cb+ca*n
                ta =nsimplify(m/ca)
                tb =nsimplify(n/cb)
                tab = kq4/kq2
                ta_b= kq3/kq1
                du = ['$\\tan(a-b)=%s$'%(latex(ta_b)),
                    '$\\tan(a+b)=%s$'%(latex(tab)),

                            ]

                da= random.choice(du)
                s = ['$\\tan(a-b)=%s$'%(latex(nsimplify(-ta_b))),
                    '$\\tan(a+b)=%s$'%(latex(nsimplify(-tab))),
                    '$\\tan(a-b)=%s$'%(latex(nsimplify(ta_b+6))),
                    '$\\tan(a+b)=%s$'%(latex(nsimplify(tab*5))),
                    '$\\tan(a-b)=%s$'%(latex(nsimplify(ta_b*(-5)))),
                    '$\\tan(a+b)=%s$'%(latex(nsimplify(tab*2))),
                    '$\\tan(a-b)=%s$'%(latex(nsimplify(ta_b*3))),
                    '$\\tan(a+b)=%s$'%(latex(nsimplify(tab*(-2)))),                  
                    '$\\tan(a-b)=%s$'%(latex(nsimplify(ta_b*(-3)))),
                    '$\\tan(a+b)=%s$'%(latex(nsimplify(tab*4))),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = '''Cho $\\sin a = %s$ với $a \\in \\left(\\dfrac{\\pi}{2};\\pi \\right)$ và $\\sin b = %s$ với $ b \\in \\left(\\dfrac{3\\pi}{2};2\\pi \\right) $. Mệnh đề nào sau đây là đúng? \n''' %(latex(m),latex(n))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có \\\\ \n'
                        '''\\hspace*{1cm} $\\sin^2a+\\cos^2a=1 \\Leftrightarrow \\cos^2a = 1 - \\sin^2a = 1-\\left(%s \\right)^2 = %s \\Leftrightarrow \\cos a = \\pm %s$.\\\\ \n'''
                        '''\\hspace*{1cm} Vì $a \\in \\left(\\dfrac{\\pi}{2};\\pi \\right)$  nên $ \\cos a <0$. Do đó $ \\cos a = %s$.\\\\ \n'''
                        '''Tương tự ta có\\\\ \n'''
                        '''\\hspace*{1cm} $\\sin^2b+\\cos^2b=1 \\Leftrightarrow \\cos^2b = 1 - \\sin^2b = 1-\\left( %s \\right)^2 = %s \\Leftrightarrow \\cos b = \\pm %s$.\\\\ \n'''
                        '''\\hspace*{1cm} Vì $ b \\in \\left(\\dfrac{3\\pi}{2};2\\pi \\right) $  nên $ \\cos b > 0$. Do đó $ \\cos b = %s$.\\\\ \n'''
                        '''Vậy\\\\ \n'''
                        '''\\hspace*{1cm} $\\tan a = \\dfrac{\\sin a}{\\cos a}=%s$.\\\\ \n'''
                        '''\\hspace*{1cm} $\\tan b = \\dfrac{\\sin b}{\\cos b}=%s$.\\\\ \n''' 
                        '''\\hspace*{1cm} $\\tan(a+b) = \\dfrac{\\tan a+\\tan b}{1-\\tan a\\tan b}=\\dfrac{%s+%s}{1-\\left(%s\\right)\\cdot \\left(%s\\right)}=%s$.\\\\ \n''' 
                        '''\\hspace*{1cm} $\\tan(a-b) = \\dfrac{\\tan a-\\tan b}{1+\\tan a\\tan b}=\\dfrac{%s-\\left(%s\\right)}{1+%s\\cdot \\left(%s\\right)}=%s$.\\\\ \n''' 
                        %(latex(m),latex(ca2),latex(-ca),
                        latex(ca),
                        latex(n),latex(cb2),latex(cb),
                        latex(cb),
                        latex(ta),
                        latex(tb),
                        latex(ta), latex(tb), latex(ta), latex(tb), latex(tab),
                        latex(ta), latex(tb), latex(ta), latex(tb), latex(ta_b),
                        ))
            if dang=='4':
                a = randint(1,10)
                b = randint(1,10)
                c = randint(1,10)
                d = randint(1,10)

                while a>=b or c>=d or a*d-b*c==0 or b**2+c**2-a**2-d**2!=0:
                        a = randint(1,10)
                        b = randint(1,10)
                        c = randint(1,10)
                        d = randint(1,10)
                m = nsimplify(a/b)
                n = nsimplify(-c/d)
                ca = nsimplify( sqrt(1-(a/b)**2))
                ca2 = nsimplify(1 - (a/b)**2)
                cb = nsimplify(sqrt(1-(c/d)**2))
                cb2 = nsimplify( 1 - (c/d)**2)
                kq1 = ca*cb+m*n
                kq2 = ca*cb-m*n
                kq3 = m*cb-ca*n
                kq4 = m*cb+ca*n
                ta =nsimplify(m/ca)
                tb =nsimplify(n/(-cb))
                tab = kq4/kq2
                ta_b= kq3/kq1

                du = ['$\\tan(a-b)=%s$'%(latex(ta_b)),
                        '$\\tan(a+b)=%s$'%(latex(tab)),
                        ]

                da= random.choice(du)
                s = ['$\\tan(a-b)=%s$'%(latex(nsimplify(-ta_b))),
                        '$\\tan(a+b)=%s$'%(latex(nsimplify(-tab))),
                        '$\\tan(a-b)=%s$'%(latex(nsimplify(ta_b+6))),
                        '$\\tan(a+b)=%s$'%(latex(nsimplify(tab*5))),
                        '$\\tan(a-b)=%s$'%(latex(nsimplify(ta_b*(-5)))),
                        '$\\tan(a+b)=%s$'%(latex(nsimplify(tab*2))),
                        '$\\tan(a-b)=%s$'%(latex(nsimplify(ta_b*3))),
                        '$\\tan(a+b)=%s$'%(latex(nsimplify(tab*(-2)))),                  
                        '$\\tan(a-b)=%s$'%(latex(nsimplify(ta_b*(-3)))),
                        '$\\tan(a+b)=%s$'%(latex(nsimplify(tab*4))),
                        ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = '''Cho $\\sin a = %s$ với $a \\in \\left(0;\\dfrac{\\pi}{2}\\right)$ và $\\sin b = %s$ với $ b \\in \\left(\\pi ;\\dfrac{3\\pi}{2}\\right) $. Mệnh đề nào sau đây là đúng? \n''' %(latex(m),latex(n))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có \\\\ \n'
                        '''\\hspace*{1cm} $\\sin^2a+\\cos^2a=1 \\Leftrightarrow \\cos^2a = 1 - \\sin^2a = 1-\\left(%s \\right)^2 = %s \\Leftrightarrow \\cos a = \\pm %s$.\\\\ \n'''
                        '''\\hspace*{1cm} Vì $a \\in \\left(0;\\dfrac{\\pi}{2}\\right)$ nên $ \\cos a > 0$. Do đó $ \\cos a = %s$.\\\\ \n'''
                        '''Tương tự ta có\\\\ \n'''
                        '''\\hspace*{1cm} $\\sin^2b+\\cos^2b=1 \\Leftrightarrow \\cos^2b = 1 - \\sin^2b = 1-\\left( %s \\right)^2 = %s \\Leftrightarrow \\cos b = \\pm %s$.\\\\ \n'''
                        '''\\hspace*{1cm} Vì $ b \\in \\left(\\pi ;\\dfrac{3\\pi}{2}\\right) $  nên $ \\cos b < 0$. Do đó $ \\cos b = %s$.\\\\ \n'''
                        '''Vậy\\\\ \n'''
                        '''\\hspace*{1cm} $\\tan a = \\dfrac{\\sin a}{\\cos a}=%s$.\\\\ \n'''
                        '''\\hspace*{1cm} $\\tan b = \\dfrac{\\sin b}{\\cos b}=%s$.\\\\ \n''' 
                        '''\\hspace*{1cm} $\\tan(a+b) = \\dfrac{\\tan a+\\tan b}{1-\\tan a\\tan b}=\\dfrac{%s+%s}{1-\\left(%s\\right)\\cdot \\left(%s\\right)}=%s$.\\\\ \n''' 
                        '''\\hspace*{1cm} $\\tan(a-b) = \\dfrac{\\tan a-\\tan b}{1+\\tan a\\tan b}=\\dfrac{%s-\\left(%s\\right)}{1+%s\\cdot \\left(%s\\right)}=%s$.\\\\ \n''' 
                        %(latex(m),latex(ca2),latex(ca),
                            latex(ca),
                            latex(n),latex(cb2),latex(cb),
                            latex(-cb),
                            latex(ta),
                            latex(tb),
                            latex(ta), latex(tb), latex(ta), latex(tb), latex(tab),
                            latex(ta), latex(tb), latex(ta), latex(tb), latex(ta_b),
                            ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice[2] \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-').replace('1x', 'x').replace('+0x^2', '').replace('+0x', '').replace('+0', '')
            return content


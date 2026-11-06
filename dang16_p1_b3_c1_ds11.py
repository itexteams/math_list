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


def bt_dang16_p1_b3_c1_ds11(self):
            # Khai báo biến
            lisdang=['1','2','3','4','5','6']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                a = randint(1,20)
                b = randint(-20,20)
                c = randint(-20,20)


                while a==11 or b==11 or b==-11 or abs(b)>=abs(2*a):
                    a = randint(1,20)
                    b = randint(-20,20)
                    c = randint(-20,20)
                y = a*x**2+b*x+c
                x_0 = Rational(b,2*a)
                y_0 = y.subs(x,x_0) 
                y_1 = y.subs(x,-1)  
                y_2 = y.subs(x,1)
                lst = ['sin','cos']
                ham = random.choice(lst)
                kq = y_0
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
                noidungcauhoi = '''Giá trị nhỏ nhất của hàm số $y=%s\\%s^2x+%s\\%s x+%s$ \n''' %(latex(a),ham,latex(b),ham,latex(c))    
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Đặt $t=\\sin x,t \\in [-1;1]$.\\\\ \n'''
                        '''Xét hàm số $f(t)=%st^2+%st+%s$ trên đoạn $[-1;1]$.\\\\ \n'''
                        '''Ta có $-\\dfrac{b}{2a}=%s \\in [-1;1]$.\\\\ \n'''
                        '''Bảng biến thiên\\\\ \n'''
                            '''\\begin{center} \n'''
                            '''\\begin{tikzpicture} \n'''
                            '''\\tkzTabInit[nocadre=false,lgt=1.2,espcl=2.5,deltacl=0.6] \n'''
                            '''{$t$ /1.2, $f(t)$ /2.5} \n'''
                            '''{$-1$,$%s$,$1$} \n'''
                            '''\\tkzTabVar{+/$%s$,-/$%s$,+/$%s$} \n'''
                            '''\\end{tikzpicture} \n'''
                            '''\\end{center} \n'''
                            '''Vậy giá trị nhỏ nhất của hàm số là $%s$.\\\\ \n'''

                        %(latex(a),latex(b),latex(c),
                            latex(x_0),
                            latex(x_0),
                            latex(y_1),latex(y_0),latex(y_2),
                            latex(kq),


                            ))
            if dang=='2':
                # Khai báo biến
                a = randint(1,10)
                b = randint(-20,20)
                c = randint(-20,20)


                while b==11 or b==-11 or abs(b)>=abs(4*a):
                    a = randint(1,10)
                    b = randint(-20,20)
                    c = randint(-20,20)
                y = 2*a*x**2+b*x-a+c
                x_0 = -Rational(b,4*a)
                y_0 = y.subs(x,x_0) 
                y_1 = y.subs(x,-1)  
                y_2 = y.subs(x,1)
                lst = ['cos']
                ham = random.choice(lst)
                kq = y_0
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
                noidungcauhoi = '''Giá trị nhỏ nhất của hàm số $y=%s\\%s x+%s\\cos 2x +%s$ \n''' %(latex(b),ham,latex(a),latex(c))    
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có $y=%s\\%s x+%s\\cos 2x+%s= %s\\%s x+%s(2\\cos^2x-1)+%s=%s\\cos^2x+%s\\cos x+%s$.\\\\ \n'''
                        '''Đặt $t=\\sin x,t \\in [-1;1]$.\\\\ \n'''
                        '''Xét hàm số $f(t)=%st^2+%st+%s$ trên đoạn $[-1;1]$.\\\\ \n'''
                        '''Ta có $-\\dfrac{b}{2a}=%s \\in [-1;1]$.\\\\ \n'''
                        '''Bảng biến thiên\\\\ \n'''
                            '''\\begin{center} \n'''
                            '''\\begin{tikzpicture} \n'''
                            '''\\tkzTabInit[nocadre=false,lgt=1.2,espcl=2.5,deltacl=0.6] \n'''
                            '''{$t$ /1.2, $f(t)$ /2.5} \n'''
                            '''{$-1$,$%s$,$1$} \n'''
                            '''\\tkzTabVar{+/$%s$,-/$%s$,+/$%s$} \n'''
                            '''\\end{tikzpicture} \n'''
                            '''\\end{center} \n'''
                            '''Vậy giá trị nhỏ nhất của hàm số là $%s$.\\\\ \n'''

                        %(latex(b),ham,latex(a),latex(c),latex(b),ham,latex(a),latex(c),latex(2*a),latex(b),latex(-a+c),
                            latex(2*a),latex(b),latex(-a+c),
                            latex(x_0),
                            latex(x_0),
                            latex(y_1),latex(y_0),latex(y_2),
                            latex(kq),


                            ))
            if dang=='3':
                # Khai báo biến
                a = randint(-10,-1)
                b = randint(-20,20)
                c = randint(-20,20)


                while b==11 or b==-11 or abs(b)>=abs(4*a):
                    a = randint(-10,-1)
                    b = randint(-20,20)
                    c = randint(-20,20)
                y = 2*a*x**2+b*x-a+c
                x_0 = -Rational(b,4*a)
                y_0 = y.subs(x,x_0) 
                y_1 = y.subs(x,-1)  
                y_2 = y.subs(x,1)
                lst = ['cos']
                ham = random.choice(lst)
                kq = y_0
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
                noidungcauhoi = '''Giá trị lớn nhất của hàm số $y=%s\\%s x+%s\\cos 2x +%s$ \n''' %(latex(b),ham,latex(a),latex(c)) 
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có $y=%s\\%s x+%s\\cos 2x+%s= %s\\%s x+%s(2\\cos^2x-1)+%s=%s\\cos^2x+%s\\cos x+%s$.\\\\ \n'''
                        'Đặt $t=\\sin x,t \\in [-1;1]$.\\\\ \n'''
                        '''Xét hàm số $f(t)=%st^2+%st+%s$ trên đoạn $[-1;1]$.\\\\ \n'''
                        '''Ta có $-\\dfrac{b}{2a}=%s \\in [-1;1]$.\\\\ \n'''
                        '''Bảng biến thiên\\\\ \n'''
                            '''\\begin{center} \n'''
                            '''\\begin{tikzpicture} \n'''
                            '''\\tkzTabInit[nocadre=false,lgt=1.2,espcl=2.5,deltacl=0.6] \n'''
                            '''{$t$ /1.2, $f(t)$ /2.5} \n'''
                            '''{$-1$,$%s$,$1$} \n'''
                            '''\\tkzTabVar{-/$%s$,+/$%s$,-/$%s$} \n'''
                            '''\\end{tikzpicture} \n'''
                            '''\\end{center} \n'''
                            '''Vậy giá trị lớn nhất của hàm số là $%s$.\\\\ \n'''

                            %(latex(b),ham,latex(a),latex(c),latex(b),ham,latex(a),latex(c),latex(2*a),latex(b),latex(-a+c),
                            latex(2*a),latex(b),latex(-a+c),
                            latex(x_0),
                            latex(x_0),
                            latex(y_1),latex(y_0),latex(y_2),
                            latex(kq),


                            ))
            if dang=='4':
                # Khai báo biến
                a = randint(1,10)
                b = randint(-20,20)
                c = randint(-20,20)


                while b==11 or b==-11 or abs(b)>=abs(4*a):
                    a = randint(1,10)
                    b = randint(-20,20)
                    c = randint(-20,20)
                y = -2*a*x**2+b*x+a+c
                x_0 = Rational(b,4*a)
                y_0 = y.subs(x,x_0) 
                y_1 = y.subs(x,-1)  
                y_2 = y.subs(x,1)
                lst = ['sin']
                ham = random.choice(lst)
                kq = y_0
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
                noidungcauhoi = '''Giá trị lớn nhất của hàm số $y=%s\\%s x+%s\\cos 2x +%s$ \n''' %(latex(b),ham,latex(a),latex(c))    
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có $y=%s\\%s x+%s\\cos 2x+%s= %s\\%s x+%s(1-2\\sin^2x)+%s=%s\\sin^2x+%s\\sin x+%s$.\\\\ \n'''
                        'Đặt $t=\\sin x,t \\in [-1;1]$.\\\\ \n'''
                        '''Xét hàm số $f(t)=%st^2+%st+%s$ trên đoạn $[-1;1]$.\\\\ \n'''
                        '''Ta có $-\\dfrac{b}{2a}=%s \\in [-1;1]$.\\\\ \n'''
                        '''Bảng biến thiên\\\\ \n'''
                            '''\\begin{center} \n'''
                            '''\\begin{tikzpicture} \n'''
                            '''\\tkzTabInit[nocadre=false,lgt=1.2,espcl=2.5,deltacl=0.6] \n'''
                            '''{$t$ /1.2, $f(t)$ /2.5} \n'''
                            '''{$-1$,$%s$,$1$} \n'''
                            '''\\tkzTabVar{-/$%s$,+/$%s$,-/$%s$} \n'''
                            '''\\end{tikzpicture} \n'''
                            '''\\end{center} \n'''
                            '''Vậy giá trị lớn nhất của hàm số là $%s$.\\\\ \n'''

                            %(latex(b),ham,latex(a),latex(c),latex(b),ham,latex(a),latex(c),latex(-2*a),latex(b),latex(a+c),
                            latex(-2*a),latex(b),latex(a+c),
                            latex(x_0),
                            latex(x_0),
                            latex(y_1),latex(y_0),latex(y_2),
                            latex(kq),


                            ))
            if dang=='5':
                # Khai báo biến
                a = randint(-10,-1)
                b = randint(-20,20)
                c = randint(-20,20)


                while b==11 or b==-11 or abs(b)>=abs(4*a):
                    a = randint(-10,-1)
                    b = randint(-20,20)
                    c = randint(-20,20)
                y = -2*a*x**2+b*x+a+c
                x_0 = Rational(b,4*a)
                y_0 = y.subs(x,x_0) 
                y_1 = y.subs(x,-1)  
                y_2 = y.subs(x,1)
                lst = ['sin']
                ham = random.choice(lst)
                kq = y_0
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
                noidungcauhoi = '''Giá trị nhỏ nhất của hàm số $y=%s\\%s x+%s\\cos 2x +%s$ \n''' %(latex(b),ham,latex(a),latex(c))    
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có $y=%s\\%s x+%s\\cos 2x+%s= %s\\%s x+%s(1-2\\sin^2x)+%s=%s\\sin^2x+%s\\sin x+%s$.\\\\ \n'''
                        '''Đặt $t=\\sin x,t \\in [-1;1]$.\\\\ \n'''
                        '''Xét hàm số $f(t)=%st^2+%st+%s$ trên đoạn $[-1;1]$.\\\\ \n'''
                        '''Ta có $-\\dfrac{b}{2a}=%s \\in [-1;1]$.\\\\ \n'''
                        '''Bảng biến thiên\\\\ \n'''
                            '''\\begin{center} \n'''
                            '''\\begin{tikzpicture} \n'''
                            '''\\tkzTabInit[nocadre=false,lgt=1.2,espcl=2.5,deltacl=0.6] \n'''
                            '''{$t$ /1.2, $f(t)$ /2.5} \n'''
                            '''{$-1$,$%s$,$1$} \n'''
                            '''\\tkzTabVar{+/$%s$,-/$%s$,+/$%s$} \n'''
                            '''\\end{tikzpicture} \n'''
                            '''\\end{center} \n'''
                            '''Vậy giá trị nhỏ nhất của hàm số là $%s$.\\\\ \n'''

                        %(latex(b),ham,latex(a),latex(c),latex(b),ham,latex(a),latex(c),latex(-2*a),latex(b),latex(a+c),
                            latex(-2*a),latex(b),latex(a+c),
                            latex(x_0),
                            latex(x_0),
                            latex(y_1),latex(y_0),latex(y_2),
                            latex(kq),


                            ))
            if dang=='6':
                # Khai báo biến
                a = randint(-20,-1)
                b = randint(-20,20)
                c = randint(-20,20)


                while a==-11 or b==11 or b==-11 or abs(b)>=abs(2*a):
                    a = randint(-20,-1)
                    b = randint(-20,20)
                    c = randint(-20,20)
                y = a*x**2+b*x+c
                x_0 = Rational(b,2*a)
                y_0 = y.subs(x,x_0) 
                y_1 = y.subs(x,-1)  
                y_2 = y.subs(x,1)
                lst = ['sin','cos']
                ham = random.choice(lst)
                kq = y_0
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
                noidungcauhoi = '''Giá trị lớn nhất của hàm số $y=%s\\%s^2x+%s\\%s x+%s$ \n''' %(latex(a),ham,latex(b),ham,latex(c))    
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Đặt $t=\\sin x,t \\in [-1;1]$.\\\\ \n'''
                        '''Xét hàm số $f(t)=%st^2+%st+%s$ trên đoạn $[-1;1]$.\\\\ \n'''
                        '''Ta có $-\\dfrac{b}{2a}=%s \\in [-1;1]$.\\\\ \n'''
                        '''Bảng biến thiên\\\\ \n'''
                            '''\\begin{center} \n'''
                            '''\\begin{tikzpicture} \n'''
                            '''\\tkzTabInit[nocadre=false,lgt=1.2,espcl=2.5,deltacl=0.6] \n'''
                            '''{$t$ /1.2, $f(t)$ /2.5} \n'''
                            '''{$-1$,$%s$,$1$} \n'''
                            '''\\tkzTabVar{-/$%s$,+/$%s$,-/$%s$} \n'''
                            '''\\end{tikzpicture} \n'''
                            '''\\end{center} \n'''
                            '''Vậy giá trị lớn nhất của hàm số là $%s$.\\\\ \n'''

                        %(latex(a),latex(b),latex(c), 
                            latex(x_0), #dòng 3
                            latex(x_0),
                            latex(y_1),latex(y_0),latex(y_2),
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-').replace('1x', 'x').replace('1\\sin','\\sin').replace('-1\\sin','-\\sin').replace('1\\cos','\\cos').replace('-1\\cos','-\\cos')
            return content


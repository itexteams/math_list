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


def bt_dang7_p1_b3_c1_ds11(self):
            # Khai báo biến
            lisdang=['1','2','3']
            dang=random.choice(lisdang)
            if dang=='3':
                x=symbols('x')
                k=symbols('k')
                m1=randint(-9,9)
                n1=randint(-9,9)
                p1=randint(-9,9)
                q1=randint(-9,9)
                while m1==0 or n1==0 or q1==0:
                    m1=randint(-9,9)
                    n1=randint(-9,9)
                    p1=randint(-9,9)
                    q1=randint(-9,9)
                a1=Rational(m1,n1)
                b1=Rational(p1,q1)
                f1=sin(a1*x+b1*pi)

                m2=randint(-9,9)
                n2=randint(-9,9)
                p2=randint(-9,9)
                q2=randint(-9,9)
                while m2==0 or n2==0 or q2==0:
                    m2=randint(-9,9)
                    n2=randint(-9,9)
                    p2=randint(-9,9)
                    q2=randint(-9,9)
                a2=Rational(m2,n2)
                b2=Rational(p2,q2)
                f2=tan(a2*x+b2*pi)

                hs1=(sin(a1*x+b1))**2
                hs11=(1-cos(2*a1*x+2*b1))/2

                hs2=(cos(a2*x+b2))**2
                hs22=(1+cos(2*a2*x+2*b2))/2

                hs=hs1+hs2+m1
                hss=hs11+hs22+m1

                num1=abs(n1*m2)
                num2=abs(n2*m1)  
                bcnn = (num1 * num2) // math.gcd(num1, num2)
                t=pi*bcnn/(abs(m1*m2))

                d = [
                    '$%s$'%(latex(t)),
                    ]
                da= random.choice(d)
                s = [
                    '$%s$'%(latex(pi/abs(2*a1))),
                    '$%s$'%(latex(2*pi/abs(a1))),
                    '$%s$'%(latex(3*pi/abs(2*a1))),
                    '$%s$'%(latex(2*pi/abs(3*a1))),
                    '$%s$'%(latex(4*pi/abs(2*a1))),
                    '$%s$'%(latex(2*pi/abs(4*a1))),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Hàm số $y=%s$ có chu kỳ là  \n'
                                %(latex(hs))
                            ) 

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
                        '\\hspace*{1cm} $y=%s=%s$.\\\\ \n'   

                        '\\hspace*{1cm} $g(x)=%s$ có chu kỳ là $T_1=\\dfrac{2\\pi}{%s}=%s$. \\\\ \n'
                        '\\hspace*{1cm} $h(x)=%s$ có chu kỳ là $T_2=\\dfrac{2\\pi}{%s}=%s$.\\\\ \n'
                        'Chu kỳ của hàm số đã cho là bội chung nhỏ nhất của $T_1$ và $T_2$. \\\\ \n'
                        'Vậy chu kỳ của hàm số đã cho là $T=%s$'

                        %(latex(hs),latex(hss),
                        latex(hs11),latex(abs(2*a1)),latex(2*pi/abs(2*a1)),
                        latex(hs22),latex(abs(2*a2)),latex(2*pi/abs(2*a2)),
                        latex(t)
                        ))
            if dang=='2':
                x=symbols('x')
                k=symbols('k')
                m1=randint(-9,9)
                n1=randint(-9,9)
                p1=randint(-9,9)
                q1=randint(-9,9)
                while m1==0 or n1==0 or q1==0:
                    m1=randint(-9,9)
                    n1=randint(-9,9)
                    p1=randint(-9,9)
                    q1=randint(-9,9)
                a1=Rational(m1,n1)
                b1=Rational(p1,q1)
                f1=sin(a1*x+b1*pi)

                m2=randint(-9,9)
                n2=randint(-9,9)
                p2=randint(-9,9)
                q2=randint(-9,9)
                while m2==0 or n2==0 or q2==0:
                    m2=randint(-9,9)
                    n2=randint(-9,9)
                    p2=randint(-9,9)
                    q2=randint(-9,9)
                a2=Rational(m2,n2)
                b2=Rational(p2,q2)
                f2=tan(a2*x+b2*pi)

                hs1=(cos(a1*x+b1))**2
                hs11=(1+cos(2*a1*x+2*b1))/2

                num1=abs(2*n1*m2)
                num2=abs(n2*m1)  
                bcnn = (num1 * num2) // math.gcd(num1, num2)
                t=pi*bcnn/(abs(m1*m2))

                d = [
                    '$%s$'%(latex(2*pi/abs(2*a1))),
                    ]
                da= random.choice(d)
                s = [
                    '$%s$'%(latex(pi/abs(2*a1))),
                    '$%s$'%(latex(2*pi/abs(a1))),
                    '$%s$'%(latex(3*pi/abs(2*a1))),
                    '$%s$'%(latex(2*pi/abs(3*a1))),
                    '$%s$'%(latex(4*pi/abs(2*a1))),
                    '$%s$'%(latex(2*pi/abs(4*a1))),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Hàm số $y=%s$ có chu kỳ là  \n'
                                %(latex(hs1))
                            ) 

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
                        '\\hspace*{1cm} $y=%s=%s$.\\\\ \n'   

                        'Vậy chu kỳ của hàm số đã cho là $T=\\dfrac{2\\pi}{%s}=%s$.'

                        %(latex(hs1),latex(hs11),latex(abs(2*a1)),latex(2*pi/abs(2*a1))
                        ))
            if dang=='1':
                x=symbols('x')
                k=symbols('k')
                m1=randint(-9,9)
                n1=randint(-9,9)
                p1=randint(-9,9)
                q1=randint(-9,9)
                while m1==0 or n1==0 or q1==0:
                    m1=randint(-9,9)
                    n1=randint(-9,9)
                    p1=randint(-9,9)
                    q1=randint(-9,9)
                a1=Rational(m1,n1)
                b1=Rational(p1,q1)
                f1=sin(a1*x+b1*pi)

                m2=randint(-9,9)
                n2=randint(-9,9)
                p2=randint(-9,9)
                q2=randint(-9,9)
                while m2==0 or n2==0 or q2==0:
                    m2=randint(-9,9)
                    n2=randint(-9,9)
                    p2=randint(-9,9)
                    q2=randint(-9,9)
                a2=Rational(m2,n2)
                b2=Rational(p2,q2)
                f2=tan(a2*x+b2*pi)

                hs1=(sin(a1*x+b1))**2
                hs11=(1-cos(2*a1*x+2*b1))/2

                num1=abs(2*n1*m2)
                num2=abs(n2*m1)  
                bcnn = (num1 * num2) // math.gcd(num1, num2)
                t=pi*bcnn/(abs(m1*m2))

                d = [
                    '$%s$'%(latex(2*pi/abs(2*a1))),
                    ]
                da= random.choice(d)
                s = [
                    '$%s$'%(latex(pi/abs(2*a1))),
                    '$%s$'%(latex(2*pi/abs(a1))),
                    '$%s$'%(latex(3*pi/abs(2*a1))),
                    '$%s$'%(latex(2*pi/abs(3*a1))),
                    '$%s$'%(latex(4*pi/abs(2*a1))),
                    '$%s$'%(latex(2*pi/abs(4*a1))),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Hàm số $y=%s$ có chu kỳ là  \n'
                                %(latex(hs1))
                            ) 

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
                        '\\hspace*{1cm} $y=%s=%s$.\\\\ \n'   

                        'Vậy chu kỳ của hàm số đã cho là $T=\\dfrac{2\\pi}{%s}=%s$.'

                        %(latex(hs1),latex(hs11),latex(abs(2*a1)),latex(2*pi/abs(2*a1))
                        ))


            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n '+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('--', '').replace('+-', '-').replace('0+', '').replace('0-', '-')
            return content


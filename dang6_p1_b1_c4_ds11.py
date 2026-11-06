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


def bt_dang6_p1_b1_c4_ds11(self):
            # Khai báo biến
            lisdang=['1','2','3','4','5']
            dang=random.choice(lisdang)
            # Khai báo biến 
            if dang=='5':
                lis0=[1,4,9,16,25,36,49,64,81]
                lis1=[1,2,3,4,5,6,7,8,9,10,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,0]
                a1=0
                b1=0
                c1=0
                d1=randint(1,9)
                e1=random.choice(lis1)

                lis2=[1,2,3,4,5,6,7,8,9,10,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
                a2=random.choice(lis0)
                b2=random.choice(lis2)
                lis2.remove(b2)
                c2=random.choice(lis2)
                lis2.remove(c2)
                d2=0
                e2=0

                n=symbols('n')
                y=(sqrt(a1*n**2+b1*n+c1)+d1*n+e1)/(sqrt(a2*n**2+b2*n+c2)+d2*n+e2)

                tu=sqrt(a1+b1/n+c1/n**2)+d1+e1/n
                mau=sqrt(a2+b2/n+c2/n**2)+d2+e2/n

                du = ['$%s$'%(latex(Rational(sqrt(a1)+d1,sqrt(a2)+d2))),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(1+Rational(sqrt(a1)+d1,sqrt(a2)+d2))),
                    '$%s$'%(latex(2+Rational(sqrt(a1)+d1,sqrt(a2)+d2))),
                    '$%s$'%(latex(3+Rational(sqrt(a1)+d1,sqrt(a2)+d2))),
                    '$%s$'%(latex(-1+Rational(sqrt(a1)+d1,sqrt(a2)+d2))),
                    '$%s$'%(latex(-2+Rational(sqrt(a1)+d1,sqrt(a2)+d2))),
                    '$%s$'%(latex(-3+Rational(sqrt(a1)+d1,sqrt(a2)+d2))),
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho $u_n=%s$. Giới hạn của dãy số $(u_n)$ là'
                                %(latex(y)
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
                loigiai=('Ta có \\\\ \n'
                        '\\hspace*{1cm} $\\underset{n \\to +\\infty} \\lim (u_n)=\\underset{n \\to +\\infty} \\lim %s = \\underset{n \\to +\\infty} \\lim \\dfrac{%s}{%s}$ \\\\ \n' 
                        '\\hspace*{2.9cm} $=\\dfrac{\\underset{n \\to +\\infty} \\lim \\left( %s \\right)}{\\underset{n \\to +\\infty} \\lim \\left( %s \\right)}=%s$.'
                        %(latex(y),
                        latex(tu),latex(mau),latex(tu),latex(mau),latex(Rational(sqrt(a1)+d1,sqrt(a2)+d2))
                        ))
            if dang=='4':
                lis0=[1,4,9,16,25,36,49,64,81]
                lis1=[1,2,3,4,5,6,7,8,9,10,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,0]
                a1=random.choice(lis0)
                b1=random.choice(lis1)
                lis1.remove(b1)
                c1=random.choice(lis1)
                lis1.remove(c1)
                d1=0
                e1=0

                lis2=[1,2,3,4,5,6,7,8,9,10,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
                a2=0
                b2=0
                c2=0
                d2=randint(1,9)
                e2=random.choice(lis2)



                n=symbols('n')
                y=(sqrt(a1*n**2+b1*n+c1)+d1*n+e1)/(sqrt(a2*n**2+b2*n+c2)+d2*n+e2)

                tu=sqrt(a1+b1/n+c1/n**2)+d1+e1/n
                mau=sqrt(a2+b2/n+c2/n**2)+d2+e2/n

                du = ['$%s$'%(latex(Rational(sqrt(a1)+d1,sqrt(a2)+d2))),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(1+Rational(sqrt(a1)+d1,sqrt(a2)+d2))),
                    '$%s$'%(latex(2+Rational(sqrt(a1)+d1,sqrt(a2)+d2))),
                    '$%s$'%(latex(3+Rational(sqrt(a1)+d1,sqrt(a2)+d2))),
                    '$%s$'%(latex(-1+Rational(sqrt(a1)+d1,sqrt(a2)+d2))),
                    '$%s$'%(latex(-2+Rational(sqrt(a1)+d1,sqrt(a2)+d2))),
                    '$%s$'%(latex(-3+Rational(sqrt(a1)+d1,sqrt(a2)+d2))),
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho $u_n=%s$. Giới hạn của dãy số $(u_n)$ là'
                                %(latex(y)
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
                loigiai=('Ta có \\\\ \n'
                        '\\hspace*{1cm} $\\underset{n \\to +\\infty} \\lim (u_n)=\\underset{n \\to +\\infty} \\lim %s = \\underset{n \\to +\\infty} \\lim \\dfrac{%s}{%s}$ \\\\ \n' 
                        '\\hspace*{2.9cm} $=\\dfrac{\\underset{n \\to +\\infty} \\lim \\left( %s \\right)}{\\underset{n \\to +\\infty} \\lim \\left( %s \\right)}=%s$.'
                        %(latex(y),
                        latex(tu),latex(mau),latex(tu),latex(mau),latex(Rational(sqrt(a1)+d1,sqrt(a2)+d2))
                        ))
            if dang=='3':
                lis0=[1,4,9,16,25,36,49,64,81]
                lis1=[1,2,3,4,5,6,7,8,9,10,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,0]
                a1=0
                b1=random.choice(lis1)
                lis1.remove(b1)
                c1=random.choice(lis1)
                lis1.remove(c1)
                d1=randint(1,9)
                e1=random.choice(lis1)

                lis2=[1,2,3,4,5,6,7,8,9,10,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
                a2=random.choice(lis0)
                b2=random.choice(lis2)
                lis2.remove(b2)
                c2=random.choice(lis2)
                lis2.remove(c2)
                d2=randint(1,9)
                e2=random.choice(lis2)

                n=symbols('n')
                y=(d1*n+e1)/(sqrt(a2*n**2+b2*n+c2)+d2*n+e2)

                tu=d1+e1/n
                mau=sqrt(a2+b2/n+c2/n**2)+d2+e2/n

                du = ['$%s$'%(latex(Rational(sqrt(a1)+d1,sqrt(a2)+d2))),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(1+Rational(sqrt(a1)+d1,sqrt(a2)+d2))),
                    '$%s$'%(latex(2+Rational(sqrt(a1)+d1,sqrt(a2)+d2))),
                    '$%s$'%(latex(3+Rational(sqrt(a1)+d1,sqrt(a2)+d2))),
                    '$%s$'%(latex(-1+Rational(sqrt(a1)+d1,sqrt(a2)+d2))),
                    '$%s$'%(latex(-2+Rational(sqrt(a1)+d1,sqrt(a2)+d2))),
                    '$%s$'%(latex(-3+Rational(sqrt(a1)+d1,sqrt(a2)+d2))),
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho $u_n=%s$. Giới hạn của dãy số $(u_n)$ là'
                                %(latex(y)
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
                loigiai=('Ta có \\\\ \n'
                        '\\hspace*{1cm} $\\underset{n \\to +\\infty} \\lim (u_n)=\\underset{n \\to +\\infty} \\lim %s = \\underset{n \\to +\\infty} \\lim \\dfrac{%s}{%s}$ \\\\ \n' 
                        '\\hspace*{2.9cm} $=\\dfrac{\\underset{n \\to +\\infty} \\lim \\left( %s \\right)}{\\underset{n \\to +\\infty} \\lim \\left( %s \\right)}=%s$.'
                        %(latex(y),
                        latex(tu),latex(mau),latex(tu),latex(mau),latex(Rational(sqrt(a1)+d1,sqrt(a2)+d2))
                        ))

            if dang=='2':
                lis0=[1,4,9,16,25,36,49,64,81]
                lis1=[1,2,3,4,5,6,7,8,9,10,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,0]
                a1=random.choice(lis0)
                b1=random.choice(lis1)
                lis1.remove(b1)
                c1=random.choice(lis1)
                lis1.remove(c1)
                d1=randint(1,9)
                e1=random.choice(lis1)

                lis2=[1,2,3,4,5,6,7,8,9,10,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
                a2=0
                b2=random.choice(lis2)
                lis2.remove(b2)
                c2=random.choice(lis2)
                lis2.remove(c2)
                d2=randint(1,9)
                e2=random.choice(lis2)

                n=symbols('n')
                y=(sqrt(a1*n**2+b1*n+c1)+d1*n+e1)/(sqrt(a2*n**2+b2*n+c2)+d2*n+e2)

                tu=sqrt(a1+b1/n+c1/n**2)+d1+e1/n
                mau=sqrt(a2+b2/n+c2/n**2)+d2+e2/n

                du = ['$%s$'%(latex(Rational(sqrt(a1)+d1,sqrt(a2)+d2))),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(1+Rational(sqrt(a1)+d1,sqrt(a2)+d2))),
                    '$%s$'%(latex(2+Rational(sqrt(a1)+d1,sqrt(a2)+d2))),
                    '$%s$'%(latex(3+Rational(sqrt(a1)+d1,sqrt(a2)+d2))),
                    '$%s$'%(latex(-1+Rational(sqrt(a1)+d1,sqrt(a2)+d2))),
                    '$%s$'%(latex(-2+Rational(sqrt(a1)+d1,sqrt(a2)+d2))),
                    '$%s$'%(latex(-3+Rational(sqrt(a1)+d1,sqrt(a2)+d2))),
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho $u_n=%s$. Giới hạn của dãy số $(u_n)$ là'
                                %(latex(y)
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
                loigiai=('Ta có \\\\ \n'
                        '\\hspace*{1cm} $\\underset{n \\to +\\infty} \\lim (u_n)=\\underset{n \\to +\\infty} \\lim %s = \\underset{n \\to +\\infty} \\lim \\dfrac{%s}{%s}$ \\\\ \n' 
                        '\\hspace*{2.9cm} $=\\dfrac{\\underset{n \\to +\\infty} \\lim \\left( %s \\right)}{\\underset{n \\to +\\infty} \\lim \\left( %s \\right)}=%s$.'
                        %(latex(y),
                        latex(tu),latex(mau),latex(tu),latex(mau),latex(Rational(sqrt(a1)+d1,sqrt(a2)+d2))
                        ))

            if dang=='1':
                lis0=[1,4,9,16,25,36,49,64,81]
                lis1=[1,2,3,4,5,6,7,8,9,10,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,0]
                a1=random.choice(lis0)
                b1=random.choice(lis1)
                lis1.remove(b1)
                c1=random.choice(lis1)
                lis1.remove(c1)
                d1=randint(1,9)
                e1=random.choice(lis1)

                lis2=[1,2,3,4,5,6,7,8,9,10,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
                a2=random.choice(lis0)
                b2=random.choice(lis2)
                lis2.remove(b2)
                c2=random.choice(lis2)
                lis2.remove(c2)
                d2=randint(1,9)
                e2=random.choice(lis2)



                n=symbols('n')
                y=(sqrt(a1*n**2+b1*n+c1)+d1*n+e1)/(sqrt(a2*n**2+b2*n+c2)+d2*n+e2)

                tu=sqrt(a1+b1/n+c1/n**2)+d1+e1/n
                mau=sqrt(a2+b2/n+c2/n**2)+d2+e2/n

                du = ['$%s$'%(latex(Rational(sqrt(a1)+d1,sqrt(a2)+d2))),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(1+Rational(sqrt(a1)+d1,sqrt(a2)+d2))),
                    '$%s$'%(latex(2+Rational(sqrt(a1)+d1,sqrt(a2)+d2))),
                    '$%s$'%(latex(3+Rational(sqrt(a1)+d1,sqrt(a2)+d2))),
                    '$%s$'%(latex(-1+Rational(sqrt(a1)+d1,sqrt(a2)+d2))),
                    '$%s$'%(latex(-2+Rational(sqrt(a1)+d1,sqrt(a2)+d2))),
                    '$%s$'%(latex(-3+Rational(sqrt(a1)+d1,sqrt(a2)+d2))),
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho $u_n=%s$. Giới hạn của dãy số $(u_n)$ là'
                                %(latex(y)
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
                loigiai=('Ta có \\\\ \n'
                        '\\hspace*{1cm} $\\underset{n \\to +\\infty} \\lim (u_n)=\\underset{n \\to +\\infty} \\lim %s = \\underset{n \\to +\\infty} \\lim \\dfrac{%s}{%s}$ \\\\ \n' 
                        '\\hspace*{2.9cm} $=\\dfrac{\\underset{n \\to +\\infty} \\lim \\left( %s \\right)}{\\underset{n \\to +\\infty} \\lim \\left( %s \\right)}=%s$.'
                        %(latex(y),
                        latex(tu),latex(mau),latex(tu),latex(mau),latex(Rational(sqrt(a1)+d1,sqrt(a2)+d2))
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content


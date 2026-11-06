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


def bt_dang14_p1_b2_c1_ds12(self):
            # Khai báo biến
            lisdang=['1','2','3','4','5','6','7','8','9']
            dang=random.choice(lisdang)
            if dang=='9':
                # Khai báo biến
                x=symbols('x')
                x1=randint(1,9)
                x2=randint(1,9)
                while x1>x2:
                    x1=randint(1,9)
                    x2=randint(1,9)
                f=sqrt(x1+x)+sqrt(x2-x)
                daoham=1/(2*sqrt(x1+x))-1/(2*sqrt(x2-x))
                x0=Rational(x2-x1,2)
                f1=sqrt(x1+x1)+sqrt(x2-x1)
                f2=sqrt(x1+x2)+sqrt(x2-x2)
                f0=sqrt(x1+x0)+sqrt(x2-x0)
                gtln=f0
                gtnn=min(f1,f2)

                du = ['$%s$'%(latex(gtln*gtnn)),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(gtnn)),
                    '$%s$'%(latex(-gtln)),
                    '$%s$'%(latex(x0)),
                    '$%s$'%(latex(x1)),
                    '$%s$'%(latex(-gtnn)),
                    '$%s$'%(latex(x2)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('''Cho hàm số $y=%s$. Tích giá trị lớn nhất và giá trị nhỏ nhất của hàm số là'''
                                %(latex(f)
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
                loigiai=('Tập xác định: $\\mathscr{D}=[%s;%s]$.\\\\ \n'
                        '''Ta có $y'=%s.\\\\ \n''' 
                        '''\\hspace*{1.1cm}y'=0 \\Leftrightarrow x=%s$.\\\\ \n'''
                        '''Bảng biến thiên\\\\ \n'''
                        '\\hspace*{1cm} \\begin{tikzpicture}[line join=round,>=stealth] \n'
                            '\\def\\myltespcl{3}\\def\\myltlgt{2}\\def\\myltdeltacl{0.5} \n'
                            '\\def\\myltx{1}\\def\\mylta{0.7}\\def\\myltb{2.1}\\def\\myltc{\\myltb/3} \n'
                            '\\path(\\myltlgt/2,-\\myltx/2) node {$x$}(\\myltlgt/2,-\\myltx-\\mylta/2) node {$y\'$}(\\myltlgt/2,-\\myltx-\\mylta-\\myltb/2) node {$y$}; \n'
                            '\\draw(0,-\\myltx)--(\\myltlgt+4*\\myltespcl+2*\\myltdeltacl,-\\myltx)(0,-\\myltx-\\mylta)--(\\myltlgt+4*\\myltespcl+2*\\myltdeltacl,-\\myltx-\\mylta)(\\myltlgt,0)--(\\myltlgt,-\\myltx-\\mylta-\\myltb);  \n'
                            '\\draw(0,0) rectangle (\\myltlgt+4*\\myltespcl+2*\\myltdeltacl,-\\myltx-\\mylta-\\myltb); \n'
                            '\\path(\\myltlgt+\\myltdeltacl,-\\myltx/2) node {$-\\infty$}; \n'
                            '\\fill[pattern=north west lines](\\myltlgt,-\\myltx) rectangle (\\myltlgt+\\myltdeltacl+\\myltespcl,-\\myltx-\\mylta); \n'
                            '\\path(\\myltlgt+\\myltdeltacl+\\myltespcl,-\\myltx/2) node {$%s$}; \n'
                            '\\draw[double](\\myltlgt+\\myltdeltacl+\\myltespcl,-\\myltx)--(\\myltlgt+\\myltdeltacl+\\myltespcl,-\\myltx-\\mylta); \n'
                            '\\path(\\myltlgt+\\myltdeltacl+1.5*\\myltespcl,-\\myltx-\\mylta/2) node {$+$}; \n'
                            '\\path(\\myltlgt+\\myltdeltacl+2*\\myltespcl,-\\myltx/2) node {$%s$}; \n'
                            '\\path(\\myltlgt+\\myltdeltacl+2.5*\\myltespcl,-\\myltx-\\mylta/2) node {$-$}; \n'
                            '\\path(\\myltlgt+\\myltdeltacl+3*\\myltespcl,-\\myltx/2) node {$%s$}; \n'
                            '\\draw[double](\\myltlgt+\\myltdeltacl+3*\\myltespcl,-\\myltx)--(\\myltlgt+\\myltdeltacl+3*\\myltespcl,-\\myltx-\\mylta); \n'
                            '\\fill[pattern=north west lines](\\myltlgt+\\myltdeltacl+3*\\myltespcl,-\\myltx) rectangle (\\myltlgt+2*\\myltdeltacl+4*\\myltespcl,-\\myltx-\\mylta); \n'
                            '\\path(\\myltlgt+\\myltdeltacl+4*\\myltespcl,-\\myltx/2) node {$+\\infty$}; \n'
                            '\\path(\\myltlgt+\\myltdeltacl+2*\\myltespcl,-\\myltx-\\mylta/2) node {$0$}; \n'
                            '\\fill[pattern=north west lines](\\myltlgt,-\\myltx-\\mylta) rectangle (\\myltlgt+\\myltdeltacl+\\myltespcl,-\\myltx-\\mylta-\\myltb); \n'
                            '\\fill[pattern=north west lines](\\myltlgt+\\myltdeltacl+3*\\myltespcl,-\\myltx-\\mylta) rectangle (\\myltlgt+2*\\myltdeltacl+4*\\myltespcl,-\\myltx-\\mylta-\\myltb); \n'
                            '\\node (nmyltb) at (\\myltlgt+\\myltdeltacl+\\myltespcl,-\\myltx-\\mylta-2.5*\\myltc) {$%s$}; \n'
                            '\\node (nmyltc) at (\\myltlgt+\\myltdeltacl+2*\\myltespcl,-\\myltx-\\mylta-0.5*\\myltc) {$%s$}; \n'
                            '\\node (nmyltd) at (\\myltlgt+\\myltdeltacl+3*\\myltespcl,-\\myltx-\\mylta-2.5*\\myltc) {$%s$}; \n'
                            '\\draw[->] (nmyltb)--(nmyltc);'
                            '\\draw[->] (nmyltc)--(nmyltd);'
                        '\\end{tikzpicture} \\\\ \n'

                        'Từ bảng biến thiên ta có \\\\ \n'
                        '''\\hspace*{1cm} Hàm số có giá trị lớn nhất là $%s$. \\\\ \n'''
                        '''\\hspace*{1cm} Hàm số có giá trị nhỏ nhất là $%s$. '''
                        %(latex(-x1),latex(x2),
                        latex(daoham),
                        latex(x0),
                        latex(x1),latex(x0),latex(x2),
                        latex(f1),latex(f0),latex(f2),
                        latex(gtln),
                        latex(gtnn)
                        ))
            if dang=='8':
                # Khai báo biến
                x=symbols('x')
                x1=randint(1,9)
                x2=randint(1,9)
                while x1>x2:
                    x1=randint(1,9)
                    x2=randint(1,9)
                f=sqrt(x1+x)+sqrt(x2-x)
                daoham=1/(2*sqrt(x1+x))-1/(2*sqrt(x2-x))
                x0=Rational(x2-x1,2)
                f1=sqrt(x1+x1)+sqrt(x2-x1)
                f2=sqrt(x1+x2)+sqrt(x2-x2)
                f0=sqrt(x1+x0)+sqrt(x2-x0)
                gtln=f0
                gtnn=min(f1,f2)

                du = ['$%s$'%(latex(gtln-gtnn)),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(gtnn)),
                    '$%s$'%(latex(-gtln)),
                    '$%s$'%(latex(x0)),
                    '$%s$'%(latex(x1)),
                    '$%s$'%(latex(-gtnn)),
                    '$%s$'%(latex(x2)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('''Cho hàm số $y=%s$. Hiệu giá trị lớn nhất và giá trị nhỏ nhất của hàm số là '''
                                %(latex(f)
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
                loigiai=('Tập xác định: $\\mathscr{D}=[%s;%s]$.\\\\ \n'
                        '''Ta có $y'=%s.\\\\ \n''' 
                        '''\\hspace*{1.1cm}y'=0 \\Leftrightarrow x=%s$.\\\\ \n'''
                        '''Bảng biến thiên\\\\ \n'''
                        '\\hspace*{1cm} \\begin{tikzpicture}[line join=round,>=stealth] \n'
                            '\\def\\myltespcl{3}\\def\\myltlgt{2}\\def\\myltdeltacl{0.5} \n'
                            '\\def\\myltx{1}\\def\\mylta{0.7}\\def\\myltb{2.1}\\def\\myltc{\\myltb/3} \n'
                            '\\path(\\myltlgt/2,-\\myltx/2) node {$x$}(\\myltlgt/2,-\\myltx-\\mylta/2) node {$y\'$}(\\myltlgt/2,-\\myltx-\\mylta-\\myltb/2) node {$y$}; \n'
                            '\\draw(0,-\\myltx)--(\\myltlgt+4*\\myltespcl+2*\\myltdeltacl,-\\myltx)(0,-\\myltx-\\mylta)--(\\myltlgt+4*\\myltespcl+2*\\myltdeltacl,-\\myltx-\\mylta)(\\myltlgt,0)--(\\myltlgt,-\\myltx-\\mylta-\\myltb);  \n'
                            '\\draw(0,0) rectangle (\\myltlgt+4*\\myltespcl+2*\\myltdeltacl,-\\myltx-\\mylta-\\myltb); \n'
                            '\\path(\\myltlgt+\\myltdeltacl,-\\myltx/2) node {$-\\infty$}; \n'
                            '\\fill[pattern=north west lines](\\myltlgt,-\\myltx) rectangle (\\myltlgt+\\myltdeltacl+\\myltespcl,-\\myltx-\\mylta); \n'
                            '\\path(\\myltlgt+\\myltdeltacl+\\myltespcl,-\\myltx/2) node {$%s$}; \n'
                            '\\draw[double](\\myltlgt+\\myltdeltacl+\\myltespcl,-\\myltx)--(\\myltlgt+\\myltdeltacl+\\myltespcl,-\\myltx-\\mylta); \n'
                            '\\path(\\myltlgt+\\myltdeltacl+1.5*\\myltespcl,-\\myltx-\\mylta/2) node {$+$}; \n'
                            '\\path(\\myltlgt+\\myltdeltacl+2*\\myltespcl,-\\myltx/2) node {$%s$}; \n'
                            '\\path(\\myltlgt+\\myltdeltacl+2.5*\\myltespcl,-\\myltx-\\mylta/2) node {$-$}; \n'
                            '\\path(\\myltlgt+\\myltdeltacl+3*\\myltespcl,-\\myltx/2) node {$%s$}; \n'
                            '\\draw[double](\\myltlgt+\\myltdeltacl+3*\\myltespcl,-\\myltx)--(\\myltlgt+\\myltdeltacl+3*\\myltespcl,-\\myltx-\\mylta); \n'
                            '\\fill[pattern=north west lines](\\myltlgt+\\myltdeltacl+3*\\myltespcl,-\\myltx) rectangle (\\myltlgt+2*\\myltdeltacl+4*\\myltespcl,-\\myltx-\\mylta); \n'
                            '\\path(\\myltlgt+\\myltdeltacl+4*\\myltespcl,-\\myltx/2) node {$+\\infty$}; \n'
                            '\\path(\\myltlgt+\\myltdeltacl+2*\\myltespcl,-\\myltx-\\mylta/2) node {$0$}; \n'
                            '\\fill[pattern=north west lines](\\myltlgt,-\\myltx-\\mylta) rectangle (\\myltlgt+\\myltdeltacl+\\myltespcl,-\\myltx-\\mylta-\\myltb); \n'
                            '\\fill[pattern=north west lines](\\myltlgt+\\myltdeltacl+3*\\myltespcl,-\\myltx-\\mylta) rectangle (\\myltlgt+2*\\myltdeltacl+4*\\myltespcl,-\\myltx-\\mylta-\\myltb); \n'
                            '\\node (nmyltb) at (\\myltlgt+\\myltdeltacl+\\myltespcl,-\\myltx-\\mylta-2.5*\\myltc) {$%s$}; \n'
                            '\\node (nmyltc) at (\\myltlgt+\\myltdeltacl+2*\\myltespcl,-\\myltx-\\mylta-0.5*\\myltc) {$%s$}; \n'
                            '\\node (nmyltd) at (\\myltlgt+\\myltdeltacl+3*\\myltespcl,-\\myltx-\\mylta-2.5*\\myltc) {$%s$}; \n'
                            '\\draw[->] (nmyltb)--(nmyltc);'
                            '\\draw[->] (nmyltc)--(nmyltd);'
                        '\\end{tikzpicture} \\\\ \n'

                        'Từ bảng biến thiên ta có \\\\ \n'
                        '''\\hspace*{1cm} Hàm số có giá trị lớn nhất là $%s$. \\\\ \n'''
                        '''\\hspace*{1cm} Hàm số có giá trị nhỏ nhất là $%s$. '''
                        %(latex(-x1),latex(x2),
                        latex(daoham),
                        latex(x0),
                        latex(x1),latex(x0),latex(x2),
                        latex(f1),latex(f0),latex(f2),
                        latex(gtln),
                        latex(gtnn)
                        ))
            if dang=='7':
                # Khai báo biến
                x=symbols('x')
                x1=randint(1,9)
                x2=randint(1,9)
                while x1>x2:
                    x1=randint(1,9)
                    x2=randint(1,9)
                f=sqrt(x1+x)+sqrt(x2-x)
                daoham=1/(2*sqrt(x1+x))-1/(2*sqrt(x2-x))
                x0=Rational(x2-x1,2)
                f1=sqrt(x1+x1)+sqrt(x2-x1)
                f2=sqrt(x1+x2)+sqrt(x2-x2)
                f0=sqrt(x1+x0)+sqrt(x2-x0)
                gtln=f0
                gtnn=min(f1,f2)

                du = ['$%s$'%(latex(gtln+gtnn)),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(gtnn)),
                    '$%s$'%(latex(-gtln)),
                    '$%s$'%(latex(x0)),
                    '$%s$'%(latex(x1)),
                    '$%s$'%(latex(-gtnn)),
                    '$%s$'%(latex(x2)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('''Cho hàm số $y=%s$. Tổng giá trị lớn nhất và giá trị nhỏ nhất của hàm số là'''
                                %(latex(f)
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
                loigiai=('Tập xác định: $\\mathscr{D}=[%s;%s]$.\\\\ \n'
                        '''Ta có $y'=%s.\\\\ \n''' 
                        '''\\hspace*{1.1cm}y'=0 \\Leftrightarrow x=%s$.\\\\ \n'''
                        '''Bảng biến thiên\\\\ \n'''
                        '\\hspace*{1cm} \\begin{tikzpicture}[line join=round,>=stealth] \n'
                            '\\def\\myltespcl{3}\\def\\myltlgt{2}\\def\\myltdeltacl{0.5} \n'
                            '\\def\\myltx{1}\\def\\mylta{0.7}\\def\\myltb{2.1}\\def\\myltc{\\myltb/3} \n'
                            '\\path(\\myltlgt/2,-\\myltx/2) node {$x$}(\\myltlgt/2,-\\myltx-\\mylta/2) node {$y\'$}(\\myltlgt/2,-\\myltx-\\mylta-\\myltb/2) node {$y$}; \n'
                            '\\draw(0,-\\myltx)--(\\myltlgt+4*\\myltespcl+2*\\myltdeltacl,-\\myltx)(0,-\\myltx-\\mylta)--(\\myltlgt+4*\\myltespcl+2*\\myltdeltacl,-\\myltx-\\mylta)(\\myltlgt,0)--(\\myltlgt,-\\myltx-\\mylta-\\myltb);  \n'
                            '\\draw(0,0) rectangle (\\myltlgt+4*\\myltespcl+2*\\myltdeltacl,-\\myltx-\\mylta-\\myltb); \n'
                            '\\path(\\myltlgt+\\myltdeltacl,-\\myltx/2) node {$-\\infty$}; \n'
                            '\\fill[pattern=north west lines](\\myltlgt,-\\myltx) rectangle (\\myltlgt+\\myltdeltacl+\\myltespcl,-\\myltx-\\mylta); \n'
                            '\\path(\\myltlgt+\\myltdeltacl+\\myltespcl,-\\myltx/2) node {$%s$}; \n'
                            '\\draw[double](\\myltlgt+\\myltdeltacl+\\myltespcl,-\\myltx)--(\\myltlgt+\\myltdeltacl+\\myltespcl,-\\myltx-\\mylta); \n'
                            '\\path(\\myltlgt+\\myltdeltacl+1.5*\\myltespcl,-\\myltx-\\mylta/2) node {$+$}; \n'
                            '\\path(\\myltlgt+\\myltdeltacl+2*\\myltespcl,-\\myltx/2) node {$%s$}; \n'
                            '\\path(\\myltlgt+\\myltdeltacl+2.5*\\myltespcl,-\\myltx-\\mylta/2) node {$-$}; \n'
                            '\\path(\\myltlgt+\\myltdeltacl+3*\\myltespcl,-\\myltx/2) node {$%s$}; \n'
                            '\\draw[double](\\myltlgt+\\myltdeltacl+3*\\myltespcl,-\\myltx)--(\\myltlgt+\\myltdeltacl+3*\\myltespcl,-\\myltx-\\mylta); \n'
                            '\\fill[pattern=north west lines](\\myltlgt+\\myltdeltacl+3*\\myltespcl,-\\myltx) rectangle (\\myltlgt+2*\\myltdeltacl+4*\\myltespcl,-\\myltx-\\mylta); \n'
                            '\\path(\\myltlgt+\\myltdeltacl+4*\\myltespcl,-\\myltx/2) node {$+\\infty$}; \n'
                            '\\path(\\myltlgt+\\myltdeltacl+2*\\myltespcl,-\\myltx-\\mylta/2) node {$0$}; \n'
                            '\\fill[pattern=north west lines](\\myltlgt,-\\myltx-\\mylta) rectangle (\\myltlgt+\\myltdeltacl+\\myltespcl,-\\myltx-\\mylta-\\myltb); \n'
                            '\\fill[pattern=north west lines](\\myltlgt+\\myltdeltacl+3*\\myltespcl,-\\myltx-\\mylta) rectangle (\\myltlgt+2*\\myltdeltacl+4*\\myltespcl,-\\myltx-\\mylta-\\myltb); \n'
                            '\\node (nmyltb) at (\\myltlgt+\\myltdeltacl+\\myltespcl,-\\myltx-\\mylta-2.5*\\myltc) {$%s$}; \n'
                            '\\node (nmyltc) at (\\myltlgt+\\myltdeltacl+2*\\myltespcl,-\\myltx-\\mylta-0.5*\\myltc) {$%s$}; \n'
                            '\\node (nmyltd) at (\\myltlgt+\\myltdeltacl+3*\\myltespcl,-\\myltx-\\mylta-2.5*\\myltc) {$%s$}; \n'
                            '\\draw[->] (nmyltb)--(nmyltc);'
                            '\\draw[->] (nmyltc)--(nmyltd);'
                        '\\end{tikzpicture} \\\\ \n'
                        'Từ bảng biến thiên ta có \\\\ \n'
                        '''\\hspace*{1cm} Hàm số có giá trị lớn nhất là $%s$. \\\\ \n'''
                        '''\\hspace*{1cm} Hàm số có giá trị nhỏ nhất là $%s$. '''
                        %(latex(-x1),latex(x2),
                        latex(daoham),
                        latex(x0),
                        latex(x1),latex(x0),latex(x2),
                        latex(f1),latex(f0),latex(f2),
                        latex(gtln),
                        latex(gtnn)
                        ))
            if dang=='6':
                # Khai báo biến
                x=symbols('x')
                x1=randint(1,9)
                x2=randint(1,9)
                while x1>x2:
                    x1=randint(1,9)
                    x2=randint(1,9)
                f=sqrt(x1+x)+sqrt(x2-x)
                daoham=1/(2*sqrt(x1+x))-1/(2*sqrt(x2-x))
                x0=Rational(x2-x1,2)
                f1=sqrt(x1+x1)+sqrt(x2-x1)
                f2=sqrt(x1+x2)+sqrt(x2-x2)
                f0=sqrt(x1+x0)+sqrt(x2-x0)
                gtln=f0
                gtnn=min(f1,f2)

                du = ['$x=%s$'%(latex(x0)),
                    ]
                da= random.choice(du)
                s = ['$x=%s$'%(latex(gtnn)),
                    '$x=%s$'%(latex(-gtln)),
                    '$x=%s$'%(latex(gtln)),
                    '$x=%s$'%(latex(x1)),
                    '$x=%s$'%(latex(-gtnn)),
                    '$x=%s$'%(latex(x2)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('''Cho hàm số $y=%s$. Hàm số đạt giá trị lớn nhất tại điểm '''
                                %(latex(f)
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
                loigiai=('Tập xác định: $\\mathscr{D}=[%s;%s]$.\\\\ \n'
                        '''Ta có $y'=%s.\\\\ \n''' 
                        '''\\hspace*{1.1cm}y'=0 \\Leftrightarrow x=%s$.\\\\ \n'''
                        '''Bảng biến thiên\\\\ \n'''
                        '\\hspace*{1cm} \\begin{tikzpicture}[line join=round,>=stealth] \n'
                            '\\def\\myltespcl{3}\\def\\myltlgt{2}\\def\\myltdeltacl{0.5} \n'
                            '\\def\\myltx{1}\\def\\mylta{0.7}\\def\\myltb{2.1}\\def\\myltc{\\myltb/3} \n'
                            '\\path(\\myltlgt/2,-\\myltx/2) node {$x$}(\\myltlgt/2,-\\myltx-\\mylta/2) node {$y\'$}(\\myltlgt/2,-\\myltx-\\mylta-\\myltb/2) node {$y$}; \n'
                            '\\draw(0,-\\myltx)--(\\myltlgt+4*\\myltespcl+2*\\myltdeltacl,-\\myltx)(0,-\\myltx-\\mylta)--(\\myltlgt+4*\\myltespcl+2*\\myltdeltacl,-\\myltx-\\mylta)(\\myltlgt,0)--(\\myltlgt,-\\myltx-\\mylta-\\myltb);  \n'
                            '\\draw(0,0) rectangle (\\myltlgt+4*\\myltespcl+2*\\myltdeltacl,-\\myltx-\\mylta-\\myltb); \n'
                            '\\path(\\myltlgt+\\myltdeltacl,-\\myltx/2) node {$-\\infty$}; \n'
                            '\\fill[pattern=north west lines](\\myltlgt,-\\myltx) rectangle (\\myltlgt+\\myltdeltacl+\\myltespcl,-\\myltx-\\mylta); \n'
                            '\\path(\\myltlgt+\\myltdeltacl+\\myltespcl,-\\myltx/2) node {$%s$}; \n'
                            '\\draw[double](\\myltlgt+\\myltdeltacl+\\myltespcl,-\\myltx)--(\\myltlgt+\\myltdeltacl+\\myltespcl,-\\myltx-\\mylta); \n'
                            '\\path(\\myltlgt+\\myltdeltacl+1.5*\\myltespcl,-\\myltx-\\mylta/2) node {$+$}; \n'
                            '\\path(\\myltlgt+\\myltdeltacl+2*\\myltespcl,-\\myltx/2) node {$%s$}; \n'
                            '\\path(\\myltlgt+\\myltdeltacl+2.5*\\myltespcl,-\\myltx-\\mylta/2) node {$-$}; \n'
                            '\\path(\\myltlgt+\\myltdeltacl+3*\\myltespcl,-\\myltx/2) node {$%s$}; \n'
                            '\\draw[double](\\myltlgt+\\myltdeltacl+3*\\myltespcl,-\\myltx)--(\\myltlgt+\\myltdeltacl+3*\\myltespcl,-\\myltx-\\mylta); \n'
                            '\\fill[pattern=north west lines](\\myltlgt+\\myltdeltacl+3*\\myltespcl,-\\myltx) rectangle (\\myltlgt+2*\\myltdeltacl+4*\\myltespcl,-\\myltx-\\mylta); \n'
                            '\\path(\\myltlgt+\\myltdeltacl+4*\\myltespcl,-\\myltx/2) node {$+\\infty$}; \n'
                            '\\path(\\myltlgt+\\myltdeltacl+2*\\myltespcl,-\\myltx-\\mylta/2) node {$0$}; \n'
                            '\\fill[pattern=north west lines](\\myltlgt,-\\myltx-\\mylta) rectangle (\\myltlgt+\\myltdeltacl+\\myltespcl,-\\myltx-\\mylta-\\myltb); \n'
                            '\\fill[pattern=north west lines](\\myltlgt+\\myltdeltacl+3*\\myltespcl,-\\myltx-\\mylta) rectangle (\\myltlgt+2*\\myltdeltacl+4*\\myltespcl,-\\myltx-\\mylta-\\myltb); \n'
                            '\\node (nmyltb) at (\\myltlgt+\\myltdeltacl+\\myltespcl,-\\myltx-\\mylta-2.5*\\myltc) {$%s$}; \n'
                            '\\node (nmyltc) at (\\myltlgt+\\myltdeltacl+2*\\myltespcl,-\\myltx-\\mylta-0.5*\\myltc) {$%s$}; \n'
                            '\\node (nmyltd) at (\\myltlgt+\\myltdeltacl+3*\\myltespcl,-\\myltx-\\mylta-2.5*\\myltc) {$%s$}; \n'
                            '\\draw[->] (nmyltb)--(nmyltc);'
                            '\\draw[->] (nmyltc)--(nmyltd);'
                        '\\end{tikzpicture} \\\\ \n'
                        'Từ bảng biến thiên ta có \\\\ \n'
                        '''\\hspace*{1cm} Hàm số có giá trị lớn nhất là $%s$. \\\\ \n'''
                        '''\\hspace*{1cm} Hàm số có giá trị nhỏ nhất là $%s$. '''
                        %(latex(-x1),latex(x2),
                        latex(daoham),
                        latex(x0),
                        latex(x1),latex(x0),latex(x2),
                        latex(f1),latex(f0),latex(f2),
                        latex(gtln),
                        latex(gtnn)
                        ))
            if dang=='5':
                # Khai báo biến
                x=symbols('x')
                x1=randint(1,9)
                x2=randint(1,9)
                while x1>x2:
                    x1=randint(1,9)
                    x2=randint(1,9)
                f=sqrt(x1+x)+sqrt(x2-x)
                daoham=1/(2*sqrt(x1+x))-1/(2*sqrt(x2-x))
                x0=Rational(x2-x1,2)
                f1=sqrt(x1+x1)+sqrt(x2-x1)
                f2=sqrt(x1+x2)+sqrt(x2-x2)
                f0=sqrt(x1+x0)+sqrt(x2-x0)
                gtln=f0
                gtnn=min(f1,f2)

                du = ['$%s$'%(latex(gtnn)),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(gtln)),
                    '$%s$'%(latex(-gtln)),
                    '$%s$'%(latex(gtnn+1)),
                    '$%s$'%(latex(gtnn+2)),
                    '$%s$'%(latex(-gtnn)),
                    '$%s$'%(latex(gtnn-1)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('''Cho hàm số $y=%s$. Giá trị nhỏ nhất của hàm số là'''
                                %(latex(f)
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
                loigiai=('Tập xác định: $\\mathscr{D}=[%s;%s]$.\\\\ \n'
                        '''Ta có $y'=%s.\\\\ \n''' 
                        '''\\hspace*{1.1cm}y'=0 \\Leftrightarrow x=%s$.\\\\ \n'''
                        '''Bảng biến thiên\\\\ \n'''
                        '\\hspace*{1cm} \\begin{tikzpicture}[line join=round,>=stealth] \n'
                            '\\def\\myltespcl{3}\\def\\myltlgt{2}\\def\\myltdeltacl{0.5} \n'
                            '\\def\\myltx{1}\\def\\mylta{0.7}\\def\\myltb{2.1}\\def\\myltc{\\myltb/3} \n'
                            '\\path(\\myltlgt/2,-\\myltx/2) node {$x$}(\\myltlgt/2,-\\myltx-\\mylta/2) node {$y\'$}(\\myltlgt/2,-\\myltx-\\mylta-\\myltb/2) node {$y$}; \n'
                            '\\draw(0,-\\myltx)--(\\myltlgt+4*\\myltespcl+2*\\myltdeltacl,-\\myltx)(0,-\\myltx-\\mylta)--(\\myltlgt+4*\\myltespcl+2*\\myltdeltacl,-\\myltx-\\mylta)(\\myltlgt,0)--(\\myltlgt,-\\myltx-\\mylta-\\myltb);  \n'
                            '\\draw(0,0) rectangle (\\myltlgt+4*\\myltespcl+2*\\myltdeltacl,-\\myltx-\\mylta-\\myltb); \n'
                            '\\path(\\myltlgt+\\myltdeltacl,-\\myltx/2) node {$-\\infty$}; \n'
                            '\\fill[pattern=north west lines](\\myltlgt,-\\myltx) rectangle (\\myltlgt+\\myltdeltacl+\\myltespcl,-\\myltx-\\mylta); \n'
                            '\\path(\\myltlgt+\\myltdeltacl+\\myltespcl,-\\myltx/2) node {$%s$}; \n'
                            '\\draw[double](\\myltlgt+\\myltdeltacl+\\myltespcl,-\\myltx)--(\\myltlgt+\\myltdeltacl+\\myltespcl,-\\myltx-\\mylta); \n'
                            '\\path(\\myltlgt+\\myltdeltacl+1.5*\\myltespcl,-\\myltx-\\mylta/2) node {$+$}; \n'
                            '\\path(\\myltlgt+\\myltdeltacl+2*\\myltespcl,-\\myltx/2) node {$%s$}; \n'
                            '\\path(\\myltlgt+\\myltdeltacl+2.5*\\myltespcl,-\\myltx-\\mylta/2) node {$-$}; \n'
                            '\\path(\\myltlgt+\\myltdeltacl+3*\\myltespcl,-\\myltx/2) node {$%s$}; \n'
                            '\\draw[double](\\myltlgt+\\myltdeltacl+3*\\myltespcl,-\\myltx)--(\\myltlgt+\\myltdeltacl+3*\\myltespcl,-\\myltx-\\mylta); \n'
                            '\\fill[pattern=north west lines](\\myltlgt+\\myltdeltacl+3*\\myltespcl,-\\myltx) rectangle (\\myltlgt+2*\\myltdeltacl+4*\\myltespcl,-\\myltx-\\mylta); \n'
                            '\\path(\\myltlgt+\\myltdeltacl+4*\\myltespcl,-\\myltx/2) node {$+\\infty$}; \n'
                            '\\path(\\myltlgt+\\myltdeltacl+2*\\myltespcl,-\\myltx-\\mylta/2) node {$0$}; \n'
                            '\\fill[pattern=north west lines](\\myltlgt,-\\myltx-\\mylta) rectangle (\\myltlgt+\\myltdeltacl+\\myltespcl,-\\myltx-\\mylta-\\myltb); \n'
                            '\\fill[pattern=north west lines](\\myltlgt+\\myltdeltacl+3*\\myltespcl,-\\myltx-\\mylta) rectangle (\\myltlgt+2*\\myltdeltacl+4*\\myltespcl,-\\myltx-\\mylta-\\myltb); \n'
                            '\\node (nmyltb) at (\\myltlgt+\\myltdeltacl+\\myltespcl,-\\myltx-\\mylta-2.5*\\myltc) {$%s$}; \n'
                            '\\node (nmyltc) at (\\myltlgt+\\myltdeltacl+2*\\myltespcl,-\\myltx-\\mylta-0.5*\\myltc) {$%s$}; \n'
                            '\\node (nmyltd) at (\\myltlgt+\\myltdeltacl+3*\\myltespcl,-\\myltx-\\mylta-2.5*\\myltc) {$%s$}; \n'
                            '\\draw[->] (nmyltb)--(nmyltc);'
                            '\\draw[->] (nmyltc)--(nmyltd);'
                        '\\end{tikzpicture} \\\\ \n'
                        'Từ bảng biến thiên ta có \\\\ \n'
                        '''\\hspace*{1cm} Hàm số có giá trị lớn nhất là $%s$. \\\\ \n'''
                        '''\\hspace*{1cm} Hàm số có giá trị nhỏ nhất là $%s$.'''
                        %(latex(-x1),latex(x2),
                        latex(daoham),
                        latex(x0),
                        latex(x1),latex(x0),latex(x2),
                        latex(f1),latex(f0),latex(f2),
                        latex(gtln),
                        latex(gtnn)
                        ))
            if dang=='4':
                # Khai báo biến
                x=symbols('x')
                x1=randint(1,9)
                x2=randint(1,9)
                while x1>=x2:
                    x1=randint(1,9)
                    x2=randint(1,9)
                f=sqrt(x1+x)+sqrt(x2-x)
                daoham=1/(2*sqrt(x1+x))-1/(2*sqrt(x2-x))
                x0=Rational(x2-x1,2)
                f1=sqrt(x1+x1)+sqrt(x2-x1)
                f2=sqrt(x1+x2)+sqrt(x2-x2)
                f0=sqrt(x1+x0)+sqrt(x2-x0)
                gtln=f0
                gtnn=min(f1,f2)

                du = ['$%s$'%(latex(gtln)),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(gtln-1)),
                    '$%s$'%(latex(gtln+1)),
                    '$%s$'%(latex(gtln+2)),
                    '$%s$'%(latex(gtln+3)),
                    '$%s$'%(latex(gtln-2)),
                    '$%s$'%(latex(gtln-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('''Cho hàm số $y=%s$. Giá trị lớn nhất của hàm số là'''
                                %(latex(f)
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
                loigiai=('Tập xác định: $\\mathscr{D}=[%s;%s]$.\\\\ \n'
                        '''Ta có $y'=%s.\\\\ \n''' 
                        '''\\hspace*{1.1cm}y'=0 \\Leftrightarrow x=%s$.\\\\ \n'''
                        '''Bảng biến thiên\\\\ \n'''
                        '\\hspace*{1cm} \\begin{tikzpicture}[line join=round,>=stealth] \n'
                            '\\def\\myltespcl{3}\\def\\myltlgt{2}\\def\\myltdeltacl{0.5} \n'
                            '\\def\\myltx{1}\\def\\mylta{0.7}\\def\\myltb{2.1}\\def\\myltc{\\myltb/3} \n'
                            '\\path(\\myltlgt/2,-\\myltx/2) node {$x$}(\\myltlgt/2,-\\myltx-\\mylta/2) node {$y\'$}(\\myltlgt/2,-\\myltx-\\mylta-\\myltb/2) node {$y$}; \n'
                            '\\draw(0,-\\myltx)--(\\myltlgt+4*\\myltespcl+2*\\myltdeltacl,-\\myltx)(0,-\\myltx-\\mylta)--(\\myltlgt+4*\\myltespcl+2*\\myltdeltacl,-\\myltx-\\mylta)(\\myltlgt,0)--(\\myltlgt,-\\myltx-\\mylta-\\myltb);  \n'
                            '\\draw(0,0) rectangle (\\myltlgt+4*\\myltespcl+2*\\myltdeltacl,-\\myltx-\\mylta-\\myltb); \n'
                            '\\path(\\myltlgt+\\myltdeltacl,-\\myltx/2) node {$-\\infty$}; \n'
                            '\\fill[pattern=north west lines](\\myltlgt,-\\myltx) rectangle (\\myltlgt+\\myltdeltacl+\\myltespcl,-\\myltx-\\mylta); \n'
                            '\\path(\\myltlgt+\\myltdeltacl+\\myltespcl,-\\myltx/2) node {$%s$}; \n'
                            '\\draw[double](\\myltlgt+\\myltdeltacl+\\myltespcl,-\\myltx)--(\\myltlgt+\\myltdeltacl+\\myltespcl,-\\myltx-\\mylta); \n'
                            '\\path(\\myltlgt+\\myltdeltacl+1.5*\\myltespcl,-\\myltx-\\mylta/2) node {$+$}; \n'
                            '\\path(\\myltlgt+\\myltdeltacl+2*\\myltespcl,-\\myltx/2) node {$%s$}; \n'
                            '\\path(\\myltlgt+\\myltdeltacl+2.5*\\myltespcl,-\\myltx-\\mylta/2) node {$-$}; \n'
                            '\\path(\\myltlgt+\\myltdeltacl+3*\\myltespcl,-\\myltx/2) node {$%s$}; \n'
                            '\\draw[double](\\myltlgt+\\myltdeltacl+3*\\myltespcl,-\\myltx)--(\\myltlgt+\\myltdeltacl+3*\\myltespcl,-\\myltx-\\mylta); \n'
                            '\\fill[pattern=north west lines](\\myltlgt+\\myltdeltacl+3*\\myltespcl,-\\myltx) rectangle (\\myltlgt+2*\\myltdeltacl+4*\\myltespcl,-\\myltx-\\mylta); \n'
                            '\\path(\\myltlgt+\\myltdeltacl+4*\\myltespcl,-\\myltx/2) node {$+\\infty$}; \n'
                            '\\path(\\myltlgt+\\myltdeltacl+2*\\myltespcl,-\\myltx-\\mylta/2) node {$0$}; \n'
                            '\\fill[pattern=north west lines](\\myltlgt,-\\myltx-\\mylta) rectangle (\\myltlgt+\\myltdeltacl+\\myltespcl,-\\myltx-\\mylta-\\myltb); \n'
                            '\\fill[pattern=north west lines](\\myltlgt+\\myltdeltacl+3*\\myltespcl,-\\myltx-\\mylta) rectangle (\\myltlgt+2*\\myltdeltacl+4*\\myltespcl,-\\myltx-\\mylta-\\myltb); \n'
                            '\\node (nmyltb) at (\\myltlgt+\\myltdeltacl+\\myltespcl,-\\myltx-\\mylta-2.5*\\myltc) {$%s$}; \n'
                            '\\node (nmyltc) at (\\myltlgt+\\myltdeltacl+2*\\myltespcl,-\\myltx-\\mylta-0.5*\\myltc) {$%s$}; \n'
                            '\\node (nmyltd) at (\\myltlgt+\\myltdeltacl+3*\\myltespcl,-\\myltx-\\mylta-2.5*\\myltc) {$%s$}; \n'
                            '\\draw[->] (nmyltb)--(nmyltc);'
                            '\\draw[->] (nmyltc)--(nmyltd);'
                        '\\end{tikzpicture} \\\\ \n'
                        'Từ bảng biến thiên ta có \\\\ \n'
                        '''\\hspace*{1cm} Hàm số có giá trị lớn nhất là $%s$. \\\\ \n'''
                        '''\\hspace*{1cm} Hàm số có giá trị nhỏ nhất là $%s$.'''
                        %(latex(-x1),latex(x2),
                        latex(daoham),
                        latex(x0),
                        latex(x1),latex(x0),latex(x2),
                        latex(f1),latex(f0),latex(f2),
                        latex(gtln),
                        latex(gtnn)
                        ))
            if dang=='3':
                # Khai báo biến
                x=symbols('x')
                x1=randint(-9,9)
                x2=randint(-9,9)
                while x2<=x1:
                    x1=randint(-9,9)
                    x2=randint(-9,9)
                f=sqrt(-x**2+(x1+x2)*x-x1*x2)
                daoham=(-2*x+x1+x2)/(2*sqrt(-x**2+(x1+x2)*x-x1*x2))
                x0=Rational(x1+x2,2)
                f1=sqrt(-x1**2+(x1+x2)*x1-x1*x2)
                f2=sqrt(-x2**2+(x1+x2)*x2-x1*x2)
                f0=sqrt(-x0**2+(x1+x2)*x0-x1*x2)
                gtln=f0
                gtnn=f1

                du = ['$x=%s$'%(latex(x0)),
                    ]
                da= random.choice(du)
                s = ['$x=%s$'%(latex(gtnn)),
                    '$x=%s$'%(latex(-gtln)),
                    '$x=%s$'%(latex(gtln)),
                    '$x=%s$'%(latex(x1)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('''Cho hàm số $y=%s$. Hàm số đạt giá trị lớn nhất tại điểm'''
                                %(latex(f)
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
                loigiai=('Tập xác định: $\\mathscr{D}=[%s;%s]$.\\\\ \n'
                        '''Ta có $y'=%s.\\\\ \n''' 
                        '''\\hspace*{1.1cm}y'=0 \\Leftrightarrow x=%s$.\\\\ \n'''
                        '''Bảng biến thiên\\\\ \n'''
                        '\\hspace*{1cm} \\begin{tikzpicture}[line join=round,>=stealth] \n'
                            '\\def\\myltespcl{3}\\def\\myltlgt{2}\\def\\myltdeltacl{0.5} \n'
                            '\\def\\myltx{1}\\def\\mylta{0.7}\\def\\myltb{2.1}\\def\\myltc{\\myltb/3} \n'
                            '\\path(\\myltlgt/2,-\\myltx/2) node {$x$}(\\myltlgt/2,-\\myltx-\\mylta/2) node {$y\'$}(\\myltlgt/2,-\\myltx-\\mylta-\\myltb/2) node {$y$}; \n'
                            '\\draw(0,-\\myltx)--(\\myltlgt+4*\\myltespcl+2*\\myltdeltacl,-\\myltx)(0,-\\myltx-\\mylta)--(\\myltlgt+4*\\myltespcl+2*\\myltdeltacl,-\\myltx-\\mylta)(\\myltlgt,0)--(\\myltlgt,-\\myltx-\\mylta-\\myltb);  \n'
                            '\\draw(0,0) rectangle (\\myltlgt+4*\\myltespcl+2*\\myltdeltacl,-\\myltx-\\mylta-\\myltb); \n'
                            '\\path(\\myltlgt+\\myltdeltacl,-\\myltx/2) node {$-\\infty$}; \n'
                            '\\fill[pattern=north west lines](\\myltlgt,-\\myltx) rectangle (\\myltlgt+\\myltdeltacl+\\myltespcl,-\\myltx-\\mylta); \n'
                            '\\path(\\myltlgt+\\myltdeltacl+\\myltespcl,-\\myltx/2) node {$%s$}; \n'
                            '\\draw[double](\\myltlgt+\\myltdeltacl+\\myltespcl,-\\myltx)--(\\myltlgt+\\myltdeltacl+\\myltespcl,-\\myltx-\\mylta); \n'
                            '\\path(\\myltlgt+\\myltdeltacl+1.5*\\myltespcl,-\\myltx-\\mylta/2) node {$+$}; \n'
                            '\\path(\\myltlgt+\\myltdeltacl+2*\\myltespcl,-\\myltx/2) node {$%s$}; \n'
                            '\\path(\\myltlgt+\\myltdeltacl+2.5*\\myltespcl,-\\myltx-\\mylta/2) node {$-$}; \n'
                            '\\path(\\myltlgt+\\myltdeltacl+3*\\myltespcl,-\\myltx/2) node {$%s$}; \n'
                            '\\draw[double](\\myltlgt+\\myltdeltacl+3*\\myltespcl,-\\myltx)--(\\myltlgt+\\myltdeltacl+3*\\myltespcl,-\\myltx-\\mylta); \n'
                            '\\fill[pattern=north west lines](\\myltlgt+\\myltdeltacl+3*\\myltespcl,-\\myltx) rectangle (\\myltlgt+2*\\myltdeltacl+4*\\myltespcl,-\\myltx-\\mylta); \n'
                            '\\path(\\myltlgt+\\myltdeltacl+4*\\myltespcl,-\\myltx/2) node {$+\\infty$}; \n'
                            '\\path(\\myltlgt+\\myltdeltacl+2*\\myltespcl,-\\myltx-\\mylta/2) node {$0$}; \n'
                            '\\fill[pattern=north west lines](\\myltlgt,-\\myltx-\\mylta) rectangle (\\myltlgt+\\myltdeltacl+\\myltespcl,-\\myltx-\\mylta-\\myltb); \n'
                            '\\fill[pattern=north west lines](\\myltlgt+\\myltdeltacl+3*\\myltespcl,-\\myltx-\\mylta) rectangle (\\myltlgt+2*\\myltdeltacl+4*\\myltespcl,-\\myltx-\\mylta-\\myltb); \n'
                            '\\node (nmyltb) at (\\myltlgt+\\myltdeltacl+\\myltespcl,-\\myltx-\\mylta-2.5*\\myltc) {$%s$}; \n'
                            '\\node (nmyltc) at (\\myltlgt+\\myltdeltacl+2*\\myltespcl,-\\myltx-\\mylta-0.5*\\myltc) {$%s$}; \n'
                            '\\node (nmyltd) at (\\myltlgt+\\myltdeltacl+3*\\myltespcl,-\\myltx-\\mylta-2.5*\\myltc) {$%s$}; \n'
                            '\\draw[->] (nmyltb)--(nmyltc);'
                            '\\draw[->] (nmyltc)--(nmyltd);'
                        '\\end{tikzpicture} \\\\ \n'
                        'Từ bảng biến thiên ta có \\\\ \n'
                        '''\\hspace*{1cm} Hàm số có giá trị lớn nhất là $%s$. \\\\ \n'''
                        '''\\hspace*{1cm} Hàm số có giá trị nhỏ nhất là $%s$. '''
                        %(latex(x1),latex(x2),
                        latex(daoham),
                        latex(x0),
                        latex(x1),latex(x0),latex(x2),
                        latex(f1),latex(f0),latex(f2),
                        latex(gtln),
                        latex(gtnn)
                        ))
            if dang=='2':
                # Khai báo biến
                x=symbols('x')
                x1=randint(-9,9)
                x2=randint(-9,9)
                while x2<=x1:
                    x1=randint(-9,9)
                    x2=randint(-9,9)
                f=sqrt(-x**2+(x1+x2)*x-x1*x2)
                daoham=(-2*x+x1+x2)/(2*sqrt(-x**2+(x1+x2)*x-x1*x2))
                x0=Rational(x1+x2,2)
                f1=sqrt(-x1**2+(x1+x2)*x1-x1*x2)
                f2=sqrt(-x2**2+(x1+x2)*x2-x1*x2)
                f0=sqrt(-x0**2+(x1+x2)*x0-x1*x2)
                gtln=f0
                gtnn=f1

                du = ['$%s$'%(latex(gtnn)),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(gtln)),
                    '$%s$'%(latex(x1)),
                    '$%s$'%(latex(x2)),
                    '$%s$'%(latex(x0)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('''Cho hàm số $y=%s$. Giá trị nhỏ nhất của hàm số là'''
                                %(latex(f)
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
                loigiai=('Tập xác định: $\\mathscr{D}=[%s;%s]$.\\\\ \n'
                        '''Ta có $y'=%s.\\\\ \n''' 
                        '''\\hspace*{1.1cm}y'=0 \\Leftrightarrow x=%s$.\\\\ \n'''
                        '''Bảng biến thiên\\\\ \n'''
                        '\\hspace*{1cm} \\begin{tikzpicture}[line join=round,>=stealth] \n'
                            '\\def\\myltespcl{3}\\def\\myltlgt{2}\\def\\myltdeltacl{0.5} \n'
                            '\\def\\myltx{1}\\def\\mylta{0.7}\\def\\myltb{2.1}\\def\\myltc{\\myltb/3} \n'
                            '\\path(\\myltlgt/2,-\\myltx/2) node {$x$}(\\myltlgt/2,-\\myltx-\\mylta/2) node {$y\'$}(\\myltlgt/2,-\\myltx-\\mylta-\\myltb/2) node {$y$}; \n'
                            '\\draw(0,-\\myltx)--(\\myltlgt+4*\\myltespcl+2*\\myltdeltacl,-\\myltx)(0,-\\myltx-\\mylta)--(\\myltlgt+4*\\myltespcl+2*\\myltdeltacl,-\\myltx-\\mylta)(\\myltlgt,0)--(\\myltlgt,-\\myltx-\\mylta-\\myltb);  \n'
                            '\\draw(0,0) rectangle (\\myltlgt+4*\\myltespcl+2*\\myltdeltacl,-\\myltx-\\mylta-\\myltb); \n'
                            '\\path(\\myltlgt+\\myltdeltacl,-\\myltx/2) node {$-\\infty$}; \n'
                            '\\fill[pattern=north west lines](\\myltlgt,-\\myltx) rectangle (\\myltlgt+\\myltdeltacl+\\myltespcl,-\\myltx-\\mylta); \n'
                            '\\path(\\myltlgt+\\myltdeltacl+\\myltespcl,-\\myltx/2) node {$%s$}; \n'
                            '\\draw[double](\\myltlgt+\\myltdeltacl+\\myltespcl,-\\myltx)--(\\myltlgt+\\myltdeltacl+\\myltespcl,-\\myltx-\\mylta); \n'
                            '\\path(\\myltlgt+\\myltdeltacl+1.5*\\myltespcl,-\\myltx-\\mylta/2) node {$+$}; \n'
                            '\\path(\\myltlgt+\\myltdeltacl+2*\\myltespcl,-\\myltx/2) node {$%s$}; \n'
                            '\\path(\\myltlgt+\\myltdeltacl+2.5*\\myltespcl,-\\myltx-\\mylta/2) node {$-$}; \n'
                            '\\path(\\myltlgt+\\myltdeltacl+3*\\myltespcl,-\\myltx/2) node {$%s$}; \n'
                            '\\draw[double](\\myltlgt+\\myltdeltacl+3*\\myltespcl,-\\myltx)--(\\myltlgt+\\myltdeltacl+3*\\myltespcl,-\\myltx-\\mylta); \n'
                            '\\fill[pattern=north west lines](\\myltlgt+\\myltdeltacl+3*\\myltespcl,-\\myltx) rectangle (\\myltlgt+2*\\myltdeltacl+4*\\myltespcl,-\\myltx-\\mylta); \n'
                            '\\path(\\myltlgt+\\myltdeltacl+4*\\myltespcl,-\\myltx/2) node {$+\\infty$}; \n'
                            '\\path(\\myltlgt+\\myltdeltacl+2*\\myltespcl,-\\myltx-\\mylta/2) node {$0$}; \n'
                            '\\fill[pattern=north west lines](\\myltlgt,-\\myltx-\\mylta) rectangle (\\myltlgt+\\myltdeltacl+\\myltespcl,-\\myltx-\\mylta-\\myltb); \n'
                            '\\fill[pattern=north west lines](\\myltlgt+\\myltdeltacl+3*\\myltespcl,-\\myltx-\\mylta) rectangle (\\myltlgt+2*\\myltdeltacl+4*\\myltespcl,-\\myltx-\\mylta-\\myltb); \n'
                            '\\node (nmyltb) at (\\myltlgt+\\myltdeltacl+\\myltespcl,-\\myltx-\\mylta-2.5*\\myltc) {$%s$}; \n'
                            '\\node (nmyltc) at (\\myltlgt+\\myltdeltacl+2*\\myltespcl,-\\myltx-\\mylta-0.5*\\myltc) {$%s$}; \n'
                            '\\node (nmyltd) at (\\myltlgt+\\myltdeltacl+3*\\myltespcl,-\\myltx-\\mylta-2.5*\\myltc) {$%s$}; \n'
                            '\\draw[->] (nmyltb)--(nmyltc);'
                            '\\draw[->] (nmyltc)--(nmyltd);'
                        '\\end{tikzpicture} \\\\ \n'
                        'Từ bảng biến thiên ta có \\\\ \n'
                        '''\\hspace*{1cm} Hàm số có giá trị lớn nhất là $%s$. \\\\ \n'''
                        '''\\hspace*{1cm} Hàm số có giá trị nhỏ nhất là $%s$. '''
                        %(latex(x1),latex(x2),
                        latex(daoham),
                        latex(x0),
                        latex(x1),latex(x0),latex(x2),
                        latex(f1),latex(f0),latex(f2),
                        latex(gtln),
                        latex(gtnn)
                        ))
            if dang=='1':
                # Khai báo biến
                x=symbols('x')
                x1=randint(-9,9)
                x2=randint(-9,9)
                while x2<=x1:
                    x1=randint(-9,9)
                    x2=randint(-9,9)
                f=sqrt(-x**2+(x1+x2)*x-x1*x2)
                daoham=(-2*x+x1+x2)/(2*sqrt(-x**2+(x1+x2)*x-x1*x2))
                x0=Rational(x1+x2,2)
                f1=sqrt(-x1**2+(x1+x2)*x1-x1*x2)
                f2=sqrt(-x2**2+(x1+x2)*x2-x1*x2)
                f0=sqrt(-x0**2+(x1+x2)*x0-x1*x2)
                gtln=f0
                gtnn=f1

                du = ['$%s$'%(latex(gtln)),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(gtnn)),
                    '$%s$'%(latex(-gtln)),
                    '$%s$'%(latex(x0)),
                    '$%s$'%(latex(x1)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('''Cho hàm số $y=%s$. Giá trị lớn nhất của hàm số là'''
                                %(latex(f)
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
                loigiai=('Tập xác định: $\\mathscr{D}=[%s;%s]$.\\\\ \n'
                        '''Ta có $y'=%s.\\\\ \n''' 
                        '''\\hspace*{1.1cm}y'=0 \\Leftrightarrow x=%s$.\\\\ \n'''
                        '''Bảng biến thiên\\\\ \n'''
                        '\\hspace*{1cm} \\begin{tikzpicture}[line join=round,>=stealth] \n'
                            '\\def\\myltespcl{3}\\def\\myltlgt{2}\\def\\myltdeltacl{0.5} \n'
                            '\\def\\myltx{1}\\def\\mylta{0.7}\\def\\myltb{2.1}\\def\\myltc{\\myltb/3} \n'
                            '\\path(\\myltlgt/2,-\\myltx/2) node {$x$}(\\myltlgt/2,-\\myltx-\\mylta/2) node {$y\'$}(\\myltlgt/2,-\\myltx-\\mylta-\\myltb/2) node {$y$}; \n'
                            '\\draw(0,-\\myltx)--(\\myltlgt+4*\\myltespcl+2*\\myltdeltacl,-\\myltx)(0,-\\myltx-\\mylta)--(\\myltlgt+4*\\myltespcl+2*\\myltdeltacl,-\\myltx-\\mylta)(\\myltlgt,0)--(\\myltlgt,-\\myltx-\\mylta-\\myltb);  \n'
                            '\\draw(0,0) rectangle (\\myltlgt+4*\\myltespcl+2*\\myltdeltacl,-\\myltx-\\mylta-\\myltb); \n'
                            '\\path(\\myltlgt+\\myltdeltacl,-\\myltx/2) node {$-\\infty$}; \n'
                            '\\fill[pattern=north west lines](\\myltlgt,-\\myltx) rectangle (\\myltlgt+\\myltdeltacl+\\myltespcl,-\\myltx-\\mylta); \n'
                            '\\path(\\myltlgt+\\myltdeltacl+\\myltespcl,-\\myltx/2) node {$%s$}; \n'
                            '\\draw[double](\\myltlgt+\\myltdeltacl+\\myltespcl,-\\myltx)--(\\myltlgt+\\myltdeltacl+\\myltespcl,-\\myltx-\\mylta); \n'
                            '\\path(\\myltlgt+\\myltdeltacl+1.5*\\myltespcl,-\\myltx-\\mylta/2) node {$+$}; \n'
                            '\\path(\\myltlgt+\\myltdeltacl+2*\\myltespcl,-\\myltx/2) node {$%s$}; \n'
                            '\\path(\\myltlgt+\\myltdeltacl+2.5*\\myltespcl,-\\myltx-\\mylta/2) node {$-$}; \n'
                            '\\path(\\myltlgt+\\myltdeltacl+3*\\myltespcl,-\\myltx/2) node {$%s$}; \n'
                            '\\draw[double](\\myltlgt+\\myltdeltacl+3*\\myltespcl,-\\myltx)--(\\myltlgt+\\myltdeltacl+3*\\myltespcl,-\\myltx-\\mylta); \n'
                            '\\fill[pattern=north west lines](\\myltlgt+\\myltdeltacl+3*\\myltespcl,-\\myltx) rectangle (\\myltlgt+2*\\myltdeltacl+4*\\myltespcl,-\\myltx-\\mylta); \n'
                            '\\path(\\myltlgt+\\myltdeltacl+4*\\myltespcl,-\\myltx/2) node {$+\\infty$}; \n'
                            '\\path(\\myltlgt+\\myltdeltacl+2*\\myltespcl,-\\myltx-\\mylta/2) node {$0$}; \n'
                            '\\fill[pattern=north west lines](\\myltlgt,-\\myltx-\\mylta) rectangle (\\myltlgt+\\myltdeltacl+\\myltespcl,-\\myltx-\\mylta-\\myltb); \n'
                            '\\fill[pattern=north west lines](\\myltlgt+\\myltdeltacl+3*\\myltespcl,-\\myltx-\\mylta) rectangle (\\myltlgt+2*\\myltdeltacl+4*\\myltespcl,-\\myltx-\\mylta-\\myltb); \n'
                            '\\node (nmyltb) at (\\myltlgt+\\myltdeltacl+\\myltespcl,-\\myltx-\\mylta-2.5*\\myltc) {$%s$}; \n'
                            '\\node (nmyltc) at (\\myltlgt+\\myltdeltacl+2*\\myltespcl,-\\myltx-\\mylta-0.5*\\myltc) {$%s$}; \n'
                            '\\node (nmyltd) at (\\myltlgt+\\myltdeltacl+3*\\myltespcl,-\\myltx-\\mylta-2.5*\\myltc) {$%s$}; \n'
                            '\\draw[->] (nmyltb)--(nmyltc);'
                            '\\draw[->] (nmyltc)--(nmyltd);'
                        '\\end{tikzpicture} \\\\ \n'
                        'Từ bảng biến thiên ta có \\\\ \n'
                        '''\\hspace*{1cm} Hàm số có giá trị lớn nhất là $%s$. \\\\ \n'''
                        '''\\hspace*{1cm} Hàm số có giá trị nhỏ nhất là $%s$. '''
                        %(latex(x1),latex(x2),
                        latex(daoham),
                        latex(x0),
                        latex(x1),latex(x0),latex(x2),
                        latex(f1),latex(f0),latex(f2),
                        latex(gtln),
                        latex(gtnn)
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-').replace('1x', 'x').replace('+0x^2', '').replace('+0x', '').replace('+0', '')
            return content


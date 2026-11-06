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


def bt_dang1_p1_b3_c1_ds11(self):
            # Khai báo biến
            lisdang=['1','2']
            dang=random.choice(lisdang)

            if dang=='2':
                x=symbols('x')
                k=symbols('k')
                m=randint(1,9)
                n=randint(1,9)
                p=randint(-9,9)
                q=randint(-9,9)
                while m==0 or n==0 or q==0:
                    m=randint(1,9)
                    n=randint(1,9)
                    p=randint(-9,9)
                    q=randint(-9,9)
                a=Rational(m,n)
                b=Rational(p,q)
                f=a*x+b*pi
                ff=m*sin(q*x+pi/m)+n

                d = [
                    '$\\mathscr{D}=\\mathbb{R} \\setminus \\left\\lbrace %s+k%s \\, | \\, k \\in \\mathbb{Z} \\right\\rbrace $'%(latex((pi/2-b*pi)/a),latex(pi/a)),
                    ]
                da= random.choice(d)
                s = [
                    '$\\mathscr{D}=\\mathbb{R} \\setminus \\left\\lbrace %s+k%s \\, | \\, k \\in \\mathbb{Z} \\right\\rbrace $'%(latex((pi/2+b*pi+pi/11)/a),latex(pi/a)),
                    '$\\mathscr{D}=\\mathbb{R} \\setminus \\left\\lbrace %s+k%s \\, | \\, k \\in \\mathbb{Z} \\right\\rbrace $'%(latex((pi-b*pi+pi/5)/a),latex(pi/a)),
                    '$\\mathscr{D}=\\mathbb{R} \\setminus \\left\\lbrace %s+k%s \\, | \\, k \\in \\mathbb{Z} \\right\\rbrace $'%(latex((-pi/2-b*pi+pi/7)/a),latex(pi/a)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Tập xác định của hàm số $y=\\dfrac{%s}{\\cos \\left( %s \\right)} $ là \n'
                                %(latex(ff),latex(f))
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
                loigiai=(
                        'Điều kiện xác định của hàm số là \\\\ \n'
                        '\\hspace*{1cm} $\\cos \\left( %s \\right) \\ne 0 \\Leftrightarrow %s \\ne \\dfrac{\\pi}{2}+k\\pi \\\\ \n'
                        '\\hspace*{4.6cm} \\Leftrightarrow %s \\ne \\dfrac{\\pi}{2}-%s+k\\pi \\\\ \n'
                        '\\hspace*{4.6cm} \\Leftrightarrow %s \\ne %s+k\\pi \\\\ \n'
                        '\\hspace*{4.6cm} \\Leftrightarrow x \\ne %s+k%s$  $(k \\in \\mathbb{Z})$.\\\\ \n'
                        'Vậy tập xác định của hàm số là \\\\ \n'
                        '\\hspace*{1cm} $\\mathscr{D}=\\mathbb{R} \\setminus \\left\\lbrace %s+k%s \\, | \\, k \\in \\mathbb{Z} \\right\\rbrace $. \\\\ \n'


                        %(latex(f),latex(f),latex(a*x),latex(b*pi),latex(a*x),latex(pi/2-b*pi),latex((pi/2-b*pi)/a),latex(pi/a),
                        latex((pi/2-b*pi)/a),latex(pi/a),

                        ))

            if dang=='1':
                x=symbols('x')
                k=symbols('k')
                m=randint(1,9)
                n=randint(1,9)
                p=randint(-9,9)
                q=randint(-9,9)
                while m==0 or n==0 or q==0:
                    m=randint(1,9)
                    n=randint(1,9)
                    p=randint(-9,9)
                    q=randint(-9,9)
                a=Rational(m,n)
                b=Rational(p,q)
                f=a*x+b*pi

                d = [
                    '$\\mathscr{D}=\\mathbb{R} \\setminus \\left\\lbrace %s+k%s \\, | \\, k \\in \\mathbb{Z} \\right\\rbrace $'%(latex((pi/2-b*pi)/a),latex(pi/a)),
                    ]
                da= random.choice(d)
                s = [
                    '$\\mathscr{D}=\\mathbb{R} \\setminus \\left\\lbrace %s+k%s \\, | \\, k \\in \\mathbb{Z} \\right\\rbrace $'%(latex((pi/3-b*pi+pi/5)/a),latex(pi/a)),
                    '$\\mathscr{D}=\\mathbb{R} \\setminus \\left\\lbrace %s+k%s \\, | \\, k \\in \\mathbb{Z} \\right\\rbrace $'%(latex((pi/5-b*pi+pi/7)/a),latex(pi/a)),
                    '$\\mathscr{D}=\\mathbb{R} \\setminus \\left\\lbrace %s+k%s \\, | \\, k \\in \\mathbb{Z} \\right\\rbrace $'%(latex((pi/7-b*pi+pi/11)/a),latex(pi/a)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Tập xác định của hàm số $y=\\tan \\left( %s \\right)$ là \n'
                                %(latex(f))
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
                loigiai=(
                        'Điều kiện xác định của hàm số là \\\\ \n'
                        '\\hspace*{1cm} $%s \\ne \\dfrac{\\pi}{2}+k\\pi \\Leftrightarrow %s \\ne \\dfrac{\\pi}{2}-%s+k\\pi \\\\ \n'
                        '\\hspace*{4.5cm} \\Leftrightarrow %s \\ne %s+k\\pi \\\\ \n'
                        '\\hspace*{4.5cm} \\Leftrightarrow x \\ne %s+k%s$ $(k \\in \\mathbb{Z})$.\\\\ \n'
                        'Vậy tập xác định của hàm số là \\\\ \n'
                        '\\hspace*{1cm} $\\mathscr{D}=\\mathbb{R} \\setminus \\left\\lbrace %s+k%s \\, | \\, k \\in \\mathbb{Z} \\right\\rbrace $. \\\\ \n'


                        %(latex(f),latex(a*x),latex(b*pi),latex(a*x),latex(pi/2-b*pi),latex((pi/2-b*pi)/a),latex(pi/a),
                        latex((pi/2-b*pi)/a),latex(pi/a),

                        ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n '+ str(noidungcauhoi)+ 
                '\\choice[2] \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('--', '+').replace('+-', '-').replace('0+', '').replace('0-', '-')
            return content


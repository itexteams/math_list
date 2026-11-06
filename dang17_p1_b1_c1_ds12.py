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


def bt_dang17_p1_b1_c1_ds12(self):
            # Khai báo biến
            x = symbols('x')
            x1=randint(-9,9)
            i1=randint(1,5)
            x2=x1+i1
            a1=1
            b1=-x1-x2
            c1=x1*x2
            f1=sqrt(a1*x**2+b1*x+c1)
            daoham1=(2*a1*x+b1)/(2*sqrt(a1*x**2+b1*x+c1))
            tu1=2*a1*x+b1

            f2=sqrt(-a1*x**2-b1*x-c1)
            daoham2=(-2*a1*x-b1)/(2*sqrt(-a1*x**2-b1*x-c1))
            tu2=-2*a1*x-b1

            a2=1
            b2=-2*x1
            c2=x1**2+1
            f3=sqrt(a2*x**2+b2*x+c2)
            daoham3=(2*a2*x+b2)/(2*sqrt(a2*x**2+b2*x+c2))
            tu3=2*a2*x+b2

            a=randint(2,9)
            b=randint(2,9)
            c=randint(2,9)
            d=randint(2,9)
            while a/b==c/d:
                a=randint(2,9)
                b=randint(2,9)
                c=randint(2,9)
                d=randint(2,9)
            x3=-Rational(b,a)
            x4=Rational(c,d)
            f4=sqrt(a*x+b)+sqrt(c-d*x)
            daoham4=a/(2*sqrt(a*x+b))-d/(2*sqrt(c-d*x))
            x0=Rational(c*a**2-b*d**2,a*d**2+d*a**2)

            lisdang=['1','2','3','4','5','6','7','8']
            dang=random.choice(lisdang)
            if dang=='8':
                d = ['$\\left(%s;%s\\right)$'%(latex(x0),latex(x4)),
                    ]
                da= random.choice(d)
                s = ['$\\left(%s;+\\infty\\right)$'%(latex(x3)), 
                    '$\\left(-\\infty;%s\\right)$'%(latex(x4)),
                    '$\\left(%s;%s\\right)$'%(latex(x3),latex(x4)),
                    '$\\left(%s;%s\\right)$'%(latex(x3),latex(x0)), #
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=%s$. Hàm số nghịch biến trên khoảng nào dưới đây?  \n'
                                %(latex(f4)
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
                loigiai=('Tập xác định: $\\mathscr{D}=\\left[%s;%s \\right]$.\\\\ \n'
                        'Ta có $y\'=%s$.\\\\ \n'
                        '\\hspace*{1cm} $y\'=0 \\Leftrightarrow %s=0 \\Leftrightarrow x=%s$. \\\\ \n'
                        '\\hspace*{1cm} $y\'$ không xác định khi $x \\in \\left(-\\infty;%s \\right] \\cup \\left[%s;+\\infty \\right)$. \\\\ \n'
                        'Bảng xét dấu \\\\ \n'
                        '\\hspace*{1cm} \\begin{tikzpicture}   \n'
                        '\\tkzTabInit[deltacl=0.5,espcl=2.5,lgt=2]  \n'
                        '{$x$/1,$y\'$/1}  \n'
                        '{$-\\infty$,$%s$,$%s$,$%s$,$+\\infty$}  \n'
                        '\\tkzTabLine{,h,d,+,0,-,d,h,}  \n'
                        '\\end{tikzpicture}  \\\\ \n'
                        'Từ bảng xét dấu ta thấy \\\\ \n'
                        '\\hspace*{1cm} Hàm số đồng biến trên khoảng $\\left(%s;%s\\right)$. \\\\ \n'
                        '\\hspace*{1cm} Hàm số nghịch biến trên khoảng $\\left(%s;%s\\right)$. \\\\ \n'
                        %(latex(x3),latex(x4),
                        latex(daoham4),
                        latex(daoham4),latex(x0),
                        latex(x3),latex(x4),
                        latex(x3),latex(x0),latex(x4),
                        latex(x3),latex(x0),
                        latex(x0),latex(x4),
                            )
                        )
            if dang=='7':
                d = ['$\\left(%s;%s\\right)$'%(latex(x3),latex(x0)), #
                    ]
                da= random.choice(d)
                s = [
                    '$\\left(%s;%s\\right)$'%(latex(x0),latex(x4)),
                    '$\\left(%s;+\\infty\\right)$'%(latex(x3)), 
                    '$\\left(-\\infty;%s\\right)$'%(latex(x4)),
                    '$\\left(%s;%s\\right)$'%(latex(x3),latex(x4)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=%s$. Hàm số đồng biến trên khoảng nào dưới đây?  \n'
                                %(latex(f4)
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
                loigiai=('Tập xác định: $\\mathscr{D}=\\left[%s;%s \\right]$.\\\\ \n'
                        'Ta có $y\'=%s$.\\\\ \n'
                        '\\hspace*{1cm} $y\'=0 \\Leftrightarrow %s=0 \\Leftrightarrow x=%s$. \\\\ \n'
                        '\\hspace*{1cm} $y\'$ không xác định khi $x \\in \\left(-\\infty;%s \\right] \\cup \\left[%s;+\\infty \\right)$. \\\\ \n'
                        'Bảng xét dấu \\\\ \n'
                        '\\hspace*{1cm} \\begin{tikzpicture}   \n'
                        '\\tkzTabInit[deltacl=0.5,espcl=2.5,lgt=2]  \n'
                        '{$x$/1,$y\'$/1}  \n'
                        '{$-\\infty$,$%s$,$%s$,$%s$,$+\\infty$}  \n'
                        '\\tkzTabLine{,h,d,+,0,-,d,h,}  \n'
                        '\\end{tikzpicture}  \\\\ \n'
                        'Từ bảng xét dấu ta thấy \\\\ \n'
                        '\\hspace*{1cm} Hàm số đồng biến trên khoảng $\\left(%s;%s\\right)$. \\\\ \n'
                        '\\hspace*{1cm} Hàm số nghịch biến trên khoảng $\\left(%s;%s\\right)$. \\\\ \n'
                        %(latex(x3),latex(x4),
                        latex(daoham4),
                        latex(daoham4),latex(x0),
                        latex(x3),latex(x4),
                        latex(x3),latex(x0),latex(x4),
                        latex(x3),latex(x0),
                        latex(x0),latex(x4),
                            )
                        )
            if dang=='6':
                d = ['$\\left(-\\infty;%s\\right)$'%(latex(Rational(-b2,2*a2))), #
                    '$\\left(-\\infty;%s\\right)$'%(latex(Rational(-b2,2*a2)-1)), #
                    ]
                da= random.choice(d)
                s = [ 
                    '$\\mathbb{R}$',
                    '$\\left(%s;%s\\right)$'%(latex(Rational(-b2,2*a2)-2),latex(Rational(-b2,2*a2)+2)),
                    '$\\left(%s;+\\infty\\right)$'%(latex(Rational(-b2,2*a2))), #
                    '$\\left(%s;+\\infty\\right)$'%(latex(Rational(-b2,2*a2)+1)), #
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=%s$. Hàm số nghịch biến trên khoảng nào dưới đây?  \n'
                                %(latex(f3)
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
                loigiai=('Tập xác định: $\\mathscr{D}=\\mathbb{R}$.\\\\ \n'
                        'Ta có $y\'=%s$.\\\\ \n'
                        '\\hspace*{1cm} $y\'=0 \\Leftrightarrow %s=0 \\Leftrightarrow x=%s$. \\\\ \n'
                        'Bảng xét dấu \\\\ \n'
                        '\\hspace*{1cm} \\begin{tikzpicture}  \n'
                        '\\tkzTabInit[deltacl=0.5,espcl=2.5,lgt=2] \n'
                        '{$x$/1,$y\'$/1} \n'
                        '{$-\\infty$,$%s$,$+\\infty$} \n'
                        '\\tkzTabLine{,-,0,+,} \n'
                        '\\end{tikzpicture} \\\\ \n'
                        'Từ bảng xét dấu ta thấy \\\\ \n'
                        '\\hspace*{1cm} Hàm số đồng biến trên khoảng $\\left(%s;+\\infty\\right)$. \\\\ \n'
                        '\\hspace*{1cm} Hàm số nghịch biến trên khoảng $\\left(-\\infty;%s\\right)$. \\\\ \n'
                        %(
                        latex(daoham3),
                        latex(daoham3),latex(Rational(-b2,2*a2)),
                        latex(Rational(-b2,2*a2)),
                        latex(Rational(-b2,2*a2)),latex(Rational(-b2,2*a2)),
                            )
                        )
            if dang=='5':
                d = ['$\\left(%s;+\\infty\\right)$'%(latex(Rational(-b2,2*a2))), #
                    '$\\left(%s;+\\infty\\right)$'%(latex(Rational(-b2,2*a2)+1)), #
                    ]
                da= random.choice(d)
                s = [ 

                    '$\\left(-\\infty;%s\\right)$'%(latex(Rational(-b2,2*a2))), #
                    '$\\left(-\\infty;%s\\right)$'%(latex(Rational(-b2,2*a2)-1)), #
                    '$\\mathbb{R}$',
                    '$\\left(%s;%s\\right)$'%(latex(Rational(-b2,2*a2)-2),latex(Rational(-b2,2*a2)+2)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=%s$. Hàm số đồng biến trên khoảng nào dưới đây?  \n'
                                %(latex(f3)
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
                loigiai=('Tập xác định: $\\mathscr{D}=\\mathbb{R}$.\\\\ \n'
                        'Ta có $y\'=%s$.\\\\ \n'
                        '\\hspace*{1cm} $y\'=0 \\Leftrightarrow %s=0 \\Leftrightarrow x=%s$. \\\\ \n'
                        'Bảng xét dấu \\\\ \n'
                        '\\hspace*{1cm} \\begin{tikzpicture}  \n'
                        '\\tkzTabInit[deltacl=0.5,espcl=2.5,lgt=2] \n'
                        '{$x$/1,$y\'$/1} \n'
                        '{$-\\infty$,$%s$,$+\\infty$} \n'
                        '\\tkzTabLine{,-,0,+,} \n'
                        '\\end{tikzpicture} \\\\ \n'
                        'Từ bảng xét dấu ta thấy \\\\ \n'
                        '\\hspace*{1cm} Hàm số đồng biến trên khoảng $\\left(%s;+\\infty\\right)$. \\\\ \n'
                        '\\hspace*{1cm} Hàm số nghịch biến trên khoảng $\\left(-\\infty;%s\\right)$. \\\\ \n'
                        %(
                        latex(daoham3),
                        latex(daoham3),latex(Rational(-b2,2*a2)),
                        latex(Rational(-b2,2*a2)),
                        latex(Rational(-b2,2*a2)),latex(Rational(-b2,2*a2)),
                            )
                        )
            if dang=='4':
                d = ['$\\left(%s;%s\\right)$'%(latex(Rational(-b1,2*a1)),latex(x2)), #
                    ]
                da= random.choice(d)
                s = [ 

                    '$\\left(%s;%s\\right)$'%(latex(x1),latex(x2)),
                    '$(%s;+\\infty)$'%(latex(x1)), 
                    '$(-\\infty;%s)$'%(latex(x2)),
                    '$\\left(%s;%s\\right)$'%(latex(x1),latex(Rational(-b1,2*a1))),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=%s$. Hàm số nghịch biến trên khoảng nào dưới đây?  \n'
                                %(latex(f2)
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
                        'Ta có $y\'=%s$.\\\\ \n'
                        '\\hspace*{1cm} $y\'=0 \\Leftrightarrow %s=0 \\Leftrightarrow x=%s$. \\\\ \n'
                        '\\hspace*{1cm} $y\'$ không xác định khi $x \\in (-\\infty;%s] \\cup [%s;+\\infty)$. \\\\ \n'
                        'Bảng xét dấu \\\\ \n'
                        '\\hspace*{1cm} \\begin{tikzpicture}   \n'
                        '\\tkzTabInit[deltacl=0.5,espcl=2.5,lgt=2]  \n'
                        '{$x$/1,$y\'$/1}  \n'
                        '{$-\\infty$,$%s$,$%s$,$%s$,$+\\infty$}  \n'
                        '\\tkzTabLine{,h,d,+,0,-,d,h,}  \n'
                        '\\end{tikzpicture}  \\\\ \n'
                        'Từ bảng xét dấu ta thấy \\\\ \n'
                        '\\hspace*{1cm} Hàm số đồng biến trên khoảng $\\left(%s;%s\\right)$. \\\\ \n'
                        '\\hspace*{1cm} Hàm số nghịch biến trên khoảng $\\left(%s;%s\\right)$. \\\\ \n'
                        %(latex(x1),latex(x2),
                        latex(daoham2),
                        latex(daoham2),latex(Rational(-b1,2*a1)),
                        latex(x1),latex(x2),
                        latex(x1),latex(Rational(-b1,2*a1)),latex(x2),
                        latex(x1),latex(Rational(-b1,2*a1)),latex(Rational(-b1,2*a1)),latex(x2),
                            )
                        )
            if dang=='3':
                d = ['$\\left(%s;%s\\right)$'%(latex(x1),latex(Rational(-b1,2*a1))),
                    ]
                da= random.choice(d)
                s = [ 
                    '$\\left(%s;%s\\right)$'%(latex(Rational(-b1,2*a1)),latex(x2)), #
                    '$\\left(%s;%s\\right)$'%(latex(x1),latex(x2)),
                    '$(%s;+\\infty)$'%(latex(x1)), 
                    '$(-\\infty;%s)$'%(latex(x2)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=%s$. Hàm số đồng biến trên khoảng nào dưới đây?  \n'
                                %(latex(f2)
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
                        'Ta có $y\'=%s$.\\\\ \n'
                        '\\hspace*{1cm} $y\'=0 \\Leftrightarrow %s=0 \\Leftrightarrow x=%s$. \\\\ \n'
                        '\\hspace*{1cm} $y\'$ không xác định khi $x \\in (-\\infty;%s] \\cup [%s;+\\infty)$. \\\\ \n'
                        'Bảng xét dấu \\\\ \n'
                        '\\hspace*{1cm} \\begin{tikzpicture}   \n'
                        '\\tkzTabInit[deltacl=0.5,espcl=2.5,lgt=2]  \n'
                        '{$x$/1,$y\'$/1}  \n'
                        '{$-\\infty$,$%s$,$%s$,$%s$,$+\\infty$}  \n'
                        '\\tkzTabLine{,h,d,+,0,-,d,h,}  \n'
                        '\\end{tikzpicture}  \\\\ \n'
                        'Từ bảng xét dấu ta thấy \\\\ \n'
                        '\\hspace*{1cm} Hàm số đồng biến trên khoảng $\\left(%s;%s\\right)$. \\\\ \n'
                        '\\hspace*{1cm} Hàm số nghịch biến trên khoảng $\\left(%s;%s\\right)$. \\\\ \n'
                        %(latex(x1),latex(x2),
                        latex(daoham2),
                        latex(daoham2),latex(Rational(-b1,2*a1)),
                        latex(x1),latex(x2),
                        latex(x1),latex(Rational(-b1,2*a1)),latex(x2),
                        latex(x1),latex(Rational(-b1,2*a1)),latex(Rational(-b1,2*a1)),latex(x2),
                            )
                        )
            if dang=='2':
                d = ['$(-\\infty;%s)$'%(latex(x1)), #
                '$(-\\infty;%s)$'%(latex(x1-1)), #
                '$(%s;%s)$'%(latex(x1-5),latex(x1-1)), #
                    ]
                da= random.choice(d)
                s = [ 

                    '$(%s;%s)$'%(latex(x1),latex(x2)),
                    '$(%s;+\\infty)$'%(latex(x2)),
                    '$(%s;+\\infty)$'%(latex(x2+1)),
                    '$(%s;%s)$'%(latex(x2+1),latex(x2+3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=%s$. Hàm số nghịch biến trên khoảng nào dưới đây?  \n'
                                %(latex(f1)
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
                loigiai=('Tập xác định: $\\mathscr{D}=(-\\infty;%s] \\cup [%s;+\\infty)$.\\\\ \n'
                        'Ta có $y\'=%s$.\\\\ \n'
                        'Dấu của $y\'$ phụ thuộc vào dấu của biểu thức $%s$. \\\\ \n'
                        '\\hspace*{1cm} $%s=0 \\Leftrightarrow x=%s$. \\\\ \n'
                        '$y\'$ không xác định trên đoạn $[%s;%s]$. \\\\ \n'
                        'Bảng xét dấu \\\\ \n'
                        '\\hspace*{1cm} \\begin{tikzpicture}   \n'
                        '\\tkzTabInit[deltacl=0.5,espcl=2.5,lgt=2]  \n'
                        '{$x$/1,$y\'$/1}  \n'
                        '{$-\\infty$,$%s$,$%s$,$%s$,$+\\infty$}  \n'
                        '\\tkzTabLine{,-,d,h,0,h,d,+,}  \n'
                        '\\end{tikzpicture}  \\\\ \n'
                        'Từ bảng xét dấu ta thấy \\\\ \n'
                        '\\hspace*{1cm} Hàm số đồng biến trên khoảng $(%s;+\\infty)$. \\\\ \n'
                        '\\hspace*{1cm} Hàm số nghịch biến trên khoảng $(-\\infty;%s)$. \\\\ \n'
                        %(latex(x1),latex(x2),
                        latex(daoham1),
                        latex(tu1),
                        latex(tu1),latex(Rational(-b1,2*a1)),
                        latex(x1),latex(x2),
                        latex(x1),latex(Rational(-b1,2*a1)),latex(x2),
                        latex(x2),latex(x1),
                            )
                        )
            if dang=='1':
                d = ['$(%s;+\\infty)$'%(latex(x2)),
                    '$(%s;+\\infty)$'%(latex(x2+1)),
                    '$(%s;%s)$'%(latex(x2+1),latex(x2+3)),
                    ]
                da= random.choice(d)
                s = [ 
                    '$(-\\infty;%s)$'%(latex(x1)), #
                    '$(-\\infty;%s)$'%(latex(x1-1)), #
                    '$(%s;%s)$'%(latex(x1-5),latex(x1-1)), #
                    '$(%s;%s)$'%(latex(x1),latex(x2)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=%s$. Hàm số đồng biến trên khoảng nào dưới đây?  \n'
                                %(latex(f1)
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
                loigiai=('Tập xác định: $\\mathscr{D}=(-\\infty;%s] \\cup [%s;+\\infty)$.\\\\ \n'
                        'Ta có $y\'=%s$.\\\\ \n'
                        'Dấu của $y\'$ phụ thuộc vào dấu của biểu thức $%s$. \\\\ \n'
                        '\\hspace*{1cm} $%s=0 \\Leftrightarrow x=%s$. \\\\ \n'
                        '$y\'$ không xác định trên đoạn $[%s;%s]$. \\\\ \n'
                        'Bảng xét dấu \\\\ \n'
                        '\\hspace*{1cm} \\begin{tikzpicture}   \n'
                        '\\tkzTabInit[deltacl=0.5,espcl=2.5,lgt=2]  \n'
                        '{$x$/1,$y\'$/1}  \n'
                        '{$-\\infty$,$%s$,$%s$,$%s$,$+\\infty$}  \n'
                        '\\tkzTabLine{,-,d,h,0,h,d,+,}  \n'
                        '\\end{tikzpicture}  \\\\ \n'
                        'Từ bảng xét dấu ta thấy \\\\ \n'
                        '\\hspace*{1cm} Hàm số đồng biến trên khoảng $(%s;+\\infty)$. \\\\ \n'
                        '\\hspace*{1cm} Hàm số nghịch biến trên khoảng $(-\\infty;%s)$. \\\\ \n'
                        %(latex(x1),latex(x2),
                        latex(daoham1),
                        latex(tu1),
                        latex(tu1),latex(Rational(-b1,2*a1)),
                        latex(x1),latex(x2),
                        latex(x1),latex(Rational(-b1,2*a1)),latex(x2),
                        latex(x2),latex(x1),
                            )
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-').replace('.0', '').replace('+1x', '+x').replace('-1x', '-x')
            return content


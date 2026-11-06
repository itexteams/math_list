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


def bt_dang12_p1_b1_c3_ds12(self):
            # Khai báo biến
            lisdang=['1','2','3','4','5','6','7','8']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                a=randint(2,7)
                b=randint(-6,6)
                c=randint(-6,6)
                d=randint(-2,2)
                k=randint(-9,9)
                while a==b or b==0 or a==-b or k==0:
                    a=randint(2,7)
                    b=randint(-6,6)
                    c=randint(-6,6)
                    d=randint(-2,2)
                    k=randint(-9,9)
                y=(a/3)*x**3+((a*c+b)/2)*x**2+b*c*x
                h=y.subs(x,d)
                hs=nsimplify(h+k)


                du = ['$F(x)=%sx^3+%sx^2+%sx+%s$'%(latex(nsimplify(a/3)),latex(nsimplify(((a*c+b)/2))),latex(c*b),latex(k))
                    ]
                da= random.choice(du)
                s = ['$F(x)=%sx^3+%sx^2+%sx+%s$'%(latex(nsimplify(-a/3)),latex(nsimplify(((a*c+b)/2))),latex(c*b),latex(k+1)),
                    '$F(x)=%sx^3+%sx^2+%sx+%s$'%(latex(nsimplify(a/3)),latex(nsimplify(((a*c+b)/2))),latex(c*b),latex(k+2)),
                    '$F(x)=%sx^3+%sx^2+%sx+%s$'%(latex(nsimplify(a/3)),latex(nsimplify(((a*c+b)))),latex(c*b),latex(k)),
                    '$F(x)=%sx^3+%sx^2+%sx+%s$'%(latex(nsimplify(a/3)),latex(nsimplify(((a*c+b)/2))),latex(c*b),latex(k-1)),
                    '$F(x)=%sx^3+%sx^2+%sx+%s$'%(latex(nsimplify(a/3)),latex(nsimplify(((a*c+b)/2))),latex(-b*c),latex(k-2)),

                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Biết $F(x)=\\displaystyle \\int{(%sx+%s)(x+%s) \\text{d}x}$ và thoả mãn $F\\left(%s\\right)=%s$. Khi đó $F(x)$ là hàm số nào trong các hàm số sau?'
                                %(latex(a),latex(b),latex(c),latex(d),latex(hs)
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
                        '\\hspace*{1cm} $\\displaystyle \\int{(%sx+%s)(x+%s) \\text{d}x}=\\displaystyle \\int{\\left(%sx^2+%sx+%s\\right) \\text{d}x}=%sx^3+%sx^2+%sx+\\text{C}$. \\\\ \n'
                        'Theo bài ta có\\\\ \n'
                        '\\hspace*{1cm} $F\\left(%s\\right)=%s \\Leftrightarrow %s\\cdot(%s)^3+%s\\cdot(%s)^2+%s\\cdot(%s)+\\text{C}=%s\\Leftrightarrow \\text{C}=%s$.\\\\ \n'
                        'Vậy $F(x)=%sx^3+%sx^2+%sx+%s$.'
                        %(latex(a),latex(b),latex(c),latex(a),latex(a*c+b),latex(b*c),
                        latex(nsimplify(a/3)),latex(nsimplify(((a*c+b)/2))),latex(c*b),
                        latex(d),latex(hs),latex(nsimplify(a/3)),latex(d),latex(nsimplify(((a*c+b)/2))),latex(d),latex(c*b),latex(d),latex(hs),latex(k),
                        latex(nsimplify(a/3)),latex(nsimplify(((a*c+b)/2))),latex(c*b),latex(k)
                        )

                        )
            if dang=='2':
                # Khai báo biến

                a=randint(2,7)
                b=randint(-6,6)
                c=randint(-2,2)
                d=randint(-6,6)
                while a==b or b==0 or a==-b or d==0:
                    a=randint(2,7)
                    b=randint(-6,6)
                    c=randint(-2,2)
                    d=randint(-6,6)
                y=(a**2/3)*x**3+a*b*x**2+b**2*x
                k=y.subs(x,c)
                hs=nsimplify(k+d)


                du = ['$F(x)=%sx^3+%sx^2+%sx+%s$'%(latex(nsimplify(a**2/3)),latex(a*b),latex(b*b),latex(d))
                    ]
                da= random.choice(du)
                s = ['$F(x)=%sx^3+%sx^2+%sx+%s$'%(latex(nsimplify(a**2/3)),latex(a*b),latex(b*b),latex(d+1)),
                    '$F(x)=%sx^3+%sx^2+%sx+%s$'%(latex(nsimplify(a**2/3)),latex(a*b),latex(b*b),latex(d+2)),
                    '$F(x)=%sx^3+%sx^2+%sx+%s$'%(latex(nsimplify(a**2/3)),latex(a*b),latex(b*b),latex(hs)),
                    '$F(x)=%sx^3+%sx^2+%sx+%s$'%(latex(nsimplify(a**2/3)),latex(a*b),latex(b*b),latex(-hs)),
                    '$F(x)=%sx^3+%sx^2+%sx+%s$'%(latex(nsimplify(a**2)),latex(a*b),latex(b*b),latex(d)),
                    '$F(x)=%sx^3+%sx^2+%sx+%s$'%(latex(nsimplify(-a**2)),latex(a*b),latex(b*b),latex(d))
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Biết $F(x)=\\displaystyle \\int{\\left(%sx+%s\\right)^2 \\text{d}x}$ và thoả mãn $F\\left(%s\\right)=%s$. Khi đó $F(x)$ là hàm số nào trong các hàm số sau?'
                                %(latex(a),latex(b),latex(c),latex(hs)
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
                        '\\hspace*{1cm} $\\displaystyle \\int{\\left(%sx+%s\\right)^2 \\text{d}x}=\\displaystyle \\int{\\left(%sx^2+%sx+%s\\right) \\text{d}x}=%sx^3+%sx^2+%sx+\\text{C}$. \\\\ \n'
                        'Theo bài ta có\\\\ \n'
                        '\\hspace*{1cm} $F\\left(%s\\right)=%s \\Leftrightarrow %s\\cdot(%s)^3+%s\\cdot(%s)^2+%s\\cdot(%s)+\\text{C}=%s\\Leftrightarrow \\text{C}=%s$.\\\\ \n'
                        'Vậy $F(x)=%sx^3+%sx^2+%sx+%s$.'
                        %(latex(a),latex(b),latex(a**2),latex(2*a*b),latex(b*b),
                        latex(nsimplify(a**2/3)),latex(a*b),latex(b*b),
                        latex(c),latex(hs),latex(nsimplify(a**2/3)),latex(c),latex(a*b),latex(c),latex(b*b),latex(c),latex(hs),latex(d),
                        latex(nsimplify(a**2/3)),latex(a*b),latex(b*b),latex(d)
                        )

                        )
            if dang=='3':
                # Khai báo biến
                a=randint(2,7)
                b=randint(2,5)
                c=randint(-9,9)
                d=randint(-15,15)
                while a==b or a==-b or d==0:
                    a=randint(2,7)
                    b=randint(2,5)
                    c=randint(-9,9)
                    d=randint(-15,15)
                x0=nsimplify((1-c)/b)

                du = ['$F(x)=%s\\ln\\abs{%sx+%s}+%s$'%(latex(nsimplify(a/b)),latex(b),latex(c),latex(d))
                    ]
                da= random.choice(du)
                s = ['$F(x)=%s\\ln\\abs{%sx+%s}+%s$'%(latex(nsimplify(a/b)),latex(b),latex(c),latex(d+1)),
                    '$F(x)=%s\\ln\\abs{%sx+%s}+%s$'%(latex(nsimplify(a/b)),latex(b),latex(c),latex(d+2)),
                    '$F(x)=%s\\ln\\abs{%sx+%s}+%s$'%(latex(nsimplify(a/b)),latex(b),latex(c),latex(d+3)),
                    '$F(x)=%s\\ln\\abs{%sx+%s}+%s$'%(latex(a),latex(b),latex(c),latex(d+4)),
                    '$F(x)=%s\\ln\\abs{%sx+%s}+%s$'%(latex(a),latex(b),latex(c),latex(d+5))
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Biết $F(x)=\\displaystyle \\int{\\dfrac{%s}{%sx+%s} \\text{d}x}$ và thoả mãn $F\\left(%s\\right)=%s$. Khi đó $F(x)$ là hàm số nào trong các hàm số sau?'
                                %(latex(a),latex(b),latex(c),latex(x0),latex(d)
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
                        '\\hspace*{1cm} $\\displaystyle \\int{\\dfrac{%s}{%sx+%s} \\text{d}x}=%s\\displaystyle \\int{\\dfrac{(%sx+%s)\'}{%sx+%s} \\text{d}x}=%s\\ln\\abs{%sx+%s}+\\text{C}$. \\\\ \n'
                        'Theo bài ta có\\\\ \n'
                        '\\hspace*{1cm} $F\\left(%s\\right)=%s \\Leftrightarrow %s\\ln\\abs{%s\\cdot\\left(%s\\right)+%s}+\\text{C}=%s\\Leftrightarrow \\text{C}=%s$.\\\\ \n'
                        'Vậy $F(x)=%s\\ln\\abs{%sx+%s}+%s$.'
                        %(latex(a),latex(b),latex(c),latex(nsimplify(a/b)),latex(b),latex(c),latex(b),latex(c),latex(nsimplify(a/b)),latex(b),latex(c),
                        latex(x0),latex(d),latex(nsimplify(a/b)),latex(b),latex(x0),latex(c),latex(d),latex(d),
                        latex(nsimplify(a/b)),latex(b),latex(c),latex(d)
                        )

                        )
            if dang=='4':
                # Khai báo biến
                a=randint(2,9)
                b=randint(-9,9)
                c=randint(-6,6)
                d=randint(-2,2)
                k=randint(-9,9)
                while a==b or b==0 or k==0:
                    a=randint(2,9)
                    b=randint(-9,9)
                    c=randint(-6,6)
                    d=randint(-2,2)
                    k=randint(-9,9)
                y=(a/3)*x**3+(b/2)*x**2+c*x
                h=y.subs(x,d)
                hs=nsimplify(h+k)


                du = ['$F(x)=%sx^3+%sx^2+%sx+%s$'%(latex(nsimplify(a/3)),latex(nsimplify(b/2)),latex(c),latex(k))
                    ]
                da= random.choice(du)
                s = ['$F(x)=%sx^3+%sx^2+%sx+%s$'%(latex(nsimplify(a/3)),latex(nsimplify(b/2)),latex(c),latex(k+1)),
                    '$F(x)=%sx^3+%sx^2+%sx+%s$'%(latex(nsimplify(a/3)),latex(nsimplify(b/2)),latex(c),latex(k+2)),
                    '$F(x)=%sx^3+%sx^2+%sx+%s$'%(latex(nsimplify(a/3)),latex(nsimplify(b/2)),latex(c),latex(k+3)),
                    '$F(x)=%sx^3+%sx^2+%sx+%s$'%(latex(nsimplify(a/3)),latex(nsimplify(b/2)),latex(c),latex(k+4)),
                    '$F(x)=%sx^3+%sx^2+%sx+%s$'%(latex(nsimplify(a)),latex(nsimplify(b/2)),latex(c),latex(k)),
                    '$F(x)=%sx^3+%sx^2+%sx+%s$'%(latex(nsimplify(-a/3)),latex(nsimplify(b/2)),latex(c),latex(k))
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Biết $F(x)=\\displaystyle \\int{(%sx^2+%sx+%s) \\text{d}x}$ và thoả mãn $F\\left(%s\\right)=%s$. Khi đó $F(x)$ là hàm số nào trong các hàm số sau?'
                                %(latex(a),latex(b),latex(c),latex(d),latex(hs)
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
                        '\\hspace*{1cm} $\\displaystyle \\int{(%sx^2+%sx+%s)\\text{d}x}=%sx^3+%sx^2+%sx+\\text{C}$. \\\\ \n'
                        'Theo bài ta có\\\\ \n'
                        '\\hspace*{1cm} $F\\left(%s\\right)=%s \\Leftrightarrow %s\\cdot(%s)^3+%s\\cdot(%s)^2+%s\\cdot(%s)+\\text{C}=%s\\Leftrightarrow \\text{C}=%s$.\\\\ \n'
                        'Vậy $F(x)=%sx^3+%sx^2+%sx+%s$.'
                        %(latex(a),latex(b),latex(c),latex(nsimplify(a/3)),latex(nsimplify(b/2)),latex(c),
                        latex(d),latex(hs),latex(nsimplify(a/3)),latex(d),latex(nsimplify(b/2)),latex(d),latex(c),latex(d),latex(hs),latex(k),
                        latex(nsimplify(a/3)),latex(nsimplify(b/2)),latex(c),latex(k)
                        )

                        )
            if dang=='5':
                # Khai báo biến
                a=randint(2,12)
                b=randint(2,15)
                k=randint(-9,9)
                while a==b or b==0 or k==0:
                    a=randint(2,12)
                    b=randint(-9,15)
                    k=randint(-9,9)
                d=nsimplify(k+a/3)

                du = ['$F(x)=%sx^3+%s\\ln\\abs{x}+%s$'%(latex(nsimplify(a/3)),latex(b),latex(k))
                    ]
                da= random.choice(du)
                s = ['$F(x)=%sx^3+%s\\ln\\abs{x}+%s$'%(latex(nsimplify(a)),latex(b),latex(k)),
                    '$F(x)=%sx^3+%s\\ln\\abs{x}+%s$'%(latex(nsimplify(a/3)),latex(-b),latex(k+1)),
                    '$F(x)=%sx^3+%s\\ln\\abs{x}+%s$'%(latex(nsimplify(a/3)),latex(b),latex(k+2)),
                    '$F(x)=%sx^3+%s\\ln\\abs{x}+%s$'%(latex(nsimplify(a/3)),latex(-b),latex(k-1)),
                    '$F(x)=%sx^3+%s\\ln\\abs{x}+%s$'%(latex(nsimplify(a/3)),latex(b),latex(k-2))
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Biết $F(x)=\\displaystyle \\int{\\left(%sx^2+\\dfrac{%s}{x}\\right) \\text{d}x}$ và thoả mãn $F\\left(1\\right)=%s$. Khi đó $F(x)$ là hàm số nào trong các hàm số sau?'
                                %(latex(a),latex(b),latex(d)
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
                        '\\hspace*{1cm} $\\displaystyle \\int{\\left(%sx^2+\\dfrac{%s}{x}\\right) \\text{d}x}=%sx^3+%s\\ln\\abs{x}+\\text{C}$. \\\\ \n'
                        'Theo bài ta có\\\\ \n'
                        '\\hspace*{1cm} $F\\left(1\\right)=%s \\Leftrightarrow %s\\cdot(1)^3+%s\\ln\\abs{1}+\\text{C}=%s\\Leftrightarrow \\text{C}=%s$.\\\\ \n'
                        'Vậy $F(x)=%sx^3+%s\\ln\\abs{x}+%s$.'
                        %(latex(a),latex(b),latex(nsimplify(a/3)),latex(b),
                        latex(d),latex(nsimplify(a/3)),latex(b),latex(d),latex(k),
                        latex(nsimplify(a/3)),latex(b),latex(k)
                        )

                        )
            if dang=='6':
                # Khai báo biến
                a=randint(2,12)
                b=randint(2,15)
                k=randint(-9,9)
                while a==b or b==0 or k==0:
                    a=randint(2,12)
                    b=randint(-9,15)
                    k=randint(-9,9)
                d=nsimplify(k+a)

                du = ['$F(x)=%sx-%s\\ln\\abs{x}+%s$'%(latex(nsimplify(a)),latex(b),latex(k))
                    ]
                da= random.choice(du)
                s = ['$F(x)=%sx-%s\\ln\\abs{x}+%s$'%(latex(nsimplify(a)),latex(b),latex(k+1)),
                    '$F(x)=%sx-%s\\ln\\abs{x}+%s$'%(latex(nsimplify(a)),latex(b),latex(k+2)),
                    '$F(x)=%sx-%s\\ln\\abs{x}+%s$'%(latex(nsimplify(a)),latex(b),latex(k-1)),
                    '$F(x)=%sx-%s\\ln\\abs{x}+%s$'%(latex(nsimplify(a)),latex(b),latex(k-2)),
                    '$F(x)=%sx-%s\\ln\\abs{x}+%s$'%(latex(nsimplify(a)),latex(b),latex(k+3))
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Biết $F(x)=\\displaystyle \\int{\\left(%s-\\dfrac{%s}{x}\\right) \\text{d}x}$ và thoả mãn $F\\left(1\\right)=%s$. Khi đó $F(x)$ là hàm số nào trong các hàm số sau?'
                                %(latex(a),latex(b),latex(d)
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
                        '\\hspace*{1cm} $\\displaystyle \\int{\\left(%s-\\dfrac{%s}{x}\\right) \\text{d}x}=%sx-%s\\ln\\abs{x}+\\text{C}$. \\\\ \n'
                        'Theo bài ta có\\\\ \n'
                        '\\hspace*{1cm} $F\\left(1\\right)=%s \\Leftrightarrow %s\\cdot1-%s\\ln\\abs{1}+\\text{C}=%s\\Leftrightarrow \\text{C}=%s$.\\\\ \n'
                        'Vậy $F(x)=%sx-%s\\ln\\abs{x}+%s$.'
                        %(latex(a),latex(b),latex(a),latex(b),
                        latex(d),latex(a),latex(b),latex(d),latex(k),
                        latex(a),latex(b),latex(k)
                        )

                        )
            if dang=='7':
                # Khai báo biến
                a=randint(2,12)
                b=randint(2,15)
                k=randint(-9,9)
                while a==b or b==0 or k==0:
                    a=randint(2,12)
                    b=randint(-9,15)
                    k=randint(-9,9)
                hs=k-a
                du = ['$F(x)=%s\\sin x+%s\\cos x+%s$'%( latex(b),latex(-a),latex(hs))
                    ]
                da= random.choice(du)
                s = ['$F(x)=%s\\sin x+%s\\cos x+%s$'%(latex(b),latex(a),latex(hs)),
                    '$F(x)=%s\\sin x+%s\\cos x+%s$'%(latex(-b),latex(-a),latex(hs+1)),
                    '$F(x)=%s\\sin x+%s\\cos x+%s$'%(latex(-b),latex(a),latex(hs)),
                    '$F(x)=%s\\sin x+%s\\cos x+%s$'%(latex(b),latex(-a),latex(hs+2)),
                    '$F(x)=%s\\sin x+%s\\cos x+%s$'%(latex(-b),latex(a),latex(hs-1))
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Biết $F(x)=\\displaystyle \\int{\\left(%s\\sin x+%s\\cos x\\right) \\text{d}x}$ và thoả mãn $F\\left(\\pi\\right)=%s$. Khi đó $F(x)$ là hàm số nào trong các hàm số sau?'
                                %(latex(a),latex(b),latex(k)
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
                        '\\hspace*{1cm} $\\displaystyle \\int{\\left(%s\\sin x+%s\\cos x\\right) \\text{d}x}=%s\\cos x+%s\\sin x+\\text{C}$. \\\\ \n'
                        'Theo bài ta có\\\\ \n'
                        '\\hspace*{1cm} $F\\left(\\pi\\right)=%s \\Leftrightarrow %s\\cos (\\pi)+%s\\sin(\\pi)+\\text{C}=%s\\Leftrightarrow \\text{C}=%s$.\\\\ \n'
                        'Vậy $F(x)=%s\\sin x+%s\\cos x+%s$.'
                        %(latex(a),latex(b),latex(-a),latex(b),
                        latex(k),latex(-a),latex(b),latex(k),latex(hs),
                        latex(b),latex(-a),latex(hs)
                        )

                        )
            if dang=='8':
                # Khai báo biến
                a=randint(2,12)
                b=randint(2,15)
                k=randint(-9,9)
                while a==b or b==0 or k==0:
                    a=randint(2,12)
                    b=randint(-9,15)
                    k=randint(-9,9)
                hs=k-b
                du = ['$F(x)=%s\\sin x+%s\\cos x+%s$'%( latex(b),latex(-a),latex(hs))
                    ]
                da= random.choice(du)
                s = ['$F(x)=%s\\sin x+%s\\cos x+%s$'%(latex(b),latex(a),latex(hs)),
                    '$F(x)=%s\\sin x+%s\\cos x+%s$'%(latex(-b),latex(-a),latex(hs+1)),
                    '$F(x)=%s\\sin x+%s\\cos x+%s$'%(latex(-b),latex(a),latex(hs)),
                    '$F(x)=%s\\sin x+%s\\cos x+%s$'%(latex(b),latex(-a),latex(hs+2)),
                    '$F(x)=%s\\sin x+%s\\cos x+%s$'%(latex(-b),latex(a),latex(hs-1))
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Biết $F(x)=\\displaystyle \\int{\\left(%s\\sin x+%s\\cos x\\right) \\text{d}x}$ và thoả mãn $F\\left(\\dfrac{\\pi}{2}\\right)=%s$. Khi đó $F(x)$ là hàm số nào trong các hàm số sau?'
                                %(latex(a),latex(b),latex(k)
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
                        '\\hspace*{1cm} $\\displaystyle \\int{\\left(%s\\sin x+%s\\cos x\\right) \\text{d}x}=%s\\cos x+%s\\sin x+\\text{C}$. \\\\ \n'
                        'Theo bài ta có\\\\ \n'
                        '\\hspace*{1cm} $F\\left(\\dfrac{\\pi}{2}\\right)=%s \\Leftrightarrow %s\\cos \\left(\\dfrac{\\pi}{2}\\right)+%s\\sin\\left(\\dfrac{\\pi}{2}\\right)+\\text{C}=%s\\Leftrightarrow \\text{C}=%s$.\\\\ \n'
                        'Vậy $F(x)=%s\\sin x+%s\\cos x+%s$.'
                        %(latex(a),latex(b),latex(-a),latex(b),
                        latex(k),latex(-a),latex(b),latex(k),latex(hs),
                        latex(b),latex(-a),latex(hs)
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('--', '+').replace('+-', '-').replace('+1x', '+x').replace('-1x', '-x').replace('+1x', '+x').replace('-1x', '-x').replace('$1x', '$x').replace('+0', '').replace('=1x', '=x').replace('=-1x', '=-x').replace('1\\cdot', '').replace('-1\\cdot', '-')
            return content


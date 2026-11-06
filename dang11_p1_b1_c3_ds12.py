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


def bt_dang11_p1_b1_c3_ds12(self):
            # Khai báo biến
            lisdang=['1','2','3','4','5','6','7']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến

                a=randint(2,20)
                b=randint(2,9)

                while a==b:

                    a=randint(2,20)
                    b=randint(2,9)


                du = ['$%se^x-\\dfrac{1}{%s^x\\ln %s}+\\text{C}$'%(latex(a),latex(b),latex(b))
                    ]
                da= random.choice(du)
                s = ['$%se^x-\\dfrac{1}{%s^x\\ln %s}+\\text{C}$'%(latex(-a),latex(b),latex(b)),
                    '$%se^x+\\dfrac{1}{%s^x\\ln %s}+\\text{C}$'%(latex(a),latex(b),latex(b)),
                    '$%se^x+\\dfrac{1}{%s^x\\ln %s}+\\text{C}$'%(latex(-a),latex(b),latex(b)),
                    '$%se^{x+1}-\\dfrac{1}{%s^x\\ln %s}+\\text{C}$'%(latex(a),latex(b),latex(b))
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('$\\displaystyle \\int{\\left(%se^x+\\dfrac{1}{%s^x}\\right) \\text{d}x}$ bằng'
                                %(latex(a),latex(b)
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
                        '\\begin{eqnarray*}\n'
                        '\\displaystyle \\int{\\left(%se^x+\\dfrac{1}{%s^x}\\right) \\text{d}x}&=&%s\\displaystyle \\int{ e^x \\text{d}x}+\\displaystyle \\int{ \\left(\\dfrac{1}{%s}\\right)^x \\text{d}x} \\\\ \n'
                        '&=&%se^x+\\dfrac{\\left(\\dfrac{1}{%s}\\right)^x}{\\ln \\dfrac{1}{%s}}+\\text{C}\\\\ \n'
                        '&=&%se^x-\\dfrac{1}{%s^x\\ln %s}+\\text{C}.\\\\ \n'
                        '\\end{eqnarray*}'
                        %(latex(a),latex(b),latex(a),latex(b),

                        latex(a),latex(b),latex(b),
                        latex(a),latex(b),latex(b))

                        )
            if dang=='2':
                # Khai báo biến

                a=randint(2,9)
                b=randint(2,9)

                while a==b:

                    a=randint(2,9)
                    b=randint(2,9)


                du = ['$\\dfrac{%s^x}{\\ln %s}+2\\cdot\\dfrac{%s^x}{\\ln %s}+\\dfrac{%s^x}{\\ln %s}+\\text{C}$'%( latex(a*a),latex(a*a),latex(a*b),latex(a*b),latex(b*b),latex(b*b))
                    ]
                da= random.choice(du)
                s = ['$\\dfrac{%s^x}{\\ln %s}+2\\cdot\\dfrac{%s^x}{\\ln %s}+\\dfrac{%s^x}{\\ln %s}+\\text{C}$'%( latex(a),latex(a),latex(a*b),latex(a*b),latex(b),latex(b)),
                    '$\\dfrac{%s^x}{\\ln %s}+2\\cdot\\dfrac{%s^x}{\\ln %s}+\\dfrac{%s^x}{\\ln %s}+\\text{C}$'%( latex(a),latex(a),latex(a*b),latex(a*b),latex(b*b),latex(b*b)),
                    '$\\dfrac{%s^x}{\\ln %s}+2\\cdot\\dfrac{%s^x}{\\ln %s}+\\dfrac{%s^x}{\\ln %s}+\\text{C}$'%( latex(a*a),latex(a*a),latex(a*b),latex(a*b),latex(b),latex(b)),
                    '$\\dfrac{%s^x}{\\ln %s}+2\\cdot\\dfrac{%s^x}{\\ln %s}+\\dfrac{%s^x}{\\ln %s}+\\text{C}$'%( latex(a*a),latex(a*a),latex(a),latex(a),latex(b*b),latex(b*b)),
                    '$\\dfrac{%s^x}{\\ln %s}+2\\cdot\\dfrac{%s^x}{\\ln %s}+\\dfrac{%s^x}{\\ln %s}+\\text{C}$'%( latex(a*a),latex(a*a),latex(b),latex(b),latex(b*b),latex(b*b))
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('$\\displaystyle \\int{\\left(%s^x+%s^x\\right)^2 \\text{d}x}$ bằng'
                                %(latex(a),latex(b)
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
                        '\\begin{eqnarray*}\n'
                        '\\displaystyle \\int{\\left(%s^x+%s^x\\right)^2 \\text{d}x}&=&\\displaystyle \\int{ \\left[\\left(%s^x\\right)^2+2\\cdot%s^x\\cdot%s^x+\\left(%s^x\\right)^2\\right] \\text{d}x} \\\\ \n'
                        '&=&\\displaystyle \\int{ \\left(%s^x+2\\cdot%s^x+%s^x\\right) \\text{d}x}\\\\ \n'
                        '&=&\\dfrac{%s^x}{\\ln %s}+2\\cdot\\dfrac{%s^x}{\\ln %s}+\\dfrac{%s^x}{\\ln %s}+\\text{C}.\\\\ \n'
                        '\\end{eqnarray*}'
                        %(latex(a),latex(b),latex(a),latex(a),latex(b),latex(b),
                        latex(a*a),latex(a*b),latex(b*b),
                        latex(a*a),latex(a*a),latex(a*b),latex(a*b),latex(b*b),latex(b*b))

                        )
            if dang=='3':
                # Khai báo biến

                a=randint(2,6)
                b=randint(2,5)
                c=randint(2,4)
                d=randint(1,3)
                while a==b:
                    a=randint(2,6)
                    b=randint(2,5)
                    c=randint(2,4)
                    d=randint(1,3)


                du = ['$\\dfrac{%s\\cdot %s^x}{\\ln %s}+\\text{C}$'%(latex(b**d),latex(a*(b**c)),latex(a*(b**c)))
                    ]
                da= random.choice(du)
                s = ['$\\dfrac{%s\\cdot %s^x}{\\ln %s}+\\text{C}$'%(latex(-b**d),latex(a*(b**c)),latex(a*(b**c))),
                    '$\\dfrac{%s\\cdot %s^x}{\\ln %s}+\\text{C}$'%(latex(d),latex(a*(b**c)),latex(a*(b**c))),
                    '$\\dfrac{%s\\cdot %s^x}{\\ln %s}+\\text{C}$'%(latex(b),latex(a*(b**c)),latex(a*(b**c))),
                    '$\\dfrac{%s\\cdot %s^x}{\\ln %s}+\\text{C}$'%(latex(b**d),latex((b**c)),latex(a*(b**c))),
                    '$\\dfrac{%s\\cdot %s^x}{\\ln %s}+\\text{C}$'%(latex(b**d),latex(a*(b**c)),latex((b**c)))
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('$\\displaystyle \\int{\\left(%s^x\\cdot%s^{%sx+%s}\\right) \\text{d}x}$ bằng'
                                %(latex(a),latex(b),latex(c),latex(d)
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
                        '\\begin{eqnarray*}\n'
                        '\\displaystyle \\int{\\left(%s^x\\cdot%s^{%sx+%s}\\right) \\text{d}x}&=&\\displaystyle \\int{ \\left(%s^x\\cdot %s^{%sx}\\cdot %s^%s \\right) \\text{d}x} \\\\ \n'
                        '&=&\\displaystyle \\int{ \\left(%s^x\\cdot \\left(%s^{%s}\\right)^x\\cdot %s \\right) \\text{d}x}\\\\ \n'
                        '&=&%s\\displaystyle \\int{ \\left(%s^x\\cdot %s^x\\right) \\text{d}x}\\\\ \n'
                        '&=&%s\\displaystyle \\int{ \\left(%s^x\\right) \\text{d}x}\\\\ \n'
                        '&=&\\dfrac{%s\\cdot %s^x}{\\ln %s}+\\text{C}.'
                        '\\end{eqnarray*}'
                        %(latex(a),latex(b),latex(c),latex(d),latex(a),latex(b),latex(c),latex(b),latex(d),
                        latex(a),latex(b),latex(c),latex(b**d),
                        latex(b**d),latex(a),latex(b**c),
                            latex(b**d),latex(a*(b**c)),
                            latex(b**d),latex(a*(b**c)),latex(a*(b**c)))

                        )
            if dang=='4':
                # Khai báo biến

                a=randint(2,5)
                b=randint(2,9)

                while a==b:

                    a=randint(2,5)
                    b=randint(2,9)


                du = ['$%sx+%se^{2x}+%s\\cdot\\dfrac{1}{e^{2x}}+\\text{C}$'%(latex(2*a*b), latex(nsimplify((a*a)/2)),latex(nsimplify((-b*b)/2)))
                    ]
                da= random.choice(du)
                s = ['$%sx+%se^{2x}+%s\\cdot\\dfrac{1}{e^{2x}}+\\text{C}$'%(latex(-2*a*b), latex(nsimplify((a*a)/2)),latex(nsimplify((-b*b)/2))),
                    '$%sx+%se^{2x}+%s\\cdot\\dfrac{1}{e^{2x}}+\\text{C}$'%(latex(a*b), latex(nsimplify((a*a)/2)),latex(nsimplify((-b*b)/2))),
                    '$%sx+%se^{2x}+%s\\cdot\\dfrac{1}{e^{2x}}+\\text{C}$'%(latex(-a*b), latex(nsimplify((a*a)/2)),latex(nsimplify((-b*b)/2))),
                    '$%sx+%se^{2x}+%s\\cdot\\dfrac{1}{e^{2x}}+\\text{C}$'%(latex(2*a*b), latex(nsimplify((a*a))),latex(nsimplify((-b*b)/2))),
                    '$%sx+%se^{2x}+%s\\cdot\\dfrac{1}{e^{2x}}+\\text{C}$'%(latex(2*a*b), latex(nsimplify((a*a)/2)),latex(nsimplify((-b*b)))),
                    '$%sx+%se^{2x}+%s\\cdot\\dfrac{1}{e^{2x}}+\\text{C}$'%(latex(2*a*b), latex(nsimplify((a*a))),latex(nsimplify((-b*b))))
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('$\\displaystyle \\int{\\left(%se^x+\\dfrac{%s}{e^x}\\right)^2 \\text{d}x}$ bằng'
                                %(latex(a),latex(b)
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
                        '\\begin{eqnarray*}\n'
                        '\\displaystyle \\int{\\left(%se^x+\\dfrac{%s}{e^x}\\right)^2 \\text{d}x}&=&\\displaystyle \\int{\\left(%se^{2x}+%s+\\dfrac{%s}{e^{2x}}\\right) \\text{d}x} \\\\ \n'
                        '&=&%s\\displaystyle \\int{e^{2x} \\text{d}x}+%s\\displaystyle \\int{\\text{d}x}+%s\\displaystyle \\int{\\dfrac{1}{e^{2x}} \\text{d}x}\\\\ \n'
                        '&=&%s\\displaystyle \\int{(2x)\'e^{2x} \\text{d}x}+%s\\displaystyle \\int{\\text{d}x}+%s\\displaystyle \\int{(-2x)\'e^{-2x} \\text{d}x}\\\\ \n'
                        '&=&%se^{2x}+%sx+%s\\cdot\\dfrac{1}{e^{2x}}+\\text{C}.'
                        '\\end{eqnarray*}'
                        %(latex(a),latex(b),latex(a*a),latex(2*a*b),latex(b*b),
                        latex(a*a),latex(2*a*b),latex(b*b),
                        latex(nsimplify((a*a)/2)),latex(2*a*b),latex(nsimplify((-b*b)/2)),
                        latex(nsimplify((a*a)/2)),latex(2*a*b),latex(nsimplify((-b*b)/2)),
                        )

                        )
            if dang=='5':
                # Khai báo biến

                a=randint(2,20)
                b=randint(2,7)
                while a==b:
                    a=randint(2,20)
                    b=randint(2,7)

                du = ['$%se^{%sx}+\\text{C}$'%(latex(nsimplify(a/b)),latex(b))
                    ]
                da= random.choice(du)
                s = ['$%se^{%sx}+\\text{C}$'%(latex(nsimplify(-a/b)),latex(b)),
                    '$%se^{%sx+1}+\\text{C}$'%(latex(nsimplify(a/b)),latex(b)),
                    '$%se^{%sx}+\\text{C}$'%(latex(a),latex(b)),
                    '$e^{%sx+1}+\\text{C}$'%(latex(b)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('$\\displaystyle \\int{%se^{%sx}\\text{d}x}$ bằng'
                                %(latex(a),latex(b)
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
                        '\\begin{eqnarray*}\n'
                        '\\displaystyle \\int{%se^{%sx}\\text{d}x}&=&%s\\displaystyle \\int{\\left(e^{%s}\\right)^x\\text{d}x} \\\\ \n'
                        '&=&%s\\cdot\\dfrac{\\left(e^{%s}\\right)^x}{\\ln e^{%s}}+\\text{C} \\\\ \n'
                        '&=&%se^{%sx}+\\text{C}.'
                        '\\end{eqnarray*}'
                        %(latex(a),latex(b),latex(a),latex(b),

                        latex(a),latex(b),latex(b),
                        latex(nsimplify(a/b)),latex(b))

                        )
            if dang=='6':
                # Khai báo biến

                a=randint(2,2024)


                du = ['$\\dfrac{-1}{%s^x\\ln %s}+\\text{C}$'%(latex(a),latex(a))
                    ]
                da= random.choice(du)
                s = ['$\\dfrac{1}{%s^x\\ln %s}+\\text{C}$'%(latex(a),latex(a)),
                    '$\\dfrac{-%s}{%s^x\\ln %s}+\\text{C}$'%(latex(a),latex(a),latex(a)),
                    '$\\dfrac{%s^x}{\\ln %s}+\\text{C}$'%(latex(a),latex(a)),
                    '$\\dfrac{-%s^x}{\\ln %s}+\\text{C}$'%(latex(a),latex(a))
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('$\\displaystyle \\int{\\dfrac{1}{%s^x}\\text{d}x}$ bằng'
                                %(latex(a)
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
                        '\\begin{eqnarray*}\n'
                        '\\displaystyle \\int{\\dfrac{1}{%s^x}\\text{d}x}&=&\\displaystyle \\int{\\left(\\dfrac{1}{%s}\\right)^x\\text{d}x} \\\\ \n'
                        '&=&\\dfrac{\\left(\\dfrac{1}{%s}\\right)^x}{\\ln \\dfrac{1}{%s}}+\\text{C} \\\\ \n'
                        '&=&\\dfrac{-1}{%s^x\\ln %s}+\\text{C}.'
                        '\\end{eqnarray*}'
                        %(latex(a),latex(a),
                        latex(a),latex(a),
                        latex(a),latex(a))

                        )
            if dang=='7':
                # Khai báo biến

                a=randint(2,2024)


                du = ['$\\dfrac{%s^x}{\\ln %s}+\\text{C}$'%(latex(a),latex(a))
                    ]
                da= random.choice(du)
                s = ['$-\\dfrac{%s^x}{\\ln %s}+\\text{C}$'%(latex(a),latex(a)),
                    '$%s^x+\\text{C}$'%(latex(a)),
                    '$-%s^x+\\text{C}$'%(latex(a)),
                    '$%s^x\\ln%s+\\text{C}$'%(latex(a),latex(a)),
                    '$\\dfrac{1}{%s^x\\ln %s}+\\text{C}$'%(latex(a),latex(a))
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('$\\displaystyle \\int{%s^x\\text{d}x}$ bằng'
                                %(latex(a)
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
                        '\\hspace*{1cm} $\\displaystyle \\int{%s^x\\text{d}x}=\\dfrac{%s^x}{\\ln %s}+\\text{C}$.'
                        %(latex(a),latex(a),latex(a)
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('--', '+').replace('+-', '-')
            return content


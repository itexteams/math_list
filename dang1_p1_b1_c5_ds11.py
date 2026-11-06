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


def bt_dang1_p1_b1_c5_ds11(self):
            # Khai báo biến
            lisdang=['1','2','3','4','5','6','7']
            dang=random.choice(lisdang)
            if dang=='7':     
                du = ['$\\left(\\dfrac{a}{b} \\right)^n =\\dfrac{a^n}{b^n}$',
                    ]
                da= random.choice(du)
                s = ['$\\left(\\dfrac{a}{b} \\right)^n =\\dfrac{a}{b^n}$',
                    '$\\left(\\dfrac{a}{b} \\right)^n =\\dfrac{a^n}{b}$',
                    '$\\left(\\dfrac{a}{b} \\right)^n =(a-b)^n$',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Với $a \\ne 0, b \\ne 0$ và $n$ là số nguyên. Khẳng định nào sau đây là đúng?'
                                %(
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
                loigiai=('Với $a \\ne 0, b \\ne 0$ và $n$ là số nguyên ta có $\\left(\\dfrac{a}{b} \\right)^n =\\dfrac{a^n}{b^n}$. \n'
                        %(
                        ))

            if dang=='6':     
                du = ['$\\left(ab \\right)^n =a^n \\cdot b^n$',
                    ]
                da= random.choice(du)
                s = ['$\\left(ab \\right)^n =a \\cdot b^n$',
                    '$\\left(ab \\right)^n =a^n \\cdot b$',
                    '$\\left(ab \\right)^n =-a^n \\cdot b^n$',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Với $a \\ne 0, b \\ne 0$ và $n$ là số nguyên. Khẳng định nào sau đây là đúng?'
                                %(
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
                loigiai=('Với $a \\ne 0, b \\ne 0$ và $n$ là số nguyên ta có $\\left(ab \\right)^n =a^n \\cdot b^n$. \n'
                        %(
                        ))

            if dang=='5':     
                du = ['$\\left(a^m \\right)^n =a^{mn}$',
                    ]
                da= random.choice(du)
                s = ['$\\left(a^m \\right)^n =a^{m+n}$',
                    '$\\left(a^m \\right)^n =a^{m-n}$',
                    '$\\left(a^m \\right)^n =a^{m^n}$',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Với $a \\ne 0$ và $m, n$ là số nguyên. Khẳng định nào sau đây là đúng?'
                                %(
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
                loigiai=('Với $a \\ne 0$ và $m, n$ là số nguyên ta có $\\left(a^m \\right)^n =a^{mn}$. \n'
                        %(
                        ))

            if dang=='4':     
                du = ['$\\dfrac{a^m}{a^n} =a^{m-n}$',
                    ]
                da= random.choice(du)
                s = ['$\\dfrac{a^m}{a^n} =a^{m+n}$',
                    '$\\dfrac{a^m}{a^n} =a^{n-m}$',
                    '$\\dfrac{a^m}{a^n} =a^{\\tfrac{m}{n}}$',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Với $a \\ne 0$ và $m, n$ là số nguyên. Khẳng định nào sau đây là đúng?'
                                %(
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
                loigiai=('Với $a \\ne 0$ và $m, n$ là số nguyên ta có $\\dfrac{a^m}{a^n} =a^{m-n}$. \n'
                        %(
                        ))

            if dang=='3':     
                du = ['$a^m \\cdot a^n =a^{m+n}$',
                    ]
                da= random.choice(du)
                s = ['$a^m \\cdot a^n =a^{m \\cdot n}$',
                    '$a^m \\cdot a^n =a^{m-n}$',
                    '$a^m \\cdot a^n =-a^{m+n}$',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Với $a \\ne 0$ và $m, n$ là số nguyên. Khẳng định nào sau đây là đúng?'
                                %(
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
                loigiai=('Với $a \\ne 0$ và $m, n$ là số nguyên ta có $a^m \\cdot a^n =a^{m+n}$. \n'
                        %(
                        ))

            if dang=='2':     
                du = ['$a^{-n}=\\dfrac{1}{a^n}$',
                    ]
                da= random.choice(du)
                s = ['$a^{-n}=-\\dfrac{1}{a^n}$',
                    '$a^{-n}=-a^n$',
                    '$a^{-n}=a^n$',
                    '$a^{-n}=\\dfrac{n}{a}$',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Với $a$ là số thực khác $0$ và $n$ là số nguyên dương. Khẳng định nào sau đây là đúng?'
                                %(
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
                loigiai=('Với $a$ là số thực khác $0$ và $n$ là số nguyên dương ta có $a^{-n}=\\dfrac{1}{a^n}$. \n'
                        %(
                        ))

            if dang=='1':     
                du = ['$a^0=1$',
                    ]
                da= random.choice(du)
                s = ['$a^0=0$',
                    '$a^0=2$',
                    '$a^0=3$',
                    '$a^0=a$',
                    '$a^0=-1$',
                    '$a^0=-2$',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Với $a$ là số thực khác $0$. Khẳng định nào sau đây là đúng?'
                                %(
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
                loigiai=('Với $a$ là số thực khác $0$ ta có $a^0=1$. \n'
                        %(
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


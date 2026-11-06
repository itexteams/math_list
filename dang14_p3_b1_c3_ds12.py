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


def bt_dang14_p3_b1_c3_ds12(self):
            # Khai báo biến
            # --- Bước 1 & 3: Nghiên cứu và tạo Random ---
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':

                m = random.randint(1, 5)
                n = random.randint(-5, 5)
                p = random.randint(1, 10)

                x = symbols('x')
                F_expr = (m*x**2 + n*x + p) / x

                a = m
                b = 0
                c = -p

                # Giá trị cần tìm: a + b - c
                kq_val = a + b - c

                # --- Tạo các đáp án nhiễu ---
                du = ['$%s$' % (kq_val)]
                da = du[0]

                s = [
                    '$%s$' % (kq_val + random.randint(1, 3)),
                    '$%s$' % (kq_val - random.randint(1, 3)),
                    '$%s$' % (kq_val + random.randint(4, 6)),
                    '$%s$' % (kq_val * 2),
                    '$%s$' % (abs(kq_val - 5))
                ]

                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # --- Bước 2: Viết lại nội dung câu hỏi (Latex) ---
                noidungcauhoi = (r'''Biết hàm số $F(x) = \frac{%s x^2 %s x + %s}{x}$ là một nguyên hàm của hàm số $f(x) = \frac{ax^2 + bx + c}{x^2}$ (với $a, b, c$ là các số thực). Khi đó giá trị $a+b-c$ bằng?''' 
                                 % (latex(m), (f"+ {n}" if n >= 0 else f"{n}"), latex(p)))

                # Các đáp án
                da_d = '\\True ' + str(da)
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = (r'''Ta có $F(x) = %s x %s + \frac{%s}{x}$. \\ 
                             Đạo hàm $F'(x) = \left( %s x %s + \frac{%s}{x} \right)' = %s - \frac{%s}{x^2} = \frac{%s x^2 - %s}{x^2}$. \\
                             Vì $F'(x) = f(x)$, đồng nhất hệ số ta được: $a = %s; b = %s; c = %s$. \\
                             Do đó $a + b - c = %s + %s - (%s) = %s$.'''
                           % (latex(m), (f"+ {n}" if n >= 0 else f"{n}"), latex(p),
                              latex(m), (f"+ {n}" if n >= 0 else f"{n}"), latex(p),
                              latex(m), latex(p), latex(m), latex(p),
                              latex(a), latex(b), latex(c),
                              latex(a), latex(b), latex(c), latex(kq_val)))
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq_val))

            # --- Xuất câu trắc nghiệm ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content  


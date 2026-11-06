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


def bt_dang20_p1_b1_c3_hh10(self):
            # Khai báo biến và chọn dạng (Trục Ox hoặc Trục Oy)
            # Khai báo biến ký hiệu
            x, y = symbols('x y')

            # B1 & B3: Thiết lập random và tính toán thông số bài toán
            # Để M có tọa độ nguyên, ta cần chọn các hệ số sao cho phép chia cho (1-k) là phép chia hết
            # Giả sử đường thẳng d: ax + by + c = 0
            # A(-c/a; 0), B(0; -c/b). Tỉ số chia là k.
            # M = (A - kB) / (1-k)

            def generate_data():
                while True:
                    # Chọn m = 1 - k để mẫu số gọn (thường k âm như -3, -2, -1/2...)
                    # Ở đây chọn k là số nguyên âm để giống đề bài mẫu
                    k = random.choice([-3, -2, -4, -5])
                    m = 1 - k 

                    # Chọn a, b nhỏ
                    a = random.choice([-3, -2, -1, 1, 2, 3])
                    b = random.choice([-3, -2, -1, 1, 2, 3])
                    if abs(a) == abs(b): continue # Tránh trường hợp quá đặc biệt

                    # Để xA = -c/a và yB = -c/b nguyên, và xM, yM nguyên:
                    # c phải chia hết cho BCNN(a*m, b*m)
                    step = abs(a * b * m)
                    c = step * random.choice([-2, -1, 1, 2])

                    # Tọa độ các điểm
                    xA = Rational(-c, a)
                    yB = Rational(-c, b)

                    # Tọa độ M
                    xM = Rational(xA - k*0, m)
                    yM = Rational(0 - k*yB, m)

                    if xM.is_integer and yM.is_integer:
                        return a, b, c, k, xA, yB, xM, yM

            a, b, c, k, xA, yB, xM, yM = generate_data()

            # Phương trình đường thẳng d dạng tổng quát
            d_expr = a*x + b*y + c

            # Đường thẳng d' đi qua M(xM, yM) và vuông góc với d
            # VTPT của d là (a, b) -> VTPT của d' là (-b, a) hoặc (b, -a)
            a_p = -b
            b_p = a
            c_p = -(a_p * xM + b_p * yM)
            d_prime_expr = a_p*x + b_p*y + c_p

            # B2: Viết lại nội dung bài toán và lời giải
            noidungcauhoi = ('''Đường thẳng $d: %s = 0$ cắt các trục tọa độ $Ox$ và $Oy$ lần lượt tại các điểm $A$ và $B$. Gọi $M$ là điểm chia đoạn $AB$ theo tỉ số $%s$. Phương trình đường thẳng đi qua $M$ và vuông góc với $d$ là'''
                            %(latex(a*x + b*y + c), latex(k)))

            # Tạo lời giải chi tiết
            loigiai = ('''Cho $x = 0 \\Rightarrow y = %s$, $y = 0 \\Rightarrow x = %s$. Do đó $A(%s; 0), B(0; %s)$.\\\\
                    Gọi $M(x_0; y_0)$ là điểm chia đoạn $AB$ theo tỉ số $k = %s$, ta có: \\\\
                    $x_0 = \\frac{x_A - kx_B}{1 - k} = \\frac{%s - (%s) \\cdot 0}{%s} = %s$. \\\\
                    $y_0 = \\frac{y_A - ky_B}{1 - k} = \\frac{0 - (%s) \\cdot (%s)}{%s} = %s$. \\\\
                    Vậy $M(%s; %s)$. \\\\
                    Vectơ pháp tuyến của $d: %s = 0$ là $\\vec{n}_d = (%s; %s)$. \\\\
                    Do đường thẳng $d'$ vuông góc với $d$ nên $d'$ có vectơ pháp tuyến là $\\vec{n}_{d'} = (%s; %s)$. \\\\
                    Phương trình đường thẳng $d'$ qua $M$ và vuông góc với $d$ là: \\\\
                    $%s(x - (%s)) + %s(y - %s) = 0 \\Leftrightarrow %s = 0$.'''
                    %(latex(yB), latex(xA), latex(xA), latex(yB), 
                      latex(k), latex(xA), latex(k), latex(1-k), latex(xM),
                      latex(k), latex(yB), latex(1-k), latex(yM),
                      latex(xM), latex(yM), latex(d_expr), latex(a), latex(b),
                      latex(a_p), latex(b_p),
                      latex(a_p), latex(xM), latex(b_p), latex(yM), latex(d_prime_expr)))

            # B4: Điều chỉnh các phương án sai
            da_d = '\\True $' + latex(d_prime_expr) + ' = 0$'

            # Tạo các đáp án nhiễu bằng cách thay đổi hệ số tự do hoặc đổi chỗ a, b
            s = [
                '$' + latex(a_p*x + b_p*y - c_p) + ' = 0$', # Sai dấu hệ số tự do
                '$' + latex(b_p*x + a_p*y + c_p) + ' = 0$', # Đổi chỗ hệ số x, y
                '$' + latex(a_p*x + b_p*y + c_p + random.choice([-2, 2, 5])) + ' = 0$', # Sai số lệch
                '$' + latex(a*x + b*y + c_p) + ' = 0$' # Cùng phương với d (song song)
            ]

            # Loại bỏ trùng lặp nếu có và chọn 3 đáp án sai
            s = list(set(s))
            if da_d in s: s.remove(da_d)
            random.shuffle(s)
            das1, das2, das3 = s[0], s[1], s[2]

            # Trộn đáp án
            list_1 = [da_d, das1, das2, das3]
            random.shuffle(list_1)

            # Xuất nội dung theo cấu trúc mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choice \n'
                '{' + str(list_1[0]) + '}\n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 


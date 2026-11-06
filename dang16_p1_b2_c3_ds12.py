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


def bt_dang16_p1_b2_c3_ds12(self):
            # Khai báo biến
            # --- CẤU HÌNH BÀI TOÁN ---
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B3: Random số liệu
                # Tử số (a): ví dụ -3
                a = randint(-5, -1) 

                # Số mũ (n): ví dụ 3 (để thành x^3)
                n = randint(2, 4)

                # Cận tích phân
                low = randint(1, 2)       # Cận dưới
                high = low + randint(1, 2) # Cận trên

                # Khai báo biến x cho Sympy
                x = symbols('x')

                # Hàm số f(x) = a / x^n
                f_expr = Rational(a, 1) / (x**n)

                # Tính tích phân đúng (Kết quả)
                kq_chuan = integrate(f_expr, (x, low, high))

                # Tính nguyên hàm để hiển thị lời giải (Antiderivative)
                nguyen_ham = integrate(f_expr, x)

                # --- TẠO CÁC PHƯƠNG ÁN NHIỄU (DISTRACTORS) ---
                # Sai lầm 1: Sai dấu (âm thành dương hoặc ngược lại)
                kq_sai1 = -kq_chuan

                # Sai lầm 2: Cộng thêm một hằng số nhỏ hoặc sai lệch mẫu số
                kq_sai2 = kq_chuan + Rational(1, 2)

                # Sai lầm 3: Sai cận hoặc tính sai phân số (đảo ngược tử mẫu chẳng hạn)
                if kq_chuan != 0:
                    kq_sai3 = 1 / kq_chuan
                else:
                    kq_sai3 = Rational(a, 2)

                # Gom đáp án vào list
                # Format hiển thị đáp án
                def fmt_ans(val):
                    return '$%s$' % latex(val)

                du = [fmt_ans(kq_chuan)] # Đáp án đúng

                # Danh sách đáp án sai
                s = [
                    fmt_ans(kq_sai1),
                    fmt_ans(kq_sai2),
                    fmt_ans(kq_sai3)
                ]

                # Đảm bảo các đáp án sai không trùng nhau và không trùng đáp án đúng
                # (Trong thực tế nên dùng set để lọc, nhưng ở đây code đơn giản)

                # Lấy ngẫu nhiên các đáp án sai vào vị trí
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # --- NỘI DUNG CÂU HỎI ---
                # Đề bài: Tích phân từ low đến high của a/x^n dx
                noidungcauhoi = ('''Tích phân $\\displaystyle \\int_{%s}^{%s} \\frac{%s}{x^{%s}} \\text{d}x$ có giá trị bằng''' 
                                 % (low, high, a, n))

                # Các đáp án
                da = du[0] # Đáp án đúng gốc
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # --- NỘI DUNG LỜI GIẢI ---
                # Xây dựng chuỗi lời giải chi tiết
                # Bước 1: Viết dưới dạng lũy thừa âm
                step1 = "Ta có: $\\displaystyle I = \\int_{%s}^{%s} %s x^{-%s} \\text{d}x$." % (low, high, a, n)

                # Bước 2: Nguyên hàm
                # Cần format nguyên hàm thủ công một chút để đẹp mắt
                # Nguyên hàm của ax^-n là (a * x^(-n+1)) / (-n+1)
                new_exp = -n + 1
                coeff = Rational(a, new_exp)

                step2 = "$= \\left. \\frac{%s x^{%s}}{%s} \\right|_{%s}^{%s} = \\left. %s \\right|_{%s}^{%s}$" % (
                    a, new_exp, new_exp, low, high, latex(nguyen_ham), low, high
                )

                # Bước 3: Thế cận
                val_high = nguyen_ham.subs(x, high)
                val_low = nguyen_ham.subs(x, low)

                step3 = "$= \\left(%s\\right) - \\left(%s\\right) = %s$." % (
                    latex(val_high), latex(val_low), latex(kq_chuan)
                )

                loigiai = step1 + " \n" + step2 + " \n" + step3

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{\n'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


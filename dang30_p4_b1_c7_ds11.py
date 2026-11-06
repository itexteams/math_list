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


def bt_dang30_p4_b1_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 1: Tạo các hệ số ngẫu nhiên cho hàm số y = (ax^2 + bx + c) / (dx + e)
                # Để bài toán đẹp, ta chọn các số nguyên nhỏ
                a = randint(1, 2)
                b = randint(1, 3)
                c = randint(-5, -1)
                d = randint(1, 2)
                e = randint(-3, 3)

                # Chọn x0 sao cho mẫu số khác 0
                x0 = randint(2, 4)
                while (d * x0 + e) == 0:
                    x0 = randint(2, 4)

                # Định nghĩa hàm số
                f_num = a*x**2 + b*x + c
                f_den = d*x + e
                f = f_num / f_den

                # Tính f(x0)
                fx0 = f.subs(x, x0)

                # Bước 2: Tính toán các thành phần cho lời giải
                # Hiệu f(x) - f(x0)
                hieu = simplify(f - fx0)
                # Phân tích tử số của hiệu thành nhân tử (x - x0) * (...)
                hieu_tu = simplify(f_num * fx0.denominator - fx0.numerator * f_den)
                hieu_tu_factor = factor(hieu_tu)
                hieu_mau = f_den * fx0.denominator

                # Biểu thức f(x)-f(x0) / (x-x0)
                ti_so_rut_gon = simplify(hieu / (x - x0))

                # Kết quả đạo hàm
                kq_value = ti_so_rut_gon.subs(x, x0)
                kq = '$%s$' % (latex(kq_value).replace('.', ','))

                # Bước 3: Tạo các phương án sai
                s = []
                candidates = [
                    kq_value + 1, 
                    kq_value - 1, 
                    kq_value + Rational(1, 2), 
                    -kq_value, 
                    1/kq_value if kq_value != 0 else 2,
                    kq_value * 2
                ]
                for val in candidates:
                    val_latex = '$%s$' % (latex(val).replace('.', ','))
                    if val_latex != kq and val_latex not in s:
                        s.append(val_latex)

                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Tính đạo hàm bằng định nghĩa của hàm số $y = f\\left(x\\right) = \\frac{%s}{%s}$ tại điểm $x_0 = %s$.'''
                                 % (latex(f_num), latex(f_den), latex(x0)))

                # Các đáp án
                da_d = ('\\True ' + str(kq))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (Viết chi tiết y hệt mẫu trong ảnh)
                # f(x) - f(x0) = ...
                step1_expr = latex(f) + ' - ' + latex(fx0)
                step1_combined = '\\frac{%s}{%s}' % (latex(hieu_tu), latex(hieu_mau))
                step1_factored = '\\frac{%s}{%s}' % (latex(hieu_tu_factor), latex(hieu_mau))

                # Tỉ số
                step2_ratio = '\\frac{%s}{x - %s}' % (step1_factored, latex(x0))
                step2_final = latex(ti_so_rut_gon)

                loigiai = ('''Tại $x_0 = %s$ ta có \\\\
                             $f\\left(x\\right) - f\\left(x_0\\right) = f\\left(x\\right) - f\\left(%s\\right) = %s = %s = %s$ \\\\
                             Suy ra \\\\
                             $\\frac{f\\left(x\\right) - f\\left(x_0\\right)}{x - x_0} = \\frac{f\\left(x\\right) - f\\left(%s\\right)}{x - %s} = %s \\cdot \\frac{1}{x - %s} = %s$ \\\\
                             Vậy \\\\
                             $f\'\\left(%s\\right) = \\lim_{x \\to x_0} \\frac{f\\left(x\\right) - f\\left(x_0\\right)}{x - x_0} = \\lim_{x \\to %s} \\frac{f\\left(x\\right) - f\\left(%s\\right)}{x - %s} = \\lim_{x \\to %s} %s = %s$.'''
                           % (latex(x0), 
                              latex(x0), step1_expr, step1_combined, step1_factored,
                              latex(x0), latex(x0), step1_factored, latex(x0), step2_final,
                              latex(x0), latex(x0), latex(x0), latex(x0), latex(x0), step2_final, latex(kq_value).replace('.', ',')))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + 
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content


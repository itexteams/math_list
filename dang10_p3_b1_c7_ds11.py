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


def bt_dang10_p3_b1_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':

                b = random.randint(-3, 3)
                # Đảm bảo mẫu thức tại x0 không bằng 0
                x0 = random.randint(-4, 4)
                c = random.randint(5, 10) # Chọn c lớn để mẫu x^2 + bx + c > 0

                f = 1 / (x**2 + b*x + c)
                k_val = x0**2 + b*x0 + c
                k = Rational(k_val) # f(x0) = 1/k

                tu_so = -x**2 - b*x + (k_val - c)

                x1 = -b - x0
                # tu_so = -(x - x0)(x - x1)

                f_prime_val = limit((f - 1/k)/(x - x0), x, x0)
                while f_prime_val<0:
                    b = random.randint(-3, 3)
                    # Đảm bảo mẫu thức tại x0 không bằng 0
                    x0 = random.randint(-4, 4)
                    c = random.randint(5, 10) # Chọn c lớn để mẫu x^2 + bx + c > 0

                    f = 1 / (x**2 + b*x + c)
                    k_val = x0**2 + b*x0 + c
                    k = Rational(k_val) # f(x0) = 1/k

                    tu_so = -x**2 - b*x + (k_val - c)

                    x1 = -b - x0
                    # tu_so = -(x - x0)(x - x1)

                    f_prime_val = limit((f - 1/k)/(x - x0), x, x0)        

                # Làm tròn đến hàng phần trăm theo yêu cầu
                kq_float = float(f_prime_val)
                kq_dec = Decimal(str(kq_float)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                kq_str = str(kq_dec).replace('.', ',')

                # Tạo các phương án nhiễu
                da_dung = '$%s$' % kq_str
                s = []
                offsets = [-0.1, 0.1, -0.05, 0.05, -0.2, 0.2]
                for offset in offsets:
                    nhieu = kq_dec + Decimal(str(offset))
                    nhieu_str = '$%s$' % (str(nhieu.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ','))
                    if nhieu_str != da_dung and nhieu_str not in s:
                        s.append(nhieu_str)

                random.shuffle(s)
                das1, das2, das3 = s[:3]

                # Nội dung câu hỏi
                # Sử dụng %s và latex() theo yêu cầu
                noidungcauhoi = ('''Đạo hàm của hàm số $y = f\\left(x\\right) = \\frac{1}{%s}$ tại $x_0 = %s$ bằng bao nhiêu? (Kết quả làm tròn đến hàng phần chục).'''
                                 % (latex(x**2 + b*x + c), latex(x0)))

                # Nội dung lời giải chi tiết
                # Thay thế các dấu ngoặc bằng \left( \right) và xử lý dấu phẩy thập phân
                expr_mau = x**2 + b*x + c
                expr_tu_rut_gon = tu_so # -x^2 - bx + k - c

                loigiai = ('''Tại $x_0 = %s$ ta có \\\\
                           $f\\left(x\\right) - f\\left(x_0\\right) = f\\left(x\\right) - f\\left(%s\\right) = \\frac{1}{%s} - \\frac{1}{%s} = \\frac{1}{%s} \\cdot \\frac{%s - \\left(%s\\right)}{%s}$ \\\\
                           $= \\frac{1}{%s} \\cdot \\frac{%s}{%s} = -\\frac{1}{%s} \\cdot \\frac{\\left(x - %s\\right)\\left(x - %s\\right)}{%s}$ \\\\
                           $\\frac{f\\left(x\\right) - f\\left(x_0\\right)}{x - x_0} = \\frac{f\\left(x\\right) - f\\left(%s\\right)}{x - %s} = -\\frac{1}{%s} \\cdot \\frac{\\left(x - %s\\right)\\left(x - %s\\right)}{%s} \\cdot \\frac{1}{x - %s} = -\\frac{1}{%s} \\cdot \\frac{x - %s}{%s}$ \\\\
                           $\\Rightarrow f'\\left(%s\\right) = \\lim_{x \\to x_0} \\frac{f\\left(x\\right) - f\\left(x_0\\right)}{x - x_0} = \\lim_{x \\to %s} \\left[ -\\frac{1}{%s} \\cdot \\frac{x - %s}{%s} \\right] = -\\frac{1}{%s} \\cdot \\frac{%s - %s}{%s^2 + %s \\cdot (%s) + %s} \\approx %s$.'''
                           % (latex(x0), latex(x0), latex(expr_mau), latex(k), latex(k), latex(k), latex(expr_mau), latex(expr_mau),
                              latex(k), latex(expr_tu_rut_gon), latex(expr_mau), latex(k), latex(x0), latex(x1), latex(expr_mau),
                              latex(x0), latex(x0), latex(k), latex(x0), latex(x1), latex(expr_mau), latex(x0), latex(k), latex(x1), latex(expr_mau),
                              latex(x0), latex(x0), latex(k), latex(x1), latex(expr_mau), latex(k), latex(x0), latex(x1), latex(x0), latex(b), latex(x0), latex(c), kq_str))
                dapan='\\shortans[0]{$%s$}\n'%(kq_str)
                # Đưa các đáp án vào danh sách
                da_d = ('\\True ' + str(da_dung))
                list_1 = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n').replace('+ -', '-').replace('- -', '+')
            return content      


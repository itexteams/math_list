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


def bt_dang60_p1_b2_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random hệ số a và c cho hàm số f(x) = a*x^2 + c/x
                a = random.randint(1, 3)
                b = random.randint(1, 6)
                sign = random.choice([-1, 1])
                c = sign * b

                # Random cận tích phân
                u = random.randint(1, 2)
                v = random.randint(u + 1, u + 2)

                # Khởi tạo hàm f(x)
                f_expr = a * x**2 + c / x

                # Tính giá trị chuẩn xác của tích phân: F = f(v) - f(u)
                f_u = f_expr.subs(x, u)
                f_v = f_expr.subs(x, v)
                ans_true = f_v - f_u

                # Tạo các phương án nhiễu theo yêu cầu: +1, +2, +3, -1, -2, -3
                distractor_pool = [ans_true + 1, ans_true + 2, ans_true + 3, 
                                   ans_true - 1, ans_true - 2, ans_true - 3]

                # Chọn ngẫu nhiên 3 phương án sai từ tập trên
                wrong_list = random.sample(distractor_pool, 3)

                # Hàm format LaTeX và dấu phẩy cho số thập phân (nếu có)
                def format_latex(expr):
                    return latex(expr).replace('.', ',')

                f_str = format_latex(f_expr)
                ans_str = format_latex(ans_true)
                w1_str = format_latex(wrong_list[0])
                w2_str = format_latex(wrong_list[1])
                w3_str = format_latex(wrong_list[2])

                # Câu hỏi
                noidungcauhoi = ('''Cho hàm số $f(x) = %s$. Giá trị của $\\int_{%s}^{%s} f'(x) \\text{d}x$ bằng'''
                                 % (f_str, u, v))

                # Gán các đáp án
                da_d = ('\\True $%s$' % ans_str)
                list_1 = [da_d, '$%s$' % w1_str, '$%s$' % w2_str, '$%s$' % w3_str]
                random.shuffle(list_1)

                # Hàm tạo chuỗi thế số vào hàm f(x) để lời giải hiển thị đẹp như ảnh
                def format_sub(val):
                    term1 = '%s^2' % val if a == 1 else '%s \\cdot %s^2' % (a, val)
                    if c > 0:
                        term2 = '+ \\frac{%s}{%s}' % (c, val)
                    else:
                        term2 = '- \\frac{%s}{%s}' % (abs(c), val)
                    return term1 + term2

                sub_v = format_sub(v)
                sub_u = format_sub(u)

                # Nội dung lời giải chi tiết
                loigiai = ('''Ta có: $\\int_{%s}^{%s} f'(x) \\text{d}x = f(x) \\big|_{%s}^{%s} = f(%s) - f(%s) = \\left(%s\\right) - \\left(%s\\right) = %s$.'''
                           % (u, v, u, v, v, u, sub_v, sub_u, ans_str))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content


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


def bt_dang30_p1_b2_c1_hh12(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        # Hàm biểu diễn tổ hợp tuyến tính dạng LaTeX
        def format_to_hop(k, m, n):
            res = ''
            # Hệ số của a
            if k == 1:
                res += '\\vec{a}'
            elif k == -1:
                res += '-\\vec{a}'
            elif k != 0:
                res += '%s\\vec{a}' % k
    
            # Hệ số của b
            if m == 1:
                res += ' + \\vec{b}' if res != '' else '\\vec{b}'
            elif m == -1:
                res += ' - \\vec{b}' if res != '' else '-\\vec{b}'
            elif m > 0:
                res += ' + %s\\vec{b}' % m if res != '' else '%s\\vec{b}' % m
            elif m < 0:
                res += ' - %s\\vec{b}' % (-m) if res != '' else '%s\\vec{b}' % m
    
            # Hệ số của c
            if n == 1:
                res += ' + \\vec{c}' if res != '' else '\\vec{c}'
            elif n == -1:
                res += ' - \\vec{c}' if res != '' else '-\\vec{c}'
            elif n > 0:
                res += ' + %s\\vec{c}' % n if res != '' else '%s\\vec{c}' % n
            elif n < 0:
                res += ' - %s\\vec{c}' % (-n) if res != '' else '%s\\vec{c}' % n
    
            return res
    
        # Sinh các vectơ độc lập tuyến tính (det != 0) và hệ số nguyên
        while True:
            a1, a2, a3 = [random.randint(-3, 3) for _ in range(3)]
            b1, b2, b3 = [random.randint(-3, 3) for _ in range(3)]
            c1, c2, c3 = [random.randint(-3, 3) for _ in range(3)]
            
            M = Matrix([
                [a1, b1, c1],
                [a2, b2, c2],
                [a3, b3, c3]
            ])
            if M.det() != 0 and (a1, a2, a3) != (0, 0, 0) and (b1, b2, b3) != (0, 0, 0) and (c1, c2, c3) != (0, 0, 0):
                break
    
        # Chọn nghiệm đúng (x0, y0, z0)
        x0 = random.choice([-3, -2, -1, 1, 2, 3])
        y0 = random.choice([-3, -2, -1, 1, 2, 3])
        z0 = random.choice([-3, -2, -1, 1, 2, 3])
    
        # Tọa độ vectơ u
        u1 = x0 * a1 + y0 * b1 + z0 * c1
        u2 = x0 * a2 + y0 * b2 + z0 * c2
        u3 = x0 * a3 + y0 * b3 + z0 * c3
    
        # Đáp án đúng
        da = '$\\vec{u} = %s$' % format_to_hop(x0, y0, z0)
    
        # Tạo các đáp án nhiễu
        candidates = [
            (x0, -y0, z0),
            (x0, y0, -z0),
            (-x0, y0, z0),
            (y0, x0, z0),
            (x0, -y0, -z0),
            (z0, y0, x0),
            (x0 + 1 if x0 > 0 else x0 - 1, y0, z0),
            (x0, y0 + 1 if y0 > 0 else y0 - 1, z0),
            (x0, y0, z0 + 1 if z0 > 0 else z0 - 1)
        ]
    
        s = []
        for (kx, ky, kz) in candidates:
            if (kx, ky, kz) != (x0, y0, z0):
                expr = '$\\vec{u} = %s$' % format_to_hop(kx, ky, kz)
                if expr not in s and expr != da:
                    s.append(expr)
    
        random.shuffle(s)
        das1 = s.pop()
        das2 = s.pop()
        das3 = s.pop()
    
        # Định dạng dấu số cho lời giải
        def str_coeff(val, var_name, is_first=False):
            if val == 0:
                return ''
            if is_first:
                if val == 1:
                    return var_name
                elif val == -1:
                    return '-%s' % var_name
                else:
                    return '%s%s' % (val, var_name)
            else:
                if val == 1:
                    return '+ %s' % var_name
                elif val == -1:
                    return '- %s' % var_name
                elif val > 0:
                    return '+ %s%s' % (val, var_name)
                else:
                    return '- %s%s' % (-val, var_name)
    
        eq1_str = '%s %s %s' % (str_coeff(a1, 'x', True), str_coeff(b1, 'y'), str_coeff(c1, 'z'))
        eq2_str = '%s %s %s' % (str_coeff(a2, 'x', True), str_coeff(b2, 'y'), str_coeff(c2, 'z'))
        eq3_str = '%s %s %s' % (str_coeff(a3, 'x', True), str_coeff(b3, 'y'), str_coeff(c3, 'z'))
    
        to_hop_dung = format_to_hop(x0, y0, z0)
    
        # Câu hỏi
        noidungcauhoi = ('''Trong không gian với hệ tọa độ $Oxyz$, cho các vectơ $\\vec{a}=(%s;%s;%s)$, $\\vec{b}=(%s;%s;%s)$, $\\vec{c}=(%s;%s;%s)$, $\\vec{u}=(%s;%s;%s)$. Mệnh đề nào sau đây đúng?'''
                         % (a1, a2, a3, b1, b2, b3, c1, c2, c3, u1, u2, u3)
                         )
    
        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
    
        # Đưa các đáp án vào danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
    
        # Lời giải
        loigiai = ('''Giả sử $\\vec{u} = x\\vec{a} + y\\vec{b} + z\\vec{c}$.\\\\
    Khi đó ta có hệ phương trình:\\\\
    $\\begin{cases} %s = %s \\\\ %s = %s \\\\ %s = %s \\end{cases} \\Leftrightarrow \\begin{cases} x = %s \\\\ y = %s \\\\ z = %s. \\end{cases}$\\\\
    Vậy $\\vec{u} = %s$.'''
                   % (eq1_str, u1, eq2_str, u2, eq3_str, u3, x0, y0, z0, to_hop_dung)
                   )
    
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\choice \n' +
               '{' + str(list_1[1]) + '}\n' +
               '{' + str(list_1[2]) + '}\n' +
               '{' + str(list_1[3]) + '}\n' +
               '{' + str(list_1[0]) + '}\n' +
               '\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
    
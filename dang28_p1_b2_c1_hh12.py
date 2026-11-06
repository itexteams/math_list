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


def bt_dang28_p1_b2_c1_hh12(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)

    if dang=='1':
        # Hàm xử lý chuỗi thông minh để triệt tiêu lỗi +- và số 1, -1
        def format_term(val, vec_name, is_first=False):
            if val == 0:
                return ""
            if val == 1:
                return f"\\vec{{{vec_name}}}" if is_first else f"+\\vec{{{vec_name}}}"
            if val == -1:
                return f"-\\vec{{{vec_name}}}"

            if val > 0:
                return f"{val}\\vec{{{vec_name}}}" if is_first else f"+{val}\\vec{{{vec_name}}}"
            else:
                return f"{val}\\vec{{{vec_name}}}"

        # Random các hệ số (đảm bảo khác 0)
        pool = [-4, -3, -2, -1, 1, 2, 3, 4]

        # Vector a: a2*j + a1*i
        a1 = random.choice(pool)
        a2 = random.choice(pool)

        # Vector b: b1*i + b3*k + b2*j
        b1 = random.choice(pool)
        b2 = random.choice(pool)
        b3 = random.choice(pool)

        # Vector c: c1*i + c3*k
        c1 = random.choice(pool)
        c3 = random.choice(pool)

        # Xây dựng biểu thức đề bài (lộn xộn giống bài gốc)
        bieuthuc_a = format_term(a2, 'j', True) + format_term(a1, 'i', False)
        bieuthuc_b = format_term(b1, 'i', True) + format_term(b3, 'k', False) + format_term(b2, 'j', False)
        bieuthuc_c = format_term(c1, 'i', True) + format_term(c3, 'k', False)

        # Xây dựng biểu thức chuẩn (đúng thứ tự i, j, k)
        chuan_a = format_term(a1, 'i', True) + format_term(a2, 'j', False) + "+0\\vec{k}"
        chuan_b = format_term(b1, 'i', True) + format_term(b2, 'j', False) + format_term(b3, 'k', False)
        chuan_c = format_term(c1, 'i', True) + "+0\\vec{j}" + format_term(c3, 'k', False)

        # Tọa độ đúng
        da_dung_str = "\\vec{a}=(%s;%s;0), \\vec{b}=(%s;%s;%s), \\vec{c}=(%s;0;%s)" % (a1, a2, b1, b2, b3, c1, c3)

        # Các đáp án nhiễu
        # Nhiễu 1: a bị nhầm thứ tự x, y (đọc luôn hệ số)
        da_sai1_str = "\\vec{a}=(%s;%s;0), \\vec{b}=(%s;%s;%s), \\vec{c}=(%s;0;%s)" % (a2, a1, b1, b2, b3, c1, c3)

        # Nhiễu 2: c bị nhầm y, z
        da_sai2_str = "\\vec{a}=(%s;%s;0), \\vec{b}=(%s;%s;%s), \\vec{c}=(%s;%s;0)" % (a1, a2, b1, b2, b3, c1, c3)

        # Nhiễu 3: Nhầm cả a và b (b nhầm thứ tự y, z)
        da_sai3_str = "\\vec{a}=(%s;%s;0), \\vec{b}=(%s;%s;%s), \\vec{c}=(%s;%s;0)" % (a2, a1, b1, b3, b2, c1, c3)

        # Các đáp án trắc nghiệm
        du = ['$%s$' % (da_dung_str)]
        da = random.choice(du)

        s = [
             '$%s$' % (da_sai1_str),
             '$%s$' % (da_sai2_str),
             '$%s$' % (da_sai3_str)
            ]

        das1 = s[0]
        das2 = s[1]
        das3 = s[2]

        # Câu hỏi
        noidungcauhoi = ('Trong không gian $Oxyz$, cho các vectơ $\\vec{a}=%s$, $\\vec{b}=%s$ và $\\vec{c}=%s$. Khẳng định nào sau đây đúng?' % (bieuthuc_a, bieuthuc_b, bieuthuc_c))

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2) 
        da_s3 = str(das3) 

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải
        loigiai = ('''Ta có $\\vec{a}=%s=%s \\Rightarrow \\vec{a}=(%s;%s;0)$;\\\\
                      $\\vec{b}=%s=%s \\Rightarrow \\vec{b}=(%s;%s;%s)$;\\\\
                      $\\vec{c}=%s=%s \\Rightarrow \\vec{c}=(%s;0;%s)$.'''
                   % (bieuthuc_a, chuan_a, a1, a2, 
                      bieuthuc_b, chuan_b, b1, b2, b3, 
                      bieuthuc_c, chuan_c, c1, c3))

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+ 
        '\n\\choice \n'
        '{'+str(list_1[1])+'}\n'
        '{'+str(list_1[2])+'}\n'
        '{'+str(list_1[3])+'}\n'
        '{'+str(list_1[0])+'}\n'
        '\\loigiai{'+str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content


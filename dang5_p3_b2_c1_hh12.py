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


def bt_dang5_p3_b2_c1_hh12(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)

    if dang=='1':
        # 1. Random nghiệm nguyên trước để đảm bảo kết quả luôn đẹp
        x_val = random.randint(-3, 3)
        y_val = random.randint(-3, 3)
        z_val = random.randint(-3, 3)

        # 2. Random các hệ số của phương trình (tránh hệ số 0)
        a2 = random.choice([-3, -2, -1, 2, 3])
        a3 = random.randint(-5, 5)

        b2 = random.choice([-3, -2, -1, 2, 3])
        b1 = random.randint(-5, 5)

        a5 = random.choice([-3, -2, -1, 2, 3])
        a4 = random.randint(-5, 5)

        # 3. Tính toán các hằng số còn lại để khớp với nghiệm
        # a1 = b1 + b2 * y_val
        # a2 * x_val + a3 = b3
        # a4 + a5 * z_val = b4
        a1 = b1 + b2 * y_val
        b3 = a2 * x_val + a3
        b4 = a4 + a5 * z_val

        # 4. Random hệ số của biểu thức T
        c1 = random.choice([-3, -2, -1, 1, 2, 3])
        c2 = random.choice([-3, -2, -1, 1, 2, 3])
        c3 = random.choice([-3, -2, -1, 1, 2, 3])

        # --- CÁC HÀM XỬ LÝ CHUỖI ĐỂ TRÁNH DẤU + - LỘN XỘN ---
        def fmt_ax_b(a, var, b):
            """Định dạng biểu thức ax + b"""
            s = f"{a}{var}" if abs(a) != 1 else (f"{var}" if a == 1 else f"-{var}")
            if b > 0:
                s += f" + {b}"
            elif b < 0:
                s += f" - {abs(b)}"
            return s

        def fmt_b_ax(b, a, var):
            """Định dạng biểu thức b + ax"""
            s = f"{b}"
            if a > 0:
                s += f" + {a}{var}" if a != 1 else f" + {var}"
            elif a < 0:
                s += f" - {abs(a)}{var}" if a != -1 else f" - {var}"
            return s

        def fmt_term(c, var, power, is_first=False):
            """Định dạng từng số hạng của biểu thức T"""
            if c == 0: return ""
            if is_first:
                sign = "" if c > 0 else "-"
            else:
                sign = " + " if c > 0 else " - "

            abs_c = abs(c)
            coeff_str = "" if abs_c == 1 else str(abs_c)
            var_str = var if power == 1 else f"{var}^{power}"
            return sign + coeff_str + var_str

        def get_sub_string(c, val, power):
            """Định dạng chuỗi thế số vào biểu thức T (vd: 2.(-1)^2)"""
            coeff = "" if c == 1 else ("-" if c == -1 else f"{c}.")
            val_str = f"({val})" if val < 0 else f"{val}"
            if power > 1: val_str += f"^{power}"
            if val == 0 and power == 1 and abs(c) == 1: return "0"
            return f"{coeff}{val_str}"

        # --- TẠO CHUỖI HIỂN THỊ ---
        # Tọa độ các vector
        vec_a_x = a1
        vec_a_y = fmt_ax_b(a2, 'x', a3)
        vec_a_z = fmt_b_ax(a4, a5, 'z')

        vec_b_x = fmt_b_ax(b1, b2, 'y')
        vec_b_y = b3
        vec_b_z = b4

        # Biểu thức T
        T_expr = fmt_term(c1, 'x', 1, True) + fmt_term(c2, 'y', 2, False) + fmt_term(c3, 'z', 3, False)

        # Tính giá trị kết quả T
        T_val = c1 * x_val + c2 * (y_val**2) + c3 * (z_val**3)

        # Chuỗi phép thế (Sử dụng replace để dọn dẹp các dấu cộng trừ liền nhau nếu có)
        sub_str = f"{get_sub_string(c1, x_val, 1)} + {get_sub_string(c2, y_val, 2)} + {get_sub_string(c3, z_val, 3)}".replace("+ -", "- ")

        # Đề bài
        noidungcauhoi = f"Trong không gian $Oxyz$, cho hai vecto $\\vec{{a}} = ({vec_a_x}; {vec_a_y}; {vec_a_z})$ và $\\vec{{b}} = ({vec_b_x}; {vec_b_y}; {vec_b_z})$. Khi $\\vec{{a}} = \\vec{{b}}$ thì tổng $T = {T_expr}$ bằng bao nhiêu?"

        # Nội dung lời giải
        loigiai = (f'Ta có $\\vec{{a}} = \\vec{{b}} \\Leftrightarrow \\begin{{cases}} {vec_a_x} = {vec_b_x} \\\\ '
                   f'{vec_a_y} = {vec_b_y} \\\\ {vec_a_z} = {vec_b_z} \\end{{cases}} \\Leftrightarrow '
                   f'\\begin{{cases}} y = {y_val} \\\\ x = {x_val} \\\\ z = {z_val} \\end{{cases}}$ \\\\\n'
                   f'$\\Rightarrow T = {sub_str} = {T_val}$.')
        #Đáp án
        dapan='\\shortans[0]{$%s$}\n'%(latex(T_val))

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac')
    return content


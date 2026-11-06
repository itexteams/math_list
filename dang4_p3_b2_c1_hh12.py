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


def bt_dang4_p3_b2_c1_hh12(self):
    # Hàm định dạng số hiển thị trong LaTeX (đổi dấu chấm sang dấu phẩy)
    def fmt(num):
        return str(num).replace('.', ',')

    # Hàm định dạng phép cộng/trừ trong phân số LaTeX
    def fmt_add(var_str, val):
        if val >= 0:
            return f"{var_str} + {val}"
        else:
            return f"{var_str} - {abs(val)}"

    # Hàm định dạng biểu thức T = m*a + n*b + p*c
    def build_T_latex(m, n, p):
        terms = []
        if m == 1: terms.append("a")
        elif m == -1: terms.append("-a")
        else: terms.append(f"{m}a")

        if n == 1: terms.append("+ b")
        elif n == -1: terms.append("- b")
        elif n > 0: terms.append(f"+ {n}b")
        else: terms.append(f"- {abs(n)}b")

        if p == 1: terms.append("+ c")
        elif p == -1: terms.append("- c")
        elif p > 0: terms.append(f"+ {p}c")
        else: terms.append(f"- {abs(p)}c")

        return " ".join(terms)

    # Hàm định dạng bước tính toán thay số cho T
    def build_T_calc(m, n, p, a, b, c):
        def fmt_term(coeff, val, is_first=False):
            if is_first:
                if coeff == 1: return f"{val}"
                elif coeff == -1: return f"(-{val})" if val < 0 else f"-{val}"
                else: return f"{coeff} \\cdot ({val})" if val < 0 else f"{coeff} \\cdot {val}"
            else:
                if coeff == 1: return f"+ ({val})" if val < 0 else f"+ {val}"
                elif coeff == -1: return f"- ({val})" if val < 0 else f"- {val}"
                elif coeff > 0: return f"+ {coeff} \\cdot ({val})" if val < 0 else f"+ {coeff} \\cdot {val}"
                else: return f"- {abs(coeff)} \\cdot ({val})" if val < 0 else f"- {abs(coeff)} \\cdot {val}"

        t1 = fmt_term(m, a, is_first=True)
        t2 = fmt_term(n, b, is_first=False)
        t3 = fmt_term(p, c, is_first=False)
        return f"{t1} {t2} {t3}"

    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        while True:
            # Tọa độ điểm A và B
            xa = random.randint(-8, 8)
            ya = random.randint(-8, 8)
            za = random.randint(-8, 8)
            xb = random.randint(-8, 8)
            yb = random.randint(-8, 8)
            zb = random.randint(-8, 8)

            # Đảm bảo các tọa độ không bằng 0
            if xa == 0 or ya == 0 or za == 0 or xb == 0 or yb == 0 or zb == 0:
                continue

            # Tìm tọa độ C(a; b; c)
            a = -xa
            c = -za
            b = -yb

            # Kiểm tra điều kiện 3 điểm A, B, C không thẳng hàng
            vAB = (xb - xa, yb - ya, zb - za)
            vAC = (-2*xa, -yb - ya, -2*za)

            cross_x = vAB[1]*vAC[2] - vAB[2]*vAC[1]
            cross_y = vAB[2]*vAC[0] - vAB[0]*vAC[2]
            cross_z = vAB[0]*vAC[1] - vAB[1]*vAC[0]

            if cross_x == 0 and cross_y == 0 and cross_z == 0:
                continue

            # Biểu thức T = m*a + n*b + p*c
            m = random.choice([1, 2, 3])
            n = random.choice([-2, -1, 1, 2])
            p = random.choice([-2, -1, 1, 2])

            T_val = m*a + n*b + p*c
            break

        T_expr_latex = build_T_latex(m, n, p)
        T_calc_str = build_T_calc(m, n, p, a, b, c)

        # Đáp án đúng
        kq = fmt(T_val)
        du = ['$%s$' % (kq)]
        da = random.choice(du)

        # Sinh các phương án sai không trùng nhau và không trùng đáp án đúng
        wrong_set = set()
        # Lỗi sai đổi dấu
        wrong_set.add(m*xa + n*yb + p*za)
        wrong_set.add(m*xa - n*yb + p*za)
        # Lỗi lệch kết quả
        for offset in [1, -1, 2, -2, 3, -3, 4, -4]:
            wrong_set.add(T_val + offset)
        if -T_val != T_val:
            wrong_set.add(-T_val)

        # Lọc bỏ đáp án đúng khỏi tập phương án sai
        wrong_set.discard(T_val)

        s = ['$%s$' % (fmt(v)) for v in wrong_set]
        random.shuffle(s)

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Trong không gian $Oxyz$, cho tam giác $ABC$ có $A(%s; %s; %s)$, $B(%s; %s; %s)$ và $C(a; b; c)$. Biết trung điểm cạnh $AC$ thuộc trục tung, trung điểm cạnh $BC$ thuộc mặt phẳng $(Oxz)$. Tổng $T = %s$ bằng bao nhiêu?'''
                         % (fmt(xa), fmt(ya), fmt(za), fmt(xb), fmt(yb), fmt(zb), T_expr_latex))

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        # Trộn ngẫu nhiên các đáp án
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Lời giải chi tiết
        loigiai = ('''Gọi $M$ là trung điểm của cạnh $AC$, ta có $M\\left(\\frac{%s}{2}; \\frac{%s}{2}; \\frac{%s}{2}\\right)$. \\\\
                 Vì $M$ thuộc trục tung $Oy$ nên $x_M = 0$ và $z_M = 0$, suy ra: \\\\
                 $\\begin{cases} \\frac{%s}{2} = 0 \\\\ \\frac{%s}{2} = 0 \\end{cases} \\Leftrightarrow \\begin{cases} a = %s \\\\ c = %s. \\end{cases}$ \\\\
                 Gọi $N$ là trung điểm của cạnh $BC$, ta có $N\\left(\\frac{%s}{2}; \\frac{%s}{2}; \\frac{%s}{2}\\right)$. \\\\
                 Vì $N$ thuộc mặt phẳng $(Oxz)$ nên $y_N = 0$, suy ra: \\\\
                 $\\frac{%s}{2} = 0 \\Leftrightarrow b = %s$. \\\\
                 Từ đó ta có tọa độ điểm $C(%s; %s; %s)$. \\\\
                 Thay $a = %s$, $b = %s$, $c = %s$ vào $T = %s$ ta được: \\\\
                 $T = %s = %s$.'''
                 % (fmt_add("a", xa), fmt_add("b", ya), fmt_add("c", za),
                    fmt_add("a", xa), fmt_add("c", za), fmt(a), fmt(c),
                    fmt_add("a", xb), fmt_add("b", yb), fmt_add("c", zb),
                    fmt_add("b", yb), fmt(b),
                    fmt(a), fmt(b), fmt(c),
                    fmt(a), fmt(b), fmt(c), T_expr_latex,
                    T_calc_str, fmt(T_val)))
    dapan='\\shortans[0]{$%s$}\n'%(fmt(T_val))
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
        '\\loigiai{' + str(loigiai) + '}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content


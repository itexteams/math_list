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


def bt_dang34_p2_b2_c3_ds12(self):
    # ================= Khởi tạo và sinh dữ liệu ngẫu nhiên =================

    while True:
        # Chọn I1 là một phân số hữu tỉ (dạng k/2 hoặc nguyên), I2 là số nguyên
        t1_num = random.choice([-9, -7, -5, -3, -1, 1, 3, 5, 7, 9])
        I1 = Rational(t1_num, 2)
        I2 = Rational(random.randint(-5, 5), 1)

        # Random giá trị F(0)
        F0 = random.randint(-4, 4)


        val_2a_b = I2 - 2 * I1
        val_6c = 6 * I1  # khi 2a + 3b = ...
        break

    # Tính giá trị F(2) đúng:
    F2_true = F0 + I2
    F2_false = F2_true + random.choice([-2, -1, 1, 2])

    # Giá trị đúng của F(1) - F(0) là I1
    I1_tex = latex(I1)
    I2_tex = latex(I2)

    noidungcauhoi = ('''Biết rằng hàm số $f(x) = ax^2 + bx + c$ thỏa mãn $\\int_0^1 f(x) \\mathrm{d}x = %s$, $\\int_0^2 f(x) \\mathrm{d}x = %s$ và $F(x)$ là một nguyên hàm của hàm số $f(x)$ trên đoạn $[0; 2]$.''' % (I1_tex, I2_tex))

    #########################################################################
    # Khẳng định a: F(1) - F(0) = I1
    # Đúng theo định nghĩa tích phân Newton-Leibniz: \int_0^1 f(x)dx = F(1) - F(0)
    #########################################################################
    da_a_d = '\\True $F(1) - F(0) = %s$' % (I1_tex)
    da_a_s = '$F(1) - F(0) = %s$' % (latex(-I1))
    list_da_a = [da_a_d, da_a_s]
    da_a = random.choice(list_da_a)
    list_a_1 = [da_a]

    loigiai_a = ('''Theo định nghĩa tích phân, vì $F(x)$ là một nguyên hàm của $f(x)$ trên $[0; 2]$ nên:\\\\ $\\int_0^1 f(x) \\mathrm{d}x = F(1) - F(0) = %s$.''' % (I1_tex))
    list_a_2 = [loigiai_a]

    combined_a = list(zip(list_a_1, list_a_2))
    random.shuffle(combined_a)
    shuffled_answers_a, shuffled_solutions_a = zip(*combined_a)

    #########################################################################
    # Khẳng định b: Cho F(0) = k thì khi đó F(2) = ...
    # Ta có \int_0^2 f(x)dx = F(2) - F(0) = I2 => F(2) = F(0) + I2
    #########################################################################
    da_b_d = '\\True Cho $F(0) = %s$ thì khi đó $F(2) = %s$' % (latex(F0), latex(F2_true))
    da_b_s = 'Cho $F(0) = %s$ thì khi đó $F(2) = %s$' % (latex(F0), latex(F2_false))
    list_da_b = [da_b_d, da_b_s]
    da_b = random.choice(list_da_b)
    list_b_1 = [da_b]

    loigiai_b = ('''Ta có $\\int_0^2 f(x) \\mathrm{d}x = F(2) - F(0) \\Leftrightarrow F(2) = F(0) + \\int_0^2 f(x) \\mathrm{d}x$.\\\\ Với $F(0) = %s$ và $\\int_0^2 f(x) \\mathrm{d}x = %s$, suy ra $F(2) = %s + (%s) = %s$.''' % (latex(F0), I2_tex, latex(F0), I2_tex, latex(F2_true)))
    list_b_2 = [loigiai_b]

    combined_b = list(zip(list_b_1, list_b_2))
    random.shuffle(combined_b)
    shuffled_answers_b, shuffled_solutions_b = zip(*combined_b)

    #########################################################################
    # Khẳng định c: Công thức nguyên hàm \int f(x)dx = \frac{a}{3}x^3 + \frac{b}{2}x^2 + cx
    # Khẳng định này thiếu hằng số C nên SAI!
    #########################################################################
    # Đáp án sai khi không có hằng số C
    da_c_s = '$\\int f(x) \\mathrm{d}x = \\int (ax^2 + bx + c) \\mathrm{d}x = \\frac{a}{3}x^3 + \\frac{b}{2}x^2 + cx$'
    # Đáp án đúng nếu có hằng số C
    da_c_d = '\\True $\\int f(x) \\mathrm{d}x = \\int (ax^2 + bx + c) \\mathrm{d}x = \\frac{a}{3}x^3 + \\frac{b}{2}x^2 + cx + C$ ($C \\in \\mathbb{R}$)'
    list_da_c = [da_c_d, da_c_s]
    da_c = random.choice(list_da_c)
    list_c_1 = [da_c]

    loigiai_c = ('''Ta có họ nguyên hàm của hàm số $f(x) = ax^2 + bx + c$ là:\\\\ $\\int f(x) \\mathrm{d}x = \\int (ax^2 + bx + c) \\mathrm{d}x = \\frac{a}{3}x^3 + \\frac{b}{2}x^2 + cx + C$ với $C \\in \\mathbb{R}$.\\\\ Khẳng định không có hằng số cộng $C$ là khẳng định sai.''' )
    list_c_2 = [loigiai_c]

    combined_c = list(zip(list_c_1, list_c_2))
    random.shuffle(combined_c)
    shuffled_answers_c, shuffled_solutions_c = zip(*combined_c)

    #########################################################################
    # Khẳng định d: Mối liên hệ giữa các hệ số a, b, c
    # \int_0^1 f(x)dx = a/3 + b/2 + c = I1 <=> 2a + 3b + 6c = 6*I1
    # \int_0^2 f(x)dx = 8a/3 + 2b + 2c = I2 <=> 8a + 6b + 6c = 3*I2
    # Suy ra: (8a + 6b + 6c) - (2a + 3b + 6c) = 6a + 3b = 3*I2 - 6*I1 <=> 2a + b = I2 - 2*I1
    #########################################################################
    val_d_true = val_2a_b
    val_d_false = val_d_true + random.choice([-3, -2, -1, 1, 2, 3])

    da_d_d = '\\True $2a + b = %s$' % (latex(val_d_true))
    da_d_s = '$2a + b = %s$' % (latex(val_d_false))
    list_da_d = [da_d_d, da_d_s]
    da_d = random.choice(list_da_d)
    list_d_1 = [da_d]

    loigiai_d = ('''Từ giả thiết ta có:\\\\ $\\int_0^1 f(x) \\mathrm{d}x = \\left. \\left( \\frac{a}{3}x^3 + \\frac{b}{2}x^2 + cx \\right) \\right|_0^1 = \\frac{a}{3} + \\frac{b}{2} + c = %s \\Leftrightarrow 2a + 3b + 6c = %s$.\\\\ $\\int_0^2 f(x) \\mathrm{d}x = \\left. \\left( \\frac{a}{3}x^3 + \\frac{b}{2}x^2 + cx \\right) \\right|_0^2 = \\frac{8a}{3} + 2b + 2c = %s \\Leftrightarrow 8a + 6b + 6c = %s$.\\\\ Trừ vế theo vế hai phương trình ta được:\\\\ $(8a + 6b + 6c) - (2a + 3b + 6c) = %s - (%s) \\Leftrightarrow 6a + 3b = %s \\Leftrightarrow 2a + b = %s$.''' % (I1_tex, latex(6*I1), I2_tex, latex(3*I2), latex(3*I2), latex(6*I1), latex(3*I2 - 6*I1), latex(val_d_true)))
    list_d_2 = [loigiai_d]

    combined_d = list(zip(list_d_1, list_d_2))
    random.shuffle(combined_d)
    shuffled_answers_d, shuffled_solutions_d = zip(*combined_d)

    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)

    # Lặp đến khi có từ 1 đến 3 đáp án đúng
    while True:
        da_a = random.choice(list_da_a)
        da_b = random.choice(list_da_b)
        da_c = random.choice(list_da_c)
        da_d = random.choice(list_da_d)

        answers = [da_a, da_b, da_c, da_d]
        true_count = count_true_answers(answers)

        if 1 <= true_count <= 3:
            break

    # Gán lại vào list
    list_a_1 = [da_a]
    list_b_1 = [da_b]
    list_c_1 = [da_c]
    list_d_1 = [da_d]

    combined_a = list(zip(list_a_1, list_a_2))
    combined_b = list(zip(list_b_1, list_b_2))
    combined_c = list(zip(list_c_1, list_c_2))
    combined_d = list(zip(list_d_1, list_d_2))

    random.shuffle(combined_a)
    random.shuffle(combined_b)
    random.shuffle(combined_c)
    random.shuffle(combined_d)

    shuffled_answers_a, shuffled_solutions_a = zip(*combined_a)
    shuffled_answers_b, shuffled_solutions_b = zip(*combined_b)
    shuffled_answers_c, shuffled_solutions_c = zip(*combined_c)
    shuffled_answers_d, shuffled_solutions_d = zip(*combined_d)

    # Xuất câu hỏi với định dạng LaTeX theo mẫu
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
               '\\choiceTFn \n'
               '{' + str(shuffled_answers_a[0]) + '}\n'
               '{' + str(shuffled_answers_b[0]) + '}\n'
               '{' + str(shuffled_answers_c[0]) + '}\n'
               '{' + str(shuffled_answers_d[0]) + '}\n'
               '\\loigiai{ \n'
               '\\begin{enumEX}[a)]{1} \n'
               '\\item ' + str(shuffled_solutions_a[0]) + '\n'
               '\\item ' + str(shuffled_solutions_b[0]) + '\n'
               '\\item ' + str(shuffled_solutions_c[0]) + '\n'
               '\\item ' + str(shuffled_solutions_d[0]) + '\n'
               '\\end{enumEX}} \n'
               '\\end{ex}\n \\end{minipage}\n\n')
    return content


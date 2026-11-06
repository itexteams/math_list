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


def bt_dang26_p2_b2_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            x = symbols('x')

            # --- BƯỚC 1: TẠO DỮ LIỆU NGẪU NHIÊN CHO BÀI TOÁN ---
            # Giả sử kết quả tích phân của f và g là các số hữu tỷ đẹp để dễ tính toán
            # A = tích phân f từ -2 đến 1, B = tích phân g từ -2 đến 1
            A_val = Rational(random.randint(2, 5)) 
            B_val = Rational(random.randint(3, 6))

            # Hệ số trong đề bài (giữ giống cấu trúc ảnh hoặc random nhẹ)
            c1, c2 = 2, -1  # 2f(x) - g(x)
            c3, c4 = 3, 5   # 3f(x) + 5g(x)

            # Tính các hằng số ở vế phải đề bài
            k1 = c1 * A_val + c2 * B_val
            k2 = c3 * A_val + c4 * B_val

            # Nội dung câu hỏi gốc
            noidungcauhoi = ('''Cho các tích phân sau: $\\int_{-2}^{1} [%s f(x) %s g(x)] \\mathrm{d}x = %s$ và $\\int_{-2}^{1} [%s g(x) + %s f(x)] \\mathrm{d}x = %s$.''' 
                             % (c1, '-' if c2 < 0 else '+', k1, c4, c3, k2))

            # --- BƯỚC 2: TÍNH TOÁN LỜI GIẢI CHI TIẾT ---
            # Giải hệ phương trình để tìm A_val và B_val (trong lời giải)
            loigiai_he = ('''Đặt $I_f = \\int_{-2}^1 f(x) \\mathrm{d}x$ và $I_g = \\int_{-2}^1 g(x) \\mathrm{d}x$. \\\\
            Từ giả thiết ta có hệ phương trình:
            $\\begin{cases} %s I_f - I_g = %s \\\\ %s I_f + %s I_g = %s \\end{cases} \\Leftrightarrow \\begin{cases} I_f = %s \\\\ I_g = %s \\end{cases}$.'''
            %(c1, k1, c3, c4, k2, latex(A_val), latex(B_val)))

            ########################################################################
            # a) Kiểm tra tích phân f
            da_a_d = '\\True $\\int_{-2}^{1} f(x) \\mathrm{d}x = %s$' % (latex(A_val))
            da_a_s = '$\\int_{-2}^{1} f(x) \\mathrm{d}x = %s$' % (latex(A_val + random.choice([-1, 1])))
            list_da_a = [da_a_d, da_a_s]
            nb_da_1 = random.choice(list_da_a)
            loigiai_a = "Dựa vào hệ phương trình đã giải, ta có $I_f = %s$." % (latex(A_val))

            ########################################################################
            # b) Kiểm tra tích phân g
            da_b_d = '\\True $\\int_{-2}^{1} g(x) \\mathrm{d}x = %s$' % (latex(B_val))
            da_b_s = '$\\int_{-2}^{1} g(x) \\mathrm{d}x = \\frac{%s}{%s}$' % (random.randint(40, 50), random.randint(11, 15))
            list_da_b = [da_b_d, da_b_s]
            th_da_1 = random.choice(list_da_b)
            loigiai_b = "Dựa vào hệ phương trình đã giải, ta có $I_g = %s$." % (latex(B_val))

            ########################################################################
            # c) Tìm tham số a
            # Tích phân (f + ax - 2) từ -2 đến 1
            # = I_f + a*[x^2/2] - [2x] = A_val + a*(1/2 - 2) - (2 - (-4)) = A_val - 1.5a - 6
            k3 = 1 # Kết quả giả thiết cho bằng 1
            # Giải: A_val - 1.5*a - 6 = 1 => 1.5*a = A_val - 7 => a = (A_val - 7) / 1.5
            a_sym = symbols('a')
            eq_c = A_val + a_sym * (Rational(1,2) - 2) - 6 - k3
            a_sol = solve(eq_c, a_sym)[0]

            khoang_dung = "(%s; %s)" % (int(a_sol)-1, int(a_sol)+1)
            khoang_sai = "(0; 5)"
            da_c_d = '\\True Biết rằng $\\int_{-2}^{1} [f(x) + ax - 2] = %s$, giá trị của tham số $a$ thỏa mãn thuộc khoảng $%s$' % (k3, khoang_dung)
            da_c_s = 'Biết rằng $\\int_{-2}^{1} [f(x) + ax - 2] = %s$, giá trị của tham số $a$ thỏa mãn thuộc khoảng $%s$' % (k3, khoang_sai)
            list_da_c = [da_c_d, da_c_s]
            vd_da_1 = random.choice(list_da_c)

            loigiai_c = ('''Ta có $\\int_{-2}^{1} [f(x) + ax - 2] \\mathrm{d}x = 1 \\Leftrightarrow \\int_{-2}^{1} f(x) \\mathrm{d}x + a \\int_{-2}^{1} x \\mathrm{d}x - \\int_{-2}^{1} 2 \\mathrm{d}x = 1$ \\\\
            $\\Leftrightarrow %s + a \\cdot \\left[ \\frac{x^2}{2} \\right]_{-2}^1 - [2x]_{-2}^1 = 1 \\Leftrightarrow %s - \\frac{3}{2}a - 6 = 1 \\Leftrightarrow a = %s$. \\\\
            Vì $a = %s$ nên $a \\in %s$.'''
            %(latex(A_val), latex(A_val), latex(a_sol), latex(a_sol), khoang_dung))

            ########################################################################
            # d) Tách tích phân
            # Giả sử tích phân từ -2 đến 0 của (f+g) là m
            m_val = random.randint(-5, -1)
            # Tính tích phân từ 0 đến 1 của (f+g) = (A + B) - m
            target_d = (A_val + B_val) - m_val

            da_d_d = '\\True Nếu $\\int_{-2}^{0} [f(x) + g(x)] \\mathrm{d}x = %s$ thì $\\int_{0}^{1} [f(x) + g(x)] \\mathrm{d}x$ bằng $%s$' % (m_val, target_d)
            da_d_s = 'Nếu $\\int_{-2}^{0} [f(x) + g(x)] \\mathrm{d}x = %s$ thì $\\int_{0}^{1} [f(x) + g(x)] \\mathrm{d}x$ bằng $%s$' % (m_val, target_d + random.randint(1, 5))
            list_da_d = [da_d_d, da_d_s]
            vdc_da_1 = random.choice(list_da_d)

            loigiai_d = ('''Ta có $\\int_{-2}^{1} [f(x) + g(x)] \\mathrm{d}x = \\int_{-2}^{1} f(x) \\mathrm{d}x + \\int_{-2}^{1} g(x) \\mathrm{d}x = %s + %s = %s$. \\\\
            Mà $\\int_{-2}^{1} [f(x) + g(x)] \\mathrm{d}x = \\int_{-2}^{0} [f(x) + g(x)] \\mathrm{d}x + \\int_{0}^{1} [f(x) + g(x)] \\mathrm{d}x$ \\\\
            $\\Rightarrow \\int_{0}^{1} [f(x) + g(x)] \\mathrm{d}x = %s - (%s) = %s$.'''
            %(latex(A_val), latex(B_val), latex(A_val + B_val), latex(A_val + B_val), m_val, latex(target_d)))

            # --- BƯỚC 3: XỬ LÝ ĐÁP ÁN ĐÚNG/SAI VÀ XUẤT NỘI DUNG ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                d1 = random.choice(list_da_a)
                d2 = random.choice(list_da_b)
                d3 = random.choice(list_da_c)
                d4 = random.choice(list_da_d)
                if 1 <= count_true_answers([d1, d2, d3, d4]) <= 3:
                    shuffled_answers = [d1, d2, d3, d4]
                    shuffled_solutions = [loigiai_a, loigiai_b, loigiai_c, loigiai_d]
                    break

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
                '{'+str(shuffled_answers[0])+'}\n'
                '{'+str(shuffled_answers[1])+'}\n'
                '{'+str(shuffled_answers[2])+'}\n'
                '{'+str(shuffled_answers[3])+'}\n'
                '\\loigiai{ \n'
                + str(loigiai_he) + '\\\\ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions[0])+'\n'
                '\\item '+str(shuffled_solutions[1])+'\n'
                '\\item '+str(shuffled_solutions[2])+'\n'
                '\\item '+str(shuffled_solutions[3])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


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


def bt_dang26_p1_b3_c3_hh10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random các tham số
                # Chọn m từ 3 đến 6 để tránh các trường hợp mẫu số bằng 0 hoặc nghiệm t2 vô tình là số nguyên
                m = random.choice([3, 4, 5, 6]) 
                n = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
                k = random.randint(1, 8)

                # Tính toán các hệ số để phương trình có nghiệm đẹp (t = 0)
                c1 = 5 * k - 3 * n
                c2 = c1 - n

                A = 3 * m + 4
                C = 4 * m - 3
                B = 5 * k

                # Tính toán nghiệm t2 (đường tròn thứ hai không nguyên)
                t2 = Rational(-2 * B, A + C)
                x_I2 = m * t2 + n
                y_I2 = t2
                R_2 = Abs(A * t2 + B) / 5
                R_2_sq = R_2**2

                # Các hàm hỗ trợ định dạng chuỗi, tự động xử lý dấu
                def format_I_t(m, n):
                    if n > 0: return f"{m}t + {n}"
                    elif n < 0: return f"{m}t - {-n}"
                    else: return f"{m}t"

                def format_poly_t(a, b):
                    if b > 0: return f"{a}t + {b}"
                    elif b < 0: return f"{a}t - {-b}"
                    else: return f"{a}t"

                def format_squared_term(var, val):
                    if val == 0: return f"{var}^2"
                    elif val > 0: return f"({var} - {sp.latex(val)})^2"
                    else: return f"({var} + {sp.latex(sp.Abs(val))})^2"

                def format_x_n(n):
                    if n > 0: return f"(x - {n})^2"
                    else: return f"(x + {abs(n)})^2"

                def format_x_plus_n(n):
                    if n > 0: return f"(x + {n})^2"
                    else: return f"(x - {abs(n)})^2"

                def format_y_n(n):
                    if n > 0: return f"(y - {n})^2"
                    else: return f"(y + {abs(n)})^2"

                # Khởi tạo các biến sympy để format phương trình đường thẳng d, d1, d2
                sym_x, sym_y = sp.symbols('x y')
                d_eq = sp.latex(sym_x - m*sym_y - n) + " = 0"
                d1_eq = sp.latex(3*sym_x + 4*sym_y + c1) + " = 0"
                d2_eq = sp.latex(4*sym_x - 3*sym_y + c2) + " = 0"

                term_x2 = format_squared_term("x", x_I2)
                term_y2 = format_squared_term("y", y_I2)

                # Các đáp án trắc nghiệm
                da = f"{format_x_n(n)} + y^2 = {k**2}"
                das1 = f"{format_x_plus_n(n)} + y^2 = {k**2}"
                das2 = f"{format_x_n(n)} + y^2 = {k}"
                das3 = f"x^2 + {format_y_n(n)} = {k**2}"

                # Câu hỏi
                noidungcauhoi = (f"Trong mặt phẳng $Oxy$, cho đường thẳng $d: {d_eq}$. "
                                 f"Phương trình đường tròn $(C)$ có tâm thuộc $d$, đồng thời tiếp xúc với "
                                 f"$\\Delta_1: {d1_eq}$ và $\\Delta_2: {d2_eq}$, biết tâm đường tròn có tọa độ nguyên là")

                da_d = "\\True $" + da + "$"
                da_s1 = "$" + das1 + "$"
                da_s2 = "$" + das2 + "$"
                da_s3 = "$" + das3 + "$"

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Các biểu thức dùng trong lời giải
                num1 = format_poly_t(A, B)
                num2 = format_poly_t(C, B)

                # Nội dung lời giải
                loigiai = (f"Gọi $I({format_I_t(m, n)}; t) \\in d$ ta có:\\\\\n"
                           f"    $d(I, \\Delta_1) = d(I, \\Delta_2) \\Leftrightarrow \\frac{{|{num1}|}}{{5}} = \\frac{{|{num2}|}}{{5}} \\Leftrightarrow t = 0$ hoặc $t = {sp.latex(t2)}$.\\\\\n"
                           f"    - Với $t = 0$ suy ra $I({n}; 0)$, $R = {k}$.\\\\\n"
                           f"    Phương trình $(C): {format_x_n(n)} + y^2 = {k**2}$.\\\\\n"
                           f"    - Với $t = {sp.latex(t2)}$ suy ra $I\\left({sp.latex(x_I2)}; {sp.latex(y_I2)}\\right)$, $R = {sp.latex(R_2)}$.\\\\\n"
                           f"    Phương trình $(C): {term_x2} + {term_y2} = {sp.latex(R_2_sq)}$.\\\\\n"
                           f"    Vì tâm đường tròn có tọa độ nguyên nên phương trình $(C)$ thỏa mãn là $(x - {n})^2 + y^2 = {k**2}$.")

                # Xử lý triệt để hiển thị dấu + - thành - và - - thành + (Guard rails)
                noidungcauhoi = noidungcauhoi.replace('+ -', '- ').replace('- -', '+ ')
                loigiai = loigiai.replace('+ -', '- ').replace('- -', '+ ')

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


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


def bt_dang28_p1_b1_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random nghiệm x1, x2 để đảm bảo phương trình luôn có 2 nghiệm nguyên phân biệt đẹp
                while True:
                    a = random.choice([-2, -1, 1, 2])
                    x1 = random.choice([-3, -2, -1, 1, 2, 3])
                    # Đảm bảo x1 và x2 cùng tính chẵn lẻ để hệ số b luôn nguyên
                    x2 = x1 + random.choice([2, 4]) 
                    if x1 != 0 and x2 != 0:
                        break

                # Tính toán các hệ số dựa trên x1, x2
                b = -3 * a * (x1 + x2) // 2
                m = 3 * a * x1 * x2
                d_val = random.randint(-5, 5)
                M_val = random.choice([2017, 2020, 2022, 2023, 2024, 2025])

                # Thiết lập hàm số và đạo hàm
                x_sym = sp.Symbol('x')
                y_func = a*x_sym**3 + b*x_sym**2 + d_val
                y_expr = sp.latex(y_func)

                y_prime = sp.diff(y_func, x_sym)
                y_prime_expr = sp.latex(y_prime)

                # Xử lý hiển thị phân số của hệ số góc đường thẳng
                if m == 1:
                    line_expr = f"x + {M_val}"
                    fraction_m_expr = "1"
                elif m == -1:
                    line_expr = f"-x + {M_val}"
                    fraction_m_expr = "-1"
                elif m < 0:
                    line_expr = f"-\\frac{{1}}{{{-m}}}x + {M_val}"
                    fraction_m_expr = f"-\\frac{{1}}{{{-m}}}"
                else:
                    line_expr = f"\\frac{{1}}{{{m}}}x + {M_val}"
                    fraction_m_expr = f"\\frac{{1}}{{{m}}}"

                # Phương trình hoành độ
                eq_left = 3*a*x_sym**2 + 2*b*x_sym + m
                eq_left_expr = sp.latex(eq_left).replace('x', 'x_0')

                # Tính tung độ tiếp điểm
                y1 = a*x1**3 + b*x1**2 + d_val
                y2 = a*x2**3 + b*x2**2 + d_val

                # Hệ số c của phương trình tiếp tuyến y = -mx + c
                c1 = m*x1 + y1
                c2 = m*x2 + y2

                # Các hàm hỗ trợ format dấu hiển thị
                def format_sign(num):
                    if num == 0: return ""
                    return f" + {num}" if num > 0 else f" - {abs(num)}"

                def format_x_minus(num):
                    return f"x - {num}" if num > 0 else f"x + {-num}" if num < 0 else "x"

                def format_line(slope, intercept):
                    if slope == 0: return str(intercept)
                    slope_str = str(slope)
                    if slope == 1: slope_str = ""
                    if slope == -1: slope_str = "-"
                    if intercept > 0: return f"{slope_str}x + {intercept}"
                    elif intercept < 0: return f"{slope_str}x - {-intercept}"
                    else: return f"{slope_str}x"

                m_str = f"{-m}"
                if -m == 1: m_str = ""
                if -m == -1: m_str = "-"

                # Phương trình tiếp tuyến dạng chưa rút gọn
                inter1 = f"y = {m_str}({format_x_minus(x1)}){format_sign(y1)}"
                inter2 = f"y = {m_str}({format_x_minus(x2)}){format_sign(y2)}"

                # Phương trình tiếp tuyến dạng cuối cùng y = ax + b (tự format tránh sympy đảo thứ tự)
                final1 = format_line(-m, c1)
                final2 = format_line(-m, c2)

                # Câu hỏi
                noidungcauhoi = f"Cho hàm số $y = {y_expr}$ có đồ thị $(C)$. Số tiếp tuyến của $(C)$ vuông góc với đường thẳng $y = {line_expr}$ là"

                # Các đáp án
                da_d = '\\True 2'
                da_s1 = '1'
                da_s2 = '0'
                da_s3 = '3'

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = f"""Gọi $(x_0; y_0)$ là tọa độ tiếp điểm.\\\\
            Ta có $y' = {y_prime_expr}$.\\\\
            Vì tiếp tuyến của $(C)$ vuông góc với đường thẳng $y = {line_expr}$ nên\\\\
            $y'(x_0) \\cdot \\left({fraction_m_expr}\\right) = -1 \\Leftrightarrow y'(x_0) = {-m} \\Leftrightarrow {eq_left_expr} = 0 \\Leftrightarrow \\left[ \\begin{{array}}{{l}} x_0 = {x1} \\\\ x_0 = {x2} \\end{{array}} \\right.$.\\\\
            Với $x_0 = {x1} \\Rightarrow y_0 = {y1}$, suy ra PTTT là: ${inter1} \\Leftrightarrow y = {final1}$.\\\\
            Với $x_0 = {x2} \\Rightarrow y_0 = {y2}$, suy ra PTTT là: ${inter2} \\Leftrightarrow y = {final2}$."""

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


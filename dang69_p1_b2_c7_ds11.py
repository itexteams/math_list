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


def bt_dang69_p1_b2_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            def format_coeff(val, is_first=False):
                """Hàm xử lý hiển thị dấu và hệ số nối tiếp"""
                if is_first:
                    return f"{val}"
                return f"+ {val}" if val > 0 else f"- {abs(val)}"

            # B1: Random hệ số (cả dấu)
            a = random.choice([i for i in range(-15, 16) if i != 0])
            b = random.choice([i for i in range(-15, 16) if i != 0])
            c = random.choice([i for i in range(-15, 16) if i != 0])
            n = random.randint(2, 6)

            # B2: Xử lý hiển thị đề bài
            # y = a*cot(x) + b*e^x + c*x^n
            f_latex = f"y = {a} \\cot x {format_coeff(b)} e^x {format_coeff(c)} x^{n}"

            # B3: Xử lý Đạo hàm đúng (Ép kiểu hiển thị -1/sin^2 x)
            # Đạo hàm của a*cot(x) là -a/sin^2(x)
            # Ta xử lý dấu của a để hiển thị đúng: nếu a=5 -> -5/sin^2, nếu a=-5 -> 5/sin^2
            prefix_a = "" if a < 0 else "-"
            abs_a = abs(a)
            part_cot = f"{prefix_a} \\frac{{{abs_a}}}{{\\sin^2 x}}"

            # Các phần còn lại
            part_exp = f"{format_coeff(b)} e^x"
            part_xn = f"{format_coeff(c*n)} x^{n-1}"

            da_dung_str = f"y' = {part_cot} {part_exp} {part_xn}"
            da_dung_str = da_dung_str.replace("+ -", "- ").replace("- -", "+ ") # Dọn dẹp dấu

            # B4: Tạo các đáp án nhiễu
            s1 = f"$y' = \\frac{{{abs_a}}}{{\\sin^2 x}} {part_exp} {part_xn}$" # Sai dấu cot
            s2 = f"$y' = {part_cot} {format_coeff(b)} e^x {format_coeff(c)} x^{n}$" # Quên đạo hàm x^n
            s3 = f"$y' = {part_cot} - e^x {part_xn}$" # Sai hệ số e^x

            da_d = '\\True $' + da_dung_str + '$'
            list_1 = [da_d, s1, s2, s3]
            random.shuffle(list_1)

            # B5: Nội dung câu hỏi và lời giải
            noidungcauhoi = f"Đạo hàm của hàm số ${f_latex}$ là"

            loigiai = (
                f"Áp dụng quy tắc đạo hàm từng số hạng:\\\\\n"
                f"$({a} \\cot x)' = {a} \\cdot \\left( -\\frac{{1}}{{\\sin^2 x}} \\right) = {part_cot}$.\\\\\n"
                f"$({b} e^x)' = {b} e^x$.\\\\\n"
                f"$({c} x^{n})' = {c} \\cdot {n}x^{{{n-1}}} = {c*n}x^{{{n-1}}}$.\\\\\n"
                f"Vậy kết quả cuối cùng là: ${da_dung_str}$."
            )

            # B6: Xuất câu trắc nghiệm
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


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


def bt_dang10_p4_b2_c5_ds11(self):
            # Khai báo biến
            # --- Khởi tạo dữ liệu ---
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':


                a = random.choice([2, 3, 5])
                n = random.randint(2, 4)
                r = random.randint(2, 4)
                k = random.randint(1, 3)
                p = random.randint(2, 5)

                base_log = a**n

                # Tính toán hệ số của alpha và beta
                # log_{a^n} ( (x^(1/r) / y^k)^p ) = (p/n) * ( (1/r)*log_a x - k*log_a y )
                # = (p / (n*r)) * alpha - (p*k / n) * beta

                coeff_alpha = Rational(p, n * r)
                coeff_beta = Rational(p * k, n)

                # Hàm format latex cho biểu thức A*alpha + B*beta
                def format_expr(ca, cb):
                    def fmt(c, var):
                        if c == 0: return ""
                        if c == 1: return var
                        if c == -1: return f"-{var}"
                        return f"{latex(c)}{var}"

                    part1 = fmt(ca, "\\alpha")
                    part2 = fmt(cb, "\\beta")

                    if not part1: return part2
                    if not part2: return part1
                    connector = " + " if cb > 0 else " " # cb < 0 đã có dấu trừ ở hàm fmt
                    return part1 + connector + part2

                # Đáp án đúng
                da_dung_str = f"${format_expr(coeff_alpha, -coeff_beta)}$"

                # Tạo các phương án nhiễu (sai)
                s_raw = [
                    (coeff_alpha, coeff_beta),   # Sai dấu beta
                    (-coeff_alpha, coeff_beta),  # Sai cả hai dấu
                    (coeff_beta, -coeff_alpha),  # Hoán vị hệ số
                    (coeff_alpha * n, -coeff_beta), # Quên chia n ở alpha
                    (coeff_alpha, -coeff_beta * n), # Quên chia n ở beta
                    (Rational(p, n), -Rational(p, n)) # Hệ số đơn giản hóa sai
                ]

                s = []
                for ca, cb in s_raw:
                    txt = f"${format_expr(ca, cb)}$"
                    if txt != da_dung_str:
                        s.append(txt)

                # Lấy ngẫu nhiên 3 đáp án sai duy nhất
                s = list(set(s))
                random.shuffle(s)
                das1, das2, das3 = s[0], s[1], s[2]

                # --- Nội dung câu hỏi ---
                # Tạo chuỗi latex cho x (căn bậc r)
                x_str = f"\\sqrt[{r}]{{x}}" if r > 2 else "\\sqrt{x}"
                y_str = f"y^{k}" if k > 1 else "y"

                noidungcauhoi = (
                    f"Với các số thực dương $x, y$ tùy ý, đặt $\\log_{{{a}}} x = \\alpha$, $\\log_{{{a}}} y = \\beta$. "
                )

                bieuthuc_goc = f"\\log_{{{base_log}}} \\left( \\frac{{{x_str}}}{{{y_str}}} \\right)^{{{p}}}"

                # --- Nội dung lời giải ---
                step1_coeff = p
                step2_base_change = Rational(1, n)

                loigiai = (
                    f"Ta có: ${bieuthuc_goc} = {p} \\log_{{{base_log}}} \\left( \\frac{{{x_str}}}{{{y_str}}} \\right)$ \\\\\n"
                    f"$= {p} \\left( \\log_{{{a}^{{{n}}}}} x^{{\\frac{1}{{{r}}}}} - \\log_{{{a}^{{{n}}}}} {y_str} \\right)$ \\\\\n"
                    f"$= {p} \\left( \\frac{1}{{{n} \\cdot {r}}} \\log_{{{a}}} x - \\frac{{{k}}}{{{n}}} \\log_{{{a}}} y \\right)$ \\\\\n"
                    f"$= {latex(coeff_alpha)} \\alpha - {latex(coeff_beta)} \\beta$."
                )

                # --- Xuất câu trắc nghiệm ---
                da_d = '\\True ' + da_dung_str
                list_1 = [da_d, das1, das2, das3]
                random.shuffle(list_1)

                content = (
                    '\\begin{minipage}{\\textwidth} \n'
                    '\\begin{ex}\n' + 
                    f"Tính ${bieuthuc_goc}$. \n" +
                    str(noidungcauhoi) + 
                    '\\loigiai{' + str(loigiai) + '}\n'
                    '\\end{ex}\n \\end{minipage} \n')
            return content


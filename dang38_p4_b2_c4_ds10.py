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


def bt_dang38_p4_b2_c4_ds10(self):
            # Khai báo biến
            # Bước 1: Thiết lập biến ngẫu nhiên
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Tạo tọa độ đỉnh I(xI, yI) và tung độ giao điểm c
                # Chọn xI khác 0 và c khác yI để bài toán hợp lệ
                xI = random.randint(1, 4) * random.choice([-1, 1])
                yI = random.randint(-4, 4)
                c = random.randint(-4, 4)
                while c == yI:
                    c = random.randint(-4, 4)

                # Tính toán các hệ số dựa trên hệ phương trình:
                # 1. c_val = c
                # 2. -b/2a = xI  => b = -2*xI*a
                # 3. yI = a(xI^2) + b(xI) + c => yI = a(xI^2) - 2a(xI^2) + c => a = (c - yI)/(xI^2)
                a_val = Rational(c - yI, xI**2)
                b_val = -2 * a_val * xI
                c_val = c

                # Hàm định dạng phương trình Parabol đẹp mắt
                def format_p(a, b, c):
                    # Hệ số a
                    if a == 1: s = "x^2"
                    elif a == -1: s = "-x^2"
                    else: s = f"{latex(a)}x^2"
                    # Hệ số b
                    if b > 0: s += f" + {latex(b) if b != 1 else ''}x"
                    elif b < 0: s += f" - {latex(abs(b)) if b != -1 else ''}x"
                    # Hệ số c
                    if c > 0: s += f" + {c}"
                    elif c < 0: s += f" - {abs(c)}"
                    return s

                # Đáp án đúng và sai
                da_dung = f"${format_p(a_val, b_val, c_val)}$"

                list_sai = []
                while len(list_sai) < 3:
                    a_s = a_val + random.choice([-1, 1, Rational(1, 2)])
                    b_s = b_val + random.randint(-2, 2)
                    c_s = c_val + random.randint(-1, 1)
                    da_s = f"${format_p(a_s, b_s, c_s)}$"
                    if da_s != da_dung and da_s not in list_sai:
                        list_sai.append(da_s)

                # Câu hỏi
                noidungcauhoi = f"Xác định parabol $y = ax^2 + bx + c$, biết rằng parabol đó có đỉnh $I({xI}; {yI})$ và cắt trục tung tại điểm có tung độ bằng ${c}$."

                # Trộn đáp án
                da_d = '\\True ' + da_dung
                list_ans = [da_d] + list_sai
                random.shuffle(list_ans)

                # Bước 2: Viết chi tiết lời giải y hệt mẫu trong ảnh
                # Tính các biểu thức trung gian để đưa vào chuỗi
                b_theo_a = -2 * xI
                delta_theo_a = 4 * yI # Vì -Delta/4a = yI => Delta = -4a*yI

                # Biến đổi hệ (1) và (2)
                loigiai = (f'''Vì $(P)$ có đỉnh $I({xI}; {yI})$ nên ta có $\\begin{{cases}} -\\frac{{b}}{{2a}} = {xI} \\\\ -\\frac{{\\Delta}}{{4a}} = {yI} \\end{{cases}} \\Leftrightarrow \\begin{{cases}} b = {b_theo_a}a \\\\ b^2 - 4ac = {latex(-4 * yI)}a \\end{{cases}} \\quad (1)$. \\\\
            Gọi $A$ là giao điểm của $(P)$ với trục tung tại điểm có tung độ bằng ${c}$. Suy ra $A(0; {c})$. Theo giả thiết $A(0; {c}) \\in (P)$ nên $a \\cdot 0^2 + b \\cdot 0 + c = {c} \\Leftrightarrow c = {c}. \\quad (2)$ \\\\
            Từ $(1)$ và $(2)$ ta có hệ $\\begin{{cases}} b = {b_theo_a}a \\\\ ({b_theo_a}a)^2 - 4a({c}) = {latex(-4 * yI)}a \\\\ c = {c} \\end{{cases}} \\Leftrightarrow \\begin{{cases}} a = 0 \\\\ b = 0 \\\\ c = {c} \\end{{cases}}$ hoặc $\\begin{{cases}} a = {latex(a_val)} \\\\ b = {latex(b_val)} \\\\ c = {c} \\end{{cases}}$. \\\\
            Do $(P)$ là parabol nên $a \\neq 0$ nên ta chọn $a = {latex(a_val)}; b = {latex(b_val)}; c = {c}$. \\\\
            Vậy $(P): y = {format_p(a_val, b_val, c_val)}$.''')

            # Xuất dữ liệu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


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


def bt_dang45_p1_b2_c4_ds10(self):
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Random các giá trị
                a_val = random.randint(-5, 5)
                while a_val == 0: a_val = random.randint(-5, 5)

                b_val = random.randint(-5, 5)
                c_val = 2 # Cố định theo đề bài

                # Chọn 2 giá trị x phân biệt
                x1 = random.randint(-3, 3)
                x2 = random.randint(-3, 3)
                while x1 == x2:
                    x2 = random.randint(-3, 3)

                y1 = a_val * x1**2 + b_val * x1 + c_val
                y2 = a_val * x2**2 + b_val * x2 + c_val

                # Hàm bổ trợ để viết phương trình Parabol chuẩn toán học
                def format_parabol(a, b, c):
                    # Xử lý ax^2
                    if a == 1: s_a = "x^2"
                    elif a == -1: s_a = "-x^2"
                    else: s_a = f"{a}x^2"

                    # Xử lý bx
                    if b == 0: s_b = ""
                    elif b == 1: s_b = " + x"
                    elif b == -1: s_b = " - x"
                    elif b > 0: s_b = f" + {b}x"
                    else: s_b = f" - {abs(b)}x"

                    # Xử lý c (ở đây c=2 là số dương nên mặc định + 2)
                    s_c = f" + {c}" if c > 0 else (f" - {abs(c)}" if c < 0 else "")
                    return f"$y = {s_a}{s_b}{s_c}$"

                # Đáp án đúng
                da = format_parabol(a_val, b_val, c_val)
                kq_a, kq_b = a_val, b_val

                # Bước 4: Tạo phương án sai (không trùng đáp án đúng)
                s = []
                while len(s) < 3:
                    wa = random.randint(-5, 5)
                    wb = random.randint(-5, 5)
                    if wa == 0: wa = 2

                    wrong_str = format_parabol(wa, wb, c_val)
                    if (wa, wb) != (kq_a, kq_b) and wrong_str not in s and wrong_str != da:
                        s.append(wrong_str)

                # Câu hỏi
                noidungcauhoi = (f"Xác định parabol $y = ax^2 + bx + 2$, biết rằng parabol đó đi qua hai điểm "
                                 f"$M({x1};{y1})$ và $N({x2};{y2})$?")

                # Các đáp án
                da_d = ('\\True ' + da)
                list_1 = [da_d] + s
                random.shuffle(list_1)

                # Nội dung lời giải
                # Thiết lập các hạng tử cho hệ phương trình để hiển thị đẹp
                def format_eq_side(x_val):
                    term_a = f"{x_val**2}a"
                    if x_val == 0: term_b = ""
                    elif x_val == 1: term_b = " + b"
                    elif x_val == -1: term_b = " - b"
                    elif x_val > 0: term_b = f" + {x_val}b"
                    else: term_b = f" - {abs(x_val)}b"
                    return f"{term_a}{term_b} + 2"

                eq1_lhs = format_eq_side(x1)
                eq2_lhs = format_eq_side(x2)

                loigiai = (f"Vì $(P)$ đi qua hai điểm $M({x1};{y1})$ và $N({x2};{y2})$ nên ta có hệ phương trình: "
                           f"$\\begin{{cases}} {eq1_lhs} = {y1} \\\\ {eq2_lhs} = {y2} \\end{{cases}} "
                           f"\\Leftrightarrow \\begin{{cases}} a = {kq_a} \\\\ b = {kq_b} \\end{{cases}}$. \\\\ "
                           f"Vậy $(P): {da.replace('$', '')}$.")

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + noidungcauhoi + '\n'
                       '\\choice \n'
                       '{' + list_1[0] + '}\n'
                       '{' + list_1[1] + '}\n'
                       '{' + list_1[2] + '}\n'
                       '{' + list_1[3] + '}\n'
                       '\\loigiai{' + loigiai + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content


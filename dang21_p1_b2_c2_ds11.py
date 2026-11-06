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


def bt_dang21_p1_b2_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến và Random bài toán
            while True:
                u1 = random.randint(1, 6)
                d = random.randint(2, 6)

                # Thiết lập phương trình 1: u_n1 = k1 * u_n2
                k1 = random.randint(2, 5)
                n2 = random.randint(2, 5)
                u_n2 = u1 + (n2 - 1) * d
                target_val1 = k1 * u_n2

                # Tìm n1 nguyên dương phù hợp
                if (target_val1 - u1) % d == 0:
                    n1 = (target_val1 - u1) // d + 1
                    if n1 > n2 and n1 < 20: 
                        # Thiết lập phương trình 2: u_n3 = k2 * u_n4 + C
                        k2 = random.randint(2, 4)
                        n4 = random.randint(3, 8)
                        n3 = random.randint(n4 + 1, 15)

                        if n1 != n3 and n2 != n4: # Tránh trùng lặp 2 phương trình
                            C = (u1 + (n3 - 1) * d) - k2 * (u1 + (n4 - 1) * d)
                            if C != 0:
                                break

            # Xử lý chuỗi dấu cho hệ số C
            sign_C = f"+ {C}" if C > 0 else f"- {abs(C)}"

            # Hàm phụ trợ format d (để in "d" thay vì "1d")
            def format_d(coef):
                if coef == 1:
                    return "d"
                return f"{coef}d"

            # Hàm phụ trợ format phương trình chuẩn: au_1 + bd = c
            def format_eq(c1, c2, rhs):
                s = ""
                if c1 == 1: s += "u_1"
                elif c1 == -1: s += "-u_1"
                elif c1 != 0: s += f"{c1}u_1"

                if c2 == 1: s += " + d" if s else "d"
                elif c2 == -1: s += " - d" if s else "-d"
                elif c2 > 0: s += f" + {c2}d" if s else f"{c2}d"
                elif c2 < 0: s += f" - {abs(c2)}d" if s else f"-{abs(c2)}d"

                if not s: s = "0"
                return s + f" = {rhs}"

            d1 = format_d(n1 - 1)
            d2 = format_d(n2 - 1)
            d3 = format_d(n3 - 1)
            d4 = format_d(n4 - 1)

            # Tính toán hệ số cho phương trình rút gọn
            c11 = k1 - 1
            c12 = k1 * (n2 - 1) - (n1 - 1)
            eq1_str = format_eq(c11, c12, 0)

            c21 = k2 - 1
            c22 = k2 * (n4 - 1) - (n3 - 1)
            eq2_str = format_eq(c21, c22, -C)

            # Các đáp án trắc nghiệm
            da_d = ('\\True $u_1 = %s$ và $d = %s$' % (u1, d))

            # Tạo bộ đáp án sai (đảm bảo logic không bao giờ trùng đáp án đúng)
            pool = [
                f"$u_1 = {u1}$ và $d = {d+1}$",
                f"$u_1 = {u1}$ và $d = {d-1}$",
                f"$u_1 = {u1+1}$ và $d = {d}$",
                f"$u_1 = {u1-1}$ và $d = {d}$",
                f"$u_1 = {d}$ và $d = {u1}$",
                f"$u_1 = {u1+1}$ và $d = {d+1}$",
                f"$u_1 = {u1-1}$ và $d = {d-1}$"
            ]

            # Loại trừ nếu có bất kỳ phương án nhiễu nào vô tình trùng đáp án đúng
            correct_str = f"$u_1 = {u1}$ và $d = {d}$"
            pool = [item for item in pool if item != correct_str]
            pool = list(dict.fromkeys(pool)) # Loại bỏ trùng lặp trong pool
            random.shuffle(pool)

            da_s1 = str(pool[0])
            da_s2 = str(pool[1])
            da_s3 = str(pool[2])

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Câu hỏi
            noidungcauhoi = ('Số hạng đầu $u_1$ và công sai $d$ của cấp số cộng $(u_n)$ có $u_{%s} = %su_{%s}$ và $u_{%s} = %su_{%s} %s$ là'
                             % (n1, k1, n2, n3, k2, n4, sign_C))

            # Nội dung lời giải
            loigiai = ('Theo giả thiết ta có: '
                       '$\\begin{cases} u_{%s} = %su_{%s} \\\\ u_{%s} = %su_{%s} %s \\end{cases} '
                       '\\Leftrightarrow \\begin{cases} u_1 + %s = %s(u_1 + %s) \\\\ u_1 + %s = %s(u_1 + %s) %s \\end{cases} \\\\'
                       '\\Leftrightarrow \\begin{cases} %s \\\\ %s \\end{cases} \\Leftrightarrow \\begin{cases} u_1 = %s \\\\ d = %s \\end{cases}$.'
                       % (n1, k1, n2, n3, k2, n4, sign_C, 
                          d1, k1, d2, d3, k2, d4, sign_C,
                          eq1_str, eq2_str, u1, d))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                       '\\choice \n'
                       '{'+str(list_1[1])+'}\n'
                       '{'+str(list_1[2])+'}\n'
                       '{'+str(list_1[3])+'}\n'
                       '{'+str(list_1[0])+'}\n'
                       '\\loigiai{\n'+str(loigiai)+'\n}\n'
                       '\\end{ex}\n\\end{minipage} \n\n')
            return content


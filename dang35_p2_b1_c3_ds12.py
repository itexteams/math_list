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


def bt_dang35_p2_b1_c3_ds12(self):
            # Khai báo biến
            # Hàm hỗ trợ chuyển đổi dấu chấm thành dấu phẩy cho số thập phân
            def format_vn(number):
                return str(number).replace('.', ',')

            # --- B3: THIẾT LẬP THÔNG SỐ RANDOM ---
            nam_goc = random.randint(2010, 2020)
            P0 = round(random.uniform(85.0, 98.0), 1)
            r = round(random.uniform(0.010, 0.016), 3)
            k = round(P0 * r, 4) 
            t_target = random.randint(10, 25)
            nam_target = nam_goc + t_target

            # Nội dung câu hỏi
            noidungcauhoi = (f"Vào năm {nam_goc}, dân số nước ta khoảng {format_vn(P0)} triệu người. "
                             f"Giả sử, dân số nước ta sau $t$ năm được xác định bởi hàm số $S(t)$ (đơn vị: triệu người), "
                             f"trong đó tốc độ gia tăng dân số được cho bởi $S'(t) = {format_vn(k)}e^{{{format_vn(r)}t}}$, "
                             f"với $t$ là số năm kể từ năm {nam_goc}, $S'(t)$ tính bằng triệu người/năm. "
                             f"Xét tính đúng sai của các mệnh đề sau.")

            ################################ Phân đoạn Mệnh đề ################################

            # a) Mệnh đề về định nghĩa
            da_a_d = "\\True $S(t)$ là một nguyên hàm của $S'(t)$"
            da_a_s = "$S(t)$ là đạo hàm của $S'(t)$"
            list_a = [da_a_d, da_a_s]
            sol_a = "Theo định nghĩa về tốc độ thay đổi, dân số $S(t)$ là một nguyên hàm của hàm tốc độ gia tăng $S'(t)$."

            # b) Mệnh đề về công thức hàm số (Sử dụng \text{d}t)
            da_b_d = f"\\True $S(t) = {format_vn(P0)}e^{{{format_vn(r)}t}}$"
            da_b_s = f"$S(t) = {format_vn(P0)}e^{{{format_vn(r)}t}} + {format_vn(P0)}$"
            list_b = [da_b_d, da_b_s]
            sol_b = (f"Ta có $\\int S'(t) \\text{{d}}t = \\int {format_vn(k)}e^{{{format_vn(r)}t}} \\text{{d}}t = "
                     f"\\frac{{{format_vn(k)}}}{{{format_vn(r)}}}e^{{{format_vn(r)}t}} + C = {format_vn(P0)}e^{{{format_vn(r)}t}} + C$.\\\\ "
                     f"Vì $S(0) = {format_vn(P0)}$ nên $C = 0$. Suy ra $S(t) = {format_vn(P0)}e^{{{format_vn(r)}t}}$.")

            # c) Mệnh đề về tốc độ tăng
            v_t = round(k * math.exp(r * t_target), 1)
            da_c_d = f"\\True Tốc độ tăng dân số năm {nam_target} khoảng {format_vn(v_t)} triệu người/năm"
            da_c_s = f"Tốc độ tăng dân số năm {nam_target} khoảng {format_vn(round(v_t + 0.8, 1))} triệu người/năm"
            list_c = [da_c_d, da_c_s]
            sol_c = f"Tốc độ tăng dân số năm {nam_target} là: $S'({t_target}) = {format_vn(k)}e^{{{format_vn(r)} \\cdot {t_target}}} \\approx {format_vn(v_t)}$ (triệu người/năm)."

            # d) Mệnh đề về dân số
            p_t = int(round(P0 * math.exp(r * t_target), 0))
            da_d_d = f"\\True Dân số nước ta năm {nam_target} khoảng {p_t} triệu người"
            da_d_s = f"Dân số nước ta năm {nam_target} khoảng {p_t + 15} triệu người"
            list_d = [da_d_d, da_d_s]
            sol_d = f"Dân số nước ta năm {nam_target} là: $S({t_target}) = {format_vn(P0)}e^{{{format_vn(r)} \\cdot {t_target}}} \\approx {p_t}$ (triệu người)."

            # --- Vòng lặp chọn ngẫu nhiên để đảm bảo số câu Đúng từ 1-3 ---
            while True:
                ans_a = random.choice(list_a)
                ans_b = random.choice(list_b)
                ans_c = random.choice(list_c)
                ans_d = random.choice(list_d)
                true_count = sum('\\True' in ans for ans in [ans_a, ans_b, ans_c, ans_d])
                if 1 <= true_count <= 3:
                    break

            # --- Xuất nội dung ---
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + noidungcauhoi + '\n'
                '\\choiceTFn \n'
                '{' + ans_a + '}\n'
                '{' + ans_b + '}\n'
                '{' + ans_c + '}\n'
                '{' + ans_d + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + sol_a + '\n'
                '\\item ' + sol_b + '\n'
                '\\item ' + sol_c + '\n'
                '\\item ' + sol_d + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


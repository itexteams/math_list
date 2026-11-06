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


def bt_dang19_p3_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            # Bước 1: Chọn trước giao điểm I(x0, y0) là số nguyên để bài toán "đẹp"
            x0 = random.randint(-5, 5)
            y0 = random.randint(-5, 5)

            # Đảm bảo x0 khác 0 để khi tính m ở bước sau không bị chia cho 0
            if x0 == 0: x0 = 1 

            # Bước 2: Tạo đường thẳng d1: a1x + b1y + c1 = 0
            a1 = random.randint(1, 5)
            b1 = random.choice([-3, -2, -1, 1, 2, 3])
            c1 = -(a1 * x0 + b1 * y0)

            # Bước 3: Tạo đường thẳng d2: a2x + b2y + c2 = 0 (phải cắt d1)
            while True:
                a2 = random.randint(1, 5)
                b2 = random.randint(-3, 3)
                if b2 != 0 and a1 * b2 != a2 * b1: # Điều kiện để hai đường thẳng cắt nhau
                    break
            c2 = -(a2 * x0 + b2 * y0)

            # Bước 4: Tạo đường thẳng d3: mx + b3y + c3 = 0
            b3 = random.randint(1, 5)
            c3 = random.randint(-10, 10)
            # Để d3 đi qua I(x0, y0) thì: m*x0 + b3*y0 + c3 = 0 => m = -(b3*y0 + c3)/x0
            m_val = Rational(-(b3 * y0 + c3), x0)

            # --- Hàm hỗ trợ định dạng dấu cho số tự do ---
            def fmt_c(val):
                if val == 0: return ""
                return f"+ {val}" if val > 0 else f"- {abs(val)}"

            def fmt_b(val):
                if val == 1: return "+"
                if val == -1: return "-"
                return f"+ {val}" if val > 0 else f"- {abs(val)}"

            # --- Nội dung câu hỏi (Dùng f-string để tránh lỗi %s) ---
            noidungcauhoi = (f"Giá trị $m$ để ba đường thẳng sau đây đồng quy bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục). "
                             f"$d_1: {a1}x {fmt_b(b1)}y {fmt_c(c1)} = 0$, "
                             f"$d_2: {a2}x {fmt_b(b2)}y {fmt_c(c2)} = 0$ và "
                             f"$d_3: mx {fmt_b(b3)}y {fmt_c(c3)} = 0$.")

            # --- Đáp án ---
            da_dung = f"$m = {latex(m_val)}$"
            sai_tu = [
                f"$m = {latex(m_val + 1)}$",
                f"$m = {latex(m_val - 2)}$",
                f"$m = {latex(-m_val)}$",
                f"$m = {latex(m_val + Rational(1, 2))}$"
            ]
            random.shuffle(sai_tu)
            list_ans = ["\\True " + da_dung, sai_tu[0], sai_tu[1], sai_tu[2]]
            random.shuffle(list_ans)

            # --- Nội dung lời giải chi tiết ---
            h1=m_val
            number = Decimal(float(h1))  # Số cần làm tròn
            kq1 = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
            kqz=str(kq1).replace('.',',')
            loigiai = (f"Tọa độ giao điểm của $d_1$ và $d_2$ là nghiệm của hệ phương trình: "
                       f"${a1}x {fmt_b(b1)}y = {-c1} \\\\ {a2}x {fmt_b(b2)}y = {-c2} "
                       f"\\Leftrightarrow x = {x0}; y = {y0}  $ "
                       f"Vậy $I({x0}; {y0})$.\\\\ "
                       f"Để ba đường thẳng $d_1, d_2, d_3$ đồng quy thì điểm $I$ phải thuộc đường thẳng $d_3$.\\\\ "
                       f"Thay tọa độ $I$ vào phương trình $d_3$, ta có: "
                       f"$m \\cdot ({x0}) {fmt_b(b3)} ({y0}) {fmt_c(c3)} = 0 \\Leftrightarrow {x0}m = {-(b3*y0 + c3)} "
                       f"\\Leftrightarrow m = {latex(m_val)}$.")
            #Đáp án
            dapan='\\shortans[0]{$%s$}\n'%(kqz)

            # --- Xuất kết quả theo mẫu ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + noidungcauhoi + str(dapan)+
                '\\loigiai{' + loigiai + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 


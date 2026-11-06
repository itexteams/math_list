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


def bt_dang36_p4_b2_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            x = symbols('x')

            # B3: Suy nghĩ tìm cách random bài toán
            # Ta sẽ random f(0) = a và f'(x) = k*x + exp(x)
            a = random.randint(2, 8)  # Giá trị f(0), trong đề bài mẫu là 4
            k = random.randint(1, 5)  # Hệ số của x, trong đề bài mẫu là 1

            # --- Tính toán lời giải bằng Sympy ---
            # 1. Tìm nguyên hàm của f'(x) để có f(x) + C
            f_prime = k*x + exp(x)
            f_temp = integrate(f_prime, x) # f_temp = k*x**2/2 + exp(x)

            # 2. Tìm hằng số C dựa trên f(0) = a
            # f(0) = f_temp(0) + C = a => C = a - f_temp(0)
            f_at_0 = f_temp.subs(x, 0)
            C_val = a - f_at_0
            f_x = f_temp + C_val

            # 3. Tính tích phân từ 0 đến 1 của f(x)
            integral_result = integrate(f_x, (x, 0, 1))
            kq_dung = latex(simplify(integral_result))

            # B4: Tạo các phương án sai (không trùng với đáp án đúng)
            def generate_distractors(correct_val, a, k):
                s = set()
                while len(s) < 3:
                    # Tạo biến thể bằng cách thay đổi các hằng số trong kết quả cuối
                    # Kết quả có dạng: (6e + m)/6. Ta thay đổi m.
                    offset = random.choice([-2, -1, 1, 2, 3])
                    # Tạo một biểu thức sai tương tự cấu trúc đáp án đúng
                    wrong_expr = simplify(integral_result + offset)
                    wrong_latex = latex(wrong_expr)

                    if wrong_latex != correct_val:
                        s.add('$%s$' % wrong_latex)
                return list(s)

            distractors = generate_distractors(kq_dung, a, k)

            # Chuẩn bị nội dung cho mẫu
            noidungcauhoi = (r'''Cho hàm số $f(x)$ thỏa mãn $f(0) = %s$ và $f'(x) = %s + e^x, \forall x \in \mathbb{R}$. Tính $\int_{0}^{1} f(x) \text{d}x$.'''
                             % (latex(a), latex(k*x)))

            da_d = r'\True $%s$' % kq_dung
            da_s1 = distractors[0]
            da_s2 = distractors[1]
            da_s3 = distractors[2]

            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Nội dung lời giải chi tiết
            loigiai = (r'''Ta có: $\int f'(x) \text{d}x = \int (%s + e^x) \text{d}x = %s + C$. \\
                         Vì $f(0) = %s$ nên: $%s + C = %s \Leftrightarrow C = %s$. \\
                         Vậy: $f(x) = %s + %s$. \\
                         $\Rightarrow \int_{0}^{1} f(x) \text{d}x = \int_{0}^{1} \left( %s + %s \right) \text{d}x = \left( %s \right) \bigg|_0^1 = %s$.'''
                       % (latex(f_prime), latex(f_temp), 
                          latex(a), latex(f_at_0), latex(a), latex(C_val),
                          latex(f_temp), latex(C_val),
                          latex(f_temp), latex(C_val), latex(integrate(f_x, x)), kq_dung))

            # Xuất kết quả theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content


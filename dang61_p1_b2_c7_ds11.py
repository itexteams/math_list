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


def bt_dang61_p1_b2_c7_ds11(self):
            # Khai báo biến
            # Hàm hỗ trợ xử lý dấu để hiển thị đẹp: + - thành -, - - thành +
            def format_sign(val):
                s = latex(val)
                if s.startswith('-'):
                    return s
                return "+" + s

            # Khai báo biến ký hiệu
            x, a, b = symbols('x a b')

            # B1: Ngẫu nhiên hóa các giá trị nền tảng để tạo bài toán
            # Chọn a, b dưới dạng phân số để bài toán "đẹp"
            a_val = Rational(random.randint(-3, 3) or 1, random.randint(2, 5))
            b_val = Rational(random.randint(-8, 8) or -2, random.randint(1, 5))

            # Các điểm x1, x2 và điểm cần tính x_target
            x1 = 1
            x2 = -2
            x_target_sq = 2 # Tương ứng với căn bậc 2 của 2
            x_target_latex = r"\sqrt{2}"

            # B2: Tính toán các giá trị đề bài dựa trên a, b đã chọn
            # f'(x) = 3ax^2 - b/x^2
            f_prime_x1 = 3 * a_val * (x1**2) - b_val / (x1**2)
            f_prime_x2 = 3 * a_val * (x2**2) - b_val / (x2**2)

            # Đáp án đúng
            kq_val = 3 * a_val * x_target_sq - b_val / x_target_sq
            kq_latex = latex(kq_val)

            # Tạo các đáp án nhiễu
            s = []
            while len(s) < 3:
                offset = Rational(random.randint(-5, 5) or 1, random.randint(1, 3))
                wrong_ans = kq_val + offset
                wrong_ans_latex = latex(wrong_ans)
                if wrong_ans_latex not in s and wrong_ans_latex != kq_latex:
                    s.append(f"${wrong_ans_latex}$")

            da_d = r'\True ' + f'${kq_latex}$'
            da_s1 = s[0]
            da_s2 = s[1]
            da_s3 = s[2]

            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # B3: Nội dung câu hỏi và lời giải
            noidungcauhoi = (r'''Cho hàm số $f(x) = ax^3 + \frac{b}{x}$ có $f'(%s) = %s, f'(%s) = %s$. Khi đó $f'(%s)$ bằng'''
                            % (latex(x1), latex(f_prime_x1), latex(x2), latex(f_prime_x2), x_target_latex))

            # Chuẩn bị các thành phần trong lời giải để xử lý dấu
            # f'(x) = 3ax^2 - b/x^2
            # f'(1) = 3a - b
            # f'(-2) = 12a - b/4
            expr_x1 = "3a - b"
            expr_x2 = r"12a - \frac{b}{4}"
            expr_target = r"6a - \frac{b}{2}"

            loigiai = (r'''Ta có $f'(x) = 3ax^2 - \frac{b}{x^2} \Rightarrow \begin{cases} f'(%s) = %s \\ f'(%s) = %s \end{cases}$ \\
                        $\Rightarrow \begin{cases} %s = %s \\ %s = %s \end{cases} \Rightarrow \begin{cases} a = %s \\ b = %s \end{cases}$. \\
                        Khi đó $f'(%s) = %s = 6 \cdot \left(%s\right) - \frac{%s}{2} = %s$.'''
                        % (latex(x1), latex(f_prime_x1), latex(x2), latex(f_prime_x2),
                           expr_x1, latex(f_prime_x1), expr_x2, latex(f_prime_x2),
                           latex(a_val), latex(b_val),
                           x_target_latex, expr_target, latex(a_val), latex(b_val), kq_latex))

            # Xuất câu trắc nghiệm đúng định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


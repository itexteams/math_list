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


def bt_dang21_p4_b1_c7_ds11(self):
            # Khai báo biến
            # Biến số
            x = symbols('x')

            # Bước 1: Random các hệ số a, b, c, d của hàm số y = (ax + b) / (cx + d)
            # Đảm bảo ad - bc != 0 và mẫu số không quá phức tạp
            while True:
                a = random.randint(-5, 5)
                c = random.randint(1, 3)
                b = random.randint(-5, 5)
                d = random.randint(-5, 5)
                while a==0 or b==0 or c==0 or d==0:
                    a = random.randint(-5, 5)
                    c = random.randint(1, 3)
                    b = random.randint(-5, 5)
                    d = random.randint(-5, 5)
                if (a*d - b*c) != 0:
                    break

            f = (a*x + b) / (c*x + d)

            # Bước 2: Chọn y0 (tung độ) sao cho x0 là số nguyên để bài toán "đẹp"
            # Ta giải phương trình f(x) = y0 => x0 = (d*y0 - b) / (a - c*y0)
            # Ở đây tôi chọn ngẫu nhiên x0 trước để suy ra y0 nguyên
            x0_val = random.choice([i for i in range(-5, 6) if i != -d/c])
            y0_val = f.subs(x, x0_val)

            # Tính đạo hàm và hệ số góc k = f'(x0)
            f_prime = diff(f, x)
            k_val = f_prime.subs(x, x0_val)

            # Phương trình tiếp tuyến: y = k(x - x0) + y0
            pt_tieptuyen = simplify(k_val * (x - x0_val) + y0_val)

            # Xử lý hiển thị dấu +- thành -
            def format_pt(expr):
                s = latex(expr)
                return s.replace('+ -', '- ').replace('- -', '+ ')

            # Tạo các đáp án nhiễu
            da_dung = f"y = {format_pt(pt_tieptuyen)}"

            # Tạo các đáp án sai bằng cách đổi dấu hoặc đổi hệ số
            s1 = f"y = {format_pt(simplify(-k_val * (x - x0_val) + y0_val))}"
            s2 = f"y = {format_pt(simplify(k_val * (x + x0_val) + y0_val))}"
            s3 = f"y = {format_pt(simplify(k_val * x + random.randint(-5, 5)))}"

            # Đảm bảo không trùng lặp
            sai_list = list(set([s1, s2, s3]))
            while len(sai_list) < 3:
                sai_list.append(f"y = {random.randint(-5, 5)}x + {random.randint(-5, 5)}")

            # --- Nội dung hiển thị ---

            noidungcauhoi = (r"Lập phương trình tiếp tuyến của đồ thị hàm số $y = %s$ tại điểm có tung độ bằng $%s$." 
                             % (latex(f), latex(y0_val)))

            da_d = '\\True $' + da_dung + '$'
            da_s1 = '$' + sai_list[0] + '$'
            da_s2 = '$' + sai_list[1] + '$'
            da_s3 = '$' + sai_list[2] + '$'

            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Lời giải chi tiết
            loigiai = (r"Gọi $M(x_0; y_0)$ thuộc đồ thị hàm số $y = %s$ mà $y_0 = %s$. \\ "
                       r"Khi đó $\frac{%s x_0 + %s}{%s x_0 + %s} = %s \Rightarrow %s x_0 + %s = %s(%s x_0 + %s) \Leftrightarrow x_0 = %s \Rightarrow M(%s; %s)$. \\ "
                       r"Ta có $y' = %s$, suy ra $y'(%s) = %s$. \\ "
                       r"Do đó phương trình tiếp tuyến tại $M(%s; %s)$ là: \\ "
                       r"$y = %s(x - %s) %s \Leftrightarrow %s$."
                       % (latex(f), latex(y0_val),
                          latex(a), latex(b), latex(c), latex(d), latex(y0_val),
                          latex(a), latex(b), latex(y0_val), latex(c), latex(d),
                          latex(x0_val), latex(x0_val), latex(y0_val),
                          latex(simplify(f_prime)), latex(x0_val), latex(k_val),
                          latex(x0_val), latex(y0_val),
                          latex(k_val), latex(x0_val), ("+ " + latex(y0_val) if y0_val >= 0 else latex(y0_val)),
                          da_dung))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('+ -','-').replace('- -','+').replace('- +','-').replace('- -','+')
            return content


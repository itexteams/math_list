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


def bt_dang22_p1_b2_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # B3: Suy nghĩ cách random
            # 1. Random cận
            a = randint(0, 2)
            b = a + randint(1, 3)

            # 2. Random hàm đa thức P(x) = m*x^2 + p*x + q
            m = randint(1, 4)
            p = randint(0, 5)
            q = randint(1, 10)
            f_poly = m*x**2 + p*x + q

            # 3. Random các hệ số khác
            n = randint(2, 5)       # Hệ số của f'(x)
            f_a = randint(-10, 10)  # Giá trị f(a)
            K = randint(-20, 20)    # Kết quả vế phải của phương trình tích phân

            # 4. Tính toán giá trị f(b)
            # Integral(f_poly, (x, a, b)) - n*(f(b) - f(a)) = K
            int_val = integrate(f_poly, (x, a, b))
            f_b_val = (int_val - K)/n + f_a

            # --- Tạo các đáp án nhiễu ---
            kq_dung = '$%s$' % latex(f_b_val)
            da_d = '\\True ' + kq_dung

            s = []
            while len(s) < 3:
                nhieu = f_b_val + randint(-10, 10)
                if nhieu != f_b_val:
                    s.append('$%s$' % latex(nhieu))

            list_1 = [da_d] + s
            random.shuffle(list_1)

            # --- Nội dung câu hỏi ---
            noidungcauhoi = (r"Cho hàm số $f(x)$ liên tục trên đoạn $[%s;%s]$ và thoả mãn "
                             r"$\int_{%s}^{%s} \left[%s - %sf'(x)\right] \text{d} x = %s$ và $f(%s) = %s$. Giá trị $f(%s)$ là" 
                             % (a, b, a, b, latex(f_poly), n, K, a, f_a, b))

            # --- Nội dung lời giải ---
            nguyen_ham = integrate(f_poly, x)
            # Xử lý hiển thị dấu cho f(a) trong lời giải
            f_a_str = f"({f_a})" if f_a < 0 else f"{f_a}"
            prefix_sign = "+" if f_a < 0 else "-"

            loigiai = (r"Ta có: $\int_{%s}^{%s} \left[%s - %sf'(x)\right] \text{d} x = %s$ \\ "
                       r"$\Leftrightarrow \int_{%s}^{%s} \left(%s\right) \text{d} x - %s\int_{%s}^{%s} f'(x) \text{d} x = %s$ \\ "
                       r"$\Leftrightarrow \left.\left( %s\right ) \right|_{%s}^{%s} - %s[f(%s) - f(%s)] = %s$ \\ "
                       r"$\Leftrightarrow %s - %s[f(%s) - %s] = %s$ \\ "
                       r"$\Leftrightarrow %s[f(%s) %s %s] = %s \Rightarrow f(%s) = %s$." 
                       % (a, b, latex(f_poly), n, K, 
                          a, b, latex(f_poly), n, a, b, K,
                          latex(nguyen_ham), a, b, n, b, a, K,
                          latex(int_val), n, b, f_a_str, K,
                          n, b, prefix_sign, abs(f_a), latex(int_val - K), b, latex(f_b_val)))

            # --- Xuất câu trắc nghiệm ---
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


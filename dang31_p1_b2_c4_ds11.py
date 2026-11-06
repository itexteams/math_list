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


def bt_dang31_p1_b2_c4_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # --- B3: Suy nghĩ tìm cách random bài toán ---
            # Ngẫu nhiên hướng tiến tới của x: -oo hoặc +oo
            huong_tien = random.choice(['-\\infty', '+\\infty'])

            # Random các số mũ sao cho tổng bậc tử = bậc mẫu
            n = random.randint(2, 4)
            m = random.randint(3, 4)
            tong_bac = n + m

            # Random các hệ số (tránh số 0 để không mất bậc)
            a = random.randint(2, 5)
            b = random.randint(1, 9)
            c = random.randint(2, 4)
            d = random.randint(1, 9)
            e = random.randint(2, 3)
            f = random.randint(1, 9)

            # Tính toán kết quả chính xác (L = (a^n * c^m) / e^(n+m))
            # Sử dụng Rational để giữ kết quả ở dạng phân số tối giản
            kq_phân_so = Rational(a**n * c**m, e**tong_bac)
            da_dung_val = latex(kq_phân_so)

            # --- Tạo các phương án trắc nghiệm ---
            da_dung = f"${da_dung_val}$"

            # Tạo danh sách đáp án nhiễu
            s = set()
            while len(s) < 3:
                # Nhiễu bằng cách thay đổi giá trị một chút hoặc đảo ngược
                sai_tu = a**n * c**m + random.randint(-5, 5)
                if sai_tu <= 0: sai_tu = 1
                item = f"${latex(Rational(sai_tu, e**tong_bac))}$"
                if item != da_dung:
                    s.add(item)

            list_s = list(s)
            da_s1, da_s2, da_s3 = list_s[0], list_s[1], list_s[2]
            da_d = "\\True " + da_dung

            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # --- Nội dung câu hỏi và lời giải ---
            noidungcauhoi = (r"Cho hàm số $f(x) = \frac{(%sx + %s)^{%s}(%sx + %s)^{%s}}{(%s + %sx)^{%s}}$. Khi đó $\lim_{x \to %s} f(x)$ bằng" 
                             % (a, b, n, c, d, m, f, e, tong_bac, huong_tien))

            loigiai = (r"Ta có: "
                       r"$$\lim_{x \to %s} \frac{(%sx + %s)^{%s}(%sx + %s)^{%s}}{(%s + %sx)^{%s}} = \lim_{x \to %s} \frac{x^{%s}\left(%s + \frac{%s}{x}\right)^{%s} \cdot x^{%s}\left(%s + \frac{%s}{x})\right)^{%s}}{x^{%s}\left(\frac{%s}{x} + %s\right)^{%s}} $$ "
                       r"$$ = \lim_{x \to %s} \frac{\left(%s + \frac{%s}{x}\right)^{%s}\left(%s + \frac{%s}{x}\right)^{%s}}{\left(\frac{%s}{x} + %s\right)^{%s}} = \frac{%s^{%s} \cdot %s^{%s}}{%s^{%s}} = %s. $$"
                       % (huong_tien, a, b, n, c, d, m, f, e, tong_bac, 
                          huong_tien, n, a, b, n, m, c, d, m, tong_bac, f, e, tong_bac,
                          huong_tien, a, b, n, c, d, m, f, e, tong_bac,
                          a, n, c, m, e, tong_bac, da_dung_val))

            # --- Xuất câu trắc nghiệm ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content


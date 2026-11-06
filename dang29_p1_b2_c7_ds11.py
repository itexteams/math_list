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


def bt_dang29_p1_b2_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            x = symbols('x')

            # B3: Suy nghĩ tìm cách random bài toán
            # Random các hệ số a, b, c cho đa thức trong ngoặc: ax^3 + bx^2 + c
            # Random số mũ n bên ngoài
            a = random.randint(-5, 5)
            while a == 0: a = random.randint(-5, 5) # Đảm bảo là bậc 3

            b = random.randint(-5, 5)
            while b == 0: b = random.randint(-5, 5) # Giữ bậc 2 để giống mẫu hình ảnh

            c = random.randint(-10, 10)
            n = random.randint(3, 15)

            # Thiết lập biểu thức f(x) = (ax^3 + bx^2 + c)^n
            u = a*x**3 + b*x**2 + c
            y = u**n

            # Tính toán đạo hàm theo quy tắc (u^n)' = n * u' * u^(n-1)
            u_prime = diff(u, x)
            y_prime_formula = n * u_prime * (u**(n-1))

            # Định dạng LaTeX chuẩn cho biểu thức ban đầu và đạo hàm
            # Chú ý xử lý các dấu +- bằng cách dùng latex() của sympy
            latex_u = latex(u)
            latex_y = "y = \\left(" + latex_u + "\\right)^{" + str(n) + "}"
            latex_u_prime = latex(u_prime)
            latex_u_pow_n_minus_1 = "\\left(" + latex_u + "\\right)^{" + str(n-1) + "}"

            # B2: Viết lại nội dung theo mẫu
            noidungcauhoi = f"Đạo đạo hàm của hàm số ${latex_y}$ là"

            # Đáp án đúng
            da_d = "\\True $y' = " + str(n) + " \\cdot \\left(" + latex_u_prime + "\\right) \\cdot " + latex_u_pow_n_minus_1 + "$"

            # Tạo các đáp án nhiễu (sai số mũ hoặc sai đạo hàm bên trong)
            s1 = "$y' = " + str(n) + " \\cdot " + latex_u_pow_n_minus_1 + "$" # Thiếu u'
            s2 = "$y' = \\left(" + latex_u_prime + "\\right) \\cdot " + latex_u_pow_n_minus_1 + "$" # Thiếu n
            s3 = "$y' = " + str(n+1) + " \\cdot \\left(" + latex_u_prime + "\\right) \\cdot \\left(" + latex_u + "\\right)^{" + str(n) + "}$" # Sai quy tắc mũ

            # Trộn đáp án
            list_1 = [da_d, s1, s2, s3]
            random.shuffle(list_1)

            # Nội dung lời giải chi tiết
            loigiai = (f"Áp dụng công thức đạo hàm hàm hợp $(u^n)' = n \\cdot u' \\cdot u^{{n-1}}$, ta có:\\\\"
                       f"Với $u = {latex_u} \\Rightarrow u' = ({latex_u})' = {latex_u_prime}$.\\\\"
                       f"Vậy $y' = {n} \\cdot ({latex_u})' \\cdot ({latex_u})^{{{n-1}}} = {n} \\cdot ({latex_u_prime}) \\cdot ({latex_u})^{{{n-1}}}$.")

            # Xuất câu trắc nghiệm
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


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


def bt_dang32_p1_b2_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # B1 & B3: Thiết lập các giá trị ngẫu nhiên cho bài toán
            # Hàm gốc trong ảnh: y = ((x^2 + x - 1)/(x - 1))^8
            # Ta sẽ random các hệ số a, b, c, d và số mũ n: ((ax^2 + bx + c)/(x + d))^n

            a = 1 # Giữ nguyên hệ số x^2 để bài toán không quá phức tạp
            b = random.randint(1, 5)
            c = random.randint(-5, -1)
            d = random.randint(-3, 3)
            if d == 0: d = -1 # Tránh mẫu số chỉ là x
            n = random.randint(5, 10)

            # Định nghĩa biểu thức
            u_num = a*x**2 + b*x + c
            u_den = x + d
            u = u_num / u_den
            y = u**n

            # B2: Tính toán đạo hàm từng bước theo quy tắc (u^n)' = n * u' * u^(n-1)
            # 1. Đạo hàm bên trong (u')
            u_prime = diff(u, x)
            u_prime_simplified = simplify(u_prime)

            # 2. Đạo hàm toàn phần (y')
            y_prime = n * u_prime * (u**(n-1))

            # Chuẩn bị hiển thị Latex
            f_u = latex(u)
            f_u_num = latex(u_num)
            f_u_den = latex(u_den)
            f_u_prime_num = latex(simplify(diff(u_num, x) * u_den - u_num * diff(u_den, x)))
            f_u_den_sq = latex(u_den**2)

            # Nội dung câu hỏi
            noidungcauhoi = r"Đạo hàm của hàm số $y = \left( %s \right)^{%s}$ là" % (f_u, n)

            # Đáp án đúng
            da_dung = r"\True $y' = %s \cdot \frac{%s}{%s} \cdot \left( %s \right)^{%s}$" % (
                n, f_u_prime_num, f_u_den_sq, f_u, n-1
            )

            # Tạo các đáp án sai (thay đổi số mũ hoặc hệ số)
            da_sai1 = r"$y' = %s \cdot \frac{%s}{%s} \cdot \left( %s \right)^{%s}$" % (
                n, f_u_prime_num, f_u_den_sq, f_u, n
            )
            da_sai2 = r"$y' = \frac{%s}{%s} \cdot \left( %s \right)^{%s}$" % (
                f_u_prime_num, f_u_den_sq, f_u, n-1
            )
            da_sai3 = r"$y' = %s \cdot \left( %s \right)^{%s}$" % (
                n, f_u, n-1
            )

            # Trộn đáp án
            list_1 = [da_dung, da_sai1, da_sai2, da_sai3]
            random.shuffle(list_1)

            # Lời giải chi tiết
            loigiai = r"""Ta có $y = u^{%s}$ với $u = %s$. \\
            Áp dụng công thức $(u^n)' = n \cdot u' \cdot u^{n-1}$, ta có: \\
            $y' = %s \cdot \left( %s \right)' \cdot \left( %s \right)^{%s}$ \\
            Tính $u' = \left( \frac{%s}{%s} \right)' = \frac{(%s)'(%s) - (%s)(%s)'}{(%s)^2} = \frac{%s}{%s}$. \\
            Vậy $y' = %s \cdot \frac{%s}{%s} \cdot \left( %s \right)^{%s}$.""" % (
                n, f_u, 
                n, f_u, f_u, n-1,
                f_u_num, f_u_den, latex(diff(u_num, x)), f_u_den, f_u_num, latex(diff(u_den, x)), f_u_den,
                f_u_prime_num, f_u_den_sq,
                n, f_u_prime_num, f_u_den_sq, f_u, n-1
            )

            # Xử lý hiển thị dấu +- thành -
            noidungcauhoi = noidungcauhoi.replace('+ -', '-').replace('- -', '+')
            loigiai = loigiai.replace('+ -', '-').replace('- -', '+')

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


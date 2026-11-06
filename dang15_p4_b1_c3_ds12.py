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


def bt_dang15_p4_b1_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            x = symbols('x')

            # --- BƯỚC RANDOM BÀI TOÁN ---
            # Để bài toán đẹp, ta chọn hệ số a chia hết cho 4, b chia hết cho 3
            a1 = random.randint(1, 4)
            b1 = random.randint(1, 4)
            a = 4 * a1
            b = 3 * b1

            # Chọn giá trị x0 và hằng số C để tính ra K
            x0 = 1 
            C_real = random.randint(-5, 5)

            # Hàm số f(x)
            f = a*x**3 + b*x**2

            # Nguyên hàm F(x) (dạng tổng quát có + C)
            F_expr = a1*x**4 + b1*x**3 # Đây là phần biến của nguyên hàm

            # Đạo hàm f'(x)
            f_prime = diff(f, x)

            # Tính giá trị để tìm K: F(x0) - f'(x0) = K
            # F(x0) = F_expr.subs(x, x0) + C
            val_F_part = F_expr.subs(x, x0)
            val_f_prime = f_prime.subs(x, x0)
            K = val_F_part + C_real - val_f_prime

            # --- TẠO CÁC ĐÁP ÁN ---
            # Đáp án đúng
            da_dung = f"${latex(F_expr + C_real)}$"
            if C_real == 0:
                da_dung = f"${latex(F_expr)}$"

            # Tạo các đáp án sai (thay đổi hằng số C)
            s = set()
            while len(s) < 3:
                c_sai = random.randint(-15, 15)
                if c_sai != C_real:
                    expr_sai = F_expr + c_sai
                    if c_sai == 0: expr_sai = F_expr
                    s.add(f"${latex(expr_sai)}$")

            list_sai = list(s)

            # --- NỘI DUNG CÂU HỎI ---
            noidungcauhoi = (f"Tìm nguyên hàm $F(x)$ của hàm số $f(x) = {latex(f)}$, "
                             f"biết $F({x0}) - f'({x0}) = {K}$.")

            # --- NỘI DUNG LỜI GIẢI ---
            loigiai = (f"Ta có: \\\\\n"
                       f"$\\int ({latex(f)}) \\text{{d}}x = {latex(F_expr)} + C$. \\\\\n"
                       f"Đạo hàm: $f'(x) = {latex(f_prime)}$. \\\\\n"
                       f"Vì $F({x0}) - f'({x0}) = {K}$ nên: \\\\\n"
                       f"$({latex(val_F_part)} + C) - {val_f_prime} = {K}$ \\\\\n"
                       f"$\\Leftrightarrow C + {val_F_part - val_f_prime} = {K} \\Rightarrow C = {C_real}$. \\\\\n"
                       f"Vậy $F(x) = {latex(F_expr + C_real if C_real != 0 else F_expr)}$.")

            # --- XUẤT KẾT QUẢ ---
            da_d = '\\True ' + da_dung
            list_1 = [da_d] + list_sai
            random.shuffle(list_1)

            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content 


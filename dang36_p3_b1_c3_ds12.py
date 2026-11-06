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


def bt_dang36_p3_b1_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # --- BƯỚC 3: KHỞI TẠO CÁC GIÁ TRỊ RANDOM ---
                # Giả sử: Integral((a*sqrt(x) + f'(x))/k) = b*x^3 + c*x*sqrt(x) + C
                k = 2 # Giữ nguyên mẫu số là 2 cho giống đề gốc
                a = 1 # Hệ số của sqrt(x)

                # Random các thông số để số liệu đẹp
                b_val = random.choice([Rational(1, 2), 1, Rational(3, 2), 2]) 
                c_val = random.choice([1, 2, 3])
                f0 = random.randint(1, 5)
                x_calc = random.choice([4, 9, 16]) # Chọn số chính phương để khai căn đẹp

                # --- TÍNH TOÁN LOGIC ---
                # Từ nguyên hàm: (1/k) * [ (2a/3)*x*sqrt(x) + f(x) ] = b*x^3 + c*x*sqrt(x)
                # => f(x) = k*b*x^3 + (k*c - 2a/3)*x*sqrt(x) + Constant

                coeff_x3 = k * b_val
                coeff_xsqrtx = k * c_val - Rational(2 * a, 3)

                # Hàm f(x) = coeff_x3 * x^3 + coeff_xsqrtx * x*sqrt(x) + f0
                def f_func(val):
                    return coeff_x3 * (val**3) + coeff_xsqrtx * (val * int(val**0.5)) + f0

                kq_val = f_func(x_calc)
                kq = latex(kq_val)

                # --- BƯỚC 4: TẠO ĐÁP ÁN VÀ TRÁNH TRÙNG LẶP ---
                da_dung = '$%s$' % kq

                s = []
                while len(s) < 3:
                    sai_val = kq_val + random.choice([-10, -5, 5, 10, 15, 20, -2, 2])
                    sai_str = '$%s$' % latex(sai_val)
                    if sai_str != da_dung and sai_str not in s:
                        s.append(sai_str)

                das1, das2, das3 = s

                # --- SOẠN NỘI DUNG CÂU HỎI ---
                # Biểu thức vế phải đề bài: b*x^3 + c*x*sqrt(x)
                vp_tex = latex(b_val * symbols('x')**3 + c_val * symbols('x') * sqrt(symbols('x')))

                noidungcauhoi = (r'''Cho hàm số $f(x)$ liên tục trên nửa khoảng $[0;+\infty)$ thoả mãn $\int \frac{\sqrt{x} + f'(x)}{%s} \text{d}x = %s + C$. Biết rằng $f(0)=%s$, giá trị $f(%s)$ bằng bao nhiêu?'''
                                 % (latex(k), vp_tex, latex(f0), latex(x_calc)))

                # --- SOẠN NỘI DUNG LỜI GIẢI ---
                loigiai = (r'''Ta có: $\int \frac{\sqrt{x} + f'(x)}{%s} \text{d}x = \frac{1}{%s} \left( \int x^{\frac{1}{2}} \text{d}x + \int f'(x) \text{d}x \right) = \frac{1}{%s} \left( \frac{2}{3}x\sqrt{x} + f(x) \right) + C_1$. \\
                             Theo giả thiết: $\frac{1}{%s} \left( \frac{2}{3}x\sqrt{x} + f(x) \right) + C_1 = %s + C$ \\
                             $\Rightarrow \frac{1}{%s}f(x) = %s - \frac{1}{%s} \cdot \frac{2}{3}x\sqrt{x} + (C - C_1)$ \\
                             $\Rightarrow f(x) = %s \cdot x^3 + \left( %s \right)x\sqrt{x} + K$. \\
                             Mà $f(0)=%s \Rightarrow K=%s$. \\
                             Vậy $f(x) = %s x^3 + %s x\sqrt{x} + %s$. \\
                             Thay $x=%s$ ta được $f(%s) = %s$.'''
                           % (latex(k), latex(k), latex(k), 
                              latex(k), vp_tex, 
                              latex(k), vp_tex, latex(k),
                              latex(coeff_x3), latex(coeff_xsqrtx),
                              latex(f0), latex(f0),
                              latex(coeff_x3), latex(coeff_xsqrtx), latex(f0),
                              latex(x_calc), latex(x_calc), kq))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(str(kq))                                                                                               

                # Đưa các đáp án vào danh sách
                da_d = '\\True ' + da_dung
                list_1 = [da_d, das1, das2, das3]
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content  


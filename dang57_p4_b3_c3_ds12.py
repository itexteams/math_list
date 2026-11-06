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


def bt_dang57_p4_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # B3: Suy nghĩ tìm cách random bài toán
                # Chọn 3 điểm cực trị x1, x2, x3 (nguyên, khác 0 để tránh suy biến hệ số tự do)
                # Đảm bảo tích x1*x2*x3 != 0
                list_roots = random.sample([i for i in range(-4, 5) if i != 0], 3)
                list_roots.sort()
                x1, x2, x3 = list_roots

                # Chọn hệ số k (hệ số của x trong f(x), và -kx trong g(x))
                k = random.randint(1, 4)
                const_term = 2 * k # Hệ số tự do của f'(x) - g'(x)

                # Tính hệ số a: const_term = 4*a*(-x1)*(-x2)*(-x3) => const_term = -4*a*x1*x2*x3
                # a = const_term / (-4*x1*x2*x3)
                a_val = Rational(const_term, -4 * x1 * x2 * x3)

                # Biểu thức f'(x) - g'(x)
                h_prime = 4 * a_val * (x - x1) * (x - x2) * (x - x3)

                # B4: Tính diện tích S
                # S = tích phân từ x1 đến x3 của |f'(x) - g'(x)|
                S_val = integrate(Abs(h_prime), (x, x1, x3))

                # Đáp án đúng
                kq = '$%s$' % (latex(S_val))

                # Tạo các phương án sai (không trùng đáp án đúng)
                s = []
                while len(s) < 3:
                    # Tạo sai số bằng cách thay đổi tử số hoặc mẫu số một chút
                    offset = random.choice([Rational(1, 2), Rational(1, 3), 1, 2, 3])
                    sign = random.choice([1, -1])
                    wrong_val = S_val + sign * offset
                    if wrong_val > 0 and wrong_val != S_val:
                        latex_wrong = '$%s$' % (latex(wrong_val))
                        if latex_wrong not in s:
                            s.append(latex_wrong)

                # Câu hỏi
                # f(x) = ax^4 + bx^3 + cx^2 + kx
                # g(x) = mx^3 + nx^2 - kx
                noidungcauhoi = ('''Cho hai hàm số $f(x) = ax^4 + bx^3 + cx^2 + %sx$ và $g(x) = mx^3 + nx^2 - %sx$, với $a, b, c, m, n \\in \\mathbb{R}$. Biết hàm số $y = f(x) - g(x)$ có ba điểm cực trị là $%s, %s$ và $%s$. Tính diện tích hình phẳng giới hạn bởi hai đường $y = f'(x)$ và $y = g'(x)$.'''
                                 %(latex(k), latex(k), latex(x1), latex(x2), latex(x3)))

                # Các đáp án
                da_d = ('\\True ' + str(kq))
                da_s1 = s[0]
                da_s2 = s[1]
                da_s3 = s[2]

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (Viết y hệt mẫu trong ảnh)
                loigiai = ('''$f(x) - g(x) = ax^4 + (b-m)x^3 + (c-n)x^2 + %sx$ \\\\
                             $\\Leftrightarrow f'(x) - g'(x) = 4ax^3 + 3(b-m)x^2 + 2(c-n)x + %s$ \\\\
                             Theo giả thiết $f'(x) - g'(x) = 4a(x - (%s))(x - %s)(x - %s)$ \\\\
                             Ta có: $%s = 4a \\cdot (%s) \\cdot (%s) \\cdot (%s) \\Leftrightarrow a = %s$ \\\\
                             $\\Leftrightarrow f'(x) - g'(x) = %s(x - (%s))(x - %s)(x - %s) = 0 \\Leftrightarrow \\left[\\begin{aligned} &x = %s \\\\ &x = %s \\\\ &x = %s \\end{aligned}\\right.$ \\\\
                             $S = \\int_{%s}^{%s} \\left| %s(x - (%s))(x - %s)(x - %s) \\right| \\text{d}x = %s$.'''
                           %(latex(2*k), latex(2*k), latex(x1), latex(x2), latex(x3),
                             latex(2*k), latex(-x1), latex(-x2), latex(-x3), latex(a_val),
                             latex(4*a_val), latex(x1), latex(x2), latex(x3), 
                             latex(x1), latex(x2), latex(x3),
                             latex(x1), latex(x3), latex(4*a_val), latex(x1), latex(x2), latex(x3), latex(S_val)
                            ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


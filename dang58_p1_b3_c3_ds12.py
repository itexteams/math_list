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


def bt_dang58_p1_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            # Khai báo biến
            x = symbols('x')

            # B1 & B3: Thiết lập tham số
            # Chọn n sao cho g(x) = 2(x-n)(x+2n)^2 = 2x^3 + 6nx^2 - 8n^3
            list_n = [Rational(1, 2), Rational(-1, 2), Rational(2, 3), Rational(1, 3)]
            n = random.choice(list_n)

            b_val = 6 * n
            d_val = 8 * n**3
            c_val = random.randint(-2, 2)

            # Các hệ số của đề bài f(x) - f'(x)
            A = simplify(b_val - 3)
            B = simplify(c_val - 2 * b_val)
            C = simplify(d_val - c_val)

            # Hàm số
            f_x = x**3 + b_val * x**2 + c_val * x + d_val
            f_prime = diff(f_x, x)
            # g_x là hàm hiệu: xf'(x) - f(x)
            g_x = simplify(x * f_prime - f_x) 

            # Tìm nghiệm phương trình hoành độ giao điểm
            roots = solve(g_x, x)
            roots = sorted(list(set(roots))) # Lấy nghiệm phân biệt và sắp xếp
            x_min, x_max = roots[0], roots[-1]

            # B2: Tính diện tích S (Lấy trị tuyệt đối của tích phân vì g_x không đổi dấu giữa 2 nghiệm này)
            # Với dạng 2(x-n)(x+2n)^2, g_x không đổi dấu giữa n và -2n
            s_val = simplify(abs(integrate(g_x, (x, x_min, x_max))))

            # B4: Tạo phương án sai dạng phân số
            def get_wrong_ans(correct_val):
                wrongs = set()
                while len(wrongs) < 3:
                    off = Rational(random.randint(1, 8), random.choice([2, 3, 4, 6]))
                    val = random.choice([correct_val + off, abs(correct_val - off)])
                    if val != correct_val and val > 0:
                        wrongs.add('$%s$' % latex(val))
                return list(wrongs)

            s_wrong = get_wrong_ans(s_val)
            da_d = '\\True $%s$' % latex(s_val)
            list_ans = [da_d] + s_wrong
            random.shuffle(list_ans)

            # Định dạng hiển thị dấu +/- cho đẹp
            def fmt(val, is_first=False):
                s = latex(val)
                if not is_first and val >= 0: return "+" + s
                return s

            noidungcauhoi = (r'''Cho hàm số bậc ba $y=f(x)$ có đạo hàm liên tục trên $\mathbb{R}$ và thỏa mãn $f(x)-f'(x)=x^3 %s x^2 %s x %s, \forall x \in \mathbb{R}$. Diện tích hình phẳng giới hạn bởi đồ thị các hàm số $y=f(x)$ và $y=xf'(x)$ bằng'''
                             % (fmt(A), fmt(B), fmt(C)))

            loigiai = (r'''Giả sử $f(x) = x^3 + bx^2 + cx + d \Rightarrow f'(x) = 3x^2 + 2bx + c$. \\
            Ta có: $f(x) - f'(x) = x^3 + (b-3)x^2 + (c-2b)x + d - c$. \\
            Đồng nhất hệ số với giả thiết, ta có:
            $\begin{cases} b-3 = %s \\ c-2b = %s \\ d-c = %s \end{cases} \Leftrightarrow \begin{cases} b = %s \\ c = %s \\ d = %s \end{cases}$ \\
            Suy ra $f(x) = %s$ và $f'(x) = %s$. \\
            Phương trình hoành độ giao điểm của $y=f(x)$ và $y=xf'(x)$: \\
            $xf'(x) - f(x) = 0 \Leftrightarrow %s = 0 \Leftrightarrow \left[ \begin{aligned} & x = %s \\ & x = %s \end{aligned} \right.$ \\
            Diện tích hình phẳng cần tìm là:
            $S = \displaystyle \int_{%s}^{%s} \left| %s \right| \text{d}x = %s$.'''
                       % (latex(A), latex(B), latex(C), latex(b_val), latex(c_val), latex(d_val),
                          latex(f_x), latex(f_prime), latex(g_x), latex(roots[0]), latex(roots[1]),
                          latex(x_min), latex(x_max), latex(g_x), latex(s_val)))

            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + noidungcauhoi + '\n\\choice \n'
                       '{' + list_ans[0] + '}\n'
                       '{' + list_ans[1] + '}\n'
                       '{' + list_ans[2] + '}\n'
                       '{' + list_ans[3] + '}\n'
                       '\\loigiai{' + loigiai + '}\n'
                       '\\end{ex}\n\\end{minipage} \n\n')
            return content


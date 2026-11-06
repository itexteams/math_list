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


def bt_dang32_p4_b2_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến sympy
            x = symbols('x')

            # B1 & B3: Nghiên cứu đề bài và thiết lập logic random
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random các thông số cho hình vẽ
                # k: tung độ của A và B (chiều cao hình thang)
                # m: hoành độ của B
                # n: hoành độ của C (điểm bắt đầu Parabol)
                # p: hoành độ điểm kết thúc nhánh Parabol trên trục Ox

                k = random.randint(2, 4)
                m = random.randint(1, 3)
                n = m + random.randint(1, 2)
                p = n + random.randint(2, 3)

                # Phương trình Parabol đi qua C(n, 0) và D(p, 0): y = (x-n)(x-p)
                # y = x^2 - (n+p)x + n*p
                b_coeff = -(n + p)
                c_coeff = n * p
                f_parabol = x**2 + b_coeff*x + c_coeff

                # B2: Tính toán lời giải
                # Diện tích hình thang OABC (phần dương)
                # Đáy lớn OC = n, đáy nhỏ AB = m, chiều cao OA = k
                S_trapezoid = Rational((m + n) * k, 2)

                # Tích phân phần Parabol từ n đến p
                S_integral = integrate(f_parabol, (x, n, p))

                # Kết quả cuối cùng
                kq_value = S_trapezoid + S_integral
                da = '$%s$' % latex(kq_value)

                # B4: Điều chỉnh các phương án sai không được trùng đáp án đúng
                s = set()
                while len(s) < 3:
                    # Tạo các phương án nhiễu bằng cách thay đổi giá trị tính toán
                    noise_list = [
                        S_trapezoid - S_integral, # Nhầm dấu tích phân
                        S_trapezoid + Rational(1, 2) * S_integral,
                        S_trapezoid + S_integral + Rational(random.randint(1, 3), 3),
                        S_trapezoid,
                        Rational(m + n, 2) * k + Rational(1, 3),
                        kq_value - Rational(2, 3),
                        kq_value + Rational(1, 2)
                    ]
                    val = '$%s$' % latex(random.choice(noise_list))
                    if val != da:
                        s.add(val)

                das_list = list(s)
                das1, das2, das3 = das_list[0], das_list[1], das_list[2]

                # Mã TikZ cho hình vẽ
                tikz_code = r'''\begin{center} \scalebox{0.6}{ \begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] 
                \draw[->] (-0.5,0) -- (''' + str(p + 1) + r''',0) node[below] {$x$};
                \draw[->] (0,-1.5) -- (0, ''' + str(k + 1) + r''') node[left] {$y$};
                \draw (0,0) node[below left] {$O$};
                \draw[thick] (0, ''' + str(k) + r''') node[above left] {$A$} -- (''' + str(m) + r''', ''' + str(k) + r''') node[above] {$B$} -- (''' + str(n) + r''',0) node[above right] {$C$};
                \draw[thick, domain=''' + str(n) + r''':''' + str(p) + r''', samples=100] plot (\x, {(\x-''' + str(n) + r''')*(\x-''' + str(p) + r''')});
                \fill[yellow, opacity=0.5] (0,0) -- (0, ''' + str(k) + r''') -- (''' + str(m) + r''', ''' + str(k) + r''') -- (''' + str(n) + r''',0) -- cycle;
                \fill[yellow, opacity=0.5, domain=''' + str(n) + r''':''' + str(p) + r'''] plot (\x, {(\x-''' + str(n) + r''')*(\x-''' + str(p) + r''')}) -- (''' + str(n) + r''',0) -- cycle;
                \draw[dashed] (''' + str(m) + r''',0) node[below] {$''' + str(m) + r'''$} -- (''' + str(m) + r''', ''' + str(k) + r''');
                \node at (0, ''' + str(k) + r''') [left] {$''' + str(k) + r'''$};
                \node at (''' + str(n) + r''', 0) [below left] {$''' + str(n) + r'''$};
                \node at (''' + str(p) + r''', 0) [below right] {$''' + str(p) + r'''$};
                \node at (''' + str(p-0.5) + r''', 1.5) {$y = x^2 ''' + ('' if b_coeff == 0 else ('+' if b_coeff > 0 else '') + str(b_coeff)) + r'x' + ('+' if c_coeff > 0 else '') + str(c_coeff) + r'''$};
            \end{tikzpicture} } \end{center}'''

                # Câu hỏi
                noidungcauhoi = ('''Hình vẽ sau (bao gồm đường gấp khúc $ABC$ và một nhánh của Parabol $(P)$ có phương trình $y = %s$) là đồ thị của hàm số $y = f(x)$.
            %s
            Tính $\\int_{0}^{%s} f(x) \\text{d}x$.'''
                                 % (latex(f_parabol), tikz_code, latex(p)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Dựa vào đồ thị, ta có:
                           $\\int_{0}^{%s} f(x) \\text{d}x = \\int_{0}^{%s} f(x) \\text{d}x + \\int_{%s}^{%s} f(x) \\text{d}x$. \\\\
                           Trong đó: \\\\
                           - $\\int_{0}^{%s} f(x) \\text{d}x$ chính là diện tích hình thang $OABC$ có đường cao $OA=%s$, hai đáy $AB=%s$ và $OC=%s$. 
                           Do đó $S_{OABC} = \\frac{(%s + %s) \\cdot %s}{2} = %s$. \\\\
                           - Với $x \\in [%s; %s]$, $f(x) = %s$. 
                           Khi đó $\\int_{%s}^{%s} (%s) \\text{d}x = %s$. \\\\
                           Vậy $\\int_{0}^{%s} f(x) \\text{d}x = %s + (%s) = %s$.'''
                           % (latex(p), latex(n), latex(n), latex(p),
                              latex(n), latex(k), latex(m), latex(n),
                              latex(m), latex(n), latex(k), latex(S_trapezoid),
                              latex(n), latex(p), latex(f_parabol),
                              latex(n), latex(p), latex(f_parabol), latex(S_integral),
                              latex(p), latex(S_trapezoid), latex(S_integral), latex(kq_value)
                              ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) +
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content


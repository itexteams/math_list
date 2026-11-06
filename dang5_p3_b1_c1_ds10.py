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


def bt_dang5_p3_b1_c1_ds10(self):
    # Khai báo biến n
    n = symbols('n')

    # B1 & B3: Nghiên cứu đề bài và thiết lập tham số ngẫu nhiên
    # Đề bài gốc: (2n^3 + n^2 + 7n + 1) chia cho (2n - 1) dư 5
    # Ta sẽ tạo dạng (an^3 + bn^2 + cn + d) chia cho (an + e)

    a = 2
    e = random.choice([-1, 1])
    divisor = a*n + e

    # Tạo đa thức thương ngẫu nhiên Q(n) = A*n^2 + B*n + C
    A = random.randint(1, 3)
    B = random.randint(1, 3)
    C = random.randint(1, 5)
    Q = A*n**2 + B*n + C

    # Số dư R phải khác 0
    R = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    # Đa thức bị chia P(n) = Q(n)*divisor + R
    P_expr = expand(Q * divisor + R)

    # SỬA LỖI: Chuyển biểu thức thành Poly để lấy hệ số hoặc sử dụng Poly trực tiếp
    P_poly = Poly(P_expr, n)
    coeffs = P_poly.all_coeffs() 

    # Tìm các giá trị nguyên của n
    # divisor (2n + e) phải là ước của R
    divisors_of_R = []
    for i in range(1, R + 1):
        if R % i == 0:
            divisors_of_R.append(i)
            divisors_of_R.append(-i)

    valid_n = []
    for d in divisors_of_R:
        # a*n + e = d  => n = (d - e) / a
        if (d - e) % a == 0:
            valid_n.append((d - e) // a)

    count_n = len(valid_n)

    # B2: Viết lại nội dung theo mẫu
    noidungcauhoi = ('''Tìm số các số nguyên $n$ để mệnh đề $P(n): $"$%s$ chia hết cho $%s$" là mệnh đề đúng.'''
                    %(latex(P_expr), latex(divisor)))

    # Đáp án đúng
    da = str(count_n)

    # Tạo danh sách đáp án nhiễu
    s_values = [count_n + 1, count_n + 2, count_n - 1, count_n - 2, 0, 1, 2, 3, 4, 5, 6]
    s_values = list(set([v for v in s_values if v >= 0 and v != count_n])) # Lọc bỏ số âm và đáp án đúng
    random.shuffle(s_values)

    das1 = str(s_values[0])
    das2 = str(s_values[1])
    das3 = str(s_values[2])

    # Tráo thứ tự đáp án
    da_d = ('\\True ' + str(da))
    list_1 = [da_d, das1, das2, das3]
    random.shuffle(list_1)

    # Nội dung lời giải
    # Sử dụng latex() giúp xử lý tự động các dấu +- thành -
    loigiai = ('''Ta có: $%s = (%s)(%s) + %s$. \\\\
                    Để $%s$ chia hết cho $%s$ thì $%s$ phải chia hết cho $%s$. \\\\
                    Khi đó $%s \\in \\{%s\\}$. \\\\
                    Ta có bảng giá trị sau: \\\\
                    \\begin{center}
                    \\begin{tabular}{|c|%s}
                    \\hline
                    $%s$ & %s \\\\
                    \\hline
                    $n$ & %s \\\\
                    \\hline
                    \\end{tabular}
                    \\end{center}
                    Vậy có %s giá trị nguyên của $n$ thỏa mãn.'''
                %(latex(P_expr), latex(Q), latex(divisor), latex(R),
                    latex(P_expr), latex(divisor), latex(R), latex(divisor),
                    latex(divisor), ', '.join(map(str, sorted(divisors_of_R))),
                    'c|' * len(divisors_of_R),
                    latex(divisor), ' & '.join(['$%s$' % d for d in sorted(divisors_of_R)]),
                    ' & '.join(['$%s$' % latex(Rational(d - e, a)) if (d-e)%a==0 else 'x' for d in sorted(divisors_of_R)]),
                    da))
    dapan=' \\shortans[0]{$%s$} '%(da)             

    # Xuất câu trắc nghiệm đúng mẫu yêu cầu
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
        '\\loigiai{'+str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content


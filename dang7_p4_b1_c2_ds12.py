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


def bt_dang7_p4_b1_c2_ds12(self):
    # Hàm xử lý hiển thị số: nếu là thập phân hữu hạn thì dùng dấu phẩy, nếu vô hạn thì để nguyên phân số LaTeX
    def format_num(val):
        if val.q in [1, 2, 4, 8, 16, 32, 5, 10, 20]:
            v = float(val)
            if v.is_integer():
                return str(int(v))
            return f"{v}".replace('.', ',')
        else:
            return latex(val)

    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        # Random tần số lớp 12A
        fA1 = randint(1, 3)
        fA2 = 0
        fA3 = randint(14, 16)
        fA4 = randint(11, 13)
        fA5 = randint(9, 11)
        fA6 = randint(4, 6)
        nA = fA1 + fA2 + fA3 + fA4 + fA5 + fA6

        # Random tần số lớp 12B
        fB1 = 0
        fB2 = 0
        fB3 = randint(16, 18)
        fB4 = randint(9, 11)
        fB5 = randint(8, 10)
        fB6 = randint(5, 7)
        nB = fB1 + fB2 + fB3 + fB4 + fB5 + fB6

        # --- TÍNH TOÁN LỚP 12A ---
        # Khoảng biến thiên
        RA = 175 - 145
        # Q1A
        posQ1A = Rational(nA, 4)
        cf_Q1A_before = fA1 + fA2
        Q1A_val = 155 + Rational(posQ1A - cf_Q1A_before, fA3) * 5
        # Q3A
        posQ3A = Rational(3*nA, 4)
        cf_Q3A_before = fA1 + fA2 + fA3 + fA4
        cf_Q3A_str = f"{fA1}+{fA3}+{fA4}" # String hiển thị tổng tần số
        Q3A_val = 165 + Rational(posQ3A - cf_Q3A_before, fA5) * 5
        # Delta QA
        Delta_QA = Q3A_val - Q1A_val

        # --- TÍNH TOÁN LỚP 12B ---
        # Khoảng biến thiên
        RB = 175 - 155
        # Q1B
        posQ1B = Rational(nB, 4)
        cf_Q1B_before = fB1 + fB2
        Q1B_val = 155 + Rational(posQ1B - cf_Q1B_before, fB3) * 5
        # Q3B
        posQ3B = Rational(3*nB, 4)
        cf_Q3B_before = fB1 + fB2 + fB3 + fB4
        cf_Q3B_str = f"{fB3}+{fB4}" # String hiển thị tổng tần số
        Q3B_val = 165 + Rational(posQ3B - cf_Q3B_before, fB5) * 5
        # Delta QB
        Delta_QB = Q3B_val - Q1B_val

        # Nội dung câu hỏi
        noidungcauhoi = (
            'Bảng sau đây cho biết chiều cao của các học sinh lớp 12A và 12B.\n'
            '\\begin{center}\n'
            '\\begin{tabular}{|c|c|c|c|c|c|c|}\n'
            '\\hline\n'
            'Thu nhập & $[145;150)$ & $[150;155)$ & $[155;160)$ & $[160;165)$ & $[165;170)$ & $[170;175)$ \\\\ \n'
            '\\hline\n'
            'Số học sinh lớp 12A & %s & %s & %s & %s & %s & %s \\\\ \n'
            '\\hline\n'
            'Số học sinh lớp 12B & %s & %s & %s & %s & %s & %s \\\\ \n'
            '\\hline\n'
            '\\end{tabular}\n'
            '\\end{center}'
            'a) Tìm khoảng biến thiên, khoảng tứ phân vị cho các mẫu số liệu ghép nhóm về chiều cao của học sinh lớp 12A, 12B.\\\\ '
            'b) Để so sánh độ phân tán về chiều cao của học sinh hai lớp này ta nên dùng khoảng biến thiên hay khoảng tứ phân vị? Vì sao?'
            % (fA1, fA2, fA3, fA4, fA5, fA6, fB1, fB2, fB3, fB4, fB5, fB6)
        )

        # Nội dung lời giải
        loigiai = (
            'a) Lớp 12A: Khoảng biến thiên: $R = 175 - 145 = %s$ \\\\'
            'Ta có cỡ mẫu $n = %s$. Giả sử $x_1, x_2, \\dots, x_{%s}$ là chiều cao của các học sinh lớp $12A$ và giả sử dãy số liệu gốc này đã được sắp xếp theo thứ tự không giảm. \\\\'
            'Vì $\\frac{n}{4} = %s$ và $%s < %s < %s + %s$ nên nhóm chứa tứ phân vị thứ nhất là nhóm $[155;160)$ và tứ phân vị thứ nhất là: $Q_1 = 155 + \\frac{\\frac{%s}{4} - %s}{%s} \\cdot 5 = %s$ \\\\'
            'Vì $\\frac{3n}{4} = %s$ và $%s < %s < %s + %s$ nên nhóm chứa tứ phân vị thứ ba là nhóm $[165;170)$ và tứ phân vị thứ ba là: $Q_3 = 165 + \\frac{\\frac{3.%s}{4} - (%s)}{%s} \\cdot 5 = %s$ \\\\'
            'Khoảng tứ phân vị của mẫu số liệu ghép nhóm là: $\\Delta_{Q_A} = %s - %s = %s$ \\\\'
            'Lớp 12B: Khoảng biến thiên: $R = 175 - 155 = %s$ \\\\'
            'Ta có cỡ mẫu $n = %s$. Giả sử $x_1, x_2, \\dots, x_{%s}$ là chiều cao của các học sinh lớp $12B$ và giả sử dãy số liệu gốc này đã được sắp xếp theo thứ tự không giảm. \\\\'
            'Vì $\\frac{n}{4} = %s$ và $0 < %s < %s$ nên nhóm chứa tứ phân vị thứ nhất là nhóm $[155;160)$ và ta có: \\\\'
            '$$Q\'_1 = 155 + \\frac{\\frac{%s}{4} - 0}{%s} \\cdot 5 = %s$$'
            'Vì $\\frac{3n}{4} = %s$ và $%s < %s < %s + %s$ nên nhóm chứa tứ phân vị thứ ba là nhóm $[165;170)$ và tứ phân vị thứ ba là $Q\'_3 = 165 + \\frac{\\frac{3.%s}{4} - (%s)}{%s} \\cdot 5 = %s$ \\\\'
            'Khoảng biến thiên của mẫu số liệu ghép nhóm là: $\\Delta_{Q_B} = %s - %s = %s$ \\\\'
            'b) Để so sánh độ phân tán về chiều cao của học sinh hai lớp này, ta nên dùng khoảng tứ phân vị vì khoảng tứ phân vị chỉ phụ thuộc vào nửa giữa của mẫu số liệu, không bị ảnh hưởng bởi các giá trị bất thường.'
            % (
                # Thêm format cho Lớp 12A
                RA, nA, nA, 
                format_num(posQ1A), fA1, format_num(posQ1A), fA1, fA3, nA, fA1, fA3, format_num(Q1A_val),
                format_num(posQ3A), cf_Q3A_str, format_num(posQ3A), cf_Q3A_str, fA5, nA, cf_Q3A_str, fA5, format_num(Q3A_val),
                format_num(Q3A_val), format_num(Q1A_val), format_num(Delta_QA),

                # Thêm format cho Lớp 12B
                RB, nB, nB,
                format_num(posQ1B), format_num(posQ1B), fB3, nB, fB3, format_num(Q1B_val),
                format_num(posQ3B), cf_Q3B_str, format_num(posQ3B), cf_Q3B_str, fB5, nB, cf_Q3B_str, fB5, format_num(Q3B_val),
                format_num(Q3B_val), format_num(Q1B_val), format_num(Delta_QB)
            )
        )

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
    return content


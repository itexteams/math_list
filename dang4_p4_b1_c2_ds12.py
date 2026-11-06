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


def bt_dang4_p4_b1_c2_ds12(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)

    def to_str(val):
        """
        Hàm hỗ trợ in phân số:
        - Nếu là số nguyên thì in số nguyên.
        - Nếu phân số có thể biểu diễn dưới dạng thập phân hữu hạn (mẫu số chỉ chứa ước nguyên tố 2 và 5) 
          thì in dưới dạng số thập phân (thay dấu '.' thành ',').
        - Ngược lại in dưới dạng phân số LaTeX.
        """
        if val.is_Integer:
            return str(val)
        d = val.q
        while d % 2 == 0: d //= 2
        while d % 5 == 0: d //= 5
        if d == 1: 
            return f"{float(val):g}".replace('.', ',')
        else:
            return sp.latex(val)

    if dang=='1':
        # Random khoảng cách h của mỗi nhóm
        h = random.choice([1, 2, 3])
        a0, a1, a2, a3, a4, a5 = 0, h, 2*h, 3*h, 4*h, 5*h

        # Chọn n chia hết cho 4 để các mốc n/4 và 3n/4 luôn là số nguyên (giống n=80 trong mẫu)
        K = random.choice([10, 15, 20, 25, 30]) # K = n/4
        n = 4 * K

        # Thiết lập random tần số f1, f2, f3, f4, f5
        # Điều kiện Q1 chắc chắn rơi vào nhóm 2: f1 < K < f1 + f2
        f1 = random.randint(3, K - 1)
        sum12 = random.randint(K + 1, 2 * K - 1) # sum12 = f1 + f2
        f2 = sum12 - f1

        # Điều kiện Q3 chắc chắn rơi vào nhóm 4: f1 + f2 + f3 < 3K < f1 + f2 + f3 + f4
        sum123 = random.randint(2 * K + 1, 3 * K - 1) # sum123 = f1 + f2 + f3
        f3 = sum123 - sum12
        sum1234 = random.randint(3 * K + 1, 4 * K - 2) # sum1234 = f1 + f2 + f3 + f4
        f4 = sum1234 - sum123
        f5 = n - sum1234

        # Tính toán giá trị chính xác bằng Sympy Rational
        Q1_val = a1 + sp.Rational(K - f1, f2) * h
        Q3_val = a3 + sp.Rational(3 * K - sum123, f4) * h
        Delta_Q = Q3_val - Q1_val

        # Đề bài
        noidungcauhoi = f"""Một người ghi lại thời gian đàm thoại của một số cuộc gọi cho kết quả như bảng sau:
    \\begin{{center}}
    \\begin{{tabular}}{{|c|c|}}
    \\hline
    \\textbf{{Thời gian $t$ (phút)}} & \\textbf{{Số cuộc gọi}} \\\\
    \\hline
    $0 \\le t < {a1}$ & ${f1}$ \\\\
    \\hline
    ${a1} \\le t < {a2}$ & ${f2}$ \\\\
    \\hline
    ${a2} \\le t < {a3}$ & ${f3}$ \\\\
    \\hline
    ${a3} \\le t < {a4}$ & ${f4}$ \\\\
    \\hline
    ${a4} \\le t < {a5}$ & ${f5}$ \\\\
    \\hline
    \\end{{tabular}}
    \\end{{center}}
    Tính khoảng tứ phân vị của mẫu số liệu ghép nhóm trên."""

        # Nội dung lời giải
        loigiai = f"""Hiệu chỉnh lại bảng số liệu ta có:
    \\begin{{center}}
    \\begin{{tabular}}{{|c|c|c|c|c|c|}}
    \\hline
    Thời gian $t$ (phút) & $[0;{a1})$ & $[{a1};{a2})$ & $[{a2};{a3})$ & $[{a3};{a4})$ & $[{a4};{a5})$ \\\\
    \\hline
    Số cuộc gọi & ${f1}$ & ${f2}$ & ${f3}$ & ${f4}$ & ${f5}$ \\\\
    \\hline
    \\end{{tabular}}
    \\end{{center}}
    Cỡ mẫu $n = {n}$. Giả sử $x_1, x_2, \\dots, x_{{{n}}}$ là thời gian đàm thoại của ${n}$ cuộc gọi và giả sử dãy số liệu gốc này đã được sắp xếp theo thứ tự tăng dần.
    Vì $\\frac{{n}}{{4}} = {K}$ và ${f1} < {K} < {f1}+{f2}$ nên nhóm chứa tứ phân vị thứ nhất là nhóm $[{a1};{a2})$ và tứ phân vị thứ nhất là: $Q_1 = {a1} + \\frac{{\\frac{{{n}}}{{4}} - {f1}}}{{{f2}}} \\cdot {h} = {to_str(Q1_val)}$
    vì $\\frac{{3n}}{{4}} = {3*K}$ và ${sum123} < {3*K} < {sum1234}$ nên nhóm chứa tứ phân vị thứ ba là nhóm $[{a3};{a4})$ và tứ phân vị thứ ba là: $Q_3 = {a3} + \\frac{{\\frac{{3 \\cdot {n}}}{{4}} - ({f1}+{f2}+{f3})}}{{{f4}}} \\cdot {h} = {to_str(Q3_val)}$
    Vậy khoảng tứ phân vị của mẫu số liệu ghép nhóm là: ${to_str(Q3_val)} - {to_str(Q1_val)} = {to_str(Delta_Q)}$"""

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\n\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
    return content


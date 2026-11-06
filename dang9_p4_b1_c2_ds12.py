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


def bt_dang9_p4_b1_c2_ds12(self):
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
        temp_d = d
        while temp_d % 2 == 0: temp_d //= 2
        while temp_d % 5 == 0: temp_d //= 5
        if temp_d == 1: 
            return f"{float(val):g}".replace('.', ',')
        else:
            return sp.latex(val)

    if dang=='1':
        # Random năm
        Y1 = random.randint(2018, 2023)
        Y2 = Y1 + 1

        n = 30 # Cố định n=30 ngày trong tháng 6

        # ---------------- BỘ SỐ NĂM Y1 ----------------
        # Yêu cầu: Q1 thuộc [32;34), Q3 thuộc [38;40), R1 = 40 - 30 = 10
        a1 = 0
        a2 = random.randint(1, 4)
        a3 = random.randint(8 - a2, 9) # Đảm bảo a2 + a3 > 7.5
        a6 = random.randint(8, 12)     # Đảm bảo tổng 5 nhóm đầu < 22.5
        rem1 = n - a1 - a2 - a3 - a6
        a4 = random.randint(2, rem1 - 2)
        a5 = rem1 - a4

        Q1_val_1 = sp.Rational(32) + sp.Rational(sp.Rational(30, 4) - a2, a3) * 2
        Q3_val_1 = sp.Rational(38) + sp.Rational(sp.Rational(90, 4) - (a2+a3+a4+a5), a6) * 2
        Delta_Q1 = Q3_val_1 - Q1_val_1
        R1 = 10

        # ---------------- BỘ SỐ NĂM Y2 ----------------
        # Yêu cầu: Q1 thuộc [32;34), Q3 thuộc [36;38), R2 = 40 - 28 = 12
        b1 = random.randint(1, 3)
        b2 = random.randint(1, 4)
        if b1 + b2 > 7: b2 = 7 - b1 # Đảm bảo b1 + b2 < 7.5
        b3 = random.randint(8 - (b1+b2), 7) # Đảm bảo b1 + b2 + b3 > 7.5
        b6 = random.randint(1, 3)
        b5 = random.randint(7, 9) # Đảm bảo b5 + b6 > 7.5 -> 4 nhóm đầu < 22.5
        b4 = n - b1 - b2 - b3 - b5 - b6

        Q1_val_2 = sp.Rational(32) + sp.Rational(sp.Rational(30, 4) - (b1+b2), b3) * 2
        Q3_val_2 = sp.Rational(36) + sp.Rational(sp.Rational(90, 4) - (b1+b2+b3+b4), b5) * 2
        Delta_Q2 = Q3_val_2 - Q1_val_2
        R2 = 12

        # So sánh R và Delta Q
        comp_R = f"Vì $R_2 > R_1$ nên nhiệt độ cao nhất trong ngày vào tháng 6 năm {Y2} biến đổi nhiều hơn nhiệt độ cao nhất trong ngày vào tháng 6 năm {Y1}." if R2 > R1 else f"Vì $R_1 > R_2$ nên nhiệt độ cao nhất trong ngày vào tháng 6 năm {Y1} biến đổi nhiều hơn nhiệt độ cao nhất trong ngày vào tháng 6 năm {Y2}."

        comp_DQ = f"Theo khoảng tứ phân vị: vì $\\Delta_{{Q_1}} > \\Delta_{{Q_2}}$ nên nhiệt độ cao nhất trong ngày vào tháng 6 năm {Y1} biến đổi nhiều hơn nhiệt độ cao nhất trong ngày vào tháng 6 năm {Y2}." if float(Delta_Q1) > float(Delta_Q2) else f"Theo khoảng tứ phân vị: vì $\\Delta_{{Q_2}} > \\Delta_{{Q_1}}$ nên nhiệt độ cao nhất trong ngày vào tháng 6 năm {Y2} biến đổi nhiều hơn nhiệt độ cao nhất trong ngày vào tháng 6 năm {Y1}."

        # Đề bài
        noidungcauhoi = f"""Thống kê số ngày trong tháng Sáu năm {Y1} và năm {Y2} theo nhiệt độ cao nhất trong ngày tại Hà Nội, người ta thu được bảng sau:
    \\begin{{center}}
    \\begin{{tabular}}{{|c|c|c|c|c|c|c|}}
    \\hline
    Nhiệt độ ($^\\circ C$) & $[28;30)$ & $[30;32)$ & $[32;34)$ & $[34;36)$ & $[36;38)$ & $[38;40)$ \\\\
    \\hline
    Số ngày trong tháng 6/{Y1} & ${a1}$ & ${a2}$ & ${a3}$ & ${a4}$ & ${a5}$ & ${a6}$ \\\\
    \\hline
    Số ngày trong tháng 6/{Y2} & ${b1}$ & ${b2}$ & ${b3}$ & ${b4}$ & ${b5}$ & ${b6}$ \\\\
    \\hline
    \\end{{tabular}}
    \\end{{center}}
    Hỏi tháng sáu năm nào ở Hà Nội nhiệt độ cao nhất trong ngày biến đổi nhiều hơn?"""

        # Nội dung lời giải
        loigiai = f"""Năm {Y1}: Khoảng biến thiên của nhiệt độ là: $R_1 = 40 - 30 = {R1}$
    Cỡ mẫu $n = 30$. Giả sử $y_1, y_2, \\dots, y_{{30}}$ là nhiệt độ cao nhất trong ngày của $30$ ngày tháng Sáu năm {Y1} và giả sử dãy số liệu gốc này đã được sắp xếp theo thứ tự không giảm.
    Vì $\\frac{{n}}{{4}} = \\frac{{30}}{{4}} = 7,5$ và ${a2} < 7,5 < {a2} + {a3}$ nên tứ phân vị thứ nhất thuộc nhóm $[32;34)$ và tứ phân vị thứ nhất là: 
    $$Q_1 = 32 + \\frac{{\\frac{{30}}{{4}} - {a2}}}{{{a3}}} \\cdot 2 = {to_str(Q1_val_1)}$$
    vì $\\frac{{3n}}{{4}} = \\frac{{3 \\cdot 30}}{{4}} = 22,5$ và ${a2}+{a3}+{a4}+{a5} < 22,5 < {a2}+{a3}+{a4}+{a5}+{a6}$ nên tứ phân vị thứ ba thuộc nhóm $[38;40)$ và tứ phân vị thứ ba là: 
    $$Q_3 = 38 + \\frac{{\\frac{{3 \\cdot 30}}{{4}} - ({a2}+{a3}+{a4}+{a5})}}{{{a6}}} \\cdot 2 = {to_str(Q3_val_1)}$$
    Khoảng biến thiên của mẫu số liệu ghép nhóm là: $\\Delta_{{Q_1}} = {to_str(Q3_val_1)} - {to_str(Q1_val_1)} = {to_str(Delta_Q1)}$
    Năm {Y2}: Khoảng biến thiên của nhiệt độ là: $R_2 = 40 - 28 = {R2}$
    Cỡ mẫu $n = 30$. Giả sử $z_1, z_2, \\dots, z_{{30}}$ là nhiệt độ cao nhất trong ngày của $30$ ngày tháng Sáu năm {Y2} và giả sử dãy số liệu gốc này đã được sắp xếp theo thứ tự tăng dần.
    vì $\\frac{{n}}{{4}} = \\frac{{30}}{{4}} = 7,5$ và ${b1}+{b2} < 7,5 < {b1}+{b2}+{b3}$ nên nhóm chứa tứ phân vị thứ nhất là nhóm $[32;34)$ và tứ phân vị thứ nhất là: 
    $$Q'_1 = 32 + \\frac{{\\frac{{30}}{{4}} - ({b1}+{b2})}}{{{b3}}} \\cdot (34 - 32) = {to_str(Q1_val_2)}$$
    vì $\\frac{{3n}}{{4}} = \\frac{{3 \\cdot 30}}{{4}} = 22,5$ và ${b1}+{b2}+{b3}+{b4} < 22,5 < {b1}+{b2}+{b3}+{b4}+{b5}$ nên nhóm chứa tứ phân vị thứ ba là nhóm $[36;38)$ và tứ phân vị thứ ba là: 
    $$Q'_3 = 36 + \\frac{{\\frac{{3 \\cdot 30}}{{4}} - ({b1}+{b2}+{b3}+{b4})}}{{{b5}}} \\cdot (38 - 36) = {to_str(Q3_val_2)}$$
    Khoảng biến thiên của mẫu số liệu ghép nhóm là: $\\Delta_{{Q_2}} = {to_str(Q3_val_2)} - {to_str(Q1_val_2)} = {to_str(Delta_Q2)}$
    Theo khoảng biến thiên: {comp_R}
    {comp_DQ}"""

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\n\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content


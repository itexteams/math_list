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


def bt_dang12_p4_b1_c2_ds12(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)

    if dang=='1':
        # Random bước nhảy (độ rộng khoảng) và giá trị bắt đầu
        step = random.choice([5, 10])
        start = random.choice([10, 15, 20])

        # Random số lượng (tần số) cho 5 nhóm
        c1 = random.randint(4, 8)
        c2 = random.randint(4, 8)
        c3 = random.randint(2, 6)
        c4 = random.randint(1, 3)
        c5 = random.randint(1, 3)

        parts = [c1, c2, c3, c4, c5]
        n = sum(parts)

        intervals = []
        interval_bounds = []
        for i in range(5):
            lower = start + i*step
            upper = start + (i+1)*step
            intervals.append(f"[{lower};{upper})")
            interval_bounds.append((lower, upper))

        # --- Tìm Q1 ---
        q1_pos = n / 4
        cf_q1 = 0
        q1_group_index = -1
        cf_prev_q1 = 0

        for i, count in enumerate(parts):
            cf_prev_q1 = cf_q1
            cf_q1 += count
            if cf_q1 >= q1_pos:
                q1_group_index = i
                break

        L_Q1 = interval_bounds[q1_group_index][0]
        U_Q1 = interval_bounds[q1_group_index][1]
        f_Q1 = parts[q1_group_index]

        Q1_val = L_Q1 + ((q1_pos - cf_prev_q1) / f_Q1) * step

        # --- Tìm Q3 ---
        q3_pos = (3 * n) / 4
        cf_q3 = 0
        q3_group_index = -1
        cf_prev_q3 = 0

        for i, count in enumerate(parts):
            cf_prev_q3 = cf_q3
            cf_q3 += count
            if cf_q3 >= q3_pos:
                q3_group_index = i
                break

        L_Q3 = interval_bounds[q3_group_index][0]
        U_Q3 = interval_bounds[q3_group_index][1]
        f_Q3 = parts[q3_group_index]

        Q3_val = L_Q3 + ((q3_pos - cf_prev_q3) / f_Q3) * step

        # --- Tính khoảng tứ phân vị ---
        delta_Q = Q3_val - Q1_val

        def fmt_num(num):
            if num == int(num):
                return str(int(num))
            # Remove trailing zeros after decimal point if they exist
            return "{:g}".format(float(num)).replace('.', ',')

        kq_dung_str = fmt_num(delta_Q)
        q1_str = fmt_num(Q1_val)
        q3_str = fmt_num(Q3_val)
        # Câu hỏi
        noidungcauhoi = ('''Bạn Chi rất thích nhảy hiện đại. Thời gian tập nhảy mỗi ngày trong thời gian gần đây của bạn Chi được thống kê lại ở bảng sau:
        \\begin{center}
        \\begin{tabular}{|c|c|c|c|c|c|}
        \\hline
        Thời gian (phút) & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\
        \\hline
        Số ngày & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\
        \\hline
        \\end{tabular}
        \\end{center}
        Tìm khoảng tứ phân vị của mẫu số liệu ghép nhóm'''
                         %(intervals[0], intervals[1], intervals[2], intervals[3], intervals[4],
                           latex(c1), latex(c2), latex(c3), latex(c4), latex(c5)
                         ))

        # Nội dung lời giải
        # Vị trí mẫu số liệu
        idx_q1 = int(n/4) + 1 if n % 4 != 0 else int(n/4)
        idx_q3 = int(3*n/4) + 1 if (3*n) % 4 != 0 else int(3*n/4)

        loigiai=('''Cỡ mẫu $n = %s$\\\\
        Gọi $x_1; x_2; \\dots; x_{%s}$ là mẫu số liệu gốc về thời gian tập nhảy mỗi ngày của bạn Chi được xếp theo thứ tự không giảm.\\\\
        Tứ phân vị thứ nhất của mẫu số liệu gốc là $x_{%s} \\in %s$. Do đó, tứ phân vị thứ nhất của mẫu số liệu ghép nhóm là: $Q_1 = %s + \\frac{\\frac{%s}{4} - %s}{%s}(%s - %s) = %s$\\\\
        Tứ phân vị thứ ba của mẫu số liệu gốc là $x_{%s} \\in %s$. Do đó, tứ phân vị thứ ba của mẫu số liệu ghép nhóm là: $Q_3 = %s + \\frac{\\frac{3 \\cdot %s}{4} - %s}{%s}(%s - %s) = %s$\\\\
        Khoảng tứ phân vị của mẫu số liệu ghép nhóm là: $\\Delta_Q = Q_3 - Q_1 = %s$'''
                 %(latex(n), latex(n),
                   idx_q1, intervals[q1_group_index], L_Q1, latex(n), fmt_num(cf_prev_q1), f_Q1, U_Q1, L_Q1, q1_str,
                   idx_q3, intervals[q3_group_index], L_Q3, latex(n), fmt_num(cf_prev_q3), f_Q3, U_Q3, L_Q3, q3_str,
                   kq_dung_str
                 ))
    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content


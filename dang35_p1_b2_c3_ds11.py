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


def bt_dang35_p1_b2_c3_ds11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Khởi tạo độ rộng khoảng ngẫu nhiên (ví dụ 2, 4, 5)
        step = random.choice([2, 4, 5])
        start = random.choice([5, 10, 15])

        # Tạo 5 khoảng liên tiếp
        intervals = []
        interval_bounds = []
        for i in range(5):
            lower = start + i*step
            upper = start + (i+1)*step
            intervals.append(f"[{lower};{upper})")
            interval_bounds.append((lower, upper))

        # Tạo số lượng ngày ngẫu nhiên cho 5 nhóm
        c1 = random.randint(2, 5)
        c2 = random.randint(5, 10)
        c3 = random.randint(5, 10)
        c4 = random.randint(2, 5)
        c5 = random.randint(1, 3)

        parts = [c1, c2, c3, c4, c5]
        n = sum(parts)

        # Tính Q1
        q1_pos = n / 4

        cf = 0
        q1_group_index = -1
        cf_prev = 0

        for i, count in enumerate(parts):
            cf_prev = cf
            cf += count
            if cf >= q1_pos:
                q1_group_index = i
                break

        # Tính giá trị Q1
        L_Q1 = interval_bounds[q1_group_index][0]
        U_Q1 = interval_bounds[q1_group_index][1]
        f_Q1 = parts[q1_group_index]

        Q1_val = L_Q1 + ((q1_pos - cf_prev) / f_Q1) * step

        # Các lựa chọn đáp án
        # Đáp án đúng (làm tròn đến 1 chữ số thập phân)
        kq_dung_round = round(Q1_val, 1)

        # Định dạng các số hiển thị
        def fmt_num(num):
            if num == int(num):
                return str(int(num))
            return str(round(num, 2)).replace('.', ',')

        da = fmt_num(kq_dung_round)

        # Tạo đáp án sai
        sai_vals = [
            round(Q1_val - 0.4, 1),
            round(Q1_val + 0.4, 1),
            round(Q1_val + step/2, 1),
            round(L_Q1, 1),
            round(L_Q1 + step, 1)
        ]

        # Loại bỏ đáp án trùng
        sai_vals = list(set([v for v in sai_vals if v != kq_dung_round]))

        # Chọn 3 đáp án sai
        s = random.sample(sai_vals, 3)

        das1 = fmt_num(s[0])
        das2 = fmt_num(s[1])
        das3 = fmt_num(s[2])

        # Gán đáp án
        da_d = ('\\True $%s$' % da)
        da_s1 = '$%s$' % das1
        da_s2 = '$%s$' % das2
        da_s3 = '$%s$' % das3

        list_1 = [da_d,da_s1,da_s2,da_s3]
        random.shuffle(list_1)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Doanh thu bán hàng trong $%s$ ngày được lựa chọn ngẫu nhiên của một cửa hàng được ghi lại ở bảng sau (đơn vị: triệu đồng):
        \\begin{center}
        \\begin{tabular}{|c|c|c|c|c|c|}
        \\hline
        Doanh thu & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\
        \\hline
        Số ngày & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\
        \\hline
        \\end{tabular}
        \\end{center}
        Tứ phân vị thứ nhất của mẫu số liệu trên gần nhất với giá trị nào trong các giá trị sau?'''
                         %(latex(n),
                           intervals[0], intervals[1], intervals[2], intervals[3], intervals[4],
                           latex(c1), latex(c2), latex(c3), latex(c4), latex(c5)
                         ))

        # Lời giải
        # Vị trí Q1 trong dãy số liệu
        if n % 4 == 0:
            pos_str = f"\\frac{{1}}{{2}}(x_{{{int(n/4)}}} + x_{{{int(n/4) + 1}}})"
        else:
            pos_str = f"x_{{{int(n/4) + 1}}}"

        q1_val_str = fmt_num(Q1_val)
        n_div_4_str = fmt_num(n/4)

        loigiai=('''Tứ phân vị thứ nhất của dãy số liệu là $%s$ thuộc nhóm $%s$ nên tứ phân vị thứ nhất của mẫu số liệu là $Q_1 = %s + \\frac{\\frac{%s}{4} - %s}{%s}(%s - %s) = %s$'''
                 %(pos_str, intervals[q1_group_index], 
                   L_Q1, latex(n), cf_prev, f_Q1, U_Q1, L_Q1, q1_val_str
                 ))

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
        '\\choice \n'
        '{'+str(list_1[1])+'}\n'
        '{'+str(list_1[2])+'}\n'
        '{'+str(list_1[3])+'}\n'
        '{'+str(list_1[0])+'}\n'
        '\\loigiai{'+str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content


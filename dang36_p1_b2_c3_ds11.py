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


def bt_dang36_p1_b2_c3_ds11(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)

    if dang=='1':
        # Random bước nhảy (độ rộng khoảng) và giá trị bắt đầu
        step = random.choice([5, 10, 20])
        start = random.choice([0, 10, 20])

        # Random số lượng (tần số) cho 5 nhóm
        c1 = random.randint(3, 8)
        c2 = random.randint(7, 15)
        c3 = random.randint(15, 25)
        c4 = random.randint(8, 15)
        c5 = random.randint(2, 7)

        parts = [c1, c2, c3, c4, c5]
        n = sum(parts)

        intervals = []
        interval_bounds = []
        for i in range(5):
            lower = start + i*step
            upper = start + (i+1)*step
            intervals.append(f"[{lower};{upper})")
            interval_bounds.append((lower, upper))

        # Random yêu cầu tìm Q1 hoặc Q3
        loai_q = random.choice([1, 3])

        if loai_q == 1:
            text_q = "Tứ phân vị thứ nhất"
            pos = n / 4
            q_sym = "Q_1"
        else:
            text_q = "Tứ phân vị thứ ba"
            pos = 3 * n / 4
            q_sym = "Q_3"

        # Tính tần số tích lũy để tìm nhóm chứa Q
        cf = 0
        group_index = -1
        cf_prev = 0

        for i, count in enumerate(parts):
            cf_prev = cf
            cf += count
            if cf >= pos:
                group_index = i
                break

        # Các thông số của nhóm chứa Q
        L = interval_bounds[group_index][0]
        U = interval_bounds[group_index][1]
        f = parts[group_index]

        # Tính toán kết quả Q1 hoặc Q3
        Q_val = L + ((pos - cf_prev) / f) * step

        # Định dạng kết quả làm tròn 2 chữ số thập phân
        Q_val_round = round(Q_val, 2)

        def fmt_num(num):
            if num == int(num):
                return str(int(num))
            return str(round(num, 2)).replace('.', ',')

        kq_dung_str = fmt_num(Q_val_round)

        # Tạo các đáp án sai ngẫu nhiên
        sai_vals = [
            round(Q_val + 1.25, 2),
            round(Q_val - 1.25, 2),
            round(Q_val + step/2, 2),
            round(L + step/4, 2),
            round(Q_val - 0.85, 2),
            round(Q_val + 2.15, 2)
        ]

        # Lọc bỏ đáp án trùng với đáp án đúng
        sai_vals = list(set([v for v in sai_vals if v != Q_val_round]))
        s_choices = random.sample(sai_vals, 3)

        da = kq_dung_str
        das1 = fmt_num(s_choices[0])
        das2 = fmt_num(s_choices[1])
        das3 = fmt_num(s_choices[2])

        # Câu hỏi
        noidungcauhoi = ('''Khảo sát thời gian sử dụng internet trong ngày (phút) của một số học sinh thu được mẫu số liệu ghép nhóm sau:
        \\begin{center}
        \\begin{tabular}{|c|c|c|c|c|c|}
        \\hline
        Thời gian & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\
        \\hline
        Số học sinh & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\
        \\hline
        \\end{tabular}
        \\end{center}
        %s của mẫu số liệu trên gần nhất với giá trị nào trong các giá trị sau?'''
                         %(intervals[0], intervals[1], intervals[2], intervals[3], intervals[4],
                           latex(c1), latex(c2), latex(c3), latex(c4), latex(c5), text_q
                         ))

        # Các đáp án
        da_d = ('\\True $%s$' % da)
        da_s1 = '$%s$' % das1
        da_s2 = '$%s$' % das2
        da_s3 = '$%s$' % das3

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d,da_s1,da_s2,da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải
        if loai_q == 1:
            if n % 4 == 0:
                gt_pos = f"\\frac{{1}}{{2}}(x_{{{int(n/4)}}} + x_{{{int(n/4) + 1}}})"
            else:
                gt_pos = f"x_{{{int(n/4) + 1}}}"
            calc_str = f"\\frac{{{n}}}{{4}}"
        else:
            if (3*n) % 4 == 0:
                gt_pos = f"\\frac{{1}}{{2}}(x_{{{int(3*n/4)}}} + x_{{{int(3*n/4) + 1}}})"
            else:
                gt_pos = f"x_{{{int(3*n/4) + 1}}}"
            calc_str = f"\\frac{{3 \\cdot {n}}}{{4}}"

        loigiai=('''Cỡ mẫu $n = %s$.\\\\
        %s của dãy số liệu là $%s$ thuộc nhóm $%s$.\\\\
        Do đó, %s của mẫu số liệu ghép nhóm là:\\\\
        $%s = %s + \\frac{%s - %s}{%s} \\cdot %s \\approx %s$.'''
                 %(latex(n), text_q, gt_pos, intervals[group_index], text_q.lower(),
                   q_sym, latex(L), calc_str, latex(cf_prev), latex(f), latex(step), kq_dung_str
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


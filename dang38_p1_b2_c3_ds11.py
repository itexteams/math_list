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


def bt_dang38_p1_b2_c3_ds11(self):
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

        # Tính vị trí Q3
        q3_pos = (3 * n) / 4

        # Tính tần số tích lũy để tìm nhóm chứa Q3
        cf = 0
        q3_group_index = -1
        cf_prev = 0

        for i, count in enumerate(parts):
            cf_prev = cf
            cf += count
            if cf >= q3_pos:
                q3_group_index = i
                break

        # Tính giá trị Q3
        L_Q3 = interval_bounds[q3_group_index][0]
        U_Q3 = interval_bounds[q3_group_index][1]
        f_Q3 = parts[q3_group_index]

        Q3_val = L_Q3 + ((q3_pos - cf_prev) / f_Q3) * step

        # Làm tròn giá trị Q3 (tương tự như bài toán gốc làm tròn thành số nguyên trong đáp án)
        kq_dung_round = round(Q3_val)
        da = str(kq_dung_round)

        # Định dạng hiển thị Q3 trong lời giải (1 chữ số thập phân)
        q3_val_str = str(round(Q3_val, 1)).replace('.', ',')

        # Tạo đáp án sai (các số nguyên gần đó)
        sai_vals = [
            kq_dung_round - 1,
            kq_dung_round + 1,
            kq_dung_round + 2,
            kq_dung_round - 2,
            kq_dung_round + 3
        ]

        # Lấy 3 đáp án sai duy nhất
        sai_vals = list(set([v for v in sai_vals if v != kq_dung_round]))
        s = random.sample(sai_vals, 3)

        das1 = str(s[0])
        das2 = str(s[1])
        das3 = str(s[2])

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
        Tứ phân vị thứ ba của mẫu số liệu trên gần nhất với giá trị nào trong các giá trị sau?'''
                         %(latex(n),
                           intervals[0], intervals[1], intervals[2], intervals[3], intervals[4],
                           latex(c1), latex(c2), latex(c3), latex(c4), latex(c5)
                         ))

        # Lời giải
        # Vị trí Q3 trong dãy số liệu
        pos1 = int((3*n)/4)
        pos2 = pos1 + 1

        if n % 4 == 0:
            pos_str = f"\\frac{{1}}{{2}}(x_{{{pos1}}} + x_{{{pos2}}})"
        else:
            # Nếu (3n/4) không nguyên, lấy phần nguyên + 1
            idx = int(q3_pos) + 1
            pos_str = f"x_{{{idx}}}"

        # Định dạng các số trong công thức
        n_str = latex(n)
        cf_prev_str = latex(cf_prev)
        f_q3_str = latex(f_Q3)

        loigiai=('''Tứ phân vị thứ ba của dãy số liệu là $%s$ thuộc nhóm $%s$ nên tứ phân vị thứ ba của mẫu số liệu là $Q_3 = %s + \\frac{\\frac{3 \\cdot %s}{4} - %s}{%s}(%s - %s) \\approx %s$'''
                 %(pos_str, intervals[q3_group_index], 
                   L_Q3, n_str, cf_prev_str, f_q3_str, U_Q3, L_Q3, q3_val_str
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


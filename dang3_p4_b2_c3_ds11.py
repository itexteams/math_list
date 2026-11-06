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


def bt_dang3_p4_b2_c3_ds11(self):
            # Khai báo biến
            #lisdang=['1','2','3','4']
            lisdang=['2']
            dang=random.choice(lisdang)

            if dang=='4': #tổng chữn - chia đôi hai bên lẻ
                # Khai báo biến
                lisv=[45,50,55,60,65]
                v = random.choice(lisv)

                # Vòng lặp để tạo tổng thỏa mãn điều kiện
                while True:
                    xe1, xe2, xe3, xe4, xe5 = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)
                    tong = xe1 + xe2 + xe3 + xe4 + xe5
                    tong1 = tong / 2

                    # Kiểm tra điều kiện thoát vòng lặp
                    if tong % 2 == 0 and tong1 % 2 != 0:
                        break

                # Chọn giá trị k ngẫu nhiên
                lisk=[5,10,15,20]
                k = random.choice(lisk)

                # Tạo danh sách số liệu gốc
                data = []
                data.extend([v] * xe1)
                data.extend([v + k] * xe2)
                data.extend([v + 2 * k] * xe3)
                data.extend([v + 3 * k] * xe4)
                data.extend([v + 4 * k] * xe5)

                # Sắp xếp danh sách
                data.sort()

                # Tính toán vị trí Q1
                n = len(data)
                Q1_index = (n + 1) / 4

                if Q1_index.is_integer():
                    Q1 = data[int(Q1_index) - 1]
                else:
                    lower_index = int(Q1_index) - 1
                    upper_index = lower_index + 1
                    Q1 = (data[lower_index] + data[upper_index]) / 2

                # Tính toán vị trí Q2 (Median)
                Q2_index = (n + 1) / 2

                if Q2_index.is_integer():
                    Q2 = data[int(Q2_index) - 1]
                else:
                    lower_index = int(Q2_index) - 1
                    upper_index = lower_index + 1
                    Q2 = (data[lower_index] + data[upper_index]) / 2

                # Tính toán vị trí Q3
                Q3_index = 3 * (n + 1) / 4

                if Q3_index.is_integer():
                    Q3 = data[int(Q3_index) - 1]
                else:
                    lower_index = int(Q3_index) - 1
                    upper_index = lower_index + 1
                    Q3 = (data[lower_index] + data[upper_index]) / 2

                # Tạo danh sách các khoảng và tần số tương ứng
                intervals = [(v, v + k), (v + k, v + 2 * k), (v + 2 * k, v + 3 * k), (v + 3 * k, v + 4 * k), (v + 4 * k, v + 5 * k)]
                frequencies = [xe1, xe2, xe3, xe4, xe5]

                # Tìm khoảng chứa Q1, Q2 và Q3
                Q1_interval, Q2_interval, Q3_interval = None, None, None
                Q1_interval_index, Q2_interval_index, Q3_interval_index = None, None, None

                for i, (start, end) in enumerate(intervals):
                    if start <= Q1 < end:
                        Q1_interval = (start, end)
                        Q1_interval_index = i
                    if start <= Q2 < end:
                        Q2_interval = (start, end)
                        Q2_interval_index = i
                    if start <= Q3 < end:
                        Q3_interval = (start, end)
                        Q3_interval_index = i

                # Tính tổng tần số đến trước khoảng chứa Q1, Q2 và Q3
                total_freq_before_Q1 = sum(frequencies[:Q1_interval_index]) if Q1_interval_index is not None else 0
                total_freq_before_Q2 = sum(frequencies[:Q2_interval_index]) if Q2_interval_index is not None else 0
                total_freq_before_Q3 = sum(frequencies[:Q3_interval_index]) if Q3_interval_index is not None else 0

                # Tìm tần số tương ứng với khoảng chứa Q1, Q2 và Q3
                Q1_interval_frequency = frequencies[Q1_interval_index] if Q1_interval_index is not None else 0
                Q2_interval_frequency = frequencies[Q2_interval_index] if Q2_interval_index is not None else 0
                Q3_interval_frequency = frequencies[Q3_interval_index] if Q3_interval_index is not None else 0

                # Tính toán kết quả Q1, Q2 và Q3
                kqQ1 = Q1_interval[0] + Rational(1 * n / 4 - total_freq_before_Q1, Q1_interval_frequency) * (Q1_interval[1] - Q1_interval[0])
                kqQ2 = Q2_interval[0] + Rational(2 * n / 4 - total_freq_before_Q2, Q2_interval_frequency) * (Q2_interval[1] - Q2_interval[0])
                kqQ3 = Q3_interval[0] + Rational(3 * n / 4 - total_freq_before_Q3, Q3_interval_frequency) * (Q3_interval[1] - Q3_interval[0])

                # Kết quả
                kq = kqQ3 - kqQ1

                h1=kqQ2
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho mẫu số liệu ghép nhóm sau \n'
                                '\\begin{center} \n'
                                '\\begin{tabular}{|c|c|c|c|c|c|} \n'
                                '\\hline \n'
                                'Giá trị & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ \\\\ \n'
                                '\\hline \n'
                                'Tần số & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '\\end{tabular} \n'
                                '\\end{center} \n'
                                'Tìm trung vị của mẫu số liệu bằng$zz$'
                                %(
                                latex(v),latex(v+k),latex(v+k),latex(v+2*k),latex(v+2*k),latex(v+3*k),latex(v+3*k),latex(v+4*k),latex(v+4*k),latex(v+5*k),
                                latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5),

                                ))

                # Nội dung lời giải
                loigiai=('Cỡ mẫu $n=%s$. Giả sử $x_1, x_2, $zz$$zz$$zz$, x_{%s}$ là số $%s$ giá trị và giả sử dãy số liệu gốc này được sắp xếp theo thứ tự không giảm$zz$ \\\\ \n'

                        'Vì $n=%s$ nên trung vị của mẫu số liệu là $M_e=\\dfrac{x_{%s}+x_{%s}}{2}$ thuộc nhóm $[%s;%s)$$zz$ \\\\ \n'
                        '\\hspace*{1cm} Do đó, trung vị là \\\\ \n'
                        '\\hspace*{1cm} $M_e=%s+\\dfrac{\\frac{%s}{2}-%s}{%s} \\cdot %s=%s$$zz$'

                        %(latex(tong),latex(tong),latex(tong),

                        latex(n),latex(n/2),latex(n/2+1),latex(Q2_interval[0]),latex(Q2_interval[1]),
                        latex(Q2_interval[0]),latex(n),latex(total_freq_before_Q2),latex(Q2_interval_frequency),latex(Q2_interval[1]-Q2_interval[0]),latex(kqQ2),

                        ))


            if dang=='3': #tổng chữn - chia đôi hai bên chẵn
                # Khai báo biến
                lisv=[45,50,55,60,65]
                v = random.choice(lisv)

                # Vòng lặp để tạo tổng thỏa mãn điều kiện
                while True:
                    xe1, xe2, xe3, xe4, xe5 = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)
                    tong = xe1 + xe2 + xe3 + xe4 + xe5
                    tong1 = tong / 2

                    # Kiểm tra điều kiện thoát vòng lặp
                    if tong % 2 == 0 and tong1 % 2 == 0:
                        break

                # Chọn giá trị k ngẫu nhiên
                lisk=[5,10,15,20]
                k = random.choice(lisk)

                # Tạo danh sách số liệu gốc
                data = []
                data.extend([v] * xe1)
                data.extend([v + k] * xe2)
                data.extend([v + 2 * k] * xe3)
                data.extend([v + 3 * k] * xe4)
                data.extend([v + 4 * k] * xe5)

                # Sắp xếp danh sách
                data.sort()

                # Tính toán vị trí Q1
                n = len(data)
                Q1_index = (n + 1) / 4

                if Q1_index.is_integer():
                    Q1 = data[int(Q1_index) - 1]
                else:
                    lower_index = int(Q1_index) - 1
                    upper_index = lower_index + 1
                    Q1 = (data[lower_index] + data[upper_index]) / 2

                # Tính toán vị trí Q2 (Median)
                Q2_index = (n + 1) / 2

                if Q2_index.is_integer():
                    Q2 = data[int(Q2_index) - 1]
                else:
                    lower_index = int(Q2_index) - 1
                    upper_index = lower_index + 1
                    Q2 = (data[lower_index] + data[upper_index]) / 2

                # Tính toán vị trí Q3
                Q3_index = 3 * (n + 1) / 4

                if Q3_index.is_integer():
                    Q3 = data[int(Q3_index) - 1]
                else:
                    lower_index = int(Q3_index) - 1
                    upper_index = lower_index + 1
                    Q3 = (data[lower_index] + data[upper_index]) / 2

                # Tạo danh sách các khoảng và tần số tương ứng
                intervals = [(v, v + k), (v + k, v + 2 * k), (v + 2 * k, v + 3 * k), (v + 3 * k, v + 4 * k), (v + 4 * k, v + 5 * k)]
                frequencies = [xe1, xe2, xe3, xe4, xe5]

                # Tìm khoảng chứa Q1, Q2 và Q3
                Q1_interval, Q2_interval, Q3_interval = None, None, None
                Q1_interval_index, Q2_interval_index, Q3_interval_index = None, None, None

                for i, (start, end) in enumerate(intervals):
                    if start <= Q1 < end:
                        Q1_interval = (start, end)
                        Q1_interval_index = i
                    if start <= Q2 < end:
                        Q2_interval = (start, end)
                        Q2_interval_index = i
                    if start <= Q3 < end:
                        Q3_interval = (start, end)
                        Q3_interval_index = i

                # Tính tổng tần số đến trước khoảng chứa Q1, Q2 và Q3
                total_freq_before_Q1 = sum(frequencies[:Q1_interval_index]) if Q1_interval_index is not None else 0
                total_freq_before_Q2 = sum(frequencies[:Q2_interval_index]) if Q2_interval_index is not None else 0
                total_freq_before_Q3 = sum(frequencies[:Q3_interval_index]) if Q3_interval_index is not None else 0

                # Tìm tần số tương ứng với khoảng chứa Q1, Q2 và Q3
                Q1_interval_frequency = frequencies[Q1_interval_index] if Q1_interval_index is not None else 0
                Q2_interval_frequency = frequencies[Q2_interval_index] if Q2_interval_index is not None else 0
                Q3_interval_frequency = frequencies[Q3_interval_index] if Q3_interval_index is not None else 0

                # Tính toán kết quả Q1, Q2 và Q3
                kqQ1 = Q1_interval[0] + Rational(1 * n / 4 - total_freq_before_Q1, Q1_interval_frequency) * (Q1_interval[1] - Q1_interval[0])
                kqQ2 = Q2_interval[0] + Rational(2 * n / 4 - total_freq_before_Q2, Q2_interval_frequency) * (Q2_interval[1] - Q2_interval[0])
                kqQ3 = Q3_interval[0] + Rational(3 * n / 4 - total_freq_before_Q3, Q3_interval_frequency) * (Q3_interval[1] - Q3_interval[0])

                # Kết quả
                kq = kqQ3 - kqQ1

                h1=kqQ2
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho mẫu số liệu ghép nhóm sau \n'
                                '\\begin{center} \n'
                                '\\begin{tabular}{|c|c|c|c|c|c|} \n'
                                '\\hline \n'
                                'Giá trị & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ \\\\ \n'
                                '\\hline \n'
                                'Tần số & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '\\end{tabular} \n'
                                '\\end{center} \n'
                                'Tìm trung vị của mẫu số liệu bằng$zz$'
                                %(
                                latex(v),latex(v+k),latex(v+k),latex(v+2*k),latex(v+2*k),latex(v+3*k),latex(v+3*k),latex(v+4*k),latex(v+4*k),latex(v+5*k),
                                latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5),

                                ))

                # Nội dung lời giải
                loigiai=('Cỡ mẫu $n=%s$. Giả sử $x_1, x_2, $zz$$zz$$zz$, x_{%s}$ là số $%s$ giá trị và giả sử dãy số liệu gốc này được sắp xếp theo thứ tự không giảm$zz$ \\\\ \n'
                        'Vì $n=%s$ nên trung vị của mẫu số liệu là $M_e=\\dfrac{x_{%s}+x_{%s}}{2}$ thuộc nhóm $[%s;%s)$$zz$ \\\\ \n'
                        '\\hspace*{1cm} Do đó, trung vị là \\\\ \n'
                        '\\hspace*{1cm} $M_e=%s+\\dfrac{\\frac{%s}{2}-%s}{%s} \\cdot %s=%s$$zz$'

                        %(latex(tong),latex(tong),latex(tong),

                        latex(n),latex(n/2),latex(n/2+1),latex(Q2_interval[0]),latex(Q2_interval[1]),
                        latex(Q2_interval[0]),latex(n),latex(total_freq_before_Q2),latex(Q2_interval_frequency),latex(Q2_interval[1]-Q2_interval[0]),latex(kqQ2)

                        ))


            if dang=='2': #tổng lẻ - chia đôi hai bên lẻ
                # Khai báo biến
                lisv=[45,50,55,60,65]
                v = random.choice(lisv)

                # Vòng lặp để tạo tổng thỏa mãn điều kiện
                while True:
                    xe1, xe2, xe3, xe4, xe5 = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)
                    tong = xe1 + xe2 + xe3 + xe4 + xe5
                    tong1 = (tong - 1) / 2

                    # Kiểm tra điều kiện thoát vòng lặp
                    if tong % 2 != 0 and tong1 % 2 != 0:
                        break

                # Chọn giá trị k ngẫu nhiên
                lisk=[5,10,15,20]
                k = random.choice(lisk)

                # Tạo danh sách số liệu gốc
                data = []
                data.extend([v] * xe1)
                data.extend([v + k] * xe2)
                data.extend([v + 2 * k] * xe3)
                data.extend([v + 3 * k] * xe4)
                data.extend([v + 4 * k] * xe5)

                # Sắp xếp danh sách
                data.sort()

                # Tính toán vị trí Q1
                n = len(data)
                Q1_index = (n + 1) / 4

                if Q1_index.is_integer():
                    Q1 = data[int(Q1_index) - 1]
                else:
                    lower_index = int(Q1_index) - 1
                    upper_index = lower_index + 1
                    Q1 = (data[lower_index] + data[upper_index]) / 2

                # Tính toán vị trí Q2 (Median)
                Q2_index = (n + 1) / 2

                if Q2_index.is_integer():
                    Q2 = data[int(Q2_index) - 1]
                else:
                    lower_index = int(Q2_index) - 1
                    upper_index = lower_index + 1
                    Q2 = (data[lower_index] + data[upper_index]) / 2

                # Tính toán vị trí Q3
                Q3_index = 3 * (n + 1) / 4

                if Q3_index.is_integer():
                    Q3 = data[int(Q3_index) - 1]
                else:
                    lower_index = int(Q3_index) - 1
                    upper_index = lower_index + 1
                    Q3 = (data[lower_index] + data[upper_index]) / 2

                # Tạo danh sách các khoảng và tần số tương ứng
                intervals = [(v, v + k), (v + k, v + 2 * k), (v + 2 * k, v + 3 * k), (v + 3 * k, v + 4 * k), (v + 4 * k, v + 5 * k)]
                frequencies = [xe1, xe2, xe3, xe4, xe5]

                # Tìm khoảng chứa Q1, Q2 và Q3
                Q1_interval, Q2_interval, Q3_interval = None, None, None
                Q1_interval_index, Q2_interval_index, Q3_interval_index = None, None, None

                for i, (start, end) in enumerate(intervals):
                    if start <= Q1 < end:
                        Q1_interval = (start, end)
                        Q1_interval_index = i
                    if start <= Q2 < end:
                        Q2_interval = (start, end)
                        Q2_interval_index = i
                    if start <= Q3 < end:
                        Q3_interval = (start, end)
                        Q3_interval_index = i

                # Tính tổng tần số đến trước khoảng chứa Q1, Q2 và Q3
                total_freq_before_Q1 = sum(frequencies[:Q1_interval_index]) if Q1_interval_index is not None else 0
                total_freq_before_Q2 = sum(frequencies[:Q2_interval_index]) if Q2_interval_index is not None else 0
                total_freq_before_Q3 = sum(frequencies[:Q3_interval_index]) if Q3_interval_index is not None else 0

                # Tìm tần số tương ứng với khoảng chứa Q1, Q2 và Q3
                Q1_interval_frequency = frequencies[Q1_interval_index] if Q1_interval_index is not None else 0
                Q2_interval_frequency = frequencies[Q2_interval_index] if Q2_interval_index is not None else 0
                Q3_interval_frequency = frequencies[Q3_interval_index] if Q3_interval_index is not None else 0

                # Tính toán kết quả Q1, Q2 và Q3
                kqQ1 = Q1_interval[0] + Rational(1 * n / 4 - total_freq_before_Q1, Q1_interval_frequency) * (Q1_interval[1] - Q1_interval[0])
                kqQ2 = Q2_interval[0] + Rational(2 * n / 4 - total_freq_before_Q2, Q2_interval_frequency) * (Q2_interval[1] - Q2_interval[0])
                kqQ3 = Q3_interval[0] + Rational(3 * n / 4 - total_freq_before_Q3, Q3_interval_frequency) * (Q3_interval[1] - Q3_interval[0])

                # Kết quả
                kq = kqQ3 - kqQ1

                h1=kqQ2
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho mẫu số liệu ghép nhóm sau \n'
                                '\\begin{center} \n'
                                '\\begin{tabular}{|c|c|c|c|c|c|} \n'
                                '\\hline \n'
                                'Giá trị & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ \\\\ \n'
                                '\\hline \n'
                                'Tần số & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '\\end{tabular} \n'
                                '\\end{center} \n'
                                'Tìm trung vị của mẫu số liệu$zz$'
                                %(
                                latex(v),latex(v+k),latex(v+k),latex(v+2*k),latex(v+2*k),latex(v+3*k),latex(v+3*k),latex(v+4*k),latex(v+4*k),latex(v+5*k),
                                latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5),

                                ))

                # Nội dung lời giải
                loigiai=('Cỡ mẫu $n=%s$. Giả sử $x_1, x_2, $zz$$zz$$zz$, x_{%s}$ là số $%s$ giá trị và giả sử dãy số liệu gốc này được sắp xếp theo thứ tự không giảm$zz$ \\\\ \n'
                        'Vì $n=%s$ nên trung vị của mẫu số liệu là $M_e=x_{%s}$ thuộc nhóm $[%s;%s)$$zz$ \\\\ \n'
                        '\\hspace*{1cm} Do đó, trung vị là \\\\ \n'
                        '\\hspace*{1cm} $M_e=%s+\\dfrac{\\frac{%s}{2}-%s}{%s} \\cdot %s=%s$$zz$'

                        %(latex(tong),latex(tong),latex(tong),
                        latex(n),latex((n+1)/2),latex(Q2_interval[0]),latex(Q2_interval[1]),
                        latex(Q2_interval[0]),latex(n),latex(total_freq_before_Q2),latex(Q2_interval_frequency),latex(Q2_interval[1]-Q2_interval[0]),latex(kqQ2)

                        ))


            if dang=='1': #tổng lẻ - chia đôi hai bên chẵn
                # Khai báo biến
                lisv=[45,50,55,60,65]
                v = random.choice(lisv)

                # Vòng lặp để tạo tổng thỏa mãn điều kiện
                while True:
                    xe1, xe2, xe3, xe4, xe5 = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)
                    tong = xe1 + xe2 + xe3 + xe4 + xe5
                    tong1 = (tong - 1) / 2

                    # Kiểm tra điều kiện thoát vòng lặp
                    if tong % 2 != 0 and tong1 % 2 == 0:
                        break

                # Chọn giá trị k ngẫu nhiên
                lisk=[5,10,15,20]
                k = random.choice(lisk)

                # Tạo danh sách số liệu gốc
                data = []
                data.extend([v] * xe1)
                data.extend([v + k] * xe2)
                data.extend([v + 2 * k] * xe3)
                data.extend([v + 3 * k] * xe4)
                data.extend([v + 4 * k] * xe5)

                # Sắp xếp danh sách
                data.sort()

                # Tính toán vị trí Q1
                n = len(data)
                Q1_index = (n + 1) / 4

                if Q1_index.is_integer():
                    Q1 = data[int(Q1_index) - 1]
                else:
                    lower_index = int(Q1_index) - 1
                    upper_index = lower_index + 1
                    Q1 = (data[lower_index] + data[upper_index]) / 2

                # Tính toán vị trí Q2 (Median)
                Q2_index = (n + 1) / 2

                if Q2_index.is_integer():
                    Q2 = data[int(Q2_index) - 1]
                else:
                    lower_index = int(Q2_index) - 1
                    upper_index = lower_index + 1
                    Q2 = (data[lower_index] + data[upper_index]) / 2

                # Tính toán vị trí Q3
                Q3_index = 3 * (n + 1) / 4

                if Q3_index.is_integer():
                    Q3 = data[int(Q3_index) - 1]
                else:
                    lower_index = int(Q3_index) - 1
                    upper_index = lower_index + 1
                    Q3 = (data[lower_index] + data[upper_index]) / 2

                # Tạo danh sách các khoảng và tần số tương ứng
                intervals = [(v, v + k), (v + k, v + 2 * k), (v + 2 * k, v + 3 * k), (v + 3 * k, v + 4 * k), (v + 4 * k, v + 5 * k)]
                frequencies = [xe1, xe2, xe3, xe4, xe5]

                # Tìm khoảng chứa Q1, Q2 và Q3
                Q1_interval, Q2_interval, Q3_interval = None, None, None
                Q1_interval_index, Q2_interval_index, Q3_interval_index = None, None, None

                for i, (start, end) in enumerate(intervals):
                    if start <= Q1 < end:
                        Q1_interval = (start, end)
                        Q1_interval_index = i
                    if start <= Q2 < end:
                        Q2_interval = (start, end)
                        Q2_interval_index = i
                    if start <= Q3 < end:
                        Q3_interval = (start, end)
                        Q3_interval_index = i

                # Tính tổng tần số đến trước khoảng chứa Q1, Q2 và Q3
                total_freq_before_Q1 = sum(frequencies[:Q1_interval_index]) if Q1_interval_index is not None else 0
                total_freq_before_Q2 = sum(frequencies[:Q2_interval_index]) if Q2_interval_index is not None else 0
                total_freq_before_Q3 = sum(frequencies[:Q3_interval_index]) if Q3_interval_index is not None else 0

                # Tìm tần số tương ứng với khoảng chứa Q1, Q2 và Q3
                Q1_interval_frequency = frequencies[Q1_interval_index] if Q1_interval_index is not None else 0
                Q2_interval_frequency = frequencies[Q2_interval_index] if Q2_interval_index is not None else 0
                Q3_interval_frequency = frequencies[Q3_interval_index] if Q3_interval_index is not None else 0

                # Tính toán kết quả Q1, Q2 và Q3
                kqQ1 = Q1_interval[0] + Rational(1 * n / 4 - total_freq_before_Q1, Q1_interval_frequency) * (Q1_interval[1] - Q1_interval[0])
                kqQ2 = Q2_interval[0] + Rational(2 * n / 4 - total_freq_before_Q2, Q2_interval_frequency) * (Q2_interval[1] - Q2_interval[0])
                kqQ3 = Q3_interval[0] + Rational(3 * n / 4 - total_freq_before_Q3, Q3_interval_frequency) * (Q3_interval[1] - Q3_interval[0])

                # Kết quả
                kq = kqQ3 - kqQ1

                h1=kqQ2
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho mẫu số liệu ghép nhóm sau \n'
                                '\\begin{center} \n'
                                '\\begin{tabular}{|c|c|c|c|c|c|} \n'
                                '\\hline \n'
                                'Giá trị & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ \\\\ \n'
                                '\\hline \n'
                                'Tần số & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '\\end{tabular} \n'
                                '\\end{center} \n'
                                'Tìm trung vị của mẫu số liệu$zz$'
                                %(
                                latex(v),latex(v+k),latex(v+k),latex(v+2*k),latex(v+2*k),latex(v+3*k),latex(v+3*k),latex(v+4*k),latex(v+4*k),latex(v+5*k),
                                latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5),

                                ))

                # Nội dung lời giải
                loigiai=('Cỡ mẫu $n=%s$. Giả sử $x_1, x_2, $zz$$zz$$zz$, x_{%s}$ là số $%s$ giá trị và giả sử dãy số liệu gốc này được sắp xếp theo thứ tự không giảm$zz$ \\\\ \n'

                        'Vì $n=%s$ nên trung vị của mẫu số liệu là $M_e=x_{%s}$ thuộc nhóm $[%s;%s)$$zz$ \\\\ \n'
                        '\\hspace*{1cm} Do đó, trung vị là \\\\ \n'
                        '\\hspace*{1cm} $M_e=%s+\\dfrac{\\frac{%s}{2}-%s}{%s} \\cdot %s=%s$$zz$'
                        %(latex(tong),latex(tong),latex(tong),
                        latex(n),latex((n+1)/2),latex(Q2_interval[0]),latex(Q2_interval[1]),
                        latex(Q2_interval[0]),latex(n),latex(total_freq_before_Q2),latex(Q2_interval_frequency),latex(Q2_interval[1]-Q2_interval[0]),latex(kqQ2)            
                        ))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.', ',').replace('$zz$', '.').replace(',0', '')
            return content 


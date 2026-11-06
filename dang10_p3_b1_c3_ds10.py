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


def bt_dang10_p3_b1_c3_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Hàm hỗ trợ định dạng số: bỏ số 0 thừa ở phần thập phân và thay dấu chấm thành phẩy
                def to_str(val):
                    s = str(val)
                    if '.' in s:
                        s = s.rstrip('0').rstrip('.')
                    if s == '':
                        s = '0'
                    return s.replace('.', ',')

                while True:
                    # Random độ dài 3 cạnh a, b, c (1 chữ số thập phân, đảm bảo tạo thành 1 tam giác)
                    a_int = random.randint(80, 200)
                    b_int = random.randint(80, 200)

                    c_min = abs(a_int - b_int) + 20
                    c_max = a_int + b_int - 20
                    if c_max <= c_min: 
                        continue

                    c_int = random.randint(c_min, c_max)

                    a_val = Decimal(a_int) / Decimal(10)
                    b_val = Decimal(b_int) / Decimal(10)
                    c_val = Decimal(c_int) / Decimal(10)

                    # Random sai số từng cạnh
                    err_pool = [0.1, 0.2, 0.3, 0.4, 0.5]
                    d_a = Decimal(str(random.choice(err_pool)))
                    d_b = Decimal(str(random.choice(err_pool)))
                    d_c = Decimal(str(random.choice(err_pool)))

                    # Tính chu vi và tổng sai số
                    P_base = a_val + b_val + c_val
                    d_P = d_a + d_b + d_c

                    # Tính sai số tương đối (%)
                    rel_error = (d_P / P_base) * 100

                    # Làm tròn kết quả đúng (2 chữ số thập phân)
                    kq_val = rel_error.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                    if kq_val > 0:
                        break

                # Chuẩn bị đáp án đúng
                kq = to_str(kq_val)

                # --- TẠO CÁC PHƯƠNG ÁN NHIỄU (Mô phỏng 4 đáp án A, B, C, D trong hình) ---
                options_set = set()

                # Nhiễu 1: Làm tròn xuống 1 chữ số thập phân (VD: 1.6%)
                dist1_val = rel_error.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                if to_str(dist1_val) != kq:
                    options_set.add(to_str(dist1_val))

                # Nhiễu 2: Làm tròn chuẩn 1 chữ số thập phân (VD: 1.7%)
                dist2_val = rel_error.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                if to_str(dist2_val) != kq:
                    options_set.add(to_str(dist2_val))

                # Nhiễu 3: Làm tròn đến 3 chữ số thập phân (VD: 1.662%)
                dist3_val = rel_error.quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)
                if to_str(dist3_val) != kq:
                    options_set.add(to_str(dist3_val))

                # Bù đắp ngẫu nhiên nếu các nhiễu trên bị trùng với kết quả đúng
                offsets = [Decimal('0.01'), Decimal('-0.01'), Decimal('0.02'), Decimal('-0.02')]
                for off in offsets:
                    if len(options_set) == 3:
                        break
                    fallback_val = kq_val + off
                    if fallback_val > 0 and to_str(fallback_val) != kq:
                        options_set.add(to_str(fallback_val))

                options_list = list(options_set)[:3]

                # Câu hỏi
                noidungcauhoi = ('''Cho tam giác $ABC$ có độ dài ba cạnh đo được như sau $a = %s\\text{cm} \\pm %s\\text{cm}$ ; $b = %s\\text{cm} \\pm %s\\text{cm}$ ; $c = %s\\text{cm} \\pm %s\\text{cm}$. Chu vi $P$ của tam giác và đánh giá sai số tuyệt đối. Sai số tương đối của số gần đúng của chu vi qua phép đo bằng bao nhiêu? (làm tròn kết quả đến hàng phần trăm).''' 
                                 % (to_str(a_val), to_str(d_a),
                                    to_str(b_val), to_str(d_b),
                                    to_str(c_val), to_str(d_c)))

                # Các đáp án
                da_d = ('\\True $%s\\%%$' % (kq))
                da_s1 = ('$%s\\%%$' % (options_list[0]))
                da_s2 = ('$%s\\%%$' % (options_list[1])) 
                da_s3 = ('$%s\\%%$' % (options_list[2])) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai=('''Giả sử $a = %s + d_1$, $b = %s + d_2$, $c = %s + d_3$.\\\\
            Ta có $P = a + b + c + d_1 + d_2 + d_3 = %s + d_1 + d_2 + d_3$.\\\\
            Theo giả thiết, ta có $-%s \\le d_1 \\le %s; -%s \\le d_2 \\le %s; -%s \\le d_3 \\le %s$.\\\\
            Suy ra $-%s \\le d_1 + d_2 + d_3 \\le %s$.\\\\
            Do đó $P = %s \\text{ cm} \\pm %s \\text{ cm}$.\\\\
            Sai số tuyệt đối $\\Delta_P \\le %s$. Sai số tương đối $\\delta_P \\le \\frac{d}{P} = \\frac{%s}{%s} \\approx %s\\%%$.'''
                         % (to_str(a_val), to_str(b_val), to_str(c_val),
                            to_str(P_base),
                            to_str(d_a), to_str(d_a),
                            to_str(d_b), to_str(d_b),
                            to_str(d_c), to_str(d_c),
                            to_str(d_P), to_str(d_P),
                            to_str(P_base), to_str(d_P),
                            to_str(d_P), to_str(d_P), to_str(P_base), kq))
                dapan='\\shortans[0]{$%s$}\n'%(kq)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content



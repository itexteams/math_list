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


def bt_dang16_p3_b3_c5_ds11(self):
            # Khai báo biến
            # Khai báo biến danh sách dạng bài
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # --- B3: Ngẫu nhiên hóa các thông số bài toán ---
                # P: Số tiền gốc ban đầu (từ 100 đến 500 triệu, bước nhảy 50)
                P = random.randint(2, 10) * 50 
                # r: Lãi suất hàng năm (từ 5% đến 9%)
                r = random.randint(5, 9)
                # n1: Số năm gửi đợt 1 (từ 4 đến 6 năm)
                n1 = random.randint(4, 6)
                # n2: Số năm gửi đợt 2 (thường bằng n1 hoặc chênh lệch ít để tổng khoảng 10 năm)
                n2 = 10 - n1

                r_dec = Decimal(r) / 100

                # --- B1 & B2: Tính toán theo logic đề bài ---
                # Giai đoạn 1: Sau n1 năm
                T1 = Decimal(P) * (1 + r_dec)**n1
                T1_round = T1.quantize(Decimal('1'), rounding=ROUND_HALF_UP)

                # Sau khi rút một nửa để sửa nhà
                P2 = T1_round / 2
                P2_round = P2.quantize(Decimal('1'), rounding=ROUND_HALF_UP)

                # Giai đoạn 2: Gửi số tiền còn lại trong n2 năm
                T2 = P2_round * (1 + r_dec)**n2
                T2_round = T2.quantize(Decimal('1'), rounding=ROUND_HALF_UP)

                # Tính tổng tiền lãi L
                L1 = T1_round - Decimal(P)
                L2 = T2_round - P2_round
                L_total = L1 + L2
                kq_val = L_total.quantize(Decimal('1'), rounding=ROUND_HALF_UP)

                # Định dạng hiển thị dấu phẩy cho số thập phân Việt Nam
                def format_vn(val):
                    return str(val).replace('.', ',')

                kq = format_vn(kq_val)

                # --- B4: Tạo các phương án sai (không trùng đáp án đúng) ---
                du = [f'${kq}$']
                da = du[0]

                s = []
                while len(s) < 3:
                    # Tạo sai số ngẫu nhiên từ -10 đến 10 đơn vị
                    offset = Decimal(random.randint(-15, 15)) + Decimal(random.random()).quantize(Decimal('1'))
                    if offset == 0: continue

                    sai_so = (kq_val + offset).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
                    sai_so_str = f'${format_vn(sai_so)}$'

                    if sai_so_str != da and sai_so_str not in s:
                        s.append(sai_so_str)

                das1, das2, das3 = s[0], s[1], s[2]

                # --- Nội dung câu hỏi ---
                noidungcauhoi = (f"Ông Tuấn gửi ${P}$ triệu vào ngân hàng với hình thức lãi kép, kỳ hạn $1$ năm với lãi suất ${r}\\%$. "
                                 f"Sau ${n1}$ năm ông rút toàn bộ tiền và dùng một nửa để sửa nhà, số tiền còn lại ông tiếp tục gửi ngân hàng "
                                 f"với lãi suất như lần trước. Số tiền lãi ông Tuấn nhận được sau $10$ năm gửi bằng bao nhiêu? (làm tròn kết quả đến hàng đơn vị).")

                # --- Nội dung lời giải chi tiết ---
                loigiai = (f"{n1} năm đầu ông Tuấn có số tiền cả gốc và lãi là: $T_1 = {P} \\cdot (1 + {r}\\%)^{{{n1}}} \\approx {format_vn(T1_round)}$. \\\\\n"
                           f"Sau khi sửa nhà, số tiền còn lại gửi vào ngân hàng trong {n2} năm tiếp theo là: $\\frac{{{format_vn(T1_round)}}}{{2}} = {format_vn(P2_round)}$. \\\\\n"
                           f"Số tiền cả gốc và lãi sau đợt gửi thứ hai là: $T_2 = {format_vn(P2_round)} \\cdot (1 + {r}\\%)^{{{n2}}} \\approx {format_vn(T2_round)}$. \\\\\n"
                           f"Số tiền lãi trong $10$ năm là: $L = ({format_vn(T1_round)} - {P}) + ({format_vn(T2_round)} - {format_vn(P2_round)}) = {kq}$.")
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq))

                # --- Xuất câu trắc nghiệm ---
                da_d = '\\True ' + str(da)
                list_1 = [da_d, das1, das2, das3]
                random.shuffle(list_1)

                content = ('\\begin{minipage}{\\textwidth} \n'
                           '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                           '\\loigiai{' + str(loigiai) + '}\n'
                           '\\end{ex}\n \\end{minipage} \n\n')
            return content


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


def bt_dang27_p1_b2_c3_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random tổng số thửa ruộng
                N = random.choice([40, 50, 60, 80])

                # Random tịnh tiến sản lượng (tạo 5 cột giá trị liên tiếp)
                v1 = random.randint(18, 25)
                v2 = v1 + 1
                v3 = v1 + 2
                v4 = v1 + 3
                v5 = v1 + 4

                # Random các tần số đã biết
                f1 = random.randint(3, 8)
                f2 = random.randint(4, 10)
                f5 = random.randint(3, 8)

                # Tính tổng tần số còn lại cho n và m
                R = N - (f1 + f2 + f5)

                # Random ẩn n và m sao cho tổng bằng R
                n = random.randint(5, R - 5)
                m = R - n

                # Tính tổng sản lượng S tuyệt đối (số nguyên)
                S = f1*v1 + f2*v2 + n*v3 + m*v4 + f5*v5

                # ==========================================
                # XỬ LÝ SỐ TRUNG BÌNH (Loại bỏ số thập phân vô hạn)
                # ==========================================
                tb_exact = Rational(S, N)
                if tb_exact.q == 1:
                    # Nếu chia hết, nó là số nguyên
                    tb_str = str(tb_exact.p)
                elif 100000 % tb_exact.q == 0:  
                    # Nếu mẫu số là ước của 10^k -> Đây là số thập phân hữu hạn (VD: 2.5, 3.25)
                    # Chuyển đổi dấu chấm thành dấu phẩy
                    tb_float = S / N
                    tb_str = str(tb_float).replace('.', ',')
                else:
                    # Nếu là số thập phân vô hạn, hiển thị dưới dạng phân số tối giản LaTeX
                    tb_str = f"\\frac{{{tb_exact.p}}}{{{tb_exact.q}}}"

                # ==========================================
                # PHẦN MỞ RỘNG: Các dạng câu hỏi
                # ==========================================
                dang_cau_hoi = random.choice(['n', 'm', 'm*n', 'm-n', '2m-n'])

                if dang_cau_hoi == 'n':
                    yeucau = "Giá trị của $n$ là"
                    kq_dung = n
                    ket_luan = f"Vậy $n = {n}$."
                    s_vals = [n - 2, n - 1, n + 1, n + 2, m] 
                elif dang_cau_hoi == 'm':
                    yeucau = "Giá trị của $m$ là"
                    kq_dung = m
                    ket_luan = f"Vậy $m = {m}$."
                    s_vals = [m - 2, m - 1, m + 1, m + 2, n]
                elif dang_cau_hoi == 'm*n':
                    yeucau = "Giá trị của tích $P = m \\cdot n$ bằng"
                    kq_dung = m * n
                    ket_luan = f"Vậy $P = m \\cdot n = {m} \\cdot {n} = {kq_dung}$."
                    s_vals = [kq_dung + n, kq_dung - m, kq_dung + 10, kq_dung - 5]
                elif dang_cau_hoi == 'm-n':
                    yeucau = "Giá trị của hiệu $P = m - n$ bằng"
                    kq_dung = m - n
                    ket_luan = f"Vậy $P = m - n = {m} - {n} = {kq_dung}$."
                    s_vals = [kq_dung + 1, kq_dung - 1, n - m, kq_dung + 2, kq_dung - 2]
                elif dang_cau_hoi == '2m-n':
                    yeucau = "Giá trị của biểu thức $P = 2m - n$ bằng"
                    kq_dung = 2 * m - n
                    ket_luan = f"Vậy $P = 2m - n = 2 \\cdot {m} - {n} = {kq_dung}$."
                    s_vals = [kq_dung + 1, kq_dung - 1, 2 * n - m, kq_dung + 3]

                da = f'${kq_dung}$'

                # Lọc đáp án nhiễu: loại bỏ trùng lặp và loại đáp án trùng với kết quả đúng
                s_vals = list(set([v for v in s_vals if v != kq_dung])) 

                # Bổ sung nếu chưa đủ 3 đáp án nhiễu
                while len(s_vals) < 3:
                    cand = kq_dung + random.randint(-5, 5)
                    if cand != kq_dung and cand not in s_vals:
                        s_vals.append(cand)

                s = [f'${v}$' for v in s_vals[:3]] # Lấy chính xác 3 phần tử

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Cấu trúc câu hỏi
                noidungcauhoi = f'''Sản lượng lúa (tạ) của ${N}$ thửa ruộng thí nghiệm có cùng diện tích được trình bày trong bảng phân bố tần số sau đây:
            \\begin{{center}}
            \\begin{{tabular}}{{|c|c|c|c|c|c|}}
            \\hline
            Sản lượng & ${v1}$ & ${v2}$ & ${v3}$ & ${v4}$ & ${v5}$ \\\\
            \\hline
            Tần số & ${f1}$ & ${f2}$ & $n$ & $m$ & ${f5}$ \\\\
            \\hline
            \\end{{tabular}}
            \\end{{center}}
            Biết sản lượng trung bình của ${N}$ thửa ruộng là ${tb_str}$ tạ. {yeucau}.'''

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Tính toán cho phần lời giải (Dùng tổng S số nguyên để tính toán tuyệt đối chính xác)
                S_known_val = f1*v1 + f2*v2 + f5*v5
                rhs_val = S - S_known_val

                # Nội dung lời giải
                loigiai = f'''Ta có tổng tần số là: ${f1} + {f2} + n + m + {f5} = {N} \\Leftrightarrow n + m = {R}$.\\\\
            Sản lượng trung bình của ${N}$ thửa ruộng là ${tb_str}$ nên:
            $$ \\frac{{1}}{{{N}}}({f1} \\cdot {v1} + {f2} \\cdot {v2} + n \\cdot {v3} + m \\cdot {v4} + {f5} \\cdot {v5}) = {tb_str} \\Leftrightarrow {v3}n + {v4}m = {rhs_val}. $$
            Giải hệ phương trình $\\begin{{cases}} n + m = {R} \\\\ {v3}n + {v4}m = {rhs_val} \\end{{cases}} \\Leftrightarrow \\begin{{cases}} n = {n} \\\\ m = {m} \\end{{cases}}$.\\\\
            {ket_luan}'''

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


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


def bt_dang22_p1_b3_c4_ds10(self):
            # Khai báo biến
            x = symbols('x')
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # ------------------------------------------------------------------
                # B3: LOGIC RANDOM NGHIỆM NGUYÊN
                # ------------------------------------------------------------------

                # Tạo 3 nghiệm nguyên phân biệt trong khoảng từ -9 đến 9
                roots = random.sample(range(-9, 10), 3)
                roots.sort() # Sắp xếp để dễ quản lý bảng xét dấu: x1 < x2 < x3
                x1_val, x2_val, x3_val = roots

                # Chia 3 nghiệm này cho 2 nhóm: 1 nhị thức và 1 tam thức
                # Chọn ngẫu nhiên 1 trong 3 nghiệm làm nghiệm của nhị thức
                nghiem_nhat = random.choice(roots)
                nghiem_hai = [r for r in roots if r != nghiem_nhat]

                # Tạo biểu thức nhị thức bậc nhất: a(x - x_nhi_thuc)
                # Random hệ số 'a' để bài toán phong phú (tránh a=0)
                a_coeff = random.choice([-3, -2, -1, 1, 2, 3])
                expr_nhat = expand(a_coeff * (x - nghiem_nhat))

                # Tạo biểu thức tam thức bậc hai: c(x - x_h1)(x - x_h2)
                c_coeff = random.choice([-2, -1, 1, 2])
                expr_hai = expand(c_coeff * (x - nghiem_hai[0]) * (x - nghiem_hai[1]))

                vt = expr_nhat * expr_hai
                dau_bpt = random.choice(['>', '<'])

                # ------------------------------------------------------------------
                # B2: GIẢI TOÁN VÀ LẬP BẢNG XÉT DẤU
                # ------------------------------------------------------------------

                # Các điểm thử để lấy dấu trong các khoảng: (-inf, x1), (x1, x2), (x2, x3), (x3, +inf)
                test_points = [x1_val - 1, (x1_val + x2_val)/2, (x2_val + x3_val)/2, x3_val + 1]

                row_nhat, row_hai, row_vt = [], [], []

                def get_sign_str(expr, val):
                    return "+" if expr.subs(x, val) > 0 else "-"

                for p in test_points:
                    s1 = get_sign_str(expr_nhat, p)
                    s2 = get_sign_str(expr_hai, p)
                    row_nhat.append(s1)
                    row_hai.append(s2)
                    row_vt.append("+" if s1 == s2 else "-")

                # Xác định vị trí 0 và gạch đứng
                z_nhat = ["0" if r == nghiem_nhat else "|" for r in roots]
                z_hai =  ["0" if r in nghiem_hai else "|" for r in roots]

                # Tạo bảng xét dấu LaTeX
                bang_xet_dau = r"""\begin{center}
            \begin{tikzpicture}
            \tkzTabInit[lgt=3,espcl=1.5]
            {$x$ /1, $%s$ /1, $%s$ /1, $VT$ /1}
            {$-\infty$, $%s$, $%s$, $%s$, $+\infty$}
            \tkzTabLine{ , %s , %s , %s , %s , %s , %s , %s , }
            \tkzTabLine{ , %s , %s , %s , %s , %s , %s , %s , }
            \tkzTabLine{ , %s , 0 , %s , 0 , %s , 0 , %s , }
            \end{tikzpicture}
            \end{center}""" % (
                    latex(expr_nhat), latex(expr_hai), x1_val, x2_val, x3_val,
                    row_nhat[0], z_nhat[0], row_nhat[1], z_nhat[1], row_nhat[2], z_nhat[2], row_nhat[3],
                    row_hai[0], z_hai[0], row_hai[1], z_hai[1], row_hai[2], z_hai[2], row_hai[3],
                    row_vt[0], row_vt[1], row_vt[2], row_vt[3]
                )

                # ------------------------------------------------------------------
                # B4: TẠO ĐÁP ÁN (KHÔNG TRÙNG LẶP)
                # ------------------------------------------------------------------
                lx1, lx2, lx3 = x1_val, x2_val, x3_val

                def build_interval(signs, target_sign):
                    intervals = []
                    if signs[0] == target_sign: intervals.append(r"\left(-\infty; %s\right)" % lx1)
                    if signs[1] == target_sign: intervals.append(r"\left(%s; %s\right)" % (lx1, lx2))
                    if signs[2] == target_sign: intervals.append(r"\left(%s; %s\right)" % (lx2, lx3))
                    if signs[3] == target_sign: intervals.append(r"\left(%s; +\infty\right)" % lx3)
                    return r"S = " + (r" \cup ".join(intervals) if intervals else r"\varnothing")

                dap_an_dung = build_interval(row_vt, "+" if dau_bpt == '>' else "-")

                # Nhiễu 1: Đảo ngược dấu của bất phương trình
                dap_an_sai1 = build_interval(row_vt, "-" if dau_bpt == '>' else "+")
                # Nhiễu 2: Lấy sai khoảng (ví dụ chỉ lấy đoạn giữa)
                dap_an_sai2 = r"S = \left(%s; %s\right)" % (lx1, lx3)
                # Nhiễu 3: Sai ngoặc tròn thành vuông
                dap_an_sai3 = dap_an_dung.replace(r"\left(", r"\left[").replace(r"\right)", r"\right]")

                # Đảm bảo các phương án không bị trùng
                options = list(set([dap_an_dung, dap_an_sai1, dap_an_sai2, dap_an_sai3]))
                while len(options) < 4:
                    options.append(r"S = \mathbb{R}")
                    options = list(set(options))

                # Chuẩn bị nội dung xuất
                noidungcauhoi = "Nghiệm của bất phương trình $(%s)(%s) %s 0$ là" % (latex(expr_nhat), latex(expr_hai), dau_bpt)

                loigiai = r"""Xét dấu vế trái (VT) của bất phương trình ta có: \\ Cho $%s = 0 \Leftrightarrow x = %s$. \\
            Cho $%s = 0 \Leftrightarrow x = %s$ hoặc $x = %s$. \\
            Bảng xét dấu:
            %s
            Dựa vào bảng xét dấu, tập nghiệm của bất phương trình là $%s$.""" % (
                    latex(expr_nhat), nghiem_nhat, latex(expr_hai), nghiem_hai[0], nghiem_hai[1],
                    bang_xet_dau, dap_an_dung
                )

                # Xử lý danh sách đáp án để in ra (đánh dấu \True)
                final_choices = []
                for opt in options:
                    if opt == dap_an_dung:
                        final_choices.append(f"\\True ${opt}$")
                    else:
                        final_choices.append(f"${opt}$")

                random.shuffle(final_choices)

                content = (
                    '\\begin{minipage}{\\textwidth} \n'
                    '\\begin{ex}\n' + noidungcauhoi + '\n'
                    '\\choice \n'
                    '{' + final_choices[0] + '}\n'
                    '{' + final_choices[1] + '}\n'
                    '{' + final_choices[2] + '}\n'
                    '{' + final_choices[3] + '}\n'
                    '\\loigiai{' + loigiai + '}\n'
                    '\\end{ex}\n \\end{minipage} \n\n')
            return content


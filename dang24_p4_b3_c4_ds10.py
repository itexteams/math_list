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


def bt_dang24_p4_b3_c4_ds10(self):
            # Khai báo biến
            # --- PHẦN 1: KHỞI TẠO VÀ RANDOM ---
            x = symbols('x')

            # Random 3 nghiệm phân biệt r1 < r2 < r3
            roots = random.sample(range(-10, 11), 3)
            roots.sort()
            r1, r2, r3 = roots

            # Chọn nghiệm ở giữa làm nghiệm mẫu (để bảng xét dấu đan xen dấu)
            idx_den = 1 
            r_den = roots[idx_den]
            r_num = [r for i, r in enumerate(roots) if i != idx_den]

            # Biểu thức tử và mẫu
            tu_so = expand((x - r_num[0]) * (x - r_num[1]))
            mau_so = x - r_den

            # Chọn ngẫu nhiên dấu bất phương trình: <, <=, >, >=
            op_idx = random.randint(0, 3)
            ops = ['<', '\\leq', '>', '\\geq']
            dau_bpt = ops[op_idx]

            # --- PHẦN 2: LOGIC XÉT DẤU ---
            def sign_linear(val, root):
                return "+" if val > root else "-"

            def sign_quad(val, root1, root2):
                return "-" if root1 < val < root2 else "+"

            test_points = [r1 - 1, (r1 + r2) / 2, (r2 + r3) / 2, r3 + 1]

            signs_tu = [sign_quad(p, r_num[0], r_num[1]) for p in test_points]
            signs_mau = [sign_linear(p, r_den) for p in test_points]
            signs_vt = ["+" if signs_tu[i] == signs_mau[i] else "-" for i in range(4)]

            # --- PHẦN 3: XÁC ĐỊNH TẬP NGHIỆM ĐÚNG (Có \left \right) ---
            def get_sol(oidx, r):
                s1, s2, s3 = r
                # Kiểm tra có lấy dấu bằng không
                lay_bang = oidx in [1, 3]

                # Định dạng ngoặc
                nb = "\\left[" if lay_bang else "\\left("
                nd = "\\right]" if lay_bang else "\\right)"
                nt = "\\left(" # Nghiệm mẫu luôn tròn
                ntd = "\\right)"

                if oidx == 0: # < 0
                    return f"\\left( -\\infty; {s1} \\right) \\cup \\left( {s2}; {s3} \\right)"
                if oidx == 1: # <= 0
                    return f"\\left( -\\infty; {s1} \\right] \\cup \\left( {s2}; {s3} \\right]"
                if oidx == 2: # > 0
                    return f"\\left( {s1}; {s2} \\right) \\cup \\left( {s3}; +\\infty \\right)"
                if oidx == 3: # >= 0
                    return f"\\left[ {s1}; {s2} \\right) \\cup \\left[ {s3}; +\\infty \\right)"

            tap_nghiem = get_sol(op_idx, roots)

            # --- PHẦN 4: TẠO BẢNG XÉT DẤU LATEX (CÓ ĐÓNG KHUNG) ---
            def make_table():
                t_vals = ["0" if r in r_num else "|" for r in roots]
                m_vals = ["0" if r == r_den else "|" for r in roots]
                v_vals = ["||" if r == r_den else "0" for r in roots]

                table = r"""\begin{center}
            \renewcommand{\arraystretch}{1.2}
            \begin{tabular}{|c|ccccccccc|}
            \hline
                $x$ & $-\infty$ & & $r1$ & & $r2$ & & $r3$ & & $+\infty$ \\ \hline
                $f(x)$ & & $s_t0$ & $t1$ & $s_t1$ & $t2$ & $s_t2$ & $t3$ & $s_t3$ & \\ \hline
                $g(x)$ & & $s_m0$ & $m1$ & $s_m1$ & $m2$ & $s_m2$ & $m3$ & $s_m3$ & \\ \hline
                $VT$ & & $s_v0$ & $v1$ & $s_v1$ & $v2$ & $s_v2$ & $v3$ & $s_v3$ & \\ \hline
            \end{tabular}
            \end{center}"""

                table = table.replace("r1", str(r1)).replace("r2", str(r2)).replace("r3", str(r3))
                table = table.replace("f(x)", latex(tu_so)).replace("g(x)", latex(mau_so))

                for i in range(4):
                    table = table.replace(f"s_t{i}", signs_tu[i]).replace(f"s_m{i}", signs_mau[i]).replace(f"s_v{i}", signs_vt[i])

                table = table.replace("t1", t_vals[0]).replace("t2", t_vals[1]).replace("t3", t_vals[2])
                table = table.replace("m1", m_vals[0]).replace("m2", m_vals[1]).replace("m3", m_vals[2])
                table = table.replace("v1", v_vals[0]).replace("v2", v_vals[1]).replace("v3", v_vals[2])
                return table

            # --- PHẦN 5: ĐÓNG GÓI NỘI DUNG ---
            da_d = f"\\True $T = {tap_nghiem}$"
            # Tạo đáp án nhiễu (ngược dấu, sai ngoặc)
            da_s1 = f"$T = {get_sol((op_idx+2)%4, roots)}$" 
            da_s2 = f"$T = \\left( {r1}; {r3} \\right)$"
            da_s3 = f"$T = {tap_nghiem.replace('left[', 'left(').replace('right]', 'right)')}$"

            list_da = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_da)

            noidungcauhoi = f"Tìm tập nghiệm $T$ của bất phương trình $\\frac{{{latex(tu_so)}}}{{{latex(mau_so)}}} {dau_bpt} 0$."

            loigiai = f"""
            Xét phương trình tử số: ${latex(tu_so)} = 0 \\Leftrightarrow \\left[ \\begin{{aligned}} & x = {r_num[0]} \\\\ & x = {r_num[1]} \\end{{aligned}} \\right.$. \\\\
            Xét phương trình mẫu số: ${latex(mau_so)} = 0 \\Leftrightarrow x = {r_den}$. \\\\
            Bảng xét dấu:
            {make_table()}
            Dựa vào bảng xét dấu và chiều của bất phương trình, ta có tập nghiệm:
            $T = {tap_nghiem}$.
            """

            # Xuất kết quả theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


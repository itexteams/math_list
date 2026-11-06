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


def bt_dang25_p1_b3_c4_ds10(self):
            # Khai báo biến
            # --- Cấu trúc tuân thủ mẫu file chỉ dẫn ---
            x = symbols('x')
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # 1. Khởi tạo nghiệm mẫu (phân biệt để tránh trùng lặp gây lỗi bảng)
                c = random.randint(2, 5)
                nghiem_mau = sorted([-c, c])

                # 2. Khởi tạo nghiệm tử (chọn các số nguyên khác nghiệm mẫu)
                potential_roots = [i for i in range(-7, 8) if i not in nghiem_mau and i != 0]
                x1, x2 = sorted(random.sample(potential_roots, 2))
                nghiem_tu = [x1, x2]

                tu_so_expand = expand((x - x1) * (x - x2))
                mau_so_expand = expand(x**2 - c**2)
                f_x = tu_so_expand / mau_so_expand

                # Sắp xếp các mốc để lập bảng xét dấu
                moc = sorted(nghiem_mau + nghiem_tu)

                # 3. Random dấu bất phương trình
                loai_dau = random.choice(['>', '>=', '<', '<='])
                dau_latex = {'>': '> 0', '>=': r'\ge 0', '<': '< 0', '<=': r'\le 0'}[loai_dau]

                # 4. Giải tập nghiệm và xử lý ngoặc chuẩn LaTeX \left( \right)
                intervals = [('-oo', moc[0]), (moc[0], moc[1]), (moc[1], moc[2]), (moc[2], moc[3]), (moc[3], 'oo')]
                results = []

                for l, r in intervals:
                    # Điểm thử dấu
                    if l == '-oo': pt = r - 0.5
                    elif r == 'oo': pt = l + 0.5
                    else: pt = (l + r) / 2

                    val = f_x.subs(x, pt)
                    is_true = False
                    if loai_dau == '>' and val > 0: is_true = True
                    elif loai_dau == '>=' and val >= 0: is_true = True
                    elif loai_dau == '<' and val < 0: is_true = True
                    elif loai_dau == '<=' and val <= 0: is_true = True

                    if is_true:
                        # Quy tắc ngoặc: Tròn cho mẫu/vô cực, Vuông cho tử nếu có dấu =
                        s_l = r'\left(' if (l in nghiem_mau or l == '-oo') else (r'\left[' if '=' in loai_dau else r'\left(')
                        s_r = r'\right)' if (r in nghiem_mau or r == 'oo') else (r'\right]' if '=' in loai_dau else r'\right)')
                        l_v = r'-\infty' if l == '-oo' else str(l)
                        r_v = r'+\infty' if r == 'oo' else str(r)
                        results.append(f"{s_l}{l_v}; {r_v}{s_r}")

                da = "$S = " + " \\cup ".join(results) + "$" if results else "$S = \\varnothing$"

                # 5. Tạo phương án nhiễu (Đảm bảo không trùng và đúng định dạng)
                def clean_latex(s): return s.replace(r'\left', '').replace(r'\right', '').replace('[', '(').replace(']', ')')

                s_nhieu_set = set()
                # Nhiễu 1: Thay đổi loại ngoặc
                s_nhieu_set.add(da.replace(r'\left[', r'\left(').replace(r'\right]', r'\right)'))
                # Nhiễu 2: Tập xác định bỏ điểm
                s_nhieu_set.add("$S = \\mathbb{R} \\setminus \\{%s; %s\\}$" % (-c, c))
                # Nhiễu 3: Đảo dấu các khoảng
                s_nhieu_set.add("$S = \\left(%s; %s\\right) \\cup \\left(%s; %s\\right)$" % (moc[0], moc[1], moc[2], moc[3]))

                s_nhieu_list = [i for i in s_nhieu_set if i != da]
                while len(s_nhieu_list) < 3:
                    rand_val = random.randint(-5, 5)
                    extra = "$S = \\left(-\\infty; %d\\right]$" % rand_val
                    if extra != da: s_nhieu_list.append(extra)

                random.shuffle(s_nhieu_list)
                da_s1, da_s2, da_s3 = s_nhieu_list[:3]

                # 6. Xây dựng Bảng xét dấu đầy đủ khung (tabular với | và \hline)
                def get_sign(expr, l, r):
                    pt = r - 0.5 if l == '-oo' else (l + 0.5 if r == 'oo' else (l + r) / 2)
                    return "+" if expr.subs(x, pt) > 0 else "-"

                s_tu = [get_sign(tu_so_expand, i[0], i[1]) for i in intervals]
                s_mau = [get_sign(mau_so_expand, i[0], i[1]) for i in intervals]
                s_fx = [get_sign(f_x, i[0], i[1]) for i in intervals]

                def sep_tu(m): return "0" if m in nghiem_tu else "|"
                def sep_mau(m): return "0" if m in nghiem_mau else "|"
                def sep_fx(m): return "||" if m in nghiem_mau else "0"

                loigiai = (r"""Xét hàm số $f(x) = \frac{%s}{%s}$.\\
                Tập xác định: $D = \mathbb{R} \setminus \{%s; %s\}$.\\
                Cho $%s = 0 \Leftrightarrow x = %s$ hoặc $x = %s$.\\
                Cho $%s = 0 \Leftrightarrow x = %s$ hoặc $x = %s$.\\
                Bảng xét dấu:
                \begin{center}
                \renewcommand{\arraystretch}{1.2}
                \begin{tabular}{|c|l*{9}{c}r|}
                \hline
                $x$ & $-\infty$ & & $%s$ & & $%s$ & & $%s$ & & $%s$ & & $+\infty$ \\ \hline
                Tử số & & $%s$ & %s & $%s$ & %s & $%s$ & %s & $%s$ & %s & $%s$ & \\ \hline
                Mẫu số & & $%s$ & %s & $%s$ & %s & $%s$ & %s & $%s$ & %s & $%s$ & \\ \hline
                $f(x)$ & & $%s$ & %s & $%s$ & %s & $%s$ & %s & $%s$ & %s & $%s$ & \\ \hline
                \end{tabular}
                \end{center}
                Dựa vào bảng xét dấu và chiều của bất phương trình, tập nghiệm của bất phương trình là %s.""" 
                % (latex(tu_so_expand), latex(mau_so_expand), -c, c,
                   latex(tu_so_expand), x1, x2, 
                   latex(mau_so_expand), -c, c,
                   moc[0], moc[1], moc[2], moc[3],
                   s_tu[0], sep_tu(moc[0]), s_tu[1], sep_tu(moc[1]), s_tu[2], sep_tu(moc[2]), s_tu[3], sep_tu(moc[3]), s_tu[4],
                   s_mau[0], sep_mau(moc[0]), s_mau[1], sep_mau(moc[1]), s_mau[2], sep_mau(moc[2]), s_mau[3], sep_mau(moc[3]), s_mau[4],
                   s_fx[0], sep_fx(moc[0]), s_fx[1], sep_fx(moc[1]), s_fx[2], sep_fx(moc[2]), s_fx[3], sep_fx(moc[3]), s_fx[4],
                   da))

                noidungcauhoi = r"Tìm tập nghiệm $S$ của bất phương trình $\frac{%s}{%s} %s$." % (latex(tu_so_expand), latex(mau_so_expand), dau_latex)

            # --- Xuất Content ---
            list_1 = [('\\True ' + str(da)), da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


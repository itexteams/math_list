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


def bt_dang27_p1_b3_c4_ds10(self):
            # Khai báo biến
            # --- PHẦN KHAI BÁO BIẾN ---
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # 1. Tạo f1 = a^2 - x^2 (Có 2 nghiệm -a, a)
                a_val = random.randint(2, 4)
                f1 = a_val**2 - x**2
                r1_list = sorted([-a_val, a_val])

                # 2. Tạo f2 = (x-m)(x-n) (Có 2 nghiệm m, n khác với r1_list)
                others = [i for i in range(-6, 7) if i not in r1_list and i != 0]
                m, n = random.sample(others, 2)
                f2 = expand((x - m) * (x - n))
                r2_list = sorted([m, n])

                # 3. Tạo f3 = x^2 + px + q (Luôn dương, Delta < 0)
                p_val = random.randint(-2, 2)
                q_val = p_val**2 + random.randint(1, 5) 
                f3 = x**2 + p_val*x + q_val

                # 4. Sắp xếp tất cả các nghiệm
                all_roots = sorted(r1_list + r2_list)
                r1, r2, r3, r4 = all_roots

                # 5. Kiểu bất phương trình
                kieu = random.randint(0, 3)
                labels = ["âm", "dương", "không dương", "không âm"]
                ops = ["< 0", "> 0", r"\leq 0", r"\geq 0"]

                # Logic xác định tập nghiệm
                if kieu == 0: # âm (<0)
                    itv = f"(-\\infty; {r1}) \\cup ({r2}; {r3}) \\cup ({r4}; +\\infty)"
                elif kieu == 1: # dương (>0)
                    itv = f"({r1}; {r2}) \\cup ({r3}; {r4})"
                elif kieu == 2: # không dương (<=0)
                    itv = f"(-\\infty; {r1}] \\cup [{r2}; {r3}] \\cup [{r4}; +\\infty)"
                else: # không âm (>=0)
                    itv = f"[{r1}; {r2}] \\cup [{r3}; {r4}]"

                # --- TẠO BẢNG XÉT DẤU ---
                tp = [r1-1, (r1+r2)/2, (r2+r3)/2, (r3+r4)/2, r4+1]
                def get_s(expr, val): return "+" if expr.subs(x, val) > 0 else "-"

                def make_row(expr):
                    row = f"${latex(expr)}$ & & "
                    for i in range(4):
                        # Thêm dấu $ vào các giá trị dấu và vạch 0/|
                        row += f"${get_s(expr, tp[i])}$ & {'$0$' if expr.subs(x, all_roots[i])==0 else '$|$'} & "
                    row += f"${get_s(expr, tp[4])}$ & \\\\ \\hline"
                    return row

                # Tạo bảng với định dạng toán học cho mọi ô số
                table_latex = r"\begin{center}" + "\n" + r"\begin{tabular}{|c|*{11}{c}|}" + "\n" + r"\hline" + "\n"
                table_latex += f"$x$ & $-\\infty$ & & ${r1}$ & & ${r2}$ & & ${r3}$ & & ${r4}$ & & $+\\infty$ \\\\ \\hline" + "\n"
                table_latex += make_row(f1) + "\n" + make_row(f2) + "\n" + make_row(f3) + "\n"

                # Dòng f(x)
                row_fx = "$f(x)$ & & "
                fx_total = f1 * f2 * f3
                for i in range(4):
                    row_fx += f"${get_s(fx_total, tp[i])}$ & $0$ & "
                row_fx += f"${get_s(fx_total, tp[4])}$ & \\\\ \\hline"
                table_latex += row_fx + "\n" + r"\end{tabular}\end{center}"

                # --- CHUẨN BỊ NỘI DUNG ---
                lf1, lf2, lf3 = latex(f1), latex(f2), latex(f3)
                noidungcauhoi = f"Biểu thức $f(x) = ({lf1})({lf2})({lf3})$ nhận giá trị {labels[kieu]} khi và chỉ khi"

                da_d = f"\\True $x \\in {itv}$"
                s = [
                    f"$x \\in ({r1}; {r4})$",
                    f"$x \\in (-\\infty; {r2}) \\cup ({r3}; +\\infty)$",
                    f"$x \\in [{r1}; {r2}] \\cup [{r3}; {r4}]$" if kieu < 2 else f"$x \\in ({r1}; {r2}) \\cup ({r3}; {r4})$",
                    f"$x \\in (-\\infty; {r1}) \\cup ({r3}; {r4})$",
                    f"$x \\in ({r1}; {r2}) \\cup ({r4}; +\\infty)$"
                ]
                random.shuffle(s)
                list_1 = [da_d, s[0], s[1], s[2]]
                random.shuffle(list_1)

                loigiai = (r"Đặt $f(x) = (" + lf1 + r")(" + lf2 + r")(" + lf3 + r")$.\\\\" 
                           r"Ta có các nghiệm của các nhị thức, tam thức bậc hai là:\\\\" 
                           f"$\\bullet$ ${lf1} = 0 \\Leftrightarrow x = {r1_list[0]}$ hoặc $x = {r1_list[1]}$.\\\\" 
                           f"$\\bullet$ ${lf2} = 0 \\Leftrightarrow x = {r2_list[0]}$ hoặc $x = {r2_list[1]}$.\\\\" 
                           f"$\\bullet$ ${lf3} = 0$ vô nghiệm vì $\\Delta < 0$.\\\\" 
                           r"Ta có bảng xét dấu như sau:" + "\n" + table_latex + 
                           f"Dựa vào bảng xét dấu, biểu thức $f(x) {ops[kieu]}$ tương ứng với $x \\in {itv}$.")

            # --- XUẤT CÂU TRẮC NGHIỆM ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


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


def bt_dang47_p1_b2_c4_ds10(self):
            # Khai báo biến
            # --- Bước 1 & 2: Thiết lập thông số để bài toán luôn có nghiệm nguyên ---
            def generate_data():
                while True:
                    # Trong ảnh c = 2
                    c = 2
                    # Giả định chọn b và a trước để tạo ra đề bài có nghiệm đẹp
                    # Chọn b là số lẻ để giống bài mẫu (b=-3 hoặc b=12)
                    b_target = random.choice([-5, -3, -1, 3, 5, 7])
                    a_target = random.choice([1, 2, 4])
                    xB = -1 # Giữ xB = -1 giống ảnh cho cấu trúc đẹp

                    # Tính yB từ a, b, c, xB
                    yB = a_target*(xB**2) + b_target*xB + c

                    # Tính tung độ đỉnh yI = -Delta / 4a
                    delta = b_target**2 - 4*a_target*c
                    yI_val = Rational(-delta, 4*a_target)

                    # Kiểm tra nếu yI là phân số đẹp (mẫu số là 4 hoặc 2 hoặc nguyên)
                    if yI_val.denominator in [1, 2, 4]:
                        return a_target, b_target, xB, yB, c, yI_val

            a_val, b_val, xB, yB, c, yI_val = generate_data()
            yI_tex = latex(yI_val)

            # --- Giải hệ để lấy các cặp nghiệm (phục vụ lời giải chi tiết) ---
            b_sym = symbols('b')
            # a - b + 2 = yB => a = yB - 2 + b
            a_expr = (yB - c - b_sym * xB) # Vì xB = -1 nên xB^2 = 1
            eq_delta = b_sym**2 - 4*a_expr*c + 4*a_expr*yI_val
            sol_b = solve(eq_delta, b_sym)
            all_solutions = []
            for bs in sol_b:
                asol = (yB - c - bs * xB)
                all_solutions.append((int(asol), int(bs)))

            # --- Bước 3 & 4: Tạo nội dung, đáp án và lời giải y hệt mẫu ảnh ---

            # Nội dung câu hỏi
            noidungcauhoi = (f"Xác định parabol $y = ax^2 + bx + {c}$, biết rằng parabol đó đi qua điểm $B({xB};{yB})$ và đỉnh có tung độ ${yI_tex}$ ?")

            # Xây dựng các chuỗi latex cho lời giải
            # Dòng 1: a - b + 2 = yB
            line1 = f"a {'-' if xB == -1 else '+'} b + {c} = {yB}"
            line1_equiv = f"a {'-' if xB == -1 else '+'} b = {yB - c}"

            # Dòng 2: -Delta/4a = yI
            line2 = f"-\\frac{{\\Delta}}{{4a}} = {yI_tex}"
            # b^2 - 4ac = -4a * yI => b^2 - 8a = -4a * (yI)
            rhs_pt2 = latex(-4 * yI_val)
            line2_equiv = f"b^2 - {4*c}a = {rhs_pt2}a"

            # Phép thế a = ...
            a_sub = f"{yB - c} + b" if xB == -1 else f"{yB - c} - b"
            line3_pt2 = f"b^2 - {4*c}({a_sub}) = {rhs_pt2}({a_sub})"

            # Phương trình bậc 2 cuối cùng (thu gọn)
            final_eq = simplify(b_sym**2 - 4*c*(yB-c+b_sym) - (-4*yI_val)*(yB-c+b_sym))
            final_eq_tex = latex(final_eq) + " = 0"

            # Kết quả các trường hợp
            case_texts = []
            final_parabols = []
            for asol, bsol in all_solutions:
                p_tex = f"y = {asol}x^2 {'+' if bsol >=0 else '-'} {abs(bsol)}x + {c}".replace(" 1x", " x")
                final_parabols.append(f"${p_tex}$")
                case_texts.append(f"-Với $\\begin{{cases}} a = {asol} \\\\ b = {bsol} \\end{{cases}}$ ta có $(P): {p_tex}$.")

            # Lời giải chi tiết
            loigiai = (f"d) Vì $(P)$ đi qua điểm $B({xB};{yB})$ và có tung độ đỉnh bằng ${yI_tex}$ nên ta có \\\\ "
                       f"$\\begin{{cases}} {line1} \\\\ {line2} \\end{{cases}} "
                       f"\\Leftrightarrow \\begin{{cases}} {line1_equiv} \\\\ {line2_equiv} \\end{{cases}} "
                       f"\\Leftrightarrow \\begin{{cases}} a = {a_sub} \\\\ {line3_pt2} \\end{{cases}} "
                       f"\\Leftrightarrow \\begin{{cases}} a = {a_sub} \\\\ {final_eq_tex} \\end{{cases}}$ \\\\ "
                       f"$\\Leftrightarrow " + " \\text{ hoặc } ".join([f"\\begin{{cases}} a = {asol} \\\\ b = {bsol} \\end{{cases}}" for asol, bsol in all_solutions]) + "$ \\\\ " +
                       " \\\\ ".join(case_texts))

            # Đáp án trắc nghiệm
            da_d = "\\True " + " và ".join(final_parabols)
            s = [f"$y = {a_val+1}x^2 + {b_val+2}x + {c}$", 
                 f"$y = {a_val+2}x^2 - {b_val}x + {c}$", 
                 f"$y = {a_val}x^2 + {b_val-3}x + {c+2}$"]
            list_1 = [da_d] + s
            random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('+ +', '+').replace('+ -', '-')
            return content


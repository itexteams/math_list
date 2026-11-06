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


def bt_dang18_p1_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            # Hàm định dạng phương trình đẹp, xử lý dấu +- thành -
            def format_eq(a, b, c):
                terms = []
                if a == 1: terms.append("x")
                elif a == -1: terms.append("-x")
                elif a != 0: terms.append(f"{a}x")

                if b == 1: terms.append("+y")
                elif b == -1: terms.append("-y")
                elif b > 0: terms.append(f"+{b}y")
                elif b < 0: terms.append(f"{b}y")

                if c > 0: terms.append(f"+{c}")
                elif c < 0: terms.append(f"{c}")

                eq = "".join(terms) + "=0"
                if eq.startswith("+"): 
                    eq = eq[1:]

                # Luôn chú ý hiển thị - - là + hoặc + - là -
                eq = eq.replace("+ -", " - ").replace("- -", " + ").replace("+-", "-").replace("--", "+")
                return eq

            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # B1, B2, B3: Nghiên cứu, viết lại và tìm cách random bài toán
                # Random toạ độ điểm I
                xI = randint(-3, 3)
                yI = randint(-3, 3)

                # Random hệ số tự do của đường thẳng d (giữ n_d=(2; -1) để góc luôn cố định 45 độ đẹp)
                Cd = randint(-5, 5)

                # Random hệ số k cho khoảng cách d = k*sqrt(10)
                k = randint(1, 2)

                if k == 1:
                    dist_tex = "\\sqrt{10}"
                    dist_val_tex = "\\sqrt{10}"
                    dist_10k = 10
                else:
                    dist_tex = f"{k}\\sqrt{{10}}"
                    dist_val_tex = f"{k}\\sqrt{{10}}"
                    dist_10k = 10 * k

                d_eq = format_eq(2, -1, Cd)

                # Tính C cho trường hợp 1: a=3, b=1 -> \Delta: 3x + y + c = 0
                S1 = 3*xI + yI
                c1_1 = dist_10k - S1
                c1_2 = -dist_10k - S1

                # Tính C cho trường hợp 2: a=1, b=-3 -> \Delta: x - 3y + c' = 0
                S2 = xI - 3*yI
                c2_1 = dist_10k - S2
                c2_2 = -dist_10k - S2

                ans_lines = [
                    format_eq(3, 1, c1_1),
                    format_eq(3, 1, c1_2),
                    format_eq(1, -3, c2_1),
                    format_eq(1, -3, c2_2)
                ]

                ans_lines_str = "; ".join(ans_lines)

                # Tạo các đáp án nhiễu sai lệch hệ số
                def generate_wrong(offset1, offset2):
                    w_lines = [
                        format_eq(3, 1, c1_1 + offset1),
                        format_eq(3, 1, c1_2 - offset1),
                        format_eq(1, -3, c2_1 + offset2),
                        format_eq(1, -3, c2_2 - offset2)
                    ]
                    return "\\Delta: " + "; ".join(w_lines)

                da = "\\Delta: " + ans_lines_str

                s = [
                    generate_wrong(1, -1),
                    generate_wrong(2, 2),
                    generate_wrong(-1, 1),
                    generate_wrong(randint(-3,-1), randint(1,3)),
                    generate_wrong(3, 1),
                    generate_wrong(randint(1,3), randint(-3,-1))
                ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Nội dung câu hỏi
                noidungcauhoi = (f"Trong mặt phẳng với hệ trục tọa độ $Oxy$, cho đường thẳng $d: {d_eq}$ và điểm $I({xI}; {yI})$. "
                                 f"Phương trình đường thẳng $\\Delta$ cách điểm $I$ một khoảng bằng ${dist_tex}$ và tạo với đường thẳng $d$ một góc bằng $45^\\circ$ là")

                # Trộn đáp án
                da_d = ('\\True $%s$' % da)
                da_s1 = '$%s$' % das1
                da_s2 = '$%s$' % das2
                da_s3 = '$%s$' % das3

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Xử lý chuỗi tử số thay dấu +- thành -
                tuso1 = f"|{S1} + c|".replace("+-", "-").replace("+ -", "- ")

                # Nội dung lời giải
                loigiai=(f"Giả sử đường thẳng $\\Delta$ có phương trình: $ax + by + c = 0, a^2 + b^2 \\neq 0$.\\\\\n"
                         f"Đường thẳng $\\Delta$ có vectơ pháp tuyến $\\vec{{n}}_{{\\Delta}} = (a; b)$.\\\\\n"
                         f"Đường thẳng $d$ có vectơ pháp tuyến $\\vec{{n}}_d = (2; -1)$.\\\\\n"
                         f"Vì $\\Delta$ tạo với đường thẳng $d$ một góc $45^\\circ$ nên\\\\\n"
                         f"$\\cos(\\Delta; d) = |\\cos(\\vec{{n}}_{{\\Delta}}; \\vec{{n}}_d)| \\Leftrightarrow \\frac{{|2a - b|}}{{\\sqrt{{a^2+b^2}} \\cdot \\sqrt{{5}}}} = \\frac{{1}}{{\\sqrt{{2}}}} \\Leftrightarrow \\left[ \\begin{{array}}{{l}} a = 3b \\\\ b = -3a \\end{{array}} \\right.$\\\\\n"
                         f"Với $a = 3b$, chọn $b=1, a=3$, ta được $\\Delta: 3x + y + c = 0$.\\\\\n"
                         f"Mặt khác $d(I; \\Delta) = {dist_tex} \\Leftrightarrow \\frac{{{tuso1}}}{{\\sqrt{{10}}}} = {dist_val_tex} \\Leftrightarrow \\left[ \\begin{{array}}{{l}} c = {c1_1} \\\\ c = {c1_2} \\end{{array}} \\right.$\\\\\n"
                         f"Với $b = -3a$, tương tự ta có hai đường thẳng $\\Delta: {format_eq(1, -3, c2_1)}; {format_eq(1, -3, c2_2)}$.\\\\\n"
                         f"Vậy các đường thẳng cần tìm là: $\\Delta: {ans_lines_str}$")

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content 


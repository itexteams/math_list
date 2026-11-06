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


def bt_dang13_p4_b2_c2_ds10(self):
            # Khai báo biến 
            # Dạng 1: Max, Dạng 2: Min
            lisdang=['1', '2']
            dang=random.choice(lisdang)

            # Vòng lặp lấy ngẫu nhiên 3 điểm không thẳng hàng có tọa độ nguyên
            while True:
                xa, ya = randint(-4, 4), randint(-4, 4)
                xb, yb = randint(-4, 4), randint(-4, 4)
                xc, yc = randint(-4, 4), randint(-4, 4)

                # Tránh các điểm nằm trên cùng một đường thẳng hoặc trùng nhau
                if len({(xa, ya), (xb, yb), (xc, yc)}) < 3:
                    continue

                xAB, yAB = xb - xa, yb - ya
                xAC, yAC = xc - xa, yc - ya

                # Tính 2 lần diện tích
                area_double = abs(xAB * yAC - xAC * yAB)
                if 2 <= area_double <= 15: # Đảm bảo 3 điểm tạo thành 1 tam giác hợp lệ
                    break

            # Tạo ngẫu nhiên biểu thức F(x, y) = ax + by + c
            a_F = randint(-4, 4)
            b_F = randint(-4, 4)
            while a_F == 0 and b_F == 0:  # Đảm bảo a và b không đồng thời bằng 0
                a_F = randint(-4, 4)
                b_F = randint(-4, 4)
            c_F = randint(-5, 5)

            # Dùng Sympy để format biểu thức F(x, y) tự động đẹp mắt (xử lý dấu cộng trừ)
            y_sym = symbols('y')
            F_expr = a_F * x + b_F * y_sym + c_F
            F_str = latex(F_expr)

            # Tính giá trị tại các đỉnh
            F_A = a_F * xa + b_F * ya + c_F
            F_B = a_F * xb + b_F * yb + c_F
            F_C = a_F * xc + b_F * yc + c_F

            # Xác định kết quả tùy theo dạng bài
            if dang == '1':
                kq_val = max(F_A, F_B, F_C)
                loai_bai = "lớn nhất"
            else:
                kq_val = min(F_A, F_B, F_C)
                loai_bai = "nhỏ nhất"

            kq_str = str(kq_val)

            # Hàm định dạng phương trình đường thẳng ax + by = c đẹp mắt
            def format_eq(a, b):
                res = ""
                if a == 1: res += "x"
                elif a == -1: res += "-x"
                elif a != 0: res += str(a) + "x"

                if b == 1:
                    if a != 0: res += " + y"
                    else: res += "y"
                elif b == -1:
                    if a != 0: res += " - y"
                    else: res += "-y"
                elif b > 0:
                    if a != 0: res += " + " + str(b) + "y"
                    else: res += str(b) + "y"
                elif b < 0:
                    if a != 0: res += " - " + str(-b) + "y"
                    else: res += str(b) + "y"
                return res

            # Hàm tìm phương trình đường thẳng qua (x1, y1), (x2, y2)
            def get_line_info(x1, y1, x2, y2, x3, y3):
                a = y2 - y1
                b = -(x2 - x1)
                c = a * x1 + b * y1

                g = math.gcd(math.gcd(abs(a), abs(b)), abs(c))
                a, b, c = a // g, b // g, c // g

                if a < 0 or (a == 0 and b < 0):
                    a, b, c = -a, -b, -c

                val = a * x3 + b * y3
                if val < c:
                    sign = '\\le'
                else:
                    sign = '\\ge'

                eq_str = format_eq(a, b)
                return eq_str + " " + sign + " " + str(c), eq_str + " = " + str(c), a, b, c

            # Khởi tạo thông tin 3 cạnh AB, BC, CA
            ineq1, line1, _, _, _ = get_line_info(xa, ya, xb, yb, xc, yc)
            ineq2, line2, _, _, _ = get_line_info(xb, yb, xc, yc, xa, ya)
            ineq3, line3, _, _, _ = get_line_info(xc, yc, xa, ya, xb, yb)

            # Các phương án trắc nghiệm (số nguyên)
            du = ['$%s$' % (kq_str)]
            da = random.choice(du)

            distractors_set = set()
            options = [1, 2, 3, -1, -2, -3, 4, -4, 5, -5]
            random.shuffle(options)
            for offset in options:
                val = kq_val + offset
                s_val = str(val)
                if s_val not in distractors_set and val != kq_val:
                    distractors_set.add(s_val)
                if len(distractors_set) >= 6:
                    break

            distractors = list(distractors_set)
            s = ['$%s$' % (d) for d in distractors]

            das1 = random.choice(s)
            s.remove(das1)
            das2 = random.choice(s)
            s.remove(das2)
            das3 = random.choice(s)

            he_bpt = "\\begin{cases} %s \\\\ %s \\\\ %s \\end{cases}" % (ineq1, ineq2, ineq3)

            noidungcauhoi = ('''Tính giá trị %s của biểu thức $F(x; y) = %s$ trên miền nghiệm của hệ bất phương trình $%s$.''' % (loai_bai, F_str, he_bpt))

            da_d = ('\\True ' + str(da))
            da_s1 = str(das1)
            da_s2 = str(das2)
            da_s3 = str(das3)

            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Trình bày lời giải thay tọa độ
            def fmt_pt(x_val, y_val, res_val):
                # Hiển thị phép tính rõ ràng cho học sinh
                calc_str = ""
                if a_F != 0:
                    calc_str += f"{a_F} \\cdot ({x_val})"

                if b_F > 0:
                    calc_str += f" + {b_F} \\cdot ({y_val})"
                elif b_F < 0:
                    calc_str += f" - {-b_F} \\cdot ({y_val})"

                if c_F > 0:
                    calc_str += f" + {c_F}"
                elif c_F < 0:
                    calc_str += f" - {-c_F}"

                if calc_str == "":
                    calc_str = "0"
                elif calc_str.startswith(" + "):
                    calc_str = calc_str[3:]

                return calc_str + f" = {res_val}"

            loigiai_eval = (
                "Ta tính giá trị của biểu thức $F(x; y)$ tại các đỉnh của tam giác $ABC$:\\\\\n"
                "+ Tại đỉnh $A(%s; %s)$: $F(A) = %s$.\\\\\n"
                "+ Tại đỉnh $B(%s; %s)$: $F(B) = %s$.\\\\\n"
                "+ Tại đỉnh $C(%s; %s)$: $F(C) = %s$.\\\\\n"
            ) % (xa, ya, fmt_pt(xa, ya, F_A),
                 xb, yb, fmt_pt(xb, yb, F_B),
                 xc, yc, fmt_pt(xc, yc, F_C))

            loigiai_eval += "So sánh các giá trị trên, ta thấy giá trị %s của biểu thức là $%s$." % (loai_bai, kq_str)

            # --- Phần vẽ TikZ cho lời giải ---
            min_vx, max_vx = -5, 5
            min_vy, max_vy = -5, 5

            def get_hatch_code(x1, y1, x2, y2, x3, y3):
                vx, vy = x2 - x1, y2 - y1
                e1x, e1y = x1 - 10*vx, y1 - 10*vy
                e2x, e2y = x2 + 10*vx, y2 + 10*vy

                nx, ny = vy, -vx

                if (x3 - x1)*nx + (y3 - y1)*ny > 0:
                    nx, ny = -nx, -ny

                length = math.hypot(nx, ny)
                if length != 0:
                    nx, ny = (nx / length) * 20, (ny / length) * 20

                v3x, v3y = e2x + nx, e2y + ny
                v4x, v4y = e1x + nx, e1y + ny

                return (
                    "    \\fill[pattern=north west lines, pattern color=gray!70] (%s,%s) -- (%s,%s) -- (%s,%s) -- (%s,%s) -- cycle;\n"
                    "    \\draw[line width=1pt] (%s,%s) -- (%s,%s);\n" % 
                    (e1x, e1y, e2x, e2y, v3x, v3y, v4x, v4y, e1x, e1y, e2x, e2y)
                )

            # Đoạn mã TikZ 
            tikz_code = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=0.8, >=stealth]\n'
            '  \\draw[color=gray!30, thin] (%s,%s) grid (%s,%s);\n'
            '  \\draw[->] (%s,0) -- (%s,0) node[right] {$x$};\n'
            '  \\draw[->] (0,%s) -- (0,%s) node[above] {$y$};\n'
            '  \\node at (0,0) [below left] {$O$};\n'
            '  \\begin{scope}\n'
            '    \\clip (%s,%s) rectangle (%s,%s);\n'
            '%s' 
            '%s' 
            '%s' 
            '  \\end{scope}\n'
            '  \\fill (%s,%s) circle (2pt) node[above right] {$A$};\n'
            '  \\fill (%s,%s) circle (2pt) node[below left] {$B$};\n'
            '  \\fill (%s,%s) circle (2pt) node[below right] {$C$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}' % (min_vx, min_vy, max_vx, max_vy, 
                              min_vx, max_vx, min_vy, max_vy,
                              min_vx, min_vy, max_vx, max_vy,
                              get_hatch_code(xa, ya, xb, yb, xc, yc),  
                              get_hatch_code(xb, yb, xc, yc, xa, ya),  
                              get_hatch_code(xc, yc, xa, ya, xb, yb),
                              xa, ya, xb, yb, xc, yc)
            )

            # --- Nội dung lời giải (có TikZ) ---
            loigiai = ('''Gọi $d_1: %s$, $d_2: %s$, $d_3: %s$.\\\\
        Ta xác định tọa độ các giao điểm của các cặp đường thẳng:\\\\
        Giải hệ gồm $d_1$ và $d_3$ ta được $A(%s; %s)$.\\\\
        Giải hệ gồm $d_1$ và $d_2$ ta được $B(%s; %s)$.\\\\
        Giải hệ gồm $d_2$ và $d_3$ ta được $C(%s; %s)$.\\\\
        Miền nghiệm của hệ bất phương trình là miền đa giác (tam giác) $ABC$ (kể cả biên).\\\\
        Ta biểu diễn miền nghiệm của hệ trên mặt phẳng tọa độ $Oxy$ (phần không bị gạch chéo):\\\\
        %s
        %s''' %
                (line1, line2, line3, 
                 latex(xa), latex(ya), latex(xb), latex(yb), latex(xc), latex(yc), 
                 tikz_code, 
                 loigiai_eval))


            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content


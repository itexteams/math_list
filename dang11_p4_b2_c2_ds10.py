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


def bt_dang11_p4_b2_c2_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Vòng lặp lấy ngẫu nhiên 4 điểm tạo thành tứ giác lồi đặc biệt
                # Đảm bảo 4 điểm chạm 4 cạnh của hình chữ nhật bao quanh để tạo ra 4 tam giác vuông ở góc
                while True:
                    # Chọn ngẫu nhiên giới hạn của hình chữ nhật bao quanh
                    x_min, x_max = sorted([randint(-4, 2), randint(-2, 4)])
                    y_min, y_max = sorted([randint(-4, 2), randint(-2, 4)])

                    if x_max - x_min < 3 or y_max - y_min < 3:
                        continue

                    # Chọn 4 đỉnh lần lượt nằm trên 4 cạnh của hình chữ nhật bao quanh
                    xa, ya = randint(x_min + 1, x_max - 1), y_max  # Đỉnh A (Cao nhất)
                    xb, yb = x_max, randint(y_min + 1, y_max - 1)  # Đỉnh B (Phải nhất)
                    xc, yc = randint(x_min + 1, x_max - 1), y_min  # Đỉnh C (Thấp nhất)
                    xd, yd = x_min, randint(y_min + 1, y_max - 1)  # Đỉnh D (Trái nhất)

                    w = x_max - x_min
                    h = y_max - y_min
                    s_rect = w * h

                    # Diện tích 4 tam giác vuông xung quanh
                    s1 = 0.5 * abs(xb - xa) * abs(yb - ya)
                    s2 = 0.5 * abs(xc - xb) * abs(yc - yb)
                    s3 = 0.5 * abs(xd - xc) * abs(yd - yc)
                    s4 = 0.5 * abs(xa - xd) * abs(ya - yd)

                    area_val = s_rect - (s1 + s2 + s3 + s4)

                    # Đảm bảo tứ giác không bị thoái hóa hoặc diện tích quá nhỏ
                    if area_val >= 4: 
                        break

                # Trọng tâm tứ giác (dùng để xác định miền nghiệm khi vẽ gạch chéo)
                cx = (xa + xb + xc + xd) / 4
                cy = (ya + yb + yc + yd) / 4

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

                # Hàm tìm phương trình đường thẳng và xác định dấu bất phương trình
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
                    return eq_str + " " + sign + " " + str(c), eq_str + " = " + str(c)

                # 4 cạnh của tứ giác ABCD
                ineq1, line1 = get_line_info(xa, ya, xb, yb, cx, cy) # d1: AB
                ineq2, line2 = get_line_info(xb, yb, xc, yc, cx, cy) # d2: BC
                ineq3, line3 = get_line_info(xc, yc, xd, yd, cx, cy) # d3: CD
                ineq4, line4 = get_line_info(xd, yd, xa, ya, cx, cy) # d4: DA

                # Định dạng kết quả
                def fmt(num):
                    return str(num).replace('.0', '').replace('.', ',')

                kq_str = fmt(area_val)

                # Tạo các phương án trắc nghiệm
                du = ['$%s$' % (kq_str)]
                da = random.choice(du)

                distractors_set = set()
                options = [0.5, 1, 1.5, 2, 2.5, -0.5, -1, -1.5, 3]
                random.shuffle(options)
                for offset in options:
                    val = area_val + offset
                    if val > 0 and val != area_val:
                        s_val = fmt(val)
                        if s_val not in distractors_set:
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

                he_bpt = "\\begin{cases} %s \\\\ %s \\\\ %s \\\\ %s \\end{cases}" % (ineq1, ineq2, ineq3, ineq4)

                noidungcauhoi = ('''Tính diện tích miền nghiệm của hệ bất phương trình $%s$.''' % (he_bpt))

                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Chuỗi giải thích diện tích bằng hình chữ nhật
                loigiai_area = (
                    "Dựng hình chữ nhật bao quanh tứ giác $ABCD$ có các cạnh song song với các trục tọa độ.\\\\\n"
                    "Kích thước hình chữ nhật là $w = %s - (%s) = %s$ và $h = %s - (%s) = %s$.\\\\\n"
                    "Diện tích hình chữ nhật là $S_{\\text{hcn}} = %s \\cdot %s = %s$.\\\\\n"
                    "Diện tích phần nằm ngoài tứ giác $ABCD$ (bên trong hình chữ nhật) gồm 4 tam giác vuông tại các góc:\\\\\n"
                ) % (x_max, x_min, w, y_max, y_min, h, w, h, s_rect)

                loigiai_area += " $S_1 = \\frac{1}{2} |x_B - x_A| \\cdot |y_B - y_A| = \\frac{1}{2} |%s - (%s)| \\cdot |%s - (%s)| = %s$.\\\\\n" % (xb, xa, yb, ya, fmt(s1))
                loigiai_area += " $S_2 = \\frac{1}{2} |x_C - x_B| \\cdot |y_C - y_B| = \\frac{1}{2} |%s - (%s)| \\cdot |%s - (%s)| = %s$.\\\\\n" % (xc, xb, yc, yb, fmt(s2))
                loigiai_area += " $S_3 = \\frac{1}{2} |x_D - x_C| \\cdot |y_D - y_C| = \\frac{1}{2} |%s - (%s)| \\cdot |%s - (%s)| = %s$.\\\\\n" % (xd, xc, yd, yc, fmt(s3))
                loigiai_area += " $S_4 = \\frac{1}{2} |x_A - x_D| \\cdot |y_A - y_D| = \\frac{1}{2} |%s - (%s)| \\cdot |%s - (%s)| = %s$.\\\\\n" % (xa, xd, ya, yd, fmt(s4))

                sum_sub = s1 + s2 + s3 + s4
                loigiai_area += "Diện tích tứ giác $ABCD$ là:\\\\\n$S = S_{\\text{hcn}} - (S_1 + S_2 + S_3 + S_4) = %s - %s = %s$." % (fmt(s_rect), fmt(sum_sub), kq_str)

                # --- Phần vẽ TikZ cho lời giải ---
                min_vx, max_vx = -5, 5
                min_vy, max_vy = -5, 5

                def get_hatch_code(x1, y1, x2, y2, rx, ry):
                    vx, vy = x2 - x1, y2 - y1
                    e1x, e1y = x1 - 10*vx, y1 - 10*vy
                    e2x, e2y = x2 + 10*vx, y2 + 10*vy

                    nx, ny = vy, -vx
                    if (rx - x1)*nx + (ry - y1)*ny > 0:
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
                '%s' 
                '  \\end{scope}\n'
                '  \\draw[dashed, red, thick] (%s,%s) rectangle (%s,%s);\n'
                '  \\fill (%s,%s) circle (2pt) node[above right] {$A$};\n'
                '  \\fill (%s,%s) circle (2pt) node[below right] {$B$};\n'
                '  \\fill (%s,%s) circle (2pt) node[below left] {$C$};\n'
                '  \\fill (%s,%s) circle (2pt) node[above left] {$D$};\n'
                '\\end{tikzpicture}\n'
                '\\end{center}' % (min_vx, min_vy, max_vx, max_vy, 
                                  min_vx, max_vx, min_vy, max_vy,
                                  min_vx, min_vy, max_vx, max_vy,
                                  get_hatch_code(xa, ya, xb, yb, cx, cy),  
                                  get_hatch_code(xb, yb, xc, yc, cx, cy),  
                                  get_hatch_code(xc, yc, xd, yd, cx, cy),
                                  get_hatch_code(xd, yd, xa, ya, cx, cy),
                                  x_min, y_min, x_max, y_max, 
                                  xa, ya, xb, yb, xc, yc, xd, yd)
                )

                # --- Nội dung lời giải ---
                loigiai = ('''Gọi $d_1: %s$, $d_2: %s$, $d_3: %s$, $d_4: %s$.\\\\
            Ta xác định tọa độ các giao điểm của các cặp đường thẳng:\\\\
            Giải hệ gồm $d_1$ và $d_4$ ta được $A(%s; %s)$.\\\\
            Giải hệ gồm $d_1$ và $d_2$ ta được $B(%s; %s)$.\\\\
            Giải hệ gồm $d_2$ và $d_3$ ta được $C(%s; %s)$.\\\\
            Giải hệ gồm $d_3$ và $d_4$ ta được $D(%s; %s)$.\\\\
            Miền nghiệm của hệ bất phương trình là miền tứ giác $ABCD$ (kể cả biên).\\\\
            Ta biểu diễn miền nghiệm của hệ trên mặt phẳng tọa độ $Oxy$ (phần không bị gạch chéo):\\\\
            %s
            %s''' %
                (line1, line2, line3, line4,
                 xa, ya, xb, yb, xc, yc, xd, yd, 
                 tikz_code, 
                 loigiai_area))


            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content


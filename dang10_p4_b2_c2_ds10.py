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


def bt_dang10_p4_b2_c2_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Vòng lặp lấy ngẫu nhiên 3 điểm không thẳng hàng có tọa độ nguyên
                # và diện tích không quá nhỏ để hình vẽ đẹp mắt
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
                # và xác định dấu bất phương trình để chứa điểm (x3, y3)
                def get_line_info(x1, y1, x2, y2, x3, y3):
                    a = y2 - y1
                    b = -(x2 - x1)
                    c = a * x1 + b * y1

                    # Rút gọn hệ số
                    g = math.gcd(math.gcd(abs(a), abs(b)), abs(c))
                    a, b, c = a // g, b // g, c // g

                    # Chuẩn hóa để hệ số 'a' ưu tiên dương
                    if a < 0 or (a == 0 and b < 0):
                        a, b, c = -a, -b, -c

                    # Kiểm tra điểm thứ 3 thuộc miền nào để xác định dấu
                    val = a * x3 + b * y3
                    if val < c:
                        sign = '\\le'
                    else:
                        sign = '\\ge'

                    eq_str = format_eq(a, b)
                    return eq_str + " " + sign + " " + str(c), eq_str + " = " + str(c), a, b, c

                # Khởi tạo thông tin 3 cạnh AB, BC, CA
                ineq1, line1, a1, b1, c1 = get_line_info(xa, ya, xb, yb, xc, yc)
                ineq2, line2, a2, b2, c2 = get_line_info(xb, yb, xc, yc, xa, ya)
                ineq3, line3, a3, b3, c3 = get_line_info(xc, yc, xa, ya, xb, yb)

                # Tính toán kết quả
                kq_val = area_double / 2
                # Định dạng số thập phân
                kq_str = str(kq_val).replace('.0', '').replace('.', ',')

                # Tạo các phương án trắc nghiệm
                du = ['$%s$' % (kq_str)]
                da = random.choice(du)

                distractors_set = set()
                options = [0.5, 1, 1.5, 2, 2.5, -0.5, -1, -1.5, 3]
                random.shuffle(options)
                for offset in options:
                    val = kq_val + offset
                    if val > 0 and val != kq_val:
                        s_val = str(val).replace('.0', '').replace('.', ',')
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

                he_bpt = "\\begin{cases} %s \\\\ %s \\\\ %s \\end{cases}" % (ineq1, ineq2, ineq3)

                noidungcauhoi = ('''Tính diện tích miền nghiệm của hệ bất phương trình $%s$.''' % (he_bpt))

                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Tính toán diện tích bằng phương pháp hình chữ nhật bao quanh
                x_min = min(xa, xb, xc)
                x_max = max(xa, xb, xc)
                y_min = min(ya, yb, yc)
                y_max = max(ya, yb, yc)

                w = x_max - x_min
                h = y_max - y_min
                s_rect = w * h

                def fmt(num):
                    return str(num).replace('.0', '').replace('.', ',')

                # Chuỗi giải thích diện tích
                loigiai_area = (
                    "Dựng hình chữ nhật bao quanh tam giác $ABC$ có các cạnh song song với các trục tọa độ.\\\\\n"
                    "Kích thước hình chữ nhật là $w = %s - (%s) = %s$ và $h = %s - (%s) = %s$.\\\\\n"
                    "Diện tích hình chữ nhật là $S_{\\text{hcn}} = %s \\cdot %s = %s$.\\\\\n"
                    "Diện tích phần nằm ngoài tam giác $ABC$ (nhưng bên trong hình chữ nhật) gồm 3 tam giác vuông xung quanh:\\\\\n"
                ) % (x_max, x_min, w, y_max, y_min, h, w, h, s_rect)

                sum_sub = 0
                for idx, (p1, p2) in enumerate([((xa, ya), (xb, yb)), ((xb, yb), (xc, yc)), ((xc, yc), (xa, ya))], 1):
                    s_val = 0.5 * abs(p1[0] - p2[0]) * abs(p1[1] - p2[1])
                    loigiai_area += " $S_%s = \\frac{1}{2} |%s - (%s)| \\cdot |%s - (%s)| = %s$.\\\\\n" % (idx, p1[0], p2[0], p1[1], p2[1], fmt(s_val))
                    sum_sub += s_val

                loigiai_area += "Diện tích tam giác $ABC$ là:\\\\\n$S = S_{\\text{hcn}} - (S_1 + S_2 + S_3) = %s - %s = %s$." % (fmt(s_rect), fmt(sum_sub), kq_str)

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

                # Đoạn mã TikZ đã bổ sung hình chữ nhật bao quanh (nét đứt màu đỏ)
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
                '  \\draw[dashed, red, thick] (%s,%s) rectangle (%s,%s);\n'
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
                                  x_min, y_min, x_max, y_max, # Tọa độ hcn
                                  xa, ya, xb, yb, xc, yc)
                )

                # --- Nội dung lời giải (có TikZ) ---
                loigiai = ('''Gọi $d_1: %s$, $d_2: %s$, $d_3: %s$.\\\\
            Ta xác định tọa độ các giao điểm của các cặp đường thẳng:\\\\
            Giải hệ gồm $d_1$ và $d_3$ ta được $A(%s; %s)$.\\\\
            Giải hệ gồm $d_1$ và $d_2$ ta được $B(%s; %s)$.\\\\
            Giải hệ gồm $d_2$ và $d_3$ ta được $C(%s; %s)$.\\\\
            Miền nghiệm của hệ bất phương trình là miền trong của tam giác $ABC$ (kể cả biên).\\\\
            Ta biểu diễn miền nghiệm của hệ trên mặt phẳng tọa độ $Oxy$ (phần không bị gạch chéo):\\\\
            %s
            %s''' %
                (line1, line2, line3, 
                 latex(xa), latex(ya), latex(xb), latex(yb), latex(xc), latex(yc), 
                 tikz_code, 
                 loigiai_area))


            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content


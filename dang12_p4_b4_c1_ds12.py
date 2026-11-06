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


def bt_dang12_p4_b4_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random tham số để tạo đồ thị hàm bậc 3
                # Chọn hệ số A để kiểm soát độ dốc (đảm bảo ra số nguyên)
                A = random.choice([1, 2])
                # Chọn tọa độ điểm uốn I(x_u, y_u)
                x_u = random.randint(-1, 1)
                y_u = random.randint(-2, 2)

                # Từ điểm uốn, xác định hoành độ 2 điểm cực trị (cách điểm uốn 1 đơn vị để tọa độ chẵn đẹp)
                x1 = x_u - 1
                x2 = x_u + 1

                # Tính tung độ cực trị dựa trên hàm y = A(x - x_u)^3 - 3A(x - x_u) + y_u
                y1 = 2 * A + y_u
                y2 = -2 * A + y_u

                # Đường thẳng qua 2 điểm cực trị: y = ax + b
                # Hệ số góc a = m_line, tung độ gốc b = n_line
                m_line = -2 * A
                n_line = y1 - m_line * x1

                # Tính giá trị biểu thức yêu cầu: a - 2b
                kq_val = m_line - 2 * n_line
                kq = str(kq_val)

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (kq)]
                da = random.choice(du)

                # Tạo các đáp án sai không trùng đáp án đúng
                s_set = set()
                while len(s_set) < 3:
                    fake_val = kq_val + random.choice([-4, -3, -2, -1, 1, 2, 3, 4, 5])
                    if fake_val != kq_val:
                        s_set.add('$%s$' % str(fake_val))
                s_list = list(s_set)

                das1 = s_list[0]
                das2 = s_list[1]
                das3 = s_list[2]

                # Tính các hệ số của hàm số y = px^3 + qx^2 + rx + s để vẽ bằng TikZ
                p = A
                q = -3 * A * x_u
                r = 3 * A * (x_u**2) - 3 * A
                s_val = -A * (x_u**3) + 3 * A * x_u + y_u

                # Xây dựng ranh giới đồ thị cho TikZ
                xmin = min(-1, x1 - 1)
                xmax = max(1, x2 + 1)
                ymin = min(-1, y2 - 1)
                ymax = max(1, y1 + 1)

                x_axis_min = xmin - 0.5
                x_axis_max = xmax + 0.5
                y_axis_min = ymin - 0.5
                y_axis_max = ymax + 0.5

                # Tạo các điểm chia vạch (ticks) trên trục tọa độ
                x_ticks = [val for val in [x1, x2, x_u] if val != 0]
                y_ticks = [val for val in [y1, y2, y_u] if val != 0]

                x_ticks_str = ",".join(["%s/%s" % (val, val) for val in x_ticks])
                y_ticks_str = ",".join(["%s/%s" % (val, val) for val in y_ticks])

                x_ticks_code = "\\foreach \\x/\\nx in {%s}\n\\draw[thin] (\\x,1pt)--(\\x,-1pt) node [below] {$\\nx$};" % x_ticks_str if x_ticks else ""
                y_ticks_code = "\\foreach \\y/\\ny in {%s}\n\\draw[thin] (1pt,\\y)--(-1pt,\\y) node [left] {$\\ny$};" % y_ticks_str if y_ticks else ""

                # Vẽ các đường gióng đứt nét tới điểm cực trị và điểm uốn
                dashed_lines = ""
                if x1 != 0 and y1 != 0:
                    dashed_lines += "\\draw[dashed,thin](%s,0)--(%s,%s)--(0,%s);\n" % (x1, x1, y1, y1)
                if x2 != 0 and y2 != 0:
                    dashed_lines += "\\draw[dashed,thin](%s,0)--(%s,%s)--(0,%s);\n" % (x2, x2, y2, y2)
                if x_u != 0 and y_u != 0:
                    dashed_lines += "\\draw[dashed,thin](%s,0)--(%s,%s)--(0,%s);\n" % (x_u, x_u, y_u, y_u)

                circle_node = "\\draw[fill=white] (%s,%s) circle (1.5pt);" % (x_u, y_u)

                # Phương trình hàm số để vẽ TikZ
                plot_eq = "%s*(\\x)^3 + (%s)*(\\x)^2 + (%s)*(\\x) + (%s)" % (p, q, r, s_val)

                # Đoạn TikZ vẽ đồ thị
                tikz_code = ('''\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,line width=1pt]
            \\tikzset{every node/.style={scale=0.9}}
            \\draw[->] (%s,0)--(%s,0) node[below left] {$x$};
            \\draw[->] (0,%s)--(0,%s) node[below left] {$y$};
            \\draw (0,0) node [below left] {$O$};
            %s
            %s
            %s
            %s
            \\begin{scope}
                \\clip (%s,%s) rectangle (%s,%s);
                \\draw[samples=200,domain=%s:%s,smooth,variable=\\x] plot (\\x,{%s});
            \\end{scope}
            \\end{tikzpicture}''' % (
                    x_axis_min, x_axis_max,
                    y_axis_min, y_axis_max,
                    x_ticks_code,
                    y_ticks_code,
                    dashed_lines.strip(),
                    circle_node,
                    x_axis_min, y_axis_min, x_axis_max, y_axis_max,
                    x_axis_min, x_axis_max, plot_eq
                ))

                # Nội dung câu hỏi
                noidungcauhoi = ('''Cho hàm số $y = ax^3 + bx^2 + cx + d$ ($a,b,c,d \\in \\mathbb{R}$) có đồ thị $(C)$ trong hình dưới đây.
            \\begin{center}
            %s
            \\end{center}
            Đường thẳng đi qua 2 điểm cực trị của đồ thị $(C)$ có dạng: $y = ax + b$, với $a,b \\in \\mathbb{R}$. Tính $a - 2b$.''' % (tikz_code))

                # Xử lý random phương án hiển thị
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Xử lý text hiển thị hệ phương trình lời giải cho chuẩn toán học
                def get_eq_left(x_val):
                    if x_val == 0: return "b"
                    if x_val == 1: return "a + b"
                    if x_val == -1: return "-a + b"
                    return "%sa + b" % x_val

                eq1_left = get_eq_left(x1)
                eq2_left = get_eq_left(x2)

                n_part = "+ %s" % n_line if n_line > 0 else ("- %s" % abs(n_line) if n_line < 0 else "")
                line_eq_str = "%sx %s" % (m_line, n_part)
                line_eq_str = line_eq_str.strip()

                # Nội dung lời giải
                loigiai = ('''Từ đồ thị hàm số, ta xác định được 2 điểm cực trị của hàm số là $A(%s; %s)$ và $B(%s; %s)$. \\\\
            Đường thẳng đi qua 2 điểm cực trị có dạng $y = ax + b$. \\\\
            Ta có hệ phương trình:
            $\\begin{cases} %s = %s \\\\ %s = %s \\end{cases} \\Leftrightarrow \\begin{cases} a = %s \\\\ b = %s \\end{cases}$. \\\\
            Vậy đường thẳng đi qua 2 điểm cực trị có phương trình $y = %s$. \\\\
            Suy ra $a = %s, b = %s$. \\\\
            Khi đó, giá trị $a - 2b = %s - 2(%s) = %s$.''' % (
                    x1, y1, x2, y2,
                    eq1_left, y1, eq2_left, y2, m_line, n_line,
                    line_eq_str,
                    m_line, n_line,
                    m_line, n_line, kq_val
                ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + 
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content  


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


def bt_dang50_p4_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            # Khai báo biến ngẫu nhiên
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bộ số gốc từ đề bài: I(6,2), M(1,5), d: x+y-5=0
                # Tịnh tiến bộ số để tạo bài toán mới (k là hệ số tịnh tiến)
                k = random.randint(-3, 3)
                xi, yi = 6 + k, 2 + k
                xm, ym = 1 + k, 5 + k
                # Đường thẳng d: x + y - c = 0. Ở đề gốc c = 5.
                # Khi tịnh tiến (x-k, y-k), phương trình trở thành (x-k) + (y-k) - 5 = 0 => x + y - (5+2k) = 0
                c_val = 5 + 2*k

                # Tính toán các giá trị cho lời giải
                # E thuộc d => E(t, c_val - t)
                # I là trung điểm NE => N = 2I - E = (2*xi - t, 2*yi - (c_val - t))
                nx_expr = 2 * xi # phần số của tọa độ x của N: 2*xi - t
                ny_expr_const = 2 * yi - c_val # phần số của tọa độ y của N: ny_expr_const + t

                # Vector MN = (nx_expr - t - xm, ny_expr_const + t - ym)
                # MN = (v1_const - t, t + v2_const)
                v1_const = nx_expr - xm
                v2_const = ny_expr_const - ym

                # Vector IE = (t - xi, c_val - t - yi)
                # IE = (t - xi, ie2_const - t)
                ie2_const = c_val - yi

                # Giải phương trình tích vô hướng MN.IE = 0
                # (v1_const - t)(t - xi) + (t + v2_const)(ie2_const - t) = 0
                # Đây là phương trình tương đương với đề bài: (11-t)(t-6) + (t-6)(3-t) = 0 (khi k=0)
                # Nghiệm luôn là t1 = xi (tương ứng t=6) và t2 = xi + 1 (tương ứng t=7)
                t1 = xi
                t2 = xi + 1

                def get_line_equation(p1, p2):
                    x1, y1 = p1
                    x2, y2 = p2
                    a = y2 - y1
                    b = -(x2 - x1)
                    c = -a * x1 - b * y1
                    if a == 0 and b == 0: return "y = 0"
                    common = math.gcd(math.gcd(a, b), c)
                    a //= common; b //= common; c //= common
                    if a < 0 or (a == 0 and b < 0):
                        a, b, c = -a, -b, -c

                    res = ""
                    if a != 0:
                        res += "x" if a == 1 else "-x" if a == -1 else f"{a}x"
                    if b != 0:
                        sign = " + " if b > 0 and a != 0 else " - " if b < 0 and a != 0 else "-" if b == -1 else ""
                        val = abs(b) if abs(b) != 1 else ""
                        res += f"{sign}{val}y"
                    if c != 0:
                        res += f" + {c} = 0" if c > 0 else f" - {abs(c)} = 0"
                    else:
                        res += " = 0"
                    return res

                # TH1: t = t1
                n1 = (2*xi - t1, 2*yi - c_val + t1)
                line1 = get_line_equation((xm, ym), n1)

                # TH2: t = t2
                n2 = (2*xi - t2, 2*yi - c_val + t2)
                line2 = get_line_equation((xm, ym), n2)

                # Đáp án đúng
                da_dung = f"$AB: {line1}$ và $AB: {line2}$"

                # Tạo các phương án nhiễu
                s1 = f"$AB: {line1}$"
                s2 = f"$AB: {line2}$"
                s3 = f"$AB: x + y - {xm+ym} = 0$ và $AB: {line1}$"

                du = [da_dung]
                da = random.choice(du)

                s = [s1, s2, s3]
                random.shuffle(s)
                das1, das2, das3 = s[0], s[1], s[2]

                # Nội dung câu hỏi
                noidungcauhoi = ('''Trong mặt phẳng với hệ tọa độ $Oxy$, cho hình chữ nhật $ABCD$ có điểm $I(%s;%s)$ là giao điểm của hai đường thẳng $AC$ và $BD$. Điểm $M(%s;%s)$ thuộc đường thẳng $AB$ và trung điểm $E$ của cạnh $CD$ thuộc đường thẳng $d: x + y - %s = 0$. Lập phương trình đường thẳng $AB$.'''
                                 % (latex(xi), latex(yi), latex(xm), latex(ym), latex(c_val)))

                # Nội dung lời giải
                loigiai = ('''Do $E \\in d$ nên $E(t; %s-t)$. Gọi $N$ là trung điểm $AB$, suy ra $I$ là trung điểm $NE$ nên $N(%s-t; t-%s)$. \\\\
            Ta có $\\overrightarrow{MN} = (%s-t; t-%s), \\overrightarrow{IE} = (t-%s; %s-t)$. \\\\
            Do $ABCD$ là hình chữ nhật nên $\\overrightarrow{MN} \\cdot \\overrightarrow{IE} = 0 \\Leftrightarrow (%s-t)(t-%s) + (t-%s)(%s-t) = 0 \\Leftrightarrow \\left[\\begin{array}{l} t = %s \\\\ t = %s \\end{array}\\right.$ \\\\
            Với $t = %s$ suy ra $N(%s; %s)$. Đường thẳng $AB$ đi qua hai điểm $M$ và $N$ nên có phương trình $AB: %s$. \\\\
            Với $t = %s$ suy ra $N(%s; %s)$. Đường thẳng $AB$ đi qua hai điểm $M$ và $N$ nên có phương trình $AB: %s$.'''
                           % (latex(c_val), latex(2*xi), latex(c_val - 2*yi), 
                              latex(v1_const), latex(abs(v2_const)), latex(xi), latex(ie2_const),
                              latex(v1_const), latex(xi), latex(abs(v2_const)), latex(ie2_const),
                              latex(t1), latex(t2),
                              latex(t1), latex(n1[0]), latex(n1[1]), line1,
                              latex(t2), latex(n2[0]), latex(n2[1]), line2))

                # Các đáp án
                da_d = '\\True ' + str(da)
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content 


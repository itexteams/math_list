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


def bt_dang25_p3_b1_c2_hh12(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Tìm phương trình mặt phẳng qua 3 điểm A, B, C có dạng ax + by + cz + d0 = 0
        # Cần đảm bảo hệ số tự do d0 != 0 và tỉ lệ chuẩn xác
        d0 = random.choice([1, 2, 3, 4, 5, -1, -2, -3, -4, -5])

        while True:
            # Chọn ngẫu nhiên tọa độ điểm A, B, C sao cho không thẳng hàng
            xA, yA, zA = randint(-5, 5), randint(-5, 5), randint(-5, 5)
            xB, yB, zB = randint(-5, 5), randint(-5, 5), randint(-5, 5)
            xC, yC, zC = randint(-5, 5), randint(-5, 5), randint(-5, 5)

            # Vectơ AB và AC
            u1, u2, u3 = xB - xA, yB - yA, zB - zA
            v1, v2, v3 = xC - xA, yC - yA, zC - zA

            # Tích có hướng [AB, AC]
            nx = u2 * v3 - u3 * v2
            ny = u3 * v1 - u1 * v3
            nz = u1 * v2 - u2 * v1

            # Kiểm tra không thẳng hàng
            if nx == 0 and ny == 0 and nz == 0:
                continue

            # Hệ số tự do của phương trình nx*x + ny*y + nz*z + D = 0
            D = -(nx * xA + ny * yA + nz * zA)

            # Mặt phẳng không đi qua gốc tọa độ (D != 0)
            if D == 0:
                continue

            # Ta cần đưa về dạng ax + by + cz + d0 = 0
            # Tức là nhân cả hai vế với d0 / D
            a_val = Rational(nx * d0, D)
            b_val = Rational(ny * d0, D)
            c_val = Rational(nz * d0, D)

            # Yêu cầu a, b, c là các số nguyên đẹp hoặc phân số gọn, ưu tiên a, b, c là số nguyên
            if a_val.q == 1 and b_val.q == 1 and c_val.q == 1:
                a = int(a_val)
                b = int(b_val)
                c = int(c_val)
                tong = a + b + c
                if -999 < tong < 9999:
                    break

        # Tính toán các bước lời giải
        pt_p_str = ''
        terms = []
        # Ghép biểu thức ax + by + cz + d0 = 0
        if a == 1:
            terms.append('x')
        elif a == -1:
            terms.append('-x')
        elif a != 0:
            terms.append('%sx' % a)

        if b == 1:
            terms.append('+ y' if terms else 'y')
        elif b == -1:
            terms.append('- y' if terms else '-y')
        elif b > 0:
            terms.append('+ %sy' % b if terms else '%sy' % b)
        elif b < 0:
            terms.append('- %sy' % abs(b) if terms else '-%sy' % abs(b))

        if c == 1:
            terms.append('+ z' if terms else 'z')
        elif c == -1:
            terms.append('- z' if terms else '-z')
        elif c > 0:
            terms.append('+ %sz' % c if terms else '%sz' % c)
        elif c < 0:
            terms.append('- %sz' % abs(c) if terms else '-%sz' % abs(c))

        if d0 > 0:
            terms.append('+ %s' % d0)
        else:
            terms.append('- %s' % abs(d0))

        pt_p_str = ' '.join(terms) + ' = 0'

        # Dạng hiển thị dạng tổng quát ax + by + cz + d0 = 0
        if d0 > 0:
            dang_pt = 'ax+by+cz+%s=0' % d0
        else:
            dang_pt = 'ax+by+cz-%s=0' % abs(d0)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Trong không gian tọa độ $Oxyz$, phương trình mặt phẳng $(P)$ đi qua ba điểm $A(%s;%s;%s)$, $B(%s;%s;%s)$, $C(%s;%s;%s)$ có dạng $%s$, khi đó giá trị của biểu thức $a+b+c$ bằng bao nhiêu?'''
                         % (xA, yA, zA, xB, yB, zB, xC, yC, zC, dang_pt))

        # Nội dung lời giải
        loigiai = ('''Ta có:\\\\
    $\\vec{AB} = (%s;%s;%s)$\\\\
    $\\vec{AC} = (%s;%s;%s)$\\\\
    Vectơ pháp tuyến của mặt phẳng $(P)$ cùng phương với tích có hướng $[\\vec{AB},\\vec{AC}]$:\\\\
    $[\\vec{AB},\\vec{AC}] = \\left( (%s)\\cdot(%s) - (%s)\\cdot(%s);\\; (%s)\\cdot(%s) - (%s)\\cdot(%s);\\; (%s)\\cdot(%s) - (%s)\\cdot(%s) \\right) = (%s;%s;%s)$.\\\\
    Mặt phẳng $(P)$ đi qua điểm $A(%s;%s;%s)$ và có một vectơ pháp tuyến là $\\vec{n} = (%s;%s;%s)$ nên có phương trình:\\\\
    $%s(x - %s) + (%s)(y - %s) + (%s)(z - %s) = 0$\\\\
    $\\Leftrightarrow %s = 0$.\\\\
    Đồng nhất với phương trình dạng $%s$, ta được:\\\\
    $a = %s$, $b = %s$, $c = %s$.\\\\
    Suy ra $a + b + c = %s + (%s) + (%s) = %s$.'''
                   % (u1, u2, u3,
                      v1, v2, v3,
                      u2, v3, u3, v2,
                      u3, v1, u1, v3,
                      u1, v2, u2, v1,
                      nx, ny, nz,
                      xA, yA, zA,
                      a, b, c,
                      a, xA, b, yA, c, zA,
                      pt_p_str,
                      dang_pt,
                      a, b, c,
                      a, b, c, tong))

        # Đáp án
        dapan = '\\shortans{$%s$}\n' % (tong)

    # Xuất câu hỏi với đáp án và lời giải đã được định dạng
    content = ('\\begin{minipage}{\\textwidth}\n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               str(dapan) +
               '\\loigiai{\n' +
               str(loigiai) + '\n}\n' +
               '\\end{ex}\n' +
               '\\end{minipage}\n\n')
    return content


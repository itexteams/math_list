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


def bt_dang5_p3_b3_c3_hh10(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Tâm I(a, b)
        a = randint(-4, 4)
        b = randint(-4, 4)

        # Chọn bộ số Pytago (R, AM, IA) để bài toán có số nguyên đẹp
        pytagos = [
            (3, 4, 5),
            (4, 3, 5),
            (5, 12, 13),
            (6, 8, 10),
            (8, 6, 10)
        ]
        R_val, AM_val, d_val = random.choice(pytagos)

        # Tìm dx, dy sao cho dx^2 + dy^2 = d_val^2
        valid_deltas = []
        for dx_i in range(-d_val, d_val + 1):
            rem = d_val**2 - dx_i**2
            dy_i = int(math.isqrt(rem))
            if dy_i**2 == rem and dy_i > 0:
                valid_deltas.append((dx_i, dy_i))
                valid_deltas.append((dx_i, -dy_i))

        dx, dy = random.choice(valid_deltas)
        xA = a + dx
        yA = b + dy

        R = R_val
        R2 = R**2
        IA = d_val
        AM = AM_val

        # Tạo chuỗi phương trình đường tròn (C)
        part_x = "(x - %s)^2" % (a) if a > 0 else ("(x + %s)^2" % (-a) if a < 0 else "x^2")
        part_y = "(y - %s)^2" % (b) if b > 0 else ("(y + %s)^2" % (-b) if b < 0 else "y^2")
        pt_dt = "%s + %s = %s" % (part_x, part_y, R2)

        # Tính độ dài MN = 2 * (R * AM) / IA
        MN_val = Rational(2 * R * AM, IA)

        # Làm tròn/định dạng đáp án
        number = Decimal(float(MN_val))
        kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP) if MN_val % 1 == 0 else number.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        kq_str = str(kq).replace('.', ',')

        # Hình vẽ TikZ chuẩn 100% theo mẫu phong cách
        tikz_code = (
            "\\begin{center}\n"
            "\\begin{tikzpicture}[scale=0.9, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n"
            "    \\coordinate (I) at (0,0);\n"
            "    \\coordinate (A) at (5,0);\n"
            "    \\coordinate (M) at (1.8,2.4);\n"
            "    \\coordinate (N) at (1.8,-2.4);\n"
            "    \\coordinate (H) at (1.8,0);\n"
            "    \\draw[line width=1pt] (I) circle (3cm);\n"
            "    \\draw[line width=1pt] (A)--(M)--(I)--(A)--(N)--(I) (M)--(N);\n"
            "    \\draw[line width=1pt, dashed] (I)--(H);\n"
            "    \\fill (I) circle (1pt) node[left] {$I$};\n"
            "    \\fill (A) circle (1pt) node[right] {$A$};\n"
            "    \\fill (M) circle (1pt) node[above] {$M$};\n"
            "    \\fill (N) circle (1pt) node[below] {$N$};\n"
            "    \\fill (H) circle (1pt) node[above left] {$H$};\n"
            "\\end{tikzpicture}\n"
            "\\end{center}"
        )

        # Nội dung câu hỏi
        noidungcauhoi = ('''Trong mặt phẳng tọa độ $Oxy$, cho phương trình đường tròn $(C): %s$ và điểm $A(%s;%s)$. Từ $A$ kẻ hai tiếp tuyến $AM,AN$ đến $(C)$ với $M,N$ là các tiếp điểm. Độ dài đoạn thẳng $MN$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần trăm).'''
                         %(pt_dt,
                           xA,
                           yA
                         ))

        # Nội dung lời giải
        loigiai = ('''%sTa có \\\\
    Đường tròn $(C)$ có tâm $I(%s;%s)$ và bán kính $R = \\sqrt{%s} = %s$. \\\\
    Ta có $\\vec{IA} = (%s;%s) \\Rightarrow IA = \\sqrt{(%s)^2 + (%s)^2} = %s$. \\\\
    Vì $AM$ là tiếp tuyến của $(C)$ tại $M$ nên tam giác $AMI$ vuông tại $M$. \\\\
    Áp dụng định lý Pytago trong tam giác vuông $AMI$, ta có: \\\\
    $AM = \\sqrt{IA^2 - IM^2} = \\sqrt{%s^2 - %s^2} = %s$. \\\\
    Gọi $H$ là giao điểm của $IA$ và $MN$. \\\\
    Vì $AM = AN$ và $IM = IN = R$ nên $IA$ là đường trung trực của đoạn thẳng $MN$, suy ra $IA \\perp MN$ tại trung điểm $H$ của $MN$. \\\\
    Áp dụng hệ thức lượng trong tam giác vuông $AMI$ có đường cao $MH$, ta có: \\\\
    $MH = \\frac{AM \\cdot IM}{IA} = \\frac{%s \\cdot %s}{%s} = %s$. \\\\
    Do đó độ dài đoạn thẳng $MN$ là: \\\\
    $MN = 2 \\cdot MH = 2 \\cdot %s = %s \\approx %s$.'''
                   %(tikz_code,
                     a, b, R2, R,
                     xA - a, yA - b, xA - a, yA - b, IA,
                     IA, R, AM,
                     AM, R, IA, latex(Rational(AM * R, IA)),
                     latex(Rational(AM * R, IA)), latex(MN_val), str(kq_str)
                   ))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n'
               '\\end{ex}\n'
               '\\end{minipage} \n\n')
    return content


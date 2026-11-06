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


def bt_dang61_p4_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 1: Random hóa tọa độ điểm M(x0, y0)
                # Chọn x0, y0 là các số chính phương để khai căn ra số nguyên cho đẹp giống mẫu
                pairs = [(4, 1), (1, 4), (9, 1), (1, 9), (4, 4), (9, 4), (4, 9)]
                x0, y0 = random.choice(pairs)

                # Bước 2: Tính toán các thông số cho lời giải
                # Đường thẳng d: a(x - x0) + b(y - y0) = 0 <=> ax + by - (ax0 + by0) = 0
                # OA = (ax0 + by0)/a, OB = (ax0 + by0)/b
                # OA + OB = x0 + y0 + (by0/a) + (ax0/b)
                # Min khi by0/a = ax0/b <=> b^2 * y0 = a^2 * x0 <=> b/a = sqrt(x0/y0)

                val_a = int(math.sqrt(y0))
                val_b = int(math.sqrt(x0))

                # Rút gọn tỉ số a, b nếu cần
                ucln = math.gcd(val_a, val_b)
                val_a //= ucln
                val_b //= ucln

                # Hệ số phương trình: ax + by + c = 0
                c_term = -(val_a * x0 + val_b * y0)

                # Giá trị nhỏ nhất của OA + OB
                min_val = int((math.sqrt(x0) + math.sqrt(y0))**2)

                # Các biểu thức trong lời giải
                tu_so_latex = latex(val_a * x0 + val_b * y0) # Tương ứng 4a + b trong mẫu nếu a=1
                # Ở đây mẫu dùng n=(a,b) tổng quát, ta sẽ viết lời giải theo biến a, b như mẫu

                # Đáp án đúng
                def format_eq(a, b, c):
                    res = ""
                    if a == 1: res += "x"
                    elif a == -1: res += "-x"
                    else: res += f"{a}x"

                    if b > 0: res += f"+{b if b != 1 else ''}y"
                    else: res += f"{b if b != -1 else '-'}y"

                    if c > 0: res += f"+{c}=0"
                    else: res += f"{c}=0"
                    return res

                da_dung = f"${format_eq(val_a, val_b, c_term)}$"

                # Các phương án sai
                s = [
                    f"${format_eq(val_a, val_b, -c_term)}$", # Sai dấu hệ số tự do
                    f"${format_eq(val_b, val_a, -(val_b * x0 + val_a * y0))}$", # Hoán đổi hệ số a, b
                    f"${format_eq(val_a, val_b + 1, -(val_a * x0 + (val_b + 1) * y0))}$",
                    f"${format_eq(val_a + 1, val_b, -((val_a + 1) * x0 + val_b * y0))}$"
                ]

                # Loại bỏ trùng lặp nếu có và chọn 3 đáp án sai
                s = list(set([x for x in s if x != da_dung]))
                random.shuffle(s)
                das1, das2, das3 = s[:3]

                # Nội dung câu hỏi
                noidungcauhoi = ('''Trong mặt phẳng với hệ tọa độ $Oxy$, lập phương trình đường thẳng $d$ đi qua $M(%s;%s)$ và cắt chiều dương các trục $Ox$, $Oy$ lần lượt tại $A$ và $B$ sao cho $OA+OB$ nhỏ nhất.'''
                                 % (latex(x0), latex(y0)))

                # Các đáp án
                da_d = ('\\True ' + str(da_dung))
                list_1 = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                # Xây dựng các chuỗi latex cho lời giải
                expr_oa = "ax + by - %sa - %sb = 0" % (latex(x0), latex(y0))
                tuso = "%sa + %sb" % (latex(x0), latex(y0))

                loigiai = ('''Giả sử đường thẳng $d$ có vectơ pháp tuyến $\\vec{n} = (a;b)$ với $a^2 + b^2 \\neq 0$ nên có phương trình \\\\
                             $d: a(x - %s) + b(y - %s) = 0$ hay $ax + by - %sa - %sb = 0$. \\\\
                             Khi đó $d \\cap Ox = A\\left( \\frac{%s}{a}; 0 \\right)$ và $d \\cap Oy = B\\left( 0; \\frac{%s}{b} \\right)$. \\\\
                             Điều kiện: $\\frac{%s}{a} > 0; \\frac{%s}{b} > 0$. \\\\
                             Ta có: \\\\
                             $OA + OB = \\left| \\frac{%s}{a} \\right| + \\left| \\frac{%s}{b} \\right| = \\frac{%s}{a} + \\frac{%s}{b} = %s + \\frac{%sb}{a} + \\frac{%sa}{b} \\geq %s + 2\\sqrt{\\frac{%sb}{a} \\cdot \\frac{%sa}{b}} = %s$. \\\\
                             Dấu "$=$" xảy ra khi và chỉ khi $\\frac{%sb}{a} = \\frac{%sa}{b} \\Leftrightarrow %sb^2 = %sa^2$. Ta chọn $a = %s$, suy ra $b = %s$. \\\\ Vậy đường thẳng cần tìm có phương trình $d: %s$.'''
                           % (latex(x0), latex(y0), latex(x0), latex(y0), 
                              tuso, tuso, tuso, tuso,
                              tuso, tuso, tuso, tuso, 
                              latex(x0 + y0), latex(y0), latex(x0), latex(x0 + y0), latex(y0), latex(x0), latex(min_val),
                              latex(y0), latex(x0), latex(y0), latex(x0), 
                              latex(val_a), latex(val_b), format_eq(val_a, val_b, c_term)
                             ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + 
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content 


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


def bt_dang65_p1_b2_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến danh sách dạng (hiện tại có 1 dạng)
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B3: Suy nghĩ tìm cách random bài toán
                # Để nghiệm đẹp (x1, x2 là số nguyên), ta chọn x1, x2 trước
                x1 = random.randint(-5, 5)
                x2 = random.randint(-5, 5)
                while x2 == x1:  # Đảm bảo có 2 điểm phân biệt hoặc xử lý nghiệm kép tùy ý
                    x2 = random.randint(-5, 5)

                # Chọn hệ số a cho parabol (thường là 1 hoặc -1 để bài toán phổ thông)
                a_val = random.choice([1, -1])

                # Phương trình hoành độ giao điểm có dạng: a(x - x1)(x - x2) = 0
                # <=> a*x^2 - a(x1 + x2)x + a*x1*x2 = 0
                # Ta giả sử đường thẳng là y = mx + n và parabol là y = ax^2 + bx + c
                # Khi đó ax^2 + (b-m)x + (c-n) = 0

                m_val = random.randint(-3, 3)
                n_val = random.randint(-10, 10)

                # Tính hệ số parabol sao cho ax^2 + bx + c - (mx + n) = a(x - x1)(x - x2)
                # => b = m - a(x1 + x2)
                # => c = n + a*x1*x2
                b_val = m_val - a_val * (x1 + x2)
                c_val = n_val + a_val * x1 * x2

                # Tọa độ y tương ứng
                y1 = m_val * x1 + n_val
                y2 = m_val * x2 + n_val

                # Sắp xếp để hiển thị đáp án đẹp hơn (x nhỏ trước)
                pts = sorted([(x1, y1), (x2, y2)], key=lambda x: x[0])
                p1, p2 = pts[0], pts[1]

                # Đáp án đúng
                kq_dung = f"({p1[0]};{p1[1]}) \\text{{ và }} ({p2[0]};{p2[1]})"

                # B4: Điều chỉnh các phương án sai (không trùng đáp án đúng)
                s = []
                while len(s) < 3:
                    # Tạo nhiễu bằng cách đảo dấu hoặc cộng/trừ 1 đơn vị
                    off_x1 = p1[0] + random.choice([-1, 1, 0])
                    off_y1 = p1[1] + random.choice([-1, 1, 0])
                    off_x2 = p2[0] + random.choice([-1, 1, 0])
                    off_y2 = p2[1] + random.choice([-1, 1, 0])

                    # Đảm bảo không tạo lại đúng cặp tọa độ ban đầu
                    if (off_x1, off_y1) == (p1[0], p1[1]) and (off_x2, off_y2) == (p2[0], p2[1]):
                        continue

                    candidate = f"({off_x1};{off_y1}) \\text{{ và }} ({off_x2};{off_y2})"
                    if candidate not in s and candidate != kq_dung:
                        s.append(candidate)

                # Câu hỏi
                # Định dạng phương trình: y = mx + n và y = ax^2 + bx + c
                line_expr = f"y = {latex(m_val*symbols('x') + n_val)}"
                para_expr = f"y = {latex(a_val*symbols('x')**2 + b_val*symbols('x') + c_val)}"

                noidungcauhoi = f"Giao điểm của các cặp đồ thị của các hàm số ${line_expr}$ và ${para_expr}$ là"

                # Các đáp án
                da_d = '\\True $' + kq_dung + '$'
                da_s1 = '$' + s[0] + '$'
                da_s2 = '$' + s[1] + '$'
                da_s3 = '$' + s[2] + '$'

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (B2: Viết lại y hệt cấu trúc ảnh)
                # Phương trình hoành độ rút gọn: ax^2 + (b-m)x + (c-n) = 0
                b_final = b_val - m_val
                c_final = c_val - n_val
                hoanh_do_eq = latex(a_val*symbols('x')**2 + b_final*symbols('x') + c_final) + " = 0"

                loigiai = (f"Tọa độ giao điểm của ${line_expr}$ và ${para_expr}$ là nghiệm của hệ sau \\\\"
                           f"$\\begin{{cases}} {line_expr} \\\\ {para_expr} \\end{{cases}} "
                           f"\\Leftrightarrow \\begin{{cases}} {line_expr} \\\\ {hoanh_do_eq} \\end{{cases}} "
                           f"\\Leftrightarrow \\begin{{cases}} x = {p1[0]} \\\\ y = {p1[1]} \\end{{cases}} \\text{{ hoặc }} "
                           f"\\begin{{cases}} x = {p2[0]} \\\\ y = {p2[1]} \\end{{cases}}$. \\\\"
                           f"Vậy hai giao điểm có tọa độ là $({p1[0]};{p1[1]})$ và $({p2[0]};{p2[1]})$.")

            # Xuất câu trắc nghiệm theo đúng cấu trúc mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choice \n'
                '{' + str(list_1[0]) + '}\n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


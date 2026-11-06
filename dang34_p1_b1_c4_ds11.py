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


def bt_dang34_p1_b1_c4_ds11(self):
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # --- Cấu hình Random bài toán ---
                n = symbols('n')


                a = randint(2, 9)          # Hệ số tự do biểu thức 1
                b_val = randint(2, 5)      # Giá trị tuyệt đối hệ số n biểu thức 1
                b = -b_val                 # Để giống mẫu (2-3n), ta cho hệ số n âm
                p = randint(2, 4)          # Số mũ biểu thức 1 (2 đến 4)

                d = randint(2, 5)          # Hệ số n biểu thức 2 (thường là 1 hoặc số nhỏ)
                c = randint(2, 5)          # Hệ số tự do biểu thức 2
                q = randint(2, 4)          # Số mũ biểu thức 2

                # Tổng số mũ n
                total_power = p + q

                # Tính giới hạn phần hệ số
                # lim (a/n + b)^p = b^p
                lim_part1 = b**p
                # lim (d + c/n)^q = d^q
                lim_part2 = d**q

                # Tích các giới hạn hệ số
                coeff_limit = lim_part1 * lim_part2

                if coeff_limit > 0:
                    ket_qua = "+\\infty"
                    wrong_sign = "-\\infty"
                else:
                    ket_qua = "-\\infty"
                    wrong_sign = "+\\infty"

                # Tạo các đáp án nhiễu
                # Nhiễu 1: Sai dấu vô cực
                da_dung = ket_qua

                # Nhiễu 2: Chỉ lấy hệ số (người học quên nhân với vô cực)
                distractor_num = coeff_limit

                # Nhiễu 3: Một số ngẫu nhiên hoặc 0
                distractor_zero = 0
                if distractor_num == 0: distractor_zero = 1 # Tránh trùng

                du = ['$%s$' % da_dung] # Đáp án đúng dạng list để random.choice nếu cần
                da = random.choice(du)

                # Danh sách đáp án sai
                s = [
                    '$%s$' % wrong_sign,
                    '$%s$' % distractor_num,
                    '$%s$' % (distractor_num * -1), # Sai dấu phần số
                    '$0$',
                    '$1$'
                ]

                # Chọn ngẫu nhiên 3 đáp án sai không trùng nhau
                # Lọc trùng với đáp án đúng trước
                s = [x for x in s if x != da]
                s = list(set(s)) # Khử trùng trong chính s
                if len(s) < 3: s.append('$10$') # Fallback nếu thiếu

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # --- Nội dung câu hỏi ---
                # Tạo biểu thức hiển thị bằng Latex
                # (a + bn)^p
                term1_str = f"({a} {b}n)^{{{p}}}" if b < 0 else f"({a} + {b}n)^{{{p}}}"
                # (dn + c)^q
                term2_str = f"({d}n + {c})^{{{q}}}"

                expr_display = term1_str + term2_str

                noidungcauhoi = ('''$\\lim_{n \\to +\\infty} %s$ bằng''' % expr_display)

                # --- Các đáp án ---
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # --- Nội dung lời giải ---
                # Chuẩn bị latex cho lời giải
                term1_factor = f"\\left(\\frac{{{a}}}{{n}} {b}\\right)^{{{p}}}" if b < 0 else f"\\left(\\frac{{{a}}}{{n}} + {b}\\right)^{{{p}}}"
                term2_factor = f"\\left({d} + \\frac{{{c}}}{{n}}\\right)^{{{q}}}"

                loigiai = ('''Ta có: \\\\
                $\\begin{aligned}
                \\lim_{n \\to +\\infty} %s &= \\lim_{n \\to +\\infty} \\left[ n^{%s} %s n^{%s} %s \\right] \\\\
                &= \\lim_{n \\to +\\infty} \\left[ n^{%s} %s %s \\right]
                \\end{aligned}$
                \\\\
                $\\lim_{n \\to +\\infty} n^{%s} = +\\infty$
                \\\\
                $\\lim_{n \\to +\\infty} %s = (%s)^{%s} = %s$
                \\\\
                $\\lim_{n \\to +\\infty} %s = %s^{%s} = %s$
                \\\\
                Do đó: $\\lim_{n \\to +\\infty} %s = %s$ ''' 
                % (
                    expr_display, 
                    p, term1_factor, q, term2_factor, 
                    total_power, term1_factor, term2_factor,
                    total_power,
                    term1_factor, b, p, lim_part1,
                    term2_factor, d, q, lim_part2,
                    expr_display, ket_qua
                ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + 
                '\\choice \n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '{' + str(list_1[0]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


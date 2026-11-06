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


def bt_dang36_p4_b1_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random hằng số cho bài toán: f(x) = (1/k)*x^2 khi x <= x0 và ax + b khi x > x0
                # Trong ảnh gốc: k=2, x0=1
                x0 = randint(1, 3)
                k = randint(2, 4)
                c = Rational(1, k)

                # Điều kiện để có đạo hàm:
                # 1. Liên tục: a*x0 + b = c*x0^2
                # 2. Đạo hàm trái = Đạo hàm phải: a = 2*c*x0

                val_a = 2 * c * x0
                val_b = c * (x0**2) - val_a * x0

                # Hàm hỗ trợ định dạng số thập phân dùng dấu phẩy
                def format_math(val):
                    if isinstance(val, Rational) and val.denominator != 1:
                        # Nếu là phân số đẹp thì để latex phân số, nếu không thì chuyển thập phân
                        f_val = float(val)
                        if f_val.is_integer():
                            return str(int(f_val))
                        res = str(f_val).replace('.', ',')
                        return res
                    return str(val).replace('.', ',')

                def to_latex_val(val):
                    return latex(val).replace('.', ',')

                # Đáp án đúng
                da_dung = '$a = %s; b = %s$' % (to_latex_val(val_a), format_math(val_b))

                # Tạo các phương án sai (không trùng đáp án đúng)
                s = []
                offsets = [(1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (2, -1)]
                for off_a, off_b in offsets:
                    wa = val_a + off_a
                    wb = val_b + off_b
                    choice = '$a = %s; b = %s$' % (to_latex_val(wa), format_math(wb))
                    if choice != da_dung:
                        s.append(choice)

                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Nội dung câu hỏi
                # f(x) = 1/k * x^2 => (x^2)/k
                bieuthuc_tren = latex(Rational(1, k) * x**2)
                noidungcauhoi = ('''Cho hàm số $f\\left(x\\right) = \\begin{cases} %s & \\text{ khi } x \\le %s \\\\ ax + b & \\text{ khi } x > %s \\end{cases}$. Tìm $a, b$ thì hàm số có đạo hàm tại $x = %s$.'''
                                 % (bieuthuc_tren, latex(x0), latex(x0), latex(x0)))

                # Nội dung lời giải chi tiết theo mẫu ảnh
                f_x0 = to_latex_val(c * x0**2)
                lim_trai = f_x0

                loigiai = ('''Ta có $\\lim_{x \\to %s^+} \\left(ax + b\\right) = a \\cdot %s + b$; $\\lim_{x \\to %s^-} \\left(%s\\right) = %s$; $f\\left(%s\\right) = %s$. \\\\
            Hàm số liên tục tại $x = %s$ nên $a \\cdot %s + b = %s$. \\\\
            Đạo hàm phải \\\\ $f'\\left(%s^+\\right) = \\lim_{x \\to %s^+} \\frac{f\\left(x\\right) - f\\left(%s\\right)}{x - %s} = \\lim_{x \\to %s^+} \\frac{ax + b - \\left(a \\cdot %s + b\\right)}{x - %s} = \\lim_{x \\to %s^+} \\frac{a\\left(x - %s\\right)}{x - %s} = \\lim_{x \\to %s^+} a = a$. \\\\
            Đạo hàm trái \\\\ $f'\\left(%s^-\\right) = \\lim_{x \\to %s^-} \\frac{f\\left(x\\right) - f\\left(%s\\right)}{x - %s} = \\lim_{x \\to %s^-} \\frac{%s - %s}{x - %s} = \\lim_{x \\to %s^-} \\frac{%s \\left(x^2 - %s\\right)}{x - %s} = \\lim_{x \\to %s^-} \\frac{%s \\left(x - %s\\right)\\left(x + %s\\right)}{x - %s} = \\lim_{x \\to %s^-} \\frac{%s \\left(x + %s\\right)}{1} = %s$. \\\\
            Hàm số có đạo hàm tại $x = %s \\Leftrightarrow f'\\left(%s^+\\right) = f'\\left(%s^-\\right) \\Leftrightarrow a = %s$. \\\\
            Thay $a = %s$ vào phương trình liên tục: $%s \\cdot %s + b = %s \\Leftrightarrow b = %s$. \\\\
            Vậy $a = %s; b = %s$.''' 
                           % (latex(x0), latex(x0), latex(x0), bieuthuc_tren, f_x0, latex(x0), f_x0,
                              latex(x0), latex(x0), f_x0,
                              latex(x0), latex(x0), latex(x0), latex(x0), latex(x0), latex(x0), latex(x0), latex(x0), latex(x0), latex(x0), latex(x0),
                              latex(x0), latex(x0), latex(x0), latex(x0), latex(x0), bieuthuc_tren, f_x0, latex(x0), latex(x0), to_latex_val(c), latex(x0**2), latex(x0), latex(x0), to_latex_val(c), latex(x0), latex(x0), latex(x0), latex(x0), to_latex_val(c), latex(x0), to_latex_val(val_a),
                              latex(x0), latex(x0), latex(x0), to_latex_val(val_a),
                              to_latex_val(val_a), to_latex_val(val_a), latex(x0), f_x0, format_math(val_b),
                              to_latex_val(val_a), format_math(val_b)))

                # Các đáp án
                da_d = ('\\True ' + str(da_dung))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


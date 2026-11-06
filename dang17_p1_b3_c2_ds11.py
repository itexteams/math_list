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


def bt_dang17_p1_b3_c2_ds11(self):
    # Khai báo biến
    x = symbols('x')
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Random các hằng số để tạo phương trình (x - a), (x + b), (c - x)
        a = random.randint(1, 4)
        b = random.randint(1, 4)
        c = random.randint(1, 5)

        # Chuỗi hiển thị đề bài
        A_str = "x - %s" % a
        B_str = "x + %s" % b
        C_str = "%s - x" % c

        # Khai báo biểu thức toán học
        A_expr = x - a
        B_expr = x + b
        C_expr = c - x

        # Tính toán các đa thức
        eq_lhs = expand(B_expr**2)
        eq_rhs = expand(A_expr * C_expr)
        eq_full = expand(eq_lhs - eq_rhs)

        # Giải phương trình bằng sympy chính xác
        sols = sp.solve(eq_full, x)
        real_sols = [s for s in sols if s.is_real]

        ans_true_str = ""
        # Trường hợp phương trình vô nghiệm
        if len(real_sols) == 0:
            ans_true_str = "Không có giá trị nào của $x$"
            # Tạo danh sách đáp án nhiễu
            fakes_pool = ["$x = \\pm %s$" % random.randint(1, 3), 
                          "$x = %s$" % random.randint(1, 4), 
                          "$x = -%s$" % random.randint(1, 4), 
                          "$x = %s$" % random.randint(5, 7)]
            fakes_pool = list(set(fakes_pool))
            while len(fakes_pool) < 3:
                fakes_pool.append("$x = %s$" % random.randint(8, 15))
            fakes = random.sample(fakes_pool, 3)
            ketluan = "Phương trình vô nghiệm. Vậy không có giá trị nào của $x$ thỏa mãn."
        # Trường hợp phương trình có nghiệm thực
        else:
            if len(real_sols) == 1:
                ans_true_str = "$x = %s$" % str(latex(real_sols[0])).replace('.', ',')
            else:
                if real_sols[0] == -real_sols[1]:
                    ans_true_str = "$x = \\pm %s$" % str(latex(abs(real_sols[0]))).replace('.', ',')
                else:
                    rs = sorted(real_sols, key=lambda val: float(val))
                    ans_true_str = "$x = %s$ hoặc $x = %s$" % (str(latex(rs[0])).replace('.', ','), str(latex(rs[1])).replace('.', ','))

            fakes = ["Không có giá trị nào của $x$"]
            fakes_pool = []
            for val in [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]:
                is_root = False
                for r in real_sols:
                    if abs(float(val) - float(r)) < 1e-6:
                        is_root = True
                        break
                if not is_root:
                    fakes_pool.append("$x = %s$" % val)

            fakes.extend(random.sample(fakes_pool, 2))
            ketluan = "Giải phương trình ta được %s." % (ans_true_str)

        # Các đáp án trắc nghiệm
        da_d = ('\\True ' + ans_true_str)
        da_s1 = fakes[0]
        da_s2 = fakes[1]
        da_s3 = fakes[2]

        # Câu hỏi
        noidungcauhoi = ('Giá trị của $x$ để 3 số $%s$; $%s$; $%s$ theo thứ tự lập thành một cấp số nhân là'
                         % (A_str, B_str, C_str))

        # Đưa các đáp án vào danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải
        loigiai = ('''Để 3 số $%s$; $%s$; $%s$ theo thứ tự lập thành một cấp số nhân thì:\\\\
                      $ (%s)^2 = (%s)(%s) $ \\\\
                      $ \\Leftrightarrow %s = %s $ \\\\
                      $ \\Leftrightarrow %s = 0 $. \\\\
                      %s''' % (
                      A_str, B_str, C_str,
                      B_str, A_str, C_str,
                      latex(eq_lhs), latex(eq_rhs),
                      latex(eq_full),
                      ketluan
                      ))

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + 
               '\n\\choice \n'
               '{' + str(list_1[1]) + '}\n'
               '{' + str(list_1[2]) + '}\n'
               '{' + str(list_1[3]) + '}\n'
               '{' + str(list_1[0]) + '}\n'
               '\\loigiai{\n' + str(loigiai) + '\n}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content


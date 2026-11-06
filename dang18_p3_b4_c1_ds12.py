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


def bt_dang18_p3_b4_c1_ds12(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        a_sym, b_sym = symbols('a b')

        # Random điểm cực tiểu x0 và tung độ giao điểm Oy (c_val)
        x0 = random.choice([1, 2])
        c_val = random.randint(-5, 5)

        # Chọn a sao cho f''(x0) = 6*x0 + 2*a > 0 (đảm bảo là điểm cực tiểu)
        if x0 == 1:
            a_val = random.randint(-2, 5)
        else:
            a_val = random.randint(-5, 3)

        while a_val == 0 or (6 * x0 + 2 * a_val <= 0):
            a_val = random.randint(-5, 5)

        # Tính b và y0 = f(x0)
        b_val = -3 * (x0**2) - 2 * a_val * x0
        y0 = x0**3 + a_val * (x0**2) + b_val * x0 + c_val

        # Giá trị T cần tính
        val_T = 3 * a_val + b_val - c_val

        # Biểu thức biến đổi từng bước trong lời giải
        eq1_step1 = 3 * (x0**2) + 2 * x0 * a_sym + b_sym
        eq1_step2_lhs = 2 * x0 * a_sym + b_sym
        eq1_step2_rhs = -3 * (x0**2)

        eq2_step1_lhs = (x0**3) + (x0**2) * a_sym + x0 * b_sym + c_val
        eq2_step2_lhs = (x0**2) * a_sym + x0 * b_sym
        eq2_step2_rhs = y0 - c_val - (x0**3)

        f_dp_expr = 6 * x + 2 * a_val
        f_dp_at_x0 = 6 * x0 + 2 * a_val

        # Đáp án đúng
        du = ['$T = %s$' % (latex(val_T))]
        da = random.choice(du)

        # Tạo danh sách phương án sai không trùng với đáp án đúng
        s_candidates = []
        for k in [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, -6, 7, -7]:
            cand = val_T + k
            if cand != val_T and cand not in s_candidates:
                s_candidates.append(cand)

        random.shuffle(s_candidates)

        das1 = '$T = %s$' % (latex(s_candidates[0]))
        das2 = '$T = %s$' % (latex(s_candidates[1]))
        das3 = '$T = %s$' % (latex(s_candidates[2]))

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho hàm số $f(x) = x^3 + ax^2 + bx + c$ đạt cực tiểu tại điểm $x = %s$, $f(%s) = %s$ và đồ thị hàm số cắt trục tung tại điểm có tung độ bằng $%s$. Giá trị $T = 3a + b - c$ bằng'''
                         % (latex(x0), latex(x0), latex(y0), latex(c_val)))

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải
        loigiai = ('''Đồ thị hàm số cắt trục tung tại điểm có tung độ bằng $%s$ nên $c = %s$.\\\\
    Tập xác định: $\\mathbb{D} = \\mathbb{R}$.\\\\
    Ta có $f'(x) = 3x^2 + 2ax + b$.\\\\
    Hàm số đạt cực tiểu tại điểm $x = %s$ nên $f'(%s) = 0$, suy ra\\\\
    $%s = 0 \\Leftrightarrow %s = %s$.\\\\
    Mặt khác, theo giả thiết $f(%s) = %s$, ta có\\\\
    $%s = %s \\Leftrightarrow %s = %s$.\\\\
    Từ đó ta có hệ phương trình\\\\
    $\\begin{cases} %s = %s \\\\ %s = %s \\end{cases} \\Leftrightarrow \\begin{cases} a = %s \\\\ b = %s \\end{cases}$\\\\
    Thử lại, với $a = %s$ ta có $f''(x) = %s$.\\\\
    Vì $f''(%s) = %s > 0$ nên $x = %s$ đúng là điểm cực tiểu của hàm số.\\\\
    Vậy $T = 3a + b - c = 3 \\cdot (%s) + (%s) - (%s) = %s$.'''
                   % (latex(c_val), latex(c_val),
                      latex(x0), latex(x0),
                      latex(eq1_step1), latex(eq1_step2_lhs), latex(eq1_step2_rhs),
                      latex(x0), latex(y0),
                      latex(eq2_step1_lhs), latex(y0), latex(eq2_step2_lhs), latex(eq2_step2_rhs),
                      latex(eq1_step2_lhs), latex(eq1_step2_rhs),
                      latex(eq2_step2_lhs), latex(eq2_step2_rhs),
                      latex(a_val), latex(b_val),
                      latex(a_val), latex(f_dp_expr),
                      latex(x0), latex(f_dp_at_x0), latex(x0),
                      latex(a_val), latex(b_val), latex(c_val), latex(val_T)
                     ))
    dapan='\\shortans[0]{$%s$}\n'%(latex(val_T))
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
        '\\loigiai{' + str(loigiai) + '}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content


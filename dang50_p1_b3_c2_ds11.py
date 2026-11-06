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


def bt_dang50_p1_b3_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Khởi tạo các số liệu hợp lý để phương trình có nghiệm đẹp (q > 0)
                # Phương trình: (q^2 + q + 1) / (q + 1) = S3 / S2
                # Chọn q > 0 (nghiệm dương). Ta thiết kế từ q dương trước.
                q_val = random.choice([2, 3, Rational(3, 2)])

                # Tính tỉ số t = S3/S2 = (q^2 + q + 1) / (q + 1)
                # S3 = u1(q^2 + q + 1), S2 = u1(q + 1)

                # Chọn u1 sao cho u1(q+1) nguyên hoặc là phân số đơn giản
                if q_val == 2:
                    u1 = random.choice([1, 2, 3])
                    S2_val = u1 * (2 + 1)
                    S3_val = u1 * (2**2 + 2 + 1)

                    q_other = -Rational(3, 2) # Nghiệm còn lại của pt
                elif q_val == 3:
                    u1 = random.choice([1, 2])
                    S2_val = u1 * (3 + 1)
                    S3_val = u1 * (3**2 + 3 + 1)

                    q_other = -Rational(4, 3)
                else: # q = 3/2
                    u1 = random.choice([16, 32])
                    S2_val = u1 * (Rational(3, 2) + 1)
                    S3_val = u1 * (Rational(9, 4) + Rational(3, 2) + 1)
                    q_other = -Rational(1, 2)

                # Tính S5 đúng
                S5_val = u1 * (q_val**4 + q_val**3 + q_val**2 + q_val + 1)

                # Tính phương án nhiễu
                # Sai lầm 1: Dùng nghiệm âm q_other
                S5_fake1 = u1 * (q_other**4 + q_other**3 + q_other**2 + q_other + 1)

                # Sai lầm 2: Tính S4 thay vì S5
                S5_fake2 = u1 * (q_val**3 + q_val**2 + q_val + 1)

                # Sai lầm 3: Tính sai ngẫu nhiên
                S5_fake3 = S5_val + random.randint(1, 10)

                # Định dạng chuỗi LaTeX (Đã sửa lỗi kiểu dữ liệu)
                def fmt(val):
                    val_sp = sympify(val)
                    if val_sp.is_integer:
                        return str(val_sp)
                    return latex(val_sp)

                kq_str = 'S_5 = %s' % fmt(S5_val)
                ds1_str = 'S_5 = %s' % fmt(S5_fake1)
                ds2_str = 'S_5 = %s' % fmt(S5_fake2)
                ds3_str = 'S_5 = %s' % fmt(S5_fake3)

                # Các đáp án trắc nghiệm
                du = ['$%s$' % kq_str]
                da = random.choice(du)
                s = [
                    '$%s$' % ds1_str,
                    '$%s$' % ds2_str,
                    '$%s$' % ds3_str,
                ]

                # Câu hỏi
                noidungcauhoi = ('''Cho cấp số nhân $(u_n)$ có tổng của hai số hạng đầu tiên bằng $%s$, tổng của ba số hạng đầu tiên bằng $%s$. Biết công bội của cấp số nhân là một số dương. Tổng của năm số hạng đầu tiên của cấp số nhân đã cho là'''
                                 % (fmt(S2_val), fmt(S3_val)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(s[0])
                da_s2 = str(s[1]) 
                da_s3 = str(s[2]) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Xử lý phương trình bậc 2 cho q
                u3_val = S3_val - S2_val
                a_eq = S2_val
                b_eq = -(S3_val - S2_val)
                c_eq = -(S3_val - S2_val)

                eq_str = ''
                if a_eq == 1: eq_str += 'q^2'
                elif a_eq == -1: eq_str += '-q^2'
                else: eq_str += '%sq^2' % a_eq

                if b_eq == 1: eq_str += ' + q'
                elif b_eq == -1: eq_str += ' - q'
                elif b_eq > 0: eq_str += ' + %sq' % b_eq
                elif b_eq < 0: eq_str += ' - %sq' % abs(b_eq)

                if c_eq > 0: eq_str += ' + %s' % c_eq
                elif c_eq < 0: eq_str += ' - %s' % abs(c_eq)
                eq_str += ' = 0'

                # Nội dung lời giải
                loigiai = ('''Gọi $u_1$ và $q$ lần lượt là số hạng đầu và công bội của cấp số nhân $(u_n)$.\\\\
                            Theo giả thiết, ta có hệ phương trình:
                            $\\begin{cases} u_1 + u_2 = %s \\\\ u_1 + u_2 + u_3 = %s \\end{cases} 
                            \\Leftrightarrow \\begin{cases} u_1(1 + q) = %s \\\\ u_1(1 + q + q^2) = %s \\end{cases}$ \\\\
                            Suy ra: $\\frac{1 + q + q^2}{1 + q} = \\frac{%s}{%s}$ (với $q \\neq -1$).\\\\
                            $\\Leftrightarrow %s(1 + q + q^2) = %s(1 + q) \\Leftrightarrow %s \\Leftrightarrow \\left[ \\begin{array}{l} q = %s \\\\ q = %s \\end{array} \\right.$.\\\\
                            Vì công bội $q > 0$ nên chọn $q = %s$. Khi đó $u_1 = \\frac{%s}{1 + %s} = %s$.\\\\
                            Tổng của năm số hạng đầu tiên của cấp số nhân là: $S_5 = u_1 \\cdot \\frac{1 - q^5}{1 - q} = %s \\cdot \\frac{1 - \\left(%s\\right)^5}{1 - %s} = %s$.'''
                         % (fmt(S2_val), fmt(S3_val), 
                            fmt(S2_val), fmt(S3_val), 
                            fmt(S3_val), fmt(S2_val),
                            fmt(S2_val), fmt(S3_val), eq_str, fmt(q_val), fmt(q_other),
                            fmt(q_val), fmt(S2_val), fmt(q_val), fmt(u1),
                            fmt(u1), fmt(q_val), fmt(q_val), fmt(S5_val)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


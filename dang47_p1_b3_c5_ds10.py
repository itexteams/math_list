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


def bt_dang47_p1_b3_c5_ds10(self):
            # Khai báo biết
            # Khai báo biến và tạo bài toán ngẫu nhiên
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Khởi tạo các thông số ngẫu nhiên cho khai triển (ax^2 + bx + c)^n
                a = 1
                n = random.randint(5, 7)  # Số mũ của khai triển
                b = random.choice([-4, -3, -2, 2, 3, 4])  # Hệ số của x
                c = random.choice([-3, -2, 1, 2, 3, 4])   # Hệ số tự do

                # Chọn số mũ m của x^m cần tìm hệ số 
                m = random.randint(n, 2*n - 2)

                # Tổng quát: 2(n-k) + i = m <=> 2n - 2k + i = m <=> 2k - i = 2n - m
                target_val = 2*n - m

                results_list = []
                tong_he_so = 0

                # Tìm các tổ hợp k, i thỏa mãn điều kiện
                for k in range(n + 1):
                    i = 2*k - target_val
                    if 0 <= i <= k:
                        # Sử dụng binomial(n, k) thay vì combinations
                        coeff = binomial(n, k) * (a**(n-k)) * binomial(k, i) * (c**(k-i)) * (b**i)
                        results_list.append((k, i, coeff))
                        tong_he_so += coeff

                # Đáp án đúng
                kq = int(tong_he_so)

                # Tạo các phương án nhiễu
                s = set()
                while len(s) < 3:
                    sai = kq + random.choice([-100, 100, -50, 50, -20, 20, -1000, 1000])
                    if sai != kq:
                        s.add('$%s$' % latex(sai))

                list_sai = list(s)

                # Chuẩn bị chuỗi LaTeX cho đa thức
                b_str = ('+ %s' % b) if b > 0 else ('- %s' % abs(b))
                c_str = ('+ %s' % c) if c > 0 else ('- %s' % abs(c))

                # Câu hỏi
                noidungcauhoi = ('''Hệ số của số hạng chứa $x^{%s}$ trong khai triển $\\left(x^2 %s x %s \\right)^{%s}$ bằng'''
                                 % (latex(m), b_str, c_str, latex(n)))

                # Các đáp án
                da_d = ('\\True $%s$' % latex(kq))
                da_s1 = list_sai[0]
                da_s2 = list_sai[1]
                da_s3 = list_sai[2]

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Xây dựng nội dung lời giải chi tiết
                buoc_giai_chi_tiet = ""
                for k_val, i_val, c_val in results_list:
                    buoc_giai_chi_tiet += ('''$k = %s \\Rightarrow i = %s \\Rightarrow$ hệ số là $C_{%s}^{%s} C_{%s}^{%s} \\cdot \\left(%s\\right)^{%s} \\cdot \\left(%s\\right)^{%s} = %s$ \\\\''' 
                                           % (latex(k_val), latex(i_val), latex(n), latex(k_val), latex(k_val), latex(i_val), 
                                              latex(c), latex(k_val-i_val), latex(b), latex(i_val), latex(int(c_val))))

                loigiai = ('''Ta có $\\left(x^2 %s x %s \\right)^{%s} = \\left(x^2 + \\left(%s x %s \\right) \\right)^{%s}$ \\\\
                             Số hạng tổng quát trong khai triển trên là $C_{%s}^k \\cdot \\left(x^2\\right)^{%s-k} \\cdot \\left(%s x %s \\right)^k$ với $k = 0; 1; 2; \\dots; %s$. \\\\
                             Số hạng tổng quát trong khai triển $\\left(%s x %s \\right)^k$ là $C_k^i \\cdot %s^{k-i} \\cdot \\left(%s x\\right)^i$ với $0 \\le i \\le k$. \\\\
                             Số hạng tổng quát trong khai triển $\\left(x^2 %s x %s \\right)^{%s}$ là $C_{%s}^k \\cdot \\left(x^2\\right)^{%s-k} \\cdot C_k^i \\cdot %s^{k-i} \\cdot \\left(%s x\\right)^i$ \\\\
                             $= C_{%s}^k C_k^i \\cdot %s^{k-i} \\cdot \\left(%s\\right)^i \\cdot \\left(x^{%s-2k+i}\\right)$ \\\\
                             Số hạng chứa $x^{%s}$ ứng với $%s-2k+i = %s \\Leftrightarrow 2k-i = %s$. Kết hợp với điều kiện ta được các nghiệm: \\\\
                             %s
                             Vậy hệ số của số hạng chứa $x^{%s}$ trong khai triển $\\left(x^2 %s x %s \\right)^{%s}$ bằng $%s$.'''
                           % (b_str, c_str, latex(n), b, c, latex(n),
                              latex(n), latex(n), b, c, latex(n),
                              b, c, latex(c), latex(b),
                              b_str, c_str, latex(n), latex(n), latex(n), latex(c), latex(b),
                              latex(n), latex(c), latex(b), latex(2*n),
                              latex(m), latex(2*n), latex(m), latex(target_val),
                              buoc_giai_chi_tiet,
                              latex(m), b_str, c_str, latex(n), latex(kq)
                              ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) +
                       '\n\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content


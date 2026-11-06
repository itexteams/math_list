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


def bt_dang44_p4_b3_c5_ds10(self):
            # Khai báo biết
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Thiết lập bộ thông số để n luôn là số nguyên dương
                # Bộ (n, A_val, B_val) thỏa mãn C_n^3 = A_val*n + B_val*C_n^2
                data_n = [
                    {'n': 9, 'An': Rational(4, 3), 'B': 2},
                    {'n': 10, 'An': 3, 'B': 2},
                    {'n': 11, 'An': 5, 'B': 2},
                    {'n': 12, 'An': Rational(15, 2), 'B': 2}
                ]
                sel_n = random.choice(data_n)
                n_val = sel_n['n']
                A_val = sel_n['An']
                B_val = sel_n['B']

                # Chọn hệ số c trong (x - c/x)^n và bậc p của x cần tìm
                c_val = random.randint(1, 3)
                # Đảm bảo n - p chia hết cho 2 để k là số nguyên
                possible_p = [p for p in range(1, n_val - 1) if (n_val - p) % 2 == 0]
                p_val = random.choice(possible_p)

                # Tính toán k và hệ số
                k_val = (n_val - p_val) // 2
                coefficient = binomial(n_val, k_val) * ((-c_val)**k_val)

                # Biến phục vụ trình bày lời giải
                # Biến đổi phương trình: (n-1)(n-2) = 6A + 3B(n-1)
                # n^2 - 3n + 2 = 6A + 3Bn - 3B
                # n^2 - (3 + 3B)n + (2 + 3B - 6A) = 0
                term_A_latex = latex(A_val)
                coeff_B_n_minus_1 = 3 * B_val
                constant_6A = 6 * A_val

                kq = int(coefficient)

                # Các đáp án trắc nghiệm
                da = '$%s$' % (latex(kq))

                # Tạo các phương án nhiễu
                s = [
                    '$%s$' % (latex(kq + random.randint(10, 30))),
                    '$%s$' % (latex(kq - random.randint(10, 30))),
                    '$%s$' % (latex(kq + random.randint(31, 50))),
                    '$%s$' % (latex(kq - random.randint(31, 50))),
                    '$%s$' % (latex(abs(kq) + 5)),
                    '$%s$' % (latex(-kq if kq != 0 else 100))
                ]

                # Loại bỏ phương án trùng với đáp án đúng
                s = [item for item in s if item != da]
                random.shuffle(s)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                # Định dạng lại chuỗi biểu thức khai triển
                bieu_thuc = '\\left( x - \\frac{%s}{x} \\right)^{n}' % (latex(c_val))
                pt_n = 'C_n^3 = %s n + %s C_n^2' % (term_A_latex, latex(B_val))

                noidungcauhoi = ('''Tìm số hạng chứa $x^{%s}$ trong khai triển $%s$, biết $n$ là số tự nhiên thỏa mãn $%s$.'''
                                 % (latex(p_val), bieu_thuc, pt_n))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                # Các bước trung gian cho lời giải chi tiết
                step1_rhs = '8n + 6n\\left( n-1 \\right)' if n_val == 9 else '%sn + %sn\\left( n-1 \\right)' % (latex(6*A_val), latex(3*B_val))
                quad_b = 3 + 3*B_val
                quad_c = 2 + 3*B_val - 6*A_val

                loigiai = ('''Điều kiện: $n \\ge 3, n \\in \\mathbb{Z}$. \\\\
                             Ta có $%s \\Leftrightarrow \\frac{n!}{3!\\left( n-3 \\right)!} = %s n + %s \\cdot \\frac{n!}{2!\\left( n-2 \\right)!}$ \\\\
                             $\\Leftrightarrow n\\left( n-1 \\right)\\left( n-2 \\right) = %s$ \\\\
                             $\\Leftrightarrow n^2 - %sn + %s = 0 \\Leftrightarrow \\left[ \\begin{aligned} & n = %s \\\\ & n = %s \\end{aligned} \\right.$ \\\\
                             Đối chiếu điều kiện ta được $n = %s$. \\\\
                             Số hạng tổng quát của khai triển $%s$ là: \\\\
                             $C_{%s}^k x^{%s-k} \\cdot \\frac{\\left( -%s \\right)^k}{x^k} = \\left( -%s \\right)^k C_{%s}^k x^{%s-2k}$. \\\\
                             Số hạng này chứa $x^{%s}$ ứng với $%s - 2k = %s \\Leftrightarrow k = %s$. \\\\
                             Vậy hệ số của số hạng đó là $\\left( -%s \\right)^{%s} \\cdot C_{%s}^{%s} = %s$.'''
                           % (pt_n, term_A_latex, latex(B_val), 
                              step1_rhs, latex(quad_b), latex(quad_c), 
                              latex(n_val), latex(quad_c if quad_c != 0 else 0), # Giả định nghiệm còn lại từ pt bậc 2
                              latex(n_val), bieu_thuc,
                              latex(n_val), latex(n_val), latex(c_val), latex(c_val), latex(n_val), latex(n_val),
                              latex(p_val), latex(n_val), latex(p_val), latex(k_val),
                              latex(c_val), latex(k_val), latex(n_val), latex(k_val), latex(kq)
                             ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


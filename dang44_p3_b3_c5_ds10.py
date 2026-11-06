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


def bt_dang44_p3_b3_c5_ds10(self):
            while True:
                # Bước 1: Chọn bộ thông số n, A, B thỏa mãn C_n^3 = A*n + B*C_n^2
                # n=7: 35 = A*7 + B*21 -> B=1, A=2
                # n=9: 84 = A*9 + B*36 -> B=2, A=4/3
                # n=10: 120 = A*10 + B*45 -> B=2, A=3
                # n=11: 165 = A*11 + B*55 -> B=2, A=5
                data_n = [
                    {'n': 7, 'An': 2, 'B': 1},
                    {'n': 9, 'An': Rational(4, 3), 'B': 2},
                    {'n': 10, 'An': 3, 'B': 2},
                    {'n': 11, 'An': 5, 'B': 2}
                ]
                sel_n = random.choice(data_n)
                n_val = sel_n['n']
                A_val = sel_n['An']
                B_val = sel_n['B']

                # Chọn hệ số c trong (x - c/x)^n
                c_val = random.randint(1, 2)

                # Chọn bậc p sao cho k = (n-p)/2 là số nguyên
                possible_p = [p for p in range(0, n_val) if (n_val - p) % 2 == 0]
                p_val = random.choice(possible_p)

                k_val = (n_val - p_val) // 2
                coefficient = math.comb(n_val, k_val) * ((-c_val)**k_val)

                # Kiểm tra điều kiện kết quả trong khoảng (-999, 9999)
                if -999 < coefficient < 9999:
                    kq = int(coefficient)
                    break

            # Định dạng các thành phần câu hỏi
            bieu_thuc = r"\left( x - \dfrac{%s}{x} \right)^{n}" % (latex(c_val))
            pt_n = r"C_n^3 = %s n + %s C_n^2" % (latex(A_val), latex(B_val))

            # Câu hỏi
            noidungcauhoi = (r"Hệ số của số hạng chứa $x^{%s}$ trong khai triển biểu thức $%s$, biết $n$ là số tự nhiên thỏa mãn $%s$ bằng bao nhiêu?"
                             % (latex(p_val), bieu_thuc, pt_n))

            # Đáp án đúng (Số nguyên)
            da_dung = r"\True $%d$" % kq

            # Tạo các phương án nhiễu
            s_set = set()
            while len(s_set) < 3:
                offset = random.choice([1, -1, 10, -10, 2, 5])
                nhieu = kq + offset
                if nhieu != kq:
                    s_set.add(r"$%d$" % nhieu)

            list_ans = [da_dung] + list(s_set)
            random.shuffle(list_ans)

            # Lời giải chi tiết
            step1_rhs = r"%sn + %sn(n-1)" % (latex(6*A_val), latex(3*B_val))
            quad_b = 3 + 3*B_val
            quad_c = 2 + 3*B_val - 6*A_val

            loigiai = (r'''Điều kiện: $n \ge 3, n \in \mathbb{Z}$. \\
                         Ta có: $%s \Leftrightarrow \dfrac{n(n-1)(n-2)}{6} = %s n + %s \cdot \dfrac{n(n-1)}{2}$ \\
                         $\Leftrightarrow n(n-1)(n-2) = %s$ \\
                         $\Leftrightarrow n^2 - %sn + %s = 0 \Leftrightarrow n = %s$ (thỏa mãn). \\
                         Số hạng tổng quát trong khai triển $%s$ là: \\
                         $T_{k+1} = C_{%s}^k x^{%s-k} \cdot \left( -\dfrac{%s}{x} \right)^k = (-%s)^k C_{%s}^k x^{%s-2k}$. \\
                         Số hạng chứa $x^{%s}$ ứng với: $%s - 2k = %s \Leftrightarrow k = %s$. \\
                         Vậy hệ số cần tìm là: $(-%d)^{%d} \cdot C_{%d}^{%d} = %d$.'''
                       % (pt_n, latex(A_val), latex(B_val), step1_rhs, latex(quad_b), latex(quad_c), 
                          latex(n_val), bieu_thuc, latex(n_val), latex(n_val), latex(c_val), 
                          latex(c_val), latex(n_val), latex(n_val), latex(p_val), 
                          latex(n_val), latex(p_val), latex(k_val), c_val, k_val, n_val, k_val, kq))

            # Đáp án ngắn (Số nguyên cụ thể)
            dapan = "\\shortans[0]{$%d$}" % kq

            # Xuất nội dung
            content = ("\\begin{minipage}{\\textwidth} " + "\n"
                       "\\begin{ex}" + "\n" + noidungcauhoi + dapan + "\n"
                       "\\loigiai{" + loigiai + "}" + "\n"
                       "\\end{ex}" + "\n" + "\\end{minipage}" + "\n\n").replace('+-', '-').replace('++', '+')

            return content


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


def bt_dang47_p3_b3_c5_ds10(self):
            while True:
                # Random các thông số cơ bản (giới hạn n nhỏ để hệ số < 9999)
                a = 1
                n = random.randint(3, 5) 
                b = random.choice([-2, -1, 1, 2])
                c = random.choice([-2, -1, 1, 2])

                # Chọn bậc m của x cần tìm hệ số (thường chọn m gần n)
                m = random.randint(2, 2*n - 1)

                target_val = 2*n - m
                results_list = []
                tong_he_so = 0

                # Thuật toán tìm hệ số của x^m trong (ax^2 + bx + c)^n
                # Số hạng tổng quát: C(n, k) * (x^2)^(n-k) * (bx + c)^k
                # = C(n, k) * x^(2n-2k) * [C(k, i) * (bx)^i * c^(k-i)]
                # = C(n, k) * C(k, i) * b^i * c^(k-i) * x^(2n-2k+i)
                for k in range(n + 1):
                    # Điều kiện: 2n - 2k + i = m => i = 2k + m - 2n
                    i = 2*k + m - 2*n
                    if 0 <= i <= k:
                        coeff = math.comb(n, k) * math.comb(k, i) * (b**i) * (c**(k-i))
                        results_list.append((k, i, int(coeff)))
                        tong_he_so += coeff

                # Kiểm tra điều kiện kết quả: -999 < kq < 9999
                if results_list and -999 < tong_he_so < 9999:
                    kq = int(tong_he_so)
                    break

            # Định dạng hiển thị dấu cho đa thức
            b_tex = f"{b:+d}x" if abs(b) != 1 else ("+x" if b == 1 else "-x")
            c_tex = f"{c:+d}"

            # Câu hỏi
            noidungcauhoi = (r"Hệ số của số hạng chứa $x^{%d}$ trong khai triển biểu thức $P(x) = \left(x^2 %s %s \right)^{%d}$ bằng bao nhiêu?"
                             % (m, b_tex, c_tex, n))

            # Đáp án đúng
            da_d = r"\True $%d$" % kq

            # Tạo các phương án nhiễu
            s_set = set()
            while len(s_set) < 3:
                offset = random.choice([1, -1, 10, -10, 2, 5, 20])
                nhieu = kq + offset
                if nhieu != kq:
                    s_set.add(r"$%d$" % nhieu)

            list_ans = [da_d] + list(s_set)
            random.shuffle(list_ans)

            # Nội dung lời giải chi tiết
            buoc_giai_chi_tiet = ""
            for k_val, i_val, c_val in results_list:
                buoc_giai_chi_tiet += (r"$k = %d, i = %d \Rightarrow$ hệ số: $C_{%d}^{%d} \cdot C_{%d}^{%d} \cdot (%d)^{%d} \cdot (%d)^{%d} = %d$.\\ " 
                                       % (k_val, i_val, n, k_val, k_val, i_val, b, i_val, c, k_val - i_val, c_val))

            loigiai = (r"Số hạng tổng quát trong khai triển $(x^2 + %sx + %s)^n$ là:\\ "
                       r"$T = C_n^k (x^2)^{n-k} (%sx + %s)^k = C_n^k x^{2n-2k} \left[ \sum_{i=0}^k C_k^i (%sx)^i (%s)^{k-i} \right]$\\ "
                       r"$= \sum C_n^k C_k^i (%d)^i (%d)^{k-i} x^{2n-2k+i}$.\\ "
                       r"Số hạng chứa $x^{%d}$ ứng với $2n - 2k + i = %d \Leftrightarrow 2k - i = %d$.\\ "
                       r"Các cặp $(k, i)$ thỏa mãn $0 \le i \le k \le %d$ là:\\ "
                       r"%s"
                       r"Vậy hệ số cần tìm là: %d."
                       % (b, c, b, c, b, c, b, c, m, m, 2*n-m, n, buoc_giai_chi_tiet, kq))

            # Đáp án ngắn (Số nguyên cụ thể)
            dapan = "\\shortans[0]{$%d$}" % kq

            # Xuất nội dung
            content = ("\\begin{minipage}{\\textwidth} " + "\n"
                       "\\begin{ex}" + "\n" + noidungcauhoi + dapan +
                       "\\loigiai{" + loigiai + "}" + "\n"
                       "\\end{ex}" + "\n" + "\\end{minipage}" + "\n\n").replace('+-', '-').replace('++', '+').replace('(+1)', '1').replace('(1)', '1')

            return content


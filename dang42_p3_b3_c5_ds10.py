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


def bt_dang42_p3_b3_c5_ds10(self):
            while True:
                # B1: Random n thông qua bất phương trình n^2 - (m+1)n + 5m <= 0
                # Chọn các cặp m sao cho n_max nhỏ để hệ số không quá lớn (<9999)
                # m=18 -> n_max=10; m=13 -> n_max=8; m=21 -> n_max=15 (hơi lớn)
                pairs = [(9, 10, 18), (7, 8, 13), (6, 7, 10.5)] # m có thể là số thập phân
                x1, x2, m = random.choice(pairs)
                n_max = int(x2)

                # B2: Thiết lập biểu thức (ax + 1/x^(1/b))^n
                a = random.randint(1, 3) # Hệ số a nhỏ để kq < 9999
                b = random.randint(2, 4)

                # B3: Tìm p sao cho k = b*(n-p)/(b+1) là số nguyên
                p_possibilities = []
                for p_test in range(0, n_max + 1):
                    if (b * (n_max - p_test)) % (b + 1) == 0:
                        p_possibilities.append(p_test)

                if not p_possibilities: continue

                p = random.choice(p_possibilities)
                k_val = int(b * (n_max - p) / (b + 1))

                # B4: Tính hệ số = C(n, k) * a^(n-k)
                # Lưu ý: n-k là số mũ của ax, k là số mũ của 1/x^(1/b)
                he_so = math.comb(n_max, k_val) * (a**(n_max - k_val))

                # Kiểm tra điều kiện kết quả < 9999
                if 0 < he_so < 9999:
                    kq = int(he_so)
                    break

            # Tạo các phương án nhiễu
            s_set = set()
            while len(s_set) < 3:
                offset = random.choice([1, -1, 10, -10, 2, 5])
                nhieu = kq + offset
                if nhieu != kq and nhieu > 0:
                    s_set.add('$%s$' % (latex(int(nhieu))))

            list_ans = ['\\True $%s$' % latex(kq)] + list(s_set)
            random.shuffle(list_ans)

            # Câu hỏi
            noidungcauhoi = (r'''Hệ số của $x^{%s}$ trong khai triển nhị thức Newton $\left( %sx + \frac{1}{\sqrt[%s]{x}} \right)^n$ với $x > 0$, biết $n$ là số tự nhiên lớn nhất thỏa mãn $A_n^5 \le %s A_{n-2}^4$ bằng bao nhiêu?'''
                             % (latex(p), latex(a) if a != 1 else "", latex(b), latex(m)))

            # Nội dung lời giải
            loigiai = (r'''Điều kiện: $n \ge 6, n \in \mathbb{Z}$. \\
                         Khi đó $A_n^5 \le %s A_{n-2}^4 \Leftrightarrow n(n-1)(n-2)(n-3)(n-4) \le %s (n-2)(n-3)(n-4)(n-5)$ \\
                         $\Leftrightarrow n(n-1) \le %s(n-5) \Leftrightarrow n^2 - (%.1f + 1)n + 5 \cdot %.1f \le 0$ \\
                         $\Leftrightarrow n^2 - %.1fn + %s \le 0 \Leftrightarrow %s \le n \le %s$. \\
                         Vì $n$ là số tự nhiên lớn nhất nên $n = %s$. \\
                         Số hạng tổng quát: $T_{k+1} = C_{%s}^k \cdot (%sx)^{%s-k} \cdot (x^{-\frac{1}{%s}})^k = C_{%s}^k \cdot %s^{%s-k} \cdot x^{%s-k-\frac{k}{%s}}$. \\
                         Số hạng chứa $x^{%s}$ ứng với: $%s - \frac{%s+1}{%s}k = %s \Leftrightarrow k = %s$. \\
                         Vậy hệ số là $C_{%s}^{%s} \cdot %s^{%s} = %s$.'''
                       % (latex(m), latex(m), latex(m), m, m, m+1, latex(int(5*m)), latex(x1), latex(x2),
                          latex(n_max), latex(n_max), latex(a) if a != 1 else "", latex(n_max), latex(b),
                          latex(n_max), latex(a), latex(n_max), latex(n_max), latex(b),
                          latex(p), latex(n_max), latex(b), latex(b), latex(p), latex(k_val),
                          latex(n_max), latex(k_val), latex(a), latex(n_max-k_val), latex(kq)))

            # Đáp án ngắn (Số nguyên cụ thể)
            dapan = '\\shortans[0]{$%s$}\n' % (latex(kq))

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + noidungcauhoi + dapan +
                       '\\loigiai{' + loigiai + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n').replace('1x', 'x').replace('+-', '-')

            return content


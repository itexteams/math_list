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


def bt_dang42_p4_b3_c5_ds10(self):
            # Khai báo biết
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 1: Random n thông qua việc giải bất phương trình n^2 - (m+1)n + 5m <= 0
                # Để n nguyên và đẹp, ta chọn cặp nghiệm (x1, x2) của phương trình n^2 - (m+1)n + 5m = 0
                # Các cặp (x1, x2, m) thỏa mãn: (9, 10, 18), (7, 15, 21), (6, 25, 30)
                pairs = [(9, 10, 18), (7, 15, 21), (6, 25, 30)]
                x1, x2, m_val = random.choice(pairs)

                n_max = x2 # n lớn nhất thỏa mãn
                m = m_val

                # Bước 2: Thiết lập biểu thức (a*x + 1/x^(1/b))^n
                a = random.randint(2, 4)
                b = random.choice([2, 3, 4, 5])

                # Bước 3: Tìm số mũ p sao cho k = b*(n-p)/(b+1) là số nguyên dương
                # n_max - p phải chia hết cho b+1
                p_possibilities = []
                for p_test in range(1, n_max):
                    if (n_max - p_test) % (b + 1) == 0:
                        p_possibilities.append(p_test)

                p = random.choice(p_possibilities)
                k_val = int(b * (n_max - p) / (b + 1))

                # Bước 4: Tính hệ số
                # Hệ số = C(n, k) * a^(n-k)
                he_so = binomial(n_max, k_val) * (a**(n_max - k_val))
                kq = int(he_so)

                # Các đáp án trắc nghiệm
                da_dung = '$%s$' % (latex(kq))

                # Tạo các phương án sai
                s = set()
                while len(s) < 3:
                    # Sai do chọn sai n (chọn n-1)
                    n_wrong = n_max - 1
                    k_wrong = int(b * (n_wrong - p) / (b + 1)) if (b * (n_wrong - p)) % (b + 1) == 0 else k_val
                    wrong1 = int(binomial(n_wrong, k_wrong) * (a**(n_wrong - k_wrong)))

                    # Sai do quên lũy thừa của a
                    wrong2 = int(binomial(n_max, k_val))

                    # Sai do tính nhầm k (k +- 1 nếu hợp lệ)
                    wrong3 = int(binomial(n_max, k_val - 1) * (a**(n_max - (k_val - 1)))) if k_val > 0 else kq + 100

                    # Random thêm nếu trùng
                    candidates = [wrong1, wrong2, wrong3, kq + 1000, kq - 500, kq * 2]
                    val = random.choice(candidates)
                    if val != kq and val > 0:
                        s.add('$%s$' % (latex(int(val))))

                list_s = list(s)
                das1, das2, das3 = list_s[0], list_s[1], list_s[2]

                # Câu hỏi
                noidungcauhoi = ('''Tìm hệ số của $x^{%s}$ trong khai triển nhị thức Newton $\\left( %sx + \\frac{1}{\\sqrt[%s]{x}} \\right)^n$ với $x > 0$, biết $n$ là số tự nhiên lớn nhất thỏa mãn $A_n^5 \\le %s A_{n-2}^4$.'''
                                 % (latex(p), latex(a), latex(b), latex(m)))

                # Các đáp án
                da_d = ('\\True ' + str(da_dung))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_ans = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_ans)

                # Nội dung lời giải
                loigiai = ('''Điều kiện: $\\begin{cases} n \\ge 6 \\\\ n \\in \\mathbb{Z} \\end{cases}$ \\\\
                             Khi đó $A_n^5 \\le %s A_{n-2}^4 \\Leftrightarrow \\frac{n!}{\\left( n-5 \\right)!} \\le %s \\cdot \\frac{\\left( n-2 \\right)!}{\\left( n-6 \\right)!}$ \\\\
                             $\\Leftrightarrow n\\left( n-1 \\right)\\left( n-2 \\right)\\left( n-3 \\right)\\left( n-4 \\right) \\le %s\\left( n-2 \\right)\\left( n-3 \\right)\\left( n-4 \\right)\\left( n-5 \\right)$ \\\\
                             $\\Leftrightarrow n\\left( n-1 \\right) \\le %s\\left( n-5 \\right) \\Leftrightarrow n^2 - %sn + %s \\le 0 \\Leftrightarrow %s \\le n \\le %s$. \\\\
                             Vì $n$ là số tự nhiên lớn nhất nên $n = %s$. \\\\
                             Số hạng tổng quát trong khai triển $\\left( %sx + \\frac{1}{\\sqrt[%s]{x}} \\right)^{%s}$ là $T_{k+1} = C_{%s}^k \\cdot \\left( %sx \\right)^{%s-k} \\cdot \\left( \\frac{1}{\\sqrt[%s]{x}} \\right)^k$ \\\\
                             $= C_{%s}^k \\cdot %s^{%s-k} \\cdot x^{%s-k} \\cdot x^{-\\frac{k}{%s}} = C_{%s}^k \\cdot %s^{%s-k} \\cdot x^{\\frac{%s-%sk}{%s}}$. \\\\
                             Tìm $k$ sao cho $\\frac{%s-%sk}{%s} = %s \\Leftrightarrow %s - %sk = %s \\Leftrightarrow k = %s$. \\\\
                             Vậy hệ số của số hạng chứa $x^{%s}$ là $C_{%s}^{%s} \\cdot %s^{%s-%s} = %s$.'''
                           % (latex(m), latex(m), latex(m), latex(m), latex(m + 1), latex(5 * m), latex(x1), latex(x2),
                              latex(n_max),
                              latex(a), latex(b), latex(n_max), latex(n_max), latex(a), latex(n_max), latex(b),
                              latex(n_max), latex(a), latex(n_max), latex(n_max), latex(b), latex(n_max), latex(a), latex(n_max),
                              latex(b * n_max), latex(b + 1), latex(b),
                              latex(b * n_max), latex(b + 1), latex(b), latex(p), latex(b * n_max), latex(b + 1), latex(b * p), latex(k_val),
                              latex(p), latex(n_max), latex(k_val), latex(a), latex(n_max), latex(k_val), latex(kq)
                              ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) +
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content


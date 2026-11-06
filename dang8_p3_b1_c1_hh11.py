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


def bt_dang8_p3_b1_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Random hệ số tỉ lệ các cạnh m, n, p
        m = random.choice([1, 2, 3])
        n = random.choice([1, 2, 3])
        p = random.choice([1, 2, 3, 4])

        # Tạo chuỗi điều kiện
        str_M = "AM = MB" if m == 1 else f"AM = {m}MB"
        str_N = "AN = NC" if n == 1 else f"AN = {n}NC"
        str_P = "AP = PD" if p == 1 else f"AP = {p}PD"

        # Tính toán các tỉ số (sử dụng sympy.Rational để giữ độ chính xác tuyệt đối)
        val1 = sp.Rational(m + 1, m)
        val2 = sp.Rational(n + 1, n)
        val3 = sp.Rational(p + 1, p)

        ratio_AT = sp.Rational(1, 2) * (val1 + val2)
        ratio_AS = sp.Rational(1, 2) * (ratio_AT + val3)

        # Tính kết quả thập phân và làm tròn đến phần trăm
        kq_exact = float(ratio_AS)
        kq_dec = Decimal(kq_exact).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        kq_str = str(kq_dec).replace('.', ',')

        # Các đáp án trắc nghiệm nhiễu
        choices = [
            Decimal(kq_exact + 0.15).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP),
            Decimal(kq_exact - 0.15).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP),
            Decimal(kq_exact + 0.25).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP),
            Decimal(kq_exact - 0.25).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP),
            Decimal(kq_exact * 1.2).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP),
            Decimal(float(ratio_AT)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        ]

        # Lọc đáp án nhiễu (loại trùng lặp và trùng đáp án đúng)
        s = []
        for c in choices:
            c_str = str(c).replace('.', ',')
            if c_str != kq_str and c_str not in s:
                s.append(c_str)

        random.shuffle(s)
        das1 = s[0]
        das2 = s[1]
        das3 = s[2]

        # Các đáp án
        da_d = '\\True $%s$' % kq_str
        da_s1 = '$%s$' % das1
        da_s2 = '$%s$' % das2
        da_s3 = '$%s$' % das3

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Chuỗi LaTeX hỗ trợ lời giải
        l_val1 = sp.latex(val1)
        l_val2 = sp.latex(val2)
        l_val3 = sp.latex(val3)
        l_AT = sp.latex(ratio_AT)
        l_AS = sp.latex(ratio_AS)

        # Câu hỏi và hình vẽ TikZ
        noidungcauhoi = ('''Cho tứ diện $ABCD$. Gọi $M, N, P$ lần lượt thuộc các cạnh $AB, AC$ và $AD$ sao cho $%s, %s$ và $%s$. Gọi $Q$ là trung điểm cạnh $BC, I$ là trung điểm của đoạn $DQ$ và $S$ là giao điểm của mặt phẳng $(MNP)$ và đường thẳng $AI$. Tỉ số $\\frac{AI}{AS}$ bằng bao nhiêu? (kết quả làm tròn đến hàng phần trăm).''' % (str_M, str_N, str_P))

        # Nội dung lời giải
        loigiai = ('''\\begin{center}
        \\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\coordinate (A) at (2.5,4.5);
        \\coordinate (B) at (0,0);
        \\coordinate (C) at (4,-1.5);
        \\coordinate (D) at (6.5,0);
        \\coordinate (M) at ($(A)!%s/%s!(B)$);
        \\coordinate (N) at ($(A)!%s/%s!(C)$);
        \\coordinate (P) at ($(A)!%s/%s!(D)$);
        \\coordinate (Q) at ($(B)!0.5!(C)$);
        \\coordinate (I) at ($(D)!0.5!(Q)$);
        \\coordinate (T) at (intersection of M--N and A--Q);
        \\coordinate (S) at (intersection of T--P and A--I);
        \\draw[line width=1pt] (A)--(B) (A)--(C) (A)--(D) (B)--(C) (C)--(D) (M)--(N) (A)--(Q);
        \\draw[line width=1pt, dashed] (B)--(D) (D)--(Q) (A)--(I) (N)--(P) (T)--(P);
        \\fill (A) circle (1pt) node[above] {$A$};
        \\fill (B) circle (1pt) node[left] {$B$};
        \\fill (C) circle (1pt) node[below] {$C$};
        \\fill (D) circle (1pt) node[right] {$D$};
        \\fill (M) circle (1pt) node[left] {$M$};
        \\fill (N) circle (1pt) node[below right] {$N$};
        \\fill (P) circle (1pt) node[above right] {$P$};
        \\fill (Q) circle (1pt) node[below left] {$Q$};
        \\fill (I) circle (1pt) node[below right] {$I$};
        \\fill (T) circle (1pt) node[below left] {$T$};
        \\fill (S) circle (1pt) node[above left] {$S$};
        \\end{tikzpicture}
        \\end{center} Gọi $T$ là giao điểm của $MN$ với $AQ$ và $S$ là giao điểm của $TP$ với $AI$.\\\\
    Khi đó $\\begin{cases} S \\in AI \\\\ S \\in TP \\subset (MNP) \\end{cases} \\Rightarrow S = AI \\cap (MNP)$.\\\\
    Ta có $\\frac{AQ}{AT} = \\frac{1}{2}\\left(\\frac{AB}{AM} + \\frac{AC}{AN}\\right) = \\frac{1}{2}\\left(%s + %s\\right) = %s$.\\\\
    Ta có $\\frac{AI}{AS} = \\frac{1}{2}\\left(\\frac{AQ}{AT} + \\frac{AD}{AP}\\right) = \\frac{1}{2}\\left(%s + %s\\right) = %s \\approx %s$.''' % (m, m+1, n, n+1, p, p+1, l_val1, l_val2, l_AT, l_AT, l_val3, l_AS, kq_str))
    dapan='\\shortans[0]{$%s$}\n'%(kq_str)
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
        '\\loigiai{\n'+str(loigiai)+'\n}\n'
        '\\end{ex}\n\\end{minipage} \n\n')
    return content      


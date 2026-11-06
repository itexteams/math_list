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


def bt_dang8_p3_b3_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # B3: Random các số trong bài toán
        # Đáy lớn AB = k1 * a, đáy nhỏ CD = k2 * a sao cho k1 > k2 và phân số k2/k1 tối giản
        pairs = [(5, 2), (4, 1), (5, 3), (7, 2), (7, 3), (8, 3), (7, 4), (5, 1)]
        k1, k2 = random.choice(pairs)

        # Do k2 và k1 nguyên tố cùng nhau nên:
        # SE/SB = HC/HB = CD/AB = k2/k1
        # ES/EB = SE/(SB - SE) = k2/(k1 - k2)
        diff = k1 - k2
        gcd_val = math.gcd(k2, diff)
        m = k2 // gcd_val
        n = diff // gcd_val

        # Giá trị 2m + 3n
        kq_val = 2 * m + 3 * n
        kq = str(kq_val)

        # B4: Điều chỉnh các phương án sai không trùng với đáp án đúng
        s_set = set()
        offsets = [1, 2, 3, 4, -1, -2, -3, -4, 5, -5]
        for off in offsets:
            val = kq_val + off
            if val > 0 and val != kq_val:
                s_set.add(str(val))

        s = ['$%s$' % v for v in s_set]
        du = ['$%s$' % (kq)]
        da = random.choice(du)

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # B1 & B2: Đề bài
        noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình thang với $AB$ là đáy lớn. Biết $AB = %sa, CD = %sa$. Gọi $E$ là điểm thuộc cạnh $SB$ thỏa mãn $\\frac{ES}{EB} = \\frac{m}{n}$ với $\\frac{m}{n}$ là phân số tối giản. Biết rằng $CE$ song song với mặt phẳng $(SAD)$. Giá trị của $2m + 3n$ bằng bao nhiêu?'''
                         % (latex(k1), latex(k2)))

        # Tỷ số điểm E trên SB: SE/SB = k2/k1
        t_e = round(float(Rational(k2, k1)), 2)

        # Hình vẽ TikZ vẽ 100% như ảnh mẫu, đường nét 1pt, điểm 1pt, màu black
        tikz_code = '''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\coordinate (A) at (0,0);
        \\coordinate (B) at (6,0);
        \\coordinate (D) at (2.6,-1.7);
        \\coordinate (C) at (5,-1.7);
        \\coordinate (S) at (3,3.2);
        \\coordinate (H) at (intersection of A--D and B--C);
        \\coordinate (E) at ($(S)!''' + str(t_e) + '''!(B)$);
        \\draw[line width=1pt] (S)--(A)--(D)--(H)--(C)--(B)--(S)--(D) (S)--(H) (S)--(C) (C)--(E);
        \\draw[line width=1pt, dashed] (A)--(B) (D)--(C);
        \\fill (A) circle (1pt) node[left] {$A$};
        \\fill (B) circle (1pt) node[right] {$B$};
        \\fill (C) circle (1pt) node[below right] {$C$};
        \\fill (D) circle (1pt) node[below left] {$D$};
        \\fill (S) circle (1pt) node[above left] {$S$};
        \\fill (H) circle (1pt) node[below] {$H$};
        \\fill (E) circle (1pt) node[above right] {$E$};
    \\end{tikzpicture}
    \\end{center}'''

        # Lời giải chi tiết
        loigiai = ('''%s
    Gọi $H$ là giao điểm của $AD$ và $BC$ trong mặt phẳng $(ABCD)$. \\\\
    Theo hệ quả Talet, ta có: $\\frac{HC}{HB} = \\frac{CD}{AB} = \\frac{%s}{%s}$. \\\\
    Ta có: \\\\
    $\\begin{cases} CE \\subset (SBH) \\\\ CE // (SAD) \\\\ (SBH) \\cap (SAD) = SH \\end{cases} \\Rightarrow CE // SH$ \\\\
    $\\Rightarrow \\frac{SE}{SB} = \\frac{HC}{HB} = \\frac{%s}{%s} \\Rightarrow SE = \\frac{%s}{%s} SB$ \\\\
    $\\Rightarrow \\frac{ES}{EB} = \\frac{%s}{%s} \\Rightarrow 2m + 3n = 2 \\cdot %s + 3 \\cdot %s = %s$.'''
                   % (tikz_code,
                      latex(k2), latex(k1),
                      latex(k2), latex(k1), latex(k2), latex(k1),
                      latex(m), latex(n),
                      latex(m), latex(n),
                      latex(kq_val)))
    dapan='\\shortans[0]{$%s$}\n'%(latex(kq_val))
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
               '\\loigiai{' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content


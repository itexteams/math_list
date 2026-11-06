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


def bt_dang19_p3_b1_c1_ds12(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Thiết kế tham số để nghiệm đạo hàm luôn đẹp
        t1 = randint(8, 12)    # Nghiệm cực đại thứ nhất
        t2 = t1 + randint(8, 12) # Nghiệm cực tiểu thứ hai
        t_max = t2 + randint(15, 25)

        # Chọn hệ số k
        k = random.choice([120, 180, 240])

        A_val = k // 3
        B_val = - (k * (t1 + t2)) // 2
        C_val = k * t1 * t2
        D_val = random.choice([50000, 80000, 100000, 120000])

        # Tính độ dài hai khoảng đồng biến
        len1 = t1 - 0
        len2 = t_max - t2

        # So sánh để tìm khoảng thời gian vi khuẩn tăng dài nhất
        if len1 > len2:
            a_val = 0
            b_val = t1
            khoang_dai_nhat = f"(0; {t1})"
            giai_thich_khoang = f"Vì độ dài khoảng $(0; {t1})$ là ${t1} - 0 = {t1}$ giây, lớn hơn độ dài khoảng $({t2}; {t_max})$ là ${t_max} - {t2} = {len2}$ giây, nên khoảng thời gian tăng dài nhất là $(0; {t1})$."
        else:
            a_val = t2
            b_val = t_max
            khoang_dai_nhat = f"({t2}; {t_max})"
            giai_thich_khoang = f"Vì độ dài khoảng $({t2}; {t_max})$ là ${t_max} - {t2} = {len2}$ giây, lớn hơn độ dài khoảng $(0; {t1})$ là ${t1} - 0 = {len1}$ giây, nên khoảng thời gian tăng dài nhất là $({t2}; {t_max})$."

        # Hiệu a - b
        hieu_val = a_val - b_val
        kq = hieu_val

        # Các đáp án trắc nghiệm
        du = ['$%s$' % (kq)]
        da = random.choice(du)

        # Tạo các phương án nhiễu 
        s_candidates = [
            -t1,
            t1,
            -t2,
            t2,
            t1 - t2,
            t2 - t1,
            t2 - t_max
        ]

        s = []
        for val in s_candidates:
            val_str = str(val).replace('.', ',')
            s.append('$%s$' % (val_str))

        s = [item for item in s if item != da]
        s = list(set(s))

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        # Định dạng dấu cho các hệ số
        sign_B = '+' if B_val >= 0 else ''
        sign_C = '+' if C_val >= 0 else ''
        sign_D = '+' if D_val >= 0 else ''

        ham_so_latex = '%s t^3 %s %s t^2 %s %s t %s %s' % (latex(A_val), sign_B, latex(B_val), sign_C, latex(C_val), sign_D, latex(D_val))
        ham_so_latex = ' '.join(ham_so_latex.split())

        # Câu hỏi
        noidungcauhoi = ('''Trong một thí nghiệm y học, người ta cấy $%s$ con vi khuẩn vào môi trường dinh dưỡng. Bằng thực nghiệm người ta xác định được số lượng vi khuẩn $N$ thay đổi theo thời gian bằng công thức $N(t) = %s$ (thời gian $t$ tính bằng giây $0 \\le t \\le %s$). Gọi $(a;b)$ là khoảng thời gian dài nhất để vi khuẩn tăng. Hiệu $a - b$ bằng bao nhiêu?'''
                         % (latex(D_val), ham_so_latex, latex(t_max)))

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2) 
        da_s3 = str(das3) 

        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Chuẩn bị lời giải chi tiết
        der_A = 3 * A_val
        der_B = 2 * B_val
        der_C = C_val
        sign_der_B = '+' if der_B >= 0 else ''
        sign_der_C = '+' if der_C >= 0 else ''

        # Lời giải
        loigiai = ('''Xét hàm số biểu thị số lượng vi khuẩn $N(t) = %s$ trên đoạn $[0; %s]$.\\\\
                       Ta tính đạo hàm của hàm số theo biến $t$:\\\\
                       $N\'(t) = %s t^2 %s %s t %s %s$.\\\\
                       Cho đạo hàm bằng $0$:\\\\
                       $N\'(t) = 0 \\Leftrightarrow %s t^2 %s %s t %s %s = 0 \\Leftrightarrow \\left[\\begin{aligned} & t = %s \\\\ & t = %s \\end{aligned}\\right.$.\\\\
                       Ta lập bảng biến thiên của hàm số trên đoạn $[0; %s]$ như sau:\\\\
                       \\begin{center}
                       \\begin{tikzpicture}[scale=1]
                       \\draw[line width=1pt] (0,0) rectangle (10,4);
                       \\draw[line width=1pt] (0,3) -- (10,3);
                       \\draw[line width=1pt] (0,2) -- (10,2);
                       \\draw[line width=1pt] (2,0) -- (2,4);
                       \\node at (1,3.5) {$t$};
                       \\node[anchor=west] at (2,3.5) {$0$};
                       \\node at (4.5,3.5) {$%s$};
                       \\node at (7,3.5) {$%s$};
                       \\node[anchor=east] at (10,3.5) {$%s$};
                       \\node at (1,2.5) {$N\'(t)$};
                       \\node at (3.25,2.5) {$+$};
                       \\node at (4.5,2.5) {$0$};
                       \\node at (5.75,2.5) {$-$};
                       \\node at (7,2.5) {$0$};
                       \\node at (8.5,2.5) {$+$};
                       \\node at (1,1) {$N(t)$};
                       \\draw[->,line width=1pt] (2.4,0.3) -- (4.2,1.7);
                       \\draw[->,line width=1pt] (4.8,1.7) -- (6.7,0.3);
                       \\draw[->,line width=1pt] (7.3,0.3) -- (9.4,1.7);
                       \\end{tikzpicture}
                       \\end{center}
                       Dựa vào bảng biến thiên, ta thấy trên đoạn $[0; %s]$, hàm số đồng biến (số lượng vi khuẩn tăng) trên các khoảng $(0; %s)$ và $(%s; %s)$.\\\\
                       %s\\\\
                       Theo bài ra, $(a; b)$ là khoảng thời gian dài nhất để vi khuẩn tăng, do đó $(a; b) = %s$, suy ra $a = %s$ và $b = %s$.\\\\
                       Vậy hiệu $a - b = %s - %s = %s$.'''
                       % (ham_so_latex, latex(t_max),
                          latex(der_A), sign_der_B, latex(der_B), sign_der_C, latex(der_C),
                          latex(der_A), sign_der_B, latex(der_B), sign_der_C, latex(der_C), latex(t1), latex(t2),
                          latex(t_max), latex(t1), latex(t2), latex(t_max),
                          latex(t_max), latex(t1), latex(t2), latex(t_max),
                          giai_thich_khoang, khoang_dai_nhat, latex(a_val), latex(b_val),
                          latex(a_val), latex(b_val), latex(kq)))
        dapan='\\shortans[0]{$%s$}\n'%(latex(kq))

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
               '\\loigiai{' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content


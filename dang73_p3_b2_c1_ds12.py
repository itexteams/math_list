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


def bt_dang73_p3_b2_c1_ds12(self):
    # Hàm định dạng số: tự động làm gọn số nguyên và thay dấu . thành ,
    def fmt(num):
        if isinstance(num, (int, float, Decimal)):
            if float(num).is_integer():
                return str(int(num))
            else:
                s = f"{float(num):g}"
                return s.replace('.', ',')
        return str(num).replace('.', ',')

    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)

    if dang=='1':
        # B3: Thuật toán Random đảm bảo x0 và hệ số a luôn là số nguyên đẹp
        while True:
            # Chọn tỷ lệ thuế t (%)
            t_val = random.choice([5, 10, 15, 20])
            k_dec = (Decimal(100) - Decimal(t_val)) / Decimal(100)

            # Chọn hệ số b của R(x) = a*x - b*x^2
            b_val = random.choice([0.002, 0.0025, 0.004, 0.005])
            b_dec = Decimal(str(b_val))

            # Chọn số lượng sản phẩm x0 tối ưu
            x0_val = random.choice([800, 1000, 1200, 1500, 1600, 1800, 2000, 2500])

            # Tính A và B cho P(x) = -A*x^2 + B*x
            A_dec = k_dec * b_dec
            two_A_dec = Decimal('2') * A_dec
            B_dec = two_A_dec * Decimal(x0_val)

            # Chọn chi phí c sao cho a = (B + c)/k là số nguyên
            c_candidates = [c_cand for c_cand in range(5, 50) if (B_dec + Decimal(c_cand)) % k_dec == Decimal('0')]
            if not c_candidates:
                continue
            c_val = random.choice(c_candidates)
            a_val = int((B_dec + Decimal(c_val)) / k_dec)

            if a_val <= 0 or a_val > 100:
                continue

            # N là số sản phẩm tối đa (N > x0)
            N_val = x0_val + random.choice([1000, 1500, 2000, 2500])
            break

        # Tính các giá trị P(x0) và P(N) điền vào Bảng biến thiên
        P_x0 = A_dec * (Decimal(x0_val) ** 2)
        P_N = -A_dec * (Decimal(N_val) ** 2) + B_dec * Decimal(N_val)

        # Chuyển đổi các số sang chuỗi hiển thị chuẩn tiếng Việt (dùng dấu phẩy)
        a_str = fmt(a_val)
        b_str = fmt(b_dec)
        t_str = fmt(t_val)
        k_str = fmt(k_dec)
        c_str = fmt(c_val)
        N_str = fmt(N_val)
        x0_str = fmt(x0_val)
        A_str = fmt(A_dec)
        B_str = fmt(B_dec)
        two_A_str = fmt(two_A_dec)
        P_x0_str = fmt(P_x0)
        P_N_str = fmt(P_N)

        # Đáp án đúng
        kq = x0_str
        du = ['$%s$' % (kq)]
        da = random.choice(du)

        # B4: Tạo các phương án sai (đảm bảo không trùng với đáp án đúng và không trùng nhau)
        wrong_vals = set()
        try:
            w1 = int(round((a_val - c_val) / (2 * float(b_val))))
            if w1 > 0 and w1 != x0_val:
                wrong_vals.add(w1)
        except:
            pass

        try:
            w2 = int(round(a_val / (2 * float(b_val))))
            if w2 > 0 and w2 != x0_val:
                wrong_vals.add(w2)
        except:
            pass

        for offset in [-300, -200, -100, -50, 50, 100, 200, 300]:
            val = x0_val + offset
            if val > 0 and val != x0_val:
                wrong_vals.add(val)

        s = ['$%s$' % (fmt(v)) for v in wrong_vals]
        random.shuffle(s)

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một doanh nghiệp dự kiến sản xuất không quá $%s$ sản phẩm cùng loại. Giả sử rằng doanh thu của doanh nghiệp khi sản xuất $x$ sản phẩm ($x \\in \\mathbb{N}; 0 \\le x \\le %s$) là $R(x) = %sx - %sx^2$ (triệu đồng) và doanh nghiệp phải nộp một khoản thuế là $%s\\%%$ của doanh thu $R(x)$. Chi phí để sản xuất mỗi sản phẩm là $%s$ triệu đồng. Lợi nhuận của doanh nghiệp (khi sản xuất $x$ sản phẩm) được tính theo công thức: Lợi nhuận bằng doanh thu trừ đi thuế và chi phí. Doanh nghiệp phải sản xuất bao nhiêu sản phẩm để thu được lợi nhuận lớn nhất?'''
                         % (N_str, N_str, a_str, b_str, t_str, c_str))

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        # Trộn các đáp án
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải (Bọc nhãn bảng biến thiên trong {} để không bị lỗi tkz-tab)
        loigiai = ('''Hàm lợi nhuận của doanh nghiệp khi sản xuất $x$ sản phẩm là: \\\\
                 $P(x) = R(x) - %s\\%% R(x) - %sx = %s( %sx - %sx^2 ) - %sx = -%sx^2 + %sx$. \\\\
                 Đạo hàm của hàm lợi nhuận: $P'(x) = -%sx + %s$. \\\\
                 Ta có $P'(x) = 0 \\Leftrightarrow -%sx + %s = 0 \\Leftrightarrow x = %s$. \\\\
                 Bảng biến thiên của hàm số $P(x)$ trên đoạn $[0; %s]$: \\\\
                 \\begin{center}
                 \\begin{tikzpicture} 
                 \\tkzTabInit[espcl=2.5,lgt=1.5]  
                 {$x$/0.7,$P'(x)$/0.7,$P(x)$/2} 
                 {$0$,$%s$,$%s$}  
                 \\tkzTabLine{,+,0,-,}  
                 \\tkzTabVar{-/$0$,+/{$%s$},-/{$%s$}} 
                 \\end{tikzpicture}
                 \\end{center}
                 Căn cứ vào bảng biến thiên, hàm số $P(x)$ đạt giá trị lớn nhất tại $x = %s$ trên đoạn $[0; %s]$. \\\\
                 Vậy doanh nghiệp cần sản xuất $%s$ sản phẩm để thu được lợi nhuận lớn nhất.'''
                 % (t_str, c_str, k_str, a_str, b_str, c_str, A_str, B_str,
                    two_A_str, B_str,
                    two_A_str, B_str, x0_str,
                    N_str,
                    x0_str, N_str,
                    P_x0_str, P_N_str,
                    x0_str, N_str,
                    x0_str))
    dapan='\\shortans[0]{$%s$}\n'%(x0_str)
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
        '\\loigiai{' + str(loigiai) + '}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content


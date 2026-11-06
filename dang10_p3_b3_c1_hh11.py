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


def bt_dang10_p3_b3_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # B3: Random các số trong bài toán
        # Trong bài gốc: a_ratio = 2, b_ratio = 4
        pairs = [(2, 4), (2, 3), (2, 5), (3, 4), (3, 5)]
        a_ratio, b_ratio = random.choice(pairs)



        tu_he = b_ratio - 1
        mau_he = a_ratio * b_ratio
        frac_he = Rational(tu_he, mau_he)

        tu_k = a_ratio * b_ratio - b_ratio + 1
        mau_k = b_ratio - 1
        frac_k = Rational(tu_k, mau_k)

        # Tính giá trị làm tròn đến hàng phần trăm (2 chữ số thập phân)
        k_num = float(frac_k)
        kq_dec = Decimal(str(k_num)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        kq = str(kq_dec).replace('.', ',')

        # B4: Điều chỉnh các phương án sai không trùng với đáp án đúng
        s_set = set()
        offsets = [Decimal('0.05'), Decimal('-0.05'), Decimal('0.10'), Decimal('-0.10'),
                   Decimal('0.15'), Decimal('-0.15'), Decimal('0.20'), Decimal('-0.20'),
                   Decimal('0.25'), Decimal('-0.25')]
        for off in offsets:
            val = kq_dec + off
            if val > 0 and val != kq_dec:
                s_set.add(str(val).replace('.', ','))

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
        noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình thang với $AD$ song song với $BC$ và $AD = %sBC$. Gọi $E$ là điểm thuộc cạnh $BC$ sao cho $BC = %sBE$. Lấy $F$ thuộc cạnh $SA$ sao cho $FA = k \\cdot FS$. Biết rằng $EF$ song song với mặt phẳng $(SCD)$. Khi đó giá trị của $k$ bằng bao nhiêu? (kết quả làm tròn đến hàng phần trăm)'''
                         % (latex(a_ratio), latex(b_ratio)))

        # Tọa độ tỉ lệ phục vụ vẽ hình TikZ
        t_e = round(1.0 / b_ratio, 3)
        t_sf = round(float(frac_he), 3)

        # Hình vẽ TikZ vẽ chuẩn 100% như ảnh mẫu, đường nét 1pt, điểm 1pt, màu black
        tikz_code = '''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\coordinate (A) at (0,0);
        \\coordinate (D) at (5.5,0);
        \\coordinate (B) at (1.8,-1.7);
        \\coordinate (C) at (4.5,-1.7);
        \\coordinate (S) at (2.7,3.5);
        \\coordinate (E) at ($(B)!''' + str(t_e) + '''!(C)$);
        \\coordinate (H) at (intersection of A--E and C--D);
        \\coordinate (F) at ($(S)!''' + str(t_sf) + '''!(A)$);
        \\draw[line width=1pt] (S)--(A) (S)--(D) (S)--(C) (S)--(B) (A)--(B)--(E) (S)--(H)--(C)--(D) (C)--(H) (E)--(H);
        \\draw[line width=1pt, dashed] (A)--(D) (B)--(C) (A)--(E) (E)--(F);
        \\fill (A) circle (1pt) node[left] {$A$};
        \\fill (D) circle (1pt) node[right] {$D$};
        \\fill (B) circle (1pt) node[below left] {$B$};
        \\fill (C) circle (1pt) node[below right] {$C$};
        \\fill (S) circle (1pt) node[above] {$S$};
        \\fill (E) circle (1pt) node[below] {$E$};
        \\fill (F) circle (1pt) node[above left] {$F$};
        \\fill (H) circle (1pt) node[below] {$H$};
    \\end{tikzpicture}
    \\end{center}'''

        # Lời giải chi tiết
        loigiai = ('''%s
    Gọi $H$ là giao điểm của $AE$ và $CD$ trong mặt phẳng $(ABCD)$. \\\\
    Theo hệ quả Talet, ta có: $\\frac{HE}{HA} = \\frac{CE}{AD} = \\frac{%s}{%s}$. \\\\
    Ta có: \\\\
    $\\begin{cases} EF \\subset (SAH) \\\\ EF // (SCD) \\\\ (SAH) \\cap (SCD) = SH \\end{cases} \\Rightarrow EF // SH$ \\\\
    $\\Rightarrow \\frac{SF}{SA} = \\frac{HE}{HA} = \\frac{%s}{%s} \\Rightarrow SF = \\frac{%s}{%s} SA$ \\\\
    $\\Rightarrow FA = \\frac{%s}{%s} FS \\Rightarrow k = \\frac{%s}{%s} \\approx %s$.'''
                   % (tikz_code,
                      latex(tu_he), latex(mau_he),
                      latex(tu_he), latex(mau_he), latex(tu_he), latex(mau_he),
                      latex(tu_k), latex(mau_k), latex(tu_k), latex(mau_k),
                      kq))
    dapan='\\shortans[0]{$%s$}\n'%(kq)
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) +dapan+
               '\\loigiai{' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content


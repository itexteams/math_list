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


def bt_dang7_p3_b2_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        danh_sach_so = [
            (2, 4),      # Bài toán gốc
            (3, 5),
            (2, 6),
            (1.5, 4.5),
            (2.5, 3.5),
            (3, 4),
            (4, 5),
            (1.5, 3.5),
            (2.5, 5.5),
            (3.5, 4.5),
            (2, 5),
            (3, 6)
        ]

        b_val, d_val = random.choice(danh_sach_so)

        # Tính CC' = BB' + DD' và OI = (BB' + DD') / 2
        cc_val = b_val + d_val
        oi_val = cc_val / 2.0

        # Hàm chuyển đổi số sang dạng chuỗi thập phân dùng dấu phẩy (làm tròn hàng phần trăm nếu lẻ)
        def format_so(val):
            dec_val = Decimal(str(val)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
            val_flt = float(dec_val)
            if val_flt.is_integer():
                return str(int(val_flt))
            else:
                s = str(dec_val).rstrip('0').rstrip('.')
                return s.replace('.', ',')

        str_bb = format_so(b_val)
        str_dd = format_so(d_val)
        str_oi = format_so(oi_val)
        str_cc = format_so(cc_val)

        # Đáp án đúng
        da = '$%s$' % (str_cc)

        # B4: Sinh các phương án sai khác nhau và tuyệt đối không trùng với đáp án đúng
        sai_cands = set()
        for delta in [-3.0, -2.0, -1.0, -0.5, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0]:
            val_sai = cc_val + delta
            if val_sai > 0 and abs(val_sai - cc_val) > 1e-4:
                str_sai = format_so(val_sai)
                if str_sai != str_cc:
                    sai_cands.add('$%s$' % (str_sai))

        sai_list = list(sai_cands)
        random.shuffle(sai_list)
        das1 = sai_list[0]
        das2 = sai_list[1]
        das3 = sai_list[2]

        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # TikZ code hình vẽ 100% chuẩn theo mẫu (nét 1pt, điểm 1pt, màu black, không raw string)
        hinh_ve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (A) at (0,0);\n'
            '\\coordinate (D) at (4.5,-0.6);\n'
            '\\coordinate (B) at (1.8,1.4);\n'
            '\\coordinate (C) at ($(B)+(D)-(A)$);\n'
            '\\coordinate (vecU) at (-0.3,1.8);\n'
            '\\coordinate (Bprime) at ($(B)+1.1*(vecU)$);\n'
            '\\coordinate (Dprime) at ($(D)+1.6*(vecU)$);\n'
            '\\coordinate (Cprime) at ($(Bprime)+(Dprime)-(A)$);\n'
            '\\coordinate (O) at ($(A)!0.5!(C)$);\n'
            '\\coordinate (I) at ($(A)!0.5!(Cprime)$);\n'
            '\\coordinate (X) at ($(Bprime)+1.2*(vecU)$);\n'
            '\\coordinate (Z) at ($(Dprime)+1.3*(vecU)$);\n'
            '\\coordinate (Y) at ($(Cprime)+0.7*(vecU)$);\n'
            '\\draw[line width=1pt] (A)--(D)--(C) (D)--(Dprime)--(Z) (C)--(Cprime)--(Y) (Bprime)--(X);\n'
            '\\draw[line width=1pt] (A)--(Bprime)--(Cprime)--(Dprime)--(A) (A)--(Cprime) (Bprime)--(Dprime);\n'
            '\\draw[line width=1pt, dashed] (A)--(B)--(C) (B)--(Bprime) (A)--(C) (B)--(D) (O)--(I);\n'
            '\\fill (A) circle (1pt) node[left] {$A$};\n'
            '\\fill (B) circle (1pt) node[left] {$B$};\n'
            '\\fill (C) circle (1pt) node[right] {$C$};\n'
            '\\fill (D) circle (1pt) node[below] {$D$};\n'
            '\\fill (Bprime) circle (1pt) node[left] {$B\'$};\n'
            '\\fill (Cprime) circle (1pt) node[above right] {$C\'$};\n'
            '\\fill (Dprime) circle (1pt) node[right] {$D\'$};\n'
            '\\fill (O) circle (1pt) node[below] {$O$};\n'
            '\\fill (I) circle (1pt) node[above] {$I$};\n'
            '\\node[above left] at (X) {$x$};\n'
            '\\node[above left] at (Z) {$z$};\n'
            '\\node[above left] at (Y) {$y$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )

        # B2: Nội dung câu hỏi và lời giải chi tiết theo đúng từng bước của ảnh gốc
        noidungcauhoi = ('''Trong mặt phẳng $(P)$, cho hình bình hành $ABCD$. Vẽ các tia $Bx, Cy, Dz$ song song với nhau, nằm cùng phía với mặt phẳng $(ABCD)$, đồng thời không nằm trong mặt phẳng $(ABCD)$. Một mặt phẳng đi qua $A$, cắt $Bx, Cy, Dz$ tương ứng tại $B\', C\', D\'$ sao cho $BB\' = %s$, $DD\' = %s$. Độ dài $CC\'$ bằng bao nhiêu?'''
                         % (str_bb, str_dd))

        loigiai = ('''%s
    Ta có: $AB\'C\'D\'$ là hình bình hành.\\\\
    $AC\' \\cap BD\' = I$ và $AC \\cap BD = O \\Rightarrow OI$ là đường trung bình của tam giác $ACC\' \\Rightarrow CC\' = 2OI$.\\\\
    $BB\'D\'D$ là hình thang có $OI$ là đường trung bình $\\Rightarrow OI = \\frac{BB\' + DD\'}{2} = \\frac{%s + %s}{2} = %s$.\\\\
    Vậy $CC\' = %s$.'''
                   % (hinh_ve, str_bb, str_dd, str_oi, str_cc))
    dapan='\\shortans[0]{$%s$}\n'%(str_cc)
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth}\n'
               '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
               '\\loigiai{' + str(loigiai) + '}\n'
               '\\end{ex}\n\\end{minipage}\n\n')
    return content 


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


def bt_dang6_p3_b2_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':


        cases = [
            ('goc', 1, 2, 'trung điểm của $AB$, $AD$ và $SO$'),
            ('ti_le_2_5', 2, 5, 'các điểm thỏa mãn $\\frac{AM}{AB} = \\frac{AN}{AD} = \\frac{SP}{SO} = \\frac{2}{5}$'),
            ('ti_le_3_5', 3, 5, 'các điểm thỏa mãn $\\frac{AM}{AB} = \\frac{AN}{AD} = \\frac{SP}{SO} = \\frac{3}{5}$'),
            ('ti_le_1_3', 1, 3, 'các điểm thỏa mãn $\\frac{AM}{AB} = \\frac{AN}{AD} = \\frac{SP}{SO} = \\frac{1}{3}$'),
            ('ti_le_2_3', 2, 3, 'các điểm thỏa mãn $\\frac{AM}{AB} = \\frac{AN}{AD} = \\frac{SP}{SO} = \\frac{2}{3}$'),
            ('ti_le_3_4', 3, 4, 'các điểm thỏa mãn $\\frac{AM}{AB} = \\frac{AN}{AD} = \\frac{SP}{SO} = \\frac{3}{4}$')
        ]

        selected_case = random.choice(cases)
        case_type, tu_u, mau_u, mo_ta_mnp = selected_case

        # Tính tỉ số đúng SH/SC = (tu_u / mau_u) / 2 = tu_u / (2 * mau_u)
        tu_kq = tu_u
        mau_kq = 2 * mau_u
        val_float = float(tu_kq) / float(mau_kq)

        # Chuyển đổi sang số thập phân, nếu lẻ làm tròn đến hàng phần trăm theo yêu cầu
        val_dec = Decimal(str(val_float)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

        # Định dạng hiển thị số thập phân dùng dấu phẩy
        if val_float == float(val_dec) and str(val_float).replace('.', '').isdigit() and len(str(val_float).split('.')[1]) <= 2:
            kq_str = str(val_float).replace('.', ',')
        else:
            kq_str = str(val_dec).replace('.', ',')

        da = '$%s$' % (kq_str)

        # B4: Tạo các phương án sai khác nhau và tuyệt đối không trùng đáp án đúng
        pool_sai = [
            '0,5', '0,25', '0,75', '0,2', '0,3', '0,4', '0,17', '0,33', '0,38', '0,13', '0,15', '0,35'
        ]
        sai_cands = [s for s in pool_sai if s != kq_str]
        random.shuffle(sai_cands)
        das1 = '$%s$' % (sai_cands[0])
        das2 = '$%s$' % (sai_cands[1])
        das3 = '$%s$' % (sai_cands[2])

        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Hình vẽ TikZ chuẩn 100% theo mẫu (nét 1pt, điểm 1pt, màu black, không raw string)
        hinh_ve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (B) at (0,0);\n'
            '\\coordinate (C) at (5.5,0);\n'
            '\\coordinate (A) at (1.5,1.8);\n'
            '\\coordinate (D) at ($(A)+(C)-(B)$);\n'
            '\\coordinate (S) at (0.8,5.4);\n'
            '\\coordinate (O) at ($(A)!0.5!(C)$);\n'
            '\\coordinate (M) at ($(A)!0.5!(B)$);\n'
            '\\coordinate (N) at ($(A)!0.5!(D)$);\n'
            '\\coordinate (I) at ($(M)!0.5!(N)$);\n'
            '\\coordinate (P) at ($(S)!0.5!(O)$);\n'
            '\\coordinate (H) at ($(S)!0.25!(C)$);\n'
            '\\draw[line width=1pt] (S)--(B)--(C)--(D)--(S)--(C);\n'
            '\\draw[line width=1pt, dashed] (S)--(A)--(B) (A)--(D) (A)--(C) (B)--(D) (S)--(O) (M)--(N) (M)--(P)--(N) (I)--(H);\n'
            '\\fill (A) circle (1pt) node[left] {$A$};\n'
            '\\fill (B) circle (1pt) node[below left] {$B$};\n'
            '\\fill (C) circle (1pt) node[below right] {$C$};\n'
            '\\fill (D) circle (1pt) node[above right] {$D$};\n'
            '\\fill (S) circle (1pt) node[above left] {$S$};\n'
            '\\fill (O) circle (1pt) node[below] {$O$};\n'
            '\\fill (M) circle (1pt) node[below left] {$M$};\n'
            '\\fill (N) circle (1pt) node[above right] {$N$};\n'
            '\\fill (I) circle (1pt) node[below] {$I$};\n'
            '\\fill (P) circle (1pt) node[left] {$P$};\n'
            '\\fill (H) circle (1pt) node[above right] {$H$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )

        # B2: Soạn thảo nội dung câu hỏi và lời giải chi tiết từng bước
        if case_type == 'goc':
            noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành tâm $O$. Gọi $M, N, P$ lần lượt là trung điểm của $AB, AD$ và $SO$. Gọi $H$ là giao điểm của $SC$ với $(MNP)$. Tỉ số $\\frac{SH}{SC}$ bằng bao nhiêu?''')

            loigiai = ('''%s
    Trong mặt phẳng $(ABCD)$, gọi $I$ là giao điểm của $MN$ với $AO$.\\\\
    Ta có: $\\begin{cases} SC \\subset (SAC) \\\\ (SAC) \\cap (MNP) = IP \\\\ \\{H\\} = IP \\cap SC \\end{cases} \\Rightarrow \\{H\\} = SC \\cap (MNP)$.\\\\
    Do $MN$ là đường trung bình của tam giác $ABD$ nên $I$ là trung điểm $AO$. Suy ra $\\frac{AI}{AC} = \\frac{1}{4}$ và $PI$ là đường trung bình của tam giác $OSA$. Do đó: $IP // SA \\Rightarrow IH // SA$.\\\\
    Áp dụng định lí Thales ta có: $\\frac{SH}{SC} = \\frac{AI}{AC} = \\frac{1}{4} = %s$.'''
                       % (hinh_ve, kq_str))
        else:
            phan_so_u_str = '\\frac{%s}{%s}' % (tu_u, mau_u)
            phan_so_kq_str = '\\frac{%s}{%s}' % (tu_kq, mau_kq)

            noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành tâm $O$. Gọi $M, N, P$ lần lượt là %s. Gọi $H$ là giao điểm của $SC$ với $(MNP)$. Tỉ số $\\frac{SH}{SC}$ bằng\\\\
    (kết quả là số thập phân)'''
                             % (mo_ta_mnp))

            loigiai = ('''%s
    Trong mặt phẳng $(ABCD)$, gọi $I$ là giao điểm của $MN$ với $AO$.\\\\
    Ta có: $\\begin{cases} SC \\subset (SAC) \\\\ (SAC) \\cap (MNP) = IP \\\\ \\{H\\} = IP \\cap SC \\end{cases} \\Rightarrow \\{H\\} = SC \\cap (MNP)$.\\\\
    Vì $MN // BD$ nên theo định lí Thales trong tam giác $ABD$ ta có $\\frac{AI}{AO} = \\frac{AM}{AB} = %s$.\\\\
    Vì $O$ là trung điểm của $AC$ nên $\\frac{AI}{AC} = \\frac{1}{2} \\cdot \\frac{AI}{AO} = %s$.\\\\
    Mặt khác $\\frac{OI}{OA} = 1 - %s$ và $\\frac{OP}{OS} = 1 - %s$ suy ra $\\frac{OI}{OA} = \\frac{OP}{OS}$, do đó $PI // SA \\Rightarrow IH // SA$.\\\\
    Áp dụng định lí Thales trong tam giác $SAC$ ta có: $\\frac{SH}{SC} = \\frac{AI}{AC} = %s = %s$.'''
                       % (hinh_ve, phan_so_u_str, phan_so_kq_str, phan_so_u_str, phan_so_u_str, phan_so_kq_str, kq_str))
    dapan='\\shortans[0]{$%s$}\n'%(kq_str)
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth}\n'
               '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
               '\\loigiai{' + str(loigiai) + '}\n'
               '\\end{ex}\n\\end{minipage}\n\n')
    return content 


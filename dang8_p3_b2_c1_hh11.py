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


def bt_dang8_p3_b2_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':

        cases = [
            ('goc', 2, 3, 'trọng tâm của $\\Delta SAB$'),
            ('ti_le_3_4', 3, 4, 'điểm trên trung tuyến $SE$ của $\\Delta SAB$ sao cho $\\frac{SG}{SE} = \\frac{3}{4}$ ($E$ là trung điểm của $AB$)'),
            ('ti_le_3_5', 3, 5, 'điểm trên trung tuyến $SE$ của $\\Delta SAB$ sao cho $\\frac{SG}{SE} = \\frac{3}{5}$ ($E$ là trung điểm của $AB$)'),
            ('ti_le_5_8', 5, 8, 'điểm trên trung tuyến $SE$ của $\\Delta SAB$ sao cho $\\frac{SG}{SE} = \\frac{5}{8}$ ($E$ là trung điểm của $AB$)'),
            ('ti_le_5_6', 5, 6, 'điểm trên trung tuyến $SE$ của $\\Delta SAB$ sao cho $\\frac{SG}{SE} = \\frac{5}{6}$ ($E$ là trung điểm của $AB$)'),
            ('ti_le_4_5', 4, 5, 'điểm trên trung tuyến $SE$ của $\\Delta SAB$ sao cho $\\frac{SG}{SE} = \\frac{4}{5}$ ($E$ là trung điểm của $AB$)')
        ]

        selected_case = random.choice(cases)
        case_type, tu_k, mau_k, mo_ta_g = selected_case

        # Tính x = 1 / (2k - 1) = mau_k / (2 * tu_k - mau_k)
        tu_x = mau_k
        mau_x = 2 * tu_k - mau_k
        val_x = Rational(tu_x, mau_x)
        val_float = float(val_x)

        # Chuyển đổi sang số thập phân, nếu lẻ làm tròn đến hàng phần trăm
        dec_x = Decimal(str(val_float)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        if val_float.is_integer():
            kq_str = str(int(val_float))
        else:
            s_tmp = str(dec_x).rstrip('0').rstrip('.')
            kq_str = s_tmp.replace('.', ',')
            if ',' not in kq_str and not val_float.is_integer():
                kq_str = str(dec_x).replace('.', ',')

        da = '$%s$' % (kq_str)

        # Sinh các phương án sai khác nhau, không trùng đáp án đúng
        sai_cands = set()
        for delta in [-2.0, -1.0, -0.5, 0.5, 1.0, 1.5, 2.0, -0.33, 0.33, 0.67, -0.67]:
            val_sai = val_float + delta
            if val_sai > 0 and abs(val_sai - val_float) > 1e-3:
                d_s = Decimal(str(round(val_sai, 2))).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                if float(val_sai).is_integer():
                    str_s = str(int(val_sai))
                else:
                    str_s = str(d_s).rstrip('0').rstrip('.').replace('.', ',')
                if str_s != kq_str:
                    sai_cands.add('$%s$' % (str_s))

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

        # Hình vẽ TikZ chuẩn 100% như ảnh cung cấp (màu black, nét 1pt, điểm 1pt)
        hinh_ve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (A) at (0,0);\n'
            '\\coordinate (B) at (5,0);\n'
            '\\coordinate (D) at (1.8,-1.5);\n'
            '\\coordinate (C) at (4.2,-1.5);\n'
            '\\coordinate (S) at (1.5,3.2);\n'
            '\\coordinate (E) at ($(A)!0.5!(B)$);\n'
            '\\coordinate (G) at ($(S)!0.6667!(E)$);\n'
            '\\coordinate (I) at ($(A)!0.5!(D)$);\n'
            '\\coordinate (J) at ($(B)!0.5!(C)$);\n'
            '\\coordinate (N) at ($(S)!0.6667!(A)$);\n'
            '\\coordinate (M) at ($(S)!0.6667!(B)$);\n'
            '\\draw[line width=1pt] (S)--(A) (S)--(D) (S)--(C) (S)--(B) (A)--(I)--(D)--(C)--(J)--(B) (N)--(I) (M)--(J) ;\n'
            '\\draw[line width=1pt, dashed] (A)--(B) (I)--(J) (S)--(E) (N)--(M);\n'
            '\\fill (A) circle (1pt) node[left] {$A$};\n'
            '\\fill (B) circle (1pt) node[right] {$B$};\n'
            '\\fill (C) circle (1pt) node[below right] {$C$};\n'
            '\\fill (D) circle (1pt) node[below] {$D$};\n'
            '\\fill (S) circle (1pt) node[above] {$S$};\n'
            '\\fill (E) circle (1pt) node[above right] {$E$};\n'
            '\\fill (G) circle (1pt) node[above right] {$G$};\n'
            '\\fill (I) circle (1pt) node[below left] {$I$};\n'
            '\\fill (J) circle (1pt) node[below right] {$J$};\n'
            '\\fill (N) circle (1pt) node[above left] {$N$};\n'
            '\\fill (M) circle (1pt) node[above right] {$M$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )

        k_str = '\\frac{%s}{%s}' % (tu_k, mau_k)
        k2_str = '\\frac{%s}{%s}' % (2 * tu_k, mau_k) if mau_k != 1 else '%s' % (2 * tu_k)
        cd_ab_str = '\\frac{%s}{%s}' % (mau_x, tu_x) if mau_x != tu_x else '1'

        if case_type == 'goc':
            noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình thang với cạnh đáy $AB$ và $CD$. Gọi $I, J$ lần lượt là trung điểm các cạnh $AD, BC$. Biết $G$ là trọng tâm của $\\Delta SAB$. Mặt phẳng $(IJG)$ cắt $SA, SB$ lần lượt tại $N$ và $M$. Biết rằng $AB = x \\cdot CD$ thì tứ giác $MNIJ$ là hình bình hành. Giá trị của $x$ bằng bao nhiêu?''')

            loigiai = ('''%s
    Ta có: $\\begin{cases} IJ // AB \\\\ \\{G\\} = (IJG) \\cap (SAB) \\end{cases} \\Rightarrow (IJG) \\cap (SAB)$ là đường thẳng qua $G$, song song $AB$ cắt $SA, SB$ lần lượt tại $N, M \\Rightarrow IJMN$ là hình thang.\\\\
    Gọi $E$ là trung điểm của $AB$, vì $G$ là trọng tâm $\\Delta SAB$ nên $\\frac{SG}{SE} = \\frac{2}{3}$.\\\\
    Ta có: $IJ = \\frac{AB + CD}{2}$; $\\frac{MN}{AB} = \\frac{SG}{SE} = \\frac{2}{3} \\Rightarrow MN = \\frac{2}{3} AB$.\\\\
    Để $IJMN$ là hình bình hành thì $MN = IJ \\Leftrightarrow \\frac{AB + CD}{2} = \\frac{2}{3} AB \\Leftrightarrow AB = 3CD$.\\\\
    Vậy $x = %s$.'''
                       % (hinh_ve, kq_str))
        else:
            noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình thang với cạnh đáy $AB$ và $CD$. Gọi $I, J$ lần lượt là trung điểm các cạnh $AD, BC$. Biết $G$ là %s. Mặt phẳng $(IJG)$ cắt $SA, SB$ lần lượt tại $N$ và $M$. Biết rằng $AB = x \\cdot CD$ thì tứ giác $MNIJ$ là hình bình hành. Tìm $x$\\\\
    (kết quả là số thập phân)'''
                             % (mo_ta_g))

            loigiai = ('''%s
    Ta có: $\\begin{cases} IJ // AB \\\\ \\{G\\} = (IJG) \\cap (SAB) \\end{cases} \\Rightarrow (IJG) \\cap (SAB)$ là đường thẳng qua $G$, song song $AB$ cắt $SA, SB$ lần lượt tại $N, M \\Rightarrow IJMN$ là hình thang.\\\\
    Ta có: $IJ = \\frac{AB + CD}{2}$; $\\frac{MN}{AB} = \\frac{SG}{SE} = %s \\Rightarrow MN = %s AB$.\\\\
    Để $IJMN$ là hình bình hành thì $MN = IJ \\Leftrightarrow \\frac{AB + CD}{2} = %s AB \\Leftrightarrow AB + CD = %s AB \\Leftrightarrow CD = %s AB \\Leftrightarrow AB = %s CD$.\\\\
    Vậy $x = %s$.'''
                       % (hinh_ve, k_str, k_str, k_str, k2_str, cd_ab_str, kq_str, kq_str))
    dapan='\\shortans[0]{$%s$}\n'%(kq_str)
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth}\n'
               '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
               '\\loigiai{' + str(loigiai) + '}\n'
               '\\end{ex}\n\\end{minipage}\n\n')
    return content 


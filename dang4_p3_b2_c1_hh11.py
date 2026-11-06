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


def bt_dang4_p3_b2_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        list_cases = [
            (1, 2, 'trung điểm'),
            (1, 3, 'điểm thỏa mãn $\\frac{SM}{SB} = \\frac{SN}{SD} = \\frac{1}{3}$'),
            (2, 3, 'điểm thỏa mãn $\\frac{SM}{SB} = \\frac{SN}{SD} = \\frac{2}{3}$'),
            (1, 4, 'điểm thỏa mãn $\\frac{SM}{SB} = \\frac{SN}{SD} = \\frac{1}{4}$'),
            (3, 4, 'điểm thỏa mãn $\\frac{SM}{SB} = \\frac{SN}{SD} = \\frac{3}{4}$')
        ]

        # Random lựa chọn một trường hợp (mặc định ưu tiên trường hợp gốc tỉ số 1/2)
        selected_case = random.choice(list_cases)
        tu_m, mau_m, mo_ta_mn = selected_case

        # Tính tỉ số SK/SC chính xác
        # SK/SC = m / (2 - m) = (tu_m / mau_m) / (2 - tu_m / mau_m) = tu_m / (2 * mau_m - tu_m)
        tu_kq = tu_m
        mau_kq = 2 * mau_m - tu_m

        ti_so_val = float(tu_kq) / float(mau_kq)
        ti_so_dec = Decimal(str(ti_so_val)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        kq = str(ti_so_dec).replace('.', ',')

        # Tạo các đáp án trắc nghiệm làm tròn đến hàng phần trăm
        da = '$%s$' % (kq)

        # Sinh các phương án sai khác nhau và không trùng với đáp án đúng
        sai_cands = set()
        for delta in [-0.15, -0.10, -0.05, 0.05, 0.10, 0.15, 0.20, -0.20, 0.08, -0.08]:
            val_sai = ti_so_val + delta
            if 0.05 <= val_sai <= 0.95:
                sai_dec = Decimal(str(val_sai)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                sai_str = str(sai_dec).replace('.', ',')
                if sai_str != kq:
                    sai_cands.add('$%s$' % (sai_str))

        sai_list = list(sai_cands)
        random.shuffle(sai_list)
        das1 = sai_list[0]
        das2 = sai_list[1]
        das3 = sai_list[2]

        da_d = '\\True ' + str(da)
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Chuỗi mô tả tỉ số cho lời giải
        phan_so_m_str = '\\frac{%s}{%s}' % (tu_m, mau_m) if mau_m != 1 else '%s' % (tu_m)
        phan_so_kq_str = '\\frac{%s}{%s}' % (tu_kq, mau_kq)

        # Hình vẽ TikZ chuẩn 100% hình gốc
        hinh_ve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (A) at (0,0);\n'
            '\\coordinate (B) at (4.5,-0.5);\n'
            '\\coordinate (D) at (1.8,1.2);\n'
            '\\coordinate (C) at ($(B)+(D)-(A)$);\n'
            '\\coordinate (S) at (1.8,4.5);\n'
            '\\coordinate (O) at ($(A)!0.5!(C)$);\n'
            '\\coordinate (M) at ($(S)!0.5!(B)$);\n'
            '\\coordinate (N) at ($(S)!0.5!(D)$);\n'
            '\\coordinate (H) at ($(S)!0.5!(O)$);\n'
            '\\coordinate (K) at ($(S)!0.3333!(C)$);\n'
            '\\coordinate (E) at ($(K)!0.5!(C)$);\n'
            '\\draw[line width=1pt] (S)--(A) (A)--(B) (B)--(C) (S)--(B) (S)--(C) (M)--(K) (A)--(M);\n'
            '\\draw[line width=1pt, dashed] (S)--(D) (A)--(D) (C)--(D) (A)--(C) (B)--(D) (S)--(O) (M)--(N) (A)--(K) (O)--(E) (N)--(K) (A)--(N);\n'
            '\\fill (A) circle (1pt) node[left] {$A$};\n'
            '\\fill (B) circle (1pt) node[below right] {$B$};\n'
            '\\fill (C) circle (1pt) node[right] {$C$};\n'
            '\\fill (D) circle (1pt) node[above right] {$D$};\n'
            '\\fill (S) circle (1pt) node[above] {$S$};\n'
            '\\fill (O) circle (1pt) node[below] {$O$};\n'
            '\\fill (M) circle (1pt) node[right] {$M$};\n'
            '\\fill (N) circle (1pt) node[left] {$N$};\n'
            '\\fill (H) circle (1pt) node[left] {$H$};\n'
            '\\fill (K) circle (1pt) node[above right] {$K$};\n'
            '\\fill (E) circle (1pt) node[above right] {$E$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )

        if tu_m == 1 and mau_m == 2:
            # Lời giải chi tiết theo đúng từng bước của ảnh gốc
            noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành. Gọi $M$, $N$ lần lượt là trung điểm cạnh $SB$, $SD$. Gọi $K$ là giao điểm của mặt phẳng $(AMN)$ và đường thẳng $SC$. Tỉ số $\\frac{SK}{SC}$ bằng bao nhiêu? (kết quả làm tròn đến hàng phần trăm).''')

            loigiai = ('''%s
    Gọi $O$ là tâm của hình bình hành $ABCD$. Gọi $H = MN \\cap SO$, khi đó $K = SC \\cap AH$.\\\\
    Xét $\\Delta SBD$ có $MN$ là đường trung bình nên ta có $\\frac{SH}{SO} = \\frac{SM}{SB} = \\frac{1}{2}$.\\\\
    Suy ra $H$ là trung điểm $SO$.\\\\
    Gọi $E$ là trung điểm $CK$, xét tam giác $AKC$ có $OE$ là đường trung bình nên $OE // HK$.\\\\
    Xét $\\Delta SOE$ có $H$ là trung điểm của $SO$ và $HK // OE$ nên $HK$ là đường trung bình, suy ra $K$ là trung điểm của $SE$.\\\\
    Vậy tỉ số $\\frac{SK}{SC} = \\frac{1}{3} \\approx %s$.'''
                       % (hinh_ve, kq))
        else:
            # Dạng tổng quát khi random tỉ số
            noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành. Gọi $M$, $N$ lần lượt là các %s tương ứng trên cạnh $SB$, $SD$. Gọi $K$ là giao điểm của mặt phẳng $(AMN)$ và đường thẳng $SC$. Tỉ số $\\frac{SK}{SC}$ bằng\\\\
    (kết quả làm tròn đến hàng phần trăm)'''
                             % (mo_ta_mn))

            loigiai = ('''%s
    Gọi $O$ là tâm của hình bình hành $ABCD$. Gọi $H = MN \\cap SO$, khi đó $K = SC \\cap AH$.\\\\
    Vì $MN // BD$ nên theo định lý Thales trong $\\Delta SBD$ ta có $\\frac{SH}{SO} = \\frac{SM}{SB} = %s$.\\\\
    Áp dụng định lý Menelaus trong $\\Delta SOC$ với cát tuyến $A-H-K$, ta có:\\\\
    $\\frac{AC}{AO} \\cdot \\frac{OH}{HS} \\cdot \\frac{SK}{KC} = 1$.\\\\
    Vì $O$ là trung điểm $AC$ nên $\\frac{AC}{AO} = 2$. Suy ra $\\frac{SK}{KC} = \\frac{1}{2} \\cdot \\frac{SH}{OH} = \\frac{%s}{2 \\cdot (%s - %s)} = \\frac{%s}{%s}$.\\\\
    Từ đó suy ra $\\frac{SK}{SC} = %s \\approx %s$.'''
                       % (hinh_ve, phan_so_m_str, tu_m, mau_m, tu_m, tu_m, 2 * (mau_m - tu_m), phan_so_kq_str, kq))
    dapan='\\shortans[0]{$%s$}\n'%(kq)
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth}\n'
               '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
               '\\loigiai{' + str(loigiai) + '}\n'
               '\\end{ex}\n\\end{minipage}\n\n')
    return content 


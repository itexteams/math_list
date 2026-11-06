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


def bt_dang5_p3_b2_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':

        cases = [
            ('goc', 2, 1),           # Trọng tâm: SN/NF = 2/1 => SI/CD = 1.0 -> 1 hoặc 1,0
            ('ti_le_3_4', 3, 1),     # SN/SF = 3/4 => SN/NF = 3/1 => SI/CD = 1.5
            ('ti_le_1_2', 1, 1),     # M, N là trung điểm SE, SF => SN/NF = 1/1 => SI/CD = 0.5
            ('ti_le_4_5', 4, 1),     # SN/SF = 4/5 => SN/NF = 4/1 => SI/CD = 2.0
            ('ti_le_3_5', 3, 2),     # SN/SF = 3/5 => SN/NF = 3/2 => SI/CD = 0.75
            ('ti_le_5_6', 5, 1),     # SN/SF = 5/6 => SN/NF = 5/1 => SI/CD = 2.5
        ]

        selected_case = random.choice(cases)

        # TikZ code hình vẽ 100% theo mẫu (độ dày 1pt, điểm 1pt, màu black, không dùng raw string)
        hinh_ve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            '\\coordinate (B) at (0,0);\n'
            '\\coordinate (C) at (5,0);\n'
            '\\coordinate (A) at (2,1.6);\n'
            '\\coordinate (D) at ($(A)+(C)-(B)$);\n'
            '\\coordinate (E) at ($(A)!0.5!(B)$);\n'
            '\\coordinate (F) at ($(C)!0.5!(D)$);\n'
            '\\coordinate (S) at (2.6,4.6);\n'
            '\\coordinate (M) at ($(S)!0.6667!(E)$);\n'
            '\\coordinate (N) at ($(S)!0.6667!(F)$);\n'
            '\\coordinate (I) at ($(C)!3!(N)$);\n'
            '\\draw[line width=1pt] (B)--(C)--(D) (S)--(B) (S)--(C) (S)--(D) (C)--(F) (C)--(I) (S)--(I);\n'
            '\\draw[line width=1pt, dashed] (A)--(B) (A)--(D) (S)--(A) (S)--(E) (S)--(F) (B)--(I) (E)--(F) (M)--(N);\n'
            '\\fill (A) circle (1pt) node[left] {$A$};\n'
            '\\fill (B) circle (1pt) node[below left] {$B$};\n'
            '\\fill (C) circle (1pt) node[below] {$C$};\n'
            '\\fill (D) circle (1pt) node[right] {$D$};\n'
            '\\fill (E) circle (1pt) node[below left] {$E$};\n'
            '\\fill (F) circle (1pt) node[below right] {$F$};\n'
            '\\fill (S) circle (1pt) node[above left] {$S$};\n'
            '\\fill (M) circle (1pt) node[right] {$M$};\n'
            '\\fill (N) circle (1pt) node[right] {$N$};\n'
            '\\fill (I) circle (1pt) node[above right] {$I$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}'
        )

        sn_nf_tu = selected_case[1]
        sn_nf_mau = selected_case[2]

        # Giá trị đúng dạng phân số và số thập phân
        val_rat = Rational(sn_nf_tu, 2 * sn_nf_mau)
        val_float = float(val_rat)
        val_dec = Decimal(str(val_float)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

        # Định dạng số thập phân dùng dấu phẩy
        if val_float.is_integer():
            kq_str = str(int(val_float))
        else:
            kq_str = str(val_dec).rstrip('0').rstrip('.').replace('.', ',')
            if ',' not in kq_str and not val_float.is_integer():
                kq_str = str(val_dec).replace('.', ',')

        da = '$%s$' % (kq_str)

        # Sinh các phương án sai dạng số thập phân, đảm bảo khác biệt hoàn toàn với đáp án đúng
        sai_cands = set()
        for delta in [-1.5, -1.0, -0.5, -0.25, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 2.0]:
            val_sai = val_float + delta
            if val_sai > 0 and abs(val_sai - val_float) > 1e-4:
                s_dec = Decimal(str(round(val_sai, 2))).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                if float(val_sai).is_integer():
                    s_str = str(int(val_sai))
                else:
                    s_str = str(s_dec).rstrip('0').rstrip('.').replace('.', ',')
                if s_str != kq_str:
                    sai_cands.add('$%s$' % (s_str))

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

        if selected_case[0] == 'goc':
            noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình chữ nhật. Gọi $M,N$ theo thứ tự là trọng tâm $\\Delta SAB$ và $\\Delta SCD$. Gọi $I$ là giao điểm của các đường thẳng $BM;CN$. Khi đó tỉ số $\\frac{SI}{CD}$ bằng bao nhiêu?''')

            loigiai = ('''%s
    Gọi $E$ và $F$ lần lượt là trung điểm $AB$ và $CD$.\\\\
    Ta có $\\{I\\} = BM \\cap CN \\Rightarrow \\begin{cases} I \\in BM \\subset (SAB) \\\\ I \\in CN \\subset (SCD) \\end{cases} \\Rightarrow I \\in (SAB) \\cap (SCD)$.\\\\
    Mà $S \\in (SAB) \\cap (SCD)$. Do đó $(SAB) \\cap (SCD) = SI$.\\\\
    Ta có: $\\begin{cases} AB // CD \\\\ AB \\subset (SAB) \\\\ CD \\subset (SCD) \\\\ (SAB) \\cap (SCD) = SI \\end{cases} \\Rightarrow SI // AB // CD$. Vì $SI // CD$ nên $SI // CF$.\\\\
    Theo định lý Ta -- let ta có: $\\frac{SI}{CF} = \\frac{SN}{NF} = 2 \\Rightarrow SI = 2CF = CD \\Rightarrow \\frac{SI}{CD} = %s$.'''
                       % (hinh_ve, kq_str))
        else:
            sn_sf_frac = Rational(sn_nf_tu, sn_nf_tu + sn_nf_mau)
            str_ti_le_de = '\\frac{%s}{%s}' % (latex(sn_sf_frac.p), latex(sn_sf_frac.q))
            str_sn_nf = '\\frac{%s}{%s}' % (sn_nf_tu, sn_nf_mau) if sn_nf_mau != 1 else '%s' % (sn_nf_tu)

            noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình chữ nhật. Gọi $E, F$ lần lượt là trung điểm của $AB$ và $CD$. Lấy các điểm $M, N$ tương ứng trên các đoạn thẳng $SE, SF$ sao cho $\\frac{SM}{SE} = \\frac{SN}{SF} = %s$. Gọi $I$ là giao điểm của các đường thẳng $BM;CN$. Khi đó tỉ số $\\frac{SI}{CD}$ bằng'''
                             % (str_ti_le_de))

            loigiai = ('''%s
    Gọi $E$ và $F$ lần lượt là trung điểm $AB$ và $CD$.\\\\
    Ta có $\\{I\\} = BM \\cap CN \\Rightarrow \\begin{cases} I \\in BM \\subset (SAB) \\\\ I \\in CN \\subset (SCD) \\end{cases} \\Rightarrow I \\in (SAB) \\cap (SCD)$.\\\\
    Mà $S \\in (SAB) \\cap (SCD)$. Do đó $(SAB) \\cap (SCD) = SI$.\\\\
    Ta có: $\\begin{cases} AB // CD \\\\ AB \\subset (SAB) \\\\ CD \\subset (SCD) \\\\ (SAB) \\cap (SCD) = SI \\end{cases} \\Rightarrow SI // AB // CD$. Vì $SI // CD$ nên $SI // CF$.\\\\
    Vì $\\frac{SN}{SF} = %s$ nên $\\frac{SN}{NF} = %s$.\\\\
    Theo định lý Ta -- let ta có: $\\frac{SI}{CF} = \\frac{SN}{NF} = %s \\Rightarrow SI = %s \\cdot CF = %s \\cdot \\frac{CD}{2} \\Rightarrow \\frac{SI}{CD} = %s$.'''
                       % (hinh_ve, str_ti_le_de, str_sn_nf, str_sn_nf, str_sn_nf, str_sn_nf, kq_str))
    dapan='\\shortans[0]{$%s$}\n'%(kq_str)
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth}\n'
               '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
               '\\loigiai{' + str(loigiai) + '}\n'
               '\\end{ex}\n\\end{minipage}\n\n')
    return content 


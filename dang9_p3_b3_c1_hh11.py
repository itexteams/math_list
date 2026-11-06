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


def bt_dang9_p3_b3_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # B3: Random bài toán
        # Gọi M là điểm trên BC sao cho MB/MC = p / q.
        # Trong bài gốc: M là trung điểm BC => p = 1, q = 1.
        # Ta xét tổng quát tỉ số: MB/MC = p (với p là số nguyên từ 1 đến 3 để đề bài tự nhiên, hoặc M là trung điểm khi p = 1).
        p = random.choice([1, 2, 3])

        tu_so = 3 + p
        mau_so = 3 * (p + 1)
        ucln = math.gcd(tu_so, mau_so)
        m = tu_so // ucln
        n = mau_so // ucln

        # Giá trị m * n luôn là số nguyên
        kq_val = m * n
        kq = str(kq_val)

        # B4: Điều chỉnh các phương án sai không trùng với đáp án đúng
        s_set = set()
        offsets = [1, 2, 3, 4, -1, -2, -3, -4, 5, 6, -5]
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

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        # Đưa các đáp án vào danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Tỷ lệ các điểm phục vụ vẽ hình TikZ
        t_bm = p / (p + 1)
        t_se = m / n

        # B1 & B2: Đề bài
        if p == 1:
            mo_ta_m = 'Gọi $G$ là trọng tâm của tam giác $ABC$'
            loigiai_m = 'Gọi $M$ là trung điểm của $BC$, $F$ là giao điểm của $AM$ và $CD$ trong mặt phẳng $(ABCD)$. \\\\'
            loigiai_talet = 'Theo định lý Talet, ta có: $\\frac{MA}{MF} = \\frac{MB}{MC} = 1 \\Rightarrow MA = MF \\Rightarrow M$ là trung điểm của $AF$ \\\\'
            loigiai_ag_af = '$\\Rightarrow \\frac{AG}{AF} = \\frac{AG}{2AM} = \\frac{1}{3}$'
            frac_ae_as = '\\frac{1}{3}'
        else:
            mo_ta_m = 'Gọi $G$ là điểm trên trung tuyến $AM$ của tam giác $ABC$ thỏa mãn $AG = \\frac{2}{3}AM$, với $M$ thuộc cạnh $BC$ sao cho $MB = %s MC$' % (p)
            loigiai_m = 'Gọi $F$ là giao điểm của $AM$ và $CD$ trong mặt phẳng $(ABCD)$. \\\\'
            loigiai_talet = 'Theo định lý Talet, ta có: $\\frac{MA}{MF} = \\frac{MB}{MC} = %s \\Rightarrow MA = %s MF \\Rightarrow AF = \\frac{%s}{%s} AM$. \\\\' % (p, p, p + 1, p)
            frac_ag_af_val = Rational(2 * p, 3 * (p + 1))
            loigiai_ag_af = '$\\Rightarrow \\frac{AG}{AF} = %s$' % (latex(frac_ag_af_val))
            frac_ae_as = latex(frac_ag_af_val)

        noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành. %s và $E$ là điểm thuộc cạnh $SA$ thỏa mãn $SE = \\frac{m}{n} \\cdot SA$ với $\\frac{m}{n}$ là phân số tối giản. Biết rằng $GE$ song song với mặt phẳng $(SCD)$. Giá trị của $m \\cdot n$ bằng bao nhiêu?'''
                         % (mo_ta_m))

        # Hình vẽ TikZ chuẩn 100% như mẫu ảnh, đường nét 1pt, điểm 1pt, màu black
        tikz_code = '''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\coordinate (B) at (0,0);
        \\coordinate (A) at (1.8,1.8);
        \\coordinate (C) at (5.2,0);
        \\coordinate (D) at ($(A)+(C)-(B)$);
        \\coordinate (S) at (2.7,4.5);
        \\coordinate (M) at ($(B)!''' + str(round(t_bm, 3)) + '''!(C)$);
        \\coordinate (F) at (intersection of A--M and C--D);
        \\coordinate (G) at ($(A)!0.667!(M)$);
        \\coordinate (E) at ($(S)!''' + str(round(t_se, 3)) + '''!(A)$);
        \\draw[line width=1pt] (S)--(B)--(M) (C)--(D)--(S)--(F)--(C) (S)--(C) (M)--(F);
        \\draw[line width=1pt, dashed] (A)--(B) (A)--(D) (S)--(A) (A)--(C) (A)--(M) (B)--(C) (E)--(G) (S)--(E);
        \\fill (S) circle (1pt) node[above left] {$S$};
        \\fill (A) circle (1pt) node[above left] {$A$};
        \\fill (B) circle (1pt) node[below left] {$B$};
        \\fill (C) circle (1pt) node[below right] {$C$};
        \\fill (D) circle (1pt) node[right] {$D$};
        \\fill (M) circle (1pt) node[below] {$M$};
        \\fill (F) circle (1pt) node[below left] {$F$};
        \\fill (G) circle (1pt) node[below left] {$G$};
        \\fill (E) circle (1pt) node[left] {$E$};
    \\end{tikzpicture}
    \\end{center}'''

        # Lời giải chi tiết
        loigiai = ('''%s
    %s
    %s
    %s \\\\
    Ta có: \\\\
    $\\begin{cases} GE \\subset (SAF) \\\\ GE // (SCD) \\\\ (SAF) \\cap (SCD) = SF \\end{cases} \\Rightarrow GE // SF$ \\\\
    $\\Rightarrow \\frac{AE}{AS} = \\frac{AG}{AF} = %s \\Rightarrow AE = %s AS$ \\\\
    $\\Rightarrow SE = \\frac{%s}{%s} SA \\Rightarrow \\frac{m}{n} = \\frac{%s}{%s} \\Rightarrow m \\cdot n = %s$.'''
                   % (tikz_code,
                      loigiai_m,
                      loigiai_talet,
                      loigiai_ag_af,
                      frac_ae_as, frac_ae_as,
                      latex(m), latex(n), latex(m), latex(n),
                      latex(kq_val)))
    dapan='\\shortans[0]{$%s$}\n'%(latex(kq_val))
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
               '\\loigiai{' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content


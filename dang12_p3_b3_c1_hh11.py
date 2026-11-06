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


def bt_dang12_p3_b3_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        r = random.choice([2, 3, 4, 5])

        val_frac = Rational(1, r + 1)

        # Tính giá trị làm tròn đến hàng phần trăm (2 chữ số thập phân)
        kq_float = float(val_frac)
        kq_dec = Decimal(str(kq_float)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        kq = str(kq_dec).replace('.', ',')

        # B4: Điều chỉnh các phương án sai không trùng với đáp án đúng
        s_set = set()
        offsets = [Decimal('0.05'), Decimal('-0.05'), Decimal('0.10'), Decimal('-0.10'),
                   Decimal('0.15'), Decimal('-0.15'), Decimal('0.20'), Decimal('-0.20')]
        for off in offsets:
            val = kq_dec + off
            if val > 0 and val < 1 and val != kq_dec:
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

        # Tỉ lệ điểm I trên đoạn AB: BI = 1/(r+1) AB
        t_bi = 1.0 / (r + 1)

        # B1 & B2: Đề bài
        if r == 1:
            ti_le_str = 'AI = IB'
        else:
            ti_le_str = 'AI = %s IB' % (r)

        noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành, $G$ là trọng tâm tam giác $SCD$, $I$ là điểm thuộc cạnh $AB$ thỏa $%s$. Đường thẳng $BG$ cắt mặt phẳng $(SIC)$ và mặt phẳng $(SAD)$ lần lượt tại $K, H$. Tỉ số $\\frac{BK}{BH}$ bằng bao nhiêu? (kết quả làm tròn đến hàng phần trăm).'''
                         % (ti_le_str))

        # Hình vẽ TikZ vẽ 100% như ảnh cung cấp, nét 1pt, điểm 1pt, màu black
        tikz_code = '''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\coordinate (B) at (0,0);
        \\coordinate (C) at (4.8,0);
        \\coordinate (A) at (2,1.8);
        \\coordinate (D) at ($(A)+(C)-(B)$);
        \\coordinate (S) at (2.9,5.2);
        \\coordinate (E) at ($(C)!0.5!(D)$);
        \\coordinate (G) at ($(S)!0.667!(E)$);
        \\coordinate (M) at ($(S)!0.5!(C)$);
        \\coordinate (N) at ($(S)!0.5!(D)$);
        \\coordinate (I) at ($(B)!''' + str(round(t_bi, 3)) + '''!(A)$);
        \\coordinate (H) at (intersection of B--G and A--N);
        \\coordinate (K) at (intersection of B--G and I--M);
        \\draw[line width=1pt] (S)--(B)--(C)--(D)--(S)--(C) (S)--(M) (S)--(E) (B)--(K)--(G)--(H) (N)--(H);
        \\draw[line width=1pt, dashed] (A)--(B) (A)--(D) (S)--(A) (S)--(I) (I)--(C) (I)--(M) (A)--(N) (A)--(M) (A)--(G);
        \\fill (S) circle (1pt) node[above] {$S$};
        \\fill (B) circle (1pt) node[below left] {$B$};
        \\fill (C) circle (1pt) node[below] {$C$};
        \\fill (D) circle (1pt) node[below right] {$D$};
        \\fill (A) circle (1pt) node[left] {$A$};
        \\fill (E) circle (1pt) node[below right] {$E$};
        \\fill (G) circle (1pt) node[above right] {$G$};
        \\fill (M) circle (1pt) node[below left] {$M$};
        \\fill (N) circle (1pt) node[above] {$N$};
        \\fill (I) circle (1pt) node[left] {$I$};
        \\fill (K) circle (1pt) node[below] {$K$};
        \\fill (H) circle (1pt) node[right] {$H$};
    \\end{tikzpicture}
    \\end{center}'''

        # Lời giải chi tiết
        loigiai = ('''%s
    Ta có $BG, IM, AN \\subset (ABMN)$ và $BG$ không song song với $IM, AN$. \\\\
    Gọi $K = BG \\cap IM, IM \\subset (SIC) \\Rightarrow K = BG \\cap (SIC)$. \\\\
    Gọi $H = BG \\cap AN, AN \\subset (SAD) \\Rightarrow H = BG \\cap (SAD)$. \\\\
    Xét tam giác $ABH$ ta có $IK // AH \\Rightarrow \\frac{BK}{BH} = \\frac{BI}{BA} = %s \\approx %s$.'''
                   % (tikz_code,
                      latex(val_frac),
                      kq))
    dapan='\\shortans[0]{$%s$}\n'%(kq)
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
               '\\loigiai{' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content


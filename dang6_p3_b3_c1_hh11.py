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


def bt_dang6_p3_b3_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # B3: Random độ dài các cạnh AB và CD
        ab = random.choice([4, 5, 6, 7, 8, 9, 10])
        cd = random.choice([val for val in [4, 5, 6, 7, 8, 9, 10] if val != ab])

        # Cạnh hình thoi MK: MK/ab + MK/cd = 1 => MK = (ab * cd) / (ab + cd)
        mk_exact = Rational(ab * cd, ab + cd)
        mk_num = float(mk_exact)

        # Làm tròn đến hàng phần trăm (2 chữ số thập phân) theo ROUND_HALF_UP
        kq_dec = Decimal(str(mk_num)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        kq = str(kq_dec).replace('.', ',')

        # B4: Tạo các phương án sai ngẫu nhiên, không trùng với đáp án đúng
        s_set = set()
        offsets = [Decimal('0.05'), Decimal('-0.05'), Decimal('0.10'), Decimal('-0.10'),
                   Decimal('0.15'), Decimal('-0.15'), Decimal('0.20'), Decimal('-0.20')]
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

        # B1 & B2: Đề bài
        noidungcauhoi = ('''Cho tứ diện $ABCD$ có $AB = %s$, $CD = %s$. Mặt phẳng $(P)$ song song với $AB$, $CD$ cắt các cạnh $BC, BD, AD, AC$ lần lượt tại $M, N, I, K$. Khi tứ giác $MNIK$ là một hình thoi, thì cạnh của hình thoi đó bằng bao nhiêu? (kết quả làm tròn đến hàng phần trăm).'''
                         % (latex(ab), latex(cd)))

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        # Đưa các đáp án vào danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Tỉ lệ điểm K trên cạnh AC: CK/AC = MK/ab = cd/(ab+cd) => AK/AC = ab/(ab+cd)
        t_val = round(float(Rational(cd, ab + cd)), 2)

        # Hình vẽ TikZ vẽ chuẩn theo ảnh mẫu, màu black
        tikz_code = '''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\coordinate (B) at (0,0);
        \\coordinate (C) at (1.8,-1.7);
        \\coordinate (D) at (5.8,0);
        \\coordinate (A) at (2,3.8);
        \\coordinate (M) at ($(B)!''' + str(t_val) + '''!(C)$);
        \\coordinate (K) at ($(A)!''' + str(1 - t_val) + '''!(C)$);
        \\coordinate (N) at ($(B)!''' + str(t_val) + '''!(D)$);
        \\coordinate (I) at ($(A)!''' + str(1 - t_val) + '''!(D)$);
        \\draw[line width=1pt] (A)--(B)--(C)--(D)--(A)--(C) (M)--(K)--(I);
        \\draw[line width=1pt, dashed] (B)--(D) (M)--(N)--(I);
        \\fill (A) circle (1pt) node[above] {$A$};
        \\fill (B) circle (1pt) node[left] {$B$};
        \\fill (C) circle (1pt) node[below] {$C$};
        \\fill (D) circle (1pt) node[right] {$D$};
        \\fill (M) circle (1pt) node[below left] {$M$};
        \\fill (K) circle (1pt) node[left] {$K$};
        \\fill (N) circle (1pt) node[below] {$N$};
        \\fill (I) circle (1pt) node[above right] {$I$};
    \\end{tikzpicture}
    \\end{center}'''

        # Tính toán chi tiết các biểu thức phụ cho lời giải
        sum_cd_ab = ab + cd
        prod_ab_cd = ab * cd

        # B2: Lời giải chi tiết (bỏ chữ Cách 1, dùng // cho song song, định dạng %s)
        loigiai = ('''%s
    Giả sử một mặt phẳng song song với $AB$ và $CD$ cắt tứ diện $ABCD$ theo một thiết diện là hình thoi $MNIK$ như hình vẽ trên. Khi đó ta có: $\\begin{cases} MK // AB // IN \\\\ MN // CD // IK \\\\ MK = KI \\end{cases}$. \\\\
    Theo định lí Ta-lét ta có: $\\begin{cases} \\frac{MK}{AB} = \\frac{CK}{AC} \\\\ \\frac{KI}{CD} = \\frac{AK}{AC} \\end{cases} \\Rightarrow \\begin{cases} \\frac{MK}{%s} = \\frac{AC - AK}{AC} \\\\ \\frac{KI}{%s} = \\frac{AK}{AC} \\end{cases}$ \\\\
    $\\Rightarrow \\frac{MK}{%s} = 1 - \\frac{AK}{AC} \\Rightarrow \\frac{MK}{%s} = 1 - \\frac{KI}{%s} \\Rightarrow \\frac{MK}{%s} = 1 - \\frac{MK}{%s} \\Leftrightarrow \\frac{%s}{%s} MK = 1 \\Leftrightarrow MK = \\frac{%s}{%s} \\approx %s$. \\\\
    Vậy hình thoi có cạnh bằng $%s$.'''
                   % (tikz_code,
                      latex(ab), latex(cd),
                      latex(ab), latex(ab), latex(cd), latex(ab), latex(cd),
                      latex(sum_cd_ab), latex(prod_ab_cd),
                      latex(prod_ab_cd), latex(sum_cd_ab),
                      kq, kq))
    dapan='\\shortans[0]{$%s$}\n'%(kq)
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
               '\\loigiai{' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content


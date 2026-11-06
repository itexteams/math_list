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


def bt_dang17_p3_b3_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':

        a_val = random.choice([3, 4, 5, 6, 7, 8, 9])

        # Các giá trị hình học tương ứng
        mn_exact = Rational(2 * a_val, 3)
        bm_exact = Rational(a_val, 3)

        # Tính toán diện tích tam giác AMN
        s_exact = Rational(a_val**2, 9) * sp.sqrt(6)
        s_float = float(s_exact.evalf())

        # Làm tròn đến hàng phần chục (1 chữ số thập phân) theo Decimal và ROUND_HALF_UP
        kq_dec = Decimal(str(s_float)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        kq = str(kq_dec).replace('.', ',')

        # B4: Điều chỉnh các phương án sai không trùng với đáp án đúng
        s_set = set()
        offsets = [Decimal('0.3'), Decimal('-0.3'), Decimal('0.5'), Decimal('-0.5'),
                   Decimal('0.7'), Decimal('-0.7'), Decimal('1.0'), Decimal('-1.0'),
                   Decimal('1.2'), Decimal('-1.2'), Decimal('1.5'), Decimal('-1.5')]
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
        noidungcauhoi = ('''Cho tứ diện đều $ABCD$ cạnh $%s$, $G$ là trọng tâm tam giác $BDC$. Mặt phẳng qua $A, G$ và song song với $BC$ cắt $DB, DC$ lần lượt tại $M, N$. Diện tích tam giác $AMN$ bằng bao nhiêu? (kết quả làm tròn đến hàng phần chục).'''
                         % (latex(a_val)))

        # Hình vẽ TikZ vẽ 100% như ảnh cung cấp, nét 1pt, điểm 1pt, màu black
        tikz_code = '''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\coordinate (A) at (0,0);
        \\coordinate (B) at (3.5,-1.7);
        \\coordinate (C) at (5.4,0);
        \\coordinate (D) at (2.4,4.2);
        \\coordinate (M) at ($(D)!0.667!(B)$);
        \\coordinate (N) at ($(D)!0.667!(C)$);
        \\coordinate (G) at ($(M)!0.5!(N)$);
        \\coordinate (E) at ($(B)!0.5!(C)$);
        \\draw[line width=1pt] (D)--(A)--(B)--(D)--(C)--(D) (D)--(M) (M)--(A) (M)--(G)--(N);
        \\draw[line width=1pt, dashed] (A)--(C) (A)--(N) (A)--(G) (D)--(E);
        \\fill (D) circle (1pt) node[above left] {$D$};
        \\fill (A) circle (1pt) node[below left] {$A$};
        \\fill (B) circle (1pt) node[below] {$B$};
        \\fill (C) circle (1pt) node[right] {$C$};
        \\fill (M) circle (1pt) node[left] {$M$};
        \\fill (N) circle (1pt) node[right] {$N$};
        \\fill (G) circle (1pt) node[above right] {$G$};
    \\end{tikzpicture}
    \\end{center}'''

        # Biểu thức tính toán chi tiết cho lời giải
        val_am_squared = Rational(7 * a_val**2, 9)
        val_ag_squared = Rational(6 * a_val**2, 9)
        am_expr = sp.sqrt(val_am_squared)
        ag_expr = sp.sqrt(val_ag_squared)

        loigiai = ('''%s
    Gọi $(\\alpha)$ là mặt phẳng qua $A, G$ và song song với $BC$. \\\\
    Vì $(\\alpha)$ và $(BCD)$ có $G$ chung, $(\\alpha) // BC$, $BC \\subset (BCD)$ nên giao tuyến của $(\\alpha)$ và $(BCD)$ là đường thẳng đi qua $G$ và song song với $BC$ cắt $DB, DC$ lần lượt tại $M, N$. \\\\
    Vì tứ diện $ABCD$ đều cạnh $%s$, $G$ là trọng tâm tam giác $BDC$ nên: \\\\
    $MN = \\frac{2}{3} BC = \\frac{2 \\cdot %s}{3} = %s, BM = \\frac{%s}{3} = %s$. \\\\
    $AM = AN = \\sqrt{%s^2 + %s^2 - 2 \\cdot %s \\cdot %s \\cdot \\cos 60^\\circ} = %s, AG = %s$. \\\\
    Vậy diện tích tam giác $AMN$ là: $S = \\frac{1}{2} \\cdot AG \\cdot MN = \\frac{1}{2} \\cdot %s \\cdot %s = %s \\approx %s$.'''
                   % (tikz_code,
                      latex(a_val),
                      latex(a_val), latex(mn_exact), latex(a_val), latex(bm_exact),
                      latex(a_val), latex(bm_exact), latex(a_val), latex(bm_exact), latex(am_expr), latex(ag_expr),
                      latex(ag_expr), latex(mn_exact), latex(s_exact), kq))
    dapan='\\shortans[0]{$%s$}\n'%(kq)
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) +dapan+
               '\\loigiai{' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content


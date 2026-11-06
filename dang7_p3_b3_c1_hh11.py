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


def bt_dang7_p3_b3_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':

        m = random.choice([1, 2, 3])

        val_frac = Rational(m + 1, m + 2)
        bi_bd_frac = Rational(1, m + 2)

        # Tính giá trị làm tròn đến hàng phần trăm (2 chữ số thập phân)
        kq_float = float(val_frac)
        kq_dec = Decimal(str(kq_float)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        kq = str(kq_dec).replace('.', ',')

        # B4: Tạo các phương án sai ngẫu nhiên, không trùng với đáp án đúng
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

        # Tỉ lệ điểm M trên cạnh BC: BM = 1/(m+1) BC
        t_bm = 1.0 / (m + 1)
        t_bi = 1.0 / (m + 2)
        t_bn = 1.0 - float(val_frac)  # BN/BS = 1 - SN/SB = 1 / (m + 2)

        # B1 & B2: Đề bài
        if m == 1:
            mo_ta_m = 'Gọi $M$ là trung điểm cạnh $BC$'
            giai_thich_i = 'Ta có $I$ là trọng tâm tam giác $ABC$.'
        else:
            mo_ta_m = 'Gọi $M$ là điểm trên cạnh $BC$ sao cho $MC = %s MB$' % (m)
            giai_thich_i = 'Theo định lí Menelaus cho tam giác $BCD$ có cát tuyến qua $A, I, M$, ta suy ra:'

        noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành. %s, $(\\alpha)$ là mặt phẳng qua $A, M$ và song song với $SD$. Mặt phẳng $(\\alpha)$ cắt $SB$ tại $N$, tỉ số $\\frac{SN}{SB}$ bằng bao nhiêu? (kết quả làm tròn đến hàng phần trăm).'''
                         % (mo_ta_m))

        # Hình vẽ TikZ chuẩn 100% theo phong cách mẫu yêu cầu
        tikz_code = '''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\coordinate (B) at (0,0);
        \\coordinate (A) at (2.2,1.8);
        \\coordinate (C) at (5.5,0);
        \\coordinate (D) at ($(A)+(C)-(B)$);
        \\coordinate (S) at (2.8,4.6);
        \\coordinate (M) at ($(B)!''' + str(round(t_bm, 3)) + '''!(C)$);
        \\coordinate (I) at (intersection of A--M and B--D);
        \\coordinate (N) at ($(B)!''' + str(round(t_bi, 3)) + '''!(S)$);
        \\draw[line width=1pt] (S)--(B)--(C)--(D)--(S)--(C);
        \\draw[line width=1pt, dashed] (S)--(A)--(D) (A)--(B) (B)--(D) (A)--(M) (I)--(N);
        \\fill (S) circle (1pt) node[above] {$S$};
        \\fill (A) circle (1pt) node[above left] {$A$};
        \\fill (B) circle (1pt) node[left] {$B$};
        \\fill (C) circle (1pt) node[below] {$C$};
        \\fill (D) circle (1pt) node[right] {$D$};
        \\fill (M) circle (1pt) node[below] {$M$};
        \\fill (I) circle (1pt) node[below right] {$I$};
        \\fill (N) circle (1pt) node[left] {$N$};
    \\end{tikzpicture}
    \\end{center}'''

        # Lời giải chi tiết
        loigiai = ('''%s
    Gọi $I$ là giao điểm của $AM$ và $BD$. %s \\\\
    Suy ra: $\\frac{BI}{BD} = %s$; $\\frac{ID}{BD} = %s$. \\\\
    Ta có: $(\\alpha)$ và mặt phẳng $(SBD)$ có chung điểm $I$, $(\\alpha) // SD$, $SD \\subset (SBD)$ nên giao tuyến của $(\\alpha)$ và mặt phẳng $(SBD)$ là đường thẳng qua $I$ song song với $SD$ cắt $SB$ tại $N$. \\\\
    Vậy $\\frac{SN}{SB} = \\frac{ID}{BD} = %s \\approx %s$.'''
                   % (tikz_code,
                      giai_thich_i,
                      latex(bi_bd_frac), latex(val_frac),
                      latex(val_frac), kq))
    dapan='\\shortans[0]{$%s$}\n'%(kq)
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
               '\\loigiai{' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content


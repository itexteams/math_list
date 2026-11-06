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


def bt_dang9_p3_b1_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Random tỷ lệ a/b của các điểm chia cạnh
        pairs = [(1, 2), (1, 3), (2, 3), (3, 4), (1, 4)]
        a, b = random.choice(pairs)

        # Chuỗi điều kiện đề bài thay đổi tùy theo tỷ lệ
        if a == 1 and b == 2:
            cond_IJ = "$I, J$ lần lượt là trung điểm của $SA$ và $SD$"
            cond_PQ = "$P, Q$ là trung điểm của $SB, SC$"
        else:
            cond_IJ = "$\\frac{SI}{SA} = \\frac{SJ}{SD} = \\frac{%s}{%s}$" % (a, b)
            cond_IJ = "$I, J$ lần lượt thuộc $SA$ và $SD$ sao cho " + cond_IJ
            cond_PQ = "$\\frac{SP}{SB} = \\frac{SQ}{SC} = \\frac{%s}{%s}$" % (a, b)
            cond_PQ = "$P, Q$ lần lượt thuộc $SB, SC$ sao cho " + cond_PQ

        kq_val = Rational(a, b)

        # Tính kết quả thập phân làm tròn đến hàng phần trăm (2 chữ số sau dấu phẩy)
        kq_exact_float = float(kq_val)
        kq_dec = Decimal(kq_exact_float).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        kq_str = str(kq_dec).replace('.', ',')

        # Các đáp án trắc nghiệm nhiễu (phân số)
        s_vals = [
            Rational(b, a),
            Rational(a, a+b),
            Rational(b, a+b),
            Rational(2*a, a+b),
            Rational(abs(a-b)+1, a+b+1)
        ]

        # Lọc đáp án nhiễu, làm tròn, đổi dấu phẩy và tránh trùng đáp án đúng hoặc trùng nhau
        s_strs = []
        for val in s_vals:
            val_float = float(val)
            val_dec = Decimal(val_float).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
            val_str = str(val_dec).replace('.', ',')
            if val_str != kq_str and val_str not in s_strs:
                s_strs.append(val_str)

        random.shuffle(s_strs)

        da_d = '\\True $%s$' % kq_str
        da_s1 = '$%s$' % s_strs[0]
        da_s2 = '$%s$' % s_strs[1]
        da_s3 = '$%s$' % s_strs[2]

        # Đưa các đáp án vào danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Tính toán tọa độ động cho TikZ (để điểm dịch chuyển theo tỷ lệ)
        tikz_ratio = a / b
        g_ratio = 2 * a / (a + b)

        # Câu hỏi (đã lược bỏ hình vẽ)
        noidungcauhoi_template = ('''Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành. Gọi %s. Gọi $G$ là giao điểm của $BJ$ và $CI$ và %s. Tỉ số $\\frac{GQ}{GA}$ bằng bao nhiêu? (kết quả làm tròn đến hàng phần trăm).''')
        noidungcauhoi = noidungcauhoi_template % (cond_IJ, cond_PQ)

        # Đoạn mã TikZ hình vẽ
        hinh_ve = ('''\\begin{center}
    \\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (D) at (0,0);
    \\coordinate (C) at (6,0);
    \\coordinate (A) at (1.7,1.8);
    \\coordinate (B) at (7.7,1.8);
    \\coordinate (S) at (3.8,6);
    \\coordinate (O) at ($(A)!0.5!(C)$);
    \\coordinate (I) at ($(S)!%s!(A)$);
    \\coordinate (J) at ($(S)!%s!(D)$);
    \\coordinate (P) at ($(S)!%s!(B)$);
    \\coordinate (Q) at ($(S)!%s!(C)$);
    \\coordinate (G) at ($(S)!%s!(O)$);
    \\draw[line width=1pt] (S)--(D) (S)--(C) (S)--(B) (D)--(C)--(B);
    \\draw[line width=1pt, dashed] (S)--(A) (D)--(A)--(B) (A)--(C) (B)--(D) (S)--(O) (C)--(I) (B)--(J) (A)--(Q) (D)--(P);
    \\fill (S) circle (1pt) node[above] {$S$};
    \\fill (A) circle (1pt) node[left] {$A$};
    \\fill (B) circle (1pt) node[right] {$B$};
    \\fill (C) circle (1pt) node[below right] {$C$};
    \\fill (D) circle (1pt) node[below left] {$D$};
    \\fill (O) circle (1pt) node[below] {$O$};
    \\fill (G) circle (1pt) node[below] {$G$};
    \\fill (I) circle (1pt) node[above left] {$I$};
    \\fill (J) circle (1pt) node[left] {$J$};
    \\fill (P) circle (1pt) node[above right] {$P$};
    \\fill (Q) circle (1pt) node[right] {$Q$};
    \\end{tikzpicture}
    \\end{center}''') % (tikz_ratio, tikz_ratio, tikz_ratio, tikz_ratio, g_ratio)

        # Lời giải thích ứng tùy theo thông số bài toán
        if a == 1 and b == 2:
            loigiai_template = ('''Gọi $O = AC \\cap BD$, $G' = CI \\cap SO$. Khi đó $G'$ là trọng tâm tam giác $SAC$ và $SBD$. Do đó $BG'$ đi qua trung điểm $J$ của $SD$. Hay $J \\in BG' \\subset (BCI)$.\\\\
    Từ đó suy ra: $G = CI \\cap BJ \\equiv G' = CI \\cap SO$.\\\\
    Ta có $\\Delta GIJ \\sim \\Delta GCB$. Do đó $\\frac{GI}{GC} = \\frac{GJ}{GB} = \\frac{IJ}{CB} = \\frac{IJ}{AD} = %s$.\\\\
    $G$ là trọng tâm tam giác $SAC$. Do đó trung tuyến $AQ$ đi qua điểm $G$.\\\\
    $G$ là trọng tâm tam giác $SBD$. Do đó trung tuyến $DP$ đi qua điểm $G$.\\\\
    Ta có $\\Delta GPQ \\sim \\Delta GDA$. Do đó $\\frac{GQ}{GA} = \\frac{GP}{GD} = \\frac{PQ}{DA} = \\frac{PQ}{CB} = %s = %s$.''')
            loigiai = loigiai_template % ("\\frac{1}{2}", "\\frac{1}{2}", kq_str)
        else:
            loigiai_template = ('''Gọi $O = AC \\cap BD$, $G' = CI \\cap SO$. Khi đó trong $\\Delta SAC$, $CI$ và $SO$ cắt nhau tại $G'$. Tương tự trong $\\Delta SBD$, $BJ$ và $SO$ cắt nhau.\\\\
    Do $%s$, ta có $G'$ cũng thuộc $BJ$. Do đó $BG'$ đi qua $J$. Hay $J \\in BG' \\subset (BCI)$.\\\\
    Từ đó suy ra: $G = CI \\cap BJ \\equiv G' = CI \\cap SO$.\\\\
    Ta có $IJ // AD // BC$ nên $\\Delta GIJ \\sim \\Delta GCB$. Do đó $\\frac{GI}{GC} = \\frac{GJ}{GB} = \\frac{IJ}{CB} = \\frac{IJ}{AD} = %s$.\\\\
    Tương tự, do $%s$ nên $AQ$ đi qua điểm $G$ trên $SO$.\\\\
    Do $%s$ nên $DP$ đi qua điểm $G$ trên $SO$.\\\\
    Ta có $PQ // AD$ nên $\\Delta GPQ \\sim \\Delta GDA$. Do đó $\\frac{GQ}{GA} = \\frac{GP}{GD} = \\frac{PQ}{DA} = \\frac{PQ}{CB} = %s \\approx %s$.''')
            l_val = latex(kq_val)
            loigiai = loigiai_template % (
                "\\frac{SI}{SA} = \\frac{SJ}{SD} = %s" % l_val,
                l_val,
                "\\frac{SI}{SA}=\\frac{SQ}{SC}=%s" % l_val,
                "\\frac{SJ}{SD}=\\frac{SP}{SB}=%s" % l_val,
                l_val,
                kq_str
            )

        # Nối hình vẽ vào cuối lời giải
        loigiai = hinh_ve +loigiai + '\n'
    dapan='\\shortans[0]{$%s$}\n'%(kq_str)
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+dapan+
        '\\loigiai{\n'+str(loigiai)+'\n}\n'
        '\\end{ex}\n\\end{minipage} \n\n')
    return content      


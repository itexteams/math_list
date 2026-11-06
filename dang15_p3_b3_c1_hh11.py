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


def bt_dang15_p3_b3_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':

        p = random.choice([3, 4, 5, 6])
        kq_val = p - 1
        kq = str(kq_val)

        # B4: Điều chỉnh các phương án sai không trùng với đáp án đúng
        s_set = set()
        candidate_vals = [
            kq_val + 1,
            kq_val + 2,
            kq_val - 1 if kq_val > 1 else kq_val + 3,
            Rational(1, kq_val),
            Rational(kq_val, kq_val + 1),
            Rational(kq_val + 1, kq_val),
            Rational(1, 2) if kq_val != 2 else Rational(1, 3),
        ]
        for val in candidate_vals:
            if val != kq_val:
                s_set.add('$%s$' % (latex(val)).replace('.', ','))

        s = list(s_set)
        du = ['$%s$' % (kq)]
        da = random.choice(du)

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        # Đưa các đáp án vào danh sách chọn ngẫu nhiên
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Tỉ lệ điểm M trên BC: BM/BC = (p - 1)/p => MC/BC = 1/p
        t_bm = round((p - 1) / p, 3)
        t_ag = round((p - 1) / p, 3)  # AG/AE = 1 - 1/p

        # B1 & B2: Đề bài
        if p == 3:
            mo_ta_g = 'Gọi $G$ là trọng tâm của tam giác $SAD$'
            loigiai_g = 'Gọi $E$ là trung điểm của $SD$, $F$ là giao điểm của $AM$ và $CD$ trong mặt phẳng $(ABCD)$.'
            ty_so_eg_ea = '\\frac{1}{3}'
        else:
            mo_ta_g = 'Gọi $E$ là trung điểm của $SD$, $G$ là điểm trên đoạn $AE$ thỏa mãn $EG = \\frac{1}{%s}EA$' % (p)
            loigiai_g = 'Gọi $F$ là giao điểm của $AM$ và $CD$ trong mặt phẳng $(ABCD)$.'
            ty_so_eg_ea = '\\frac{1}{%s}' % (p)

        noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành. %s và $M$ là điểm thuộc cạnh $BC$ sao cho $GM$ song song với mặt phẳng $(SCD)$. Khi đó tỉ số diện tích của hai tam giác $MAB$ và $MAC$ bằng'''
                         % (mo_ta_g))

        # Hình vẽ TikZ vẽ 100% như ảnh cung cấp, nét 1pt, điểm 1pt, màu black
        tikz_code = '''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\coordinate (B) at (0,0);
        \\coordinate (A) at (1.8,1.8);
        \\coordinate (C) at (5.4,0);
        \\coordinate (D) at ($(A)+(C)-(B)$);
        \\coordinate (S) at (3.6,6.2);
        \\coordinate (E) at ($(S)!0.5!(D)$);
        \\coordinate (M) at ($(B)!''' + str(t_bm) + '''!(C)$);
        \\coordinate (F) at (intersection of A--M and C--D);
        \\coordinate (G) at ($(A)!''' + str(t_ag) + '''!(E)$);
        \\draw[line width=1pt] (S)--(B)--(M) (C)--(D)--(S)--(C) (E)--(D) (E)--(F)--(C) (S)--(F) (M)--(F);
        \\draw[line width=1pt, dashed] (A)--(B) (A)--(D) (S)--(A) (A)--(E) (A)--(M) (M)--(C) (G)--(M) (A)--(M);
        \\fill (S) circle (1pt) node[above left] {$S$};
        \\fill (A) circle (1pt) node[left] {$A$};
        \\fill (B) circle (1pt) node[below left] {$B$};
        \\fill (C) circle (1pt) node[below right] {$C$};
        \\fill (D) circle (1pt) node[right] {$D$};
        \\fill (E) circle (1pt) node[above right] {$E$};
        \\fill (G) circle (1pt) node[above left] {$G$};
        \\fill (M) circle (1pt) node[below] {$M$};
        \\fill (F) circle (1pt) node[below] {$F$};
    \\end{tikzpicture}
    \\end{center}'''

        # Lời giải chi tiết
        loigiai = ('''%s
    %s \\\\
    Ta có: \\\\
    $\\begin{cases} GM \\subset (AEF) \\\\ GM // (SCD) \\\\ (AEF) \\cap (SCD) = EF \\end{cases} \\Rightarrow GM // EF$ \\\\
    $\\Rightarrow \\frac{FM}{FA} = \\frac{EG}{EA} = %s$ \\\\
    Theo hệ quả Talet, ta có: $\\frac{MC}{AD} = \\frac{FM}{FA} = %s$ \\\\
    $\\Rightarrow MC = %s AD = %s BC \\Rightarrow \\frac{MB}{MC} = %s$. \\\\
    Nhận xét: $\\Delta MAB$ và $\\Delta MAC$ có chung đường cao kẻ từ $A$. \\\\
    Do đó: $\\frac{S_{\\Delta MAB}}{S_{\\Delta MAC}} = \\frac{MB}{MC} = %s$.'''
                   % (tikz_code,
                      loigiai_g,
                      ty_so_eg_ea,
                      ty_so_eg_ea,
                      ty_so_eg_ea, ty_so_eg_ea, latex(kq_val),
                      latex(kq)))
    dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
               '\\loigiai{' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content


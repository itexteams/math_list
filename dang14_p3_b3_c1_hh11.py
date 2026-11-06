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


def bt_dang14_p3_b3_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':

        m_val = random.choice([1, 2, 3, 4])

        kq_val = m_val
        kq = str(kq_val)

        # B4: Điều chỉnh các phương án sai không trùng với đáp án đúng
        s_set = set()
        candidate_vals = [
            kq_val + 1,
            kq_val + 2,
            kq_val - 1 if kq_val > 1 else kq_val + 3,
            Rational(1, 2),
            Rational(1, 3),
            Rational(2, 3),
            Rational(3, 2),
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

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Tỉ lệ điểm M trên cạnh SB: SM = m_val / (m_val + 1) * SB
        t_sm = round(m_val / (m_val + 1), 3)

        # B1 & B2: Đề bài
        if m_val == 1:
            mo_ta_m = 'Gọi $M$ là trung điểm của $SB$'
        else:
            mo_ta_m = 'Gọi $M$ là điểm thuộc cạnh $SB$ sao cho $MS = %s MB$' % (m_val)

        noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành. Gọi $I, K$ lần lượt là trung điểm của $BC$ và $CD$. %s. Gọi $F$ là giao điểm của $DM$ và $(SIK)$. Tỉ số $\\frac{MF}{MD}$ bằng bao nhiêu?'''
                         % (mo_ta_m))

        # Hình vẽ TikZ chuẩn 100% theo mẫu ảnh cung cấp, nét 1pt, điểm 1pt, màu black
        tikz_code = '''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\coordinate (B) at (0,0);
        \\coordinate (C) at (4.5,0);
        \\coordinate (A) at (2,1.8);
        \\coordinate (D) at ($(A)+(C)-(B)$);
        \\coordinate (S) at (2.6,5.2);
        \\coordinate (I) at ($(B)!0.5!(C)$);
        \\coordinate (K) at ($(C)!0.5!(D)$);
        \\coordinate (O) at ($(A)!0.5!(C)$);
        \\coordinate (E) at ($(O)!0.5!(C)$);
        \\coordinate (M) at ($(S)!''' + str(t_sm) + '''!(B)$);
        \\coordinate (F) at ($(S)+(-4.8,-0.9)$);
        \\coordinate (X) at ($(S)+(4.8,0.9)$);
        \\draw[line width=1pt] (S)--(B)--(I)--(C)--(K)--(D)--(S)--(C) (S)--(I) (S)--(K) (S)--(X) (F)--(S) (F)--(M);
        \\draw[line width=1pt, dashed] (A)--(B) (A)--(D) (S)--(A) (B)--(D) (A)--(C) (I)--(K) (S)--(E) (M)--(D) (M)--(E) (S)--(O);
        \\fill (S) circle (1pt) node[above] {$S$};
        \\fill (B) circle (1pt) node[below left] {$B$};
        \\fill (C) circle (1pt) node[below right] {$C$};
        \\fill (D) circle (1pt) node[right] {$D$};
        \\fill (A) circle (1pt) node[above left] {$A$};
        \\fill (I) circle (1pt) node[below] {$I$};
        \\fill (K) circle (1pt) node[below right] {$K$};
        \\fill (M) circle (1pt) node[above left] {$M$};
        \\fill (E) circle (1pt) node[below] {$E$};
        \\fill (O) circle (1pt) node[below] {$O$};
        \\fill (F) circle (1pt) node[left] {$F$};
        \\node at ($(X)+(0.2,0)$) {$x$};
    \\end{tikzpicture}
    \\end{center}'''

        # Lời giải chi tiết
        loigiai = ('''%s
    Ta có $S \\in (SIK) \\cap (SAC)$. \\\\
    Trong mặt phẳng $(ABCD)$, gọi $E = IK \\cap AC \\Rightarrow \\begin{cases} E \\in IK \\subset (SIK) \\\\ E \\in AC \\subset (SAC) \\end{cases} \\Rightarrow E \\in (SIK) \\cap (SAC)$. \\\\
    Suy ra $SE = (SIK) \\cap (SAC)$. \\\\
    Ta có $\\begin{cases} S \\in (SIK) \\cap (SBD) \\\\ BD \\subset (SBD), IK \\subset (SIK) \\\\ BD // IK \\end{cases} \\Rightarrow (SIK) \\cap (SBD) = Sx, (Sx // BD // IK)$. \\\\
    Trong mặt phẳng $(SBD)$, gọi $F = Sx \\cap DM \\Rightarrow \\begin{cases} F \\in DM \\\\ F \\in Sx \\subset (SIK) \\end{cases} \\Rightarrow F = DM \\cap (SIK)$. \\\\
    Ta có $SF // BD \\Rightarrow \\frac{MF}{MD} = \\frac{MS}{MB} = %s$.'''
                   % (tikz_code, latex(kq_val)))
    dapan='\\shortans[0]{$%s$}\n'%(latex(kq_val))
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
               '\\loigiai{' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content


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


def bt_dang23_p1_b3_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1', '2']
    dang = random.choice(lisdang)

    if dang == '1':
        # Dạng 1: Giống bài toán gốc trong ảnh (M, N là trung điểm AB, CD; P thuộc SA; tìm giao tuyến của (SAD) và (PMN))
        canh1 = "AB"
        canh2 = "CD"
        canh_song_song = "AD"
        mp_xet = "SAD"
        diem_p = "P"
        canh_chua_p = "SA"

        hinh_tikz = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,0);
    \\coordinate (B) at (-1.3,-1.6);
    \\coordinate (C) at (2.2,-1.6);
    \\coordinate (D) at (3.5,0);
    \\coordinate (S) at (0.2,2.8);
    \\coordinate (M) at ($(A)!0.5!(B)$);
    \\coordinate (N) at ($(C)!0.5!(D)$);
    \\coordinate (P) at ($(S)!0.55!(A)$);
    \\coordinate (Q) at ($(S)!0.55!(D)$);
    \\coordinate (O) at ($(M)!0.5!(N)$);
    \\draw[line width=1pt] (S)--(B)--(C)--(D)--(S)--(C) (Q)--(N);
    \\draw[line width=1pt, dashed] (S)--(A)--(B) (A)--(D) (M)--(N) (B)--(D) (A)--(C) (P)--(M) (P)--(Q) ;
    \\fill (A) circle (1pt) node[above right] {$A$};
    \\fill (B) circle (1pt) node[below left] {$B$};
    \\fill (C) circle (1pt) node[below] {$C$};
    \\fill (D) circle (1pt) node[right] {$D$};
    \\fill (S) circle (1pt) node[above] {$S$};
    \\fill (M) circle (1pt) node[left] {$M$};
    \\fill (N) circle (1pt) node[below right] {$N$};
    \\fill (P) circle (1pt) node[above left] {$P$};
    \\fill (O) circle (1pt) node[below] {$O$};
    \\end{tikzpicture}
    \\end{center}''')

        da = 'đường thẳng qua $%s$ và song song với $%s$' % (diem_p, canh_song_song)

        s = [
            'đường thẳng qua $%s$ và song song với $%s$' % (diem_p, canh1),
            '$%sD$' % (diem_p),
            'đường thẳng qua $%s$ và song song với $MC$' % (diem_p),
            '$%sN$' % (diem_p),
            'đường thẳng qua $%s$ và song song với $SC$' % (diem_p)
        ]

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy là hình bình hành. Gọi $M, N$ lần lượt là trung điểm của $%s$ và $%s$, điểm $%s$ thuộc cạnh $%s$. Giao tuyến của hai mặt phẳng $(%s)$ và $(%sMN)$ là'''
                         % (canh1, canh2, diem_p, canh_chua_p, mp_xet, diem_p))

        loigiai = ('''%s
    Ta có: \\\\
    $\\left\\{\\begin{array}{l} MN // %s \\\\ MN \\subset (%sMN) \\\\ %s \\subset (%s) \\\\ %s \\in (%sMN) \\cap (%s) \\end{array}\\right. \\Rightarrow$ Giao tuyến của hai mặt phẳng $(%s)$ và $(%sMN)$ là đường thẳng qua $%s$ và song song với $%s$.'''
                   % (hinh_tikz, canh_song_song, diem_p, canh_song_song, mp_xet, diem_p, diem_p, mp_xet, mp_xet, diem_p, diem_p, canh_song_song))

    elif dang == '2':
        # Dạng 2: M, N là trung điểm AD và BC; P thuộc SA; tìm giao tuyến của (SAB) và (PMN)
        canh1 = "AD"
        canh2 = "BC"
        canh_song_song = "AB"
        mp_xet = "SAB"
        diem_p = "P"
        canh_chua_p = "SA"

        hinh_tikz = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,0);
    \\coordinate (B) at (-1.3,-1.6);
    \\coordinate (C) at (2.2,-1.6);
    \\coordinate (D) at (3.5,0);
    \\coordinate (S) at (0.2,2.8);
    \\coordinate (M) at ($(A)!0.5!(D)$);
    \\coordinate (N) at ($(B)!0.5!(C)$);
    \\coordinate (P) at ($(S)!0.55!(A)$);
    \\coordinate (Q) at ($(S)!0.55!(B)$);
    \\coordinate (O) at ($(M)!0.5!(N)$);
    \\draw[line width=1pt] (S)--(B)--(C)--(D)--(S)--(C) (P)--(Q) (Q)--(N);
    \\draw[line width=1pt, dashed] (S)--(A)--(B) (A)--(D) (M)--(N) (B)--(D) (A)--(C) (P)--(M) ;
    \\fill (A) circle (1pt) node[above right] {$A$};
    \\fill (B) circle (1pt) node[below left] {$B$};
    \\fill (C) circle (1pt) node[below] {$C$};
    \\fill (D) circle (1pt) node[right] {$D$};
    \\fill (S) circle (1pt) node[above] {$S$};
    \\fill (M) circle (1pt) node[above] {$M$};
    \\fill (N) circle (1pt) node[below] {$N$};
    \\fill (P) circle (1pt) node[above left] {$P$};
    \\fill (O) circle (1pt) node[below] {$O$};
    \\end{tikzpicture}
    \\end{center}''')

        da = 'đường thẳng qua $%s$ và song song với $%s$' % (diem_p, canh_song_song)

        s = [
            'đường thẳng qua $%s$ và song song với $%s$' % (diem_p, canh1),
            '$%sB$' % (diem_p),
            'đường thẳng qua $%s$ và song song với $MD$' % (diem_p),
            '$%sN$' % (diem_p),
            'đường thẳng qua $%s$ và song song với $SD$' % (diem_p)
        ]

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy là hình bình hành. Gọi $M, N$ lần lượt là trung điểm của $%s$ và $%s$, điểm $%s$ thuộc cạnh $%s$. Giao tuyến của hai mặt phẳng $(%s)$ và $(%sMN)$ là'''
                         % (canh1, canh2, diem_p, canh_chua_p, mp_xet, diem_p))

        loigiai = ('''%s
    Ta có: \\\\
    $\\left\\{\\begin{array}{l} MN // %s \\\\ MN \\subset (%sMN) \\\\ %s \\subset (%s) \\\\ %s \\in (%sMN) \\cap (%s) \\end{array}\\right. \\Rightarrow$ Giao tuyến của hai mặt phẳng $(%s)$ và $(%sMN)$ là đường thẳng qua $%s$ và song song với $%s$.'''
                   % (hinh_tikz, canh_song_song, diem_p, canh_song_song, mp_xet, diem_p, diem_p, mp_xet, mp_xet, diem_p, diem_p, canh_song_song))

    # Các đáp án
    da_d = ('\\True ' + str(da))
    da_s1 = str(das1)
    da_s2 = str(das2)
    da_s3 = str(das3)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_1 = [da_d, da_s1, da_s2, da_s3]
    random.shuffle(list_1)

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
        '\\choice \n'
        '{' + str(list_1[1]) + '}\n'
        '{' + str(list_1[2]) + '}\n'
        '{' + str(list_1[3]) + '}\n'
        '{' + str(list_1[0]) + '}\n'
        '\\loigiai{' + str(loigiai) + '}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content


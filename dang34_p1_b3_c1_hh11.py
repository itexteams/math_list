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


def bt_dang34_p1_b3_c1_hh11(self):
    # Dạng 2: M, N lần lượt là trung điểm của SB và SD => MN // BD => MN // (ABCD)
    lisdang = ['1', '2']
    dang = random.choice(lisdang)

    if dang == '1':
        canh1 = 'SA'
        canh2 = 'SC'
        duong_cheo = 'AC'
        tam_giac = 'SAC'

        # Đáp án đúng
        da = '$MN // (ABCD)$'

        # Tập hợp các phương án gây nhiễu (không được trùng với đáp án đúng)
        s = [
            '$MN // (SAB)$',
            '$MN // (SCD)$',
            '$MN // (SBC)$',
            '$MN // (SAD)$'
        ]
        if da in s:
            s.remove(da)

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho hình chóp tứ giác $S.ABCD$. Gọi $M$ và $N$ lần lượt là trung điểm của $%s$ và $%s$. Khẳng định nào sau đây đúng?'''
                         % (canh1, canh2))

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        # Đưa các đáp án vào danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Hình vẽ TikZ vẽ 100% chuẩn theo ảnh, nét 1pt, điểm 1pt, màu black
        tikz_fig = '''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,0);
    \\coordinate (B) at (1.8,-1.5);
    \\coordinate (C) at (3.8,-1.2);
    \\coordinate (D) at (4.5,0);
    \\coordinate (S) at (1.6,2.3);
    \\coordinate (M) at ($(S)!0.5!(A)$);
    \\coordinate (N) at ($(S)!0.5!(C)$);
    \\draw[line width=1pt] (S)--(A)--(B)--(C)--(D)--(S) (S)--(B) (S)--(C);
    \\draw[line width=1pt, dashed] (A)--(D) (A)--(C) (M)--(N);
    \\fill (A) circle (1pt) node[left] {$A$};
    \\fill (B) circle (1pt) node[below] {$B$};
    \\fill (C) circle (1pt) node[right] {$C$};
    \\fill (D) circle (1pt) node[right] {$D$};
    \\fill (S) circle (1pt) node[above] {$S$};
    \\fill (M) circle (1pt) node[left] {$M$};
    \\fill (N) circle (1pt) node[right] {$N$};
    \\end{tikzpicture}
    \\end{center}'''

        # Nội dung lời giải chi tiết, đầy đủ
        loigiai = ('''%s
    $MN$ là đường trung bình của $\\Delta %s$ nên $MN // %s$.\\\\
    Ta có $\\begin{cases} MN // %s \\\\ %s \\subset (ABCD) \\\\ MN \\not\\subset (ABCD) \\end{cases} \\Rightarrow MN // (ABCD)$.'''
                   % (tikz_fig, tam_giac, duong_cheo, duong_cheo, duong_cheo))

    elif dang == '2':
        canh1 = 'SB'
        canh2 = 'SD'
        duong_cheo = 'BD'
        tam_giac = 'SBD'

        da = '$MN // (ABCD)$'

        s = [
            '$MN // (SAB)$',
            '$MN // (SCD)$',
            '$MN // (SBC)$',
            '$MN // (SAD)$'
        ]
        if da in s:
            s.remove(da)

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        noidungcauhoi = ('''Cho hình chóp tứ giác $S.ABCD$. Gọi $M$ và $N$ lần lượt là trung điểm của $%s$ và $%s$. Khẳng định nào sau đây đúng?'''
                         % (canh1, canh2))

        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        tikz_fig = '''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,0);
    \\coordinate (B) at (1.8,-1.5);
    \\coordinate (C) at (3.8,-1.2);
    \\coordinate (D) at (4.5,0);
    \\coordinate (S) at (1.6,2.3);
    \\coordinate (M) at ($(S)!0.5!(B)$);
    \\coordinate (N) at ($(S)!0.5!(D)$);
    \\draw[line width=1pt] (S)--(A)--(B)--(C)--(D)--(S) (S)--(B) (S)--(C);
    \\draw[line width=1pt, dashed] (A)--(D) (B)--(D) (M)--(N);
    \\fill (A) circle (1pt) node[left] {$A$};
    \\fill (B) circle (1pt) node[below] {$B$};
    \\fill (C) circle (1pt) node[right] {$C$};
    \\fill (D) circle (1pt) node[right] {$D$};
    \\fill (S) circle (1pt) node[above] {$S$};
    \\fill (M) circle (1pt) node[left] {$M$};
    \\fill (N) circle (1pt) node[right] {$N$};
    \\end{tikzpicture}
    \\end{center}'''

        loigiai = ('''%s
    $MN$ là đường trung bình của $\\Delta %s$ nên $MN // %s$.\\\\
    Ta có $\\begin{cases} MN // %s \\\\ %s \\subset (ABCD) \\\\ MN \\not\\subset (ABCD) \\end{cases} \\Rightarrow MN // (ABCD)$.'''
                   % (tikz_fig, tam_giac, duong_cheo, duong_cheo, duong_cheo))

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


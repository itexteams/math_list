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


def bt_dang36_p1_b3_c1_hh11(self):
    # Dạng 2: Biến thể: M là trung điểm SC, hỏi SA song song với mặt phẳng nào? => (MJK)
    lisdang = ['1', '2']
    dang = random.choice(lisdang)

    # Random mẫu số của tỉ số khoảng cách: 1/3, 1/4, 1/5
    mau_so = random.choice([3, 4, 5])
    ti_so_str = '\\frac{1}{%s}' % mau_so

    if dang == '1':
        canh_hoi = 'SC'
        trung_diem_goc = 'SA'
        da_dung_val = '(MJK)'

        # Đáp án đúng
        da = '$%s$' % (da_dung_val)

        # Danh sách các phương án gây nhiễu
        s = [
            '$(IJK)$',
            '$(IBK)$',
            '$(IJA)$',
            '$(SBD)$',
            '$(SAB)$',
            '$(SCD)$'
        ]
        if da in s:
            s.remove(da)

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        # Câu hỏi
        noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành. $I$ là trung điểm $SB$. $J, K$ là điểm thuộc $BC, AD$ sao cho $\\frac{BJ}{BC} = \\frac{DK}{DA} = %s$, $M$ là trung điểm $%s$. Hỏi $%s$ song song với mặt phẳng nào sau đây?'''
                         % (ti_so_str, trung_diem_goc, canh_hoi))

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        # Đưa các đáp án vào danh sách và xáo trộn
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải kèm hình vẽ TikZ đúng chuẩn 100%
        loigiai = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (S) at (0,3.5);
    \\coordinate (B) at (0.4,0);
    \\coordinate (C) at (2.6,0);
    \\coordinate (A) at (1.1,1.1);
    \\coordinate (D) at (3.3,1.1);
    \\coordinate (I) at ($(S)!0.5!(B)$);
    \\coordinate (M) at ($(S)!0.5!(A)$);
    \\coordinate (J) at ($(B)!0.3333!(C)$);
    \\coordinate (K) at ($(D)!0.3333!(A)$);
    \\coordinate (O) at (intersection of A--C and J--K);
    \\draw[line width=1pt] (S)--(B)--(C)--(D)--(S) (S)--(C);
    \\draw[line width=1pt, dashed] (S)--(A) (A)--(B) (A)--(D) (A)--(C) (M)--(J) (M)--(K) (J)--(K);
    \\fill (S) circle (1pt) node[above] {$S$};
    \\fill (B) circle (1pt) node[left] {$B$};
    \\fill (C) circle (1pt) node[right] {$C$};
    \\fill (A) circle (1pt) node[above] {$A$};
    \\fill (D) circle (1pt) node[right] {$D$};
    \\fill (I) circle (1pt) node[left] {$I$};
    \\fill (M) circle (1pt) node[left] {$M$};
    \\fill (J) circle (1pt) node[below] {$J$};
    \\fill (K) circle (1pt) node[above] {$K$};
    \\fill (O) circle (1pt) node[below] {$O$};
    \\end{tikzpicture}
    \\end{center}
    Do $\\frac{BJ}{BC} = \\frac{DK}{DA} = %s$ và $BC = AD$ nên $BJ = DK$ hay $JC = AK$.\\\\
    Gọi $O$ là giao điểm của $AC$ và $JK$. Khi đó: $\\frac{OA}{OC} = \\frac{AK}{JC} = 1 \\Rightarrow O$ là trung điểm $AC$.\\\\
    $\\Rightarrow MO$ là đường trung bình tam giác $SAC \\Rightarrow MO // %s$, mà $MO \\subset %s$.\\\\
    Vậy $%s // %s$.'''
                   % (ti_so_str, canh_hoi, da_dung_val, canh_hoi, da_dung_val))

    elif dang == '2':
        canh_hoi = 'SA'
        trung_diem_goc = 'SC'
        da_dung_val = '(MJK)'

        da = '$%s$' % (da_dung_val)

        s = [
            '$(IJK)$',
            '$(IBK)$',
            '$(IJA)$',
            '$(SBD)$',
            '$(SAB)$',
            '$(SAD)$'
        ]
        if da in s:
            s.remove(da)

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành. $I$ là trung điểm $SB$. $J, K$ là điểm thuộc $BC, AD$ sao cho $\\frac{BJ}{BC} = \\frac{DK}{DA} = %s$, $M$ là trung điểm $%s$. Hỏi $%s$ song song với mặt phẳng nào sau đây?'''
                         % (ti_so_str, trung_diem_goc, canh_hoi))

        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        loigiai = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (S) at (0,3.5);
    \\coordinate (B) at (0.4,0);
    \\coordinate (C) at (2.6,0);
    \\coordinate (A) at (1.1,1.1);
    \\coordinate (D) at (3.3,1.1);
    \\coordinate (I) at ($(S)!0.5!(B)$);
    \\coordinate (M) at ($(S)!0.5!(C)$);
    \\coordinate (J) at ($(B)!0.3333!(C)$);
    \\coordinate (K) at ($(D)!0.3333!(A)$);
    \\coordinate (O) at (intersection of A--C and J--K);
    \\draw[line width=1pt] (S)--(B)--(C)--(D)--(S) (S)--(C) (M)--(J);
    \\draw[line width=1pt, dashed] (S)--(A) (A)--(B) (A)--(D) (A)--(C) (M)--(K) (J)--(K);
    \\fill (S) circle (1pt) node[above] {$S$};
    \\fill (B) circle (1pt) node[left] {$B$};
    \\fill (C) circle (1pt) node[right] {$C$};
    \\fill (A) circle (1pt) node[above] {$A$};
    \\fill (D) circle (1pt) node[right] {$D$};
    \\fill (I) circle (1pt) node[left] {$I$};
    \\fill (M) circle (1pt) node[right] {$M$};
    \\fill (J) circle (1pt) node[below] {$J$};
    \\fill (K) circle (1pt) node[above] {$K$};
    \\fill (O) circle (1pt) node[below] {$O$};
    \\end{tikzpicture}
    \\end{center}
    Do $\\frac{BJ}{BC} = \\frac{DK}{DA} = %s$ và $BC = AD$ nên $BJ = DK$ hay $JC = AK$.\\\\
    Gọi $O$ là giao điểm của $AC$ và $JK$. Khi đó: $\\frac{OA}{OC} = \\frac{AK}{JC} = 1 \\Rightarrow O$ là trung điểm $AC$.\\\\
    $\\Rightarrow MO$ là đường trung bình tam giác $SAC \\Rightarrow MO // %s$, mà $MO \\subset %s$.\\\\
    Vậy $%s // %s$.'''
                   % (ti_so_str, canh_hoi, da_dung_val, canh_hoi, da_dung_val))

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


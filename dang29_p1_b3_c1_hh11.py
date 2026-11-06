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


def bt_dang29_p1_b3_c1_hh11(self):
    # Dạng 3: I là trung điểm AB, M = BD giao CI, K thuộc SD sao cho SK = 1/2 KD => MK // (SAB)
    lisdang = ['1', '2', '3']
    dang = random.choice(lisdang)

    if dang == '1':
        canh_day = 'BC'
        doan1 = 'BD'
        doan2 = 'AI'
        canh_ben = 'SD'
        tam_giac = 'ABC'
        duong_cheo = 'BD'
        canh_song_song = 'SB'
        mp_song_song = '(SBC)'

        # Đáp án đúng
        da = '$MK // %s$' % (mp_song_song)

        # Tập hợp các phương án gây nhiễu
        s = [
            '$MK // (ABCD)$',
            '$MK // (SBD)$',
            '$MK // (SCD)$',
            '$MK // (SAD)$'
        ]
        if da in s:
            s.remove(da)

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        # Câu hỏi
        noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình thoi tâm $O$. Gọi $I$ là trung điểm của $%s$, $K$ thuộc cạnh $%s$ sao cho $SK = \\frac{1}{2}KD$. $M$ là giao điểm của $%s$ và $%s$. Tìm khẳng định đúng trong các khẳng định sau?'''
                         % (canh_day, canh_ben, doan1, doan2))

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        # Đưa các đáp án vào danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải kèm hình vẽ TikZ
        loigiai = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,0);
    \\coordinate (B) at (2,-1.5);
    \\coordinate (C) at (6,-1.5);
    \\coordinate (D) at (4,0);
    \\coordinate (S) at (1.5,3.5);
    \\coordinate (O) at (intersection of A--C and B--D);
    \\coordinate (I) at ($(B)!0.5!(C)$);
    \\coordinate (M) at (intersection of B--D and A--I);
    \\coordinate (K) at ($(S)!0.3333!(D)$);
    \\draw[line width=1pt] (S)--(A)--(B)--(C)--(S)--(B) (S)--(C);
    \\draw[line width=1pt, dashed] (A)--(D)--(C) (S)--(D) (A)--(C) (B)--(D) (A)--(I) (M)--(K);
    \\fill (A) circle (1pt) node[left] {$A$};
    \\fill (B) circle (1pt) node[below] {$B$};
    \\fill (C) circle (1pt) node[right] {$C$};
    \\fill (D) circle (1pt) node[above right] {$D$};
    \\fill (S) circle (1pt) node[above] {$S$};
    \\fill (O) circle (1pt) node[above] {$O$};
    \\fill (I) circle (1pt) node[below] {$I$};
    \\fill (M) circle (1pt) node[below] {$M$};
    \\fill (K) circle (1pt) node[above right] {$K$};
    \\end{tikzpicture}
    \\end{center}
    Có điểm $M$ là trọng tâm của tam giác $%s$ và $O$ là trung điểm của $%s$ nên $BM = \\frac{1}{2}MD$.\\\\
    Theo giả thiết ta có $SK = \\frac{1}{2}KD$.\\\\
    Do đó $\\begin{cases} MK // %s \\\\ %s \\subset %s \\\\ MK \\not\\subset %s \\end{cases} \\Rightarrow MK // %s$.\\\\
    Vậy $MK // %s$.'''
                   % (tam_giac, duong_cheo, canh_song_song, canh_song_song, mp_song_song, mp_song_song, mp_song_song, mp_song_song))

    elif dang == '2':
        canh_day = 'CD'
        doan1 = 'AC'
        doan2 = 'DI'
        canh_ben = 'SB'
        tam_giac = 'ACD'
        duong_cheo = 'AC'
        canh_song_song = 'SD'
        mp_song_song = '(SCD)'

        da = '$MK // %s$' % (mp_song_song)

        s = [
            '$MK // (ABCD)$',
            '$MK // (SBD)$',
            '$MK // (SBC)$',
            '$MK // (SAB)$'
        ]
        if da in s:
            s.remove(da)

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình thoi tâm $O$. Gọi $I$ là trung điểm của $%s$, $K$ thuộc cạnh $%s$ sao cho $SK = \\frac{1}{2}KB$. $M$ là giao điểm của $%s$ và $%s$. Tìm khẳng định đúng trong các khẳng định sau?'''
                         % (canh_day, canh_ben, doan1, doan2))

        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        loigiai = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,0);
    \\coordinate (B) at (2,-1.5);
    \\coordinate (C) at (6,-1.5);
    \\coordinate (D) at (4,0);
    \\coordinate (S) at (1.5,3.5);
    \\coordinate (O) at (intersection of A--C and B--D);
    \\coordinate (I) at ($(C)!0.5!(D)$);
    \\coordinate (M) at (intersection of A--C and D--I);
    \\coordinate (K) at ($(S)!0.3333!(B)$);
    \\draw[line width=1pt] (S)--(A)--(B)--(C)--(S)--(B) (S)--(C);
    \\draw[line width=1pt, dashed] (A)--(D)--(C) (S)--(D) (A)--(C) (B)--(D) (D)--(I) (M)--(K);
    \\fill (A) circle (1pt) node[left] {$A$};
    \\fill (B) circle (1pt) node[below] {$B$};
    \\fill (C) circle (1pt) node[right] {$C$};
    \\fill (D) circle (1pt) node[above right] {$D$};
    \\fill (S) circle (1pt) node[above] {$S$};
    \\fill (O) circle (1pt) node[above] {$O$};
    \\fill (I) circle (1pt) node[right] {$I$};
    \\fill (M) circle (1pt) node[below] {$M$};
    \\fill (K) circle (1pt) node[left] {$K$};
    \\end{tikzpicture}
    \\end{center}
    Có điểm $M$ là trọng tâm của tam giác $%s$ và $O$ là trung điểm của $%s$ nên $DM = \\frac{1}{2}MB$.\\\\
    Theo giả thiết ta có $SK = \\frac{1}{2}KB$.\\\\
    Do đó $\\begin{cases} MK // %s \\\\ %s \\subset %s \\\\ MK \\not\\subset %s \\end{cases} \\Rightarrow MK // %s$.\\\\
    Vậy $MK // %s$.'''
                   % (tam_giac, duong_cheo, canh_song_song, canh_song_song, mp_song_song, mp_song_song, mp_song_song, mp_song_song))

    elif dang == '3':
        canh_day = 'AB'
        doan1 = 'BD'
        doan2 = 'CI'
        canh_ben = 'SD'
        tam_giac = 'ABD'
        duong_cheo = 'BD'
        canh_song_song = 'SA'
        mp_song_song = '(SAB)'

        da = '$MK // %s$' % (mp_song_song)

        s = [
            '$MK // (ABCD)$',
            '$MK // (SBD)$',
            '$MK // (SBC)$',
            '$MK // (SCD)$'
        ]
        if da in s:
            s.remove(da)

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình thoi tâm $O$. Gọi $I$ là trung điểm của $%s$, $K$ thuộc cạnh $%s$ sao cho $SK = \\frac{1}{2}KD$. $M$ là giao điểm của $%s$ và $%s$. Tìm khẳng định đúng trong các khẳng định sau?'''
                         % (canh_day, canh_ben, doan1, doan2))

        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        loigiai = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,0);
    \\coordinate (B) at (2,-1.5);
    \\coordinate (C) at (6,-1.5);
    \\coordinate (D) at (4,0);
    \\coordinate (S) at (1.5,3.5);
    \\coordinate (O) at (intersection of A--C and B--D);
    \\coordinate (I) at ($(A)!0.5!(B)$);
    \\coordinate (M) at (intersection of B--D and C--I);
    \\coordinate (K) at ($(S)!0.3333!(D)$);
    \\draw[line width=1pt] (S)--(A)--(B)--(C)--(S)--(B) (S)--(C);
    \\draw[line width=1pt, dashed] (A)--(D)--(C) (S)--(D) (A)--(C) (B)--(D) (C)--(I) (M)--(K);
    \\fill (A) circle (1pt) node[left] {$A$};
    \\fill (B) circle (1pt) node[below] {$B$};
    \\fill (C) circle (1pt) node[right] {$C$};
    \\fill (D) circle (1pt) node[above right] {$D$};
    \\fill (S) circle (1pt) node[above] {$S$};
    \\fill (O) circle (1pt) node[above] {$O$};
    \\fill (I) circle (1pt) node[left] {$I$};
    \\fill (M) circle (1pt) node[below] {$M$};
    \\fill (K) circle (1pt) node[above right] {$K$};
    \\end{tikzpicture}
    \\end{center}
    Có điểm $M$ là trọng tâm của tam giác $%s$ và $O$ là trung điểm của $%s$ nên $BM = \\frac{1}{2}MD$.\\\\
    Theo giả thiết ta có $SK = \\frac{1}{2}KD$.\\\\
    Do đó $\\begin{cases} MK // %s \\\\ %s \\subset %s \\\\ MK \\not\\subset %s \\end{cases} \\Rightarrow MK // %s$.\\\\
    Vậy $MK // %s$.'''
                   % (tam_giac, duong_cheo, canh_song_song, canh_song_song, mp_song_song, mp_song_song, mp_song_song, mp_song_song))

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


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


def bt_dang32_p1_b3_c1_hh11(self):
    # Khai báo danh sách dạng bài
    # Dạng 1: I, J lần lượt là trọng tâm tam giác SAB và SAD; M là trung điểm CD => IJ // (SBD)
    # Dạng 2: I, J lần lượt là trọng tâm tam giác SCB và SCD; M là trung điểm AB => IJ // (SBD)
    lisdang = ['1', '2']
    dang = random.choice(lisdang)

    if dang == '1':
        tg1 = 'SAB'
        tg2 = 'SAD'
        canh_M = 'CD'
        canh_N = 'AB'
        canh_P = 'AD'
        canh_day_songsong = 'BD'
        mp_dung = '(SBD)'

        # Đáp án đúng
        da = '$IJ // %s$' % (mp_dung)

        # Tập hợp các phương án gây nhiễu
        s = [
            '$IJ // (SBM)$',
            '$IJ // (SCD)$',
            '$IJ // (SBC)$',
            '$IJ // (SAD)$',
            '$IJ // (ABCD)$'
        ]
        if da in s:
            s.remove(da)

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        # Câu hỏi
        noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy là hình bình hành. Các điểm $I, J$ lần lượt là trọng tâm các tam giác $%s$ và $%s$. Gọi $M$ là trung điểm $%s$. Chọn mệnh đề đúng trong các mệnh đề sau'''
                         % (tg1, tg2, canh_M))

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        # Đưa các đáp án vào danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải với hình vẽ TikZ đúng 100% hình mẫu
        loigiai = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (B) at (0,0);
    \\coordinate (C) at (3,-0.2);
    \\coordinate (A) at (1,1.5);
    \\coordinate (D) at (4,1.5);
    \\coordinate (S) at (1,4.2);
    \\coordinate (N) at ($(A)!0.5!(B)$);
    \\coordinate (P) at ($(A)!0.5!(D)$);
    \\coordinate (M) at ($(C)!0.5!(D)$);
    \\coordinate (I) at ($(S)!0.66667!(N)$);
    \\coordinate (J) at ($(S)!0.66667!(P)$);
    \\draw[line width=1pt] (S)--(B)--(C)--(D)--(S)--(C) (S)--(M) (S)--(N);
    \\draw[line width=1pt, dashed] (B)--(A)--(D) (S)--(A) (S)--(P) (N)--(P) (I)--(J) (B)--(D);
    \\fill (A) circle (1pt) node[above right] {$A$};
    \\fill (B) circle (1pt) node[below left] {$B$};
    \\fill (C) circle (1pt) node[below] {$C$};
    \\fill (D) circle (1pt) node[right] {$D$};
    \\fill (S) circle (1pt) node[above] {$S$};
    \\fill (N) circle (1pt) node[left] {$N$};
    \\fill (P) circle (1pt) node[above] {$P$};
    \\fill (M) circle (1pt) node[below right] {$M$};
    \\fill (I) circle (1pt) node[above left] {$I$};
    \\fill (J) circle (1pt) node[above right] {$J$};
    \\end{tikzpicture}
    \\end{center}
    Gọi $N, P$ lần lượt là trung điểm của $%s, %s$.\\\\
    Ta có $\\frac{SI}{SN} = \\frac{SJ}{SP} = \\frac{2}{3} \\Rightarrow IJ // NP$ mà $NP // %s$ suy ra $IJ // %s$.'''
                   % (canh_N, canh_P, canh_day_songsong, mp_dung))

    elif dang == '2':
        tg1 = 'SCB'
        tg2 = 'SCD'
        canh_M = 'AB'
        canh_N = 'CB'
        canh_P = 'CD'
        canh_day_songsong = 'BD'
        mp_dung = '(SBD)'

        da = '$IJ // %s$' % (mp_dung)

        s = [
            '$IJ // (SAM)$',
            '$IJ // (SAB)$',
            '$IJ // (SAD)$',
            '$IJ // (SBC)$',
            '$IJ // (ABCD)$'
        ]
        if da in s:
            s.remove(da)

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy là hình bình hành. Các điểm $I, J$ lần lượt là trọng tâm các tam giác $%s$ và $%s$. Gọi $M$ là trung điểm $%s$. Chọn mệnh đề đúng trong các mệnh đề sau'''
                         % (tg1, tg2, canh_M))

        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        loigiai = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (B) at (0,0);
    \\coordinate (C) at (3,-0.2);
    \\coordinate (A) at (1,1.5);
    \\coordinate (D) at (4,1.5);
    \\coordinate (S) at (1,4.2);
    \\coordinate (N) at ($(C)!0.5!(B)$);
    \\coordinate (P) at ($(C)!0.5!(D)$);
    \\coordinate (M) at ($(A)!0.5!(B)$);
    \\coordinate (I) at ($(S)!0.66667!(N)$);
    \\coordinate (J) at ($(S)!0.66667!(P)$);
    \\draw[line width=1pt] (S)--(B)--(C)--(D)--(S)--(C) (S)--(N) (S)--(P) ;
    \\draw[line width=1pt, dashed] (B)--(A)--(D) (S)--(A) (S)--(M) (B)--(D) (N)--(P) (I)--(J);
    \\fill (A) circle (1pt) node[above right] {$A$};
    \\fill (B) circle (1pt) node[below left] {$B$};
    \\fill (C) circle (1pt) node[below] {$C$};
    \\fill (D) circle (1pt) node[right] {$D$};
    \\fill (S) circle (1pt) node[above] {$S$};
    \\fill (N) circle (1pt) node[below] {$N$};
    \\fill (P) circle (1pt) node[below right] {$P$};
    \\fill (M) circle (1pt) node[left] {$M$};
    \\fill (I) circle (1pt) node[left] {$I$};
    \\fill (J) circle (1pt) node[right] {$J$};
    \\end{tikzpicture}
    \\end{center}
    Gọi $N, P$ lần lượt là trung điểm của $%s, %s$.\\\\
    Ta có $\\frac{SI}{SN} = \\frac{SJ}{SP} = \\frac{2}{3} \\Rightarrow IJ // NP$ mà $NP // %s$ suy ra $IJ // %s$.'''
                   % (canh_N, canh_P, canh_day_songsong, mp_dung))

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


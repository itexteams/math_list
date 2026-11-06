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


def bt_dang17_p1_b3_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1', '2', '3']
    dang = random.choice(lisdang)

    if dang == '1':
        # Dạng 1: Giống bài toán gốc trong ảnh (A', B' lần lượt là trung điểm của SA, SB)
        p1 = "A'"
        p2 = "B'"
        c1 = "SA"
        c2 = "SB"
        canh_day = "AB"
        mp_song_song = "(ABCD)"
        mp_chua = "(SAB)"

        # TikZ vẽ hình chính xác 100% như ảnh mẫu (SA vuông góc đáy dạng phối cảnh, nét liền/đứt chuẩn xác)
        hinh_tikz = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,0);
    \\coordinate (B) at (-1.3,-1.7);
    \\coordinate (C) at (1.8,-1.7);
    \\coordinate (D) at (3.1,0);
    \\coordinate (S) at (0,2.3);
    \\coordinate (A1) at ($(S)!0.5!(A)$);
    \\coordinate (B1) at ($(S)!0.5!(B)$);
    \\draw[line width=1pt] (S)--(B)--(C)--(D)--(S)--(C) (A1)--(B1);
    \\draw[line width=1pt, dashed] (S)--(A)--(B) (A)--(D) (S)--(A1);
    \\fill (A) circle (1pt) node[left] {$A$};
    \\fill (B) circle (1pt) node[below left] {$B$};
    \\fill (C) circle (1pt) node[below right] {$C$};
    \\fill (D) circle (1pt) node[right] {$D$};
    \\fill (S) circle (1pt) node[above left] {$S$};
    \\fill (A1) circle (1pt) node[right] {$A'$};
    \\fill (B1) circle (1pt) node[left] {$B'$};
    \\end{tikzpicture}
    \\end{center}''')

        da = '$%s$' % (mp_song_song)
        s = [
            '$%s$' % (mp_chua),
            '$(SAD)$',
            '$(SBC)$',
            '$(SCD)$'
        ]

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành. Gọi $%s,%s$ lần lượt là trung điểm của $%s,%s$. Đường thẳng $%s%s$ song song với mặt phẳng nào dưới đây?'''
                         % (p1, p2, c1, c2, p1, p2))

        loigiai = ('''Ta có: \\\\
    %s
    Xét tam giác $SAB$, ta có $%s,%s$ lần lượt là trung điểm của $%s$ và $%s$. \\\\
    Suy ra $%s%s // %s$ (tính chất đường trung bình trong tam giác). \\\\
    Mặt khác: \\\\
    $\\begin{cases} %s%s // %s \\\\ %s \\subset %s \\\\ %s%s \\not\\subset %s \\end{cases} \\Rightarrow %s%s // %s$.'''
                   % (hinh_tikz, p1, p2, c1, c2, p1, p2, canh_day, p1, p2, canh_day, canh_day, mp_song_song, p1, p2, mp_song_song, p1, p2, mp_song_song))

    elif dang == '2':
        # Dạng 2: Random trung điểm trên cạnh khác: C', D' lần lượt là trung điểm của SC, SD
        p1 = "C'"
        p2 = "D'"
        c1 = "SC"
        c2 = "SD"
        canh_day = "CD"
        mp_song_song = "(ABCD)"
        mp_chua = "(SCD)"

        hinh_tikz = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,0);
    \\coordinate (B) at (-1.3,-1.7);
    \\coordinate (C) at (1.8,-1.7);
    \\coordinate (D) at (3.1,0);
    \\coordinate (S) at (0,2.3);
    \\coordinate (C1) at ($(S)!0.5!(C)$);
    \\coordinate (D1) at ($(S)!0.5!(D)$);
    \\draw[line width=1pt] (S)--(B)--(C)--(D)--(S)--(C) (C1)--(D1);
    \\draw[line width=1pt, dashed] (S)--(A)--(B) (A)--(D);
    \\fill (A) circle (1pt) node[left] {$A$};
    \\fill (B) circle (1pt) node[below left] {$B$};
    \\fill (C) circle (1pt) node[below right] {$C$};
    \\fill (D) circle (1pt) node[right] {$D$};
    \\fill (S) circle (1pt) node[above left] {$S$};
    \\fill (C1) circle (1pt) node[right] {$C'$};
    \\fill (D1) circle (1pt) node[above right] {$D'$};
    \\end{tikzpicture}
    \\end{center}''')

        da = '$%s$' % (mp_song_song)
        s = [
            '$%s$' % (mp_chua),
            '$(SAB)$',
            '$(SBC)$',
            '$(SAD)$'
        ]

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành. Gọi $%s,%s$ lần lượt là trung điểm của $%s,%s$. Đường thẳng $%s%s$ song song với mặt phẳng nào dưới đây?'''
                         % (p1, p2, c1, c2, p1, p2))

        loigiai = ('''Ta có: \\\\
    %s
    Xét tam giác $SCD$, ta có $%s,%s$ lần lượt là trung điểm của $%s$ và $%s$. \\\\
    Suy ra $%s%s // %s$ (tính chất đường trung bình trong tam giác). \\\\
    Mặt khác: \\\\
    $\\begin{cases} %s%s // %s \\\\ %s \\subset %s \\\\ %s%s \\not\\subset %s \\end{cases} \\Rightarrow %s%s // %s$.'''
                   % (hinh_tikz, p1, p2, c1, c2, p1, p2, canh_day, p1, p2, canh_day, canh_day, mp_song_song, p1, p2, mp_song_song, p1, p2, mp_song_song))

    elif dang == '3':
        # Dạng 3: B', C' lần lượt là trung điểm của SB, SC -> Song song mặt phẳng (SAD)
        p1 = "B'"
        p2 = "C'"
        c1 = "SB"
        c2 = "SC"
        canh_day = "BC"
        mp_song_song = "(SAD)"
        mp_chua = "(SBC)"

        hinh_tikz = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,0);
    \\coordinate (B) at (-1.3,-1.7);
    \\coordinate (C) at (1.8,-1.7);
    \\coordinate (D) at (3.1,0);
    \\coordinate (S) at (0,2.3);
    \\coordinate (B1) at ($(S)!0.5!(B)$);
    \\coordinate (C1) at ($(S)!0.5!(C)$);
    \\draw[line width=1pt] (S)--(B)--(C)--(D)--(S)--(C) (B1)--(C1);
    \\draw[line width=1pt, dashed] (S)--(A)--(B) (A)--(D);
    \\fill (A) circle (1pt) node[left] {$A$};
    \\fill (B) circle (1pt) node[below left] {$B$};
    \\fill (C) circle (1pt) node[below right] {$C$};
    \\fill (D) circle (1pt) node[right] {$D$};
    \\fill (S) circle (1pt) node[above left] {$S$};
    \\fill (B1) circle (1pt) node[left] {$B'$};
    \\fill (C1) circle (1pt) node[right] {$C'$};
    \\end{tikzpicture}
    \\end{center}''')

        da = '$%s$' % (mp_song_song)
        s = [
            '$%s$' % (mp_chua),
            '$(SAB)$',
            '$(ABCD)$',
            '$(SCD)$'
        ]

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành. Gọi $%s,%s$ lần lượt là trung điểm của $%s,%s$. Đường thẳng $%s%s$ song song với mặt phẳng nào dưới đây?'''
                         % (p1, p2, c1, c2, p1, p2))

        loigiai = ('''Ta có: \\\\
    %s
    Xét tam giác $SBC$, ta có $%s,%s$ lần lượt là trung điểm của $%s$ và $%s$. \\\\
    Suy ra $%s%s // %s$. \\\\
    Vì đáy $ABCD$ là hình bình hành nên $%s // AD$. Do đó $%s%s // AD$. \\\\
    Mặt khác: \\\\
    $\\begin{cases} %s%s // AD \\\\ AD \\subset %s \\\\ %s%s \\not\\subset %s \\end{cases} \\Rightarrow %s%s // %s$.'''
                   % (hinh_tikz, p1, p2, c1, c2, p1, p2, canh_day, canh_day, p1, p2, p1, p2, mp_song_song, p1, p2, mp_song_song, p1, p2, mp_song_song))

    # Các đáp án trắc nghiệm
    da_d = ('\\True ' + str(da))
    da_s1 = str(das1)
    da_s2 = str(das2)
    da_s3 = str(das3)

    # Đưa các đáp án vào danh sách chọn ngẫu nhiên
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


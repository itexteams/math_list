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


def bt_dang21_p1_b3_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1', '2']
    dang = random.choice(lisdang)

    if dang == '1':
        # Dạng 1: Giống hệt bài gốc trong ảnh (M, N là trọng tâm tam giác ABC và ABD)
        dinh_chung = "A"
        tg1 = "ABC"
        tg2 = "ABD"
        c_day1 = "BC"
        c_day2 = "BD"
        diem_E = "E"
        diem_F = "F"
        mp_dung = "(BCD)"

        # TikZ vẽ hình tứ diện ABCD cùng trọng tâm M, N giống 100% như ảnh mẫu
        hinh_tikz = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,3);
    \\coordinate (B) at (-1.8,-0.2);
    \\coordinate (C) at (-0.1,-1.6);
    \\coordinate (D) at (2.8,0);
    \\coordinate (E) at ($(B)!0.5!(C)$);
    \\coordinate (F) at ($(B)!0.5!(D)$);
    \\coordinate (M) at ($(A)!0.6667!(E)$);
    \\coordinate (N) at ($(A)!0.6667!(F)$);
    \\draw[line width=1pt] (A)--(B)--(C)--(D)--(A)--(C) (A)--(E);
    \\draw[line width=1pt, dashed] (B)--(D) (A)--(F) (E)--(F) (M)--(N);
    \\fill (A) circle (1pt) node[above] {$A$};
    \\fill (B) circle (1pt) node[below left] {$B$};
    \\fill (C) circle (1pt) node[below] {$C$};
    \\fill (D) circle (1pt) node[right] {$D$};
    \\fill (E) circle (1pt) node[below left] {$E$};
    \\fill (F) circle (1pt) node[below right] {$F$};
    \\fill (M) circle (1pt) node[left] {$M$};
    \\fill (N) circle (1pt) node[right] {$N$};
    \\end{tikzpicture}
    \\end{center}''')

        da = '$%s$' % (mp_dung)

        s = [
            '$(ABC)$',
            '$(ABD)$',
            '$(AMN)$',
            '$(ACD)$'
        ]

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        noidungcauhoi = ('''Cho tứ diện $ABCD$ có $M, N$ lần lượt là trọng tâm tam giác $%s$ và tam giác $%s$. Đường thẳng $MN$ song song với mặt phẳng nào dưới đây?'''
                         % (tg1, tg2))

        loigiai = ('''%s
    Gọi $%s, %s$ lần lượt là trung điểm của $%s$ và $%s$. \\\\
    Ta có $\\frac{%sM}{%s%s} = \\frac{%sN}{%s%s} = \\frac{2}{3} \\Rightarrow MN // %s%s$. \\\\
    Mà $%s%s \\subset %s$, $MN \\not\\subset %s$. \\\\
    Suy ra $MN // %s$.'''
                   % (hinh_tikz, diem_E, diem_F, c_day1, c_day2, dinh_chung, dinh_chung, diem_E, dinh_chung, dinh_chung, diem_F, diem_E, diem_F, diem_E, diem_F, mp_dung, mp_dung, mp_dung))

    elif dang == '2':
        # Dạng 2: M, N là trọng tâm tam giác ABC và ACD (chung đỉnh A, chung đáy BCD)
        dinh_chung = "A"
        tg1 = "ABC"
        tg2 = "ACD"
        c_day1 = "BC"
        c_day2 = "CD"
        diem_E = "E"
        diem_F = "K"
        mp_dung = "(BCD)"

        hinh_tikz = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,3);
    \\coordinate (B) at (-1.8,-0.2);
    \\coordinate (C) at (-0.1,-1.6);
    \\coordinate (D) at (2.8,0);
    \\coordinate (E) at ($(B)!0.5!(C)$);
    \\coordinate (K) at ($(C)!0.5!(D)$);
    \\coordinate (M) at ($(A)!0.6667!(E)$);
    \\coordinate (N) at ($(A)!0.6667!(K)$);
    \\draw[line width=1pt] (A)--(B)--(C)--(D)--(A)--(C) (A)--(E) (A)--(K) (E)--(K) (M)--(N);
    \\draw[line width=1pt, dashed] (B)--(D);
    \\fill (A) circle (1pt) node[above] {$A$};
    \\fill (B) circle (1pt) node[below left] {$B$};
    \\fill (C) circle (1pt) node[below] {$C$};
    \\fill (D) circle (1pt) node[right] {$D$};
    \\fill (E) circle (1pt) node[below left] {$E$};
    \\fill (K) circle (1pt) node[below right] {$K$};
    \\fill (M) circle (1pt) node[left] {$M$};
    \\fill (N) circle (1pt) node[right] {$N$};
    \\end{tikzpicture}
    \\end{center}''')

        da = '$%s$' % (mp_dung)

        s = [
            '$(ABC)$',
            '$(ACD)$',
            '$(AMN)$',
            '$(ABD)$'
        ]

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        noidungcauhoi = ('''Cho tứ diện $ABCD$ có $M, N$ lần lượt là trọng tâm tam giác $%s$ và tam giác $%s$. Đường thẳng $MN$ song song với mặt phẳng nào dưới đây?'''
                         % (tg1, tg2))

        loigiai = ('''%s
    Gọi $%s, %s$ lần lượt là trung điểm của $%s$ và $%s$. \\\\
    Ta có $\\frac{%sM}{%s%s} = \\frac{%sN}{%s%s} = \\frac{2}{3} \\Rightarrow MN // %s%s$. \\\\
    Mà $%s%s \\subset %s$, $MN \\not\\subset %s$. \\\\
    Suy ra $MN // %s$.'''
                   % (hinh_tikz, diem_E, diem_F, c_day1, c_day2, dinh_chung, dinh_chung, diem_E, dinh_chung, dinh_chung, diem_F, diem_E, diem_F, diem_E, diem_F, mp_dung, mp_dung, mp_dung))

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


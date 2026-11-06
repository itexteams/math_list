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


def bt_dang25_p1_b3_c1_hh11(self):
    # Khai báo danh sách dạng bài (ngẫu nhiên hóa giữa cặp mặt phẳng (SAD) & (SBC) hoặc (SAB) & (SCD))
    lisdang = ['1', '2']
    dang = random.choice(lisdang)

    if dang == '1':
        # Giao tuyến của (SAD) và (SBC)
        mp1 = '(SAD)'
        mp2 = '(SBC)'
        canh_songsong_1 = 'AD'
        canh_songsong_2 = 'BC'

        # Đáp án đúng có thể chọn ngẫu nhiên là AD hoặc BC
        da_dung_val = random.choice([canh_songsong_1, canh_songsong_2])
        da = '$%s$' % (da_dung_val)

        # Tập hợp các phương án gây nhiễu
        cac_canh_khac = ['AC', 'BD', 'DC', 'AB', 'SA', 'SB', 'SC', 'SD']
        s = ['$%s$' % c for c in cac_canh_khac if c != da_dung_val]

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        # Câu hỏi
        noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có mặt đáy $ABCD$ là hình bình hành. Giao tuyến của hai mặt phẳng $%s$ và $%s$ là đường thẳng song song với đường thẳng nào sau đây?'''
                         % (mp1, mp2))

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        # Đưa các đáp án vào danh sách và xáo trộn
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải kèm hình vẽ TikZ đúng 100% mẫu hình
        loigiai = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,0);
    \\coordinate (B) at (3,0);
    \\coordinate (D) at (1.3,1);
    \\coordinate (C) at (4.3,1);
    \\coordinate (S) at (1.7,3.5);
    \\coordinate (d1) at ($(S)!-0.6!(D)-(A)+(S)$);
    \\coordinate (d2) at ($(S)!0.8!(D)-(A)+(S)$);
    \\draw[line width=1pt] (A)--(B)--(C) (S)--(A) (S)--(B) (S)--(C);
    \\draw[line width=1pt, dashed] (A)--(D)--(C) (S)--(D);
    \\draw[line width=1pt] ($(S)!-0.5!(0.2,1.3)$) -- ($(S)!1.5!(0.2,1.3)$) node[left] {$d$};
    \\fill (A) circle (1pt) node[below left] {$A$};
    \\fill (B) circle (1pt) node[below] {$B$};
    \\fill (C) circle (1pt) node[right] {$C$};
    \\fill (D) circle (1pt) node[below] {$D$};
    \\fill (S) circle (1pt) node[above] {$S$};
    \\end{tikzpicture}
    \\end{center}
    Giao tuyến của 2 mặt phẳng chứa 2 đường thẳng song song với nhau là đường thẳng đi qua 1 điểm chung của 2 mặt phẳng đó và song song với 2 đường thẳng song song trên.\\\\
    Ta có: $\\begin{cases} %s // %s \\\\ %s \\subset %s \\\\ %s \\subset %s \\\\ S \\in %s \\cap %s \\end{cases}$. Suy ra $d = %s \\cap %s$ với $S \\in d$ và $d // %s // %s$.'''
                   % (canh_songsong_1, canh_songsong_2,
                      canh_songsong_1, mp1,
                      canh_songsong_2, mp2,
                      mp1, mp2,
                      mp1, mp2,
                      canh_songsong_1, canh_songsong_2))

    elif dang == '2':
        # Giao tuyến của (SAB) và (SCD)
        mp1 = '(SAB)'
        mp2 = '(SCD)'
        canh_songsong_1 = 'AB'
        canh_songsong_2 = 'CD'

        # Đáp án đúng có thể chọn ngẫu nhiên là AB hoặc CD
        da_dung_val = random.choice([canh_songsong_1, canh_songsong_2])
        da = '$%s$' % (da_dung_val)

        cac_canh_khac = ['AC', 'BD', 'AD', 'BC', 'SA', 'SB', 'SC', 'SD']
        s = ['$%s$' % c for c in cac_canh_khac if c != da_dung_val]

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        # Câu hỏi
        noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có mặt đáy $ABCD$ là hình bình hành. Giao tuyến của hai mặt phẳng $%s$ và $%s$ là đường thẳng song song với đường thẳng nào sau đây?'''
                         % (mp1, mp2))

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        # Đưa các đáp án vào danh sách và xáo trộn
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải
        loigiai = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,0);
    \\coordinate (B) at (3,0);
    \\coordinate (D) at (1.3,1);
    \\coordinate (C) at (4.3,1);
    \\coordinate (S) at (1.7,3.5);
    \\draw[line width=1pt] (A)--(B)--(C) (S)--(A) (S)--(B) (S)--(C);
    \\draw[line width=1pt, dashed] (A)--(D)--(C) (S)--(D);
    \\draw[line width=1pt] ($(S)+(-1.5,0)$) -- ($(S)+(1.5,0)$) node[right] {$d$};
    \\fill (A) circle (1pt) node[below left] {$A$};
    \\fill (B) circle (1pt) node[below] {$B$};
    \\fill (C) circle (1pt) node[right] {$C$};
    \\fill (D) circle (1pt) node[below] {$D$};
    \\fill (S) circle (1pt) node[above] {$S$};
    \\end{tikzpicture}
    \\end{center}
    Giao tuyến của 2 mặt phẳng chứa 2 đường thẳng song song với nhau là đường thẳng đi qua 1 điểm chung của 2 mặt phẳng đó và song song với 2 đường thẳng song song trên.\\\\
    Ta có: $\\begin{cases} %s // %s \\\\ %s \\subset %s \\\\ %s \\subset %s \\\\ S \\in %s \\cap %s \\end{cases}$. Suy ra $d = %s \\cap %s$ với $S \\in d$ và $d // %s // %s$.'''
                   % (canh_songsong_1, canh_songsong_2,
                      canh_songsong_1, mp1,
                      canh_songsong_2, mp2,
                      mp1, mp2,
                      mp1, mp2,
                      canh_songsong_1, canh_songsong_2))

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


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


def bt_dang20_p1_b3_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1', '2']
    dang = random.choice(lisdang)

    # TikZ vẽ hình chóp S.ABCD đáy hình bình hành đúng 100% như hình mẫu
    hinh_tikz = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,0);
    \\coordinate (B) at (-1.3,-1.7);
    \\coordinate (C) at (2.2,-1.7);
    \\coordinate (D) at (3.5,0);
    \\coordinate (S) at (0.6,2.6);
    \\draw[line width=1pt] (S)--(B)--(C)--(D)--(S)--(C);
    \\draw[line width=1pt, dashed] (S)--(A)--(B) (A)--(D);
    \\fill (A) circle (1pt) node[left] {$A$};
    \\fill (B) circle (1pt) node[below left] {$B$};
    \\fill (C) circle (1pt) node[below right] {$C$};
    \\fill (D) circle (1pt) node[right] {$D$};
    \\fill (S) circle (1pt) node[above] {$S$};
    \\end{tikzpicture}
    \\end{center}''')

    if dang == '1':
        # Dạng 1: Giống ảnh gốc - Xét giao tuyến của (SAB) và (SCD)
        mp1 = "SAB"
        mp2 = "SCD"
        c1 = "AB"
        c2 = "CD"

        # Đáp án đúng có thể chọn hiển thị là AB hoặc CD
        da_dung_val = random.choice([c1, c2])
        da = '$%s$' % (da_dung_val)

        # Danh sách các phương án sai (không được trùng với c1, c2)
        s = [
            '$AD$',
            '$BC$',
            '$BD$',
            '$AC$',
            '$SA$',
            '$SB$'
        ]

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành. Giao tuyến của hai mặt phẳng $(%s)$ và $(%s)$ song song với đường thẳng nào sau đây?'''
                         % (mp1, mp2))

        loigiai = ('''%s
    Ta có: \\\\
    $\\left\\{\\begin{array}{l} S \\in (%s) \\cap (%s) \\\\ %s \\subset (%s) \\\\ %s \\subset (%s) \\\\ %s // %s \\end{array}\\right. \\Rightarrow$ Giao tuyến của hai mặt phẳng $(%s)$ và $(%s)$ là đường thẳng đi qua $S$ và song song với các đường thẳng $%s$ và $%s$. \\\\
    Do đó, giao tuyến song song với $%s$.'''
                   % (hinh_tikz, mp1, mp2, c1, mp1, c2, mp2, c1, c2, mp1, mp2, c1, c2, da_dung_val))

    elif dang == '2':
        # Dạng 2: Xét giao tuyến của cặp mặt phẳng đối diện còn lại (SAD) và (SBC)
        mp1 = "SAD"
        mp2 = "SBC"
        c1 = "AD"
        c2 = "BC"

        # Đáp án đúng có thể chọn hiển thị là AD hoặc BC
        da_dung_val = random.choice([c1, c2])
        da = '$%s$' % (da_dung_val)

        # Danh sách các phương án sai (không được trùng với c1, c2)
        s = [
            '$AB$',
            '$CD$',
            '$BD$',
            '$AC$',
            '$SC$',
            '$SD$'
        ]

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành. Giao tuyến của hai mặt phẳng $(%s)$ và $(%s)$ song song với đường thẳng nào sau đây?'''
                         % (mp1, mp2))

        loigiai = ('''%s
    Ta có: \\\\
    $\\left\\{\\begin{array}{l} S \\in (%s) \\cap (%s) \\\\ %s \\subset (%s) \\\\ %s \\subset (%s) \\\\ %s // %s \\end{array}\\right. \\Rightarrow$ Giao tuyến của hai mặt phẳng $(%s)$ và $(%s)$ là đường thẳng đi qua $S$ và song song với các đường thẳng $%s$ và $%s$. \\\\
    Do đó, giao tuyến song song với $%s$.'''
                   % (hinh_tikz, mp1, mp2, c1, mp1, c2, mp2, c1, c2, mp1, mp2, c1, c2, da_dung_val))

    # Các đáp án trắc nghiệm
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


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


def bt_dang25_p1_b2_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Cố định các đỉnh và điểm theo đề bài gốc
        v1, v2, v3, v4 = 'S', 'A', 'B', 'C'
        pE, pF, pG = 'E', 'F', 'G'

        # Nội dung câu hỏi
        noidungcauhoi = (
            f'Cho tứ diện ${v1}{v2}{v3}{v4}$. Gọi ${pE}$ và ${pF}$ lần lượt là trung điểm của các cạnh '
            f'${v1}{v3}$ và ${v2}{v3}$, ${pG}$ là một điểm trên cạnh ${v2}{v4}$. '
            f'Giao tuyến của hai mặt phẳng $({v1}{v2}{v4})$ và $({pE}{pF}{pG})$ song song với đường thẳng nào sau đây?'
        )

        # Các đáp án trắc nghiệm
        da_d = f'\\True ${v1}{v2}$'
        da_s1 = f'${v1}{v4}$'
        da_s2 = f'${v2}{v3}$'
        da_s3 = f'${v1}{v3}$'

        # Trộn ngẫu nhiên các phương án
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải kèm hình vẽ TikZ chuẩn theo các đỉnh S, A, B, C, E, F, G
        loigiai = (
            f'\\begin{{center}}\n'
            f'\\begin{{tikzpicture}}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
            f'\\coordinate (A) at (0,2);\n'
            f'\\coordinate (B) at (2.2,0);\n'
            f'\\coordinate (C) at (5.2,2);\n'
            f'\\coordinate (S) at (2.5,5.5);\n'
            f'\\coordinate (E) at ($(S)!0.5!(B)$);\n'
            f'\\coordinate (F) at ($(A)!0.5!(B)$);\n'
            f'\\coordinate (G) at ($(A)!0.7!(C)$);\n'
            f'\\coordinate (I) at ($(C)!0.3!(S)$);\n'
            f'\\coordinate (X) at ($(G)!1.3!(I)$);\n'
            f'\\coordinate (Gdown) at ($(I)!1.3!(G)$);\n'
            f'\\draw[line width=1pt] (S)--(A) (S)--(B) (S)--(C) (A)--(B) (B)--(C) (F)--(E) (I)--(X);\n'
            f'\\draw[line width=1pt, dashed] (A)--(C) (F)--(G) (E)--(G) (Gdown)--(I);\n'
            f'\\fill (A) circle (1pt) node[left] {{${v2}$}};\n'
            f'\\fill (B) circle (1pt) node[below] {{${v3}$}};\n'
            f'\\fill (C) circle (1pt) node[right] {{${v4}$}};\n'
            f'\\fill (S) circle (1pt) node[above] {{${v1}$}};\n'
            f'\\fill (E) circle (1pt) node[right] {{${pE}$}};\n'
            f'\\fill (F) circle (1pt) node[below left] {{${pF}$}};\n'
            f'\\fill (G) circle (1pt) node[above] {{${pG}$}};\n'
            f'\\node at (X) [right] {{$x$}};\n'
            f'\\end{{tikzpicture}}\n'
            f'\\end{{center}}\n'
            f'Xét tam giác ${v1}{v2}{v3}$, có ${pE}{pF}$ là đường trung bình nên ${pE}{pF} // {v1}{v2}$. \\\\\n'
            f'Ta có: $\\begin{{cases}} {pG} \\in ({pE}{pF}{pG}) \\cap ({v1}{v2}{v4}) \\\\ '
            f'{pE}{pF} // {v1}{v2} \\\\ '
            f'{pE}{pF} \\subset ({pE}{pF}{pG}), \\ {v1}{v2} \\subset ({v1}{v2}{v4}) '
            f'\\end{{cases}} \\Rightarrow ({pE}{pF}{pG}) \\cap ({v1}{v2}{v4}) = {pG}x$ '
            f'với ${pG}x // {pE}{pF} // {v1}{v2}$.'
        )

    # Xuất câu trắc nghiệm
    content = (
        '\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
        '\\choice \n'
        '{' + str(list_1[1]) + '}\n'
        '{' + str(list_1[2]) + '}\n'
        '{' + str(list_1[3]) + '}\n'
        '{' + str(list_1[0]) + '}\n'
        '\\loigiai{' + str(loigiai) + '}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content


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


def bt_dang11_p3_b4_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Theo đề bài gốc:
        # M là trung điểm SC => H là trọng tâm tam giác SAC nên HO/HS = 1/2
        # N là trung điểm OB => ND/NO = (OD + ON)/ON = (2*ON + ON)/ON = 3
        # Khi đó ID/IS = (ND/NO) * (HO/HS) = 3 * (1/2) = 3/2 => SI/ID = 2/3
        val = Decimal(2) / Decimal(3)
        kq = val.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        kq_str = str(kq).replace('.', ',')

        # Hình vẽ TikZ vẽ đúng 100% như ảnh, nét 1pt, điểm 1pt, màu black, không lưới kẻ ô
        hinhve = (
            "\\begin{center}\n"
            "        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n"
            "        \\coordinate (S) at (1.0, 4.5);\n"
            "        \\coordinate (D) at (0.0, 0.0);\n"
            "        \\coordinate (C) at (5.0, 0.0);\n"
            "        \\coordinate (A) at (2.0, 1.5);\n"
            "        \\coordinate (B) at (7.0, 1.5);\n"
            "        \\coordinate (O) at (3.5, 0.75);\n"
            "        \\coordinate (M) at ($(S)!0.5!(C)$);\n"
            "        \\coordinate (N) at ($(O)!0.5!(B)$);\n"
            "        \\coordinate (H) at (intersection of S--O and A--M);\n"
            "        \\coordinate (I) at (intersection of S--D and N--H);\n"
            "        \\coordinate (E) at ($(N)!0.45!(H)$);\n"
            "        \\draw[line width=1pt] (S)--(D)--(C)--(B)--(S) (S)--(C);\n"
            "        \\draw[line width=1pt, dashed] (D)--(A)--(B) (S)--(A) (A)--(C) (B)--(D) (S)--(O) (A)--(M) (I)--(N) (A)--(N) (O)--(E);\n"
            "        \\fill (S) circle (1pt) node[above right] {$S$};\n"
            "        \\fill (D) circle (1pt) node[below left] {$D$};\n"
            "        \\fill (C) circle (1pt) node[below right] {$C$};\n"
            "        \\fill (A) circle (1pt) node[above right] {$A$};\n"
            "        \\fill (B) circle (1pt) node[above right] {$B$};\n"
            "        \\fill (O) circle (1pt) node[below left] {$O$};\n"
            "        \\fill (M) circle (1pt) node[above right] {$M$};\n"
            "        \\fill (N) circle (1pt) node[above right] {$N$};\n"
            "        \\fill (H) circle (1pt) node[above left] {$H$};\n"
            "        \\fill (I) circle (1pt) node[left] {$I$};\n"
            "        \\fill (E) circle (1pt) node[above right] {$E$};\n"
            "        \\end{tikzpicture}\n"
            "        \\end{center}"
        )

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành. Gọi $M, N$ lần lượt là trung điểm của các $SC, OB$ với $O = AC \\cap BD$; $I = SD \\cap (AMN)$. Tỉ số $\\frac{SI}{ID}$ bằng bao nhiêu? (kết quả làm tròn đến hàng phần trăm). ''')

        # Nội dung lời giải
        loigiai = ('''Trong $(SAC)$, gọi $H = SO \\cap AM \\Rightarrow H$ là trọng tâm $\\Delta SAC$.\\\\
    Trong $(SBD)$:\\\\
    $\\begin{cases} I = NH \\cap SD \\\\ I \\in NH \\subset (AMN) \\Rightarrow I \\in (AMN) \\\\ I \\in SD \\end{cases}$\\\\
    $\\Rightarrow I = SD \\cap (AMN)$.\\\\
    Kẻ $OE // SD$. Theo định lý Thales, ta có:\\\\
    $\\frac{ND}{NO} = \\frac{ID}{OE}$. (1)\\\\
    $\\frac{HO}{HS} = \\frac{OE}{IS}$. (2)\\\\
    Ta có (1) $\\cdot$ (2):\\\\
    $\\frac{ND}{NO} \\cdot \\frac{HO}{HS} = \\frac{ID}{OE} \\cdot \\frac{OE}{IS}$\\\\
    $\\Leftrightarrow \\frac{ND}{NO} \\cdot \\frac{HO}{HS} = \\frac{ID}{IS}$\\\\
    $\\Leftrightarrow 3 \\cdot \\frac{1}{2} = \\frac{ID}{IS}$\\\\
    $\\Leftrightarrow \\frac{SI}{ID} = \\frac{2}{3} \\approx %s$.\\\\
    Vậy tỉ số $\\frac{SI}{ID} \\approx %s$.'''
                   % (kq_str, kq_str)
                   )

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = (
        '\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) +
        '\\loigiai{ \n' + str(loigiai) + '}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content


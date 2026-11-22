
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


def bt_dang30_p4_b1_c2_hh10(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        bo_dinh = random.choice([('A', 'B', 'C'), ('E', 'F', 'G'), ('P', 'Q', 'R')])
        pA, pB, pC = bo_dinh
        pO = random.choice(['O', 'K'])
        pI = random.choice(['I', 'J'])
        pM = random.choice(['M', 'N'])
        line_d = random.choice(['d', '\\Delta'])
        vec_v = random.choice(['v', 'u'])
        k = randint(1, 3)
        sk = '' if k == 1 else str(k)
        s2k = str(2 * k)
        s4k = str(4 * k)
        if k == 1:
            buoc_tach = f'\\overrightarrow{{{pO}{pA}}} - \\overrightarrow{{{pO}{pM}}} + \\overrightarrow{{{pO}{pB}}} - \\overrightarrow{{{pO}{pM}}} + 2\\left(\\overrightarrow{{{pO}{pC}}} - \\overrightarrow{{{pO}{pM}}}\\right)'
        else:
            buoc_tach = f'{sk}\\left(\\overrightarrow{{{pO}{pA}}} - \\overrightarrow{{{pO}{pM}}}\\right) + {sk}\\left(\\overrightarrow{{{pO}{pB}}} - \\overrightarrow{{{pO}{pM}}}\\right) + {s2k}\\left(\\overrightarrow{{{pO}{pC}}} - \\overrightarrow{{{pO}{pM}}}\\right)'
        noidungcauhoi = ('Cho tam giác $%s%s%s$ và đường thẳng $%s$. Gọi $%s$ là điểm thỏa mãn hệ thức $%s\\overrightarrow{%s%s} + %s\\overrightarrow{%s%s} + %s\\overrightarrow{%s%s} = \\overrightarrow{0}$. Tìm điểm $%s$ trên đường thẳng $%s$ sao cho vectơ $\\vec{%s} = %s\\overrightarrow{%s%s} + %s\\overrightarrow{%s%s} + %s\\overrightarrow{%s%s}$ có độ dài nhỏ nhất. \n'
                         %(pA, pB, pC, line_d, pO, sk, pO, pA, sk, pO, pB, s2k, pO, pC, pM, line_d, vec_v, sk, pM, pA, sk, pM, pB, s2k, pM, pC))
        loigiai = ('\\begin{center} \n'
                   '\\begin{tikzpicture}[line width=1pt, scale=0.8] \n'
                   '\\coordinate (B) at (0,0); \n'
                   '\\coordinate (C) at (4,0); \n'
                   '\\coordinate (A) at (1,3); \n'
                   '\\coordinate (I) at (0.5,1.5); \n'
                   '\\coordinate (O) at (2.25,0.75); \n'
                   '\\coordinate (M) at (3.75,1.95); \n'
                   '\\draw (A) -- (B) -- (C) -- cycle; \n'
                   '\\draw (I) -- (C) (O) -- (M); \n'
                   '\\draw (2.55,3.45) node[right] {$%s$} -- (5.35,-0.05); \n'
                   '\\fill (A) circle (1.5pt) node[above] {$%s$}; \n'
                   '\\fill (B) circle (1.5pt) node[left] {$%s$}; \n'
                   '\\fill (C) circle (1.5pt) node[right] {$%s$}; \n'
                   '\\fill (I) circle (1.5pt) node[left] {$%s$}; \n'
                   '\\fill (O) circle (1.5pt) node[below] {$%s$}; \n'
                   '\\fill (M) circle (1.5pt) node[above right] {$%s$}; \n'
                   '\\end{tikzpicture} \n'
                   '\\end{center} \n'
                   'Gọi $%s$ là trung điểm của $%s%s$. \\\\ \n'
                   'Khi đó: $%s\\overrightarrow{%s%s} + %s\\overrightarrow{%s%s} + %s\\overrightarrow{%s%s} = \\overrightarrow{0} \\Leftrightarrow %s\\overrightarrow{%s%s} + %s\\overrightarrow{%s%s} = \\overrightarrow{0} \\Leftrightarrow \\overrightarrow{%s%s} + \\overrightarrow{%s%s} = \\overrightarrow{0} \\Rightarrow %s$ là trung điểm của $%s%s$. \\\\ \n'
                   'Ta có: $\\vec{%s} = %s\\overrightarrow{%s%s} + %s\\overrightarrow{%s%s} + %s\\overrightarrow{%s%s} = %s = %s\\overrightarrow{%s%s} + %s\\overrightarrow{%s%s} + %s\\overrightarrow{%s%s} - %s\\overrightarrow{%s%s} = -%s\\overrightarrow{%s%s}$. \\\\ \n'
                   'Do đó $\\left|\\vec{%s}\\right| = %s%s%s$ nên độ dài vectơ $\\vec{%s}$ nhỏ nhất khi và chỉ khi $%s%s%s$ nhỏ nhất. \\\\ \n'
                   'Hay $%s$ là hình chiếu vuông góc của $%s$ trên $%s$. \n'
                   %(line_d, pA, pB, pC, pI, pO, pM,
                     pI, pA, pB,
                     sk, pO, pA, sk, pO, pB, s2k, pO, pC, s2k, pO, pI, s2k, pO, pC, pO, pI, pO, pC, pO, pI, pC,
                     vec_v, sk, pM, pA, sk, pM, pB, s2k, pM, pC, buoc_tach, sk, pO, pA, sk, pO, pB, s2k, pO, pC, s4k, pO, pM, s4k, pO, pM,
                     vec_v, s4k, pO, pM, vec_v, s4k, pO, pM,
                     pM, pO, line_d))
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
    return content

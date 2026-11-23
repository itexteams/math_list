
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


def bt_dang20_p4_b3_c2_hh10(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        bo_ten = [
            ('A', 'B', 'C', "B'", "C'", 'D'),
            ('M', 'N', 'P', "N'", "P'", 'Q'),
            ('D', 'E', 'F', "E'", "F'", 'K')
        ]
        A, B, C, Bp, Cp, D = random.choice(bo_ten)
        tamgiac = A + B + C
        a_sym = symbols('a', positive=True)
        k = randint(1, 3)
        canh_val = k * a_sym
        m = randint(2, 5)
        n = random.choice([-5, -4, -3, -2, -1, 2, 3, 4, 5])
        if n == -1:
            sign_n = '-'
            hn = ''
            n_str = '-'
        elif n < -1:
            sign_n = '-'
            hn = str(abs(n))
            n_str = str(n)
        else:
            sign_n = '+'
            hn = str(n)
            n_str = str(n)
        bt_vec = f'{m}\\overrightarrow{{{A}{B}}} {sign_n} {hn}\\overrightarrow{{{A}{C}}}'
        abp_sq = (m * k)**2 * a_sym**2
        acp_sq = (abs(n) * k)**2 * a_sym**2
        kq_val = simplify(sqrt(abp_sq + acp_sq))
        xBp = round(1.2 + 0.9 * (m - 1), 2)
        if n < 0:
            yCp = round(-1.2 - 0.35 * (abs(n) - 1), 2)
            pos_B = 'above right'
            pos_C = 'above'
            pos_Bp = 'above'
            pos_Cp = 'left'
            pos_D = 'right'
        else:
            yCp = round(1.2 + 0.55 * (n - 1), 2)
            pos_B = 'below'
            pos_C = 'left'
            pos_Bp = 'below'
            pos_Cp = 'above'
            pos_D = 'above right'
        hinhve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[line width=1pt, scale=1]\n'
            f'\\coordinate (A) at (0,0);\n'
            f'\\coordinate (B) at (1.2,0);\n'
            f'\\coordinate (C) at (0,1.2);\n'
            f'\\coordinate (Bp) at ({xBp},0);\n'
            f'\\coordinate (Cp) at (0,{yCp});\n'
            f'\\coordinate (D) at ({xBp},{yCp});\n'
            '\\draw (C)--(A)--(B)--cycle;\n'
            '\\draw (A)--(Bp)--(D)--(Cp)--cycle;\n'
            '\\draw (A)--(D);\n'
            f'\\fill (A) circle (1.5pt) node[left] {{${A}$}};\n'
            f'\\fill (B) circle (1.5pt) node[{pos_B}] {{${B}$}};\n'
            f'\\fill (C) circle (1.5pt) node[{pos_C}] {{${C}$}};\n'
            f'\\fill (Bp) circle (1.5pt) node[{pos_Bp}] {{${Bp}$}};\n'
            f'\\fill (Cp) circle (1.5pt) node[{pos_Cp}] {{${Cp}$}};\n'
            f'\\fill (D) circle (1.5pt) node[{pos_D}] {{${D}$}};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}\n'
        )
        noidungcauhoi = f'Tam giác ${tamgiac}$ vuông cân tại ${A}$, ${A}{B} = {latex(canh_val)}$. Tính độ dài vectơ ${bt_vec}$.\n'
        loigiai = (
            hinhve +
            f'Vẽ $\\overrightarrow{{{A}{Bp}}} = {m}\\overrightarrow{{{A}{B}}}$; $\\overrightarrow{{{A}{Cp}}} = {n_str}\\overrightarrow{{{A}{C}}}$ và hình bình hành ${A}{Cp}{D}{Bp}$.\\\\\n'
            f'Ta có: $\\left|{bt_vec}\\right| = \\left|\\overrightarrow{{{A}{Bp}}} + \\overrightarrow{{{A}{Cp}}}\\right| = \\left|\\overrightarrow{{{A}{D}}}\\right| = {A}{D}$.\\\\\n'
            f'Do đó: ${A}{D} = \\sqrt{{{A}{Bp}^2 + {A}{Cp}^2}} = \\sqrt{{{latex(abp_sq)} + {latex(acp_sq)}}} = {latex(kq_val)}$.\n'
        )
        noidungcauhoi = noidungcauhoi.replace('- -', '+').replace('+ -', '-')
        loigiai = loigiai.replace('- -', '+').replace('+ -', '-')
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
    return content

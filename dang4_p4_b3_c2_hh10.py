
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


def bt_dang4_p4_b3_c2_hh10(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        bo_ten = [
            ('A', 'B', 'C', 'D', 'O', 'I'),
            ('M', 'N', 'P', 'Q', 'O', 'K'),
            ('E', 'F', 'G', 'H', 'O', 'M')
        ]
        A, B, C, D, O, I = random.choice(bo_ten)
        hinh_name = A + B + C + D
        ab = randint(2, 12)
        ad = randint(2, 12)
        while ab == ad:
            ad = randint(2, 12)
        kieu = random.choice([1, 2, 3, 4])
        if kieu == 1:
            bieuthuc = f'\\left|\\overrightarrow{{{A}{C}}} + \\overrightarrow{{{B}{D}}}\\right|'
            canh_td = f'{D}{C}'
            v1, v2 = f'{O}{C}', f'{O}{D}'
            canh_ss = f'{B}{C}'
            giatri_ss = ad
            kq = 2 * ad
            toa_do_I = '(2,0)'
            pos_I = 'below'
            pos_O = 'left'
            buoc_dau = f'{bieuthuc} = \\left|2\\overrightarrow{{{v1}}} + 2\\overrightarrow{{{v2}}}\\right|'
        elif kieu == 2:
            bieuthuc = f'\\left|\\overrightarrow{{{C}{A}}} + \\overrightarrow{{{D}{B}}}\\right|'
            canh_td = f'{A}{B}'
            v1, v2 = f'{O}{A}', f'{O}{B}'
            canh_ss = f'{A}{D}'
            giatri_ss = ad
            kq = 2 * ad
            toa_do_I = '(2,3)'
            pos_I = 'above'
            pos_O = 'below'
            buoc_dau = f'{bieuthuc} = \\left|2\\overrightarrow{{{v1}}} + 2\\overrightarrow{{{v2}}}\\right|'
        elif kieu == 3:
            bieuthuc = f'\\left|\\overrightarrow{{{A}{C}}} - \\overrightarrow{{{B}{D}}}\\right|'
            canh_td = f'{B}{C}'
            v1, v2 = f'{O}{C}', f'{O}{B}'
            canh_ss = f'{A}{B}'
            giatri_ss = ab
            kq = 2 * ab
            toa_do_I = '(4,1.5)'
            pos_I = 'right'
            pos_O = 'left'
            buoc_dau = f'{bieuthuc} = \\left|\\overrightarrow{{{A}{C}}} + \\overrightarrow{{{D}{B}}}\\right| = \\left|2\\overrightarrow{{{v1}}} + 2\\overrightarrow{{{v2}}}\\right|'
        else:
            bieuthuc = f'\\left|\\overrightarrow{{{B}{D}}} - \\overrightarrow{{{A}{C}}}\\right|'
            canh_td = f'{A}{D}'
            v1, v2 = f'{O}{D}', f'{O}{A}'
            canh_ss = f'{A}{B}'
            giatri_ss = ab
            kq = 2 * ab
            toa_do_I = '(0,1.5)'
            pos_I = 'left'
            pos_O = 'right'
            buoc_dau = f'{bieuthuc} = \\left|\\overrightarrow{{{B}{D}}} + \\overrightarrow{{{C}{A}}}\\right| = \\left|2\\overrightarrow{{{v1}}} + 2\\overrightarrow{{{v2}}}\\right|'
        pos_ab = 'above' if kieu != 2 else 'below'
        pos_ad = 'left' if kieu != 4 else 'right'
        hinhve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[line width=1pt, scale=1]\n'
            '\\coordinate (D) at (0,0);\n'
            '\\coordinate (C) at (4,0);\n'
            '\\coordinate (B) at (4,3);\n'
            '\\coordinate (A) at (0,3);\n'
            '\\coordinate (O) at (2,1.5);\n'
            f'\\coordinate (I) at {toa_do_I};\n'
            '\\draw (A)--(B)--(C)--(D)--cycle;\n'
            '\\draw (A)--(C) (B)--(D) (O)--(I);\n'
            '\\draw (0,2.75)--(0.25,2.75)--(0.25,3);\n'
            '\\draw (3.75,3)--(3.75,2.75)--(4,2.75);\n'
            '\\draw (3.75,0)--(3.75,0.25)--(4,0.25);\n'
            '\\draw (0,0.25)--(0.25,0.25)--(0.25,0);\n'
            f'\\fill (A) circle (1.5pt) node[above left] {{${A}$}};\n'
            f'\\fill (B) circle (1.5pt) node[above right] {{${B}$}};\n'
            f'\\fill (C) circle (1.5pt) node[below right] {{${C}$}};\n'
            f'\\fill (D) circle (1.5pt) node[below left] {{${D}$}};\n'
            f'\\fill (O) circle (1.5pt) node[{pos_O}] {{${O}$}};\n'
            f'\\fill (I) circle (1.5pt) node[{pos_I}] {{${I}$}};\n'
            f'\\path (A)--(B) node[pos=0.25, {pos_ab}] {{${ab}$}};\n'
            f'\\path (A)--(D) node[pos=0.25, {pos_ad}] {{${ad}$}};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}\n'
        )
        noidungcauhoi = f'Cho hình chữ nhật ${hinh_name}$ tâm ${O}$ có ${A}{B} = {ab}, {A}{D} = {ad}$. Tính ${bieuthuc}$.\n'
        loigiai = (
            hinhve +
            f'Gọi ${I}$ là trung điểm của ${canh_td}$ thì ta có ${buoc_dau} = \\left|2\\left(\\overrightarrow{{{v1}}} + \\overrightarrow{{{v2}}}\\right)\\right| = 2\\left|\\overrightarrow{{{v1}}} + \\overrightarrow{{{v2}}}\\right|$.\\\\\n'
            f'$\\Rightarrow {bieuthuc} = 2\\left|2\\overrightarrow{{{O}{I}}}\\right| = 4{O}{I} = 2{canh_ss} = 2\\cdot {giatri_ss} = {kq}$.\n'
        )
        noidungcauhoi = noidungcauhoi.replace('- -', '+').replace('+ -', '-')
        loigiai = loigiai.replace('- -', '+').replace('+ -', '-')
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
    return content


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


def bt_dang17_p4_b3_c2_hh10(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        bo_ten = [
            ('A', 'B', 'C', 'D', 'M', 'N', 'I'),
            ('A', 'B', 'C', 'D', 'E', 'F', 'I'),
            ('M', 'N', 'P', 'Q', 'E', 'F', 'K')
        ]
        A, B, C, D, M, N, I = random.choice(bo_ten)
        hinh_name = A + B + C + D
        a_sym = symbols('a', positive=True)
        p = randint(1, 5)
        q = randint(p + 1, 7)
        AB_val = p * a_sym
        CD_val = q * a_sym
        MI_val = simplify(CD_val / 2)
        MN_val = simplify((AB_val + CD_val) / 2)
        tiso_MI = Rational(q, p + q)
        dau = random.choice([-1, 1])
        dau_str = '-' if dau == -1 else '+'
        heso_MN = 2 * tiso_MI + dau
        kq_val = simplify(heso_MN * MN_val)
        ab_len = max(1.3, min(3.8, round(5.0 * p / q, 2)))
        bx = round(0.7 + ab_len, 2)
        nx = round((bx + 5.0) / 2, 2)
        hinhve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[line width=1pt, scale=1]\n'
            f'\\coordinate ({D}) at (0,0);\n'
            f'\\coordinate ({C}) at (5,0);\n'
            f'\\coordinate ({A}) at (0.7,2);\n'
            f'\\coordinate ({B}) at ({bx},2);\n'
            f'\\coordinate ({M}) at (0.35,1);\n'
            f'\\coordinate ({N}) at ({nx},1);\n'
            f'\\coordinate ({I}) at (2.85,1);\n'
            f'\\draw ({A})--({B})--({C})--({D})--cycle;\n'
            f'\\draw ({A})--({C}) ({M})--({N});\n'
            f'\\fill ({A}) circle (1.5pt) node[above] {{${A}$}};\n'
            f'\\fill ({B}) circle (1.5pt) node[above] {{${B}$}};\n'
            f'\\fill ({C}) circle (1.5pt) node[right] {{${C}$}};\n'
            f'\\fill ({D}) circle (1.5pt) node[left] {{${D}$}};\n'
            f'\\fill ({M}) circle (1.5pt) node[left] {{${M}$}};\n'
            f'\\fill ({N}) circle (1.5pt) node[right] {{${N}$}};\n'
            f'\\fill ({I}) circle (1.5pt) node[above right] {{${I}$}};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}\n'
        )
        ab_s = latex(AB_val)
        cd_s = latex(CD_val)
        mi_s = latex(MI_val)
        mn_s = latex(MN_val)
        tiso_s = latex(tiso_MI)
        heso_s = '' if heso_MN == 1 else latex(heso_MN)
        heso_mul = '' if heso_MN == 1 else latex(heso_MN) + '\\cdot'
        kq_s = latex(kq_val)
        noidungcauhoi = f'Cho hình thang ${hinh_name}$ có 2 đáy là ${A}{B} = {ab_s}$ và ${C}{D} = {cd_s}$. Gọi ${M}, {N}$ lần lượt là trung điểm của ${A}{D}$ và ${B}{C}$. Tính $\\left|\\overrightarrow{{{M}{A}}} + \\overrightarrow{{{M}{C}}} {dau_str} \\overrightarrow{{{M}{N}}}\\right|$.\n'
        loigiai = (
            hinhve +
            f'Gọi ${I}$ là trung điểm ${A}{C}$. Khi đó ${M}{I}$ là đường trung bình của tam giác ${A}{C}{D} \\Rightarrow {M}{I} = \\dfrac{{{C}{D}}}{{2}} = {mi_s}$.\\\\\n'
            f'${M}{N}$ là đường trung bình của hình thang ${hinh_name}$\\\\\n'
            f'$\\Rightarrow {M}{N} = \\dfrac{{{A}{B} + {C}{D}}}{{2}} = \\dfrac{{{ab_s} + {cd_s}}}{{2}} = {mn_s} \\Rightarrow \\overrightarrow{{{M}{I}}} = {tiso_s}\\overrightarrow{{{M}{N}}}$.\\\\\n'
            f'$\\left|\\left(\\overrightarrow{{{M}{A}}} + \\overrightarrow{{{M}{C}}}\\right) {dau_str} \\overrightarrow{{{M}{N}}}\\right| = \\left|2\\overrightarrow{{{M}{I}}} {dau_str} \\overrightarrow{{{M}{N}}}\\right| = \\left|2\\cdot{tiso_s}\\overrightarrow{{{M}{N}}} {dau_str} \\overrightarrow{{{M}{N}}}\\right| = \\left|{heso_s}\\overrightarrow{{{M}{N}}}\\right| = {heso_s}{M}{N} = {heso_mul}{mn_s} = {kq_s}$.\n'
        )
        noidungcauhoi = noidungcauhoi.replace('- -', '+').replace('+ -', '-')
        loigiai = loigiai.replace('- -', '+').replace('+ -', '-')
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
    return content

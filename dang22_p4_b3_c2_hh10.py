
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


def bt_dang22_p4_b3_c2_hh10(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        bo_ten = [
            ('A', 'B', 'C', 'M', 'I'),
            ('D', 'E', 'F', 'M', 'I'),
            ('A', 'B', 'C', 'M', 'K'),
            ('P', 'Q', 'R', 'M', 'I')
        ]
        A, B, C, M, I = random.choice(bo_ten)
        a = randint(2, 6)
        b = randint(1, 5)
        c = random.choice([1, 1, 2, 3])
        while c == a:
            c = randint(1, 3)
        dau = random.choice([1, -1])
        hb = '' if b == 1 else str(b)
        hc = '' if c == 1 else str(c)
        r_ba = Rational(b, a)
        r_ca = Rational(c, a)
        r_ba_str = '' if r_ba == 1 else latex(r_ba)
        if r_ca.q == 1:
            r_ca_kq = f'{r_ca.p}{C}{B}' if r_ca.p > 1 else f'{C}{B}'
        elif r_ca.p == 1:
            r_ca_kq = f'\\dfrac{{{C}{B}}}{{{r_ca.q}}}'
        else:
            r_ca_kq = f'\\dfrac{{{r_ca.p}{C}{B}}}{{{r_ca.q}}}'
        r_ca_heso = f'{latex(r_ca)}{C}{B}' if r_ca != 1 else f'{C}{B}'
        if dau == 1:
            s1, s2 = '+', '-'
            vec_hieu = f'{C}{B}'
            vec_ia = f'{B}{C}'
        else:
            s1, s2 = '-', '+'
            vec_hieu = f'{B}{C}'
            vec_ia = f'{C}{B}'
        vt_M = f'{a}\\overrightarrow{{{M}{A}}} {s1} {hb}\\overrightarrow{{{M}{B}}} {s2} {hb}\\overrightarrow{{{M}{C}}}'
        vt_I = f'{a}\\overrightarrow{{{I}{A}}} {s1} {hb}\\overrightarrow{{{I}{B}}} {s2} {hb}\\overrightarrow{{{I}{C}}}'
        vp_M = f'{hc}\\overrightarrow{{{M}{B}}} - {hc}\\overrightarrow{{{M}{C}}}'
        chen_I = f'{a}\\left(\\overrightarrow{{{M}{I}}} + \\overrightarrow{{{I}{A}}}\\right) {s1} {hb}\\left(\\overrightarrow{{{M}{I}}} + \\overrightarrow{{{I}{B}}}\\right) {s2} {hb}\\left(\\overrightarrow{{{M}{I}}} + \\overrightarrow{{{I}{C}}}\\right)'
        noidungcauhoi = f'Tìm tập hợp điểm ${M}$ thỏa mãn hệ thức $\\left|{vt_M}\\right| = \\left|{vp_M}\\right|$.\n'
        loigiai = (
            f'Chọn điểm ${I}$ sao cho: ${vt_I} = \\vec{{0}}$.\\\\\n'
            f'Ta có: ${vt_I} = \\vec{{0}} \\Leftrightarrow {a}\\overrightarrow{{{I}{A}}} + {hb}\\overrightarrow{{{vec_hieu}}} = \\vec{{0}} \\Leftrightarrow \\overrightarrow{{{I}{A}}} = {r_ba_str}\\overrightarrow{{{vec_ia}}}$.\\\\\n'
            f'$\\Rightarrow {vt_M} = {chen_I} = {a}\\overrightarrow{{{M}{I}}}$.\\\\\n'
            f'$\\Rightarrow \\left|{vt_M}\\right| = \\left|{vp_M}\\right| \\Leftrightarrow {a}{M}{I} = {hc}{C}{B} \\Leftrightarrow {M}{I} = {r_ca_heso}$.\\\\\n'
            f'Vậy tập hợp điểm ${M}$ là đường tròn tâm ${I}$ bán kính ${r_ca_kq}$.\n'
        )
        noidungcauhoi = noidungcauhoi.replace('- -', '+').replace('+ -', '-')
        loigiai = loigiai.replace('- -', '+').replace('+ -', '-')
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
    return content

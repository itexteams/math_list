
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


def bt_dang8_p3_b4_c2_hh10(self):
    def fmt_term(coef, vec_name):
        if coef == 1:
            return vec_name
        elif coef == -1:
            return '-' + vec_name
        else:
            return str(coef) + vec_name
    def fmt_lin_comb(m, n):
        s1 = fmt_term(m, r'\vec{a}')
        if n == 1:
            s2 = r' + \vec{b}'
        elif n == -1:
            s2 = r' - \vec{b}'
        elif n > 0:
            s2 = ' + ' + str(n) + r'\vec{b}'
        else:
            s2 = ' - ' + str(abs(n)) + r'\vec{b}'
        return s1 + s2
    def fmt_mx_const(m, const_val):
        s1 = '-x' if m == -1 else str(m) + 'x'
        if const_val > 0:
            return s1 + ' + ' + str(const_val)
        else:
            return s1 + ' - ' + str(abs(const_val))
    def fix_signs(s):
        return s.replace('+ -', '- ').replace('+-', '-').replace('- -', '+ ').replace('--', '+')
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        while True:
            m = random.choice([-4, -3, -1, 2, 3, 5, 6])
            n = random.choice([i for i in range(-5, 6) if i != 0])
            xb = random.choice([i for i in range(-5, 6) if i != 0])
            ya = random.choice([i for i in range(-5, 6) if i != 0])
            yb = random.choice([i for i in range(-5, 6) if i != 0])
            yc = m * ya + n * yb
            x_val = Rational(n * xb, 1 - m)
            if x_val.q == 1:
                kq_str = str(x_val.p)
            else:
                val_dec = Decimal(x_val.p) / Decimal(x_val.q)
                kq_str = format(val_dec.normalize(), 'f').replace('.', ',')
            if len(kq_str) <= 4:
                break
        kq = sp.Symbol(kq_str)
        lin_str = fmt_lin_comb(m, n)
        ma_str = fmt_term(m, r'\vec{a}')
        nb_str = fmt_term(n, r'\vec{b}')
        mx_str = '-x' if m == -1 else str(m) + 'x'
        rhs_x = fmt_mx_const(m, n * xb)
        if x_val.q == 1:
            kl_x = latex(x_val)
        else:
            kl_x = '%s = %s' % (latex(x_val), kq_str)
        noidungcauhoi = fix_signs('''Cho $\\vec{a} = (x; %s)$, $\\vec{b} = (%s; %s)$, $\\vec{c} = (x; %s)$. Biết $\\vec{c} = %s$, giá trị của $x$ bằng bao nhiêu?''' % (ya, xb, yb, yc, lin_str))
        loigiai = fix_signs('''Ta có $\\begin{cases} %s = (%s; %s) \\\\ %s = (%s; %s) \\end{cases} \\Rightarrow %s = (%s; %s)$.\\\\
    Để $\\vec{c} = %s \\Leftrightarrow \\begin{cases} x = %s \\\\ %s = %s \\end{cases} \\Rightarrow x = %s$.''' % (ma_str, mx_str, m * ya, nb_str, n * xb, n * yb, lin_str, rhs_x, yc, lin_str, rhs_x, yc, yc, kl_x))
        dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
        content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+ '\\loigiai{ \n' +str(loigiai)+'}\n' '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac')
        return content

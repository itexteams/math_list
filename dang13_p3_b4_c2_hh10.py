
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


def bt_dang13_p3_b4_c2_hh10(self):
    def is_valid_num(val):
        r = Rational(val)
        q = r.q
        while q % 2 == 0:
            q //= 2
        while q % 5 == 0:
            q //= 5
        return q == 1
    def fmt_num(val):
        r = Rational(val)
        if r.q == 1:
            return str(r.p)
        d = Decimal(r.p) / Decimal(r.q)
        return format(d.normalize(), 'f').replace('.', ',')
    def fmt_var_minus(var_name, a):
        if a == 0:
            return var_name
        elif a > 0:
            return var_name + ' - ' + str(a)
        else:
            return var_name + ' + ' + str(abs(a))
    def fmt_vec_eq(p, q):
        s1 = str(p) + r'\overrightarrow{AM}'
        if q == 1:
            s2 = r' + \overrightarrow{AB}'
        elif q == -1:
            s2 = r' - \overrightarrow{AB}'
        elif q > 0:
            s2 = ' + ' + str(q) + r'\overrightarrow{AB}'
        else:
            s2 = ' - ' + str(abs(q)) + r'\overrightarrow{AB}'
        return s1 + s2
    def fix_signs(s):
        return s.replace('+ -', '- ').replace('+-', '-').replace('- -', '+ ').replace('--', '+')
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        while True:
            p = random.choice([-5, -4, -3, -2, 2, 3, 4, 5])
            q = random.choice([i for i in range(-5, 6) if i != 0])
            xa = randint(-5, 5)
            ya = randint(-5, 5)
            u1 = random.choice([i for i in range(-6, 7) if i != 0])
            u2 = random.choice([i for i in range(-6, 7) if i != 0])
            xb = xa + u1
            yb = ya + u2
            xm = xa - Rational(q * u1, p)
            ym = ya - Rational(q * u2, p)
            tong = xm + ym
            if is_valid_num(xm) and is_valid_num(ym) and is_valid_num(tong):
                xm_str = fmt_num(xm)
                ym_str = fmt_num(ym)
                kq_str = fmt_num(tong)
                if len(xm_str) <= 4 and len(ym_str) <= 4 and len(kq_str) <= 4:
                    break
        kq = sp.Symbol(kq_str)
        vec_lhs = fmt_vec_eq(p, q)
        am_x = fmt_var_minus('x_M', xa)
        am_y = fmt_var_minus('y_M', ya)
        term_xm_eq = (str(p) + 'x_M') if xa == 0 else (str(p) + '(' + am_x + ')')
        term_ym_eq = (str(p) + 'y_M') if ya == 0 else (str(p) + '(' + am_y + ')')
        c1 = q * u1
        c2 = q * u2
        c1_str = (' + ' + str(c1)) if c1 > 0 else (' - ' + str(abs(c1)))
        c2_str = (' + ' + str(c2)) if c2 > 0 else (' - ' + str(abs(c2)))
        if ym >= 0:
            sum_expr = '%s + %s' % (xm_str, ym_str)
        else:
            sum_expr = '%s - %s' % (xm_str, fmt_num(abs(ym)))
        noidungcauhoi = fix_signs('''Trong mặt phẳng $Oxy$, cho các điểm $A(%s; %s)$, $B(%s; %s)$. Điểm $M(x_M; y_M)$ thỏa mãn $%s = \\vec{0}$ có tổng $x_M + y_M$ bằng bao nhiêu?''' % (xa, ya, xb, yb, vec_lhs))
        loigiai = fix_signs('''Giả sử $M(x_M; y_M)$ suy ra $\\overrightarrow{AM} = (%s; %s)$ và $\\overrightarrow{AB} = (%s; %s)$.\\\\
    Ta có: $%s = \\vec{0} \\Leftrightarrow \\begin{cases} %s%s = 0 \\\\ %s%s = 0 \\end{cases} \\Leftrightarrow \\begin{cases} x_M = %s \\\\ y_M = %s \\end{cases} \\Rightarrow M(%s; %s)$.\\\\
    Vậy $x_M + y_M = %s = %s$.''' % (am_x, am_y, u1, u2, vec_lhs, term_xm_eq, c1_str, term_ym_eq, c2_str, xm_str, ym_str, xm_str, ym_str, sum_expr, kq_str))
        dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
        content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+ '\\loigiai{ \n' +str(loigiai)+'}\n' '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac')
        return content


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


def bt_dang12_p3_b4_c2_hh10(self):
    def fmt_num(val):
        r = Rational(val)
        if r.q == 1:
            return str(r.p)
        d = Decimal(r.p) / Decimal(r.q)
        return format(d.normalize(), 'f').replace('.', ',')
    def fmt_var_minus(var_name, r_val):
        r = Rational(r_val)
        if r == 0:
            return var_name
        elif r > 0:
            return var_name + ' - ' + latex(r)
        else:
            return var_name + ' + ' + latex(-r)
    def fix_signs(s):
        return s.replace('+ -', '- ').replace('+-', '-').replace('- -', '+ ').replace('--', '+')
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        while True:
            half_first = random.choice([True, False])
            if half_first:
                xa = Rational(2 * randint(2, 7) + 1, 2)
                ya = Rational(randint(3, 8))
            else:
                xa = Rational(randint(3, 8))
                ya = Rational(2 * randint(2, 7) + 1, 2)
            xb = Rational(randint(2, 8))
            yb = Rational(randint(2, 8))
            xd = Rational(randint(2, 8))
            yd = Rational(randint(2, 8))
            abx = xb - xa
            aby = yb - ya
            adx = xd - xa
            ady = yd - ya
            cross = abs(abx * ady - aby * adx)
            len_ab = math.hypot(float(abx), float(aby))
            len_ad = math.hypot(float(adx), float(ady))
            if len_ab < 2.2 or len_ad < 2.2:
                continue
            if float(cross) < 0.4 * len_ab * len_ad:
                continue
            acx = abx + adx
            acy = aby + ady
            xc = xa + acx
            yc = ya + acy
            if not (1 <= xc <= 9 and 1 <= yc <= 9):
                continue
            tong = xc + yc
            kq_str = fmt_num(tong)
            if len(kq_str) <= 4:
                break
        kq = sp.Symbol(kq_str)
        ax_f, ay_f = float(xa), float(ya)
        bx_f, by_f = float(xb), float(yb)
        cx_f, cy_f = float(xc), float(yc)
        dx_f, dy_f = float(xd), float(yd)
        gx = (ax_f + bx_f + cx_f + dx_f) / 4.0
        gy = (ay_f + by_f + cy_f + dy_f) / 4.0
        pts = {'A': (ax_f, ay_f), 'B': (bx_f, by_f), 'C': (cx_f, cy_f), 'D': (dx_f, dy_f)}
        lbl_pos = {}
        for name, (px, py) in pts.items():
            dist = math.hypot(px - gx, py - gy)
            ux = (px - gx) / dist
            uy = (py - gy) / dist
            lbl_pos[name] = (round(px + 0.55 * ux, 2), round(py + 0.55 * uy, 2))
        tikz_code = (
            '\n\n\\centerline{\\begin{tikzpicture}[scale=0.52,line cap=round,line join=round,line width=1pt]\n'
            '\\draw[dotted,line width=0.6pt] (-1,-1) grid (10,10);\n'
            '\\draw[->,line width=1pt] (-1.3,0)--(10.4,0) node[below left] {$x$};\n'
            '\\draw[->,line width=1pt] (0,-1.3)--(0,10.4) node[below left] {$y$};\n'
            '\\fill (0,0) circle (2.2pt) node[below left] {$O$};\n'
            '\\coordinate (A) at (%s,%s);\n'
            '\\coordinate (B) at (%s,%s);\n'
            '\\coordinate (C) at (%s,%s);\n'
            '\\coordinate (D) at (%s,%s);\n'
            '\\draw[->,line width=1pt] (A)--(B);\n'
            '\\draw[->,line width=1pt] (A)--(D);\n'
            '\\draw[->,line width=1pt] (A)--(C);\n'
            '\\draw[dashed,line width=1pt] (B)--(C);\n'
            '\\draw[dashed,line width=1pt] (D)--(C);\n'
            '\\fill (A) circle (2.2pt);\n'
            '\\fill (B) circle (2.2pt);\n'
            '\\fill (C) circle (2.2pt);\n'
            '\\fill (D) circle (2.2pt);\n'
            '\\node at (%s,%s) {$A$};\n'
            '\\node at (%s,%s) {$B$};\n'
            '\\node at (%s,%s) {$C$};\n'
            '\\node at (%s,%s) {$D$};\n'
            '\\end{tikzpicture}}\n'
        ) % (ax_f, ay_f, bx_f, by_f, cx_f, cy_f, dx_f, dy_f, lbl_pos['A'][0], lbl_pos['A'][1], lbl_pos['B'][0], lbl_pos['B'][1], lbl_pos['C'][0], lbl_pos['C'][1], lbl_pos['D'][0], lbl_pos['D'][1])
        q_text = fix_signs('''Hai máy tời kéo tàu biển được đặt ở hai vị trí $B$, $D$ dọc theo kênh đào được minh họa ở hình dưới đây. Hai máy tời đó kéo một con tàu từ vị trí $A$ hướng đến vị trí $C$. Biết tọa độ các điểm $A\\left(%s; %s\\right)$, $B(%s; %s)$, $D(%s; %s)$ và điểm $C(a; b)$, giá trị của $a + b$ bằng bao nhiêu?''' % (latex(xa), latex(ya), latex(xb), latex(yb), latex(xd), latex(yd)))
        noidungcauhoi = q_text + tikz_code
        x_lhs = fmt_var_minus('x', xa)
        y_lhs = fmt_var_minus('y', ya)
        if tong.q == 1:
            kl_sum = latex(tong)
        else:
            kl_sum = '%s = %s' % (latex(tong), kq_str)
        loigiai = fix_signs('''Ta có $\\overrightarrow{AB} = \\left(%s; %s\\right)$, $\\overrightarrow{AD} = \\left(%s; %s\\right)$.\\\\
    Mặt khác tàu di chuyển từ $A$ đến $C$ nên $\\overrightarrow{AC} = \\overrightarrow{AB} + \\overrightarrow{AD} \\Rightarrow \\overrightarrow{AC} = \\left(%s; %s\\right)$.\\\\
    Gọi $C(x; y) \\Rightarrow \\overrightarrow{AC} = \\left(%s; %s\\right) \\Rightarrow \\begin{cases} %s = %s \\\\ %s = %s \\end{cases} \\Leftrightarrow \\begin{cases} x = %s \\\\ y = %s \\end{cases} \\Rightarrow \\begin{cases} a = %s \\\\ b = %s \\end{cases} \\Rightarrow a + b = %s$.''' % (latex(abx), latex(aby), latex(adx), latex(ady), latex(acx), latex(acy), x_lhs, y_lhs, x_lhs, latex(acx), y_lhs, latex(acy), latex(xc), latex(yc), latex(xc), latex(yc), kl_sum))
        dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
        content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+ '\\loigiai{ \n' +str(loigiai)+'}\n' '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac')
        return content

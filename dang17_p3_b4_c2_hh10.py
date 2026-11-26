
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


def bt_dang17_p3_b4_c2_hh10(self):
    def fmt_num(val):
        r = Rational(val)
        if r.q == 1:
            return str(r.p)
        d = Decimal(r.p) / Decimal(r.q)
        return format(d.normalize(), 'f').replace('.', ',')
    def fmt_term_vec(coef, vname):
        return vname if coef == 1 else (str(coef) + vname)
    def fix_signs(s):
        return s.replace('+ -', '- ').replace('+-', '-').replace('- -', '+ ').replace('--', '+')
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        ten_cot = {2: 'thứ hai', 3: 'thứ ba', 4: 'thứ tư'}
        while True:
            L = random.choice([100, 110, 120, 130, 140, 150, 160, 180])
            W = random.choice([40, 45, 50, 55, 60, 70, 80])
            d1 = random.choice([10, 15, 20, 25, 30])
            d5 = random.choice([15, 20, 25, 30, 35, 40])
            if d1 + d5 >= L - 30:
                continue
            k = random.choice([2, 3, 4])
            x5 = L - d5
            xk = d1 + Rational((k - 1) * (x5 - d1), 4)
            yk = Rational((k - 1) * W, 4)
            kq_str = fmt_num(xk)
            if len(kq_str) <= 4:
                break
        kq = sp.Symbol(kq_str)
        xk_str = fmt_num(xk)
        yk_str = fmt_num(yk)
        ratio = Rational(k - 1, 4)
        den = ratio.q
        p_coef = ratio.p
        q_coef = den - p_coef
        vec_rhs = fmt_term_vec(p_coef, r'\overrightarrow{OC_5}') + ' + ' + fmt_term_vec(q_coef, r'\overrightarrow{OC_1}')
        sc = 8.0 / L
        bx_t = round(L * sc, 2)
        dy_t = round(W * sc, 2)
        c_pts = []
        for i in range(1, 6):
            xi_v = d1 + (i - 1) * (x5 - d1) / 4.0
            yi_v = (i - 1) * W / 4.0
            c_pts.append((round(xi_v * sc, 2), round(yi_v * sc, 2)))
        xmax_g = math.ceil(bx_t + 1.0)
        ymax_g = math.ceil(dy_t + 1.0)
        tikz_code = (
            '\n\n\\centerline{\\begin{tikzpicture}[line cap=round,line join=round,line width=1pt]\n'
            '\\draw[dotted,line width=0.6pt] (-1,-1) grid (%s,%s);\n'
            '\\draw[->,line width=1pt] (-1.2,0)--(%s,0) node[below left] {$x$};\n'
            '\\draw[->,line width=1pt] (0,-1.2)--(0,%s) node[below left] {$y$};\n'
            '\\draw[line width=1pt] (0,0)--(%s,0)--(%s,%s)--(0,%s)--cycle;\n'
            '\\coordinate (C1) at (%s,%s);\n'
            '\\coordinate (C2) at (%s,%s);\n'
            '\\coordinate (C3) at (%s,%s);\n'
            '\\coordinate (C4) at (%s,%s);\n'
            '\\coordinate (C5) at (%s,%s);\n'
            '\\draw[line width=1pt] (C1)--(C5);\n'
            '\\fill (0,0) circle (1.6pt) node[below left] {$O$} node[above left] {$A$};\n'
            '\\fill (%s,0) circle (1.6pt) node[above right] {$B$} node[below] {$%s$};\n'
            '\\fill (%s,%s) circle (1.6pt) node[above right] {$C$};\n'
            '\\fill (0,%s) circle (1.6pt) node[above right] {$D$} node[left] {$%s$};\n'
            '\\fill (C1) circle (1.6pt) node[below] {$C_1$};\n'
            '\\fill (C2) circle (1.6pt) node[below right] {$C_2$};\n'
            '\\fill (C3) circle (1.6pt) node[below right] {$C_3$};\n'
            '\\fill (C4) circle (1.6pt) node[below right] {$C_4$};\n'
            '\\fill (C5) circle (1.6pt) node[above] {$C_5$};\n'
            '\\end{tikzpicture}}\n\n'
        ) % (xmax_g, ymax_g, xmax_g + 0.4, ymax_g + 0.4, bx_t, bx_t, dy_t, dy_t, c_pts[0][0], c_pts[0][1], c_pts[1][0], c_pts[1][1], c_pts[2][0], c_pts[2][1], c_pts[3][0], c_pts[3][1], c_pts[4][0], c_pts[4][1], bx_t, L, bx_t, dy_t, dy_t, W)
        noidungcauhoi = fix_signs('''Để kéo đường dây điện băng qua một hồ hình chữ nhật $ABCD$ với độ dài $AB = %s\\,\\mathrm{m}$, $AD = %s\\,\\mathrm{m}$. Người ta dự định làm $5$ cột điện liên tiếp thẳng hàng và cách đều nhau. Cột thứ nhất nằm trên bờ $AB$ và cách đỉnh $A$ một khoảng bằng $%s\\,\\mathrm{m}$. Cột thứ năm nằm trên bờ $CD$ và cách đỉnh $C$ một khoảng bằng $%s\\,\\mathrm{m}$. Khoảng cách từ cột %s đến bờ $AD$ (tính theo đơn vị mét) bằng bao nhiêu?''' % (L, W, d1, d5, ten_cot[k]))
        lg_part1 = fix_signs('''Chọn hệ trục như hình vẽ $A(0; 0)$, $B(%s; 0)$, $C(%s; %s)$, $D(0; %s)$.''' % (L, L, W, W))
        lg_part2 = fix_signs('''Chọn vị trí $5$ cột điện ở $C_1, C_2, C_3, C_4, C_5$ như hình vẽ.\\\\
    Vì $C_1 \\in AB$ và cách đỉnh $A$ một đoạn bằng $%s\\,\\mathrm{m}$ nên $C_1(%s; 0)$.\\\\
    Vì $C_5 \\in CD$ và cách đỉnh $C$ một đoạn bằng $%s\\,\\mathrm{m}$ nên $C_5(%s; %s)$.\\\\
    Ta có: $\\overrightarrow{C_1C_%s} = %s\\overrightarrow{C_1C_5} \\Leftrightarrow %s\\overrightarrow{OC_%s} = %s \\Rightarrow C_%s(%s; %s) \\Rightarrow d(C_%s, AD) = %s\\,\\mathrm{m}$.''' % (d1, d1, d5, x5, W, k, latex(ratio), den, k, vec_rhs, k, xk_str, yk_str, k, kq_str))
        loigiai = lg_part1 + tikz_code + lg_part2
        dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
        content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+ '\\loigiai{ \n' +str(loigiai)+'}\n' '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac')
        return content

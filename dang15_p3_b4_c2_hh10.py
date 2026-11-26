
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


def bt_dang15_p3_b4_c2_hh10(self):
    def fmt_dec(d):
        if d == d.to_integral_value():
            return str(int(d))
        return str(d).replace('.', ',')
    def fmt_diff_sq(x2, x1):
        if x1 >= 0:
            return '(%s - %s)^2' % (x2, x1)
        else:
            return '(%s + %s)^2' % (x2, abs(x1))
    def fix_signs(s):
        return s.replace('+ -', '- ').replace('+-', '-').replace('- -', '+ ').replace('--', '+')
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        while True:
            xa = randint(-15, -6)
            ya = randint(10, 22)
            xb = randint(20, 40)
            yb = randint(15, 30)
            xc = randint(18, 36)
            yc = randint(-28, -12)
            if (xb - xa) * (yc - ya) - (yb - ya) * (xc - xa) == 0:
                continue
            ab_sq = (xb - xa) ** 2 + (yb - ya) ** 2
            ac_sq = (xc - xa) ** 2 + (yc - ya) ** 2
            if math.isqrt(ab_sq) ** 2 == ab_sq or math.isqrt(ac_sq) ** 2 == ac_sq:
                continue
            ab = math.sqrt(ab_sq)
            ac = math.sqrt(ac_sq)
            tot = ab + ac
            if abs((ab * 10) % 1 - 0.5) < 0.08 or abs((ac * 10) % 1 - 0.5) < 0.08 or abs((tot * 10) % 1 - 0.5) < 0.08:
                continue
            ab_1 = Decimal(str(ab)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
            ac_1 = Decimal(str(ac)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
            tot_1 = Decimal(str(tot)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
            if ab_1 == ab_1.to_integral_value() or ac_1 == ac_1.to_integral_value() or tot_1 == tot_1.to_integral_value():
                continue
            if ab_1 + ac_1 != tot_1:
                continue
            kq_str = fmt_dec(tot_1)
            if len(kq_str) <= 4:
                break
        kq = sp.Symbol(kq_str)
        ab_str = fmt_dec(ab_1)
        ac_str = fmt_dec(ac_1)
        sq_ab = fmt_diff_sq(xb, xa) + ' + ' + fmt_diff_sq(yb, ya)
        sq_ac = fmt_diff_sq(xc, xa) + ' + ' + fmt_diff_sq(yc, ya)
        sc = 0.09
        ax_t = round(xa * sc, 2)
        ay_t = round(ya * sc, 2)
        bx_t = round(xb * sc, 2)
        by_t = round(yb * sc, 2)
        cx_t = round(xc * sc, 2)
        cy_t = round(yc * sc, 2)
        xmin_t = round(ax_t - 1.2, 2)
        xmax_t = round(max(bx_t, cx_t) + 1.3, 2)
        ymin_t = round(cy_t - 0.8, 2)
        ymax_t = round(by_t + 0.8, 2)
        tikz_code = (
            '\n\n\\centerline{\\begin{tikzpicture}[line cap=round,line join=round,line width=1pt]\n'
            '\\draw[->,line width=1pt] (%s,0)--(%s,0) node[above left] {$x$};\n'
            '\\draw[->,line width=1pt] (0,%s)--(0,%s) node[below right] {$y$};\n'
            '\\fill (0,0) circle (1.5pt) node[below left] {$O$};\n'
            '\\coordinate (A) at (%s,%s);\n'
            '\\coordinate (B) at (%s,%s);\n'
            '\\coordinate (C) at (%s,%s);\n'
            '\\draw[line width=1pt] (A)--(B);\n'
            '\\draw[line width=1pt] (A)--(C);\n'
            '\\draw[line width=1pt] (A)--++(-0.72,0)--++(0.14,-0.18)--++(0.42,0)--cycle;\n'
            '\\draw[line width=1pt] (A)++(-0.52,0)--++(0,0.16)--++(0.26,0)--++(0,-0.16);\n'
            '\\draw[line width=1pt] (B)++(-0.15,-0.08)..controls ++(0.25,0.34) and ++(0.55,0.34)..++(0.85,0)--cycle;\n'
            '\\draw[line width=1pt] (C)++(-0.15,-0.08)..controls ++(0.25,0.34) and ++(0.55,0.34)..++(0.85,0)--cycle;\n'
            '\\fill (A) circle (1.5pt) node[below=4pt] {$A$};\n'
            '\\fill (B) circle (1.5pt) node[below=4pt] {$B$};\n'
            '\\fill (C) circle (1.5pt) node[below=4pt] {$C$};\n'
            '\\end{tikzpicture}}\n'
        ) % (xmin_t, xmax_t, ymin_t, ymax_t, ax_t, ay_t, bx_t, by_t, cx_t, cy_t)
        q_text = fix_signs('''Một trò chơi trên máy tính đang mô phỏng một vùng biển có hai hòn đảo nhỏ có tọa độ $B(%s; %s)$, $C(%s; %s)$. Một con tàu đang neo đậu tại điểm $A(%s; %s)$. Cho biết một đơn vị trên trục tọa độ tương ứng với $1\\,\\mathrm{km}$. Tổng khoảng cách từ con tàu đến mỗi hòn đảo (làm tròn kết quả đến hàng phần chục theo đơn vị ki-lô-mét) bằng bao nhiêu?''' % (xb, yb, xc, yc, xa, ya))
        noidungcauhoi = q_text + tikz_code
        loigiai = fix_signs('''Vì con tàu đang neo đậu tại điểm $A(%s; %s)$ và hòn đảo $B(%s; %s)$ nên khoảng cách từ con tàu đến hòn đảo $B$ là:\\\\
    $AB = \\sqrt{%s} \\approx %s\\,(\\mathrm{km})$.\\\\
    Vì con tàu đang neo đậu tại điểm $A(%s; %s)$ và hòn đảo $C(%s; %s)$ nên khoảng cách từ con tàu đến hòn đảo $C$ là:\\\\
    $AC = \\sqrt{%s} \\approx %s\\,(\\mathrm{km})$.\\\\
    Vậy tổng khoảng cách từ con tàu đến mỗi hòn đảo là $AB + AC \\approx %s + %s = %s\\,(\\mathrm{km})$.''' % (xa, ya, xb, yb, sq_ab, ab_str, xa, ya, xc, yc, sq_ac, ac_str, ab_str, ac_str, kq_str))
        dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
        content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+ '\\loigiai{ \n' +str(loigiai)+'}\n' '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac')
        return content

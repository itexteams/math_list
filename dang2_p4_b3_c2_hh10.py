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


def bt_dang2_p4_b3_c2_hh10(self):
    def fmt_coef_f1(c):
        return r'|\overrightarrow{F_1}|' if c == 1 else (str(c) + r'|\overrightarrow{F_1}|')
    def fix_signs(s):
        return s.replace('+ -', '- ').replace('+-', '-').replace('- -', '+ ').replace('--', '+')
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        while True:
            k = random.choice([2, 3, 4])
            alpha = random.choice([30, 45])
            f0 = random.choice([8, 10, 12, 14, 15, 16, 18, 20, 24, 25, 30])
            oa_val = sp.simplify(2 * f0 * sp.cos(sp.rad(alpha)))
            f1_val = sp.simplify(oa_val / (k - 1))
            f2_val = sp.simplify(k * f1_val)
            f2_num = float(f2_val.evalf())
            if abs((f2_num * 10) % 1 - 0.5) > 0.05:
                break
        kq_dec = Decimal(str(f2_num)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        kq_str = str(kq_dec).replace('.', ',')
        rad_a = math.radians(alpha)
        r_vec = 2.6
        cx = round(r_vec * math.cos(rad_a), 3)
        cy = round(r_vec * math.sin(rad_a), 3)
        ax = round(2 * cx, 3)
        ex = round(ax + 0.9, 3)
        ang_r = 1.48
        ang_x = round(ang_r * math.cos(rad_a / 2.0), 3)
        ang_y = round(ang_r * math.sin(rad_a / 2.0), 3)
        f3_x = round(0.62 * cx, 3)
        f3_y = round(0.62 * cy, 3)
        tikz_code = (
            '\n\n\\centerline{\\begin{tikzpicture}[line cap=round,line join=round,line width=1pt]\n'
            '\\draw[line width=1pt] (0,0) circle (0.95);\n'
            '\\draw[->,>=stealth,line width=1pt] (0,0)--(-6.8,0);\n'
            '\\draw[->,>=stealth,line width=1pt] (0,0)--(%s,0);\n'
            '\\draw[->,>=stealth,line width=1pt] (0,0)--(%s,%s);\n'
            '\\draw[->,>=stealth,line width=1pt] (0,0)--(%s,%s);\n'
            '\\draw[dashed,line width=1pt] (%s,0)--(%s,%s) (%s,0)--(%s,%s);\n'
            '\\node at (-0.12,0.28) {$O$};\n'
            '\\node[below=2pt] at (%s,0) {$A$};\n'
            '\\node[below right=2pt] at (-6.8,0) {$B$};\n'
            '\\node[above right=-1pt] at (%s,%s) {$C$};\n'
            '\\node[below right=-1pt] at (%s,%s) {$D$};\n'
            '\\node[above=2pt] at (%s,0) {$\\overrightarrow{F_1}$};\n'
            '\\node[above=2pt] at (-5.6,0) {$\\overrightarrow{F_2}$};\n'
            '\\node[above left=1pt] at (%s,%s) {$\\overrightarrow{F_3}$};\n'
            '\\node[below left=1pt] at (%s,%s) {$\\overrightarrow{F_4}$};\n'
            '\\node at (%s,%s) {$%s^\\circ$};\n'
            '\\node at (%s,%s) {$%s^\\circ$};\n'
            '\\end{tikzpicture}}'
        ) % (ex, cx, cy, cx, -cy, ax, cx, cy, ax, cx, -cy, ax, cx, cy, cx, -cy, ex, f3_x, f3_y, f3_x, -f3_y, ang_x, ang_y, alpha, ang_x, -ang_y, alpha)
        q_text = fix_signs('''Một vật đang ở vị trí $O$ chịu tác dụng của hai lực ngược chiều nhau là $\\overrightarrow{F_1}$ và $\\overrightarrow{F_2}$, trong đó độ lớn lực $\\overrightarrow{F_2}$ lớn gấp $%s$ lần độ lớn lực $\\overrightarrow{F_1}$. Người ta muốn vật dừng lại nên cần tác dụng vào vật hai lực $\\overrightarrow{F_3}, \\overrightarrow{F_4}$ có phương hợp với lực $\\overrightarrow{F_1}$ các góc $%s^\\circ$ như hình vẽ, chúng có độ lớn bằng nhau và bằng $%s\\text{ N}$. Tính độ lớn của lực $\\overrightarrow{F_2}$ (làm tròn kết quả đến hàng phần chục).''' % (k, alpha, f0))
        noidungcauhoi = q_text + tikz_code
        if k == 2:
            step_f1 = '''|%s| + %s = 2|%s| \\Leftrightarrow |%s| = %s\\text{ (N)}.''' % (r'\overrightarrow{F_1}', latex(oa_val), r'\overrightarrow{F_1}', r'\overrightarrow{F_1}', latex(f1_val))
        else:
            step_f1 = '''|%s| + %s = %s|%s| \\Leftrightarrow %s = %s \\Leftrightarrow |%s| = \\dfrac{%s}{%s} = %s\\text{ (N)}.''' % (r'\overrightarrow{F_1}', latex(oa_val), k, r'\overrightarrow{F_1}', fmt_coef_f1(k - 1), latex(oa_val), r'\overrightarrow{F_1}', latex(oa_val), k - 1, latex(f1_val))
        loigiai = fix_signs('''Dựng hình bình hành $OCAD$ với $\\overrightarrow{OC} = \\overrightarrow{F_3}$ và $\\overrightarrow{OD} = \\overrightarrow{F_4}$ như hình vẽ.\\\\
    Vì $|\\overrightarrow{F_3}| = |\\overrightarrow{F_4}| = %s\\text{ N}$ nên $OC = OD = %s$, suy ra $OCAD$ là hình thoi có $\\widehat{COA} = \\widehat{DOA} = %s^\\circ$.\\\\
    Theo quy tắc hình bình hành, hợp lực của hai lực $\\overrightarrow{F_3}$ và $\\overrightarrow{F_4}$ là: $\\overrightarrow{F_3} + \\overrightarrow{F_4} = \\overrightarrow{OC} + \\overrightarrow{OD} = \\overrightarrow{OA}$.\\\\
    Ta có $OA = 2 \\cdot OC \\cdot \\cos %s^\\circ = 2 \\cdot %s \\cdot \\cos %s^\\circ = %s\\text{ (N)}$ và vectơ $\\overrightarrow{OA}$ cùng hướng với $\\overrightarrow{F_1}$.\\\\
    Để vật dừng lại thì tổng hợp lực tác dụng lên vật bằng $\\vec{0}$:\\\\
    $\\overrightarrow{F_1} + \\overrightarrow{F_2} + \\overrightarrow{F_3} + \\overrightarrow{F_4} = \\vec{0} \\Leftrightarrow \\left(\\overrightarrow{F_1} + \\overrightarrow{OA}\\right) + \\overrightarrow{F_2} = \\vec{0}$.\\\\
    Vì $\\overrightarrow{F_1}$ và $\\overrightarrow{OA}$ cùng hướng, còn $\\overrightarrow{F_2}$ ngược hướng với $\\overrightarrow{F_1}$ nên $|\\overrightarrow{F_1}| + OA = |\\overrightarrow{F_2}|$.\\\\
    Mặt khác $|\\overrightarrow{F_2}| = %s|\\overrightarrow{F_1}|$, suy ra $%s$\\\\
    Vậy độ lớn của lực $\\overrightarrow{F_2}$ là $|\\overrightarrow{F_2}| = %s|\\overrightarrow{F_1}| = %s \\approx %s\\text{ (N)}$.''' % (f0, f0, alpha, alpha, f0, alpha, latex(oa_val), k, step_f1, k, latex(f2_val), kq_str))
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
    return content


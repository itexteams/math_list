
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


def bt_dang14_p3_b4_c2_hh10(self):
    def fmt_term_vec(coef, pt, vname):
        vec = r'\overrightarrow{' + pt + vname + '}'
        if coef == 1:
            return vec
        elif coef == -1:
            return '-' + vec
        else:
            return str(coef) + vec
    def fmt_vec_comb(alpha, beta, gamma, pt):
        s1 = fmt_term_vec(alpha, pt, 'A')
        v2 = r'\overrightarrow{' + pt + 'B}'
        if beta == 1:
            s2 = ' + ' + v2
        elif beta == -1:
            s2 = ' - ' + v2
        elif beta > 0:
            s2 = ' + ' + str(beta) + v2
        else:
            s2 = ' - ' + str(abs(beta)) + v2
        v3 = r'\overrightarrow{' + pt + 'C}'
        if gamma == 1:
            s3 = ' + ' + v3
        elif gamma == -1:
            s3 = ' - ' + v3
        elif gamma > 0:
            s3 = ' + ' + str(gamma) + v3
        else:
            s3 = ' - ' + str(abs(gamma)) + v3
        return s1 + s2 + s3
    def fmt_s_vec(s_coef):
        if s_coef == 1:
            return r'\overrightarrow{FJ}'
        elif s_coef == -1:
            return r'-\overrightarrow{FJ}'
        else:
            return str(s_coef) + r'\overrightarrow{FJ}'
    def fmt_abs_s_fj(s_coef):
        a_s = abs(s_coef)
        return 'FJ' if a_s == 1 else (str(a_s) + 'FJ')
    def fmt_lin_a(p, q):
        if q > 0:
            return str(p) + 'a + ' + str(q)
        else:
            return str(p) + 'a - ' + str(abs(q))
    def fix_signs(s):
        return s.replace('+ -', '- ').replace('+-', '-').replace('- -', '+ ').replace('--', '+')
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        while True:
            alpha = random.choice([-2, -1, 1, 2])
            beta = random.choice([-3, -2, -1, 1, 2, 3])
            gamma = random.choice([-3, -2, -1, 1, 2, 3])
            s_coef = alpha + beta + gamma
            if s_coef == 0:
                continue
            xa = randint(-6, 6)
            ya = randint(-6, 6)
            xb = randint(-6, 6)
            yb = randint(-6, 6)
            xc = randint(-6, 6)
            yc = randint(-6, 6)
            if (xb - xa) * (yc - ya) - (yb - ya) * (xc - xa) == 0:
                continue
            num_x = alpha * xa + beta * xb + gamma * xc
            num_y = alpha * ya + beta * yb + gamma * yc
            if num_x % s_coef == 0 and num_y % s_coef == 0:
                xj = num_x // s_coef
                yj = num_y // s_coef
                if xj != 0 and yj != 0 and abs(xj) <= 12 and abs(yj) <= 12:
                    p = random.choice([2, 3, 4, 5])
                    q = random.choice([i for i in range(-9, 10) if i != 0])
                    kq_val = p * yj + q
                    if len(str(kq_val)) <= 4:
                        break
        kq = Integer(kq_val)
        f_comb = fmt_vec_comb(alpha, beta, gamma, 'F')
        j_comb = fmt_vec_comb(alpha, beta, gamma, 'J')
        s_fj_vec = fmt_s_vec(s_coef)
        abs_s_fj = fmt_abs_s_fj(s_coef)
        expr_a = fmt_lin_a(p, q)
        noidungcauhoi = fix_signs('''Trong mặt phẳng tọa độ $Oxy$, cho tam giác $ABC$ có $A(%s; %s)$, $B(%s; %s)$, $C(%s; %s)$. Biết rằng điểm $F(0; a)$ trên $Oy$ thỏa mãn $\\left|%s\\right|$ đạt giá trị nhỏ nhất. Giá trị của $%s$ bằng bao nhiêu?''' % (xa, ya, xb, yb, xc, yc, f_comb, expr_a))
        loigiai = fix_signs('''Gọi $J$ là điểm sao cho $%s = \\vec{0} \\Rightarrow J(%s; %s)$.\\\\
    Suy ra $%s = %s \\Rightarrow \\left|%s\\right| = %s$.\\\\
    Để $\\left|%s\\right|$ đạt giá trị nhỏ nhất khi $FJ$ nhỏ nhất.\\\\
    Khi đó $F$ là hình chiếu của $J$ trên $Oy$ nên $F(0; %s) \\Rightarrow a = %s \\Rightarrow %s = %s$.''' % (j_comb, xj, yj, f_comb, s_fj_vec, f_comb, abs_s_fj, f_comb, yj, yj, expr_a, kq_val))
        dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
        content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+ '\\loigiai{ \n' +str(loigiai)+'}\n' '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac')
        return content

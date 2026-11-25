
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


def bt_dang9_p2_b4_c2_hh10(self):
    y = symbols('y')
    def fmt_coord(u, v):
        ru, rv = Rational(u), Rational(v)
        su = latex(ru).replace('\\frac', '\\dfrac')
        sv = latex(rv).replace('\\frac', '\\dfrac')
        if ru.q != 1 or rv.q != 1:
            return f'\\left({su};{sv}\\right)'
        return f'({su};{sv})'
    def fmt_shift(var_s, val):
        return f'{var_s}-{val}' if val > 0 else f'{var_s}+{-val}'
    def fmt_sq(var_s, val):
        return f'({var_s}-{val})^2' if val > 0 else f'({var_s}+{-val})^2'
    def fmt_dot_eq(u, x0, v, y0):
        sx = fmt_shift('x', x0)
        sy = fmt_shift('y', y0)
        p1 = f'{u}({sx})'
        p2 = f'+{v}({sy})' if v > 0 else f'{v}({sy})'
        return f'{p1}{p2}=0'
    while True:
        x0 = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
        y0 = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
        h = random.choice([-4, -3, -2, 2, 3, 4])
        d = random.choice([2, 3, 4])
        if d == abs(h):
            continue
        xA, yA = x0 + h, y0
        xB, yB = x0, y0 + d
        xC, yC = x0, y0 - d
        if 0 in [xA, yA, xB, yB, xC, yC]:
            continue
        if any(abs(val) > 8 for val in [xA, yA, xB, yB, xC, yC]):
            continue
        xI = Rational(2 * x0 * h + h**2 - d**2, 2 * h)
        if xI != 0:
            break
    ab1, ab2 = xB - xA, yB - yA
    bc1, bc2 = xC - xB, yC - yB
    ac1, ac2 = xC - xA, yC - yA
    xD, yD = xC - ab1, yC - ab2
    xE, yE = 3 * xA - xB - xC, 3 * yA - yB - yC
    xH, yH = Rational(x0 * h + d**2, h), Rational(y0)
    yI = Rational(y0)
    H_str = fmt_coord(xH, yH)
    I_str = fmt_coord(xI, yI)
    xH_tex = latex(xH).replace('\\frac', '\\dfrac')
    yH_tex = latex(yH).replace('\\frac', '\\dfrac')
    xI_tex = latex(xI).replace('\\frac', '\\dfrac')
    yI_tex = latex(yI).replace('\\frac', '\\dfrac')
    noidungcauhoi = f'Cho tam giác $ABC$ có $A({xA};{yA})$, $B({xB};{yB})$, $C({xC};{yC})$. Xét tính đúng sai của các khẳng định sau:\n'
    wrong_D = random.choice([p for p in [(xD, -yD), (-xD, yD), (xD + 1, yD), (xD - 1, yD), (xD, yD + 2)] if p != (xD, yD)])
    nb_da_1_d = f'\\True $ABCD$ là hình bình hành khi $D({xD};{yD})$'
    nb_da_1_s = f'$ABCD$ là hình bình hành khi $D({wrong_D[0]};{wrong_D[1]})$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    wrong_E = random.choice([p for p in [(-xE, yE), (xE, -yE), (xE + 2, yE), (xE - 2, yE), (xE, yE + 2)] if p != (xE, yE)])
    th_da_1_d = f'\\True Tọa độ điểm $E$ để tam giác $BCE$ nhận điểm $A$ làm trọng tâm là $E({xE};{yE})$'
    th_da_1_s = f'Tọa độ điểm $E$ để tam giác $BCE$ nhận điểm $A$ làm trọng tâm là $E({wrong_E[0]};{wrong_E[1]})$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    wrong_H = random.choice([p for p in [(-xH, yH), (xH, -yH), (xH + 1, yH), (xH - 1, yH), (xH, yH + 1)] if p != (xH, yH)])
    wH_str = fmt_coord(wrong_H[0], wrong_H[1])
    vd_da_1_d = f'\\True Tọa độ trực tâm $H$ của tam giác $ABC$ là $H{H_str}$'
    vd_da_1_s = f'Tọa độ trực tâm $H$ của tam giác $ABC$ là $H{wH_str}$'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    wrong_I = random.choice([p for p in [(-xI, yI), (xI, -yI), (xI + 1, yI), (xI - 1, yI), (xI, yI + 1)] if p != (xI, yI)])
    wI_str = fmt_coord(wrong_I[0], wrong_I[1])
    vdc_da_1_d = f'\\True Tọa độ tâm đường tròn ngoại tiếp tam giác $ABC$ là $I{I_str}$'
    vdc_da_1_s = f'Tọa độ tâm đường tròn ngoại tiếp tam giác $ABC$ là $I{wI_str}$'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)
    while True:
        nb_da_1 = random.choice(list_nb_da_1)
        th_da_1 = random.choice(list_th_da_1)
        vd_da_1 = random.choice(list_vd_da_1)
        vdc_da_1 = random.choice(list_vdc_da_1)
        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        true_count = count_true_answers(answers)
        if 1 <= true_count <= 3:
            break
    tt_nb = 'Đúng' if '\\True' in nb_da_1 else 'Sai'
    tt_th = 'Đúng' if '\\True' in th_da_1 else 'Sai'
    tt_vd = 'Đúng' if '\\True' in vd_da_1 else 'Sai'
    tt_vdc = 'Đúng' if '\\True' in vdc_da_1 else 'Sai'
    num_xE = f'{xB}+{xC}+x_E'.replace('+-', '-').replace('--', '+')
    num_yE = f'{yB}+{yC}+y_E'.replace('+-', '-').replace('--', '+')
    ah_x, ah_y = fmt_shift('x', xA), fmt_shift('y', yA)
    bh_x, bh_y = fmt_shift('x', xB), fmt_shift('y', yB)
    h_eq1 = fmt_dot_eq(bc1, xA, bc2, yA)
    h_eq2 = fmt_dot_eq(ac1, xB, ac2, yB)
    lhs_A = latex(sp.expand((x - xA)**2 + (y - yA)**2 - x**2 - y**2))
    rhs_B = latex(sp.expand((x - xB)**2 + (y - yB)**2 - x**2 - y**2))
    rhs_C = latex(sp.expand((x - xC)**2 + (y - yC)**2 - x**2 - y**2))
    eq1_lhs = latex(2 * (xB - xA) * x + 2 * (yB - yA) * y)
    eq1_rhs = xB**2 + yB**2 - xA**2 - yA**2
    eq2_lhs = latex(2 * (xC - xA) * x + 2 * (yC - yA) * y)
    eq2_rhs = xC**2 + yC**2 - xA**2 - yA**2
    loigiai_nb_1 = f'{tt_nb}: Gọi $D(x;y) \\Rightarrow \\overrightarrow{{DC}}=({xC}-x;{yC}-y)$, $\\overrightarrow{{AB}}=({ab1};{ab2})$ nên $ABCD$ là hình bình hành\\\\ $\\Leftrightarrow \\overrightarrow{{AB}}=\\overrightarrow{{DC}} \\Leftrightarrow \\begin{{cases}} {xC}-x={ab1} \\\\ {yC}-y={ab2} \\end{{cases}} \\Leftrightarrow \\begin{{cases}} x={xD} \\\\ y={yD} \\end{{cases}}$ hay $D({xD};{yD})$.'
    loigiai_th_1 = f'{tt_th}: Tam giác $BCE$ nhận điểm $A$ làm trọng tâm nên\\\\ $\\begin{{cases}} x_A=\\dfrac{{x_B+x_C+x_E}}{{3}} \\\\ y_A=\\dfrac{{y_B+y_C+y_E}}{{3}} \\end{{cases}} \\Leftrightarrow \\begin{{cases}} {xA}=\\dfrac{{{num_xE}}}{{3}} \\\\ {yA}=\\dfrac{{{num_yE}}}{{3}} \\end{{cases}} \\Leftrightarrow \\begin{{cases}} x_E={xE} \\\\ y_E={yE} \\end{{cases}}$ nên $E({xE};{yE})$.'
    loigiai_vd_1 = f'{tt_vd}: Gọi $H(x;y) \\Rightarrow \\overrightarrow{{AH}}=({ah_x};{ah_y})$, $\\overrightarrow{{BH}}=({bh_x};{bh_y})$; $\\overrightarrow{{BC}}=({bc1};{bc2})$, $\\overrightarrow{{AC}}=({ac1};{ac2})$.\\\\ $H$ là trực tâm tam giác $ABC$ nên $\\begin{{cases}} AH\\perp BC \\\\ BH\\perp AC \\end{{cases}} \\Leftrightarrow \\begin{{cases}} \\overrightarrow{{AH}}\\cdot\\overrightarrow{{BC}}=0 \\\\ \\overrightarrow{{BH}}\\cdot\\overrightarrow{{AC}}=0 \\end{{cases}}$\\\\ $\\Leftrightarrow \\begin{{cases}} {h_eq1} \\\\ {h_eq2} \\end{{cases}} \\Leftrightarrow \\begin{{cases}} x={xH_tex} \\\\ y={yH_tex} \\end{{cases}}$ hay $H{H_str}$.'
    loigiai_vdc_1 = f'{tt_vdc}: Gọi $I(x;y)$ là tâm đường tròn ngoại tiếp tam giác $ABC$.\\\\ Ta có: $IA=IB=IC \\Leftrightarrow \\begin{{cases}} AI^2=BI^2 \\\\ AI^2=CI^2 \\end{{cases}} \\Leftrightarrow \\begin{{cases}} {fmt_sq("x", xA)}+{fmt_sq("y", yA)}={fmt_sq("x", xB)}+{fmt_sq("y", yB)} \\\\ {fmt_sq("x", xA)}+{fmt_sq("y", yA)}={fmt_sq("x", xC)}+{fmt_sq("y", yC)} \\end{{cases}}$\\\\ $\\Leftrightarrow \\begin{{cases}} {lhs_A}={rhs_B} \\\\ {lhs_A}={rhs_C} \\end{{cases}} \\Leftrightarrow \\begin{{cases}} {eq1_lhs}={eq1_rhs} \\\\ {eq2_lhs}={eq2_rhs} \\end{{cases}} \\Leftrightarrow \\begin{{cases}} x={xI_tex} \\\\ y={yI_tex} \\end{{cases}} \\Rightarrow I{I_str}$.'
    list_nb_1 = [nb_da_1]
    list_th_1 = [th_da_1]
    list_vd_1 = [vd_da_1]
    list_vdc_1 = [vdc_da_1]
    list_nb_2 = [loigiai_nb_1]
    list_th_2 = [loigiai_th_1]
    list_vd_2 = [loigiai_vd_1]
    list_vdc_2 = [loigiai_vdc_1]
    combined_nb = list(zip(list_nb_1, list_nb_2))
    combined_th = list(zip(list_th_1, list_th_2))
    combined_vd = list(zip(list_vd_1, list_vd_2))
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))
    random.shuffle(combined_nb)
    random.shuffle(combined_th)
    random.shuffle(combined_vd)
    random.shuffle(combined_vdc)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\choiceTFn \n'
        '{'+str(shuffled_answers_nb[0])+'}\n'
        '{'+str(shuffled_answers_th[0])+'}\n'
        '{'+str(shuffled_answers_vd[0])+'}\n'
        '{'+str(shuffled_answers_vdc[0])+'}\n'
        '\\loigiai{ \n'
        '\\begin{enumEX}[a)]{1} \n'
        '\\item '+str(shuffled_solutions_nb[0])+'\n'
        '\\item '+str(shuffled_solutions_th[0])+'\n'
        '\\item '+str(shuffled_solutions_vd[0])+'\n'
        '\\item '+str(shuffled_solutions_vdc[0])+'\n'
        '\\end{enumEX}} \n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content

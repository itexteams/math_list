
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


def bt_dang10_p2_b4_c2_hh10(self):
    def fmt_coord(u, v):
        ru, rv = Rational(u), Rational(v)
        su = latex(ru).replace('\\frac', '\\dfrac')
        sv = latex(rv).replace('\\frac', '\\dfrac')
        if ru.q != 1 or rv.q != 1:
            return f'\\left({su};{sv}\\right)'
        return f'({su};{sv})'
    def fmt_shift(var_s, val):
        if val == 0:
            return f'{var_s}'
        if val > 0:
            return f'{var_s}-{val}'
        return f'{var_s}+{-val}'
    def fmt_k_shift(k, var_s, val, is_first=False):
        expr = fmt_shift(var_s, val)
        if val == 0:
            if k == 1:
                return f'{var_s}' if is_first else f'+{var_s}'
            if k == -1:
                return f'-{var_s}'
            if k > 0:
                return f'{k}{var_s}' if is_first else f'+{k}{var_s}'
            return f'{k}{var_s}'
        if k == 1:
            return f'{expr}' if is_first else f'+{expr}'
        if k == -1:
            return f'-({expr})'
        if k > 0:
            return f'{k}({expr})' if is_first else f'+{k}({expr})'
        return f'{k}({expr})'
    def fmt_vec_eq(k2, k3):
        s2 = '+\\overrightarrow{BN}' if k2 == 1 else ('-\\overrightarrow{BN}' if k2 == -1 else (f'+{k2}\\overrightarrow{{BN}}' if k2 > 0 else f'{k2}\\overrightarrow{{BN}}'))
        s3 = '+\\overrightarrow{CN}' if k3 == 1 else ('-\\overrightarrow{CN}' if k3 == -1 else (f'+{k3}\\overrightarrow{{CN}}' if k3 > 0 else f'{k3}\\overrightarrow{{CN}}'))
        return f'\\overrightarrow{{AN}}{s2}{s3}=\\vec{{0}}'
    vals = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    while True:
        xA, yA = random.choice(vals), random.choice(vals)
        xB, yB = random.choice(vals), random.choice(vals)
        xC, yC = random.choice(vals), random.choice(vals)
        ab1, ab2 = xB - xA, yB - yA
        ac1, ac2 = xC - xA, yC - yA
        bc1, bc2 = xC - xB, yC - yB
        if ab1 == 0 or ab2 == 0 or ac1 == 0 or ac2 == 0 or bc1 == 0 or bc2 == 0:
            continue
        if ab1 * ac2 == ab2 * ac1:
            continue
        k2 = random.choice([2, 3])
        k3 = random.choice([-5, -4, -3, -2])
        denom = 1 + k2 + k3
        if denom == 0:
            continue
        num_x = xA + k2 * xB + k3 * xC
        num_y = yA + k2 * yB + k3 * yC
        if num_x % denom != 0 or num_y % denom != 0:
            continue
        xN, yN = num_x // denom, num_y // denom
        if abs(xN) <= 20 and abs(yN) <= 20:
            break
    xI, yI = Rational(xA + xB, 2), Rational(yA + yB, 2)
    I_str = fmt_coord(xI, yI)
    xI_tex = latex(xI).replace('\\frac', '\\dfrac')
    yI_tex = latex(yI).replace('\\frac', '\\dfrac')
    vec_eq = fmt_vec_eq(k2, k3)
    noidungcauhoi = f'Cho ba điểm $A({xA};{yA})$, $B({xB};{yB})$, $C({xC};{yC})$. Xét tính đúng sai của các khẳng định sau:\n'
    wrong_ab = random.choice([p for p in [(-ab1, ab2), (ab1, -ab2), (-ab1, -ab2), (ab2, ab1), (ab1 + 1, ab2)] if p != (ab1, ab2)])
    nb_da_1_d = f'\\True $\\overrightarrow{{AB}}=({ab1};{ab2})$'
    nb_da_1_s = f'$\\overrightarrow{{AB}}=({wrong_ab[0]};{wrong_ab[1]})$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    wrong_ac_bc = random.choice([p for p in [((-ac1, ac2), (bc1, bc2)), ((ac1, -ac2), (bc1, bc2)), ((ac1, ac2), (-bc1, bc2)), ((ac1, ac2), (bc1, -bc2)), ((ac1 + 1, ac2), (bc1, bc2))] if p != ((ac1, ac2), (bc1, bc2))])
    th_da_1_d = f'\\True $\\overrightarrow{{AC}}=({ac1};{ac2}); \\overrightarrow{{BC}}=({bc1};{bc2})$'
    th_da_1_s = f'$\\overrightarrow{{AC}}=({wrong_ac_bc[0][0]};{wrong_ac_bc[0][1]}); \\overrightarrow{{BC}}=({wrong_ac_bc[1][0]};{wrong_ac_bc[1][1]})$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    wrong_I = random.choice([p for p in [(-xI, yI), (xI, -yI), (yI, xI), (xI + 1, yI), (xI, yI + 1)] if p != (xI, yI)])
    wI_str = fmt_coord(wrong_I[0], wrong_I[1])
    vd_da_1_d = f'\\True Tọa độ trung điểm của đoạn $AB$ là $I{I_str}$'
    vd_da_1_s = f'Tọa độ trung điểm của đoạn $AB$ là $I{wI_str}$'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    wrong_N = random.choice([p for p in [(xN, yN + 10), (xN, -yN), (-xN, yN), (xN + 2, yN), (xN, yN + 2), (xN - 2, yN)] if p != (xN, yN)])
    vdc_da_1_d = f'\\True Tọa độ điểm $N$ sao cho ${vec_eq}$ là $N({xN};{yN})$'
    vdc_da_1_s = f'Tọa độ điểm $N$ sao cho ${vec_eq}$ là $N({wrong_N[0]};{wrong_N[1]})$'
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
    num_xI = f'{xA}+{xB}'.replace('+-', '-').replace('--', '+')
    num_yI = f'{yA}+{yB}'.replace('+-', '-').replace('--', '+')
    an_x, an_y = fmt_shift('x', xA), fmt_shift('y', yA)
    bn_x, bn_y = fmt_shift('x', xB), fmt_shift('y', yB)
    cn_x, cn_y = fmt_shift('x', xC), fmt_shift('y', yC)
    eq_x = fmt_k_shift(1, 'x', xA, True) + fmt_k_shift(k2, 'x', xB, False) + fmt_k_shift(k3, 'x', xC, False) + '=0'
    eq_y = fmt_k_shift(1, 'y', yA, True) + fmt_k_shift(k2, 'y', yB, False) + fmt_k_shift(k3, 'y', yC, False) + '=0'
    loigiai_nb_1 = f'{tt_nb}: $\\overrightarrow{{AB}}=({ab1};{ab2})$.'
    loigiai_th_1 = f'{tt_th}: $\\overrightarrow{{AC}}=({ac1};{ac2}); \\overrightarrow{{BC}}=({bc1};{bc2})$.'
    loigiai_vd_1 = f'{tt_vd}: Vì $I$ là trung điểm của đoạn $AB$ nên $\\begin{{cases}} x_I=\\dfrac{{{num_xI}}}{{2}}={xI_tex} \\\\ y_I=\\dfrac{{{num_yI}}}{{2}}={yI_tex} \\end{{cases}}$ nên $I{I_str}$.'
    loigiai_vdc_1 = f'{tt_vdc}: Gọi $N(x;y)$. Ta có $\\overrightarrow{{AN}}=({an_x};{an_y})$; $\\overrightarrow{{BN}}=({bn_x};{bn_y})$; $\\overrightarrow{{CN}}=({cn_x};{cn_y})$.\\\\ Vì ${vec_eq} \\Leftrightarrow \\begin{{cases}} {eq_x} \\\\ {eq_y} \\end{{cases}} \\Leftrightarrow \\begin{{cases}} x={xN} \\\\ y={yN} \\end{{cases}}$ nên $N({xN};{yN})$.'
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

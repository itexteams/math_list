
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


def bt_dang15_p2_b4_c2_hh10(self):
    def fmt_coord(u, v):
        ru, rv = Rational(u), Rational(v)
        su = latex(ru).replace('\\frac', '\\dfrac')
        sv = latex(rv).replace('\\frac', '\\dfrac')
        if ru.q != 1 or rv.q != 1:
            return f'\\left({su};{sv}\\right)'
        return f'({su};{sv})'
    def fmt_dist(dx, dy):
        sq1, sq2 = dx**2, dy**2
        total = sq1 + sq2
        val = sp.sqrt(total)
        val_tex = latex(val)
        if val.is_integer or val_tex == f'\\sqrt{{{total}}}':
            return f'\\sqrt{{{sq1}+{sq2}}}={val_tex}'
        return f'\\sqrt{{{sq1}+{sq2}}}=\\sqrt{{{total}}}={val_tex}'
    uv_vals = [-4, -3, -2, -1, 1, 2, 3, 4]
    a_vals = [-4, -3, -2, -1, 1, 2, 3, 4]
    while True:
        u, v = random.choice(uv_vals), random.choice(uv_vals)
        if abs(u) == abs(v) or u**2 + v**2 > 20:
            continue
        k = random.choice([2, 3])
        orient = random.choice([-1, 1])
        ac1, ac2 = (-k * v, k * u) if orient == 1 else (k * v, -k * u)
        xA, yA = random.choice(a_vals), random.choice(a_vals)
        xB, yB = xA + u, yA + v
        xC, yC = xA + ac1, yA + ac2
        coords = [xA, yA, xB, yB, xC, yC]
        if any(c == 0 or abs(c) > 12 for c in coords):
            continue
        if (xB + xC) % 2 != 0 or (yB + yC) % 2 != 0:
            continue
        if (k * (u**2 + v**2)) % 2 != 0:
            continue
        xN, yN = Rational(xA + xC, 2), Rational(yA + yC, 2)
        if xN == xB or yN == yB:
            continue
        break
    ab1, ab2 = xB - xA, yB - yA
    bc1, bc2 = xC - xB, yC - yB
    bc_sq = bc1**2 + bc2**2
    ab_tex = latex(sp.sqrt(ab1**2 + ab2**2))
    ac_tex = latex(sp.sqrt(ac1**2 + ac2**2))
    S_val = (k * (ab1**2 + ab2**2)) // 2
    xI, yI = (xB + xC) // 2, (yB + yC) // 2
    N_str = fmt_coord(xN, yN)
    xN_tex = latex(xN).replace('\\frac', '\\dfrac')
    yN_tex = latex(yN).replace('\\frac', '\\dfrac')
    num_BN = int((2 * xN - 2 * xB)**2 + (2 * yN - 2 * yB)**2)
    BN_val = sp.sqrt(Rational(num_BN, 4))
    BN_tex = latex(BN_val).replace('\\frac', '\\dfrac')
    noidungcauhoi = f'Cho $A({xA};{yA})$, $B({xB};{yB})$, $C({xC};{yC})$. Xét tính đúng sai của các khẳng định sau:\n'
    wrong_v = random.choice(['B', 'C'])
    nb_da_1_d = '\\True $\\triangle ABC$ vuông tại $A$'
    nb_da_1_s = f'$\\triangle ABC$ vuông tại ${wrong_v}$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    wrong_S = random.choice([s for s in [S_val - 3, S_val + 3, 2 * S_val, S_val - 2, S_val + 2] if s > 0 and s != S_val])
    th_da_1_d = f'\\True $S_{{\\triangle ABC}}={S_val}$'
    th_da_1_s = f'$S_{{\\triangle ABC}}={wrong_S}$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    wrong_BN_cands = [sp.sqrt(Rational(max(5, num_BN // 10), 4)), sp.sqrt(Rational(num_BN + 4, 4)), sp.sqrt(Rational(max(4, num_BN - 4), 4)), sp.sqrt(num_BN)]
    wrong_BN = random.choice([val for val in wrong_BN_cands if val != BN_val])
    wrong_BN_tex = latex(wrong_BN).replace('\\frac', '\\dfrac')
    vd_da_1_d = f'\\True Độ dài trung tuyến $BN={BN_tex}$'
    vd_da_1_s = f'Độ dài trung tuyến $BN={wrong_BN_tex}$'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    wrong_I = random.choice([p for p in [(-xI, yI), (xI, -yI), (yI, xI), (xI + 1, yI), (xI, yI + 1), (xI - 1, yI)] if p != (xI, yI)])
    vdc_da_1_d = f'\\True $I({xI};{yI})$ là tọa độ tâm đường tròn ngoại tiếp $\\triangle ABC$'
    vdc_da_1_s = f'$I({wrong_I[0]};{wrong_I[1]})$ là tọa độ tâm đường tròn ngoại tiếp $\\triangle ABC$'
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
    num_xN = f'{xA}+{xC}'.replace('+-', '-').replace('--', '+')
    num_yN = f'{yA}+{yC}'.replace('+-', '-').replace('--', '+')
    dx_bn = f'{xN_tex}-{xB}' if xB > 0 else f'{xN_tex}+{-xB}'
    dy_bn = f'{yN_tex}-{yB}' if yB > 0 else f'{yN_tex}+{-yB}'
    num_xI = f'{xB}+{xC}'.replace('+-', '-').replace('--', '+')
    num_yI = f'{yB}+{yC}'.replace('+-', '-').replace('--', '+')
    loigiai_nb_1 = f'{tt_nb}: $AB={fmt_dist(ab1, ab2)}$; $BC={fmt_dist(bc1, bc2)}$; $AC={fmt_dist(ac1, ac2)}$.\\\\ Khi đó $BC^2=AB^2+AC^2={bc_sq} \\Rightarrow \\triangle ABC$ vuông tại $A$.'
    loigiai_th_1 = f'{tt_th}: $S_{{\\triangle ABC}}=\\dfrac{{1}}{{2}}AB\\cdot AC=\\dfrac{{1}}{{2}}\\cdot {ab_tex}\\cdot {ac_tex}={S_val}$.'
    loigiai_vd_1 = f'{tt_vd}: Gọi $N$ là trung điểm $AC \\Leftrightarrow \\begin{{cases}} x_N=\\dfrac{{x_A+x_C}}{{2}}=\\dfrac{{{num_xN}}}{{2}}={xN_tex} \\\\ y_N=\\dfrac{{y_A+y_C}}{{2}}=\\dfrac{{{num_yN}}}{{2}}={yN_tex} \\end{{cases}} \\Rightarrow N{N_str}$.\\\\ Khi đó $BN=\\sqrt{{\\left({dx_bn}\\right)^2+\\left({dy_bn}\\right)^2}}={BN_tex}$.'
    loigiai_vdc_1 = f'{tt_vdc}: Gọi $I$ là tâm đường tròn ngoại tiếp $\\triangle ABC$. $\\triangle ABC$ vuông tại $A \\Rightarrow I$ là trung điểm $BC \\Leftrightarrow \\begin{{cases}} x_I=\\dfrac{{x_B+x_C}}{{2}}=\\dfrac{{{num_xI}}}{{2}}={xI} \\\\ y_I=\\dfrac{{y_B+y_C}}{{2}}=\\dfrac{{{num_yI}}}{{2}}={yI} \\end{{cases}} \\Rightarrow I({xI};{yI})$.'
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

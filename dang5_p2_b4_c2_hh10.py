
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


def bt_dang5_p2_b4_c2_hh10(self):
    def fmt_coord(u, v):
        ru, rv = Rational(u), Rational(v)
        su = latex(ru).replace('\\frac', '\\dfrac')
        sv = latex(rv).replace('\\frac', '\\dfrac')
        if ru.q != 1 or rv.q != 1:
            return f'\\left({su};{sv}\\right)'
        return f'({su};{sv})'
    def fmt_var_sub(var_s, val):
        if val == 0:
            return f'{var_s}'
        if val > 0:
            return f'{var_s}-{val}'
        return f'{var_s}+{-val}'
    def fmt_num_sub_var(val, var_s):
        if val == 0:
            return f'-{var_s}'
        return f'{val}-{var_s}'
    vals = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    while True:
        xA, yA, xB, yB = random.choice(vals), random.choice(vals), random.choice(vals), random.choice(vals)
        m = random.choice([-4, -3, -2, 2, 3, 4])
        k = random.choice([-4, -3, -2, 2, 3, 4])
        if xA == xB or yA == yB or (xA == 0 and yA == 0) or (xB == 0 and yB == 0):
            continue
        ab1, ab2 = xB - xA, yB - yA
        xC, yC = m * ab1, m * ab2
        ac1, ac2 = xC - xA, yC - yA
        xD, yD = 2 * xC - xA, 2 * yC - yA
        if ac1 != 0 and ac2 != 0 and xD != 0:
            break
    xM, yM = Rational(xA - k * xB, 1 - k), Rational(yA - k * yB, 1 - k)
    M_str = fmt_coord(xM, yM)
    noidungcauhoi = f'Cho hai điểm $A({xA};{yA})$, $B({xB};{yB})$. Xét tính đúng sai của các khẳng định sau:\n'
    wrong_ab = random.choice([p for p in [(-ab1, ab2), (ab1, -ab2), (-ab1, -ab2), (ab2, ab1), (ab1 + 1, ab2)] if p != (ab1, ab2)])
    nb_da_1_d = f'\\True $\\overrightarrow{{AB}}=({ab1};{ab2})$'
    nb_da_1_s = f'$\\overrightarrow{{AB}}=({wrong_ab[0]};{wrong_ab[1]})$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    wrong_C = random.choice([p for p in [(xC, -yC), (-xC, yC), (xC, yC + 2), (xC + 2, yC), (xC, -ab2)] if p != (xC, yC)])
    th_da_1_d = f'\\True Tọa độ điểm $C$ sao cho $\\overrightarrow{{OC}}={m}\\overrightarrow{{AB}}$ là $C({xC};{yC})$'
    th_da_1_s = f'Tọa độ điểm $C$ sao cho $\\overrightarrow{{OC}}={m}\\overrightarrow{{AB}}$ là $C({wrong_C[0]};{wrong_C[1]})$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    wrong_xD = random.choice([val for val in [xD - 2, xD + 2, -xD, xD - 1, xD + 1] if val != xD])
    vd_da_1_d = f'\\True Tọa độ điểm $D$ đối xứng của $A$ qua $C$ có hoành độ bằng ${xD}$'
    vd_da_1_s = f'Tọa độ điểm $D$ đối xứng của $A$ qua $C$ có hoành độ bằng ${wrong_xD}$'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    wrong_M = random.choice([p for p in [(xM, -yM), (-xM, yM), (Rational(xA + k * xB, 1 + k), Rational(yA + k * yB, 1 + k)), (xM + 1, yM), (xM, yM + 1)] if p != (xM, yM)])
    wM_str = fmt_coord(wrong_M[0], wrong_M[1])
    vdc_da_1_d = f'\\True Tọa độ điểm $M$ chia đoạn $AB$ theo tỉ số $k={k}$ là $M{M_str}$'
    vdc_da_1_s = f'Tọa độ điểm $M$ chia đoạn $AB$ theo tỉ số $k={k}$ là $M{wM_str}$'
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
    cd_x, cd_y = fmt_var_sub('c', xC), fmt_var_sub('d', yC)
    ma_x, ma_y = fmt_num_sub_var(xA, 'x'), fmt_num_sub_var(yA, 'y')
    mb_x, mb_y = fmt_num_sub_var(xB, 'x'), fmt_num_sub_var(yB, 'y')
    loigiai_nb_1 = f'{tt_nb}: Ta có $\\overrightarrow{{AB}}=({xB}-{xA};{yB}-{yA})=({ab1};{ab2})$.'.replace('--', '+').replace('+-', '-')
    loigiai_th_1 = f'{tt_th}: Gọi $C(a;b) \\Rightarrow \\overrightarrow{{OC}}=(a;b)$. Ta có $\\overrightarrow{{OC}}={m}\\overrightarrow{{AB}} \\Leftrightarrow \\begin{{cases}} a={xC} \\\\ b={yC} \\end{{cases}}$ nên $C({xC};{yC})$.'
    loigiai_vd_1 = f'{tt_vd}: Gọi $D(c;d) \\Rightarrow \\overrightarrow{{CD}}=({cd_x};{cd_y})$; $\\overrightarrow{{AC}}=({ac1};{ac2})$.\\\\ Khi đó: $\\overrightarrow{{AC}}=\\overrightarrow{{CD}} \\Leftrightarrow \\begin{{cases}} {cd_x}={ac1} \\\\ {cd_y}={ac2} \\end{{cases}} \\Rightarrow D({xD};{yD})$. Vậy hoành độ điểm $D$ bằng ${xD}$.'
    loigiai_vdc_1 = f'{tt_vdc}: Gọi $M(x;y) \\Rightarrow \\overrightarrow{{MA}}=({ma_x};{ma_y})$; $\\overrightarrow{{MB}}=({mb_x};{mb_y})$.\\\\ Vì $M$ chia đoạn $AB$ theo tỉ số $k={k} \\Rightarrow \\overrightarrow{{MA}}={k}\\overrightarrow{{MB}} \\Rightarrow \\begin{{cases}} {ma_x}={k}({mb_x}) \\\\ {ma_y}={k}({mb_y}) \\end{{cases}} \\Rightarrow M{M_str}$.'
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

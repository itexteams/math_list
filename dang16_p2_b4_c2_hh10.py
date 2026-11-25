
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


def bt_dang16_p2_b4_c2_hh10(self):
    def fmt_shift(var_s, val):
        if val == 0:
            return f'{var_s}'
        if val > 0:
            return f'{var_s}-{val}'
        return f'{var_s}+{-val}'
    def fmt_lin(coef, const, var_s):
        if const == 0:
            return f'{coef}{var_s}'
        if const > 0:
            return f'{coef}{var_s}+{const}'
        return f'{coef}{var_s}{const}'
    def fmt_signed_coef_vec(coef, vec_str):
        return f'+{coef}{vec_str}' if coef > 0 else f'{coef}{vec_str}'
    vals = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]
    while True:
        xA, yA = random.choice(vals), random.choice(vals)
        xB, yB = random.choice(vals), random.choice(vals)
        xC, yC = random.choice(vals), random.choice(vals)
        ab1, ab2 = xB - xA, yB - yA
        ac1, ac2 = xC - xA, yC - yA
        bc1, bc2 = xC - xB, yC - yB
        if ab1 == 0 or ab2 == 0 or ac1 == 0 or ac2 == 0 or (bc1 == 0 and bc2 == 0):
            continue
        if ab1 * ac2 == ab2 * ac1:
            continue
        if (yA * ab1) % ab2 != 0:
            continue
        xE = xA - (yA * ab1) // ab2
        xD = 3 * xC - xA - xB
        yD = 3 * yC - yA - yB
        if xE == 0 or abs(xE) > 15 or xD == 0 or yD == 0 or abs(xD) > 18 or abs(yD) > 18:
            continue
        p = random.choice([-3, -2, 2, 3])
        q = random.choice([-3, -2, 2, 3])
        num_xF = xA + bc1 + p * ac1 - q * xC
        num_yF = yA + bc2 + p * ac2 - q * yC
        if num_xF % (1 - q) != 0 or num_yF % (1 - q) != 0:
            continue
        xF = num_xF // (1 - q)
        yF = num_yF // (1 - q)
        if xF != 0 and yF != 0 and abs(xF) <= 25 and abs(yF) <= 25:
            break
    vec_ac = '\\overrightarrow{AC}'
    vec_cf = '\\overrightarrow{CF}'
    term_ac = fmt_signed_coef_vec(p, vec_ac)
    term_cf = fmt_signed_coef_vec(q, vec_cf)
    vec_rhs = f'\\overrightarrow{{BC}}{term_ac}{term_cf}'
    vec_eq = f'\\overrightarrow{{AF}}={vec_rhs}'
    noidungcauhoi = f'Trong mặt phẳng tọa độ $Oxy$, cho các điểm $A({xA};{yA})$, $B({xB};{yB})$, $C({xC};{yC})$. Xét tính đúng sai của các khẳng định sau:\n'
    wrong_D = random.choice([p_pt for p_pt in [(xD, -yD), (-xD, yD), (xD + 2, yD), (xD - 2, yD), (xD, yD + 2)] if p_pt != (xD, yD)])
    nb_da_1_d = f'\\True Tọa độ điểm $D$ sao cho $C$ là trọng tâm tam giác $ABD$ là $D({xD};{yD})$'
    nb_da_1_s = f'Tọa độ điểm $D$ sao cho $C$ là trọng tâm tam giác $ABD$ là $D({wrong_D[0]};{wrong_D[1]})$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    wrong_xE = random.choice([val for val in [-xE, xE + 2, xE - 2, xE + 1, xE - 1] if val != xE])
    th_da_1_d = f'\\True Tọa độ điểm $E$ thuộc trục hoành sao cho $A, B, E$ thẳng hàng là $E({xE};0)$'
    th_da_1_s = f'Tọa độ điểm $E$ thuộc trục hoành sao cho $A, B, E$ thẳng hàng là $E({wrong_xE};0)$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    wrong_bc_ac = random.choice([pair for pair in [((-bc1, bc2), (ac1, ac2)), ((bc1, -bc2), (ac1, ac2)), ((bc1, bc2), (-ac1, ac2)), ((bc1, bc2), (ac1, -ac2)), ((bc1 + 1, bc2), (ac1, ac2))] if pair != ((bc1, bc2), (ac1, ac2))])
    vd_da_1_d = f'\\True $\\overrightarrow{{BC}}=({bc1};{bc2}), \\overrightarrow{{AC}}=({ac1};{ac2})$'
    vd_da_1_s = f'$\\overrightarrow{{BC}}=({wrong_bc_ac[0][0]};{wrong_bc_ac[0][1]}), \\overrightarrow{{AC}}=({wrong_bc_ac[1][0]};{wrong_bc_ac[1][1]})$'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    wrong_F = random.choice([f_pt for f_pt in [(xF, -yF), (-xF, yF), (xF + 2, yF), (xF - 2, yF), (xF, yF + 2)] if f_pt != (xF, yF)])
    vdc_da_1_d = f'\\True Tọa độ $F$ thỏa mãn ${vec_eq}$ là $F({xF};{yF})$'
    vdc_da_1_s = f'Tọa độ $F$ thỏa mãn ${vec_eq}$ là $F({wrong_F[0]};{wrong_F[1]})$'
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
    num_xD = f'{xA}+{xB}+x_D'.replace('+-', '-').replace('--', '+')
    num_yD = f'{yA}+{yB}+y_D'.replace('+-', '-').replace('--', '+')
    ae_x = fmt_shift('x', xA)
    rhs_ae = (-yA * ab1) // ab2
    af_x, af_y = fmt_shift('x', xA), fmt_shift('y', yA)
    cf_x, cf_y = fmt_shift('x', xC), fmt_shift('y', yC)
    q_cf_x = fmt_lin(q, -q * xC, 'x')
    q_cf_y = fmt_lin(q, -q * yC, 'y')
    rhs_x = fmt_lin(q, bc1 + p * ac1 - q * xC, 'x')
    rhs_y = fmt_lin(q, bc2 + p * ac2 - q * yC, 'y')
    loigiai_nb_1 = f'{tt_nb}: Điểm $C$ là trọng tâm tam giác $ABD$\\\\ $\\Leftrightarrow \\begin{{cases}} x_C=\\dfrac{{x_A+x_B+x_D}}{{3}} \\\\ y_C=\\dfrac{{y_A+y_B+y_D}}{{3}} \\end{{cases}} \\Leftrightarrow \\begin{{cases}} {xC}=\\dfrac{{{num_xD}}}{{3}} \\\\ {yC}=\\dfrac{{{num_yD}}}{{3}} \\end{{cases}} \\Leftrightarrow \\begin{{cases}} x_D={xD} \\\\ y_D={yD} \\end{{cases}}$ nên $D({xD};{yD})$.'
    loigiai_th_1 = f'{tt_th}: Gọi $E(x;0)\\in Ox \\Rightarrow \\overrightarrow{{AE}}=({ae_x};{-yA}), \\overrightarrow{{AB}}=({ab1};{ab2})$.\\\\ Ba điểm $A, B, E$ thẳng hàng $\\Leftrightarrow \\overrightarrow{{AE}}$ cùng phương $\\overrightarrow{{AB}} \\Leftrightarrow \\dfrac{{{ae_x}}}{{{ab1}}}=\\dfrac{{{-yA}}}{{{ab2}}} \\Leftrightarrow {ae_x}={rhs_ae} \\Leftrightarrow x={xE}$.\\\\ Vậy $E({xE};0)$.'
    loigiai_vd_1 = f'{tt_vd}: Ta có $\\overrightarrow{{BC}}=({bc1};{bc2}), \\overrightarrow{{AC}}=({ac1};{ac2})$.'
    loigiai_vdc_1 = f'{tt_vdc}: Gọi $F(x;y)$. Ta có: $\\overrightarrow{{AF}}=({af_x};{af_y}), \\overrightarrow{{BC}}=({bc1};{bc2}), \\overrightarrow{{AC}}=({ac1};{ac2})$\\\\ $\\Rightarrow {p}\\overrightarrow{{AC}}=({p * ac1};{p * ac2}), \\overrightarrow{{CF}}=({cf_x};{cf_y}), {q}\\overrightarrow{{CF}}=({q_cf_x};{q_cf_y})$.\\\\ Suy ra ${vec_rhs}=({rhs_x};{rhs_y})$.\\\\ Ta có ${vec_eq} \\Leftrightarrow \\begin{{cases}} {af_x}={rhs_x} \\\\ {af_y}={rhs_y} \\end{{cases}} \\Leftrightarrow \\begin{{cases}} x={xF} \\\\ y={yF} \\end{{cases}}$. Vậy $F({xF};{yF})$.'
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

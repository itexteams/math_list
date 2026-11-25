
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


def bt_dang11_p2_b4_c2_hh10(self):
    def fmt_coord(u, v):
        ru, rv = Rational(u), Rational(v)
        su = latex(ru).replace('\\frac', '\\dfrac')
        sv = latex(rv).replace('\\frac', '\\dfrac')
        if ru.q != 1 or rv.q != 1:
            return f'\\left({su};{sv}\\right)'
        return f'({su};{sv})'
    def fmt_sq(val):
        return f'({val})^2' if val < 0 else f'{val}^2'
    def fmt_diff_sq(a, b):
        return f'[{a}-({b})]^2' if b < 0 else f'({a}-{b})^2'
    def fmt_mul(val):
        return f'({val})' if val < 0 else f'{val}'
    def fmt_sub_var(val, var_s):
        return f'-{var_s}' if val == 0 else f'{val}-{var_s}'
    def fmt_cos_chain(dot_val, sq1, sq2):
        t1 = latex(sp.sqrt(sq1))
        t2 = latex(sp.sqrt(sq2))
        raw = f'\\dfrac{{{dot_val}}}{{{t1}\\cdot {t2}}}'
        simp = latex(Rational(dot_val, 1) / (sp.sqrt(sq1) * sp.sqrt(sq2))).replace('\\frac', '\\dfrac')
        if sp.sqrt(sq1 * sq2).is_integer or math.gcd(abs(dot_val), int(sp.sqrt(sq1)) if sp.sqrt(sq1).is_integer else 1) > 1 or math.gcd(abs(dot_val), int(sp.sqrt(sq2)) if sp.sqrt(sq2).is_integer else 1) > 1:
            if simp != raw:
                return f'{raw}={simp}'
        return raw
    vals = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]
    while True:
        xA, yA = random.choice(vals), random.choice(vals)
        xB, yB = random.choice(vals), random.choice(vals)
        xC, yC = random.choice(vals), random.choice(vals)
        ab1, ab2 = xB - xA, yB - yA
        ac1, ac2 = xC - xA, yC - yA
        bc1, bc2 = xC - xB, yC - yB
        if ab1 == 0 or ab2 == 0 or (ac1 == 0 and ac2 == 0) or (bc1 == 0 and bc2 == 0):
            continue
        if ab1 * ac2 == ab2 * ac1:
            continue
        if xA + xB + xC == 0 and yA + yB + yC == 0:
            continue
        xD, yD = xC - ab1, yC - ab2
        if xD == 0 or yD == 0 or abs(xD) > 15 or abs(yD) > 15:
            continue
        ab_sq = ab1**2 + ab2**2
        ac_sq = ac1**2 + ac2**2
        bc_sq = bc1**2 + bc2**2
        dot_AB_AC = ab1 * ac1 + ab2 * ac2
        ba1, ba2 = -ab1, -ab2
        dot_BA_BC = ba1 * bc1 + ba2 * bc2
        cosA_num = dot_AB_AC / math.sqrt(ab_sq * ac_sq)
        cosB_num = dot_BA_BC / math.sqrt(ab_sq * bc_sq)
        deg_A = round(math.degrees(math.acos(max(-1.0, min(1.0, cosA_num)))))
        deg_B = round(math.degrees(math.acos(max(-1.0, min(1.0, cosB_num)))))
        deg_C = 180 - (deg_A + deg_B)
        if 20 <= deg_C <= 130:
            break
    xG, yG = Rational(xA + xB + xC, 3), Rational(yA + yB + yC, 3)
    G_str = fmt_coord(xG, yG)
    ab_tex = latex(sp.sqrt(ab_sq))
    ac_tex = latex(sp.sqrt(ac_sq))
    bc_tex = latex(sp.sqrt(bc_sq))
    cosA_chain = fmt_cos_chain(dot_AB_AC, ab_sq, ac_sq)
    cosB_chain = fmt_cos_chain(dot_BA_BC, ab_sq, bc_sq)
    exact_A = abs(math.cos(math.radians(deg_A)) - cosA_num) < 1e-9
    exact_B = abs(math.cos(math.radians(deg_B)) - cosB_num) < 1e-9
    rel_A = '=' if exact_A else '\\approx'
    rel_B = '=' if exact_B else '\\approx'
    rel_C = '=' if (exact_A and exact_B) else '\\approx'
    noidungcauhoi = f'Trong mặt phẳng toạ độ $Oxy$, cho $A({xA};{yA})$, $B({xB};{yB})$, $C({xC};{yC})$. Xét tính đúng sai của các khẳng định sau:\n'
    nb_da_1_d = '\\True Ba điểm $A, B, C$ không thẳng hàng'
    nb_da_1_s = 'Ba điểm $A, B, C$ thẳng hàng'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    wrong_G = random.choice([p for p in [(-xG, yG), (xG, -yG), (yG, xG), (xG + 1, yG), (xG, yG + 1)] if p != (xG, yG)])
    wG_str = fmt_coord(wrong_G[0], wrong_G[1])
    th_da_1_d = f'\\True $G{G_str}$ là tọa độ trọng tâm của tam giác $ABC$'
    th_da_1_s = f'$G{wG_str}$ là tọa độ trọng tâm của tam giác $ABC$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    wrong_D = random.choice([p for p in [(xD, yD - 2), (xD, yD + 2), (-xD, yD), (xD, -yD), (xD + 2, yD)] if p != (xD, yD)])
    vd_da_1_d = f'\\True Tứ giác $ABCD$ là hình bình hành khi đó tọa độ điểm $D$ là $D({xD};{yD})$'
    vd_da_1_s = f'Tứ giác $ABCD$ là hình bình hành khi đó tọa độ điểm $D$ là $D({wrong_D[0]};{wrong_D[1]})$'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    wrong_deg = random.choice([d for d in [30, 45, 60, 75, 90, deg_C + 10, deg_C - 10] if 10 <= d <= 160 and d != deg_C])
    vdc_da_1_d = f'\\True $\\widehat{{ACB}}={deg_C}^\\circ$'
    vdc_da_1_s = f'$\\widehat{{ACB}}={wrong_deg}^\\circ$'
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
    dc_x, dc_y = fmt_sub_var(xC, 'x'), fmt_sub_var(yC, 'y')
    loigiai_nb_1 = f'{tt_nb}: Ta có: $\\overrightarrow{{AB}}=({ab1};{ab2}), \\overrightarrow{{AC}}=({ac1};{ac2})$.\\\\ Do $\\dfrac{{{ac1}}}{{{ab1}}} \\neq \\dfrac{{{ac2}}}{{{ab2}}}$ nên $\\overrightarrow{{AB}}, \\overrightarrow{{AC}}$ không cùng phương nên ba điểm $A, B, C$ không thẳng hàng.'
    loigiai_th_1 = f'{tt_th}: Do $G$ là trọng tâm của tam giác $ABC$ nên $G\\left(\\dfrac{{{xA}+{xB}+{xC}}}{{3}};\\dfrac{{{yA}+{yB}+{yC}}}{{3}}\\right) \\Rightarrow G{G_str}$.'.replace('+-', '-').replace('--', '+')
    loigiai_vd_1 = f'{tt_vd}: Giả sử $D(x;y)$ nên ta có $\\overrightarrow{{AB}}=({ab1};{ab2}), \\overrightarrow{{DC}}=({dc_x};{dc_y})$.\\\\ Tứ giác $ABCD$ là hình bình hành nếu $\\overrightarrow{{AB}}=\\overrightarrow{{DC}} \\Leftrightarrow \\begin{{cases}} {ab1}={dc_x} \\\\ {ab2}={dc_y} \\end{{cases}} \\Leftrightarrow \\begin{{cases}} x={xD} \\\\ y={yD} \\end{{cases}}$ nên $D({xD};{yD})$.'
    loigiai_vdc_1 = f'{tt_vdc}: Ta có: $AB=\\sqrt{{{fmt_sq(ab1)}+{fmt_sq(ab2)}}}={ab_tex}$; $AC=\\sqrt{{{fmt_diff_sq(xC, xA)}+{fmt_diff_sq(yC, yA)}}}={ac_tex}$, $BC=\\sqrt{{{fmt_diff_sq(xC, xB)}+{fmt_diff_sq(yC, yB)}}}={bc_tex}$.\\\\ Ta có: $\\overrightarrow{{AB}}\\cdot\\overrightarrow{{AC}}={fmt_mul(ab1)}\\cdot {fmt_mul(ac1)}+{fmt_mul(ab2)}\\cdot {fmt_mul(ac2)}={dot_AB_AC}$.\\\\ Suy ra: $\\cos \\widehat{{BAC}}=\\cos\\left(\\overrightarrow{{AB}},\\overrightarrow{{AC}}\\right)=\\dfrac{{\\overrightarrow{{AB}}\\cdot\\overrightarrow{{AC}}}}{{\\left|\\overrightarrow{{AB}}\\right|\\cdot\\left|\\overrightarrow{{AC}}\\right|}}={cosA_chain}$ nên $\\widehat{{BAC}} {rel_A} {deg_A}^\\circ$.\\\\ Ta có: $\\overrightarrow{{BA}}\\cdot\\overrightarrow{{BC}}={fmt_mul(ba1)}\\cdot {fmt_mul(bc1)}+{fmt_mul(ba2)}\\cdot {fmt_mul(bc2)}={dot_BA_BC}$.\\\\ Suy ra $\\cos \\widehat{{ABC}}=\\cos\\left(\\overrightarrow{{BA}},\\overrightarrow{{BC}}\\right)=\\dfrac{{\\overrightarrow{{BA}}\\cdot\\overrightarrow{{BC}}}}{{\\left|\\overrightarrow{{BA}}\\right|\\cdot\\left|\\overrightarrow{{BC}}\\right|}}={cosB_chain}$ nên $\\widehat{{ABC}} {rel_B} {deg_B}^\\circ$.\\\\ Vậy $\\widehat{{ACB}}=180^\\circ-(\\widehat{{BAC}}+\\widehat{{ABC}}) {rel_C} 180^\\circ-({deg_A}^\\circ+{deg_B}^\\circ)={deg_C}^\\circ$.'
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

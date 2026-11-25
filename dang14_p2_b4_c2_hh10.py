
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


def bt_dang14_p2_b4_c2_hh10(self):
    y = symbols('y')
    def fmt_sq_num(val):
        return f'({val})^2' if val < 0 else f'{val}^2'
    def fmt_zero_sq(val):
        return f'(0-{val})^2' if val > 0 else f'(0+{-val})^2'
    def fmt_var_sq(var_s, val):
        return f'({var_s}-{val})^2' if val > 0 else f'({var_s}+{-val})^2'
    def fmt_k_mul(val):
        return f'k({val})' if val < 0 else f'k\\cdot {val}'
    triples = [(3, 4, 5), (4, 3, 5), (6, 8, 10), (8, 6, 10)]
    vals = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]
    while True:
        leg1, leg2, hyp = random.choice(triples)
        u = random.choice([-1, 1]) * leg1
        v = random.choice([-1, 1]) * leg2
        xA, yA = random.choice(vals), random.choice(vals)
        xB, yB = xA + u, yA
        xC, yC = xA, yA + v
        xD, yD = xC - u, yC
        if xB == 0 or yB == 0 or xC == 0 or yC == 0:
            continue
        if abs(xB) > 9 or abs(yC) > 9 or abs(xD) > 10:
            continue
        yN = Rational(xC**2 + yC**2 - xB**2 - yB**2, 2 * (yC - yB))
        if yN != 0:
            break
    bc1, bc2 = xC - xB, yC - yB
    S_val = (leg1 * leg2) // 2
    P_val = leg1 + leg2 + hyp
    yN_tex = latex(yN).replace('\\frac', '\\dfrac')
    N_str = f'\\left(0;{yN_tex}\\right)' if yN.q != 1 else f'(0;{yN_tex})'
    noidungcauhoi = f'Cho ba điểm $A({xA};{yA})$, $B({xB};{yB})$, $C({xC};{yC})$. Xét tính đúng sai của các khẳng định sau:\n'
    nb_da_1_d = '\\True $A, B, C$ là ba đỉnh của một tam giác'
    nb_da_1_s = 'Ba điểm $A, B, C$ thẳng hàng'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    wrong_S = random.choice([s for s in [2 * S_val, P_val, S_val + 2, S_val + 4] if s != S_val])
    th_da_1_d = f'\\True $S_{{\\triangle ABC}}={S_val}$'
    th_da_1_s = f'$S_{{\\triangle ABC}}={wrong_S}$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    wrong_D = random.choice([p for p in [(-xD, yD), (xD, -yD), (xC + u, yC), (xD + 1, yD), (xD, yD + 1)] if p != (xD, yD)])
    vd_da_1_d = f'\\True Tứ giác $ABCD$ là hình bình hành khi $D({xD};{yD})$'
    vd_da_1_s = f'Tứ giác $ABCD$ là hình bình hành khi $D({wrong_D[0]};{wrong_D[1]})$'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    wrong_yN = random.choice([val for val in [-yN, yN + 1, yN - 1, Rational(yN.p + 1, yN.q), Rational(yN.p - 1, yN.q)] if val != yN])
    wrong_yN_tex = latex(wrong_yN).replace('\\frac', '\\dfrac')
    vdc_da_1_d = f'\\True Điểm $N$ thuộc trục $Oy$ sao cho $N$ cách đều $B, C$ có tung độ bằng ${yN_tex}$'
    vdc_da_1_s = f'Điểm $N$ thuộc trục $Oy$ sao cho $N$ cách đều $B, C$ có tung độ bằng ${wrong_yN_tex}$'
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
    expr_BN = latex(sp.expand(xB**2 + (y - yB)**2))
    expr_CN = latex(sp.expand(xC**2 + (y - yC)**2))
    loigiai_nb_1 = f'{tt_nb}: Ta có $\\overrightarrow{{AB}}=({u};0)$; $\\overrightarrow{{AC}}=(0;{v})$.\\\\ Xét số thực $k$ thỏa mãn $\\overrightarrow{{AB}}=k\\overrightarrow{{AC}} \\Rightarrow \\begin{{cases}} {u}=k\\cdot 0 \\\\ 0={fmt_k_mul(v)} \\end{{cases}}$ (vô lí).\\\\ Do vậy không tồn tại số $k$ thỏa mãn $\\overrightarrow{{AB}}=k\\overrightarrow{{AC}}$ hay hai vectơ $\\overrightarrow{{AB}}, \\overrightarrow{{AC}}$ không cùng phương; suy ra ba điểm $A, B, C$ không thẳng hàng. Vậy $A, B, C$ là ba đỉnh của một tam giác.'
    loigiai_th_1 = f'{tt_th}: Ta có $AB=\\sqrt{{{fmt_sq_num(u)}+0^2}}={leg1}$, $AC=\\sqrt{{0^2+{fmt_sq_num(v)}}}={leg2}$, $\\overrightarrow{{BC}}=({bc1};{bc2})$, $BC=\\sqrt{{{fmt_sq_num(bc1)}+{fmt_sq_num(bc2)}}}={hyp}$.\\\\ Dễ thấy $AB^2+AC^2=BC^2$ nên $\\triangle ABC$ vuông tại $A$.\\\\ Chu vi tam giác $ABC$ là: $2p=AB+AC+BC={leg1}+{leg2}+{hyp}={P_val}$.\\\\ Diện tích tam giác là: $S_{{\\triangle ABC}}=\\dfrac{{1}}{{2}}AB\\cdot AC=\\dfrac{{1}}{{2}}\\cdot {leg1}\\cdot {leg2}={S_val}$.'
    loigiai_vd_1 = f'{tt_vd}: Gọi $D(x;y) \\Rightarrow \\overrightarrow{{DC}}=({xC}-x;{yC}-y)$, $\\overrightarrow{{AB}}=({u};0)$.\\\\ Tứ giác $ABCD$ là hình bình hành $\\Leftrightarrow \\overrightarrow{{AB}}=\\overrightarrow{{DC}} \\Leftrightarrow \\begin{{cases}} {xC}-x={u} \\\\ {yC}-y=0 \\end{{cases}} \\Leftrightarrow \\begin{{cases}} x={xD} \\\\ y={yD} \\end{{cases}} \\Rightarrow D({xD};{yD})$.'
    loigiai_vdc_1 = f'{tt_vdc}: Gọi $N(0;y) \\Rightarrow \\begin{{cases}} BN^2={fmt_zero_sq(xB)}+{fmt_var_sq("y", yB)} \\\\ CN^2={fmt_zero_sq(xC)}+{fmt_var_sq("y", yC)} \\end{{cases}}$.\\\\ Điểm $N$ cách đều $B$ và $C \\Leftrightarrow BN=CN \\Leftrightarrow BN^2=CN^2$\\\\ $\\Leftrightarrow {abs(xB)}^2+{fmt_var_sq("y", yB)}={abs(xC)}^2+{fmt_var_sq("y", yC)} \\Leftrightarrow {expr_BN}={expr_CN} \\Leftrightarrow y={yN_tex} \\Rightarrow N{N_str}$.'
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

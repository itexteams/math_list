
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


def bt_dang8_p2_b4_c2_hh10(self):
    def fmt_coord(u, v):
        ru, rv = Rational(u), Rational(v)
        su = latex(ru).replace('\\frac', '\\dfrac')
        sv = latex(rv).replace('\\frac', '\\dfrac')
        if ru.q != 1 or rv.q != 1:
            return f'\\left({su};{sv}\\right)'
        return f'({su};{sv})'
    def fmt_shift(var_s, val):
        return f'{var_s}-{val}' if val > 0 else f'{var_s}+{-val}'
    def fmt_mul(val):
        return f'({val})' if val < 0 else f'{val}'
    vals = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]
    while True:
        xA, yA = random.choice(vals), random.choice(vals)
        xB, yB = random.choice(vals), random.choice(vals)
        xC, yC = random.choice(vals), random.choice(vals)
        if yA * yB >= 0 or xB * xC <= 0:
            continue
        ab1, ab2 = xB - xA, yB - yA
        ac1, ac2 = xC - xA, yC - yA
        bc_p1, bc_p2 = -xC - xB, yC - yB
        if ab1 == 0 or ab2 == 0 or ac1 == 0 or ac2 == 0 or bc_p2 == 0:
            continue
        if ab1 * ac2 == ab2 * ac1:
            continue
        if xA + xB == 0 and yA + yB == 0:
            continue
        xM = Rational(xA * yB - xB * yA, yB - yA)
        yN = Rational(xB * yC + xC * yB, xB + xC)
        if xM != 0 and yN != 0:
            break
    xI, yI = Rational(xA + xB, 2), Rational(yA + yB, 2)
    I_str = fmt_coord(xI, yI)
    M_str = fmt_coord(xM, 0)
    N_str = fmt_coord(0, yN)
    xM_tex = latex(xM).replace('\\frac', '\\dfrac')
    yN_tex = latex(yN).replace('\\frac', '\\dfrac')
    noidungcauhoi = f'Trong mặt phẳng tọa độ $Oxy$, cho ba điểm $A({xA};{yA})$, $B({xB};{yB})$, $C({xC};{yC})$. Xét tính đúng sai của các khẳng định sau:\n'
    nb_da_1_d = '\\True $A, B, C$ là ba đỉnh một tam giác'
    nb_da_1_s = 'Ba điểm $A, B, C$ thẳng hàng'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    wrong_I = random.choice([p for p in [(-xI, yI), (xI, -yI), (yI, xI), (xI + 1, yI), (xI, yI + 1)] if p != (xI, yI)])
    wI_str = fmt_coord(wrong_I[0], wrong_I[1])
    th_da_1_d = f'\\True Điểm $I{I_str}$ là trung điểm của $AB$'
    th_da_1_s = f'Điểm $I{wI_str}$ là trung điểm của $AB$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    wrong_xM = random.choice([val for val in [-xM, xM + 1, xM - 1, Rational(xM.p + 1, xM.q), Rational(xM.p - 1, xM.q)] if val != xM])
    wxM_tex = latex(wrong_xM).replace('\\frac', '\\dfrac')
    vd_da_1_d = f'\\True Điểm $M$ thuộc $Ox$ sao cho $AM+BM$ bé nhất có hoành độ bằng ${xM_tex}$'
    vd_da_1_s = f'Điểm $M$ thuộc $Ox$ sao cho $AM+BM$ bé nhất có hoành độ bằng ${wxM_tex}$'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    wrong_yN = random.choice([val for val in [-yN, yN + 1, yN - 1, Rational(yN.p + 1, yN.q), Rational(yN.p - 1, yN.q)] if val != yN])
    wyN_tex = latex(wrong_yN).replace('\\frac', '\\dfrac')
    vdc_da_1_d = f'\\True Điểm $N$ thuộc $Oy$ sao cho $BN+CN$ bé nhất có tung độ bằng ${yN_tex}$'
    vdc_da_1_s = f'Điểm $N$ thuộc $Oy$ sao cho $BN+CN$ bé nhất có tung độ bằng ${wyN_tex}$'
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
    am_x = fmt_shift('x', xA)
    am_y = -yA
    lhs_c = f'{ab2}x+{-ab2 * xA}'.replace('+-', '-')
    rhs_c = ab1 * am_y
    bn_x = -xB
    bn_y = fmt_shift('y', yB)
    lhs_d = bn_x * bc_p2
    rhs_d = f'{bc_p1}y+{-bc_p1 * yB}'.replace('+-', '-')
    loigiai_nb_1 = f'{tt_nb}: Ta có: $\\overrightarrow{{AB}}=({ab1};{ab2})$, $\\overrightarrow{{AC}}=({ac1};{ac2})$ vì $\\dfrac{{{ab1}}}{{{ac1}}} \\neq \\dfrac{{{ab2}}}{{{ac2}}} \\Rightarrow \\overrightarrow{{AB}}, \\overrightarrow{{AC}}$ không cùng phương.\\\\ Vậy $A, B, C$ không thẳng hàng hay $A, B, C$ là ba đỉnh một tam giác.'
    loigiai_th_1 = f'{tt_th}: Trung điểm $AB$ có tọa độ ${I_str}$.'
    loigiai_vd_1 = f'{tt_vd}: Do $y_A\\cdot y_B={fmt_mul(yA)}\\cdot {fmt_mul(yB)}={yA * yB}<0$ nên hai điểm $A, B$ nằm khác phía so với trục $Ox$. Vì $M$ thuộc $Ox$ mà $AM+BM$ bé nhất nên $A, M, B$ thẳng hàng hay $\\overrightarrow{{AB}}, \\overrightarrow{{AM}}$ cùng phương.\\\\ Gọi $M(x;0)\\in Ox \\Rightarrow \\overrightarrow{{AM}}=({am_x};{am_y})$.\\\\ Ta có: $\\overrightarrow{{AB}}, \\overrightarrow{{AM}}$ cùng phương $\\Leftrightarrow \\dfrac{{{am_x}}}{{{ab1}}}=\\dfrac{{{am_y}}}{{{ab2}}} \\Leftrightarrow {lhs_c}={rhs_c} \\Leftrightarrow x={xM_tex}$.\\\\ Vậy $M{M_str}$.'
    loigiai_vdc_1 = f'{tt_vdc}: Do $x_B\\cdot x_C={fmt_mul(xB)}\\cdot {fmt_mul(xC)}={xB * xC}>0$ nên hai điểm $B, C$ nằm cùng phía so với trục $Oy$.\\\\ Lấy $C\'$ đối xứng với $C$ qua $Oy$, suy ra $C\'({-xC};{yC})$ (lúc này $C\'$ và $B$ khác phía so với trục $Oy$).\\\\ Vì $N$ thuộc $Oy$ nên $CN=C\'N$.\\\\ Do vậy $BN+CN=BN+C\'N$ mà tổng này bé nhất khi và chỉ khi $B, N, C\'$ thẳng hàng hay $\\overrightarrow{{BC\'}}, \\overrightarrow{{BN}}$ cùng phương.\\\\ Gọi $N(0;y)\\in Oy \\Rightarrow \\overrightarrow{{BN}}=({bn_x};{bn_y})$, $\\overrightarrow{{BC\'}}=({bc_p1};{bc_p2})$.\\\\ Ta có $\\overrightarrow{{BC\'}}, \\overrightarrow{{BN}}$ cùng phương $\\Leftrightarrow \\dfrac{{{bn_x}}}{{{bc_p1}}}=\\dfrac{{{bn_y}}}{{{bc_p2}}} \\Leftrightarrow {lhs_d}={rhs_d} \\Leftrightarrow y={yN_tex}$.\\\\ Vậy $N{N_str}$.'
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

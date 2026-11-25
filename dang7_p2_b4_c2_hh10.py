
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


def bt_dang7_p2_b4_c2_hh10(self):
    y = symbols('y')
    def fmt_sq(var_s, val):
        return f'({var_s}-{val})^2' if val > 0 else f'({var_s}+{-val})^2'
    def fmt_zero_sq(val):
        return f'(0-{val})^2' if val > 0 else f'(0+{-val})^2'
    circles = [((1, 7), (5, 5)), ((9, 7), (11, 3)), ((13, 1), (11, 7)), ((15, 5), (13, 9))]
    odd_vals = [-5, -3, -1, 1, 3, 5]
    while True:
        u = random.choice(odd_vals)
        v = random.choice(odd_vals)
        pair1, pair2 = random.choice(circles)
        pts = set()
        for p, q in [pair1, pair2]:
            for sx in (-1, 1):
                for sy in (-1, 1):
                    pts.add(((u + sx * p) // 2, (v + sy * q) // 2))
                    pts.add(((u + sx * q) // 2, (v + sy * p) // 2))
        pts = [pt for pt in pts if pt[0] != 0 and pt[1] != 0 and abs(pt[0]) <= 9 and abs(pt[1]) <= 9]
        if len(pts) < 3:
            continue
        A, B, C = random.sample(pts, 3)
        xA, yA = A
        xB, yB = B
        xC, yC = C
        if xA == xB or xA == xC or yA == yB or yA == yC:
            continue
        a11 = 2 * (xB - xA)
        a12 = 2 * (yB - yA)
        rhs1 = xB**2 + yB**2 - xA**2 - yA**2
        a21 = 2 * (xC - xA)
        a22 = 2 * (yC - yA)
        rhs2 = xC**2 + yC**2 - xA**2 - yA**2
        if rhs1 % a11 != 0:
            continue
        xD = rhs1 // a11
        if xD != 0 and abs(xD) <= 20:
            break
    ab1, ab2 = xB - xA, yB - yA
    xI = Rational(u, 2)
    yI = Rational(v, 2)
    xI_tex = latex(xI).replace('\\frac', '\\dfrac')
    yI_tex = latex(yI).replace('\\frac', '\\dfrac')
    N_val = pair1[0]**2 + pair1[1]**2
    R_val = sp.sqrt(Rational(N_val, 4))
    R_tex = latex(R_val).replace('\\frac', '\\dfrac')
    noidungcauhoi = f'Trong mặt phẳng tọa độ $Oxy$, cho $\\triangle ABC$ với $A({xA};{yA})$, $B({xB};{yB})$, $C({xC};{yC})$. Xét tính đúng sai của các khẳng định sau:\n'
    wrong_ab = random.choice([p for p in [(-ab1, ab2), (ab1, -ab2), (-ab1, -ab2), (ab2, ab1), (ab1 + 1, ab2)] if p != (ab1, ab2)])
    nb_da_1_d = f'\\True $\\overrightarrow{{AB}}=({ab1};{ab2})$'
    nb_da_1_s = f'$\\overrightarrow{{AB}}=({wrong_ab[0]};{wrong_ab[1]})$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    wrong_xD = random.choice([val for val in [-xD, xD + 1, xD - 1, xD + 2, xD - 2] if val != xD])
    th_da_1_d = f'\\True Tọa độ điểm $D$ thuộc $Ox$ cách đều hai điểm $A, B$ có hoành độ bằng ${xD}$'
    th_da_1_s = f'Tọa độ điểm $D$ thuộc $Ox$ cách đều hai điểm $A, B$ có hoành độ bằng ${wrong_xD}$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    wrong_I = random.choice([p for p in [(-xI, yI), (xI, -yI), (yI, xI), (xI + 1, yI), (xI, yI + 1)] if p != (xI, yI)])
    wxI_tex = latex(wrong_I[0]).replace('\\frac', '\\dfrac')
    wyI_tex = latex(wrong_I[1]).replace('\\frac', '\\dfrac')
    vd_da_1_d = f'\\True $I\\left({xI_tex};{yI_tex}\\right)$ là tọa độ tâm của đường tròn ngoại tiếp tam giác $ABC$'
    vd_da_1_s = f'$I\\left({wxI_tex};{wyI_tex}\\right)$ là tọa độ tâm của đường tròn ngoại tiếp tam giác $ABC$'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    wrong_R_cands = [sp.sqrt(Rational(N_val // 10, 4)), sp.sqrt(N_val), sp.sqrt(Rational(N_val + 4, 4)), sp.sqrt(Rational(N_val - 4, 4))]
    wrong_R = random.choice([r for r in wrong_R_cands if r != R_val])
    wrong_R_tex = latex(wrong_R).replace('\\frac', '\\dfrac')
    vdc_da_1_d = f'\\True Bán kính $R$ của đường tròn ngoại tiếp tam giác $ABC$ bằng ${R_tex}$'
    vdc_da_1_s = f'Bán kính $R$ của đường tròn ngoại tiếp tam giác $ABC$ bằng ${wrong_R_tex}$'
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
    expr_AD = latex(sp.expand((x - xA)**2 + yA**2))
    expr_BD = latex(sp.expand((x - xB)**2 + yB**2))
    lhs_d = latex(a11 * x)
    eq1_lhs = latex(a11 * x + a12 * y)
    eq2_lhs = latex(a21 * x + a22 * y)
    dx_ia = f'{xI_tex}-{xA}' if xA > 0 else f'{xI_tex}+{-xA}'
    dy_ia = f'{yI_tex}-{yA}' if yA > 0 else f'{yI_tex}+{-yA}'
    loigiai_nb_1 = f'{tt_nb}: $\\overrightarrow{{AB}}=({ab1};{ab2})$.'
    loigiai_th_1 = f'{tt_th}: Gọi $D(x;0)\\in Ox \\Rightarrow AD=\\sqrt{{{fmt_sq("x", xA)}+{fmt_zero_sq(yA)}}}=\\sqrt{{{expr_AD}}}$;\\\\ Khi đó $BD=\\sqrt{{{fmt_sq("x", xB)}+{fmt_zero_sq(yB)}}}=\\sqrt{{{expr_BD}}}$.\\\\ Ta có: $AD^2=BD^2 \\Leftrightarrow {expr_AD}={expr_BD} \\Leftrightarrow {lhs_d}={rhs1} \\Leftrightarrow x={xD}$. Vậy $D({xD};0)$.'
    loigiai_vd_1 = f'{tt_vd}: Gọi $I(x;y)$ là tâm đường tròn ngoại tiếp $\\triangle ABC$.\\\\ Ta có: $IA=IB=IC \\Leftrightarrow \\begin{{cases}} IA^2=IB^2 \\\\ IA^2=IC^2 \\end{{cases}} \\Leftrightarrow \\begin{{cases}} {fmt_sq("x", xA)}+{fmt_sq("y", yA)}={fmt_sq("x", xB)}+{fmt_sq("y", yB)} \\\\ {fmt_sq("x", xA)}+{fmt_sq("y", yA)}={fmt_sq("x", xC)}+{fmt_sq("y", yC)} \\end{{cases}}$\\\\ $\\Leftrightarrow \\begin{{cases}} {eq1_lhs}={rhs1} \\\\ {eq2_lhs}={rhs2} \\end{{cases}} \\Leftrightarrow \\begin{{cases}} x={xI_tex} \\\\ y={yI_tex} \\end{{cases}}$ nên $I\\left({xI_tex};{yI_tex}\\right)$.'
    loigiai_vdc_1 = f'{tt_vdc}: Bán kính đường tròn là: $R=IA=\\sqrt{{\\left({dx_ia}\\right)^2+\\left({dy_ia}\\right)^2}}={R_tex}$.'
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

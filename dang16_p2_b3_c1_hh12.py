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


def bt_dang16_p2_b3_c1_hh12(self):
    def f_sub(var, val):
        if val > 0: return f"{var}-{val}"
        elif val < 0: return f"{var}+{-val}"
        return f"{var}"
    def f_num(val):
        return f"({val})" if val < 0 else f"{val}"
    while True:
        xA, yA, zA = [randint(-3, 3) for _ in range(3)]
        xB, yB, zB = [randint(-3, 3) for _ in range(3)]
        xD, yD, zD = [randint(-3, 3) for _ in range(3)]
        xC_prime, yC_prime, zC_prime = [randint(-5, 5) for _ in range(3)]
        vAB = (xB - xA, yB - yA, zB - zA)
        vAD = (xD - xA, yD - yA, zD - zA)
        cross_base = (vAB[1]*vAD[2] - vAB[2]*vAD[1], vAB[2]*vAD[0] - vAB[0]*vAD[2], vAB[0]*vAD[1] - vAB[1]*vAD[0])
        if cross_base == (0, 0, 0): continue
        vAC_prime = (xC_prime - xA, yC_prime - yA, zC_prime - zA)
        vol = cross_base[0]*vAC_prime[0] + cross_base[1]*vAC_prime[1] + cross_base[2]*vAC_prime[2]
        if vol == 0: continue
        break
    vAD_x, vAD_y, vAD_z = xD - xA, yD - yA, zD - zA
    xC, yC, zC = xB + vAD_x, yB + vAD_y, zB + vAD_z
    xB_prime, yB_prime, zB_prime = xC_prime - vAD_x, yC_prime - vAD_y, zC_prime - vAD_z
    xI, yI, zI = Rational(xB_prime + xC, 2), Rational(yB_prime + yC, 2), Rational(zB_prime + zC, 2)
    vCC_prime_x, vCC_prime_y, vCC_prime_z = xC_prime - xC, yC_prime - yC, zC_prime - zC
    xD_prime, yD_prime, zD_prime = xD + vCC_prime_x, yD + vCC_prime_y, zD + vCC_prime_z
    vAC_x, vAC_y, vAC_z = xC - xA, yC - yA, zC - zA
    vB_prime_D_prime_x, vB_prime_D_prime_y, vB_prime_D_prime_z = xD_prime - xB_prime, yD_prime - yB_prime, zD_prime - zB_prime
    u_x = vAC_y * vB_prime_D_prime_z - vAC_z * vB_prime_D_prime_y
    u_y = vAC_z * vB_prime_D_prime_x - vAC_x * vB_prime_D_prime_z
    u_z = vAC_x * vB_prime_D_prime_y - vAC_y * vB_prime_D_prime_x
    noidungcauhoi = f"Trong không gian $Oxyz$, cho hình hộp $ABCD.A'B'C'D'$ có $A({xA};{yA};{zA}), B({xB};{yB};{zB}), D({xD};{yD};{zD})$ và $C'({xC_prime};{yC_prime};{zC_prime})$."
    sai_vAD_y = vAD_y + 1 if vAD_y == 0 else -vAD_y
    nb_da_1_d = f"\\True Tọa độ vectơ $\\overrightarrow{{AD}}$ là $({vAD_x};{vAD_y};{vAD_z})$"
    nb_da_1_s = f"Tọa độ vectơ $\\overrightarrow{{AD}}$ là $({vAD_x};{sai_vAD_y};{vAD_z})$"
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    list_nb_1 = [nb_da_1]
    loigiai_nb_1 = f"Ta có $\\overrightarrow{{AD}} = ({xD}-{f_num(xA)}; {yD}-{f_num(yA)}; {zD}-{f_num(zA)}) = ({vAD_x};{vAD_y};{vAD_z})$."
    list_nb_2 = [loigiai_nb_1]
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    sai_yC = yC + 1 if yC == 0 else -yC
    th_da_1_d = f"\\True Tọa độ điểm $C$ là $({xC};{yC};{zC})$"
    th_da_1_s = f"Tọa độ điểm $C$ là $({xC};{sai_yC};{zC})$"
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    list_th_1 = [th_da_1]
    loigiai_th_1 = f"Gọi tọa độ của điểm $C$ là $(x_C; y_C; z_C)$, ta có $\\overrightarrow{{BC}} = ({f_sub('x_C', xB)}; {f_sub('y_C', yB)}; {f_sub('z_C', zB)})$. Trong hình hộp $ABCD.A'B'C'D'$, ta có $\\overrightarrow{{AD}} = \\overrightarrow{{BC}}$. Suy ra: $\\begin{{cases}} {f_sub('x_C', xB)} = {vAD_x} \\\\ {f_sub('y_C', yB)} = {vAD_y} \\\\ {f_sub('z_C', zB)} = {vAD_z} \\end{{cases}} \\Leftrightarrow \\begin{{cases}} x_C = {xC} \\\\ y_C = {yC} \\\\ z_C = {zC} \\end{{cases}}$. Vậy tọa độ của điểm $C({xC};{yC};{zC})$."
    list_th_2 = [loigiai_th_1]
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    sai_zI = zI + 1 if zI == 0 else zI - 1
    vd_da_1_d = f"\\True Tọa độ trung điểm của $B'C$ là $\\left({latex(xI)};{latex(yI)};{latex(zI)}\\right)$"
    vd_da_1_s = f"Tọa độ trung điểm của $B'C$ là $\\left({latex(xI)};{latex(yI)};{latex(sai_zI)}\\right)$"
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    list_vd_1 = [vd_da_1]
    loigiai_vd_1 = f"Ta có: $\\overrightarrow{{BC}} = ({vAD_x};{vAD_y};{vAD_z})$. Trong hình hộp $ABCD.A'B'C'D'$, ta có $\\overrightarrow{{BC}} = \\overrightarrow{{B'C'}}$. Gọi tọa độ của điểm $B'$ là $(x_{{B'}}; y_{{B'}}; z_{{B'}})$, Suy ra: $\\begin{{cases}} {xC_prime} - x_{{B'}} = {vAD_x} \\\\ {yC_prime} - y_{{B'}} = {vAD_y} \\\\ {zC_prime} - z_{{B'}} = {vAD_z} \\end{{cases}} \\Leftrightarrow \\begin{{cases}} x_{{B'}} = {xB_prime} \\\\ y_{{B'}} = {yB_prime} \\\\ z_{{B'}} = {zB_prime} \\end{{cases}}$. Gọi tọa độ trung điểm $I$ của $B'C$ là $(x_I; y_I; z_I)$. Ta có: $\\begin{{cases}} x_I = \\frac{{{xB_prime} + {xC}}}{{2}} \\\\ y_I = \\frac{{{yB_prime} + {yC}}}{{2}} \\\\ z_I = \\frac{{{zB_prime} + {zC}}}{{2}} \\end{{cases}} \\Leftrightarrow \\begin{{cases}} x_I = {latex(xI)} \\\\ y_I = {latex(yI)} \\\\ z_I = {latex(zI)} \\end{{cases}}$. Vậy tọa độ của điểm $I\\left({latex(xI)};{latex(yI)};{latex(zI)}\\right)$."
    list_vd_2 = [loigiai_vd_1]
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    sai_u_x = u_x + 1 if u_x == 0 else -u_x
    vdc_da_1_d = f"\\True Tọa độ của một vectơ vuông góc với cả hai vectơ $\\overrightarrow{{AC}}$ và $\\overrightarrow{{B'D'}}$ là $({u_x};{u_y};{u_z})$"
    vdc_da_1_s = f"Tọa độ của một vectơ vuông góc với cả hai vectơ $\\overrightarrow{{AC}}$ và $\\overrightarrow{{B'D'}}$ là $({sai_u_x};{u_y};{u_z})$"
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    list_vdc_1 = [vdc_da_1]
    is_true_vdc = "\\True" in vdc_da_1
    test_u_x = u_x if is_true_vdc else sai_u_x
    test_u_y = u_y
    test_u_z = u_z
    dot_AC = test_u_x * vAC_x + test_u_y * vAC_y + test_u_z * vAC_z
    dot_BD = test_u_x * vB_prime_D_prime_x + test_u_y * vB_prime_D_prime_y + test_u_z * vB_prime_D_prime_z
    loigiai_vdc_1_parts = [
        f"Theo câu b) ta có $C({xC};{yC};{zC})$. Tương tự $D'({xD_prime};{yD_prime};{zD_prime}), B'({xB_prime};{yB_prime};{zB_prime})$.",
        f"Suy ra $\\overrightarrow{{AC}} = ({vAC_x};{vAC_y};{vAC_z})$ và $\\overrightarrow{{B'D'}} = ({vB_prime_D_prime_x};{vB_prime_D_prime_y};{vB_prime_D_prime_z})$.",
        f"Xét vectơ $\\vec{{n}} = ({test_u_x};{test_u_y};{test_u_z})$, ta kiểm tra tính vuông góc bằng tích vô hướng:",
        f"$\\vec{{n}} \\cdot \\overrightarrow{{AC}} = {f_num(test_u_x)} \\cdot {f_num(vAC_x)} + {f_num(test_u_y)} \\cdot {f_num(vAC_y)} + {f_num(test_u_z)} \\cdot {f_num(vAC_z)} = {dot_AC}$.",
        f"$\\vec{{n}} \\cdot \\overrightarrow{{B'D'}} = {f_num(test_u_x)} \\cdot {f_num(vB_prime_D_prime_x)} + {f_num(test_u_y)} \\cdot {f_num(vB_prime_D_prime_y)} + {f_num(test_u_z)} \\cdot {f_num(vB_prime_D_prime_z)} = {dot_BD}$."
    ]
    if dot_AC == 0 and dot_BD == 0:
        loigiai_vdc_1_parts.append(f"Vì $\\vec{{n}} \\cdot \\overrightarrow{{AC}} = 0$ và $\\vec{{n}} \\cdot \\overrightarrow{{B'D'}} = 0$ nên vectơ $\\vec{{n}}$ vuông góc với cả hai vectơ $\\overrightarrow{{AC}}$ và $\\overrightarrow{{B'D'}}$.")
    else:
        loigiai_vdc_1_parts.append(f"Vì tích vô hướng không đồng thời bằng $0$ nên vectơ $\\vec{{n}}$ không vuông góc với cả hai vectơ $\\overrightarrow{{AC}}$ và $\\overrightarrow{{B'D'}}$.")
    loigiai_vdc_1 = " \\\\ \n".join(loigiai_vdc_1_parts)
    list_vdc_2 = [loigiai_vdc_1]
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))
    random.shuffle(combined_vdc)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)
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
    list_nb_1 = [nb_da_1]
    list_th_1 = [th_da_1]
    list_vd_1 = [vd_da_1]
    list_vdc_1 = [vdc_da_1]
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
        '\\begin{ex}\n'+
        str(noidungcauhoi)+'\n'
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
        '\\end{ex}\n \\end{minipage}\n\n')
    return content


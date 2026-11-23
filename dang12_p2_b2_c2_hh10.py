
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


def bt_dang12_p2_b2_c2_hh10(self):
    def fmt_a(val_sq):
        val = sp.simplify(sp.sqrt(val_sq))
        if val == 1:
            return 'a'
        if val.is_Integer:
            return '%sa' % val
        c, r = val.as_coeff_Mul()
        if c == 1:
            return 'a%s' % latex(r)
        return '%sa%s' % (latex(c), latex(r))
    while True:
        m = random.randint(1, 5)
        n = random.randint(1, 5)
        if m != n:
            break
    canh_m = 'a' if m == 1 else '%sa' % m
    canh_n = 'a' if n == 1 else '%sa' % n
    dc2_str = 'a^2' if m == 1 else '%sa^2' % (m ** 2)
    if n % 2 == 0:
        p = n // 2
        ce2_str = 'a^2' if p == 1 else '%sa^2' % (p ** 2)
    else:
        ce2_str = '\\left(\\dfrac{a}{2}\\right)^2' if n == 1 else '\\left(\\dfrac{%sa}{2}\\right)^2' % n
    A, B, C, D = random.choice([('A', 'B', 'C', 'D'), ('M', 'N', 'P', 'Q')])
    O = random.choice(['O', 'I'])
    E = random.choice(['E', 'K'])
    noidungcauhoi = 'Cho hình chữ nhật $%s%s%s%s$ tâm $%s$ có cạnh $%s%s = %s, %s%s = %s$. Xét tính đúng sai của các khẳng định sau:' % (A, B, C, D, O, A, B, canh_m, B, C, canh_n)
    nb_v1, nb_v2, nb_kq_d, nb_kq_s = random.choice([(A + B, A + D, A + C, C + A), (B + A, B + C, B + D, D + B), (C + B, C + D, C + A, A + C), (D + A, D + C, D + B, B + D)])
    nb_da_1_d = '\\True $\\overrightarrow{%s} + \\overrightarrow{%s} = \\overrightarrow{%s}$' % (nb_v1, nb_v2, nb_kq_d)
    nb_da_1_s = '$\\overrightarrow{%s} + \\overrightarrow{%s} = \\overrightarrow{%s}$' % (nb_v1, nb_v2, nb_kq_s)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    list_nb_1 = [nb_da_1]
    loigiai_nb_1 = 'Ta có theo quy tắc hình bình hành: $\\overrightarrow{%s} + \\overrightarrow{%s} = \\overrightarrow{%s}$.' % (nb_v1, nb_v2, nb_kq_d)
    list_nb_2 = [loigiai_nb_1]
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    th_s_vp = random.choice([A + C, B + D, A + B])
    th_da_1_d = '\\True $\\overrightarrow{%s%s} + \\overrightarrow{%s%s} + \\overrightarrow{%s%s} + \\overrightarrow{%s%s} = \\overrightarrow{0}$' % (O, A, O, B, O, C, O, D)
    th_da_1_s = '$\\overrightarrow{%s%s} + \\overrightarrow{%s%s} + \\overrightarrow{%s%s} + \\overrightarrow{%s%s} = \\overrightarrow{%s}$' % (O, A, O, B, O, C, O, D, th_s_vp)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    list_th_1 = [th_da_1]
    loigiai_th_1 = 'Ta có theo tính chất $%s$ là tâm hình chữ nhật thì $%s$ là trung điểm các đoạn $%s%s, %s%s$ nên: $\\overrightarrow{%s%s} + \\overrightarrow{%s%s} + \\overrightarrow{%s%s} + \\overrightarrow{%s%s} = \\left(\\overrightarrow{%s%s} + \\overrightarrow{%s%s}\\right) + \\left(\\overrightarrow{%s%s} + \\overrightarrow{%s%s}\\right) = \\overrightarrow{0}$.' % (O, O, A, C, B, D, O, A, O, B, O, C, O, D, O, A, O, C, O, D, O, B)
    list_th_2 = [loigiai_th_1]
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    vd_v1, vd_v2, vd_kq = random.choice([(D + A, D + C, D + B), (B + A, B + C, B + D), (A + B, A + D, A + C), (C + B, C + D, C + A)])
    vd_sq = m ** 2 + n ** 2
    vd_val_d = fmt_a(vd_sq)
    vd_s_candidates = [fmt_a(x) for x in [abs(m ** 2 - n ** 2) if abs(m ** 2 - n ** 2) > 0 else 2, vd_sq + 2, (m + n) ** 2] if fmt_a(x) != vd_val_d]
    vd_val_s = random.choice(vd_s_candidates)
    vd_da_1_d = '\\True $\\left|\\overrightarrow{%s} + \\overrightarrow{%s}\\right| = %s$' % (vd_v1, vd_v2, vd_val_d)
    vd_da_1_s = '$\\left|\\overrightarrow{%s} + \\overrightarrow{%s}\\right| = %s$' % (vd_v1, vd_v2, vd_val_s)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    list_vd_1 = [vd_da_1]
    loigiai_vd_1 = 'Theo quy tắc hình bình hành ta có: $\\left|\\overrightarrow{%s} + \\overrightarrow{%s}\\right| = \\left|\\overrightarrow{%s}\\right| = %s = %s$.' % (vd_v1, vd_v2, vd_kq, vd_kq, vd_val_d)
    list_vd_2 = [loigiai_vd_1]
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    vdc_sq = 4 * m ** 2 + n ** 2
    vdc_val_d = fmt_a(vdc_sq)
    vdc_s_candidates = [fmt_a(x) for x in [m ** 2 + n ** 2, m ** 2 + 4 * n ** 2, vdc_sq + 2] if fmt_a(x) != vdc_val_d]
    vdc_val_s = random.choice(vdc_s_candidates)
    vdc_da_1_d = '\\True $\\left|\\overrightarrow{%s%s} + \\overrightarrow{%s%s}\\right| = %s$' % (A, B, D, B, vdc_val_d)
    vdc_da_1_s = '$\\left|\\overrightarrow{%s%s} + \\overrightarrow{%s%s}\\right| = %s$' % (A, B, D, B, vdc_val_s)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    list_vdc_1 = [vdc_da_1]
    loigiai_vdc_1 = 'Gọi $%s$ là trung điểm của $%s%s$ ta có: $\\left|\\overrightarrow{%s%s} + \\overrightarrow{%s%s}\\right| = \\left|\\overrightarrow{%s%s} + \\overrightarrow{%s%s}\\right| = 2\\left|\\overrightarrow{%s%s}\\right| = 2\\sqrt{%s%s^2 + %s%s^2} = 2\\sqrt{%s + %s} = %s$.' % (E, C, B, A, B, D, B, D, B, D, C, D, E, D, C, C, E, dc2_str, ce2_str, vdc_val_d)
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
        '\\end{ex}\n \\end{minipage}\n\n')
    return content


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


def bt_dang13_p2_b2_c2_hh10(self):
    k = random.randint(1, 6)
    ang = random.choice([60, 120])
    canh = 'a' if k == 1 else '%da' % k
    A, B, C, D, H = random.choice([('A', 'B', 'C', 'D', 'H'), ('A', 'B', 'C', 'D', 'O'), ('M', 'N', 'P', 'Q', 'O')])
    if ang == 60:
        cx, cy, dx, dy, hx, hy = 1.5, 2.6, -1.5, 2.6, 0.75, 1.3
        ac_str = canh
        ah_str = ('a' if k == 2 else '%da' % (k // 2)) if k % 2 == 0 else ('\\dfrac{a}{2}' if k == 1 else '\\dfrac{%da}{2}' % k)
        sum_str = ('%da' % (3 * k // 2)) if k % 2 == 0 else '\\dfrac{%da}{2}' % (3 * k)
        s_cands = ['a\\sqrt{13}' if k == 1 else '%da\\sqrt{13}' % k, 'a\\sqrt{3}' if k == 1 else '%da\\sqrt{3}' % k, '\\dfrac{3a\\sqrt{3}}{2}' if k == 1 else '\\dfrac{%da\\sqrt{3}}{2}' % (3 * k)]
        giai_tamgiac = 'nên $\\triangle %s%s%s$ đều, suy ra $%s%s = %s$ và $%s%s = %s$' % (A, B, C, A, C, ac_str, A, H, ah_str)
    else:
        cx, cy, dx, dy, hx, hy = 4.5, 2.6, 1.5, 2.6, 2.25, 1.3
        ac_str = 'a\\sqrt{3}' if k == 1 else '%da\\sqrt{3}' % k
        ah_str = ('a\\sqrt{3}' if k == 2 else '%da\\sqrt{3}' % (k // 2)) if k % 2 == 0 else ('\\dfrac{a\\sqrt{3}}{2}' if k == 1 else '\\dfrac{%da\\sqrt{3}}{2}' % k)
        sum_str = ('%da\\sqrt{3}' % (3 * k // 2)) if k % 2 == 0 else '\\dfrac{%da\\sqrt{3}}{2}' % (3 * k)
        s_cands = ['a\\sqrt{13}' if k == 1 else '%da\\sqrt{13}' % k, '\\dfrac{3a}{2}' if k == 1 else '\\dfrac{%da}{2}' % (3 * k), '2a' if k == 1 else '%da' % (2 * k)]
        giai_tamgiac = 'nên $\\widehat{%s%s%s} = 60^\\circ$, suy ra $\\triangle %s%s%s$ đều cạnh $%s$, do đó $%s%s = %s$ và $%s%s = %s$' % (B, A, D, A, B, D, canh, A, C, ac_str, A, H, ah_str)
    hinh_thoi = ('\\begin{center}\n'
    '\\begin{tikzpicture}[line width=1pt]\n'
    '\\coordinate (A) at (0,0);\n'
    '\\coordinate (B) at (3,0);\n'
    '\\coordinate (C) at (%.2f,%.2f);\n'
    '\\coordinate (D) at (%.2f,%.2f);\n'
    '\\coordinate (H) at (%.2f,%.2f);\n'
    '\\draw (A) -- (B) -- (C) -- (D) -- cycle;\n'
    '\\draw (A) -- (C) (B) -- (D);\n'
    '\\fill (A) circle (1.5pt) node[below left] {$%s$};\n'
    '\\fill (B) circle (1.5pt) node[below right] {$%s$};\n'
    '\\fill (C) circle (1.5pt) node[above right] {$%s$};\n'
    '\\fill (D) circle (1.5pt) node[above left] {$%s$};\n'
    '\\fill (H) circle (1.5pt) node[below] {$%s$};\n'
    '\\end{tikzpicture}\n'
    '\\end{center}' % (cx, cy, dx, dy, hx, hy, A, B, C, D, H))
    noidungcauhoi = 'Cho hình thoi $%s%s%s%s$ tâm $%s$ có cạnh bằng $%s$ và $\\widehat{%s%s%s} = %d^\\circ$. Xét tính đúng sai của các khẳng định sau:' % (A, B, C, D, H, canh, A, B, C, ang)
    nb_s_vec = random.choice([C + A, B + D, D + B])
    nb_da_1_d = '\\True $\\overrightarrow{%s%s} + \\overrightarrow{%s%s} = \\overrightarrow{%s%s}$' % (A, B, A, D, A, C)
    nb_da_1_s = '$\\overrightarrow{%s%s} + \\overrightarrow{%s%s} = \\overrightarrow{%s}$' % (A, B, A, D, nb_s_vec)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    list_nb_1 = [nb_da_1]
    loigiai_nb_1 = hinh_thoi + '\nTa có $\\overrightarrow{%s%s} + \\overrightarrow{%s%s} = \\overrightarrow{%s%s}$ theo quy tắc hình bình hành.' % (A, B, A, D, A, C)
    list_nb_2 = [loigiai_nb_1]
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    th_s_vec = random.choice([B + D, A + C, C + A])
    th_da_1_d = '\\True $\\overrightarrow{%s%s} - \\overrightarrow{%s%s} = \\overrightarrow{%s%s}$' % (A, B, A, D, D, B)
    th_da_1_s = '$\\overrightarrow{%s%s} - \\overrightarrow{%s%s} = \\overrightarrow{%s}$' % (A, B, A, D, th_s_vec)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    list_th_1 = [th_da_1]
    loigiai_th_1 = 'Ta có $\\overrightarrow{%s%s} - \\overrightarrow{%s%s} = \\overrightarrow{%s%s}$ theo quy tắc trừ.' % (A, B, A, D, D, B)
    list_th_2 = [loigiai_th_1]
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    vd_s_vec = random.choice([A + D, A + B, B + C])
    vd_da_1_d = '\\True $\\overrightarrow{%s%s} + \\overrightarrow{%s%s} = \\overrightarrow{%s%s}$' % (H, A, H, B, D, A)
    vd_da_1_s = '$\\overrightarrow{%s%s} + \\overrightarrow{%s%s} = \\overrightarrow{%s}$' % (H, A, H, B, vd_s_vec)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    list_vd_1 = [vd_da_1]
    loigiai_vd_1 = 'Ta có $%s$ là trung điểm của $%s%s$ nên $\\overrightarrow{%s%s} = \\overrightarrow{%s%s}$, suy ra $\\overrightarrow{%s%s} + \\overrightarrow{%s%s} = \\overrightarrow{%s%s} + \\overrightarrow{%s%s} = \\overrightarrow{%s%s}$.' % (H, B, D, H, B, D, H, H, A, H, B, D, H, H, A, D, A)
    list_vd_2 = [loigiai_vd_1]
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    vdc_s_val = random.choice(s_cands)
    vdc_da_1_d = '\\True $\\left|\\overrightarrow{%s%s} + \\overrightarrow{%s%s}\\right| = %s$' % (A, C, A, H, sum_str)
    vdc_da_1_s = '$\\left|\\overrightarrow{%s%s} + \\overrightarrow{%s%s}\\right| = %s$' % (A, C, A, H, vdc_s_val)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    list_vdc_1 = [vdc_da_1]
    loigiai_vdc_1 = 'Vì hình thoi $%s%s%s%s$ có cạnh bằng $%s$ và $\\widehat{%s%s%s} = %d^\\circ$ %s. Do $%s$ là trung điểm $%s%s$ nên $\\overrightarrow{%s%s}$ và $\\overrightarrow{%s%s}$ cùng hướng, suy ra $\\left|\\overrightarrow{%s%s} + \\overrightarrow{%s%s}\\right| = %s%s + %s%s = %s + %s = %s$.' % (A, B, C, D, canh, A, B, C, ang, giai_tamgiac, H, A, C, A, C, A, H, A, C, A, H, A, C, A, H, ac_str, ah_str, sum_str)
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

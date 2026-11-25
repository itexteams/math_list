
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


def bt_dang3_p2_b4_c2_hh10(self):
    def format_vec(u, v):
        s1 = '\\vec{i}' if u == 1 else ('-\\vec{i}' if u == -1 else f'{u}\\vec{{i}}')
        s2 = '+\\vec{j}' if v == 1 else ('-\\vec{j}' if v == -1 else (f'+{v}\\vec{{j}}' if v > 0 else f'{v}\\vec{{j}}'))
        return (s1 + s2).replace('+-', '-').replace('--', '+')
    vals = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]
    while True:
        a1, a2, b1, b2 = random.choice(vals), random.choice(vals), random.choice(vals), random.choice(vals)
        if (a1, a2) != (b1, b2) and (a1, a2) != (-b1, -b2):
            break
    m, n = random.sample([2, 3, 4], 2)
    k = random.choice([2, 3, 4])
    vec_a = format_vec(a1, a2)
    vec_b = format_vec(b1, b2)
    ma1, ma2 = m * a1, m * a2
    nb1, nb2 = n * b1, n * b2
    c1, c2 = ma1 + nb1, ma2 + nb2
    kb1, kb2 = -k * b1, -k * b2
    d1, d2 = a1 + kb1, a2 + kb2
    noidungcauhoi = f'Cho $\\vec{{a}}={vec_a}$, $\\vec{{b}}={vec_b}$. Xét tính đúng sai của các khẳng định sau:\n'
    wrong_a = random.choice([p for p in [(a1, -a2), (-a1, a2), (a2, a1), (a1 + 1, a2), (a1 - 1, a2)] if p != (a1, a2)])
    nb_da_1_d = f'\\True $\\vec{{a}}=({a1};{a2})$'
    nb_da_1_s = f'$\\vec{{a}}=({wrong_a[0]};{wrong_a[1]})$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    wrong_b = random.choice([p for p in [(-b1, -b2), (-b1, b2), (b1, -b2), (b2, b1), (b1 + 1, b2)] if p != (b1, b2)])
    th_da_1_d = f'\\True $\\vec{{b}}=({b1};{b2})$'
    th_da_1_s = f'$\\vec{{b}}=({wrong_b[0]};{wrong_b[1]})$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    wrong_c = random.choice([p for p in [(c1 + 1, c2), (c1 - 1, c2), (c1, c2 + 1), (c1, c2 - 1), (ma1 - nb1, ma2 - nb2)] if p != (c1, c2)])
    vd_da_1_d = f'\\True ${m}\\vec{{a}}+{n}\\vec{{b}}=({c1};{c2})$'
    vd_da_1_s = f'${m}\\vec{{a}}+{n}\\vec{{b}}=({wrong_c[0]};{wrong_c[1]})$'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    wrong_d = random.choice([p for p in [(d1 + 1, d2), (d1 - 1, d2), (d1, d2 + 1), (d1, d2 - 1), (a1 + k * b1, a2 + k * b2)] if p != (d1, d2)])
    vdc_da_1_d = f'\\True $\\vec{{a}}-{k}\\vec{{b}}=({d1};{d2})$'
    vdc_da_1_s = f'$\\vec{{a}}-{k}\\vec{{b}}=({wrong_d[0]};{wrong_d[1]})$'
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
    loigiai_nb_1 = f'{tt_nb}. Vì $\\vec{{a}}={vec_a}$ nên $\\vec{{a}}=({a1};{a2})$.'
    loigiai_th_1 = f'{tt_th}. Vì $\\vec{{b}}={vec_b}$ nên $\\vec{{b}}=({b1};{b2})$.'
    loigiai_vd_1 = f'{tt_vd}. Ta có $\\begin{{cases}}{m}\\vec{{a}}=({ma1};{ma2}) \\\\ {n}\\vec{{b}}=({nb1};{nb2})\\end{{cases}} \\Rightarrow {m}\\vec{{a}}+{n}\\vec{{b}}=({c1};{c2})$.'
    loigiai_vdc_1 = f'{tt_vdc}. Ta có $-{k}\\vec{{b}}=({kb1};{kb2}) \\Rightarrow \\vec{{a}}-{k}\\vec{{b}}=({d1};{d2})$.'
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

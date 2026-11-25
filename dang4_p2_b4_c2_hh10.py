
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


def bt_dang4_p2_b4_c2_hh10(self):
    def fmt_mul(val):
        return f'({val})' if val < 0 else f'{val}'
    def fmt_lc(m_val, n_val):
        s1 = '\\vec{b}' if m_val == 1 else ('-\\vec{b}' if m_val == -1 else f'{latex(m_val)}\\vec{{b}}')
        s2 = '+\\vec{c}' if n_val == 1 else ('-\\vec{c}' if n_val == -1 else (f'+{latex(n_val)}\\vec{{c}}' if n_val > 0 else f'{latex(n_val)}\\vec{{c}}'))
        return (s1 + s2).replace('\\frac', '\\dfrac').replace('+-', '-').replace('--', '+')
    while True:
        e1, e2 = random.choice([-3, -2, -1, 1, 2, 3]), random.choice([-3, -2, -1, 1, 2, 3])
        ke = random.choice([2, 3])
        a1, a2 = ke * e1, ke * e2
        kf = random.choice([-4, -3, -2])
        b1 = random.choice([-abs(kf), abs(kf)])
        b2 = random.choice([v for v in [-3, -2, -1, 1, 2, 3] if v % abs(kf) != 0])
        c1, c2 = 0, random.choice([-2, -1, 1, 2])
        m = Rational(a1, b1)
        n = Rational(a2 - m * b2, c2)
        if n != 0 and m.q <= 4 and n.q <= 4:
            break
    p = random.choice([2, 3])
    r = random.choice([2, 3, 4])
    pa1, pa2 = p * a1, p * a2
    rc1, rc2 = -r * c1, -r * c2
    d1, d2 = pa1 - b1 + rc1, pa2 - b2 + rc2
    f1 = Rational(b1, kf)
    f2 = Rational(b2, kf)
    f1_tex = latex(f1).replace('\\frac', '\\dfrac')
    f2_tex = latex(f2).replace('\\frac', '\\dfrac')
    m_tex = latex(m).replace('\\frac', '\\dfrac')
    n_tex = latex(n).replace('\\frac', '\\dfrac')
    lc_true = fmt_lc(m, n)
    wrong_mn = random.choice([q for q in [(m, -n), (-m, n), (m + 1, n), (m - 1, n), (m, n + 1), (m, n - 1)] if q != (m, n) and q[0] != 0 and q[1] != 0])
    lc_false = fmt_lc(wrong_mn[0], wrong_mn[1])
    noidungcauhoi = f'Trong mặt phẳng tọa độ $Oxy$, cho các vectơ $\\vec{{a}}=({a1};{a2})$, $\\vec{{b}}=({b1};{b2})$ và $\\vec{{c}}=({c1};{c2})$. Xét tính đúng sai của các khẳng định sau:\n'
    wrong_d = random.choice([(d1 + 1, d2), (d1 - 1, d2), (d1, d2 + 1), (d1, d2 - 1)])
    nb_da_1_d = f'\\True ${p}\\vec{{a}}-\\vec{{b}}-{r}\\vec{{c}}=({d1};{d2})$'
    nb_da_1_s = f'${p}\\vec{{a}}-\\vec{{b}}-{r}\\vec{{c}}=({wrong_d[0]};{wrong_d[1]})$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    th_da_1_d = f'\\True Vectơ $\\vec{{e}}=({e1};{e2})$ cùng phương, cùng hướng với vectơ $\\vec{{a}}$'
    th_da_1_s = f'Vectơ $\\vec{{e}}=({e1};{e2})$ cùng phương, ngược hướng với vectơ $\\vec{{a}}$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    vd_da_1_d = f'\\True Vectơ $\\vec{{f}}=\\left({f1_tex};{f2_tex}\\right)$ cùng phương, ngược hướng với vectơ $\\vec{{b}}$'
    vd_da_1_s = f'Vectơ $\\vec{{f}}=\\left({f1_tex};{f2_tex}\\right)$ cùng phương, cùng hướng với vectơ $\\vec{{b}}$'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vdc_da_1_d = f'\\True $\\vec{{a}}={lc_true}$'
    vdc_da_1_s = f'$\\vec{{a}}={lc_false}$'
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
    loigiai_nb_1 = f'{tt_nb}: Ta có: $\\begin{{cases}}{p}\\vec{{a}}=({pa1};{pa2}) \\\\ -\\vec{{b}}=({-b1};{-b2}) \\\\ -{r}\\vec{{c}}=({rc1};{rc2})\\end{{cases}} \\Rightarrow \\vec{{d}}={p}\\vec{{a}}-\\vec{{b}}-{r}\\vec{{c}}=({d1};{d2})$.'
    loigiai_th_1 = f'{tt_th}: Ta có $\\vec{{a}}=({a1};{a2})={ke}\\vec{{e}}$ nên $\\vec{{a}},\\vec{{e}}$ là hai vectơ cùng phương với nhau, hơn nữa chúng cùng hướng với nhau vì $\\vec{{a}}=k\\vec{{e}}, k={ke}>0$.'
    loigiai_vd_1 = f'{tt_vd}: Tương tự: $\\vec{{b}}=({b1};{b2})={kf}\\vec{{f}}$, tức là $\\vec{{b}}=k\\vec{{f}}, k={kf}<0$ nên $\\vec{{b}}$ và $\\vec{{f}}$ là hai vectơ cùng phương, ngược hướng với nhau.'
    loigiai_vdc_1 = f'{tt_vdc}: Gọi $m,n$ là các số thỏa mãn $\\vec{{a}}=m\\vec{{b}}+n\\vec{{c}}$ ($\\vec{{b}},\\vec{{c}}$ không cùng phương).\\\\ Khi đó: $\\begin{{cases}}{a1}=m\\cdot {fmt_mul(b1)}+n\\cdot {fmt_mul(c1)} \\\\ {a2}=m\\cdot {fmt_mul(b2)}+n\\cdot {fmt_mul(c2)}\\end{{cases}} \\Leftrightarrow \\begin{{cases}}m={m_tex} \\\\ n={n_tex}\\end{{cases}}$. Vậy $\\vec{{a}}={lc_true}$.'
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

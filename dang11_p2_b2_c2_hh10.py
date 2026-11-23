
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


def bt_dang11_p2_b2_c2_hh10(self):
    f1 = random.randint(3, 9)
    f2 = random.randint(2, f1 - 1)
    alpha = random.choice([60, 120])
    beta = 180 - alpha
    r1 = 3.5
    r2 = 2.5
    bx = round(r2 * math.cos(math.radians(alpha)), 2)
    by = round(r2 * math.sin(math.radians(alpha)), 2)
    dx = round(r1 + bx, 2)
    dy = by
    ang_de = alpha // 2
    ang_lg = 20 if alpha == 120 else 45
    hinh_de = ('\\begin{center}\n'
    '\\begin{tikzpicture}[line width=1pt, >=stealth]\n'
    '\\coordinate (A) at (0,0);\n'
    '\\coordinate (C) at (%.2f,0);\n'
    '\\coordinate (B) at (%.2f,%.2f);\n'
    '\\draw[->] (A) -- (C) node[midway, below] {$\\overrightarrow{F}_1$};\n'
    '\\draw[->] (A) -- (B) node[midway, left] {$\\overrightarrow{F}_2$};\n'
    '\\draw (0.55,0) arc (0:%d:0.55);\n'
    '\\draw (0.65,0) arc (0:%d:0.65);\n'
    '\\node at (%d:1.0) {$%d^\\circ$};\n'
    '\\fill (A) circle (1.5pt);\n'
    '\\end{tikzpicture}\n'
    '\\end{center}' % (r1, bx, by, alpha, alpha, ang_de, alpha))
    hinh_lg = ('\\begin{center}\n'
    '\\begin{tikzpicture}[line width=1pt, >=stealth]\n'
    '\\coordinate (A) at (0,0);\n'
    '\\coordinate (C) at (%.2f,0);\n'
    '\\coordinate (B) at (%.2f,%.2f);\n'
    '\\coordinate (D) at (%.2f,%.2f);\n'
    '\\draw[->] (A) -- (C) node[midway, below] {$\\overrightarrow{F}_1$};\n'
    '\\draw[->] (A) -- (B) node[midway, left] {$\\overrightarrow{F}_2$};\n'
    '\\draw[->] (A) -- (D);\n'
    '\\draw[dashed] (B) -- (D) -- (C);\n'
    '\\draw (0.55,0) arc (0:%d:0.55);\n'
    '\\draw (0.65,0) arc (0:%d:0.65);\n'
    '\\node at (%d:1.15) {$%d^\\circ$};\n'
    '\\fill (A) circle (1.5pt) node[below] {$A$};\n'
    '\\fill (B) circle (1.5pt) node[left] {$B$};\n'
    '\\fill (C) circle (1.5pt) node[below right] {$C$};\n'
    '\\fill (D) circle (1.5pt) node[above right] {$D$};\n'
    '\\end{tikzpicture}\n'
    '\\end{center}' % (r1, bx, by, dx, dy, alpha, alpha, ang_lg, alpha))
    noidungcauhoi = 'Hình vẽ dưới biểu diễn hai lực $\\overrightarrow{F}_1, \\overrightarrow{F}_2$ cùng tác động lên một vật, cho $\\left|\\overrightarrow{F}_1\\right| = %d\\text{ N}, \\left|\\overrightarrow{F}_2\\right| = %d\\text{ N}$. Xét tính đúng sai của các khẳng định sau:\n' % (f1, f2) + hinh_de
    nb_s_txt = random.choice(['cùng hướng', 'ngược hướng', 'cùng phương'])
    nb_da_1_d = '\\True $\\overrightarrow{F}_1$ không cùng hướng với $\\overrightarrow{F}_2$'
    nb_da_1_s = '$\\overrightarrow{F}_1$ %s với $\\overrightarrow{F}_2$' % nb_s_txt
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    list_nb_1 = [nb_da_1]
    loigiai_nb_1 = 'Vì góc giữa hai vectơ là $%d^\\circ$ nên $\\overrightarrow{F}_1$ không cùng phương (không cùng hướng, không ngược hướng) với $\\overrightarrow{F}_2$.' % alpha
    list_nb_2 = [loigiai_nb_1]
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    th_da_1_d = '\\True $\\left|\\overrightarrow{F}_1 + \\overrightarrow{F}_2\\right| \\neq \\left|\\overrightarrow{F}_1\\right| + \\left|\\overrightarrow{F}_2\\right|$'
    th_da_1_s = '$\\left|\\overrightarrow{F}_1 + \\overrightarrow{F}_2\\right| = \\left|\\overrightarrow{F}_1\\right| + \\left|\\overrightarrow{F}_2\\right|$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    list_th_1 = [th_da_1]
    loigiai_th_1 = 'Vì $\\overrightarrow{F}_1$ không cùng hướng với $\\overrightarrow{F}_2$ nên $\\left|\\overrightarrow{F}_1 + \\overrightarrow{F}_2\\right| \\neq \\left|\\overrightarrow{F}_1\\right| + \\left|\\overrightarrow{F}_2\\right|$.'
    list_th_2 = [loigiai_th_1]
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    vd_da_1_d = '\\True $\\left|\\overrightarrow{F}_1 - \\overrightarrow{F}_2\\right| \\neq \\left|\\overrightarrow{F}_1\\right| - \\left|\\overrightarrow{F}_2\\right|$'
    vd_da_1_s = '$\\left|\\overrightarrow{F}_1 - \\overrightarrow{F}_2\\right| = \\left|\\overrightarrow{F}_1\\right| - \\left|\\overrightarrow{F}_2\\right|$'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    list_vd_1 = [vd_da_1]
    loigiai_vd_1 = 'Vì $\\overrightarrow{F}_1$ không cùng hướng với $\\overrightarrow{F}_2$ nên $\\left|\\overrightarrow{F}_1 - \\overrightarrow{F}_2\\right| \\neq \\left|\\overrightarrow{F}_1\\right| - \\left|\\overrightarrow{F}_2\\right|$.'
    list_vd_2 = [loigiai_vd_1]
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    ad_sq = f2 ** 2 + f1 ** 2 - f1 * f2 if beta == 60 else f2 ** 2 + f1 ** 2 + f1 * f2
    ad_sq_s = f2 ** 2 + f1 ** 2 + f1 * f2 if beta == 60 else f2 ** 2 + f1 ** 2 - f1 * f2
    ad_val_d = latex(sp.simplify(sp.sqrt(ad_sq)))
    ad_val_s = latex(sp.simplify(sp.sqrt(ad_sq_s)))
    vdc_da_1_d = '\\True $\\left|\\overrightarrow{F}_1 + \\overrightarrow{F}_2\\right| = %s$' % ad_val_d
    vdc_da_1_s = '$\\left|\\overrightarrow{F}_1 + \\overrightarrow{F}_2\\right| = %s$' % ad_val_s
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    list_vdc_1 = [vdc_da_1]
    loigiai_vdc_1 = 'Dựng hình bình hành $ABDC$ với hai cạnh là hai vectơ $\\overrightarrow{F}_1, \\overrightarrow{F}_2$ như hình vẽ:\n' + hinh_lg + '\nTa có: $\\overrightarrow{F}_1 + \\overrightarrow{F}_2 = \\overrightarrow{AC} + \\overrightarrow{AB} = \\overrightarrow{AD} \\Rightarrow \\left|\\overrightarrow{F}_1 + \\overrightarrow{F}_2\\right| = \\left|\\overrightarrow{AD}\\right| = AD$. Xét $\\triangle ABD$ ta có: $BD = AC = \\left|\\overrightarrow{F}_1\\right| = %d$, $AB = \\left|\\overrightarrow{F}_2\\right| = %d$ và $\\widehat{ABD} = 180^\\circ - \\widehat{BAC} = 180^\\circ - %d^\\circ = %d^\\circ$. Theo định lí côsin ta có: $AD^2 = AB^2 + BD^2 - 2 \\cdot AB \\cdot BD \\cdot \\cos \\widehat{ABD} \\Leftrightarrow AD^2 = %d^2 + %d^2 - 2 \\cdot %d \\cdot %d \\cdot \\cos %d^\\circ \\Leftrightarrow AD^2 = %d \\Leftrightarrow AD = %s \\Rightarrow \\left|\\overrightarrow{F}_1 + \\overrightarrow{F}_2\\right| = %s$.' % (f1, f2, alpha, beta, f2, f1, f2, f1, beta, ad_sq, ad_val_d, ad_val_d)
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

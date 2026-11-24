
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


def bt_dang6_p2_b3_c2_hh10(self):
    def clean_sign(s):
        return s.replace('- -', '+ ').replace('--', '+').replace('+ -', '- ').replace('+-', '-')
    tri_sets = [('A', 'B', 'C'), ('D', 'E', 'F'), ('P', 'Q', 'R'), ('H', 'K', 'I')]
    p1, p2, p3 = random.choice(tri_sets)
    tri_name = p1 + p2 + p3
    used = set([p1, p2, p3])
    m_pt = random.choice([c for c in ['M', 'I', 'K', 'E'] if c not in used])
    used.add(m_pt)
    g_pt = random.choice([c for c in ['G', 'T'] if c not in used])
    used.add(g_pt)
    n_pt = random.choice([c for c in ['N', 'O', 'S', 'X'] if c not in used])
    s_AM, s_BC = p1 + m_pt, p2 + p3
    s_MB, s_MC = m_pt + p2, m_pt + p3
    s_GA, s_AG, s_GM = g_pt + p1, p1 + g_pt, g_pt + m_pt
    s_GB, s_GC = g_pt + p2, g_pt + p3
    s_NA, s_NB, s_NC = n_pt + p1, n_pt + p2, n_pt + p3
    s_NG, s_GN = n_pt + g_pt, g_pt + n_pt
    s_AB, s_AC = p1 + p2, p1 + p3
    noidungcauhoi = '''Cho tam giác $%s$ với trung tuyến $%s$ và trọng tâm $%s$. Xét tính đúng sai của các khẳng định sau:''' % (tri_name, s_AM, g_pt)
    tikz_hinh = '''\\begin{tikzpicture}[line width=1pt, scale=0.8]
    \\coordinate (B) at (0,0);
    \\coordinate (C) at (4.8,0);
    \\coordinate (A) at (1.2,2.7);
    \\coordinate (M) at (2.4,0);
    \\coordinate (G) at (2,0.9);
    \\draw (A)--(B)--(C)--cycle;
    \\draw (A)--(M);
    \\fill (A) circle (1.5pt) node[above] {$%s$};
    \\fill (B) circle (1.5pt) node[below left] {$%s$};
    \\fill (C) circle (1.5pt) node[below right] {$%s$};
    \\fill (M) circle (1.5pt) node[below] {$%s$};
    \\fill (G) circle (1.5pt) node[above right] {$%s$};
    \\end{tikzpicture}''' % (p1, p2, p3, m_pt, g_pt)
    nb_da_1_d = '\\True Tổng $\\overrightarrow{%s}+\\overrightarrow{%s}=\\vec{0}$' % (s_MB, s_MC)
    nb_da_1_s = random.choice(['Tổng $\\overrightarrow{%s}-\\overrightarrow{%s}=\\vec{0}$' % (s_MB, s_MC), 'Tổng $\\overrightarrow{%s}+\\overrightarrow{%s}=\\overrightarrow{%s}$' % (s_MB, s_MC, s_BC)])
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    list_nb_1 = [nb_da_1]
    loigiai_nb_1 = clean_sign('''Vì $%s$ là trung điểm của $%s$ nên $\\overrightarrow{%s}+\\overrightarrow{%s}=\\vec{0}$.''' % (m_pt, s_BC, s_MB, s_MC)) + ' \\\\\n' + tikz_hinh
    list_nb_2 = [loigiai_nb_1]
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    th_type = random.choice([1, 2, 3])
    if th_type == 1:
        th_da_1_d = '\\True Biểu diễn $\\overrightarrow{%s}=-\\dfrac{2}{3}\\overrightarrow{%s}$' % (s_GA, s_AM)
        th_da_1_s = 'Biểu diễn $\\overrightarrow{%s}=\\dfrac{2}{3}\\overrightarrow{%s}$' % (s_GA, s_AM)
        loigiai_th_1 = clean_sign('''Ta có $%s=\\dfrac{2}{3}%s$. Mặt khác $\\overrightarrow{%s}$ và $\\overrightarrow{%s}$ ngược hướng nên $\\overrightarrow{%s}=-\\dfrac{2}{3}\\overrightarrow{%s}$.''' % (s_GA, s_AM, s_GA, s_AM, s_GA, s_AM))
    elif th_type == 2:
        th_da_1_d = '\\True Biểu diễn $\\overrightarrow{%s}=\\dfrac{2}{3}\\overrightarrow{%s}$' % (s_AG, s_AM)
        th_da_1_s = 'Biểu diễn $\\overrightarrow{%s}=-\\dfrac{2}{3}\\overrightarrow{%s}$' % (s_AG, s_AM)
        loigiai_th_1 = clean_sign('''Ta có $%s=\\dfrac{2}{3}%s$. Mặt khác $\\overrightarrow{%s}$ và $\\overrightarrow{%s}$ cùng hướng nên $\\overrightarrow{%s}=\\dfrac{2}{3}\\overrightarrow{%s}$.''' % (s_AG, s_AM, s_AG, s_AM, s_AG, s_AM))
    else:
        th_da_1_d = '\\True Biểu diễn $\\overrightarrow{%s}=\\dfrac{1}{3}\\overrightarrow{%s}$' % (s_GM, s_AM)
        th_da_1_s = 'Biểu diễn $\\overrightarrow{%s}=-\\dfrac{1}{3}\\overrightarrow{%s}$' % (s_GM, s_AM)
        loigiai_th_1 = clean_sign('''Ta có $%s=\\dfrac{1}{3}%s$. Mặt khác $\\overrightarrow{%s}$ và $\\overrightarrow{%s}$ cùng hướng nên $\\overrightarrow{%s}=\\dfrac{1}{3}\\overrightarrow{%s}$.''' % (s_GM, s_AM, s_GM, s_AM, s_GM, s_AM))
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    list_th_1 = [th_da_1]
    list_th_2 = [loigiai_th_1]
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    vd_da_1_d = '\\True Với mọi điểm $%s$ thì $\\overrightarrow{%s}+\\overrightarrow{%s}+\\overrightarrow{%s}=3\\overrightarrow{%s}$' % (n_pt, s_NA, s_NB, s_NC, s_NG)
    vd_da_1_s = random.choice(['Với mọi điểm $%s$ thì $\\overrightarrow{%s}+\\overrightarrow{%s}+\\overrightarrow{%s}=3\\overrightarrow{%s}$' % (n_pt, s_NA, s_NB, s_NC, s_GN), 'Với mọi điểm $%s$ thì $\\overrightarrow{%s}+\\overrightarrow{%s}+\\overrightarrow{%s}=2\\overrightarrow{%s}$' % (n_pt, s_NA, s_NB, s_NC, s_NG)])
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    list_vd_1 = [vd_da_1]
    loigiai_vd_1 = clean_sign('''Vì $%s$ là trọng tâm tam giác $%s$ nên $\\overrightarrow{%s}+\\overrightarrow{%s}+\\overrightarrow{%s}=\\vec{0} \\Rightarrow \\overrightarrow{%s}-\\overrightarrow{%s}+\\overrightarrow{%s}-\\overrightarrow{%s}+\\overrightarrow{%s}-\\overrightarrow{%s}=\\vec{0} \\Rightarrow \\overrightarrow{%s}+\\overrightarrow{%s}+\\overrightarrow{%s}=3\\overrightarrow{%s}$.''' % (g_pt, tri_name, s_GA, s_GB, s_GC, s_NA, s_NG, s_NB, s_NG, s_NC, s_NG, s_NA, s_NB, s_NC, s_NG))
    list_vd_2 = [loigiai_vd_1]
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    vdc_da_1_d = '\\True Phân tích $\\overrightarrow{%s}$ theo hai vectơ $\\overrightarrow{%s}, \\overrightarrow{%s}$ ta được $\\overrightarrow{%s}=\\dfrac{\\overrightarrow{%s}+\\overrightarrow{%s}}{3}$' % (s_AG, s_AB, s_AC, s_AG, s_AB, s_AC)
    vdc_da_1_s = random.choice(['Phân tích $\\overrightarrow{%s}$ theo hai vectơ $\\overrightarrow{%s}, \\overrightarrow{%s}$ ta được $\\overrightarrow{%s}=\\dfrac{\\overrightarrow{%s}+\\overrightarrow{%s}}{2}$' % (s_AG, s_AB, s_AC, s_AG, s_AB, s_AC), 'Phân tích $\\overrightarrow{%s}$ theo hai vectơ $\\overrightarrow{%s}, \\overrightarrow{%s}$ ta được $\\overrightarrow{%s}=\\dfrac{2\\left(\\overrightarrow{%s}+\\overrightarrow{%s}\\right)}{3}$' % (s_AG, s_AB, s_AC, s_AG, s_AB, s_AC)])
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    list_vdc_1 = [vdc_da_1]
    loigiai_vdc_1 = clean_sign('''Ta có $\\overrightarrow{%s}=\\dfrac{2}{3}\\overrightarrow{%s}=\\dfrac{2}{3}\\cdot\\dfrac{1}{2}\\left(\\overrightarrow{%s}+\\overrightarrow{%s}\\right) \\Rightarrow \\overrightarrow{%s}=\\dfrac{\\overrightarrow{%s}+\\overrightarrow{%s}}{3}$.''' % (s_AG, s_AM, s_AB, s_AC, s_AG, s_AB, s_AC))
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
    list_nb_1 = [clean_sign(nb_da_1)]
    list_th_1 = [clean_sign(th_da_1)]
    list_vd_1 = [clean_sign(vd_da_1)]
    list_vdc_1 = [clean_sign(vdc_da_1)]
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

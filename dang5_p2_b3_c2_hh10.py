
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


def bt_dang5_p2_b3_c2_hh10(self):
    def clean_sign(s):
        return s.replace('- -', '+ ').replace('--', '+').replace('+ -', '- ').replace('+-', '-')
    quad_sets = [('A', 'B', 'C', 'D'), ('E', 'F', 'G', 'H'), ('P', 'Q', 'R', 'S')]
    p1, p2, p3, p4 = random.choice(quad_sets)
    quad_name = p1 + p2 + p3 + p4
    used = set([p1, p2, p3, p4])
    mid_sets = [pair for pair in [('M', 'N'), ('I', 'J'), ('K', 'L')] if pair[0] not in used and pair[1] not in used]
    m1, m2 = random.choice(mid_sets)
    used.update([m1, m2])
    g_pt = random.choice([c for c in ['G', 'T', 'U'] if c not in used])
    used.add(g_pt)
    o_pt = random.choice([c for c in ['O', 'S', 'X'] if c not in used])
    s_AB, s_CD, s_DC = p1 + p2, p3 + p4, p4 + p3
    s_MN, s_NM = m1 + m2, m2 + m1
    s_MA, s_MB, s_MC, s_MD = m1 + p1, m1 + p2, m1 + p3, m1 + p4
    s_BC, s_AD, s_AC, s_BD = p2 + p3, p1 + p4, p1 + p3, p2 + p4
    s_OA, s_OB, s_OC, s_OD = o_pt + p1, o_pt + p2, o_pt + p3, o_pt + p4
    s_OM, s_ON, s_OG = o_pt + m1, o_pt + m2, o_pt + g_pt
    noidungcauhoi = '''Cho tứ giác $%s$. Gọi $%s, %s$ lần lượt là trung điểm của các cạnh $%s$ và $%s$. Gọi $%s$ là trung điểm $%s$. Gọi $%s$ là điểm bất kì. Xét tính đúng sai của các khẳng định sau:''' % (quad_name, m1, m2, s_AB, s_CD, g_pt, s_MN, o_pt)
    tikz_hinh = '''\\begin{tikzpicture}[line width=1pt, scale=0.8]
    \\coordinate (B) at (0,0);
    \\coordinate (C) at (3,0);
    \\coordinate (A) at (-0.6,2.2);
    \\coordinate (D) at (4.2,3.2);
    \\coordinate (M) at (-0.3,1.1);
    \\coordinate (N) at (3.6,1.6);
    \\draw (A)--(B)--(C)--(D)--cycle;
    \\draw (M)--(N) (M)--(C) (M)--(D);
    \\fill (A) circle (1.5pt) node[above left] {$%s$};
    \\fill (B) circle (1.5pt) node[below left] {$%s$};
    \\fill (C) circle (1.5pt) node[below right] {$%s$};
    \\fill (D) circle (1.5pt) node[above right] {$%s$};
    \\fill (M) circle (1.5pt) node[left] {$%s$};
    \\fill (N) circle (1.5pt) node[right] {$%s$};
    \\end{tikzpicture}''' % (p1, p2, p3, p4, m1, m2)
    nb_da_1_d = '\\True $\\overrightarrow{%s}+\\overrightarrow{%s}=2\\overrightarrow{%s}$' % (s_MC, s_MD, s_MN)
    nb_da_1_s = random.choice(['$\\overrightarrow{%s}+\\overrightarrow{%s}=2\\overrightarrow{%s}$' % (s_MC, s_MD, s_NM), '$\\overrightarrow{%s}+\\overrightarrow{%s}=4\\overrightarrow{%s}$.' % (s_MC, s_MD, s_MN)])
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    list_nb_1 = [nb_da_1]
    loigiai_nb_1 = clean_sign('''Do $%s$ là trung điểm của cạnh $%s$ nên $\\overrightarrow{%s}+\\overrightarrow{%s}=\\vec{0}$. Do $%s$ là trung điểm của cạnh $%s$ nên $2\\overrightarrow{%s}=\\overrightarrow{%s}+\\overrightarrow{%s}$.''' % (m1, s_AB, s_MB, s_MA, m2, s_DC, s_MN, s_MC, s_MD)) + ' \\\\\n' + tikz_hinh
    list_nb_2 = [loigiai_nb_1]
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    th_da_1_d = '\\True $\\overrightarrow{%s}+\\overrightarrow{%s}=2\\overrightarrow{%s}$' % (s_BC, s_AD, s_MN)
    th_da_1_s = random.choice(['$\\overrightarrow{%s}+\\overrightarrow{%s}=2\\overrightarrow{%s}$' % (s_BC, s_AD, s_NM), '$\\overrightarrow{%s}+\\overrightarrow{%s}=4\\overrightarrow{%s}$' % (s_BC, s_AD, s_MN)])
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    list_th_1 = [th_da_1]
    loigiai_th_1 = clean_sign('''Ta có: $2\\overrightarrow{%s}=\\overrightarrow{%s}+\\overrightarrow{%s}=\\overrightarrow{%s}+\\overrightarrow{%s}+\\overrightarrow{%s}+\\overrightarrow{%s}=\\overrightarrow{%s}+\\overrightarrow{%s}+\\left(\\overrightarrow{%s}+\\overrightarrow{%s}\\right)=\\overrightarrow{%s}+\\overrightarrow{%s}$.''' % (s_MN, s_MC, s_MD, s_MB, s_BC, s_MA, s_AD, s_AD, s_BC, s_MA, s_MB, s_AD, s_BC))
    list_th_2 = [loigiai_th_1]
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    vd_da_1_d = '\\True $\\overrightarrow{%s}+\\overrightarrow{%s}=2\\overrightarrow{%s}$' % (s_AC, s_BD, s_MN)
    vd_da_1_s = random.choice(['$\\overrightarrow{%s}+\\overrightarrow{%s}=2\\overrightarrow{%s}$.' % (s_AC, s_BD, s_NM), '$\\overrightarrow{%s}+\\overrightarrow{%s}=4\\overrightarrow{%s}$' % (s_AC, s_BD, s_MN)])
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    list_vd_1 = [vd_da_1]
    loigiai_vd_1 = clean_sign('''Mặt khác: $2\\overrightarrow{%s}=\\overrightarrow{%s}+\\overrightarrow{%s}=\\left(\\overrightarrow{%s}+\\overrightarrow{%s}\\right)+\\left(\\overrightarrow{%s}+\\overrightarrow{%s}\\right)=\\overrightarrow{%s}+\\overrightarrow{%s}$.''' % (s_MN, s_AD, s_BC, s_AC, s_CD, s_BD, s_DC, s_AC, s_BD))
    list_vd_2 = [loigiai_vd_1]
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    k_mau_sai = random.choice([2, 3])
    vdc_da_1_d = '\\True $\\overrightarrow{%s}=\\dfrac{1}{4}\\left(\\overrightarrow{%s}+\\overrightarrow{%s}+\\overrightarrow{%s}+\\overrightarrow{%s}\\right)$' % (s_OG, s_OA, s_OB, s_OC, s_OD)
    vdc_da_1_s = '$\\overrightarrow{%s}=\\dfrac{1}{%s}\\left(\\overrightarrow{%s}+\\overrightarrow{%s}+\\overrightarrow{%s}+\\overrightarrow{%s}\\right)$' % (s_OG, k_mau_sai, s_OA, s_OB, s_OC, s_OD)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    list_vdc_1 = [vdc_da_1]
    loigiai_vdc_1 = clean_sign('''Ta có: $\\dfrac{1}{4}\\left(\\overrightarrow{%s}+\\overrightarrow{%s}+\\overrightarrow{%s}+\\overrightarrow{%s}\\right)=\\dfrac{1}{4}\\left(2\\overrightarrow{%s}+2\\overrightarrow{%s}\\right)=\\dfrac{1}{2}\\left(\\overrightarrow{%s}+\\overrightarrow{%s}\\right)=\\dfrac{1}{2}\\cdot 2\\overrightarrow{%s}=\\overrightarrow{%s}$.''' % (s_OA, s_OB, s_OC, s_OD, s_OM, s_ON, s_OM, s_ON, s_OG, s_OG))
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


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


def bt_dang4_p2_b3_c2_hh10(self):
    def clean_sign(s):
        return s.replace('- -', '+ ').replace('--', '+').replace('+ -', '- ').replace('+-', '-')
    vertex_sets = [('A', 'B', 'C', 'D'), ('M', 'N', 'P', 'Q'), ('E', 'F', 'G', 'H'), ('I', 'J', 'K', 'L')]
    p1, p2, p3, p4 = random.choice(vertex_sets)
    hbh_name = p1 + p2 + p3 + p4
    ct = random.choice([c for c in ['O', 'I'] if c not in (p1, p2, p3, p4)])
    pt = random.choice([m for m in ['M', 'S', 'K', 'N'] if m not in (p1, p2, p3, p4, ct)])
    noidungcauhoi = '''Cho hình bình hành $%s$ có tâm $%s$, $%s$ là một điểm bất kỳ. Xét tính đúng sai của các khẳng định sau:''' % (hbh_name, ct, pt)
    tikz_hinh = '''\\begin{tikzpicture}[line width=1pt, scale=0.8]
    \\coordinate (B) at (0,0);
    \\coordinate (C) at (4,0);
    \\coordinate (A) at (1,2);
    \\coordinate (D) at (5,2);
    \\coordinate (O) at (2.5,1);
    \\draw (A)--(B)--(C)--(D)--cycle;
    \\draw (A)--(C) (B)--(D);
    \\fill (A) circle (2pt) node[above left] {$%s$};
    \\fill (B) circle (2pt) node[below left] {$%s$};
    \\fill (C) circle (2pt) node[below right] {$%s$};
    \\fill (D) circle (2pt) node[above right] {$%s$};
    \\fill (O) circle (2pt) node[below] {$%s$};
    \\end{tikzpicture}''' % (p1, p2, p3, p4, ct)
    nb_cases = [(p1, p2, p4, p3), (p2, p1, p3, p4), (p3, p2, p4, p1), (p4, p1, p3, p2)]
    v0, v1, v2, v_opp = random.choice(nb_cases)
    nb_da_1_d = '\\True $\\overrightarrow{%s%s}+\\overrightarrow{%s%s}=\\overrightarrow{%s%s}$' % (v0, v1, v0, v2, v0, v_opp)
    nb_da_1_s = '$\\overrightarrow{%s%s}+\\overrightarrow{%s%s}=\\overrightarrow{%s%s}$' % (v0, v1, v0, v2, v_opp, v0)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    list_nb_1 = [nb_da_1]
    loigiai_nb_1 = clean_sign('''Theo quy tắc hình bình hành ta có: $\\overrightarrow{%s%s}+\\overrightarrow{%s%s}=\\overrightarrow{%s%s}$.''' % (v0, v1, v0, v2, v0, v_opp)) + ' \\\\\n' + tikz_hinh
    list_nb_2 = [loigiai_nb_1]
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    th_cases = [(p1, p3), (p3, p1), (p2, p4), (p4, p2)]
    u_d, v_d = random.choice(th_cases)
    th_da_1_d = '\\True $\\overrightarrow{%s%s}=2\\overrightarrow{%s%s}$' % (u_d, v_d, u_d, ct)
    th_da_1_s = '$\\overrightarrow{%s%s}=2\\overrightarrow{%s%s}$' % (u_d, v_d, ct, u_d)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    list_th_1 = [th_da_1]
    loigiai_th_1 = clean_sign('''Do $%s$ là hình bình hành tâm $%s$ nên $%s$ là trung điểm của $%s%s \\Rightarrow \\overrightarrow{%s%s}=2\\overrightarrow{%s%s}$.''' % (hbh_name, ct, ct, u_d, v_d, u_d, v_d, u_d, ct))
    list_th_2 = [loigiai_th_1]
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    k_sai = random.choice([2, 3, 6, -4])
    vd_da_1_d = '\\True $\\overrightarrow{%s%s}+\\overrightarrow{%s%s}+\\overrightarrow{%s%s}+\\overrightarrow{%s%s}=4\\overrightarrow{%s%s}$' % (pt, p1, pt, p2, pt, p3, pt, p4, pt, ct)
    vd_da_1_s = '$\\overrightarrow{%s%s}+\\overrightarrow{%s%s}+\\overrightarrow{%s%s}+\\overrightarrow{%s%s}=%s\\overrightarrow{%s%s}$' % (pt, p1, pt, p2, pt, p3, pt, p4, k_sai, pt, ct)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    list_vd_1 = [vd_da_1]
    loigiai_vd_1 = clean_sign('''Ta có: $\\overrightarrow{%s%s}+\\overrightarrow{%s%s}+\\overrightarrow{%s%s}+\\overrightarrow{%s%s}$ \\\\ $= \\overrightarrow{%s%s}+\\overrightarrow{%s%s}+\\overrightarrow{%s%s}+\\overrightarrow{%s%s}+\\overrightarrow{%s%s}+\\overrightarrow{%s%s}+\\overrightarrow{%s%s}+\\overrightarrow{%s%s} = 4\\overrightarrow{%s%s}+\\left(\\underbrace{\\overrightarrow{%s%s}+\\overrightarrow{%s%s}}_{\\vec{0}}\\right)+\\left(\\underbrace{\\overrightarrow{%s%s}+\\overrightarrow{%s%s}}_{\\vec{0}}\\right)=4\\overrightarrow{%s%s}$.''' % (pt, p1, pt, p2, pt, p3, pt, p4, pt, ct, ct, p1, pt, ct, ct, p2, pt, ct, ct, p3, pt, ct, ct, p4, pt, ct, ct, p1, ct, p3, ct, p2, ct, p4, pt, ct))
    list_vd_2 = [loigiai_vd_1]
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    vdc_cases = [(p1, p2, p3, p4, p1+p2+p4, p2+p3+p4), (p2, p1, p3, p4, p1+p2+p3, p1+p3+p4), (p3, p1, p2, p4, p2+p3+p4, p1+p2+p4), (p4, p1, p2, p3, p1+p3+p4, p1+p2+p3)]
    ex_v, r1, r2, r3, tri_true, tri_false = random.choice(vdc_cases)
    vdc_da_1_d = '\\True Nếu $\\overrightarrow{%s%s}+\\overrightarrow{%s%s}+\\overrightarrow{%s%s}=6\\overrightarrow{%s%s}$ thì $%s$ là trọng tâm $\\triangle %s$' % (pt, r1, pt, r2, pt, r3, pt, ct, pt, tri_true)
    vdc_da_1_s = 'Nếu $\\overrightarrow{%s%s}+\\overrightarrow{%s%s}+\\overrightarrow{%s%s}=6\\overrightarrow{%s%s}$ thì $%s$ là trọng tâm $\\triangle %s$' % (pt, r1, pt, r2, pt, r3, pt, ct, pt, tri_false)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    list_vdc_1 = [vdc_da_1]
    loigiai_vdc_1 = clean_sign('''Ta có $\\overrightarrow{%s%s}+\\overrightarrow{%s%s}+\\overrightarrow{%s%s}=6\\overrightarrow{%s%s} \\Rightarrow 4\\overrightarrow{%s%s}-\\overrightarrow{%s%s}=6\\overrightarrow{%s%s} \\Rightarrow -\\overrightarrow{%s%s}=2\\overrightarrow{%s%s} \\Rightarrow \\overrightarrow{%s%s}=-2\\overrightarrow{%s%s}$. Mặt khác $%s%s$ là trung tuyến của $\\triangle %s$ nên suy ra $%s$ là trọng tâm $\\triangle %s$.''' % (pt, r1, pt, r2, pt, r3, pt, ct, pt, ct, pt, ex_v, pt, ct, pt, ex_v, pt, ct, pt, ex_v, pt, ct, ex_v, ct, tri_true, pt, tri_true))
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

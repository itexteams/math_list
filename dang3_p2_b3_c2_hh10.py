
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


def bt_dang3_p2_b3_c2_hh10(self):
    def clean_sign(s):
        return s.replace('- -', '+ ').replace('--', '+').replace('+ -', '- ').replace('+-', '-')
    dir_pairs = [('đông bắc', 'tây nam', 45, 225), ('tây bắc', 'đông nam', 135, 315), ('đông', 'tây', 0, 180), ('bắc', 'nam', 90, 270)]
    hA, hB, angA, angB = random.choice(dir_pairs)
    speeds = [400, 450, 500, 600, 750, 800, 900]
    vA, vB = random.sample(speeds, 2)
    k = Rational(vB, vA)
    inv_k = Rational(vA, vB)
    lenA = round(1.5 * vA / max(vA, vB) + 0.5, 2)
    lenB = round(1.5 * vB / max(vA, vB) + 0.5, 2)
    cxA, cyA = 4.2, 0.9
    cxB, cyB = 4.5, -0.9
    dxA, dyA = round(lenA * math.cos(math.radians(angA)) / 2, 2), round(lenA * math.sin(math.radians(angA)) / 2, 2)
    dxB, dyB = round(lenB * math.cos(math.radians(angB)) / 2, 2), round(lenB * math.sin(math.radians(angB)) / 2, 2)
    xA1, yA1, xA2, yA2 = round(cxA - dxA, 2), round(cyA - dyA, 2), round(cxA + dxA, 2), round(cyA + dyA, 2)
    xB1, yB1, xB2, yB2 = round(cxB - dxB, 2), round(cyB - dyB, 2), round(cxB + dxB, 2), round(cyB + dyB, 2)
    tikz_hinh = '''\\begin{center}
    \\begin{tikzpicture}[line width=1pt, scale=0.85]
    \\draw (0,0) circle (1.1);
    \\draw[->] (0,-1.5)--(0,1.5) node[above] {N};
    \\node[below] at (0,-1.5) {S};
    \\draw[->] (-1.5,0)--(1.5,0) node[right] {E};
    \\node[left] at (-1.5,0) {W};
    \\draw (-0.95,-0.95)--(0.95,0.95);
    \\draw (-0.95,0.95)--(0.95,-0.95);
    \\node[above right] at (0.78,0.78) {\\footnotesize NE};
    \\node[above left] at (-0.78,0.78) {\\footnotesize NW};
    \\node[below left] at (-0.78,-0.78) {\\footnotesize SW};
    \\node[below right] at (0.78,-0.78) {\\footnotesize SE};
    \\fill (0,0) circle (2pt);
    \\draw[->, blue] (%s,%s)--(%s,%s) node[above left] {$\\vec{a}$};
    \\fill[blue] (%s,%s) circle (2pt) node[below left, black] {$A$};
    \\draw[->, red] (%s,%s)--(%s,%s) node[below right] {$\\vec{b}$};
    \\fill[red] (%s,%s) circle (2pt) node[above right, black] {$B$};
    \\end{tikzpicture}
    \\end{center}''' % (xA1, yA1, xA2, yA2, xA1, yA1, xB1, yB1, xB2, yB2, xB1, yB1)
    noidungcauhoi = clean_sign('''Máy bay $A$ đang bay về hướng %s với tốc độ $%s\\text{ km/h}$. Cùng lúc đó, máy bay $B$ đang bay về hướng %s với tốc độ $%s\\text{ km/h}$ (như hình vẽ). Xét tính đúng sai của các khẳng định sau:''' % (hA, vA, hB, vB)) + ' \\\\\n' + tikz_hinh
    nb_da_1_d = '\\True Vectơ vận tốc $\\vec{b}$ của máy bay $B$ ngược hướng với vectơ vận tốc $\\vec{a}$ của máy bay $A$'
    nb_da_1_s = 'Vectơ vận tốc $\\vec{b}$ của máy bay $B$ cùng hướng với vectơ vận tốc $\\vec{a}$ của máy bay $A$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    list_nb_1 = [nb_da_1]
    loigiai_nb_1 = clean_sign('''Ta thấy hướng %s ngược hướng với hướng %s nên vectơ vận tốc $\\vec{b}$ của máy bay $B$ ngược hướng với vectơ vận tốc $\\vec{a}$ của máy bay $A$ (1).''' % (hA, hB))
    list_nb_2 = [loigiai_nb_1]
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    th_da_1_d = '\\True $|\\vec{a}|=%s\\text{ (km/h)}$; $|\\vec{b}|=%s\\text{ (km/h)}$' % (vA, vB)
    th_da_1_s = '$|\\vec{a}|=%s\\text{ (km/h)}$; $|\\vec{b}|=%s\\text{ (km/h)}$' % (vB, vA)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    list_th_1 = [th_da_1]
    loigiai_th_1 = clean_sign('''Theo đề bài ta có $|\\vec{a}|=%s\\text{ (km/h)}$; $|\\vec{b}|=%s\\text{ (km/h)}$.''' % (vA, vB))
    list_th_2 = [loigiai_th_1]
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    vd_da_1_d = '\\True $\\vec{b}=%s\\vec{a}$' % (latex(-k))
    vd_da_1_s = random.choice(['$\\vec{b}=%s\\vec{a}$' % (latex(k)), '$\\vec{b}=%s\\vec{a}$' % (latex(-inv_k))])
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    list_vd_1 = [vd_da_1]
    loigiai_vd_1 = clean_sign('''Ta có $\\dfrac{|\\vec{b}|}{|\\vec{a}|}=\\dfrac{%s}{%s}=%s \\Rightarrow |\\vec{b}|=%s|\\vec{a}|$ (2). Từ (1) và (2) suy ra $\\vec{b}=%s\\vec{a}$.''' % (vB, vA, latex(k), latex(k), latex(-k)))
    list_vd_2 = [loigiai_vd_1]
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    vdc_da_1_d = '\\True $\\vec{a}=%s\\vec{b}$' % (latex(-inv_k))
    vdc_da_1_s = random.choice(['$\\vec{a}=%s\\vec{b}$' % (latex(inv_k)), '$\\vec{a}=%s\\vec{b}$' % (latex(k))])
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    list_vdc_1 = [vdc_da_1]
    loigiai_vdc_1 = clean_sign('''Từ $\\vec{b}=%s\\vec{a}$ suy ra $\\vec{a}=%s\\vec{b}$.''' % (latex(-k), latex(-inv_k)))
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

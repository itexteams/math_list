
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


def bt_dang19_p2_b2_c2_hh10(self):
    k = random.randint(1, 6)
    canh = 'a' if k == 1 else '%sa' % k
    kq_vd_d = 'a\\sqrt{3}' if k == 1 else '%sa\\sqrt{3}' % k
    kq_vd_s1 = 'a\\sqrt{2}' if k == 1 else '%sa\\sqrt{2}' % k
    kq_vd_s2 = '2a' if k == 1 else '%sa' % (2 * k)
    kq_vd_s3 = '\\dfrac{a\\sqrt{3}}{2}' if k == 1 else '\\dfrac{%sa\\sqrt{3}}{2}' % k
    kq_vd_s = random.choice([kq_vd_s1, kq_vd_s2, kq_vd_s3])
    A, B, C, I, M, D, H = random.choice([('A', 'B', 'C', 'I', 'M', 'D', 'H'), ('A', 'B', 'C', 'E', 'M', 'D', 'H'), ('M', 'N', 'P', 'I', 'K', 'Q', 'H'), ('D', 'E', 'F', 'I', 'M', 'K', 'H')])
    hinh_vd = ('\\begin{center}\n'
    '\\begin{tikzpicture}[line width=1pt]\n'
    '\\coordinate (A) at (0,2.25);\n'
    '\\coordinate (B) at (-1.3,0);\n'
    '\\coordinate (C) at (1.3,0);\n'
    '\\coordinate (D) at (0,-2.25);\n'
    '\\coordinate (H) at (0,0);\n'
    '\\draw (A) -- (B) -- (D) -- (C) -- cycle;\n'
    '\\draw (A) -- (D) (B) -- (C);\n'
    '\\fill (A) circle (1.5pt) node[above] {$%s$};\n'
    '\\fill (B) circle (1.5pt) node[left] {$%s$};\n'
    '\\fill (C) circle (1.5pt) node[right] {$%s$};\n'
    '\\fill (D) circle (1.5pt) node[below] {$%s$};\n'
    '\\fill (H) circle (1.5pt) node[below left] {$%s$};\n'
    '\\end{tikzpicture}\n'
    '\\end{center}' % (A, B, C, D, H))
    noidungcauhoi = 'Cho $\\triangle %s%s%s$ đều cạnh $%s$, với $%s$ là trung điểm cạnh $%s%s$. Xét tính đúng sai của các khẳng định sau:' % (A, B, C, canh, I, A, C)
    nb_opt_d, nb_opt_s = random.choice([('=%s%s' % (I, C), '=%s%s' % (C, I)), ('=-%s%s' % (C, I), '=%s%s' % (C, I))])
    if nb_opt_d.startswith('=-'):
        nb_da_1_d = '\\True $\\overrightarrow{%s%s} = -\\overrightarrow{%s%s}$' % (A, I, C, I)
    else:
        nb_da_1_d = '\\True $\\overrightarrow{%s%s} = \\overrightarrow{%s%s}$' % (A, I, I, C)
    nb_da_1_s = '$\\overrightarrow{%s%s} = \\overrightarrow{%s%s}$' % (A, I, C, I)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    list_nb_1 = [nb_da_1]
    loigiai_nb_1 = 'Ta có $%s$ là trung điểm cạnh $%s%s$ suy ra $\\overrightarrow{%s%s}, \\overrightarrow{%s%s}$ ngược hướng và cùng độ dài nên $\\overrightarrow{%s%s} = -\\overrightarrow{%s%s} = \\overrightarrow{%s%s}$.' % (I, A, C, A, I, C, I, A, I, C, I, I, C)
    list_nb_2 = [loigiai_nb_1]
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    th_da_1_d = '\\True $\\overrightarrow{%s%s} - \\overrightarrow{%s%s} = \\overrightarrow{%s%s}$' % (C, A, B, A, C, B)
    th_da_1_s = '$\\overrightarrow{%s%s} - \\overrightarrow{%s%s} = \\overrightarrow{%s%s}$' % (C, A, B, A, B, C)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    list_th_1 = [th_da_1]
    loigiai_th_1 = 'Ta có $\\overrightarrow{%s%s} - \\overrightarrow{%s%s} = \\overrightarrow{%s%s} + \\overrightarrow{%s%s} = \\overrightarrow{%s%s} = -\\overrightarrow{%s%s}$.' % (C, A, B, A, C, A, A, B, C, B, B, C)
    list_th_2 = [loigiai_th_1]
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    vd_da_1_d = '\\True $\\left|\\overrightarrow{%s%s} + \\overrightarrow{%s%s}\\right| = %s$' % (A, B, A, C, kq_vd_d)
    vd_da_1_s = '$\\left|\\overrightarrow{%s%s} + \\overrightarrow{%s%s}\\right| = %s$' % (A, B, A, C, kq_vd_s)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    list_vd_1 = [vd_da_1]
    loigiai_vd_1 = 'Dựng hình thoi $%s%s%s%s$ có tâm $%s$ là trung điểm của $%s%s$. Ta có $\\left|\\overrightarrow{%s%s} + \\overrightarrow{%s%s}\\right| = \\left|\\overrightarrow{%s%s}\\right| = %s%s = 2%s%s = 2 \\cdot %s\\dfrac{\\sqrt{3}}{2} = %s$.\n' % (A, B, D, C, H, B, C, A, B, A, C, A, D, A, D, A, H, canh, kq_vd_d) + hinh_vd
    list_vd_2 = [loigiai_vd_1]
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    hbh_s = random.choice([A + B + M + C, A + C + B + M])
    vdc_da_1_d = '\\True Điểm $%s$ thỏa mãn đẳng thức $\\overrightarrow{%s%s} + \\overrightarrow{%s%s} = \\overrightarrow{%s%s}$ là một đỉnh của hình bình hành $%s%s%s%s$' % (M, A, B, I, M, I, C, A, B, C, M)
    vdc_da_1_s = 'Điểm $%s$ thỏa mãn đẳng thức $\\overrightarrow{%s%s} + \\overrightarrow{%s%s} = \\overrightarrow{%s%s}$ là một đỉnh của hình bình hành $%s$' % (M, A, B, I, M, I, C, hbh_s)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    list_vdc_1 = [vdc_da_1]
    loigiai_vdc_1 = 'Ta có $\\overrightarrow{%s%s} + \\overrightarrow{%s%s} = \\overrightarrow{%s%s} \\Leftrightarrow \\overrightarrow{%s%s} = \\overrightarrow{%s%s} - \\overrightarrow{%s%s} \\Leftrightarrow \\overrightarrow{%s%s} = \\overrightarrow{%s%s}$ nên $%s$ là một đỉnh của hình bình hành $%s%s%s%s$.' % (A, B, I, M, I, C, A, B, I, C, I, M, A, B, M, C, M, A, B, C, M)
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

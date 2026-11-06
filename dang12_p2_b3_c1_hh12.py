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


def bt_dang12_p2_b3_c1_hh12(self):
    def f_v(x, y, z):
        terms = []
        if x != 0: terms.append(f"\\vec{{i}}" if x==1 else f"-\\vec{{i}}" if x==-1 else f"{x}\\vec{{i}}")
        if y != 0: terms.append(f"+ \\vec{{j}}" if y==1 else f"- \\vec{{j}}" if y==-1 else f"+ {y}\\vec{{j}}" if y>0 else f"- {abs(y)}\\vec{{j}}")
        if z != 0: terms.append(f"+ \\vec{{k}}" if z==1 else f"- \\vec{{k}}" if z==-1 else f"+ {z}\\vec{{k}}" if z>0 else f"- {abs(z)}\\vec{{k}}")
        res = " ".join(terms)
        if res.startswith("+ "): res = res[2:]
        return res if res else "\\vec{0}"
    def f_e(var, val):
        if val > 0: return f"{var}-{val}"
        elif val < 0: return f"{var}+{abs(val)}"
        return f"{var}"
    def f_s(v1, v2):
        if v2 < 0: return f"{v1}+{-v2}"
        return f"{v1}-{v2}"
    xm, ym, zm = randint(-5, 5), randint(-5, 5), randint(-5, 5)
    xn, yn, zn = randint(-5, 5), randint(-5, 5), randint(-5, 5)
    xa, ya, za = randint(-5, 5), randint(-5, 5), random.choice([0, randint(-3, 3)])
    noidungcauhoi = f"Trong không gian $Oxyz$, cho $\\overrightarrow{{OM}} = {f_v(xm, ym, zm)}$, $\\overrightarrow{{ON}} = {f_v(xn, yn, zn)}$ và $\\vec{{a}} = {f_v(xa, ya, za)}$."
    nb_da_1_d = f"\\True Tọa độ của vectơ $\\vec{{a}}$ là $({xa}; {ya}; {za})$"
    sai_za = za + random.choice([-2, -1, 1, 2])
    nb_da_1_s = f"Tọa độ của vectơ $\\vec{{a}}$ là $({xa}; {ya}; {sai_za})$"
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    list_nb_1 = [nb_da_1]
    loigiai_nb_1 = f"Ta có tọa độ của vectơ $\\vec{{a}}$ là $({xa}; {ya}; {za})$."
    list_nb_2 = [loigiai_nb_1]
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    th_da_1_d = f"\\True Tọa độ của điểm $M$ là $({xm}; {ym}; {zm})$"
    th_da_1_s = f"Tọa độ của điểm $M$ là $({-xm}; {-ym}; {-zm})$"
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    list_th_1 = [th_da_1]
    loigiai_th_1 = f"Tọa độ của điểm $M$ là $({xm}; {ym}; {zm})$."
    list_th_2 = [loigiai_th_1]
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    xmn, ymn, zmn = xn - xm, yn - ym, zn - zm
    vd_da_1_d = f"\\True Tọa độ của vectơ $\\overrightarrow{{MN}}$ là $({xmn}; {ymn}; {zmn})$"
    vd_da_1_s = f"Tọa độ của vectơ $\\overrightarrow{{MN}}$ là $({-xmn}; {-ymn}; {-zmn})$"
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    list_vd_1 = [vd_da_1]
    loigiai_vd_1 = f"Tọa độ của điểm $N$ là $({xn}; {yn}; {zn})$. \\\\\nTa có $\\overrightarrow{{MN}} = ({f_s(xn, xm)}; {f_s(yn, ym)}; {f_s(zn, zm)}) = ({xmn}; {ymn}; {zmn})$."
    list_vd_2 = [loigiai_vd_1]
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    xk, yk, zk = xa + xm, ya + ym, za + zm
    vdc_da_1_d = f"\\True Nếu $\\overrightarrow{{MK}} = \\vec{{a}}$ thì tọa độ của điểm $K$ là $({xk}; {yk}; {zk})$"
    vdc_da_1_s = f"Nếu $\\overrightarrow{{MK}} = \\vec{{a}}$ thì tọa độ của điểm $K$ là $({xk + random.choice([-1, 1])}; {yk}; {zk})$"
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    list_vdc_1 = [vdc_da_1]
    loigiai_vdc_1 = f"Gọi tọa độ của $K$ là $(x; y; z)$. \\\\\nTa có $\\overrightarrow{{MK}} = ({f_e('x', xm)}; {f_e('y', ym)}; {f_e('z', zm)})$. \\\\\nVì $\\overrightarrow{{MK}} = \\vec{{a}}$ nên \n$\\begin{{cases}} {f_e('x', xm)} = {xa} \\\\ {f_e('y', ym)} = {ya} \\\\ {f_e('z', zm)} = {za} \\end{{cases}} \\Leftrightarrow \\begin{{cases}} x = {xk} \\\\ y = {yk} \\\\ z = {zk} \\end{{cases}}$. \\\\\nVậy $K({xk}; {yk}; {zk})$."
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
        if 1 <= count_true_answers(answers) <= 3:
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
        '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
        '\\choiceTFn \n'
        '{' + str(shuffled_answers_nb[0]) + '}\n'
        '{' + str(shuffled_answers_th[0]) + '}\n'
        '{' + str(shuffled_answers_vd[0]) + '}\n'
        '{' + str(shuffled_answers_vdc[0]) + '}\n'
        '\\loigiai{ \n'
        '\\begin{enumEX}[a)]{1} \n'
        '\\item ' + str(shuffled_solutions_nb[0]) + '\n'
        '\\item ' + str(shuffled_solutions_th[0]) + '\n'
        '\\item ' + str(shuffled_solutions_vd[0]) + '\n'
        '\\item ' + str(shuffled_solutions_vdc[0]) + '\n'
        '\\end{enumEX}} \n'
        '\\end{ex}\n\\end{minipage}\n\n')
    return content


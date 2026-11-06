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


def bt_dang15_p2_b3_c1_hh12(self):
    def f_num(val):
        return "(%s)" % val if val < 0 else "%s" % val

    a = randint(2, 6)
    b = randint(2, 6)
    c = randint(2, 6)
    k = randint(2, 4)

    G_x = sp.Rational(2*a, 3)
    G_y = sp.Rational(2*b, 3)
    G_z = sp.Rational(2*c, 3)

    DB_x = a
    DB_y = -b
    DB_z = -c

    dot_AC_BD = b**2 - a**2
    len_AC_sq = a**2 + b**2
    len_BD_sq = a**2 + b**2 + c**2
    len_AC = sp.sqrt(len_AC_sq)
    len_BD = sp.sqrt(len_BD_sq)
    cos_val = dot_AC_BD / (len_AC * len_BD)

    N_x = k * a
    N_y = k * b
    N_z = sp.Rational(k + 1, 2) * c

    MN_x = k * a
    MN_y = k * b
    MN_z = sp.Rational(k, 2) * c

    MC_x = a
    MC_y = b
    MC_z = sp.Rational(1, 2) * c

    # Thêm "line width=1pt" vào trong tùy chọn của tikzpicture
    tikz_code = ("\\begin{center}\n\\begin{tikzpicture}[scale=0.5, x={(-0.5cm,-0.5cm)}, y={(1cm,0cm)}, z={(0cm,1cm)}, >=stealth, line width=1pt]\n\\coordinate (A) at (0,0,0);\n\\coordinate (B) at (%s,0,0);\n\\coordinate (C) at (%s,%s,0);\n\\coordinate (D) at (0,%s,0);\n\\coordinate (A') at (0,0,%s);\n\\coordinate (B') at (%s,0,%s);\n\\coordinate (C') at (%s,%s,%s);\n\\coordinate (D') at (0,%s,%s);\n\\draw[->] (B) -- (%s,0,0) node[right] {$x$};\n\\draw[->] (D) -- (0,%s,0) node[below] {$y$};\n\\draw[->] (A') -- (0,0,%s) node[right] {$z$};\n\\draw[dashed] (A) -- (B);\n\\draw[dashed] (A) -- (D);\n\\draw[dashed] (A) -- (A');\n\\draw (B) -- (C) -- (D);\n\\draw (B) -- (B');\n\\draw (C) -- (C');\n\\draw (D) -- (D');\n\\draw (A') -- (B') -- (C') -- (D') -- cycle;\n\\node[left] at (B) {$B$};\n\\node[right] at (C) {$C$};\n\\node[above right] at (D) {$D$};\n\\node[right] at (A') {$A'$};\n\\node[left] at (B') {$B'$};\n\\node[right] at (C') {$C'$};\n\\node[above right] at (D') {$D'$};\n\\node[below right] at (A) {$A$};\n\\end{tikzpicture}\n\\end{center}" % (a, a, b, b, c, a, c, a, b, c, b, c, a+1.5, b+1.5, c+1.5))

    noidungcauhoi = ("Cho hình hộp chữ nhật $ABCD.A'B'C'D'$ có $AB = %s, AD = %s, AA' = %s$ và hệ trục tọa độ $Oxyz$ được gắn như hình vẽ, $(O \\equiv A)$.\n%s" % (a, b, c, tikz_code))

    nb_da_1_d = "\\True Tọa độ trọng tâm của tam giác $B'C'D$ là $G\\left( %s; %s; %s \\right)$" % (latex(G_x), latex(G_y), latex(G_z))
    nb_da_1_s = "Tọa độ trọng tâm của tam giác $B'C'D$ là $G\\left( %s; %s; %s \\right)$" % (latex(G_x), latex(G_y), c)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    list_nb_1 = [nb_da_1]

    loigiai_nb_1 = ("Ta có $A$ là gốc tọa độ nên $A(0;0;0)$, suy ra $B'(%s;0;%s); C'(%s;%s;%s); D(0;%s;0)$. \\\\\n Tọa độ trọng tâm của tam giác $B'C'D$ là $G\\left( %s; %s; %s \\right)$." % (a, c, a, b, c, b, latex(G_x), latex(G_y), latex(G_z)))
    list_nb_2 = [loigiai_nb_1]
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

    th_da_1_d = "\\True $\\overrightarrow{D'B} = (%s; %s; %s)$" % (DB_x, DB_y, DB_z)
    th_da_1_s = "$\\overrightarrow{D'B} = (%s; %s; %s)$" % (-DB_x, -DB_y, -DB_z)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    list_th_1 = [th_da_1]

    loigiai_th_1 = ("Ta có $D'(0;%s;%s), B(%s;0;0)$ nên $\\overrightarrow{D'B} = (%s; %s; %s)$." % (b, c, a, DB_x, DB_y, DB_z))
    list_th_2 = [loigiai_th_1]
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

    sai_cos_val = -cos_val if cos_val != 0 else sp.Rational(1, 2)
    vd_da_1_d = "\\True $\\cos(\\overrightarrow{AC}, \\overrightarrow{B'D}) = %s$" % (latex(cos_val))
    vd_da_1_s = "$\\cos(\\overrightarrow{AC}, \\overrightarrow{B'D}) = %s$" % (latex(sai_cos_val))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    list_vd_1 = [vd_da_1]

    loigiai_vd_1 = ("Ta có $A(0;0;0), C(%s;%s;0)$ nên $\\overrightarrow{AC} = (%s;%s;0)$. \\\\\n $B'(%s;0;%s), D(0;%s;0)$ nên $\\overrightarrow{B'D} = (%s;%s;%s)$. \\\\\n $\\cos(\\overrightarrow{AC}, \\overrightarrow{B'D}) = \\frac{\\overrightarrow{AC} \\cdot \\overrightarrow{B'D}}{|\\overrightarrow{AC}| \\cdot |\\overrightarrow{B'D}|} = \\frac{%s + %s}{\\sqrt{%s + %s} \\cdot \\sqrt{%s + %s + %s}} = %s$." % (a, b, a, b, a, c, b, -a, b, -c, f_num(-a**2), b**2, a**2, b**2, (-a)**2, b**2, (-c)**2, latex(cos_val)))
    list_vd_2 = [loigiai_vd_1]
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

    vdc_da_1_d = "\\True Gọi $M$ là trung điểm của đoạn thẳng $AA'$, điểm $N\\left(%s; %s; %s \\right)$. Khi đó ba điểm $M, N, C'$ thẳng hàng" % (N_x, N_y, latex(N_z))
    vdc_da_1_s = "Gọi $M$ là trung điểm của đoạn thẳng $AA'$, điểm $N\\left(%s; %s; %s\\right)$. Khi đó ba điểm $M, N, C'$ thẳng hàng" % (N_x, N_y, latex(N_z + 1))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    list_vdc_1 = [vdc_da_1]

    M_z = sp.Rational(c, 2)
    loigiai_vdc_1 = ("Ta có $A'(0;0;%s)$, $M$ là trung điểm của đoạn thẳng $AA'$ nên $M\\left(0; 0; %s\\right)$. \\\\\n Xét điểm $N(%s; %s; %s)$ (với trường hợp mệnh đề đúng): $\\overrightarrow{MN} = \\left(%s; %s; %s\\right)$, $\\overrightarrow{MC'} = \\left(%s; %s; %s\\right)$. \\\\\n Vì $\\overrightarrow{MN} = %s \\overrightarrow{MC'}$ nên 3 điểm $M, N, C'$ thẳng hàng." % (c, latex(M_z), N_x, N_y, latex(N_z), MN_x, MN_y, latex(MN_z), MC_x, MC_y, latex(MC_z), k))
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


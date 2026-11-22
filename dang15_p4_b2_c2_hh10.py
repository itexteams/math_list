
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


def bt_dang15_p4_b2_c2_hh10(self):
    lisdang=['1', '2', '3']
    dang=random.choice(lisdang)
    F = random.choice([10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 80, 100])
    vat = random.choice(['ô tô', 'vật', 'chất điểm'])
    M, A, B, C, D = random.choice([('M','A','B','C','D'), ('O','A','B','C','D'), ('I','A','B','C','E')])
    if dang=='1':
        alpha = 60
        kq = F * sqrt(3)
    elif dang=='2':
        alpha = 90
        kq = F * sqrt(2)
    else:
        alpha = 120
        kq = F
    half_ang = alpha // 2
    ang1 = 180 - half_ang
    ang2 = 180 + half_ang
    d_val = round(2 * 2.5 * math.cos(math.radians(half_ang)), 2)
    ang_lbl = 180 + half_ang // 2
    hinh_de = ('\\begin{center}\n'
               '\\begin{tikzpicture}[scale=0.7, line width=1pt, line join=round, line cap=round]\n'
               '\\coordinate (M) at (0,0);\n'
               '\\coordinate (A) at (%s:2.5);\n'
               '\\coordinate (B) at (%s:2.5);\n'
               '\\coordinate (C) at (%s,0);\n'
               '\\draw[->, >=stealth] (M)--(A) node[midway, above right] {$\\vec{F}_1$};\n'
               '\\draw[->, >=stealth] (M)--(B) node[midway, below right] {$\\vec{F}_2$};\n'
               '\\draw[->, >=stealth] (M)--(C) node[midway, above] {$\\vec{F}_3$};\n'
               '\\draw (%s:0.6) arc (%s:%s:0.6);\n'
               '\\node at (180:1.1) {$%s^\\circ$};\n'
               '\\fill (A) circle (1.5pt) node[above] {$%s$};\n'
               '\\fill (B) circle (1.5pt) node[below] {$%s$};\n'
               '\\fill (C) circle (1.5pt) node[above] {$%s$};\n'
               '\\fill (M) circle (1.5pt) node[below] {$%s$};\n'
               '\\end{tikzpicture}\n'
               '\\end{center}\n' %(ang1, ang2, d_val, ang1, ang1, ang2, alpha, A, B, C, M))
    hinh_lg = ('\\begin{center}\n'
               '\\begin{tikzpicture}[scale=0.7, line width=1pt, line join=round, line cap=round]\n'
               '\\coordinate (M) at (0,0);\n'
               '\\coordinate (A) at (%s:2.5);\n'
               '\\coordinate (B) at (%s:2.5);\n'
               '\\coordinate (D) at (-%s,0);\n'
               '\\coordinate (C) at (%s,0);\n'
               '\\draw[->, >=stealth] (M)--(A) node[midway, above right] {$\\vec{F}_1$};\n'
               '\\draw[->, >=stealth] (M)--(B) node[midway, below right] {$\\vec{F}_2$};\n'
               '\\draw[->, >=stealth] (M)--(C) node[midway, above] {$\\vec{F}_3$};\n'
               '\\draw[->, >=stealth] (M)--(D) node[midway, above] {$\\vec{F}_1 + \\vec{F}_2$};\n'
               '\\draw[dashed] (A)--(D)--(B);\n'
               '\\draw (%s:0.6) arc (%s:%s:0.6);\n'
               '\\node at (%s:1.15) {$%s^\\circ$};\n'
               '\\fill (A) circle (1.5pt) node[above] {$%s$};\n'
               '\\fill (B) circle (1.5pt) node[below] {$%s$};\n'
               '\\fill (C) circle (1.5pt) node[above] {$%s$};\n'
               '\\fill (D) circle (1.5pt) node[left] {$%s$};\n'
               '\\fill (M) circle (1.5pt) node[below] {$%s$};\n'
               '\\end{tikzpicture}\n'
               '\\end{center}\n' %(ang1, ang2, d_val, d_val, ang1, ang1, ang2, ang_lbl, alpha, A, B, C, D, M))
    noidungcauhoi = ('Cho ba lực $\\vec{F}_1 = \\overrightarrow{%s%s}$, $\\vec{F}_2 = \\overrightarrow{%s%s}$, $\\vec{F}_3 = \\overrightarrow{%s%s}$ cùng tác động vào một %s tại điểm $%s$ và %s đứng yên. Cho biết cường độ hai lực $\\vec{F}_1, \\vec{F}_2$ đều bằng $%s\\text{ N}$ và góc $\\widehat{%s%s%s} = %s^\\circ$. Khi đó tính cường độ $\\vec{F}_3$. \n'
                     %(M, A, M, B, M, C, vat, M, vat, latex(F), A, M, B, alpha)) + hinh_de
    if dang=='1':
        buoc_tinh = ('Do $\\widehat{%s%s%s} = 60^\\circ$ nên $\\Delta %s%s%s$ là tam giác đều nên $%s%s = 2\\cdot\\frac{%s\\sqrt{3}}{2} = %s\\text{ (N)}$. \\\\ \n'
                     %(A, M, B, M, A, B, M, D, latex(F), latex(kq)))
    elif dang=='2':
        buoc_tinh = ('Do $\\widehat{%s%s%s} = 90^\\circ$ nên hình bình hành $%s%s%s%s$ là hình vuông, suy ra $%s%s = %s\\sqrt{2} = %s\\text{ (N)}$. \\\\ \n'
                     %(A, M, B, A, M, B, D, M, D, latex(F), latex(kq)))
    else:
        buoc_tinh = ('Do $\\widehat{%s%s%s} = 120^\\circ$ và $%s%s%s%s$ là hình thoi nên $\\widehat{%s%s%s} = 60^\\circ$, suy ra $\\Delta %s%s%s$ là tam giác đều, do đó $%s%s = %s%s = %s\\text{ (N)}$. \\\\ \n'
                     %(A, M, B, A, M, B, D, A, M, D, M, A, D, M, D, M, A, latex(kq)))
    loigiai = (hinh_lg +
               'Ta có: $\\vec{F}_1 + \\vec{F}_2 = \\overrightarrow{%s%s} + \\overrightarrow{%s%s} = \\overrightarrow{%s%s}$ (với $%s$ là điểm sao cho $%s%s%s%s$ là hình bình hành). \\\\ \n'
               'Ta có: $%s%s = \\left|\\overrightarrow{%s%s}\\right| = \\left|\\vec{F}_1\\right| = %s\\text{ N}$ và $%s%s = \\left|\\overrightarrow{%s%s}\\right| = \\left|\\vec{F}_2\\right| = %s\\text{ N}$. \\\\ \n'
               %(M, A, M, B, M, D, D, A, M, B, D, M, A, M, A, latex(F), M, B, M, B, latex(F)) +
               buoc_tinh +
               'Do %s đứng yên nên cường độ lực tác dụng lên %s bằng $0$ hay $\\vec{F}_1 + \\vec{F}_2 + \\vec{F}_3 = \\vec{0}$. \\\\ \n'
               'Suy ra: $\\vec{F}_3 = -\\left(\\vec{F}_1 + \\vec{F}_2\\right) \\Rightarrow \\left|\\vec{F}_3\\right| = \\left|-\\left(\\vec{F}_1 + \\vec{F}_2\\right)\\right| = \\left|\\overrightarrow{%s%s}\\right| = %s%s = %s\\text{ (N)}$. \\\\ \n'
               'Vậy cường độ của $\\vec{F}_3$ là $%s\\text{ (N)}$. \n'
               %(vat, vat, D, M, M, D, latex(kq), latex(kq)))
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('- -', '+').replace('+ -', '-')
    return content

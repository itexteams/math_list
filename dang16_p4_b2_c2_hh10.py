
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


def bt_dang16_p4_b2_c2_hh10(self):
    lisdang=['1', '2']
    dang=random.choice(lisdang)
    bo_ten = random.choice([
        ('A','B','C','M','G','E','F'),
        ('A','B','C','I','G','D','E'),
        ('M','N','P','I','G','E','F'),
        ('D','E','F','M','G','P','Q')
    ])
    A, B, C, M, G, E, F = bo_ten
    P1 = random.choice([B, C])
    hinh_ve = ('\\begin{center}\n'
               '\\begin{tikzpicture}[scale=1.1, line width=1pt, line join=round, line cap=round]\n'
               '\\coordinate (B) at (0,0);\n'
               '\\coordinate (C) at (2,0);\n'
               '\\coordinate (M) at (1,0);\n'
               '\\coordinate (A) at (1,1.732);\n'
               '\\coordinate (G) at (1,0.577);\n'
               '\\coordinate (F) at (-1,1.732);\n'
               '\\coordinate (E) at (0,3.464);\n'
               '\\coordinate (O) at (0,1.732);\n'
               '\\draw (B)--(C)--(E)--(F)--cycle (A)--(B) (A)--(M) (A)--(F) (B)--(E);\n'
               '\\fill (A) circle (1.5pt) node[right] {$%s$};\n'
               '\\fill (B) circle (1.5pt) node[below] {$%s$};\n'
               '\\fill (C) circle (1.5pt) node[right] {$%s$};\n'
               '\\fill (M) circle (1.5pt) node[below] {$%s$};\n'
               '\\fill (G) circle (1.5pt) node[right] {$%s$};\n'
               '\\fill (E) circle (1.5pt) node[above] {$%s$};\n'
               '\\fill (F) circle (1.5pt) node[left] {$%s$};\n'
               '\\fill (O) circle (1.5pt);\n'
               '\\end{tikzpicture}\n'
               '\\end{center}\n' %(A, B, C, M, G, E, F))
    if dang=='1':
        a_sym = symbols('a', positive=True)
        k = random.choice([1, 2, 3, 4, 6])
        canh = k * a_sym
        AM_val = canh * sqrt(3) / 2
        kq1 = Rational(2, 3) * AM_val
        kq2 = 2 * AM_val
        noidungcauhoi = ('Cho tam giác $%s%s%s$ đều, cạnh $%s$. Gọi $%s$ là trung điểm của $%s%s$ và $%s$ là trọng tâm của tam giác $%s%s%s$. Tính $\\left|\\overrightarrow{%s%s} + \\overrightarrow{%s%s}\\right|$ và $\\left|\\overrightarrow{%s%s} - \\overrightarrow{%s%s}\\right|$ theo $a$. \n'
                         %(A, B, C, latex(canh), M, B, C, G, A, B, C, P1, G, A, P1, B, A, A, C))
        loigiai = (hinh_ve +
                   'Tính $\\left|\\overrightarrow{%s%s} + \\overrightarrow{%s%s}\\right|$ ta có: $\\overrightarrow{%s%s} + \\overrightarrow{%s%s} = \\overrightarrow{%s%s} - \\overrightarrow{%s%s} = \\overrightarrow{%s%s}$ \\\\ \n'
                   '$\\Rightarrow \\left|\\overrightarrow{%s%s} + \\overrightarrow{%s%s}\\right| = \\left|\\overrightarrow{%s%s}\\right| = \\frac{2}{3}%s%s = \\frac{2}{3}\\cdot %s = %s$. \\\\ \n'
                   'Tính $\\left|\\overrightarrow{%s%s} - \\overrightarrow{%s%s}\\right|$ ta vẽ hình bình hành $%s%s%s%s$. \\\\ \n'
                   '$\\overrightarrow{%s%s} - \\overrightarrow{%s%s} = \\overrightarrow{%s%s} + \\overrightarrow{%s%s} = \\overrightarrow{%s%s} + \\overrightarrow{%s%s} = \\overrightarrow{%s%s} \\Rightarrow \\left|\\overrightarrow{%s%s} - \\overrightarrow{%s%s}\\right| = \\left|\\overrightarrow{%s%s}\\right| = %s%s = 2%s%s = 2\\cdot %s = %s$. \n'
                   %(P1, G, A, P1, P1, G, A, P1, P1, G, P1, A, A, G,
                     P1, G, A, P1, A, G, A, M, latex(AM_val), latex(kq1),
                     B, A, A, C, B, A, E, F,
                     B, A, A, C, B, A, C, A, B, A, B, F, B, E, B, A, A, C, B, E, B, E, A, M, latex(AM_val), latex(kq2)))
    elif dang=='2':
        c = random.choice([2, 3, 4, 6, 8, 9, 12])
        AM_val = Rational(c, 2) * sqrt(3)
        kq1 = Rational(2, 3) * AM_val
        kq2 = 2 * AM_val
        noidungcauhoi = ('Cho tam giác $%s%s%s$ đều, cạnh bằng $%s$. Gọi $%s$ là trung điểm của $%s%s$ và $%s$ là trọng tâm của tam giác $%s%s%s$. Tính $\\left|\\overrightarrow{%s%s} + \\overrightarrow{%s%s}\\right|$ và $\\left|\\overrightarrow{%s%s} - \\overrightarrow{%s%s}\\right|$. \n'
                         %(A, B, C, latex(c), M, B, C, G, A, B, C, P1, G, A, P1, B, A, A, C))
        loigiai = (hinh_ve +
                   'Tính $\\left|\\overrightarrow{%s%s} + \\overrightarrow{%s%s}\\right|$ ta có: $\\overrightarrow{%s%s} + \\overrightarrow{%s%s} = \\overrightarrow{%s%s} - \\overrightarrow{%s%s} = \\overrightarrow{%s%s}$ \\\\ \n'
                   '$\\Rightarrow \\left|\\overrightarrow{%s%s} + \\overrightarrow{%s%s}\\right| = \\left|\\overrightarrow{%s%s}\\right| = \\frac{2}{3}%s%s = \\frac{2}{3}\\cdot %s = %s$. \\\\ \n'
                   'Tính $\\left|\\overrightarrow{%s%s} - \\overrightarrow{%s%s}\\right|$ ta vẽ hình bình hành $%s%s%s%s$. \\\\ \n'
                   '$\\overrightarrow{%s%s} - \\overrightarrow{%s%s} = \\overrightarrow{%s%s} + \\overrightarrow{%s%s} = \\overrightarrow{%s%s} + \\overrightarrow{%s%s} = \\overrightarrow{%s%s} \\Rightarrow \\left|\\overrightarrow{%s%s} - \\overrightarrow{%s%s}\\right| = \\left|\\overrightarrow{%s%s}\\right| = %s%s = 2%s%s = 2\\cdot %s = %s$. \n'
                   %(P1, G, A, P1, P1, G, A, P1, P1, G, P1, A, A, G,
                     P1, G, A, P1, A, G, A, M, latex(AM_val), latex(kq1),
                     B, A, A, C, B, A, E, F,
                     B, A, A, C, B, A, C, A, B, A, B, F, B, E, B, A, A, C, B, E, B, E, A, M, latex(AM_val), latex(kq2)))
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('- -', '+').replace('+ -', '-')
    return content

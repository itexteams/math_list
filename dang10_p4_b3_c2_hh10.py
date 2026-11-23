
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


def bt_dang10_p4_b3_c2_hh10(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        bo_ten = [
            ('A', 'B', 'C', 'I', 'M'),
            ('M', 'N', 'P', 'I', 'K'),
            ('D', 'E', 'F', 'I', 'M')
        ]
        A, B, C, I, M = random.choice(bo_ten)
        tamgiac = A + B + C
        a_sym = symbols('a', positive=True)
        k = randint(1, 4)
        goc = random.choice([30, 45, 60])
        AB_val = k * a_sym
        if goc == 30:
            tan_val = sqrt(3) / 3
            cos_val = sqrt(3) / 2
            yA, xC = 4.0, 2.31
        elif goc == 45:
            tan_val = Rational(1)
            cos_val = sqrt(2) / 2
            yA, xC = 3.2, 3.2
        else:
            tan_val = sqrt(3)
            cos_val = Rational(1, 2)
            yA, xC = 2.31, 4.0
        BC_val = simplify(AB_val * tan_val)
        AC_val = simplify(AB_val / cos_val)
        kieu_b = random.choice([1, 2])
        if kieu_b == 1:
            bieuthuc_b = f'\\left|\\overrightarrow{{{A}{B}}} + \\overrightarrow{{{A}{C}}}\\right|'
            canh_M = f'{B}{C}'
            dinh_M = A
            canh_goc_vuong = f'{A}{B}'
            doan_1 = AB_val
            doan_2 = simplify(BC_val / 2)
            kq_b = simplify(2 * sqrt(doan_1**2 + doan_2**2))
            mx, my = round(xC / 2, 2), 0.0
            pos_M = 'below'
        else:
            bieuthuc_b = f'\\left|\\overrightarrow{{{C}{B}}} + \\overrightarrow{{{C}{A}}}\\right|'
            canh_M = f'{A}{B}'
            dinh_M = C
            canh_goc_vuong = f'{B}{C}'
            doan_1 = BC_val
            doan_2 = simplify(AB_val / 2)
            kq_b = simplify(2 * sqrt(doan_1**2 + doan_2**2))
            mx, my = 0.0, round(yA / 2, 2)
            pos_M = 'left'
        ix, iy = round(xC / 2, 2), round(yA / 2, 2)
        hinhve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[line width=1pt, scale=1]\n'
            f'\\coordinate ({B}) at (0,0);\n'
            f'\\coordinate ({C}) at ({xC},0);\n'
            f'\\coordinate ({A}) at (0,{yA});\n'
            f'\\coordinate ({I}) at ({ix},{iy});\n'
            f'\\coordinate ({M}) at ({mx},{my});\n'
            f'\\draw ({A})--({B})--({C})--cycle;\n'
            '\\draw (0,0.25)--(0.25,0.25)--(0.25,0);\n'
            f'\\draw[-latex] ({B})--({I});\n'
            f'\\draw[-latex] ({dinh_M})--({M});\n'
            f'\\fill ({A}) circle (1.5pt) node[above] {{${A}$}};\n'
            f'\\fill ({B}) circle (1.5pt) node[below left] {{${B}$}};\n'
            f'\\fill ({C}) circle (1.5pt) node[right] {{${C}$}};\n'
            f'\\fill ({I}) circle (1.5pt) node[above right] {{${I}$}};\n'
            f'\\fill ({M}) circle (1.5pt) node[{pos_M}] {{${M}$}};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}\n'
        )
        noidungcauhoi = (
            f'Cho $\\triangle {tamgiac}$ vuông tại ${B}$ có ${A} = {goc}^\\circ$, ${A}{B} = {latex(AB_val)}$. Gọi ${I}$ là trung điểm của ${A}{C}$. Hãy tính: \\\\\n'
            f'a) $\\left|\\overrightarrow{{{B}{A}}} + \\overrightarrow{{{B}{C}}}\\right|$ \\\\\n'
            f'b) ${bieuthuc_b}$ \\\\\n'
        )
        loigiai = (
            hinhve +
            f'Ta có: ${B}{C} = {A}{B}\\tan {A} = {latex(AB_val)}\\tan {goc}^\\circ = {latex(BC_val)}$, ${A}{C} = \\dfrac{{{A}{B}}}{{\\cos {A}}} = \\dfrac{{{latex(AB_val)}}}{{\\cos {goc}^\\circ}} = {latex(AC_val)}$.\n'
            '\\begin{enumEX}[a)]{1}\n'
            f'\\item $\\left|\\overrightarrow{{{B}{A}}} + \\overrightarrow{{{B}{C}}}\\right| = \\left|2\\overrightarrow{{{B}{I}}}\\right| = 2\\left|\\overrightarrow{{{B}{I}}}\\right| = 2{B}{I} = 2\\cdot\\dfrac{{{A}{C}}}{{2}} = {A}{C} = {latex(AC_val)}$.\n'
            f'\\item Gọi ${M}$ là trung điểm của ${canh_M}$, ta có ${bieuthuc_b} = \\left|2\\overrightarrow{{{dinh_M}{M}}}\\right| = 2\\left|\\overrightarrow{{{dinh_M}{M}}}\\right| = 2{dinh_M}{M} = 2\\sqrt{{{canh_goc_vuong}^2 + {B}{M}^2}} = 2\\sqrt{{\\left({latex(doan_1)}\\right)^2 + \\left({latex(doan_2)}\\right)^2}} = {latex(kq_b)}$.\n'
            '\\end{enumEX}\n'
        )
        noidungcauhoi = noidungcauhoi.replace('- -', '+').replace('+ -', '-')
        loigiai = loigiai.replace('- -', '+').replace('+ -', '-')
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
    return content

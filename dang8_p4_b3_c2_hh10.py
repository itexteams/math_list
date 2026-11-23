
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


def bt_dang8_p4_b3_c2_hh10(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        bo_ten = [
            ('A', 'B', 'C', 'D', 'E', 'F'),
            ('M', 'N', 'P', 'Q', 'E', 'F'),
            ('A', 'B', 'C', 'D', 'M', 'N')
        ]
        A, B, C, D, E, F = random.choice(bo_ten)
        hinh_name = A + B + C + D
        while True:
            q = randint(2, 8)
            p = randint(1, q - 1)
            if math.gcd(p, q) == 1:
                break
        r_bc = Rational(p, q)
        r_bd = Rational(p, p + q)
        r_ab = Rational(q, p + q)
        k_val = Rational(p + q, q)
        c_hs = random.choice([q, 2 * q])
        d_const = randint(2024, 2030)
        kq = int(c_hs * k_val + d_const)
        ex = round(4.5 * p / q, 3)
        fx = round(5.7 * p / (p + q), 3)
        fy = round(2.5 * p / (p + q), 3)
        noidungcauhoi = f'Cho hình bình hành ${hinh_name}$. Gọi ${E}$ và ${F}$ là 2 điểm thỏa $\\overrightarrow{{{B}{E}}} = {latex(r_bc)}\\overrightarrow{{{B}{C}}}$, $\\overrightarrow{{{B}{F}}} = {latex(r_bd)}\\overrightarrow{{{B}{D}}}$. Khi đó $\\overrightarrow{{{A}{E}}} = k\\overrightarrow{{{A}{F}}}$. Tính ${c_hs}k + {d_const}$.\n'
        hinhve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[line width=1pt, scale=1]\n'
            f'\\coordinate ({B}) at (0,0);\n'
            f'\\coordinate ({C}) at (4.5,0);\n'
            f'\\coordinate ({A}) at (1.2,2.5);\n'
            f'\\coordinate ({D}) at (5.7,2.5);\n'
            f'\\coordinate ({E}) at ({ex},0);\n'
            f'\\coordinate ({F}) at ({fx},{fy});\n'
            f'\\draw ({A})--({B})--({C})--({D})--cycle;\n'
            f'\\draw ({B})--({D}) ({A})--({E});\n'
            f'\\fill ({A}) circle (1.5pt) node[above] {{${A}$}};\n'
            f'\\fill ({B}) circle (1.5pt) node[left] {{${B}$}};\n'
            f'\\fill ({C}) circle (1.5pt) node[right] {{${C}$}};\n'
            f'\\fill ({D}) circle (1.5pt) node[right] {{${D}$}};\n'
            f'\\fill ({E}) circle (1.5pt) node[below] {{${E}$}};\n'
            f'\\fill ({F}) circle (1.5pt) node[below right] {{${F}$}};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}\n'
        )
        loigiai = (
            hinhve +
            f'Ta phân tích $\\overrightarrow{{{A}{E}}}$ và $\\overrightarrow{{{A}{F}}}$ theo 2 vectơ $\\overrightarrow{{{A}{B}}}$ và $\\overrightarrow{{{A}{D}}}$.\\\\\n'
            f'$\\overrightarrow{{{A}{E}}} = \\overrightarrow{{{A}{B}}} + \\overrightarrow{{{B}{E}}} = \\overrightarrow{{{A}{B}}} + {latex(r_bc)}\\overrightarrow{{{B}{C}}} = \\overrightarrow{{{A}{B}}} + {latex(r_bc)}\\overrightarrow{{{A}{D}}}$;\\\\\n'
            f'$\\overrightarrow{{{A}{F}}} = \\overrightarrow{{{A}{B}}} + \\overrightarrow{{{B}{F}}} = \\overrightarrow{{{A}{B}}} + {latex(r_bd)}\\left(\\overrightarrow{{{A}{D}}} - \\overrightarrow{{{A}{B}}}\\right) = {latex(r_ab)}\\overrightarrow{{{A}{B}}} + {latex(r_bd)}\\overrightarrow{{{A}{D}}}$.\\\\\n'
            f'Xét hệ: $\\begin{{cases}} \\overrightarrow{{{A}{E}}} = \\overrightarrow{{{A}{B}}} + {latex(r_bc)}\\overrightarrow{{{A}{D}}} \\\\ \\overrightarrow{{{A}{F}}} = {latex(r_ab)}\\overrightarrow{{{A}{B}}} + {latex(r_bd)}\\overrightarrow{{{A}{D}}} \\end{{cases}} \\Leftrightarrow \\begin{{cases}} \\overrightarrow{{{A}{E}}} = \\overrightarrow{{{A}{B}}} + {latex(r_bc)}\\overrightarrow{{{A}{D}}} \\\\ {latex(k_val)}\\overrightarrow{{{A}{F}}} = \\overrightarrow{{{A}{B}}} + {latex(r_bc)}\\overrightarrow{{{A}{D}}} \\end{{cases}} \\Rightarrow \\overrightarrow{{{A}{E}}} = {latex(k_val)}\\overrightarrow{{{A}{F}}} \\Rightarrow k = {latex(k_val)}$.\\\\\n'
            f'Khi đó: ${c_hs}k + {d_const} = {kq}$.\n'
        )
        noidungcauhoi = noidungcauhoi.replace('- -', '+').replace('+ -', '-')
        loigiai = loigiai.replace('- -', '+').replace('+ -', '-')
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
    return content

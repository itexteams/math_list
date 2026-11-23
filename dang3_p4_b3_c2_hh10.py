
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


def bt_dang3_p4_b3_c2_hh10(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        bo_ten = [
            ('A', 'B', 'C', 'D', 'O', 'M'),
            ('M', 'N', 'P', 'Q', 'O', 'I'),
            ('E', 'F', 'G', 'H', 'O', 'K'),
            ('A', 'B', 'C', 'D', 'I', 'N')
        ]
        A, B, C, D, O, M = random.choice(bo_ten)
        hinh_name = A + B + C + D
        canh_options = [
            (A, B, D, C),
            (B, C, A, D),
            (C, D, B, A),
            (D, A, C, B)
        ]
        X, Y, X_doi, Y_doi = random.choice(canh_options)
        cau_a_list = [
            (f'2\\overrightarrow{{{A}{O}}}', f'Vì ${O}$ là trung điểm của ${A}{C}$ nên $2\\overrightarrow{{{A}{O}}} = \\overrightarrow{{{A}{C}}}$.'),
            (f'2\\overrightarrow{{{C}{O}}}', f'Vì ${O}$ là trung điểm của ${A}{C}$ nên $2\\overrightarrow{{{C}{O}}} = \\overrightarrow{{{C}{A}}}$.'),
            (f'-2\\overrightarrow{{{A}{O}}}', f'Vì ${O}$ là trung điểm của ${A}{C}$ nên $-2\\overrightarrow{{{A}{O}}} = 2\\overrightarrow{{{O}{A}}} = \\overrightarrow{{{C}{A}}}$.'),
            (f'2\\overrightarrow{{{B}{O}}}', f'Vì ${O}$ là trung điểm của ${B}{D}$ nên $2\\overrightarrow{{{B}{O}}} = \\overrightarrow{{{B}{D}}}$.')
        ]
        cau_b_list = [
            (f'-\\dfrac{{1}}{{2}}\\overrightarrow{{{D}{B}}}', f'Vì ${O}$ là trung điểm của ${B}{D}$ nên $-\\dfrac{{1}}{{2}}\\overrightarrow{{{D}{B}}} = \\dfrac{{1}}{{2}}\\overrightarrow{{{B}{D}}} = \\overrightarrow{{{B}{O}}} = \\overrightarrow{{{O}{D}}}$.'),
            (f'-\\dfrac{{1}}{{2}}\\overrightarrow{{{B}{D}}}', f'Vì ${O}$ là trung điểm của ${B}{D}$ nên $-\\dfrac{{1}}{{2}}\\overrightarrow{{{B}{D}}} = \\dfrac{{1}}{{2}}\\overrightarrow{{{D}{B}}} = \\overrightarrow{{{D}{O}}} = \\overrightarrow{{{O}{B}}}$.'),
            (f'-\\dfrac{{1}}{{2}}\\overrightarrow{{{C}{A}}}', f'Vì ${O}$ là trung điểm của ${A}{C}$ nên $-\\dfrac{{1}}{{2}}\\overrightarrow{{{C}{A}}} = \\dfrac{{1}}{{2}}\\overrightarrow{{{A}{C}}} = \\overrightarrow{{{A}{O}}} = \\overrightarrow{{{O}{C}}}$.'),
            (f'\\dfrac{{1}}{{2}}\\overrightarrow{{{D}{B}}}', f'Vì ${O}$ là trung điểm của ${B}{D}$ nên $\\dfrac{{1}}{{2}}\\overrightarrow{{{D}{B}}} = \\overrightarrow{{{D}{O}}} = \\overrightarrow{{{O}{B}}}$.')
        ]
        cau_c_list = [
            (f'2\\overrightarrow{{{X}{M}}}', f'Vì ${M}$ là trung điểm của ${X}{Y}$ và ${hinh_name}$ là hình bình hành nên $2\\overrightarrow{{{X}{M}}} = \\overrightarrow{{{X}{Y}}} = \\overrightarrow{{{X_doi}{Y_doi}}}$.'),
            (f'2\\overrightarrow{{{Y}{M}}}', f'Vì ${M}$ là trung điểm của ${X}{Y}$ và ${hinh_name}$ là hình bình hành nên $2\\overrightarrow{{{Y}{M}}} = \\overrightarrow{{{Y}{X}}} = \\overrightarrow{{{Y_doi}{X_doi}}}$.'),
            (f'-2\\overrightarrow{{{X}{M}}}', f'Vì ${M}$ là trung điểm của ${X}{Y}$ và ${hinh_name}$ là hình bình hành nên $-2\\overrightarrow{{{X}{M}}} = 2\\overrightarrow{{{M}{X}}} = \\overrightarrow{{{Y}{X}}} = \\overrightarrow{{{Y_doi}{X_doi}}}$.')
        ]
        cau_d_list = [
            (f'\\dfrac{{1}}{{2}}\\overrightarrow{{{Y}{X}}}', f'Vì ${M}$ là trung điểm của ${X}{Y}$ nên $\\dfrac{{1}}{{2}}\\overrightarrow{{{Y}{X}}} = \\overrightarrow{{{Y}{M}}} = \\overrightarrow{{{M}{X}}}$.'),
            (f'\\dfrac{{1}}{{2}}\\overrightarrow{{{X}{Y}}}', f'Vì ${M}$ là trung điểm của ${X}{Y}$ nên $\\dfrac{{1}}{{2}}\\overrightarrow{{{X}{Y}}} = \\overrightarrow{{{X}{M}}} = \\overrightarrow{{{M}{Y}}}$.'),
            (f'-\\dfrac{{1}}{{2}}\\overrightarrow{{{X}{Y}}}', f'Vì ${M}$ là trung điểm của ${X}{Y}$ nên $-\\dfrac{{1}}{{2}}\\overrightarrow{{{X}{Y}}} = \\dfrac{{1}}{{2}}\\overrightarrow{{{Y}{X}}} = \\overrightarrow{{{Y}{M}}} = \\overrightarrow{{{M}{X}}}$.')
        ]
        qa, la = random.choice(cau_a_list)
        qb, lb = random.choice(cau_b_list)
        qc, lc = random.choice(cau_c_list)
        qd, ld = random.choice(cau_d_list)
        hinhve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[line width=1pt, scale=1]\n'
            '\\coordinate (D) at (0,0);\n'
            '\\coordinate (C) at (4,0);\n'
            '\\coordinate (A) at (1,2);\n'
            '\\coordinate (B) at (5,2);\n'
            '\\coordinate (O) at (2.5,1);\n'
            '\\draw (A)--(B)--(C)--(D)--cycle;\n'
            '\\draw (A)--(C) (B)--(D);\n'
            f'\\fill (A) circle (1.5pt) node[above left] {{${A}$}};\n'
            f'\\fill (B) circle (1.5pt) node[above right] {{${B}$}};\n'
            f'\\fill (C) circle (1.5pt) node[below right] {{${C}$}};\n'
            f'\\fill (D) circle (1.5pt) node[below left] {{${D}$}};\n'
            f'\\fill (O) circle (1.5pt) node[below] {{${O}$}};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}\n'
        )
        noidungcauhoi = (
            f'Cho hình bình hành ${hinh_name}$. Gọi ${O}$ là giao điểm của ${A}{C}, {B}{D}$ và ${M}$ là trung điểm của ${X}{Y}$. Tìm vectơ trong các trường hợp sau:\n'
            + hinhve +
            f'a) ${qa}$ \\\\\n'
            f'b) ${qb}$ \\\\\n'
            f'c) ${qc}$ \\\\\n'
            f'd) ${qd}$ \\\\\n'
        )
        loigiai = (
            '\\begin{enumEX}[a)]{1}\n'
            f'\\item {la}\n'
            f'\\item {lb}\n'
            f'\\item {lc}\n'
            f'\\item {ld}\n'
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

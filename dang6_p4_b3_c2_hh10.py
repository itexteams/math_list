
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


def bt_dang6_p4_b3_c2_hh10(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        bo_ten = [
            ('A', 'B', 'C', "A'", "B'", "C'", 'G', "G'"),
            ('M', 'N', 'P', "M'", "N'", "P'", 'G_1', 'G_2'),
            ('A', 'B', 'C', 'D', 'E', 'F', 'G', "G'"),
            ('P', 'Q', 'R', "P'", "Q'", "R'", 'I', 'J')
        ]
        A, B, C, A1, B1, C1, G, G1 = random.choice(bo_ten)
        tg1 = A + B + C
        tg2 = A1 + B1 + C1
        X, Y, Z = random.sample([A1, B1, C1], 3)
        m = randint(1, 4)
        hm = '' if m == 1 else str(m)
        dau = random.choice([1, -1])
        if dau == 1:
            vec_G = f'\\overrightarrow{{{G}{G1}}}'
            k_val = 3 * m
        else:
            vec_G = f'\\overrightarrow{{{G1}{G}}}'
            k_val = -3 * m
        vp_de = f'{hm}\\overrightarrow{{{A}{X}}} + {hm}\\overrightarrow{{{B}{Y}}} + {hm}\\overrightarrow{{{C}{Z}}}'
        noidungcauhoi = f'Nếu ${G}$ và ${G1}$ lần lượt là trọng tâm tam giác ${tg1}$ và ${tg2}$ thì $k{vec_G} = {vp_de}$. Tìm giá trị của $k$.\n'
        buoc1 = f'Ta có: $\\overrightarrow{{{A}{X}}} + \\overrightarrow{{{B}{Y}}} + \\overrightarrow{{{C}{Z}}} = \\overrightarrow{{{A}{G}}} + \\overrightarrow{{{G}{G1}}} + \\overrightarrow{{{G1}{X}}} + \\overrightarrow{{{B}{G}}} + \\overrightarrow{{{G}{G1}}} + \\overrightarrow{{{G1}{Y}}} + \\overrightarrow{{{C}{G}}} + \\overrightarrow{{{G}{G1}}} + \\overrightarrow{{{G1}{Z}}}$\\\\\n'
        buoc2 = f'$= 3\\overrightarrow{{{G}{G1}}} + \\left(\\overrightarrow{{{A}{G}}} + \\overrightarrow{{{B}{G}}} + \\overrightarrow{{{C}{G}}}\\right) + \\left(\\overrightarrow{{{G1}{X}}} + \\overrightarrow{{{G1}{Y}}} + \\overrightarrow{{{G1}{Z}}}\\right) = 3\\overrightarrow{{{G}{G1}}} + \\vec{{0}} + \\vec{{0}} = 3\\overrightarrow{{{G}{G1}}}$.'
        if m == 1 and dau == 1:
            ketluan = f' Suy ra $k = {k_val}$.\n'
        elif m == 1 and dau == -1:
            ketluan = f'\\\\\nSuy ra $\\overrightarrow{{{A}{X}}} + \\overrightarrow{{{B}{Y}}} + \\overrightarrow{{{C}{Z}}} = {k_val}{vec_G}$, do đó $k = {k_val}$.\n'
        elif m > 1 and dau == 1:
            ketluan = f'\\\\\nSuy ra ${vp_de} = {k_val}{vec_G}$, do đó $k = {k_val}$.\n'
        else:
            ketluan = f'\\\\\nSuy ra ${vp_de} = {3*m}\\overrightarrow{{{G}{G1}}} = {k_val}{vec_G}$, do đó $k = {k_val}$.\n'
        loigiai = buoc1 + buoc2 + ketluan
        noidungcauhoi = noidungcauhoi.replace('- -', '+').replace('+ -', '-')
        loigiai = loigiai.replace('- -', '+').replace('+ -', '-')
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
    return content


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


def bt_dang5_p4_b3_c2_hh10(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        bo_ten = [
            ('A', 'B', 'K', 'O'),
            ('M', 'N', 'I', 'O'),
            ('P', 'Q', 'K', 'O'),
            ('C', 'D', 'E', 'O')
        ]
        A, B, K, O = random.choice(bo_ten)
        while True:
            a = randint(1, 6)
            b = randint(1, 6)
            if math.gcd(a, b) == 1 and (a + b) > 2:
                break
        S = a + b
        ha = '' if a == 1 else str(a)
        hb = '' if b == 1 else str(b)
        fa = latex(Rational(a, S))
        fb = latex(Rational(b, S))
        f_ba = latex(Rational(-b, a))
        bt_chen = f'\\left(\\overrightarrow{{{K}{A}}} + \\overrightarrow{{{A}{B}}}\\right)'
        bt_b_chen = f'{hb}{bt_chen}' if b > 1 else f'\\overrightarrow{{{K}{A}}} + \\overrightarrow{{{A}{B}}}'
        vp_a = f'-\\overrightarrow{{{A}{B}}}' if b == 1 else f'-{b}\\overrightarrow{{{A}{B}}}'
        noidungcauhoi = (
            f'Cho hai điểm phân biệt ${A}$ và ${B}$. \\\\\n'
            f'a) Hãy xác định điểm ${K}$ sao cho ${ha}\\overrightarrow{{{K}{A}}} + {hb}\\overrightarrow{{{K}{B}}} = \\vec{{0}}$. \\\\\n'
            f'b) Chứng minh rằng với mọi điểm ${O}$ ta luôn có $\\overrightarrow{{{O}{K}}} = {fa}\\overrightarrow{{{O}{A}}} + {fb}\\overrightarrow{{{O}{B}}}$. \\\\\n'
        )
        loigiai = (
            '\\begin{enumEX}[a)]{1}\n'
            f'\\item ${ha}\\overrightarrow{{{K}{A}}} + {hb}\\overrightarrow{{{K}{B}}} = \\vec{{0}} \\Leftrightarrow {ha}\\overrightarrow{{{K}{A}}} + {bt_b_chen} = \\vec{{0}} \\Leftrightarrow {S}\\overrightarrow{{{K}{A}}} = {vp_a} \\Leftrightarrow \\overrightarrow{{{A}{K}}} = {fb}\\overrightarrow{{{A}{B}}}$.\n'
            f'\\item Ta có: ${ha}\\overrightarrow{{{K}{A}}} + {hb}\\overrightarrow{{{K}{B}}} = \\vec{{0}} \\Leftrightarrow \\overrightarrow{{{K}{A}}} = {f_ba}\\overrightarrow{{{K}{B}}}$.\\\\\n'
            f'${fa}\\overrightarrow{{{O}{A}}} + {fb}\\overrightarrow{{{O}{B}}} = {fa}\\left(\\overrightarrow{{{O}{K}}} + \\overrightarrow{{{K}{A}}}\\right) + {fb}\\left(\\overrightarrow{{{O}{K}}} + \\overrightarrow{{{K}{B}}}\\right) = \\overrightarrow{{{O}{K}}} + {fa}\\overrightarrow{{{K}{A}}} + {fb}\\overrightarrow{{{K}{B}}} = \\overrightarrow{{{O}{K}}} + {fa}\\left({f_ba}\\overrightarrow{{{K}{B}}}\\right) + {fb}\\overrightarrow{{{K}{B}}} = \\overrightarrow{{{O}{K}}}$.\n'
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


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


def bt_dang19_p4_b3_c2_hh10(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        bo_ten = [
            ('A', 'B', 'C', 'D', 'I', 'J'),
            ('M', 'N', 'P', 'Q', 'I', 'J'),
            ('E', 'F', 'G', 'H', 'M', 'N'),
            ('A', 'B', 'C', 'D', 'M', 'N')
        ]
        A, B, C, D, I, J = random.choice(bo_ten)
        tugiac = A + B + C + D
        m = randint(1, 4)
        hm = '' if m == 1 else str(m)
        kieu = random.choice([1, 2, 3, 4])
        if kieu == 1:
            p1, q1, p2, q2 = A, B, C, D
            dau = 1
            k_val = 2 * m
        elif kieu == 2:
            p1, q1, p2, q2 = A, D, C, B
            dau = 1
            k_val = 2 * m
        elif kieu == 3:
            p1, q1, p2, q2 = B, A, D, C
            dau = -1
            k_val = -2 * m
        else:
            p1, q1, p2, q2 = D, A, B, C
            dau = -1
            k_val = -2 * m
        noidungcauhoi = f'Cho tứ giác ${tugiac}$. Gọi ${I}, {J}$ lần lượt là trung điểm của hai đường chéo ${A}{C}$ và ${B}{D}$. Biết rằng biểu thức ${hm}\\overrightarrow{{{p1}{q1}}} + {hm}\\overrightarrow{{{p2}{q2}}} = k\\overrightarrow{{{I}{J}}}$. Tìm giá trị của $k$.\n'
        hinhve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[line width=1pt, scale=1]\n'
            f'\\coordinate ({D}) at (0,0);\n'
            f'\\coordinate ({C}) at (4.5,0);\n'
            f'\\coordinate ({A}) at (1.3,2.8);\n'
            f'\\coordinate ({B}) at (3.8,2.1);\n'
            f'\\coordinate ({I}) at (2.9,1.4);\n'
            f'\\coordinate ({J}) at (1.9,1.05);\n'
            f'\\draw ({A})--({B})--({C})--({D})--cycle;\n'
            f'\\draw ({A})--({C}) ({B})--({D});\n'
            f'\\draw[-latex] ({I})--({J});\n'
            f'\\fill ({A}) circle (1.5pt) node[above] {{${A}$}};\n'
            f'\\fill ({B}) circle (1.5pt) node[right] {{${B}$}};\n'
            f'\\fill ({C}) circle (1.5pt) node[right] {{${C}$}};\n'
            f'\\fill ({D}) circle (1.5pt) node[left] {{${D}$}};\n'
            f'\\fill ({I}) circle (1.5pt) node[above right] {{${I}$}};\n'
            f'\\fill ({J}) circle (1.5pt) node[above left] {{${J}$}};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}\n'
        )
        if dau == 1:
            he_pt = f'\\begin{{cases}} \\overrightarrow{{{I}{J}}} = \\overrightarrow{{{I}{p1}}} + \\overrightarrow{{{p1}{q1}}} + \\overrightarrow{{{q1}{J}}} & (1) \\\\ \\overrightarrow{{{I}{J}}} = \\overrightarrow{{{I}{p2}}} + \\overrightarrow{{{p2}{q2}}} + \\overrightarrow{{{q2}{J}}} & (2) \\end{{cases}}'
            cong_ve = f'$2\\overrightarrow{{{I}{J}}} = \\left(\\overrightarrow{{{I}{p1}}} + \\overrightarrow{{{I}{p2}}}\\right) + \\left(\\overrightarrow{{{p1}{q1}}} + \\overrightarrow{{{p2}{q2}}}\\right) + \\left(\\overrightarrow{{{q1}{J}}} + \\overrightarrow{{{q2}{J}}}\\right) \\Leftrightarrow 2\\overrightarrow{{{I}{J}}} = \\vec{{0}} + \\overrightarrow{{{p1}{q1}}} + \\overrightarrow{{{p2}{q2}}} + \\vec{{0}} = \\overrightarrow{{{p1}{q1}}} + \\overrightarrow{{{p2}{q2}}}$.'
            if m == 1:
                suyra = f'Suy ra $k = {k_val}$.'
            else:
                suyra = f'Nhân hai vế với ${m}$ ta được ${hm}\\overrightarrow{{{p1}{q1}}} + {hm}\\overrightarrow{{{p2}{q2}}} = {k_val}\\overrightarrow{{{I}{J}}}$. Suy ra $k = {k_val}$.'
        else:
            he_pt = f'\\begin{{cases}} \\overrightarrow{{{J}{I}}} = \\overrightarrow{{{J}{p1}}} + \\overrightarrow{{{p1}{q1}}} + \\overrightarrow{{{q1}{I}}} & (1) \\\\ \\overrightarrow{{{J}{I}}} = \\overrightarrow{{{J}{p2}}} + \\overrightarrow{{{p2}{q2}}} + \\overrightarrow{{{q2}{I}}} & (2) \\end{{cases}}'
            cong_ve = f'$2\\overrightarrow{{{J}{I}}} = \\left(\\overrightarrow{{{J}{p1}}} + \\overrightarrow{{{J}{p2}}}\\right) + \\left(\\overrightarrow{{{p1}{q1}}} + \\overrightarrow{{{p2}{q2}}}\\right) + \\left(\\overrightarrow{{{q1}{I}}} + \\overrightarrow{{{q2}{I}}}\\right) \\Leftrightarrow 2\\overrightarrow{{{J}{I}}} = \\vec{{0}} + \\overrightarrow{{{p1}{q1}}} + \\overrightarrow{{{p2}{q2}}} + \\vec{{0}} = \\overrightarrow{{{p1}{q1}}} + \\overrightarrow{{{p2}{q2}}}$.'
            if m == 1:
                suyra = f'Do $\\overrightarrow{{{J}{I}}} = -\\overrightarrow{{{I}{J}}}$ nên $\\overrightarrow{{{p1}{q1}}} + \\overrightarrow{{{p2}{q2}}} = -2\\overrightarrow{{{I}{J}}}$. Suy ra $k = {k_val}$.'
            else:
                suyra = f'Do $\\overrightarrow{{{J}{I}}} = -\\overrightarrow{{{I}{J}}}$ nên $\\overrightarrow{{{p1}{q1}}} + \\overrightarrow{{{p2}{q2}}} = -2\\overrightarrow{{{I}{J}}} \\Rightarrow {hm}\\overrightarrow{{{p1}{q1}}} + {hm}\\overrightarrow{{{p2}{q2}}} = {k_val}\\overrightarrow{{{I}{J}}}$. Suy ra $k = {k_val}$.'
        loigiai = (
            hinhve +
            f'Ta có ${he_pt}$.\\\\\n'
            'Cộng theo vế $(1)$ và $(2)$ ta được:\\\\\n'
            + cong_ve + '\\\\\n'
            + suyra + '\n'
        )
        noidungcauhoi = noidungcauhoi.replace('- -', '+').replace('+ -', '-')
        loigiai = loigiai.replace('- -', '+').replace('+ -', '-')
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
    return content

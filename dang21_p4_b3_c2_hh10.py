
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


def bt_dang21_p4_b3_c2_hh10(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        bo_ten = [
            ('A', 'B', 'C', 'D', 'E'),
            ('A', 'B', 'C', 'M', 'N'),
            ('M', 'N', 'P', 'E', 'F')
        ]
        A, B, C, D, E = random.choice(bo_ten)
        tamgiac = A + B + C
        k = random.choice([1, 1, 2, 3])
        while True:
            p = randint(1, 6)
            q = randint(1, 6)
            if math.gcd(p, q) == 1:
                break
        hp = '' if p == 1 else str(p)
        hq = '' if q == 1 else str(q)
        if k == 1:
            gt_D = f'đối xứng với ${A}$ qua ${B}$'
            dx, dy = -1.2, -2.0
        else:
            gt_D = f'thỏa mãn $\\overrightarrow{{{B}{D}}} = {k}\\overrightarrow{{{A}{B}}}$'
            dx, dy = -1.5, -2.5
        m_val = -(k + 1)
        n_val = Rational(q, p + q)
        t_ratio = q / (p + q)
        ex = round(1.2 + t_ratio * 2.8, 2)
        ey = round(2.0 - t_ratio * 2.0, 2)
        kieu_hoi = random.choice([1, 2, 3])
        if kieu_hoi == 1:
            bt_hoi = 'm\\cdot n'
            kq = m_val * n_val
        elif kieu_hoi == 2:
            bt_hoi = 'm + n'
            kq = m_val + n_val
        else:
            bt_hoi = 'm - n'
            kq = m_val - n_val
        noidungcauhoi = f'Cho tam giác ${tamgiac}$. Lấy điểm ${D}$ {gt_D} và lấy điểm ${E}$ trên đoạn ${A}{C}$ sao cho ${hp}{A}{E} = {hq}{E}{C}$. Nếu $\\overrightarrow{{{D}{E}}} = m\\overrightarrow{{{A}{B}}} + n\\overrightarrow{{{A}{C}}}$ thì tính giá trị ${bt_hoi}$.\n'
        hinhve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[line width=1pt, scale=1]\n'
            f'\\coordinate ({B}) at (0,0);\n'
            f'\\coordinate ({C}) at (4,0);\n'
            f'\\coordinate ({A}) at (1.2,2);\n'
            f'\\coordinate ({D}) at ({dx},{dy});\n'
            f'\\coordinate ({E}) at ({ex},{ey});\n'
            f'\\draw ({A})--({B})--({C})--cycle;\n'
            f'\\draw ({B})--({D}) ({D})--({E});\n'
            f'\\fill ({A}) circle (1.5pt) node[above] {{${A}$}};\n'
            f'\\fill ({B}) circle (1.5pt) node[left] {{${B}$}};\n'
            f'\\fill ({C}) circle (1.5pt) node[right] {{${C}$}};\n'
            f'\\fill ({D}) circle (1.5pt) node[left] {{${D}$}};\n'
            f'\\fill ({E}) circle (1.5pt) node[above right] {{${E}$}};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}\n'
        )
        loigiai = (
            hinhve +
            f'Ta có $\\overrightarrow{{{D}{E}}} = \\overrightarrow{{{D}{A}}} + \\overrightarrow{{{A}{E}}} = {m_val}\\overrightarrow{{{A}{B}}} + {latex(n_val)}\\overrightarrow{{{A}{C}}} \\Rightarrow m = {m_val}, n = {latex(n_val)} \\Rightarrow {bt_hoi} = {latex(kq)}$.\n'
        )
        noidungcauhoi = noidungcauhoi.replace('- -', '+').replace('+ -', '-')
        loigiai = loigiai.replace('- -', '+').replace('+ -', '-')
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
    return content

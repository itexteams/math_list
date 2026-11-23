
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


def bt_dang11_p4_b3_c2_hh10(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        bo_ten = [
            ('A', 'B', 'C', 'K', 'M', 'I'),
            ('D', 'E', 'F', 'K', 'M', 'I'),
            ('M', 'N', 'P', 'K', 'E', 'I'),
            ('P', 'Q', 'R', 'K', 'M', 'I')
        ]
        A, B, C, K, M, I = random.choice(bo_ten)
        tamgiac = A + B + C
        ds_dinh = [A, B, C]
        a1, a2, a3 = random.sample(ds_dinh, 3)
        if random.choice([True, False]):
            vt_a = f'\\overrightarrow{{{K}{a1}}} + 2\\overrightarrow{{{K}{a2}}}'
        else:
            vt_a = f'2\\overrightarrow{{{K}{a2}}} + \\overrightarrow{{{K}{a1}}}'
        vp_a = f'\\overrightarrow{{{a3}{a2}}}'
        b1, b2, b3 = random.sample(ds_dinh, 3)
        k = random.choice([1, 2, 3])
        hs1 = '' if k == 1 else str(k)
        hs2 = str(2 * k)
        vt_b = f'{hs1}\\overrightarrow{{{M}{b1}}} + {hs1}\\overrightarrow{{{M}{b2}}} + {hs2}\\overrightarrow{{{M}{b3}}}'
        coords = {A: (1.5, 3.0), B: (0.0, 0.0), C: (5.0, 0.0)}
        ix = round((coords[b1][0] + coords[b2][0]) / 2, 2)
        iy = round((coords[b1][1] + coords[b2][1]) / 2, 2)
        mx = round((ix + coords[b3][0]) / 2, 2)
        my = round((iy + coords[b3][1]) / 2, 2)
        kx = round((coords[A][0] + coords[B][0] + coords[C][0]) / 3, 2)
        ky = round((coords[A][1] + coords[B][1] + coords[C][1]) / 3, 2)
        pos_I_map = {C: 'left', B: 'above right', A: 'below'}
        pos_I = pos_I_map[b3]
        hinhve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[line width=1pt, scale=1]\n'
            f'\\coordinate ({A}) at (1.5,3);\n'
            f'\\coordinate ({B}) at (0,0);\n'
            f'\\coordinate ({C}) at (5,0);\n'
            f'\\coordinate ({I}) at ({ix},{iy});\n'
            f'\\coordinate ({K}) at ({kx},{ky});\n'
            f'\\coordinate ({M}) at ({mx},{my});\n'
            f'\\draw ({A})--({B})--({C})--cycle;\n'
            f'\\draw ({I})--({b3});\n'
            f'\\draw[-latex] ({K})--({a1});\n'
            f'\\draw[-latex] ({K})--({a2});\n'
            f'\\fill ({A}) circle (1.5pt) node[above] {{${A}$}};\n'
            f'\\fill ({B}) circle (1.5pt) node[left] {{${B}$}};\n'
            f'\\fill ({C}) circle (1.5pt) node[right] {{${C}$}};\n'
            f'\\fill ({I}) circle (1.5pt) node[{pos_I}] {{${I}$}};\n'
            f'\\fill ({K}) circle (1.5pt) node[above right] {{${K}$}};\n'
            f'\\fill ({M}) circle (1.5pt) node[below right] {{${M}$}};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}\n'
        )
        noidungcauhoi = (
            f'Cho tam giác ${tamgiac}$. \\\\\n'
            f'a) Tìm điểm ${K}$ sao cho ${vt_a} = {vp_a}$ \\\\\n'
            f'b) Tìm điểm ${M}$ sao cho ${vt_b} = \\vec{{0}}$ \\\\\n'
        )
        loigiai = (
            hinhve +
            '\\begin{enumEX}[a)]{1}\n'
            f'\\item Ta có: ${vt_a} = {vp_a} \\Leftrightarrow {vt_a} = \\overrightarrow{{{K}{a2}}} - \\overrightarrow{{{K}{a3}}} \\Leftrightarrow \\overrightarrow{{{K}{A}}} + \\overrightarrow{{{K}{B}}} + \\overrightarrow{{{K}{C}}} = \\vec{{0}}$.\\\\\n'
            f'$\\Rightarrow {K}$ là trọng tâm của tam giác ${tamgiac}$.\n'
            f'\\item Gọi ${I}$ là trung điểm của ${b1}{b2}$.\\\\\n'
            f'Ta có: ${vt_b} = \\vec{{0}} \\Leftrightarrow {hs2}\\overrightarrow{{{M}{I}}} + {hs2}\\overrightarrow{{{M}{b3}}} = \\vec{{0}} \\Leftrightarrow \\overrightarrow{{{M}{I}}} + \\overrightarrow{{{M}{b3}}} = \\vec{{0}} \\Rightarrow {M}$ là trung điểm của ${I}{b3}$.\n'
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

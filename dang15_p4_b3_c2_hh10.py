
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


def bt_dang15_p4_b3_c2_hh10(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        bo_ten = [
            ('A', 'B', 'C', 'M', 'I'),
            ('D', 'E', 'F', 'M', 'I'),
            ('M', 'N', 'P', 'K', 'I'),
            ('P', 'Q', 'R', 'M', 'I')
        ]
        A, B, C, M, I = random.choice(bo_ten)
        tamgiac = A + B + C
        X, Y, Z = random.sample([A, B, C], 3)
        ds_pq = [(1, 1), (2, 1), (1, 2), (3, 1), (1, 3), (3, 2), (2, 3)]
        p, q = random.choice(ds_pq)
        hp = '' if p == 1 else str(p)
        hq = '' if q == 1 else str(q)
        if p == 1 and q == 1:
            gt_I = f'Gọi ${I}$ là trung điểm ${X}{M}$.'
        else:
            gt_I = f'Lấy điểm ${I}$ trên đoạn ${X}{M}$ sao cho ${hp}{I}{X} = {hq}{I}{M}$.'
        g = math.gcd(2 * p, q)
        cX = (2 * p) // g
        cYZ = q // g
        cM = 2 * cYZ
        hcX = '' if cX == 1 else str(cX)
        hcYZ = '' if cYZ == 1 else str(cYZ)
        hcM = '' if cM == 1 else str(cM)
        t_ratio = q / (p + q)
        ix = round(1.8 + t_ratio * (2.25 - 1.8), 3)
        iy = round(3.2 + t_ratio * (0.3 - 3.2), 3)
        hinhve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[line width=1pt, scale=1]\n'
            f'\\coordinate ({Y}) at (0,0);\n'
            f'\\coordinate ({Z}) at (4.5,0.6);\n'
            f'\\coordinate ({X}) at (1.8,3.2);\n'
            f'\\coordinate ({M}) at (2.25,0.3);\n'
            f'\\coordinate ({I}) at ({ix},{iy});\n'
            f'\\draw ({X})--({Y})--({Z})--cycle;\n'
            f'\\draw ({X})--({M}) ({I})--({Y}) ({I})--({Z});\n'
            f'\\fill ({X}) circle (1.5pt) node[above] {{${X}$}};\n'
            f'\\fill ({Y}) circle (1.5pt) node[left] {{${Y}$}};\n'
            f'\\fill ({Z}) circle (1.5pt) node[right] {{${Z}$}};\n'
            f'\\fill ({M}) circle (1.5pt) node[below] {{${M}$}};\n'
            f'\\fill ({I}) circle (1.5pt) node[left] {{${I}$}};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}\n'
        )
        vt_de = f'{hcX}\\overrightarrow{{{I}{X}}} + {hcYZ}\\overrightarrow{{{I}{Y}}} + {hcYZ}\\overrightarrow{{{I}{Z}}}'
        bt_nhom = f'{hcX}\\overrightarrow{{{I}{X}}} + {hcYZ}\\left(\\overrightarrow{{{I}{Y}}} + \\overrightarrow{{{I}{Z}}}\\right)'
        bt_im = f'{hcX}\\overrightarrow{{{I}{X}}} + {hcM}\\overrightarrow{{{I}{M}}}'
        g_im = math.gcd(cX, cM)
        if g_im == 1:
            ket_cuoi = '\\vec{0}'
        else:
            ket_cuoi = f'{g_im}\\left({hp}\\overrightarrow{{{I}{X}}} + {hq}\\overrightarrow{{{I}{M}}}\\right) = \\vec{{0}}'
        noidungcauhoi = f'Cho tam giác ${tamgiac}$ có trung tuyến ${X}{M}$. {gt_I} Chứng minh rằng ${vt_de} = \\vec{{0}}$.\n'
        loigiai = (
            hinhve +
            f'Ta có: ${vt_de} = {bt_nhom} = {bt_im} = {ket_cuoi}$.\n'
        )
        noidungcauhoi = noidungcauhoi.replace('- -', '+').replace('+ -', '-')
        loigiai = loigiai.replace('- -', '+').replace('+ -', '-')
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
    return content

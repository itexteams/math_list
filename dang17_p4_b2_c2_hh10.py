
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


def bt_dang17_p4_b2_c2_hh10(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        bo_dinh = random.choice([('A', 'B', 'C'), ('D', 'E', 'F'), ('X', 'Y', 'Z')])
        bo_td = random.choice([('M', 'N', 'P'), ('I', 'J', 'K')])
        pA, pB, pC = bo_dinh
        pM, pN, pP = bo_td
        pO = random.choice(['O', 'S', 'H'])
        chieu = random.choice(['xuoi', 'nguoc'])
        if chieu == 'xuoi':
            ht_a = f'\\overrightarrow{{{pB}{pM}}} + \\overrightarrow{{{pC}{pN}}} + \\overrightarrow{{{pA}{pP}}} = \\vec{{0}}'
            v1, v1_thay, v2, v2_thay, v3, v_tong = f'{pB}{pM}', f'{pP}{pN}', f'{pC}{pN}', f'{pN}{pA}', f'{pA}{pP}', f'{pP}{pA}'
            dau_b = '-'
            nhom_b = f'\\overrightarrow{{{pB}{pM}}} + \\overrightarrow{{{pC}{pN}}} + \\overrightarrow{{{pA}{pP}}}'
        else:
            ht_a = f'\\overrightarrow{{{pM}{pB}}} + \\overrightarrow{{{pN}{pC}}} + \\overrightarrow{{{pP}{pA}}} = \\vec{{0}}'
            v1, v1_thay, v2, v2_thay, v3, v_tong = f'{pM}{pB}', f'{pN}{pP}', f'{pN}{pC}', f'{pA}{pN}', f'{pP}{pA}', f'{pA}{pP}'
            dau_b = '+'
            nhom_b = f'\\overrightarrow{{{pM}{pB}}} + \\overrightarrow{{{pN}{pC}}} + \\overrightarrow{{{pP}{pA}}}'
        noidungcauhoi = ('Cho tam giác $%s%s%s$. Gọi $%s, %s, %s$ lần lượt là trung điểm của các cạnh $%s%s, %s%s, %s%s$. Chứng minh rằng: \\\\ \n'
                         'a) $%s$. \\\\ \n'
                         'b) $\\overrightarrow{%s%s} + \\overrightarrow{%s%s} + \\overrightarrow{%s%s} = \\overrightarrow{%s%s} + \\overrightarrow{%s%s} + \\overrightarrow{%s%s}$, với $%s$ là điểm bất kì. \n'
                         %(pA, pB, pC, pM, pN, pP, pB, pC, pC, pA, pA, pB, ht_a,
                           pO, pA, pO, pB, pO, pC, pO, pM, pO, pN, pO, pP, pO))
        loigiai = ('\\begin{center} \n'
                   '\\begin{tikzpicture}[line width=1pt, scale=0.8] \n'
                   '\\coordinate (B) at (0,0); \n'
                   '\\coordinate (C) at (5,0); \n'
                   '\\coordinate (A) at (1.6,3.4); \n'
                   '\\coordinate (M) at (2.5,0); \n'
                   '\\coordinate (N) at (3.3,1.7); \n'
                   '\\coordinate (P) at (0.8,1.7); \n'
                   '\\draw (A) -- (B) -- (C) -- cycle; \n'
                   '\\draw (M) -- (N) -- (P) -- cycle; \n'
                   '\\fill (A) circle (1.5pt) node[above] {$%s$}; \n'
                   '\\fill (B) circle (1.5pt) node[left] {$%s$}; \n'
                   '\\fill (C) circle (1.5pt) node[right] {$%s$}; \n'
                   '\\fill (M) circle (1.5pt) node[below] {$%s$}; \n'
                   '\\fill (N) circle (1.5pt) node[right] {$%s$}; \n'
                   '\\fill (P) circle (1.5pt) node[left] {$%s$}; \n'
                   '\\end{tikzpicture} \n'
                   '\\end{center} \n'
                   '\\begin{enumEX}[a)]{1} \n'
                   '\\item Vì $%s%s, %s%s$ là đường trung bình của tam giác $%s%s%s$ nên $%s%s \\parallel %s%s, %s%s \\parallel %s%s$ suy ra tứ giác $%s%s%s%s$ là hình bình hành $\\Rightarrow \\overrightarrow{%s} = \\overrightarrow{%s}$ và $%s$ là trung điểm của $%s%s \\Rightarrow \\overrightarrow{%s} = \\overrightarrow{%s}$. \\\\ \n'
                   'Do đó theo quy tắc ba điểm ta có: $\\overrightarrow{%s} + \\overrightarrow{%s} + \\overrightarrow{%s} = \\left(\\overrightarrow{%s} + \\overrightarrow{%s}\\right) + \\overrightarrow{%s} = \\overrightarrow{%s} + \\overrightarrow{%s} = \\vec{0}$. \n'
                   '\\item Theo quy tắc ba điểm ta có: \\\\ \n'
                   '$\\overrightarrow{%s%s} + \\overrightarrow{%s%s} + \\overrightarrow{%s%s} = \\left(\\overrightarrow{%s%s} + \\overrightarrow{%s%s}\\right) + \\left(\\overrightarrow{%s%s} + \\overrightarrow{%s%s}\\right) + \\left(\\overrightarrow{%s%s} + \\overrightarrow{%s%s}\\right) = \\left(\\overrightarrow{%s%s} + \\overrightarrow{%s%s} + \\overrightarrow{%s%s}\\right) + \\overrightarrow{%s%s} + \\overrightarrow{%s%s} + \\overrightarrow{%s%s}$ \\\\ \n'
                   '$= \\left(\\overrightarrow{%s%s} + \\overrightarrow{%s%s} + \\overrightarrow{%s%s}\\right) %s \\left(%s\\right)$. \\\\ \n'
                   'Theo câu a) $%s$ ta suy ra $\\overrightarrow{%s%s} + \\overrightarrow{%s%s} + \\overrightarrow{%s%s} = \\overrightarrow{%s%s} + \\overrightarrow{%s%s} + \\overrightarrow{%s%s}$. \n'
                   '\\end{enumEX} \n'
                   %(pA, pB, pC, pM, pN, pP,
                     pP, pN, pM, pN, pA, pB, pC, pP, pN, pB, pM, pM, pN, pB, pP, pB, pM, pN, pP, v1, v1_thay, pN, pA, pC, v2, v2_thay,
                     v1, v2, v3, v1_thay if chieu == 'xuoi' else v2_thay, v2_thay if chieu == 'xuoi' else v1_thay, v3, v_tong, v3,
                     pO, pA, pO, pB, pO, pC, pO, pP, pP, pA, pO, pM, pM, pB, pO, pN, pN, pC, pO, pM, pO, pN, pO, pP, pP, pA, pM, pB, pN, pC,
                     pO, pM, pO, pN, pO, pP, dau_b, nhom_b,
                     ht_a, pO, pA, pO, pB, pO, pC, pO, pM, pO, pN, pO, pP))
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
    return content

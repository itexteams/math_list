
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


def bt_dang25_p4_b1_c2_hh10(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        bo_dinh = random.choice([('A', 'B', 'C', 'D'), ('E', 'F', 'G', 'H')])
        bo_td = random.choice([('M', 'N', 'P', 'Q'), ('I', 'J', 'K', 'L')])
        pA, pB, pC, pD = bo_dinh
        pM, pN, pP, pQ = bo_td
        kieu = random.choice(['MN_QP', 'NM_PQ', 'MQ_NP', 'QM_PN'])
        if kieu in ['MN_QP', 'NM_PQ']:
            duong_cheo = f'{pA}{pC}'
            ve_cheo = '\\draw (A) -- (C);'
            d1, d2 = f'{pM}{pN}', f'{pP}{pQ}'
            if kieu == 'MN_QP':
                dt_vec = f'\\overrightarrow{{{pM}{pN}}} = \\overrightarrow{{{pQ}{pP}}}'
            else:
                dt_vec = f'\\overrightarrow{{{pN}{pM}}} = \\overrightarrow{{{pP}{pQ}}}'
        else:
            duong_cheo = f'{pB}{pD}'
            ve_cheo = '\\draw (B) -- (D);'
            d1, d2 = f'{pM}{pQ}', f'{pN}{pP}'
            if kieu == 'MQ_NP':
                dt_vec = f'\\overrightarrow{{{pM}{pQ}}} = \\overrightarrow{{{pN}{pP}}}'
            else:
                dt_vec = f'\\overrightarrow{{{pQ}{pM}}} = \\overrightarrow{{{pP}{pN}}}'
        noidungcauhoi = ('Cho tứ giác $%s%s%s%s$. Gọi $%s, %s, %s, %s$ lần lượt là trung điểm của $%s%s, %s%s, %s%s, %s%s$. Chứng minh $%s$. \n'
                         %(pA, pB, pC, pD, pM, pN, pP, pQ, pA, pB, pB, pC, pC, pD, pD, pA, dt_vec))
        loigiai = ('\\begin{center} \n'
                   '\\begin{tikzpicture}[line width=1pt, scale=0.8] \n'
                   '\\coordinate (A) at (0,0); \n'
                   '\\coordinate (B) at (1.8,1.8); \n'
                   '\\coordinate (C) at (5,0); \n'
                   '\\coordinate (D) at (1.6,-1.6); \n'
                   '\\coordinate (M) at (0.9,0.9); \n'
                   '\\coordinate (N) at (3.4,0.9); \n'
                   '\\coordinate (P) at (3.3,-0.8); \n'
                   '\\coordinate (Q) at (0.8,-0.8); \n'
                   '\\draw (A) -- (B) -- (C) -- (D) -- cycle; \n'
                   '%s \n'
                   '\\draw (M) -- (N) -- (P) -- (Q) -- cycle; \n'
                   '\\fill (A) circle (1.5pt) node[left] {$%s$}; \n'
                   '\\fill (B) circle (1.5pt) node[above] {$%s$}; \n'
                   '\\fill (C) circle (1.5pt) node[right] {$%s$}; \n'
                   '\\fill (D) circle (1.5pt) node[below] {$%s$}; \n'
                   '\\fill (M) circle (1.5pt) node[above left] {$%s$}; \n'
                   '\\fill (N) circle (1.5pt) node[above right] {$%s$}; \n'
                   '\\fill (P) circle (1.5pt) node[below right] {$%s$}; \n'
                   '\\fill (Q) circle (1.5pt) node[below left] {$%s$}; \n'
                   '\\end{tikzpicture} \n'
                   '\\end{center} \n'
                   'Ta có $\\begin{cases} %s \\parallel %s \\\\ %s = \\dfrac{1}{2}%s \\end{cases}$; $\\begin{cases} %s \\parallel %s \\\\ %s = \\dfrac{1}{2}%s \\end{cases} \\Rightarrow \\begin{cases} %s \\parallel %s \\\\ %s = %s \\end{cases} \\Rightarrow %s$. \\\\ \n'
                   'Vậy $%s$. \n'
                   %(ve_cheo, pA, pB, pC, pD, pM, pN, pP, pQ,
                     d1, duong_cheo, d1, duong_cheo, d2, duong_cheo, d2, duong_cheo,
                     d1, d2, d1, d2, dt_vec, dt_vec))
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
    return content

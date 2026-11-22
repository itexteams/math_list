
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


def bt_dang10_p4_b2_c2_hh10(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        bo_dinh = random.choice([('A', 'B', 'C', 'D'), ('E', 'F', 'G', 'H'), ('P', 'Q', 'R', 'S')])
        bo_td = random.choice([('M', 'N'), ('I', 'J'), ('K', 'L')])
        pA, pB, pC, pD = bo_dinh
        pM, pN = bo_td
        kieu_a = random.choice(['1', '2'])
        if kieu_a == '1':
            va1, va2, va_thay, va_kq = f'{pN}{pC}', f'{pM}{pC}', f'{pA}{pN}', f'{pA}{pC}'
        else:
            va1, va2, va_thay, va_kq = f'{pM}{pA}', f'{pN}{pA}', f'{pC}{pM}', f'{pC}{pA}'
        kieu_b = random.choice(['1', '2'])
        if kieu_b == '1':
            vb1, vb2, vb_thay, vb_kq = f'{pA}{pM}', f'{pC}{pD}', f'{pB}{pA}', f'{pB}{pM}'
        else:
            vb1, vb2, vb_thay, vb_kq = f'{pC}{pN}', f'{pA}{pB}', f'{pD}{pC}', f'{pD}{pN}'
        noidungcauhoi = ('Cho hình bình hành $%s%s%s%s$ với $%s$ và $%s$ lần lượt là trung điểm của $%s%s$ và $%s%s$. Tìm tổng của hai vectơ: \\\\ \n'
                         'a) $\\overrightarrow{%s}$ và $\\overrightarrow{%s}$. \\\\ \n'
                         'b) $\\overrightarrow{%s}$ và $\\overrightarrow{%s}$. \n'
                         %(pA, pB, pC, pD, pM, pN, pB, pC, pA, pD, va1, va2, vb1, vb2))
        loigiai = ('\\begin{center} \n'
                   '\\begin{tikzpicture}[line width=1pt, scale=0.8] \n'
                   '\\coordinate (B) at (0,0); \n'
                   '\\coordinate (C) at (4.5,0); \n'
                   '\\coordinate (A) at (1.5,2.5); \n'
                   '\\coordinate (D) at (6,2.5); \n'
                   '\\coordinate (M) at (2.25,0); \n'
                   '\\coordinate (N) at (3.75,2.5); \n'
                   '\\draw (A) -- (B) -- (C) -- (D) -- cycle; \n'
                   '\\draw (A) -- (M) (N) -- (C); \n'
                   '\\fill (A) circle (1.5pt) node[above] {$%s$}; \n'
                   '\\fill (B) circle (1.5pt) node[below] {$%s$}; \n'
                   '\\fill (C) circle (1.5pt) node[below] {$%s$}; \n'
                   '\\fill (D) circle (1.5pt) node[right] {$%s$}; \n'
                   '\\fill (M) circle (1.5pt) node[below] {$%s$}; \n'
                   '\\fill (N) circle (1.5pt) node[above] {$%s$}; \n'
                   '\\end{tikzpicture} \n'
                   '\\end{center} \n'
                   '\\begin{enumEX}[a)]{1} \n'
                   '\\item Vì $\\overrightarrow{%s} = \\overrightarrow{%s}$ nên ta có $\\overrightarrow{%s} + \\overrightarrow{%s} = \\overrightarrow{%s} + \\overrightarrow{%s} = \\overrightarrow{%s} + \\overrightarrow{%s} = \\overrightarrow{%s}$. \n'
                   '\\item Vì $\\overrightarrow{%s} = \\overrightarrow{%s}$ nên ta có $\\overrightarrow{%s} + \\overrightarrow{%s} = \\overrightarrow{%s} + \\overrightarrow{%s} = \\overrightarrow{%s} + \\overrightarrow{%s} = \\overrightarrow{%s}$. \n'
                   '\\end{enumEX} \n'
                   %(pA, pB, pC, pD, pM, pN,
                     va2, va_thay, va1, va2, va1, va_thay, va_thay, va1, va_kq,
                     vb2, vb_thay, vb1, vb2, vb1, vb_thay, vb_thay, vb1, vb_kq))
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
    return content

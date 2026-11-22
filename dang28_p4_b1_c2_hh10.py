
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


def bt_dang28_p4_b1_c2_hh10(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        bo_dinh = random.choice([('A', 'B', 'C'), ('M', 'N', 'P'), ('D', 'E', 'F')])
        bo_td = random.choice([('I', 'J'), ('H', 'K'), ('U', 'V')])
        pA, pB, pC = bo_dinh
        pI, pJ = bo_td
        pBp = pB + "'"
        chieu_a = random.choice(['xuoi', 'nguoc'])
        if chieu_a == 'xuoi':
            va1, va2 = f'{pB}{pI}', f'{pI}{pC}'
        else:
            va1, va2 = f'{pI}{pB}', f'{pC}{pI}'
        chieu_b = random.choice(['xuoi', 'nguoc'])
        if chieu_b == 'xuoi':
            vb1, vb2 = f'{pB}{pJ}', f'{pI}G'
        else:
            vb1, vb2 = f'{pJ}{pB}', f'G{pI}'
        noidungcauhoi = ('Cho tam giác $%s%s%s$ có trọng tâm $G$. Gọi $%s$ là trung điểm của $%s%s$. Dựng điểm $%s$ sao cho $\\overrightarrow{%s%s} = \\overrightarrow{%sG}$. \\\\ \n'
                         'a) Chứng minh rằng $\\overrightarrow{%s} = \\overrightarrow{%s}$. \\\\ \n'
                         'b) Gọi $%s$ là trung điểm của $%s%s$. Chứng minh rằng $\\overrightarrow{%s} = \\overrightarrow{%s}$. \n'
                         %(pA, pB, pC, pI, pB, pC, pBp, pBp, pB, pA, va1, va2, pJ, pB, pBp, vb1, vb2))
        loigiai = ('\\begin{center} \n'
                   '\\begin{tikzpicture}[line width=1pt, scale=0.8] \n'
                   '\\coordinate (B) at (0,0); \n'
                   '\\coordinate (C) at (5,0); \n'
                   '\\coordinate (A) at (1,3.6); \n'
                   '\\coordinate (I) at (2.5,0); \n'
                   '\\coordinate (G) at (2,1.2); \n'
                   '\\coordinate (Bp) at (-1,2.4); \n'
                   '\\coordinate (J) at (-0.5,1.2); \n'
                   '\\draw (A) -- (B) -- (C) -- cycle; \n'
                   '\\draw (A) -- (I) (B) -- (Bp); \n'
                   '\\fill (A) circle (1.5pt) node[above] {$%s$}; \n'
                   '\\fill (B) circle (1.5pt) node[left] {$%s$}; \n'
                   '\\fill (C) circle (1.5pt) node[right] {$%s$}; \n'
                   '\\fill (I) circle (1.5pt) node[below] {$%s$}; \n'
                   '\\fill (G) circle (1.5pt) node[right] {$G$}; \n'
                   '\\fill (Bp) circle (1.5pt) node[above] {$%s$}; \n'
                   '\\fill (J) circle (1.5pt) node[left] {$%s$}; \n'
                   '\\end{tikzpicture} \n'
                   '\\end{center} \n'
                   '\\begin{enumEX}[a)]{1} \n'
                   '\\item Vì $%s$ là trung điểm của $%s%s$ nên $%s%s = %s%s$ và $\\overrightarrow{%s}$ cùng hướng với $\\overrightarrow{%s}$ do đó $\\overrightarrow{%s} = \\overrightarrow{%s}$. \n'
                   '\\item Ta có $\\overrightarrow{%s%s} = \\overrightarrow{%sG}$ suy ra $%s%s = %sG$ và $%s%s \\parallel %sG$ nên $\\overrightarrow{%s}, \\overrightarrow{%s}$ cùng hướng (1). \\\\ \n'
                   'Vì $G$ là trọng tâm tam giác $%s%s%s$ nên $%sG = \\dfrac{1}{2}%sG$, $%s$ là trung điểm $%s%s$ suy ra $%s%s = \\dfrac{1}{2}%s%s$. \\\\ \n'
                   'Vì vậy $%s%s = %sG$ (2). \\\\ \n'
                   'Từ (1) và (2) ta có $\\overrightarrow{%s} = \\overrightarrow{%s}$. \n'
                   '\\end{enumEX} \n'
                   %(pA, pB, pC, pI, pBp, pJ,
                     pI, pB, pC, pB, pI, pC, pI, va1, va2, va1, va2,
                     pBp, pB, pA, pBp, pB, pA, pB, pBp, pA, vb1, vb2,
                     pA, pB, pC, pI, pA, pJ, pB, pBp, pB, pJ, pB, pBp,
                     pB, pJ, pI, vb1, vb2))
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
    return content

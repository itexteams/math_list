
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


def bt_dang27_p4_b1_c2_hh10(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        bo_dinh = random.choice([('A', 'B', 'C', 'D', 'E', 'F'), ('P', 'Q', 'R', 'S', 'T', 'U')])
        bo_td = random.choice([('M', 'N', 'I', 'K'), ('H', 'J', 'X', 'Y')])
        pA, pB, pC, pD, pE, pF = bo_dinh
        pM, pN, pI, pK = bo_td
        dt_a = random.choice([f'\\overrightarrow{{{pA}{pB}}} = \\overrightarrow{{{pN}{pM}}}', f'\\overrightarrow{{{pB}{pA}}} = \\overrightarrow{{{pM}{pN}}}'])
        dt_b = random.choice([f'\\overrightarrow{{{pM}{pK}}} = \\overrightarrow{{{pN}{pI}}}', f'\\overrightarrow{{{pK}{pM}}} = \\overrightarrow{{{pI}{pN}}}'])
        noidungcauhoi = ('Cho tam giác $%s%s%s$. Vẽ $%s$ đối xứng với $%s$ qua $%s$, $%s$ đối xứng với $%s$ qua $%s$ và $%s$ đối xứng với $%s$ qua $%s$. Gọi $G$ là giao điểm của trung tuyến $%s%s$ của tam giác $%s%s%s$ với trung tuyến $%s%s$ của tam giác $%s%s%s$. Gọi $%s, %s$ lần lượt là trung điểm của $G%s$ và $G%s$. Chứng minh rằng: \\\\ \n'
                         'a) $%s$. \\\\ \n'
                         'b) $%s$. \n'
                         %(pA, pB, pC, pD, pA, pB, pE, pB, pC, pF, pC, pA, pA, pM, pA, pB, pC, pD, pN, pD, pE, pF, pI, pK, pA, pD, dt_a, dt_b))
        loigiai = ('\\begin{center} \n'
                   '\\begin{tikzpicture}[line width=1pt, scale=0.8] \n'
                   '\\coordinate (A) at (0,2); \n'
                   '\\coordinate (B) at (1.4,0.4); \n'
                   '\\coordinate (C) at (-1.4,-0.4); \n'
                   '\\coordinate (M) at (0,0); \n'
                   '\\coordinate (D) at (2.8,-1.2); \n'
                   '\\coordinate (E) at (-4.2,-1.2); \n'
                   '\\coordinate (F) at (1.4,4.4); \n'
                   '\\coordinate (N) at (-1.4,1.6); \n'
                   '\\coordinate (G) at (0,0.667); \n'
                   '\\coordinate (I) at (0,1.333); \n'
                   '\\coordinate (K) at (1.4,-0.267); \n'
                   '\\draw (D) -- (E) -- (F) -- cycle; \n'
                   '\\draw (A) -- (D) (B) -- (E) (C) -- (F); \n'
                   '\\draw (A) -- (M) (D) -- (N) (A) -- (N); \n'
                   '\\draw (N) -- (I) -- (K) -- (M) -- cycle; \n'
                   '\\fill (A) circle (1.5pt) node[above left] {$%s$}; \n'
                   '\\fill (B) circle (1.5pt) node[above right] {$%s$}; \n'
                   '\\fill (C) circle (1.5pt) node[left] {$%s$}; \n'
                   '\\fill (D) circle (1.5pt) node[below right] {$%s$}; \n'
                   '\\fill (E) circle (1.5pt) node[below left] {$%s$}; \n'
                   '\\fill (F) circle (1.5pt) node[above right] {$%s$}; \n'
                   '\\fill (M) circle (1.5pt) node[below] {$%s$}; \n'
                   '\\fill (N) circle (1.5pt) node[left] {$%s$}; \n'
                   '\\fill (G) circle (1.5pt) node[above right] {$G$}; \n'
                   '\\fill (I) circle (1.5pt) node[right] {$%s$}; \n'
                   '\\fill (K) circle (1.5pt) node[below] {$%s$}; \n'
                   '\\end{tikzpicture} \n'
                   '\\end{center} \n'
                   '\\begin{enumEX}[a)]{1} \n'
                   '\\item Ta có $%s%s$ là đường trung bình của tam giác $%s%s%s$ nên $%s%s \\parallel %s%s \\Rightarrow %s%s \\parallel %s%s$. \\\\ \n'
                   '$%s%s = \\dfrac{1}{2}%s%s$; $%s%s = \\dfrac{1}{2}%s%s = \\dfrac{1}{2}%s%s \\Rightarrow %s%s = %s%s$. \\\\ \n'
                   'Suy ra tứ giác $%s%s%s%s$ là hình bình hành $\\Rightarrow %s$. \n'
                   '\\item Vì $%s, %s$ lần lượt là trung điểm của $G%s$ và $G%s$ nên $\\overrightarrow{%s%s} = \\dfrac{1}{2}\\overrightarrow{%s%s} = \\overrightarrow{%s%s} = \\overrightarrow{%s%s}$. \\\\ \n'
                   'Do đó tứ giác $%s%s%s%s$ là hình bình hành $\\Rightarrow %s$. \n'
                   '\\end{enumEX} \n'
                   %(pA, pB, pC, pD, pE, pF, pM, pN, pI, pK,
                     pA, pN, pF, pC, pE, pA, pN, pC, pE, pA, pN, pM, pB,
                     pA, pN, pC, pE, pM, pB, pC, pB, pC, pE, pA, pN, pM, pB,
                     pA, pN, pM, pB, dt_a,
                     pI, pK, pA, pD, pI, pK, pA, pD, pA, pB, pN, pM,
                     pI, pN, pM, pK, dt_b))
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
    return content

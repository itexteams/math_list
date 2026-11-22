
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


def bt_dang20_p4_b1_c2_hh10(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        bo_dinh = random.choice([('A', 'B', 'C', 'D'), ('E', 'F', 'G', 'H')])
        bo_phu = random.choice([('M', 'N', 'P'), ('I', 'J', 'K')])
        pA, pB, pC, pD = bo_dinh
        pM, pN, pP = bo_phu
        c = randint(2, 12)
        n = random.choice([2, 3, 4])
        am = Rational(c, n)
        pm = c + am
        mn2 = c**2 + pm**2
        mn = sqrt(mn2)
        xM = round(3.0 / n, 2)
        if n == 2:
            gt_M = f'${pM}$ là trung điểm của ${pA}{pB}$'
        else:
            gt_M = f'${pM}$ thuộc cạnh ${pA}{pB}$ sao cho ${pA}{pB} = {n}{pA}{pM}$'
        noidungcauhoi = ('Cho hình vuông $%s%s%s%s$ tâm $O$ cạnh bằng $%s$. Gọi %s, $%s$ là điểm đối xứng với $%s$ qua $%s$. Hãy tính độ dài của vectơ $\\overrightarrow{%s%s}$. \n'
                         %(pA, pB, pC, pD, latex(c), gt_M, pN, pC, pD, pM, pN))
        loigiai = ('\\begin{center} \n'
                   '\\begin{tikzpicture}[line width=1pt, scale=0.8] \n'
                   '\\coordinate (A) at (0,0); \n'
                   '\\coordinate (B) at (3,0); \n'
                   '\\coordinate (C) at (3,3); \n'
                   '\\coordinate (D) at (0,3); \n'
                   '\\coordinate (O) at (1.5,1.5); \n'
                   '\\coordinate (M) at (%s,0); \n'
                   '\\coordinate (N) at (-3,3); \n'
                   '\\coordinate (P) at (-3,0); \n'
                   '\\draw (P) -- (B) -- (C) -- (N) -- cycle; \n'
                   '\\draw (A) -- (D) (A) -- (C) (B) -- (D) (N) -- (M); \n'
                   '\\fill (A) circle (1.5pt) node[below] {$%s$}; \n'
                   '\\fill (B) circle (1.5pt) node[below] {$%s$}; \n'
                   '\\fill (C) circle (1.5pt) node[above right] {$%s$}; \n'
                   '\\fill (D) circle (1.5pt) node[above] {$%s$}; \n'
                   '\\fill (O) circle (1.5pt) node[below=4pt] {$O$}; \n'
                   '\\fill (M) circle (1.5pt) node[below] {$%s$}; \n'
                   '\\fill (N) circle (1.5pt) node[above left] {$%s$}; \n'
                   '\\fill (P) circle (1.5pt) node[below] {$%s$}; \n'
                   '\\end{tikzpicture} \n'
                   '\\end{center} \n'
                   'Qua $%s$ kẻ đường thẳng song song với $%s%s$ cắt đường thẳng $%s%s$ tại $%s$. \\\\ \n'
                   'Khi đó tứ giác $%s%s%s%s$ là hình vuông nên $%s%s = %s%s = %s$ và $%s%s = %s%s + %s%s = %s + %s = %s$. \\\\ \n'
                   'Áp dụng định lý Pytago trong tam giác vuông $%s%s%s$ ta có: \\\\ \n'
                   '$%s%s^2 = %s%s^2 + %s%s^2 = %s^2 + \\left(%s\\right)^2 = %s \\Rightarrow %s%s = %s$. \\\\ \n'
                   'Suy ra $\\left|\\overrightarrow{%s%s}\\right| = %s%s = %s$. \n'
                   %(xM, pA, pB, pC, pD, pM, pN, pP,
                     pN, pA, pD, pA, pB, pP,
                     pA, pD, pN, pP, pN, pP, pP, pA, latex(c), pP, pM, pP, pA, pA, pM, latex(c), latex(am), latex(pm),
                     pN, pP, pM,
                     pM, pN, pN, pP, pP, pM, latex(c), latex(pm), latex(mn2), pM, pN, latex(mn),
                     pM, pN, pM, pN, latex(mn)))
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
    return content

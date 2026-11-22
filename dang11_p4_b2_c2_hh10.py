
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


def bt_dang11_p4_b2_c2_hh10(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        bo_dinh = random.choice([('A','B','C','D'), ('M','N','P','Q'), ('E','F','G','H'), ('A','D','C','B')])
        if bo_dinh == ('A','D','C','B'):
            bo_dinh = ('A','B','C','D')
        p0, p1, p2, p3 = bo_dinh
        O = random.choice([t for t in ['O', 'I', 'K'] if t not in bo_dinh])
        hoan_vi = [
            (p0, p1, p2, p3), (p1, p2, p3, p0), (p2, p3, p0, p1), (p3, p0, p1, p2),
            (p0, p3, p2, p1), (p3, p2, p1, p0), (p2, p1, p0, p3), (p1, p0, p3, p2)
        ]
        X1, Y1, Z1, T1 = random.choice(hoan_vi)
        X2, Y2, Z2, T2 = random.choice(hoan_vi)
        noidungcauhoi = ('Cho hình thoi $%s%s%s%s$, gọi $%s$ là giao điểm của hai đường chéo. Chứng minh rằng: \\\\ \n'
                         'a) $\\overrightarrow{%s%s} - \\overrightarrow{%s%s} = \\overrightarrow{%s%s}$ \\\\ \n'
                         'b) $\\overrightarrow{%s%s} - \\overrightarrow{%s%s} = \\overrightarrow{%s%s}$ \\\\ \n'
                         %(p0, p1, p2, p3, O,
                           O, Y1, T1, X1, X1, O,
                           X2, Y2, Y2, Z2, T2, Y2))
        loigiai = ('\\begin{center}\n'
                   '\\begin{tikzpicture}[scale=0.8, line width=1pt, line join=round, line cap=round]\n'
                   '\\coordinate (A) at (-3,0);\n'
                   '\\coordinate (B) at (0,-1.5);\n'
                   '\\coordinate (C) at (3,0);\n'
                   '\\coordinate (D) at (0,1.5);\n'
                   '\\coordinate (O) at (0,0);\n'
                   '\\draw (A)--(B)--(C)--(D)--cycle (A)--(C) (B)--(D);\n'
                   '\\fill (A) circle (1.5pt) node[left] {$%s$};\n'
                   '\\fill (B) circle (1.5pt) node[below] {$%s$};\n'
                   '\\fill (C) circle (1.5pt) node[right] {$%s$};\n'
                   '\\fill (D) circle (1.5pt) node[above] {$%s$};\n'
                   '\\fill (O) circle (1.5pt) node[above right] {$%s$};\n'
                   '\\end{tikzpicture}\n'
                   '\\end{center}\n'
                   '\\begin{enumEX}[a)]{1} \n'
                   '\\item $\\overrightarrow{%s%s} - \\overrightarrow{%s%s} = \\overrightarrow{%s%s} - \\overrightarrow{%s%s} = \\overrightarrow{%s%s}$. \n'
                   '\\item $\\overrightarrow{%s%s} - \\overrightarrow{%s%s} = \\overrightarrow{%s%s} - \\overrightarrow{%s%s} = \\overrightarrow{%s%s}$. \n'
                   '\\end{enumEX} \n'
                   %(p0, p1, p2, p3, O,
                     O, Y1, T1, X1, T1, O, T1, X1, X1, O,
                     X2, Y2, Y2, Z2, X2, Y2, X2, T2, T2, Y2))
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('- -', '+').replace('+ -', '-')
    return content


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


def bt_dang13_p4_b2_c2_hh10(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        bo_ten = random.choice([
            ('A','B','C','M','N','P'),
            ('A','B','C','D','E','F'),
            ('A','B','C','I','J','K'),
            ('D','E','F','M','N','P'),
            ('M','N','P','I','J','K')
        ])
        A, B, C, M, N, P = bo_ten
        trung_diem = {
            frozenset([A, B]): M,
            frozenset([A, C]): N,
            frozenset([B, C]): P
        }
        hoan_vi = [
            (A, B, C), (A, C, B),
            (B, A, C), (B, C, A),
            (C, A, B), (C, B, A)
        ]
        X1, Y1, Z1 = random.choice(hoan_vi)
        M1_1, M2_1 = trung_diem[frozenset([X1, Y1])], trung_diem[frozenset([X1, Z1])]
        X2, Y2, Z2 = random.choice(hoan_vi)
        M1_2, M2_2, M3_2 = trung_diem[frozenset([X2, Y2])], trung_diem[frozenset([X2, Z2])], trung_diem[frozenset([Y2, Z2])]
        X3, Y3, Z3 = random.choice(hoan_vi)
        M1_3, M2_3, M3_3 = trung_diem[frozenset([X3, Y3])], trung_diem[frozenset([X3, Z3])], trung_diem[frozenset([Y3, Z3])]
        noidungcauhoi = ('Cho tam giác $%s%s%s$. Các điểm $%s$, $%s$ và $%s$ lần lượt là trung điểm các cạnh $%s%s$, $%s%s$ và $%s%s$. Tìm các hiệu sau: $\\overrightarrow{%s%s} - \\overrightarrow{%s%s}$; $\\overrightarrow{%s%s} - \\overrightarrow{%s%s}$ và $\\overrightarrow{%s%s} - \\overrightarrow{%s%s}$. \n'
                         %(A, B, C, M, N, P, A, B, A, C, B, C,
                           X1, M1_1, X1, M2_1,
                           M1_2, M2_2, M3_2, M2_2,
                           M1_3, M2_3, M2_3, Z3))
        loigiai = ('\\begin{center}\n'
                   '\\begin{tikzpicture}[scale=0.8, line width=1pt, line join=round, line cap=round]\n'
                   '\\coordinate (A) at (1.2,3);\n'
                   '\\coordinate (B) at (0,0);\n'
                   '\\coordinate (C) at (4.5,0);\n'
                   '\\coordinate (M) at (0.6,1.5);\n'
                   '\\coordinate (N) at (2.85,1.5);\n'
                   '\\coordinate (P) at (2.25,0);\n'
                   '\\draw (A)--(B)--(C)--cycle (M)--(N)--(P)--cycle;\n'
                   '\\fill (A) circle (1.5pt) node[above] {$%s$};\n'
                   '\\fill (B) circle (1.5pt) node[left] {$%s$};\n'
                   '\\fill (C) circle (1.5pt) node[right] {$%s$};\n'
                   '\\fill (M) circle (1.5pt) node[left] {$%s$};\n'
                   '\\fill (N) circle (1.5pt) node[right] {$%s$};\n'
                   '\\fill (P) circle (1.5pt) node[below] {$%s$};\n'
                   '\\end{tikzpicture}\n'
                   '\\end{center}\n'
                   'Theo quy tắc ba điểm: $\\overrightarrow{%s%s} - \\overrightarrow{%s%s} = \\overrightarrow{%s%s}$. \\\\ \n'
                   'Vì $-\\overrightarrow{%s%s} = \\overrightarrow{%s%s}$ nên $\\overrightarrow{%s%s} - \\overrightarrow{%s%s} = \\overrightarrow{%s%s} + \\overrightarrow{%s%s} = \\overrightarrow{%s%s}$. \\\\ \n'
                   'Vì $%s%s$ là đường trung bình của tam giác $%s%s%s$ và $\\overrightarrow{%s%s}$ cùng hướng với $\\overrightarrow{%s%s}$ nên ta có $\\overrightarrow{%s%s} = \\overrightarrow{%s%s}$. \\\\ \n'
                   'Do vậy $\\overrightarrow{%s%s} - \\overrightarrow{%s%s} = \\overrightarrow{%s%s} - \\overrightarrow{%s%s} = \\overrightarrow{%s%s}$. \n'
                   %(A, B, C, M, N, P,
                     X1, M1_1, X1, M2_1, M2_1, M1_1,
                     M3_2, M2_2, M2_2, M3_2, M1_2, M2_2, M3_2, M2_2, M1_2, M2_2, M2_2, M3_2, M1_2, M3_2,
                     M1_3, M3_3, A, B, C, M1_3, M3_3, M2_3, Z3, M2_3, Z3, M1_3, M3_3,
                     M1_3, M2_3, M2_3, Z3, M1_3, M2_3, M1_3, M3_3, M3_3, M2_3))
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('- -', '+').replace('+ -', '-')
    return content


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


def bt_dang14_p4_b1_c2_hh10(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        bo_dinh = random.choice([('A', 'B', 'C'), ('D', 'E', 'F')])
        bo_td = random.choice([('M', 'N', 'P'), ('I', 'J', 'K')])
        pA, pB, pC = bo_dinh
        pM, pN, pP = bo_td
        kieu_vec = random.choice(['MN', 'NP', 'PM'])
        yeu_cau = random.choice(['cùng phương', 'cùng hướng', 'ngược hướng'])
        if kieu_vec == 'MN':
            v_hoi = f'{pM}{pN}'
            v_nguoc = f'{pN}{pM}'
            c1, c2 = f'{pA}{pB}', f'{pB}{pC}'
            song_song = f'{pA}{pC}'
            cung_huong = [f'\\overrightarrow{{{pA}{pC}}}', f'\\overrightarrow{{{pA}{pP}}}', f'\\overrightarrow{{{pP}{pC}}}']
            nguoc_huong = [f'\\overrightarrow{{{pN}{pM}}}', f'\\overrightarrow{{{pC}{pA}}}', f'\\overrightarrow{{{pP}{pA}}}', f'\\overrightarrow{{{pC}{pP}}}']
        elif kieu_vec == 'NP':
            v_hoi = f'{pN}{pP}'
            v_nguoc = f'{pP}{pN}'
            c1, c2 = f'{pB}{pC}', f'{pC}{pA}'
            song_song = f'{pB}{pA}'
            cung_huong = [f'\\overrightarrow{{{pB}{pA}}}', f'\\overrightarrow{{{pB}{pM}}}', f'\\overrightarrow{{{pM}{pA}}}']
            nguoc_huong = [f'\\overrightarrow{{{pP}{pN}}}', f'\\overrightarrow{{{pA}{pB}}}', f'\\overrightarrow{{{pM}{pB}}}', f'\\overrightarrow{{{pA}{pM}}}']
        else:
            v_hoi = f'{pP}{pM}'
            v_nguoc = f'{pM}{pP}'
            c1, c2 = f'{pC}{pA}', f'{pA}{pB}'
            song_song = f'{pC}{pB}'
            cung_huong = [f'\\overrightarrow{{{pC}{pB}}}', f'\\overrightarrow{{{pC}{pN}}}', f'\\overrightarrow{{{pN}{pB}}}']
            nguoc_huong = [f'\\overrightarrow{{{pM}{pP}}}', f'\\overrightarrow{{{pB}{pC}}}', f'\\overrightarrow{{{pN}{pC}}}', f'\\overrightarrow{{{pB}{pN}}}']
        if yeu_cau == 'cùng phương':
            ds_kq = ', '.join(nguoc_huong[:1] + cung_huong + nguoc_huong[1:])
        elif yeu_cau == 'cùng hướng':
            ds_kq = ', '.join(cung_huong)
        else:
            ds_kq = ', '.join(nguoc_huong)
        noidungcauhoi = ('Cho tam giác $%s%s%s$. Gọi $%s, %s, %s$ lần lượt là trung điểm của $%s%s, %s%s, %s%s$. Xác định các vectơ (khác $\\vec{0}$, có điểm đầu và điểm cuối là các điểm đã cho) %s với $\\overrightarrow{%s}$. \n'
                         %(pA, pB, pC, pM, pN, pP, pA, pB, pB, pC, pC, pA, yeu_cau, v_hoi))
        loigiai = ('\\begin{center} \n'
                   '\\begin{tikzpicture}[line width=1pt, scale=0.8] \n'
                   '\\coordinate (B) at (0,0); \n'
                   '\\coordinate (C) at (5,0); \n'
                   '\\coordinate (A) at (1.8,3.2); \n'
                   '\\coordinate (M) at (0.9,1.6); \n'
                   '\\coordinate (N) at (2.5,0); \n'
                   '\\coordinate (P) at (3.4,1.6); \n'
                   '\\draw (A) -- (B) -- (C) -- cycle; \n'
                   '\\fill (A) circle (1.5pt) node[above] {$%s$}; \n'
                   '\\fill (B) circle (1.5pt) node[below left] {$%s$}; \n'
                   '\\fill (C) circle (1.5pt) node[below right] {$%s$}; \n'
                   '\\fill (M) circle (1.5pt) node[above left] {$%s$}; \n'
                   '\\fill (N) circle (1.5pt) node[below] {$%s$}; \n'
                   '\\fill (P) circle (1.5pt) node[above right] {$%s$}; \n'
                   '\\end{tikzpicture} \n'
                   '\\end{center} \n'
                   'Vì $%s, %s$ lần lượt là trung điểm của $%s, %s$ nên $%s$ là đường trung bình của tam giác $%s%s%s$, suy ra $%s \\parallel %s$. \\\\ \n'
                   'Do đó, các vectơ %s với $\\overrightarrow{%s}$ là: $%s$. \n'
                   %(pA, pB, pC, pM, pN, pP,
                     v_hoi[0], v_hoi[1], c1, c2, v_hoi, pA, pB, pC, v_hoi, song_song,
                     yeu_cau, v_hoi, ds_kq))
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
    return content

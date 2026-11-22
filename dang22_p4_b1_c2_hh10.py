
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


def bt_dang22_p4_b1_c2_hh10(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        bo_dinh = random.choice([('A', 'B', 'C'), ('M', 'N', 'P'), ('X', 'Y', 'Z')])
        bo_td = random.choice([('D', 'E', 'F'), ('I', 'J', 'K')])
        pA, pB, pC = bo_dinh
        pD, pE, pF = bo_td
        kieu = random.choice(['EF_CD', 'FE_BD', 'FD_AE', 'DE_BF'])
        if kieu == 'EF_CD':
            v1, v2, canh, hbh = f'{pE}{pF}', f'{pC}{pD}', f'{pB}{pC}', f'{pE}{pF}{pD}{pC}'
        elif kieu == 'FE_BD':
            v1, v2, canh, hbh = f'{pF}{pE}', f'{pB}{pD}', f'{pB}{pC}', f'{pF}{pE}{pD}{pB}'
        elif kieu == 'FD_AE':
            v1, v2, canh, hbh = f'{pF}{pD}', f'{pA}{pE}', f'{pC}{pA}', f'{pF}{pD}{pE}{pA}'
        else:
            v1, v2, canh, hbh = f'{pD}{pE}', f'{pB}{pF}', f'{pA}{pB}', f'{pD}{pE}{pF}{pB}'
        noidungcauhoi = ('Cho tam giác $%s%s%s$. Gọi $%s, %s, %s$ lần lượt là trung điểm các cạnh $%s%s, %s%s, %s%s$. Chứng minh $\\overrightarrow{%s} = \\overrightarrow{%s}$. \n'
                         %(pA, pB, pC, pD, pE, pF, pB, pC, pC, pA, pA, pB, v1, v2))
        loigiai = ('\\begin{center} \n'
                   '\\begin{tikzpicture}[line width=1pt, scale=0.8] \n'
                   '\\coordinate (B) at (0,0); \n'
                   '\\coordinate (C) at (5,0); \n'
                   '\\coordinate (A) at (2.2,3.6); \n'
                   '\\coordinate (D) at (2.5,0); \n'
                   '\\coordinate (E) at (3.6,1.8); \n'
                   '\\coordinate (F) at (1.1,1.8); \n'
                   '\\draw (A) -- (B) -- (C) -- cycle; \n'
                   '\\draw (D) -- (E) -- (F) -- cycle; \n'
                   '\\fill (A) circle (1.5pt) node[above] {$%s$}; \n'
                   '\\fill (B) circle (1.5pt) node[below left] {$%s$}; \n'
                   '\\fill (C) circle (1.5pt) node[below right] {$%s$}; \n'
                   '\\fill (D) circle (1.5pt) node[below] {$%s$}; \n'
                   '\\fill (E) circle (1.5pt) node[above right] {$%s$}; \n'
                   '\\fill (F) circle (1.5pt) node[above left] {$%s$}; \n'
                   '\\end{tikzpicture} \n'
                   '\\end{center} \n'
                   '\\textit{Cách 1:} Vì $%s$ là đường trung bình của tam giác $%s%s%s$ nên $%s \\parallel %s$ và $%s = \\dfrac{1}{2}%s \\Rightarrow %s = %s \\Rightarrow \\left|\\overrightarrow{%s}\\right| = \\left|\\overrightarrow{%s}\\right|$ (1). \\\\ \n'
                   'Mặt khác: $\\overrightarrow{%s}$ cùng hướng $\\overrightarrow{%s}$ (2). \\\\ \n'
                   'Từ (1) và (2) ta có: $\\overrightarrow{%s} = \\overrightarrow{%s}$. \\\\ \n'
                   '\\textit{Cách 2:} Chứng minh $%s$ là hình bình hành. \\\\ \n'
                   'Dễ chứng minh được $%s = \\dfrac{1}{2}%s = %s$ và $%s \\parallel %s \\Rightarrow %s$ là hình bình hành $\\Rightarrow \\overrightarrow{%s} = \\overrightarrow{%s}$. \n'
                   %(pA, pB, pC, pD, pE, pF,
                     v1, pA, pB, pC, v1, v2, v1, canh, v1, v2, v1, v2,
                     v1, v2, v1, v2,
                     hbh, v1, canh, v2, v1, v2, hbh, v1, v2))
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
    return content

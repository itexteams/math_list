
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


def bt_dang11_p4_b1_c2_hh10(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        bo_dinh = random.choice([('A', 'B', 'C', 'D'), ('E', 'F', 'G', 'H'), ('I', 'J', 'K', 'L')])
        bo_td = random.choice([('N', 'P'), ('U', 'V')])
        pA, pB, pC, pD = bo_dinh
        pN, pP = bo_td
        pM = random.choice(['M', 'S', 'T'])
        pO = 'O'
        loai_hinh = random.choice(['hình chữ nhật', 'hình vuông', 'hình bình hành', 'hình thoi'])
        if loai_hinh == 'hình chữ nhật':
            cA, cB, cC, cD, cO, cN, cP = '(0,0)', '(0,3)', '(5,3)', '(5,0)', '(2.5,1.5)', '(2.5,0)', '(0,1.5)'
        elif loai_hinh == 'hình vuông':
            cA, cB, cC, cD, cO, cN, cP = '(0,0)', '(0,3.5)', '(3.5,3.5)', '(3.5,0)', '(1.75,1.75)', '(1.75,0)', '(0,1.75)'
        elif loai_hinh == 'hình bình hành':
            cA, cB, cC, cD, cO, cN, cP = '(0,0)', '(1.2,3)', '(5.2,3)', '(4,0)', '(2.6,1.5)', '(2,0)', '(0.6,1.5)'
        else:
            cA, cB, cC, cD, cO, cN, cP = '(0,1.5)', '(2.5,3)', '(5,1.5)', '(2.5,0)', '(2.5,1.5)', '(1.25,0.75)', '(1.25,2.25)'
        kieu = random.choice(['AP_NM', 'AN_PM'])
        if kieu == 'AP_NM':
            v1, v2, v_o = f'{pA}{pP}', f'{pN}{pM}', f'{pN}{pO}'
            ve_doan = '(O) -- (N)'
        else:
            v1, v2, v_o = f'{pA}{pN}', f'{pP}{pM}', f'{pP}{pO}'
            ve_doan = '(O) -- (P)'
        noidungcauhoi = ('Cho %s $%s%s%s%s$, $%s, %s$ lần lượt là trung điểm cạnh $%s%s, %s%s$ và điểm $%s$ thỏa mãn $\\overrightarrow{%s} = \\overrightarrow{%s}$. Xác định vị trí điểm $%s$. \n'
                         %(loai_hinh, pA, pB, pC, pD, pN, pP, pA, pD, pA, pB, pM, v1, v2, pM))
        loigiai = ('\\begin{center} \n'
                   '\\begin{tikzpicture}[line width=1pt, scale=0.8] \n'
                   '\\coordinate (A) at %s; \n'
                   '\\coordinate (B) at %s; \n'
                   '\\coordinate (C) at %s; \n'
                   '\\coordinate (D) at %s; \n'
                   '\\coordinate (O) at %s; \n'
                   '\\coordinate (N) at %s; \n'
                   '\\coordinate (P) at %s; \n'
                   '\\draw (A) -- (B) -- (C) -- (D) -- cycle; \n'
                   '\\draw (A) -- (C) (B) -- (D) %s; \n'
                   '\\fill (A) circle (1.5pt) node[below left] {$%s$}; \n'
                   '\\fill (B) circle (1.5pt) node[above left] {$%s$}; \n'
                   '\\fill (C) circle (1.5pt) node[above right] {$%s$}; \n'
                   '\\fill (D) circle (1.5pt) node[below right] {$%s$}; \n'
                   '\\fill (O) circle (1.5pt) node[above=3pt] {$%s$}; \n'
                   '\\fill (N) circle (1.5pt) node[below] {$%s$}; \n'
                   '\\fill (P) circle (1.5pt) node[left] {$%s$}; \n'
                   '\\end{tikzpicture} \n'
                   '\\end{center} \n'
                   'Gọi $%s$ là tâm %s $%s%s%s%s \\Rightarrow \\overrightarrow{%s} = \\overrightarrow{%s}$. \\\\ \n'
                   'Mà $\\overrightarrow{%s} = \\overrightarrow{%s}$ suy ra $\\overrightarrow{%s} = \\overrightarrow{%s} \\Rightarrow %s \\equiv %s$. Vậy $%s$ là tâm của %s $%s%s%s%s$. \n'
                   %(cA, cB, cC, cD, cO, cN, cP, ve_doan,
                     pA, pB, pC, pD, pO, pN, pP,
                     pO, loai_hinh, pA, pB, pC, pD, v1, v_o,
                     v1, v2, v2, v_o, pM, pO, pM, loai_hinh, pA, pB, pC, pD))
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
    return content

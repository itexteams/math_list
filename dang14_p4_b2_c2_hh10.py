
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


def bt_dang14_p4_b2_c2_hh10(self):
    lisdang=['1', '2']
    dang=random.choice(lisdang)
    if dang=='1':
        A, B = random.choice([('A','B'), ('C','D'), ('E','F'), ('P','Q')])
        M = random.choice(['M', 'K', 'X'])
        N = random.choice([t for t in ['N', 'H', 'Y'] if t not in [A, B, M]])
        O = random.choice([t for t in ['O', 'I'] if t not in [A, B, M, N]])
        thu_tu = random.choice([1, 2])
        if thu_tu == 1:
            P1, P2 = A, B
        else:
            P1, P2 = B, A
        noidungcauhoi = ('Cho hai điểm $%s$ và $%s$. Tìm tập hợp các điểm $%s$ thỏa mãn điều kiện $\\left|\\overrightarrow{%s%s} + \\overrightarrow{%s%s}\\right| = \\left|\\overrightarrow{%s%s} - \\overrightarrow{%s%s}\\right|$. \n'
                         %(A, B, M, M, A, M, B, M, P1, M, P2))
        loigiai = ('Vẽ hình bình hành $%s%s%s%s$. \\\\ \n'
                   'Gọi $%s$ là giao điểm hai đường chéo ta có: $\\overrightarrow{%s%s} + \\overrightarrow{%s%s} = \\overrightarrow{%s%s} \\Rightarrow \\left|\\overrightarrow{%s%s} + \\overrightarrow{%s%s}\\right| = \\left|\\overrightarrow{%s%s}\\right| = %s%s = 2%s%s$. \\\\ \n'
                   '$\\overrightarrow{%s%s} - \\overrightarrow{%s%s} = \\overrightarrow{%s%s} \\Rightarrow \\left|\\overrightarrow{%s%s} - \\overrightarrow{%s%s}\\right| = \\left|\\overrightarrow{%s%s}\\right| = %s%s \\Rightarrow 2%s%s = %s%s \\Rightarrow %s%s = \\frac{%s%s}{2}$. \\\\ \n'
                   'Vậy tập hợp các điểm $%s$ là đường tròn đường kính $%s%s$. \n'
                   %(A, M, B, N,
                     O, M, A, M, B, M, N, M, A, M, B, M, N, M, N, M, O,
                     M, P1, M, P2, P2, P1, M, P1, M, P2, P2, P1, P2, P1, M, O, A, B, M, O, A, B,
                     M, A, B))
    elif dang=='2':
        A, B = random.choice([('A','B'), ('C','D'), ('E','F'), ('P','Q')])
        M = random.choice(['M', 'K', 'X'])
        N = random.choice([t for t in ['N', 'H', 'Y'] if t not in [A, B, M]])
        O = random.choice([t for t in ['O', 'I'] if t not in [A, B, M, N]])
        r = randint(2, 6)
        d = 2 * r
        k = random.choice([2, 3, 4])
        R = k * r
        noidungcauhoi = ('Cho hai điểm cố định $%s$ và $%s$ với $%s%s = %s$. Tìm tập hợp các điểm $%s$ thỏa mãn điều kiện $\\left|\\overrightarrow{%s%s} + \\overrightarrow{%s%s}\\right| = %s\\left|\\overrightarrow{%s%s} - \\overrightarrow{%s%s}\\right|$. \n'
                         %(A, B, A, B, latex(d), M, M, A, M, B, latex(k), M, A, M, B))
        loigiai = ('Vẽ hình bình hành $%s%s%s%s$. \\\\ \n'
                   'Gọi $%s$ là giao điểm hai đường chéo (khi đó $%s$ là trung điểm cố định của $%s%s$), ta có: $\\overrightarrow{%s%s} + \\overrightarrow{%s%s} = \\overrightarrow{%s%s} \\Rightarrow \\left|\\overrightarrow{%s%s} + \\overrightarrow{%s%s}\\right| = \\left|\\overrightarrow{%s%s}\\right| = %s%s = 2%s%s$. \\\\ \n'
                   '$\\overrightarrow{%s%s} - \\overrightarrow{%s%s} = \\overrightarrow{%s%s} \\Rightarrow %s\\left|\\overrightarrow{%s%s} - \\overrightarrow{%s%s}\\right| = %s\\left|\\overrightarrow{%s%s}\\right| = %s%s%s$. \\\\ \n'
                   'Từ giả thiết suy ra $2%s%s = %s%s%s \\Rightarrow %s%s = \\frac{%s \\cdot %s}{2} = %s$. \\\\ \n'
                   'Vậy tập hợp các điểm $%s$ là đường tròn tâm $%s$ (trung điểm của $%s%s$) bán kính $R = %s$. \n'
                   %(A, M, B, N,
                     O, O, A, B, M, A, M, B, M, N, M, A, M, B, M, N, M, N, M, O,
                     M, A, M, B, B, A, latex(k), M, A, M, B, latex(k), B, A, latex(k), A, B,
                     M, O, latex(k), A, B, M, O, latex(k), latex(d), latex(R),
                     M, O, A, B, latex(R)))
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('- -', '+').replace('+ -', '-')
    return content

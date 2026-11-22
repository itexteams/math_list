
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


def bt_dang29_p4_b1_c2_hh10(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        bo_dinh = random.choice([('A', 'B', 'C', 'D'), ('E', 'F', 'G', 'H')])
        bo_mn = random.choice([('M', 'N'), ('P', 'Q')])
        pA, pB, pC, pD = bo_dinh
        pM, pN = bo_mn
        a = randint(1, 8)
        b = randint(1, 8)
        c = randint(1, 10)
        d = randint(1, 10)
        while c == a and d == b:
            c = randint(1, 10)
        r1 = Rational(c, a)
        r2 = Rational(d, b)
        kq = Rational(b * c, a * d)
        s_r1 = '' if r1 == 1 else latex(r1)
        s_r2 = '' if r2 == 1 else latex(r2)
        noidungcauhoi = ('Cho tứ giác $%s%s%s%s$ có hai đường chéo cắt nhau tại $O$. Qua trung điểm $%s$ của $%s%s$ dựng đường thẳng $%sO$ cắt $%s%s$ tại $%s$. Biết $O%s = %s, O%s = %s, O%s = %s$ và $O%s = %s$. Tính tỷ số $\\dfrac{%s%s}{%s%s}$. \n'
                         %(pA, pB, pC, pD, pM, pA, pB, pM, pC, pD, pN, pA, latex(a), pB, latex(b), pC, latex(c), pD, latex(d), pC, pN, pN, pD))
        loigiai = ('Ta có: $\\overrightarrow{O%s} = -%s\\overrightarrow{O%s}$; $\\overrightarrow{O%s} = -%s\\overrightarrow{O%s}$. \\\\ \n'
                   'Vì $%s$ là trung điểm $%s%s$ và $\\overrightarrow{O%s}, \\overrightarrow{O%s}$ cùng phương nên $\\exists t$ sao cho $\\overrightarrow{O%s} = t\\overrightarrow{O%s} = \\dfrac{t}{2}\\left(\\overrightarrow{O%s} + \\overrightarrow{O%s}\\right)$ (1). \\\\ \n'
                   'Đặt $\\dfrac{%s%s}{%s%s} = k$ ($k > 0$), suy ra $\\overrightarrow{%s%s} = k\\overrightarrow{%s%s} \\Leftrightarrow \\overrightarrow{O%s} = \\dfrac{1}{1+k}\\overrightarrow{O%s} + \\dfrac{k}{1+k}\\overrightarrow{O%s}$. \\\\ \n'
                   'Thay $\\overrightarrow{O%s}, \\overrightarrow{O%s}$ vào ta được: $\\overrightarrow{O%s} = -\\dfrac{%s}{1+k}\\overrightarrow{O%s} - \\dfrac{%sk}{1+k}\\overrightarrow{O%s}$ (2). \\\\ \n'
                   'Từ (1) và (2) suy ra $-\\dfrac{%s}{1+k} = -\\dfrac{%sk}{1+k} \\Leftrightarrow k = %s$. Vậy $\\dfrac{%s%s}{%s%s} = %s$. \n'
                   %(pC, s_r1, pA, pD, s_r2, pB,
                     pM, pA, pB, pM, pN, pN, pM, pA, pB,
                     pC, pN, pN, pD, pC, pN, pN, pD, pN, pC, pD,
                     pC, pD, pN, latex(r1), pA, s_r2, pB,
                     latex(r1), s_r2, latex(kq), pC, pN, pN, pD, latex(kq)))
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
    return content

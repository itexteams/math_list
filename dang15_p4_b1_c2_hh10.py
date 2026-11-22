
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


def bt_dang15_p4_b1_c2_hh10(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        ptA = random.choice(['A', 'B', 'C', 'I', 'O'])
        ptM = random.choice(['M', 'N', 'P', 'Q'])
        ptE = random.choice(['E', 'F', 'K', 'H'])
        vec_name = random.choice(['a', 'b', 'u', 'v'])
        line_delta = random.choice(['\\Delta', 'd_1', '\\ell'])
        line_m = random.choice(['m', 'd', 'd_2'])
        huong = random.choice(['cùng hướng', 'ngược hướng'])
        if huong == 'cùng hướng':
            coord_M = '(2.7,2.6)'
            coord_E = '(2.9,3.0)'
        else:
            coord_M = '(1.7,0.6)'
            coord_E = '(1.5,0.2)'
        noidungcauhoi = ('Cho điểm $%s$ và véctơ $\\vec{%s}$ khác $\\vec{0}$. Tìm điểm $%s$ sao cho: \\\\ \n'
                         'a) $\\overrightarrow{%s%s}$ cùng phương với $\\vec{%s}$. \\\\ \n'
                         'b) $\\overrightarrow{%s%s}$ %s với $\\vec{%s}$. \n'
                         %(ptA, vec_name, ptM, ptA, ptM, vec_name, ptA, ptM, huong, vec_name))
        loigiai = ('\\begin{center} \n'
                   '\\begin{tikzpicture}[line width=1pt, >=stealth, scale=0.8] \n'
                   '\\draw (0,0) -- (2,4) node[below right] {$%s$}; \n'
                   '\\draw[->] (0.7,1.4) -- (1.3,2.6) node[midway, left=4pt] {$\\vec{%s}$}; \n'
                   '\\fill (0.7,1.4) circle (1.5pt); \n'
                   '\\draw (1.2,-0.4) -- (3.2,3.6) node[below right] {$%s$}; \n'
                   '\\fill (2.2,1.6) circle (1.5pt) node[right] {$%s$}; \n'
                   '\\fill %s circle (1.5pt) node[right] {$%s$}; \n'
                   '\\fill %s circle (1.5pt) node[left] {$%s$}; \n'
                   '\\end{tikzpicture} \n'
                   '\\end{center} \n'
                   'Gọi $%s$ là giá của $\\vec{%s}$. \n'
                   '\\begin{enumEX}[a)]{1} \n'
                   '\\item Nếu $\\overrightarrow{%s%s}$ cùng phương với $\\vec{%s}$ thì đường thẳng $%s%s$ song song với $%s$. Do đó $%s$ thuộc đường thẳng $%s$ đi qua $%s$ và song song với $%s$. Ngược lại, mọi điểm $%s$ thuộc đường thẳng $%s$ thì $\\overrightarrow{%s%s}$ cùng phương với $\\vec{%s}$. Chú ý rằng nếu $%s$ thuộc đường thẳng $%s$ thì $%s$ trùng với $%s$. \n'
                   '\\item Lập luận tương tự như trên, ta thấy các điểm $%s$ thuộc một nửa đường thẳng gốc $%s$ của đường thẳng $%s$. Cụ thể, đó là nửa đường thẳng chứa điểm $%s$ sao cho $\\overrightarrow{%s%s}$ và $\\vec{%s}$ %s. \n'
                   '\\end{enumEX} \n'
                   %(line_delta, vec_name, line_m, ptA, coord_M, ptM, coord_E, ptE,
                     line_delta, vec_name,
                     ptA, ptM, vec_name, ptA, ptM, line_delta, ptM, line_m, ptA, line_delta, ptM, line_m, ptA, ptM, vec_name, ptA, line_delta, line_m, line_delta,
                     ptM, ptA, line_m, ptE, ptA, ptE, vec_name, huong))
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
    return content

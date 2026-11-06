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


def bt_dang17_p1_b3_c1_hh12(self):
    d1 = 'k\\overrightarrow{a} = (ka_1; ka_2; ka_3)'
    d2 = '\\overrightarrow{a} \\pm \\overrightarrow{b} = (a_1 \\pm b_1; a_2 \\pm b_2; a_3 \\pm b_3)'
    d3 = '|\\overrightarrow{a}| = \\sqrt{a_1^2 + a_2^2 + a_3^2}'
    d4 = '\\overrightarrow{a} \\cdot \\overrightarrow{b} = a_1b_1 + a_2b_2 + a_3b_3'
    s1_1 = 'k\\overrightarrow{a} = (ka_1; a_2; a_3)'
    s1_2 = 'k\\overrightarrow{a} = (ka_1; a_2; ka_3).'
    s2_1 = '\\overrightarrow{a} - \\overrightarrow{b} = (a_1 + b_1; a_2 + b_2; a_3 + b_3)'
    s2_2 = '\\overrightarrow{a} + \\overrightarrow{b} = (a_1 - b_1; a_2 - b_2; a_3 - b_3)'
    s3_1 = '|\\overrightarrow{a}| = a_1^2 + a_2^2 + a_3^2'
    s3_2 = '|\\overrightarrow{a}| = a_1 + a_2 + a_3'
    s4_1 = '\\overrightarrow{a} \\cdot \\overrightarrow{b} = a_1b_1 - a_2b_2 - a_3b_3'
    s4_2 = '\\overrightarrow{a} \\cdot \\overrightarrow{b} = a_1b_2 + a_2b_3 + a_3b_1'
    list_cau_dung = [d1, d2, d3, d4]
    cau_dung_chon = random.choice(list_cau_dung)
    da_d = '\\True $' + cau_dung_chon + '$'
    list_cau_sai_chon = []
    if cau_dung_chon == d1:
        list_cau_sai_chon = [random.choice([s2_1, s2_2]), random.choice([s3_1, s3_2]), random.choice([s4_1, s4_2])]
    elif cau_dung_chon == d2:
        list_cau_sai_chon = [random.choice([s1_1, s1_2]), random.choice([s3_1, s3_2]), random.choice([s4_1, s4_2])]
    elif cau_dung_chon == d3:
        list_cau_sai_chon = [random.choice([s1_1, s1_2]), random.choice([s2_1, s2_2]), random.choice([s4_1, s4_2])]
    else:
        list_cau_sai_chon = [random.choice([s1_1, s1_2]), random.choice([s2_1, s2_2]), random.choice([s3_1, s3_2])]
    das1 = '$' + list_cau_sai_chon[0] + '$'
    das2 = '$' + list_cau_sai_chon[1] + '$'
    das3 = '$' + list_cau_sai_chon[2] + '$'
    noidungcauhoi = '''Trong không gian $Oxyz$, cho hai véc tơ $\\overrightarrow{a}=(a_1;a_2;a_3)$; $\\overrightarrow{b}=(b_1;b_2;b_3)$ và $k \\in \\mathbb{R}$. Khẳng định nào dưới đây đúng?'''
    list_1 = [da_d, das1, das2, das3]
    random.shuffle(list_1)
    loigiai = '''Dựa vào các tính chất và phép toán của véc tơ trong không gian, ta thấy khẳng định đúng là $%s$''' % (cau_dung_chon)
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
        '\\choice \n'
        '{'+str(list_1[1])+'}\n'
        '{'+str(list_1[2])+'}\n'
        '{'+str(list_1[3])+'}\n'
        '{'+str(list_1[0])+'}\n'
        '\\loigiai{'+str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content


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


def bt_dang30_p1_b3_c1_hh12(self):
    vec_base = random.choice(['i', 'j', 'k'])
    if vec_base == 'i':
        vec_b_latex = '\\overrightarrow{i}'
        x1, y1, z1 = 1, 0, 0
    elif vec_base == 'j':
        vec_b_latex = '\\overrightarrow{j}'
        x1, y1, z1 = 0, 1, 0
    else:
        vec_b_latex = '\\overrightarrow{k}'
        x1, y1, z1 = 0, 0, 1
    list_goc = [30, 45, 60, 90, 120, 135, 150]
    goc = random.choice(list_goc)
    cos_val = sp.cos(sp.rad(goc))
    if vec_base == 'i':
        x2 = cos_val * 2
        if goc in [90]:
            y2 = random.choice([-2, -1, 1, 2])
            z2 = random.choice([-2, -1, 1, 2])
        else:
            temp = sp.sqrt(4 - x2**2)
            y2 = temp * random.choice([-1, 1]) / sp.sqrt(2)
            z2 = temp * random.choice([-1, 1]) / sp.sqrt(2)
    elif vec_base == 'j':
        y2 = cos_val * 2
        if goc in [90]:
            x2 = random.choice([-2, -1, 1, 2])
            z2 = random.choice([-2, -1, 1, 2])
        else:
            temp = sp.sqrt(4 - y2**2)
            x2 = temp * random.choice([-1, 1]) / sp.sqrt(2)
            z2 = temp * random.choice([-1, 1]) / sp.sqrt(2)
    else:
        z2 = cos_val * 2
        if goc in [90]:
            x2 = random.choice([-2, -1, 1, 2])
            y2 = random.choice([-2, -1, 1, 2])
        else:
            temp = sp.sqrt(4 - z2**2)
            x2 = temp * random.choice([-1, 1]) / sp.sqrt(2)
            y2 = temp * random.choice([-1, 1]) / sp.sqrt(2)
    x2_latex = latex(sp.simplify(x2))
    y2_latex = latex(sp.simplify(y2))
    z2_latex = latex(sp.simplify(z2))
    tich_vo_huong = sp.simplify(x1*x2 + y1*y2 + z1*z2)
    do_dai_u = sp.simplify(sp.sqrt(x2**2 + y2**2 + z2**2))
    cos_latex = latex(sp.simplify(tich_vo_huong / (1 * do_dai_u)))
    kq = goc
    du = ['$%s^\\circ$'%(kq)]
    da = random.choice(du)
    s = [30, 45, 60, 90, 120, 135, 150]
    if kq in s:
        s.remove(kq)
    random.shuffle(s)
    das1 = s[0]
    das2 = s[1]
    das3 = s[2]
    noidungcauhoi = ('''Trong không gian $Oxyz$, góc giữa hai vectơ $%s$ và $\\overrightarrow{u}=(%s; %s; %s)$ là''' % (vec_b_latex, x2_latex, y2_latex, z2_latex))
    da_d = ('\\True ' + str(da))
    da_s1 = '$%s^\\circ$' % str(das1)
    da_s2 = '$%s^\\circ$' % str(das2)
    da_s3 = '$%s^\\circ$' % str(das3)
    list_1 = [da_d, da_s1, da_s2, da_s3]
    random.shuffle(list_1)
    str_x2 = f"({x2_latex})" if '-' in x2_latex else x2_latex
    str_y2 = f"({y2_latex})" if '-' in y2_latex else y2_latex
    str_z2 = f"({z2_latex})" if '-' in z2_latex else z2_latex
    tu_so = f"{x1}.{str_x2} + {y1}.{str_y2} + {z1}.{str_z2}".replace('+ -', '- ')
    mau_so = f"1.\\sqrt{{{str_x2}^2 + {str_y2}^2 + {str_z2}^2}}"
    loigiai = ('''Ta có $%s=(%s; %s; %s)$. \\\\ Do đó $\\cos(%s, \\overrightarrow{u}) = \\frac{%s \\cdot \\overrightarrow{u}}{|%s| \\cdot |\\overrightarrow{u}|} = \\frac{%s}{%s} = %s \\Rightarrow (%s, \\overrightarrow{u}) = %s^\\circ$.''' % (vec_b_latex, x1, y1, z1, vec_b_latex, vec_b_latex, vec_b_latex, tu_so, mau_so, cos_latex, vec_b_latex, kq))
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+ 
        '\n\\choice \n'
        '{'+str(list_1[1])+'}\n'
        '{'+str(list_1[2])+'}\n'
        '{'+str(list_1[3])+'}\n'
        '{'+str(list_1[0])+'}\n'
        '\\loigiai{'+str(loigiai)+'}\n'
        '\\end{ex}\n\\end{minipage} \n\n')
    return content


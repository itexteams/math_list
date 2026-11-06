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


def bt_dang33_p1_b3_c1_hh12(self):
    truc_thuoc = random.choice(['Ox', 'Oy', 'Oz'])
    if truc_thuoc == 'Ox':
        truc_str = 'Ox'
        xc = random.randint(-3, 3)
        yc = 0
        zc = 0
    elif truc_thuoc == 'Oy':
        truc_str = 'Oy'
        xc = 0
        yc = random.randint(-3, 3)
        zc = 0
    else:
        truc_str = 'Oz'
        xc = 0
        yc = 0
        zc = random.randint(-3, 3)
    v_ab_x = random.choice([-2, -1, 1, 2, 3])
    v_ab_y = random.choice([-2, -1, 1, 2, 3])
    v_ab_z = random.choice([-2, -1, 1, 2, 3])
    xd = xc - v_ab_x
    yd = yc - v_ab_y
    zd = zc - v_ab_z
    v_bc_x = random.choice([-2, -1, 1, 2, 3])
    v_bc_y = random.choice([-2, -1, 1, 2, 3])
    if v_ab_z != 0:
        v_bc_z = -(v_ab_x * v_bc_x + v_ab_y * v_bc_y) / v_ab_z
        while v_bc_z != int(v_bc_z) or v_bc_z == 0:
            v_bc_x = random.choice([-2, -1, 1, 2, 3])
            v_bc_y = random.choice([-2, -1, 1, 2, 3])
            v_bc_z = -(v_ab_x * v_bc_x + v_ab_y * v_bc_y) / v_ab_z
        v_bc_z = int(v_bc_z)
    else:
        v_bc_x = random.choice([-2, -1, 1, 2, 3])
        v_bc_z = random.choice([-2, -1, 1, 2, 3])
        v_bc_y = -(v_ab_x * v_bc_x + v_ab_z * v_bc_z) / v_ab_y
        while v_bc_y != int(v_bc_y) or v_bc_y == 0:
            v_bc_x = random.choice([-2, -1, 1, 2, 3])
            v_bc_z = random.choice([-2, -1, 1, 2, 3])
            v_bc_y = -(v_ab_x * v_bc_x + v_ab_z * v_bc_z) / v_ab_y
        v_bc_y = int(v_bc_y)
    xb = xc - v_bc_x
    yb = yc - v_bc_y
    zb = zc - v_bc_z
    xa = xb - v_ab_x
    ya = yb - v_ab_y
    za = zb - v_ab_z
    kq = xd + yd + zd
    du = ['$%s$' % kq]
    da = du[0]
    s = [kq + 1, kq - 1, kq + 2, kq - 2, kq + 3, kq - 3]
    random.shuffle(s)
    das1 = '$%s$' % s[0]
    das2 = '$%s$' % s[1]
    das3 = '$%s$' % s[2]
    noidungcauhoi = '''Trong không gian $Oxyz$, cho hình chữ nhật $ABCD$ trong đó $A(%s;%s;%s), B(%s;%s;%s), C \\in %s, D(a;b;c)$. Tính giá trị biểu thức $P = a+b+c$.''' % (xa, ya, za, xb, yb, zb, truc_str)
    da_d = '\\True ' + str(da)
    list_1 = [da_d, das1, das2, das3]
    random.shuffle(list_1)
    if truc_thuoc == 'Ox':
        g_c = "C(a;0;0)"
        v_bc_str = "(a - %s; %s; %s)" % (xb, -yb, -zb)
        tich = f"{v_ab_x}(a - {xb}) + {v_ab_y}.({-yb}) + {v_ab_z}.({-zb}) = 0".replace('+ -', '- ').replace('.(-', '.(').replace('-)', ')')
        a_val = xc
        c_pt = f"C({xc};0;0)"
    elif truc_thuoc == 'Oy':
        g_c = "C(0;b;0)"
        v_bc_str = "(%s; b - %s; %s)" % (-xb, yb, -zb)
        tich = f"{v_ab_x}.({-xb}) + {v_ab_y}(b - {yb}) + {v_ab_z}.({-zb}) = 0".replace('+ -', '- ').replace('.(-', '.(').replace('-)', ')')
        a_val = yc
        c_pt = f"C(0;{yc};0)"
    else:
        g_c = "C(0;0;c)"
        v_bc_str = "(%s; %s; c - %s)" % (-xb, -yb, zb)
        tich = f"{v_ab_x}.({-xb}) + {v_ab_y}.({-yb}) + {v_ab_z}(c - {zb}) = 0".replace('+ -', '- ').replace('.(-', '.(').replace('-)', ')')
        a_val = zc
        c_pt = f"C(0;0;{zc})"
    loigiai = '''Gọi $%s$ \\\\ Ta có $\\overrightarrow{DC} = \\overrightarrow{AB} \\Rightarrow \\overrightarrow{DC} = (%s;%s;%s)$ \\\\ Ta có $\\overrightarrow{DC} \\perp \\overrightarrow{BC} \\Leftrightarrow \\overrightarrow{DC} \\cdot \\overrightarrow{BC} = 0 \\Leftrightarrow %s \\Leftrightarrow a = %s \\Rightarrow %s$ \\\\ Mặt khác $\\overrightarrow{DC} = (%s;%s;%s) \\Rightarrow D(%s;%s;%s) \\Rightarrow P = %s$.''' % (g_c, v_ab_x, v_ab_y, v_ab_z, tich, a_val, c_pt, v_ab_x, v_ab_y, v_ab_z, xd, yd, zd, kq)
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


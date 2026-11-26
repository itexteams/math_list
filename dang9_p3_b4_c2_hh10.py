
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


def bt_dang9_p3_b4_c2_hh10(self):
    def fmt_lin(p, q):
        s1 = 'm' if p == 1 else ('-m' if p == -1 else str(p) + 'm')
        s2 = ' + ' + str(q) if q > 0 else ' - ' + str(abs(q))
        return s1 + s2
    def fmt_rhs_cross(c0, c2):
        s1 = str(c0)
        if c2 == 1:
            s2 = ' + m^2'
        elif c2 == -1:
            s2 = ' - m^2'
        elif c2 > 0:
            s2 = ' + ' + str(c2) + 'm^2'
        else:
            s2 = ' - ' + str(abs(c2)) + 'm^2'
        return s1 + s2
    def fmt_quad(A, B, C):
        s1 = 'm^2' if A == 1 else str(A) + 'm^2'
        if B == 1:
            s2 = ' + m'
        elif B == -1:
            s2 = ' - m'
        elif B > 0:
            s2 = ' + ' + str(B) + 'm'
        else:
            s2 = ' - ' + str(abs(B)) + 'm'
        s3 = ' + ' + str(C) if C > 0 else ' - ' + str(abs(C))
        return s1 + s2 + s3
    def fix_signs(s):
        return s.replace('+ -', '- ').replace('+-', '-').replace('- -', '+ ').replace('--', '+')
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        while True:
            xa = random.choice([-3, -2, -1, 1, 2, 3])
            ya = random.choice([-3, -2, -1, 1, 2, 3])
            xb = random.choice([-3, -2, -1, 1, 2, 3])
            yb = random.choice([-3, -2, -1, 1, 2, 3])
            if xa * yb == ya * xb:
                continue
            m1 = random.choice([1, 2, 3, 4])
            m2 = random.choice([-4, -3, -2, -1])
            if m1 + m2 == 0:
                continue
            r = random.choice([1, 2, 3, 4, 5, 6])
            num_p = -xa * (m1 + m2)
            num_q = xa * (r + m1 * m2)
            if num_p % ya == 0 and num_q % ya == 0:
                p = num_p // ya
                q = num_q // ya
                if p != 0 and q != 0:
                    break
        kq = Integer(m1)
        xd_str = fmt_lin(p, q)
        yd_str = str(r) + ' - m^2'
        lhs_cross = fmt_lin(ya * p, ya * q)
        rhs_cross = fmt_rhs_cross(xa * r, -xa)
        if xa > 0:
            quad_str = fmt_quad(xa, ya * p, ya * q - xa * r)
        else:
            quad_str = fmt_quad(-xa, -ya * p, xa * r - ya * q)
        noidungcauhoi = fix_signs('''Trong mặt phẳng tọa độ $Oxy$, cho các vectơ $\\vec{a} = (%s; %s)$, $\\vec{b} = (%s; %s)$ và $\\vec{d} = (%s; %s)$. Biết rằng $\\vec{d}$ cùng phương với $\\vec{a}$, giá trị dương của $m$ bằng bao nhiêu?''' % (xa, ya, xb, yb, xd_str, yd_str))
        loigiai = fix_signs('''Ta có: $\\vec{d}$ cùng phương với $\\vec{a}$ khi và chỉ khi $\\dfrac{%s}{%s} = \\dfrac{%s}{%s}$\\\\
    $\\Leftrightarrow %s = %s \\Leftrightarrow %s = 0 \\Leftrightarrow \\left[\\begin{array}{l} m = %s \\\\ m = %s \\end{array}\\right.$.\\\\
    Vì $m$ dương nên $m = %s$ thỏa mãn.''' % (xd_str, xa, yd_str, ya, lhs_cross, rhs_cross, quad_str, m2, m1, m1))
        dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
        content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+ '\\loigiai{ \n' +str(loigiai)+'}\n' '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac')
        return content

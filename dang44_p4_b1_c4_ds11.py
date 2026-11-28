
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


def bt_dang44_p4_b1_c4_ds11(self):
    def fix_sign(s):
        return s.replace('+ -', '- ').replace('- -', '+ ').replace('+-', '-').replace('--', '+')
    def fmt_linear(a, b):
        pa = "n" if a == 1 else ("-n" if a == -1 else f"{a}n")
        pb = f"+ {b}" if b > 0 else f"- {abs(b)}"
        return f"{pa} {pb}"
    def fmt_rev_linear(b, a):
        pa = "+ n" if a == 1 else ("- n" if a == -1 else (f"+ {a}n" if a > 0 else f"- {abs(a)}n"))
        return f"{b} {pa}"
    def fmt_quad(a, b, c):
        pa = "n^2" if a == 1 else ("-n^2" if a == -1 else f"{a}n^2")
        pb = "+ n" if b == 1 else ("- n" if b == -1 else (f"+ {b}n" if b > 0 else f"- {abs(b)}n"))
        pc = f"+ {c}" if c > 0 else f"- {abs(c)}"
        return f"{pa} {pb} {pc}"
    def fmt_div_n(a, b):
        return f"{a} + \\dfrac{{{b}}}{{n}}" if b > 0 else f"{a} - \\dfrac{{{abs(b)}}}{{n}}"
    def fmt_rev_div_n(b, a):
        pa = f"+ {a}" if a > 0 else f"- {abs(a)}"
        return f"\\dfrac{{{b}}}{{n}} {pa}"
    def fmt_quad_div(a, b, c):
        pb = f"+ \\dfrac{{{b}}}{{n}}" if b > 0 else f"- \\dfrac{{{abs(b)}}}{{n}}"
        pc = f"+ \\dfrac{{{c}}}{{n^2}}" if c > 0 else f"- \\dfrac{{{abs(c)}}}{{n^2}}"
        return f"{a} {pb} {pc}"
    def fmt_frac(val):
        if val.q == 1:
            return str(val.p)
        if val < 0:
            return f"-\\dfrac{{{abs(val.p)}}}{{{val.q}}}"
        return f"\\dfrac{{{val.p}}}{{{val.q}}}"
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        p3 = random.choice([2, 3])
        p4 = random.choice([4, 6])
        deg = 2 * p3 + p4
        p1 = random.randint(3, deg - 3)
        p2 = deg - p1
        a1 = random.randint(2, 4)
        b1 = random.choice([i for i in range(-5, 6) if i != 0])
        a2 = random.randint(2, 4)
        b2 = random.choice([i for i in range(-5, 6) if i != 0])
        a3 = random.randint(2, 5)
        b3 = random.choice([i for i in range(-5, 6) if i != 0])
        c3 = random.choice([i for i in range(-5, 6) if i != 0])
        b4 = random.randint(2, 9)
        a4 = random.choice([-6, -5, -4, -3, -2])
        tu = f"({fmt_linear(a1, b1)})^{{{p1}}}({fmt_linear(a2, b2)})^{{{p2}}}"
        mau = f"({fmt_quad(a3, b3, c3)})^{{{p3}}}({fmt_rev_linear(b4, a4)})^{{{p4}}}"
        tu_chia = f"\\left({fmt_div_n(a1, b1)}\\right)^{{{p1}}}\\left({fmt_div_n(a2, b2)}\\right)^{{{p2}}}"
        mau_chia = f"\\left({fmt_quad_div(a3, b3, c3)}\\right)^{{{p3}}}\\left({fmt_rev_div_n(b4, a4)}\\right)^{{{p4}}}"
        kq = Rational((a1**p1) * (a2**p2), (a3**p3) * (a4**p4))
        kq_str = fmt_frac(kq)
        a4_disp = f"({a4})" if a4 < 0 else str(a4)
        noidungcauhoi = fix_sign(f"Tính giới hạn $\\lim \\dfrac{{{tu}}}{{{mau}}}$.")
        loigiai = fix_sign(f"Chia cả tử và mẫu cho $n^{{{deg}}}$, ta được: $$\\lim \\dfrac{{{tu}}}{{{mau}}} = \\lim \\dfrac{{{tu_chia}}}{{{mau_chia}}} = \\dfrac{{{a1}^{{{p1}}} \\cdot {a2}^{{{p2}}}}}{{{a3}^{{{p3}}} \\cdot {a4_disp}^{{{p4}}}}} = {kq_str}.$$")
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content

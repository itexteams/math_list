
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


def bt_dang42_p4_b1_c4_ds11(self):
    def fix_sign(s):
        return s.replace('+ -', '- ').replace('- -', '+ ').replace('+-', '-').replace('--', '+')
    def fmt_linear(a, b):
        pa = "n" if a == 1 else ("-n" if a == -1 else f"{a}n")
        pb = f"+ {b}" if b > 0 else f"- {abs(b)}"
        return f"{pa} {pb}"
    def fmt_div_n(a, b):
        return f"{a} + \\dfrac{{{b}}}{{n}}" if b > 0 else f"{a} - \\dfrac{{{abs(b)}}}{{n}}"
    def fmt_frac(val):
        if val.q == 1:
            return str(val.p)
        if val < 0:
            return f"-\\dfrac{{{abs(val.p)}}}{{{val.q}}}"
        return f"\\dfrac{{{val.p}}}{{{val.q}}}"
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        a = random.randint(2, 6)
        b = random.choice([i for i in range(-7, 8) if i != 0])
        c = random.randint(1, 5)
        d = random.choice([i for i in range(-7, 8) if i != 0])
        e = random.randint(2, 7)
        f = random.choice([i for i in range(-7, 8) if i != 0])
        f1 = fmt_linear(a, b)
        f2 = fmt_linear(c, d)
        f3 = fmt_linear(e, f)
        d1 = fmt_div_n(a, b)
        d2 = fmt_div_n(c, d)
        d3 = fmt_div_n(e, f)
        kq = Rational(a**2, c * e)
        kq_str = fmt_frac(kq)
        raw_frac = f"\\dfrac{{{a**2}}}{{{c * e}}}"
        buoc_cuoi = f"= \\dfrac{{{a}^2}}{{{c} \\cdot {e}}} = {raw_frac} = {kq_str}" if raw_frac != kq_str else f"= \\dfrac{{{a}^2}}{{{c} \\cdot {e}}} = {kq_str}"
        noidungcauhoi = fix_sign(f"Tính giới hạn $\\lim \\dfrac{{({f1})^2}}{{({f2})({f3})}}$.")
        loigiai = fix_sign(f"Chia cả tử và mẫu cho $n^2$, ta được: $$\\lim \\dfrac{{({f1})^2}}{{({f2})({f3})}} = \\lim \\dfrac{{\\left({d1}\\right)^2}}{{\\left({d2}\\right)\\left({d3}\\right)}} {buoc_cuoi}.$$")
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content

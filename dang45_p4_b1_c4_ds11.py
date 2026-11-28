
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


def bt_dang45_p4_b1_c4_ds11(self):
    def fix_sign(s):
        return s.replace('+ -', '- ').replace('- -', '+ ').replace('+-', '-').replace('--', '+')
    def fmt_term_first(coef, base, shift):
        exp_str = "n" if shift == 0 else f"n+{shift}"
        if coef == 1:
            return f"{base}^{{{exp_str}}}"
        if coef == -1:
            return f"-{base}^{{{exp_str}}}"
        return f"{coef} \\cdot {base}^{{{exp_str}}}"
    def fmt_term_next(coef, base, shift):
        exp_str = "n" if shift == 0 else f"n+{shift}"
        if coef == 1:
            return f"+ {base}^{{{exp_str}}}"
        if coef == -1:
            return f"- {base}^{{{exp_str}}}"
        if coef > 0:
            return f"+ {coef} \\cdot {base}^{{{exp_str}}}"
        return f"- {abs(coef)} \\cdot {base}^{{{exp_str}}}"
    def fmt_frac(val):
        if val.q == 1:
            return str(val.p)
        if val < 0:
            return f"-\\dfrac{{{abs(val.p)}}}{{{val.q}}}"
        return f"\\dfrac{{{val.p}}}{{{val.q}}}"
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        p, q = random.choice([(2, 3), (2, 5), (3, 4), (3, 5), (4, 5)])
        a = random.choice([i for i in range(-7, 8) if i != 0])
        b = random.choice([i for i in range(-7, 8) if i != 0])
        c = random.randint(1, 5)
        d = random.choice([i for i in range(-7, 8) if i != 0])
        k1 = random.choice([1, 2])
        k2 = random.choice([1, 2])
        k3 = random.choice([1, 2])
        tu = f"{fmt_term_first(a, p, 0)} {fmt_term_next(b, q, k1)}"
        mau = f"{fmt_term_first(c, q, k2)} {fmt_term_next(d, p, k3)}"
        B = b * (q**k1)
        C = c * (q**k2)
        D = d * (p**k3)
        tu_rut = f"{fmt_term_first(a, p, 0)} {fmt_term_next(B, q, 0)}"
        mau_rut = f"{fmt_term_first(C, q, 0)} {fmt_term_next(D, p, 0)}"
        ratio_str = f"\\left(\\dfrac{{{p}}}{{{q}}}\\right)^n"
        tu_chia = f"{a} \\cdot {ratio_str} + {B}" if B > 0 else f"{a} \\cdot {ratio_str} - {abs(B)}"
        mau_chia = f"{C} + {D} \\cdot {ratio_str}" if D > 0 else f"{C} - {abs(D)} \\cdot {ratio_str}"
        kq = Rational(B, C)
        kq_str = fmt_frac(kq)
        raw_frac = f"\\dfrac{{{B}}}{{{C}}}" if B > 0 else f"-\\dfrac{{{abs(B)}}}{{{C}}}"
        buoc_cuoi = f"= {raw_frac} = {kq_str}" if raw_frac != kq_str else f"= {kq_str}"
        noidungcauhoi = fix_sign(f"Tính giới hạn $\\lim \\dfrac{{{tu}}}{{{mau}}}$.")
        loigiai = fix_sign(f"Chia cả tử và mẫu cho ${q}^n$, ta được: $$\\lim \\dfrac{{{tu}}}{{{mau}}} = \\lim \\dfrac{{{tu_rut}}}{{{mau_rut}}} = \\lim \\dfrac{{{tu_chia}}}{{{mau_chia}}} {buoc_cuoi}$$ (do $\\lim {ratio_str} = 0$).")
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content

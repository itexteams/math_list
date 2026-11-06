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


def bt_dang3_p3_b4_c1_ds11(self):
            # Khai báo biến
            x, k = symbols('x k', real=True, integer=True)
            a = random.choice([i for i in range(-6, 7) if i not in (0, 1, -1)])
            b = random.choice([i for i in range(-6, 7) if i != 0])
            abs_b = abs(b)

            if b > 0:
                shift_latex = rf"x + \dfrac{{\pi}}{{{b}}}"
            else:
                shift_latex = rf"x - \dfrac{{\pi}}{{{abs_b}}}"

            x1_expr = (pi/b + 2*k*pi)/(a-1)
            x2_expr = (pi - pi/b + 2*k*pi)/(a+1)

            # Nhánh 1
            A1 = pi/b
            B1 = a - 1
            if B1 > 0:
                bound1 = -A1/(2*pi)
                k1 = math.ceil(float(bound1))
            else:
                bound1 = -A1/(2*pi)
                k1 = math.floor(float(bound1))
            x1_val = float(N(x1_expr.subs(k, k1)))
            x1_sym = x1_expr.subs(k, k1)

            # Nhánh 2
            A2 = pi - pi/b
            B2 = a + 1
            if B2 > 0:
                bound2 = -A2/(2*pi)
                k2 = math.ceil(float(bound2))
            else:
                bound2 = -A2/(2*pi)
                k2 = math.floor(float(bound2))
            x2_val = float(N(x2_expr.subs(k, k2)))
            x2_sym = x2_expr.subs(k, k2)

            # Chọn nghiệm dương nhỏ nhất
            candidates = [(x1_val, x1_sym, k1), (x2_val, x2_sym, k2)]
            candidates = [c for c in candidates if c[0] > 0]
            if not candidates:
                raise ValueError("Không có nghiệm dương nhỏ nhất!") # Lý thuyết thì không xảy ra với a≠0,±1; b≠0
            final_val, final_sym, final_k = min(candidates, key=lambda t: t[0])
            final_val_round = round(final_val, 1)

            noidungcauhoi = rf"""Tìm nghiệm dương nhỏ nhất của phương trình: $\sin({a}x) = \sin\left({shift_latex}\right)$. (kết quả làm tròn đến hàng phần mười)"""

            loigiai = rf"""Ta có: $\sin({a}x) = \sin\left({shift_latex}\right)$\\
            $\Leftrightarrow \hoac{{
                {a}x = {shift_latex} + 2k\pi \\
                {a}x = \pi - ({shift_latex}) + 2k\pi}}$
            $\Leftrightarrow \hoac{{
                x = {latex(simplify(x1_expr))} \quad (1)\\
                x = {latex(simplify(x2_expr))} \quad (2) }}$\\
            + Xét nhánh (1): Để $x>0$ và $x$ nhỏ nhất thì $k={k1}$, khi đó $x_1 = {latex(simplify(x1_sym))} \approx {x1_val:.2f}$.\\
            + Xét nhánh (2): Để $x>0$ và $x$ nhỏ nhất thì $k={k2}$, khi đó $x_2 = {latex(simplify(x2_sym))} \approx {x2_val:.2f}$.\\
            So sánh hai nghiệm $x_1; x_2$, ta thấy nghiệm dương nhỏ nhất là: $x \approx {final_val_round}$."""

            kq = str(final_val_round).replace('.', ',')
            dapan = rf"\shortans[0]{{{kq}}}"

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('+-', '-').replace('-+', '-').replace('--', '+').replace('++', '+').replace('\\frac', '\\dfrac')
            return content       


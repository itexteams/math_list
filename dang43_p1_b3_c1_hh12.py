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


def bt_dang43_p1_b3_c1_hh12(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        m = sp.Symbol('m')
        nice_u_list = [(2, -2, 1), (-2, 1, 2), (1, 2, -2), (3, 4, 0), (4, 0, -3), (2, 3, 6), (6, -2, -3)]
        u1, u2, u3 = random.choice(nice_u_list)
        U = u1**2 + u2**2 + u3**2
        len_u = int(math.sqrt(U))
        valid_params = []
        for a in range(-5, 6):
            for b in range(-4, 5):
                if b == 0: continue
                poly = m**2 + b**2 + (m+a)**2 - U
                discr = sp.discriminant(poly, m)
                if discr > 0:
                    sq = int(math.sqrt(discr))
                    if sq*sq == discr:
                        valid_params.append((a, b, 2))
                elif discr == 0:
                    valid_params.append((a, b, 1))
                elif discr < 0:
                    valid_params.append((a, b, 0))
        a, b, ans_val = random.choice(valid_params)
        def format_vec_i_j_k(cx, cy, cz):
            res = ""
            if cx != 0:
                if cx == 1: res += "\\vec{i}"
                elif cx == -1: res += "-\\vec{i}"
                else: res += f"{cx}\\vec{{i}}"
            if cy != 0:
                sign = "+" if cy > 0 else "-"
                abs_y = abs(cy)
                if res: res += sign
                elif sign == "-": res += "-"
                if abs_y == 1: res += "\\vec{j}"
                else: res += f"{abs_y}\\vec{{j}}"
            if cz != 0:
                sign = "+" if cz > 0 else "-"
                abs_z = abs(cz)
                if res: res += sign
                elif sign == "-": res += "-"
                if abs_z == 1: res += "\\vec{k}"
                else: res += f"{abs_z}\\vec{{k}}"
            return res
        vec_u_str = format_vec_i_j_k(u1, u2, u3)
        def format_m_plus_a(ca):
            if ca == 0: return "m"
            elif ca > 0: return f"m+{ca}"
            else: return f"m{ca}"
        m_plus_a_str = format_m_plus_a(a)
        vec_v_str = f"({m};{b};{m_plus_a_str})"
        da = f"${ans_val}$"
        s_set = set()
        s_set.add("$0$")
        s_set.add("$1$")
        s_set.add("$2$")
        s_set.add("$3$")
        s_set.add("$4$")
        if da in s_set:
            s_set.remove(da)
        s = list(s_set)
        random.shuffle(s)
        das1 = s[0]
        das2 = s[1]
        das3 = s[2]
        noidungcauhoi = f"Trong không gian $Oxyz$, cho các véc tơ $\\vec{{u}} = {vec_u_str}, \\vec{{v}} = {vec_v_str}$ với $m$ là tham số thực. Có bao nhiêu giá trị của $m$ để $|\\vec{{u}}| = |\\vec{{v}}|$?"
        da_d = '\\True ' + str(da)
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
        A = 2
        B = 2*a
        C = a**2 + b**2 - U
        gcd = math.gcd(abs(A), math.gcd(abs(B), abs(C)))
        A_simp = A // gcd
        B_simp = B // gcd
        C_simp = C // gcd
        def format_poly(cA, cB, cC):
            res = ""
            if cA == 1: res += "m^2"
            elif cA == -1: res += "-m^2"
            else: res += f"{cA}m^2"
            if cB > 0: res += f"+{cB}m" if cB != 1 else "+m"
            elif cB < 0: res += f"{cB}m" if cB != -1 else "-m"
            if cC > 0: res += f"+{cC}"
            elif cC < 0: res += f"{cC}"
            return res
        poly_str = format_poly(A, B, a**2 + b**2)
        poly_eq_str = format_poly(A, B, C)
        poly_simp_str = format_poly(A_simp, B_simp, C_simp)
        if gcd != 1 and (A!=A_simp or B!=B_simp or C!=C_simp):
            eq_str = f"{U} = {poly_str} \\Leftrightarrow {poly_eq_str} = 0 \\Leftrightarrow {poly_simp_str} = 0"
        else:
            eq_str = f"{U} = {poly_str} \\Leftrightarrow {poly_eq_str} = 0"
        if ans_val == 2:
            roots = sp.solve(A_simp*m**2 + B_simp*m + C_simp, m)
            r1_str = sp.latex(roots[0])
            r2_str = sp.latex(roots[1])
            solve_str = f"\\Leftrightarrow \\left[ \\begin{{matrix}} m = {r1_str} \\\\ m = {r2_str} \\end{{matrix}} \\right."
            conclude_str = f"Vậy có $2$ giá trị của $m$ thỏa yêu cầu bài toán."
        elif ans_val == 1:
            roots = sp.solve(A_simp*m**2 + B_simp*m + C_simp, m)
            r1_str = sp.latex(roots[0])
            solve_str = f"\\Leftrightarrow m = {r1_str}"
            conclude_str = f"Vậy có $1$ giá trị của $m$ thỏa yêu cầu bài toán."
        else:
            solve_str = "\\text{ (Vô nghiệm)}"
            conclude_str = f"Vậy có $0$ giá trị của $m$ thỏa yêu cầu bài toán."
        def format_sq(val):
            if val < 0: return f"({val})^2"
            return f"{val}^2"
        loigiai = f"Ta có $\\vec{{u}} = ({u1};{u2};{u3})$. Khi đó: $|\\vec{{u}}| = \\sqrt{{{format_sq(u1)} + {format_sq(u2)} + {format_sq(u3)}}} = {len_u}$. \\\\\n$|\\vec{{v}}| = \\sqrt{{m^2 + {format_sq(b)} + ({m_plus_a_str})^2}} = \\sqrt{{{poly_str}}}$. \\\\\nDo đó $|\\vec{{u}}| = |\\vec{{v}}| \\Leftrightarrow {eq_str} {solve_str}$ \\\\\n{conclude_str}"
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
        '\\choice \n'
        '{'+str(list_1[1])+'}\n'
        '{'+str(list_1[2])+'}\n'
        '{'+str(list_1[3])+'}\n'
        '{'+str(list_1[0])+'}\n'
        '\\loigiai{\n'+str(loigiai)+'\n}\n'
        '\\end{ex}\n\\end{minipage} \n\n')
    content = content.replace("+-", "-").replace("- -", "+").replace("--", "+").replace("+ -", "-")
    return content


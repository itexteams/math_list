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


def bt_dang38_p1_b3_c1_hh12(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        m_sym, n_sym, p_sym = symbols('m n p')
        while True:
            a1, a2, a3 = randint(-4, 4), randint(-4, 4), randint(-4, 4)
            b1, b2, b3 = randint(-4, 4), randint(-4, 4), randint(-4, 4)
            c1, c2, c3 = randint(-4, 4), randint(-4, 4), randint(-4, 4)
            M = Matrix([[a1, b1, c1], [a2, b2, c2], [a3, b3, c3]])
            if M.det() != 0:
                d1, d2, d3 = randint(-5, 5), randint(-5, 5), randint(-5, 5)
                sol = M.LUsolve(Matrix([d1, d2, d3]))
                m_val, n_val, p_val = sol[0], sol[1], sol[2]
                if m_val != 0 and n_val != 0 and p_val != 0:
                    break
        def f_vec(m, n, p):
            res = f"\\vec{{d}}={latex(m)}\\vec{{a}}+{latex(n)}\\vec{{b}}+{latex(p)}\\vec{{c}}"
            return res
        da = f"${f_vec(m_val, n_val, p_val)}$"
        s_set = set()
        s_set.add(f"${f_vec(-m_val, -n_val, -p_val)}$")
        s_set.add(f"${f_vec(-m_val, n_val, p_val)}$")
        s_set.add(f"${f_vec(m_val, p_val, n_val)}$")
        s_set.add(f"${f_vec(-m_val, p_val, n_val)}$")
        s_set.add(f"${f_vec(n_val, m_val, p_val)}$")
        if da in s_set: s_set.remove(da)
        s = list(s_set)
        random.shuffle(s)
        das1, das2, das3 = s[0], s[1], s[2]
        noidungcauhoi = f"Trong không gian $Oxyz$, cho $\\vec{{a}}=({a1};{a2};{a3})$, $\\vec{{b}}=({b1};{b2};{b3})$, $\\vec{{c}}=({c1};{c2};{c3})$, $\\vec{{d}}=({d1};{d2};{d3})$. Hãy phân tích vectơ $\\vec{{d}}$ theo 3 vectơ $\\vec{{a}}, \\vec{{b}}, \\vec{{c}}$."
        da_d = '\\True ' + str(da)
        list_1 = [da_d, str(das1), str(das2), str(das3)]
        random.shuffle(list_1)
        def f_eq(c1, c2, c3):
            r = ""
            if c1 == 1: r += "m"
            elif c1 == -1: r += "-m"
            elif c1 != 0: r += f"{c1}m"
            if c2 == 1: r += "+n"
            elif c2 == -1: r += "-n"
            elif c2 > 0: r += f"+{c2}n"
            elif c2 < 0: r += f"{c2}n"
            if c3 == 1: r += "+p"
            elif c3 == -1: r += "-p"
            elif c3 > 0: r += f"+{c3}p"
            elif c3 < 0: r += f"{c3}p"
            if r.startswith("+"): r = r[1:]
            return r
        eq1 = f"{f_eq(a1, b1, c1)}={d1}"
        eq2 = f"{f_eq(a2, b2, c2)}={d2}"
        eq3 = f"{f_eq(a3, b3, c3)}={d3}"
        loigiai = f"Giả sử $\\vec{{d}}=m\\vec{{a}}+n\\vec{{b}}+p\\vec{{c}} \\Leftrightarrow \\begin{{cases}} {eq1} \\\\ {eq2} \\\\ {eq3} \\end{{cases}} \\Leftrightarrow m={latex(m_val)}, n={latex(n_val)}, p={latex(p_val)}$."
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


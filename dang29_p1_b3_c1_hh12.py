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


def bt_dang29_p1_b3_c1_hh12(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        target_cosines = [0, sp.Rational(1,2), -sp.Rational(1,2), sp.sqrt(2)/2, -sp.sqrt(2)/2, sp.sqrt(3)/2, -sp.sqrt(3)/2]
        while True:
            a1, a2, a3 = randint(-3, 3), randint(-3, 3), randint(-3, 3)
            b1, b2, b3 = randint(-3, 3), randint(-3, 3), randint(-3, 3)
            if (a1, a2, a3) == (0, 0, 0) or (b1, b2, b3) == (0, 0, 0): continue
            dot_prod = a1*b1 + a2*b2 + a3*b3
            len_a_sq = a1**2 + a2**2 + a3**2
            len_b_sq = b1**2 + b2**2 + b3**2
            cos_val = sp.Rational(dot_prod, 1) / sp.sqrt(len_a_sq * len_b_sq)
            if cos_val in target_cosines:
                break
        def f_p(num): return f"({num})" if num < 0 else str(num)
        tu_str = f"{f_p(a1)}.{f_p(b1)} + {f_p(a2)}.{f_p(b2)} + {f_p(a3)}.{f_p(b3)}"
        mau_str = f"\\sqrt{{{f_p(a1)}^2 + {f_p(a2)}^2 + {f_p(a3)}^2}} . \\sqrt{{{f_p(b1)}^2 + {f_p(b2)}^2 + {f_p(b3)}^2}}"
        cos_latex = latex(cos_val)
        angle_rad = sp.acos(cos_val)
        angle_deg = int(angle_rad * 180 / sp.pi)
        kq = f"{angle_deg}^\\circ"
        da = f"${kq}$"
        all_angles = [30, 45, 60, 90, 120, 135, 150]
        if angle_deg in all_angles: all_angles.remove(angle_deg)
        random.shuffle(all_angles)
        s_set = set([f"${a}^\\circ$" for a in all_angles[:3]])
        s = list(s_set)
        das1, das2, das3 = s[0], s[1], s[2]
        noidungcauhoi = f"Trong không gian $Oxyz$, tính góc giữa hai vectơ $\\vec{{a}}=({a1};{a2};{a3})$ và $\\vec{{b}}=({b1};{b2};{b3})$."
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
        loigiai = f"Ta có $\\cos(\\vec{{a}}, \\vec{{b}}) = \\frac{{\\vec{{a}}.\\vec{{b}}}}{{|\\vec{{a}}|.|\\vec{{b}}|}} = \\frac{{{tu_str}}}{{{mau_str}}} = {cos_latex}\\\\ \\Rightarrow (\\vec{{a}}, \\vec{{b}}) = {kq}$."
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


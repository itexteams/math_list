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


def bt_dang35_p1_b3_c1_hh12(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        while True:
            u1, u2, u3 = randint(-4, 4), randint(-4, 4), randint(-4, 4)
            if (u1, u2, u3) != (0, 0, 0):
                break
        k = random.choice([-5, -4, -3, -2, -1, 2, 3, 4, 5])
        mod_u_sq = u1**2 + u2**2 + u3**2
        P = k * mod_u_sq
        v1, v2, v3 = k*u1, k*u2, k*u3
        kq_str = f"({v1};{v2};{v3})"
        da = f"${kq_str}$"
        s_set = set()
        s_set.add(f"$({-v1};{-v2};{-v3})$")
        k_sai1 = k + 1 if k != -1 else 2
        s_set.add(f"$({k_sai1*u1};{k_sai1*u2};{k_sai1*u3})$")
        k_sai2 = k - 1 if k != 1 else -2
        s_set.add(f"$({k_sai2*u1};{k_sai2*u2};{k_sai2*u3})$")
        s_set.add(f"$({v1+1};{v2-1};{v3})$")
        if da in s_set:
            s_set.remove(da)
        s = list(s_set)
        random.shuffle(s)
        das1, das2, das3 = s[0], s[1], s[2]
        def format_k(c):
            if c == 0: return "0"
            if c == 1: return "k"
            if c == -1: return "-k"
            return f"{c}k"
        def format_k2(c_sq):
            if c_sq == 1: return "k"
            return f"{c_sq}k"
        vk_str = f"({format_k(u1)};{format_k(u2)};{format_k(u3)})"
        terms = [format_k2(c**2) for c in [u1, u2, u3] if c != 0]
        eq_left = " + ".join(terms)
        noidungcauhoi = f"Trong không gian $Oxyz$, cho vectơ $\\vec{{u}}({u1};{u2};{u3})$. Tìm vectơ $\\vec{{v}}$ biết $\\vec{{v}}$ cùng phương với $\\vec{{u}}$ và $\\vec{{u}}.\\vec{{v}} = {P}$."
        da_d = '\\True ' + str(da)
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
        dk_k = f"k > 0" if k > 0 else f"k < 0"
        loigiai = f"Vì $\\vec{{v}}$ cùng phương với $\\vec{{u}}$ nên $\\vec{{v}} = k.\\vec{{u}} = {vk_str}$, với ${dk_k}$. \\\\\nTa có $\\vec{{u}}.\\vec{{v}} = {eq_left} = {mod_u_sq}k = {P} \\Leftrightarrow k = {k}$. Vậy $\\vec{{v}} = {kq_str}$."
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


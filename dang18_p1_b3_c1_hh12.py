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


def bt_dang18_p1_b3_c1_hh12(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        while True:
            u1, u2, u3 = randint(-3, 4), randint(-3, 4), randint(-3, 4)
            v1, v2, v3 = randint(-3, 4), randint(-3, 4), randint(-3, 4)
            if (u1, u2, u3) != (0, 0, 0) and (v1, v2, v3) != (0, 0, 0):
                break
        k = random.choice([-3, -2, 2, 3])
        def f_p(num): return f"({num})" if num < 0 else str(num)
        mod_u_sq = u1**2 + u2**2 + u3**2
        mod_v_sq = v1**2 + v2**2 + v3**2
        uv_dot = u1*v1 + u2*v2 + u3*v3
        term2_coef = 2 * k
        term3_coef = k**2
        val_term2 = term2_coef * uv_dot
        val_term3 = term3_coef * mod_v_sq
        ans_sq = mod_u_sq + val_term2 + val_term3
        kq = sp.sqrt(ans_sq)
        ans_latex = latex(kq)
        k_str = f"+ {k}" if k > 0 else f"- {abs(k)}"
        term2_str = f"+ {term2_coef}" if term2_coef > 0 else f"- {abs(term2_coef)}"
        val_term2_str = f"+ {val_term2}" if val_term2 > 0 else f"- {abs(val_term2)}"
        if val_term2 == 0: val_term2_str = "+ 0"
        s_set = set()
        w1_sq = mod_u_sq + 2*uv_dot + mod_v_sq # Sai: Quên nhân hệ số k
        w2_sq = mod_u_sq - val_term2 + val_term3 # Sai: Nhầm dấu cụm 2(u.v)
        w3_sq = ans_sq + random.choice([2, 3, 5]) # Sai: Tính toán nhầm
        w4_sq = abs(ans_sq - random.choice([2, 3, 4])) 
        if w4_sq == 0: w4_sq = ans_sq + 1
        s_set.add(f"${latex(sp.sqrt(w1_sq))}$")
        s_set.add(f"${latex(sp.sqrt(w2_sq))}$")
        s_set.add(f"${latex(sp.sqrt(w3_sq))}$")
        s_set.add(f"${latex(sp.sqrt(w4_sq))}$")
        da = f"${ans_latex}$"
        if da in s_set:
            s_set.remove(da) # Đảm bảo đáp án đúng không nằm trong set nhiễu
        s = list(s_set)
        random.shuffle(s)
        das1, das2, das3 = s[0], s[1], s[2]
        noidungcauhoi = f"Trong không gian $Oxyz$, cho hai vectơ $\\vec{{u}} = ({u1}; {u2}; {u3})$ và $\\vec{{v}} = ({v1}; {v2}; {v3})$. Tính $|\\vec{{u}} {k_str}\\vec{{v}}|$."
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2) 
        da_s3 = str(das3) 
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
        loigiai = (
            f"Ta có $|\\vec{{u}}| = \\sqrt{{{mod_u_sq}}}; |\\vec{{v}}| = \\sqrt{{{mod_v_sq}}}; \\vec{{u}}\\vec{{v}} = {u1}.{f_p(v1)} + {u2}.{f_p(v2)} + {u3}.{f_p(v3)} = {uv_dot}$. \\\\\n"
            f"Suy ra $|\\vec{{u}} {k_str}\\vec{{v}}|^2 = |\\vec{{u}}|^2 {term2_str}\\vec{{u}}\\vec{{v}} + {term3_coef}|\\vec{{v}}|^2 = {mod_u_sq} {val_term2_str} + {val_term3} = {ans_sq}$. \\\\\n"
            f"Vậy $|\\vec{{u}} {k_str}\\vec{{v}}| = {ans_latex}$."
        )
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



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


def bt_dang9_p4_b3_c2_hh10(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        bo_ten = [
            ('A', 'B', 'C', 'H'),
            ('M', 'N', 'P', 'H'),
            ('D', 'E', 'F', 'I'),
            ('P', 'Q', 'R', 'K')
        ]
        A, B, C, H = random.choice(bo_ten)
        tamgiac = A + B + C
        a_sym = symbols('a', positive=True)
        k = randint(1, 6)
        canh = k * a_sym
        nua_canh = simplify(canh / 2)
        kq_a = simplify(2 * canh)
        kq_b = simplify(canh * sqrt(3))
        ds_dinh = [A, B, C]
        u, v, w = random.sample(ds_dinh, 3)
        vec_a_list = [f'\\overrightarrow{{{u}{v}}}', f'\\overrightarrow{{{u}{w}}}', f'\\overrightarrow{{{v}{w}}}']
        random.shuffle(vec_a_list)
        bt_a = ' + '.join(vec_a_list)
        P, Q, R = random.sample(ds_dinh, 3)
        bt_b = f'\\overrightarrow{{{P}{Q}}} + \\overrightarrow{{{P}{R}}}'
        canh_sq_str = f'{latex(canh)}^2' if k == 1 else f'\\left({latex(canh)}\\right)^2'
        nua_sq_str = f'\\left({latex(nua_canh)}\\right)^2'
        hinhve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[line width=1pt, scale=1]\n'
            f'\\coordinate ({Q}) at (0,0);\n'
            f'\\coordinate ({R}) at (4,0);\n'
            f'\\coordinate ({P}) at (2,3.46);\n'
            f'\\coordinate ({H}) at (2,0);\n'
            f'\\draw ({P})--({Q})--({R})--cycle;\n'
            f'\\draw ({P})--({H});\n'
            f'\\fill ({P}) circle (1.5pt) node[above] {{${P}$}};\n'
            f'\\fill ({Q}) circle (1.5pt) node[left] {{${Q}$}};\n'
            f'\\fill ({R}) circle (1.5pt) node[right] {{${R}$}};\n'
            f'\\fill ({H}) circle (1.5pt) node[below] {{${H}$}};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}\n'
        )
        noidungcauhoi = (
            f'Cho tam giác đều ${tamgiac}$ cạnh ${latex(canh)}$. Tính\n'
            + hinhve +
            f'a) $\\left|{bt_a}\\right|$ \\\\\n'
            f'b) $\\left|{bt_b}\\right|$ \\\\\n'
        )
        loigiai = (
            hinhve +
            '\\begin{enumEX}[a)]{1}\n'
            f'\\item $\\left|{bt_a}\\right| = \\left|\\left(\\overrightarrow{{{u}{v}}} + \\overrightarrow{{{v}{w}}}\\right) + \\overrightarrow{{{u}{w}}}\\right| = \\left|\\overrightarrow{{{u}{w}}} + \\overrightarrow{{{u}{w}}}\\right| = \\left|2\\overrightarrow{{{u}{w}}}\\right| = 2\\left|\\overrightarrow{{{u}{w}}}\\right| = 2{u}{w} = {latex(kq_a)}$.\n'
            f'\\item Gọi ${H}$ là trung điểm của ${Q}{R}$.\\\\\n'
            f'Ta có: $\\left|{bt_b}\\right| = \\left|2\\overrightarrow{{{P}{H}}}\\right| = 2\\left|\\overrightarrow{{{P}{H}}}\\right| = 2{P}{H} = 2\\sqrt{{{P}{Q}^2 - {Q}{H}^2}} = 2\\sqrt{{{canh_sq_str} - {nua_sq_str}}} = {latex(kq_b)}$.\n'
            '\\end{enumEX}\n'
        )
        noidungcauhoi = noidungcauhoi.replace('- -', '+').replace('+ -', '-')
        loigiai = loigiai.replace('- -', '+').replace('+ -', '-')
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
    return content

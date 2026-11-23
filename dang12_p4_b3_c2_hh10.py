
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


def bt_dang12_p4_b3_c2_hh10(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        bo_ten = [
            ('A', 'B', 'C', 'D', 'O', 'G', "G'"),
            ('M', 'N', 'P', 'Q', 'O', 'G_1', 'G_2'),
            ('E', 'F', 'K', 'H', 'I', 'G', "G'"),
            ('A', 'B', 'C', 'D', 'I', 'G_1', 'G_2')
        ]
        A, B, C, D, O, G1, G2 = random.choice(bo_ten)
        tugiac = A + B + C + D
        coords = {
            O: (0.0, 0.0),
            A: (-1.8, 0.2),
            C: (4.5, -0.5),
            B: (0.3, 1.8),
            D: (-0.4, -2.4)
        }
        kieu = random.choice([1, 2, 3, 4])
        if kieu == 1:
            u1, v1, u2, v2 = A, B, C, D
        elif kieu == 2:
            u1, v1, u2, v2 = C, D, A, B
        elif kieu == 3:
            u1, v1, u2, v2 = A, D, C, B
        else:
            u1, v1, u2, v2 = C, B, A, D
        g1x = round((coords[O][0] + coords[u1][0] + coords[v1][0]) / 3, 2)
        g1y = round((coords[O][1] + coords[u1][1] + coords[v1][1]) / 3, 2)
        g2x = round((coords[O][0] + coords[u2][0] + coords[v2][0]) / 3, 2)
        g2y = round((coords[O][1] + coords[u2][1] + coords[v2][1]) / 3, 2)
        m1x = round((coords[O][0] + coords[v1][0]) / 2, 2)
        m1y = round((coords[O][1] + coords[v1][1]) / 2, 2)
        m2x = round((coords[O][0] + coords[u2][0]) / 2, 2)
        m2y = round((coords[O][1] + coords[u2][1]) / 2, 2)
        pos_g1 = 'above' if g1y >= 0 else 'below'
        pos_g2 = 'above' if g2y >= 0 else 'below'
        hinhve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[line width=1pt, scale=1]\n'
            f'\\coordinate ({O}) at (0,0);\n'
            f'\\coordinate ({A}) at (-1.8,0.2);\n'
            f'\\coordinate ({C}) at (4.5,-0.5);\n'
            f'\\coordinate ({B}) at (0.3,1.8);\n'
            f'\\coordinate ({D}) at (-0.4,-2.4);\n'
            f'\\coordinate (M1) at ({m1x},{m1y});\n'
            f'\\coordinate (M2) at ({m2x},{m2y});\n'
            f'\\coordinate (G1) at ({g1x},{g1y});\n'
            f'\\coordinate (G2) at ({g2x},{g2y});\n'
            f'\\draw ({A})--({B})--({C})--({D})--cycle;\n'
            f'\\draw ({A})--({C}) ({B})--({D}) ({u1})--(M1) ({v2})--(M2) (G1)--(G2);\n'
            f'\\fill ({A}) circle (1.5pt) node[left] {{${A}$}};\n'
            f'\\fill ({B}) circle (1.5pt) node[above] {{${B}$}};\n'
            f'\\fill ({C}) circle (1.5pt) node[right] {{${C}$}};\n'
            f'\\fill ({D}) circle (1.5pt) node[below] {{${D}$}};\n'
            f'\\fill ({O}) circle (1.5pt) node[below left] {{${O}$}};\n'
            f'\\fill (G1) circle (1.5pt) node[{pos_g1}] {{${G1}$}};\n'
            f'\\fill (G2) circle (1.5pt) node[{pos_g2}] {{${G2}$}};\n'
            '\\fill (M1) circle (1.5pt);\n'
            '\\fill (M2) circle (1.5pt);\n'
            '\\end{tikzpicture}\n'
            '\\end{center}\n'
        )
        noidungcauhoi = f'Cho tứ giác ${tugiac}$, ${O}$ là giao điểm của hai đường chéo ${A}{C}$ và ${B}{D}$. Gọi ${G1}, {G2}$ theo thứ tự là trọng tâm của tam giác ${O}{u1}{v1}$ và ${O}{u2}{v2}$. Chứng minh rằng $\\overrightarrow{{{u1}{u2}}} + \\overrightarrow{{{v1}{v2}}} = 3\\overrightarrow{{{G1}{G2}}}$.\n'
        loigiai = (
            hinhve +
            f'Vì ${G2}$ là trọng tâm của tam giác ${O}{u2}{v2}$ nên ta có: $\\overrightarrow{{{G1}{G2}}} = \\dfrac{{1}}{{3}}\\left(\\overrightarrow{{{G1}{O}}} + \\overrightarrow{{{G1}{u2}}} + \\overrightarrow{{{G1}{v2}}}\\right) \\quad (1)$.\\\\\n'
            f'Vì ${G1}$ là trọng tâm của tam giác ${O}{u1}{v1}$ nên ta có $\\overrightarrow{{{G1}{O}}} + \\overrightarrow{{{G1}{u1}}} + \\overrightarrow{{{G1}{v1}}} = \\vec{{0}} \\Rightarrow \\overrightarrow{{{G1}{O}}} = -\\left(\\overrightarrow{{{G1}{u1}}} + \\overrightarrow{{{G1}{v1}}}\\right) \\quad (2)$.\\\\\n'
            f'Từ $(1)$ và $(2) \\Rightarrow \\overrightarrow{{{G1}{G2}}} = \\dfrac{{1}}{{3}}\\left(\\overrightarrow{{{G1}{u2}}} - \\overrightarrow{{{G1}{u1}}} + \\overrightarrow{{{G1}{v2}}} - \\overrightarrow{{{G1}{v1}}}\\right) = \\dfrac{{1}}{{3}}\\left(\\overrightarrow{{{u1}{u2}}} + \\overrightarrow{{{v1}{v2}}}\\right) \\Rightarrow \\overrightarrow{{{u1}{u2}}} + \\overrightarrow{{{v1}{v2}}} = 3\\overrightarrow{{{G1}{G2}}}$.\n'
        )
        noidungcauhoi = noidungcauhoi.replace('- -', '+').replace('+ -', '-')
        loigiai = loigiai.replace('- -', '+').replace('+ -', '-')
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
    return content

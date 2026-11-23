
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


def bt_dang14_p4_b3_c2_hh10(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        bo_ten = [
            ('A', 'B', 'C', 'H', 'O', 'G', 'D', 'M', 'E', 'F'),
            ('M', 'N', 'P', 'H', 'O', 'G', 'D', 'I', 'E', 'F'),
            ('A', 'B', 'C', 'H', 'I', 'G', 'K', 'M', 'E', 'F'),
            ('P', 'Q', 'R', 'H', 'O', 'G', 'D', 'M', 'E', 'F')
        ]
        A, B, C, H, O, G, D, M, E, F = random.choice(bo_ten)
        tamgiac = A + B + C
        kieu = random.choice([1, 2, 3, 4])
        if kieu == 1:
            yeucau = f'$\\overrightarrow{{{O}{H}}} = 3\\overrightarrow{{{O}{G}}}$'
            ketluan = f'Do ${G}$ là trọng tâm của tam giác ${tamgiac}$ nên $\\overrightarrow{{{O}{A}}} + \\overrightarrow{{{O}{B}}} + \\overrightarrow{{{O}{C}}} = 3\\overrightarrow{{{O}{G}}} \\Rightarrow \\overrightarrow{{{O}{H}}} = 3\\overrightarrow{{{O}{G}}}$.'
        elif kieu == 2:
            yeucau = f'$\\overrightarrow{{{G}{H}}} + 2\\overrightarrow{{{G}{O}}} = \\vec{{0}}$'
            ketluan = f'Do ${G}$ là trọng tâm của tam giác ${tamgiac}$ nên $\\overrightarrow{{{O}{H}}} = 3\\overrightarrow{{{O}{G}}} \\Leftrightarrow \\overrightarrow{{{O}{G}}} + \\overrightarrow{{{G}{H}}} = 3\\overrightarrow{{{O}{G}}} \\Leftrightarrow \\overrightarrow{{{G}{H}}} - 2\\overrightarrow{{{O}{G}}} = \\vec{{0}} \\Leftrightarrow \\overrightarrow{{{G}{H}}} + 2\\overrightarrow{{{G}{O}}} = \\vec{{0}}$.'
        elif kieu == 3:
            yeucau = f'$\\overrightarrow{{{H}{G}}} = \\dfrac{{2}}{{3}}\\overrightarrow{{{H}{O}}}$'
            ketluan = f'Do ${G}$ là trọng tâm của tam giác ${tamgiac}$ nên $\\overrightarrow{{{O}{H}}} = 3\\overrightarrow{{{O}{G}}} \\Leftrightarrow \\overrightarrow{{{O}{H}}} = 3\\left(\\overrightarrow{{{O}{H}}} + \\overrightarrow{{{H}{G}}}\\right) \\Leftrightarrow 3\\overrightarrow{{{H}{G}}} = -2\\overrightarrow{{{O}{H}}} = 2\\overrightarrow{{{H}{O}}} \\Leftrightarrow \\overrightarrow{{{H}{G}}} = \\dfrac{{2}}{{3}}\\overrightarrow{{{H}{O}}}$.'
        else:
            yeucau = f'$\\overrightarrow{{{H}{A}}} + \\overrightarrow{{{H}{B}}} + \\overrightarrow{{{H}{C}}} = 2\\overrightarrow{{{H}{O}}}$'
            ketluan = f'Suy ra $\\overrightarrow{{{O}{H}}} = \\left(\\overrightarrow{{{O}{H}}} + \\overrightarrow{{{H}{A}}}\\right) + \\left(\\overrightarrow{{{O}{H}}} + \\overrightarrow{{{H}{B}}}\\right) + \\left(\\overrightarrow{{{O}{H}}} + \\overrightarrow{{{H}{C}}}\\right) = 3\\overrightarrow{{{O}{H}}} + \\overrightarrow{{{H}{A}}} + \\overrightarrow{{{H}{B}}} + \\overrightarrow{{{H}{C}}} \\Rightarrow \\overrightarrow{{{H}{A}}} + \\overrightarrow{{{H}{B}}} + \\overrightarrow{{{H}{C}}} = -2\\overrightarrow{{{O}{H}}} = 2\\overrightarrow{{{H}{O}}}$.'
        noidungcauhoi = f'Cho tam giác ${tamgiac}$ với ${H}, {O}, {G}$ lần lượt là trực tâm, tâm đường tròn ngoại tiếp và trọng tâm của tam giác. Chứng minh {yeucau}.\n'
        hinhve = (
            '\\begin{center}\n'
            '\\begin{tikzpicture}[line width=1pt, scale=1]\n'
            f'\\coordinate ({O}) at (0,0);\n'
            f'\\coordinate ({A}) at (-1.19,2.2);\n'
            f'\\coordinate ({B}) at (-2.24,-1.1);\n'
            f'\\coordinate ({C}) at (2.24,-1.1);\n'
            f'\\coordinate ({D}) at (1.19,-2.2);\n'
            f'\\coordinate ({M}) at (0,-1.1);\n'
            f'\\coordinate ({H}) at (-1.19,0);\n'
            f'\\coordinate ({G}) at (-0.4,0);\n'
            f'\\coordinate ({E}) at (-1.19,-1.1);\n'
            f'\\coordinate ({F}) at (-0.09,1.14);\n'
            f'\\draw ({O}) circle (2.5);\n'
            f'\\draw ({A})--({B})--({C})--cycle;\n'
            f'\\draw ({A})--({E}) ({B})--({F}) ({A})--({M}) ({O})--({M}) ({H})--({O}) ({A})--({D}) ({D})--({C});\n'
            f'\\fill ({A}) circle (1.5pt) node[above] {{${A}$}};\n'
            f'\\fill ({B}) circle (1.5pt) node[left] {{${B}$}};\n'
            f'\\fill ({C}) circle (1.5pt) node[right] {{${C}$}};\n'
            f'\\fill ({D}) circle (1.5pt) node[below] {{${D}$}};\n'
            f'\\fill ({O}) circle (1.5pt) node[below right] {{${O}$}};\n'
            f'\\fill ({H}) circle (1.5pt) node[above left] {{${H}$}};\n'
            f'\\fill ({G}) circle (1.5pt) node[below left] {{${G}$}};\n'
            f'\\fill ({M}) circle (1.5pt) node[below] {{${M}$}};\n'
            f'\\fill ({E}) circle (1.5pt) node[below] {{${E}$}};\n'
            f'\\fill ({F}) circle (1.5pt) node[above right] {{${F}$}};\n'
            '\\end{tikzpicture}\n'
            '\\end{center}\n'
        )
        loigiai = (
            hinhve +
            f'Gọi ${D}$ là điểm đối xứng của ${A}$ qua ${O}$ nên ta có ${B}{H} \\parallel {D}{C}$ (cùng vuông góc với ${A}{C}$) $(1)$.\\\\\n'
            f'Mặt khác ${C}{H} \\parallel {B}{D}$ (cùng vuông góc với ${A}{B}$) $(2)$.\\\\\n'
            f'Từ $(1)$ và $(2)$ suy ra tứ giác ${B}{H}{C}{D}$ là hình bình hành.\\\\\n'
            f'Gọi ${M}$ là trung điểm của ${B}{C}$, vậy ba điểm ${H}, {M}, {D}$ thẳng hàng $\\Rightarrow \\overrightarrow{{{A}{H}}} = 2\\overrightarrow{{{O}{M}}}$.\\\\\n'
            f'Ta có $\\overrightarrow{{{O}{H}}} = \\overrightarrow{{{O}{A}}} + \\overrightarrow{{{A}{H}}} = \\overrightarrow{{{O}{A}}} + 2\\overrightarrow{{{O}{M}}} = \\overrightarrow{{{O}{A}}} + \\overrightarrow{{{O}{B}}} + \\overrightarrow{{{O}{C}}}$.\\\\\n'
            + ketluan + '\n'
        )
        noidungcauhoi = noidungcauhoi.replace('- -', '+').replace('+ -', '-')
        loigiai = loigiai.replace('- -', '+').replace('+ -', '-')
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
    return content

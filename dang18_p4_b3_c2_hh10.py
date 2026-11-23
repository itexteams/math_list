
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


def bt_dang18_p4_b3_c2_hh10(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        bo_ten = [
            ('A', 'B', 'C', 'D', 'M', 'N'),
            ('M', 'N', 'P', 'Q', 'I', 'J'),
            ('E', 'F', 'G', 'H', 'M', 'N'),
            ('P', 'Q', 'R', 'S', 'I', 'K')
        ]
        A, B, C, D, M, N = random.choice(bo_ten)
        tugiac = A + B + C + D
        kieu_canh = random.choice([1, 2])
        if kieu_canh == 1:
            X1, X2, Y1, Y2 = A, D, B, C
        else:
            X1, X2, Y1, Y2 = A, B, D, C
        k = random.choice([1, 1, 2, 3])
        hk = '' if k == 1 else str(k)
        h2k = str(2 * k)
        them_buoc = '' if k == 1 else f' Nhân hai vế với ${k}$ ta được ${hk}\\overrightarrow{{{X1}{Y2}}} + {hk}\\overrightarrow{{{X2}{Y1}}} = {h2k}\\overrightarrow{{{M}{N}}}$.'
        them_buoc_b = '' if k == 1 else f' Nhân hai vế với ${k}$ ta được ${hk}\\overrightarrow{{{X1}{Y1}}} + {hk}\\overrightarrow{{{X2}{Y2}}} = {h2k}\\overrightarrow{{{M}{N}}}$.'
        them_buoc_c = '' if k == 1 else f' $\\Rightarrow {hk}\\overrightarrow{{{M}{Y1}}} + {hk}\\overrightarrow{{{M}{Y2}}} = {h2k}\\overrightarrow{{{M}{N}}}$'
        noidungcauhoi = (
            f'Gọi ${M}, {N}$ lần lượt là trung điểm các cạnh ${X1}{X2}, {Y1}{Y2}$ của tứ giác ${tugiac}$. Chứng minh các đẳng thức sau: \\\\\n'
            f'a) ${hk}\\overrightarrow{{{X1}{Y2}}} + {hk}\\overrightarrow{{{X2}{Y1}}} = {h2k}\\overrightarrow{{{M}{N}}}$. \\\\\n'
            f'b) ${hk}\\overrightarrow{{{X1}{Y1}}} + {hk}\\overrightarrow{{{X2}{Y2}}} = {h2k}\\overrightarrow{{{M}{N}}}$. \\\\\n'
            f'c) ${hk}\\overrightarrow{{{M}{Y1}}} + {hk}\\overrightarrow{{{M}{Y2}}} = {h2k}\\overrightarrow{{{M}{N}}}$. \\\\\n'
        )
        loigiai = (
            '\\begin{enumEX}[a)]{1}\n'
            f'\\item $2\\overrightarrow{{{M}{N}}} = \\overrightarrow{{{M}{N}}} + \\overrightarrow{{{M}{N}}} = \\left(\\overrightarrow{{{M}{X1}}} + \\overrightarrow{{{X1}{Y2}}} + \\overrightarrow{{{Y2}{N}}}\\right) + \\left(\\overrightarrow{{{M}{X2}}} + \\overrightarrow{{{X2}{Y1}}} + \\overrightarrow{{{Y1}{N}}}\\right)$\\\\\n'
            f'$= \\left(\\overrightarrow{{{X1}{Y2}}} + \\overrightarrow{{{X2}{Y1}}}\\right) + \\left(\\overrightarrow{{{M}{X1}}} + \\overrightarrow{{{M}{X2}}}\\right) + \\left(\\overrightarrow{{{Y2}{N}}} + \\overrightarrow{{{Y1}{N}}}\\right) = \\overrightarrow{{{X1}{Y2}}} + \\overrightarrow{{{X2}{Y1}}} + \\vec{{0}} + \\vec{{0}} = \\overrightarrow{{{X1}{Y2}}} + \\overrightarrow{{{X2}{Y1}}}$.{them_buoc}\n'
            f'\\item $2\\overrightarrow{{{M}{N}}} = \\overrightarrow{{{M}{N}}} + \\overrightarrow{{{M}{N}}} = \\left(\\overrightarrow{{{M}{X1}}} + \\overrightarrow{{{X1}{Y1}}} + \\overrightarrow{{{Y1}{N}}}\\right) + \\left(\\overrightarrow{{{M}{X2}}} + \\overrightarrow{{{X2}{Y2}}} + \\overrightarrow{{{Y2}{N}}}\\right)$\\\\\n'
            f'$= \\left(\\overrightarrow{{{X1}{Y1}}} + \\overrightarrow{{{X2}{Y2}}}\\right) + \\left(\\overrightarrow{{{M}{X1}}} + \\overrightarrow{{{M}{X2}}}\\right) + \\left(\\overrightarrow{{{Y1}{N}}} + \\overrightarrow{{{Y2}{N}}}\\right) = \\overrightarrow{{{X1}{Y1}}} + \\overrightarrow{{{X2}{Y2}}} + \\vec{{0}} + \\vec{{0}} = \\overrightarrow{{{X1}{Y1}}} + \\overrightarrow{{{X2}{Y2}}}$.{them_buoc_b}\n'
            f'\\item Vì ${N}$ là trung điểm của cạnh ${Y1}{Y2}$ nên $\\overrightarrow{{{M}{Y1}}} + \\overrightarrow{{{M}{Y2}}} = 2\\overrightarrow{{{M}{N}}}${them_buoc_c}.\n'
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

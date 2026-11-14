
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


def bt_dang21_p4_b4_c1_hh11(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        list_points = [
            ['S', 'A', 'B', 'C', 'D', 'H', 'E', 'F', 'K'],
            ['S', 'M', 'N', 'P', 'Q', 'O', 'I', 'J', 'R'],
            ['V', 'A', 'B', 'C', 'D', 'I', 'E', 'F', 'M']
        ]
        pt = random.choice(list_points)
        S, A, B, C, D, H, E, F, K = pt[0], pt[1], pt[2], pt[3], pt[4], pt[5], pt[6], pt[7], pt[8]
        noidungcauhoi = ('Cho hình chóp $'+S+'.'+A+B+C+D+'$ đáy $'+A+B+C+D+'$ là hình bình hành tâm $'+H+'$. Mặt phẳng $(P)$ đi qua $'+H+'$ và song song với $('+S+A+B+')$. Tìm giao tuyến của:\\\\ \n'
                         'a) Mặt phẳng $(P)$ và mặt phẳng $('+A+B+C+D+')$. \\\\ \n'
                         'b) Mặt phẳng $(P)$ và mặt phẳng $('+S+B+C+')$. \n')
        loigiai = ( '\\begin{center} \n'
                    '\\begin{tikzpicture}[scale=0.8, line join=round, line cap=round] \n'
                    '\\coordinate ('+A+') at (1,2); \n'
                    '\\coordinate ('+B+') at (-2,0); \n'
                    '\\coordinate ('+C+') at (3,0); \n'
                    '\\coordinate ('+D+') at (6,2); \n'
                    '\\coordinate ('+S+') at (2.5,5); \n'
                    '\\coordinate ('+H+') at (intersection of '+A+'--'+C+' and '+B+'--'+D+'); \n'
                    '\\coordinate ('+E+') at ($('+B+')!0.5!('+C+')$); \n'
                    '\\coordinate ('+F+') at ($('+A+')!0.5!('+D+')$); \n'
                    '\\coordinate ('+K+') at ($('+S+')!0.5!('+C+')$); \n'
                    '\\draw[dashed] ('+B+') -- ('+A+') -- ('+D+') ('+F+') -- ('+K+') ('+A+') -- ('+C+') ('+B+') -- ('+D+') ('+S+') -- ('+A+') ('+E+') -- ('+F+'); \n'
                    '\\draw ('+S+') -- ('+B+') -- ('+C+') -- ('+D+') -- ('+S+') -- ('+C+') ('+E+') -- ('+K+'); \n'
                    '\\fill ('+S+') circle (1.5pt) node[above] {$'+S+'$}; \n'
                    '\\fill ('+A+') circle (1.5pt) node[above left] {$'+A+'$}; \n'
                    '\\fill ('+B+') circle (1.5pt) node[below left] {$'+B+'$}; \n'
                    '\\fill ('+C+') circle (1.5pt) node[below right] {$'+C+'$}; \n'
                    '\\fill ('+D+') circle (1.5pt) node[right] {$'+D+'$}; \n'
                    '\\fill ('+H+') circle (1.5pt) node[below] {$'+H+'$}; \n'
                    '\\fill ('+E+') circle (1.5pt) node[below] {$'+E+'$}; \n'
                    '\\fill ('+F+') circle (1.5pt) node[above] {$'+F+'$}; \n'
                    '\\fill ('+K+') circle (1.5pt) node[left] {$'+K+'$}; \n'
                    '\\end{tikzpicture} \n'
                    '\\end{center} \n'
                    '\\begin{enumEX}[a)]{1} \n'
                    '\\item Giao tuyến của mặt phẳng $(P)$ và mặt phẳng $('+A+B+C+D+')$. \\\\ \n'
                    'Ta có: $\\begin{cases} (P) \\parallel ('+S+A+B+') \\\\ ('+A+B+C+D+') \\cap ('+S+A+B+') = '+A+B+' \\\\ (P) \\cap ('+A+B+C+D+') = '+H+' \\end{cases} \\Leftrightarrow (P) \\cap ('+A+B+C+D+') = '+E+F+'$ với $\\begin{cases} '+E+F+' \\text{ qua } '+H+' \\\\ '+E+F+' \\parallel '+A+B+' \\\\ '+E+' \\in '+B+C+', '+F+' \\in '+A+D+' \\end{cases}$. \n'
                    '\\item Giao tuyến của mặt phẳng $(P)$ và mặt phẳng $('+S+B+C+')$. \\\\ \n'
                    'Ta có: $\\begin{cases} (P) \\parallel ('+S+A+B+') \\\\ ('+S+B+C+') \\cap ('+S+A+B+') = '+S+B+' \\\\ (P) \\cap ('+S+B+C+') = '+E+' \\end{cases} \\Leftrightarrow (P) \\cap ('+S+B+C+') = '+E+K+'$ với $\\begin{cases} '+E+K+' \\cap '+S+C+' = '+K+' \\\\ '+E+K+' \\parallel '+S+B+' \\end{cases}$. \n'
                    '\\end{enumEX} \n')
    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
    return content

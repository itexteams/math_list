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


def bt_dang37_p1_b3_c1_hh12(self):
    a1 = random.randint(-5, 5)
    a2 = random.randint(-5, 5)
    a3 = random.randint(-5, 5)
    b1 = random.randint(-5, 5)
    b2 = random.randint(-5, 5)
    b3 = random.randint(-5, 5)
    while a1*b2 == a2*b1 and a2*b3 == a3*b2:
        b1 = random.randint(-5, 5)
        b2 = random.randint(-5, 5)
        b3 = random.randint(-5, 5)
    x_val = random.randint(-4, 4)
    y_val = random.randint(-4, 4)
    c1 = a1 * x_val + b1 * y_val
    c2 = a2 * x_val + b2 * y_val
    c3 = a3 * x_val + b3 * y_val
    kq = x_val + y_val
    du = ['$%s$' % kq]
    da = du[0]
    s = [kq + 1, kq - 1, kq + 2, kq - 2, kq + 3, kq - 3, kq + 4]
    random.shuffle(s)
    das1 = '$%s$' % s[0]
    das2 = '$%s$' % s[1]
    das3 = '$%s$' % s[2]
    noidungcauhoi = '''Trong không gian $Oxyz$, cho các vectơ $\\overrightarrow{a}=(%s;%s;%s), \\overrightarrow{b}=(%s;%s;%s)$ và $\\overrightarrow{c}=(%s;%s;%s)$. Biết rằng $\\overrightarrow{c} = x\\overrightarrow{a} + y\\overrightarrow{b}$, với $x,y$ là các số thực. Khi đó, $x+y$ bằng''' % (a1, a2, a3, b1, b2, b3, c1, c2, c3)
    da_d = '\\True ' + str(da)
    list_1 = [da_d, das1, das2, das3]
    random.shuffle(list_1)
    str_b1 = f"+ {b1}y" if b1 > 0 else f"- {-b1}y" if b1 < 0 else ""
    str_b2 = f"+ {b2}y" if b2 > 0 else f"- {-b2}y" if b2 < 0 else ""
    str_b3 = f"+ {b3}y" if b3 > 0 else f"- {-b3}y" if b3 < 0 else ""
    str_a1 = f"{a1}x " if a1 != 0 else ""
    str_a2 = f"{a2}x " if a2 != 0 else ""
    str_a3 = f"{a3}x " if a3 != 0 else ""
    if str_a1 == "" and str_b1 != "": str_b1 = str_b1.replace("+ ", "").replace("- ", "-")
    if str_a2 == "" and str_b2 != "": str_b2 = str_b2.replace("+ ", "").replace("- ", "-")
    if str_a3 == "" and str_b3 != "": str_b3 = str_b3.replace("+ ", "").replace("- ", "-")
    eq1 = f"{str_a1}{str_b1} = {c1}"
    eq2 = f"{str_a2}{str_b2} = {c2}"
    eq3 = f"{str_a3}{str_b3} = {c3}"
    v_c_str = f"({str_a1}{str_b1}; {str_a2}{str_b2}; {str_a3}{str_b3})"
    loigiai = '''$\\overrightarrow{c} = x\\overrightarrow{a} + y\\overrightarrow{b} = %s$ nên $\\begin{cases} %s \\\\ %s \\\\ %s \\end{cases} \\Leftrightarrow \\begin{cases} x = %s \\\\ y = %s \\end{cases} \\Rightarrow x + y = %s$.''' % (v_c_str, eq1, eq2, eq3, x_val, y_val, kq)
    loigiai = loigiai.replace('+ -', '- ')
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
        '\\choice \n'
        '{'+str(list_1[1])+'}\n'
        '{'+str(list_1[2])+'}\n'
        '{'+str(list_1[3])+'}\n'
        '{'+str(list_1[0])+'}\n'
        '\\loigiai{'+str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content


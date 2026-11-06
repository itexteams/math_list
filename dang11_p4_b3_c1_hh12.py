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


def bt_dang11_p4_b3_c1_hh12(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        xA = random.randint(-5, 5)
        yA = random.randint(-5, 5)
        zA = random.randint(-5, 5)
        xB = random.randint(-5, 5)
        yB = random.randint(-5, 5)
        zB = random.randint(-5, 5)
        while (xB, yB, zB) == (xA, yA, zA):
            xB = random.randint(-5, 5)
            yB = random.randint(-5, 5)
            zB = random.randint(-5, 5)
        xC = random.randint(-5, 5)
        yC = random.randint(-5, 5)
        zC = random.randint(-5, 5)
        while (xC, yC, zC) == (xA, yA, zA) or (xC, yC, zC) == (xB, yB, zB):
            xC = random.randint(-5, 5)
            yC = random.randint(-5, 5)
            zC = random.randint(-5, 5)
        a, b, c = symbols('a b c')
        vecAB_x = xB - xA
        vecAB_y = yB - yA
        vecAB_z = zB - zA
        vecDC_x_eq = f"-a + {xC}" if xC > 0 else f"-a - {-xC}" if xC < 0 else "-a"
        vecDC_y_eq = f"-b + {yC}" if yC > 0 else f"-b - {-yC}" if yC < 0 else "-b"
        vecDC_z_eq = f"-c + {zC}" if zC > 0 else f"-c - {-zC}" if zC < 0 else "-c"
        xD = xC - vecAB_x
        yD = yC - vecAB_y
        zD = zC - vecAB_z
        P_val = xD**2 - yD**2 + zD**2
        noidungcauhoi = f"Trong không gian $Oxyz$, cho hình bình hành $ABCD$ có $A({xA};{yA};{zA}); B({xB};{yB};{zB}); C({xC};{yC};{zC})$ và $D(a;b;c)$. Tính $P = a^2 - b^2 + c^2$."
        loigiai = f'''Ta có: $\\overrightarrow{{AB}} = ({vecAB_x};{vecAB_y};{vecAB_z})$, $\\overrightarrow{{DC}} = ({vecDC_x_eq};{vecDC_y_eq};{vecDC_z_eq})$.\\\\
    $ABCD$ là hình bình hành $\\Leftrightarrow \\overrightarrow{{AB}} = \\overrightarrow{{DC}} \\Leftrightarrow \\begin{{cases}} {vecDC_x_eq} = {vecAB_x} \\\\ {vecDC_y_eq} = {vecAB_y} \\\\ {vecDC_z_eq} = {vecAB_z} \\end{{cases}} \\Leftrightarrow \\begin{{cases}} a = {xD} \\\\ b = {yD} \\\\ c = {zD} \\end{{cases}}$.\\\\
    Vậy $P = a^2 - b^2 + c^2 = {xD**2} - {yD**2} + {zD**2} = {P_val}$.'''
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\n\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content


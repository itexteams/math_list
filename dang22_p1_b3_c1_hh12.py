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


def bt_dang22_p1_b3_c1_hh12(self):
    xa, ya, za = [random.randint(-5, 5) for _ in range(3)]
    xb, yb, zb = [random.randint(-5, 5) for _ in range(3)]
    xc, yc, zc = [random.randint(-5, 5) for _ in range(3)]
    x1 = xb - xa
    y1 = yb - ya
    z1 = zb - za
    x2 = xc - xa
    y2 = yc - ya
    z2 = zc - za
    t1 = x1 * x2
    t2 = y1 * y2
    t3 = z1 * z2
    kq = t1 + t2 + t3
    du = ['$%s$'%(kq)]
    da = random.choice(du)
    s = [kq + 1, kq - 1, kq + 2, kq - 2, kq + 3, kq - 3, kq + 4, kq - 4]
    das1 = random.choice(s)
    s.remove(das1)
    das2 = random.choice(s)
    s.remove(das2)
    das3 = random.choice(s)
    noidungcauhoi = ('''Trong không gian $Oxyz$, cho ba điểm $A(%s;%s;%s), B(%s;%s;%s), C(%s;%s;%s)$. Tính tích vô hướng $\\overrightarrow{AB} \\cdot \\overrightarrow{AC}$.'''
                     %(xa, ya, za, xb, yb, zb, xc, yc, zc))
    da_d = ('\\True ' + str(da))
    da_s1 = '$%s$' % str(das1)
    da_s2 = '$%s$' % str(das2)
    da_s3 = '$%s$' % str(das3)
    list_1 = [da_d, da_s1, da_s2, da_s3]
    random.shuffle(list_1)
    str_t2 = f"+ {t2}" if t2 >= 0 else f"- {-t2}"
    str_t3 = f"+ {t3}" if t3 >= 0 else f"- {-t3}"
    loigiai = ('''Ta có: $\\overrightarrow{AB} = (%s;%s;%s)$, $\\overrightarrow{AC} = (%s;%s;%s) \\Rightarrow \\overrightarrow{AB} \\cdot \\overrightarrow{AC} = %s %s %s = %s$.'''
               % (x1, y1, z1, x2, y2, z2, t1, str_t2, str_t3, kq))
    loigiai = loigiai.replace('+ -', '- ')
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+ 
        '\n\\choice \n'
        '{'+str(list_1[1])+'}\n'
        '{'+str(list_1[2])+'}\n'
        '{'+str(list_1[3])+'}\n'
        '{'+str(list_1[0])+'}\n'
        '\\loigiai{'+str(loigiai)+'}\n'
        '\\end{ex}\n\\end{minipage} \n\n')
    return content


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


def bt_dang32_p1_b3_c1_hh12(self):
    xa = random.randint(-2, 3)
    ya = random.randint(-2, 3)
    za = random.randint(-2, 3)
    v1x = random.choice([-2, -1, 1, 2])
    v1y = random.choice([-2, -1, 1, 2])
    v1z = random.choice([-2, -1, 1, 2])
    xb = xa + v1x
    yb = ya + v1y
    zb = za + v1z
    if v1x != 0:
        v2y = random.choice([-2, -1, 1, 2])
        v2z = random.choice([-2, -1, 1, 2])
        v2x = -(v1y*v2y + v1z*v2z) / v1x
        while v2x != int(v2x) or v2x == 0:
            v2y = random.choice([-2, -1, 1, 2])
            v2z = random.choice([-2, -1, 1, 2])
            v2x = -(v1y*v2y + v1z*v2z) / v1x
        v2x = int(v2x)
    elif v1y != 0:
        v2x = random.choice([-2, -1, 1, 2])
        v2z = random.choice([-2, -1, 1, 2])
        v2y = -(v1x*v2x + v1z*v2z) / v1y
        while v2y != int(v2y) or v2y == 0:
            v2x = random.choice([-2, -1, 1, 2])
            v2z = random.choice([-2, -1, 1, 2])
            v2y = -(v1x*v2x + v1z*v2z) / v1y
        v2y = int(v2y)
    else:
        v2x = random.choice([-2, -1, 1, 2])
        v2y = random.choice([-2, -1, 1, 2])
        v2z = -(v1x*v2x + v1y*v2y) / v1z
        while v2z != int(v2z) or v2z == 0:
            v2x = random.choice([-2, -1, 1, 2])
            v2y = random.choice([-2, -1, 1, 2])
            v2z = -(v1x*v2x + v1y*v2y) / v1z
        v2z = int(v2z)
    xc = xa + v2x
    yc = ya + v2y
    zc = za + v2z
    xd = xc + v1x
    yd = yc + v1y
    zd = zc + v1z
    da = '$D(%s;%s;%s)$' % (xd, yd, zd)
    da_d = '\\True ' + da
    das1 = '$D(%s;%s;%s)$' % (xd+1, yd-1, zd+2)
    das2 = '$D(%s;%s;%s)$' % (xd-1, yd+2, zd-1)
    das3 = '$D(%s;%s;%s)$' % (xd+2, yd+1, zd-2)
    noidungcauhoi = 'Trong không gian $Oxyz$, cho ba điểm $A(%s;%s;%s)$, $B(%s;%s;%s)$, $C(%s;%s;%s)$. Tìm tọa độ điểm $D$ sao cho bốn điểm $A$, $B$, $C$, $D$ lập thành một hình chữ nhật.' % (xa, ya, za, xb, yb, zb, xc, yc, zc)
    list_1 = [da_d, das1, das2, das3]
    random.shuffle(list_1)
    str_v2x = f"({v2x})" if v2x < 0 else str(v2x)
    str_v2y = f"({v2y})" if v2y < 0 else str(v2y)
    str_v2z = f"({v2z})" if v2z < 0 else str(v2z)
    tich = f"{v1x}.{str_v2x} + {v1y}.{str_v2y} + {v1z}.{str_v2z}".replace('+ -', '- ')
    str_xc = f"+ {-xc}" if xc < 0 else f"- {xc}" if xc > 0 else ""
    str_yc = f"+ {-yc}" if yc < 0 else f"- {yc}" if yc > 0 else ""
    str_zc = f"+ {-zc}" if zc < 0 else f"- {zc}" if zc > 0 else ""
    vCD_str = f"(x {str_xc}; y {str_yc}; z {str_zc})"
    eq1 = f"x {str_xc} = {v1x}"
    eq2 = f"y {str_yc} = {v1y}"
    eq3 = f"z {str_zc} = {v1z}"
    loigiai = 'Ta có: $\\overrightarrow{AB} = (%s;%s;%s)$; $\\overrightarrow{AC} = (%s;%s;%s)$, $\\overrightarrow{AB}.\\overrightarrow{AC} = %s = 0$ nên $AB \\perp AC$ \\\\ Điều này cho thấy $A, B, C$ không thẳng hàng và hình chữ nhật tạo ra phải là $ABDC$. \\\\ Gọi $D(x;y;z)$, ta có $\\overrightarrow{CD} = %s$. \\\\ $ABDC$ là hình chữ nhật khi và chỉ khi $\\overrightarrow{AB} = \\overrightarrow{CD} \\Leftrightarrow \\begin{cases} %s \\\\ %s \\\\ %s \\end{cases} \\Leftrightarrow \\begin{cases} x = %s \\\\ y = %s \\\\ z = %s \\end{cases} \\Rightarrow D(%s;%s;%s)$. \\\\ Vậy $D(%s;%s;%s)$.' % (v1x, v1y, v1z, v2x, v2y, v2z, tich, vCD_str, eq1, eq2, eq3, xd, yd, zd, xd, yd, zd, xd, yd, zd)
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


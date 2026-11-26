
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


def bt_dang18_p3_b4_c2_hh10(self):
    def fmt_num(val):
        r = Rational(val)
        if r.q == 1:
            return str(r.p)
        d = Decimal(r.p) / Decimal(r.q)
        return format(d.normalize(), 'f').replace('.', ',')
    def fmt_var_minus(var_name, a):
        if a == 0:
            return var_name
        elif a > 0:
            return var_name + ' - ' + str(a)
        else:
            return var_name + ' + ' + str(abs(a))
    def fix_signs(s):
        return s.replace('+ -', '- ').replace('+-', '-').replace('- -', '+ ').replace('--', '+')
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        t_pool = [Rational(3, 2), Rational(5, 2), Rational(7, 2), Rational(6, 5), Rational(7, 5), Rational(8, 5), Rational(9, 5), Rational(12, 5)]
        while True:
            xa = randint(-5, 5)
            ya = randint(-5, 5)
            vx = random.choice([i for i in range(-6, 7) if i != 0])
            vy = random.choice([i for i in range(-6, 7) if i != 0])
            t_val = random.choice(t_pool)
            dx = t_val * vx
            dy = t_val * vy
            xb = xa + dx
            yb = ya + dy
            tong = xb + yb
            kq_str = fmt_num(tong)
            if len(kq_str) <= 4:
                break
        kq = sp.Symbol(kq_str)
        t_str = fmt_num(t_val)
        x_lhs = fmt_var_minus('x', xa)
        y_lhs = fmt_var_minus('y', ya)
        dx_str = fmt_num(dx)
        dy_str = fmt_num(dy)
        xb_str = fmt_num(xb)
        yb_str = fmt_num(yb)
        if yb >= 0:
            sum_expr = '%s + %s' % (xb_str, yb_str)
        else:
            sum_expr = '%s - %s' % (xb_str, fmt_num(abs(yb)))
        noidungcauhoi = fix_signs('''Sự chuyển động của một tàu thủy được thể hiện trên một mặt phẳng tọa độ như sau: Tàu khởi hành từ vị trí $A(%s; %s)$ chuyển động thẳng đều với vận tốc (tính theo giờ) được biểu thị bởi vectơ $\\vec{v} = (%s; %s)$. Sau khi khởi hành $%s$ giờ, tàu ở vị trí $B(x; y)$ trên mặt phẳng tọa độ. Giá trị của $x + y$ bằng bao nhiêu?''' % (xa, ya, vx, vy, t_str))
        loigiai = fix_signs('''Gọi $B(x; y)$ là vị trí của tàu (trên mặt phẳng tọa độ) tại thời điểm sau khi khởi hành $%s$ giờ.\\\\
    Do tàu khởi hành từ $A$ di chuyển với vận tốc được biểu thị bởi vectơ $\\vec{v} = (%s; %s)$ nên cứ sau mỗi giờ, tàu di chuyển được một quãng bằng $|\\vec{v}|$.\\\\
    Vậy sau $%s$ giờ tàu di chuyển tới $B$ ta được: $\\overrightarrow{AB} = %s \\cdot \\vec{v}$\\\\
    $\\Leftrightarrow (%s; %s) = %s \\cdot (%s; %s) \\Leftrightarrow \\begin{cases} %s = %s \\\\ %s = %s \\end{cases} \\Leftrightarrow \\begin{cases} x = %s \\\\ y = %s \\end{cases}$.\\\\
    Vậy sau $%s$ giờ tàu ở vị trí (trên mặt phẳng tọa độ) là $B(%s; %s)$. Do đó $x + y = %s = %s$.''' % (t_str, vx, vy, t_str, t_str, x_lhs, y_lhs, t_str, vx, vy, x_lhs, dx_str, y_lhs, dy_str, xb_str, yb_str, t_str, xb_str, yb_str, sum_expr, kq_str))
        dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
        content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+ '\\loigiai{ \n' +str(loigiai)+'}\n' '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac')
        return content

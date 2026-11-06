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


def bt_dang31_p1_b3_c1_hh12(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        xA, yA, zA = randint(-4, 4), randint(-4, 4), randint(-4, 4)
        xB, yB, zB = randint(-4, 4), randint(-4, 4), randint(-4, 4)
        xC, yC, zC = randint(-4, 4), randint(-4, 4), randint(-4, 4)
        k1 = random.choice([2, 3, 4])
        k2 = random.choice([2, 3, 4, 5])
        vABx, vABy, vABz = xB - xA, yB - yA, zB - zA
        tu_x = xA - k1 * vABx + k2 * xC
        tu_y = yA - k1 * vABy + k2 * yC
        tu_z = zA - k1 * vABz + k2 * zC
        mau = k2 + 1
        ans_x, ans_y, ans_z = sp.Rational(tu_x, mau), sp.Rational(tu_y, mau), sp.Rational(tu_z, mau)
        lx, ly, lz = latex(ans_x), latex(ans_y), latex(ans_z)
        da = f"$M\\left({lx};{ly};{lz}\\right)$"
        s_set = set()
        s_set.add(f"$M\\left({ly};{lz};{lx}\\right)$")
        s_set.add(f"$M\\left({latex(-ans_x)};{latex(-ans_y)};{latex(-ans_z)}\\right)$")
        s_set.add(f"$M\\left({latex(sp.Rational(tu_x+1, mau))};{latex(sp.Rational(tu_y-1, mau))};{lz}\\right)$")
        s_set.add(f"$M\\left({latex(ans_x+1)};{latex(ans_y)};{latex(ans_z-1)}\\right)$")
        s_set.add(f"$M\\left({lz};{lx};{ly}\\right)$")
        if da in s_set:
            s_set.remove(da)
        s = list(s_set)
        random.shuffle(s)
        das1, das2, das3 = s[0], s[1], s[2]
        def f_p(num): return f"({num})" if num < 0 else str(num)
        def f_v(var, val): return f"{var}+{abs(val)}" if val < 0 else (f"{var}-{val}" if val > 0 else var)
        eq_x_l = f"{xA}-x-{k1}.{f_p(vABx)}"
        eq_y_l = f"{yA}-y-{k1}.{f_p(vABy)}"
        eq_z_l = f"{zA}-z-{k1}.{f_p(vABz)}"
        eq_x_r = f"{k2}({f_v('x', xC)})"
        eq_y_r = f"{k2}({f_v('y', yC)})"
        eq_z_r = f"{k2}({f_v('z', zC)})"
        noidungcauhoi = f"Trong không gian $Oxyz$, cho ba điểm $A({xA};{yA};{zA}), B({xB};{yB};{zB}), C({xC};{yC};{zC})$. Tìm tọa độ điểm $M(x;y;z)$ thỏa mãn $\\overrightarrow{{MA}}-{k1}\\overrightarrow{{AB}}={k2}\\overrightarrow{{CM}}$."
        da_d = '\\True ' + str(da)
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
        loigiai = f"Ta có: $\\overrightarrow{{MA}}-{k1}\\overrightarrow{{AB}}={k2}\\overrightarrow{{CM}} \\Rightarrow \\begin{{cases}} {eq_x_l} = {eq_x_r} \\\\ {eq_y_l} = {eq_y_r} \\\\ {eq_z_l} = {eq_z_r} \\end{{cases}}\\\\ \\Leftrightarrow \\begin{{cases}} x = {lx} \\\\ y = {ly} \\longrightarrow M\\left({lx};{ly};{lz}\\right). \\\\ z = {lz} \\end{{cases}}$"
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
        '\\choice \n'
        '{'+str(list_1[1])+'}\n'
        '{'+str(list_1[2])+'}\n'
        '{'+str(list_1[3])+'}\n'
        '{'+str(list_1[0])+'}\n'
        '\\loigiai{\n'+str(loigiai)+'\n}\n'
        '\\end{ex}\n\\end{minipage} \n\n')
    content = content.replace("+-", "-").replace("- -", "+").replace("--", "+").replace("+ -", "-")
    return content


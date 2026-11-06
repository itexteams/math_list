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


def bt_dang14_p4_b3_c1_hh12(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        xA, yA, zA = random.randint(-2, 2), random.randint(-2, 2), random.randint(-2, 2)
        AB_x, AB_y, AB_z = random.randint(-3, 3), random.randint(-3, 3), random.randint(-3, 3)
        while AB_x**2 + AB_y**2 + AB_z**2 == 0:
            AB_x, AB_y, AB_z = random.randint(-3, 3), random.randint(-3, 3), random.randint(-3, 3)
        xB, yB, zB = xA + AB_x, yA + AB_y, zA + AB_z
        BC_x, BC_y, BC_z = random.randint(-4, 4), random.randint(-4, 4), random.randint(-4, 4)
        while BC_x**2 + BC_y**2 + BC_z**2 == 0 or BC_x*AB_x + BC_y*AB_y + BC_z*AB_z != 0:
            BC_x, BC_y, BC_z = random.randint(-4, 4), random.randint(-4, 4), random.randint(-4, 4)
        xC, yC, zC = xB + BC_x, yB + BC_y, zB + BC_z
        k_num = random.randint(1, 3)
        k_den = random.randint(1, 3)
        k = Rational(k_num, k_den)
        AD_x = k * BC_x
        AD_y = k * BC_y
        AD_z = k * BC_z
        xD = xA + AD_x
        yD = yA + AD_y
        zD = zA + AD_z
        len_AB = math.sqrt(AB_x**2 + AB_y**2 + AB_z**2)
        len_BC = math.sqrt(BC_x**2 + BC_y**2 + BC_z**2)
        len_AD = float(k) * len_BC
        area = 0.5 * len_AB * (len_AD + len_BC)
        ans = xD + yD + zD
        def format_num(num):
            if num == int(num):
                return str(int(num))
            else:
                return sp.latex(sp.Rational(str(num)))
        len_AB_str = sp.latex(sp.sqrt(AB_x**2 + AB_y**2 + AB_z**2))
        len_BC_str = sp.latex(sp.sqrt(BC_x**2 + BC_y**2 + BC_z**2))
        len_AD_str = sp.latex(sp.Rational(k_num, k_den) * sp.sqrt(BC_x**2 + BC_y**2 + BC_z**2))
        area_str = sp.latex(sp.simplify(sp.Rational(1, 2) * sp.sqrt(AB_x**2 + AB_y**2 + AB_z**2) * (sp.Rational(k_num, k_den) + 1) * sp.sqrt(BC_x**2 + BC_y**2 + BC_z**2)))
        noidungcauhoi = f"Trong không gian $Oxyz$, cho hình thang $ABCD$ vuông tại $A$ và $B$. Biết ba đỉnh $A({xA}; {yA}; {zA}), B({xB}; {yB}; {zB}), C({xC}; {yC}; {zC})$ và hình thang $ABCD$ có diện tích bằng ${area_str}$. Giả sử đỉnh $D(a; b; c)$, tính $a + b + c$."
        loigiai = f"Ta có $\\overrightarrow{{AB}} = ({AB_x}; {AB_y}; {AB_z}) \\Rightarrow |\\overrightarrow{{AB}}| = {len_AB_str}; \\overrightarrow{{BC}} = ({BC_x}; {BC_y}; {BC_z}) \\Rightarrow |\\overrightarrow{{BC}}| = {len_BC_str}$.\\\\\n"
        loigiai += f"Theo giả thiết $ABCD$ là hình thang vuông tại $A$ và $B$ và có diện tích bằng ${area_str}$ nên\\\\\n"
        loigiai += f"$\\frac{{1}}{{2}}AB(AD + BC) = {area_str} \\Leftrightarrow \\frac{{1}}{{2}}.{len_AB_str}.(AD + {len_BC_str}) = {area_str} \\Rightarrow AD = {len_AD_str} \\Rightarrow AD = {sp.latex(k)}BC$.\\\\\n"
        loigiai += f"Do $ABCD$ là hình thang vuông tại $A$ và $B$ nên $\\overrightarrow{{AD}} = {sp.latex(k)}\\overrightarrow{{BC}}$.\\\\\n"
        loigiai += f"Giả sử $D(a; b; c)$ khi đó ta có $\\begin{{cases}} a - ({xA}) = {sp.latex(AD_x)} \\\\ b - ({yA}) = {sp.latex(AD_y)} \\\\ c - ({zA}) = {sp.latex(AD_z)} \\end{{cases}} \\Leftrightarrow \\begin{{cases}} a = {sp.latex(xD)} \\\\ b = {sp.latex(yD)} \\\\ c = {sp.latex(zD)} \\end{{cases}} \\Rightarrow a + b + c = {sp.latex(ans)}$."
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\n\\loigiai{ \n'
        +str(loigiai)+'\n}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content


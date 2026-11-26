
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


def bt_dang16_p3_b4_c2_hh10(self):
    def fix_signs(s):
        return s.replace('+ -', '- ').replace('+-', '-').replace('- -', '+ ').replace('--', '+')
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        while True:
            xa = randint(-5, 6)
            ya = randint(-5, 6)
            xb = random.choice([i for i in range(-5, 7) if i != 0])
            yb = random.choice([i for i in range(-5, 7) if i != 0])
            xc = randint(-5, 6)
            yc = randint(-5, 6)
            if (xb - xa) * (yc - ya) - (yb - ya) * (xc - xa) == 0:
                continue
            xd = xa + xc - xb
            yd = ya + yc - yb
            if xd == 0 or yd == 0:
                continue
            if (xa + xb + xc) % 3 == 0 and (ya + yb + yc) % 3 == 0:
                continue
            kq_val = xb + yd
            if len(str(kq_val)) <= 4:
                break
        xi = Rational(xa + xc, 2)
        yi = Rational(ya + yc, 2)
        xn = Rational(xa + xb + xc, 3)
        yn = Rational(ya + yb + yc, 3)
        kq = Integer(kq_val)
        tikz_code = (
            '\n\n\\centerline{\\begin{tikzpicture}[line cap=round,line join=round,line width=1pt]\n'
            '\\coordinate (B) at (0,0);\n'
            '\\coordinate (C) at (4.4,0);\n'
            '\\coordinate (A) at (1.3,2.3);\n'
            '\\coordinate (D) at (5.7,2.3);\n'
            '\\coordinate (M) at (2.2,0);\n'
            '\\coordinate (I) at (2.85,1.15);\n'
            '\\coordinate (N) at (1.9,0.7667);\n'
            '\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle;\n'
            '\\draw[line width=1pt] (A)--(C) (B)--(D) (A)--(M);\n'
            '\\fill (A) circle (1.6pt) node[above] {$A$};\n'
            '\\fill (B) circle (1.6pt) node[left] {$B$};\n'
            '\\fill (C) circle (1.6pt) node[right] {$C$};\n'
            '\\fill (D) circle (1.6pt) node[right] {$D$};\n'
            '\\fill (M) circle (1.6pt) node[below] {$M$};\n'
            '\\fill (I) circle (1.6pt) node[above] {$I$};\n'
            '\\fill (N) circle (1.6pt) node[left] {$N$};\n'
            '\\end{tikzpicture}}\n\n'
        )
        noidungcauhoi = fix_signs('''Trong mặt phẳng tọa độ $Oxy$, cho hình bình hành $ABCD$ có $A(%s; %s)$, $C(%s; %s)$. Gọi $M$ là trung điểm của cạnh $BC$, $N$ là giao điểm của $BD$ và $AM$. Biết $N\\left(%s; %s\\right)$ và hai đỉnh còn lại là $B(x_B; y_B)$, $D(x_D; y_D)$, giá trị của $x_B + y_D$ bằng bao nhiêu?''' % (xa, ya, xc, yc, latex(xn), latex(yn)))
        lg_part1 = fix_signs('''Do $I$ là tâm của hình bình hành $ABCD$ ta có $I$ là trung điểm của đoạn thẳng $AC$ nên tọa độ của điểm $I\\left(%s; %s\\right)$.''' % (latex(xi), latex(yi)))
        lg_part2 = fix_signs('''Xét tam giác $ABC$ thì $BI$, $AM$ là hai đường trung tuyến nên $N$ là trọng tâm tam giác $ABC$.\\\\
    Do đó $\\begin{cases} %s = \\dfrac{%s + x_B + %s}{3} \\\\ %s = \\dfrac{%s + y_B + %s}{3} \\end{cases} \\Leftrightarrow \\begin{cases} x_B = %s \\\\ y_B = %s \\end{cases} \\Rightarrow B(%s; %s)$.\\\\
    Gọi $D(x_D; y_D)$. Do $I$ là trung điểm của $BD$ nên $\\begin{cases} %s + x_D = %s \\\\ %s + y_D = %s \\end{cases} \\Leftrightarrow \\begin{cases} x_D = %s \\\\ y_D = %s \\end{cases}$ nên $D(%s; %s)$.\\\\
    Vậy $B(%s; %s)$, $D(%s; %s)$ và $x_B + y_D = %s + %s = %s$.''' % (latex(xn), xa, xc, latex(yn), ya, yc, xb, yb, xb, yb, xb, xa + xc, yb, ya + yc, xd, yd, xd, yd, xb, yb, xd, yd, xb, yd, kq_val))
        loigiai = lg_part1 + tikz_code + lg_part2
        dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
        content = ('\\begin{minipage}{\\textwidth} \n' '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+ '\\loigiai{ \n' +str(loigiai)+'}\n' '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac')
        return content

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


def bt_dang14_p3_b2_c2_hh12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # --- Randomization of the problem parameters ---

                # Randomize starting point A(ax, ay, az)
                ax, ay, az = random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)

                # Randomize direction vectơ u(u1, u2, u3)
                # Ensure |u| is a simple integer (e.g., 3, 5, 7, 10) for clean calculations
                # Common Pythagorean triples for length |u|:
                # (3, 4, 0) -> |u|=5
                # (2, 1, 2) -> |u|=3 (Used in the original problem: (2, -1, 2) -> |u|=3)
                # (3, 4, 12) -> |u|=13

                u_choices = [(2, -1, 2), (1, 2, 2), (-3, 0, 4), (0, 3, -4), (6, 0, 8)]
                u_choice = random.choice(u_choices)
                u1, u2, u3 = u_choice

                # Calculate |u|
                len_u = int(sqrt(u1**2 + u2**2 + u3**2))

                # Randomize velocity v (must be integer)
                v = random.randint(3, 8)

                # Randomize time t_time (must be integer)
                t_time = random.randint(5, 12)

                # --- Calculation ---

                # 1. Total distance AB
                AB_dist = v * t_time

                # 2. Relationship between distance and parameter t: AB_dist = |t| * |u|
                # |t| = AB_dist / |u|
                t_param = Rational(AB_dist , len_u)

                # Since cabin moves in the direction of u, t_param > 0.

                # 3. Coordinates of B(a, b, c)
                a = ax + t_param * u1
                b = ay + t_param * u2
                c = az + t_param * u3

                # Ensure a, b, c are integers (guaranteed by the choice of u, v, t_time)
                a, b, c = int(a), int(b), int(c)

                # 4. Final result: a + b + c
                kq = a + b + c

                # --- Multiple Choice Answers ---
                # The correct answer in LaTeX format
                da = '$%s$'%(latex(kq))

                # Incorrect answers
                s = [latex(kq + random.choice([1, 2, 3])),
                     latex(kq + random.choice([4, 5, 6])),
                     latex(kq - random.choice([1, 2, 3])),
                     latex(kq - random.choice([4, 5, 6])),
                    ]

                s_latex = ['$%s$'%(val) for val in s]

                # Ensure three distinct wrong answers
                def latex_to_text(l):
                    l_str = str(l).replace('\\circ', '').replace('$', '').replace('{', '').replace('}', '').replace(' ', '').replace('latex(', '').replace(')', '').replace('\\frac', '').replace('\\left', '').replace('\\right', '').strip()
                    try:
                         return int(l_str)
                    except ValueError:
                         return kq + 1000 

                s_unique = []
                seen_values = {kq}
                for val in s_latex:
                    raw_val = latex_to_text(val)
                    if raw_val not in seen_values:
                        s_unique.append(val)
                        seen_values.add(raw_val)

                while len(s_unique) < 3:
                    new_wrong_val = kq + random.choice([7, 8, 9, -7, -8, -9])
                    if new_wrong_val not in seen_values:
                        s_unique.append(latex(new_wrong_val))
                        seen_values.add(new_wrong_val)

                s_latex = s_unique

                das1 = random.choice(s_latex)
                s_latex.remove(das1)
                das2 = random.choice(s_latex)
                s_latex.remove(das2)
                das3 = random.choice(s_latex)

                # --- Question Content ---
                noidungcauhoi = ('''Trong không gian $Oxyz$, một cabin cáp treo xuất phát từ vị trí điểm $A(%s;%s;%s)$ và chuyển động đều trên đường cáp có vectơ chỉ phương là $\\vec{u}(%s;%s;%s)$ với vận tốc không đổi là $%s$ m/s (đơn vị trên mỗi trục tọa độ là mét). Sau $%s$ giây kể từ lúc xuất phát, cabin chuyển động theo hướng của vectơ $\\vec{u}$ đến vị trí điểm $B(a;b;c)$. Giá trị $a+b+c$ bằng bao nhiêu?'''
                                 %(latex(ax), latex(ay), latex(az), latex(u1), latex(u2), latex(u3), latex(v), latex(t_time)
                                 ))

                # --- Answers List ---
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

                # --- Solution Content ---
                loigiai=('''Phương trình tham số của đường cáp là $d: \\begin{cases} x = %s + %st \\\\ y = %s + %st \\\\ z = %s + %st \\end{cases}$.\\\\
            Độ dài của vectơ chỉ phương là $|\\vec{u}| = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = %s$.\\\\
            Do vận tốc của cabin là $%s$ m/s nên sau $%s$ giây kể từ lúc xuất phát, cabin di chuyển \\\\
            được quãng đường $AB = %s \\cdot %s = %s$ m.\\\\
            Ta có $B$ thuộc đường cáp nên $B(%s + %st; %s + %st; %s + %st)$. \\\\
            Quãng đường $AB$ tương ứng với độ lớn tham số $t$ là $AB = |\\vec{u}| \\cdot |t| = %s|t|$.\\\\
            Do đó $|t| = \\frac{AB}{|\\vec{u}|} = \\frac{%s}{%s} = %s$. Vì cabin chuyển động theo hướng của vectơ $\\vec{u}$ nên $t>0$. \\\\
            Suy ra $t=%s$. \\\\
            Tọa độ điểm $B(a;b;c)$ là: \\\\
            $a = %s + %s(%s) = %s$. \\\\
            $b = %s + %s(%s) = %s$. \\\\
            $c = %s + %s(%s) = %s$. \\\\
            Vậy $B(%s;%s;%s)$, và $a+b+c = %s + %s + %s = %s$.'''

                         # Parametric equation
                         %(latex(ax), latex(u1), latex(ay), latex(u2), latex(az), latex(u3),
                           # Length of u
                           latex(u1), latex(u2), latex(u3), latex(len_u),
                           # Distance AB
                           latex(v), latex(t_time), latex(v), latex(t_time), latex(AB_dist),
                           # B coordinates in terms of t
                           latex(ax), latex(u1), latex(ay), latex(u2), latex(az), latex(u3),
                           # Find t
                           latex(len_u), latex(AB_dist), latex(len_u), latex(t_param), latex(t_param),
                           # Final coordinates
                           latex(ax), latex(u1), latex(t_param), latex(a),
                           latex(ay), latex(u2), latex(t_param), latex(b),
                           latex(az), latex(u3), latex(t_param), latex(c),
                           # Final sum
                           latex(a), latex(b), latex(c), latex(a), latex(b), latex(c), latex(kq)
                           ))

                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('+ -', '-').replace('- -', '+')
            return content   


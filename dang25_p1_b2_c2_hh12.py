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


def bt_dang25_p1_b2_c2_hh12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Given points and line parameters
                A = (1, 0, 0)
                B = (0, 2, 0)
                C = (0, 0, 3)

                # Parametric equation of the line d
                x_t, y_t, z_t = symbols('x_t y_t z_t')
                t = symbols('t')

                # Define x, y, z as symbols
                x, y, z = symbols('x y z')

                # Equation of the plane (ABC) in intercept form
                plane_eq = x/A[0] + y/B[1] + z/C[2] - 1
                plane_eq_simplified = sp.simplify(plane_eq * 6)

                # Substitute line d into the plane equation
                plane_eq_substituted = plane_eq_simplified.subs([(x, -t), (y, 2+t), (z, 3+t)])

                # Solve for t
                t_sol = sp.solve(plane_eq_substituted, t)[0]

                # Find coordinates of M
                a = -t_sol
                b = 2 + t_sol
                c = 3 + t_sol

                # Calculate the sum S
                S = a + b - c

                # Convert results to LaTeX format
                A_latex = latex(A)
                B_latex = latex(B)
                C_latex = latex(C)
                line_latex = r'''\begin{cases} x = -t \\ y = 2+t \\ z = 3+t \end{cases}'''
                plane_eq_latex = latex(plane_eq_simplified)
                t_sol_latex = latex(t_sol)
                M_latex = latex((a, b, c))
                S_latex = latex(S)

                # Problem statement
                noidungcauhoi = ('''Trong không gian với hệ tọa độ $Oxyz$, cho 3 điểm $A%s$, $B%s$, $C%s$ và đường thẳng $d: %s$. Gọi $M(a;b;c)$ là tọa độ giao điểm của đường thẳng $d$ với mặt phẳng $(ABC)$. Tổng $S = a+b-c$ bằng''' % (A_latex, B_latex, C_latex, line_latex))

                # Answer and distractors
                kq = S_latex
                du = ['$%s$' % (kq)]
                da = random.choice(du)
                s = ['$%s$' % (latex(S+1)), '$%s$' % (latex(S+2)), '$%s$' % (latex(S+3)), '$%s$' % (latex(S-1)), '$%s$' % (latex(S-2)), '$%s$' % (latex(S-3))]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Solution
                loigiai = ('''Phương trình mặt phẳng $(ABC)$ có dạng: $\\frac{x}{%s} + \\frac{y}{%s} + \\frac{z}{%s} = 1 \\Leftrightarrow %s = 0$. \\\\
            Điểm $M\\in(d)\\Rightarrow M(-t;2+t;3+t)$. Lại vì $M = d\\cap(ABC)$ nên ta có \\\\
            $6(-t)+3(2+t)+2(3+t)-6 = 0 \\Leftrightarrow %s=0 \\Leftrightarrow t=%s \\Rightarrow M%s$. \\\\
            Vậy ta có $S=a+b-c=%s$.'''
                % (A[0], B[1], C[2], plane_eq_latex, latex(plane_eq_substituted), t_sol_latex, M_latex, S_latex))

                # Output to LaTeX format
                content = ('\\begin{minipage}{\\textwidth} \n'
                        '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                        '\\choice \n'
                        '{'+str(list_1[1])+'}\n'
                        '{'+str(list_1[2])+'}\n'
                        '{'+str(list_1[3])+'}\n'
                        '{'+str(list_1[0])+'}\n'
                        '\\loigiai{'+str(loigiai)+'}\n'
                        '\\end{ex}\n \\end{minipage} \n\n')
            return content


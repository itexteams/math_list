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


def bt_dang24_p1_b2_c2_hh12(self):
            # Khai báo biến
            while True:
                x_I = random.randint(-5, 5)
                y_I = random.randint(-5, 5)
                z_I = random.randint(-5, 5)
                if not (x_I == 0 and y_I == 0 and z_I == 0):
                    break

            # Randomize direction vectơ of line d
            a_d = random.choice([1,2,3,4,5,-1,-2,-3,-4,-5])
            b_d = random.choice([1,2,3,4,5,-1,-2,-3,-4,-5])
            c_d = random.choice([1,2,3,4,5,-1,-2,-3,-4,-5])

            # Create vectơ OI and vectơ u
            OI_vec = sp.Matrix([x_I, y_I, z_I])
            u_vec = sp.Matrix([a_d, b_d, c_d])

            # Calculate the cross product for the direction vectơ of Delta
            u_delta = OI_vec.cross(u_vec)
            # Simplify the vectơ by dividing by the greatest common divisor
            gcd = math.gcd(u_delta[0], math.gcd(u_delta[1], u_delta[2]))
            u_delta_simplified = u_delta / gcd
            if u_delta_simplified[0] < 0:
                u_delta_simplified = -u_delta_simplified

            # Store the components of the simplified vectơ
            a_delta = int(u_delta_simplified[0])
            b_delta = int(u_delta_simplified[1])
            c_delta = int(u_delta_simplified[2])

            # Construct the correct answer
            da = f'$\\frac{{x-{latex(x_I)}}}{{{latex(a_delta)}}}=\\frac{{y-{latex(y_I)}}}{{{latex(b_delta)}}}=\\frac{{z-{latex(z_I)}}}{{{latex(c_delta)}}}$'
            da_d = ('\\True ' + str(da))

            # Create incorrect answers by slightly modifying the correct one
            da_s1 = f'$\\frac{{x-{latex(x_I)}}}{{{latex(-a_delta)}}}=\\frac{{y-{latex(y_I)}}}{{{latex(b_delta)}}}=\\frac{{z-{latex(z_I)}}}{{{latex(c_delta)}}}$'
            da_s2 = f'$\\frac{{x-{latex(x_I)}}}{{{latex(a_delta)}}}=\\frac{{y-{latex(y_I)}}}{{{latex(-b_delta)}}}=\\frac{{z-{latex(z_I)}}}{{{latex(c_delta)}}}$'
            da_s3 = f'$\\frac{{x-{latex(x_I)}}}{{{latex(a_d)}}}=\\frac{{y-{latex(y_I)}}}{{{latex(b_d)}}}=\\frac{{z-{latex(z_I)}}}{{{latex(c_d)}}}$'

            # The question text
            noidungcauhoi = (f'''Trong không gian $Oxyz$, cho đường thẳng $d: \\frac{{x-1}}{{{latex(a_d)}}}=\\frac{{y-2}}{{{latex(b_d)}}}=\\frac{{z-2}}{{{latex(c_d)}}}$ và điểm $I({latex(x_I)};{latex(y_I)};{latex(z_I)})$. Đường thẳng $\\Delta$ đi qua $I$ và vuông góc với hai đường thẳng $OI, d$ có phương trình là''')

            # Put the answers in a list and shuffle
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # The solution text
            loigiai = (f'''Đường thẳng $d$ có một vectơ chỉ phương là $\\vec{{u}}=({latex(a_d)};{latex(b_d)};{latex(c_d)})$. \\\\
                        Đường thẳng $\\Delta$ vuông góc với hai đường thẳng $OI$ và $d$ nên nhận vectơ \\\\ $[\\vec{{OI}}, \\vec{{u}}]=({latex(u_delta[0])};{latex(u_delta[1])};{latex(u_delta[2])})$ làm một vectơ chỉ phương. \\\\
                        Ta có $\\vec{{u}}_\\Delta=({latex(a_delta)};{latex(b_delta)};{latex(c_delta)})$. \\\\
                        Do $I({latex(x_I)};{latex(y_I)};{latex(z_I)}) \\in \\Delta$ nên $\\Delta$ có phương trình là $\\frac{{x-{latex(x_I)}}}{{{latex(a_delta)}}}=\\frac{{y-{latex(y_I)}}}{{{latex(b_delta)}}}=\\frac{{z-{latex(z_I)}}}{{{latex(c_delta)}}}$.''')

            # Output the problem in the specified format
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) +
                '\\choice \n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '{' + str(list_1[0]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('--', '+')
            return content


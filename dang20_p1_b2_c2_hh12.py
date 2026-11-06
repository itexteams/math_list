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


def bt_dang20_p1_b2_c2_hh12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Randomize coefficients for plane P
                a1 = random.choice([2, 3, 4,-2,-3,-4])
                b1 = random.choice([-2, -3, -4,2,3,4])
                c1 = random.choice([2, 3, 4,-2,-3,-4])
                d1 = randint(2, 5)

                # Randomize coefficients for plane Q
                a2 = random.choice([2, 3, 4,-2,-3,-4])
                b2 = random.choice([-2, -3, -4,2,3,4])
                c2 = random.choice([2, 3, 4,-2,-3,-4])
                d2 = randint(2, 5)

                # Define the normal vectơrs
                n1_vec = Matrix([a1, b1, c1])
                n2_vec = Matrix([a2, b2, c2])

                # Check if the normal vectơrs are parallel
                while n1_vec.cross(n2_vec) == Matrix([0, 0, 0]):
                    a2 = random.choice([5, 2, 3, 4])
                    b2 = random.choice([-4, -2, -3, -4])
                    c2 = random.choice([5, 2, 3, 4])
                    n2_vec = Matrix([a2, b2, c2])

                # Calculate the cross product for the direction vectơr
                u_vec = n1_vec.cross(n2_vec)

                # Get the components of the correct direction vectơr
                ux, uy, uz = u_vec[0], u_vec[1], u_vec[2]

                # Format the correct answer vectơr
                kq = f'$(%s;%s;%s)$' % (latex(ux), latex(uy), latex(uz))
                da = f'$(%s;%s;%s)$' % (ux, uy, uz)

                # Generate incorrect answer vectơrs
                s = [
                    f'$(%s;%s;%s)$' % (latex(ux), latex(-uy), latex(uz)), # Change sign of y
                    f'$(%s;%s;%s)$' % (latex(uy), latex(ux), latex(uz)), # Swap x and y
                    f'$(%s;%s;%s)$' % (latex(ux+1), latex(uy), latex(uz)), # Add 1 to x
                    f'$(%s;%s;%s)$' % (latex(-ux), latex(uy), latex(-uz)), # Change signs of x and z
                    f'$(%s;%s;%s)$' % (latex(ux), latex(uy+1), latex(uz)), # Add 1 to y
                    f'$(%s;%s;%s)$' % (latex(ux), latex(uy), latex(uz-1)), # Subtract 1 from z
                ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Trong không gian $Oxyz$, cho mặt phẳng $(P):%sx%s%sy%s%sz%s%s = 0$ và mặt phẳng $(Q):%sx%s%sy%s%sz%s%s = 0$. Gọi $\\Delta$ là giao tuyến của hai mặt phẳng $(P), (Q)$. vectơ nào sau đây là một vectơ chỉ phương của đường thẳng $\\Delta$?'''
                                 % (
                                     latex(a1), '+' if b1 > 0 else '', latex(b1), '+' if c1 > 0 else '', latex(c1), '+' if d1 > 0 else '', latex(d1),
                                     latex(a2), '+' if b2 > 0 else '', latex(b2), '+' if c2 > 0 else '', latex(c2), '+' if d2 > 0 else '', latex(d2),
                                 ))

                # Các đáp án
                da_d = ('\\True ' + str(kq))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Mặt phẳng $(P)$ có vectơ pháp tuyến $\\vec{n_1}=(%s;%s;%s)$.\\\\
            Mặt phẳng $(Q)$ có vectơ pháp tuyến $\\vec{n_2}=(%s;%s;%s)$.\\\\
            Gọi $\\vec{u}$ là một vectơ chỉ phương của $\\Delta$. \\\\
            Vì $\\Delta$ là giao tuyến của $(P)$ và $(Q)$ nên $\\vec{u}$ vuông góc với cả $\\vec{n_1}$ và $\\vec{n_2}$.\\\\
            Do đó, ta có thể chọn $\\vec{u} = [\\vec{n_1},\\vec{n_2}] = (%s,%s,%s)$.'''
                           % (
                               latex(a1), latex(b1), latex(c1),
                               latex(a2), latex(b2), latex(c2),
                               latex(b1*c2 - b2*c1), latex(c1*a2 - c2*a1), latex(a1*b2 - a2*b1),
                           ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) +
                       '\\choice \n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '{' + str(list_1[0]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content


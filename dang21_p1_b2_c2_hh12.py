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


def bt_dang21_p1_b2_c2_hh12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Randomize the point A
                ax = randint(-3, 3)
                ay = randint(-3, 3)
                az = randint(-3, 3)

                # Randomize coefficients for plane (alpha)
                a1 = random.choice([-2, -5, 5, 2, 3])
                b1 = random.choice([-2, -5, 5, 2, 3])
                c1 = random.choice([-2, -5, 5, 2, 3])
                d1 = randint(-5, 5)

                # Randomize direction vectơr for line d
                a2 = random.choice([-2, -5, 5, 2, 3])
                b2 = random.choice([-2, -5, 5, 2, 3])
                c2 = random.choice([-2, -5, 5, 2, 3])

                # Define the normal vectơr of the plane and direction vectơr of the line
                n_vec = Matrix([a1, b1, c1])
                a_vec = Matrix([a2, b2, c2])

                # Check for parallel vectơrs, if so, re-randomize
                while n_vec.cross(a_vec) == Matrix([0, 0, 0]):
                    a2 = random.choice([-2, -5, 5, 2, 3])
                    b2 = random.choice([-2, -5, 5, 2, 3])
                    c2 = random.choice([-2, -5, 5, 2, 3])
                    a_vec = Matrix([a2, b2, c2])

                # Calculate the cross product for the direction vectơr of Delta
                u_vec = n_vec.cross(a_vec)

                # Get the components of the correct direction vectơr
                ux, uy, uz = u_vec[0], u_vec[1], u_vec[2]

                # Format the correct answer vectơr
                kq = f'$(%s;%s;%s)$' % (latex(ux), latex(uy), latex(uz))
                da = f'$(%s;%s;%s)$' % (ux, uy, uz)

                # Generate incorrect answer vectơrs
                s = [
                    f'$(%s;%s;%s)$' % (latex(ux+1), latex(uy), latex(uz)), # Change sign of x
                    f'$(%s;%s;%s)$' % (latex(ux), latex(uy+1), latex(uz)), # Swap x and y
                    f'$(%s;%s;%s)$' % (latex(ux), latex(uy), latex(uz+1)), # Add 1 to x
                    f'$(%s;%s;%s)$' % (latex(ux-1), latex(uy), latex(uz)), # Change sign of z
                    f'$(%s;%s;%s)$' % (latex(ux), latex(uy-1), latex(uz)), # Use the normal vectơr
                    f'$(%s;%s;%s)$' % (latex(ux), latex(uy), latex(uz-1)), # Use the direction vectơr of d
                ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Trong không gian $Oxyz$, cho mặt phẳng $(\\alpha):%sx%s%sy%s%sz%s%s=0$ và đường thẳng $d:\\frac{x-%s}{%s}=\\frac{y-%s}{%s}=\\frac{z-%s}{%s}$. $\\Delta$ là đường thẳng nằm trong mặt phẳng $(\\alpha)$ và đồng thời vuông góc với đường thẳng $d$. vectơ nào sau đây là vectơ chỉ phương của đường thẳng $\\Delta$?'''
                                 % (
                                     latex(a1), '+' if b1 > 0 else '', latex(b1), '+' if c1 > 0 else '', latex(c1), '+' if d1 > 0 else '', latex(d1),
                                     latex(0) if a2 < 0 else latex(0) if a2 == 0 else latex(0), latex(a2),
                                     latex(0) if b2 < 0 else latex(0) if b2 == 0 else latex(0), latex(b2),
                                     latex(0) if c2 < 0 else latex(0) if c2 == 0 else latex(0), latex(c2),
                                 ))

                # The above is not a correct way to format the line equation for randomized numbers.
                # A better way is:
                x0, y0, z0 = randint(-3, 3), randint(-3, 3), randint(-3, 3)
                noidungcauhoi = ('''Trong không gian $Oxyz$, cho mặt phẳng $(\\alpha):%sx%s%sy%s%sz%s%s=0$ và đường thẳng $d:\\frac{x%s}{%s}=\\frac{y%s}{%s}=\\frac{z%s}{%s}$. $\\Delta$ là đường thẳng song song với mặt phẳng $(\\alpha)$ và đồng thời vuông góc với đường thẳng $d$. vectơ nào sau đây là vectơ chỉ phương của đường thẳng $\\Delta$?'''
                                 % (
                                     latex(a1), '+' if b1 > 0 else '', latex(b1), '+' if c1 > 0 else '', latex(c1), '+' if d1 > 0 else '', latex(d1),
                                     '-' + latex(x0) if x0 > 0 else '+' + latex(abs(x0)) if x0 < 0 else '', latex(a2),
                                     '-' + latex(y0) if y0 > 0 else '+' + latex(abs(y0)) if y0 < 0 else '', latex(b2),
                                     '-' + latex(z0) if z0 > 0 else '+' + latex(abs(z0)) if z0 < 0 else '', latex(c2),
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
                loigiai = ('''Vectơ pháp tuyến của mặt phẳng $(\\alpha)$ là $\\vec{n}=(%s;%s;%s)$.\\\\
            Vectơ chỉ phương của đường thẳng $d$ là $\\vec{a}=(%s;%s;%s)$.\\\\
            Giả sử $\\vec{u}$ là một vectơ chỉ phương của $\\Delta$. Vì $\\Delta$ nằm trong mặt phẳng $(\\alpha)$ nên $\\vec{u}$ vuông góc với $\\vec{n}$.\\\\
            Vì $\\Delta$ vuông góc với đường thẳng $d$ nên $\\vec{u}$ vuông góc với $\\vec{a}$.\\\\
            Ta có $\\vec{u}=[\\vec{n},\\vec{a}]=(%s,%s,%s)$.'''
                           % (
                               latex(a1), latex(b1), latex(c1),
                               latex(a2), latex(b2), latex(c2),
                               latex(ux), latex(uy), latex(uz)
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


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


def bt_dang18_p4_b1_c2_hh12(self):
            # Khai báo biến
            k1 = 1
            k2 = random.choice([2, 3, 4])
            k_vec = [1, k1, k2]

            # Define a random plane
            plane = random.choice(['Oxy', 'Oyz', 'Oxz'])

            # Generate random integer coordinates for A, B, C
            Ax, Ay, Az = randint(-5, 5), randint(-5, 5), randint(-5, 5)
            Bx, By, Bz = randint(-5, 5), randint(-5, 5), randint(-5, 5)
            Cx, Cy, Cz = randint(-5, 5), randint(-5, 5), randint(-5, 5)

            # Calculate the coordinates of I
            denom = sum(k_vec)
            Ix_num = k_vec[0]*Ax + k_vec[1]*Bx + k_vec[2]*Cx
            Iy_num = k_vec[0]*Ay + k_vec[1]*By + k_vec[2]*Cy
            Iz_num = k_vec[0]*Az + k_vec[1]*Bz + k_vec[2]*Cz

            Ix = Rational(Ix_num, denom)
            Iy = Rational(Iy_num, denom)
            Iz = Rational(Iz_num, denom)

            # Coordinates of M (projection of I on the chosen plane)
            if plane == 'Oxy':
                Mx, My, Mz = Ix, Iy, 0
            elif plane == 'Oyz':
                Mx, My, Mz = 0, Iy, Iz
            else: # Oxz
                Mx, My, Mz = Ix, 0, Iz

            # Values of a, b, c
            a, b, c = Mx, My, Mz

            # Randomize the expression P
            p1, p2, p3 = randint(-5, 5), randint(-5, 5), randint(-5, 5)
            P_val = p1*a + p2*b + p3*c

            # The question and answer content
            noidungcauhoi = ('''Trong không gian với hệ tọa độ $Oxyz$, cho $A(%s;%s;%s)$, $B(%s;%s;%s)$, $C(%s;%s;%s)$. Gọi điểm $M(a;b;c) \\in (%s)$ sao cho $T = \\vec{MA} \\cdot \\vec{MB} + %s\\vec{MA} \\cdot \\vec{MC}$ nhỏ nhất. Tính giá trị biểu thức $P=%sa%s%sb%s%sc$.'''
                            %(latex(Ax),latex(Ay),latex(Az),latex(Bx),latex(By),latex(Bz),latex(Cx),latex(Cy),latex(Cz),
                            plane, latex(k2),
                            latex(p1) if p1 != 1 else '', '+' if p2 >= 0 else '-', latex(abs(p2)),
                            '+' if p3 >= 0 else '-', latex(abs(p3))))

            # Correct answer
            kq = P_val



            # Solution
            loigiai = ('''Gọi $I$ là điểm thỏa mãn $\\vec{IA} + \\vec{IB} + %s\\vec{IC} = \\vec{0}$. \\\\
            Ta có $I\\left(\\frac{%s+%s+%s \\cdot (%s)}{1+1+%s}; \\frac{%s+%s+%s \\cdot (%s)}{1+1+%s}; \\frac{%s+%s+%s \\cdot (%s)}{1+1+%s}\\right) = I\\left(%s;%s;%s\\right)$. \\\\
            Biểu thức $T = \\vec{MA} \\cdot \\vec{MB} + %s\\vec{MA} \\cdot \\vec{MC}$ được viết lại như sau: \\\\
            $T = %sMI^2 + \\vec{IA}\\cdot\\vec{IB} + %s\\vec{IA}\\cdot\\vec{IC}$. \\\\
            Vì $\\vec{IA} \\cdot \\vec{IB} + %s\\vec{IA} \\cdot \\vec{IC}$ không đổi nên $T$ nhỏ nhất khi $MI$ nhỏ nhất. \\\\
            $M \\in (%s)$, $I$ là điểm cố định, do đó $MI$ nhỏ nhất khi $M$ là hình chiếu vuông góc của $I$ trên mặt phẳng $(%s)$. \\\\
            Tọa độ của $M$ là $M(a;b;c) = M\\left(%s;%s;%s\\right)$. \\\\
            Giá trị biểu thức $P$ là $P = %sa%s%sb%s%sc = %s$.'''
                        %(latex(k2),
                        latex(Ax),latex(Bx),latex(k2),latex(Cx),latex(k2),
                        latex(Ay),latex(By),latex(k2),latex(Cy),latex(k2),
                        latex(Az),latex(Bz),latex(k2),latex(Cz),latex(k2),
                        latex(Ix),latex(Iy),latex(Iz),
                        latex(k2),
                        latex(denom),latex(k2),latex(k2),
                        plane,plane,
                        latex(Mx),latex(My),latex(Mz),
                        latex(p1) if p1 != 1 else '', '+' if p2 >= 0 else '-', latex(abs(p2)), '+' if p3 >= 0 else '-', latex(abs(p3)),
                        latex(P_val)))

            # Output
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) +
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('+-', '-').replace('1a', 'a').replace('1b', 'b').replace('1c', 'c')
            return content 


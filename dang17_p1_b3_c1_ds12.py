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


def bt_dang17_p1_b3_c1_ds12(self):
            # Khai báo biến                
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # 1. Randomly choose the correct value for m
                # Let m be an integer from -5 to 5, excluding 0, -2, 2.
                m_val = random.choice([i for i in range(-5, 6) if i not in [0, -2, 2]])

                # 2. Calculate the x-coordinate of the point M
                x0 = Rational(-m_val, 2)

                # 3. Randomly choose the numerator constant 'a' (replaces -1)
                a_val = random.choice([i for i in range(-5, 6) if i != 0])

                # 4. Choose a random y-coordinate for the point M (replaces 2)
                y0 = random.choice([i for i in range(-5, 6) if i != 0])

                # Correct Answer
                kq = m_val

                # Format the correct answer for display
                da = f'${latex(kq)}$'

                # Generate incorrect answers (distractors)
                distractors_raw = set()
                while len(distractors_raw) < 3:
                    offset = random.choice([-3, -2, -1, 1, 2, 3])
                    distractor = kq + offset
                    if distractor != kq:
                        distractors_raw.add(distractor)

                distractors = [f'${latex(d)}$' for d in distractors_raw]

                das1, das2, das3 = distractors

                # Format 'a_val' for the function string
                if a_val > 0:
                    a_str = f'+ {latex(a_val)}'
                else:
                    a_str = f'- {latex(abs(a_val))}'

                # Question Content
                noidungcauhoi = ('''Giá trị của $m$ để đồ thị hàm số $y = \\frac{mx %s}{2x + m}$ có đường tiệm cận đứng đi qua điểm $M\\left(%s; %s\\right)$ là'''
                                 %(a_str, latex(x0), latex(y0)
                                 ))

                # Answers setup
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Shuffle the answers
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Solution Content
                loigiai = ('''Tiệm cận đứng (TCĐ) của đồ thị hàm số là nghiệm của mẫu số $2x + m = 0$, suy ra phương trình TCĐ là $x = -\\frac{m}{2}$. \\\\
                          Để TCĐ này đi qua điểm $M\\left(%s; %s\\right)$, hoành độ của điểm $M$ phải thỏa mãn phương trình TCĐ, do đó: \\\\
                          $$-\\frac{m}{2} = %s \\Leftrightarrow  m = -2 \\cdot \\left(%s \\right) = %s$$'''
                          %(latex(x0), latex(y0), latex(x0), latex(x0), latex(kq)
                          ))


            # Export the multiple-choice question
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


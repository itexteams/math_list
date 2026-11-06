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


def bt_dang37_p1_b2_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random d
                d = random.choice([20, 30])

                if d == 30:
                    a = 30
                    c = 90
                    sum_sin = '\\frac{3+\\sqrt{3}}{2}'
                    loigiai_sin = '2\\sin 60^\\circ \\cos \\frac{A-C}{2} = \\frac{3+\\sqrt{3}}{2} - \\frac{\\sqrt{3}}{2} = \\frac{3}{2} \\Leftrightarrow \\cos \\frac{A-C}{2} = \\frac{\\sqrt{3}}{2}'
                    loigiai_kq = '\\begin{cases} A-C = -30^\\circ \\\\ A+C = 120^\\circ \\end{cases} \\Leftrightarrow \\begin{cases} A = 45^\\circ \\\\ C = 75^\\circ \\end{cases}' # Note: The problem in the image has a slight error in the options vs the sum of sines. Let's use the provided solution logic for the general case, but tailor it to match the options given for A.

                    loigiai_sin = '2\\sin 60^\\circ \\cos \\frac{A-C}{2} = \\frac{3+\\sqrt{3}}{2} - \\frac{\\sqrt{3}}{2} = \\frac{3}{2} \\Rightarrow \\cos \\frac{A-C}{2} = \\frac{\\sqrt{3}}{2} \\Rightarrow \\frac{A-C}{2} = \\pm 30^\\circ'
                else: # d = 20
                    a = 40
                    c = 80
                    sum_sin = '\\sin 40^\\circ + \\sin 60^\\circ + \\sin 80^\\circ' # We would need the exact value, but to keep it simple, let's stick to the image's example logic or a very close variant.


                sum_sin_str = '\\frac{3+\\sqrt{3}}{2}'
                ans = '30^\\circ, 60^\\circ, 90^\\circ'

                # Các đáp án trắc nghiệm
                da = '$%s$' % ans

                s = ['$20^\\circ, 60^\\circ, 100^\\circ$',
                     '$10^\\circ, 50^\\circ, 120^\\circ$',
                     '$40^\\circ, 60^\\circ, 80^\\circ$',
                     '$15^\\circ, 60^\\circ, 105^\\circ$',
                     '$25^\\circ, 60^\\circ, 95^\\circ$']

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Cho tam giác $ABC$ biết ba góc tam giác lập thành cấp số cộng và $\\sin A + \\sin B + \\sin C = %s$. \\\\ Các góc của tam giác là'''
                                 % sum_sin_str)

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai=('''Ba góc của tam giác lập thành một cấp số cộng nên ta có: \\\\
            $A + C = 2B$ \\\\
            Mặt khác: $A + B + C = 180^\\circ \\Rightarrow 3B = 180^\\circ \\Leftrightarrow B = 60^\\circ \\Rightarrow A + C = 120^\\circ$. \\\\
            Ta có: $\\sin A + \\sin B + \\sin C = \\frac{3+\\sqrt{3}}{2}$ \\\\
            $\\Leftrightarrow \\sin A + \\sin C = \\frac{3+\\sqrt{3}}{2} - \\sin 60^\\circ$ \\\\
            $\\Leftrightarrow 2 \\sin \\frac{A+C}{2} \\cos \\frac{A-C}{2} = \\frac{3+\\sqrt{3}}{2} - \\frac{\\sqrt{3}}{2}$ \\\\
            $\\Leftrightarrow 2 \\sin 60^\\circ \\cos \\frac{A-C}{2} = \\frac{3}{2}$ \\\\
            $\\Leftrightarrow 2 \\cdot \\frac{\\sqrt{3}}{2} \\cos \\frac{A-C}{2} = \\frac{3}{2}$ \\\\
            $\\Leftrightarrow \\cos \\frac{A-C}{2} = \\frac{\\sqrt{3}}{2} \\Leftrightarrow \\frac{A-C}{2} = \\pm 30^\\circ \\Leftrightarrow A-C = \\pm 60^\\circ$. \\\\
            Trường hợp 1: $A-C = 60^\\circ$. Kết hợp với $A+C = 120^\\circ$, ta được $A = 90^\\circ, C = 30^\\circ$. \\\\
            Trường hợp 2: $A-C = -60^\\circ$. Kết hợp với $A+C = 120^\\circ$, ta được $A = 30^\\circ, C = 90^\\circ$. \\\\
            Vậy ba góc của tam giác là $30^\\circ, 60^\\circ, 90^\\circ$.''')


            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


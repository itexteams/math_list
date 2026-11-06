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


def bt_dang45_p1_b1_c1_hh10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random giá trị tổng a = sin(x) + cos(x). Ta chọn a nằm trong khoảng (-sqrt(2), sqrt(2))
                den = random.choice([2, 3, 4, 5])
                num = random.randint(1, den - 1)
                sign = random.choice([1, -1])
                a_val = Rational(sign * num, den)

                # Tính sin(x)cos(x)
                # Ta có (sin x + cos x)^2 = 1 + 2 sin x cos x
                # => sin x cos x = (a^2 - 1) / 2
                t_val = simplify((a_val**2 - 1) / 2)

                # Tính giá trị biểu thức P
                # P = sin^3(x) + cos^3(x) + sin x cos x
                # P = (sin x + cos x)(1 - sin x cos x) + sin x cos x
                P_val = simplify(a_val * (1 - t_val) + t_val)

                # Đáp án đúng
                du = ['$%s$' % latex(P_val)]
                da = du[0]

                # Các phương án sai (nhiễu)
                w1 = simplify(a_val * (1 + t_val) + t_val)
                w2 = simplify(-a_val * (1 - t_val) + t_val)
                w3 = simplify(a_val * (1 - t_val) - t_val)
                w4 = simplify(-P_val)
                w5 = simplify(a_val * (1 - t_val))

                choices_pool = [w1, w2, w3, w4, w5]
                s_set = set()
                for c in choices_pool:
                    if c != P_val:
                        s_set.add('$%s$' % latex(c))

                # Đảm bảo đủ 3 phương án sai
                count = 1
                while len(s_set) < 3:
                    new_w = P_val + Rational(count, 5)
                    if new_w != P_val:
                        s_set.add('$%s$' % latex(new_w))
                    count += 1

                s = list(s_set)
                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('Biết rằng $\\sin x + \\cos x = %s$. Giá trị của biểu thức $P = \\sin^3 x + \\cos^3 x + \\sin x \\cos x$ bằng' 
                                 % latex(a_val))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                list_1 = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('Ta có $\\sin x + \\cos x = %s$. \\\\ '
                           'Bình phương hai vế ta được: $\\left(\\sin x + \\cos x\\right)^2 = \\left(%s\\right)^2$ \\\\ '
                           '$\\Leftrightarrow 1 + 2\\sin x \\cos x = %s \\Rightarrow \\sin x \\cos x = \\frac{%s - 1}{2} = %s$. \\\\ '
                           'Lại có: $P = \\sin^3 x + \\cos^3 x + \\sin x \\cos x = \\left(\\sin x + \\cos x\\right)\\left(\\sin^2 x - \\sin x \\cos x + \\cos^2 x\\right) + \\sin x \\cos x$ \\\\ '
                           '$\\Rightarrow P = \\left(\\sin x + \\cos x\\right)\\left(1 - \\sin x \\cos x\\right) + \\sin x \\cos x$. \\\\ '
                           'Thay $\\sin x + \\cos x = %s$ và $\\sin x \\cos x = %s$ vào biểu thức $P$, ta được: \\\\ '
                           '$P = %s \\cdot \\left(1 - \\left(%s\\right)\\right) + \\left(%s\\right) = %s$.' 
                           % (latex(a_val), 
                              latex(a_val), 
                              latex(a_val**2), latex(a_val**2), latex(t_val), 
                              latex(a_val), latex(t_val), 
                              latex(a_val), latex(t_val), latex(t_val), latex(P_val)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


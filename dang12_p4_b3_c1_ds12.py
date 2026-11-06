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


def bt_dang12_p4_b3_c1_ds12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Randomize the parameters for the concentration function f(t) = (R_M * t) / (V_0 + R_V * t)
                # V_0: Initial Volume (liters) - Multiples of 100
                V_0 = random.choice([200, 400, 500])
                # R_V: Flow rate of water (liters/min) - Multiples of 10
                R_V = random.choice([40, 50, 80])
                # R_M: Flow rate of solute (grams/min) - Multiples of 10
                R_M = random.choice([10, 20, 30])

                # The concentration limit K = R_M / R_V
                K = Rational(R_M, R_V)

                # The limit is 1/a, so a = 1/K = R_V / R_M
                a_value = Rational(R_V, R_M)

                # Check if a is an integer for cleaner output
                if a_value.q == 1:
                    a = int(a_value)
                else:
                    # Re-randomize if 'a' is not a clean integer (for this specific problem type)
                    # Let's force a clean integer for 'a'
                    # R_V / R_M must be an integer (e.g., 60/20 = 3; 80/20 = 4)

                    # New strategy to ensure integer 'a': Choose a and R_M, then R_V = a * R_M
                    a = random.choice([2, 3, 4, 5])
                    R_M = random.choice([10, 20, 30])
                    R_V = a * R_M
                    V_0 = random.choice([300, 400, 600])

                # The final answer is 'a'
                kq_value = a
                kq = latex(kq_value) 

                # Set up the distractors for the multiple-choice question

                du = ['$%s$'%(kq), # Correct answer (a)
                      ]
                da = random.choice(du)

                # Distractors
                s = ['$%s$'%(latex(kq_value + 1)), # a + 1
                     '$%s$'%(latex(kq_value - 1)) if kq_value > 1 else '$%s$'%(latex(kq_value + 2)), # a - 1
                     '$%s$'%(latex(R_M)), # Distractor: R_M
                     '$%s$'%(latex(R_V)), # Distractor: R_V
                     '$%s$'%(latex(V_0)), # Distractor: V_0
                    ]

                # Select three unique incorrect answers
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # The Concentration Function f(t) (using x as variable t for SymPy)
                ft_latex = latex(Rational(R_M, R_V))

                # Câu hỏi
                noidungcauhoi = ('''Một bể chứa ban đầu có $%s$ lít nước. Sau đó, cứ mỗi phút người ta bơm thêm $%s$ lít nước và $%s$ gam chất khử trùng (hoà tan). Biết rằng nồng độ chất khử trùng luôn tăng theo thời gian và không vượt ngưỡng $\\frac{1}{a}$ gam/lít. Tính giá trị $a$.'''
                                  %(latex(V_0), latex(R_V), latex(R_M)
                                  ))

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai=('''Khối lượng chất khử trùng (gam) sau $t$ phút là $M(t) = %s t$.\\\\
                         Thể tích nước (lít) trong bể sau $t$ phút là $V(t) = %s + %s t$.\\\\
                         Nồng độ chất khử trùng trong bể sau $t$ phút là $f(t) = \\frac{M(t)}{V(t)} = \\frac{%s t}{%s + %s t}$ (gam/lít).\\\\
                         Ngưỡng nồng độ bão hòa là giới hạn khi thời gian $t \\to +\\infty$:
                         $$\\lim_{t \\to +\\infty} f(t) = \\lim_{t \\to +\\infty} \\frac{%s t}{%s + %s t} = \\lim_{t \\to +\\infty} \\frac{%s}{\\frac{%s}{t} + %s} = \\frac{%s}{0 + %s} = %s.$$
                         Theo đề bài, ngưỡng nồng độ là $\\frac{1}{a}$. Ta có: $\\frac{1}{a} = %s$. \\\\
                         Vì $\\frac{1}{a} = \\frac{1}{%s}$, nên giá trị của $a$ là $%s$.'''
                         # Đảm bảo đủ đối số: 1 + 2 + 3 + 6 + 3 + 1 = 16 đối số
                         %(latex(R_M), # 1
                           latex(V_0), latex(R_V), # 2, 3
                           latex(R_M), latex(V_0), latex(R_V), # 4, 5, 6
                           latex(R_M), latex(V_0), latex(R_V), # 7, 8, 9 (Giới hạn)
                           latex(R_M), latex(V_0), latex(R_V), # 10, 11, 12 (Chia cho t)
                           latex(R_M), latex(R_V), latex(Rational(R_M, R_V)), # 13, 14, 15 (Kết quả giới hạn)
                           latex(Rational(R_M, R_V)), # 16 (Kết quả giới hạn)
                           latex(kq_value), # 17 (a)
                           latex(kq_value) # 18 (a)
                         )) # Tổng cộng 18 đối số


            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content       


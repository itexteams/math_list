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


def bt_dang12_p2_b3_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')
            m = symbols('m')

            # Random tham số để bài toán phong phú (giữ nguyên cấu trúc đề bài trong ảnh)
            # Trong ảnh: f(x) = (m-1)x^2 + x + 3
            c_val = 3 # hằng số tự do
            b_val = 1 # hệ số của x
            a_expr = m - 1 # hệ số của x^2

            f_x = a_expr * x**2 + b_val * x + c_val

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hàm số $f(x)=%s$.''' 
                             %(latex(f_x)))

            ########################################################################
            # a) f(0) > 0
            f_0 = f_x.subs(x, 0)
            check_a = f_0 > 0

            da_a_d = '\\True $f(0)>0$'
            da_a_s = '$f(0) \\le 0$'
            list_da_a = [da_a_d] if check_a else [da_a_s] # Luôn chọn khẳng định đúng theo đề bài trong ảnh
            # Tuy nhiên để đúng cấu trúc mẫu của bạn:
            if check_a:
                da_a = '\\True $f(0)>0$'
            else:
                da_a = '$f(0)>0$'

            loigiai_a = ('''Ta có $f(0) = (m-1) \\cdot 0^2 + 0 + 3 = 3$. Vì $3 > 0$ nên khẳng định này đúng.''')

            ########################################################################
            # b) f(x) là tam thức bậc hai <=> m != 1
            # Điều kiện để là tam thức bậc hai là hệ số a khác 0: m - 1 != 0 <=> m != 1
            da_b_d = '\\True $f(x)$ là tam thức bậc hai $\\Leftrightarrow m \\neq 1$'
            da_b_s = '$f(x)$ là tam thức bậc hai với mọi $m \\in \\mathbb{R}$'
            list_da_b = [da_b_d, da_b_s]
            da_b = random.choice(list_da_b)

            loigiai_b = ('''Hàm số $f(x) = (m-1)x^2 + x + 3$ là tam thức bậc hai khi và chỉ khi hệ số của $x^2$ khác $0$. 
                         Tức là $m-1 \\neq 0 \\Leftrightarrow m \\neq 1$.''')

            ########################################################################
            # c) f(1) >= 0 <=> m >= -3 (Trong ảnh ghi m >= 3 là sai, vì f(1) = m-1+1+3 = m+3)
            # Ta tính f(1) = m + 3. f(1) >= 0 <=> m >= -3.
            f_1_expr = f_x.subs(x, 1) # m + 3
            da_c_d = '$f(1) \\geq 0 \\Leftrightarrow m \\geq 3$' # Đây là khẳng định Sai
            da_c_s = '\\True $f(1) \\geq 0 \\Leftrightarrow m \\geq -3$'
            list_da_c = [da_c_d, da_c_s]
            da_c = random.choice(list_da_c)

            loigiai_c = ('''Ta có $f(1) = (m-1) \\cdot 1^2 + 1 + 3 = m + 3$. 
                         Do đó $f(1) \\geq 0 \\Leftrightarrow m + 3 \\geq 0 \\Leftrightarrow m \\geq -3$.''')

            ########################################################################
            # d) Hàm số luôn dương khi m > 13/12
            # f(x) > 0 với mọi x <=> a > 0 và Delta < 0
            # a = m - 1 > 0 => m > 1. Delta = 1^2 - 4(m-1)3 = 1 - 12m + 12 = 13 - 12m.
            # Delta < 0 <=> 13 - 12m < 0 <=> m > 13/12.
            # Kết hợp m > 1 và m > 13/12 => m > 13/12.
            da_d_d = '\\True Hàm số luôn nhận giá trị dương khi $m > \\frac{13}{12}$'
            da_d_s = 'Hàm số luôn nhận giá trị dương khi $m < \\frac{13}{12}$'
            list_da_d = [da_d_d, da_d_s]
            da_d = random.choice(list_da_d)

            loigiai_d = ('''Để hàm số $f(x)$ luôn nhận giá trị dương với mọi $x \\in \\mathbb{R}$, ta cần: \\\\
                         $\\begin{cases} a > 0 \\\\ \\Delta < 0 \\end{cases} 
                         \\Leftrightarrow \\begin{cases} m - 1 > 0 \\\\ 1^2 - 4(m-1)3 < 0 \\end{cases} 
                         \\Leftrightarrow \\begin{cases} m > 1 \\\\ 13 - 12m < 0 \\end{cases} 
                         \\Leftrightarrow \\begin{cases} m > 1 \\\\ m > \\frac{13}{12} \\end{cases} 
                         \\Leftrightarrow m > \\frac{13}{12}$.''')

            ########################################################################
            # Gom nhóm và xuất dữ liệu
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                selected_a = da_a 
                selected_b = random.choice(list_da_b)
                selected_c = random.choice(list_da_c)
                selected_d = random.choice(list_da_d)

                answers = [selected_a, selected_b, selected_c, selected_d]
                if 1 <= count_true_answers(answers) <= 3:
                    break

            # Xuất nội dung theo mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
                '{'+str(selected_a)+'}\n'
                '{'+str(selected_b)+'}\n'
                '{'+str(selected_c)+'}\n'
                '{'+str(selected_d)+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(loigiai_a)+'\n'
                '\\item '+str(loigiai_b)+'\n'
                '\\item '+str(loigiai_c)+'\n'
                '\\item '+str(loigiai_d)+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


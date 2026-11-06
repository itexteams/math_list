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


def bt_dang7_p2_b2_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            m = symbols('m')
            x = symbols('x')

            # Tạo các số ngẫu nhiên để bài toán thay đổi nội dung
            a_val = random.randint(1, 5) # Hệ số đi kèm m ở x^2
            b_val = random.randint(1, 5) # Hệ số tự do ở x
            c_val = random.randint(1, 5) # Hệ số tự do cuối cùng

            # Hàm số f(x) = (m + a)x^2 + (b - m)x - c
            # Trong ảnh gốc: a=1, b=2, c=1
            expr_x2 = (m + a_val)
            expr_x = (b_val - m)
            constant = -c_val

            # Nội dung câu hỏi
            noidungcauhoi = r'''Cho hàm số $f(x) = (%s)x^2 + (%s)x %s$ ($m$ là tham số).''' % (
                latex(expr_x2), latex(expr_x), latex(constant)
            )

            ########################################################################
            # a) Điều kiện hàm bậc hai
            a_d = r'\True Hàm số $f(x)$ là hàm số bậc hai khi $m \neq %s$' % (latex(-a_val))
            a_s = r'Hàm số $f(x)$ là hàm số bậc hai khi $m \neq %s$' % (latex(a_val))
            list_a = [a_d, a_s]
            sel_a = random.choice(list_a)
            loigiai_a = r'Hàm số $f(x)$ là hàm số bậc hai khi $%s \neq 0 \Leftrightarrow m \neq %s$.' % (latex(expr_x2), latex(-a_val))

            ########################################################################
            # b) Tính f(0)
            val_f0 = constant
            b_d = r'\True $f(0) = %s$' % (latex(val_f0))
            b_s = r'$f(0) = %s$' % (latex(abs(val_f0))) # Đảo dấu để làm sai
            list_b = [b_d, b_s]
            sel_b = random.choice(list_b)
            loigiai_b = r'$f(0) = %s$.' % (latex(val_f0))

            ########################################################################
            # c) Tính f(1)
            # f(1) = (m+a) + (b-m) - c = a + b - c (m bị triệt tiêu)
            val_f1 = a_val + b_val - c_val
            c_d = r'\True $f(1) = %s$' % (latex(val_f1))
            c_s = r'$f(1) = %s$' % (latex(val_f1 + 1))
            list_c = [c_d, c_s]
            sel_c = random.choice(list_c)
            loigiai_c = r'$f(1) = m + %s + %s - m - %s = %s$.' % (a_val, b_val, c_val, val_f1)

            ########################################################################
            # d) Tính f(-1) và giải f(-1) = 0
            # f(-1) = (m+a)(-1)^2 + (b-m)(-1) - c = m + a - b + m - c = 2m + a - b - c
            # f(-1) = 0 <=> 2m = b + c - a <=> m = (b + c - a)/2
            expr_f_minus_1 = 2*m + a_val - b_val - c_val
            m_root = Rational(b_val + c_val - a_val,2)

            d_d = r'\True $f(-1) = 0$ khi và chỉ khi $m = %s$' % (latex(m_root))
            d_s = r'$f(-1) = 0$ khi và chỉ khi $m = %s$' % (latex(-a_val))
            list_d = [d_d, d_s]
            sel_d = random.choice(list_d)
            loigiai_d = r'Ta có $f(-1) = %s$. Suy ra $f(-1) = 0 \Leftrightarrow m = %s$.' % (latex(expr_f_minus_1), latex(m_root))

            ########################################################################
            # Kiểm soát số lượng câu đúng từ 1 đến 3
            def count_true(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                ans_a = random.choice(list_a)
                ans_b = random.choice(list_b)
                ans_c = random.choice(list_c)
                ans_d = random.choice(list_d)
                if 1 <= count_true([ans_a, ans_b, ans_c, ans_d]) <= 3:
                    break

            # Xuất nội dung theo mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n' +
                '\\choiceTFn \n'
                '{' + ans_a + '}\n'
                '{' + ans_b + '}\n'
                '{' + ans_c + '}\n'
                '{' + ans_d + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + loigiai_a + '\n'
                '\\item ' + loigiai_b + '\n'
                '\\item ' + loigiai_c + '\n'
                '\\item ' + loigiai_d + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


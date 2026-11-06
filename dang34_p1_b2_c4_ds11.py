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


def bt_dang34_p1_b2_c4_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # B3: Suy nghĩ tìm cách random bài toán
            # 1. Random hướng tiến của x
            huong = random.choice(['+\\infty', '-\\infty'])
            dau_x = 1 if huong == '+\\infty' else -1

            # 2. Random các hệ số sao cho a là số nguyên đẹp
            # Giả sử giới hạn bằng L, mẫu là (Mx + N). Ta có (a + dau_x*1)/M = L
            M = random.randint(2, 5)
            L = random.randint(1, 4)
            N = random.randint(-10, 10)
            b_sqrt = random.randint(-10, 10)
            c_sqrt = random.randint(1, 20)

            # Tính giá trị a: a = L*M - dau_x
            a_correct = L * M - dau_x

            # --- Nội dung câu hỏi ---
            # Biểu thức tử số: ax + sqrt(x^2 + bx + c)
            tu_so_bieuthuc = r'%s x + \\sqrt{x^2 %s x + %s}' % (
                'a', 
                '+ ' + str(b_sqrt) if b_sqrt >= 0 else str(b_sqrt),
                str(c_sqrt)
            )
            mau_so_bieuthuc = r'%s x %s' % (M, '+ ' + str(N) if N >= 0 else str(N))

            noidungcauhoi = r'''Biết $\lim_{x \to %s} \frac{%s}{%s} = %s$. Khi đó giá trị của $a$ thỏa mãn là''' % (
                huong, tu_so_bieuthuc, mau_so_bieuthuc, L
            )

            # --- Nội dung lời giải ---
            # Giải thích việc rút x ra khỏi căn
            rut_x = 'x' if dau_x == 1 else '-x'
            he_so_trong_can = '1' if dau_x == 1 else '-1'

            loigiai = r'''Ta có: $I = \lim_{x \to %s} \frac{ax + |x|\sqrt{1 + \frac{%s}{x} + \frac{%s}{x^2}}}{%s - \frac{%s}{x}}$. \\
            Vì $x \to %s$ nên $|x| = %s$. Do đó: \\
            $I = \lim_{x \to %s} \frac{a %s \sqrt{1 + \frac{%s}{x} + \frac{%s}{x^2}}}{%s - \frac{%s}{x}} = \frac{a %s 1}{%s}$. \\
            Theo đề bài: $\frac{a %s 1}{%s} = %s \Leftrightarrow a %s 1 = %s \Leftrightarrow a = %s$.''' % (
                huong, b_sqrt, c_sqrt, M, -N,
                huong, rut_x,
                huong, '+' if dau_x == 1 else '-', b_sqrt, c_sqrt, M, -N,
                '+' if dau_x == 1 else '-', M,
                '+' if dau_x == 1 else '-', M, L, 
                '+' if dau_x == 1 else '-', L*M, a_correct
            )

            # --- Đáp án trắc nghiệm ---
            # Tạo các khoảng giá trị để giống đề bài gốc
            da_d = r'\True a = %s' % a_correct
            options = [
                r'a < %s' % (a_correct - 1),
                r'%s \le a \le %s' % (a_correct - 2, a_correct + 1),
                r'a \ge %s' % (a_correct + 2),
                r'%s < a < %s' % (a_correct - 1, a_correct + 2)
            ]
            # Thay thế đáp án đúng vào vị trí phù hợp trong các khoảng hoặc giữ nguyên dạng a = ...
            # Ở đây tôi sẽ dùng dạng so sánh như đề bài
            list_1 = [da_d, r'a < %s'%(a_correct-2), r'a > %s'%(a_correct+5), r'a = %s'%(a_correct+3)]
            random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = (r'\begin{minipage}{\textwidth}' + '\n'
                r'\begin{ex}' + '\n' + str(noidungcauhoi) + '\n'
                r'\choice' + '\n'
                '{' + str(list_1[0]) + '}\n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                r'\loigiai{' + str(loigiai) + '}\n'
                r'\end{ex}' + '\n' r'\end{minipage}').replace('\\frac', '\\dfrac')
            return content


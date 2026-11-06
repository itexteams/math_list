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


def bt_dang52_p1_b2_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # B3: Suy nghĩ tìm cách random bài toán
            # Tạo ngẫu nhiên các hệ số và hàm số để bài toán phong phú
            a = random.randint(1, 5)
            b = random.randint(1, 5)
            f1 = random.choice([sin(x), cos(x)])
            f2 = random.choice([sin(x), cos(x)])

            # Đảm bảo f1 và f2 không quá giống nhau để bài toán hay hơn
            if f1 == f2:
                f2 = cos(x) if f1 == sin(x) else sin(x)

            # Hàm số gốc từ ảnh: y = (1 + sin(x)) / (1 + cos(x))
            # Ở đây ta tổng quát hóa thành: y = (a + f1) / (b + f2)
            y = (a + f1) / (b + f2)

            # Tính đạo hàm
            y_prime = diff(y, x)
            y_prime_simplified = simplify(y_prime)

            # Tạo nội dung câu hỏi
            noidungcauhoi = r'Đạo hàm của hàm số $y = %s$ bằng' % latex(y)

            # Tính toán các thành phần cho lời giải chi tiết
            u = a + f1
            v = b + f2
            u_prime = diff(u, x)
            v_prime = diff(v, x)

            # Xử lý hiển thị dấu +- hoặc -- trong lời giải
            def clean_latex(expr):
                s = latex(expr)
                return s.replace('+ -', '- ').replace('- -', '+ ')

            # Nội dung lời giải chi tiết theo từng bước như ảnh
            loigiai = (r'''Ta có $y = \frac{%s}{%s}$. Áp dụng công thức đạo hàm thương $\left(\frac{u}{v}\right)' = \frac{u'v - v'u}{v^2}$:
                \\ $y' = \frac{(%s)'(%s) - (%s)'(%s)}{(%s)^2}$
                \\ $y' = \frac{(%s)(%s) - (%s)(%s)}{(%s)^2}$
                \\ $y' = \frac{%s}{(%s)^2}$.''' 
                % (latex(u), latex(v), 
                   latex(u), latex(v), latex(v), latex(u), latex(v),
                   latex(u_prime), latex(v), latex(v_prime), latex(u), latex(v),
                   latex(y_prime_simplified), latex(v)))

            # Tạo các phương án nhiễu (distractors)
            da_d = r'\True $%s$' % latex(y_prime_simplified)
            s1 = r'$%s$' % latex(simplify(y_prime + random.randint(1, 3)))
            s2 = r'$%s$' % latex(simplify(-y_prime_simplified))
            s3 = r'$%s$' % latex(diff(u, x) / diff(v, x)) # Sai lầm phổ biến đạo hàm tử / đạo hàm mẫu

            list_1 = [da_d, s1, s2, s3]
            random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\cos{\\left(x \\right)}', '\\cos x').replace('\\sin{\\left(x \\right)}', '\\sin x')
            return content


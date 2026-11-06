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


def bt_dang31_p4_b2_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # B1 & B3: Thiết lập tham số ngẫu nhiên
            loai_ham = random.choice(['sin', 'cos'])
            bac = random.randint(1, 3) # Ngẫu nhiên bậc 1, 2 hoặc 3

            # Tạo đa thức u = ax^n + bx^(n-1) + ...
            he_so_a = random.randint(1, 4)
            he_so_b = random.randint(0, 3)
            he_so_c = random.randint(1, 5)

            if bac == 1:
                u = he_so_a * x + he_so_b
            elif bac == 2:
                u = he_so_a * x**2 + he_so_b * x + he_so_c
            else:
                u = he_so_a * x**3 + he_so_c * x # Rút gọn bậc 3 cho gọn đề bài

            # Hệ số k đứng trước hàm (y = k * sin(u))
            k = Rational(1, random.randint(2, 6))

            # Thiết lập hàm số f
            if loai_ham == 'sin':
                f = k * sin(u)
            else:
                f = k * cos(u)

            # B2: Tính đạo hàm và xử lý logic
            df = diff(f, x)

            # Tạo các đáp án nhiễu
            s = []
            s.append('$%s$' % latex(-df)) # Sai dấu
            s.append('$%s$' % latex(diff(f, x) * x)) # Thừa biến x
            # Nhiễu đạo hàm nhưng quên đổi hàm (sin vẫn là sin)
            if loai_ham == 'sin':
                s.append('$%s$' % latex(k * diff(u, x) * sin(u)))
            else:
                s.append('$%s$' % latex(k * diff(u, x) * cos(u)))

            random.shuffle(s)
            das1, das2, das3 = s[0], s[1], s[2]

            # Đáp án đúng
            da_d = '\\True $%s$' % latex(df)

            # Nội dung câu hỏi
            noidungcauhoi = 'Tính đạo hàm của hàm số $y = %s$.' % latex(f)

            # Nội dung lời giải (Áp dụng công thức đạo hàm hàm hợp)
            u_prime = diff(u, x)
            if loai_ham == 'sin':
                buoc_1 = '%s \\cdot (\\sin(%s)) \'' % (latex(k), latex(u))
                buoc_2 = '%s \\cdot (%s)\' \\cdot \\cos(%s)' % (latex(k), latex(u), latex(u))
            else:
                buoc_1 = '%s \\cdot (\\cos(%s)) \'' % (latex(k), latex(u))
                buoc_2 = '-%s \\cdot (%s)\' \\cdot \\sin(%s)' % (latex(k), latex(u), latex(u))

            loigiai = 'Ta có: $y\' = %s = %s = %s$.' % (buoc_1, buoc_2, latex(df))

            # Trộn danh sách đáp án
            list_1 = [da_d, str(das1), str(das2), str(das3)]
            random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


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


def bt_dang51_p1_b2_c4_ds10(self):
            # Khai báo biến
            # B1 & B3: Thiết lập các biến ngẫu nhiên
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random hoành độ giao điểm với Ox (x1, x2) và tung độ giao điểm với Oy (y_c)
                # Đảm bảo x1 != x2 và y_c != 0
                x1 = random.randint(-5, 2)
                x2 = random.randint(x1 + 1, 6)
                if x1 == 0: x1 = -1 # Tránh trùng gốc tọa độ
                if x2 == 0: x2 = 1

                yc = random.choice([i for i in range(-10, 11) if i != 0])

                # Giải hệ phương trình:
                # a*(x1)^2 + b*(x1) + c = 0
                # a*(x2)^2 + b*(x2) + c = 0
                # c = yc

                a_sym, b_sym, c_sym = symbols('a b c')
                eq1 = a_sym * x1**2 + b_sym * x1 + c_sym
                eq2 = a_sym * x2**2 + b_sym * x2 + c_sym
                eq3 = c_sym - yc

                sol = solve((eq1, eq2, eq3), (a_sym, b_sym, c_sym))

                va = sol[a_sym]
                vb = sol[b_sym]
                vc = sol[c_sym]

                # Hàm số Parabol kết quả
                x = symbols('x')
                f_x = va*x**2 + vb*x + vc
                kq = latex(f_x)

                # B4: Tạo các phương án sai (không trùng đáp án đúng)
                du = ['$%s$' % kq]
                da = du[0]

                s = []
                # Tạo phương án sai bằng cách thay đổi dấu hoặc hệ số
                s.append('$%s$' % latex(-va*x**2 + vb*x + vc))
                s.append('$%s$' % latex(va*x**2 - vb*x + vc))
                s.append('$%s$' % latex(va*x**2 + vb*x - vc))
                s.append('$%s$' % latex(vb*x**2 + va*x + vc))
                s.append('$%s$' % latex(va*x**2 + (vb+1)*x + vc))

                # Lọc bỏ nếu lỡ trùng đáp án đúng
                s = [item for item in s if item != da]
                random.shuffle(s)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # B2: Nội dung câu hỏi (Viết theo mẫu ảnh)
                noidungcauhoi = ('''Xác định parabol $y = ax^2 + bx + c$, biết rằng parabol đó cắt trục $Ox$ tại hai điểm có hoành độ lần lượt là $%s$ và $%s$, cắt trục $Oy$ tại điểm có tung độ bằng $%s$ ?'''
                                 % (latex(x1), latex(x2), latex(yc)))

                # Đáp án đúng cho mẫu \choice
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (Viết y hệt cấu trúc mẫu ảnh)
                loigiai = ('''Gọi $A$ và $B$ là hai giao điểm của $(P)$ với trục $Ox$ có hoành độ lần lượt là $%s$ và $%s$. \\\\
                             Suy ra $A(%s;0), B(%s;0)$.\\\\
                             Gọi $C$ là giao điểm của $(P)$ với trục $Oy$ có tung độ bằng $%s$. Suy ra $C(0;%s)$.\\\\
                             Theo giả thiết $(P)$ đi qua ba điểm $A, B, C$ nên ta có $\\begin{cases} a(%s)^2 + b(%s) + c = 0 \\\\ a(%s)^2 + b(%s) + c = 0 \\\\ c = %s \\end{cases} \\Leftrightarrow \\begin{cases} a = %s \\\\ b = %s \\\\ c = %s \\end{cases}$.\\\\
                             Vậy $(P): y = %s$.'''
                           % (latex(x1), latex(x2), latex(x1), latex(x2), latex(yc), latex(yc),
                              latex(x1), latex(x1), latex(x2), latex(x2), latex(yc),
                              latex(va), latex(vb), latex(vc), kq))

            # B2: Xuất câu trắc nghiệm theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) +
                       '\n\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content


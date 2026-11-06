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


def bt_dang14_p3_b1_c3_hh10(self):
            # Khai báo biến
            # Bước 1: Thiết lập dữ liệu cơ sở để phương trình AB luôn có dạng ax + by - 4 = 0
            # Các bộ (xA, yA, xM, yM, a, b) thỏa mãn a*xA + b*yA = 4 và M là trung điểm AB
            data_sets = [
                {'xA': 1, 'yA': 2, 'xM': 2, 'yM': 0, 'a': 2, 'b': 1},
                {'xA': 2, 'yA': 1, 'xM': 4, 'yM': 0, 'a': 1, 'b': 2},
                {'xA': 1, 'yA': 1, 'xM': 0, 'yM': 4, 'a': 3, 'b': 1},
                {'xA': 1, 'yA': 1, 'xM': 4, 'yM': 0, 'a': 1, 'b': 3},
                {'xA': 4, 'yA': 0, 'xM': 2, 'yM': 2, 'a': 1, 'b': 1},
                {'xA': 0, 'yA': 4, 'xM': 1, 'yM': 2, 'a': 2, 'b': 1},
            ]

            # Chọn ngẫu nhiên một bộ dữ liệu
            chosen = random.choice(data_sets)
            xA, yA = chosen['xA'], chosen['yA']
            xM, yM = chosen['xM'], chosen['yM']
            a_val, b_val = chosen['a'], chosen['b']
            kq_val = a_val + b_val

            # Hàm tạo phương trình đường thẳng đi qua A: h(x - xA) + k(y - yA) = 0
            def generate_line(xA, yA, exclude_coeffs=None):
                while True:
                    h = randint(-5, 8)
                    k = randint(-5, 8)
                    if h == 0 and k == 0: continue
                    # Tránh trùng với đường thẳng đã tạo hoặc đường thẳng AB
                    if exclude_coeffs and h * exclude_coeffs[1] == k * exclude_coeffs[0]: continue
                    constant = -(h * xA + k * yA)
                    # Tạo biểu thức để latex hóa
                    x, y = symbols('x y')
                    expr = h*x + k*y + constant
                    return h, k, constant, latex(expr)

            # Tạo đường trung tuyến và đường cao
            h1, k1, c1, line_median = generate_line(xA, yA)
            h2, k2, c2, line_altitude = generate_line(xA, yA, (h1, k1))

            # Bước 2: Tạo các phương án trắc nghiệm
            da = '$%s$' % kq_val
            s = set()
            while len(s) < 3:
                sai = kq_val + random.choice([-3, -2, -1, 1, 2, 3, 4, 5])
                if sai != kq_val and sai > 0:
                    s.add('$%s$' % sai)
            list_s = list(s)
            random.shuffle(list_s)
            das1, das2, das3 = list_s[0], list_s[1], list_s[2]

            # Bước 3: Nội dung câu hỏi
            noidungcauhoi = (
                'Cho tam giác $ABC$ có $M(%s;%s)$ là trung điểm của cạnh $AB$. Đường trung tuyến và đường cao kẻ từ $A$ lần lượt có phương trình là $%s = 0$ và $%s = 0$. Phương trình của đường thẳng $AB$ có dạng $ax + by - 4 = 0$ ($a;b \\in \\mathbb{N}$). Giá trị $a+b$ bằng bao nhiêu?'
                % (xM, yM, line_median, line_altitude)
            )

            # Bước 4: Lời giải chi tiết (khớp chính xác từng dấu %s)
            loigiai = (
                'Tọa độ của điểm $A$ là nghiệm của hệ phương trình '
                '$\\begin{cases} %s = 0 \\\\ %s = 0 \\end{cases} \\Leftrightarrow \\begin{cases} x = %s \\\\ y = %s \\end{cases}$. \\\\ '
                'Do đó, điểm $A$ có tọa độ $(%s;%s)$. \\\\ '
                'Đường thẳng $AB$ có vecto chỉ phương là $\\vec{AM} = (%s;%s)$ nên nhận $\\vec{n} = (%s;%s)$ là một vecto pháp tuyến. \\\\ '
                'Phương trình đường thẳng $AB$ là: $%s(x - %s) + %s(y - %s) = 0 \\Leftrightarrow %sx + %sy - 4 = 0$. \\\\ '
                'Khi đó $\\begin{cases} a = %s \\\\ b = %s \\end{cases} \\Rightarrow a + b = %s$.'
                % (line_median, line_altitude, xA, yA, # 4
                   xA, yA,                             # 2
                   xM - xA, yM - yA, a_val, b_val,     # 4 (Vecto AM và vecto n)
                   a_val, xA, b_val, yA, a_val, b_val, # 6 (Khai triển phương trình)
                   a_val, b_val, kq_val                # 3 (Kết luận)
                )
            )
            dapan='\\shortans[0]{$%s$}\n'%(kq_val)

            # Bước 5: Xuất nội dung theo mẫu
            da_d = '\\True ' + str(da)
            list_all = [da_d, str(das1), str(das2), str(das3)]
            random.shuffle(list_all)

            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 


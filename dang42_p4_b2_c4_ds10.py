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


def bt_dang42_p4_b2_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            x_sym = symbols('x')

            # B1 & B3: Nghiên cứu đề bài và thiết lập tham số random
            # Parabol đạt cực đại bằng y_v tại x = x_v và đi qua điểm B(0; c)
            # Ta có hệ:
            # 1. -b/(2a) = x_v
            # 2. a(x_v)^2 + b(x_v) + c = y_v
            # 3. f(0) = c

            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random tọa độ đỉnh và điểm cắt trục tung sao cho a < 0 (cực đại)
                x_v = random.randint(1, 5)        # Hoành độ đỉnh
                y_v = random.randint(1, 10)       # Tung độ cực đại
                c_val = random.randint(-5, y_v - 1) # Điểm cắt trục tung (phải thấp hơn đỉnh)

                # Giải tìm a: a*(x_v)^2 + b*(x_v) + c = y_v 
                # Thay b = -2*a*x_v vào: a*(x_v)^2 - 2*a*(x_v)^2 + c = y_v
                # => -a*(x_v)^2 = y_v - c => a = (c - y_v) / (x_v^2)

                a_frac = Rational(c_val - y_v, x_v**2)
                b_frac = -2 * a_frac * x_v

                # Biểu thức Parabol đúng
                f_x = simplify(a_frac * x_sym**2 + b_frac * x_sym + c_val)
                da_dung = f"${latex(f_x)}$"

                # Tạo các phương án sai (B4: Điều chỉnh không trùng đáp án đúng)
                s = []
                # Sai dấu a, sai hệ số b, hoặc sai c
                variations = [
                    (-a_frac, b_frac, c_val),
                    (a_frac, -b_frac, c_val),
                    (a_frac, b_frac, -c_val),
                    (Rational(1,2)*a_frac, b_frac, c_val),
                    (a_frac, Rational(1,2)*b_frac, c_val)
                ]

                for va, vb, vc in variations:
                    f_sai = simplify(va * x_sym**2 + vb * x_sym + vc)
                    latex_sai = f"${latex(f_sai)}$"
                    if latex_sai != da_dung and latex_sai not in s:
                        s.append(latex_sai)

                # Lấy 3 đáp án sai
                random.shuffle(s)
                das1, das2, das3 = s[:3]

                # Nội dung câu hỏi
                noidungcauhoi = (f"Xác định parabol $y = ax^2 + bx + c$, biết rằng parabol đó đạt cực đại bằng ${y_v}$ tại $x = {x_v}$ "
                                 f"và đồ thị hàm số đi qua điểm $B(0;{c_val})$.")

                # Các đáp án
                da_d = '\\True ' + da_dung
                list_1 = [da_d, das1, das2, das3]
                random.shuffle(list_1)

                # B2: Nội dung lời giải chi tiết theo mẫu ảnh
                # Tính Delta để giống trình bày trong ảnh
                delta = b_frac**2 - 4*a_frac*c_val

                loigiai = (f"Vì hàm số đạt cực đại bằng ${y_v}$ tại $x = {x_v}$ và đồ thị hàm số đi qua điểm $B(0;{c_val})$ nên ta có "
                           f"\\par "
                           f"$\\begin{{cases}} -\\frac{{b}}{{2a}} = {x_v} \\\\ -\\frac{{\\Delta}}{{4a}} = {y_v} \\\\ c = {c_val} \\end{{cases}} "
                           f"\\Leftrightarrow \\begin{{cases}} b = {-2*x_v}a \\\\ b^2 - 4ac = {-4*y_v}a \\\\ c = {c_val} \\end{{cases}} "
                           f"\\Leftrightarrow \\begin{{cases}} b = {-2*x_v}a \\\\ ({-2*x_v}a)^2 - 4a({c_val}) = {-4*y_v}a \\\\ c = {c_val} \\end{{cases}}$ \\\\ "
                           f"$\\Leftrightarrow \\begin{{cases}} b = {-2*x_v}a \\\\ {4*x_v**2}a^2 + {4*(y_v - c_val)}a = 0 \\\\ c = {c_val} \\end{{cases}} "
                           f"\\Leftrightarrow \\begin{{cases}} a = {latex(a_frac)} \\\\ b = {latex(b_frac)} \\\\ c = {c_val} \\end{{cases}}$ (do $a \\neq 0$). \\\\ "
                           f"Vậy $(P): y = {latex(f_x)}$.")

            # Xuất câu trắc nghiệm đúng cấu trúc
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


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


def bt_dang33_p4_b1_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến sympy
            x = symbols('x')

            # B1: Khởi tạo các giá trị random
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':

                n = randint(1, 3)
                m = randint(1, 4)

                a = 4 * n
                b = 3 * m
                f1 = n + m # Điều này dẫn tới C = 0
                x0 = 2


                C = f1 - (n + m) # Ở đây C = 0


                fx0 = n * (x0**3) + m * (x0**2)
                f_prime_x0 = 3 * n * (x0**2) + 2 * m * x0

                # Phương trình tiếp tuyến: y = f'(x0)*x - f'(x0)*x0 + f(x0)
                # y = Ax + B
                A = f_prime_x0
                B = fx0 - f_prime_x0 * x0

                # Đáp án đúng
                # Chuyển B sang dạng chuỗi có dấu phù hợp
                dau_B = "+" if B >= 0 else ""
                ten_pttt = f"y = {A}x {dau_B}{B}" if B != 0 else f"y = {A}x"
                da_dung = f"${ten_pttt}$"

                # Tạo các đáp án nhiễu (B4: Không trùng đáp án đúng)
                s = [
                    f"$y = {A}x {'' if -(B+2) < 0 else '+'}{-(B+2)}$",
                    f"$y = {A+2}x {dau_B}{B}$",
                    f"$y = {A}x {'' if B-5 < 0 else '+'}{B-5}$",
                    f"$y = {f_prime_x0 - 4}x {'' if fx0 < 0 else '+'}{fx0}$",
                    f"$y = {A}x {'' if B+10 < 0 else '+'}{B+10}$"
                ]

                # Lọc bỏ nếu lỡ trùng da_dung
                s = [item for item in s if item != da_dung]
                random.shuffle(s)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Nội dung câu hỏi
                noidungcauhoi = (f"Cho hàm số $y = f(x)$ có đạo hàm liên tục trên $(0;+\\infty)$ thỏa mãn "
                                 f"$f'(x) + \\frac{{f(x)}}{{x}} = {a}x^2 + {b}x$ và $f(1) = {f1}$. "
                                 f"Viết phương trình tiếp tuyến của đồ thị hàm số $y = f(x)$ tại điểm có hoành độ $x = {x0}$.")

                # Nội dung lời giải
                loigiai = (f"Ta có: $f'(x) + \\frac{{f(x)}}{{x}} = {a}x^2 + {b}x \\Leftrightarrow xf'(x) + f(x) = {a}x^3 + {b}x^2$. \\\\\n"
                           f"Lấy nguyên hàm hai vế ta được: $xf(x) = \\int ({a}x^3 + {b}x^2) \\text{{d}}x = {n}x^4 + {m}x^3 + C$. \\\\\n"
                           f"Với $x = 1$ ta có: $f(1) = {n} + {m} + C = {n+m} + C$. \\\\\n"
                           f"Theo bài ra $f(1) = {f1} \\Rightarrow {n+m} + C = {f1} \\Leftrightarrow C = {C}$. \\\\\n"
                           f"Vậy $xf(x) = {n}x^4 + {m}x^3 \\Leftrightarrow f(x) = {n}x^3 + {m}x^2$. \\\\\n"
                           f"Ta có: $f'(x) = {3*n}x^2 + {2*m}x$. \\\\\n"
                           f"Tại $x = {x0}$: $f'({x0}) = {f_prime_x0}; f({x0}) = {fx0}$. \\\\\n"
                           f"Phương trình tiếp tuyến tại điểm có hoành độ $x = {x0}$ là: \\\\\n"
                           f"$y = {f_prime_x0}(x - {x0}) + {fx0} \\Leftrightarrow $ {da_dung}.")

                # Các đáp án
                da_d = '\\True ' + da_dung
                list_1 = [da_d, das1, das2, das3]
                random.shuffle(list_1)

            # Xuất kết quả
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content 


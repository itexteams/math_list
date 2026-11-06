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


def bt_dang12_p4_b3_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            x = symbols('x')
            a, b, c = symbols('a b c')

            # B1: Nghiên cứu đề bài và B3: Suy nghĩ cách random
            # Hàm số có dạng: f(x) = ax^5 + bx^3 - 2cx^2 + 3x - 2
            # Điều kiện: f(x1) = v1; f'(x2) = v2; f''(x3) = v3

            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random các giá trị để bài toán phong phú
                # f(x1) = v1
                x1 = 1
                v1 = random.randint(3, 8) # Nguyên bản là 5

                # f'(x2) = v2
                x2 = -1
                v2 = 0 # Thường để bằng 0 cho đẹp

                # f''(x3) = v3
                x3 = Rational(1, 2)
                v3 = random.randint(4, 7) # Nguyên bản là 5

                # Định nghĩa hàm số và đạo hàm
                f = a*x**5 + b*x**3 - 2*c*x**2 + 3*x - 2
                f_prime = f.diff(x)
                f_double_prime = f_prime.diff(x)

                # Thiết lập hệ phương trình
                eq1 = f.subs(x, x1) - v1
                eq2 = f_prime.subs(x, x2) - v2
                eq3 = f_double_prime.subs(x, x3) - v3

                # Giải hệ phương trình tìm a, b, c
                sol = solve((eq1, eq2, eq3), (a, b, c))

                res_a = sol[a]
                res_b = sol[b]
                res_c = sol[c]

                # Hàm số kết quả
                f_final = f.subs({a: res_a, b: res_b, c: res_c})

                # Hàm xử lý hiển thị dấu +- thành -
                def format_latex(expr):
                    return latex(expr).replace('+ -', '- ').replace('- -', '+ ')

                # Nội dung câu hỏi
                noidungcauhoi = (r"Xác định hàm số $f(x) = ax^5 + bx^3 - 2cx^2 + 3x - 2$ ($a \neq 0$). "
                                 r"Biết $f(%s) = %s$; $f'(%s) = %s$; $f''\left(%s\right) = %s$." 
                                 % (latex(x1), latex(v1), latex(x2), latex(v2), latex(x3), latex(v3)))

                # Đáp án đúng
                da = "$f(x) = %s$" % format_latex(f_final)
                da_d = "\\True " + da

                # Tạo các đáp án nhiễu (random sai số)
                f_s1 = f.subs({a: res_a + 1, b: res_b - 1, c: res_c})
                f_s2 = f.subs({a: res_a, b: res_b + 2, c: res_c - 1})
                f_s3 = f.subs({a: res_a - 1, b: res_b, c: res_c + 1})

                da_s1 = "$f(x) = %s$" % format_latex(f_s1)
                da_s2 = "$f(x) = %s$" % format_latex(f_s2)
                da_s3 = "$f(x) = %s$" % format_latex(f_s3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Lời giải chi tiết
                loigiai = (r"Ta có: $f'(x) = %s$, $f''(x) = %s$.\\"
                           r"Từ giả thiết $f(%s)=%s; f'(%s)=%s; f''\left(%s\right)=%s$ ta có hệ PT:\\"
                           r"$\begin{cases} %s \\ %s \\ %s \end{cases} \Leftrightarrow \begin{cases} a = %s \\ b = %s \\ c = %s \end{cases}$\\"
                           r"Vậy $f(x) = %s$."
                           %(latex(f_prime), latex(f_double_prime), 
                             latex(x1), latex(v1), latex(x2), latex(v2), latex(x3), latex(v3),
                             format_latex(eq1 + v1), format_latex(eq2 + v2), format_latex(eq3 + v3),
                             latex(res_a), latex(res_b), latex(res_c),
                             format_latex(f_final)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


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


def bt_dang27_p4_b1_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến SymPy
            x = symbols('x')


            n = random.randint(1, 3) # Số mũ của x
            k = random.randint(2, 6) # Hệ số của vế phải
            val_x1 = 1
            val_f1 = Rational(random.randint(1, 5), 2) # Giá trị f(1) ngẫu nhiên (dạng phân số)
            val_target = random.choice([4, 9, 16]) # Điểm cần tính f(x), chọn số chính phương để đẹp

            # Bước 2: Giải toán bằng SymPy để lấy kết quả chính xác
            # Chia 2 vế cho 2*sqrt(x) ta được: (sqrt(x)*f(x))' = (k * x^n * sqrt(x)) / (2*sqrt(x)) = (k/2) * x^n
            f_prime_integrated = (Rational(k, 2)) * x**n
            integral_result = integrate(f_prime_integrated, x) # Kết quả là (k/(2*(n+1))) * x^(n+1)

            # Tìm hằng số C: sqrt(1)*f(1) = integral_result(1) + C
            c_val = val_f1 - integral_result.subs(x, val_x1)

            # Hàm f(x) = (integral_result + c_val) / sqrt(x)
            f_x_expr = (integral_result + c_val) / sqrt(x)
            final_result = f_x_expr.subs(x, val_target)

            # Bước 3: Tạo các phương án trắc nghiệm
            kq_dung = final_result
            da_d = '$%s$' % latex(kq_dung)

            # Tạo danh sách đáp án nhiễu (không trùng đáp án đúng)
            s = []
            while len(s) < 3:
                sai_val = kq_dung + random.choice([-2, -1, 1, 2, Rational(1,2), Rational(3,2)])
                label_sai = '$%s$' % latex(sai_val)
                if label_sai not in s and sai_val != kq_dung:
                    s.append(label_sai)

            list_1 = ['\\True ' + da_d, s[0], s[1], s[2]]
            random.shuffle(list_1)

            # Bước 4: Viết nội dung câu hỏi và lời giải (Latex)
            noidungcauhoi = (r'''Cho hàm số $y = f(x)$ liên tục trên $(0;+\infty)$ thỏa mãn $2xf'(x) + f(x) = %s x^{%s} \sqrt{x}$. Biết $f(%s) = %s$. Tính $f(%s)$.'''
                             % (latex(k), latex(n), latex(val_x1), latex(val_f1), latex(val_target)))

            loigiai = (r'''Trên khoảng $(0;+\infty)$, ta có:
            $$2xf'(x) + f(x) = %s x^{%s} \sqrt{x} \Leftrightarrow \sqrt{x}f'(x) + \frac{1}{2\sqrt{x}}f(x) = \frac{%s}{2}x^{%s}$$
            $$\Rightarrow (\sqrt{x} \cdot f(x))' = \frac{%s}{2}x^{%s} \Rightarrow \int (\sqrt{x} \cdot f(x))' \text{d}x = \int \frac{%s}{2}x^{%s} \text{d}x$$
            $$\Rightarrow \sqrt{x} \cdot f(x) = %s + C$$
            Mà $f(%s) = %s$ nên: $\sqrt{%s} \cdot f(%s) = %s + C \Rightarrow C = %s$.
            Vậy $f(x) = \frac{%s + %s}{\sqrt{x}}$.
            Suy ra $f(%s) = %s$.'''
                       % (k, n, k, n, k, n, k, n, 
                          latex(integral_result), val_x1, latex(val_f1), val_x1, val_x1, 
                          latex(integral_result.subs(x, val_x1)), latex(c_val), 
                          latex(integral_result), latex(c_val), val_target, latex(kq_dung)))

            # Xuất câu trắc nghiệm theo mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + 
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content 


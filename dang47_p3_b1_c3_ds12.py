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


def bt_dang47_p3_b1_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # --- B3: Suy nghĩ tìm cách random bài toán ---
                # f'(x) = x^n * f(x)^2. Trong hình n = 3. 
                # Ta chọn n lẻ để biểu thức x^(n+1) luôn dương, dễ kiểm soát mẫu số.
                n = random.choice([1, 3]) 

                # Chọn hằng số a để hàm số có dạng f(x) = -(n+1) / (x^(n+1) + a)
                # Điều này đảm bảo f'(x) = (n+1)^2 * x^n / (x^(n+1) + a)^2 = x^n * f(x)^2
                a = random.randint(1, 10) 

                # Điểm cho trước x0 và điểm cần tính x1
                x0 = 2
                x1 = 1

                # Tính f(x0) làm giả thiết
                tu_f0 = -(n + 1)
                mau_f0 = x0**(n + 1) + a
                f_x0 = Rational(tu_f0, mau_f0) # f(2) = y0

                # Tính đáp án đúng f(x1)
                tu_f1 = -(n + 1)
                mau_f1 = x1**(n + 1) + a
                kq_val = Rational(tu_f1, mau_f1)

                # Hằng số C trong lời giải: -1/f(x) = x^(n+1)/(n+1) + C
                # => C = -1/f(x0) - x0^(n+1)/(n+1)
                inv_f0 = Rational(mau_f0, -tu_f0)
                term_x0 = Rational(x0**(n+1), n+1)
                C_val = inv_f0 - term_x0

                # --- B4: Điều chỉnh phương án sai ---
                da = '$%s$' % latex(kq_val)

                s = []
                candidates = [
                    Rational(-tu_f1, mau_f1),          # Đổi dấu
                    Rational(tu_f1, x1**(n+1) + a + 1), # Sai mẫu số
                    Rational(1, 2), Rational(-1, 2),
                    Rational(1, 1), Rational(-2, 1),
                    Rational(0, 1), Rational(n+1, a)
                ]

                for cand in candidates:
                    cand_latex = '$%s$' % latex(cand)
                    if cand_latex != da and cand_latex not in s:
                        s.append(cand_latex)

                random.shuffle(s)
                das1, das2, das3 = s[:3]

                # --- Nội dung câu hỏi ---
                noidungcauhoi = (r'''Cho hàm số $y = f(x)$ thỏa mãn $f(%s) = %s$ và $f'(x) = x^{%s} f^2(x)$ $\forall x \in \mathbb{R}$. Giá trị của $f(%s)$ bằng bao nhiêu?'''
                                 % (latex(x0), latex(f_x0), latex(n), latex(x1)))

                # --- Nội dung lời giải ---
                # Các bước trung gian cho lời giải
                expr_int = r'\frac{x^{%s}}{%s}' % (latex(n+1), latex(n+1))

                loigiai = (r'''Ta có $f'(x) = x^{%s} f^2(x) \Leftrightarrow \frac{f'(x)}{f^2(x)} = x^{%s} \Rightarrow \int \frac{f'(x)}{f^2(x)} dx = \int x^{%s} dx \Leftrightarrow -\frac{1}{f(x)} = %s + C$. \\
                          Mà $f(%s) = %s \Rightarrow %s = \frac{%s}{%s} + C \Rightarrow C = %s$. \\
                          Suy ra $f(x) = -\frac{1}{%s + %s} = -\frac{%s}{x^{%s} + %s}$. \\
                          Vậy $f(%s) = %s$.'''
                          % (latex(n), latex(n), latex(n), expr_int,
                             latex(x0), latex(f_x0), latex(-1/f_x0), latex(x0**(n+1)), latex(n+1), latex(C_val),
                             expr_int, latex(C_val), latex(n+1), latex(n+1), latex((n+1)*C_val),
                             latex(x1), latex(kq_val)
                          ))
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq_val)) 

                # --- Xuất câu trắc nghiệm ---
                da_d = '\\True ' + str(da)
                list_1 = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)

                content = ('\\begin{minipage}{\\textwidth} \n'
                    '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                    '\\loigiai{'+str(loigiai)+'}\n'
                    '\\end{ex}\n \\end{minipage} \n\n')
            return content  


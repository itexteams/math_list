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


def bt_dang13_p4_b1_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            x = symbols('x')

            # Bước 1 & 3: Nghiên cứu và thiết lập thông số ngẫu nhiên
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random các hệ số a, b trong biểu thức (a - bx)/x^2
                # Để bài toán đẹp, ta thường chọn x_0 = 1
                a = randint(1, 5)
                b = randint(1, 5)
                x0 = 1
                y0 = randint(1, 10)

                # Biểu thức đạo hàm f'(x) = (a - b*x) / x^2
                f_prime = (a - b*x) / (x**2)

                # Tính nguyên hàm f(x) = \int f'(x) dx = -a/x - b*ln(x) + C
                # Sympy tính nguyên hàm:
                f_integ = integrate(f_prime, x) 
                # f_integ lúc này là -a/x - b*log(x)

                # Tính hằng số C: f(x0) = y0 => y0 = (-a/x0 - b*ln(x0)) + C
                # Với x0 = 1, ln(1) = 0 => y0 = -a + C => C = y0 + a
                C_val = y0 + a

                # Hàm số đúng
                f_final = f_integ + C_val

                # Đáp án đúng (LaTeX)
                da_dung = '$f(x) = %s$' % latex(f_final).replace('log', 'ln')

                # Bước 4: Tạo các phương án sai (không trùng đáp án đúng)
                s = set()
                while len(s) < 3:
                    # Sai dấu của phần phân thức
                    sai1 = latex(-f_integ + C_val).replace('log', 'ln')
                    # Sai dấu của phần log
                    sai2 = latex(integrate((a + b*x)/(x**2), x) + C_val).replace('log', 'ln')
                    # Sai hằng số C
                    sai3 = latex(f_integ + C_val - randint(1, 3)).replace('log', 'ln')
                    # Sai biểu thức hoàn toàn
                    sai4 = latex(f_integ + y0).replace('log', 'ln')

                    candidates = [
                        '$f(x) = %s$' % sai1,
                        '$f(x) = %s$' % sai2,
                        '$f(x) = %s$' % sai3,
                        '$f(x) = %s$' % sai4
                    ]

                    for cand in candidates:
                        if cand != da_dung:
                            s.add(cand)

                list_sai = list(s)
                das1, das2, das3 = list_sai[0], list_sai[1], list_sai[2]

                # Câu hỏi
                noidungcauhoi = (r'''Biết rằng đồ thị của hàm số $y = f(x)$ đi qua điểm $(%s;%s)$ và có hệ số góc của tiếp tuyến tại mỗi điểm $(x;f(x))$ là $\frac{%s - %sx}{x^2}$ với $x > 0$. Tìm hàm số $f(x)$.'''
                                 % (latex(x0), latex(y0), latex(a), latex(b)))

                # Nội dung lời giải
                loigiai = (r'''Theo giả thiết, ta có $f'(x) = \frac{%s - %sx}{x^2}$ với $x > 0$ và $f(%s) = %s$. \\
                           $f(x) = \int f'(x) \text{d}x = \int \frac{%s - %sx}{x^2} \text{d}x = \int \left( %sx^{-2} - \frac{%s}{x} \right) \text{d}x = -\frac{%s}{x} - %s\ln x + C$. \\
                           $f(%s) = %s \Rightarrow -\frac{%s}{%s} - %s\ln %s + C = %s \Rightarrow %s + C = %s \Rightarrow C = %s$. \\
                           Vậy $f(x) = %s$.'''
                           % (latex(a), latex(b), latex(x0), latex(y0),
                              latex(a), latex(b), latex(a), latex(b), latex(a), latex(b),
                              latex(x0), latex(y0), latex(a), latex(x0), latex(b), latex(x0), latex(y0),
                              latex(-a), latex(y0), latex(C_val),
                              latex(f_final).replace('log', 'ln')
                              ))

                # Trộn đáp án
                da_d = '\\True ' + da_dung
                list_ans = [da_d, das1, das2, das3]
                random.shuffle(list_ans)

            # Xuất nội dung theo mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content 


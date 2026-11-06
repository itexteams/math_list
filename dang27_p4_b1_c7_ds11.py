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


def bt_dang27_p4_b1_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến và chọn dạng
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Suy nghĩ tìm cách random bài toán
                # Để nghiệm x0 đẹp, ta chọn x1, x2 trước rồi suy ngược ra hệ số b và k
                # Xét hàm y = x^3 + bx^2 + c. Đạo hàm y' = 3x^2 + 2bx
                # Ta muốn y'(x) = k có 2 nghiệm x1, x2 phân biệt

                a = 1 # Giữ a=1 cho giống mẫu
                x1 = randint(-3, 4)
                x2 = Rational(randint(-2, 5), randint(1, 4))
                while x1 == x2: # Đảm bảo 2 tiếp điểm khác nhau
                    x2 = Rational(randint(-2, 5), randint(1, 4))

                # Từ phương trình 3x^2 + 2bx - k = 3(x-x1)(x-x2) = 3x^2 - 3(x1+x2)x + 3*x1*x2
                # => 2b = -3(x1+x2) => b = -3(x1+x2)/2
                # => -k = 3*x1*x2 => k = -3*x1*x2

                b_val = Rational(-3 * (x1 + x2), 2)
                k_val = -3 * x1 * x2
                c_val = randint(-5, 5)
                n_val = randint(-10, 10) # Hệ số tự do của đường thẳng d1

                # Hàm số và đạo hàm
                f = x**3 + b_val*x**2 + c_val
                f_prime = diff(f, x)

                # Đường thẳng d1: y - kx - n = 0 => y = kx + n. 
                # Nhưng mẫu là y + 3x - 1 = 0 => y = -3x + 1. Vậy k_tieptuyen = -3.
                # Để giống mẫu d1: y + mx + n = 0 => k = -m
                m_val = -k_val

                # Tọa độ tiếp điểm và phương trình tiếp tuyến
                y1 = f.subs(x, x1)
                y2 = f.subs(x, x2)

                # PTTT: y = k(x - x0) + y0
                pttt1 = expand(k_val * (x - x1) + y1)
                pttt2 = expand(k_val * (x - x2) + y2)

                # Nội dung câu hỏi
                # Chú ý xử lý dấu cho đường thẳng d1: y + mx + n = 0
                # Nếu m_val > 0 hiển thị + m_val, nếu < 0 hiển thị - |m_val|
                d1_str = "y"
                if m_val > 0: d1_str += " + " + latex(m_val) + "x"
                elif m_val < 0: d1_str += " - " + latex(abs(m_val)) + "x"

                if n_val > 0: d1_str += " + " + latex(n_val)
                elif n_val < 0: d1_str += " - " + latex(abs(n_val))
                d1_str += " = 0"

                noidungcauhoi = (r'Cho hàm số $y = %s$ $(C)$. Viết phương trình tiếp tuyến của hàm số song song với đường thẳng $(d_1): %s$'
                                 % (latex(f), d1_str))

                # Đáp án đúng
                da_dung = r'$y = %s$ và $y = %s$' % (latex(pttt1), latex(pttt2))

                # Tạo đáp án nhiễu
                du = [da_dung]
                s = [
                    r'$y = %s$ và $y = %s$' % (latex(expand(pttt1 + 2)), latex(pttt2)),
                    r'$y = %s$ và $y = %s$' % (latex(pttt1), latex(expand(pttt2 - 5))),
                    r'$y = %s$ và $y = %s$' % (latex(expand(k_val*x + 5)), latex(expand(k_val*x - 2))),
                    r'$y = %s$' % (latex(pttt1)),
                    r'$y = %s$ và $y = %s$' % (latex(expand(-k_val*(x-x1)+y1)), latex(pttt2))
                ]

                random.shuffle(s)
                das1, das2, das3 = s[0], s[1], s[2]

                # Các đáp án trắc nghiệm
                da_d = '\\True ' + str(da_dung)
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (B2 - Viết lại y hệt bài toán mẫu)
                loigiai = (r'''$y' = %s$ \\
                           Tiếp tuyến song song đường thẳng $(d_1): %s$ nên hệ số góc tiếp tuyến $k = %s$ \\
                           Gọi $M(x_0;y_0)$ là điểm tiếp xúc của tiếp tuyến với đồ thị $(C)$ khi đó ta có: \\
                           $y'(x_0) = k = %s \Leftrightarrow %s = %s \Leftrightarrow \left[\begin{aligned} & x_0 = %s \\ & x_0 = %s \end{aligned}\right.$ \\
                           * $x_0 = %s \Rightarrow y_0 = %s \Rightarrow PTTT: y = %s(x - %s) %s \Rightarrow y = %s$ \\
                           * $x_0 = %s \Rightarrow y_0 = %s \Rightarrow PTTT: y = %s\left(x - %s\right) %s \Rightarrow y = %s$'''
                           % (latex(f_prime), d1_str, latex(k_val),
                              latex(k_val), latex(f_prime.subs(x, symbols('x_0'))), latex(k_val), latex(x1), latex(x2),
                              latex(x1), latex(y1), latex(k_val), latex(x1), ("+ " + latex(y1) if y1 >= 0 else latex(y1)), latex(pttt1),
                              latex(x2), latex(y2), latex(k_val), latex(x2), ("+ " + latex(y2) if y2 >= 0 else latex(y2)), latex(pttt2)
                             ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


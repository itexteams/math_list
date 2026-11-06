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


def bt_dang14_p4_b3_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            x = symbols('x')

            # Danh sách dạng bài (ở đây tập trung vào hàm số y = x*sqrt(x^2 + k))
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random hằng số k trong căn (x^2 + k)
                # Để giống đề bài gốc (x^2 + 1), ta có thể chọn k ngẫu nhiên từ 1 đến 9
                k = random.randint(1, 9)

                # Biểu thức hàm số
                y = x * sqrt(x**2 + k)

                # Tính đạo hàm cấp 1 (để trình bày lời giải)
                y_prime = simplify(diff(y, x))
                # Tính đạo hàm cấp 2 (đáp án đúng)
                y_double_prime = simplify(diff(y_prime, x))

                # Đáp án đúng
                kq = latex(y_double_prime).replace('.', ',')
                da = '$%s$' % (kq)

                # Tạo các phương án sai (nhiễu)
                # Nhiễu 1: Đạo hàm cấp 1
                s1 = '$%s$' % (latex(y_prime).replace('.', ','))

                # Nhiễu 2: Sai hệ số tử số
                sai_tu_2 = (x * (x**2 + 3*k)) / ((x**2 + k)**(sp.Rational(3, 2)))
                s2 = '$%s$' % (latex(simplify(sai_tu_2)).replace('.', ','))

                # Nhiễu 3: Sai mẫu số (mất căn hoặc sai bậc)
                s3 = '$\\frac{%s}{%s}$' % (latex(2*x**3 + 3*k*x), latex(x**2 + k))

                # Nhiễu 4: Đạo hàm sai quy tắc tích
                s4 = '$\\frac{%s}{\\sqrt{x^2+%s}}$' % (latex(x**2 + k), latex(k))

                du = [da]
                da_d_text = random.choice(du)

                # Trộn các phương án sai
                s = [s1, s2, s3, s4]
                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Kiểm tra tránh trùng lặp đáp án đúng (dù xác suất rất thấp với hàm này)
                while das1 == da_d_text or das2 == da_d_text or das3 == da_d_text:
                    k_new = random.randint(1, 9)
                    # Thực hiện lại logic nếu cần, nhưng với hàm này các biểu thức nhiễu cấu trúc khác hẳn
                    break

                # Câu hỏi
                noidungcauhoi = ('Tính đạo hàm cấp hai của hàm số $y = %s$.'
                                 % (latex(y)))

                # Các đáp án
                da_d = ('\\True ' + str(da_d_text))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                # Bước 1: Tính y'
                buoc1 = 'y\' = (x)\' \\cdot \\sqrt{x^2 + %s} + x \\cdot (\\sqrt{x^2 + %s})\'' % (k, k)
                buoc2 = 'y\' = \\sqrt{x^2 + %s} + x \\cdot \\frac{x}{\\sqrt{x^2 + %s}} = \\frac{x^2 + %s + x^2}{\\sqrt{x^2 + %s}} = \\frac{2x^2 + %s}{\\sqrt{x^2 + %s}}' % (k, k, k, k, k, k)

                # Bước 2: Tính y''
                buoc3 = 'y\'\' = \\left( \\frac{2x^2 + %s}{\\sqrt{x^2 + %s}} \\right)\' = \\frac{(4x)\\sqrt{x^2 + %s} - (2x^2 + %s)\\frac{x}{\\sqrt{x^2 + %s}}}{x^2 + %s}' % (k, k, k, k, k, k)
                buoc4 = 'y\'\' = \\frac{4x(x^2 + %s) - x(2x^2 + %s)}{(x^2 + %s)\\sqrt{x^2 + %s}} = \\frac{4x^3 + %sx - 2x^3 - %sx}{\\sqrt{(x^2 + %s)^3}}' % (k, k, k, k, 4*k, k, k)

                loigiai = ('''Ta có: \\\\
                             $%s$ \\\\
                             $%s$ \\\\
                             Đạo hàm cấp 2 là: \\\\
                             $%s$ \\\\
                             $%s$ \\\\
                             $\\Rightarrow y\'\' = %s$.'''
                           % (buoc1, buoc2, buoc3, buoc4, latex(y_double_prime).replace('.', ',')))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content


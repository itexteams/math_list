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


def bt_dang9_p3_b2_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Random bài toán
                # H(x) = sqrt(a*x^2 + b)
                a = randint(2, 8)
                b = randint(20, 100)
                # x(t) = c*t + d
                c = randint(10, 30)
                d = randint(20, 60)
                # Thời điểm t0
                t0 = randint(3, 10)

                # Tính toán các giá trị trung gian
                x0 = c * t0 + d
                # H'(x) = (a*x) / sqrt(a*x^2 + b)
                # Dao ham tai x0: h_prime_x0 = (a * x0) / sqrt(a * x0**2 + b)
                # Toc do tang: v = h_prime_x0 * c
                val_inner = a * (x0**2) + b
                res_float = (a * x0 * c) / math.sqrt(val_inner)

                # Làm tròn đến hàng phần chục
                kq_decimal = Decimal(str(res_float)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq_str = str(kq_decimal).replace('.', ',')

                # Đáp án đúng
                da = '$%s$' % (kq_str)

                # Bước 4: Tạo các phương án sai (không trùng đáp án đúng)
                s = []
                offsets = [-5.2, -3.5, 2.8, 4.1, 7.3, -8.4]
                random.shuffle(offsets)

                for offset in offsets:
                    wrong_val = Decimal(str(res_float + offset)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                    wrong_str = '$%s$' % (str(wrong_val).replace('.', ','))
                    if wrong_str != da and wrong_str not in s:
                        s.append(wrong_str)
                    if len(s) == 3:
                        break

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Một công ty xác định rằng tổng chi phí của họ (tính theo nghìn đô-la), để sản xuất $%s$ mặt hàng là $H\\left(x\\right) = \\sqrt{%s x^2 + %s}$ và công ty lên kế hoạch nâng sản lượng trong $t$ tháng kể từ nay theo hàm số $x\\left(t\\right) = %s t + %s$. Chi phí sẽ tăng với tốc độ bao nhiêu nghìn đô-la/tháng sau $%s$ tháng kể từ khi công ty thực hiện kế hoạch đó? (làm tròn đến hàng phần chục).'''
                                 % (latex(x), latex(a), latex(b), latex(c), latex(d), latex(t0)))

                # Nội dung lời giải
                # Đạo hàm H'(x)
                h_prime_expr = '\\frac{%s x}{\\sqrt{%s x^2 + %s}}' % (latex(a), latex(a), latex(b))

                loigiai = ('''Ta có: $H'\\left(x\\right) = %s$; $x'\\left(t\\right) = %s$; $x\\left(%s\\right) = %s \\cdot %s + %s = %s$.\\\\
                             Mà $H'\\left(x\\left(t\\right)\\right) = H'\\left(x\\right) \\cdot x'\\left(t\\right)$ hay $H'\\left(x\\left(%s\\right)\\right) = H'\\left(%s\\right) \\cdot x'\\left(%s\\right)$.\\\\
                             Do đó $H'\\left(x\\left(%s\\right)\\right) = \\frac{%s \\cdot %s}{\\sqrt{%s \\cdot %s^2 + %s}} \\cdot %s \\approx %s$ nghìn đô-la/tháng.'''
                           % (h_prime_expr, latex(c), latex(t0), latex(c), latex(t0), latex(d), latex(x0),
                              latex(t0), latex(x0), latex(t0),
                              latex(t0), latex(a), latex(x0), latex(a), latex(x0), latex(b), latex(c), kq_str))
                dapan='\\shortans[0]{$%s$}\n'%(kq_str)
                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) +dapan+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content  


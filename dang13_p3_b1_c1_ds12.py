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


def bt_dang13_p3_b1_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Tạo ngẫu nhiên 2 nghiệm x1, x2 là số nguyên
                # Để b0 = -3*a0*(x1+x2)/2 là số nguyên thì (x1+x2) phải chia hết cho 2 (cùng chẵn hoặc cùng lẻ)
                par = random.choice(['chan', 'le'])
                if par == 'chan':
                    x1 = random.choice([-2, 0, 2])
                    x2 = x1 + random.choice([2, 4])
                else:
                    x1 = random.choice([-3, -1, 1])
                    x2 = x1 + random.choice([2, 4])

                a0 = random.choice([1, -1])
                b0 = -3 * a0 * (x1 + x2) // 2
                c0 = 3 * a0 * x1 * x2
                d0 = randint(-5, 8)

                # Tính tọa độ cực trị
                y1 = a0 * (x1**3) + b0 * (x1**2) + c0 * x1 + d0
                y2 = a0 * (x2**3) + b0 * (x2**2) + c0 * x2 + d0

                # Tính độ dài AB
                ab_squared = (x2 - x1)**2 + (y2 - y1)**2
                ab_val = math.sqrt(ab_squared)

                # Làm tròn đến hàng phần mười bằng Decimal để tránh lỗi chính xác của float
                kq_dec = Decimal(str(ab_val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq = str(kq_dec).replace('.', ',')

                # Tạo các phương án nhiễu (làm tròn 1 chữ số thập phân) không trùng với đáp án đúng
                kq_float = float(kq_dec)
                s_candidates = [
                    round(kq_float + 1.2, 1),
                    round(kq_float + 2.5, 1),
                    round(kq_float - 1.5, 1) if kq_float > 2 else round(kq_float + 3.1, 1),
                    round(kq_float - 2.1, 1) if kq_float > 3 else round(kq_float + 4.3, 1),
                    round(math.sqrt(ab_squared + 5), 1),
                    round(math.sqrt(abs(ab_squared - 8)), 1)
                ]

                s = []
                for val in s_candidates:
                    val_str = str(val).replace('.', ',')
                    s.append('$%s$' % (val_str))

                s = [item for item in s if item != '$%s$' % (kq)]
                s = list(set(s))

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Định dạng hiển thị hàm số bậc ba cho đẹp mắt
                sign_b = '+' if b0 > 0 else ''
                sign_c = '+' if c0 > 0 else ''
                sign_d = '+' if d0 > 0 else ''

                term_a = 'x^3' if a0 == 1 else '-x^3'
                term_b = '%s%s x^2' % (sign_b, b0) if b0 != 0 else ''
                term_c = '%s%s x' % (sign_c, c0) if c0 != 0 else ''
                term_d = '%s%s' % (sign_d, d0) if d0 != 0 else ''

                ham_so_latex = '%s %s %s %s' % (term_a, term_b, term_c, term_d)
                # Loại bỏ khoảng trắng thừa
                ham_so_latex = ' '.join(ham_so_latex.split())

                # Câu hỏi
                noidungcauhoi = ('''Cho hàm số $y = %s$ có đồ thị $(C)$. Độ dài đoạn thẳng nối hai điểm cực trị của đồ thị $(C)$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục).'''
                                 % (ham_so_latex))

                # Các đáp án
                da_d = ('\\True $%s$' % (kq))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Lời giải chi tiết từng bước
                der_a = 3 * a0
                der_b = 2 * b0
                der_c = c0

                sign_der_b = '+' if der_b > 0 else ''
                sign_der_c = '+' if der_c > 0 else ''
                term_der_b = '%s%s x' % (sign_der_b, der_b) if der_b != 0 else ''
                term_der_c = '%s%s' % (sign_der_c, der_c) if der_c != 0 else ''

                dao_ham_latex = '%s x^2 %s %s' % (der_a, term_der_b, term_der_c)
                dao_ham_latex = ' '.join(dao_ham_latex.split())

                loigiai = ('''Tập xác định của hàm số là $D = \\mathbb{R}$.\\\\
                           Ta có đạo hàm của hàm số là:\\\\
                           $y\' = %s$.\\\\
                           Cho $y\' = 0 \\Leftrightarrow \\left[\\begin{aligned} & x = %s \\\\ & x = %s \\end{aligned}\\right.$.\\\\
                           Với $x = %s \\Rightarrow y = %s$, ta được điểm cực trị thứ nhất là $A(%s; %s)$.\\\\
                           Với $x = %s \\Rightarrow y = %s$, ta được điểm cực trị thứ hai là $B(%s; %s)$.\\\\
                           Độ dài đoạn thẳng nối hai điểm cực trị $A$ và $B$ là:\\\\
                           $AB = \\sqrt{(x_B - x_A)^2 + (y_B - y_A)^2} = \\sqrt{(%s - %s)^2 + (%s - %s)^2} = \\sqrt{%s} \\approx %s$.\\\\
                           Vậy độ dài đoạn thẳng nối hai điểm cực trị của đồ thị $(C)$ xấp xỉ $%s$.'''
                           % (dao_ham_latex, latex(x1), latex(x2),
                              latex(x1), latex(y1), latex(x1), latex(y1),
                              latex(x2), latex(y2), latex(x2), latex(y2),
                              latex(x2), latex(x1), latex(y2), latex(y1), latex(ab_squared), latex(kq), latex(kq)))
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content  


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


def bt_dang17_p3_b1_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':


                # Để đảm bảo gcd(m, n) = 1, ta chọn m và n trước
                n = random.randint(2, 6) # n là số nguyên dương
                m = random.choice([i for i in range(-7, 4) if i != 0 and i != n])

                # Đảm bảo phân số m/n tối giản
                common = math.gcd(abs(m), n)
                m = m // common
                n = n // common

                # Tính hệ số a = 1 / (m/n) = n/m
                a_rat = Rational(n, m)

                # Tính m1 và n1 cho đề bài gốc: m/n = 1 - m1/n1 => m1/n1 = 1 - m/n = (n-m)/n
                # Vậy m1 = n - m, n1 = n
                m1 = n - m
                n1 = n

                # Tính giá trị biểu thức S = a + m + n
                val_S = float(a_rat) + m + n

                # Làm tròn đến hàng phần mười (0.1)
                kq_decimal = Decimal(str(val_S)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq_str = str(kq_decimal).replace('.', ',')

                # Đáp án đúng
                da = '$%s$' % kq_str

                # Bước 4: Điều chỉnh các phương án sai không trùng với đáp án đúng
                s = set()
                while len(s) < 3:
                    sai_offset = random.choice([-2, -1.5, -1, 1, 1.5, 2, 2.5])
                    sai_val = float(kq_decimal) + sai_offset
                    sai_str = str(Decimal(str(sai_val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')
                    if sai_str != kq_str:
                        s.add('$%s$' % sai_str)

                list_sai = list(s)
                das1, das2, das3 = list_sai[0], list_sai[1], list_sai[2]

                # Câu hỏi (B2: Viết lại y hệt bài toán theo mẫu)
                noidungcauhoi = (r'''Giả sử $\int \frac{1}{\sqrt[%s]{x^{%s}}} \text{d}x = ax^{\frac{m}{n}} + C$ với $a$ là hằng số thực, $n$ là số nguyên dương, $m$ là số nguyên và ước số chung lớn nhất của $m$ và $n$ bằng $1$. Giá trị của biểu thức $S = a + m + n$ là bao nhiêu? (làm tròn kết quả đến hàng phần chục).'''
                                 % (latex(n1), latex(m1)))

                # Nội dung lời giải
                # Biến đổi Latex cho phần phân số âm
                exponent_step = Rational(-m1, n1)
                new_exponent = exponent_step + 1

                loigiai = (r'''$\int \frac{1}{\sqrt[%s]{x^{%s}}} \text{d}x = \int \frac{1}{x^{\frac{%s}{%s}}} \text{d}x = \int x^{%s} \text{d}x = \frac{x^{%s+1}}{%s+1} + C = \frac{%s}{%s} x^{\frac{%s}{%s}} + C$. \\
                             Dựa vào dạng bài cho, ta có: \\
                             $a = \frac{%s}{%s}$, $m = %s$, $n = %s$. \\
                             Khi đó $S = a + m + n = \frac{%s}{%s} + (%s) + %s \approx %s$.'''
                           % (latex(n1), latex(m1), latex(m1), latex(n1), latex(exponent_step), 
                              latex(exponent_step), latex(exponent_step), latex(n), latex(m), latex(m), latex(n),
                              latex(n), latex(m), latex(m), latex(n),
                              latex(n), latex(m), latex(m), latex(n), kq_str))
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq_str))

                # Đưa các đáp án vào danh sách
                da_d = '\\True ' + str(da)
                list_ans = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_ans)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content  


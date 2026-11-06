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


def bt_dang49_p3_b3_c5_ds10(self):
            while True:
                # Random các thông số cho biểu thức x(ax + b)^n + (x + d)^m
                # Giới hạn a và d nhỏ để hệ số không vượt quá 9999
                a = randint(1, 3)
                b = random.choice([-2, -1, 1, 2])
                n = randint(6, 10)

                d = random.choice([-2, -1, 1, 2])
                m = randint(7, 12)

                # Phần 1: x*(ax + b)^n -> Cần tìm x^4 trong (ax+b)^n
                # h1 = C(n, 4) * a^4 * b^(n-4)
                h1 = math.comb(n, 4) * (a**4) * (b**(n-4))

                # Phần 2: (x + d)^m -> Cần tìm x^5 trong (x+d)^m
                # h2 = C(m, 5) * 1^5 * d^(m-5)
                h2 = math.comb(m, 5) * (d**(m-5))

                # Tổng hệ số
                kq_val = int(h1 + h2)

                # Kiểm tra điều kiện đề bài: -999 < kq < 9999
                if -999 < kq_val < 9999:
                    break

            # Định dạng hiển thị LaTeX
            a_tex = latex(a) if a != 1 else ""
            b_sign = "+" if b > 0 else "-"
            b_abs = abs(b)
            d_sign = "+" if d > 0 else "-"
            d_abs = abs(d)

            # Câu hỏi
            noidungcauhoi = (r'''Hệ số của số hạng chứa $x^5$ trong khai triển biểu thức $P(x) = x\left(%sx %s %s\right)^{%s} + \left(x %s %s\right)^{%s}$ bằng bao nhiêu?'''
                             %(a_tex, b_sign, latex(b_abs), latex(n), d_sign, latex(d_abs), latex(m)))

            # Đáp án đúng
            da_d = '\\True $%d$' % kq_val

            # Tạo các phương án nhiễu (số nguyên)
            s_set = set()
            while len(s_set) < 3:
                offset = random.choice([1, -1, 10, -10, 2, -2, 5, -5])
                nhieu = kq_val + offset
                if nhieu != kq_val:
                    s_set.add('$%d$' % nhieu)

            list_ans = [da_d] + list(s_set)
            random.shuffle(list_ans)

            # Nội dung lời giải
            loigiai = (r'''Xét biểu thức $P(x) = x\left(%sx %s %s\right)^{%s} + \left(x %s %s\right)^{%s}$. \\
                         + Số hạng chứa $x^5$ trong $x\left(%sx %s %s\right)^{%s}$ tương ứng với số hạng chứa $x^4$ trong khai triển $\left(%sx %s %s\right)^{%s}$. \\
                         Hệ số này là: $C_{%s}^{4} \cdot (%s)^{4} \cdot (%s)^{%s} = %s$. \\
                         + Số hạng chứa $x^5$ trong khai triển $\left(x %s %s\right)^{%s}$ là: $C_{%s}^{5} \cdot 1^{5} \cdot (%s)^{%s} = %s$. \\
                         Vậy hệ số của $x^5$ trong khai triển đã cho là: $%s + (%s) = %d$.'''
                       %(a_tex, b_sign, latex(b_abs), latex(n), d_sign, latex(d_abs), latex(m),
                         a_tex, b_sign, latex(b_abs), latex(n), a_tex, b_sign, latex(b_abs), latex(n),
                         latex(n), latex(a), latex(b), latex(n-4), latex(h1),
                         d_sign, latex(d_abs), latex(m), latex(m), latex(d), latex(m-5), latex(h2),
                         latex(h1), latex(h2), kq_val))

            # Đáp án ngắn (Ghi số nguyên vào dapan)
            dapan = '\\shortans[0]{$%d$}\n' % kq_val

            # Xuất câu trắc nghiệm và làm sạch dấu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + noidungcauhoi + dapan +
                       '\\loigiai{' + loigiai + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n').replace('+-', '-').replace('--', '+').replace('++','+').replace('1x', 'x')

            return content


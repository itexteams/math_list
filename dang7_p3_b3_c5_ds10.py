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


def bt_dang7_p3_b3_c5_ds10(self):
            while True:
                # Khai báo biến ngẫu nhiên
                a = randint(-5, 5)
                b = randint(-5, 5)
                k = randint(0, 4) # k chạy từ 0 đến 4 để có đủ các số hạng x^4 đến x^0

                if a == 0 or b == 0:
                    continue

                # Tính hệ số của x^(4-k): hs = C(4, k) * a^(4-k) * b^k
                C_val = math.comb(4, k)
                hs = C_val * (a**(4 - k)) * (b**k)

                # Kiểm tra điều kiện hệ số nằm trong khoảng (-999, 9999)
                if -999 < hs < 9999:
                    break

            # Tính các hệ số khai triển để trình bày lời giải
            A1 = a**4
            A2 = 4 * (a**3) * b
            A3 = 6 * (a**2) * (b**2)
            A4 = 4 * a * (b**3)
            A5 = b**4

            ax_latex = latex(a*x).replace('1x', 'x')

            # Câu hỏi
            noidungcauhoi = (r'Hệ số của số hạng chứa $x^{%s}$ trong khai triển $(%s %s %s)^4$ bằng bao nhiêu?' 
                             % (latex(4-k), latex(a) if a != 1 else "", "x", f"{b:+d}"))

            # Nội dung lời giải
            loigiai = (r'Ta có:\\ '
                       r'$(%s %s %s)^4 = (%s x)^4 + C_4^1(%s x)^3(%s) + C_4^2(%s x)^2(%s)^2 + C_4^3(%s x)(%s)^3 + (%s)^4$\\ '
                       r' \hspace*{1cm} $= %s x^4 %s x^3 %s x^2 %s x %s$.\\ '
                       r'Vậy hệ số của $x^{%s}$ là $%s$.'
                       % (latex(a) if a != 1 else "", "x", f"{b:+d}",
                          latex(a), latex(a), latex(b), latex(a), latex(b), latex(a), latex(b), latex(b),
                          latex(A1), f"{A2:+d}", f"{A3:+d}", f"{A4:+d}", f"{A5:+d}",
                          latex(4-k), latex(hs)))

            # Đáp án đúng (Số nguyên)
            dapan = '\\shortans[0]{$%s$}\n' % (latex(hs))

            # Tạo các phương án nhiễu trắc nghiệm (Số nguyên)
            da_d = '\\True $%s$' % (latex(hs))
            s_set = set()
            while len(s_set) < 3:
                offset = random.choice([1, -1, 2, -2, 10, -10])
                nhieu = hs + offset
                if nhieu != hs:
                    s_set.add('$%s$' % (latex(nhieu)))

            list_ans = [da_d] + list(s_set)
            random.shuffle(list_ans)

            # Xuất nội dung và dọn dẹp ký tự thừa
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + noidungcauhoi + dapan +
                       '\\loigiai{' + loigiai + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n'
                       ).replace('+-', '-').replace('-+', '-').replace('--', '+').replace('++', '+').replace('1x', 'x').replace('x^1', 'x').replace('x^0', '').replace(' 0x', '')

            return content


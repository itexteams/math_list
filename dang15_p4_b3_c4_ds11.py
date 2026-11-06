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


def bt_dang15_p4_b3_c4_ds11(self):
            # Khai báo biến
            # Chọn ngẫu nhiên một năm n (ví dụ từ 2020 đến 2026)
            n = random.randint(2025, 2030)
            # Theo logic phân tích để triệt tiêu: a = n + 2
            a = n + 2
            # Giá trị trong căn ở kết quả: a + 1 = n + 3
            res_val = n + 3

            # Các biểu thức Sympy để render Latex
            x = symbols('x')
            f_tu = x**n + x - 2
            f_mau = sqrt(a*x + 1) - sqrt(x + a)

            # Kết quả đúng k = 2 * sqrt(n+3)
            kq_dung = 2 * sqrt(res_val)

            # --- Tạo các đáp án nhiễu ---
            da_dung = '$k = %s$' % latex(kq_dung)

            # Tạo các phương án sai bằng cách thay đổi hệ số hoặc giá trị trong căn
            s1 = '$k = %s$' % latex(sqrt(res_val))
            s2 = '$k = %s$' % latex(2 * sqrt(n + 1))
            s3 = '$k = %s$' % latex(n * sqrt(res_val))
            s4 = '$k = %s$' % latex(2 * sqrt(n))

            list_options = [da_dung, s1, s2, s3, s4]
            random.shuffle(list_options)

            # Phân loại phương án cho cấu trúc \choice
            # Lưu ý: mẫu của bạn dùng \True cho đáp án đúng
            choices_str = ""
            for opt in list_options:
                if opt == da_dung:
                    choices_str += '{\\True ' + opt + '}\n'
                else:
                    choices_str += '{' + opt + '}\n'

            # --- Nội dung câu hỏi ---
            noidungcauhoi = (r'''Cho hàm số $f(x) = \begin{cases} \dfrac{x^{%d} + x - 2}{\sqrt{%dx + 1} - \sqrt{x + %d}} & \text{khi } x \neq 1 \\ k & \text{khi } x = 1 \end{cases}$. Tìm giá trị của $k$ để hàm số $f(x)$ liên tục tại $x = 1$.''' 
                             % (n, a, a))

            # --- Nội dung lời giải chi tiết ---
            # Tính toán các bước trung gian cho lời giải
            n_minus_1 = n - 1
            loigiai = (r'''Ta có: $\lim_{x \to 1} \dfrac{x^{%d} + x - 2}{\sqrt{%dx + 1} - \sqrt{x + %d}} = \lim_{x \to 1} \dfrac{(x^{%d} - 1 + x - 1)(\sqrt{%dx + 1} + \sqrt{x + %d})}{%dx - %d}$ \\
                       $= \lim_{x \to 1} \dfrac{(x-1)(x^{%d} + x^{%d} + \dots + x + 1 + 1)(\sqrt{%dx + 1} + \sqrt{x + %d})}{%d(x-1)}$ \\
                       $= \dfrac{(%d+1) \cdot 2\sqrt{%d}}{%d} = 2\sqrt{%d}$. \\
                       Để hàm số liên tục tại $x = 1 \Leftrightarrow \lim_{x \to 1} f(x) = f(1) \Leftrightarrow k = 2\sqrt{%d}$.''' 
                       % (n, a, a, n, a, a, a-1, a-1, 
                          n_minus_1, n_minus_1-1, a, a, a-1, 
                          n_minus_1, n+1, a-1, res_val, res_val))

            # --- Xuất nội dung theo mẫu ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content 


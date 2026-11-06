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


def bt_dang14_p1_b1_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            x = symbols('x')

            # B1 & B3: Thiết lập các giá trị ngẫu nhiên
            # Hàm số có dạng:
            # f(x) = ax^2 + bx khi x >= x0
            # f(x) = c*x + d   khi x < x0
            # Trong hình: x0 = 1, c = 2, d = -1

            x0 = 1
            c = random.randint(1, 5) # Hệ số góc của nhánh dưới
            d = random.randint(-5, 5) # Hệ số tự do của nhánh dưới

            # Để có đạo hàm tại x0, hàm phải liên tục tại x0:
            # a(x0^2) + b(x0) = c(x0) + d  => a + b = c + d (với x0=1)
            # Và đạo hàm trái bằng đạo hàm phải:
            # 2ax0 + b = c => 2a + b = c (với x0=1)

            # Giải hệ:
            # a + b = c + d
            # 2a + b = c
            # => a = -d, b = c + 2d

            a_val = -d
            b_val = c + 2*d
            target_value = 2*a_val + b_val # Giá trị cần tìm (2a + b)

            # Tạo các phương án nhiễu
            du = [f'${latex(target_value)}$']
            da = target_value

            s = []
            while len(s) < 3:
                noise = random.randint(target_value - 5, target_value + 5)
                if noise != target_value and noise not in s:
                    s.append(noise)

            das1 = f'${latex(s[0])}$'
            das2 = f'${latex(s[1])}$'
            das3 = f'${latex(s[2])}$'

            # Nội dung câu hỏi
            noidungcauhoi = (r"Cho hàm số $f(x) = \begin{cases} ax^2 + bx & \text{khi } x \ge %s \\ %sx %s & \text{khi } x < %s \end{cases}$. "
                             r"Để hàm số đã cho có đạo hàm tại $x = %s$ thì $2a + b$ bằng" 
                             % (latex(x0), latex(c), ("+" + str(d) if d >= 0 else str(d)), latex(x0), latex(x0)))

            # Đáp án
            da_d = r'\True ' + du[0]
            list_1 = [da_d, das1, das2, das3]
            random.shuffle(list_1)

            # B2: Viết lại lời giải theo logic toán học
            loigiai = (r"Để hàm số có đạo hàm tại $x = %s$, trước hết hàm số phải liên tục tại $x = %s$. \\ "
                       r"Ta có: $\lim_{x \to %s^-} f(x) = \lim_{x \to %s^-} (%sx %s) = %s$. \\ "
                       r"$\lim_{x \to %s^+} f(x) = f(%s) = a(%s)^2 + b(%s) = a + b$. \\ "
                       r"Để hàm số liên tục thì $a + b = %s$. (1) \\ "
                       r"Mặt khác, đạo hàm tại $x = %s$ tồn tại khi và chỉ khi: \\ "
                       r"$\lim_{x \to %s^-} \frac{f(x) - f(%s)}{x - %s} = \lim_{x \to %s^+} \frac{f(x) - f(%s)}{x - %s}$. \\ "
                       r"Ta có: $\lim_{x \to %s^-} \frac{%sx %s - (%s)}{x - %s} = %s$. \\ "
                       r"$\lim_{x \to %s^+} \frac{ax^2 + bx - (a+b)}{x - %s} = \lim_{x \to %s^+} \frac{a(x^2-1) + b(x-1)}{x - 1} = 2a + b$. \\ "
                       r"Vậy ta có $2a + b = %s$."
                       % (latex(x0), latex(x0), 
                          latex(x0), latex(x0), latex(c), ("+" + str(d) if d >= 0 else str(d)), latex(c*x0 + d),
                          latex(x0), latex(x0), latex(x0), latex(x0),
                          latex(c*x0 + d),
                          latex(x0),
                          latex(x0), latex(x0), latex(x0), latex(x0), latex(x0), latex(x0),
                          latex(x0), latex(c), ("+" + str(d) if d >= 0 else str(d)), latex(c*x0 + d), latex(x0), latex(c),
                          latex(x0), latex(x0), latex(x0),
                          latex(c)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('1x','x')
            return content


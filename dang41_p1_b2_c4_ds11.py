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


def bt_dang41_p1_b2_c4_ds11(self):
            # Khai báo biến
            # --- B3: Khởi tạo và Random ---
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Chọn số mũ n ngẫu nhiên từ 100 đến 2025
                n = random.randint(100, 2025)
                m = n - 1

                # Tính toán giá trị a, b dựa trên đạo hàm (L'Hopital) tại x=1
                # Tử số: x^n + x - 2 -> đạo hàm: n*x^(n-1) + 1. Tại x=1, giá trị là n + 1
                # Mẫu số: x^m + x - 2 -> đạo hàm: m*x^(m-1) + 1. Tại x=1, giá trị là m + 1 = (n-1) + 1 = n
                a = n + 1
                b = n

                # Kết quả cần tìm là a^2 - b^2
                # Vì a = n+1 và b = n nên a^2 - b^2 = (n+1)^2 - n^2 = 2n + 1
                kq_val = a**2 - b**2
                da = f"${latex(kq_val)}$"

                # Tạo các đáp án nhiễu (sai)
                s = [
                    f"${latex(kq_val + random.randint(1, 10))}$",
                    f"${latex(kq_val - random.randint(1, 5))}$",
                    f"${latex(a + b + 2)}$",
                    f"${latex(a**2 + b**2)}$",
                    f"${latex(2*n)}$",
                    f"${latex(n**2)}$"
                ]
                # Loại bỏ giá trị trùng với đáp án đúng nếu có
                s = list(set([i for i in s if i != da]))

                das1 = random.choice(s); s.remove(das1)
                das2 = random.choice(s); s.remove(das2)
                das3 = random.choice(s)

                # --- B2: Viết lại đề bài ---
                noidungcauhoi = (r"Giá trị của $\lim_{x \to 1} \frac{x^{%s} + x - 2}{x^{%s} + x - 2}$ bằng $\frac{a}{b}$, với $\frac{a}{b}$ là phân số tối giản. Giá trị của $a^2 - b^2$ bằng"
                                 % (latex(n), latex(m)))

                # Nội dung lời giải chi tiết
                loigiai = (r"""Ta có:
                    $$\lim_{x \to 1} \frac{x^{%s} + x - 2}{x^{%s} + x - 2} = \lim_{x \to 1} \frac{(x^{%s} - 1) + (x - 1)}{(x^{%s} - 1) + (x - 1)}$$
                    $$= \lim_{x \to 1} \frac{(x-1)(x^{%s} + x^{%s} + \dots + 1) + (x-1)}{(x-1)(x^{%s} + x^{%s} + \dots + 1) + (x-1)}$$
                    $$= \lim_{x \to 1} \frac{x^{%s} + x^{%s} + \dots + x + 2}{x^{%s} + x^{%s} + \dots + x + 2}$$
                    $$= \frac{1+1+\dots+1+2}{1+1+\dots+1+2} = \frac{%s}{%s}.$$
                    Vì $\frac{%s}{%s}$ là phân số tối giản nên $a = %s, b = %s$.
                    Vậy $a^2 - b^2 = %s^2 - %s^2 = %s.$"""
                           % (latex(n), latex(m), latex(n), latex(m),
                              latex(n-1), latex(n-2), latex(m-1), latex(m-2),
                              latex(n-1), latex(n-2), latex(m-1), latex(m-2),
                              latex(a), latex(b), latex(a), latex(b),
                              latex(a), latex(b), latex(a), latex(b), latex(kq_val)))

                # --- Đóng gói đáp án ---
                da_d = '\\True ' + str(da)
                list_1 = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)

            # --- Xuất kết quả theo format mẫu (Đã sửa list_all thành list_1) ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


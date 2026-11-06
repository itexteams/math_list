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


def bt_dang19_p4_b1_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # B1: Nghiên cứu đề bài - Viết phương trình tiếp tuyến y = f'(x0)(x - x0) + y0
            # B3: Suy nghĩ cách random
            a = random.choice([1, 2, 3, -1, -2])
            b = random.randint(-5, 5)
            c = random.randint(-5, 5)
            x0 = random.randint(-2, 3)

            # Thiết lập hàm số
            f = a*x**3 + b*x**2 + c
            y0 = f.subs(x, x0)
            f_prime = diff(f, x)
            k = f_prime.subs(x, x0)

            # Thành phần phương trình tiếp tuyến: y = kx + m
            m = -k*x0 + y0

            # Hàm xử lý dấu toán học để hiển thị đẹp (y = ax + b)
            def format_line(coeff, const):
                expr = coeff * x + const
                return latex(expr)

            # Tạo các đáp án
            da_dung = f"y = {format_line(k, m)}"
            s = [
                f"y = {format_line(k, m + random.randint(1, 3))}",
                f"y = {format_line(k + 1, m)}",
                f"y = {format_line(1, m)}", # Giống câu 2 trong hình
                f"y = {latex(-1*x + m)}",
                f"y = {latex(sp.Rational(1,2)*x + m)}"
            ]
            random.shuffle(s)
            list_da = [f"\\True ${da_dung}$", f"${s[0]}$", f"${s[1]}$", f"${s[2]}$"]
            random.shuffle(list_da)

            # B2: Viết lại nội dung theo mẫu
            noidungcauhoi = (r'Cho hàm số $y = %s$ $(C)$. Lập phương trình tiếp tuyến của hàm số tại điểm $M(%s; %s)$.' 
                             %(latex(f), latex(x0), latex(y0)))

            # Xử lý trình bày lời giải (Sửa lỗi hiển thị dấu bằng và dấu ngoặc)
            loigiai = (r'''Ta có $y' = %s$. \\
            Tại điểm $M(%s; %s)\in (C)$, hệ số góc của tiếp tuyến là $y'(%s) = %s$. \\
            Phương trình tiếp tuyến của $(C)$ tại $M$ là: \\
            $y = y'(%s)(x - %s) + (%s) \Leftrightarrow y = %s(x %s) %s \Leftrightarrow y = %s$.'''
                %(latex(f_prime), 
                  latex(x0), latex(y0), latex(x0), latex(k),
                  latex(x0), latex(x0), latex(y0), 
                  latex(k), 
                  ('- ' + latex(x0) if x0 >= 0 else '+ ' + latex(abs(x0))), 
                  ('+ ' + latex(y0) if y0 >= 0 else '- ' + latex(abs(y0))),
                  format_line(k, m)
                ))

            # Xuất câu trắc nghiệm đúng mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


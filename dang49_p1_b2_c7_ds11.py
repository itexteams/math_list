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


def bt_dang49_p1_b2_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # B1 & B3: Phân tích và tạo biến ngẫu nhiên
            a = random.randint(2, 6) 
            c = 1 - (a + 2) 

            # Viết biểu thức đúng cú pháp Python
            y = a * sin(x)**2 - cos(2*x) + x

            # Tính đạo hàm
            y_prime = diff(y, x)
            coeff_sin = a + 2
            val_sin = (c - 1) / coeff_sin

            # Các thành phần hiển thị lời giải
            y_prime_step1 = f"{2*a}\\sin x \\cos x + 2\\sin 2x + 1"
            y_prime_step2 = f"{a}\\sin 2x + 2\\sin 2x + 1"
            y_prime_final = f"{coeff_sin}\\sin 2x + 1"

            # Đáp án
            da_dung = f"$x = -\\frac{{\\pi}}{4} + k\\pi, k \\in \\mathbb{{Z}}$"
            s = [
                f"$x = \\frac{{\\pi}}{4} + k\\pi, k \\in \\mathbb{{Z}}$",
                f"$x = -\\frac{{\\pi}}{2} + k2\\pi, k \\in \\mathbb{{Z}}$",
                f"$x = \\frac{{\\pi}}{6} + k\\pi, k \\in \\mathbb{{Z}}$",
                f"$x = k\\pi, k \\in \\mathbb{{Z}}$"
            ]
            random.shuffle(s)
            das1, das2, das3 = s[:3]

            # --- SỬA LỖI F-STRING TẠI ĐÂY ---
            # Bước 1: Lấy mã latex của y
            y_latex = latex(y)
            # Bước 2: Thay thế các ký hiệu để hiển thị đẹp hơn bên ngoài f-string
            y_display = y_latex.replace(r'sin^{2}{\left(x \right)}', r'sin^2 x')
            # Bước 3: Đưa vào nội dung câu hỏi
            noidungcauhoi = f"Cho hàm số $y = {y_display}$, giải phương trình $y' = {c}$ được nghiệm là"
            # -------------------------------

            # Trộn đáp án
            da_d = '\\True ' + da_dung
            list_1 = [da_d, das1, das2, das3]
            random.shuffle(list_1)

            # Lời giải
            loigiai = (f"TXĐ: $D = \\mathbb{{R}}$ \\\\\n"
                       f"Ta có: $y' = {y_prime_step1} = {y_prime_step2} = {y_prime_final}$ \\\\\n"
                       f"$y' = {c} \\Leftrightarrow {y_prime_final} = {c} \\Leftrightarrow \\sin 2x = {int(val_sin)}$ \\\\\n"
                       f"$\\Leftrightarrow 2x = -\\frac{{\\pi}}{2} + k2\\pi \\Leftrightarrow x = -\\frac{{\\pi}}{4} + k\\pi (k \\in \\mathbb{{Z}})$.")

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content


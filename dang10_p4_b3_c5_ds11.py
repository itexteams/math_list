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


def bt_dang10_p4_b3_c5_ds11(self):
            # Khai báo biến
            # Chọn số chính phương để khai căn ra số nguyên đẹp
            b_val = random.choice([4, 9, 16, 25, 36]) 
            sqrt_b = int(b_val**0.5)

            # Chọn hệ số sao cho d/c là phân số không nguyên (để bài toán hay hơn)
            c_val = random.randint(2, 5)
            d_val = random.randint(1, 7)
            while d_val % c_val == 0 or not (-sqrt_b < d_val/c_val < sqrt_b):
                d_val = random.randint(1, 10)

            a_val = random.randint(2, 2025)
            n_val = random.randint(2, 2025)

            # --- Xử lý phân số bằng Sympy ---
            phan_so = Rational(d_val, c_val)
            phan_so_latex = latex(phan_so)

            # --- Nội dung đề bài ---
            noidungcauhoi = (f"Tìm tập xác định $D$ của hàm số $y = \\log_{{{a_val}}}({b_val} - x^2) + ({c_val}x - {d_val})^{{-{n_val}}}$.")

            # --- Các phương án trả lời ---
            # Đáp án đúng
            da_dung = f"\\True $\\left(-{sqrt_b}; {phan_so_latex}\\right) \\cup \\left({phan_so_latex}; {sqrt_b}\\right)$"

            # Các đáp án sai (định dạng phân số)
            da_s1 = f"$\\left[-{sqrt_b}; {phan_so_latex}\\right) \\cup \\left({phan_so_latex}; {sqrt_b}\\right]$"
            da_s2 = f"$\\left(-{sqrt_b}; {sqrt_b}\\right)$"
            da_s3 = f"$\\left({phan_so_latex}; {sqrt_b}\\right)$"

            list_1 = [da_dung, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # --- Nội dung lời giải ---
            loigiai = (f"Điều kiện xác định của hàm số là: "
                       f"$\\begin{{cases}} {b_val} - x^2 > 0 \\\\ {c_val}x - {d_val} \\neq 0 \\end{{cases}} "
                       f"\\Leftrightarrow \\begin{{cases}} -{sqrt_b} < x < {sqrt_b} \\\\ x \\neq \\frac{{{d_val}}}{{{c_val}}} \\end{{cases}}$. \\\\ "
                       f"Vậy tập xác định của hàm số là $D = \\left(-{sqrt_b}; {phan_so_latex}\\right) \\cup \\left({phan_so_latex}; {sqrt_b}\\right)$.")

            # --- Xuất câu trắc nghiệm ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


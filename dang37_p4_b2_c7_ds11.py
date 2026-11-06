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


def bt_dang37_p4_b2_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # B1- Nghiên cứu đề bài và lời giải
            # B3- Random bài toán
            a = random.choice([2, 3, 5, 7])
            b = random.choice([2, 3, 5])
            c = random.randint(2, 5)

            u = -c*x**2 + x
            y = a**x + log(u, b)

            # Tính toán đạo hàm bằng sympy
            dy_exp = a**x * ln(a)
            du = sp.diff(u, x)
            dy_log = du / (u * ln(b))
            y_prime = dy_exp + dy_log

            # Hàm xử lý định dạng Latex chuẩn
            def clean_latex(expr):
                s = latex(expr)
                # Thay thế các lỗi hiển thị dấu phổ biến
                s = s.replace('+ -', '- ').replace('- -', '+ ')
                return s

            # Chuẩn hóa đạo hàm y' sang y^\prime để tránh lỗi \mathaccent
            y_p_tex = r"y^{\prime}"

            # Các đáp án
            da_dung = r'\True $%s$' % clean_latex(y_prime)
            sai1 = r'$%s$' % clean_latex(a**x / ln(a) + dy_log)
            sai2 = r'$%s$' % clean_latex(dy_exp + du / u)
            sai3 = r'$%s$' % clean_latex(dy_exp + 1 / (u * ln(b)))

            list_da = [da_dung, sai1, sai2, sai3]
            random.shuffle(list_da)

            # B2- Viết nội dung lời giải (Sử dụng r'' và tránh dấu nháy đơn trực tiếp)
            noidungcauhoi = r'Tính đạo hàm của hàm số: $y = %s + \log_{%s}(%s)$. ' % (latex(a**x), b, latex(u))

            loigiai = (r'Ta có $%s = \left(%s + \log_{%s}(%s)\right)^{\prime} = \left(%s\right)^{\prime} + \left(\log_{%s}(%s)\right)^{\prime}$ \\ '
                       r'$= %s \cdot \ln %s + \frac{\left(%s\right)^{\prime}}{\left(%s\right)\ln %s}$ \\ '
                       r'$= %s + \frac{%s}{(%s)\ln %s}$.' 
                       % (y_p_tex, latex(a**x), b, latex(u), latex(a**x), b, latex(u),
                          latex(a**x), a, latex(u), latex(u), b,
                          clean_latex(dy_exp), clean_latex(du), latex(u), b))

            # --- Xuất câu trắc nghiệm ---
            # Đảm bảo cấu trúc minipage, ex, choice và loigiai chính xác
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'
                + str(noidungcauhoi) + '\n'
                '\\loigiai{' + loigiai + '}\n'
                '\\end{ex}\n'
                '\\end{minipage} \n\n')
            return content


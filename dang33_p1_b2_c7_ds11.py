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


def bt_dang33_p1_b2_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            x = symbols('x')

            # B1: Nghiên cứu đề bài - Tính đạo hàm y = 5^(2x-1)
            # B3: Suy nghĩ cách random bài toán
            # Random cơ số a (dương, khác 1) và hệ số của số mũ (ax + b)
            a = random.choice([2, 3, 4, 5, 6, 7, 10])
            h_so_x = random.randint(2, 9)
            h_so_tu_do = random.randint(-9, 9)

            # Hàm số tổng quát: y = a^(h_so_x * x + h_so_tu_do)
            f_mu = h_so_x * x + h_so_tu_do
            y = a**f_mu

            # Tính đạo hàm
            # Công thức: (a^u)' = u' * a^u * ln(a)
            u_prime = sp.diff(f_mu, x)
            y_prime = u_prime * (a**f_mu) * ln(a)

            # Định dạng hiển thị số mũ để tránh dấu +- hoặc --
            def format_mu(h_x, h_td):
                dau = "+" if h_td >= 0 else ""
                if h_td == 0:
                    return f"{h_x}x"
                return f"{h_x}x{dau}{h_td}".replace("+-", "-")

            mu_str = format_mu(h_so_x, h_so_tu_do)

            # B2: Viết lại nội dung theo mẫu
            noidungcauhoi = r"Đạo hàm của hàm số: $y = %s^{%s}$ là" % (a, mu_str)

            # Đáp án đúng
            da_dung = r"$y' = %s \cdot %s^{%s} \cdot \ln %s$" % (latex(u_prime), a, mu_str, a)

            # Tạo các đáp án nhiễu (sai công thức)
            s1 = r"$y' = %s^{%s} \cdot \ln %s$" % (a, mu_str, a) # Thiếu u'
            s2 = r"$y' = %s \cdot %s^{%s}$" % (latex(u_prime), a, mu_str) # Thiếu ln(a)
            s3 = r"$y' = (%s) \cdot %s^{%s - 1}$" % (mu_str, a, mu_str) # Nhầm sang đạo hàm hàm lũy thừa

            da_d = '\\True ' + da_dung
            list_1 = [da_d, s1, s2, s3]
            random.shuffle(list_1)

            # Lời giải chi tiết
            loigiai = r"Ta có $y' = (%s)' \cdot %s^{%s} \cdot \ln %s = %s \cdot %s^{%s} \cdot \ln %s$." % (
                mu_str, a, mu_str, a, latex(u_prime), a, mu_str, a
            )

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


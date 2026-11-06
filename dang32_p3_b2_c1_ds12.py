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


def bt_dang32_p3_b2_c1_ds12(self):
    # Khai báo hàm làm tròn
    def round_SA(a): 
        val = float(a)
        if val.is_integer():
            return "", str(int(val))

        str_a = f"{val:.5f}".rstrip('0')
        integer_part, _, decimal_part = str_a.partition('.')

        if len(integer_part) > 2:
            number = Decimal(str(val)).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
            cirle = "(làm tròn kết quả đến hàng đơn vị)."
        elif len(integer_part) == 2 and len(decimal_part) > 1:
            number = Decimal(str(val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
            cirle = "(làm tròn kết quả đến hàng phần chục)."
        elif len(decimal_part) <= 2:
            number = Decimal(str_a)
            cirle = ""
        else:
            number = Decimal(str(val)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
            cirle = "(làm tròn kết quả đến hàng phần trăm)."

        return cirle, str(number).replace('.', ',')

    # ------------------------------------------------------------------------------BÀI TOÁN
    # 1. Sinh ngẫu nhiên các giá trị gốc cho bài toán
    W = random.randint(2, 5)                # Chiều rộng sông (km)
    L = random.randint(W + 3, 12)           # Khoảng cách hạ lưu (km)
    v_cheo = random.randint(3, 6)           # Tốc độ chèo (km/h)
    v_chay = random.randint(v_cheo + 1, 10) # Tốc độ chạy (km/h)

    x = symbols('x', positive=True, real=True)

    # 2. Giải bài toán
    # Hàm tổng thời gian T(x)
    ham_T = sp.sqrt(W**2 + x**2) / v_cheo + (L - x) / v_chay
    T_prime = sp.diff(ham_T, x)

    try:
        solutions = sp.solve(sp.Eq(T_prime, 0), x)
        pos_sols = [sol for sol in solutions if sol.is_real and sol > 0]
        x_candidate = pos_sols[0] if pos_sols else (W * v_cheo) / sp.sqrt(v_chay**2 - v_cheo**2)
    except Exception:
        x_candidate = (W * v_cheo) / sp.sqrt(v_chay**2 - v_cheo**2)

    if float(x_candidate) >= L:
        x_final = L
    else:
        x_final = x_candidate

    # Tính kết quả thời gian nhỏ nhất
    ket_qua = ham_T.subs(x, x_final)

    # 3. Mã TikZ để vẽ hình minh họa
    scale_val = 0.4 if L > 7 else 0.6
    d_coord = min(4, L - 1)
    tikz_code = f"""\\begin{{tikzpicture}}[scale={scale_val},line width=1pt,line cap=round,line join=round,font=\\footnotesize]

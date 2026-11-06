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


def bt_dang26_p4_b2_c3_ds12(self):
            # Khai báo biến
            # --- BƯỚC 1: THIẾT LẬP BIẾN VÀ RANDOM ---
            a = random.randint(2, 6) 
            b = random.randint(2, 6) 
            # Đảm bảo b != a để n != 0 cho bài toán thú vị
            while a == b:
                b = random.randint(2, 6)

            m = a
            n = b - a
            p = -b
            ket_qua_bieu_thuc = m + 2*n - p

            # --- BƯỚC 2: TẠO CÁC ĐÁP ÁN NHIỄU ---
            da_dung = ket_qua_bieu_thuc
            s = set()
            while len(s) < 3:
                nhieu = da_dung + random.choice([-3, -2, -1, 1, 2, 3, 4, 5])
                if nhieu != da_dung:
                    s.add(nhieu)
            list_1 = [r'\True $%s$' % latex(da_dung)] + [r'$%s$' % latex(x) for x in s]
            random.shuffle(list_1)

            # --- BƯỚC 3: XỬ LÝ DẤU TRONG LỜI GIẢI ---
            # Hàm bổ trợ để hiển thị dấu + hoặc - chuẩn xác
            def display_sign(val):
                return "+" + str(val) if val > 0 else str(val)

            n_hien_thi = display_sign(n) # Ví dụ: "+1" hoặc "-2"

            # --- NỘI DUNG CÂU HỎI ---
            noidungcauhoi = (r"Biết rằng $\displaystyle \int_0^1 \frac{%se^{2x} + %s}{e^x} \,\text{d}x = \frac{m \cdot e^2 + n \cdot e + p}{e}$ "
                             r"(với $m, n, p \in \mathbb{Z}$). Tính $m + 2n - p$."
                             %(latex(a), latex(b)))

            # --- NỘI DUNG LỜI GIẢI ---
            loigiai = (r"Ta có: $\displaystyle \int_0^1 \frac{%se^{2x} + %s}{e^x} \,\text{d}x = \int_0^1 (%se^x + %se^{-x}) \,\text{d}x$ \\ "
                       r"$= (%se^x - %se^{-x}) \bigg|_0^1 = \left(%se - \frac{%s}{e}\right) - \left(%se^0 - %se^0\right)$ \\ "
                       r"$= %se - \frac{%s}{e} - (%s - %s) = %se - \frac{%s}{e} %s$ \\ "
                       r"$= \frac{%se^2 %se - %s}{e}$. \\ "
                       r"Do đó $m = %s, n = %s, p = %s$. \\ "
                       r"Vậy $m + 2n - p = %s + 2(%s) - (%s) = %s$."
                       %(latex(a), latex(b), latex(a), latex(b), 
                         latex(a), latex(b), latex(a), latex(b), latex(a), latex(b),
                         latex(a), latex(b), latex(a), latex(b), latex(a), latex(b), n_hien_thi,
                         latex(a), n_hien_thi, latex(b),
                         latex(m), latex(n), latex(p),
                         latex(m), latex(n), latex(p), latex(ket_qua_bieu_thuc)))

            # --- XUẤT KẾT QUẢ ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


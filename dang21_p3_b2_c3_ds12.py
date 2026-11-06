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


def bt_dang21_p3_b2_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')


            c = random.randint(-1, 2)          # Điểm phân nhánh
            m = c - random.randint(2, 3)       # Cận dưới (đảm bảo m < c)
            n = c + random.randint(1, 3)       # Cận trên (đảm bảo n > c)

            a1 = random.randint(1, 4)
            b1 = random.randint(1, 5)
            a2 = random.choice([2, 4, 6, 8])
            b2 = random.randint(-5, 5)

            f1 = a1*x**2 + b1
            f2 = a2*x + b2

            # --- TÍNH TOÁN ---
            # I1 = tích phân từ m đến c của f1
            I1 = integrate(f1, (x, m, c))
            # I2 = tích phân từ c đến n của f2
            I2 = integrate(f2, (x, c, n))

            kq_dung = I1 + I2

            # Tạo danh sách đáp án
            da_dung = '\\True $%s$' % latex(kq_dung)
            s = [
                '$%s$' % latex(kq_dung + random.randint(1, 5)),
                '$%s$' % latex(kq_dung - random.randint(1, 5)),
                '$%s$' % latex(I1 - I2)  # Đáp án nhiễu do sai dấu
            ]
            random.shuffle(s)

            list_1 = [da_dung, s[0], s[1], s[2]]
            random.shuffle(list_1)

            # --- NỘI DUNG CÂU HỎI ---
            # Sử dụng \mathrm{d}x theo yêu cầu
            noidungcauhoi = r'''Cho hàm số $f(x) = \begin{cases} %s & \text{khi } x \le %s \\ %s & \text{khi } x > %s \end{cases}$. Khi đó giá trị của $\displaystyle \int_{%s}^{%s} f(x) \mathrm{d}x$ bằng''' % (
                latex(f1), latex(c), latex(f2), latex(c), latex(m), latex(n)
            )

            # --- NỘI DUNG LỜI GIẢI ---
            loigiai = r'''Ta có: $\displaystyle \int_{%s}^{%s} f(x) \mathrm{d}x = \int_{%s}^{%s} f(x) \mathrm{d}x + \int_{%s}^{%s} f(x) \mathrm{d}x$ \\
            $= \displaystyle \int_{%s}^{%s} (%s) \mathrm{d}x + \int_{%s}^{%s} (%s) \mathrm{d}x$ \\
            $= \left( %s \right) \Big|_{%s}^{%s} + \left( %s \right) \Big|_{%s}^{%s}$ \\
            $= %s + %s = %s$.''' % (
                latex(m), latex(n), latex(m), latex(c), latex(c), latex(n),
                latex(m), latex(c), latex(f1), latex(c), latex(n), latex(f2),
                latex(integrate(f1, x)), latex(m), latex(c), latex(integrate(f2, x)), latex(c), latex(n),
                latex(I1), latex(I2), latex(kq_dung)
            )
            #Đáp án
            dapan='\\shortans[0]{$%s$}\n'%(latex(kq_dung))

            # --- XUẤT CÂU TRẮC NGHIỆM ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


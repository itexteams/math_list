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


def bt_dang50_p4_b2_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            x = symbols('x')

            # Danh sách các dạng bài tập
            lisdang = ['1', '2']
            dang = random.choice(lisdang)

            if dang == '1':
                # Dạng f(x) = sin^2(ax)
                a = random.randint(1, 5)
                if a == 1:
                    f = sin(x)**2
                    expr_tex = "\\sin^2 x"
                    u = "\\sin x"
                    u_prime_tex = "\\cos x"
                else:
                    f = sin(a*x)**2
                    expr_tex = f"\\sin^2({a}x)"
                    u = f"\\sin({a}x)"
                    u_prime_tex = f"{a}\\cos({a}x)"

                f_prime = diff(f, x)
                # Rút gọn về dạng sin(2ax)
                kq_chuan = f"{a}\\sin({2*a}x)" if a != 1 else "\\sin(2x)"

                noidungcauhoi = f"Tính đạo hàm của hàm số $f(x) = {expr_tex}$."

                da_d = f"\\True $f'(x) = {kq_chuan}$"

                # Tạo các đáp án nhiễu
                s = [
                    f"$f'(x) = 2{u}$",
                    f"$f'(x) = -{kq_chuan}$",
                    f"$f'(x) = {a}\\cos({2*a}x)$",
                    f"$f'(x) = 2{u_prime_tex}$"
                ]

                loigiai = (f"Ta có $f(x) = ({u})^2$. \\\\\n"
                           f"Áp dụng công thức đạo hàm hàm hợp $(u^n)' = n \\cdot u^{{n-1}} \\cdot u'$: \\\\\n"
                           f"$f'(x) = 2 \\cdot {u} \\cdot ({u})' = 2 \\cdot {u} \\cdot {u_prime_tex}$. \\\\\n"
                           f"Sử dụng công thức nhân đôi $2\\sin \\alpha \\cos \\alpha = \\sin 2\\alpha$, ta được: \\\\\n"
                           f"$f'(x) = {kq_chuan}$.")

            else:
                # Dạng f(x) = cos^2(ax)
                a = random.randint(1, 5)
                if a == 1:
                    f = cos(x)**2
                    expr_tex = "\\cos^2 x"
                    u = "cos x"
                    u_prime_tex = "-\\sin x"
                else:
                    f = cos(a*x)**2
                    expr_tex = f"\\cos^2({a}x)"
                    u = f"cos({a}x)"
                    u_prime_tex = f"-{a}\\sin({a}x)"

                f_prime = diff(f, x)
                kq_chuan = f"-{a}\\sin({2*a}x)" if a != 1 else "-\\sin(2x)"

                noidungcauhoi = f"Tính đạo hàm của hàm số $f(x) = {expr_tex}$."

                da_d = f"\\True $f'(x) = {kq_chuan}$"

                s = [
                    f"$f'(x) = 2{u}$",
                    f"$f'(x) = {a if a!=1 else ''}\\sin({2*a}x)$",
                    f"$f'(x) = -2{u}$",
                    f"$f'(x) = -{a}\\cos({2*a}x)$"
                ]

                loigiai = (f"Ta có $f(x) = ({u})^2$. \\\\\n"
                           f"Áp dụng công thức đạo hàm hàm hợp $(u^n)' = n \\cdot u^{{n-1}} \\cdot u'$: \\\\\n"
                           f"$f'(x) = 2 \\cdot {u} \\cdot ({u})' = 2 \\cdot {u} \\cdot ({u_prime_tex})$. \\\\\n"
                           f"Sử dụng công thức nhân đôi $2\\sin \\alpha \\cos \\alpha = \\sin 2\\alpha$, ta được: \\\\\n"
                           f"$f'(x) = {kq_chuan}$.")

            # Lấy ngẫu nhiên 3 đáp án sai
            random.shuffle(s)
            da_s1, da_s2, da_s3 = s[0], s[1], s[2]

            # Đưa các đáp án vào danh sách chọn ngẫu nhiên
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


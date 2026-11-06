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


def bt_dang49_p4_b3_c5_ds10(self):
            # Khai báo biết
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random các thông số cho biểu thức x(ax + b)^n + (x + d)^m
                # Tìm hệ số của x^5
                a = randint(2, 4)
                b = random.choice([-2, -1, 1, 2])
                n = randint(6, 8)

                d = random.choice([-4, -3, -2, 2, 3, 4])
                m = randint(7, 9)

                # Tính toán hệ số cho phần 1: x*(ax + b)^n
                # Cần tìm hệ số x^4 trong (ax + b)^n
                k1 = 4
                c_n_k1 = binomial(n, k1)
                h1 = c_n_k1 * (a**k1) * (b**(n-k1))

                # Tính toán hệ số cho phần 2: (x + d)^m
                # Cần tìm hệ số x^5 trong (x + d)^m
                k2 = 5
                c_m_k2 = binomial(m, k2)
                h2 = c_m_k2 * (1**k2) * (d**(m-k2))

                # Tổng hệ số
                kq_val = h1 + h2
                kq = latex(kq_val)

                # Tạo các phương án sai
                s = [
                    latex(h1 - h2),
                    latex(kq_val + randint(100, 500)),
                    latex(kq_val - randint(100, 500)),
                    latex(-kq_val),
                    latex(h2 - h1),
                    latex(kq_val + 1000)
                ]

                # Loại bỏ trùng lặp và đáp án đúng
                s = list(set(s))
                if kq in s:
                    s.remove(kq)

                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Xử lý hiển thị dấu cho b và d trong đề bài
                b_sign = "+" if b > 0 else "-"
                b_abs = abs(b)
                d_sign = "+" if d > 0 else "-"
                d_abs = abs(d)

                # Câu hỏi
                noidungcauhoi = ('''Tìm hệ số của $x^5$ trong khai triển biểu thức $x\\left(%sx %s %s\\right)^{%s} + \\left(x %s %s\\right)^{%s}$.'''
                                 %(latex(a), b_sign, latex(b_abs), latex(n), d_sign, latex(d_abs), latex(m)))

                # Các đáp án
                da_d = ('\\True $%s$'%(kq))
                da_s1 = '$%s$'%(das1)
                da_s2 = '$%s$'%(das2) 
                da_s3 = '$%s$'%(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                # Phần 1
                loigiai = ('''Hệ số của $x^5$ trong khai triển biểu thức $x\\left(%sx %s %s\\right)^{%s}$ là $\\text{C}_{%s}^{%s} \\cdot %s^{%s} \\cdot \\left(%s\\right)^{%s} = %s$. \\\\
                           Hệ số của $x^5$ trong khai triển biểu thức $\\left(x %s %s\\right)^{%s}$ là $\\text{C}_{%s}^{%s} \\cdot \\left(%s\\right)^{%s} = %s$. \\\\
                           Suy ra hệ số của $x^5$ trong khai triển biểu thức đã cho là $%s %s %s = %s$.'''
                           %(latex(a), b_sign, latex(b_abs), latex(n), latex(n), latex(k1), latex(a), latex(k1), latex(b), latex(n-k1), latex(h1),
                             d_sign, latex(d_abs), latex(m), latex(m), latex(k2), latex(d), latex(m-k2), latex(h2),
                             latex(h1), "+" if h2 >= 0 else "-", latex(abs(h2)), latex(kq_val)
                            ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


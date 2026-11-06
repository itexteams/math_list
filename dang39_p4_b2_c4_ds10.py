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


def bt_dang39_p4_b2_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 1: Random tọa độ hai điểm cắt trục hoành A(x1, 0) và B(x2, 0)
                # Để bài toán đẹp, ta chọn x1, x2 là số nguyên
                x1 = random.randint(-5, 2)
                khoang_cach = random.randint(2, 6)
                x2 = x1 + khoang_cach # Đảm bảo x1 < x2

                # Đường thẳng chứa đỉnh y = k (k khác 0)
                k = random.choice([-4, -2, -1, 1, 2, 4])


                x_d = Rational(x1 + x2, 2)
                a = k / ((x_d - x1) * (x_d - x2))

                b = -a * (x1 + x2)
                c = a * x1 * x2

                # Đáp án đúng
                f_x = a*x**2 + b*x + c
                kq = latex(f_x).replace('**2', '^2')
                da_d = '\\True $y = ' + kq + '$'

                # Tạo các đáp án sai (nhiễu)
                # Nhiễu 1: Sai dấu hệ số a
                f_s1 = -a*x**2 - b*x - c
                # Nhiễu 2: Đổi chỗ x1, x2 (thực tế vẫn ra đáp án cũ, nên ta đổi k)
                f_s2 = a*x**2 + b*x - c
                # Nhiễu 3: Tịnh tiến đồ thị
                f_s3 = a*x**2 + b*x + c + 1

                s = [
                    '$y = ' + latex(f_s1).replace('**2', '^2') + '$',
                    '$y = ' + latex(f_s2).replace('**2', '^2') + '$',
                    '$y = ' + latex(f_s3).replace('**2', '^2') + '$'
                ]

                # Trộn đáp án
                list_1 = [da_d, s[0], s[1], s[2]]
                random.shuffle(list_1)

                # Câu hỏi
                noidungcauhoi = ('''Xác định parabol $y = ax^2 + bx + c$, biết rằng parabol đó cắt trục hoành tại hai điểm $A(%s;0)$, $B(%s;0)$ và có đỉnh nằm trên đường thẳng $y = %s$.'''
                                 %(latex(x1), latex(x2), latex(k)))

                # Nội dung lời giải chi tiết theo mẫu ảnh
                delta_sym = 'b^2 - 4ac'
                loigiai = ('''Vì $(P)$ cắt trục hoành tại hai điểm $A(%s;0)$, $B(%s;0)$ nên \\\\
                             $\\begin{cases} 0 = a \\cdot (%s)^2 + b \\cdot (%s) + c \\\\ 0 = a \\cdot (%s)^2 + b \\cdot (%s) + c \\end{cases} \\Leftrightarrow \\begin{cases} %s a + %s b + c = 0 \\\\ %s a + %s b + c = 0 \\end{cases} (1)$ \\\\
                             Hơn nữa $(P)$ có đỉnh thuộc đường thẳng $y = %s$ nên \\\\
                             $-\\frac{\\Delta}{4a} = %s \\Leftrightarrow \\Delta = %s a \\Leftrightarrow b^2 - 4ac = %s a (2)$ \\\\
                             Từ (1) và (2) ta tìm được $a = %s, b = %s, c = %s$. \\\\
                             Vậy $(P): y = %s$.'''
                           %(latex(x1), latex(x2), 
                             latex(x1), latex(x1), latex(x2), latex(x2),
                             latex(x1**2), latex(x1), latex(x2**2), latex(x2),
                             latex(k), latex(k), latex(-4*k), latex(-4*k),
                             latex(a), latex(b), latex(c), kq))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


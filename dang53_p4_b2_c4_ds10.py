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


def bt_dang53_p4_b2_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B3: Suy nghĩ tìm cách random bài toán
                # Chọn các hệ số sao cho nghiệm x0 đẹp (thường là số nguyên nhỏ)
                # Phương trình: y = mx^2 + 2(m + k)x + (am + b)
                # Gom m: m(x^2 + 2x + a) + (2kx + b - y) = 0

                x0_1 = random.randint(-3, 2)
                x0_2 = random.randint(x0_1 + 1, 5)

                # Tạo đa thức m: (x - x0_1)(x - x0_2) = x^2 - (x0_1+x0_2)x + x0_1*x0_2
                # Để giống mẫu 2(m - 2), ta đặt hệ số của x là 2*(m + k)
                # Ở đây mình sẽ làm tổng quát: y = m*x^2 + (m*A + B)x + (m*C + D)

                A = random.randint(-5, 5)
                B = random.randint(-5, 5)
                C = random.randint(-10, 10)
                D = random.randint(-10, 10)

                m, x, y = symbols('m x y')
                # Hàm số: y = m*x**2 + (m*A + B)*x + (m*C + D)
                # Gom theo m: m*(x**2 + A*x + C) + (B*x + D - y) = 0

                # Giải tìm x0
                x_coords = solve(x**2 + A*x + C, x)

                # Đảm bảo có 2 nghiệm phân biệt và là số hữu tỷ/nguyên để đề bài đẹp
                while len(x_coords) < 2 or not all(val.is_rational for val in x_coords):
                    A = random.randint(-5, 5)
                    C = random.randint(-10, 10)
                    x_coords = solve(x**2 + A*x + C, x)

                x1, x2 = x_coords
                y1 = B*x1 + D
                y2 = B*x2 + D

                # Đáp án đúng
                da_dung = '$A_1(%s; %s), A_2(%s; %s)$' % (latex(x1), latex(y1), latex(x2), latex(y2))

                # B4: Điều chỉnh các phương án sai (không trùng đáp án đúng)
                s = []
                while len(s) < 3:
                    # Tạo các cặp điểm sai bằng cách đảo dấu hoặc cộng ngẫu nhiên
                    off_x = random.choice([-1, 1, 2])
                    off_y = random.choice([-1, 1, 2])
                    wrong_da = '$A_1(%s; %s), A_2(%s; %s)$' % (latex(x1+off_x), latex(y1-off_y), latex(x2-off_x), latex(y2+off_y))
                    if wrong_da != da_dung and wrong_da not in s:
                        s.append(wrong_da)

                # Nội dung câu hỏi
                # y = mx^2 + (Am + B)x + Cm + D
                # Biến đổi về dạng giống ảnh: y = mx^2 + (A)mx + Bx + Cm + D
                # Ví dụ ảnh: y = mx^2 + 2(m-2)x - 3m + 1
                term_x = ""
                if B == 0:
                    term_x = "%s m x" % (latex(A))
                else:
                    term_x = " ( %s m %s ) x" % (latex(A), "+ " + str(B) if B > 0 else str(B))

                # Làm đẹp biểu thức để in ra đề bài
                expr_y = "m x^2 + %s" % (latex(sp.expand((A*m + B)*x + C*m + D)))

                noidungcauhoi = ('''Tìm điểm cố định mà đồ thị hàm số $y = %s$ luôn đi qua.''' % latex(m*x**2 + (A*m + B)*x + C*m + D))

                # Các đáp án cho vào list
                da_d = '\\True ' + da_dung
                list_1 = [da_d, s[0], s[1], s[2]]
                random.shuffle(list_1)

                # B2: Viết lại lời giải chi tiết theo mẫu ảnh
                loigiai = ('''Gọi $A(x_0; y_0)$ là điểm cố định của đồ thị hàm số $\\Leftrightarrow y_0 = m x_0^2 + (%s m %s) x_0 + %s m %s$ với mọi $m$ \\\\
            $\\Leftrightarrow m(x_0^2 + %s x_0 %s) + %s x_0 - y_0 %s = 0$ với mọi $m$ \\\\
            $\\Leftrightarrow \\begin{cases} x_0^2 + %s x_0 %s = 0 \\\\ %s x_0 - y_0 %s = 0 \\end{cases} 
            \\Leftrightarrow \\begin{cases} x_0 = %s \\\\ y_0 = %s \\end{cases}$ hoặc $\\begin{cases} x_0 = %s \\\\ y_0 = %s \\end{cases}$ \\\\
            Vậy đồ thị luôn đi qua hai điểm cố định là $A_1(%s; %s)$ và $A_2(%s; %s)$ với mọi giá trị $m$.'''
                           % (latex(A), "+ " + str(B) if B >= 0 else str(B), latex(C), "+ " + str(D) if D >= 0 else str(D),
                              latex(A), "+ " + str(C) if C >= 0 else str(C), latex(B), "+ " + str(D) if D >= 0 else str(D),
                              latex(A), "+ " + str(C) if C >= 0 else str(C), latex(B), "+ " + str(D) if D >= 0 else str(D),
                              latex(x1), latex(y1), latex(x2), latex(y2),
                              latex(x1), latex(y1), latex(x2), latex(y2)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


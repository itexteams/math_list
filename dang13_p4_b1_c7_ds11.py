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


def bt_dang13_p4_b1_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            x = symbols('x')

            # B3: Suy nghĩ tìm cách random bài toán
            # Tạo hàm số y = (ax + b) / (cx + d) sao cho có nghiệm đẹp
            def generate_data():
                while True:
                    a = random.randint(-5, 5)
                    b = random.randint(-10, 10)
                    c = random.randint(1, 3)
                    d = random.randint(-5, 5)

                    # Đảm bảo hàm số không suy biến (ad - bc != 0) và mẫu khác 0
                    if (a*d - b*c) == 0: continue

                    f = (a*x + b) / (c*x + d)

                    # Chọn tung độ y0 sao cho hoành độ x0 là số nguyên để bài toán "đẹp"
                    # y0 = (ax0 + b) / (cx0 + d) => x0 = (d*y0 - b) / (a - c*y0)
                    y0 = random.randint(-5, 5)

                    # Kiểm tra điều kiện tồn tại x0 và x0 nguyên
                    tu = d * y0 - b
                    mau = a - c * y0
                    if mau != 0 and tu % mau == 0:
                        x0 = tu // mau
                        # Kiểm tra x0 không là nghiệm mẫu
                        if c * x0 + d != 0:
                            return a, b, c, d, y0, x0

            a, b, c, d, y0, x0 = generate_data()

            # Tính đạo hàm và hệ số góc k
            f = (a*x + b) / (c*x + d)
            f_prime = diff(f, x)
            k_value = f_prime.subs(x, x0)

            # Chuyển đổi k_value sang LaTeX và xử lý dấu
            k_latex = latex(k_value)

            # B2: Viết lại nội dung theo mẫu
            noidungcauhoi = (r'Cho hàm số $y = \frac{%s}{%s}$ có đồ thị $(C)$. Gọi $d$ là tiếp tuyến của $(C)$ tại điểm có tung độ bằng $%s$. Tìm hệ số góc $k$ của đường thẳng $d$.' 
                            % (latex(a*x + b), latex(c*x + d), latex(y0)))

            # Tạo các đáp án nhiễu
            da_dung = '$%s$' % k_latex
            s = set()
            while len(s) < 3:
                nhieu = k_value + random.choice([-2, -1, 1, 2, sp.Rational(1, 2), sp.Rational(-1, 2)])
                if nhieu != k_value:
                    s.add('$%s$' % latex(nhieu))

            list_nhieu = list(s)
            da_d = '\\True ' + da_dung
            list_1 = [da_d, list_nhieu[0], list_nhieu[1], list_nhieu[2]]
            random.shuffle(list_1)

            # Nội dung lời giải
            # Xử lý hiển thị đạo hàm gọn gàng theo công thức (ad-bc)/(cx+d)^2
            ad_bc = a*d - b*c
            mau_so_dao_ham = (c*x + d)**2

            loigiai = (r'''Tập xác định: $\mathscr{D} = \mathbb{R} \setminus \left\lbrace %s \right\rbrace$. \\
            Với $y = %s$, ta có: $\frac{%s}{%s} = %s \Rightarrow %s = %s \Leftrightarrow x = %s$. \\
            Ta có: $y' = \frac{%s}{%s}$. \\
            Hệ số góc của tiếp tuyến tại điểm có hoành độ bằng $%s$ là: \\
            $k = y'(%s) = \frac{%s}{(%s \cdot (%s) + %s)^2} = %s$.''' 
                      % (latex(sp.Rational(-d, c)), latex(y0), latex(a*x + b), latex(c*x + d), latex(y0), 
                         latex(a*x + b), latex(y0*(c*x + d)), latex(x0),
                         latex(ad_bc), latex(mau_so_dao_ham),
                         latex(x0), latex(x0), latex(ad_bc), latex(c), latex(x0), latex(d), k_latex))

            # Chỉnh sửa hiển thị dấu: Thay thế + - thành -
            loigiai = loigiai.replace('+ -', '- ').replace('- -', '+ ')

            # B4: Xuất câu trắc nghiệm theo mẫu yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


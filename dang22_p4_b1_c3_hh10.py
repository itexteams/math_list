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


def bt_dang22_p4_b1_c3_hh10(self):
            # Khai báo biến và chọn dạng (Trục Ox hoặc Trục Oy)
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                y=symbols('y')
                # Bước 3: Random các tọa độ điểm A, B, C
                # Đảm bảo các điểm không trùng nhau và không thẳng hàng để tạo thành tam giác
                check_collinear = True
                while check_collinear:
                    xa, ya = randint(-5, 5), randint(-5, 5)
                    xb, yb = randint(-5, 5), randint(-5, 5)
                    xc, yc = randint(-5, 5), randint(-5, 5)

                    # Vectơ BC
                    ubc_x = xc - xb
                    ubc_y = yc - yb

                    # Điều kiện BC không phải là 1 điểm và A, B, C không thẳng hàng
                    if (ubc_x != 0 or ubc_y != 0):
                        # Kiểm tra tích có hướng để tránh thẳng hàng
                        if (xb - xa) * (yc - ya) - (yb - ya) * (xc - xa) != 0:
                            check_collinear = False

                # Tính toán vectơ pháp tuyến của đường thẳng cần tìm
                # Vì đường thẳng song song với BC nên nhận vectơ pháp tuyến của BC làm VTPT
                # Vectơ chỉ phương u_BC = (ubc_x, ubc_y) -> VTPT n = (ubc_y, -ubc_x)
                n_x = ubc_y
                n_y = -ubc_x

                # Tối giản tọa độ VTPT (chia cho GCD)
                common = math.gcd(n_x, n_y)
                n_x //= common
                n_y //= common

                # Phương trình: n_x(x - xa) + n_y(y - ya) = 0 <=> n_x*x + n_y*y + (-n_x*xa - n_y*ya) = 0
                c_const = -n_x * xa - n_y * ya

                # Tạo biểu thức sympy để dùng hàm latex() cho đẹp
                pt_dung = n_x*x + n_y*y + c_const
                da_dung_str = '$' + latex(pt_dung) + ' = 0$'

                # Bước 4: Tạo các phương án sai (không trùng phương án đúng)
                list_sai = set()
                while len(list_sai) < 3:
                    # Cách 1: Thay đổi hệ số tự do
                    c_sai = c_const + randint(-5, 5)
                    if c_sai != c_const:
                        expr_sai = n_x*x + n_y*y + c_sai
                        list_sai.add('$' + latex(expr_sai) + ' = 0$')

                    # Cách 2: Đổi dấu một trong các hệ số
                    if len(list_sai) < 3:
                        expr_sai2 = n_x*x - n_y*y + randint(-5, 5)
                        if expr_sai2 != pt_dung:
                            list_sai.add('$' + latex(expr_sai2) + ' = 0$')

                list_sai = list(list_sai)

                # Câu hỏi
                noidungcauhoi = ('''Cho tam giác $ABC$ biết $A(%s; %s)$, $B(%s; %s)$, $C(%s; %s)$. Lập phương trình tổng quát đường thẳng qua $A$ và song song với $BC$.'''
                                 % (latex(xa), latex(ya), latex(xb), latex(yb), latex(xc), latex(yc)))

                # Các đáp án
                da_d = ('\\True ' + da_dung_str)
                da_s1 = list_sai[0]
                da_s2 = list_sai[1]
                da_s3 = list_sai[2]

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = ('''Vectơ chỉ phương của đường thẳng $BC$ là $\\vec{BC} = (%s - (%s); %s - (%s)) = (%s; %s)$. \\\\
                             Đường thẳng $BC$ có một vectơ pháp tuyến là $\\vec{n} = (%s; %s)$. \\\\
                             Vì đường thẳng cần tìm song song với đường thẳng $BC$ nên nó cũng nhận $\\vec{n} = (%s; %s)$ làm vectơ pháp tuyến. \\\\
                             Phương trình tổng quát của đường thẳng đi qua $A(%s; %s)$ và có VTPT $\\vec{n}$ là \\\\
                             $%s(x - (%s)) + (%s)(y - (%s)) = 0 \\Leftrightarrow %s$.'''
                           % (latex(xc), latex(xb), latex(yc), latex(yb), latex(ubc_x), latex(ubc_y),
                              latex(n_x), latex(n_y), 
                              latex(n_x), latex(n_y),
                              latex(xa), latex(ya),
                              latex(n_x), latex(xa), latex(n_y), latex(ya),
                              latex(pt_dung) + ' = 0'
                              ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 


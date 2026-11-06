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


def bt_dang78_p1_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # B3: Suy nghĩ tìm cách random bài toán
                # Tạo tọa độ điểm A và B ngẫu nhiên
                xa = randint(-5, 5)
                ya = randint(-5, 5)
                xb = randint(-5, 5)
                yb = randint(-5, 5)

                # Đảm bảo A và B không trùng nhau
                while xa == xb and ya == yb:
                    xb = randint(-5, 5)
                    yb = randint(-5, 5)

                # Tính tọa độ trung điểm I của AB
                xi = Rational(xa + xb, 2)
                yi = Rational(ya + yb, 2)

                # Tạo một đường thẳng đi qua I: a(x - xi) + b(y - yi) = 0  => ax + by + c = 0
                # Chọn hệ số a, b ngẫu nhiên cho phương án đúng
                a = randint(-3, 3)
                b = randint(-3, 3)
                if a == 0 and b == 0: a = 1

                # Tính c sao cho đường thẳng đi qua I
                # a*xi + b*yi + c = 0 => c = -(a*xi + b*yi)
                c_val = -(a * xi + b * yi)

                # Để phương trình đẹp (số nguyên), ta nhân tất cả với mẫu số chung của xi, yi (thường là 2)
                common_deno = 2
                a_final = a * common_deno
                b_final = b * common_deno
                c_final = c_val * common_deno

                # Rút gọn hệ số bằng gcd
                u = math.gcd(math.gcd(int(a_final), int(b_final)), int(c_final))
                a_final //= u
                b_final //= u
                c_final //= u

                # Đảm bảo hệ số a dương để nhìn đề bài chuyên nghiệp hơn
                if a_final < 0 or (a_final == 0 and b_final < 0):
                    a_final *= -1
                    b_final *= -1
                    c_final *= -1

                # Tạo biểu thức vế trái phương trình: ax + by + c
                x, y = symbols('x y')
                expr = a_final * x + b_final * y + c_final
                da_dung_str = latex(expr) + " = 0"

                # B4: Điều chỉnh các phương án sai (thay đổi hệ số tự do c)
                s_list = []
                offsets = [-10, -5, 2, 5, 10, 100]
                random.shuffle(offsets)
                for offset in offsets:
                    c_wrong = c_final + offset
                    if c_wrong != c_final:
                        expr_wrong = a_final * x + b_final * y + c_wrong
                        s_list.append("$" + latex(expr_wrong) + " = 0$")
                    if len(s_list) >= 3:
                        break

                # Gán các phương án
                da = "$" + da_dung_str + "$"
                das1, das2, das3 = s_list[0], s_list[1], s_list[2]

                # Câu hỏi
                noidungcauhoi = ('''Trong mặt phẳng với hệ tọa độ $Oxy$, cho hai điểm $A(%s;%s)$ và $B(%s;%s)$. Đường thẳng nào sau đây cách đều hai điểm $A$ và $B$?'''
                                 %(latex(xa), latex(ya), latex(xb), latex(yb)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Trộn đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = ('''Đường thẳng cách đều hai điểm $A$ và $B$ khi và chỉ khi nó thuộc một trong hai trường hợp sau:\\\\
                             Trường hợp 1: Đường thẳng đó song song hoặc trùng với đường thẳng $AB$.\\\\
                             Trường hợp 2: Đường thẳng đó đi qua trung điểm $I$ của đoạn thẳng $AB$.\\\\
                             Ta có tọa độ trung điểm $I$ của $AB$ là: $I\\left( \\frac{%s + %s}{2}; \\frac{%s + %s}{2} \\right) = I\\left( %s; %s \\right)$.\\\\
                             Kiểm tra phương án đúng: Thay tọa độ điểm $I$ vào phương trình $%s = 0$ ta được:\\\\
                             $%s \\cdot \\left(%s\\right) + %s \\cdot \\left(%s\\right) + %s = 0$ (luôn đúng).\\\\
                             Vậy đường thẳng $%s = 0$ cách đều hai điểm $A$ và $B$.'''
                           %(latex(xa), latex(xb), latex(ya), latex(yb), latex(xi), latex(yi),
                             latex(expr), latex(a_final), latex(xi), latex(b_final), latex(yi), latex(c_final),
                             latex(expr)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('+ -', '-')
            return content 


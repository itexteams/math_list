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


def bt_dang34_p1_b1_c3_hh10(self):
            # Khai báo biến và chọn dạng (Trục Ox hoặc Trục Oy)
            # Khai báo biến và chọn dạng
            lisdang=['1']
            dang = random.choice(lisdang)

            if dang=='1':
                # B3: Suy nghĩ tìm cách random bài toán
                # Chọn tọa độ điểm M(a; b) sao cho a, b nguyên dương và khác nhau để bài toán hay hơn
                a = randint(1, 6)
                b = randint(1, 6)
                while a == b:
                    b = randint(1, 6)

                # Thiết lập các ký hiệu toán học
                var_x, var_y = symbols('x y')

                # Tính toán phương trình đúng: x/a + y/b = 1 <=> b*x + a*y - a*b = 0
                # Sử dụng sympy để viết phương trình chuẩn tắc
                expr_dung = b*var_x + a*var_y - a*b
                da_dung_str = '$' + latex(expr_dung) + ' = 0$'

                # B4: Điều chỉnh các phương án sai (không trùng đáp án đúng)
                # Phương án sai 1: Nhầm hệ số giữa x và y (a*x + b*y - a*b = 0)
                expr_sai1 = a*var_x + b*var_y - a*b
                # Phương án sai 2: Sai dấu hằng số tự do (b*x + a*y + a*b = 0)
                expr_sai2 = b*var_x + a*var_y + a*b
                # Phương án sai 3: Tổng x + y = a + b (giống phương án D trong ảnh)
                expr_sai3 = var_x + var_y - (a + b)

                # Kiểm tra trùng lặp và tạo danh sách đáp án
                s_tap = {latex(expr_sai1) + ' = 0', latex(expr_sai2) + ' = 0', latex(expr_sai3) + ' = 0'}
                # Nếu vô tình trùng đáp án đúng, tạo một cái khác
                if latex(expr_dung) + ' = 0' in s_tap:
                    s_tap.discard(latex(expr_dung) + ' = 0')
                    s_tap.add(latex(b*var_x + a*var_y - (a*b + 1)) + ' = 0')

                list_sai = list(s_tap)
                while len(list_sai) < 3: # Đảm bảo đủ 3 câu sai
                    list_sai.append(latex(var_x + var_y + randint(1, 5)) + ' = 0')

                # Gán các biến đáp án
                da = da_dung_str
                das1 = '$' + list_sai[0] + '$'
                das2 = '$' + list_sai[1] + '$'
                das3 = '$' + list_sai[2] + '$'

                # B2: Viết nội dung câu hỏi (Chi tiết theo mẫu ảnh)
                noidungcauhoi = ('''Trong mặt phẳng $Oxy$ cho điểm $M(%s;%s)$. Gọi $A, B$ là hình chiếu của $M$ lên $Ox, Oy$. Phương trình đường thẳng $AB$ là'''
                                 %(latex(a), latex(b)))

                # Các đáp án trắc nghiệm
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # B2: Nội dung lời giải chi tiết (không viết tắt, giống ảnh mẫu)
                loigiai = ('''Ta có hình chiếu của điểm $M(%s;%s)$ lên $Ox, Oy$ lần lượt là $A(%s;0)$ và $B(0;%s)$.\\\\ Do đó phương trình đường thẳng $AB$ đi qua hai điểm $A, B$ (theo phương trình đường thẳng theo đoạn chắn) là: \\\\
                             $\\frac{x}{%s} + \\frac{y}{%s} = 1 \\Leftrightarrow %s x + %s y - %s = 0$.'''
                           %(latex(a), latex(b), latex(a), latex(b), 
                             latex(a), latex(b), latex(b), latex(a), latex(a*b)))

            # Xuất câu trắc nghiệm (Không dùng tiền tố r ở content)
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 


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


def bt_dang29_p1_b1_c3_hh10(self):
            # Khai báo biến và chọn dạng (Trục Ox hoặc Trục Oy)
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 1: Random tọa độ hai điểm A và B
                xA = randint(-10, 10)
                yA = randint(-10, 10)
                xB = randint(-10, 10)
                yB = randint(-10, 10)

                # Đảm bảo B không trùng với A
                while xA == xB and yA == yB:
                    xB = randint(-10, 10)
                    yB = randint(-10, 10)

                # Bước 2: Tính toán các thông số
                # Vectơ chỉ phương AB = (u1, u2)
                u1 = xB - xA
                u2 = yB - yA

                # Tìm ước chung lớn nhất để tối giản như trong ảnh (ví dụ 4;2 thành 2(2;1))
                common = math.gcd(u1, u2)
                u1_rutgon = u1 // common
                u2_rutgon = u2 // common

                # Vectơ pháp tuyến n = (-u2_rutgon, u1_rutgon)
                nx = -u2_rutgon
                ny = u1_rutgon

                # Đáp án đúng
                kq = '(%s;%s)' % (latex(nx), latex(ny))
                da_dung = '$%s$' % (kq)

                # Tạo các phương án nhiễu (đảm bảo không trùng với đáp án đúng)
                s_set = set()
                # Các trường hợp sai hay gặp:
                potential_wrongs = [
                    (u1_rutgon, u2_rutgon),    # Nhầm với vectơ chỉ phương
                    (-u1_rutgon, -u2_rutgon),  # Vectơ chỉ phương đối
                    (ny, nx),                  # Quên đổi dấu khi hoán vị
                    (-nx, -ny),                # Vectơ pháp tuyến đối (nếu bài toán yêu cầu chính xác n này)
                    (nx, -ny),                 # Sai dấu
                    (-u2_rutgon * 2, u1_rutgon * 2) # Tỉ lệ khác nhưng đề bài ở đây đang chọn dạng tối giản
                ]

                for w_x, w_y in potential_wrongs:
                    wrong_str = '$((%s;%s))$'.replace('((', '(').replace('))', ')') % (latex(w_x), latex(w_y))
                    if wrong_str != da_dung:
                        s_set.add(wrong_str)

                # Nếu chưa đủ 3 phương án sai thì thêm ngẫu nhiên
                while len(s_set) < 3:
                    w_x, w_y = randint(-5, 5), randint(-5, 5)
                    wrong_str = '$(%s;%s)$' % (latex(w_x), latex(w_y))
                    if wrong_str != da_dung:
                        s_set.add(wrong_str)

                s = list(s_set)
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Cho hai điểm $A = (%s;%s)$ và $B = (%s;%s)$. Vectơ pháp tuyến của đường thẳng $AB$ là'''
                                 %(latex(xA), latex(yA), latex(xB), latex(yB)))

                # Các đáp án
                da_d = ('\\True ' + str(da_dung))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết theo mẫu ảnh
                # Ta có AB = (u1; u2) = common(u1_rutgon; u2_rutgon)
                if common != 1:
                    v_ab_str = '(%s;%s) = %s(%s;%s)' % (latex(u1), latex(u2), latex(common), latex(u1_rutgon), latex(u2_rutgon))
                else:
                    v_ab_str = '(%s;%s)' % (latex(u1), latex(u2))

                loigiai=('''Ta có $\\vec{AB} = %s$ suy ra vectơ pháp tuyến của đường thẳng $AB$ là $\\vec{n}_{AB} = (%s;%s)$.'''
                         %(v_ab_str, latex(nx), latex(ny)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 


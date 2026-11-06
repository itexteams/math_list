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


def bt_dang27_p1_b1_c3_hh10(self):
            # Khai báo biến và chọn dạng (Trục Ox hoặc Trục Oy)
            # Khai báo biến và chọn dạng (theo mẫu)
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Suy nghĩ tìm cách random bài toán
                # Tạo tọa độ điểm M(x0, y0) và vectơ chỉ phương u(a, b)
                x0 = randint(-10, 10)
                y0 = randint(-10, 10)
                a = randint(-10, 10)
                while a == 0: a = randint(-1, 10) # Đảm bảo mẫu số khác 0
                b = randint(-10, 10)
                while b == 0: b = randint(-1, 10)

                # Thiết lập hiển thị cho tử số (x - x0) và (y - y0)
                # Ví dụ: x - 2 hoặc x + 3
                tu_x = "x - " + str(x0) if x0 >= 0 else "x + " + str(abs(x0))
                tu_y = "y - " + str(y0) if y0 >= 0 else "y + " + str(abs(y0))

                # Rút gọn chuỗi nếu x0 hoặc y0 bằng 0
                if x0 == 0: tu_x = "x"
                if y0 == 0: tu_y = "y"

                # Đáp án đúng (Dạng hệ phương trình tham số)
                # x = x0 + at
                # y = y0 + bt
                line_x = str(x0) + (" + " + str(a) if a > 0 else " - " + str(abs(a))) + "t"
                line_y = str(y0) + (" + " + str(b) if b > 0 else " - " + str(abs(b))) + "t"

                da_dung = "$\\begin{cases} x = %s \\\\ y = %s \\end{cases}$" % (line_x, line_y)

                # Bước 4: Điều chỉnh các phương án sai (không trùng đáp án đúng)
                s = []
                # Phương án sai 1: Đổi dấu điểm đi qua
                s.append("$\\begin{cases} x = %s \\\\ y = %s \\end{cases}$" % (
                    str(-x0) + (" + " + str(a) if a > 0 else " - " + str(abs(a))) + "t",
                    str(-y0) + (" + " + str(b) if b > 0 else " - " + str(abs(b))) + "t"
                ))
                # Phương án sai 2: Đổi dấu vectơ chỉ phương
                s.append("$\\begin{cases} x = %s \\\\ y = %s \\end{cases}$" % (
                    str(x0) + (" - " + str(a) if a > 0 else " + " + str(abs(a))) + "t",
                    str(y0) + (" - " + str(b) if b > 0 else " + " + str(abs(b))) + "t"
                ))
                # Phương án sai 3: Hoán vị tọa độ và vectơ
                s.append("$\\begin{cases} x = %s \\\\ y = %s \\end{cases}$" % (
                    str(a) + (" + " + str(x0) if x0 > 0 else " - " + str(abs(x0))) + "t",
                    str(b) + (" + " + str(y0) if y0 > 0 else " - " + str(abs(y0))) + "t"
                ))

                # Loại bỏ trùng lặp nếu có và chọn 3 đáp án sai
                s = list(set(s))
                if da_dung in s: s.remove(da_dung)
                while len(s) < 3: # Đề phòng trường hợp hiếm hoi bị trùng
                    s.append("$\\begin{cases} x = %s \\\\ y = %s \\end{cases}$" % (randint(-20,20), randint(-20,20)))

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi (B2: Viết lại y hệt cấu trúc bài toán)
                noidungcauhoi = ("Phương trình tham số của đường thẳng $d: \\frac{%s}{%s} = \\frac{%s}{%s}$ là"
                                 % (tu_x, str(a), tu_y, str(b)))

                # Các đáp án
                da_d = ('\\True ' + str(da_dung))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (B2: Viết chi tiết không viết tắt)
                loigiai = ("Đặt $\\frac{%s}{%s} = \\frac{%s}{%s} = t$ thì $%s = %st, %s = %st$. \\\\ "
                           "Vậy phương trình tham số của $d$ là: "
                           "$\\begin{cases} x = %s \\\\ y = %s \\end{cases}$."
                           % (tu_x, str(a), tu_y, str(b), tu_x, str(a), tu_y, str(b), line_x, line_y))

            # Xuất câu trắc nghiệm (Phần Content không dùng tiền tố r)
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content 


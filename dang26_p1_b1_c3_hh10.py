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


def bt_dang26_p1_b1_c3_hh10(self):
            # Khai báo biến và chọn dạng (Trục Ox hoặc Trục Oy)
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Tạo các hệ số a, b sao cho đường thẳng không quá phức tạp
                # Phương trình có dạng: ax + by + c = 0
                a = randint(1, 6)
                b = randint(1, 6)
                # Để điểm M(0; y0) có tọa độ nguyên, c phải chia hết cho b
                y0 = randint(-5, 5)
                if y0 == 0: y0 = 2 # Tránh trường hợp đi qua gốc tọa độ quá đơn giản
                c = -b * y0

                # Vector pháp tuyến và vector chỉ phương
                # n = (a, b) -> u = (-b, a)
                u1 = -b
                u2 = a

                # Tạo chuỗi phương trình tổng quát để hiển thị
                # Xử lý dấu của c khi viết phương trình
                sign_c = "+" if c >= 0 else ""
                pt_tong_quat = str(a) + "x + " + str(b) + "y " + sign_c + str(c) + " = 0"

                # Đáp án đúng: x = u1*t, y = y0 + u2*t
                # Định dạng hệ phương trình trong LaTeX
                def format_ptts(x0, y0, u1, u2):
                    # Hàm bổ trợ để viết pt tham số đẹp hơn
                    x_part = str(u1) + "t" if u1 != 1 else "t"
                    if u1 == -1: x_part = "-t"

                    y_const = str(y0) if y0 != 0 else ""
                    y_u = ""
                    if u2 > 0:
                        y_u = (" + " if y0 != 0 else "") + (str(u2) if u2 != 1 else "") + "t"
                    else:
                        y_u = (" - " if y0 != 0 else "-") + (str(abs(u2)) if abs(u2) != 1 else "") + "t"

                    return "\\begin{cases} x = " + x_part + " \\\\ y = " + y_const + y_u + " \\end{cases}"

                da_dung_str = format_ptts(0, y0, u1, u2)

                # Các phương án sai (thay đổi vector hoặc điểm)
                s = [
                    format_ptts(0, y0, a, b),           # Nhầm VTCP thành VTPT
                    format_ptts(y0, 0, u1, u2),         # Lộn tọa độ điểm M
                    format_ptts(0, -y0, u1, u2),        # Sai dấu tung độ điểm
                    format_ptts(0, y0, -u1, -u2),       # VTCP cùng phương (thực tế vẫn đúng nhưng ta đổi để tạo nhiễu)
                    format_ptts(0, y0, b, a),           # Sai vector
                ]

                # Lọc bỏ phương án sai nếu vô tình trùng đáp án đúng
                s = [item for item in s if item != da_dung_str]
                random.shuffle(s)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ("Phương trình tham số của đường thẳng $d: %s$ là" % (pt_tong_quat))

                # Các đáp án
                da_d = ("\\True $" + da_dung_str + "$")
                da_s1 = "$" + das1 + "$"
                da_s2 = "$" + das2 + "$" 
                da_s3 = "$" + das3 + "$" 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết theo ảnh
                loigiai = ("$d: %s$ có VTPT $\\vec{n} = (%s;%s) \\Rightarrow$ VTCP $\\vec{u} = (%s;%s)$. \\\\ "
                           "Cho $x = 0$ thì $y = %s$ nên $d$ đi qua điểm $M(0;%s)$. \\\\ "
                           "Vậy phương trình tham số của $d$ là: $%s$."
                           %(pt_tong_quat, a, b, u1, u2, y0, y0, da_dung_str))

            # Xuất câu trắc nghiệm
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


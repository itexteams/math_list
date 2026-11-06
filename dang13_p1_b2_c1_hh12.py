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


def bt_dang13_p1_b2_c1_hh12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random tọa độ vector a
                x_val = random.randint(-4, 4)
                y_val = random.randint(-4, 4)
                z_val = random.randint(-4, 4)

                # Đảm bảo vector a không phải là vector không
                while x_val == 0 and y_val == 0 and z_val == 0:
                    x_val = random.randint(-4, 4)

                # Random hệ số k
                k = random.choice([-3, -2, 2, 3, 4, 5])

                # Tính tọa độ vector k*a (Kết quả đúng)
                kx = k * x_val
                ky = k * y_val
                kz = k * z_val

                # Hàm tạo chuỗi tọa độ hiển thị
                def format_vec(a, b, c):
                    return '(%s; %s; %s)' % (a, b, c)

                # Hàm xử lý đóng ngoặc nếu là số âm trong phép nhân
                def format_mul(num):
                    if num < 0:
                        return '(%s)' % num
                    return str(num)

                vec_a_str = format_vec(x_val, y_val, z_val)
                vec_kq_str = format_vec(kx, ky, kz)

                # Thuật toán tạo các phương án nhiễu sai (không được trùng với đáp án đúng)
                wrong_set = set()
                while len(wrong_set) < 3:
                    # Các kiểu nhiễu phổ biến học sinh hay sai
                    w1 = (-kx, ky, kz) # Sai dấu hoành độ
                    w2 = (kx, -ky, kz) # Sai dấu tung độ
                    w3 = (kx, ky, -kz) # Sai dấu cao độ
                    w4 = (-kx, -ky, -kz) # Nhân sai dấu toàn bộ
                    w5 = (kx + random.choice([-2, -1, 1, 2]), ky, kz + random.choice([-2, -1, 1, 2])) # Sai số do tính toán

                    # Thêm ngẫu nhiên các phương án trên vào set để đảm bảo tính duy nhất
                    for w in [w1, w2, w3, w4, w5]:
                        if w != (kx, ky, kz):
                            wrong_set.add(w)

                wrong_list = list(wrong_set)
                # Lấy 3 phương án sai (đã đảm bảo tính duy nhất)
                w_ans1 = format_vec(wrong_list[0][0], wrong_list[0][1], wrong_list[0][2])
                w_ans2 = format_vec(wrong_list[1][0], wrong_list[1][1], wrong_list[1][2])
                w_ans3 = format_vec(wrong_list[2][0], wrong_list[2][1], wrong_list[2][2])

                # Các đáp án trắc nghiệm
                da = '$%s\\vec{a}=%s$' % (k, vec_kq_str)
                das1 = '$%s\\vec{a}=%s$' % (k, w_ans1)
                das2 = '$%s\\vec{a}=%s$' % (k, w_ans2)
                das3 = '$%s\\vec{a}=%s$' % (k, w_ans3)

                # Câu hỏi
                noidungcauhoi = ('''Trong không gian $Oxyz$, cho vectơ $\\vec{a} = %s$. Mệnh đề nào dưới đây đúng?'''
                                 % (vec_a_str))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = ('''Ta có: $%s\\vec{a} = %s\\left(%s; %s; %s\\right) = \\left(%s \\cdot %s; %s \\cdot %s; %s \\cdot %s\\right) = %s$.'''
                           % (k, k, x_val, y_val, z_val, k, format_mul(x_val), k, format_mul(y_val), k, format_mul(z_val), vec_kq_str))


            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


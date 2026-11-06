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


def bt_dang22_p1_b1_c6_ds10(self):
            # Khai báo biến
            # Khai báo biến loại bài tập
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B3: Suy nghĩ tìm cách random bài toán
                # N là tổng số quân bài (thường là 52, có thể random từ 30 đến 52)
                N = random.randint(30, 52)
                # k là số quân bài rút ra (random từ 2 đến 5)
                k = random.randint(2, 5)

                # Tính toán kết quả n(Omega) = C(N, k)
                def combination(n, r):
                    return math.comb(n, r)

                def permutation(n, r):
                    return math.perm(n, r)

                kq_num = combination(N, k)
                kq = str(kq_num).replace('.', ',') # Quy đổi dấu chấm thành phẩy cho số thập phân (nếu có)

                # Đáp án đúng
                da = '$%s$' % (kq)

                # B4: Tạo các phương án sai không trùng với đáp án đúng
                s = []
                # Phương án sai 1: Chỉnh hợp A(N, k)
                val_s1 = permutation(N, k)
                if val_s1 != kq_num:
                    s.append('$%s$' % (str(val_s1)))

                # Phương án sai 2: Lấy N^k (chọn có hoàn lại)
                val_s2 = N**k
                if val_s2 != kq_num:
                    s.append('$%s$' % (str(val_s2)))

                # Phương án sai 3: Lấy N * k
                val_s3 = N * k
                if val_s3 != kq_num:
                    s.append('$%s$' % (str(val_s3)))

                # Phương án sai 4: C(N, k-1)
                val_s4 = combination(N, k-1)
                if val_s4 != kq_num:
                    s.append('$%s$' % (str(val_s4)))

                # Đảm bảo đủ phương án sai
                while len(s) < 3:
                    fake_val = kq_num + random.randint(10, 1000)
                    s.append('$%s$' % (str(fake_val)))

                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # B2: Viết lại nội dung câu hỏi
                # Thay ( ) bằng \left( \right)
                noidungcauhoi = ('''Rút ngẫu nhiên cùng lúc $%s$ con bài từ cỗ bài tú lơ khơ $%s$ con thì $n\\left(\\Omega\\right)$ bằng bao nhiêu?'''
                                 % (latex(k), latex(N)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết (không viết tắt)
                # n(Omega) = C_N^k
                loigiai = ('''Mỗi cách rút ngẫu nhiên cùng lúc $%s$ con bài từ cỗ bài tú lơ khơ $%s$ con là một tổ hợp chập $%s$ của $%s$ phần tử.\\\\
                             Ta có $n\\left(\\Omega\\right) = C_{%s}^{%s} = %s$.'''
                           % (latex(k), latex(N), latex(k), latex(N), latex(N), latex(k), latex(kq_num)))

            # B2: Xuất câu trắc nghiệm theo mẫu content
            # Không dùng tiền tố r (raw string), thay ( ) bằng \left( \right)
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + 
                '\n\\choice \n'
                '{' + str(list_1[0]) + '}\n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 


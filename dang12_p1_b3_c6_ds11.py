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


def bt_dang12_p1_b3_c6_ds11(self):
            # Khai báo biến
            # B1 & B3: Nghiên cứu đề bài và thiết lập thông số random
            # n: tổng số chìa khóa
            # k: số chìa khóa mở được cửa
            # m: lần mở được cửa (trong ảnh là lần thứ 3)

            n = randint(8, 12) 
            k = randint(2, 3)
            m = 3 # Cố định lần thứ 3 như đề bài hoặc có thể random randint(2, 4)

            # Tính toán các thành phần xác suất theo logic hình ảnh
            # Lần 1 không mở được: (n-k)/n
            p1 = Rational(n - k, n)
            # Lần 2 không mở được: (n-k-1)/(n-1)
            p2 = Rational(n - k - 1, n - 1)
            # Lần 3 mở được: k/(n-2)
            p3 = Rational(k, n - 2)

            # Đáp án đúng
            kq = p1 * p2 * p3

            # B4: Tạo các phương án sai không trùng với đáp án đúng
            def generate_distractors(correct_val, n, k):
                s = set()
                # Sai lầm 1: Tính theo xác suất có hoàn lại
                sai1 = Rational((n - k)**2 * k, n**3)
                # Sai lầm 2: Chỉ lấy k/n
                sai2 = Rational(k, n)
                # Sai lầm 3: Quên trừ số lượng chìa sau mỗi lần thử
                sai3 = Rational((n - k) * (n - k) * k, n * (n - 1) * (n - 2))
                # Sai lầm 4: Một phân số ngẫu nhiên
                sai4 = Rational(k, n - 1)

                candidates = [sai1, sai2, sai3, sai4]
                for c in candidates:
                    if c != correct_val:
                        s.add('$%s$' % latex(c))

                # Nếu chưa đủ 3 đáp án sai thì tạo thêm
                while len(s) < 3:
                    fake = Rational(randint(1, 5), randint(10, 50))
                    if fake != correct_val:
                        s.add('$%s$' % latex(fake))
                return list(s)[:3]

            distractors = generate_distractors(kq, n, k)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một người có một chùm chìa khóa gồm $%s$ chiếc, bề ngoài của chúng giống hệt nhau và chỉ có đúng $%s$ chiếc mở được cửa nhà. Người đó thử ngẫu nhiên từng chìa. Xác suất để mở được cửa trong lần mở thứ ba là'''
                             % (latex(n), latex(k)))

            # Các đáp án
            da_d = '\\True $%s$' % latex(kq)
            da_s1 = distractors[0]
            da_s2 = distractors[1]
            da_s3 = distractors[2]

            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Lời giải chi tiết theo mẫu trong ảnh
            loigiai = ('''Để mở được cửa trong lần mở thứ 3 thì lần thứ nhất và lần thứ hai không mở được và lần thứ 3 mở được. \\\\
            Xác suất để lần thứ nhất không mở được là $\\frac{%s}{%s} = %s$. \\\\
            Xác suất lần thứ 2 không mở được là $\\frac{%s}{%s} = %s$. \\\\
            Xác suất lần thứ 3 mở được là $\\frac{%s}{%s}$. \\\\
            Vì ba lần mở cửa độc lập với nhau nên xác suất để mở được cửa trong lần mở thứ 3 là \\\\
            $%s \\cdot %s \\cdot %s = %s$.'''
                       % (latex(n - k), latex(n), latex(p1),
                          latex(n - k - 1), latex(n - 1), latex(p2),
                          latex(k), latex(n - 2),
                          latex(p1), latex(p2), latex(p3), latex(kq)))

            # B2: Xuất câu trắc nghiệm theo mẫu content
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


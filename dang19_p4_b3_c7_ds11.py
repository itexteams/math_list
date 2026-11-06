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


def bt_dang19_p4_b3_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Random bài toán - Chọn ngẫu nhiên giữa sin^2(x) và cos^2(x)
                kieu_ham = random.choice(['sin', 'cos'])

                if kieu_ham == 'sin':
                    f = sin(x)**2
                    ten_ham = "\\sin^2 x"
                else:
                    f = cos(x)**2
                    ten_ham = "\\cos^2 x"

                # Tính đạo hàm cấp 1 và cấp 2
                f_prime = diff(f, x)
                f_double_prime = diff(f, x, 2)

                # Rút gọn để hiển thị giống mẫu (2sinxcosx -> sin2x)
                f_prime_simp = sp.simplify(f_prime)
                f_double_prime_simp = sp.simplify(f_double_prime)

                # Kết quả đúng (y'')
                kq_dung = '$%s$' % latex(f_double_prime_simp)

                # Tạo các đáp án nhiễu (sai dấu hoặc sai hàm)
                distractors = [
                    '$%s$' % latex(-f_double_prime_simp),
                    '$%s$' % latex(diff(f_prime_simp, x) * 0.5), # Sai hệ số
                    '$%s$' % latex(f_prime_simp),               # Quên đạo hàm tiếp
                    '$2\\sin 2x$',
                    '$-2\\sin 2x$',
                    '$%s$' % latex(sp.simplify(diff(f, x, 3)))  # Đạo hàm cấp 3
                ]

                # Lấy ngẫu nhiên 3 đáp án sai từ danh sách nhiễu
                random.shuffle(distractors)
                da_s = []
                for d in distractors:
                    if d != kq_dung and d not in da_s:
                        da_s.append(d)
                    if len(da_s) == 3:
                        break

                # Câu hỏi
                noidungcauhoi = ('''Tính đạo hàm cấp $2$ của hàm số $y = %s$.''' % ten_ham)

                # Các đáp án
                da_d = ('\\True ' + str(kq_dung))
                da_s1 = str(da_s[0])
                da_s2 = str(da_s[1])
                da_s3 = str(da_s[2])

                # Trộn thứ tự đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (trình bày chi tiết như ảnh mẫu)
                # y' của sin^2x = 2sinxcosx = sin2x; y'' = 2cos2x
                # y' của cos^2x = -2cosxsinx = -sin2x; y'' = -2cos2x
                buoc_trung_gian = latex(f_prime).replace(' ', '')
                loigiai = ('''Tập xác định: $\\mathscr{D} = \\mathbb{R}$. \\\\
                             Đạo hàm cấp 1: $y\' = %s = %s$. \\\\
                             Đạo hàm cấp 2: $y\'\' = (%s)\' = %s$.''' 
                           % (latex(f_prime), latex(f_prime_simp), latex(f_prime_simp), latex(f_double_prime_simp)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


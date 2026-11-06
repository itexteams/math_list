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


def bt_dang23_p1_b4_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bài toán gốc: 3*sin(2x) - m^2 + 5 = 0  <=>  sin(2x) = (m^2 - 5)/3
                # Dạng tổng quát: A*sin(2x) - m^2 + B = 0  <=>  sin(2x) = (m^2 - B)/A (với A > 0)
                A = randint(2, 5)
                B = randint(3, 7)

                # Giải tìm số giá trị nguyên của m để phương trình có nghiệm
                # Điều kiện có nghiệm: -1 <= (m^2 - B)/A <= 1 
                # <=> -A <= m^2 - B <= A  <=>  B - A <= m^2 <= B + A
                min_m2 = B - A
                max_m2 = B + A

                # Đếm số lượng m nguyên
                count_m = 0
                m_values = []

                # Xác định tập nghiệm m nguyên bằng cách duyệt qua khoảng thực tế
                lower_bound = 0 if min_m2 < 0 else math.ceil(math.sqrt(min_m2))
                upper_bound = math.floor(math.sqrt(max_m2))

                # Thêm các nghiệm dương và âm tương ứng
                for val in range(lower_bound, upper_bound + 1):
                    if min_m2 <= val**2 <= max_m2:
                        if val == 0:
                            m_values.append(0)
                        else:
                            m_values.append(val)
                            m_values.append(-val)

                count_m = len(set(m_values))

                # Đáp án đúng
                da = '$%s$' % count_m

                # Tạo các phương án sai ngẫu nhiên không trùng với đáp án đúng
                s = set()
                while len(s) < 3:
                    sai = randint(0, count_m + 6)
                    if sai != count_m:
                        s.add('$%s$' % sai)

                s = list(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Tạo chuỗi LaTeX cho điều kiện m^2 để đưa vào lời giải
                if min_m2 <= 0:
                    b2_m2 = '[0;%s]' % max_m2
                else:
                    b2_m2 = '[%s;%s]' % (min_m2, max_m2)

                # Chuỗi LaTeX cho khoảng của m khi lấy căn bậc hai
                if min_m2 > 0:
                    sqrt_min = latex(sqrt(min_m2))
                    sqrt_max = latex(sqrt(max_m2))
                    chuoi_m_range = '\\left[ \\begin{aligned} & -%s \\le m \\le -%s \\\\ & %s \\le m \\le %s \\end{aligned} \\right.' % (sqrt_max, sqrt_min, sqrt_min, sqrt_max)
                else:
                    sqrt_max = latex(sqrt(max_m2))
                    chuoi_m_range = '-%s \\le m \\le %s' % (sqrt_max, sqrt_max)

                # Câu hỏi
                noidungcauhoi = ('''Có bao nhiêu giá trị nguyên của tham số $m$ để phương trình $%s\\sin 2x - m^2 + %s = 0$ có nghiệm?'''
                                 % (latex(A), latex(B)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = ('''Phương trình đã cho tương đương với phương trình $\\sin 2x = \\frac{m^2 - %s}{%s}$ \\\\
            Vì $\\sin 2x \\in [-1;1]$ nên $\\frac{m^2 - %s}{%s} \\in [-1;1] \\Leftrightarrow m^2 \\in %s \\Leftrightarrow %s$ \\\\
            Vậy có %s giá trị nguyên của $m$ thỏa mãn.'''
                           % (latex(B), latex(A), latex(B), latex(A), b2_m2, chuoi_m_range, count_m))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '{' + str(list_1[0]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content


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


def bt_dang42_p1_b2_c4_ds11(self):
            # Khai báo biến
            # Khai báo biến ký hiệu cho Sympy
            x = symbols('x')
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # --- Bước 1: Random các thông số ---
                # a là điểm giới hạn (ví dụ từ 2 đến 6)
                a = random.randint(2, 6)
                # b là nghiệm còn lại của mẫu số (khác a để tránh nghiệm kép khó rút gọn)
                b = random.choice([i for i in range(-3, 7) if i != a])
                # k là hệ số trong trị tuyệt đối (ví dụ từ 2 đến 5)
                k = random.randint(2, 5)

                # --- Bước 2: Tạo các biểu thức ---
                # Tử số có dạng |ka - kx|
                bieu_thuc_trong_tri = k*a - k*x
                tu_so = Abs(bieu_thuc_trong_tri)

                # Mẫu số có dạng (x-a)(x-b)
                mau_so_don_gian = (x - a) * (x - b)
                mau_so = expand(mau_so_don_gian)

                # --- Bước 3: Tính toán kết quả ---
                # Khi x -> a+, x > a nên a - x < 0. 
                # Do đó |k(a - x)| = -k(a - x) = k(x - a)
                # Giới hạn trở thành: lim [k(x-a)] / [(x-a)(x-b)] = k / (a-b)
                kq_limit = Rational(k, a - b)

                # --- Bước 4: Tạo bộ đáp án ---
                da_dung = '$%s$' % latex(kq_limit)

                # Tạo danh sách đáp án nhiễu
                s = [
                    '$%s$' % latex(-kq_limit),               # Ngược dấu
                    '$%s$' % latex(Rational(1, k)),          # Nghịch đảo
                    '$%s$' % latex(kq_limit + 1),            # Sai lệch
                    '$0$',                                   # Đáp án phổ biến
                    '$\\infty$',                             # Đáp án vô cực
                    '$%s$' % latex(Rational(k, a + b if a+b != 0 else 1)) # Tính sai dấu mẫu
                ]

                # Loại bỏ đáp án đúng nếu lỡ trùng trong danh sách nhiễu
                s = [i for i in s if i != da_dung]
                random.shuffle(s)
                das1, das2, das3 = s[:3]

                # --- Bước 5: Soạn nội dung câu hỏi và lời giải ---
                noidungcauhoi = (r'Giới hạn $\displaystyle \lim_{x \to %s^+} \frac{%s}{%s}$ bằng' 
                                 % (latex(a), latex(tu_so), latex(mau_so)))

                # Giải thích phá trị tuyệt đối
                tu_pha_tri = k*x - k*a
                tu_rut_gon = k * (x - a)

                loigiai = (r'Ta có $\displaystyle \lim_{x \to %s^+} \frac{|%s|}{%s} = \lim_{x \to %s^+} \frac{%s}{%s}$ '
                           r'\\ $= \displaystyle \lim_{x \to %s^+} \frac{%s}{(x - %s)(x - %s)} = \lim_{x \to %s^+} \frac{%s}{x - %s} = %s$.'
                           %(latex(a), latex(bieu_thuc_trong_tri), latex(mau_so), 
                             latex(a), latex(tu_pha_tri), latex(mau_so),
                             latex(a), latex(tu_rut_gon), latex(a), latex(b),
                             latex(a), latex(k), latex(b), latex(kq_limit)))

                # --- Bước 6: Đóng gói ---
                da_d = '\\True ' + str(da_dung)
                list_1 = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)

            # --- Bước 7: Xuất kết quả (Đã sửa list_all thành list_1) ---
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


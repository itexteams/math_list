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


def bt_dang4_p2_b2_c6_ds10(self):
            # Khai báo biến
            # Ngẫu nhiên số học sinh của lớp (từ 35 đến 45)
            n = random.randint(35, 45)
            # Ngẫu nhiên số học sinh trong nhóm siêu quậy (từ 3 đến 5)
            k = random.randint(3, 5)

            # Danh sách tên để chọn ngẫu nhiên
            danh_sach_ten = ["Việt", "Đức", "Cường", "Thịnh", "An", "Bình", "Tuấn", "Nam", "Hoàng", "Long"]
            nhom_quay = random.sample(danh_sach_ten, k)
            # Tạo chuỗi tên: A, B, C và D
            ten_nhom_str = ", ".join(nhom_quay[:-1]) + " và " + nhom_quay[-1]

            # Tính toán các giá trị không gian mẫu và biến cố (nCr = n! / (r!(n-r)!))
            tong_cach_chon = n * (n - 1) // 2  # nC2
            n_ngoai_nhom = n - k
            cach_chon_0_quay = n_ngoai_nhom * (n_ngoai_nhom - 1) // 2 # (n-k)C2
            cach_chon_1_quay = k * n_ngoai_nhom # kC1 * (n-k)C1
            cach_chon_2_quay = k * (k - 1) // 2 # kC2

            # Tính xác suất dưới dạng phân số tối giản
            xs_0_quay = frac(cach_chon_0_quay, tong_cach_chon)
            xs_1_quay = frac(cach_chon_1_quay, tong_cach_chon)
            xs_2_quay = frac(cach_chon_2_quay, tong_cach_chon)

            # Nội dung câu hỏi
            noidungcauhoi = ("Lớp 10B có %s học sinh, trong đó có nhóm siêu quậy gồm %s. Cô giáo gọi ngẫu nhiên 2 bạn trong lớp để kiểm tra bài cũ." 
                             % (n, ten_nhom_str))

            # ========================== THIẾT LẬP CÁC MỆNH ĐỀ ==========================

            # --- Mệnh đề (a): Nhận biết ---
            da_a_d = "\\True Số cách chọn ra 2 bạn trong %s bạn lớp 10B là: %s (cách)" % (n, tong_cach_chon)
            da_a_s = "Số cách chọn ra 2 bạn trong %s bạn lớp 10B là: %s (cách)" % (n, tong_cach_chon + 10)
            list_da_a = [da_a_d, da_a_s]
            loigiai_a = "Số phần tử của không gian mẫu là $n\\left(\\Omega\\right) = C_{%s}^2 = %s$." % (n, tong_cach_chon)

            # --- Mệnh đề (b): Thông hiểu ---
            da_b_d = "\\True Xác suất của biến cố \"Không bạn nào trong nhóm siêu quậy được gọi\" bằng $\\frac{%s}{%s}$" % (xs_0_quay.numerator, xs_0_quay.denominator)
            da_b_s = "Xác suất của biến cố \"Không bạn nào trong nhóm siêu quậy được gọi\" bằng $\\frac{%s}{%s}$" % (xs_0_quay.numerator + 1, xs_0_quay.denominator)
            list_da_b = [da_b_d, da_b_s]
            loigiai_b = ("Số cách chọn 2 bạn không nằm trong nhóm siêu quậy (chọn từ %s bạn còn lại) là: $C_{%s}^2 = %s$. "
                         "Xác suất là $P = \\frac{%s}{%s} = \\frac{%s}{%s}$." 
                         % (n_ngoai_nhom, n_ngoai_nhom, cach_chon_0_quay, cach_chon_0_quay, tong_cach_chon, xs_0_quay.numerator, xs_0_quay.denominator))

            # --- Mệnh đề (c): Vận dụng ---
            da_c_d = "\\True Xác suất của biến cố \"Một bạn trong nhóm siêu quậy được gọi\" bằng: $\\frac{%s}{%s}$" % (xs_1_quay.numerator, xs_1_quay.denominator)
            da_c_s = "Xác suất của biến cố \"Một bạn trong nhóm siêu quậy được gọi\" bằng: $\\frac{%s}{%s}$" % (xs_1_quay.numerator, xs_1_quay.denominator + 5)
            list_da_c = [da_c_d, da_c_s]
            loigiai_c = ("Số cách chọn 1 bạn trong nhóm siêu quậy và 1 bạn ngoài nhóm là: $C_{%s}^1 \\cdot C_{%s}^1 = %s \\cdot %s = %s$. "
                         "Xác suất là $P = \\frac{%s}{%s} = \\frac{%s}{%s}$." 
                         % (k, n_ngoai_nhom, k, n_ngoai_nhom, cach_chon_1_quay, cach_chon_1_quay, tong_cach_chon, xs_1_quay.numerator, xs_1_quay.denominator))

            # --- Mệnh đề (d): Vận dụng cao ---
            da_d_d = "\\True Xác suất của biến cố \"Cả hai bạn được gọi đều trong nhóm siêu quậy\" bằng: $\\frac{%s}{%s}$" % (xs_2_quay.numerator, xs_2_quay.denominator)
            da_d_s = "Xác suất của biến cố \"Cả hai bạn được gọi đều trong nhóm siêu quậy\" bằng: $\\frac{%s}{%s}$" % (xs_2_quay.numerator + 1, xs_2_quay.denominator)
            list_da_d = [da_d_d, da_d_s]
            loigiai_d = ("Số cách chọn 2 bạn đều trong nhóm siêu quậy là: $C_{%s}^2 = %s$. "
                         "Xác suất là $P = \\frac{%s}{%s} = \\frac{%s}{%s}$." 
                         % (k, cach_chon_2_quay, cach_chon_2_quay, tong_cach_chon, xs_2_quay.numerator, xs_2_quay.denominator))

            # ========================== TRỘN VÀ XUẤT FILE ==========================

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                chon_a = random.choice(list_da_a)
                chon_b = random.choice(list_da_b)
                chon_c = random.choice(list_da_c)
                chon_d = random.choice(list_da_d)
                if 1 <= count_true_answers([chon_a, chon_b, chon_c, chon_d]) <= 3:
                    break

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(chon_a) + '}\n'
                '{' + str(chon_b) + '}\n'
                '{' + str(chon_c) + '}\n'
                '{' + str(chon_d) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_a) + '\n'
                '\\item ' + str(loigiai_b) + '\n'
                '\\item ' + str(loigiai_c) + '\n'
                '\\item ' + str(loigiai_d) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


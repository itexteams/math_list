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


def bt_dang6_p2_b1_c4_ds11(self):
            # Khai báo biến
            # Khai báo biến ngẫu nhiên cho bài toán
            # D: Liều lượng thuốc hàng ngày (mg)
            # p: Tỉ lệ tồn dư (%)
            D = random.choice([50, 100, 150, 200, 250,300,350])
            p = random.choice([2, 4, 5, 8, 10])
            r_val = Rational(p, 100) # Tỉ lệ r = p/100

            # Hàm hỗ trợ định dạng số thập phân dùng dấu phẩy và xử lý số nguyên
            def format_vn(value, precision=4):
                val = round(float(value), precision)
                # Nếu giá trị là số nguyên (phần thập phân bằng 0)
                if val.is_integer():
                    return str(int(val))
                # Nếu có phần thập phân, đổi dấu chấm thành dấu phẩy
                return str(val).replace('.', ',')

            # Tính toán các giá trị cơ bản
            val_a = format_vn(D * r_val)
            val_b = format_vn(D + D * r_val)
            val_c = format_vn(D * (1 + r_val + r_val**2 + r_val**3))
            val_d = format_vn(D / (1 - r_val), 3)

            # Nội dung câu hỏi
            noidungcauhoi = (r'''Một bệnh nhân hàng ngày phải uống một viên thuốc $%s\,mg$. Sau ngày đầu, trước mỗi lần uống, hàm lượng thuốc cũ trong cơ thể vẫn còn tồn dư $%s\%%$.''' 
                             %(latex(D), latex(p)))

            ########################################################################
            # Nhận biết
            ########################################################################
            nb_da_1_d = r'\True Ngay trước khi uống viên thuốc ngày thứ 2, hàm lượng thuốc trong cơ thể là $%s\,mg$' % val_a
            nb_da_1_s = r'Ngay trước khi uống viên thuốc ngày thứ 2, hàm lượng thuốc trong cơ thể là $%s\,mg$' % format_vn(D + 5.5)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = (r'''Ngay trước khi uống viên thuốc ngày thứ 2: \\ Hàm lượng thuốc trong cơ thể là $%s \cdot %s\%% = %s\,mg$.''' 
                            %(latex(D), latex(p), val_a))

            ########################################################################
            # Thông hiểu
            ########################################################################
            th_da_1_d = r'\True Ngay sau khi uống viên thuốc ngày thứ 2, hàm lượng thuốc trong cơ thể là $%s\,mg$' % val_b
            th_da_1_s = r'Ngay sau khi uống viên thuốc ngày thứ 2, hàm lượng thuốc trong cơ thể là $%s\,mg$' % format_vn(D + 10)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = (r'''Ngay sau khi uống viên thuốc ngày thứ 2: \\ Hàm lượng thuốc trong cơ thể là $%s + %s = %s\,mg$.''' 
                            %(latex(D), val_a, val_b))

            ########################################################################
            # Vận dụng
            ########################################################################
            vd_da_1_d = r'\True Sau khi uống viên thuốc ngày thứ 4, hàm lượng thuốc trong cơ thể là $u_4 \approx %s\,mg$' % val_c
            vd_da_1_s = r'Sau khi uống viên thuốc ngày thứ 4, hàm lượng thuốc trong cơ thể là $u_4 \approx %s\,mg$' % format_vn(D*4)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = (r'''Gọi $u_n$ là hàm lượng thuốc sau khi uống ngày thứ $n$. Ta có $u_1 = %s$; $u_2 = %s \cdot \frac{1}{%s} + %s$. \\
                            Tổng quát $u_n = %s \cdot \frac{1-r^n}{1-r}$ với $r = \frac{1}{%s}$. \\
                            Với $n=4$, $u_4 = %s \left( 1 + \frac{1}{%s} + \left(\frac{1}{%s}\right)^2 + \left(\frac{1}{%s}\right)^3 \right) \approx %s\,mg$.''' 
                            %(latex(D), latex(D), latex(int(1/r_val)), latex(D), latex(D), latex(int(1/r_val)), latex(D), latex(int(1/r_val)), latex(int(1/r_val)), latex(int(1/r_val)), val_c))

            ########################################################################
            # Vận dụng cao
            ########################################################################
            vdc_da_1_d = r'\True Nếu sử dụng thuốc lâu ngày thì hàm lượng thuốc trong cơ thể hằng ngày xấp xỉ $%s\,mg$' % val_d
            vdc_da_1_s = r'Nếu sử dụng thuốc lâu ngày thì hàm lượng thuốc trong cơ thể hằng ngày xấp xỉ $%s\,mg$' % format_vn(D*2)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = (r'''Khi sử dụng lâu ngày ($n \to \infty$), hàm lượng thuốc là: \\
                            $\lim_{n \to \infty} u_n = \lim_{n \to \infty} %s \cdot \frac{1-r^n}{1-r} = \frac{%s}{1-r} = \frac{%s}{1-\frac{1}{%s}} \approx %s\,mg$.''' 
                            %(latex(D), latex(D), latex(D), latex(int(1/r_val)), val_d))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                ans_nb = random.choice(list_nb_da_1)
                ans_th = random.choice(list_th_da_1)
                ans_vd = random.choice(list_vd_da_1)
                ans_vdc = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([ans_nb, ans_th, ans_vd, ans_vdc]) <= 3:
                    break

            shuffled_answers = [ans_nb, ans_th, ans_vd, ans_vdc]
            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(shuffled_answers[0]) + '}\n'
                '{' + str(shuffled_answers[1]) + '}\n'
                '{' + str(shuffled_answers[2]) + '}\n'
                '{' + str(shuffled_answers[3]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(shuffled_solutions[0]) + '\n'
                '\\item ' + str(shuffled_solutions[1]) + '\n'
                '\\item ' + str(shuffled_solutions[2]) + '\n'
                '\\item ' + str(shuffled_solutions[3]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


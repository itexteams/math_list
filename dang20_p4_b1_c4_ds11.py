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


def bt_dang20_p4_b1_c4_ds11(self):
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':


                k = randint(2, 5)  # Khoảng cách giữa 2 thừa số mẫu (VD: 2, 3, 4, 5)
                a = randint(1, 4)  # Thừa số đầu tiên của số hạng đầu (VD: 1, 2, 3...)

                term1_1 = a
                term1_2 = a + k

                # Số hạng 2: 1 / ((a+k) * (a+2k))
                term2_1 = a + k
                term2_2 = a + 2 * k

                c1 = a - k # Hằng số của thừa số 1
                c2 = a     # Hằng số của thừa số 2

                # Hàm hỗ trợ định dạng hiển thị (kn + b) đẹp mắt (xử lý dấu cộng/trừ)
                def format_poly(h, c):
                    if c > 0:
                        return f"{h}n+{c}"
                    elif c < 0:
                        return f"{h}n-{abs(c)}"
                    else:
                        return f"{h}n"

                str_n_1 = format_poly(k, c1) # Biểu thức (kn + ...) thứ nhất
                str_n_2 = format_poly(k, c2) # Biểu thức (kn + ...) thứ hai


                val_k = Rational(1, k)      # Phân số 1/k
                val_a = Rational(1, a)      # Phân số 1/a
                kq_chuan = Rational(1, k*a) # Kết quả đúng
                h1=kq_chuan
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq1=str(kq).replace('.', ',')

                # Tạo đáp án sai (Nhiễu)
                # Nhiễu 1: Quên nhân 1/k -> ra 1/a
                f1 = Rational(1, a)
                # Nhiễu 2: Quên số hạng đầu a -> ra 1/k
                f2 = Rational(1, k)
                # Nhiễu 3: Sai mẫu số một chút
                f3 = Rational(1, k*a + k)
                # Nhiễu 4: Biến thể khác
                f4 = Rational(1, k*a*2)

                # Tập hợp các đáp án
                list_dapan = [kq_chuan, f1, f2, f3, f4]
                # Loại bỏ trùng lặp và giữ lại kq_chuan
                list_dapan = sorted(list(set(list_dapan)), key=lambda x: random.random())

                # Lấy ra các đáp án sai để hiển thị
                wrong_answers = []
                for x in list_dapan:
                    if x != kq_chuan:
                        wrong_answers.append(x)

                # Đảm bảo đủ 3 đáp án sai
                while len(wrong_answers) < 3:
                    wrong_answers.append(Rational(1, k*a + randint(1,10)))

                # Gán vào biến hiển thị
                da = '$%s$' % latex(kq_chuan)        # Đáp án đúng
                das1 = '$%s$' % latex(wrong_answers[0]) # Sai 1
                das2 = '$%s$' % latex(wrong_answers[1]) # Sai 2
                das3 = '$%s$' % latex(wrong_answers[2]) # Sai 3

                # --- BƯỚC 3: TẠO NỘI DUNG LỜI GIẢI VÀ CÂU HỎI ---

                # Nội dung câu hỏi
                noidungcauhoi = (
                    'Cho dãy số $(u_n)$ với $u_n = \\frac{1}{%s.%s} + \\frac{1}{%s.%s} + ... + \\frac{1}{(%s).(%s)}$. '
                    'Tính giới hạn của dãy số.' 
                    % (term1_1, term1_2, term2_1, term2_2, str_n_1, str_n_2)
                )

                # Chuẩn bị lời giải chi tiết
                phan_so_tach = latex(val_k)
                phan_so_dau = latex(val_a)

                # Logic lời giải:
                # Bước 1: Tách 1/(AB) = 1/k * (1/A - 1/B)
                # Bước 2: Rút gọn dãy
                # Bước 3: Tính lim

                loigiai = (
                    'Ta có: $u_n = \\frac{1}{%s.%s} + \\frac{1}{%s.%s} + ... + \\frac{1}{(%s).(%s)}$ \\\\\n'
                    '$= %s \\left( \\frac{1}{%s} - \\frac{1}{%s} + \\frac{1}{%s} - \\frac{1}{%s} + ... + \\frac{1}{%s} - \\frac{1}{%s} \\right)$ \\\\\n'
                    '$= %s \\left( \\frac{1}{%s} - \\frac{1}{%s} \\right)$ \\\\\n'
                    'Suy ra $\\lim_{n \\to +\\infty} u_n = \\lim_{n \\to +\\infty} \\left[ %s \\left( \\frac{1}{%s} - \\frac{1}{%s} \\right) \\right] = %s . \\frac{1}{%s} = %s$.'
                    % (
                        # Dòng 1: Đề bài lại
                        term1_1, term1_2, term2_1, term2_2, str_n_1, str_n_2,
                        # Dòng 2: Khai triển
                        phan_so_tach, term1_1, term1_2, term2_1, term2_2, str_n_1, str_n_2,
                        # Dòng 3: Rút gọn
                        phan_so_tach, term1_1, str_n_2,
                        # Dòng 4: Kết luận Lim
                        phan_so_tach, term1_1, str_n_2, phan_so_tach, term1_1, latex(kq_chuan)
                    )
                )

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


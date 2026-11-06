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


def bt_dang40_p4_b3_c3_ds12(self):
            # Khai báo biến
            # Cấu hình hiển thị LaTeX cho Sympy
            def to_vietnamese_latex(expr):
                """Chuyển đổi ký hiệu \\log của Sympy thành \\ln theo chuẩn Việt Nam"""
                s = latex(expr)
                return s.replace('\\log', '\\ln')

            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 1: Random các thông số bài toán
                # Ta chọn cơ số a = 2 (giống đề bài mẫu)
                a = 2
                # Chọn hoành độ giao điểm k sao cho b = a^k là số nguyên đẹp
                k = random.choice([0, 1, 2]) 
                b = a**k

                # Chọn các cận c và d sao cho c < k < d để tích phân phải chia làm 2 miền
                c = k - random.randint(1, 2)
                d = k + random.randint(1, 2)

                # Bước 2: Tính toán diện tích thực tế bằng Sympy
                # S = tích phân từ c đến d của |2^x - b|
                f = a**x - b

                # Miền 1: từ c đến k, b >= a^x
                tp1_expr = b - a**x
                tp1 = integrate(tp1_expr, (x, c, k))

                # Miền 2: từ k đến d, a^x >= b
                tp2_expr = a**x - b
                tp2 = integrate(tp2_expr, (x, k, d))

                kq_chuan = simplify(tp1 + tp2)

                # Đáp án đúng
                da_str = to_vietnamese_latex(kq_chuan)
                da = '$%s$' % da_str

                # Bước 3: Tạo các phương án sai (không trùng đáp án đúng)
                du_s = []
                # Các kịch bản sai: sai dấu, quên chia ln(2), hoặc sai hằng số
                sai1 = simplify(tp1 - tp2) # Sai dấu giữa 2 miền
                sai2 = simplify(integrate(f, (x, c, d))) # Không lấy trị tuyệt đối
                sai3 = simplify(kq_chuan + Rational(random.choice([1, 2]), 2)) # Lệch đơn vị

                list_sai_raw = [sai1, sai2, sai3]
                for item in list_sai_raw:
                    val = '$%s$' % to_vietnamese_latex(item)
                    if val != da and val not in du_s:
                        du_s.append(val)

                # Đảm bảo luôn có đủ 3 đáp án sai khác nhau
                offset = 1
                while len(du_s) < 3:
                    val = '$%s$' % to_vietnamese_latex(kq_chuan + offset)
                    if val != da and val not in du_s:
                        du_s.append(val)
                    offset += 1

                das1, das2, das3 = du_s[0], du_s[1], du_s[2]

                # Bước 4: Nội dung câu hỏi
                noidungcauhoi = ('''Tính diện tích hình phẳng giới hạn bởi đồ thị hàm số $y = %s^x$ và các đường thẳng $y = %s; x = %s; x = %s$.'''
                                 %(latex(a), latex(b), latex(c), latex(d)))

                # Bước 5: Nội dung lời giải (Sử dụng \text{d}x và \ln)
                # Nguyên hàm của a^x là a^x / ln(a)
                nguyen_ham_f = a**x / ln(a)

                loigiai = ('''Phương trình hoành độ giao điểm: $%s^x = %s \\Leftrightarrow x = %s$.\\\\
                             Diện tích hình phẳng cần tính là: \\\\
                             $S = \\int_{%s}^{%s} |%s^x - %s| \\text{d}x = \\int_{%s}^{%s} |%s^x - %s| \\text{d}x + \\int_{%s}^{%s} |%s^x - %s| \\text{d}x$ \\\\
                             $= \\int_{%s}^{%s} (%s - %s^x) \\text{d}x + \\int_{%s}^{%s} (%s^x - %s) \\text{d}x$ \\\\
                             $= \\left. \\left( %sx - \\frac{%s^x}{\\ln %s} \\right) \\right|_{%s}^{%s} + \\left. \\left( \\frac{%s^x}{\\ln %s} - %sx \\right) \\right|_{%s}^{%s} = %s$.'''
                          %(latex(a), latex(b), latex(k),
                            latex(c), latex(d), latex(a), latex(b), 
                            latex(c), latex(k), latex(a), latex(b), 
                            latex(k), latex(d), latex(a), latex(b),
                            latex(c), latex(k), latex(b), latex(a), 
                            latex(k), latex(d), latex(a), latex(b),
                            latex(b), latex(a), latex(a), latex(c), latex(k), 
                            latex(a), latex(a), latex(b), latex(k), latex(d), 
                            da_str
                           ))

                # Đưa các đáp án vào danh sách và trộn ngẫu nhiên
                da_d = ('\\True ' + str(da))
                list_1 = [da_d, das1, das2, das3]
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm theo đúng định dạng mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


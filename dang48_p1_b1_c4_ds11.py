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


def bt_dang48_p1_b1_c4_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # --- BƯỚC 1: RANDOM HÓA DỮ LIỆU ĐẦU VÀO ---
                # Cấu trúc số: a,b(c) (Ví dụ: 3,1(5))
                a = randint(1, 9)      # Phần nguyên
                b = randint(1, 9)      # Chữ số thập phân không tuần hoàn
                c = randint(1, 9)      # Chữ số tuần hoàn
                while c == b:          # Đảm bảo c khác b để bài toán rõ ràng
                    c = randint(1, 9)

                # --- BƯỚC 2: TÍNH TOÁN KẾT QUẢ ---
                # Giá trị phần a,b = a + b/10
                val_ab = a + Rational(b, 10)

                # Giá trị phần đuôi tuần hoàn c: c * (1/100 + 1/1000 + ...)
                # Đây là CSN lùi vô hạn với u1 = 1/100, q = 1/10
                # Tổng chuỗi S = (1/100) / (1 - 1/10) = (1/100) / (9/10) = 1/90
                val_c_part = c * Rational(1, 90)

                # Kết quả cuối cùng (phân số tối giản)
                kq_chuan = val_ab + val_c_part

                # --- BƯỚC 3: TẠO CÁC ĐÁP ÁN NHIỄU (DISTRACTORS) ---
                # Đáp án đúng
                da = '$%s$' % latex(kq_chuan)

                # Tạo đáp án sai bằng cách thay đổi tử hoặc mẫu một chút
                # Sai 1: Cộng thêm 1 vào tử số
                s1 = kq_chuan + Rational(randint(1, 5), kq_chuan.q)
                # Sai 2: Trừ đi 1 ở tử số
                s2 = kq_chuan - Rational(randint(1, 5), kq_chuan.q)
                # Sai 3: Sai lầm phổ biến (coi mẫu là 99 thay vì 90) -> a,bc = (abc-a)/99
                # Hoặc đơn giản là random mẫu số khác
                s3 = kq_chuan + Rational(1, randint(2, 5))

                s = [
                    '$%s$' % latex(s1),
                    '$%s$' % latex(s2),
                    '$%s$' % latex(s3)
                ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # --- BƯỚC 4: XÂY DỰNG NỘI DUNG CÂU HỎI VÀ LỜI GIẢI ---

                # Chuỗi hiển thị đề bài: 3,15555... = 3,1(5)
                # Lưu ý: Code thay thế dấu chấm (.) thành phẩy (,) để phù hợp quy ước toán VN
                de_bai_str_full = f"{a},{b}{c}{c}{c}{c}..."
                de_bai_str_short = f"{a},{b}({c})"

                noidungcauhoi = (
                    f"Số thập phân vô hạn tuần hoàn ${de_bai_str_full} = {de_bai_str_short}$ viết dưới dạng hữu tỉ là"
                )

                # Các đáp án
                da_d = '\\True ' + str(da)
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Xây dựng lời giải chi tiết y hệt ảnh mẫu
                # Dòng 1: Phân tích thành tổng
                # Dòng 2: Áp dụng công thức tổng CSN lùi vô hạn
                # Dòng 3: Kết quả

                loigiai = (
                    f"${de_bai_str_full} = {de_bai_str_short} = {a},{b} + {c} \\left( \\dfrac{{1}}{{10^2}} + \\dfrac{{1}}{{10^3}} + ... \\right)$ \\\\\n"
                    f"$= {a},{b} + {c} \\cdot \\dfrac{{\\dfrac{{1}}{{10^2}}}}{{1 - \\dfrac{{1}}{{10}}}} = \\dfrac{{{latex(val_ab.p)}}}{{{val_ab.q}}} + \\dfrac{{{c}}}{{90}} = {latex(kq_chuan)}.$"
                )

            # Xuất câu trắc nghiệm
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + ' \n'
                '\\choice \n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '{' + str(list_1[0]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


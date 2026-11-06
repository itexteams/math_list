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


def bt_dang38_p4_b3_c5_ds11(self):
            # Khai báo biến
            # --- B3: Tư duy Random ---
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # 1. Random dữ liệu (Ví dụ khớp với hình: M=1.1 tỷ, r=0.9, n=31)
                # Bạn có thể để cố định hoặc để random trong khoảng
                M_val = random.randint(10, 15) * 100000000  # 1 tỷ đến 1,5 tỷ
                r_val = random.choice([0.7, 0.8, 0.9, 1.0, 1.1]) # % mỗi tháng
                n_val = random.randint(24, 48) # Từ 2 đến 4 năm

                # Sử dụng Decimal để tính toán chính xác tuyệt đối
                # Chuyển r_val thành Decimal trước khi chia
                r_decimal = Decimal(str(r_val)) / Decimal('100')
                M_dec = Decimal(str(M_val))

                # 2. Tính toán số tiền A hàng tháng
                # Công thức: A = (M * r * (1+r)^n) / ((1+r)^n - 1)
                one_plus_r = Decimal('1') + r_decimal
                mu_n = one_plus_r ** n_val

                A_val = (M_dec * r_decimal * mu_n) / (mu_n - Decimal('1'))

                # Làm tròn số tiền cuối cùng (Đơn vị đồng)
                kq_tron = int(A_val.quantize(Decimal('1'), rounding=ROUND_HALF_UP))

                # --- Hàm định dạng số chuẩn Việt Nam ---
                def format_vn(n, is_rate=False, is_full_decimal=False):
                    """
                    is_rate=True: Dùng cho 0,9%
                    is_full_decimal=True: Dùng cho 0,009 (không bị lỗi 0.009000...1)
                    """
                    if is_rate:
                        return str(n).replace('.', ',')
                    if is_full_decimal:
                        # Định dạng lấy tối đa 10 chữ số nhưng loại bỏ số 0 thừa ở cuối
                        # Cách này giúp triệt tiêu sai số 0.00900000000000001
                        formatted = "{:g}".format(float(n))
                        return formatted.replace('.', ',')

                    # Định dạng tiền tệ: 1.100.000.000
                    return "{:,}".format(int(n)).replace(',', '.')

                # Chuẩn bị chuỗi hiển thị
                M_str = format_vn(M_val)
                r_str = format_vn(r_val, is_rate=True)
                r_decimal_str = format_vn(r_decimal, is_full_decimal=True)
                r_display = format_vn(float(one_plus_r), is_full_decimal=True)
                kq_str = format_vn(kq_tron)

                # Tạo đáp án
                da_dung = f"{kq_str} đồng."
                # Tạo nhiễu bằng cách thay đổi vài đơn vị ở cuối
                list_s = [
                    f"{format_vn(kq_tron + 20000)} đồng.",
                    f"{format_vn(kq_tron + 10000)} đồng.",
                    f"{format_vn(kq_tron - 10000)} đồng."
                ]

                # --- Nội dung câu hỏi ---
                noidungcauhoi = (f"Một người vay tiền ở một ngân hàng theo hình thức lãi kép với lãi suất ${r_str}\\%$/tháng với tổng số tiền vay là {M_str} đồng. "
                                 f"Mỗi tháng người đó đều trả cho ngân hàng một số tiền như nhau để trừ vào tiền gốc và lãi. "
                                 f"Biết rằng đúng ${n_val}$ tháng thì người đó trả hết gốc và lãi cho ngân hàng. "
                                 f"Hỏi số tiền của người đó trả cho ngân hàng ở mỗi tháng gần nhất với số nào sau đây?")

                # Trộn đáp án
                da_d = '\\True ' + da_dung
                list_1 = [da_d] + list_s
                random.shuffle(list_1)

                # --- Nội dung lời giải (Sửa lỗi hiển thị số thập phân dài) ---
                loigiai = (f"Gọi $M$ là số tiền vay ban đầu ($M = {M_str}$ đồng).\\\\ "
                           f"Gọi $A$ là số tiền mà hàng tháng người đó trả cho ngân hàng.\\\\ "
                           f"Sau tháng 1 dư nợ còn lại là: $M \\cdot {r_display} - A$\\\\ "
                           f"Sau tháng 2 dư nợ còn lại là: $(M \\cdot {r_display} - A) \\cdot {r_display} - A = M \\cdot {r_display}^2 - A \\cdot {r_display} - A$\\\\ "
                           f"Sau tháng thứ $n$ dư nợ còn lại là: $M \\cdot {r_display}^n - A \\cdot \\left[ {r_display}^{{n-1}} + {r_display}^{{n-2}} + \\dots + 1 \\right]$\\\\ "
                           f"Vì đúng ${n_val}$ tháng thì trả hết nợ nên:\\\\ "
                           f"${M_str} \\cdot {r_display}^{{{n_val}}} - A \\cdot \\frac{{{r_display}^{{{n_val}}} - 1}}{{{r_decimal_str}}} = 0$\\\\ "
                           f"$\\Leftrightarrow A = \\frac{{{M_str} \\cdot {r_decimal_str} \\cdot {r_display}^{{{n_val}}}}}{{{r_display}^{{{n_val}}} - 1}} \\approx {kq_str}$ đồng.")

            # --- Xuất kết quả ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


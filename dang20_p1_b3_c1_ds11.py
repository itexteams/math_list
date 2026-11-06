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


def bt_dang20_p1_b3_c1_ds11(self):
            # Khai báo biến
            def round_SA(a): 
                # Kiểm tra nếu a là số nguyên
                if a == int(a):
                    return "", int(a)

                # Chuyển số thành chuỗi và tách phần nguyên, phần thập phân
                str_a = f"{a:.5f}".rstrip('0')
                integer_part, _, decimal_part = str_a.partition('.')

                # Xác định cách làm tròn
                if len(integer_part) > 2:
                    number = Decimal(float(a)).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
                    cirle = "(làm tròn kết quả đến hàng đơn vị)."
                elif len(integer_part) == 2 and len(decimal_part) > 1:
                    number = Decimal(float(a)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                    cirle = "(làm tròn kết quả đến hàng phần chục)."
                elif len(decimal_part) <= 2:
                    number = str_a 
                    cirle = ""
                else:
                    number = Decimal(float(a)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                    cirle = "(làm tròn kết quả đến hàng phần trăm)."

                # Chuyển dấu chấm thành dấu phẩy
                return cirle, str(number).replace('.', ',')

            # =============================================================================

            # --- RANDOM ĐỐI SỐ ---
            C_avg_depth = S(random.randint(35, 55)) / 10
            A_amplitude = S(random.randint(5, 15)) / 10
            B_freq = S(pi)/6

            # Biến t cho câu hỏi
            t1 = random.randint(2, 5)

            # --- TÍNH ĐÁP ÁN ĐÚNG TRƯỚC ---
            dap_an_dung_raw = A_amplitude * cos(B_freq * t1) + C_avg_depth

            # Lấy chuỗi hiển thị của đáp án đúng để so sánh (tránh trùng lặp về mặt hiển thị)
            note_correct, str_correct_val = round_SA(N(dap_an_dung_raw))
            str_correct_full = f"${str_correct_val}\\ \\text{{m}}$"

            # --- XỬ LÝ TẠO ĐÁP ÁN NHIỄU (KHÔNG TRÙNG LẶP) ---
            # Danh sách các lỗi logic tiềm năng (Potential logical errors)
            potential_errors = [
                A_amplitude * (cos(B_freq * t1)),                 # Lỗi: Quên cộng C
                A_amplitude * cos(t1) + C_avg_depth,              # Lỗi: Quên nhân B_freq
                A_amplitude * (-cos(B_freq * t1)) + C_avg_depth,  # Lỗi: Dùng -cos
                dap_an_dung_raw + 1,                              # Lỗi: Cộng thêm 1
                dap_an_dung_raw - 1,                              # Lỗi: Trừ đi 1
            ]

            distractor_set = set() # Sử dụng Set để tự động loại bỏ trùng lặp

            # 1. Thử thêm các lỗi logic vào danh sách nhiễu
            for err_val in potential_errors:
                _, str_err_val = round_SA(N(err_val))
                str_err_full = f"${str_err_val}\\ \\text{{m}}$"
                # Chỉ thêm nếu khác đáp án đúng
                if str_err_full != str_correct_full:
                    distractor_set.add(str_err_full)

            # 2. Nếu chưa đủ 3 đáp án nhiễu, tiếp tục random cho đến khi đủ
            loop_count = 0
            while len(distractor_set) < 3 and loop_count < 100: 
                loop_count += 1
                # Tạo độ lệch ngẫu nhiên từ -2.5 đến 2.5 (tránh số 0)
                delta = random.uniform(-2.5, 2.5)
                if abs(delta) < 0.2: delta = 0.5 # Đảm bảo lệch ít nhất 0.5

                fake_val = dap_an_dung_raw + delta
                _, str_fake_val = round_SA(N(fake_val))
                str_fake_full = f"${str_fake_val}\\ \\text{{m}}$"

                # Kiểm tra trùng với đáp án đúng
                if str_fake_full != str_correct_full:
                    distractor_set.add(str_fake_full)

            # Chuyển về list và lấy đúng 3 phần tử nhiễu
            list_nhieu_final = list(distractor_set)[:3]

            # ------------------------------------------------

            # --- TẠO NỘI DUNG ĐỀ BÀI (KHẮC PHỤC LỖI SYNTAX) ---

            # Bước quan trọng: Tạo chuỗi Latex cho B_freq ở ngoài f-string 
            # để tránh lỗi "backslash in f-string expression"
            latex_B_freq = latex(B_freq, mul_symbol='\\cdot')

            de_bai_chung = f"""Độ sâu $h$ (m) của mực nước ở một cảng biển vào thời điểm $t$ (giờ) sau khi thuỷ triều
            lên lần đầu tiên trong ngày được tính xấp xỉ bởi công thức:
            $$h(t) = {latex(A_amplitude)} \\cos\\left({latex_B_freq} t\\right) + {latex(C_avg_depth)}$$"""

            # Nội dung câu hỏi cụ thể
            cau_hoi = f"""Độ sâu của nước vào thời điểm $t = {t1}$ là bao nhiêu mét? {note_correct}"""

            # Nội dung lời giải
            loi_giai = f"""Thay $t = {t1}$ vào công thức, ta có:
            $$h({t1}) = {latex(A_amplitude)} \\cos\\left({latex_B_freq} \\cdot {t1}\\right) + {latex(C_avg_depth)} \\approx {str_correct_val}\\,\\text{{m}}.$$"""

            # Tập hợp đáp án
            list_dap_an_final = [
                f"\\True {str_correct_full}",    # Đúng
                list_nhieu_final[0],             # Nhiễu 1
                list_nhieu_final[1],             # Nhiễu 2
                list_nhieu_final[2]              # Nhiễu 3
            ]
            # Trộn đáp án
            random.shuffle(list_dap_an_final)

            # Xuất câu trắc nghiệm ra định dạng LaTeX
            content = ('\\begin{minipage}{\\textwidth} \n' 
                '\\begin{ex}\n'+ de_bai_chung + cau_hoi + '\n'
                '\\choice \n'
                '{'+ list_dap_an_final[0] +'}\n'
                '{'+ list_dap_an_final[1] +'}\n'
                '{'+ list_dap_an_final[2] +'}\n'
                '{'+ list_dap_an_final[3] +'}\n'
                '\\loigiai{'+ loi_giai +'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content


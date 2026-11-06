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


def bt_dang36_p2_b1_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            t = symbols('t')

            # --- HÀM HỖ TRỢ ---

            def format_vn(value, precision=1):
                """Định dạng số thập phân dùng dấu phẩy và làm tròn."""
                num = round(float(value), precision)
                # Nếu là số nguyên (ví dụ 5.0) thì trả về '5', nếu lẻ thì trả về '5,1'
                if num == int(num):
                    return str(int(num))
                return str(num).replace('.', ',')

            def count_true_answers(answers):
                """Đếm số lượng đáp án đúng trong danh sách."""
                return sum(1 for ans in answers if '\\True' in ans)

            # --- BƯỚC 1: RANDOM DỮ LIỆU GỐC ---
            # v(t) = - (1/k)*t^3 + a*t^2
            a_val = random.randint(1, 3) 
            k_val = random.choice([5, 6, 8, 10, 12]) 
            t_max_growth = a_val * k_val 
            h0 = random.randint(3, 8) 

            # Thiết lập các hàm số Sympy
            vt = -Rational(1, k_val)*t**3 + a_val*t**2
            ht_func = integrate(vt, t) + h0

            # Nội dung câu hỏi gốc
            noidungcauhoi = (f"Cây cà chua khi trồng có chiều cao ${h0}$ cm. Tốc độ tăng chiều cao của cây sau khi trồng "
                             f"được cho bởi hàm số $v(t) = {latex(vt)}$, trong đó $t$ tính theo tuần, $v(t)$ tính bằng cm/tuần. "
                             f"Gọi $h(t)$ là chiều cao của cây ở tuần thứ $t$. Xét tính đúng sai của các mệnh đề sau:")

            # --- BƯỚC 2: CHUẨN BỊ CÁC LỰA CHỌN ĐÚNG/SAI ---

            # a) Nhận biết: Công thức hàm số
            lg_a = f"Ta có $h(t) = \\int ({latex(vt)}) dt = {latex(integrate(vt, t))} + C$. Vì $h(0) = {h0} \\Rightarrow C = {h0}$."
            list_da_a = [
                f"\\True Công thức xác định hàm số $h(t)$ là $h(t) = {latex(ht_func)}$ với $t \\geq 0$",
                f"Công thức xác định hàm số $h(t)$ là $h(t) = {latex(ht_func - h0)}$ với $t \\geq 0$"
            ]

            # b) Thông hiểu: Thời gian tăng trưởng
            lg_b = f"Cây tăng trưởng khi $v(t) > 0 \\Leftrightarrow {latex(vt)} > 0 \\Leftrightarrow t^2({a_val} - \\frac{{1}}{{{k_val}}}t) > 0 \\Leftrightarrow t < {t_max_growth}$."
            list_da_b = [
                f"\\True Giai đoạn tăng trưởng của cây kéo dài ${t_max_growth}$ tuần",
                f"Giai đoạn tăng trưởng của cây kéo dài ${t_max_growth + 2}$ tuần"
            ]

            # c) Vận dụng: Chiều cao tối đa
            h_max = ht_func.subs(t, t_max_growth)
            val_c = format_vn(h_max)
            lg_c = f"Chiều cao tối đa đạt được tại $t = {t_max_growth}$. Khi đó $h({t_max_growth}) = {latex(h_max)} \\approx {val_c}$ cm."
            list_da_c = [
                f"\\True Chiều cao tối đa của cây cà chua là ${val_c}$ cm",
                f"Chiều cao tối đa của cây cà chua là ${format_vn(float(h_max) - 10)}$ cm"
            ]

            # d) Vận dụng cao: Tốc độ phát triển nhanh nhất
            v_prime = diff(vt, t)
            t_fastest = solve(v_prime, t)[1] # Lấy nghiệm dương
            h_at_fastest = ht_func.subs(t, t_fastest)
            val_d = format_vn(h_at_fastest)
            lg_d = f"Tốc độ tăng trưởng nhanh nhất khi $v'(t) = 0 \\Leftrightarrow {latex(v_prime)} = 0 \\Leftrightarrow t = {latex(t_fastest)}$. \\\\" \
                   f"Khi đó $h({latex(t_fastest)}) = {latex(h_at_fastest)} \\approx {val_d}$ cm."
            list_da_d = [
                f"\\True Thời điểm cây phát triển nhanh nhất thì cây cao khoảng ${val_d}$ cm",
                f"Thời điểm cây phát triển nhanh nhất thì cây cao khoảng ${format_vn(float(h_at_fastest) + 15)}$ cm"
            ]

            # --- BƯỚC 3: LẶP ĐỂ ĐẢM BẢO SỐ CÂU ĐÚNG TỪ 1 ĐẾN 3 ---

            while True:
                ans_a = random.choice(list_da_a)
                ans_b = random.choice(list_da_b)
                ans_c = random.choice(list_da_c)
                ans_d = random.choice(list_da_d)

                shuffled_answers = [ans_a, ans_b, ans_c, ans_d]
                true_count = count_true_answers(shuffled_answers)

                if 1 <= true_count <= 3:
                    break

            # --- BƯỚC 4: XUẤT NỘI DUNG THEO ĐỊNH DẠNG ---

            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choiceTFn \n'
                       '{' + str(shuffled_answers[0]) + '}\n'
                       '{' + str(shuffled_answers[1]) + '}\n'
                       '{' + str(shuffled_answers[2]) + '}\n'
                       '{' + str(shuffled_answers[3]) + '}\n'
                       '\\loigiai{ \n'
                       '\\begin{enumEX}[a)]{1} \n'
                       '\\item ' + str(lg_a) + '\n'
                       '\\item ' + str(lg_b) + '\n'
                       '\\item ' + str(lg_c) + '\n'
                       '\\item ' + str(lg_d) + '\n'
                       '\\end{enumEX}} \n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content


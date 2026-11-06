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


def bt_dang52_p1_b1_c4_ds11(self):
            # Khai báo biến
            # --- KHAI BÁO BIẾN CẤU HÌNH ---
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # --- BƯỚC 1: RANDOM HÓA DỮ LIỆU ĐẦU VÀO ---
                # Dạng u_n = a * u_{n-1} + b
                # Chọn hệ số a (công bội) thường là số nguyên dương > 1 để giới hạn hội tụ về hằng số
                a_val = randint(2, 5) 

                # Chọn hệ số b (hệ số tự do), tránh 0 để bài toán không trở thành CSN thuần túy ngay từ đầu
                b_val = randint(-5, 5)
                while b_val == 0:
                    b_val = randint(-5, 5)

                # Chọn u1 (số hạng đầu)
                u1_val = randint(-5, 5)

                # --- BƯỚC 2: TÍNH TOÁN LỜI GIẢI (DÙNG SYMPY) ---
                # Chuyển đổi sang đối tượng Rational của Sympy để tính toán phân số chính xác
                a = Integer(a_val)
                b = Integer(b_val)
                u1 = Integer(u1_val)

                # Tìm hằng số c sao cho u_n - c = a(u_{n-1} - c)
                # c = b / (1 - a)
                c = Rational(b, 1 - a)

                # Tìm v1 = u1 - c
                v1 = u1 - c

                # Kết quả giới hạn L = v1 / a
                kq_chinh_xac = v1 / a

                # --- BƯỚC 3: TẠO CÁC ĐÁP ÁN NHIỄU (DISTRACTORS) ---
                # Đáp án đúng
                da = '$%s$' % latex(kq_chinh_xac)

                # Tạo tập hợp các đáp án sai để tránh trùng lặp
                wrong_answers = set()

                # Nhiễu 1: Quên chia cho a (chỉ lấy v1)
                wrong_answers.add(v1)

                # Nhiễu 2: Sai dấu kết quả
                wrong_answers.add(-kq_chinh_xac)

                # Nhiễu 3: Lấy chính giá trị c (hằng số phụ)
                wrong_answers.add(c)

                # Nhiễu 4: Cộng thêm hoặc trừ đi 1 đơn vị
                wrong_answers.add(kq_chinh_xac + 1)
                wrong_answers.add(kq_chinh_xac - 1)

                # Nhiễu 5: Random phân số ngẫu nhiên
                wrong_answers.add(Rational(randint(-10,10), randint(2,6)))

                # Loại bỏ đáp án đúng nếu vô tình trùng và chuyển thành list
                if kq_chinh_xac in wrong_answers:
                    wrong_answers.remove(kq_chinh_xac)

                list_wrong = list(wrong_answers)
                random.shuffle(list_wrong)

                # Lấy 3 đáp án sai
                s = ['$%s$' % latex(x) for x in list_wrong[:3]]

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # --- BƯỚC 4: XÂY DỰNG NỘI DUNG LATEX ---

                # Xử lý hiển thị dấu cho phương trình u_n = a*u_{n-1} + b
                # Nếu b âm thì hiện dấu trừ, b dương hiện dấu cộng
                dau_b = "-" if b_val < 0 else "+"
                tri_tuyet_doi_b = abs(b_val)

                # Câu hỏi
                noidungcauhoi = (
                    '''Cho dãy số $(u_n)$ biết $\\heva{& u_1 = %s \\\\ & u_n = %su_{n-1} %s %s, \\forall n \\ge 2}$, khi đó $L = \\lim\\limits_{n \\to +\\infty} \\dfrac{u_n}{%s^n}$ bằng'''
                    % (latex(u1), latex(a), dau_b, latex(tri_tuyet_doi_b), latex(a))
                )

                # Lời giải chi tiết
                # Xử lý hiển thị phép tính v_n + c để trông tự nhiên (ví dụ: v_n + -1/2 thành v_n - 1/2)
                c_str = latex(c)
                if c > 0:
                    c_display = "+ " + c_str
                    c_display_nguoc = "- " + c_str # dùng cho phép tính u1 - c
                else:
                    c_display = c_str # Đã có dấu trừ
                    c_display_nguoc = "+ " + latex(abs(c))

                # Chuỗi hiển thị v1 = u1 - c
                v1_calc_str = f"{latex(u1)} {c_display_nguoc} = {latex(v1)}"

                loigiai = ('''Đặt $u_n = v_n %s$, thay vào biểu thức truy hồi ta có
                $$v_n %s = %s \\left( v_{n-1} %s \\right) %s %s \\Leftrightarrow v_n = %sv_{n-1}, \\forall n \\ge 2.$$
                Dễ thấy $(v_n)$ là cấp số nhân với $v_1 = u_1 - (%s) = %s$, công bội $q=%s$. \\\\
                Suy ra $v_n = %s \\cdot %s^{n-1}$. \\\\
                Do đó $u_n = v_n %s = %s \\cdot %s^{n-1} %s, (n \\ge 1)$. \\\\
                Vậy $L = \\lim\\limits_{n \\to +\\infty} \\dfrac{u_n}{%s^n} = \\lim\\limits_{n \\to +\\infty} \\left( \\dfrac{%s}{%s} + \\dfrac{%s}{%s \\cdot %s^n} \\right) = %s$.'''
                % (
                    c_display, # Đặt u_n = v_n + c
                    c_display, # v_n + c
                    latex(a), # a
                    c_display, # (v_{n-1} + c)
                    dau_b, latex(tri_tuyet_doi_b), # + b
                    latex(a), # => v_n = a*v_{n-1}
                    c_str, v1_calc_str, latex(a), # v1 = u1 - c..., q=a
                    latex(v1), latex(a), # v_n = v1 . a^(n-1)
                    c_display, latex(v1), latex(a), c_display, # u_n = ...
                    latex(a), # L = ... / a^n
                    latex(Rational(v1, a)), latex(a), # (-5/2) / 3 -> viết dưới dạng phân số đẹp hơn ở code logic nhưng ở đây hiển thị text
                    c_str, latex(a), latex(a), # c / (a.a^n) ... phần này biểu diễn hơi phức tạp, ta viết thẳng kết quả
                    latex(kq_chinh_xac)
                ))

                # Tinh chỉnh lại dòng cuối của lời giải cho khớp công thức toán học hơn
                # Dòng limit trong ảnh mẫu: -5/6 + 1/(2.3^n) -> -5/6. 
                # Ta tái tạo logic đó: L = v1/a
                term1 = latex(v1) # v1
                term2 = latex(a) # a
                term_res = latex(kq_chinh_xac)

                # Cập nhật lại chuỗi lời giải phần tính Limit cho mượt
                loigiai = ('''Đặt $u_n = v_n %s$, thay vào biểu thức truy hồi ta có 
                $$v_n %s = %s \\left( v_{n-1} %s \\right) %s %s \\Leftrightarrow v_n = %sv_{n-1}, \\forall n \\ge 2.$$
                Dễ thấy $(v_n)$ là cấp số nhân với $v_1 = u_1 - (%s) = %s$, công bội $q=%s$. \\\\
                Suy ra $v_n = %s \\cdot %s^{n-1}$. \\\\
                Do đó $u_n = v_n %s = %s \\cdot %s^{n-1} %s, (n \\ge 1)$. \\\\
                Vậy $L = \\lim\\limits_{n \\to +\\infty} \\dfrac{u_n}{%s^n} = \\lim\\limits_{n \\to +\\infty} \\left( \\dfrac{%s \\cdot %s^{n-1}}{%s^n} + \\dfrac{%s}{%s^n} \\right) = \\dfrac{%s}{%s} = %s$.'''
                % (
                    c_display, 
                    c_display, 
                    latex(a), c_display, dau_b, latex(tri_tuyet_doi_b), latex(a),
                    latex(c), v1_calc_str, latex(a),
                    latex(v1), latex(a),
                    c_display, latex(v1), latex(a), c_display,
                    latex(a), 
                    latex(v1), latex(a), latex(a), latex(c), latex(a), # Phần biểu thức trong ngoặc limit
                    latex(v1), latex(a), term_res # Kết quả cuối
                ))

                # --- BƯỚC 5: XUẤT OUTPUT ---
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                content = ('\\begin{minipage}{\\textwidth} \n'
                    '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                    '\\choice \n'
                    '{' + str(list_1[0]) + '}\n'
                    '{' + str(list_1[1]) + '}\n'
                    '{' + str(list_1[2]) + '}\n'
                    '{' + str(list_1[3]) + '}\n'
                    '\\loigiai{' + str(loigiai) + '}\n'
                    '\\end{ex}\n \\end{minipage} \n\n')
            return content


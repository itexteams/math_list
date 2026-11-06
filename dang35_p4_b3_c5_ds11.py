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


def bt_dang35_p4_b3_c5_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B3: Random bài toán
                # A_vay: Số tiền vay (triệu đồng), chọn từ 50 đến 500 triệu, bước nhảy 10
                A_vay = random.randint(5, 50) * 10 
                # r_nam: Lãi suất năm (%), chọn các số chia hết cho 12 để lãi tháng đẹp
                r_nam = random.choice([6, 12, 18, 24]) 
                # n: Số tháng hoàn nợ
                n = 3 # Giữ nguyên 3 tháng theo mẫu hình ảnh để đảm bảo logic lời giải khớp

                r_thang_phan_tram = r_nam / 12
                r = r_thang_phan_tram / 100 # Lãi suất thực tế (ví dụ 0.01)
                he_so = 1 + r

                # Tính toán giá trị m theo công thức: m = A * r * (1+r)^n / ((1+r)^n - 1)
                # Để khớp với cách biến đổi trong ảnh: m = A * (1+r)^n * (r) / ((1+r)^n - 1)
                m_val = (A_vay * (he_so**n) * r) / (he_so**n - 1)

                # Làm tròn kết quả đến 3 chữ số thập phân để hiển thị
                kq_num = round(m_val, 3)
                kq_str = str(kq_num).replace('.', ',')

                # Đáp án đúng
                da_dung = f"${kq_str}$"

                # B4: Tạo các phương án sai không trùng với đáp án đúng
                s = []
                while len(s) < 3:
                    sai = round(m_val + random.choice([-5.2, -2.1, 1.5, 3.3, 4.8]), 3)
                    sai_str = f"${str(sai).replace('.', ',')}$"
                    if sai_str != da_dung and sai_str not in s:
                        s.append(sai_str)

                das1, das2, das3 = s

                # B2: Viết lại nội dung câu hỏi
                noidungcauhoi = (f"Ông A vay ngắn hạn ngân hàng ${A_vay}$ triệu đồng, với lãi suất ${r_nam}\\%$/năm. "
                                 f"Ông muốn hoàn nợ cho ngân hàng theo cách: Sau đúng một tháng kể từ ngày vay, ông bắt đầu hoàn nợ; "
                                 f"hai lần hoàn nợ liên tiếp cách nhau đúng một tháng, số tiền hoàn nợ ở mỗi lần là như nhau và trả hết nợ "
                                 f"sau đúng ${n}$ tháng kể từ ngày vay. Hỏi, theo cách đó, số tiền $m$ mà ông A sẽ phải trả cho ngân hàng "
                                 f"trong mỗi lần hoàn nợ là bao nhiêu? Biết rằng, lãi suất ngân hàng không thay đổi trong thời gian ông A hoàn nợ.")

                # Nội dung lời giải chi tiết dựa theo hình ảnh
                # Chuyển đổi dấu chấm thành dấu phẩy cho chuẩn Tiếng Việt trong LaTeX
                def vn_latex(val):
                    return str(val).replace('.', ',')

                loigiai = (f"Theo đề ta có: ông A trả hết tiền sau ${n}$ tháng vậy ông A hoàn nợ ${n}$ lần.\\\\"
                           f"Với lãi suất ${r_nam}\\%$/năm suy ra lãi suất một tháng là ${vn_latex(r_thang_phan_tram)}\\%$.\\\\"
                           f"Hoàn nợ lần 1:\\\\"
                           f"Tổng tiền cần trả (gốc và lãi) là : ${A_vay} \\cdot {vn_latex(r)} + {A_vay} = {A_vay} \\cdot {vn_latex(he_so)}$ (triệu đồng)\\\\"
                           f"Số tiền dư : ${A_vay} \\cdot {vn_latex(he_so)} - m$ (triệu đồng)\\\\"
                           f"Hoàn nợ lần 2:\\\\"
                           f"Tổng tiền cần trả (gốc và lãi) là:\\\\"
                           f"$({A_vay} \\cdot {vn_latex(he_so)} - m) \\cdot {vn_latex(r)} + ({A_vay} \\cdot {vn_latex(he_so)} - m) = ({A_vay} \\cdot {vn_latex(he_so)} - m) \\cdot {vn_latex(he_so)} = {A_vay} \\cdot ({vn_latex(he_so)})^2 - {vn_latex(he_so)}m$ (triệu đồng)\\\\"
                           f"Số tiền dư: ${A_vay} \\cdot ({vn_latex(he_so)})^2 - {vn_latex(he_so)}m - m$ (triệu đồng)\\\\"
                           f"Hoàn nợ lần 3:\\\\"
                           f"Tổng tiền cần trả (gốc và lãi) là :\\\\ "
                           f"$\\left[ {A_vay} \\cdot ({vn_latex(he_so)})^2 - {vn_latex(he_so)}m - m \\right] \\cdot {vn_latex(he_so)} = {A_vay} \\cdot ({vn_latex(he_so)})^3 - ({vn_latex(he_so)})^2 m - {vn_latex(he_so)}m$ (triệu đồng)\\\\"
                           f"Số tiền dư: ${A_vay} \\cdot ({vn_latex(he_so)})^3 - ({vn_latex(he_so)})^2 m - {vn_latex(he_so)}m - m$ (triệu đồng)\\\\"
                           f"$\\Rightarrow {A_vay} \\cdot ({vn_latex(he_so)})^3 - ({vn_latex(he_so)})^2 m - {vn_latex(he_so)}m - m = 0 \\Leftrightarrow m = \\frac{{{A_vay} \\cdot ({vn_latex(he_so)})^3}}{{{vn_latex(he_so)}^2 + {vn_latex(he_so)} + 1}}$\\\\"
                           f"$\\Leftrightarrow m = \\frac{{{A_vay} \\cdot ({vn_latex(he_so)})^3 \\cdot ({vn_latex(he_so)} - 1)}}{{[({vn_latex(he_so)})^2 + {vn_latex(he_so)} + 1] \\cdot ({vn_latex(he_so)} - 1)}} = \\frac{{{A_vay} \\cdot ({vn_latex(he_so)})^3 \\cdot {vn_latex(r)}}}{{({vn_latex(he_so)})^3 - 1}} \\approx {vn_latex(kq_num)}$ (triệu đồng).")

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                list_1 = ['\\True ' + da_dung, das1, das2, das3]
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content


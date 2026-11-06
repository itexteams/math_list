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


def bt_dang57_p1_b3_c5_ds11(self):
            # Khai báo biến
            # --- B3: Suy nghĩ tìm cách random bài toán ---
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # 1. Khai báo các biến ngẫu nhiên
                # A_val: Số tiền vay (triệu đồng). Ví dụ 2.5 tỷ = 2500 triệu
                A_val = random.randint(15, 40) * 100 
                A_ty_hien_thi = str(A_val / 1000).replace('.', ',')

                # r_percent: Lãi suất phần trăm hàng tháng (từ 0.4% đến 0.8%)
                r_percent = random.choice([0.45, 0.48, 0.5, 0.51, 0.55, 0.62, 0.65])
                r = r_percent / 100 # Giá trị thập phân dùng để tính toán

                # m_val: Số tiền trả hàng tháng (triệu đồng)
                # Tính toán m_val hợp lý để nợ giảm dần (m > A*r)
                min_m = int(A_val * r) + 5
                m_val = random.randint(min_m, min_m + 30)

                # n_val: Số tháng vay
                n_val = random.choice([24, 36, 48, 60])

                # 2. Tính toán kết quả theo công thức trong hình (Trả tiền đầu kỳ)
                # Công thức: Tn = A*(1+r)^n - m * [ (1+r)^(n+1) - (1+r) ] / r
                r_plus_1 = 1 + r
                kq_chinh_xac = A_val * (r_plus_1**n_val) - m_val * ((r_plus_1**(n_val + 1) - r_plus_1) / r)

                # Làm tròn đến hàng triệu (số nguyên)
                kq_lam_tron = int(Decimal(str(kq_chinh_xac)).quantize(Decimal('1'), rounding=ROUND_HALF_UP))

                # --- B4: Điều chỉnh phương án sai (không trùng đáp án đúng) ---
                da_dung = f"${kq_lam_tron}$"

                s_sai = set()
                while len(s_sai) < 3:
                    # Tạo sai số từ 10 đến 100 đơn vị
                    lech = random.choice([-50, -30, -20, 20, 30, 50, 80])
                    phuong_an_sai = kq_lam_tron + lech
                    if phuong_an_sai != kq_lam_tron and phuong_an_sai > 0:
                        s_sai.add(f"${phuong_an_sai}$")

                list_sai = list(s_sai)

                # --- B2: Viết nội dung câu hỏi và lời giải ---
                # Định dạng hiển thị số thập phân dùng dấu phẩy cho tiếng Việt
                r_percent_str = str(r_percent).replace('.', ',')
                r_str = "{:.4f}".format(r).replace('.', ',')
                r_plus_1_str = str(round(r_plus_1, 4)).replace('.', ',')

                noidungcauhoi = (f"Ông Thành vay ngân hàng {A_ty_hien_thi} tỷ đồng và trả góp hàng tháng với lãi suất ${r_percent_str}\\%$. "
                                 f"Hàng tháng, ông Thành trả {m_val} triệu đồng (bắt đầu từ khi vay). "
                                 f"Hỏi sau {n_val} tháng thì số tiền ông Thành còn nợ là bao nhiêu (làm tròn đến hàng triệu)?")

                loigiai = (f"Đặt $A = {A_val}$ (triệu), $r = {r_str}$, $m = {m_val}$ (triệu).\\\\ "
                           f"Tiền còn nợ sau 1 tháng: $T_1 = (A-m)(1+r) = A(1+r) - m(1+r)$\\\\ "
                           f"Tiền còn nợ sau 2 tháng: $T_2 = (T_1-m)(1+r) = A(1+r)^2 - m[(1+r)^2 + (1+r)] = A(1+r)^2 - m\\frac{{(1+r)^3 - (1+r)}}{{r}}$\\\\ "
                           f"Do vậy số tiền còn nợ sau {n_val} tháng là: $T_{{{n_val}}} = A(1+r)^{{{n_val}}} - m\\frac{{(1+r)^{{{n_val+1}}} - (1+r)}}{{r}}$\\\\ "
                           f"Thay số vào ta được $T_{{{n_val}}} = {A_val}.({r_plus_1_str})^{{{n_val}}} - {m_val}.\\frac{{({r_plus_1_str})^{{{n_val+1}}} - ({r_plus_1_str})}}{{{r_str}}} \\approx {kq_lam_tron}$ (triệu).")

                # Đưa các đáp án vào danh sách và xáo trộn
                da_d = '\\True ' + da_dung
                list_ans = [da_d, list_sai[0], list_sai[1], list_sai[2]]
                random.shuffle(list_ans)

            # --- Xuất câu trắc nghiệm theo định dạng mẫu ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_ans[0]) + '}\n'
                       '{' + str(list_ans[1]) + '}\n'
                       '{' + str(list_ans[2]) + '}\n'
                       '{' + str(list_ans[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content


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


def bt_dang9_p4_b1_c2_ds11(self):
            # Khai báo biến
            # Số vi khuẩn ban đầu: (10 đến 50) x 10^8
            u_1_base = random.randint(10, 50)
            u_1_power = 8
            u_1_value = u_1_base * (10**u_1_power)

            # Số vi khuẩn bị tiêu diệt: (3 đến 9) x 10^7
            D_base = random.randint(3, 9)
            D_power = 7
            D_value = D_base * (10**D_power)

            # Tỷ lệ tăng trưởng: 10%, 15%, 20%, 25%, 30%
            r_percent_list = [10, 15, 20, 25, 30]
            r_percent = random.choice(r_percent_list)
            r_rate = 1 + (r_percent / 100.0)

            # Số lần lặp (trước lần dùng thuốc thứ N+1): N từ 3 đến 5
            N_times = random.randint(3, 5) # Cần tính u_N

            # --- THỰC HIỆN TÍNH TOÁN ---
            # Công thức: u_{n+1} = r * u_n - D (Theo logic tính toán trong bài giải gốc)
            # Bắt đầu từ u_1
            u_values = {}
            u_values[1] = u_1_value

            for n in range(1, N_times): # n chạy từ 1 đến N-1 để tính u_2 đến u_N
                # Tính u_{n+1}
                next_u = r_rate * u_values[n] - D_value

                # Đảm bảo số vi khuẩn không âm
                u_values[n+1] = max(0, next_u)

            # Kết quả cần tìm là u_N
            kq_uN = u_values[N_times]
            kq_display = int(kq_uN)

            # --- CHUẨN BỊ DỮ LIỆU ĐỂ HIỂN THỊ LATEX ---
            # Hàm format số lớn thành chuỗi '$X.Y \cdot 10^Z$'
            def format_scientific(number, exponent):
                if number == 0:
                    return '$0$'
                base = number / (10**exponent)
                precision = 0
                temp = base
                while temp != round(temp, precision):
                    precision += 1
                    if precision > 10: break

                # Sử dụng format chuẩn Latex
                formatted_base = ('{:.%sf}' % precision).format(base).replace('.',',')
                return f'${formatted_base} \\cdot 10^{exponent}$'

            # Hàm format r_rate với dấu phẩy
            def format_r_rate(rate):
                return str(rate).replace('.',',')


            # Dữ liệu cho câu hỏi (Đã bao gồm $ $ trong hàm format_scientific)
            u_1_latex = format_scientific(u_1_value, u_1_power)
            D_latex = format_scientific(D_value, D_power)
            r_percent_latex = latex(r_percent)
            N_latex = latex(N_times)
            N_plus_one_latex = latex(N_times + 1)
            r_rate_formatted = format_r_rate(r_rate) # Hệ số r_rate đã có dấu phẩy


            # Câu hỏi
            noidungcauhoi = ('''Một công ty dược phẩm đang thử nghiệm một loại thuốc mới. Một thí nghiệm bắt đầu với %s vi khuẩn. Mỗi liều thuốc được sử dụng sau mỗi bốn giờ có thể tiêu diệt %s vi khuẩn. Giữa các liều thuốc, số lượng vi khuẩn tăng lên %s\\%%. Tìm số vi khuẩn còn sống trước lần sử dụng thuốc thứ %s.''' 
            % (u_1_latex, D_latex, r_percent_latex, N_plus_one_latex))

            # Lời giải chi tiết
            loigiai_steps = []
            for n in range(1, N_times + 1):
                if n == 1:
                    step_text = f'$u_1 = {u_1_latex.strip("$")}$;'
                else:
                    # Chỉ hiển thị kết quả cuối cùng theo format
                    if u_values[n] > 0:
                        # Format số kết quả (không dùng khoa học)
                        kq_step_formatted = '{:,}'.format(int(u_values[n])).replace(',', 'a').replace('.',',').replace('a', '.')
                        # SỬ DỤNG r_rate_formatted ĐÃ CÓ DẤU PHẨY
                        step_text = f'$u_{n} = {r_rate_formatted}u_{n-1} - {D_latex.strip("$")} \\approx {kq_step_formatted}$;' 
                    else: # Nếu bị âm thì là 0
                        # SỬ DỤNG r_rate_formatted ĐÃ CÓ DẤU PHẨY
                        step_text = f'$u_{n} = {r_rate_formatted}u_{n-1} - {D_latex.strip("$")} = 0$'
                        break # Dừng tính toán khi đã về 0
                loigiai_steps.append(step_text)

            loigiai_steps_text = '\\item '.join(loigiai_steps)


            loigiai=(
            '''Gọi $u_1 = %s$ là số vi khuẩn ban đầu và $u_n$ là số vi khuẩn trước lần dùng thuốc thứ $n$. \\\\
            Công thức truy hồi được sử dụng là: $u_{n+1} = (u_n - %s) + %s\\%% \\cdot u_n = %s u_n - %s$ (trong đó %s là hệ số tăng trưởng). \\\\
            Ta tính $u_{%s}$ như sau:
            \\begin{itemize}
                \\item %s
            \\end{itemize}
            Vậy số vi khuẩn còn sống trước lần sử dụng thuốc thứ %s là $\\mathbf{%s}$ con.
            '''%(
                u_1_latex.strip('$'),
                D_latex.strip('$'),
                r_percent_latex,
                r_rate_formatted, # ĐÃ ĐƯỢC THAY THẾ
                D_latex.strip('$'),
                r_rate_formatted, # ĐÃ ĐƯỢC THAY THẾ
                N_plus_one_latex,
                loigiai_steps_text,
                N_plus_one_latex,
                '{:,}'.format(kq_display).replace(',', 'a').replace('.',',').replace('a', '.')
            ))

            # --- TẠO CÁC ĐÁP ÁN TRẮC NGHIỆM ---
            kq_formatted = '{:,}'.format(kq_display).replace(',', 'a').replace('.',',').replace('a', '.')
            da_d = ('\\True ' + '$%s$'%(kq_formatted))

            # Tạo đáp án sai bằng cách thêm/bớt các giá trị nhỏ
            da_s_list = []
            # Sai khác 10%
            da_s_list.append(int(kq_display * 1.1) if kq_display > 0 else random.randint(1000, 50000))
            da_s_list.append(int(kq_display * 0.9) if kq_display > 1000000 else random.randint(1000, 50000))
            # Sai khác một số đơn vị
            da_s_list.append(int(kq_display + random.randint(100000, 500000)) if kq_display > 0 else random.randint(1000, 50000))
            da_s_list.append(int(kq_display - random.randint(100000, 500000)) if kq_display > 1000000 else random.randint(1000, 50000))
            # Lọc các đáp án trùng
            da_s_set = set([d for d in da_s_list if d != kq_display and d > 0])
            # Chọn 3 đáp án sai ngẫu nhiên từ set
            da_s_final = random.sample(list(da_s_set), min(3, len(da_s_set)))

            da_s1 = '$%s$' % ('{:,}'.format(da_s_final[0]).replace(',', 'a').replace('.',',').replace('a', '.') if len(da_s_final) > 0 else '0')
            da_s2 = '$%s$' % ('{:,}'.format(da_s_final[1]).replace(',', 'a').replace('.',',').replace('a', '.') if len(da_s_final) > 1 else '0')
            da_s3 = '$%s$' % ('{:,}'.format(da_s_final[2]).replace(',', 'a').replace('.',',').replace('a', '.') if len(da_s_final) > 2 else '0')
            list_1 = [da_d,da_s1,da_s2,da_s3]
            random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


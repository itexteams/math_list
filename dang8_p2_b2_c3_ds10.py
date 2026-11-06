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


def bt_dang8_p2_b2_c3_ds10(self):
            # Khai báo biến
            # Hàm định dạng số thập phân theo kiểu Việt Nam (thay dấu . thành ,)
            def format_vn(val):
                if isinstance(val, float):
                    val = round(val, 2)
                    if val.is_integer():
                        return str(int(val))
                    return str(val).replace('.', ',')
                return str(val)

            # ==========================================
            # 1. SINH NGẪU NHIÊN DỮ LIỆU MẪU
            # ==========================================
            N = 100
            x_vals = [1, 2, 3, 4, 5, 6]

            # Sinh ngẫu nhiên tần số n_i sao cho tổng bằng 100 và có 1 mốt duy nhất
            while True:
                # Khởi tạo ngẫu nhiên tần số cho 5 mặt đầu tiên
                n_vals = [random.randint(5, 25) for _ in range(5)]
                n_last = N - sum(n_vals)
                # Mặt thứ 6 cũng phải có tần số hợp lý
                if 5 <= n_last <= 40:
                    n_vals.append(n_last)
                    # Đảm bảo mốt là duy nhất
                    if n_vals.count(max(n_vals)) == 1:
                        break

            # ==========================================
            # 2. TÍNH TOÁN CÁC SỐ ĐẶC TRƯNG CHÍNH XÁC
            # ==========================================
            # Số trung bình
            sum_fx = sum(x_vals[i] * n_vals[i] for i in range(6))
            x_mean = sum_fx / N

            # Mốt
            max_n = max(n_vals)
            max_idx = n_vals.index(max_n)
            M_o = x_vals[max_idx]

            # Phân tích vị trí để tìm Q2, Q3
            # Tạo mảng cộng dồn tần số để dễ tìm vị trí
            cum_freq = []
            current = 0
            for n in n_vals:
                current += n
                cum_freq.append(current)

            def get_val_at_index(idx):
                for i, cf in enumerate(cum_freq):
                    if idx <= cf:
                        return x_vals[i]

            # Q2 là trung bình cộng của x_50 và x_51
            v50 = get_val_at_index(50)
            v51 = get_val_at_index(51)
            Q_2 = (v50 + v51) / 2

            # Q3 là trung bình cộng của x_75 và x_76
            v75 = get_val_at_index(75)
            v76 = get_val_at_index(76)
            Q_3 = (v75 + v76) / 2

            # Tạo các giá trị SAI để làm nhiễu
            M_o_sai = x_vals[(max_idx + random.randint(1, 5)) % 6]
            Q_2_sai = Q_2 + random.choice([-0.5, 0.5, 1])
            Q_3_sai = Q_3 + random.choice([-0.5, 0.5, -1])
            x_mean_sai = round(x_mean + random.choice([-0.15, 0.25, -0.05]), 2)

            # ==========================================
            # 3. NỘI DUNG CÂU HỎI VÀ MỆNH ĐỀ
            # ==========================================
            noidungcauhoi = (
                f"Nhóm bạn Dũng tung một con xúc xắc {N} lần liên tiếp và ghi kết quả vào bảng sau:\n"
                f"\\begin{{center}}\n"
                f"\\begin{{tabular}}{{|c|c|c|c|c|c|c|}}\n"
                f"\\hline\n"
                f"\\textbf{{Số chấm trên xúc xắc}} & 1 & 2 & 3 & 4 & 5 & 6 \\\\\n"
                f"\\hline\n"
                f"\\textbf{{Số lần}} & {n_vals[0]} & {n_vals[1]} & {n_vals[2]} & {n_vals[3]} & {n_vals[4]} & {n_vals[5]} \\\\\n"
                f"\\hline\n"
                f"\\end{{tabular}}\n"
                f"\\end{{center}}\n"
                f"Khi đó:"
            )

            ################################ Nhận biết (Mốt) ################################
            nb_da_1_d = f'\\True Mốt: $M_O = {M_o}$'
            nb_da_1_s = f'Mốt: $M_O = {M_o_sai}$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = f'Mốt: $M_O = {M_o}$ (vì tần số lớn nhất là {max_n}).'
            list_nb_2 = [loigiai_nb_1]

            ################################ Thông hiểu (Q3) ########################
            th_da_1_d = f'\\True $Q_3 = {format_vn(Q_3)}$'
            th_da_1_s = f'$Q_3 = {format_vn(Q_3_sai)}$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = (
                f"Tứ phân vị thứ ba là trung vị của nửa mẫu số liệu phía trên: $x_{{51}}; x_{{52}}; \\dots ; x_{{100}}$.\\\\\n"
                f"Do đó: $Q_3 = \\frac{{1}}{{2}}(x_{{75}} + x_{{76}}) = \\frac{{1}}{{2}}({v75} + {v76}) = {format_vn(Q_3)}.$"
            )
            list_th_2 = [loigiai_th_1]

            ################################ Vận dụng (Q2) ############################
            vd_da_1_d = f'\\True Giá trị của tứ phân vị thứ hai là $Q_2 = {format_vn(Q_2)}$'
            vd_da_1_s = f'Giá trị của tứ phân vị thứ hai là $Q_2 = {format_vn(Q_2_sai)}$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = (
                f"Vì cỡ mẫu là $n = 100$, là số chẵn, nên giá trị của tứ phân vị thứ hai là\\\\\n"
                f"$Q_2 = \\frac{{1}}{{2}}(x_{{50}} + x_{{51}}) = \\frac{{1}}{{2}}({v50} + {v51}) = {format_vn(Q_2)}.$"
            )
            list_vd_2 = [loigiai_vd_1]

            ################################ Vận dụng cao (Số trung bình) ###################
            vdc_da_1_d = f'\\True Số trung bình: $\\overline{{x}} = {format_vn(x_mean)}$'
            vdc_da_1_s = f'Số trung bình: $\\overline{{x}} = {format_vn(x_mean_sai)}$'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            chuoi_tinh_tb = " + ".join([f"{x_vals[i]} \\cdot {n_vals[i]}" for i in range(6)])
            loigiai_vdc_1 = (
                f"Số trung bình: $\\overline{{x}} = \\frac{{{chuoi_tinh_tb}}}{{100}} = {format_vn(x_mean)}.$"
            )
            list_vdc_2 = [loigiai_vdc_1]

            # ==========================================
            # 4. RANDOM MỆNH ĐỀ VÀ XUẤT LATEX
            # ==========================================
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi bộ có từ 1 đến 3 đáp án đúng
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)
                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                if 1 <= count_true_answers(answers) <= 3:
                    break

            # Gán và trộn
            combined_nb = list(zip([nb_da_1], list_nb_2))
            combined_th = list(zip([th_da_1], list_th_2))
            combined_vd = list(zip([vd_da_1], list_vd_2))
            combined_vdc = list(zip([vdc_da_1], list_vdc_2))

            random.shuffle(combined_nb)
            random.shuffle(combined_th)
            random.shuffle(combined_vd)
            random.shuffle(combined_vdc)

            ans_nb, sol_nb = zip(*combined_nb)
            ans_th, sol_th = zip(*combined_th)
            ans_vd, sol_vd = zip(*combined_vd)
            ans_vdc, sol_vdc = zip(*combined_vdc)

            # Xuất kết quả
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' +
                str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(ans_nb[0]) + '}\n'
                '{' + str(ans_th[0]) + '}\n'
                '{' + str(ans_vd[0]) + '}\n'
                '{' + str(ans_vdc[0]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(sol_nb[0]) + '\n'
                '\\item ' + str(sol_th[0]) + '\n'
                '\\item ' + str(sol_vd[0]) + '\n'
                '\\item ' + str(sol_vdc[0]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n\\end{minipage}\n\n')
            return content


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


def bt_dang7_p2_b2_c3_ds10(self):
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
            # Chọn kích thước mẫu N chẵn tròn chục để tính toán đẹp
            N = random.choice([10, 20, 30, 40, 50])

            # Chọn giá trị bắt đầu x_start ngẫu nhiên từ 1 đến 10
            x_start = random.randint(1, 10)
            x_vals = [x_start + i for i in range(5)]

            # Sinh ngẫu nhiên các tần số n_i sao cho tổng bằng N và có 1 mốt duy nhất
            while True:
                n_vals = [random.randint(1, N - 4) for _ in range(5)]
                if sum(n_vals) == N:
                    max_n = max(n_vals)
                    if n_vals.count(max_n) == 1:  # Đảm bảo mốt duy nhất để bài toán rõ ràng
                        break

            # Tần số tương đối f_i
            f_vals = [n / N for n in n_vals]

            # ==========================================
            # 2. TÍNH TOÁN CÁC SỐ ĐẶC TRƯNG CHÍNH XÁC
            # ==========================================
            # Số trung bình
            x_mean = sum(x_vals[i] * f_vals[i] for i in range(5))

            # Mốt
            max_f_idx = n_vals.index(max(n_vals))
            M_o = x_vals[max_f_idx]

            # Trung vị M_e và Tứ phân vị thứ hai Q_2
            full_list = []
            for i in range(5):
                full_list.extend([x_vals[i]] * n_vals[i])

            # Do list đã được sinh theo thứ tự tăng dần nên không cần sort thêm
            idx1 = N // 2 - 1
            idx2 = N // 2
            v1 = full_list[idx1]
            v2 = full_list[idx2]
            M_e = (v1 + v2) / 2
            Q_2 = M_e

            # Tạo các giá trị sai để làm nhiễu cho đáp án sai
            M_o_sai = x_vals[(max_f_idx + 1) % 5]

            Q_2_sai = Q_2 + random.choice([-1, 1])
            if Q_2_sai == Q_2: Q_2_sai += 1

            M_e_sai = M_e + random.choice([-0.5, 0.5, 1])
            if M_e_sai == M_e: M_e_sai += 1

            x_mean_sai = round(x_mean + random.choice([-0.4, 0.4, 1.2]), 2)
            if x_mean_sai == x_mean: x_mean_sai += 1

            # ==========================================
            # 3. NỘI DUNG CÂU HỎI (BẢNG LATEX CHẠY ĐỘNG)
            # ==========================================
            noidungcauhoi = (
                f"Mẫu số liệu cho bảng tần số tương đối dưới đây:\n"
                f"\\begin{{center}}\n"
                f"\\begin{{tabular}}{{|l|c|c|c|c|c|}}\n"
                f"\\hline\n"
                f"Giá trị $x_i$ & {x_vals[0]} & {x_vals[1]} & {x_vals[2]} & {x_vals[3]} & {x_vals[4]} \\\\\n"
                f"\\hline\n"
                f"Tần số tương đối $f_i$ & {format_vn(f_vals[0])} & {format_vn(f_vals[1])} & {format_vn(f_vals[2])} & {format_vn(f_vals[3])} & {format_vn(f_vals[4])} \\\\\n"
                f"\\hline\n"
                f"\\end{{tabular}}\n"
                f"\\end{{center}}\n"
                f"Biết kích thước mẫu là {N}. Khi đó:"
            )

            ################################ Nhận biết (Mốt) ################################
            nb_da_1_d = f'\\True Mốt: $M_o = {M_o}$'
            nb_da_1_s = f'Mốt: $M_o = {M_o_sai}$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = f'Mốt: $M_o = {M_o}$.'
            list_nb_2 = [loigiai_nb_1]

            ################################ Thông hiểu (Tứ phân vị) ########################
            th_da_1_d = f'\\True Tứ phân vị thứ hai là $Q_2 = {format_vn(Q_2)}$'
            th_da_1_s = f'Tứ phân vị thứ hai là $Q_2 = {format_vn(Q_2_sai)}$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = f'Tứ phân vị thứ hai là $Q_2 = M_e = {format_vn(Q_2)}$.'
            list_th_2 = [loigiai_th_1]

            ################################ Vận dụng (Trung vị) ############################
            vd_da_1_d = f'\\True $M_e = {format_vn(M_e)}$'
            vd_da_1_s = f'$M_e = {format_vn(M_e_sai)}$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = (
                f"Ta sắp xếp mẫu thành dãy số liệu không giảm.\\\\\n"
                f"Do kích thước mẫu là {N} (chẵn) nên trung vị là trung bình cộng giá trị của mẫu số liệu "
                f"thứ {N//2} và {N//2+1}: $M_e = \\frac{{1}}{{2}}({v1} + {v2}) = {format_vn(M_e)}.$"
            )
            list_vd_2 = [loigiai_vd_1]

            ################################ Vận dụng cao (Số trung bình) ###################
            vdc_da_1_d = f'\\True Số trung bình: $\\overline{{x}} = {format_vn(x_mean)}$'
            vdc_da_1_s = f'Số trung bình: $\\overline{{x}} = {format_vn(x_mean_sai)}$'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = (
                f"Số trung bình: $\\overline{{x}} = {x_vals[0]} \\cdot {format_vn(f_vals[0])} + "
                f"{x_vals[1]} \\cdot {format_vn(f_vals[1])} + {x_vals[2]} \\cdot {format_vn(f_vals[2])} + "
                f"{x_vals[3]} \\cdot {format_vn(f_vals[3])} + {x_vals[4]} \\cdot {format_vn(f_vals[4])} = {format_vn(x_mean)}.$"
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
                true_count = count_true_answers(answers)
                if 1 <= true_count <= 3:
                    break

            # Gán lại vào list và trộn
            list_nb_1 = [nb_da_1]
            list_th_1 = [th_da_1]
            list_vd_1 = [vd_da_1]
            list_vdc_1 = [vdc_da_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            combined_th = list(zip(list_th_1, list_th_2))
            combined_vd = list(zip(list_vd_1, list_vd_2))
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            random.shuffle(combined_nb)
            random.shuffle(combined_th)
            random.shuffle(combined_vd)
            random.shuffle(combined_vdc)

            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # Xuất câu hỏi dưới định dạng mã LaTeX
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' +
                str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(shuffled_answers_nb[0]) + '}\n'
                '{' + str(shuffled_answers_th[0]) + '}\n'
                '{' + str(shuffled_answers_vd[0]) + '}\n'
                '{' + str(shuffled_answers_vdc[0]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(shuffled_solutions_nb[0]) + '\n'
                '\\item ' + str(shuffled_solutions_th[0]) + '\n'
                '\\item ' + str(shuffled_solutions_vd[0]) + '\n'
                '\\item ' + str(shuffled_solutions_vdc[0]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n\\end{minipage}\n\n')
            return content


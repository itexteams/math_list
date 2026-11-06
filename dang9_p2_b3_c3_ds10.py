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


def bt_dang9_p2_b3_c3_ds10(self):
            # Khai báo biến
            # Hàm chuẩn hóa số thập phân sang định dạng Việt Nam (dùng dấu phẩy)
            def format_vn(num):
                if num == int(num):
                    return str(int(num))
                return "{:.2f}".format(num).replace('.', ',').rstrip('0').rstrip(',') if '.' in "{:.2f}".format(num) else "{:.2f}".format(num).replace('.', ',')

            # Sinh dữ liệu ngẫu nhiên cho bảng tần số
            values = list(range(1, 15))
            freq_A = [random.randint(0, 5) for _ in range(14)]
            freq_B = [random.randint(0, 5) for _ in range(14)]

            # Đảm bảo tổng tần số không bằng 0
            if sum(freq_A) == 0: freq_A[random.randint(0, 13)] = random.randint(1, 5)
            if sum(freq_B) == 0: freq_B[random.randint(0, 13)] = random.randint(1, 5)

            n_A = sum(freq_A)
            n_B = sum(freq_B)

            # Tính toán các thông số thống kê chính xác
            mean_A = sum(v * f for v, f in zip(values, freq_A)) / n_A
            var_A = sum(f * (v - mean_A)**2 for v, f in zip(values, freq_A)) / n_A
            std_A = math.sqrt(var_A)

            mean_B = sum(v * f for v, f in zip(values, freq_B)) / n_B
            var_B = sum(f * (v - mean_B)**2 for v, f in zip(values, freq_B)) / n_B
            std_B = math.sqrt(var_B)

            # Làm tròn 2 chữ số thập phân
            mean_A = round(mean_A, 2)
            var_A = round(var_A, 2)
            std_A = round(std_A, 2)
            mean_B = round(mean_B, 2)
            var_B = round(var_B, 2)
            std_B = round(std_B, 2)

            # Tạo chuỗi LaTeX cho Bảng A
            table_A = "\\begin{tabular}{|l|" + "c|" * 14 + "}\n\\hline\nGiá trị"
            for v in values: table_A += f" & {v}"
            table_A += " \\\\\n\\hline\nTần số"
            for f in freq_A: table_A += f" & {f}"
            table_A += " \\\\\n\\hline\n\\end{tabular}"

            # Tạo chuỗi LaTeX cho Bảng B
            table_B = "\\begin{tabular}{|l|" + "c|" * 14 + "}\n\\hline\nGiá trị"
            for v in values: table_B += f" & {v}"
            table_B += " \\\\\n\\hline\nTần số"
            for f in freq_B: table_B += f" & {f}"
            table_B += " \\\\\n\\hline\n\\end{tabular}"

            # Nội dung câu hỏi
            noidungcauhoi = (f"Cho hai mẫu số liệu $A$ và $B$ được cho dưới dạng tần số như sau:\n\n"
                             f"Mẫu A:\n\n\\begin{{center}}\n{table_A}\n\\end{{center}}\n"
                             f"Mẫu B:\n\n\\begin{{center}}\n{table_B}\n\\end{{center}}")

            ######################################################################## Nhận biết ############################################
            fake_mean_A = round(mean_A + random.choice([-1.15, 1.25, 0.82, -0.95]), 2)
            nb_da_1_d = f"\\True Với mẫu A ta có: giá trị trung bình $\\overline{{x_A}} = {format_vn(mean_A)}$"
            nb_da_1_s = f"Với mẫu A ta có: giá trị trung bình $\\overline{{x_A}} = {format_vn(fake_mean_A)}$"
            list_nb_da_1=[nb_da_1_d, nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)
            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = (f"Với mẫu A ta có: giá trị trung bình $\\overline{{x_A}} = {format_vn(mean_A)}$.")
            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            fake_var_B = round(var_B + random.choice([-2.12, 1.34, 3.15, -1.55]), 2)
            th_da_1_d = f"\\True Với mẫu B ta có phương sai $s_B^2 = {format_vn(var_B)}$"
            th_da_1_s = f"Với mẫu B ta có phương sai $s_B^2 = {format_vn(fake_var_B)}$"
            list_th_da_1=[th_da_1_d, th_da_1_s]
            th_da_1=random.choice(list_th_da_1)
            list_th_1 = [th_da_1]

            loigiai_th_1 = (f"Với mẫu $B$ ta có: giá trị trung bình $\\overline{{x_B}} = {format_vn(mean_B)}$, "
                            f"phương sai $s_B^2 = {format_vn(var_B)}$ và độ lệch chuẩn $s_B = {format_vn(std_B)}$.")
            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            fake_std_A = round(std_A + random.choice([-1.05, 0.75, 1.25, -0.85]), 2)
            vd_da_1_d = f"\\True Với mẫu A ta có độ lệch chuẩn $s_A = {format_vn(std_A)}$"
            vd_da_1_s = f"Với mẫu A ta có độ lệch chuẩn $s_A = {format_vn(fake_std_A)}$"
            list_vd_da_1=[vd_da_1_d, vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)
            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = (f"Phương sai $s_A^2 = {format_vn(var_A)}$ và độ lệch chuẩn $s_A = {format_vn(std_A)}$.")
            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            if std_A > std_B:
                vdc_da_1_d = "\\True Mẫu $A$ có độ phân tán cao hơn mẫu $B$"
                vdc_da_1_s = "Mẫu $B$ có độ phân tán cao hơn mẫu $A$"
                lg_vdc = f"Vì $s_A > s_B$ ($ {format_vn(std_A)} > {format_vn(std_B)} $) nên ta có thể khẳng định mẫu $A$ có độ phân tán cao hơn mẫu $B$."
            elif std_B > std_A:
                vdc_da_1_d = "\\True Mẫu $B$ có độ phân tán cao hơn mẫu $A$"
                vdc_da_1_s = "Mẫu $A$ có độ phân tán cao hơn mẫu $B$"
                lg_vdc = f"Vì $s_B > s_A$ ($ {format_vn(std_B)} > {format_vn(std_A)} $) nên ta có thể khẳng định mẫu $B$ có độ phân tán cao hơn mẫu $A$."
            else:
                vdc_da_1_d = "\\True Mẫu $A$ và mẫu $B$ có độ phân tán bằng nhau"
                vdc_da_1_s = "Mẫu $A$ có độ phân tán cao hơn mẫu $B$"
                lg_vdc = f"Vì $s_A = s_B = {format_vn(std_A)}$ nên hai mẫu có độ phân tán bằng nhau."

            list_vdc_da_1=[vdc_da_1_d, vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)
            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = lg_vdc
            list_vdc_2 = [loigiai_vdc_1]

            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 đúng
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)
                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)
                if 1 <= true_count <= 3:
                    break

            # Gán lại vào list
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

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n'+
                       str(noidungcauhoi)+ '\n'
                       '\\choiceTFn \n'
                       '{'+str(shuffled_answers_nb[0])+'}\n'
                       '{'+str(shuffled_answers_th[0])+'}\n'
                       '{'+str(shuffled_answers_vd[0])+'}\n'
                       '{'+str(shuffled_answers_vdc[0])+'}\n'
                       '\\loigiai{ \n'
                       '\\begin{enumEX}[a)]{1} \n'
                       '\\item '+str(shuffled_solutions_nb[0])+'\n'
                       '\\item '+str(shuffled_solutions_th[0])+'\n'
                       '\\item '+str(shuffled_solutions_vd[0])+'\n'
                       '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                       '\\end{enumEX}} \n'
                       '\\end{ex}\n\\end{minipage}\n\n')
            return content


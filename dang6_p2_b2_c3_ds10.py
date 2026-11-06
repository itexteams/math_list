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


def bt_dang6_p2_b2_c3_ds10(self):
    import statistics  # Bổ sung import để tránh NameError nếu file chưa import bên ngoài

    # Khai báo biến
    # Khởi tạo dữ liệu ngẫu nhiên có cỡ mẫu n=10
    # Cố tình tạo một giá trị mode xuất hiện 3 lần để đảm bảo bài toán có mốt rõ ràng
    base_val = random.randint(110, 115)
    mode_val = random.randint(base_val, base_val + 3)
    data = [mode_val] * 3

    # Thêm 7 giá trị ngẫu nhiên khác sao cho không vượt qua tần số của mode
    while len(data) < 10:
        val = random.randint(base_val - 2, base_val + 6)
        if data.count(val) < 2:
            data.append(val)

    random.shuffle(data)

    # Tính toán các thông số
    sorted_data = sorted(data)

    # (a) Trung bình
    mean_val = sum(data) / 10
    mean_str = f"{mean_val:g}".replace('.', ',')
    sum_str = "+".join(map(str, data))

    # (b) Chuỗi sắp xếp
    sorted_str = " ".join(map(str, sorted_data))

    # Tạo một chuỗi sắp xếp sai (đảo vị trí 2 phần tử liền kề khác nhau)
    fake_sorted = sorted_data.copy()
    for i in range(len(fake_sorted) - 1):
        if fake_sorted[i] < fake_sorted[i+1]:
            fake_sorted[i], fake_sorted[i+1] = fake_sorted[i+1], fake_sorted[i]
            break
    fake_sorted_str = " ".join(map(str, fake_sorted))

    # (c) Trung vị
    median_val = (sorted_data[4] + sorted_data[5]) / 2
    median_str = f"{median_val:g}".replace('.', ',')

    # (d) Mốt
    real_mode = mode_val  # Do đã chủ đích tạo mode_val xuất hiện 3 lần, an toàn tuyệt đối
    mode_count = data.count(real_mode)

    # Tìm một mốt giả (là một phần tử có trong list nhưng không phải mode thật)
    fake_mode = random.choice(list(set(data) - {real_mode}))

    # Bảng LaTeX dữ liệu
    table_latex = "\\begin{tabular}{|" + "c|"*10 + "}\n\\hline\n"
    table_latex += " & ".join(map(str, data)) + " \\\\\n\\hline\n\\end{tabular}"

    # Nội dung câu hỏi
    noidungcauhoi = f"Cho mẫu số liệu thống kê về sản lượng chè thu được trong 1 năm (kg/sào) của 10 hộ gia đình:\n\\begin{{center}}\n{table_latex}\n\\end{{center}}\nKhi đó:"

    ######################################################################## Nhận biết ############################################

    # Các đáp án
    nb_da_1_d = f'\\True Sản lượng chè trung bình thu được trong một năm của mỗi gia đình là $\\approx {mean_str}$ (kg/sào)'
    fake_mean = round(mean_val + random.choice([-0.5, 0.5, 1.2, -1.2]), 1)
    fake_mean_str = f"{fake_mean:g}".replace('.', ',')
    nb_da_1_s = f'Sản lượng chè trung bình thu được trong một năm của mỗi gia đình là $\\approx {fake_mean_str}$ (kg/sào)'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    list_nb_1 = [nb_da_1]

    # Nội dung lời giải
    loigiai_nb_1 = f"Sản lượng chè trung bình thu được trong một năm của mỗi gia đình là: \\\\ \n$\\overline{{x}} = \\dfrac{{{sum_str}}}{{10}} = {mean_str}$ (kg/sào)."
    list_nb_2 = [loigiai_nb_1]

    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

    ######################################################################## Thông hiểu ############################################

    # Các đáp án
    th_da_1_d = f'\\True Ta viết lại mẫu số liệu trên theo thứ tự không giảm: \\\\ \n\\centerline{{{sorted_str}}}'
    th_da_1_s = f'Ta viết lại mẫu số liệu trên theo thứ tự không giảm: \\\\ \n\\centerline{{{fake_sorted_str}}}'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    list_th_1 = [th_da_1]

    # Nội dung lời giải
    loigiai_th_1 = f"Ta viết lại mẫu số liệu trên theo thứ tự không giảm: \\\\ \n\\centerline{{{sorted_str}}}"
    list_th_2 = [loigiai_th_1]

    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

    ######################################################################## Vận dụng ############################################

    # Các đáp án
    vd_da_1_d = f'\\True Số trung vị là ${median_str}$'
    fake_median = median_val + random.choice([-0.5, 0.5, 1, -1])
    fake_median_str = f"{fake_median:g}".replace('.', ',')
    vd_da_1_s = f'Số trung vị là ${fake_median_str}$'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    list_vd_1 = [vd_da_1]

    # Nội dung lời giải
    loigiai_vd_1 = f"Vì số giá trị của mẫu $n=10$ (chẵn) nên trung bình cộng hai số chính giữa mẫu đã sắp xếp là trung vị. \\\\\nVậy trung vị là: $\\dfrac{{{sorted_data[4]} + {sorted_data[5]}}}{{2}} = {median_str}$."
    list_vd_2 = [loigiai_vd_1]

    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

    ######################################################################## Vận dụng cao ############################################

    # Các đáp án
    vdc_da_1_d = f'\\True ${real_mode}$ là mốt của mẫu số liệu đã cho'
    vdc_da_1_s = f'${fake_mode}$ là mốt của mẫu số liệu đã cho'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    list_vdc_1 = [vdc_da_1]

    # Nội dung lời giải
    loigiai_vdc_1 = f"Trong mẫu trên, giá trị ${real_mode}$ xuất hiện nhiều nhất ({mode_count} lần) nên ${real_mode}$ là mốt của mẫu số liệu đã cho."
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
               '\\end{ex}\n'
               '\\end{minipage}\n\n')
    return content


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


def bt_dang13_p2_b3_c3_ds10(self):
            # Khai báo biến
            # Khai báo hàm đếm số đáp án đúng
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Định dạng số phẩy của Việt Nam thay vì dấu chấm
            def format_num(num):
                return f"{num:g}".replace('.', ',')

            ######################################################################## Xử lý Data Random ########################

            # Sinh ngẫu nhiên 10 dữ liệu
            # 9 số đầu lấy ngẫu nhiên từ 1 đến 15
            data_part = sorted([random.randint(1, 15) for _ in range(9)])
            # Số thứ 10 cố tình tạo một khoảng cách để kiểm tra giá trị bất thường
            outlier = data_part[-1] + random.randint(10, 20)
            data = data_part + [outlier]

            # Tính toán các đại lượng thống kê thực tế
            n = 10
            sum_data = sum(data)
            mean_val = sum_data / n
            mean_str = format_num(mean_val)

            q1 = data[2]
            q2 = (data[4] + data[5]) / 2
            q3 = data[7]
            delta_q = q3 - q1

            q2_str = format_num(q2)

            sum_sq_diff = sum((val - mean_val)**2 for val in data)
            variance = sum_sq_diff / n
            variance_str = format_num(variance)

            std_dev = math.sqrt(variance)
            std_dev_round = round(std_dev, 2)
            std_dev_str = format_num(std_dev_round)

            # Chuỗi số liệu để in ra đề bài
            data_str_display = " \\quad ".join(map(str, data))

            # Nội dung câu hỏi
            noidungcauhoi = f"Mẫu số liệu dưới đây thống kê thời gian chờ xe bus (đơn vị: phút) của 10 học sinh ở cùng một bến: ${data_str_display}$."

            ######################################################################## Nhận biết ############################################

            # Đáp án sai ngẫu nhiên
            mean_fake = mean_val + random.choice([-1.2, 1.5, 2.1, -0.8])
            mean_fake_str = format_num(round(mean_fake, 1))

            # Các đáp án
            nb_da_1_d = f'\\True Số trung bình cộng của mẫu số liệu là: $\\overline{{x}} = {mean_str}$ (phút)'
            nb_da_1_s = f'Số trung bình cộng của mẫu số liệu là: $\\overline{{x}} = {mean_fake_str}$ (phút)'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            # Nội dung lời giải
            sum_str_display = "+".join(map(str, data))
            loigiai_nb_1 = f"Số trung bình cộng của mẫu số liệu là:\\\\ $\\overline{{x}} = \\frac{{{sum_str_display}}}{{{n}}} = {mean_str}$ (phút)."
            list_nb_2 = [loigiai_nb_1]

            ######################################################################## Thông hiểu ############################################

            # Đáp án sai ngẫu nhiên
            delta_q_fake = delta_q + random.choice([-2, -1, 1, 2])

            # Các đáp án
            th_da_1_d = f'\\True Khoảng tứ phân vị của mẫu số liệu là: $\\Delta_Q = {delta_q}$ (phút)'
            th_da_1_s = f'Khoảng tứ phân vị của mẫu số liệu là: $\\Delta_Q = {delta_q_fake}$ (phút)'
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            # Nội dung lời giải
            loigiai_th_1 = (f"Mẫu số liệu đã sắp xếp theo thứ tự không giảm.\\\\"
                            f"Trung vị của mẫu số liệu là: $\\frac{{{data[4]}+{data[5]}}}{{2}} = {q2_str}$ (phút).\\\\"
                            f"Trung vị của dãy gồm 5 số liệu đầu tiên là $Q_1 = {q1}$. Trung vị của dãy gồm 5 số liệu cuối cùng là $Q_3 = {q3}$.\\\\"
                            f"Vậy khoảng tứ phân vị của mẫu số liệu là: $\\Delta_Q = {q3} - {q1} = {delta_q}$ (phút).")
            list_th_2 = [loigiai_th_1]

            ######################################################################## Vận dụng ############################################

            # Đáp án sai ngẫu nhiên
            std_dev_fake = round(std_dev + random.choice([-1.15, 1.25, 2.05]), 2)
            std_dev_fake_str = format_num(std_dev_fake)

            # Các đáp án
            vd_da_1_d = f'\\True Độ lệch chuẩn của mẫu số liệu là: $s \\approx {std_dev_str}$ (phút)'
            vd_da_1_s = f'Độ lệch chuẩn của mẫu số liệu là: $s \\approx {std_dev_fake_str}$ (phút)'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            # Tạo rút gọn biểu thức phương sai để lời giải không bị dài
            var_terms = [f"({data[0]}-{mean_str})^2", f"({data[1]}-{mean_str})^2", "\\dots", f"({data[-1]}-{mean_str})^2"]
            var_str_display = " + ".join(var_terms)

            # Nội dung lời giải
            loigiai_vd_1 = (f"Ta có: ${var_str_display} = {format_num(sum_sq_diff)}$.\\\\"
                            f"Suy ra phương sai của mẫu số liệu là: $s^2 = \\frac{{{format_num(sum_sq_diff)}}}{{{n}}} = {variance_str}$.\\\\"
                            f"Độ lệch chuẩn của mẫu số liệu là: $s = \\sqrt{{{variance_str}}} \\approx {std_dev_str}$ (phút).")
            list_vd_2 = [loigiai_vd_1]

            ######################################################################## Vận dụng cao ########################################

            upper_bound = q3 + 1.5 * delta_q
            upper_bound_str = format_num(upper_bound)
            is_outlier = data[-1] > upper_bound

            if is_outlier:
                vdc_da_1_d = f'\\True ${data[-1]}$ là giá trị bất thường của mẫu số liệu'
                vdc_da_1_s = f'${data[-1]}$ không phải là giá trị bất thường của mẫu số liệu'
                ket_luan = f"Vì ${data[-1]} > {upper_bound_str}$ nên ${data[-1]}$ là giá trị bất thường của mẫu số liệu."
            else:
                vdc_da_1_d = f'\\True ${data[-1]}$ không phải là giá trị bất thường của mẫu số liệu'
                vdc_da_1_s = f'${data[-1]}$ là giá trị bất thường của mẫu số liệu'
                ket_luan = f"Vì ${data[-1]} \\le {upper_bound_str}$ nên ${data[-1]}$ không phải là giá trị bất thường của mẫu số liệu."

            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            # Nội dung lời giải
            loigiai_vdc_1 = (f"Ta có giới hạn trên của mẫu số liệu để xác định giá trị ngoại lệ là:\\\\"
                             f"$Q_3 + 1,5\\Delta_Q = {q3} + 1,5 \\cdot {delta_q} = {upper_bound_str}$.\\\\"
                             f"{ket_luan}")
            list_vdc_2 = [loigiai_vdc_1]

            ######################################################################## Xáo trộn và in kết quả ###############################

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
                '\\end{ex}\n'
                '\\end{minipage}\n\n')
            return content


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


def bt_dang5_p2_b2_c3_ds10(self):
            # Khai báo biến
            # Sinh dữ liệu ngẫu nhiên
            # 10 mức lương bình thường tập trung quanh 20000 - 22000
            normal_salaries = [random.randint(2000, 2200) * 10 for _ in range(10)]
            # 2 mức lương ngoại lai (rất cao) để minh họa cho câu d
            outlier_1 = random.randint(7000, 8000) * 10
            outlier_2 = random.randint(12000, 15000) * 10

            data = normal_salaries + [outlier_1, outlier_2]
            random.shuffle(data)

            # Tạo bảng LaTeX 3x4
            table_latex = "\\begin{tabular}{|c|c|c|c|}\n\\hline\n"
            table_latex += f"{data[0]} & {data[1]} & {data[2]} & {data[3]} \\\\\n\\hline\n"
            table_latex += f"{data[4]} & {data[5]} & {data[6]} & {data[7]} \\\\\n\\hline\n"
            table_latex += f"{data[8]} & {data[9]} & {data[10]} & {data[11]} \\\\\n\\hline\n" + "\\end{tabular}"

            # Tính toán các đặc trưng mẫu
            total_sum = sum(data)
            mean_val = round(total_sum / 12, 1)
            mean_str = f"{mean_val:g}".replace('.', ',')

            sorted_data = sorted(data)
            # SỬA LỖI: Dùng dấu chấm phẩy để ngăn cách các số, tránh bị dính liền trong môi trường toán học LaTeX
            sorted_str = "; ".join(map(str, sorted_data))

            max_val = sorted_data[-1]
            second_max = sorted_data[-2]

            # Vì n = 12 (chẵn) nên trung vị là trung bình cộng của x_6 và x_7 (index 5 và 6)
            median_val = (sorted_data[5] + sorted_data[6]) / 2
            median_str = f"{median_val:g}".replace('.', ',')

            # Nội dung câu hỏi
            noidungcauhoi = f"Bảng số liệu sau cho biết mức lương hàng năm của các cán bộ và nhân viên trong một công ty (đơn vị: nghìn đồng).\n\\begin{{center}}\n{table_latex}\n\\end{{center}}\nKhi đó:"

            ######################################################################## Nhận biết ############################################

            # Các đáp án (SỬA LỖI: Đã bỏ dấu chấm ở cuối câu)
            nb_da_1_d = f'\\True Mức lương trung bình các cán bộ nhân viên là: $\\overline{{x}} = {mean_str}$ (nghìn đồng)'
            fake_mean = round(mean_val + random.choice([-100.5, 100.5, 50.5, -50.5]), 1)
            fake_mean_str = f"{fake_mean:g}".replace('.', ',')
            nb_da_1_s = f'Mức lương trung bình các cán bộ nhân viên là: $\\overline{{x}} = {fake_mean_str}$ (nghìn đồng)'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = (f"Mức lương trung bình các cán bộ nhân viên là: \\\\\n"
                            f"$\\overline{{x}} = \\dfrac{{{data[0]} + {data[1]} + \\dots + {data[-1]}}}{{12}} = {mean_str}$ (nghìn đồng).")
            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################

            # Các đáp án
            th_da_1_d = f'\\True Mức lương lớn nhất là ${max_val}$'
            th_da_1_s = f'Mức lương lớn nhất là ${second_max}$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = (f"Sắp theo thứ tự không giảm bảng lương ta được: \\\\\n"
                            f"${sorted_str}$;\\\\ ($n=12$).\n"
                            f"Mức lương lớn nhất là: ${max_val}$")
            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################

            # Các đáp án (SỬA LỖI: Đã bỏ dấu chấm ở cuối câu)
            vd_da_1_d = f'\\True Số trung vị là: ${median_str}$ (nghìn đồng)'
            fake_median = median_val + random.choice([-50, 50, 100, -100])
            fake_median_str = f"{fake_median:g}".replace('.', ',')
            vd_da_1_s = f'Số trung vị là: ${fake_median_str}$ (nghìn đồng)'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = f"Số trung vị là: $\\dfrac{{{sorted_data[5]} + {sorted_data[6]}}}{{2}} = {median_str}$ (nghìn đồng)."
            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################

            # Các đáp án (SỬA LỖI: Đã bỏ dấu chấm ở cuối câu)
            vdc_da_1_d = '\\True Không thể lấy mức lương bình quân làm giá trị đại diện'
            vdc_da_1_s = 'Có thể lấy mức lương bình quân làm giá trị đại diện'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ("Ý nghĩa: Nên dùng số trung vị làm đại diện cho mức lương của cán bộ nhân viên công ty, "
                             "vì trong trường hợp này chênh lệch giữa các số liệu quá lớn (xuất hiện các mức lương ngoại lai rất cao) "
                             "nên mức lương bình quân bị kéo lệch, không thể lấy làm giá trị đại diện.")
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


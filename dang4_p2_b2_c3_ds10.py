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


def bt_dang4_p2_b2_c3_ds10(self):
            # Khai báo biến
            # Sinh dữ liệu ngẫu nhiên: 30 học sinh, số giờ học từ 0 đến 10
            data = [random.randint(0, 10) for _ in range(30)]

            # Cắt thành 2 dòng (mỗi dòng 15 số) để hiển thị bảng giống đề bài
            row1 = data[:15]
            row2 = data[15:]

            # Tạo bảng dữ liệu LaTeX (Bảng chưa sắp xếp)
            table_latex = "\\begin{tabular}{|" + "c|"*15 + "}\n\\hline\n"
            table_latex += " & ".join(map(str, row1)) + " \\\\\n\\hline\n"
            table_latex += " & ".join(map(str, row2)) + " \\\\\n\\hline\n\\end{tabular}"

            # Tính toán các thông số thống kê thực tế
            sorted_data = sorted(data)
            max_val = sorted_data[-1]

            # Tính số trung bình (làm tròn 1 chữ số thập phân, đổi dấu chấm thành phẩy cho chuẩn VN)
            mean_val = round(sum(data) / 30, 1)
            mean_str = f"{mean_val}".replace('.', ',')

            # Tính Q2 (Trung bình cộng phần tử thứ 15 và 16 - index 14 và 15)
            q2_val = (sorted_data[14] + sorted_data[15]) / 2
            q2_str = f"{q2_val:g}".replace('.', ',')

            # Tính Q1 (Trung vị của nửa trái gồm 15 phần tử đầu tiên -> phần tử thứ 8 - index 7)
            q1_val = sorted_data[7]
            q1_str = f"{q1_val:g}".replace('.', ',')

            # Tạo bảng dữ liệu LaTeX đã sắp xếp (cho phần lời giải)
            sorted_row1 = sorted_data[:15]
            sorted_row2 = sorted_data[15:]
            sorted_table = "\\begin{tabular}{|" + "c|"*15 + "}\n\\hline\n"
            sorted_table += " & ".join(map(str, sorted_row1)) + " \\\\\n\\hline\n"
            sorted_table += " & ".join(map(str, sorted_row2)) + " \\\\\n\\hline\n\\end{tabular}"

            # Nội dung câu hỏi
            noidungcauhoi = f"Số giờ học thêm ngoài trường học của 30 học sinh được thống kê như sau:\n\\begin{{center}}\n{table_latex}\n\\end{{center}}\nKhi đó:"

            ######################################################################## Nhận biết ############################################

            # Các đáp án
            nb_da_1_d = f'\\True Số giờ học thêm ngoài trường học của 30 học sinh lớn nhất là {max_val}'
            fake_max = max_val + random.choice([-1, 1, 2])
            if fake_max < 0: fake_max = max_val + 1
            nb_da_1_s = f'Số giờ học thêm ngoài trường học của 30 học sinh lớn nhất là {fake_max}'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = f"Sắp xếp lại mẫu dữ liệu theo thứ tự tăng dần ta được:\n\\begin{{center}}\n{sorted_table}\n\\end{{center}}\nSố giờ học thêm ngoài trường học của 30 học sinh lớn nhất là {max_val}."
            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################

            # Các đáp án
            th_da_1_d = f'\\True Số trung bình là {mean_str}'
            fake_mean = round(mean_val + random.choice([-0.2, 0.2, 0.5, -0.5, 1.0]), 1)
            fake_mean_str = f"{fake_mean}".replace('.', ',')
            th_da_1_s = f'Số trung bình là {fake_mean_str}'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = f"Số trung bình là $\\overline{{x}} = \\frac{{{sum(data)}}}{{30}} \\approx {mean_str}$.\nĐiều này nói lên rằng trung bình một học sinh sử dụng {mean_str} giờ cho việc học thêm ngoài trường."
            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################

            # Các đáp án
            vd_da_1_d = f'\\True $Q_2 = {q2_str}$'
            fake_q2 = q2_val + random.choice([-0.5, 0.5, 1, -1])
            if fake_q2 < 0: fake_q2 = q2_val + 1
            fake_q2_str = f"{fake_q2:g}".replace('.', ',')
            vd_da_1_s = f'$Q_2 = {fake_q2_str}$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = f"Cỡ mẫu $n=30$ là số chẵn nên trung vị là trung bình cộng của hai giá trị chính giữa (thứ 15 và 16).\nSố trung vị $Q_2 = \\frac{{{sorted_data[14]} + {sorted_data[15]}}}{{2}} = {q2_str}$."
            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################

            # Các đáp án
            vdc_da_1_d = f'\\True $Q_1 = {q1_str}$'
            fake_q1 = q1_val + random.choice([-1, 1, 2])
            if fake_q1 < 0: fake_q1 = q1_val + 1
            fake_q1_str = f"{fake_q1:g}".replace('.', ',')
            vdc_da_1_s = f'$Q_1 = {fake_q1_str}$'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = f"Nửa dữ liệu bên trái $Q_2$ gồm 15 giá trị. Cỡ mẫu này là số lẻ nên trung vị của nửa này là giá trị chính giữa (thứ 8).\nSố trung vị của nửa bên trái $Q_2$ là $Q_1 = {q1_str}$."
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


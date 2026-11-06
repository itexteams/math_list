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


def bt_dang5_p2_b3_c3_ds10(self):
            # Khai báo biến
            # Hàm hỗ trợ định dạng số thập phân dùng dấu phẩy (chuẩn Việt Nam)
            def format_num(num):
                if num == int(num):
                    return str(int(num))
                return str(num).replace('.', ',')

            # ==============================================================================
            # B3 - TẠO DỮ LIỆU NGẪU NHIÊN VÀ TÍNH TOÁN
            # ==============================================================================
            while True:
                # Tạo 18 giá trị cốt lõi xoay quanh trung bình
                core_data = [random.randint(36, 45) for _ in range(18)]
                # Tạo 2 giá trị bất thường ở hai đầu
                outlier_low = random.randint(25, 30)
                outlier_high = random.randint(48, 55)

                data = core_data + [outlier_low, outlier_high]
                random.shuffle(data)

                sorted_data = sorted(data)
                min_val = sorted_data[0]
                max_val = sorted_data[-1]

                # Tính các tứ phân vị (Mẫu N=20)
                Q1 = (sorted_data[4] + sorted_data[5]) / 2
                Q2 = (sorted_data[9] + sorted_data[10]) / 2
                Q3 = (sorted_data[14] + sorted_data[15]) / 2

                delta_Q = Q3 - Q1
                if delta_Q > 0: # Đảm bảo có độ lệch
                    low_threshold = Q1 - 1.5 * delta_Q
                    high_threshold = Q3 + 1.5 * delta_Q

                    outliers = [x for x in sorted_data if x < low_threshold or x > high_threshold]

                    # Chỉ lấy bộ dữ liệu nếu đúng 2 giá trị min và max là giá trị bất thường
                    if len(outliers) == 2 and outliers[0] == min_val and outliers[1] == max_val:
                        break

            # ==============================================================================
            # B2 - XUẤT CÂU HỎI VÀ LỜI GIẢI THEO TEMPLATE
            # ==============================================================================

            # Chia dữ liệu thành 2 hàng để hiển thị trong bảng
            row1 = " & ".join(map(str, data[:10]))
            row2 = " & ".join(map(str, data[10:]))

            # Nội dung câu hỏi
            noidungcauhoi = (f'''Một cơ sở chăn nuôi gia cầm tiến hành nuôi thử nghiệm giống gà đẻ trứng mới. Khi gà đã cho trứng họ tiến hành khảo sát với 20 quả được cân nặng (gam) như sau:
            \\begin{{center}}
            \\begin{{tabular}}{{|c|c|c|c|c|c|c|c|c|c|}}
            \\hline
            {row1} \\\\
            \\hline
            {row2} \\\\
            \\hline
            \\end{{tabular}}
            \\end{{center}}
            Khi đó:''')

            ######################################################################## Nhận biết ############################################

            nb_da_1_d = f'\\True Giá trị nhỏ nhất của mẫu là ${min_val}$'
            nb_da_1_s = f'Giá trị nhỏ nhất của mẫu là ${min_val + random.randint(1, 3)}$'
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)
            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = (f'''Sắp xếp mẫu theo thứ tự tăng dần, ta tìm được giá trị nhỏ nhất của mẫu là ${min_val}$.''')
            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################

            th_da_1_d = f'\\True Giá trị lớn nhất của mẫu là ${max_val}$'
            th_da_1_s = f'Giá trị lớn nhất của mẫu là ${max_val - random.randint(1, 3)}$'
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)
            list_th_1 = [th_da_1]

            loigiai_th_1 = (f'''Giá trị lớn nhất của mẫu là ${max_val}$.''')
            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################

            vd_da_1_d = f'\\True Khoảng tứ phân vị: $\\Delta_Q = {format_num(delta_Q)}$'
            vd_da_1_s = f'Khoảng tứ phân vị: $\\Delta_Q = {format_num(delta_Q + random.choice([0.5, 1, 1.5]))}$'
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)
            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = (f'''Ta có $Q_1 = {format_num(Q1)}; Q_2 = {format_num(Q2)}$ và $Q_3 = {format_num(Q3)}$. \\\\
            Khoảng tứ phân vị: $\\Delta_Q = {format_num(Q3)} - {format_num(Q1)} = {format_num(delta_Q)}$.''')

            list_vd_2 = [loigiai_vd_1]
            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################

            vdc_da_1_d = f'\\True Các giá trị bất thường là ${min_val}$ và ${max_val}$'
            vdc_da_1_s = f'Các giá trị bất thường là ${min_val + 1}$ và ${max_val - 1}$'
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)
            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = (f'''Ta có $Q_1 - 1,5 \\cdot \\Delta_Q = {format_num(Q1)} - 1,5 \\cdot {format_num(delta_Q)} = {format_num(low_threshold)}$ và $Q_3 + 1,5 \\cdot \\Delta_Q = {format_num(Q3)} + 1,5 \\cdot {format_num(delta_Q)} = {format_num(high_threshold)}$. \\\\
            Vì ${min_val} < {format_num(low_threshold)}$ và ${max_val} > {format_num(high_threshold)}$ nên các giá trị bất thường là ${min_val}$ và ${max_val}$.''')

            list_vdc_2 = [loigiai_vdc_1]
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)


            # Đếm số câu đúng
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

            # Xuất câu hỏi
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
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


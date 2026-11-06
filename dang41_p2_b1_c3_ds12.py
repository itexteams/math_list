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


def bt_dang41_p2_b1_c3_ds12(self):
            # Khai báo biến ký hiệu
            # Khai báo biến
            x = symbols('x')

            # Random các thông số cho bài toán
            A = random.randint(3, 6) # Điều khiển khối lượng ban đầu 2^A
            h = random.choice([4, 5, 6, 8, 10]) # Điều khiển chu kỳ bán rã (thời gian giảm một nửa)

            # Các thời điểm
            t1 = h
            t2 = 2 * h
            t3 = 3 * h

            # Khối lượng tương ứng
            m1 = 2**(A - 1)
            m2 = 2**(A - 2)
            m3 = 2**(A - 3) # Giá trị dùng để so sánh ở câu d

            # Tạo ngẫu nhiên một giá trị so sánh xoay quanh m3
            compare_offset = random.choice([-0.2, -0.4, 0.2, 0.4])
            if m3 + compare_offset <= 0:
                compare_offset = 0.2
            compare_val = m3 + compare_offset
            compare_val_str = ("%.1f" % compare_val).replace('.', ',')

            # Nội dung câu hỏi
            noidungcauhoi = ('''Trong y học hạt nhân, đồng vị phóng xạ I-131 thường được sử dụng để hỗ trợ chẩn đoán và điều trị các bệnh lý về tuyến giáp. Sau khi tiêm vào cơ thể bệnh nhân, số lượng hạt nhân phóng xạ sẽ giảm dần theo thời gian. Giả sử khối lượng $m(t)$ (đơn vị: mg) của I-131 còn lại trong cơ thể tại thời điểm $t$ ngày ($t \\ge 0$) thỏa mãn $m(t) > 0$ và tốc độ phân rã tỉ lệ thuận với khối lượng hiện có theo phương trình $m'(t) = k.m(t)$ với $k \\neq 0$. Kết quả kiểm tra cho thấy khối lượng I-131 còn lại tại thời điểm $t = %s$ ngày và $t = %s$ ngày lần lượt là $%s$ mg và $%s$ mg.'''
                             % (t1, t2, m1, m2))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True $m(t) = e^{kt+C}$ với $C$ là một hằng số xác định'
            nb_da_1_s = '$m(t) = e^{k+Ct}$ với $C$ là một hằng số xác định'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Từ phương trình $m'(t) = k.m(t)$ ta có:\\\\ $\\frac{m'(t)}{m(t)} = k \\Rightarrow \\int \\frac{1}{m(t)} \\text{d}m = \\int k \\text{d}t \\Rightarrow \\ln|m(t)| = kt + C$. \\\\
            Vì $m(t) > 0 \\Rightarrow m(t) = e^{kt+C}$.''')

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            h_false = h - 2 if h > 4 else h + 2
            # Các đáp án
            th_da_1_d = '\\True $k = -\\frac{\\ln 2}{%s}$' % h
            th_da_1_s = '$k = -\\frac{\\ln 2}{%s}$' % h_false
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Theo đề bài, tại $t = %s$ ngày thì $m(%s) = %s$ và tại $t = %s$ ngày thì $m(%s) = %s$. \\\\
            Ta có hệ phương trình $\\begin{cases} e^{%sk+C} = %s \\quad (1) \\\\ e^{%sk+C} = %s \\quad (2) \\end{cases}$ \\\\
            Lấy $\\frac{(2)}{(1)} \\Leftrightarrow \\frac{e^{%sk+C}}{e^{%sk+C}} = \\frac{%s}{%s} \\Rightarrow e^{%sk} = \\frac{1}{2} \\Rightarrow k = -\\frac{\\ln 2}{%s}$.'''
                            % (t1, t1, m1, t2, t2, m2, t1, m1, t2, m2, t2, t1, m2, m1, h, h))

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True $C = %s \\ln 2$' % A
            vd_da_1_s = '$C = %s \\ln 2$' % (A + 1)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Thay giá trị $k = -\\frac{\\ln 2}{%s}$ vào $(1)$ ta được: \\\\
            $e^{-\\frac{\\ln 2}{%s} \\cdot %s + C} = %s \\Leftrightarrow e^{-\\ln 2 + C} = 2^{%s} \\Leftrightarrow -\\ln 2 + C = %s \\ln 2 \\Leftrightarrow C = %s \\ln 2$.'''
                            % (h, h, t1, m1, A-1, A-1, A))

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Xử lý logic tạo câu hỏi so sánh đúng hoặc sai
            if m3 < compare_val:
                ineq_true = "nhỏ hơn"
                ineq_false = "lớn hơn"
                sign = "<"
            else:
                ineq_true = "lớn hơn"
                ineq_false = "nhỏ hơn"
                sign = ">"

            # Các đáp án
            vdc_da_1_d = '\\True Khối lượng I-131 còn lại trong cơ thể tại thời điểm $t = %s$ ngày %s $%s$ mg' % (t3, ineq_true, compare_val_str)
            vdc_da_1_s = 'Khối lượng I-131 còn lại trong cơ thể tại thời điểm $t = %s$ ngày %s $%s$ mg' % (t3, ineq_false, compare_val_str)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Xử lý hiển thị số mũ cho số e
            if A - 3 == 0:
                power_str = "0"
            elif A - 3 == 1:
                power_str = "\\ln 2"
            else:
                power_str = "%s\\ln 2" % (A - 3)

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Với $k = -\\frac{\\ln 2}{%s}$ và $C = %s \\ln 2$, hàm số khối lượng là : $m(t) = e^{-\\frac{\\ln 2}{%s}t + %s \\ln 2}$. \\\\
            Tại thời điểm $t = %s$ ngày: $m(%s) = e^{-\\frac{\\ln 2}{%s} \\cdot %s + %s \\ln 2} = e^{%s} = %s \\text{ (mg)} %s %s \\text{ (mg)}$.'''
                             % (h, A, h, A, t3, t3, h, t3, A, power_str, m3, sign, compare_val_str))

            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vdc)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
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
                       str(noidungcauhoi) + '\n' +
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
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content


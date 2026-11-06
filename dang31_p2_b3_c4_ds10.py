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


def bt_dang31_p2_b3_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Hàm bổ trợ để chuyển dấu . thành dấu , cho số thập phân
            def format_decimal(value, precision=2):
                return str(round(float(value), precision)).replace('.', ',')

            # Giải bất phương trình T(x) >= 1.000.000 (1 tỷ đồng)
            target_revenue = 1000000

            # Random cho đến khi phương trình có nghiệm thực
            while True:
                coeff_a = random.randint(-60, -50) * 10 
                coeff_b = random.randint(480, 520) * 100

                # Biểu thức hàm số
                T_x = coeff_a * x**2 + coeff_b * x

                # Tính toán các giá trị quan trọng
                x_vertex = -coeff_b / (2 * coeff_a)
                y_max = T_x.subs(x, x_vertex)

                # Nếu đạt yêu cầu thì thoát vòng lặp
                if y_max >= target_revenue:
                    break

            # Đổi đơn vị sang tỷ đồng
            y_max_billion_str = format_decimal(float(y_max) / 10**6, 3)
            y_max_billion_part = int(y_max / 10**6)
            y_max_million = int((float(y_max) % 10**6) / 10**3)

            # Giải phương trình (đảm bảo có nghiệm thực)
            roots = solve(T_x - target_revenue, x)
            roots = sorted([r.evalf() for r in roots])

            root_1 = roots[0]
            root_2 = roots[1]

            # Các giá trị số đã định dạng dấu phẩy
            x_vertex_f = format_decimal(x_vertex, 2)
            y_max_f = format_decimal(y_max, 0)  # Doanh thu thường để số nguyên nghìn đồng
            root_1_f = format_decimal(root_1, 2)
            root_2_f = format_decimal(root_2, 2)


            # Nội dung câu hỏi
            noidungcauhoi = ('''Một công ty đồ gia dụng sản xuất bình đựng nước thấy rằng khi đơn giá của bình đựng nước là $x$ nghìn đồng thì doanh thu thu được biểu diễn theo $x$ có phương trình $T(x) = %s$. Xét tính đúng, sai của các khẳng định sau:''' 
                             % (latex(T_x)))

            ########################################################################
            # Nhận biết: Về hình dáng đồ thị
            nb_da_1_d = '\\True $T(x) = %s$ là hàm số bậc hai có đồ thị là parabol với bề lõm quay xuống dưới' % (latex(T_x))
            nb_da_1_s = '$T(x) = %s$ là hàm số bậc hai có đồ thị là parabol với bề lõm quay hướng lên trên' % (latex(T_x))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Hàm số $T(x) = %sx^2 + %sx$ có hệ số $a = %s < 0$ nên đây là hàm số bậc hai có đồ thị là một đường parabol có bề lõm quay xuống dưới.''' 
                            % (coeff_a, coeff_b, coeff_a))

            ########################################################################
            # Thông hiểu: Khả năng đạt doanh thu cao (1,5 tỷ)
            th_da_1_d = '\\True Doanh thu từ việc bán bình đựng nước không thể đạt $1,5$ tỷ đồng'
            th_da_1_s = 'Doanh thu từ việc bán bình đựng nước có thể đạt mức $1,6$ tỷ đồng'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Vì giá trị lớn nhất của hàm số là $T_{max} \\approx %s$ (nghìn đồng), tương đương khoảng $%s$ tỷ đồng, nên doanh thu không thể đạt mức $1,5$ tỷ đồng.''' 
                            % (format_decimal(y_max, 2), y_max_billion_str))

            ########################################################################
            # Vận dụng: Giá trị doanh thu tối đa
            vd_da_1_d = '\\True Doanh thu từ việc bán bình đựng nước tối đa khoảng %s tỷ %s triệu đồng' % (y_max_billion_part, y_max_million)
            vd_da_1_s = 'Doanh thu từ việc bán bình đựng nước tối đa đạt mức %s tỷ đồng' % (y_max_billion_part + 1)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Toạ độ đỉnh của parabol là $x_I = -\\frac{b}{2a} = -\\frac{%s}{2 \\cdot (%s)} \\approx %s$. \\\\ Doanh thu tối đa là $T(%s) \\approx %s$ nghìn đồng, tức khoảng %s tỷ %s triệu đồng.''' 
                            % (coeff_b, coeff_a, x_vertex_f, x_vertex_f, y_max_f, y_max_billion_part, y_max_million))

            ########################################################################
            # Vận dụng cao: Khoảng giá để đạt doanh thu mục tiêu
            vdc_da_1_d = '\\True Để doanh thu đạt tối thiểu $1$ tỷ đồng thì đơn giá $x$ phải nằm trong khoảng $%s \\le x \\le %s$' % (int(root_1), math.ceil(root_2))
            vdc_da_1_s = 'Để doanh thu đạt tối thiểu $1$ tỷ đồng thì đơn giá $x$ phải lớn hơn $%s$ nghìn đồng' % (math.ceil(root_2))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Để doanh thu đạt tối thiểu $1$ tỷ đồng, ta giải bất phương trình: \\\\ $%s \\ge 1.000.000 \\Leftrightarrow %s - 1.000.000 \\ge 0$. \\\\ Giải phương trình bậc hai ta được nghiệm $x_1 \\approx %s$ và $x_2 \\approx %s$. \\\\ Vậy với $%s \\le x \\le %s$ thì doanh thu đạt ít nhất $1$ tỷ đồng.''' 
                             % (latex(T_x), latex(T_x), root_1_f, root_2_f, int(root_1), math.ceil(root_2)))

            # --- Phần xử lý xuất nội dung ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                ans_nb = random.choice(list_nb_da_1)
                ans_th = random.choice(list_th_da_1)
                ans_vd = random.choice(list_vd_da_1)
                ans_vdc = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([ans_nb, ans_th, ans_vd, ans_vdc]) <= 3:
                    break

            shuffled_answers = [ans_nb, ans_th, ans_vd, ans_vdc]
            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' +
                str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(shuffled_answers[0]) + '}\n'
                '{' + str(shuffled_answers[1]) + '}\n'
                '{' + str(shuffled_answers[2]) + '}\n'
                '{' + str(shuffled_answers[3]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(shuffled_solutions[0]) + '\n'
                '\\item ' + str(shuffled_solutions[1]) + '\n'
                '\\item ' + str(shuffled_solutions[2]) + '\n'
                '\\item ' + str(shuffled_solutions[3]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


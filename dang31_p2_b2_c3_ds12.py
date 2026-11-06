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


def bt_dang31_p2_b2_c3_ds12(self):
            # Khai báo biến
            # Hàm định dạng số hiển thị dấu phẩy thay cho dấu chấm theo chuẩn VN
            def format_num(num):
                n = round(num, 2)
                if n == int(n): return str(int(n))
                return str(n).replace('.', ',')

            # BỘ DỮ LIỆU RANDOM
            # Chọn ngẫu nhiên hệ số k để sinh bài toán mới (k=0.1 là bài gốc, k=0.2 là bài trong ảnh của bạn)
            k = round(random.choice([0.1, 0.2, 0.3, 0.4, 0.5]), 2)

            # Tốc độ f(t) = a_f*t^2 + b_f*t
            a_f = round(-3 * k, 2)
            b_f = round(36 * k, 2)

            # Năng lượng F(t) = a_F*t^3 + b_F*t^2
            a_F = round(-1 * k, 2)
            b_F = round(18 * k, 2)

            def calc_F(t_val):
                return a_F * (t_val**3) + b_F * (t_val**2)

            # Các mốc thời gian kiểm tra
            t1, t2 = 1, 4
            t3, t4 = 1, 7

            # Tính giá trị năng lượng thực tế
            val_c = round(calc_F(t2) - calc_F(t1), 2)
            val_d1 = round(calc_F(t4) - calc_F(t3), 2)
            val_d2 = val_c

            # Tạo mốc so sánh đúng / sai cho câu C
            c_false_threshold = round(val_c - 0.1, 2)
            c_true_threshold = round(val_c + 0.1, 2)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một hệ thống pin năng lượng mặt trời gồm các tấm pin được kết nối với một bộ lưu trữ điện. Trong thời gian mặt trời chiếu sáng của một ngày, năng lượng điện thu được từ các tấm pin được lưu trong bộ lưu trữ điện. Gọi $F(t)$ là năng lượng điện (kWh) lưu trữ được kể từ thời điểm hệ thống bắt đầu hoạt động đến thời điểm $t$, trong đó $t$ là thời gian tính theo giờ ($0 \\le t \\le 12$) và thời điểm hệ thống bắt đầu hoạt động ứng với $t=0$. Biết rằng $F(0)=0$. \\\\
            Tốc độ lưu trữ năng lượng điện (kW) của hệ thống này là hàm số $f(t)=%st^2 + %st$ với $0 \\le t \\le 12$. Số liệu ghi nhận được ở một ngày cụ thể trong năm cho thấy $f(t)=%st^2 + %st$ với $0 \\le t \\le 12$.''' 
                             % (format_num(a_f), format_num(b_f), format_num(a_f), format_num(b_f)))

            ######################################################################## Nhận biết ############################################

            nb_da_1_d = '\\True $F(t)=%st^3 + %st^2$ với $0 \\le t \\le 12$' % (format_num(a_F), format_num(b_F))
            loigiai_nb_1_d = '''Ta có $F(t) = \\int f(t) dt = \\int \\left(%st^2 + %st\\right) dt = %st^3 + %st^2 + C$. \\\\ Do $F(0) = 0 \\Rightarrow C = 0$. \\\\ Vậy $F(t) = %st^3 + %st^2$. Phát biểu đúng.''' % (format_num(a_f), format_num(b_f), format_num(a_F), format_num(b_F), format_num(a_F), format_num(b_F))

            nb_da_1_s = '$F(t)=%st^3 - %st^2$ với $0 \\le t \\le 12$' % (format_num(a_F), format_num(b_F))
            loigiai_nb_1_s = '''Ta có $F(t) = \\int f(t) dt = \\int \\left(%st^2 + %st\\right) dt = %st^3 + %st^2 + C$. \\\\ Do $F(0) = 0 \\Rightarrow C = 0$. \\\\ Vậy $F(t) = %st^3 + %st^2$. Phát biểu sai.''' % (format_num(a_f), format_num(b_f), format_num(a_F), format_num(b_F), format_num(a_F), format_num(b_F))

            ######################################################################## Thông hiểu ############################################

            th_da_1_d = '\\True Năng lượng điện (kWh) lưu trữ được kể từ thời điểm $t=a$ đến thời điểm $t=b$ ($0 \\le a < b \\le 12$) là $\\int\\limits_a^b f(t) dt$'
            loigiai_th_1_d = '''Theo định nghĩa tích phân và mối liên hệ $F'(t) = f(t)$, năng lượng điện lưu trữ được trong khoảng thời gian từ $a$ đến $b$ bằng sự biến thiên của hàm năng lượng: $\\int\\limits_a^b f(t) dt = F(b) - F(a)$. Phát biểu đúng.'''

            th_da_1_s = 'Năng lượng điện (kWh) lưu trữ được kể từ thời điểm $t=a$ đến thời điểm $t=b$ ($0 \\le a < b \\le 12$) là $\\int\\limits_a^b F(t) dt$'
            loigiai_th_1_s = '''Năng lượng điện lưu trữ được tính bằng công thức $\\int\\limits_a^b f(t) dt$, chứ không phải $\\int\\limits_a^b F(t) dt$. Phát biểu sai.'''

            ######################################################################## Vận dụng ############################################

            vd_da_1_d = '\\True Năng lượng điện lưu trữ được kể từ thời điểm $t=%s$ đến thời điểm $t=%s$ nhỏ hơn $%s$ kWh' % (t1, t2, format_num(c_true_threshold))
            loigiai_vd_1_d = '''Năng lượng điện lưu trữ từ $t=%s$ đến $t=%s$ là: \\\\ $E_1 = \\int\\limits_{%s}^{%s} f(t) dt = F(%s) - F(%s) = %s$ (kWh). \\\\ Vì $%s < %s$ nên phát biểu đúng.''' % (t1, t2, t1, t2, t2, t1, format_num(val_c), format_num(val_c), format_num(c_true_threshold))

            vd_da_1_s = 'Năng lượng điện lưu trữ được kể từ thời điểm $t=%s$ đến thời điểm $t=%s$ nhỏ hơn $%s$ kWh' % (t1, t2, format_num(c_false_threshold))
            loigiai_vd_1_s = '''Năng lượng điện lưu trữ từ $t=%s$ đến $t=%s$ là: \\\\ $E_1 = \\int\\limits_{%s}^{%s} f(t) dt = F(%s) - F(%s) = %s$ (kWh). \\\\ Vì $%s > %s$ nên phát biểu sai.''' % (t1, t2, t1, t2, t2, t1, format_num(val_c), format_num(val_c), format_num(c_false_threshold))

            ######################################################################## Vận dụng cao ############################################

            vdc_da_1_d = '\\True Năng lượng điện lưu trữ được kể từ thời điểm $t=%s$ đến thời điểm $t=%s$ lớn hơn hai lần năng lượng điện lưu trữ được kể từ thời điểm $t=%s$ đến thời điểm $t=%s$' % (t3, t4, t1, t2)
            loigiai_vdc_1_d = '''Năng lượng điện lưu trữ từ $t=%s$ đến $t=%s$ là: \\\\ $E_2 = F(%s) - F(%s) = %s$ (kWh). \\\\ Ta thấy $E_2 = %s > 2 \\times E_1 = 2 \\times %s = %s$. \\\\ Do đó, năng lượng điện lưu trữ trong giai đoạn này lớn hơn hai lần khoảng thời gian trước đó, phát biểu đúng.''' % (t3, t4, t4, t3, format_num(val_d1), format_num(val_d1), format_num(val_d2), format_num(2*val_d2))

            vdc_da_1_s = 'Năng lượng điện lưu trữ được kể từ thời điểm $t=%s$ đến thời điểm $t=%s$ gấp hai lần năng lượng điện lưu trữ được kể từ thời điểm $t=%s$ đến thời điểm $t=%s$' % (t3, t4, t1, t2)
            loigiai_vdc_1_s = '''Năng lượng điện lưu trữ từ $t=%s$ đến $t=%s$ là: \\\\ $E_2 = F(%s) - F(%s) = %s$ (kWh). \\\\ Ta thấy $E_2 = %s \\neq 2 \\times E_1 = 2 \\times %s = %s$. \\\\ Do đó, năng lượng điện lưu trữ trong giai đoạn này không bằng hai lần khoảng thời gian trước đó, phát biểu sai.''' % (t3, t4, t4, t3, format_num(val_d1), format_num(val_d1), format_num(val_d2), format_num(2*val_d2))

            ######################################################################## Trộn và xuất ############################################

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi bộ đáp án có từ 1 đến 3 lựa chọn đúng
            while True:
                nb_choice = random.choice([(nb_da_1_d, loigiai_nb_1_d), (nb_da_1_s, loigiai_nb_1_s)])
                th_choice = random.choice([(th_da_1_d, loigiai_th_1_d), (th_da_1_s, loigiai_th_1_s)])
                vd_choice = random.choice([(vd_da_1_d, loigiai_vd_1_d), (vd_da_1_s, loigiai_vd_1_s)])
                vdc_choice = random.choice([(vdc_da_1_d, loigiai_vdc_1_d), (vdc_da_1_s, loigiai_vdc_1_s)])

                answers = [nb_choice[0], th_choice[0], vd_choice[0], vdc_choice[0]]
                if 1 <= count_true_answers(answers) <= 3:
                    break

            # Gắn đáp án và lời giải tương ứng
            ans_nb, sol_nb = nb_choice
            ans_th, sol_th = th_choice
            ans_vd, sol_vd = vd_choice
            ans_vdc, sol_vdc = vdc_choice

            # Xuất câu hỏi với đáp án và lời giải đã được kết hợp chuẩn xác
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n'+
                       str(noidungcauhoi)+ '\n'
                       '\\choiceTFn \n'
                       '{'+str(ans_nb)+'}\n'
                       '{'+str(ans_th)+'}\n'
                       '{'+str(ans_vd)+'}\n'
                       '{'+str(ans_vdc)+'}\n'
                       '\\loigiai{ \n'
                       '\\begin{enumEX}[a)]{1} \n'
                       '\\item '+str(sol_nb)+'\n'
                       '\\item '+str(sol_th)+'\n'
                       '\\item '+str(sol_vd)+'\n'
                       '\\item '+str(sol_vdc)+'\n'
                       '\\end{enumEX}} \n'
                       '\\end{ex}\n\\end{minipage}\n\n')
            return content


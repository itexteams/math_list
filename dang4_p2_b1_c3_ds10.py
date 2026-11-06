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


def bt_dang4_p2_b1_c3_ds10(self):
            # Khai báo biến
            # Hàm hỗ trợ định dạng số thập phân sang dấu phẩy chuẩn Việt Nam
            def format_num(num):
                if int(num) == num:
                    return str(int(num))
                return str(round(num, 2)).replace('.', ',')

            # Sinh bộ số ngẫu nhiên đảm bảo hai sai số tương đối khác nhau
            while True:
                a1 = random.choice([100, 120, 150, 152, 180, 200, 250, 300])
                d1 = random.choice([0.1, 0.2, 0.3, 0.4, 0.5])
                a2 = random.choice([10.5, 12.5, 15.2, 18.5, 20.0, 25.5])
                d2 = random.choice([0.1, 0.2, 0.3, 0.4])

                delta1 = (d1 / a1) * 100
                delta2 = (d2 / a2) * 100

                delta1_str = format_num(round(delta1, 2))
                delta2_str = format_num(round(delta2, 2))

                if delta1_str != delta2_str: 
                    break

            # Các giá trị nhiễu cho đáp án SAI
            delta1_wrong_str = format_num(round(delta1 * 2 + 0.11, 2))
            delta2_wrong_str = format_num(round(delta2 * 2 + 0.15, 2))

            # Nội dung câu hỏi
            noidungcauhoi = ('Kết quả đo chiều dài của một cây cầu được ghi $' + format_num(a1) + 'm \\pm ' + format_num(d1) + 'm$; kết quả đo chiều cao của một ngôi nhà được ghi là $' + format_num(a2) + 'm \\pm ' + format_num(d2) + 'm$.')

            ######################################################################## Nhận biết ############################################

            # Các đáp án
            nb_da_1_d = '\\True Sai số tương đối trong cách ghi thứ nhất (đo chiều dài của một cây cầu): $\\delta_1 \\le \\frac{d_1}{|a_1|} = \\frac{' + format_num(d1) + '}{' + format_num(a1) + '} \\approx ' + delta1_str + '\\%$'
            nb_da_1_s = 'Sai số tương đối trong cách ghi thứ nhất (đo chiều dài của một cây cầu): $\\delta_1 \\le \\frac{d_1}{|a_1|} = \\frac{' + format_num(d1) + '}{' + format_num(a1) + '} \\approx ' + delta1_wrong_str + '\\%$'
            list_nb_da_1=[nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('Sai số tương đối trong cách ghi thứ nhất (đo chiều dài của một cây cầu):\\\\ $\\delta_1 \\le \\frac{d_1}{|a_1|} = \\frac{' + format_num(d1) + '}{' + format_num(a1) + '} \\approx ' + delta1_str + '\\%$\\\\\nHay sai số tương đối không vượt quá $' + delta1_str + '\\%$.')
            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################

            # Các đáp án
            th_da_1_d = '\\True Sai số tương đối trong cách ghi thứ hai (đo chiều cao của một ngôi nhà): $\\delta_2 \\le \\frac{d_2}{|a_2|} = \\frac{' + format_num(d2) + '}{' + format_num(a2) + '} \\approx ' + delta2_str + '\\%$'
            th_da_1_s = 'Sai số tương đối trong cách ghi thứ hai (đo chiều cao của một ngôi nhà): $\\delta_2 \\le \\frac{d_2}{|a_2|} = \\frac{' + format_num(d2) + '}{' + format_num(a2) + '} \\approx ' + delta2_wrong_str + '\\%$'
            list_th_da_1=[th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('Sai số tương đối trong cách ghi thứ hai (đo chiều cao của một ngôi nhà):\\\\ $\\delta_2 \\le \\frac{d_2}{|a_2|} = \\frac{' + format_num(d2) + '}{' + format_num(a2) + '} \\approx ' + delta2_str + '\\%$.')
            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################

            # Các đáp án
            vd_da_1_d = '\\True Sai số tương đối trong cách ghi thứ hai (đo chiều cao của một ngôi nhà) không vượt quá $' + delta2_str + '\\%$'
            vd_da_1_s = 'Sai số tương đối trong cách ghi thứ hai (đo chiều cao của một ngôi nhà) lớn hơn $' + delta2_str + '\\%$'
            list_vd_da_1=[vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('Sai số tương đối trong cách ghi thứ hai không vượt quá $' + delta2_str + '\\%$.')
            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################

            # Logic so sánh độ chính xác
            if delta1 < delta2:
                true_cmp = "cao hơn"
                false_cmp = "thấp hơn"
                operator = "<"
            else:
                true_cmp = "thấp hơn"
                false_cmp = "cao hơn"
                operator = ">"

            # Các đáp án
            vdc_da_1_d = '\\True Cách ghi thứ nhất (đo chiều dài cây cầu) có độ chính xác ' + true_cmp + ' cách ghi thứ hai (đo chiều cao ngôi nhà)'
            vdc_da_1_s = 'Cách ghi thứ nhất (đo chiều dài cây cầu) có độ chính xác ' + false_cmp + ' cách ghi thứ hai (đo chiều cao ngôi nhà)'
            list_vdc_da_1=[vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('Qua đánh giá sai số tương đối trong hai cách ghi, ta thấy $' + delta1_str + '\\% ' + operator + ' ' + delta2_str + '\\%$\\\\\nNên cách ghi thứ nhất (đo chiều dài cây cầu) có độ chính xác ' + true_cmp + ' cách ghi thứ hai (đo chiều cao ngôi nhà).')
            list_vdc_2 = [loigiai_vdc_1]

            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # Kiểm tra đáp án Đúng
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
                '\\end{ex}\n\\end{minipage}\n\n')
            return content


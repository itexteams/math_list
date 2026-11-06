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


def bt_dang34_p2_b2_c4_ds12(self):
            # Khai báo biến
            # Hàm hỗ trợ đổi dấu chấm thành dấu phẩy cho số thập phân
            def format_num(val):
                return str(val).replace('.', ',')

            # --- Bước 1: Khởi tạo dữ liệu ngẫu nhiên ---
            # Tỉ lệ sản xuất của phân xưởng 1 (ví dụ từ 50% đến 70%)
            p1_percent = random.choice([55, 60, 65, 70])
            p2_percent = 100 - p1_percent

            # Tỉ lệ phế phẩm (ví dụ từ 10% đến 25%)
            d1_percent = random.choice([12, 14, 16, 18])
            d2_percent = random.choice([15, 20, 22, 25])

            # Chuyển sang số thập phân để tính toán
            pA = p1_percent / 100
            pnotA = p2_percent / 100
            pB_A = d1_percent / 100
            pB_notA = d2_percent / 100

            # Tính toán các giá trị xác suất theo công thức
            # b) Xác suất phế phẩm toàn phần
            pB = round(pA * pB_A + pnotA * pB_notA, 4)

            # c) Xác suất Bayes: Biết là phế phẩm, tìm xác suất từ PX1
            pA_B = round((pA * pB_A) / pB, 2)
            pnotA_B = round(1 - pA_B, 2)

            # d) Xác suất sản phẩm tốt
            pnotB = round(1 - pB, 4)
            pnotB_A = round(1 - pB_A, 2)
            pnotB_notA = round(1 - pB_notA, 2)

            # Xác suất chọn được máy 1 nếu là sản phẩm tốt
            pA_notB = round((pA * pnotB_A) / pnotB, 2)
            pnotA_notB = round(1 - pA_notB, 2)

            # So sánh khả năng ở câu d
            is_PX1_higher = pA_notB > pnotA_notB
            higher_workshop = "thứ nhất" if is_PX1_higher else "thứ hai"
            lower_workshop = "thứ hai" if is_PX1_higher else "thứ nhất"

            # --- Bước 2: Nội dung câu hỏi ---
            noidungcauhoi = ('''Một nhà máy có hai phân xưởng cùng sản xuất một loại sản phẩm. Phân xưởng thứ nhất sản xuất %s\\%% và phân xưởng thứ hai sản xuất %s\\%% tổng số sản phẩm của cả nhà máy. Tỉ lệ phế phẩm của từng phân xưởng lần lượt là %s\\%% và %s\\%%. Lấy ngẫu nhiên một sản phẩm trong kho hàng của nhà máy.''' 
                             % (p1_percent, p2_percent, d1_percent, d2_percent))

            # --- NHẬN BIẾT (Câu a) ---
            nb_da_1_d = '\\True Xác suất để sản phẩm đó do phân xưởng thứ nhất sản xuất là %s' % format_num(pA)
            nb_da_1_s = 'Xác suất để sản phẩm đó do phân xưởng thứ nhất sản xuất là %s' % format_num(pnotA)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)
            loigiai_nb_1 = ('''Do phân xưởng thứ nhất sản xuất %s\\%% tổng số sản phẩm của cả nhà máy nên xác suất để sản phẩm đó do phân xưởng thứ nhất sản xuất là %s.''' 
                            % (p1_percent, format_num(pA)))

            # --- THÔNG HIỂU (Câu b) ---
            th_da_1_d = '\\True Xác suất để lấy được phế phẩm bằng %s' % format_num(pB)
            th_da_1_s = 'Xác suất để lấy được phế phẩm bằng %s' % format_num(round(pB + 0.02, 3))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)
            loigiai_th_1 = ('''Gọi $A$ là biến cố "Chọn được sản phẩm từ phân xưởng thứ nhất", $\\overline{A}$ là biến cố "Chọn được sản phẩm từ phân xưởng thứ hai".\\\\ B là biến cố "Chọn được sản phẩm là phế phẩm".\\\\ Khi đó: $P(A)=%s; P(\\overline{A})=%s$;\\\\ $P(B | A)=%s; P(\\overline{B} | A)=%s; P(B | \\overline{A})=%s$\\\\ Áp dụng công thức tính xác suất toàn phần, ta có:\\\\ $P(B)=P(A).P(B | A)+P(\\overline{A}).P(B | \\overline{A})$\\\\ $=%s.%s + %s.%s = %s$.\\\\ Vậy xác suất lấy được phế phẩm là %s.''' 
                            % (format_num(pA), format_num(pnotA), format_num(pB_A), format_num(pnotB_A), format_num(pB_notA), format_num(pA), format_num(pB_A), format_num(pnotA), format_num(pB_notA), format_num(pB), format_num(pB)))

            # --- VẬN DỤNG (Câu c) ---
            vd_da_1_d = '\\True Giả sử đã lấy được phế phẩm, xác suất phế phẩm đó do phân xưởng thứ nhất sản xuất bằng %s (kết quả làm tròn đến hàng phần trăm)' % format_num(pA_B)
            vd_da_1_s = 'Giả sử đã lấy được phế phẩm, xác suất phế phẩm đó do phân xưởng thứ nhất sản xuất bằng %s' % format_num(pnotA_B)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)
            loigiai_vd_1 = ('''Chọn được phế phẩm, biến cố phế phẩm đó do phân xưởng thứ nhất sản xuất là $A | B$, áp dụng công thức Bayes, ta được:\\\\ $P(A | B)=\\frac{P(A).P(B | A)}{P(B)}=\\frac{%s.%s}{%s} \\approx %s$.''' 
                            % (format_num(pA), format_num(pB_A), format_num(pB), format_num(pA_B)))

            # --- VẬN DỤNG CAO (Câu d) ---
            vdc_da_1_d = '\\True Nếu lấy được sản phẩm tốt, khả năng sản phẩm đó do phân xưởng %s sản xuất là cao hơn khả năng sản phẩm đó do phân xưởng %s sản xuất' % (higher_workshop, lower_workshop)
            vdc_da_1_s = 'Nếu lấy được sản phẩm tốt, khả năng sản phẩm đó do phân xưởng %s sản xuất là cao hơn khả năng sản phẩm đó do phân xưởng %s sản xuất' % (lower_workshop, higher_workshop)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)
            loigiai_vdc_1 = ('''Khi lấy được sản phẩm tốt, để so sánh khả năng sản phẩm thuộc phân xưởng, ta tính xác suất để sản phẩm tốt được chọn ấy thuộc phân xưởng thứ nhất.\\\\ Từ ý a) suy ra $P(\\overline{B})=1-%s=%s$.\\\\ Theo công thức Bayes, ta có: $P(A | \\overline{B})=\\frac{P(A).P(\\overline{B} | A)}{P(\\overline{B})}=\\frac{%s.%s}{%s} \\approx %s$.\\\\ Vì $P(A | \\overline{B}) = %s$ nên $P(\\overline{A} | \\overline{B}) \\approx %s$.\\\\ Vậy khả năng sản phẩm tốt được chọn từ phân xưởng %s cao hơn.''' 
                             % (format_num(pB), format_num(pnotB), format_num(pA), format_num(pnotB_A), format_num(pnotB), format_num(pA_notB), format_num(pA_notB), format_num(pnotA_notB), higher_workshop))

            # --- XỬ LÝ ĐÁP ÁN ĐÚNG/SAI ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                d1 = random.choice(list_nb_da_1)
                d2 = random.choice(list_th_da_1)
                d3 = random.choice(list_vd_da_1)
                d4 = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([d1, d2, d3, d4]) <= 3:
                    break

            # Gán lại kết quả cuối cùng
            shuffled_answers = [d1, d2, d3, d4]
            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            # --- XUẤT NỘI DUNG ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' +
                str(noidungcauhoi) + 
                '\n\\choiceTFn \n'
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


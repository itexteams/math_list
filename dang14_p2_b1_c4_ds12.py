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


def bt_dang14_p2_b1_c4_ds12(self):
            # Khai báo biến
            # Bước 1: Khởi tạo các giá trị ngẫu nhiên cho bài toán
            n_do = random.choice([40, 50, 60])
            n_vang = random.choice([20, 30, 40])
            n_tong = n_do + n_vang

            # Phần trăm đánh số (để nguyên % để tính toán nhưng kết quả sẽ xuất dạng phân số)
            p_do = random.choice([40, 50, 60, 70])
            p_vang = random.choice([40, 50, 60])

            # Tính toán các giá trị trung gian bằng Rational
            bi_do_co_so = Rational(n_do * p_do, 100)
            bi_vang_co_so = Rational(n_vang * p_vang, 100)
            bi_do_ko_so = n_do - bi_do_co_so
            bi_vang_ko_so = n_vang - bi_vang_co_so
            bi_ko_so_tong = bi_do_ko_so + bi_vang_ko_so

            # Xác suất cho các câu hỏi (Dạng Rational)
            xs_vang_co_so = Rational(bi_vang_co_so, n_tong)
            xs_do = Rational(n_do, n_tong)
            xs_ko_so = Rational(bi_ko_so_tong, n_tong)

            # Xác suất có điều kiện (Câu d)
            xs_do_neu_ko_so = Rational(bi_do_ko_so, bi_ko_so_tong)
            xs_vang_neu_ko_so = Rational(bi_vang_ko_so, bi_ko_so_tong)

            # So sánh xác suất câu d
            if xs_do_neu_ko_so > xs_vang_neu_ko_so:
                ss_text_d = "cao hơn"
                ss_text_s = "thấp hơn"
            elif xs_do_neu_ko_so < xs_vang_neu_ko_so:
                ss_text_d = "thấp hơn"
                ss_text_s = "cao hơn"
            else:
                ss_text_d = "bằng"
                ss_text_s = "khác"

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một hộp có %s viên bi, trong đó có %s viên bi màu đỏ và %s viên bi màu vàng. Các viên bi có kích thước và khối lượng như nhau. Sau khi kiểm tra, người ta thấy có %s\\%% số viên bi màu đỏ đánh số và %s\\%% số viên bi màu vàng có đánh số, những viên bi còn lại không đánh số. Lấy ra ngẫu nhiên 1 viên bi trong hộp.''' 
                             %(n_tong, n_do, n_vang, p_do, p_vang))

            ########################################################################
            # a) Nhận biết: Xác suất chọn được viên bi màu vàng có đánh số
            # Hiển thị dạng phân số Rational
            nb_da_1_d = '\\True Xác suất chọn được viên bi màu vàng có đánh số bằng $%s$' %(latex(xs_vang_co_so))
            nb_da_1_s = 'Xác suất chọn được viên bi màu vàng có đánh số bằng $%s$' %(latex(xs_vang_co_so + Rational(1, 20)))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ('''Số bi vàng có đánh số là: $%s \\cdot %s\\%% = %s$. \\\\ Số viên bi trong hộp là $%s$. \\\\ Vậy xác suất chọn được viên bi màu vàng có đánh số bằng $\\frac{%s}{%s} = %s$.'''
                            %(n_vang, p_vang, latex(bi_vang_co_so), n_tong, latex(bi_vang_co_so), n_tong, latex(xs_vang_co_so)))

            ########################################################################
            # b) Thông hiểu: Xác suất chọn được viên bi màu đỏ
            th_da_1_d = '\\True Xác suất chọn được viên bi màu đỏ bằng $%s$' %(latex(xs_do))
            th_da_1_s = 'Xác suất chọn được viên bi màu đỏ bằng $%s$' %(latex(xs_do - Rational(1, 10)))
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ('''Trong hộp có $%s$ viên bi màu đỏ. \\\\ Số viên bi trong hộp là $%s$. \\\\ Vậy xác suất chọn được viên bi màu đỏ bằng $\\frac{%s}{%s} = %s$.'''
                            %(n_do, n_tong, n_do, n_tong, latex(xs_do)))

            ########################################################################
            # c) Vận dụng: Xác suất chọn được viên bi không đánh số
            vd_da_1_d = '\\True Xác suất chọn được viên bi không đánh số bằng $%s$' %(latex(xs_ko_so))
            vd_da_1_s = 'Xác suất chọn được viên bi không đánh số bằng $%s$' %(latex(xs_ko_so + Rational(1, 40)))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ('''Số bi đỏ có đánh số là: $%s \\cdot %s\\%% = %s$. \\\\ Số bi vàng có đánh số là: $%s \\cdot %s\\%% = %s$. \\\\ Vậy số viên bi không đánh số là $%s - %s - %s = %s$. \\\\ Khi đó: xác suất chọn được viên bi không đánh số bằng $\\frac{%s}{%s} = %s$.'''
                            %(n_do, p_do, latex(bi_do_co_so), n_vang, p_vang, latex(bi_vang_co_so), n_tong, latex(bi_do_co_so), latex(bi_vang_co_so), latex(bi_ko_so_tong), latex(bi_ko_so_tong), n_tong, latex(xs_ko_so)))

            ########################################################################
            # d) Vận dụng cao: Xác suất có điều kiện
            vdc_da_1_d = '\\True Giả sử viên bi được lấy ra là viên bi chưa được đánh số, xác suất để viên bi đó là bi đỏ %s xác suất viên bi đó là bi vàng' %(ss_text_d)
            vdc_da_1_s = 'Giả sử viên bi được lấy ra là viên bi chưa được đánh số, xác suất để viên bi đó là bi đỏ %s xác suất viên bi đó là bi vàng' %(ss_text_s)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = ('''Gọi $A$ là biến cố viên bi được chọn màu đỏ. \\\\ Khi đó $\\overline{A}$ là biến cố viên bi được chọn màu vàng. \\\\ Gọi $B$ là biến cố viên bi được chọn có đánh số. \\\\ Khi đó $\\overline{B}$ là biến cố viên bi được chọn không đánh số. \\\\ Ta có $P(A|\\overline{B}) = \\frac{P(A \\cap \\overline{B})}{P(\\overline{B})} = \\frac{%s}{%s} = %s$. \\\\ Ta có $P(\\overline{A}|\\overline{B}) = \\frac{P(\\overline{A} \\cap \\overline{B})}{P(\\overline{B})} = \\frac{%s}{%s} = %s$. \\\\ Vậy viên bi được lấy ra là viên bi chưa được đánh số, xác suất để viên bi đó là bi đỏ %s hơn xác suất viên bi đó là bi vàng.'''
                             %(latex(bi_do_ko_so), latex(bi_ko_so_tong), latex(xs_do_neu_ko_so), latex(bi_vang_ko_so), latex(bi_ko_so_tong), latex(xs_vang_neu_ko_so), ss_text_d))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_da = random.choice(list_nb_da_1)
                th_da = random.choice(list_th_da_1)
                vd_da = random.choice(list_vd_da_1)
                vdc_da = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([nb_da, th_da, vd_da, vdc_da]) <= 3:
                    break

            shuffled_answers = [nb_da, th_da, vd_da, vdc_da]
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


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


def bt_dang18_p2_b1_c4_ds12(self):
            # Khai báo biến
            # B1 & B3: Nghiên cứu đề bài và thiết lập thông số ngẫu nhiên
            # Số lượng quả cầu mỗi màu
            blue = random.randint(3, 5)   # Quả cầu xanh
            red = random.randint(2, 4)    # Quả cầu đỏ
            yellow = random.randint(2, 3) # Quả cầu vàng
            total = blue + red + yellow

            # Các giá trị tính toán
            n_omega = math.comb(total, 3)
            n_no_red = math.comb(blue + yellow, 3)
            p_no_red = Rational(n_no_red, n_omega)
            p_at_least_one_red = 1 - p_no_red

            # Nội dung câu hỏi gốc
            noidungcauhoi = ('''Một chiếc hộp chứa %s quả cầu gồm %s quả cầu màu xanh, %s quả cầu màu đỏ và %s quả cầu màu vàng. Lấy ngẫu nhiên 3 quả cầu từ hộp đó.''' 
                             %(total, blue, red, yellow))

            ########################################################################
            # Nhận biết: Số cách lấy 3 quả cầu bất kỳ
            nb_da_1_d = '\\True Số cách lấy ngẫu nhiên 3 quả cầu từ hộp đó là %s' % (n_omega)
            nb_da_1_s = 'Số cách lấy ngẫu nhiên 3 quả cầu từ hộp đó là %s' % (n_omega + random.choice([-2, 2, 5]))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Số cách chọn 3 quả cầu từ %s quả cầu là $C_{%s}^3 = %s$.''' 
                            % (total, total, n_omega))

            list_nb_1 = [nb_da_1]
            list_nb_2 = [loigiai_nb_1]
            combined_nb = list(zip(list_nb_1, list_nb_2))

            ########################################################################
            # Thông hiểu: Số cách lấy 3 quả không có màu đỏ
            th_da_1_d = '\\True Số cách lấy được 3 quả cầu không có quả màu đỏ là %s' % (n_no_red)
            th_da_1_s = 'Số cách lấy được 3 quả cầu không có quả màu đỏ là %s' % (n_no_red + 5)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Để chọn 3 quả cầu không có quả màu đỏ, ta chỉ có thể chọn từ %s quả màu xanh và %s quả màu vàng, tức là chọn từ %s quả cầu. Số cách chọn 3 quả cầu từ %s quả cầu là $C_{%s}^3 = %s$.''' 
                            % (blue, yellow, blue + yellow, blue + yellow, blue + yellow, n_no_red))

            list_th_1 = [th_da_1]
            list_th_2 = [loigiai_th_1]
            combined_th = list(zip(list_th_1, list_th_2))

            ########################################################################
            # Vận dụng: Xác suất không có quả màu đỏ
            vd_da_1_d = '\\True Xác suất lấy được 3 quả cầu không có quả màu đỏ bằng $%s$' % (latex(p_no_red))
            vd_da_1_s = 'Xác suất lấy được 3 quả cầu không có quả màu đỏ bằng $\\frac{1}{%s}$' % (n_omega)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Gọi $\\Omega$ là không gian mẫu của phép thử lấy ngẫu nhiên 3 quả trong %s quả cầu, khi đó $n(\\Omega) = C_{%s}^3 = %s$. \\\\
            Gọi $A$: "Lấy 3 quả cầu không có quả màu đỏ", khi đó theo ý b ta có $n(A) = C_{%s}^3 = %s$. \\\\
            Vậy xác suất lấy được 3 quả cầu không có quả màu đỏ là: $P(A) = \\frac{n(A)}{n(\\Omega)} = \\frac{%s}{%s} = %s$.''' 
                            % (total, total, n_omega, blue + yellow, n_no_red, n_no_red, n_omega, latex(p_no_red)))

            list_vd_1 = [vd_da_1]
            list_vd_2 = [loigiai_vd_1]
            combined_vd = list(zip(list_vd_1, list_vd_2))

            ########################################################################
            # Vận dụng cao: Xác suất có ít nhất 1 quả màu đỏ
            vdc_da_1_d = '\\True Xác suất lấy được 3 quả cầu có ít nhất 1 quả màu đỏ bằng $%s$' % (latex(p_at_least_one_red))
            vdc_da_1_s = 'Xác suất lấy được 3 quả cầu có ít nhất 1 quả màu đỏ bằng $\\frac{%s}{%s}$' % (n_omega - 1, n_omega)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Xét biến cố đối của biến cố "Lấy 3 quả cầu có ít nhất 1 quả màu đỏ" là biến cố $A$: "Lấy 3 quả cầu không có quả màu đỏ". \\\\
            Ta có xác suất của biến cố đối là $P(A) = %s$. \\\\
            Vậy xác suất cần tìm là $P(\\overline{A}) = 1 - P(A) = 1 - %s = %s$.''' 
                             % (latex(p_no_red), latex(p_no_red), latex(p_at_least_one_red)))

            list_vdc_1 = [vdc_da_1]
            list_vdc_2 = [loigiai_vdc_1]
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            ########################################################################
            # Kiểm tra số lượng đáp án đúng (từ 1 đến 3)
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                if 1 <= count_true_answers(answers) <= 3:
                    break

            # Cập nhật lại danh sách sau khi chọn
            shuffled_answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            # Xuất nội dung theo định dạng yêu cầu
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


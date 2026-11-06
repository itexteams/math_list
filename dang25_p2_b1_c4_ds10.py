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


def bt_dang25_p2_b1_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # BƯỚC 1: RANDOM THAM SỐ
            # Hàm số mẫu: y = sqrt(6 - 3x) -> dạng y = sqrt(b + ax) với a < 0
            # Để bài toán đẹp, ta chọn a âm và b sao cho nghiệm b/-a là số nguyên
            a_val = random.choice([-1, -2, -3, -4, -5])
            limit_x = random.randint(1, 5) # Điểm biên tập xác định
            b_val = -a_val * limit_x 

            expr = b_val + a_val * x
            f = sqrt(expr)

            # Điểm A để kiểm tra thuộc đồ thị (chọn x_0 < limit_x)
            x_A = limit_x - 3
            y_A = f.subs(x, x_A)

            # Khoảng xét tính biến thiên (x1, x2)
            x_range_min = limit_x - 7
            x_range_max = limit_x - 2

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hàm số $y = %s$.''' % (latex(f)))

            ########################################################################
            # a) Nhận biết: Tập xác định
            nb_da_1_d = '\\True Tập xác định của hàm số là $D = (-\\infty; %s]$ ' % (latex(limit_x))
            nb_da_1_s = 'Tập xác định của hàm số là $D = [%s; +\\infty)$' % (latex(limit_x))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Điều kiện: $%s \\geq 0 \\Leftrightarrow %s x \\geq %s \\Leftrightarrow x \\leq %s$ nên tập xác định $D = (-\\infty; %s]$.''' 
                            % (latex(expr), latex(a_val), latex(-b_val), latex(limit_x), latex(limit_x)))

            ########################################################################
            # b) Thông hiểu: Điểm thuộc đồ thị
            nb_da_2_d = '\\True Điểm $A(%s; %s)$ thuộc đồ thị hàm số' % (latex(x_A), latex(y_A))
            nb_da_2_s = 'Điểm $A(%s; %s)$ thuộc đồ thị hàm số' % (latex(x_A), latex(y_A + 1))
            list_nb_da_2 = [nb_da_2_d, nb_da_2_s]
            nb_da_2 = random.choice(list_nb_da_2)

            loigiai_th_1 = ('''Thay $x = %s \\Rightarrow y = \\sqrt{%s + %s.(%s)} = %s \\Rightarrow$ Điểm $A(%s; %s)$ thuộc đồ thị hàm số.''' 
                            % (latex(x_A), b_val, a_val, x_A, latex(y_A), latex(x_A), latex(y_A)))

            ########################################################################
            # c) Vận dụng: Tập giá trị
            vd_da_1_d = '\\True Tập giá trị của hàm số là $[0; +\\infty)$'
            vd_da_1_s = 'Tập giá trị của hàm số là $\\mathbb{R}$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Vì $y = \\sqrt{%s} \\geq 0, \\forall x \\in (-\\infty; %s]$ nên tập giá trị của hàm số là $[0; +\\infty)$.''' 
                            % (latex(expr), latex(limit_x)))

            ########################################################################
            # d) Vận dụng cao: Tính đơn điệu
            vdc_da_1_d = '\\True Hàm số nghịch biến trên khoảng $(%s; %s)$' % (x_range_min, x_range_max)
            vdc_da_1_s = 'Hàm số đồng biến trên khoảng $(%s; %s)$' % (x_range_min, x_range_max)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''$\\forall x_1, x_2 \\in (%s; %s)$ sao cho $x_1 < x_2$, ta có: \\\\
            $%s < x_1 < x_2 < %s \\Rightarrow %s x_1 > %s x_2 \\Rightarrow %s %s x_1 > %s %s x_2 \\Rightarrow \\sqrt{%s} > \\sqrt{%s} \\Rightarrow y_1 > y_2$. \\\\
            Vậy hàm số nghịch biến trên khoảng $(%s; %s)$.''' 
                            % (x_range_min, x_range_max, x_range_min, x_range_max, a_val, a_val, b_val, a_val, b_val, a_val, latex(expr.subs(x, symbols('x_1'))), latex(expr.subs(x, symbols('x_2'))), x_range_min, x_range_max))

            ########################################################################
            # KIỂM TRA SỐ LƯỢNG ĐÁP ÁN ĐÚNG
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                d1 = random.choice(list_nb_da_1)
                d2 = random.choice(list_nb_da_2)
                d3 = random.choice(list_vd_da_1)
                d4 = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([d1, d2, d3, d4]) <= 3:
                    break

            # Gán kết quả cuối cùng
            shuffled_answers = [d1, d2, d3, d4]
            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            # Xuất nội dung theo mẫu
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


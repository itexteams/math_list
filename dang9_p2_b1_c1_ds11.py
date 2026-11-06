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


def bt_dang9_p2_b1_c1_ds11(self):
            # Khai báo biến
            # Tạo phân số cos x = n / m với m từ 2 đến 5 và n < m
            m = random.choice([2, 3, 4, 5])
            n = random.randint(1, m - 1)

            val_cos = Rational(n, m)
            val_cos_sq = val_cos**2

            # Tính giá trị biểu thức dưới căn cho sin^2 x = 1 - cos^2 x
            under_root = 1 - val_cos_sq

            # Chọn ngẫu nhiên góc phần tư để sinh dấu của sin x
            # Cấu hình 1: Góc phần tư thứ I (0 < x < pi/2) -> sin x > 0
            # Cấu hình 2: Góc phần tư thứ IV (-pi/2 < x < 0) -> sin x < 0
            goc_phan_tu = random.choice([1, 2])

            if goc_phan_tu == 1:
                txt_range = '0 < x < \\frac{\\pi}{2}'
                txt_sin_sign = '\\sin x > 0'
                sign_sin = 1
            else:
                txt_range = '-\\frac{\\pi}{2} < x < 0'
                txt_sin_sign = '\\sin x < 0'
                sign_sin = -1

            # Tính toán chính xác các giá trị lượng giác bằng SymPy
            val_sin = sign_sin * sqrt(under_root)
            val_tan = val_sin / val_cos
            val_cot = val_cos / val_sin

            # Nội dung câu hỏi tổng quát dùng định dạng %s
            noidungcauhoi = ('''Tính được các giá trị lượng giác còn lại của góc $x$, biết: $\\cos x = %s$ với $%s$. Khi đó:''' 
                             % (latex(val_cos), txt_range))

            ########################################################################
            # Nhận biết (Mệnh đề a: Xét dấu của sin x)
            if sign_sin == 1:
                nb_da_1_d = '\\True $\\sin x > 0$'
                nb_da_1_s = '$\\sin x < 0$'
            else:
                nb_da_1_d = '\\True $\\sin x < 0$'
                nb_da_1_s = '$\\sin x > 0$'

            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]
            loigiai_nb_1 = ('''Do $%s$ nên $%s$.''' % (txt_range, txt_sin_sign))
            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu (Mệnh đề b: Tính giá trị sin x)
            th_da_1_d = '\\True $\\sin x = %s$' % (latex(val_sin))
            th_da_1_s = '$\\sin x = %s$' % (latex(-val_sin))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]
            loigiai_th_1 = ('''Ta có: $\\sin^2 x + \\cos^2 x = 1 \\Rightarrow \\sin^2 x = 1 - \\cos^2 x = 1 - \\frac{%s}{%s} = \\frac{%s}{%s} \\Rightarrow \\sin x = %s$.''' 
                            % (latex(n**2), latex(m**2), latex(m**2 - n**2), latex(m**2), latex(val_sin)))
            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng (Mệnh đề c: Tính giá trị tan x)
            vd_da_1_d = '\\True $\\tan x = %s$' % (latex(val_tan))
            vd_da_1_s = '$\\tan x = %s$' % (latex(-val_tan))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]
            loigiai_vd_1 = ('''$\\tan x = \\frac{\\sin x}{\\cos x} = \\frac{%s}{%s} = %s$.''' 
                            % (latex(val_sin), latex(val_cos), latex(val_tan)))
            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao (Mệnh đề d: Tính giá trị cot x)
            vdc_da_1_d = '\\True $\\cot x = %s$' % (latex(val_cot))
            vdc_da_1_s = '$\\cot x = %s$' % (latex(-val_cot))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]
            loigiai_vdc_1 = ('''$\\cot x = \\frac{\\cos x}{\\sin x} = \\frac{%s}{%s} = %s$.''' 
                             % (latex(val_cos), latex(val_sin), latex(val_cot)))
            list_vdc_2 = [loigiai_vdc_1]

            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)


            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)


            # Vòng lặp kiểm tra số lượng câu đúng nằm trong khoảng [1, 3]
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

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

            # Khởi tạo khối lời giải chi tiết phân bổ rõ ràng theo cấu trúc enumEX [a)]{1}
            loigiai = ('''\\begin{enumEX}[a)]{1} \n'''
                       '''\\item %s\n'''
                       '''\\item %s\n'''
                       '''\\item %s\n'''
                       '''\\item %s\n'''
                       '''\\end{enumEX}'''
                       % (shuffled_solutions_nb[0], shuffled_solutions_th[0], shuffled_solutions_vd[0], shuffled_solutions_vdc[0]))

            # Kết xuất cấu trúc chuỗi mẫu bằng định dạng %s thống nhất với khung chương trình
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' +
                str(noidungcauhoi) + 
                '\n\\choiceTFn \n'
                '{' + str(shuffled_answers_nb[0]) + '}\n'
                '{' + str(shuffled_answers_th[0]) + '}\n'
                '{' + str(shuffled_answers_vd[0]) + '}\n'
                '{' + str(shuffled_answers_vdc[0]) + '}\n'
                '\\loigiai{ \n'
                +loigiai+
                '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


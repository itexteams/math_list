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


def bt_dang6_p2_b1_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')
            k = randint(2, 4)  # Tử số
            a_val = randint(1, 3)  # Hằng số trong mẫu số (a - x)
            # Hàm số f(x) = k / (a_val - x)
            f_expr = k / (a_val - x)
            f_prime = diff(f_expr, x)

            # Các điểm x0 để tính toán
            x1 = a_val + 1
            x2 = a_val + k

            val_f_prime_x1 = f_prime.subs(x, x1)
            val_f_prime_x2 = f_prime.subs(x, x2)
            tong_f_prime = val_f_prime_x1 + val_f_prime_x2

            # Nội dung câu hỏi
            noidungcauhoi = ('''Dùng định nghĩa để tính đạo hàm của hàm số $f\\left( x \\right) = \\frac{%s}{%s - x}$ với $x \\neq %s$.''' 
                             %(latex(k), latex(a_val), latex(a_val)))

            ########################################################################
            # Nhận biết: Định nghĩa đạo hàm qua giới hạn
            nb_da_1_d = '\\True Với bất kì $x_0 \\neq %s$, ta có: $f\'\\left( x_0 \\right) = \\lim_{x \\to x_0} \\frac{%s}{\\left( %s - x \\right)\\left( %s - x_0 \\right)}$' %(latex(a_val), latex(k), latex(a_val), latex(a_val))
            nb_da_1_s = 'Với bất kì $x_0 \\neq %s$, ta có: $f\'\\left( x_0 \\right) = \\lim_{x \\to x_0} \\frac{%s}{\\left( x - %s \\right)\\left( x_0 - %s \\right)}$' %(latex(a_val), latex(k), latex(a_val), latex(a_val))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = ('''Theo định nghĩa, đạo hàm tại $x_0$ là:\\\\
            $f\'\\left( x_0 \\right) = \\lim_{x \\to x_0} \\frac{f\\left( x \\right) - f\\left( x_0 \\right)}{x - x_0} = \\lim_{x \\to x_0} \\frac{\\frac{%s}{%s - x} - \\frac{%s}{%s - x_0}}{x - x_0}$ \\\\
            $= \\lim_{x \\to x_0} \\frac{%s\\left( %s - x_0 \\right) - %s\\left( %s - x \\right)}{\\left( %s - x \\right)\\left( %s - x_0 \\right)\\left( x - x_0 \\right)} = \\lim_{x \\to x_0} \\frac{%s\\left( x - x_0 \\right)}{\\left( %s - x \\right)\\left( %s - x_0 \\right)\\left( x - x_0 \\right)}$ \\\\
            $= \\lim_{x \\to x_0} \\frac{%s}{\\left( %s - x \\right)\\left( %s - x_0 \\right)}$.'''
                            %(latex(k), latex(a_val), latex(k), latex(a_val), 
                              latex(k), latex(a_val), latex(k), latex(a_val), 
                              latex(a_val), latex(a_val), latex(k), 
                              latex(a_val), latex(a_val), latex(k), latex(a_val), latex(a_val)))

            list_nb_2 = [loigiai_nb_1]
            combined_nb = list(zip(list_nb_1, list_nb_2))

            ########################################################################
            # Thông hiểu: Tính f'(x1)
            th_da_1_d = '\\True $f\'\\left( %s \\right) = %s$' %(latex(x1), latex(val_f_prime_x1))
            th_da_1_s = '$f\'\\left( %s \\right) = %s$' %(latex(x1), latex(val_f_prime_x1 + randint(1, 3)))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            loigiai_th_1 = ('''Thay $x_0 = %s$ vào biểu thức $f\'\\left( x_0 \\right) = \\frac{%s}{\\left( %s - x_0 \\right)^2}$, ta được:\\\\
            $f\'\\left( %s \\right) = \\frac{%s}{\\left( %s - %s \\right)^2} = %s$.'''
                            %(latex(x1), latex(k), latex(a_val), latex(x1), latex(k), latex(a_val), latex(x1), latex(val_f_prime_x1)))

            list_th_2 = [loigiai_th_1]
            combined_th = list(zip(list_th_1, list_th_2))

            ########################################################################
            # Vận dụng: Tính f'(x2)
            vd_da_1_d = '\\True $f\'\\left( %s \\right) = %s$' %(latex(x2), latex(val_f_prime_x2))
            vd_da_1_s = '$f\'\\left( %s \\right) = %s$' %(latex(x2), latex(Rational(1, randint(5, 10))))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = ('''Thay $x_0 = %s$ vào biểu thức $f\'\\left( x_0 \\right) = \\frac{%s}{\\left( %s - x_0 \\right)^2}$, ta được:\\\\
            $f\'\\left( %s \\right) = \\frac{%s}{\\left( %s - %s \\right)^2} = %s$.'''
                            %(latex(x2), latex(k), latex(a_val), latex(x2), latex(k), latex(a_val), latex(x2), latex(val_f_prime_x2)))

            list_vd_2 = [loigiai_vd_1]
            combined_vd = list(zip(list_vd_1, list_vd_2))

            ########################################################################
            # Vận dụng cao: Tổng f'(x1) + f'(x2)
            vdc_da_1_d = '\\True $f\'\\left( %s \\right) + f\'\\left( %s \\right) = %s$' %(latex(x1), latex(x2), latex(tong_f_prime))
            vdc_da_1_s = '$f\'\\left( %s \\right) + f\'\\left( %s \\right) = %s$' %(latex(x1), latex(x2), latex(tong_f_prime - Rational(1, 2)))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = ('''Từ kết quả các câu trên, ta có:\\\\
            $f\'\\left( %s \\right) + f\'\\left( %s \\right) = %s + %s = %s$.'''
                             %(latex(x1), latex(x2), latex(val_f_prime_x1), latex(val_f_prime_x2), latex(tong_f_prime)))

            list_vdc_2 = [loigiai_vdc_1]
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 đúng
            while True:
                nb_sel = random.choice(list_nb_da_1)
                th_sel = random.choice(list_th_da_1)
                vd_sel = random.choice(list_vd_da_1)
                vdc_sel = random.choice(list_vdc_da_1)

                answers = [nb_sel, th_sel, vd_sel, vdc_sel]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán lại giá trị đã chọn vào list để xử lý zip
            list_nb_1 = [nb_sel]
            list_th_1 = [th_sel]
            list_vd_1 = [vd_sel]
            list_vdc_1 = [vdc_sel]

            # Cập nhật lại combined với các lựa chọn đã chốt từ vòng lặp while
            combined_nb = list(zip(list_nb_1, list_nb_2))
            combined_th = list(zip(list_th_1, list_th_2))
            combined_vd = list(zip(list_vd_1, list_vd_2))
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # Xuất câu hỏi
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\\choiceTFn \n'
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
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


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


def bt_dang6_p2_b4_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Thiết lập các hệ số của bài toán trong ảnh
            # sqrt(a*x^2 + b*x + c) = d*x + e
            a_val, b_val, c_val = 2, 1, -6
            d_val, e_val = 1, 2

            # Biểu thức dưới căn và vế phải
            f_left = a_val*x**2 + b_val*x + c_val
            f_right = d_val*x + e_val

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho phương trình $\\sqrt{%s} = %s \\quad (*)$.''' 
                             %(latex(f_left), latex(f_right)))

            ########################################################################
            # Nhận biết - Ý a: Bình phương 2 vế
            ########################################################################
            # Phương trình sau khi bình phương: (a-d^2)x^2 + (b-2de)x + (c-e^2) = 0
            eq_sq = sp.simplify(f_left - f_right**2)
            nb_da_1_d = '\\True Bình phương 2 vế phương trình ta được $%s = 0$' %(latex(eq_sq))
            nb_da_1_s = 'Bình phương 2 vế phương trình ta được $%s = 0$' %(latex(eq_sq + 2*x)) # Sai hệ số
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ('''Bình phương hai vế của phương trình $(*)$, ta có:\\\\
                            $%s = (%s)^2 \\Leftrightarrow %s = %s \\Leftrightarrow %s = 0$.'''
                            %(latex(f_left), latex(f_right), latex(f_left), latex(f_right**2), latex(eq_sq)))

            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # Thông hiểu - Ý b: Điều kiện
            ########################################################################
            th_da_1_d = '\\True Điều kiện của phương trình (*) là $x \\ge %s$' %(latex(-Rational(e_val, d_val)))
            th_da_1_s = 'Điều kiện của phương trình (*) là $x \\ge %s$' %(latex(Rational(e_val, d_val))) # Sai dấu (giống đề bài x >= 2)
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ('''Phương trình có dạng $\\sqrt{A}=B$, điều kiện có nghiệm là $B \\ge 0$.\\\\
                            Ta có: $%s \\ge 0 \\Leftrightarrow x \\ge %s$.'''
                            %(latex(f_right), latex(-Rational(e_val, d_val))))

            list_th_2 = [loigiai_th_1]

            ########################################################################
            # Vận dụng - Ý c: Số nghiệm
            ########################################################################
            # Giải phương trình hệ quả
            roots = sp.solve(eq_sq, x)
            # Lọc nghiệm thỏa điều kiện x >= -2
            valid_roots = [r for r in roots if r >= -Rational(e_val, d_val)]
            num_roots = len(valid_roots)

            vd_da_1_d = '\\True Phương trình (*) có %s nghiệm' %(num_roots)
            vd_da_1_s = 'Phương trình (*) có %s nghiệm' %(num_roots - 1 if num_roots > 1 else 2)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ('''Giải phương trình $x^2 - 3x - 10 = 0$, ta tìm được $x = 5$ và $x = -2$.\\\\
                            Đối chiếu với điều kiện $x \\ge -2$, ta thấy cả hai nghiệm đều thỏa mãn.\\\\
                            Vậy phương trình có %s nghiệm là $x_1 = 5, x_2 = -2$.''' %(num_roots))

            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # Vận dụng cao - Ý d: Tổng bình phương các nghiệm
            ########################################################################
            sum_sq = sum(r**2 for r in valid_roots)
            vdc_da_1_d = '\\True Tổng bình phương các nghiệm của phương trình (*) bằng %s' %(latex(sum_sq))
            vdc_da_1_s = 'Tổng bình phương các nghiệm của phương trình (*) bằng 20' # Giống đề bài
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = ('''Các nghiệm của phương trình là $x_1 = 5$ và $x_2 = -2$.\\\\
                             Tổng bình phương các nghiệm là: $5^2 + (-2)^2 = 25 + 4 = %s$.''' %(latex(sum_sq)))

            list_vdc_2 = [loigiai_vdc_1]

            ########################################################################
            # Logic chọn đáp án và xuất bản (Giữ nguyên cấu trúc mẫu)
            ########################################################################
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Đóng gói kết quả
            shuffled_answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\\choiceTFn \n'
                '{'+str(shuffled_answers[0])+'}\n'
                '{'+str(shuffled_answers[1])+'}\n'
                '{'+str(shuffled_answers[2])+'}\n'
                '{'+str(shuffled_answers[3])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions[0])+'\n'
                '\\item '+str(shuffled_solutions[1])+'\n'
                '\\item '+str(shuffled_solutions[2])+'\n'
                '\\item '+str(shuffled_solutions[3])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


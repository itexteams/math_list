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


def bt_dang4_p2_b3_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến sympy
            x = symbols('x')

            # B1: Nghiên cứu đề bài và thiết lập hằng số random
            # f(x) = a*x^3 + b*x + c
            # g(x) = e^(k*x + m)
            a = random.randint(1, 2)
            b = random.randint(2, 4)
            c = random.randint(1, 3)
            k = random.randint(2, 3)
            m = random.randint(1, 2)

            # Các điểm tính giá trị đạo hàm
            x0 = random.randint(-2, -1)
            x1 = random.randint(1, 2)

            # Thiết lập hàm số và đạo hàm
            f = a*x**3 + b*x + c
            g = exp(k*x + m)

            f1 = diff(f, x)
            f2 = diff(f, x, 2)
            g1 = diff(g, x)
            g2 = diff(g, x, 2)

            # Tính giá trị cụ thể
            val_f2 = f2.subs(x, x0)
            val_g2_expr = k**2  # Hệ số trước e
            val_g2_exp = k*x1 + m # Số mũ

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hai hàm số $f\\left( x \\right) = %s$ và $g\\left( x \\right) = e^{%s x + %s}$.''' 
                             %(latex(f), latex(k), latex(m)))

            ########################################################################
            # Nhận biết ############################################
            # Kiểm tra f''(x)
            nb_da_1_d = '\\True Đạo hàm cấp hai của hàm số $f\\left( x \\right)$ là $f\'\'\\left( x \\right) = %s$' %(latex(f2))
            nb_da_1_s = 'Đạo hàm cấp hai của hàm số $f\\left( x \\right)$ là $f\'\'\\left( x \\right) = %s$' %(latex(f1))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Ta có $f\'\\left( x \\right) = %s \\Rightarrow f\'\'\\left( x \\right) = %s$.''' 
                            %(latex(f1), latex(f2)))
            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # Thông hiểu ############################################
            # Kiểm tra g''(x)
            th_da_1_d = '\\True Đạo hàm cấp hai của hàm số $g\\left( x \\right)$ là $g\'\'\\left( x \\right) = %s e^{%s x + %s}$' %(latex(k**2), latex(k), latex(m))
            th_da_1_s = 'Đạo hàm cấp hai của hàm số $g\\left( x \\right)$ là $g\'\'\\left( x \\right) = %s e^{%s x - %s}$' %(latex(k**2), latex(k), latex(m))
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            # Nội dung lời giải
            loigiai_th_1 = ('''Ta có $g\'\\left( x \\right) = %s e^{%s x + %s} \\Rightarrow g\'\'\\left( x \\right) = %s e^{%s x + %s}$.''' 
                            %(latex(k), latex(k), latex(m), latex(k**2), latex(k), latex(m)))
            list_th_2 = [loigiai_th_1]

            ########################################################################
            # Vận dụng ############################################
            # Giá trị f''(x0)
            vd_da_1_d = '\\True Đạo hàm cấp hai của hàm số $f\\left( x \\right)$ tại $x_0 = %s$ là $f\'\'\\left( %s \\right) = %s$' %(latex(x0), latex(x0), latex(val_f2))
            vd_da_1_s = 'Đạo hàm cấp hai của hàm số $f\\left( x \\right)$ tại $x_0 = %s$ là $f\'\'\\left( %s \\right) = %s$' %(latex(x0), latex(x0), latex(val_f2 + 2))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Thay $x = %s$ vào biểu thức $f\'\'\\left( x \\right) = %s$, ta được \\\\ $f\'\'\\left( %s \\right) = %s \\cdot \\left( %s \\right) = %s$.''' 
                            %(latex(x0), latex(f2), latex(x0), latex(6*a), latex(x0), latex(val_f2)))
            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # Vận dụng cao ############################################
            # Giá trị g''(x1)
            vdc_da_1_d = '\\True Đạo hàm cấp hai của hàm số $g\\left( x \\right)$ tại $x_0 = %s$ là $g\'\'\\left( %s \\right) = %s e^{%s}$' %(latex(x1), latex(x1), latex(val_g2_expr), latex(val_g2_exp))
            vdc_da_1_s = 'Đạo hàm cấp hai của hàm số $g\\left( x \\right)$ tại $x_0 = %s$ là $g\'\'\\left( %s \\right) = %s e^{%s}$' %(latex(x1), latex(x1), latex(k), latex(val_g2_exp))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Thay $x = %s$ vào biểu thức $g\'\'\\left( x \\right) = %s e^{%s x + %s}$, ta được \\\\ $g\'\'\\left( %s \\right) = %s e^{%s \\cdot %s + %s} = %s e^{%s}$.''' 
                             %(latex(x1), latex(k**2), latex(k), latex(m), latex(x1), latex(k**2), latex(k), latex(x1), latex(m), latex(k**2), latex(val_g2_exp)))
            list_vdc_2 = [loigiai_vdc_1]

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 đúng
            while True:
                nb_sel = random.choice(list_nb_da_1)
                th_sel = random.choice(list_th_da_1)
                vd_sel = random.choice(list_vd_da_1)
                vdc_sel = random.choice(list_vdc_da_1)

                answers = [nb_sel, th_sel, vd_sel, vdc_sel]
                if 1 <= count_true_answers(answers) <= 3:
                    break

            # Đóng gói kết quả xáo trộn
            def shuffle_pair(ans_list, sol_list, selected_ans):
                # Tìm index của đáp án đã chọn trong list gốc để lấy lời giải tương ứng
                # Ở đây mỗi phần chỉ có 1 lời giải cố định, nhưng ta giữ cấu trúc zip để đúng mẫu
                combined = list(zip(ans_list, sol_list))
                # Trong bài này, sol_list chỉ có 1 phần tử nên ta lấy [0]
                return selected_ans, sol_list[0]

            res_nb_a, res_nb_s = shuffle_pair(list_nb_da_1, list_nb_2, nb_sel)
            res_th_a, res_th_s = shuffle_pair(list_th_da_1, list_th_2, th_sel)
            res_vd_a, res_vd_s = shuffle_pair(list_vd_da_1, list_vd_2, vd_sel)
            res_vdc_a, res_vdc_s = shuffle_pair(list_vdc_da_1, list_vdc_2, vdc_sel)

            # Xuất câu hỏi
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' +
                str(noidungcauhoi) + 
                '\n\\choiceTFn \n'
                '{' + str(res_nb_a) + '}\n'
                '{' + str(res_th_a) + '}\n'
                '{' + str(res_vd_a) + '}\n'
                '{' + str(res_vdc_a) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(res_nb_s) + '\n'
                '\\item ' + str(res_th_s) + '\n'
                '\\item ' + str(res_vd_s) + '\n'
                '\\item ' + str(res_vdc_s) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n\\end{minipage}\n\n')
            return content


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


def bt_dang10_p2_b4_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # --- BƯỚC 1: SINH DỮ LIỆU ---
            # Thiết lập thông số dựa trên đề bài trong ảnh
            # Phương trình (1): sqrt(5x + 10) = 8 - x
            a1, b1, c1 = 5, 10, 8
            eq1_L = sqrt(a1*x + b1)
            eq1_R = c1 - x

            # Phương trình (2): sqrt(3x^2 - 9x + 1) = x - 2
            a2, b2, c2, d2 = 3, -9, 1, -2
            eq2_L = sqrt(a2*x**2 + b2*x + c2)
            eq2_R = x + d2

            # --- BƯỚC 2: GIẢI TOÁN ---
            # Giải phương trình (1)
            sol1_all = solve(sp.Eq(a1*x + b1, (c1 - x)**2), x)
            sol1 = [s for s in sol1_all if (c1 - s) >= 0]

            # Giải phương trình (2)
            sol2_all = solve(sp.Eq(a2*x**2 + b2*x + c2, (eq2_R)**2), x)
            sol2 = [s for s in sol2_all if (s + d2) >= 0]

            # Các giá trị logic
            count1 = len(sol1)
            count2 = len(sol2)
            is_same_set = set(sol1) == set(sol2)
            tong_nghiem = sum(sol1) + sum(sol2)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho 2 phương trình $%s = %s$ (1) và $%s = %s$ (2).''' 
                             %(latex(eq1_L), latex(eq1_R), latex(eq2_L), latex(eq2_R)))

            ########################################################################
            # Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Phương trình (1) có %s nghiệm' % (count1)
            nb_da_1_s = 'Phương trình (1) có %s nghiệm' % (count1 + 1)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Phương trình (1) $\\Leftrightarrow \\begin{cases} %s \\ge 0 \\\\ %s = (%s)^2 \\end{cases} \\Leftrightarrow \\begin{cases} x \\le %s \\\\ %s = 0 \\end{cases}$. \\\\
                            Giải ra ta được $x \\in \\{%s\\}$. Đối chiếu điều kiện ta có nghiệm $x = %s$. \\\\ Vậy phương trình (1) có %s nghiệm.''' 
                            %(latex(eq1_R), latex(a1*x + b1), latex(eq1_R), latex(c1), latex(sp.simplify((c1-x)**2 - (a1*x + b1))), 
                              ", ".join([latex(s) for s in sol1_all]), ", ".join([latex(s) for s in sol1]), count1))

            list_nb_2 = [loigiai_nb_1]
            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Phương trình (2) có %s nghiệm' % (count2)
            th_da_1_s = 'Phương trình (2) có 2 nghiệm' if count2 != 2 else 'Phương trình (2) vô nghiệm'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Phương trình (2) $\\Leftrightarrow \\begin{cases} %s \\ge 0 \\\\ %s = (%s)^2 \\end{cases} \\Leftrightarrow \\begin{cases} x \\ge %s \\\\ %s = 0 \\end{cases}$. \\\\
                            Giải ra ta được $x \\in \\{%s\\}$. Đối chiếu điều kiện ta có nghiệm $x = %s$. \\\\ Vậy phương trình (2) có %s nghiệm.''' 
                            %(latex(eq2_R), latex(a2*x**2 + b2*x + c2), latex(eq2_R), latex(-d2), latex(sp.simplify(a2*x**2 + b2*x + c2 - (eq2_R)**2)), 
                              ", ".join([latex(s) for s in sol2_all]), ", ".join([latex(s) for s in sol2]), count2))

            list_th_2 = [loigiai_th_1]
            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Phương trình (1) và (2) có chung tập nghiệm' if is_same_set else '\\True Phương trình (1) và (2) không có chung tập nghiệm'
            vd_da_1_s = 'Phương trình (1) và (2) không có chung tập nghiệm' if is_same_set else 'Phương trình (1) và (2) có chung tập nghiệm'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Dựa vào kết quả giải ở trên: \\\\
                            Tập nghiệm phương trình (1) là $S_1 = \\{%s\\}$. \\\\
                            Tập nghiệm phương trình (2) là $S_2 = \\{%s\\}$. \\\\
                            Vậy hai phương trình %s chung tập nghiệm.''' 
                            %(", ".join([latex(s) for s in sol1]), ", ".join([latex(s) for s in sol2]), "có" if is_same_set else "không có"))

            list_vd_2 = [loigiai_vd_1]
            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Tổng các nghiệm của phương trình (1) và (2) bằng %s' % (latex(tong_nghiem))
            vdc_da_1_s = 'Tổng các nghiệm của phương trình (1) và (2) bằng %s' % (latex(tong_nghiem + 1))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Tổng các nghiệm của phương trình (1) là $T_1 = %s$. \\\\
                            Tổng các nghiệm của phương trình (2) là $T_2 = %s$. \\\\
                            Tổng các nghiệm của cả hai phương trình là $T = T_1 + T_2 = %s$.''' 
                             %(latex(sum(sol1)), latex(sum(sol2)), latex(tong_nghiem)))

            list_vdc_2 = [loigiai_vdc_1]
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

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

            # Cập nhật lại danh sách sau khi chọn đúng số lượng câu True
            shuffled_answers_nb = [nb_da_1]
            shuffled_answers_th = [th_da_1]
            shuffled_answers_vd = [vd_da_1]
            shuffled_answers_vdc = [vdc_da_1]

            # Xuất nội dung
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
                '\\end{ex}\n \\end{minipage}\n\n')
            return content


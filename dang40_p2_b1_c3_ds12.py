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


def bt_dang40_p2_b1_c3_ds12(self):
            # Khai báo biến ký hiệu
            # Khai báo biến
            x = symbols('x')

            # Random các hệ số
            # Chọn a_val ngẫu nhiên từ 1 đến 3 để đảm bảo f'(x) > 0 luôn đúng
            a_val = random.randint(1, 3) 
            c1 = random.randint(-5, 5) # Giá trị của f(0)
            c2 = random.randint(-5, 5) # Giá trị của F(0)

            # Các hằng số được tính toán
            a3 = 3 * a_val
            a6 = 6 * a_val
            a3_minus_1 = a3 - 1
            c3 = c2 + 1

            # Xử lý chuỗi để in ra LaTeX đẹp mắt (tránh các dấu cộng trừ liền nhau)
            ax3_str = "x^3" if a_val == 1 else "%sx^3" % a_val
            c1_str = "" if c1 == 0 else (" + %s" % c1 if c1 > 0 else " - %s" % abs(c1))
            f_x_str = "%s + \\sin x%s" % (ax3_str, c1_str)

            if a_val == 1:
                a4_str = "\\frac{x^4}{4}"
            elif a_val == 2:
                a4_str = "\\frac{x^4}{2}"
            else:
                a4_str = "\\frac{3x^4}{4}"

            c1x_str = "" if c1 == 0 else (" + x" if c1 == 1 else (" - x" if c1 == -1 else (" + %sx" % c1 if c1 > 0 else " - %sx" % abs(c1))))
            c3_str = "" if c3 == 0 else (" + %s" % c3 if c3 > 0 else " - %s" % abs(c3))
            F_x_str = "%s - \\cos x%s%s" % (a4_str, c1x_str, c3_str)

            # Phương án sai cho mệnh đề b
            c3_false = c2
            c3_false_str = "" if c3_false == 0 else (" + %s" % c3_false if c3_false > 0 else " - %s" % abs(c3_false))
            F_x_false_str = "%s - \\cos x%s%s" % (a4_str, c1x_str, c3_false_str)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hàm số $y = f(x)$ xác định trên $\\mathbb{R}$ và có đạo hàm $f'(x) = %sx^2 + \\cos x$. Biết rằng $f(0) = %s$ và $F(x)$ là một nguyên hàm của $f(x)$ thỏa mãn $F(0) = %s$.'''
                             % (a3, c1, c2))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True $f(x) = %s$' % f_x_str
            nb_da_1_s = '$f(x) = %s - \\sin x%s$' % (ax3_str, c1_str)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Ta có $f(x) = \\int f'(x) \\text{d}x = \\int \\left(%sx^2 + \\cos x\\right) \\text{d}x = %s + \\sin x + C$. \\\\
            Theo giả thiết $f(0) = %s \\Leftrightarrow 0^3 + \\sin 0 + C = %s \\Rightarrow C = %s$. \\\\
            Khi đó $f(x) = %s$.'''
                            % (a3, ax3_str, c1, c1, c1, f_x_str))

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True $F(x) = %s$' % F_x_str
            th_da_1_s = '$F(x) = %s$' % F_x_false_str
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            c1_0_str = "" if c1 == 0 else (" + %s \\cdot 0" % c1 if c1 > 0 else " - %s \\cdot 0" % abs(c1))
            loigiai_th_1 = ('''Ta có $F(x) = \\int f(x) \\text{d}x = \\int \\left(%s\\right) \\text{d}x = %s - \\cos x%s + C'$. \\\\
            Theo giả thiết $F(0) = %s \\Leftrightarrow \\frac{0^4}{4} - \\cos 0%s + C' = %s \\Rightarrow -1 + C' = %s \\Rightarrow C' = %s$. \\\\
            Khi đó $F(x) = %s$.'''
                            % (f_x_str, a4_str, c1x_str, c2, c1_0_str, c2, c2, c3, F_x_str))

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Hàm số $y = f(x)$ đồng biến trên $\\mathbb{R}$'
            vd_da_1_s = 'Hàm số $y = f(x)$ nghịch biến trên $\\mathbb{R}$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Xét đạo hàm $f'(x) = %sx^2 + \\cos x$ và luôn có $\\cos x \\ge -1 \\forall x \\in \\mathbb{R}$. \\\\
            Nếu $|x| \\ge 1$ thì $%sx^2 \\ge %s \\Rightarrow f'(x) \\ge %s - 1 = %s > 0$. \\\\
            Nếu $|x| < 1$, ta xét hàm $g(x) = %sx^2 + \\cos x$ có $g'(x) = %sx - \\sin x$. \\\\
            Vì $|\\sin x| \\le |x|$ nên với $x > 0 \\Rightarrow %sx > \\sin x \\Rightarrow g'(x) > 0$; với $x < 0 \\Rightarrow g'(x) < 0$. \\\\
            Do đó $g(x)$ đạt giá trị nhỏ nhất tại $x=0$ nên Giá trị nhỏ nhất là $f'(0) = %s(0)^2 + \\cos(0) = 1$. \\\\
            Vì $f'(x) \\ge 1 > 0 \\forall x \\in \\mathbb{R}$ thì hàm số $y = f(x)$ luôn đồng biến trên $\\mathbb{R}$.'''
                            % (a3, a3, a3, a3, a3_minus_1, a3, a6, a6, a3))

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Đồ thị hàm số cắt trục hoành tại một điểm duy nhất'
            vdc_da_1_s = 'Đồ thị hàm số cắt trục hoành tại ba điểm phân biệt'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Hàm số $f(x)$ là hàm số luôn đồng biến trên $\\mathbb{R}$. \\\\
            Giới hạn của hàm số: $\\lim\\limits_{x \\to -\\infty} f(x) = -\\infty$ và $\\lim\\limits_{x \\to +\\infty} f(x) = +\\infty$. \\\\
            Kết hợp với việc hàm số luôn đồng biến (tăng liên tục từ $-\\infty$ đến $+\\infty$), đồ thị hàm số chắc chắn cắt trục hoành tại duy nhất một điểm.''')

            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vdc)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
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
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content


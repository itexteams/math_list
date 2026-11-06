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


def bt_dang17_p2_b3_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Thực hiện vòng lặp để khởi tạo các giá trị ngẫu nhiên hợp lý cho bài toán
            while True:
                x_0 = random.randint(1, 4)
                y_0 = random.randint(1, 4)
                a_val = random.randint(1, 2)
                b_val = random.randint(-3, 3)
                while b_val == 0:
                    b_val = random.randint(-3, 3)

                A_1 = random.choice([1, 2])
                B_1 = random.randint(-3, 3)
                while B_1 == 0:
                    B_1 = random.randint(-3, 3)

                # Đảm bảo tiệm cận đứng của hai hàm số không trùng nhau
                x_c2 = Rational(-B_1, A_1)
                if x_c2 == x_0:
                    continue

                R_val = random.choice([-2, -1, 1, 2])

                # Thiết lập tử số và mẫu số cho f(x) = (y_0*x + k) / (x - x_0)
                k_val = -y_0 * x_0 + random.choice([-2, -1, 1, 2])
                if k_val == 0:
                    k_val = 1

                tu_f = y_0 * x + k_val
                mau_f = x - x_0

                # Thiết lập tử số và mẫu số cho g(x) = a_val*x + b_val + R_val/(A_1*x + B_1)
                tu_g = expand((a_val * x + b_val) * (A_1 * x + B_1) + R_val)
                mau_g = A_1 * x + B_1

                # Tính diện tích tam giác tạo bởi 3 đường tiệm cận
                S_true = Rational((a_val * x_0 + b_val - y_0)**2, 2 * abs(a_val))
                if S_true > 0:
                    break

            # Tạo biểu thức hiển thị LaTeX cho câu hỏi
            ham_f_latex = '\\frac{%s}{%s}' % (latex(tu_f), latex(mau_f))
            ham_g_latex = '\\frac{%s}{%s}' % (latex(tu_g), latex(mau_g))

            # Nội dung câu hỏi sử dụng định dạng %s theo mẫu
            noidungcauhoi = ('''Cho hàm số $f(x)=%s$ có đồ thị $(C_1)$ và $g(x)=%s$ có đồ thị $(C_2)$. Biết đồ thị hàm số $(C_1)$ có tiệm cận đứng và tiệm cận ngang là các đường thẳng $x=x_0$, $y=y_0$; đồ thị hàm số $(C_2)$ có tiệm cận xiên là đường thẳng $\\Delta : y=ax+b$.''' 
                             % (ham_f_latex, ham_g_latex))

            ########################################################################
            # Nhận biết ############################################
            # Các đáp án
            val_true = x_0 + 2 * y_0 + 3 * b_val
            val_false = val_true + random.choice([-2, -1, 1, 2])

            nb_da_1_d = '\\True $x_0 + 2y_0 + 3b = %s$' % (latex(val_true))
            nb_da_1_s = '$x_0 + 2y_0 + 3b = %s$' % (latex(val_false))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Từ hàm số $f(x) = %s$, ta có tiệm cận đứng là $x = %s$ và tiệm cận ngang là $y = %s$, do đó $x_0 = %s$ và $y_0 = %s$.\\\\
            Từ hàm số $g(x) = %s = %s x + %s + \\frac{%s}{%s}$, ta có tiệm cận xiên là $\\Delta: y = %s x + %s$, do đó $a = %s$ và $b = %s$.\\\\
            Giá trị của biểu thức là: $x_0 + 2y_0 + 3b = %s + 2 \\cdot %s + 3 \\cdot (%s) = %s$.''' 
                            % (ham_f_latex, latex(x_0), latex(y_0), latex(x_0), latex(y_0),
                               ham_g_latex, latex(a_val), latex(b_val), latex(R_val), latex(mau_g),
                               latex(a_val), latex(b_val), latex(a_val), latex(b_val),
                               latex(x_0), latex(y_0), latex(b_val), latex(val_true)))

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Đồ thị hàm số $(C_2)$ không có tiệm cận ngang'
            th_da_1_s = 'Đồ thị hàm số $(C_2)$ có tiệm cận ngang là đường thẳng $y = \\frac{1}{2}$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Xét hàm số $g(x) = %s$. Vì bậc của tử số lớn hơn bậc của mẫu số đúng 1 bậc nên $\\lim_{x \\to \\pm\\infty} g(x) = \\pm\\infty$, do đó đồ thị hàm số $(C_2)$ không có tiệm cận ngang mà chỉ có tiệm cận đứng và tiệm cận xiên.''' 
                            % (ham_g_latex))

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Đồ thị hàm số $(C_1)$ và $(C_2)$ không có chung đường tiệm cận đứng'
            vd_da_1_s = 'Đồ thị hàm số $(C_1)$ và $(C_2)$ có chung đường tiệm cận đứng'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Đồ thị hàm số $(C_1)$ có đường tiệm cận đứng là $x = %s$.\\\\
            Đồ thị hàm số $(C_2)$ có đường tiệm cận đứng là $x = %s$.\\\\
            Vì $%s \\neq %s$ nên đồ thị hàm số $(C_1)$ và $(C_2)$ không có chung đường tiệm cận đứng.''' 
                            % (latex(x_0), latex(x_c2), latex(x_0), latex(x_c2)))

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao ############################################
            # Các đáp án
            S_wrong = S_true + random.choice([1, Rational(1, 2)])
            vdc_da_1_d = '\\True Giao điểm của ba đường tiệm cận $x = x_0$, $y = y_0$ và $y = ax + b$ tạo thành tam giác có diện tích bằng $%s$' % (latex(S_true))
            vdc_da_1_s = 'Giao điểm của ba đường tiệm cận $x = x_0$, $y = y_0$ và $y = ax + b$ tạo thành tam giác có diện tích bằng $%s$' % (latex(S_wrong))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            y_A = a_val * x_0 + b_val
            x_B = Rational(y_0 - b_val, a_val)
            loigiai_vdc_1 = ('''Ba đường tiệm cận gồm có: $x = %s$, $y = %s$ và $y = %s x + %s$.\\\\
            - Giao điểm của $x = %s$ và $y = %s$ là $I\\left(%s; %s\\right)$.\\\\
            - Giao điểm của $x = %s$ và $y = %s x + %s$ là $A\\left(%s; %s\\right)$.\\\\
            - Giao điểm của $y = %s$ và $y = %s x + %s$ là $B\\left(%s; %s\\right)$.\\\\
            Tam giác $IAB$ vuông tại $I$, có độ dài hai cạnh góc vuông là:\\\\
            $IA = |%s - %s| = %s$.\\\\
            $IB = |%s - %s| = %s$.\\\\
            Diện tích tam giác $IAB$ là: $S = \\frac{1}{2} \\cdot IA \\cdot IB = \\frac{1}{2} \\cdot %s \\cdot %s = %s$.''' 
                             % (latex(x_0), latex(y_0), latex(a_val), latex(b_val),
                                latex(x_0), latex(y_0), latex(x_0), latex(y_0),
                                latex(x_0), latex(a_val), latex(b_val), latex(x_0), latex(y_A),
                                latex(y_0), latex(a_val), latex(b_val), latex(x_B), latex(y_0),
                                latex(y_A), latex(y_0), latex(abs(y_A - y_0)),
                                latex(x_B), latex(x_0), latex(abs(x_B - x_0)),
                                latex(abs(y_A - y_0)), latex(abs(x_B - x_0)), latex(S_true)))

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
                str(noidungcauhoi) + '\n'
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


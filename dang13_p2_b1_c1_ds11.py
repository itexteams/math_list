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


def bt_dang13_p2_b1_c1_ds11(self):
            # Khai báo biến
            # Bước 1: Nghiên cứu đề bài và chọn phương án random số đẹp
            # Chọn ngẫu nhiên mẫu số của phân số trong biểu thức c và d (đề bài mẫu là 5 và 8)
            # Ta chọn ngẫu nhiên các mẫu số trong khoảng từ 3 đến 9 để đảm bảo số không quá lớn
            m_c = randint(3, 7)
            m_d = randint(4, 9)

            # Chọn tử số tương ứng sao cho góc không vượt quá chu kỳ hoặc giữ nguyên tính chất bài toán mẫu
            t_c = randint(1, m_c - 1)
            t_d = randint(1, m_d - 1)

            # Định nghĩa các phân số bằng SymPy Rational
            frac_c = Rational(t_c, m_c)
            frac_d = Rational(t_d, m_d)

            # Tính toán các đầu mút khoảng để lập luận lời giải chính xác
            # Ý a: alpha + pi -> khoảng (pi; 3*pi/2) -> góc thuộc góc phần tư thứ III -> cos < 0
            # Ý b: alpha - pi -> khoảng (-pi; -pi/2) -> góc thuộc góc phần tư thứ III -> tan > 0
            # Ý c: alpha + frac_c * pi -> khoảng (frac_c * pi; (1/2 + frac_c) * pi)
            # Ý d: alpha - frac_d * pi -> khoảng (-frac_d * pi; (1/2 - frac_d) * pi)

            # Biến để kiểm tra dấu thực tế (True tương ứng với > 0, False tương ứng với < 0)
            # Ý a: cos luôn < 0
            sign_a_real = "<"
            # Ý b: tan luôn > 0
            sign_b_real = ">"

            # Ý c: sin của góc trong khoảng (t_c/m_c * pi ; (1/2 + t_c/m_c)*pi)
            # Để đơn giản và chính xác tuyệt đối, ta kiểm tra điểm giữa của khoảng: alpha = pi/4
            alpha_test = math.pi / 4
            val_c = math.sin(alpha_test + (t_c / m_c) * math.pi)
            sign_c_real = ">" if val_c > 0 else "<"

            # Ý d: cos của góc trong khoảng (-t_d/m_d * pi ; (1/2 - t_d/m_d)*pi)
            val_d = math.cos(alpha_test - (t_d / m_d) * math.pi)
            sign_d_real = ">" if val_d > 0 else "<"

            # Random dấu hiển thị trong câu hỏi để tạo câu Đúng / Sai ngẫu nhiên
            sign_a_show = random.choice(["<", ">"])
            sign_b_show = random.choice(["<", ">"])
            sign_c_show = random.choice(["<", ">"])
            sign_d_show = random.choice(["<", ">"])

            # Nội dung câu hỏi gốc
            noidungcauhoi = ('''Cho $0 < \\alpha < \\frac{\\pi}{2}$. Xét được dấu của các biểu thức sau. Khi đó:''')

            ########################################################################
            # Nhận biết ############################################
            # Kiểm tra câu đúng sai của ý a
            is_a_true = (sign_a_show == sign_a_real)
            prefix_a = "\\True " if is_a_true else ""
            nb_da_1 = '%s$A = \\cos(\\alpha + \\pi) %s 0$' % (prefix_a, sign_a_show)
            list_nb_1 = [nb_da_1]

            # Lời giải chi tiết ý a
            loigiai_nb_1 = ('''Vì $0 < \\alpha < \\frac{\\pi}{2} \\Rightarrow \\pi < \\alpha + \\pi < \\frac{3\\pi}{2} \\Rightarrow \\cos(\\alpha + \\pi) < 0$.''')
            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            # Kiểm tra câu đúng sai của ý b
            is_b_true = (sign_b_show == sign_b_real)
            prefix_b = "\\True " if is_b_true else ""
            th_da_1 = '%s$B = \\tan(\\alpha - \\pi) %s 0$' % (prefix_b, sign_b_show)
            list_th_1 = [th_da_1]

            # Lời giải chi tiết ý b
            loigiai_th_1 = ('''Vì $0 < \\alpha < \\frac{\\pi}{2} \\Rightarrow -\\pi < \\alpha - \\pi < -\\frac{\\pi}{2} \\Rightarrow \\tan(\\alpha - \\pi) > 0$.''')
            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng ############################################
            # Kiểm tra câu đúng sai của ý c
            is_c_true = (sign_c_show == sign_c_real)
            prefix_c = "\\True " if is_c_true else ""
            vd_da_1 = '%s$C = \\sin\\left(\\alpha + \\frac{%s\\pi}{%s}\\right) %s 0$' % (prefix_c, latex(t_c), latex(m_c), sign_c_show)
            list_vd_1 = [vd_da_1]

            # Lời giải chi tiết ý c sử dụng Rational để quy đồng mẫu số phân số lượng giác
            frac_c_right = Rational(1, 2) + frac_c
            loigiai_vd_1 = ('''Vì $0 < \\alpha < \\frac{\\pi}{2} \\Rightarrow \\frac{%s\\pi}{%s} < \\alpha + \\frac{%s\\pi}{%s} < \\frac{%s\\pi}{%s} \\Rightarrow \\sin\\left(\\alpha + \\frac{%s\\pi}{%s}\\right) %s 0$.'''
                            % (latex(t_c), latex(m_c), latex(t_c), latex(m_c), latex(frac_c_right.p), latex(frac_c_right.q), latex(t_c), latex(m_c), sign_c_real))
            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao ############################################
            # Kiểm tra câu đúng sai của ý d
            is_d_true = (sign_d_show == sign_d_real)
            prefix_d = "\\True " if is_d_true else ""
            vdc_da_1 = '%s$D = \\cos\\left(\\alpha - \\frac{%s\\pi}{%s}\\right) %s 0$' % (prefix_d, latex(t_d), latex(m_d), sign_d_show)
            list_vdc_1 = [vdc_da_1]

            # Lời giải chi tiết ý d sử dụng Rational để quy đồng mẫu số phân số lượng giác
            frac_d_right = Rational(1, 2) - frac_d
            # Xử lý chuỗi hiển thị cho tử số của frac_d_right khi âm hoặc dương
            if frac_d_right.p < 0:
                str_d_right = '-\\frac{%s\\pi}{%s}' % (latex(abs(frac_d_right.p)), latex(frac_d_right.q))
            else:
                str_d_right = '\\frac{%s\\pi}{%s}' % (latex(frac_d_right.p), latex(frac_d_right.q))

            loigiai_vdc_1 = ('''Vì $0 < \\alpha < \\frac{\\pi}{2} \\Rightarrow -\\frac{%s\\pi}{%s} < \\alpha - \\frac{%s\\pi}{%s} < %s \\Rightarrow \\cos\\left(\\alpha - \\frac{%s\\pi}{%s}\\right) %s 0$.'''
                             % (latex(t_d), latex(m_d), latex(t_d), latex(m_d), str_d_right, latex(t_d), latex(m_d), sign_d_real))
            list_vdc_2 = [loigiai_vdc_1]

            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)


            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)


            # Lặp kiểm tra điều kiện đề bài: Có từ 1 đến 3 câu đúng
            while True:
                # Nếu không thỏa mãn số lượng câu đúng mong muốn, tiến hành random lại các dấu hiển thị
                sign_a_show = random.choice(["<", ">"])
                sign_b_show = random.choice(["<", ">"])
                sign_c_show = random.choice(["<", ">"])
                sign_d_show = random.choice(["<", ">"])

                is_a_true = (sign_a_show == sign_a_real)
                is_b_true = (sign_b_show == sign_b_real)
                is_c_true = (sign_c_show == sign_c_real)
                is_d_true = (sign_d_show == sign_d_real)

                answers = [
                    "\\True" if is_a_true else "",
                    "\\True" if is_b_true else "",
                    "\\True" if is_c_true else "",
                    "\\True" if is_d_true else ""
                ]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    # Cập nhật lại các biến hiển thị chính thức
                    nb_da_1 = '%s$A = \\cos(\\alpha + \\pi) %s 0$' % ("\\True " if is_a_true else "", sign_a_show)
                    th_da_1 = '%s$B = \\tan(\\alpha - \\pi) %s 0$' % ("\\True " if is_b_true else "", sign_b_show)
                    vd_da_1 = '%s$C = \\sin\\left(\\alpha + \\frac{%s\\pi}{%s}\\right) %s 0$' % ("\\True " if is_c_true else "", latex(t_c), latex(m_c), sign_c_show)
                    vdc_da_1 = '%s$D = \\cos\\left(\\alpha - \\frac{%s\\pi}{%s}\\right) %s 0$' % ("\\True " if is_d_true else "", latex(t_d), latex(m_d), sign_d_show)
                    break

            # Gán lại vào list sau khi đã thỏa mãn điều kiện số lượng câu đúng
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

            # Xuất câu hỏi với đáp án và lời giải đúng cấu trúc đề bài yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' +
                       str(noidungcauhoi) +
                       '\n\\choiceTFn \n'
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


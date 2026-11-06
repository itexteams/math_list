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


def bt_dang39_p2_b1_c3_ds12(self):
            # Khai báo biến ký hiệu
            # Khai báo biến
            x = symbols('x')

            # Random các hằng số để tạo bài toán mới (m = t_max)
            m_list = [2, 4]
            m = random.choice(m_list)
            a_list = [2, 4, 6]
            a = random.choice(a_list)

            # Tính toán các hệ số dựa trên tham số random để nghiệm luôn đẹp
            k = a + m
            t_meet = int(3 * m / 2)
            d_max_val = Fraction(m**3, 6)

            def format_frac(f):
                if f.denominator == 1:
                    return str(f.numerator)
                return "\\frac{%s}{%s}" % (f.numerator, f.denominator)

            d_max_tex = format_frac(d_max_val)

            k_over_2_tex = format_frac(Fraction(k, 2))
            a_over_2_tex = format_frac(Fraction(a, 2))
            diff_over_2_tex = format_frac(Fraction(m, 2))

            # Lược bỏ số 1 đứng trước t^2 cho đẹp (vd: 1t^2 -> t^2)
            k_over_2_str = "" if k_over_2_tex == "1" else k_over_2_tex
            a_over_2_str = "" if a_over_2_tex == "1" else a_over_2_tex
            diff_coeff_str = "" if diff_over_2_tex == "1" else diff_over_2_tex

            # Tính vận tốc tại thời điểm gặp nhau
            vA_meet = k * t_meet - t_meet**2
            vB_meet = a * t_meet

            cmp_correct = "lớn hơn" if vA_meet > vB_meet else "nhỏ hơn"
            cmp_wrong = "nhỏ hơn" if vA_meet > vB_meet else "lớn hơn"
            cmp_sign = ">" if vA_meet > vB_meet else "<"

            # Nội dung câu hỏi
            noidungcauhoi = ('Trên một trục tọa độ $Ox$, hai chất điểm đồng thời xuất phát từ gốc tọa độ $O$ tại thời điểm $t = 0$ và chuyển động cùng chiều dương. Chất điểm thứ nhất chuyển động với vận tốc biến thiên theo quy luật $v_A(t) = %st - t^2$ (m/s) còn chất điểm thứ hai chuyển động nhanh dần đều với gia tốc không đổi là $a = %s$ (m/s$^2$).' % (k, a))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Phương trình vận tốc của chất điểm thứ hai là $v_B(t) = %st$ (m/s)' % (a)
            nb_da_1_s = 'Phương trình vận tốc của chất điểm thứ hai là $v_B(t) = %st$ (m/s)' % (a + 2)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('Ta có $v_B(t) = \\int %s \\text{d}t = %st + C_1$ mà $v_B(0) = 0 \\Rightarrow C_1 = 0$ suy ra $v_B(t) = %st$ (m/s) nên mệnh đề đúng.' % (a, a, a))

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
            th_da_1_d = '\\True Hai chất điểm gặp nhau tại thời điểm $t = %s$ (giây)' % (t_meet)
            th_da_1_s = 'Hai chất điểm gặp nhau tại thời điểm $t = %s$ (giây)' % (t_meet + 1)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('Chất điểm A: $x_A(t) = \\int (%st - t^2)\\text{d}t = %st^2 - \\frac{t^3}{3} + C_2$ mà tại thời điểm $t = 0$ thì $x_A = 0 \\Rightarrow C_2 = 0$. \\\\\n'
                            'Khi đó $x_A(t) = %st^2 - \\frac{t^3}{3}$. \\\\\n'
                            'Chất điểm B: $x_B(t) = \\int %st \\text{d}t = %st^2 + C_3$ mà tại thời điểm $t = 0$ thì $x_B = 0 \\Rightarrow C_3 = 0$. \\\\\n'
                            'Khi đó $x_B(t) = %st^2$. \\\\\n'
                            'Hai chất điểm gặp nhau thì $x_A(t) = x_B(t) \\Leftrightarrow %st^2 - \\frac{t^3}{3} = %st^2 \\Leftrightarrow %st^2 - \\frac{t^3}{3} = 0 \\Leftrightarrow \\left[ \\begin{array}{l} t = 0 \\\\ t = %s \\end{array} \\right.$. \\\\\n'
                            'Vậy thời điểm hai chất điểm gặp nhau kể từ khi xuất phát là $t = %s$.' 
                            % (k, k_over_2_str, k_over_2_str, a, a_over_2_str, a_over_2_str, k_over_2_str, a_over_2_str, diff_coeff_str, t_meet, t_meet))

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
            vd_da_1_d = '\\True Khoảng cách lớn nhất giữa hai chất điểm trong quá trình chuyển động là $%s$ mét' % (d_max_tex)
            vd_da_1_s = 'Khoảng cách lớn nhất giữa hai chất điểm trong quá trình chuyển động là $%s$ mét' % (format_frac(d_max_val + Fraction(1, 3)))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('Khoảng cách giữa hai chất điểm trước khi gặp nhau là: $d(t) = |x_A(t) - x_B(t)| = \\left| %st^2 - \\frac{t^3}{3} \\right|$. \\\\\n'
                            'Xét hàm số $d(t) = %st^2 - \\frac{t^3}{3}$ trên đoạn $[0; %s]$ ta có $d\'(t) = %st - t^2 = 0 \\Leftrightarrow \\left[ \\begin{array}{l} t = 0 \\\\ t = %s \\end{array} \\right.$. \\\\\n'
                            'Thay các giá trị: $d(0) = 0; d(%s) = %s$ và $d(%s) = 0$ suy ra $d_{\\max} = %s$.'
                            % (diff_coeff_str, diff_coeff_str, t_meet, m, m, m, d_max_tex, t_meet, d_max_tex))

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
            vdc_da_1_d = '\\True Tại thời điểm hai chất điểm gặp nhau thì vận tốc của chất điểm thứ nhất %s vận tốc của chất điểm thứ hai' % (cmp_correct)
            vdc_da_1_s = 'Tại thời điểm hai chất điểm gặp nhau thì vận tốc của chất điểm thứ nhất %s vận tốc của chất điểm thứ hai' % (cmp_wrong)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('Tại thời điểm hai chất điểm gặp nhau là $t = %s$, thay vào phương trình vận tốc: \\\\\n'
                             '$v_A(%s) = %s \\cdot %s - %s^2 = %s$. \\\\\n'
                             '$v_B(%s) = %s \\cdot %s = %s$. \\\\\n'
                             'Ta thấy $v_A(%s) %s v_B(%s)$ nên vận tốc của chất điểm thứ nhất %s vận tốc của chất điểm thứ hai.'
                             % (t_meet, t_meet, k, t_meet, t_meet, vA_meet, t_meet, a, t_meet, vB_meet, t_meet, cmp_sign, t_meet, cmp_correct))

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
                       '\\end{ex}\n'
                       '\\end{minipage}\n\n')
            return content


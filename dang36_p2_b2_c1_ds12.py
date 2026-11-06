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


def bt_dang36_p2_b2_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Hàm format số để xử lý Rational và Float đẹp mắt
            def format_num(num):
                if isinstance(num, Rational):
                    if num.is_integer:
                        return str(int(num))
                    else:
                        return str(float(num)).replace('.', ',')
                elif isinstance(num, (int, float)):
                    if num == int(num):
                        return str(int(num))
                    else:
                        return str(num).replace('.', ',')
                return str(num).replace('.', ',')

            # Lặp để random dữ liệu bài toán sao cho kết quả ra số nguyên đẹp
            while True:
                S = random.choice([40, 50, 60, 80, 100])
                d0 = random.choice([15, 20, 25])
                N0 = S * d0

                # Dùng Rational để tránh sai số thập phân kéo dài
                W0_val = random.choice([Rational(12, 10), Rational(15, 10), Rational(18, 10), Rational(2, 1), Rational(25, 10)])
                W0 = float(W0_val)
                M_kg = int(N0 * W0)
                M_tan_val = Rational(M_kg, 1000)

                delta_W_val = random.choice([Rational(2, 10), Rational(4, 10), Rational(5, 10), Rational(8, 10)])
                delta_N = random.choice([4, 5, 8, 10])

                k_val = delta_W_val / delta_N

                b_val = W0_val + k_val * N0

                N_max = b_val / (2 * k_val)

                if N_max.is_integer and N_max > 0:
                    N_max = int(N_max)
                    F_max_val = (b_val**2) / (4 * k_val)
                    if F_max_val.is_integer or (F_max_val * 10).is_integer:
                        break

            # Chuyển đổi số liệu sang định dạng dấu phẩy tiếng Việt
            M_tan_str = format_num(M_tan_val)
            delta_W_str = format_num(delta_W_val)
            W0_str = format_num(W0_val)
            b_str = format_num(b_val)
            a_dec_pos_str = format_num(k_val)
            two_k_str = format_num(2 * k_val)
            F_max_str = format_num(F_max_val)

            # Random đáp án nhiễu (xử lý không bị âm và không bị sai số float)
            false_a = float(k_val) + random.uniform(0.01, 0.03)
            false_a_str = str(round(false_a, 4)).replace('.', ',')

            false_b = int(b_val / 2) if b_val > 10 else 16
            false_b_str = str(false_b)

            false_N_max = abs(N_max + random.choice([50, 128, -50, -128]))
            if false_N_max == 0:
                false_N_max = 128

            false_N0 = abs(N0 + random.choice([200, 500, -200, -500]))
            if false_N0 == 0:
                false_N0 = 500

            # Nội dung câu hỏi
            noidungcauhoi = ('''Bác Hồng nuôi cá tra ở một cái ao có diện tích là $%s m^2$. Vụ trước Bác Hồng nuôi với mật độ là $%s$ con/m$^2$ và thu được $%s$ tấn cá. Theo kinh nghiệm nuôi cá của mình thì cứ thả giảm đi $%s$ con thì mỗi con cá khi thu hoạch tăng lên $%s$ kg. Giả sử không có hao hụt khi nuôi.'''
                             % (S, d0, M_tan_str, delta_N, delta_W_str))

            ########################################################################
            # Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Số cá giống mà Bác Hồng đã thả trong vụ vừa qua là $%s$ con' % (N0)
            nb_da_1_s = 'Số cá giống mà Bác Hồng đã thả trong vụ vừa qua là $%s$ con' % (false_N0)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Số cá giống Bác Hồng đã thả trong vụ vừa qua là: $ %s \\times %s = %s $ (con).''' % (S, d0, N0))

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
            th_da_1_d = '\\True Khối lượng trung bình mỗi con cá thành phẩm trong vụ vừa qua là $%s$ (kg)' % W0_str
            th_da_1_s = 'Khối lượng trung bình mỗi con cá thành phẩm trong vụ vừa qua là $%s$ (kg)' % str(round(W0 + random.choice([0.5, 1.0]), 1)).replace('.', ',')
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Đổi $%s$ tấn = $%s$ kg. \\\\
            Khối lượng trung bình mỗi con cá thành phẩm trong vụ vừa qua là: $ \\frac{%s}{%s} = %s $ (kg).''' % (M_tan_str, M_kg, M_kg, N0, W0_str))

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
            vd_da_1_d = '\\True Gọi $x$ là số cá giống thả, tổng trọng lượng cá thu được là $F(x) = -%s x^2 + %s x$ (kg)' % (a_dec_pos_str, b_str)
            vd_da_1_s = 'Gọi $x$ là số cá giống thả, tổng trọng lượng cá thu được là $F(x) = -%s x^2 + %s x + %s$ (kg)' % (false_a_str, false_b_str, M_kg)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Gọi $x$ là số cá giống thả trong vụ tới ($x \\in \\mathbb{N}^*$). \\\\
            Sự chênh lệch số lượng cá giảm đi so với vụ trước là $ %s - x $. \\\\
            Khối lượng trung bình của một con cá khi đó là: $ %s + \\frac{%s}{%s} ( %s - x ) = %s - %s x $ (kg). \\\\
            Tổng trọng lượng cá thu được là: \\\\
            $F(x) = x \\cdot ( %s - %s x ) = - %s x^2 + %s x$ (kg).''' 
            % (N0, W0_str, delta_W_str, delta_N, N0, b_str, a_dec_pos_str, b_str, a_dec_pos_str, a_dec_pos_str, b_str))

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
            vdc_da_1_d = '\\True Vụ tới Bác Hồng phải thả $%s$ con cá giống để được tổng năng suất khi thu hoạch là cao nhất' % N_max
            vdc_da_1_s = 'Vụ tới Bác Hồng phải thả $%s$ con cá giống để được tổng năng suất khi thu hoạch là cao nhất' % false_N_max
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải (Đã sửa lỗi z thay vì 0 trong tkzTabLine)
            loigiai_vdc_1 = ('''Xét hàm số $F(x) = - %s x^2 + %s x$ với $x > 0$. \\\\
            Ta có $F'(x) = - %s x + %s$. \\\\
            $F'(x) = 0 \\Leftrightarrow - %s x + %s = 0 \\Leftrightarrow x = %s$. \\\\
            Bảng biến thiên:
            \\begin{center}
            \\begin{tikzpicture}[line width=1pt]
            \\tkzTabInit[lgt=1.5,espcl=3]{$x$/1,$F'(x)$/1,$F(x)$/2}{$0$,$%s$,$+\\infty$}
            \\tkzTabLine{,+,0,-,}
            \\tkzTabVar{-/ $0$ ,+/ {$%s$} ,-/ $-\\infty$}
            \\end{tikzpicture}
            \\end{center}
            Dựa vào bảng biến thiên, hàm số đạt giá trị lớn nhất tại $x = %s$. \\\\
            Vậy vụ tới Bác Hồng phải thả $%s$ con cá giống để đạt tổng năng suất cao nhất.''' 
            % (a_dec_pos_str, b_str, two_k_str, b_str, two_k_str, b_str, N_max, N_max, F_max_str, N_max, N_max))

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
                '\\end{ex}\n\\end{minipage}\n\n')
            return content


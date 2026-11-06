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


def bt_dang3_p2_b1_c2_ds12(self):
    # Hàm hỗ trợ định dạng số: đổi dấu chấm thành dấu phẩy và bỏ đuôi .0 nếu là số nguyên
    def fmt(val):
        if round(val, 5) == int(val):
            return str(int(val))
        return str(round(val, 4)).replace('.', ',')

    # Khai báo biến
    # Khởi tạo một số bộ tần số cố định để đảm bảo kết quả tính phân vị luôn là số hữu tỉ/thập phân đẹp
    datasets = [
        (3, 5, 7, 4, 1),
        (5, 10, 15, 8, 2),
        (4, 6, 10, 3, 2)
    ]
    f1, f2, f3, f4, f5 = random.choice(datasets)
    n = f1 + f2 + f3 + f4 + f5
    cf = [f1, f1+f2, f1+f2+f3, f1+f2+f3+f4, n]

    idx1 = f1 # Chắc chắn thuộc nhóm 1
    idx2 = cf[1] + 1 # Chắc chắn thuộc nhóm 3

    q3_pos = 3 * n / 4
    q3_val = 170 + (q3_pos - cf[1]) / f3 * 5

    q1_pos = n / 4
    q1_val = 165 + (q1_pos - cf[0]) / f2 * 5

    delta_q = q3_val - q1_val

    prob = (f4 + f5) / n

    # Định dạng toàn bộ biến thành chuỗi theo chuẩn dấu phẩy
    s_n = fmt(n)
    s_f1 = fmt(f1)
    s_f2 = fmt(f2)
    s_f3 = fmt(f3)
    s_f4 = fmt(f4)
    s_f5 = fmt(f5)
    s_idx1 = fmt(idx1)
    s_idx2 = fmt(idx2)

    s_q3_pos = fmt(q3_pos)
    s_q3_val = fmt(q3_val)
    s_q3_wrong = fmt(q3_val + 0.5)

    s_q1_pos = fmt(q1_pos)
    s_q1_val = fmt(q1_val)

    s_dq = fmt(delta_q)
    s_dq_wrong = fmt(delta_q + 0.5)

    s_sum_f4_f5 = fmt(f4 + f5)
    s_prob = fmt(prob)
    s_prob_wrong = fmt(prob + 0.05)
    s_cf0 = fmt(cf[0])
    s_cf1 = fmt(cf[1])
    s_cf2 = fmt(cf[2])
    s_cf3 = fmt(cf[3])
    s_cf4 = fmt(cf[4])
    s_f1_plus_1 = fmt(f1 + 1)
    s_cf1_plus_1 = fmt(cf[1] + 1)

    # Nội dung câu hỏi
    noidungcauhoi = ('''Khảo sát chiều cao của %s học sinh nam lớp 12A của một trường THPT X, người ta được kết quả thống kê trong bảng sau:
    \\begin{center}
    \\begin{tabular}{|c|c|c|c|c|c|}
    \\hline
    \\textbf{Chiều cao (cm)} & $[160;165)$ & $[165;170)$ & $[170;175)$ & $[175;180)$ & $[180;185)$ \\\\
    \\hline
    \\textbf{Số học sinh} & %s & %s & %s & %s & %s \\\\
    \\hline
    \\end{tabular}
    \\end{center}''' % (s_n, s_f1, s_f2, s_f3, s_f4, s_f5))

    ########################################################################
    # Nhận biết ############################################
    # Các đáp án
    nb_da_1_d = '\\True Gọi $x_1;x_2;\\dots;x_{%s}$ là mẫu số liệu gốc gồm chiều cao của %s học sinh trên được xếp theo thứ tự không giảm. Khi đó, $x_{%s} \\in [160;165)$ và $x_{%s} \\in [170;175)$' % (s_n, s_n, s_idx1, s_idx2)
    nb_da_1_s = 'Gọi $x_1;x_2;\\dots;x_{%s}$ là mẫu số liệu gốc gồm chiều cao của %s học sinh trên được xếp theo thứ tự không giảm. Khi đó, $x_{%s} \\in [165;170)$ và $x_{%s} \\in [170;175)$' % (s_n, s_n, s_idx1, s_idx2)
    list_nb_da_1=[nb_da_1_d,nb_da_1_s]
    nb_da_1=random.choice(list_nb_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]

    # Nội dung lời giải
    loigiai_nb_1 = ('''Từ bảng số liệu ta thấy có %s học sinh có chiều cao thuộc $[160;165)$ nên $x_1, \\dots, x_{%s} \\in [160;165)$, suy ra $x_{%s} \\in [160;165)$. \\\\
    Tương tự, có %s học sinh có chiều cao thuộc $[165;170)$ nên $x_{%s}, \\dots, x_{%s} \\in [165;170)$; có %s học sinh có chiều cao thuộc $[170;175)$ nên $x_{%s}, \\dots, x_{%s} \\in [170;175)$, suy ra $x_{%s} \\in [170;175)$.''' % (s_f1, s_f1, s_idx1, s_f2, s_f1_plus_1, s_cf1, s_f3, s_cf1_plus_1, s_cf2, s_idx2))

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
    th_da_1_d = '\\True Tứ phân vị thứ ba của mẫu số liệu ghép nhóm đã cho bằng $%s$' % (s_q3_val)
    th_da_1_s = 'Tứ phân vị thứ ba của mẫu số liệu ghép nhóm đã cho bằng $%s$' % (s_q3_wrong)
    list_th_da_1=[th_da_1_d,th_da_1_s]
    th_da_1=random.choice(list_th_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]

    # Nội dung lời giải
    loigiai_th_1 = ('''Cỡ mẫu $n = %s$. Ta có $\\frac{3n}{4} = \\frac{3 \\cdot %s}{4} = %s$. \\\\
    Tần số tích lũy của các nhóm lần lượt là $cf_1=%s$, $cf_2=%s$, $cf_3=%s$, $cf_4=%s$, $cf_5=%s$. \\\\
    Do đó nhóm chứa tứ phân vị thứ ba là $[170;175)$. \\\\
    Ta có $Q_3 = 170 + \\frac{%s - %s}{%s} \\cdot 5 = %s$.''' % (s_n, s_n, s_q3_pos, s_cf0, s_cf1, s_cf2, s_cf3, s_cf4, s_q3_pos, s_cf1, s_f3, s_q3_val))

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
    vd_da_1_d = '\\True Khoảng tứ phân vị của mẫu số liệu ghép nhóm đã cho là $\\Delta _Q = Q_3 - Q_1 = %s$' % (s_dq) 
    vd_da_1_s = 'Khoảng tứ phân vị của mẫu số liệu ghép nhóm đã cho là $\\Delta _Q = Q_3 - Q_1 = %s$' % (s_dq_wrong) 
    list_vd_da_1=[vd_da_1_d,vd_da_1_s]
    vd_da_1=random.choice(list_vd_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]

    # Nội dung lời giải
    loigiai_vd_1 = ('''Ta có $\\frac{n}{4} = \\frac{%s}{4} = %s$. Nhóm chứa tứ phân vị thứ nhất là $[165;170)$. \\\\
    Tứ phân vị thứ nhất là $Q_1 = 165 + \\frac{%s - %s}{%s} \\cdot 5 = %s$. \\\\
    Khoảng tứ phân vị của mẫu số liệu ghép nhóm là $\\Delta _Q = Q_3 - Q_1 = %s - %s = %s$.''' % (s_n, s_q1_pos, s_q1_pos, s_cf0, s_f2, s_q1_val, s_q3_val, s_q1_val, s_dq))

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
    vdc_da_1_d = '\\True Chọn ngẫu nhiên một học sinh trong nhóm khảo sát nói trên, xác suất chọn được học sinh có chiều cao từ $175$ cm trở lên bằng $%s$' % (s_prob) 
    vdc_da_1_s = 'Chọn ngẫu nhiên một học sinh trong nhóm khảo sát nói trên, xác suất chọn được học sinh có chiều cao từ $175$ cm trở lên bằng $%s$' % (s_prob_wrong) 
    list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
    vdc_da_1=random.choice(list_vdc_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]

    # Nội dung lời giải
    loigiai_vdc_1 = ('''Số học sinh có chiều cao từ $175$ cm trở lên (thuộc các nhóm $[175;180)$ và $[180;185)$) là $f_4 + f_5 = %s + %s = %s$. \\\\
    Xác suất chọn được học sinh có chiều cao từ $175$ cm trở lên là $P = \\frac{%s}{%s} = %s$.''' % (s_f4, s_f5, s_sum_f4_f5, s_sum_f4_f5, s_n, s_prob))

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
        '\\begin{ex}\n'+
        str(noidungcauhoi)+ 
        '\n\\choiceTFn \n'
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
        '\\end{ex}\n\\end{minipage}\n\n')
    return content


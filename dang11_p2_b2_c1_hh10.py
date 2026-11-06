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


def bt_dang11_p2_b2_c1_hh10(self):
    # Hàm bổ trợ định dạng số thập phân dùng dấu phẩy
    def fmt(val, dec=2):
        res = f"{float(val):.{dec}f}"
        return res.replace('.', ',')

    # Chọn các cạnh a, b, c thỏa mãn bất đẳng thức tam giác và tổng a+b+c là số chẵn (để p nguyên hoặc bán nguyên đẹp)
    while True:
        a = random.randint(5, 10)
        b = random.randint(7, 12)
        c = random.randint(10, 15)

        # Đảm bảo điều kiện tạo thành tam giác và các cạnh khác nhau cho đa dạng
        if a + b > c and a + c > b and b + c > a and a != b and b != c and a != c:
            break

    # Tính nửa chu vi p
    p = sp.Rational(a + b + c, 2)

    # Tính diện tích bình phương S^2 = p(p-a)(p-b)(p-c)
    S2 = p * (p - a) * (p - b) * (p - c)
    S = sp.sqrt(S2)

    # Xét tính chất tam giác nhọn/tù
    # Tìm cạnh lớn nhất
    max_edge = max(a, b, c)
    if max_edge == c:
        cos_val_num = a**2 + b**2 - c**2
        cos_val_den = 2 * a * b
        angle_name = 'C'
    elif max_edge == b:
        cos_val_num = a**2 + c**2 - b**2
        cos_val_den = 2 * a * c
        angle_name = 'B'
    else:
        cos_val_num = b**2 + c**2 - a**2
        cos_val_den = 2 * b * c
        angle_name = 'A'

    cos_val_frac = sp.Rational(cos_val_num, cos_val_den)
    is_obtuse = cos_val_num < 0
    triangle_type = "tù" if is_obtuse else "nhọn"
    wrong_triangle_type = "nhọn" if is_obtuse else "tù"

    # Xét mệnh đề d
    is_d_true = (b + c == 2 * a)

    # Nội dung câu hỏi
    noidungcauhoi = ('''Cho tam giác $ABC$ có $a = %s, b = %s, c = %s$.'''
                     %(latex(a), latex(b), latex(c)
                         ))

    ######################################################################## Nhận biết ############################################
    # Các đáp án
    nb_da_1_d = '\\True $p = %s$' %(latex(p))
    nb_da_1_s = '$p = %s$' %(latex(p + 1))
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]

    # Nội dung lời giải
    loigiai_nb_1 = ('''Nửa chu vi của tam giác $ABC$ là $p = \\frac{a + b + c}{2} = \\frac{%s + %s + %s}{2} = %s$.'''
                %(latex(a), latex(b), latex(c), latex(p)
                    ))

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
    th_da_1_d = '\\True $S = %s$' %(latex(S))
    th_da_1_s = '$S = %s$' %(latex(sp.sqrt(S2 + 5)))
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]

    # Nội dung lời giải
    loigiai_th_1 = ('''Áp dụng công thức Heron để tính diện tích tam giác $ABC$: \\\\
    $S = \\sqrt{p(p-a)(p-b)(p-c)} = \\sqrt{%s(%s-%s)(%s-%s)(%s-%s)} = %s$.'''
                %(latex(p), latex(p), latex(a), latex(p), latex(b), latex(p), latex(c), latex(S)
                    ))

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
    vd_da_1_d = '\\True Tam giác $ABC$ là tam giác %s' %(triangle_type)
    vd_da_1_s = 'Tam giác $ABC$ là tam giác %s' %(wrong_triangle_type)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]

    # Nội dung lời giải
    if is_obtuse:
        loigiai_vd_1 = ('''Xét góc lớn nhất trong tam giác là góc đối diện với cạnh lớn nhất (cạnh $%s$). \\\\
    Theo hệ quả định lý côsin, ta có: $\\cos %s = \\frac{%s}{%s} = %s < 0$. \\\\
    Vì $\\cos %s < 0$ nên góc $%s$ là góc tù. Do đó tam giác $ABC$ là tam giác tù.'''
                    %(max_edge, angle_name, latex(cos_val_num), latex(cos_val_den), latex(cos_val_frac), angle_name, angle_name
                        ))
    else:
        loigiai_vd_1 = ('''Xét góc lớn nhất trong tam giác là góc đối diện với cạnh lớn nhất (cạnh $%s$). \\\\
    Theo hệ quả định lý côsin, ta có: $\\cos %s = \\frac{%s}{%s} = %s > 0$. \\\\
    Vì $\\cos %s > 0$ nên góc $%s$ là góc nhọn. Do đó tam giác $ABC$ là tam giác nhọn.'''
                    %(max_edge, angle_name, latex(cos_val_num), latex(cos_val_den), latex(cos_val_frac), angle_name, angle_name
                        ))

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
    if is_d_true:
        vdc_da_1_d = '\\True $\\frac{1}{h_b} + \\frac{1}{h_c} = \\frac{2}{h_a}$'
        vdc_da_1_s = '$\\frac{1}{h_b} + \\frac{1}{h_c} \\neq \\frac{2}{h_a}$'
    else:
        vdc_da_1_d = '\\True $\\frac{1}{h_b} + \\frac{1}{h_c} \\neq \\frac{2}{h_a}$'
        vdc_da_1_s = '$\\frac{1}{h_b} + \\frac{1}{h_c} = \\frac{2}{h_a}$'

    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]

    b_plus_c = b + c
    two_a = 2 * a
    eq_sign = "=" if is_d_true else "\\neq"

    # Nội dung lời giải
    loigiai_vdc_1 = ('''Diện tích tam giác được tính bằng công thức: $S = \\frac{1}{2}ah_a = \\frac{1}{2}bh_b = \\frac{1}{2}ch_c$. \\\\
    Suy ra: $h_a = \\frac{2S}{a}$, $h_b = \\frac{2S}{b}$, $h_c = \\frac{2S}{c}$. \\\\
    Ta có: $\\frac{1}{h_b} + \\frac{1}{h_c} = \\frac{b}{2S} + \\frac{c}{2S} = \\frac{b+c}{2S}$. \\\\
    Mặt khác: $\\frac{2}{h_a} = \\frac{2}{\\frac{2S}{a}} = \\frac{2a}{2S}$. \\\\
    Theo giả thiết đề bài, $b+c = %s + %s = %s$ và $2a = 2 \\cdot %s = %s$. \\\\
    Vì $b+c %s 2a$ ($%s %s %s$) nên $\\frac{1}{h_b} + \\frac{1}{h_c} %s \\frac{2}{h_a}$.'''
                %(latex(b), latex(c), latex(b_plus_c), latex(a), latex(two_a), eq_sign, latex(b_plus_c), eq_sign, latex(two_a), eq_sign
                    ))

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
        '\\end{ex}\n \\end{minipage} \n\n')
    return content


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


def bt_dang34_p2_b2_c2_ds10(self):
    # Khai báo biến
    x, y = symbols('x y')

    # Sinh các tham số ngẫu nhiên cho bài toán quy hoạch tuyến tính
    danh_sach_bo_so = [
        (80, 60, 120),  # x_max, y_max, W -> x_c = 50, y_b = 24
        (70, 50, 110),  # x_c = 50, y_b = 26
        (90, 70, 130),  # x_c = 50, y_b = 22
        (75, 60, 114),  # x_c = 45, y_b = 24
        (85, 65, 125)   # x_c = 50, y_b = 23
    ]

    x_max, y_max, W_val = random.choice(danh_sach_bo_so)
    c_x_str = '1,2'
    W_mult_5 = 5 * W_val

    # Tọa độ các đỉnh của đa giác miền nghiệm OABCD
    x_c = int((W_val - y_max) * 5 / 6)
    y_b = int(W_val - 1.2 * x_max)

    # Hệ số hàm mục tiêu lợi nhuận L(x, y) = p_x * x + p_y * y (triệu đồng)
    p_x = random.choice([35, 40, 45, 50])
    p_y = random.choice([25, 30, 35])

    # Tính giá trị lợi nhuận tại các đỉnh
    L_O = 0
    L_A = p_x * x_max
    L_B = p_x * x_max + p_y * y_b
    L_C = p_x * x_c + p_y * y_max
    L_D = p_y * y_max

    max_L = max(L_O, L_A, L_B, L_C, L_D)
    if max_L == L_B:
        ket_luan_dieu_kien = 'nhà máy vận hành tối đa công suất sợi X'
    else:
        ket_luan_dieu_kien = 'nhà máy vận hành tối đa công suất sợi Y'

    # Phương án sai
    x_c_wrong = x_c + random.choice([-10, 10, 15])
    max_L_wrong = max_L + random.choice([200, 280, 300, 350])

    # Tính toán các tọa độ tỉ lệ để vẽ TikZ (chuẩn hóa về khoảng [0, 6] cm)
    x_max_tikz = round(x_max / 20.0, 2)
    y_max_tikz = round(y_max / 20.0, 2)
    x_c_tikz = round(x_c / 20.0, 2)
    y_b_tikz = round(y_b / 20.0, 2)
    x_axis_lim = round((x_max + 25) / 20.0, 2)
    y_axis_lim = round((y_max + 25) / 20.0, 2)

    # Chuỗi TikZ vẽ miền nghiệm ngũ giác khép kín OABCD gạch sọc theo mẫu
    tikz_mien_nghiem = ('''\\begin{center}
    \\begin{tikzpicture}[>=stealth, scale=1, line width=1pt]
    \\draw[->] (-0.5, 0) -- (%s, 0) node[below] {$x$};
    \\draw[->] (0, -0.5) -- (0, %s) node[left] {$y$};
    \\node at (0,0) [below left] {$O$};
    \\fill[pattern=north east lines, pattern color=black] (-0.5,-0.5) rectangle (%s,%s);
    \\fill[white] (0,0) -- (%s,0) -- (%s,%s) -- (%s,%s) -- (0,%s) -- cycle;
    \\draw[black] (0,0) -- (%s,0) -- (%s,%s) -- (%s,%s) -- (0,%s) -- cycle;
    \\draw[dashed] (%s,0) -- (%s,%s) (0,%s) -- (%s,%s);
    \\coordinate (A) at (%s,0);
    \\coordinate (B) at (%s,%s);
    \\coordinate (C) at (%s,%s);
    \\coordinate (D) at (0,%s);
    \\fill (A) circle (1.5pt) node[below] {$A(%s;0)$};
    \\fill (B) circle (1.5pt) node[above right] {$B(%s;%s)$};
    \\fill (C) circle (1.5pt) node[above right] {$C(%s;%s)$};
    \\fill (D) circle (1.5pt) node[left] {$D(0;%s)$};
    \\end{tikzpicture}
    \\end{center}''' % (
        x_axis_lim, y_axis_lim,
        x_axis_lim, y_axis_lim,
        x_max_tikz, x_max_tikz, y_b_tikz, x_c_tikz, y_max_tikz, y_max_tikz,
        x_max_tikz, x_max_tikz, y_b_tikz, x_c_tikz, y_max_tikz, y_max_tikz,
        x_c_tikz, x_c_tikz, y_max_tikz, y_b_tikz, x_max_tikz, y_b_tikz,
        x_max_tikz,
        x_max_tikz, y_b_tikz,
        x_c_tikz, y_max_tikz,
        y_max_tikz,
        x_max,
        x_max, y_b,
        x_c, y_max,
        y_max
    ))

    # Nội dung câu hỏi
    noidungcauhoi = ('''Một nhà máy dệt sản xuất hai loại sợi gai cao cấp X và Y. Năng lực máy móc tối đa cho phép sản xuất không quá $%s$ tấn sợi X và không quá $%s$ tấn sợi Y mỗi tuần. Nguồn cung nguyên liệu sợi thô tổng hợp mỗi tuần tối đa là $%s$ tấn; trong đó để tạo ra $1$ tấn sợi X cần $%s$ tấn sợi thô; còn $1$ tấn sợi Y cần $1$ tấn sợi thô. Gọi $x, y$ (đơn vị: tấn) lần lượt là sản lượng sợi X và sợi Y sản xuất trong tuần. Lợi nhuận tổng thu được là $L(x;y) = %sx + %sy$ (triệu đồng).''' % (x_max, y_max, W_val, c_x_str, p_x, p_y))

    #############################################################################
    # Nhận biết
    nb_da_1_d = '\\True Nếu nhà máy quyết định sản xuất hết công suất tối đa loại sợi Y ($y = %s$ tấn) thì sản lượng sợi X tối đa có thể đạt được là $%s$ tấn' % (y_max, x_c)
    nb_da_1_s = 'Nếu nhà máy quyết định sản xuất hết công suất tối đa loại sợi Y ($y = %s$ tấn) thì sản lượng sợi X tối đa có thể đạt được là $%s$ tấn' % (y_max, x_c_wrong)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    list_nb_1 = [nb_da_1]

    loigiai_nb_1 = ('''Khi nhà máy sản xuất hết công suất sợi Y với $y = %s$ tấn, lượng nguyên liệu thô cần dùng là $1 \\cdot %s = %s$ tấn. \\\\ Lượng nguyên liệu thô còn lại dành cho sợi X tối đa là: $%s - %s = %s$ (tấn). \\\\ Khi đó sản lượng sợi X tối đa có thể sản xuất là: $\\frac{%s}{%s} = %s$ (tấn) (thỏa mãn không quá năng lực máy móc là $%s$ tấn).''' % (y_max, y_max, y_max, W_val, y_max, W_val - y_max, W_val - y_max, c_x_str, x_c, x_max))
    list_nb_2 = [loigiai_nb_1]

    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

    #############################################################################
    # Thông hiểu (Có hình vẽ TikZ minh họa miền nghiệm)
    th_da_1_d = '\\True Tập hợp các phương án sản xuất trên mặt phẳng $Oxy$ là một ngũ giác khép kín'
    th_da_1_s = 'Tập hợp các phương án sản xuất trên mặt phẳng $Oxy$ là một tứ giác khép kín'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    list_th_1 = [th_da_1]

    loigiai_th_1 = ('''Miền nghiệm của hệ bất phương trình ràng buộc là miền đa giác (không bị gạch sọc) giới hạn bởi các đường thẳng $x = 0$, $y = 0$, $x = %s$, $y = %s$ và $6x + 5y = %s$. \\\\ Các đỉnh của miền nghiệm gồm có: $O(0;0)$, $A(%s;0)$, $B(%s;%s)$, $C(%s;%s)$, $D(0;%s)$. \\\\ Do đó, tập hợp các phương án sản xuất trên mặt phẳng $Oxy$ là một ngũ giác khép kín $OABCD$. \\\\ %s''' % (x_max, y_max, W_mult_5, x_max, x_max, y_b, x_c, y_max, y_max, tikz_mien_nghiem))
    list_th_2 = [loigiai_th_1]

    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

    #############################################################################
    # Vận dụng
    vd_da_1_d = '\\True Hệ bất phương trình mô tả các ràng buộc kỹ thuật và nguyên liệu là: $\\begin{cases} 0 \\le x \\le %s \\\\ 0 \\le y \\le %s \\\\ 6x + 5y \\le %s \\end{cases}$' % (x_max, y_max, W_mult_5)
    vd_da_1_s = 'Hệ bất phương trình mô tả các ràng buộc kỹ thuật và nguyên liệu là: $\\begin{cases} 0 \\le x \\le %s \\\\ 0 \\le y \\le %s \\\\ 5x + 6y \\le %s \\end{cases}$' % (x_max, y_max, W_mult_5)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    list_vd_1 = [vd_da_1]

    loigiai_vd_1 = ('''Do sản lượng không âm và không vượt quá năng lực máy móc nên: $0 \\le x \\le %s$ và $0 \\le y \\le %s$. \\\\ Tổng số nguyên liệu thô cần dùng mỗi tuần là: $%sx + y$ (tấn). \\\\ Do nguồn cung nguyên liệu không quá $%s$ tấn/tuần nên: $%sx + y \\le %s \\Leftrightarrow \\frac{6}{5}x + y \\le %s \\Leftrightarrow 6x + 5y \\le %s$. \\\\ Vậy hệ bất phương trình mô tả các ràng buộc là: $\\begin{cases} 0 \\le x \\le %s \\\\ 0 \\le y \\le %s \\\\ 6x + 5y \\le %s \\end{cases}$''' % (x_max, y_max, c_x_str, W_val, c_x_str, W_val, W_val, W_mult_5, x_max, y_max, W_mult_5))
    list_vd_2 = [loigiai_vd_1]

    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

    #############################################################################
    # Vận dụng cao
    vdc_da_1_d = '\\True Lợi nhuận cực đại của nhà máy đạt được là $%s$ triệu đồng khi %s' % (max_L, ket_luan_dieu_kien)
    vdc_da_1_s = 'Lợi nhuận cực đại của nhà máy đạt được là $%s$ triệu đồng khi %s' % (max_L_wrong, ket_luan_dieu_kien)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    list_vdc_1 = [vdc_da_1]

    loigiai_vdc_1 = ('''Lợi nhuận thu được là $L(x;y) = %sx + %sy$ (triệu đồng). \\\\ Giá trị của $L(x;y)$ đạt cực đại tại một trong các đỉnh của ngũ giác miền nghiệm: \\\\ - Tại $O(0;0)$: $L(0;0) = 0$. \\\\ - Tại $A(%s;0)$: $L(%s;0) = %s \\cdot %s = %s$ (triệu đồng). \\\\ - Tại $B(%s;%s)$: $L(%s;%s) = %s \\cdot %s + %s \\cdot %s = %s$ (triệu đồng). \\\\ - Tại $C(%s;%s)$: $L(%s;%s) = %s \\cdot %s + %s \\cdot %s = %s$ (triệu đồng). \\\\ - Tại $D(0;%s)$: $L(0;%s) = %s \\cdot %s = %s$ (triệu đồng). \\\\ So sánh các giá trị trên, ta thấy $L(x;y)$ đạt cực đại bằng $%s$ triệu đồng khi %s.''' % (
        p_x, p_y,
        x_max, x_max, p_x, x_max, L_A,
        x_max, y_b, x_max, y_b, p_x, x_max, p_y, y_b, L_B,
        x_c, y_max, x_c, y_max, p_x, x_c, p_y, y_max, L_C,
        y_max, y_max, p_y, y_max, L_D,
        max_L, ket_luan_dieu_kien
    ))
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
    content = (
        '\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
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


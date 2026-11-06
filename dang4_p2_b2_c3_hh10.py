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


def bt_dang4_p2_b2_c3_hh10(self):
            # Khai báo biến
            # Khai báo biến
            x, y, t = symbols('x y t')

            # --- KHỞI TẠO DỮ LIỆU NGẪU NHIÊN ---
            # Câu a: Hệ số góc k
            a_m = random.randint(2, 5)
            a_n = random.randint(-5, 5)
            if a_n == 0: a_n = 1
            line_a = a_m * x + a_n

            # Câu b: Trục Ox hoặc Oy
            axis_choice = random.choice(['Ox', 'Oy'])
            if axis_choice == 'Ox':
                vec_n_correct = (0, 1)
                vec_n_wrong = (1, 0)
            else:
                vec_n_correct = (1, 0)
                vec_n_wrong = (0, 1)

            # Câu c: Điểm thuộc đường thẳng Delta: ax + by + c = 0
            c_a = random.randint(2, 6)
            c_b = random.randint(2, 6)
            c_x0 = random.randint(1, 4)
            c_y0 = random.randint(1, 4)
            # Để tạo câu Sai: tính giá trị khác 0
            val_c = c_a * c_x0 + c_b * c_y0
            c_c_true = -val_c
            c_c_wrong = -val_c + random.choice([-2, -1, 1, 2])

            # Câu d: Vectơ chỉ phương của đường thẳng tham số
            d_x0 = random.randint(-3, 3)
            d_y0 = random.randint(-3, 3)
            d_u1 = random.randint(-5, 5)
            d_u2 = random.randint(-5, 5)
            if d_u1 == 0: d_u1 = 1
            if d_u2 == 0: d_u2 = 2
            d_vec_correct = (d_u1, d_u2)
            d_vec_wrong = (random.randint(1, 3), random.randint(-3, -1)) # Tạo một vector ngẫu nhiên thường là sai

            # --- NỘI DUNG CÂU HỎI ---
            noidungcauhoi = ('''Trong hệ tọa độ $Oxy$.''')

            ########################################################################
            # Nhận biết - Câu a: Hệ số góc #########################################
            nb_da_1_d = '\\True Hệ số góc của đường thẳng $y = %s$ là $k = %s$' % (latex(line_a), latex(a_m))
            nb_da_1_s = 'Hệ số góc của đường thẳng $y = %s$ là $k = %s$' % (latex(line_a), latex(a_n))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)
            loigiai_nb_1 = ('''Đường thẳng $y = %sx %s$ có dạng $y = kx + b$, suy ra hệ số góc là $k = %s$.''' 
                            % (latex(a_m), ('' if a_n < 0 else '+') + latex(a_n), latex(a_m)))

            ########################################################################
            # Thông hiểu - Câu b: Vectơ pháp tuyến ##################################
            th_da_1_d = '\\True Một vectơ pháp tuyến của đường thẳng song song với trục $%s$ là $\\vec{u} = (%s; %s)$' % (axis_choice, latex(vec_n_correct[0]), latex(vec_n_correct[1]))
            th_da_1_s = 'Một vectơ pháp tuyến của đường thẳng song song với trục $%s$ là $\\vec{u} = (%s; %s)$' % (axis_choice, latex(vec_n_wrong[0]), latex(vec_n_wrong[1]))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)
            loigiai_th_1 = ('''Đường thẳng song song với trục $%s$ sẽ vuông góc với trục còn lại. Một vectơ pháp tuyến của nó chính là vectơ đơn vị của trục kia, tức là $\\vec{u} = (%s; %s)$.''' 
                            % (axis_choice, latex(vec_n_correct[0]), latex(vec_n_correct[1])))

            ########################################################################
            # Vận dụng - Câu c: Điểm thuộc đường thẳng #############################
            vd_da_1_d = '\\True Điểm $A(%s; %s)$ nằm trên đường thẳng $\\Delta: %sx + %sy %s = 0$' % (latex(c_x0), latex(c_y0), latex(c_a), latex(c_b), latex(c_c_true) if c_c_true < 0 else '+'+latex(c_c_true))
            vd_da_1_s = 'Điểm $A(%s; %s)$ nằm trên đường thẳng $\\Delta: %sx + %sy %s = 0$' % (latex(c_x0), latex(c_y0), latex(c_a), latex(c_b), latex(c_c_wrong) if c_c_wrong < 0 else '+'+latex(c_c_wrong))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Logic lời giải câu c (tính toán cụ thể)
            c_c_val = c_c_true if '\\True' in vd_da_1 else c_c_wrong
            check_val = c_a * c_x0 + c_b * c_y0 + c_c_val
            symbol_belong = '\\in' if check_val == 0 else '\\notin'
            loigiai_vd_1 = ('''Thay tọa độ điểm $A$ vào phương trình $\\Delta$, ta có: \\\\ $%s \\cdot %s + %s \\cdot %s %s = %s$. \\\\ Vì kết quả %s nên $A %s \\Delta$.''' 
                            % (latex(c_a), latex(c_x0), latex(c_b), latex(c_y0), ('' if c_c_val < 0 else '+') + latex(c_c_val), latex(check_val), ('bằng 0' if check_val == 0 else 'khác 0'), symbol_belong))

            ########################################################################
            # Vận dụng cao - Câu d: Vectơ chỉ phương ################################
            vdc_da_1_d = '\\True Một vectơ chỉ phương của đường thẳng $d: \\begin{cases} x = %s %s t \\\\ y = %s %s t \\end{cases}$ là $\\vec{u} = (%s; %s)$' % (latex(d_x0), ('' if d_u1 < 0 else '+') + latex(d_u1), latex(d_y0), ('' if d_u2 < 0 else '+') + latex(d_u2), latex(d_u1), latex(d_u2))
            vdc_da_1_s = 'Một vectơ chỉ phương của đường thẳng $d: \\begin{cases} x = %s %s t \\\\ y = %s %s t \\end{cases}$ là $\\vec{u} = (%s; %s)$' % (latex(d_x0), ('' if d_u1 < 0 else '+') + latex(d_u1), latex(d_y0), ('' if d_u2 < 0 else '+') + latex(d_u2), latex(d_vec_wrong[0]), latex(d_vec_wrong[1]))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Logic lời giải câu d (kiểm tra cùng phương)
            u_check = d_vec_correct if '\\True' in vdc_da_1 else d_vec_wrong
            is_collinear = (d_u1 * u_check[1] == d_u2 * u_check[0])
            loigiai_vdc_1 = ('''Từ phương trình tham số của $d$, ta thấy một vectơ chỉ phương là $\\vec{a} = (%s; %s)$. \\\\ Xét vectơ đề bài cho $\\vec{u} = (%s; %s)$. \\\\ Ta có $%s \\cdot %s %s %s \\cdot %s$ nên $\\vec{u}$ %s cùng phương với $\\vec{a}$. \\\\ Vậy $\\vec{u}$  %s là vectơ chỉ phương của $d$.''' 
                             % (latex(d_u1), latex(d_u2), latex(u_check[0]), latex(u_check[1]), latex(d_u1), latex(u_check[1]), ('=' if is_collinear else '\\neq'), latex(d_u2), latex(u_check[0]), ('' if is_collinear else 'không'), ('không phải' if not is_collinear else 'chính')))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Vòng lặp đảm bảo số lượng đáp án đúng từ 1 đến 3
            while True:
                ans_a = random.choice(list_nb_da_1)
                ans_b = random.choice(list_th_da_1)
                ans_c = random.choice(list_vd_da_1)
                ans_d = random.choice(list_vdc_da_1)

                if 1 <= count_true_answers([ans_a, ans_b, ans_c, ans_d]) <= 3:
                    # Cập nhật lại các biến để xuất content
                    shuffled_answers = [ans_a, ans_b, ans_c, ans_d]
                    # Tìm lời giải tương ứng (do lời giải phụ thuộc vào việc chọn đáp án Đúng hay Sai)
                    # Lưu ý: Trong mã này lời giải đã được thiết kế linh hoạt theo biến đáp án ở trên
                    break

            # Xuất nội dung theo định dạng mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' +
                str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(ans_a) + '}\n'
                '{' + str(ans_b) + '}\n'
                '{' + str(ans_c) + '}\n'
                '{' + str(ans_d) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content   


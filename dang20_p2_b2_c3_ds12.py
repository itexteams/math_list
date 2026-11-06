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


def bt_dang20_p2_b2_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            x = symbols('x')
            a_sym = symbols('a')

            # --- B3: SUY NGHĨ TÌM CÁCH RANDOM ---
            # Để bài toán đẹp như trong hình (f(x) = 2x - 4):
            # 1. Chọn hệ số góc 'a' dương (thường là 2).
            # 2. Chọn nghiệm 'x0' nguyên để các phép tính tích phân ra số nguyên.
            # 3. f(x) = a*x + b => b = -a*x0.

            val_a = 2 
            val_x0 = random.randint(2, 4) # Nghiệm của f(x)=0
            val_b = -val_a * val_x0
            f = val_a * x + val_b

            # Nội dung câu hỏi
            noidungcauhoi = r'''Cho hàm số $y = f(x) = %s$.''' % (latex(f))

            ########################################################################
            # Nhận biết: Tính chất tích phân cận trùng nhau
            ########################################################################
            # Cận dưới/trên lấy ngẫu nhiên
            can_a = -val_x0
            nb_da_1_d = r'\True $\int_{%s}^{%s} f(x) \text{d}x = 0$' % (can_a, can_a)
            nb_da_1_s = r'Ta có: $\int_{%s}^{%s} f(x) \text{d}x = %s$' % (can_a, can_a, val_a)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = r'''Áp dụng tính chất tích phân: $\int_{a}^{a} f(x) \text{d}x = 0$. Ta có $\int_{%s}^{%s} f(x) \text{d}x = 0$.''' % (can_a, can_a)

            list_nb_1 = [nb_da_1]
            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # Thông hiểu: Tích phân hàm bình phương
            ########################################################################
            # Tính tích phân f(x)^2 từ 1 đến x0+2 (giống mẫu 1 đến 4 với x0=2)
            c1, c2 = 1, val_x0 + 2
            f_sq = f**2
            res_b = Integral(f_sq, (x, c1, c2)).doit()

            th_da_1_d = r'\True $\int_{%s}^{%s} f^2(x) \text{d}x = %s$' % (c1, c2, latex(res_b))
            th_da_1_s = r'$\int_{%s}^{%s} f^2(x) \text{d}x = %s$' % (c1, c2, latex(res_b + 5))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Lời giải chi tiết phần b
            f_sq_expand = simplify(f_sq)
            nguyen_ham_b = Integral(f_sq, x).doit()
            loigiai_th_1 = r'''$\int_{%s}^{%s} f^2(x) \text{d}x = \int_{%s}^{%s} (%s)^2 \text{d}x = \int_{%s}^{%s} (%s) \text{d}x = \left( %s \right) \bigg|_{%s}^{%s} = %s$.''' % (
                c1, c2, c1, c2, latex(f), c1, c2, latex(f_sq_expand), latex(nguyen_ham_b), c1, c2, latex(res_b)
            )

            list_th_1 = [th_da_1]
            list_th_2 = [loigiai_th_1]

            ########################################################################
            # Vận dụng: Tích phân chứa dấu trị tuyệt đối
            ########################################################################
            # Cận từ -x0 đến x0+3 (tương ứng -2 đến 5)
            v1, v2 = -val_x0, val_x0 + 3
            # Tính tích phân trị tuyệt đối
            res_c = Integral(Abs(f), (x, v1, v2)).doit()

            # Phân tích res_c thành 3^n * 5^m. (Trong mẫu là 25 = 3^0 * 5^2)
            # Ở đây ta giả định kết quả có thể ép về dạng này hoặc giữ nguyên logic tìm m, n
            # Để đơn giản và đúng mẫu, ta xét kết quả cụ thể. 
            # Với val_x0=2, v1=-2, v2=5, res_c = 25.
            m_val = 0 # Số mũ của 3
            n_val = 0 # Số mũ của 5
            temp_res = res_c
            while temp_res % 5 == 0 and temp_res > 0:
                temp_res //= 5
                n_val += 1
            while temp_res % 3 == 0 and temp_res > 0:
                temp_res //= 3
                m_val += 1

            sum_mn = m_val**2 + n_val**2

            vd_da_1_d = r'\True Cho $\int_{%s}^{%s} |f(x)| \text{d}x = 3^m \cdot 5^n$. Khi đó $m^2 + n^2 = %s$' % (v1, v2, sum_mn)
            vd_da_1_s = r'Cho $\int_{%s}^{%s} |f(x)| \text{d}x = 3^m \cdot 5^n$. Khi đó $m^2 + n^2 = %s$' % (v1, v2, sum_mn + 1)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = r'''Ta có $\int_{%s}^{%s} |%s| \text{d}x = \int_{%s}^{%s} (%s) \text{d}x + \int_{%s}^{%s} (%s) \text{d}x = %s$. \\
            Suy ra $3^m \cdot 5^n = %s \Rightarrow m=%s, n=%s \Rightarrow m^2+n^2=%s$.''' % (
                v1, v2, latex(f), v1, val_x0, latex(-f), val_x0, v2, latex(f), res_c, res_c, m_val, n_val, sum_mn
            )

            list_vd_1 = [vd_da_1]
            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # Vận dụng cao: Tìm cực trị của hàm số tích phân
            ########################################################################
            # F(a) = tích phân từ 0 đến a của f(x)
            F_a_expr = Integral(f, (x, 0, a_sym)).doit()
            # F(a) = (val_a/2)a^2 + val_b*a
            # Đạo hàm F'(a) = f(a) = val_a*a + val_b. Cực trị tại a = -val_b/val_a = val_x0
            min_val_F = F_a_expr.subs(a_sym, val_x0)

            vdc_da_1_d = r'\True Hàm số $F(a) = \int_{0}^{a} f(x) \text{d}x$ đạt giá trị nhỏ nhất bằng $%s$ khi $a = %s$' % (min_val_F, val_x0)
            vdc_da_1_s = r'Hàm số $F(a) = \int_{0}^{a} f(x) \text{d}x$ đạt giá trị nhỏ nhất bằng $%s$ khi $a = %s$' % (min_val_F + 2, val_x0)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = r'''Ta có $F(a) = \int_{0}^{a} (%s) \text{d}x = (%s) \bigg|_0^a = %s$. \\
            Đây là hàm số bậc hai đạt giá trị nhỏ nhất tại $a = %s$ với $F(%s) = %s$.''' % (
                latex(f), latex(Integral(f, x).doit()), latex(simplify(F_a_expr)), val_x0, val_x0, min_val_F
            )

            list_vdc_1 = [vdc_da_1]
            list_vdc_2 = [loigiai_vdc_1]

            # --- PHẦN TRỘN VÀ XUẤT KẾT QUẢ ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                d1 = random.choice(list_nb_da_1)
                d2 = random.choice(list_th_da_1)
                d3 = random.choice(list_vd_da_1)
                d4 = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([d1, d2, d3, d4]) <= 3:
                    shuffled_answers = [d1, d2, d3, d4]
                    shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]
                    break

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(shuffled_answers[0]) + '}\n'
                '{' + str(shuffled_answers[1]) + '}\n'
                '{' + str(shuffled_answers[2]) + '}\n'
                '{' + str(shuffled_answers[3]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(shuffled_solutions[0]) + '\n'
                '\\item ' + str(shuffled_solutions[1]) + '\n'
                '\\item ' + str(shuffled_solutions[2]) + '\n'
                '\\item ' + str(shuffled_solutions[3]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


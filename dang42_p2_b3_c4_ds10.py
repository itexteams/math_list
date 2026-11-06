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


def bt_dang42_p2_b3_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # --- Bước 1: Khởi tạo dữ liệu ngẫu nhiên ---
            # f(x) có nghiệm kép a, luôn dương => f(x) = k(x - a)^2
            val_a = random.randint(1, 4)
            val_k = random.randint(1, 2)
            f_expr = val_k * (x - val_a)**2
            f_expand = sp.expand(f_expr)

            # Tạo g(x) chứa tham số m, n để tính S = m + n
            # Giả sử g(x) = x^2 - 2nx + (n^2 + m)
            val_n = random.randint(2, 5)
            val_m = random.randint(5, 15)
            const_term = val_n**2 + val_m
            g_expr = x**2 - 2*val_n*x + const_term
            sum_mn = val_m + val_n

            # --- Nội dung câu hỏi ---
            noidungcauhoi = ('''Cho hai tam thức bậc hai $f(x) = %s$ và $g(x) = %s$. Tam thức $f(x)$ có bảng xét dấu như hình vẽ dưới đây (với $a$ là một số thực). Tính giá trị biểu thức $S = m + n$ biết $m, n$ là các hằng số trong biểu thức của $g(x)$ tương ứng với dạng $g(x) = x^2 - 2nx + n^2 + m$.''' 
                             %(latex(f_expand), latex(g_expr)))

            # Vẽ bảng xét dấu bằng TikZ
            tikz_bxd = ('''\\begin{center}
            \\begin{tikzpicture}
            \\tkzTabInit[lgt=1.2, espcl=2.5]{$x$/1, $f(x)$/1}{$-\\infty$, $%s$, $+\\infty$}
            \\tkzTabLine{, +, 0, +, }
            \\end{tikzpicture}
            \\end{center}''' % (latex(val_a)))

            noidungcauhoi = noidungcauhoi + "\n" + tikz_bxd

            ########################################################################
            # Nhận biết
            ########################################################################
            nb_da_1_d = '\\True Hai tam thức không đổi dấu qua điểm $x = a$'
            nb_da_1_s = 'Hai tam thức đổi dấu qua điểm $x = a$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Dựa vào bảng xét dấu của tam thức bậc hai $f(x)$, ta thấy tại điểm $x = a$, $f(x) = 0$ nhưng dấu của $f(x)$ ở hai bên điểm $x = a$ đều là dấu dương (+). Do đó, tam thức không đổi dấu qua điểm $x = a$.''')

            ########################################################################
            # Thông hiểu
            ########################################################################
            th_da_1_d = '\\True Giá trị của $a = %s$' % (latex(val_a))
            th_da_1_s = 'Giá trị của $a = %s$' % (latex(val_a + 2))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Tam thức $f(x) = %s$ có nghiệm kép khi và chỉ khi $\\Delta = 0$. Giải phương trình $f(x) = 0 \\Leftrightarrow %s = 0 \\Leftrightarrow x = %s$. Đối chiếu với bảng xét dấu, ta có $a = %s$.''' 
                            % (latex(f_expand), latex(f_expand), latex(val_a), latex(val_a)))

            ########################################################################
            # Vận dụng
            ########################################################################
            vd_da_1_d = '\\True Giá trị biểu thức $m + n = %s$' % (latex(sum_mn))
            vd_da_1_s = 'Giá trị biểu thức $m + n = %s$' % (latex(sum_mn + random.randint(1,3)))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Ta có $g(x) = %s$. Theo đề bài $g(x) = x^2 - 2nx + n^2 + m$. \\\\
            Đồng nhất hệ số ta có: $-2n = %s \\Rightarrow n = %s$. \\\\
            Mặt khác $n^2 + m = %s \\Rightarrow %s^2 + m = %s \\Rightarrow m = %s$. \\\\
            Vậy $S = m + n = %s + %s = %s$.''' 
                            % (latex(g_expr), latex(-2*val_n), latex(val_n), latex(const_term), latex(val_n), latex(const_term), latex(val_m), latex(val_m), latex(val_n), latex(sum_mn)))

            ########################################################################
            # Vận dụng cao
            ########################################################################
            # Xét bất phương trình 2f(x) >= g(x) + 1
            # Tính h(x) = 2f(x) - g(x) - 1


            h_expr = simplify(2*f_expand - g_expr - 1)
            h_coeff_a = collect(h_expr, x).coeff(x, 2)

            # Tính Delta của h(x) = Ax^2 + Bx + C
            A = simplify(h_coeff_a)
            B = simplify(h_expr.coeff(x, 1))
            C = simplify(h_expr.coeff(x, 0))
            delta_h = simplify(B**2 - 4*A*C)

            # Kiểm tra dấu bằng SymPy (tránh lỗi Relational)
            if delta_h.is_negative and A.is_positive:
                ket_luan = "vô nghiệm"
                is_true = False
            else:
                ket_luan = "có nghiệm"
                is_true = True


            vdc_da_1_d = '\\True Bất phương trình $2f(x) \\geq g(x) + 1$ có tập nghiệm khác rỗng'
            vdc_da_1_s = 'Bất phương trình $2f(x) \\geq g(x) + 1$ vô nghiệm'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Xét bất phương trình $2f(x) \\geq g(x) + 1 \\Leftrightarrow 2f(x) - g(x) - 1 \\geq 0$. \\\\
            Thay biểu thức của $f(x)$ và $g(x)$ vào, ta được: \\\\
            $2\\left(%s\\right) - \\left(%s\\right) - 1 \\geq 0 \\\\
            \\Leftrightarrow %s \\geq 0$. \\\\
            Xét tam thức $h(x) = %s$ có hệ số $a = %s$. \\\\
            Biệt thức $\\Delta = (%s)^2 - 4 \\cdot (%s) \\cdot (%s) = %s$. \\\\
            ''' % (latex(f_expand), latex(g_expr), latex(h_expr), latex(h_expr), latex(A), latex(B), latex(A), latex(C), latex(delta_h)))

            if delta_h < 0:
                if A > 0:
                    loigiai_vdc_1 += "Vì $a > 0$ và $\\Delta < 0$ nên $h(x) > 0$ với mọi $x \\in \\mathbb{R}$. Vậy bất phương trình có tập nghiệm là $S = \\mathbb{R}$."
                else:
                    loigiai_vdc_1 += "Vì $a < 0$ và $\\Delta < 0$ nên $h(x) < 0$ với mọi $x \\in \\mathbb{R}$. Vậy bất phương trình vô nghiệm."
            else:
                loigiai_vdc_1 += "Vì $\\Delta \\geq 0$, tam thức $h(x)$ luôn có nghiệm hoặc có khoảng làm cho $h(x) \\geq 0$. Vậy bất phương trình luôn có nghiệm."

            # --- Xử lý chọn đáp án đúng/sai như mẫu ---
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

            # Xuất câu hỏi
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n' +
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


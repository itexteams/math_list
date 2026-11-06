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


def bt_dang38_p2_b3_c3_ds12(self):
                # Khai báo biến symbolic
                # Khai báo biến
                x = symbols('x')
                a_var = symbols('a')

                # ================= B3: RANDOM HỆ SỐ =================
                # Để bài toán "đẹp", ta chọn m, n, p sao cho f(x) có nghiệm hoặc cực trị hữu tỷ
                # Một cách dễ nhất là chọn f(x) = k*(2x^3 - 3x^2 + 1) với k ngẫu nhiên
                k = random.randint(1, 3) 
                m, n, p = 2*k, -3*k, 1*k

                # Hoặc bạn có thể random tự do hơn như sau:
                # m = random.choice([2, 4, 6])
                # n = -1.5 * m
                # p = m / 2
                # =====================================================

                f_x = m*x**3 + n*x**2 + p

                # Nội dung câu hỏi
                noidungcauhoi = ('''Cho hàm số $f(x)=%s$.''' % (latex(f_x)))

                ########################################################################
                # Nhận biết 
                ########################################################################
                # Nguyên hàm chuẩn: G(x) = (m/4)x^4 + (n/3)x^3 + px
                G_x_dung = Integral(f_x, x).doit()
                # Tạo một đáp án sai bằng cách sai hệ số
                G_x_sai = G_x_dung + random.choice([x**2, x, 1]) 

                nb_da_1_d = '\\True Hàm số đã cho có một nguyên hàm là hàm số $G(x) = %s$' % (latex(G_x_dung))
                nb_da_1_s = 'Hàm số đã cho có một nguyên hàm là hàm số $G(x) = %s$' % (latex(G_x_sai))
                list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
                nb_da_1 = random.choice(list_nb_da_1)

                loigiai_nb_1 = ('''Ta có $\\int f(x) \\text{d}x = \\int \\left( %s \\right) \\text{d}x = %s + C$. \\\\ Với $C=0$, ta có một nguyên hàm là $G(x) = %s$.'''
                                % (latex(f_x), latex(G_x_dung), latex(G_x_dung)))

                ########################################################################
                # Thông hiểu 
                ########################################################################
                # Tính diện tích từ 0 đến 2. Lưu ý: f(x) = k(x-1)^2(2x+1) luôn >= 0 trên [0, 2]
                area_val = Integral(f_x, (x, 0, 2)).doit()
                area_str = latex(area_val)

                th_da_1_d = '\\True Diện tích hình phẳng giới hạn bởi đồ thị hàm số đã cho, trục hoành và hai đường thẳng $x=0, x=2$ bằng $%s$' % (area_str)
                th_da_1_s = 'Diện tích hình phẳng giới hạn bởi đồ thị hàm số đã cho, trục hoành và hai đường thẳng $x=0, x=2$ bằng $%s$' % (latex(area_val + random.randint(1, 3)))
                list_th_da_1 = [th_da_1_d, th_da_1_s]
                th_da_1 = random.choice(list_th_da_1)

                loigiai_th_1 = ('''Diện tích hình phẳng cần tìm là $S = \\int\\limits_{0}^{2} |f(x)| \\text{d} x$. \\\\ Vì $f(x) \\ge 0$ với mọi $x \\in \\left[ 0; 2 \\right]$ nên: \\\\ $S = \\int\\limits_{0}^{2} \\left( %s \\right) \\text{d}x = \\left. \\left( %s \\right) \\right|_{0}^{2} = %s$.'''
                                % (latex(f_x), latex(G_x_dung), area_str))

                ########################################################################
                # Vận dụng 
                ########################################################################
                # Tìm F(x) sao cho F(2) = 2
                val_at_2 = G_x_dung.subs(x, 2)
                C_val = 2 - val_at_2
                F_x = G_x_dung + C_val
                F_minus_1 = F_x.subs(x, -1)

                vd_da_1_d = '\\True $F(x)$ là một nguyên hàm của hàm số đã cho thỏa mãn $F(2)=2$, khi đó $F(-1)=%s$' % (latex(F_minus_1))
                vd_da_1_s = '$F(x)$ là một nguyên hàm của hàm số đã cho thỏa mãn $F(2)=2$, khi đó $F(-1)=%s$' % (latex(F_minus_1 + 1))
                list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
                vd_da_1 = random.choice(list_vd_da_1)

                loigiai_vd_1 = ('''Họ nguyên hàm của hàm số là $F(x) = %s + C$. \\\\ Theo giả thiết $F(2)=2 \\Leftrightarrow %s + C = 2 \\Leftrightarrow C = %s$. \\\\ Do đó $F(x) = %s$. Suy ra $F(-1) = %s$.'''
                                % (latex(G_x_dung), latex(val_at_2), latex(C_val), latex(simplify(F_x)), latex(F_minus_1)))

                ########################################################################
                # Vận dụng cao
                ########################################################################
                # H(a) đạt GTLN trên [-1, 2]
                # H'(a) = f(a). Các nghiệm của f(x) là 1 và -1/2
                roots = solve(f_x, x)
                # Lọc các nghiệm thực trong khoảng [-1, 2]
                points_to_check = [-1, 2]
                for r in roots:
                    if r.is_real and -1 <= r <= 2:
                        points_to_check.append(r)

                # Tính giá trị tại các điểm để tìm GTLN
                values = {p_check: Integral(f_x, (x, -1, p_check)).doit() for p_check in points_to_check}
                max_a = max(values, key=values.get)
                max_val = values[max_a]

                vdc_da_1_d = '\\True Với $a \\in \\left[ -1; 2 \\right]$, hàm số $H(a) = \\int\\limits_{-1}^{a} f(x) \\text{d}x$ đạt giá trị lớn nhất tại $a=%s$' % (latex(max_a))
                vdc_da_1_s = 'Với $a \\in \\left[ -1; 2 \\right]$, hàm số $H(a) = \\int\\limits_{-1}^{a} f(x) \\text{d}x$ đạt giá trị lớn nhất tại $a=0$'
                list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
                vdc_da_1 = random.choice(list_vdc_da_1)

                # Chuẩn bị lời giải cho VDC (tự động điền các điểm cực trị)
                list_values_str = ", ".join(["H(%s) = %s" % (latex(p), latex(values[p])) for p in sorted(points_to_check)])

                loigiai_vdc_1 = ('''Xét hàm số $H(a) = \\int\\limits_{-1}^{a} f(x) \\text{d}x$ trên đoạn $\\left[ -1; 2 \\right]$. \\\\ Ta có $H\'(a) = f(a) = %s$. \\\\ $H\'(a) = 0 \\Leftrightarrow a \\in \\left\\lbrace%s \\right\\rbrace$. \\\\ Ta tính được: $%s$. \\\\ So sánh các giá trị, ta thấy hàm số đạt giá trị lớn nhất tại $a=%s$.'''
                                 % (latex(f_x.subs(x, a_var)), ", ".join([latex(r) for r in roots if r.is_real]), list_values_str, latex(max_a)))

                ########################################################################
                # Logic xáo trộn và xuất nội dung (Giữ nguyên cấu trúc của bạn)
                ########################################################################
                def count_true_answers(answers):
                    return sum('\\True' in ans for ans in answers)

                while True:
                    nb_sel, th_sel, vd_sel, vdc_sel = random.choice(list_nb_da_1), random.choice(list_th_da_1), random.choice(list_vd_da_1), random.choice(list_vdc_da_1)
                    if 1 <= count_true_answers([nb_sel, th_sel, vd_sel, vdc_sel]) <= 3:
                        break

                # In kết quả (Sử dụng các biến đã chọn)
                content = ('\\begin{minipage}{\\textwidth} \n'
                    '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n\\choiceTFn \n'
                    '{'+str(nb_sel)+'}\n'
                    '{'+str(th_sel)+'}\n'
                    '{'+str(vd_sel)+'}\n'
                    '{'+str(vdc_sel)+'}\n'
                    '\\loigiai{ \n'
                    '\\begin{enumEX}[a)]{1} \n'
                    '\\item '+str(loigiai_nb_1)+'\n'
                    '\\item '+str(loigiai_th_1)+'\n'
                    '\\item '+str(loigiai_vd_1)+'\n'
                    '\\item '+str(loigiai_vdc_1)+'\n'
                    '\\end{enumEX}} \n'
                    '\\end{ex}\n \\end{minipage} \n\n')

                return content


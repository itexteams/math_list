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


def bt_dang15_p3_b1_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Khởi tạo biến ký hiệu x của SymPy
                x_sym = symbols('x')

                while True:
                    # Chọn m, n nguyên dương để hệ số bậc hai và bậc nhất nguyên đẹp
                    # m là tâm cực trị, n là nửa khoảng cách giữa 2 hoành độ cực trị
                    m = randint(-2, 2)
                    n = randint(1, 3)
                    d = randint(-5, 5)

                    # Hàm số bậc ba: y = x^3 - 3*m*x^2 + 3*(m^2 - n^2)*x + d
                    coeff_a = 1
                    coeff_b = -3 * m
                    coeff_c = 3 * (m**2 - n**2)
                    coeff_d = d

                    # Đảm bảo đạo hàm có hai nghiệm phân biệt (n > 0 đã đảm bảo điều này)
                    # Tạo đa thức y bằng SymPy
                    y_expr = coeff_a * x_sym**3 + coeff_b * x_sym**2 + coeff_c * x_sym + coeff_d
                    dy_expr = diff(y_expr, x_sym)

                    # Tìm phần dư của phép chia y cho y' để xác định đường thẳng đi qua hai điểm cực trị
                    r_expr = rem(y_expr, dy_expr)

                    # r_expr có dạng: A*x + B
                    # Đường thẳng d: A*x - y + B = 0 (tương đương coeff_A*x + coeff_B*y + coeff_C = 0)
                    coeff_A = r_expr.coeff(x_sym)
                    coeff_B = -1
                    coeff_C = r_expr.subs(x_sym, 0)

                    # Tránh các trường hợp đường thẳng đi qua gốc tọa độ O (khoảng cách = 0)
                    if coeff_C == 0:
                        continue

                    # Tính khoảng cách từ O(0,0) đến đường thẳng coeff_A*x + coeff_B*y + coeff_C = 0
                    distance_val = abs(coeff_C) / sqrt(coeff_A**2 + coeff_B**2)

                    # Chuyển đổi thành giá trị float để làm tròn
                    dist_float = float(distance_val)

                    # Làm tròn đến hàng phần chục (hàng phần mười)
                    kq_dec = Decimal(str(dist_float)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                    kq = str(kq_dec).replace('.', ',')

                    # Chỉ lấy các giá trị khoảng cách dương và hợp lý
                    if dist_float > 0.05:
                        break

                # Tạo các phương án trắc nghiệm sai lệch
                du = ['$%s$' % (kq)]
                da = random.choice(du)

                # Tạo các đáp án nhiễu (không trùng với đáp án đúng)
                kq_float = float(kq_dec)
                s_candidates = [
                    round(kq_float + 0.4, 1),
                    round(kq_float + 0.8, 1),
                    round(kq_float + 1.2, 1),
                    round(kq_float - 0.4, 1) if kq_float > 0.4 else round(kq_float + 1.6, 1),
                    round(kq_float - 0.8, 1) if kq_float > 0.8 else round(kq_float + 2.0, 1),
                    round(1 / kq_float, 1) if kq_float > 0 else round(kq_float + 1.5, 1)
                ]

                s = []
                for val in s_candidates:
                    val_str = str(val).replace('.', ',')
                    s.append('$%s$' % (val_str))

                s = [item for item in s if item != da]
                s = list(set(s))

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Chuẩn bị định dạng hiển thị hàm số y = ax^3 + bx^2 + cx + d
                sign_b = '+' if coeff_b > 0 else ''
                sign_c = '+' if coeff_c > 0 else ''
                sign_d = '+' if coeff_d > 0 else ''

                term_b = '%s%s x^2' % (sign_b, coeff_b) if coeff_b != 0 else ''
                term_c = '%s%s x' % (sign_c, coeff_c) if coeff_c != 0 else ''
                term_d = '%s%s' % (sign_d, coeff_d) if coeff_d != 0 else ''

                ham_so_latex = 'x^3 %s %s %s' % (term_b, term_c, term_d)
                ham_so_latex = ' '.join(ham_so_latex.split())

                # Câu hỏi
                noidungcauhoi = ('''Đồ thị của hàm số $y = %s$ có hai điểm cực trị là $A$ và $B$. Khoảng cách từ gốc tọa độ $O$ đến đường thẳng $AB$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục).'''
                                 % (ham_so_latex))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Lời giải chi tiết từng bước theo yêu cầu
                # Biểu diễn phương trình đường thẳng cực trị d: y = Ax + C
                sign_coeff_C = '+' if coeff_C >= 0 else ''
                line_eq_y = '%s x %s %s' % (latex(coeff_A), sign_coeff_C, latex(coeff_C))
                line_eq_y = ' '.join(line_eq_y.split())

                # Phương trình tổng quát Ax + By + C = 0
                sign_coeff_C_general = '+' if coeff_C >= 0 else ''
                general_eq = '%s x - y %s %s = 0' % (latex(coeff_A), sign_coeff_C_general, latex(coeff_C))
                general_eq = ' '.join(general_eq.split())

                loigiai = ('''Tập xác định của hàm số là $D = \\mathbb{R}$.\\\\
                           Đạo hàm của hàm số: $y\' = 3x^2 %s x %s$.\\\\
                           Vì $y\' = 0$ luôn có hai nghiệm phân biệt nên đồ thị hàm số có hai điểm cực trị là $A$ và $B$.\\\\
                           Thực hiện phép chia đa thức $y$ cho $y\'$, ta được:
                           $$y = y\' \\cdot Q(x) + \\left(%s x %s %s\\right)$$
                           Vì tọa độ hai điểm cực trị $A, B$ thỏa mãn $y\'(x_A) = y\'(x_B) = 0$ nên phương trình đường thẳng $AB$ đi qua hai điểm cực trị có dạng:
                           $$y = %s \\Leftrightarrow %s.$$ 
                           Khoảng cách từ gốc tọa độ $O(0; 0)$ đến đường thẳng $AB$ là:
                           $$d(O, AB) = \\frac{|%s \\cdot 0 - 0 %s %s|}{\\sqrt{(%s)^2 + (-1)^2}} = \\frac{|%s|}{\\sqrt{%s}} \\approx %s.$$ 
                           Vậy khoảng cách từ gốc tọa độ $O$ đến đường thẳng $AB$ xấp xỉ $%s$.'''
                           % ('+' + str(2 * coeff_b) if 2 * coeff_b >= 0 else str(2 * coeff_b),
                              '+' + str(coeff_c) if coeff_c >= 0 else str(coeff_c),
                              latex(coeff_A), sign_coeff_C, latex(coeff_C),
                              line_eq_y, general_eq,
                              latex(coeff_A), sign_coeff_C_general, latex(coeff_C),
                              latex(coeff_A), latex(coeff_C), latex(coeff_A**2 + 1), latex(kq), latex(kq)))
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content  


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


def bt_dang6_p2_b2_c2_ds10(self):
            # Khai báo biến
            # Khai báo biến sympy để format biểu thức đẹp
            x, y = symbols('x y')

            # =====================================================================
            # THUẬT TOÁN SINH NGƯỢC BÀI TOÁN TỪ ĐỈNH ĐA GIÁC
            # =====================================================================
            def generate_parameters():
                while True:
                    # 1. Random đỉnh A nằm trên đường y = 2x (Đảm bảo số chẵn chục cho đẹp)
                    xA = random.randint(10, 20) * 10
                    yA = 2 * xA

                    # 2. Random đỉnh C nằm trên đường y = x
                    xC = random.randint(xA // 10 + 2, xA // 10 + 10) * 10
                    yC = xC

                    # Đảm bảo khoảng cách y để B có không gian lồi
                    if yA <= yC + 10:
                        continue

                    # 3. Random đỉnh B ở giữa, đảm bảo tính chất lồi của đa giác
                    xB = random.randint(xA // 10 + 1, xC // 10 - 1) * 10
                    yB = random.randint(yC // 10 + 1, yA // 10 - 1) * 10

                    dxAB, dyAB = xB - xA, yB - yA
                    dxBC, dyBC = xC - xB, yC - yB

                    # Tính hệ số góc (Slope) để kiểm tra đa giác lồi
                    slopeAB = dyAB / dxAB if dxAB != 0 else float('inf')
                    slopeBC = dyBC / dxBC if dxBC != 0 else float('inf')

                    # Đường AB phải dốc hơn BC và cả hai đều phải đi xuống (âm)
                    if slopeAB >= slopeBC or slopeAB >= 0 or slopeBC >= 0:
                        continue

                    # 4. Tìm Ràng buộc 1: Đường thẳng AB (Giờ công)
                    # Dạng: a1*x + b1*y = c1
                    a1, b1 = -dyAB, dxAB
                    c1 = a1 * xA + b1 * yA
                    g1 = math.gcd(math.gcd(a1, b1), c1)
                    a1, b1, c1 = a1//g1, b1//g1, c1//g1

                    # 5. Tìm Ràng buộc 2: Đường thẳng BC (Vải)
                    # Dạng: a2*x + b2*y = c2
                    a2, b2 = -dyBC, dxBC
                    c2 = a2 * xB + b2 * yB
                    g2 = math.gcd(math.gcd(a2, b2), c2)
                    a2, b2, c2 = a2//g2, b2//g2, c2//g2

                    # Tránh các hệ số nguyên vật liệu quá to (lớn hơn 30 đơn vị)
                    if max(a1, b1, a2, b2) > 30:
                        continue

                    return {
                        'A': (xA, yA), 'B': (xB, yB), 'C': (xC, yC),
                        'a1': a1, 'b1': b1, 'c1': c1, # Hệ số Giờ công
                        'a2': a2, 'b2': b2, 'c2': c2  # Hệ số Vải
                    }

            # =====================================================================
            # ÁP DỤNG THÔNG SỐ VÀO BÀI TOÁN
            # =====================================================================

            params = generate_parameters()
            xA, yA = params['A']
            xB, yB = params['B']
            xC, yC = params['C']

            # Hệ số Ràng buộc
            a1, b1, c1 = params['a1'], params['b1'], params['c1'] # Công
            a2, b2, c2 = params['a2'], params['b2'], params['c2'] # Vải

            # Random lợi nhuận
            p_v = random.choice([200, 250, 300, 350, 400])
            p_t = random.choice([100, 150, 180, 200])

            # Biểu thức Sympy để render LaTeX
            expr_cong = a1*x + b1*y
            expr_vai = a2*x + b2*y
            expr_loinhuan = p_v*x + p_t*y

            # Tìm đỉnh có lợi nhuận Max
            points = [(0, 0), (xA, yA), (xB, yB), (xC, yC)]
            profits = [(px, py, p_v * px + p_t * py) for px, py in points]
            max_profit = max(profits, key=lambda item: item[2])
            x_max, y_max, f_max = max_profit

            # Điểm nhiễu cho câu Vận dụng cao
            wrong_points = [p for p in points if p[0] != x_max or p[1] != y_max and p[0] != 0]
            x_wrong, y_wrong = random.choice(wrong_points)

            # NỘI DUNG CÂU HỎI
            noidungcauhoi = ('''Một phân xưởng may áo vest và quần âu để chuẩn bị bán cho dịp cuối năm. Biết may một cái áo vest hết $%s$ m vải, và cần $%s$ giờ; 1 quần âu hết $%s$ m vải và cần $%s$ giờ. Phân xưởng được giao sử dụng không quá $%s$ m vải và số giờ công không vượt quá $%s$ giờ. Theo khảo sát thị trường, số lượng quần bán ra không nhỏ hơn số lượng áo và không vượt quá 2 lần số lượng áo. Khi bán ra thị trường, một chiếc áo lãi $%s$ ngàn đồng và một chiếc quần lãi $%s$ ngàn đồng. Gọi $x; y$ lần lượt là số lượng áo vest và quần âu mà phân xưởng cần may.''' 
                             % (a2, a1, b2, b1, c2, c1, p_v, p_t))

            # ----------------- Nhận biết -----------------
            nb_da_1_d = '\\True Số tiền lãi của phân xưởng là $F(x; y)=%s$ (đơn vị ngàn đồng)' % latex(expr_loinhuan)
            nb_da_1_s = 'Số tiền lãi của phân xưởng là $F(x; y)=%s$ (đơn vị ngàn đồng)' % latex(p_t*x + p_v*y)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Vì một chiếc áo vest lãi $%s$ (ngàn đồng) và một chiếc quần lãi $%s$ (ngàn đồng) nên số tiền lãi của phân xưởng khi sản xuất $x$ chiếc áo vest và $y$ chiếc quần âu là: $F(x;y)=%s$.''' % (p_v, p_t, latex(expr_loinhuan)))

            # ----------------- Thông hiểu -----------------
            th_da_1_d = '\\True Số mét vải để may quần và áo thỏa mãn: $%s \\le %s$; và số giờ cần dùng thỏa mãn: $%s \\le %s$' % (latex(expr_vai), c2, latex(expr_cong), c1)
            th_da_1_s = 'Số mét vải để may quần và áo thỏa mãn: $%s \\ge %s$; và số giờ cần dùng thỏa mãn: $%s \\ge %s$' % (latex(expr_vai), c2, latex(expr_cong), c1)

            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Một chiếc áo cần $%s$ m; quần cần $%s$ m; số vải không vượt quá $%s$ m nên có: $%s \\le %s$. \\\\ Tương tự, thời gian may áo cần $%s$ giờ, quần cần $%s$ giờ, tổng giờ không vượt quá $%s$ nên có: $%s \\le %s$.''' % (a2, b2, c2, latex(expr_vai), c2, a1, b1, c1, latex(expr_cong), c1))

            # ----------------- Vận dụng -----------------
            vd_da_1_d = '''\\True Hệ bất phương trình thỏa mãn điều kiện đề bài là: $\\begin{cases} x \\ge 0 \\\\ y \\ge 0 \\\\ %s \\le %s \\\\ %s \\le %s \\\\ x \\le y \\le 2x \\end{cases}$''' % (latex(expr_vai), c2, latex(expr_cong), c1)
            vd_da_1_s = '''Hệ bất phương trình thỏa mãn điều kiện đề bài là: $\\begin{cases} x \\ge 0 \\\\ y \\ge 0 \\\\ %s \\le %s \\\\ %s \\le %s \\\\ y \\le x \\le 2y \\end{cases}$''' % (latex(expr_vai), c2, latex(expr_cong), c1)

            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Số lượng quần bán ra không nhỏ hơn áo và không vượt quá 2 lần áo nên ta có: $x \\le y \\le 2x$. \\\\ Hệ bất phương trình là: $\\begin{cases} x \\ge 0 \\\\ y \\ge 0 \\\\ %s \\le %s \\\\ %s \\le %s \\\\ x \\le y \\le 2x \\end{cases}$''' % (latex(expr_vai), c2, latex(expr_cong), c1))

            # ----------------- Vận dụng cao -----------------
            vdc_da_1_d = '\\True Để thu được tiền lãi cao nhất thì phân xưởng cần may $%s$ chiếc áo vest và $%s$ chiếc quần âu' % (x_max, y_max)
            vdc_da_1_s = 'Để thu được tiền lãi cao nhất thì phân xưởng cần may $%s$ chiếc áo vest và $%s$ chiếc quần âu' % (x_wrong, y_wrong)

            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Miền nghiệm của hệ là miền tứ giác $OABC$ với $O(0;0); A(%s;%s); B(%s;%s); C(%s;%s)$. \\\\ Ta có $F$ đạt giá trị lớn nhất khi $x=%s; y=%s$. \\\\ Vậy phân xưởng cần may $%s$ áo vest và $%s$ quần âu để có lãi cao nhất.''' % (xA, yA, xB, yB, xC, yC, x_max, y_max, x_max, y_max))

            # =====================================================================
            # KIỂM SOÁT RANDOM ĐÚNG SAI & IN KẾT QUẢ
            # =====================================================================
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                ans_nb = random.choice(list_nb_da_1)
                ans_th = random.choice(list_th_da_1)
                ans_vd = random.choice(list_vd_da_1)
                ans_vdc = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([ans_nb, ans_th, ans_vd, ans_vdc]) <= 3:
                    break

            # Xuất chuỗi cuối cùng
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ '\n'
                '\\choiceTFn \n'
                '{'+str(ans_nb)+'}\n'
                '{'+str(ans_th)+'}\n'
                '{'+str(ans_vd)+'}\n'
                '{'+str(ans_vdc)+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(loigiai_nb_1)+'\n'
                '\\item '+str(loigiai_th_1)+'\n'
                '\\item '+str(loigiai_vd_1)+'\n'
                '\\item '+str(loigiai_vdc_1)+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n\\end{minipage}\n\n')
            return content


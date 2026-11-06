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


def bt_dang50_p2_b3_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x') # x là số tiền tăng thêm (nghìn đồng/kg)

            # --- THIẾT LẬP THÔNG SỐ NGẪU NHIÊN ---
            # H: Sản lượng (kg)
            H = random.choice([800, 1000, 1200, 1500, 2000]) 
            # P0: Giá gốc (nghìn đồng)
            P0 = random.choice([20, 25, 30, 35, 40])
            # K: Hệ số tăng rau thừa (kg/1000đ tăng thêm)
            K = random.choice([10, 20, 25, 40, 50])
            # Pf: Giá thanh lý làm thức ăn chăn nuôi (nghìn đồng)
            Pf = random.choice([1, 2, 3, 5])

            # Đảm bảo giá thanh lý luôn thấp hơn giá bán gốc
            if Pf >= P0: Pf = 2

            # Các biểu thức cơ bản
            gia_ban = x + P0
            rau_thua = K * x
            rau_ban_duoc = H - K * x

            # Doanh thu: T = (rau_ban_duoc * gia_ban) + (rau_thua * Pf)
            T_expr = expand(rau_ban_duoc * gia_ban + rau_thua * Pf)

            # 1. Tìm x để doanh thu max
            T_diff = diff(T_expr, x)
            x_max = solve(T_diff, x)[0]
            gia_max = x_max + P0

            # 2. Thiết lập thông số cho câu d (Bất phương trình doanh thu)
            # Chọn một giá trị x_start nguyên để bài toán đẹp
            x_start = random.randint(2, 5)
            T_target = int(T_expr.subs(x, x_start))
            # Tìm nghiệm còn lại của phương trình T(x) = T_target
            roots = solve(T_expr - T_target, x)
            x_end = int(max(roots))

            # --- NỘI DUNG CÂU HỎI ---
            noidungcauhoi = ('''Một trang trại rau sạch ở Đà Lạt mỗi ngày thu hoạch được $%s$ tấn rau. Mỗi ngày nếu giá bán rau là $%s$ đồng/1kg thì bán hết rau, nếu giá bán rau tăng $1000$ đồng/kg thì số rau thừa tăng $%s$ kg. Số rau thừa này được thu mua hết để làm thức ăn chăn nuôi với giá $%s$ đồng/kg. Gọi $x (x > 0)$ là số tiền tăng lên cho mỗi kg rau (đơn vị nghìn đồng). ''' 
            % (latex(Rational(H, 1000)), latex(P0 * 1000), latex(K), latex(Pf * 1000)))

            ########################################################################
            # a) Nhận biết: Về giá bán và số lượng rau thừa
            nb_da_1_d = '\\True Số tiền bán cho mỗi kg rau sau khi tăng là $x + %s$ (nghìn đồng) và số kg rau thừa là $%sx$ với $x < %s$' % (P0, K, H//K)
            nb_da_1_s = 'Số tiền bán cho mỗi kg rau sau khi tăng là $x + %s$ (nghìn đồng) và số kg rau thừa là $%sx$ với $x < %s$' % (P0, K+5, H//K)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Giá bán ban đầu là %s nghìn đồng/kg. Khi tăng thêm $x$ nghìn đồng thì giá mới là $x + %s$. Theo đề bài, cứ tăng 1 nghìn đồng thì thừa %s kg, vậy tăng $x$ nghìn đồng thì thừa $%sx$ kg. Điều kiện để lượng rau bán ra không âm là $%s - %sx \\ge 0 \\Leftrightarrow x \\le %s$.''' % (P0, P0, K, K, H, K, H//K))

            ########################################################################
            # b) Thông hiểu: Công thức tổng doanh thu
            th_da_1_d = '\\True Tổng số tiền thu được là $T = %s$ (nghìn đồng)' % (latex(T_expr))
            th_da_1_s = 'Tổng số tiền thu được là $T = (%s - %sx)(x + %s)$ (nghìn đồng)' % (H, K, P0)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Tổng tiền thu được gồm tiền bán rau sạch và tiền bán rau thừa làm thức ăn chăn nuôi: \\\\
            $T(x) = (%s - %sx)(x + %s) + %sx \\cdot %s$ \\\\
            $T(x) = %s$.''' % (H, K, P0, K, Pf, latex(T_expr)))

            ########################################################################
            # c) Vận dụng: Giá bán để doanh thu lớn nhất
            vd_da_1_d = '\\True Nếu trang trại bán rau với giá $%s$ nghìn đồng/1kg thì mỗi ngày thu được tiền bán lớn nhất' % (latex(gia_max))
            vd_da_1_s = 'Nếu trang trại bán rau với giá $%s$ nghìn đồng/1kg thì mỗi ngày thu được tiền bán lớn nhất' % (latex(gia_max + 5))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Để tìm doanh thu lớn nhất, ta xét hàm số doanh thu $T(x) = %s$. \\\\
            Ta có $T\'(x) = %s$. \\\\
            $T\'(x) = 0 \\Leftrightarrow x = %s$. \\\\
            Khi đó giá bán để doanh thu đạt cực đại là: $%s + %s = %s$ (nghìn đồng/kg).''' % (latex(T_expr), latex(T_diff), latex(x_max), P0, latex(x_max), latex(gia_max)))

            ########################################################################
            # d) Vận dụng cao: Giải bất phương trình doanh thu
            vdc_da_1_d = '\\True Để tổng số tiền thu được không nhỏ hơn %s (nghìn đồng) thì $x \\in [%s; %s]$' % (T_target, x_start, x_end)
            vdc_da_1_s = 'Để tổng số tiền thu được không nhỏ hơn %s (nghìn đồng) thì $x \\in [1; %s]$' % (T_target, x_end + 2)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Yêu cầu bài toán tương đương với: $T(x) \\ge %s$ \\\\
            $\\Leftrightarrow %s \\ge %s$ \\\\
            $\\Leftrightarrow %s \\ge 0$. \\\\
            Giải bất phương trình bậc hai trên, ta thu được tập nghiệm là $x \\in [%s; %s]$.''' % (T_target, latex(T_expr), T_target, latex(expand(T_expr - T_target)), x_start, x_end))

            # --- XỬ LÝ NGẪU NHIÊN ĐÚNG/SAI ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                ans_a = random.choice(list_nb_da_1)
                ans_b = random.choice(list_th_da_1)
                ans_c = random.choice(list_vd_da_1)
                ans_d = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([ans_a, ans_b, ans_c, ans_d]) <= 3:
                    break

            # Gán đáp án và lời giải tương ứng
            final_answers = [ans_a, ans_b, ans_c, ans_d]
            final_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            # --- XUẤT KẾT QUẢ ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(final_answers[0]) + '}\n'
                '{' + str(final_answers[1]) + '}\n'
                '{' + str(final_answers[2]) + '}\n'
                '{' + str(final_answers[3]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(final_solutions[0]) + '\n'
                '\\item ' + str(final_solutions[1]) + '\n'
                '\\item ' + str(final_solutions[2]) + '\n'
                '\\item ' + str(final_solutions[3]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


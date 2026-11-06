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


def bt_dang20_p2_b1_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # BƯỚC 3: NGẪU NHIÊN HÓA BÀI TOÁN
            a = random.randint(1, 5)
            b_val = random.randint(2, 6)
            b_sq = b_val**2 

            noidungcauhoi = (r'''Cho hàm số $y = x - %s + \sqrt{%s - x}$. Có tập xác định $\mathscr{D}$.''' 
                             % (latex(a), latex(b_sq)))

            ########################################################################
            # a) Nhận biết: Tập xác định
            ########################################################################
            nb_da_1_d = r'\True Tập xác định của hàm số là $\mathscr{D} = (-\infty; %s]$ ' % latex(b_sq)
            nb_da_1_s = r'Tập xác định của hàm số là $\mathscr{D} = [-%s; +\infty)$ ' % latex(b_sq)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = (r'''Hàm số xác định khi và chỉ khi $%s - x \ge 0 \Leftrightarrow x \le %s$. 
                            Vậy tập xác định của hàm số là $\mathscr{D} = (-\infty; %s]$.''' 
                            % (latex(b_sq), latex(b_sq), latex(b_sq)))

            ########################################################################
            # b) Thông hiểu: Giao điểm trục tung
            ########################################################################
            y_intercept = -a + b_val 
            th_da_1_d = r'\True Đồ thị hàm số cắt trục tung tại điểm $(0; %s)$' % latex(y_intercept)
            th_da_1_s = r'Đồ thị hàm số cắt trục tung tại điểm $(0; %s)$' % latex(-a)
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = (r'''Để tìm giao điểm với trục tung, ta cho $x = 0$. Thay vào hàm số ta được:
                            $y = 0 - %s + \sqrt{%s - 0} = -%s + %s = %s$. 
                            Vậy đồ thị hàm số cắt trục tung tại điểm $(0; %s)$.''' 
                            %(latex(a), latex(b_sq), latex(a), latex(b_val), latex(y_intercept), latex(y_intercept)))

            ########################################################################
            # c) Vận dụng: Liệt kê phần tử nguyên
            ########################################################################
            low_bound = -2
            high_bound = 10
            end_point = min(b_sq, high_bound)
            # Tạo danh sách liệt kê chi tiết các phần tử nguyên
            nguyen_list = list(range(low_bound, end_point + 1))
            str_nguyen = "; ".join(map(str, nguyen_list))
            so_phan_tu = len(nguyen_list)

            vd_da_1_d = r'\True Có %s giá trị nguyên thuộc tập $\mathscr{D} \cap [%s; %s]$' % (so_phan_tu, low_bound, high_bound)
            vd_da_1_s = r'Có %s giá trị nguyên thuộc tập $\mathscr{D} \cap [%s; %s]$' % (so_phan_tu + 2, low_bound, high_bound)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = (r'''Ta có $\mathscr{D} \cap [%s; %s] = (-\infty; %s] \cap [%s; %s] = [%s; %s]$. 
                            Các giá trị nguyên thuộc tập hợp này bao gồm: $\{%s\}$. 
                            Tổng cộng có %s giá trị nguyên.''' 
                            %(low_bound, high_bound, latex(b_sq), low_bound, high_bound, low_bound, end_point, str_nguyen, so_phan_tu))

            ########################################################################
            # d) Vận dụng cao: Tham số m (Chi tiết các bước giải)
            ########################################################################
            c_param = 5
            m_sq_limit = b_sq + c_param
            m_val_limit = int(math.sqrt(m_sq_limit))
            # Tập S: các giá trị m nguyên sao cho m^2 >= m_sq_limit
            # Để viết chi tiết, ta xét m nguyên từ -10 đến 10 chẳng hạn
            S_list = [m for m in range(-15, 16) if m**2 >= m_sq_limit] # Giả định trong khoảng hẹp để minh họa
            # Trong bài toán gốc ảnh: m^2 - 5 <= 4 <=> m^2 <= 9 <=> -3 <= m <= 3 (Có 7 giá trị)
            # Ta làm theo đúng logic ảnh: m^2 - c_param <= b_sq
            so_m_nguyen = 2 * int(math.sqrt(b_sq + c_param)) + 1
            limit_val = int(math.sqrt(b_sq + c_param))
            m_nguyen_liet_ke = "; ".join(map(str, range(-limit_val, limit_val + 1)))

            vdc_da_1_d = r'\True Số phần tử của tập hợp $S$ là %s' % (so_m_nguyen)
            vdc_da_1_s = r'Số phần tử của tập hợp $S$ là %s' % (so_m_nguyen + 2)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = (r'''Để hàm số $y = \frac{\sqrt{m^2 - %s - x}}{2024}$ xác định trên tập $\mathscr{D} = (-\infty; %s]$, \\
                            điều kiện cần và đủ là $m^2 - %s - x \ge 0$ với mọi $x \in (-\infty; %s]$. \\
                            $\Leftrightarrow m^2 - %s \ge x$ với mọi $x \le %s$. \\
                            $\Leftrightarrow m^2 - %s \ge %s \Leftrightarrow m^2 \ge %s$. \\
                            $\Leftrightarrow -%s \le m \le %s$. \\
                            Vì $m$ là số nguyên nên $m \in \{%s\}$. \\
                            Vậy tập hợp $S$ có %s phần tử.''' 
                            %(c_param, latex(b_sq), c_param, latex(b_sq), c_param, latex(b_sq), c_param, latex(b_sq), b_sq + c_param, limit_val, limit_val, m_nguyen_liet_ke, so_m_nguyen))

            # --- Phần trộn và xuất nội dung giữ nguyên theo mẫu của bạn ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                ans_nb = random.choice(list_nb_da_1)
                ans_th = random.choice(list_th_da_1)
                ans_vd = random.choice(list_vd_da_1)
                ans_vdc = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([ans_nb, ans_th, ans_vd, ans_vdc]) <= 3:
                    break

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + 
                '\n\\choiceTFn \n'
                '{' + str(ans_nb) + '}\n'
                '{' + str(ans_th) + '}\n'
                '{' + str(ans_vd) + '}\n'
                '{' + str(ans_vdc) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


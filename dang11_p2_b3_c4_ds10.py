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


def bt_dang11_p2_b3_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # B1: Tạo giá trị ngẫu nhiên cho hai nghiệm x1, x2 (nguyên)
            # Để giống đề bài mẫu (1 và 2), ta cho x1 < x2
            x1 = random.randint(-2, 3)
            x2 = x1 + random.randint(1, 4)

            # Tính toán hệ số a, b theo Vi-et cho tam thức f(x) = x^2 - ax + b
            # f(x) = (x - x1)(x - x2) = x^2 - (x1 + x2)x + x1*x2
            val_a = x1 + x2
            val_b = x1 * x2

            # Hàm số f(x)
            f_x = x**2 - val_a*x + val_b

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho tam thức bậc hai $f(x) = x^2 - %s x + %s$ có bảng xét dấu như hình vẽ
            \\begin{center}
            \\begin{tabular}{|c|ccccccc|}
            \\hline
            $x$ & $-\\infty$ & & $%s$ & & $%s$ & & $+\\infty$ \\\\
            \\hline
            $f(x)$ & & $+$ & $0$ & $-$ & $0$ & $+$ & \\\\
            \\hline
            \\end{tabular}
            \\end{center}''' % (latex(val_a), latex(val_b), latex(x1), latex(x2)))

            ########################################################################
            # a) Nhận biết: Kiểm tra f(k) với k nằm ngoài khoảng nghiệm
            k_outside = x2 + 1
            val_fk = f_x.subs(x, k_outside)
            nb_da_1_d = '\\True $f(%s) > 0$' % (k_outside)
            nb_da_1_s = '$f(%s) < 0$' % (k_outside)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)
            loigiai_nb_1 = ('''Dựa vào bảng xét dấu, với $x > %s$ thì $f(x) > 0$. Vì $%s > %s$ nên $f(%s) > 0$.''' % (latex(x2), k_outside, latex(x2), k_outside))

            ########################################################################
            # b) Thông hiểu: Tập nghiệm f(x) <= 0
            th_da_1_d = '\\True $f(x) \\le 0 \\Leftrightarrow x \\in [%s; %s]$' % (latex(x1), latex(x2))
            th_da_1_s = '$f(x) \\le 0 \\Leftrightarrow x \\in (%s; %s)$' % (latex(x1), latex(x2))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)
            loigiai_th_1 = ('''Quan sát bảng xét dấu, ta thấy $f(x) \\le 0$ khi $x$ nằm trong đoạn giữa hai nghiệm $[%s; %s]$.''' % (latex(x1), latex(x2)))

            ########################################################################
            # c) Vận dụng: Tính tổng a + b
            sum_ab = val_a + val_b
            vd_da_1_d = '\\True $a + b = %s$' % (latex(sum_ab))
            vd_da_1_s = '$a + b = %s$' % (latex(sum_ab + 1))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)
            loigiai_vd_1 = ('''Từ bảng xét dấu, tam thức có hai nghiệm là $x= %s$ và $x= %s$. \\\\
            Theo định lý Vi-ét ta có: $\\begin{cases} x_1 + x_2 = a \\\\ x_1 x_2 = b \\end{cases} \\Rightarrow \\begin{cases} a = %s \\\\ b = %s \\end{cases}$. \\\\
            Vậy $a + b = %s + %s = %s$.''' % (latex(x1), latex(x2), latex(val_a), latex(val_b), latex(val_a), latex(val_b), latex(sum_ab)))

            ########################################################################
            # d) Vận dụng cao: Bất phương trình f(sqrt(x)) <= sqrt(x) + 2
            # f(t) = t^2 - at + b <= t + 2 => t^2 - (a+1)t + (b-2) <= 0
            t = symbols('t')
            bpt_t = t**2 - (val_a + 1)*t + (val_b - 2)
            nghiem_t = solve(bpt_t, t)
            t_min, t_max = nghiem_t[0], nghiem_t[1]

            # Điều kiện: sqrt(x) >= 0 và t_min <= sqrt(x) <= t_max
            # x_min = max(0, t_min)^2, x_max = t_max^2
            actual_t_min = max(0, t_min)
            x_min = actual_t_min**2
            x_max = t_max**2

            # Đếm số nghiệm nguyên x
            count_x = 0
            if x_max >= x_min:
                count_x = int(x_max) - int(x_min) + (1 if x_min == int(x_min) else 0)

            vdc_da_1_d = '\\True Bất phương trình $f(\\sqrt{x}) \\le \\sqrt{x} + 2$ có %s nghiệm nguyên' % (count_x)
            vdc_da_1_s = 'Bất phương trình $f(\\sqrt{x}) \\le \\sqrt{x} + 2$ có %s nghiệm nguyên' % (count_x + 2)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Đặt $t = \\sqrt{x}$ ($t \\ge 0$). Bất phương trình trở thành: \\\\
            $t^2 - %s t + %s \\le t + 2 \\Leftrightarrow t^2 - %s t + %s \\le 0$ \\\\
            Giải bất phương trình bậc hai theo $t$, ta được: $%s \\le t \\le %s$. \\\\
            Kết hợp điều kiện $t \\ge 0$, ta có: $%s \\le \\sqrt{x} \\le %s \\Leftrightarrow %s \\le x \\le %s$. \\\\
            Số nghiệm nguyên của bất phương trình là %s.''' 
            % (latex(val_a), latex(val_b), latex(val_a+1), latex(val_b-2), latex(t_min), latex(t_max), latex(actual_t_min), latex(t_max), latex(x_min), latex(x_max), count_x))

            # --- Xử lý Logic Chọn đáp án (1-3 câu đúng) ---
            while True:
                ans_a = random.choice(list_nb_da_1)
                ans_b = random.choice(list_th_da_1)
                ans_c = random.choice(list_vd_da_1)
                ans_d = random.choice(list_vdc_da_1)

                true_count = sum('\\True' in ans for ans in [ans_a, ans_b, ans_c, ans_d])
                if 1 <= true_count <= 3:
                    break

            # Gán lời giải tương ứng
            sol_a = loigiai_nb_1
            sol_b = loigiai_th_1
            sol_c = loigiai_vd_1
            sol_d = loigiai_vdc_1

            # Xuất kết quả
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
                '\\item ' + str(sol_a) + '\n'
                '\\item ' + str(sol_b) + '\n'
                '\\item ' + str(sol_c) + '\n'
                '\\item ' + str(sol_d) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('+ -','-')
            return content


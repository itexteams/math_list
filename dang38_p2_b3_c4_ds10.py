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


def bt_dang38_p2_b3_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')
            m = symbols('m')

            # Random tham số k để tạo biểu thức x^2 - 2kx + m - 1
            # Trong ảnh x^2 - 4x + m - 1 ứng với k = 2
            k = randint(2, 4)
            b_coeff = -2 * k
            m_crit = k**2 + 1 # Giá trị m để Delta' = 0 (m = k^2 + 1)

            # Biểu thức dưới căn
            g_x = x**2 + b_coeff*x + m - 1

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hàm số $y = \\frac{1}{\\sqrt{%s}}$.''' 
                             % (latex(g_x)))

            ########################################################################
            # a) Nhận biết: Kiểm tra TXĐ với m cụ thể (m < m_crit)
            ########################################################################
            m_val_a = m_crit - 1
            # Nghiệm của x^2 - 2kx + (m_crit - 2) = 0 là k-1 và k+1
            x1 = k - 1
            x2 = k + 1

            nb_da_1_d = '\\True Với $m = %s$ hàm số đã cho có tập xác định là $(-\\infty ; %s) \\cup (%s ; +\\infty)$' % (latex(m_val_a), latex(x1), latex(x2))
            nb_da_1_s = 'Với $m = %s$ hàm số đã cho có tập xác định là $(%s ; %s)$' % (latex(m_val_a), latex(x1), latex(x2))

            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Với $m = %s$, hàm số trở thành $y = \\frac{1}{\\sqrt{x^2 - %sx + %s}}$.\\\\
                            Điều kiện xác định: $x^2 - %sx + %s > 0 \\Leftrightarrow (x - %s)(x - %s) > 0 \\Leftrightarrow \\left[ \\begin{aligned} & x > %s \\\\ & x < %s \\end{aligned} \\right.$.\\\\
                            Vậy tập xác định là $\\mathscr{D} = (-\\infty ; %s) \\cup (%s ; +\\infty)$.''' 
                            % (latex(m_val_a), latex(2*k), latex(m_val_a - 1), latex(2*k), latex(m_val_a - 1), latex(x2), latex(x1), latex(x2), latex(x1), latex(x1), latex(x2)))

            list_nb_1 = [nb_da_1]
            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # b) Thông hiểu: Kiểm tra tính xác định trên R với m cụ thể (m > m_crit)
            ########################################################################
            m_val_b = m_crit + 1

            th_da_1_d = '\\True Với $m = %s$ hàm số đã cho luôn xác định trên $\\mathbb{R}$' % (latex(m_val_b))
            th_da_1_s = 'Với $m = %s$ hàm số đã cho không xác định trên $\\mathbb{R}$' % (latex(m_val_b))

            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Với $m = %s$, hàm số trở thành $y = \\frac{1}{\\sqrt{x^2 - %sx + %s}}$.\\\\
                            Xét tam thức $g(x) = x^2 - %sx + %s$ có $\\Delta' = (%s)^2 - 1 \\cdot %s = %s < 0$.\\\\
                            Vì $a = 1 > 0$ và $\\Delta' < 0$ nên $g(x) > 0$ với mọi $x \\in \\mathbb{R}$.\\\\
                            Vậy hàm số luôn xác định trên $\\mathbb{R}$.''' 
                            % (latex(m_val_b), latex(2*k), latex(m_val_b - 1), latex(2*k), latex(m_val_b - 1), latex(-k), latex(m_val_b - 1), latex(k**2 - (m_val_b - 1))))

            list_th_1 = [th_da_1]
            list_th_2 = [loigiai_th_1]

            ########################################################################
            # c) Vận dụng: Vị trí đồ thị (luôn nằm trên trục hoành)
            ########################################################################
            vd_da_1_d = '\\True Đồ thị hàm số luôn nằm phía bên trên trục hoành'
            vd_da_1_s = 'Đồ thị hàm số luôn nằm phía bên dưới trục hoành'

            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Hàm số có dạng $y = \\frac{1}{\\sqrt{g(x)}}$.\\\\
                            Điều kiện xác định là $g(x) > 0$. Khi đó $\\sqrt{g(x)} > 0$, suy ra $y = \\frac{1}{\\sqrt{g(x)}} > 0$ với mọi $x$ thuộc tập xác định.\\\\
                            Vì $y > 0$ nên đồ thị hàm số luôn nằm phía bên trên trục hoành.''')

            list_vd_1 = [vd_da_1]
            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # d) Vận dụng cao: Tìm m để hàm số xác định trên R
            ########################################################################
            vdc_da_1_d = '\\True $m > %s$ là điều kiện để hàm số luôn xác định trên $\\mathbb{R}$' % (latex(m_crit))
            vdc_da_1_s = '$m \\ge %s$ là điều kiện để hàm số luôn xác định trên $\\mathbb{R}$' % (latex(m_crit))

            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Để hàm số luôn xác định trên $\\mathbb{R}$, ta cần $x^2 - %sx + m - 1 > 0$ với mọi $x \\in \\mathbb{R}$.\\\\
                             Điều này xảy ra khi và chỉ khi: $\\Delta' < 0 \\Leftrightarrow (-%s)^2 - 1 \\cdot (m - 1) < 0 \\\\
                             \\Leftrightarrow %s - m + 1 < 0 \\Leftrightarrow %s - m < 0 \\Leftrightarrow m > %s$.''' 
                             % (latex(2*k), latex(k), latex(k**2), latex(k**2 + 1), latex(m_crit)))

            list_vdc_1 = [vdc_da_1]
            list_vdc_2 = [loigiai_vdc_1]

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi có từ 1 đến 3 đáp án đúng
            while True:
                nb_sel = random.choice(list_nb_da_1)
                th_sel = random.choice(list_th_da_1)
                vd_sel = random.choice(list_vd_da_1)
                vdc_sel = random.choice(list_vdc_da_1)

                if 1 <= count_true_answers([nb_sel, th_sel, vd_sel, vdc_sel]) <= 3:
                    # Tìm index lời giải tương ứng
                    idx_nb = list_nb_da_1.index(nb_sel)
                    idx_th = list_th_da_1.index(th_sel)
                    idx_vd = list_vd_da_1.index(vd_sel)
                    idx_vdc = list_vdc_da_1.index(vdc_sel)

                    final_ans = [nb_sel, th_sel, vd_sel, vdc_sel]
                    # Lời giải tương ứng (ở đây danh sách list_x_2 chỉ có 1 phần tử nên dùng chung hoặc mở rộng nếu cần)
                    # Để đơn giản và đúng logic, ta gán trực tiếp lời giải chi tiết
                    final_sol = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]
                    break

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' +
                str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(final_ans[0]) + '}\n'
                '{' + str(final_ans[1]) + '}\n'
                '{' + str(final_ans[2]) + '}\n'
                '{' + str(final_ans[3]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(final_sol[0]) + '\n'
                '\\item ' + str(final_sol[1]) + '\n'
                '\\item ' + str(final_sol[2]) + '\n'
                '\\item ' + str(final_sol[3]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


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


def bt_dang10_p2_b3_c4_ds11(self):
            # Khai báo biến
            # --- KHAI BÁO BIẾN ---
            x = symbols('x')

            # --- SINH HỆ SỐ NGẪU NHIÊN CHO f(x) ---
            # f_tren = (sqrt(a_f*x + b_f) - c_f) / (x^2 - 4)
            a_f = random.randint(2, 6)
            c_f = random.randint(1, 3)
            # Để lim x->2 tồn tại, ta chọn b_f sao cho tử bằng 0 tại x=2
            b_f = c_f**2 - 2*a_f 

            p_f = random.randint(1, 5)
            q_f = random.randint(-5, 5)
            r_f = random.randint(2, 5)

            # --- SINH HỆ SỐ NGẪU NHIÊN CHO g(x) ---
            # g_tren = (sqrt(x + m_g) - n_g) / (2 - x)
            m_g = random.randint(2, 10)
            n_g = int(math.sqrt(2 + m_g))
            if n_g**2 != (2 + m_g): # Đảm bảo số chính phương để biểu thức đẹp
                m_g = 7; n_g = 3

            u_g = random.randint(-5, 5)
            v_g = random.randint(2, 6)

            # Biểu thức Sympy để tính toán
            f_tren = (sqrt(a_f*x + b_f) - c_f) / (x**2 - 4)
            f_duoi = (p_f*x + q_f) / r_f
            g_tren = (sqrt(x + m_g) - n_g) / (2 - x)
            g_duoi = (u_g - x) / v_g

            # --- TÍNH TOÁN TOÁN HỌC ---
            # f(x) tại x=2
            val_f_2 = simplify(f_duoi.subs(x, 2))
            lim_f_right = limit(f_tren, x, 2, dir='+')
            is_f_cont = (lim_f_right == val_f_2)

            # g(x) tại x=2
            val_g_2 = simplify(g_duoi.subs(x, 2))
            lim_g_right = limit(g_tren, x, 2, dir='+')
            is_g_cont = (lim_g_right == val_g_2)

            # Hàm thương f/g tại x=2
            is_div_cont = is_f_cont and is_g_cont and (val_g_2 != 0)

            # Nội dung câu hỏi
            noidungcauhoi = r'''Cho các hàm số $f(x) = \begin{cases} %s & \text{khi } x > 2 \\ %s & \text{khi } x \le 2 \end{cases}$ và $g(x) = \begin{cases} %s & \text{khi } x > 2 \\ %s & \text{khi } x \le 2 \end{cases}$.''' % (
                latex(f_tren), latex(f_duoi), latex(g_tren), latex(g_duoi)
            )

            # --- KHỞI TẠO CÁC ĐÁP ÁN VÀ LỜI GIẢI ---

            # 1. Nhận biết: Tính liên tục của f(x)
            nb_da_1_d = r'\True Hàm số $f(x)$ liên tục tại điểm $x_0 = 2$' if is_f_cont else r'\True Hàm số $f(x)$ gián đoạn tại điểm $x_0 = 2$'
            nb_da_1_s = r'Hàm số $f(x)$ gián đoạn tại điểm $x_0 = 2$' if is_f_cont else r'Hàm số $f(x)$ liên tục tại điểm $x_0 = 2$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            loigiai_nb_1 = r'''Ta có $f(2) = %s$; $\lim_{x \to 2^-} f(x) = %s$. \\ 
            $\lim_{x \to 2^+} f(x) = \lim_{x \to 2^+} %s = %s$. \\ 
            Vì $\lim_{x \to 2^+} f(x) %s f(2)$ nên hàm số $f(x)$ %s tại $x_0 = 2$.''' % (
                latex(val_f_2), latex(val_f_2), latex(f_tren), latex(lim_f_right),
                '=' if is_f_cont else r'\neq', 'liên tục' if is_f_cont else 'gián đoạn'
            )

            # 2. Thông hiểu: Giới hạn của g(x)
            th_da_1_d = r'\True Giới hạn bên phải của hàm số $g(x)$ tại $x=2$ bằng $%s$' % latex(lim_g_right)
            th_da_1_s = r'Giới hạn bên phải của hàm số $g(x)$ tại $x=2$ bằng $%s$' % latex(lim_g_right + Rational(1, 2))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            loigiai_th_1 = r'''Ta có $\lim_{x \to 2^+} g(x) = \lim_{x \to 2^+} %s = %s$.''' % (latex(g_tren), latex(lim_g_right))

            # 3. Vận dụng: Tính liên tục của g(x)
            vd_da_1_d = r'\True Hàm số $g(x)$ liên tục tại điểm $x_0 = 2$' if is_g_cont else r'\True Hàm số $g(x)$ gián đoạn tại điểm $x_0 = 2$'
            vd_da_1_s = r'Hàm số $g(x)$ gián đoạn tại điểm $x_0 = 2$' if is_g_cont else r'Hàm số $g(x)$ liên tục tại điểm $x_0 = 2$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            loigiai_vd_1 = r'''Ta có $g(2) = %s$ và $\lim_{x \to 2^+} g(x) = %s$. \\ 
            Vì $\lim_{x \to 2} g(x) %s g(2)$ nên hàm số $g(x)$ %s tại $x_0 = 2$.''' % (
                latex(val_g_2), latex(lim_g_right), '=' if is_g_cont else r'\neq', 'liên tục' if is_g_cont else 'gián đoạn'
            )

            # 4. Vận dụng cao: Tính liên tục của hàm thương
            vdc_da_1_d = r'\True Hàm số $y = \frac{f(x)}{g(x)}$ liên tục tại điểm $x_0 = 2$' if is_div_cont else r'\True Hàm số $y = \frac{f(x)}{g(x)}$ gián đoạn tại điểm $x_0 = 2$'
            vdc_da_1_s = r'Hàm số $y = \frac{f(x)}{g(x)}$ gián đoạn tại điểm $x_0 = 2$' if is_div_cont else r'Hàm số $y = \frac{f(x)}{g(x)}$ liên tục tại điểm $x_0 = 2$'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            loigiai_vdc_1 = r'''Vì $f(x)$ %s tại $x=2$, $g(x)$ %s tại $x=2$ và $g(2) = %s %s 0$ nên hàm số $y = \frac{f(x)}{g(x)}$ %s tại $x_0 = 2$.''' % (
                'liên tục' if is_f_cont else 'gián đoạn',
                'liên tục' if is_g_cont else 'gián đoạn',
                latex(val_g_2), r'\neq' if val_g_2 != 0 else '=',
                'liên tục' if is_div_cont else 'gián đoạn'
            )

            # --- LẶP ĐẾN KHI CÓ 1 ĐẾN 3 ĐÁP ÁN ĐÚNG ---
            def count_true_answers(ans_list):
                return sum('\\True' in ans for ans in ans_list)

            while True:
                nb_da = random.choice(list_nb_da_1)
                th_da = random.choice(list_th_da_1)
                vd_da = random.choice(list_vd_da_1)
                vdc_da = random.choice(list_vdc_da_1)

                if 1 <= count_true_answers([nb_da, th_da, vd_da, vdc_da]) <= 3:
                    break

            # --- XUẤT NỘI DUNG THEO MẪU LATEX ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(nb_da) + '}\n'
                '{' + str(th_da) + '}\n'
                '{' + str(vd_da) + '}\n'
                '{' + str(vdc_da) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


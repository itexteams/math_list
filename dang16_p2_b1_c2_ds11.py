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


def bt_dang16_p2_b1_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến và chọn tham số ngẫu nhiên
            ten = random.choice(['An', 'Bình', 'Cường', 'Dũng', 'Mai'])
            A = random.choice([2, 3, 4, 5])  # Số tiền gửi hàng tháng (triệu đồng)
            r_pct = random.choice([0.5, 0.6, 0.8, 1.0])  # Lãi suất hàng tháng (%)
            r = r_pct / 100.0

            r_str = str(r_pct).replace('.', ',')
            base = 1 + r
            base_str = f"{base:.3f}".rstrip('0').rstrip('.').replace('.', ',')

            S1 = A
            S2 = A * base + A
            coef = A / r
            coef_int = int(coef) if coef.is_integer() else coef
            coef_str = str(coef_int).replace('.', ',')

            S12 = coef * (base**12 - 1)
            T = S12 * base

            S1_str = str(S1)
            S2_str = f"{S2:.2f}".replace('.', ',')
            S2_w_str = f"{S2 + 0.15:.2f}".replace('.', ',')

            coef_w = coef + random.choice([50, 100, -50])
            coef_w_str = str(int(coef_w) if coef_w.is_integer() else coef_w).replace('.', ',')

            S12_str = f"{S12:.2f}".replace('.', ',')
            S12_w_str = f"{S12 - 1.25:.2f}".replace('.', ',')

            T_str = f"{T:.2f}".replace('.', ',')
            T_w_str = f"{T + 1.15:.2f}".replace('.', ',')

            # Nội dung câu hỏi
            noidungcauhoi = ('''Tài khoản tiết kiệm cố định: Ngày đầu tiên của mỗi tháng (từ tháng 1 đến tháng 12), %s gửi vào ngân hàng %s triệu đồng. Ngân hàng áp dụng lãi suất cố định %s\\%%/tháng (lãi nhập gốc cuối mỗi tháng). Gọi $S_n$ (đơn vị: triệu đồng) là tổng số tiền có trong tài khoản tiết kiệm ngay sau khi %s gửi tiền ở tháng thứ $n$ ($1 \\le n \\le 12$).'''
                             % (ten, A, r_str, ten))

            ########################################################################
            # Nhận biết ############################################
            nb_da_1_d = '\\True Ngay sau khi gửi tiền ở tháng thứ nhất và tháng thứ hai, số tiền trong tài khoản lần lượt là $S_1 = %s$ triệu đồng và $S_2 = %s$ triệu đồng' % (S1_str, S2_str)
            nb_da_1_s = 'Ngay sau khi gửi tiền ở tháng thứ nhất và tháng thứ hai, số tiền trong tài khoản lần lượt là $S_1 = %s$ triệu đồng và $S_2 = %s$ triệu đồng' % (S1_str, S2_w_str)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = ('''Ngay sau khi gửi tiền ở tháng thứ nhất, số tiền trong tài khoản là $S_1 = %s$ (triệu đồng). \\\\
            Cuối tháng thứ nhất, số tiền $S_1$ sinh lãi $%s \\cdot %s\\%% = %s$ (triệu đồng). \\\\
            Ngay sau khi gửi thêm $%s$ triệu đồng ở đầu tháng thứ hai, tổng số tiền là $S_2 = %s \\cdot (1 + %s\\%%) + %s = %s$ (triệu đồng).'''
                            % (S1_str, S1_str, r_str, f"{S1 * r:.4f}".replace('.', ','), A, S1_str, r_str, A, S2_str))

            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            th_da_1_d = '\\True Công thức tổng quát của $S_n$ theo $n$ là $S_n = %s \\left( %s^n - 1 \\right)$ (triệu đồng) và $(S_n)$ là dãy số tăng' % (coef_str, base_str)
            th_da_1_s = 'Công thức tổng quát của $S_n$ theo $n$ là $S_n = %s \\left( %s^n - 1 \\right)$ (triệu đồng) và $(S_n)$ là dãy số tăng' % (coef_w_str, base_str)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            loigiai_th_1 = ('''Số tiền trong tài khoản ngay sau khi gửi ở tháng thứ $n$ lập thành tổng của cấp số nhân có số hạng đầu $u_1 = %s$ và công bội $q = %s$. \\\\
            Tổng số tiền là: $S_n = %s + %s \\cdot %s + \\dots + %s \\cdot %s^{n-1} = %s \\cdot \\frac{%s^n - 1}{%s - 1} = %s \\left( %s^n - 1 \\right)$ (triệu đồng). \\\\
            Vì $S_{n+1} - S_n = %s \\cdot %s^n > 0, \\forall n \\ge 1$ nên $(S_n)$ là dãy số tăng.'''
                            % (A, base_str, A, A, base_str, A, base_str, A, base_str, base_str, coef_str, base_str, A, base_str))

            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng ############################################
            vd_da_1_d = '\\True Tổng số tiền %s có trong tài khoản tiết kiệm ngay sau khi gửi tiền ở tháng thứ $12$ là khoảng %s triệu đồng' % (ten, S12_str)
            vd_da_1_s = 'Tổng số tiền %s có trong tài khoản tiết kiệm ngay sau khi gửi tiền ở tháng thứ $12$ là khoảng %s triệu đồng' % (ten, S12_w_str)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = ('''Thay $n = 12$ vào công thức tổng quát của $S_n$, ta được: \\\\
            $S_{12} = %s \\left( %s^{12} - 1 \\right) \\approx %s$ (triệu đồng).'''
                            % (coef_str, base_str, S12_str))

            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao ############################################
            vdc_da_1_d = '\\True Đến cuối tháng thứ $12$, nếu %s rút toàn bộ tiền trong tài khoản (bao gồm tiền lãi tháng $12$) thì số tiền nhận được là khoảng %s triệu đồng' % (ten, T_str)
            vdc_da_1_s = 'Đến cuối tháng thứ $12$, nếu %s rút toàn bộ tiền trong tài khoản (bao gồm tiền lãi tháng $12$) thì số tiền nhận được là khoảng %s triệu đồng' % (ten, T_w_str)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = ('''Cuối tháng thứ $12$, số tiền $S_{12}$ sinh thêm lãi cho cả tháng thứ $12$. \\\\
            Tổng số tiền %s nhận được khi rút toàn bộ vào cuối tháng thứ $12$ là: \\\\
            $T = S_{12} \\cdot (1 + %s\\%%) = %s \\cdot %s \\approx %s$ (triệu đồng).'''
                             % (ten, r_str, S12_str, base_str, T_str))

            list_vdc_2 = [loigiai_vdc_1]

            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 đúng
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            list_nb_1 = [nb_da_1]
            list_th_1 = [th_da_1]
            list_vd_1 = [vd_da_1]
            list_vdc_1 = [vdc_da_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            combined_th = list(zip(list_th_1, list_th_2))
            combined_vd = list(zip(list_vd_1, list_vd_2))
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            random.shuffle(combined_nb)
            random.shuffle(combined_th)
            random.shuffle(combined_vd)
            random.shuffle(combined_vdc)

            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
            str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
               '{'+str(shuffled_answers_nb[0])+'}\n'
               '{'+str(shuffled_answers_th[0])+'}\n'
               '{'+str(shuffled_answers_vd[0])+'}\n'
               '{'+str(shuffled_answers_vdc[0])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions_nb[0])+'\n'
                '\\item '+str(shuffled_solutions_th[0])+'\n'
                '\\item '+str(shuffled_solutions_vd[0])+'\n'
                '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


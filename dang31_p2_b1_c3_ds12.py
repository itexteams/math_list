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


def bt_dang31_p2_b1_c3_ds12(self):
                # --- BƯỚC 1: KHAI BÁO BIẾN VÀ RANDOM ---
                t = symbols('t')
                T_days = random.choice([200, 300, 400, 500]) 
                b_val = random.choice([2, 4, 6])
                a_val = b_val * T_days
                unit_price = random.choice([300000, 400000, 500000])

                m_t = a_val - b_val * t
                M_t_func = integrate(m_t, t)
                M_T_val = M_t_func.subs(t, T_days)
                total_cost = M_T_val * unit_price

                # --- BƯỚC 2: NỘI DUNG CÂU HỎI ---
                noidungcauhoi = (r'''Đối với các dự án xây dựng, chi phí nhân công lao động được tính theo số ngày công. Gọi $m(t)$ là số lượng công nhân được sử dụng ở ngày thứ $t$ (kể từ khi khởi công dự án). Gọi $M(t)$ là số ngày công được tính đến hết ngày thứ $t$. Trong kinh tế xây dựng, người ta đã biết rằng $M'(t) = m(t)$. Một công trình xây dựng dự kiến hoàn thành trong %s ngày. Số lượng công nhân được sử dụng cho bởi hàm số $m(t) = %s$, trong đó $t$ tính theo ngày ($0 \le t \le %s$), $m(t)$ tính theo người. Đơn giá cho một ngày công lao động là %s đồng.''' 
                                 % (T_days, latex(m_t), T_days, unit_price))

                # --- BƯỚC 3: CÁC ĐÁP ÁN VÀ LỜI GIẢI ---
                # NHẬN BIẾT
                nb_da_1_d = r'\True $M(t)$ là một nguyên hàm của hàm số $m(t) = %s$' % latex(m_t)
                nb_da_1_s = r'$m(t)$ là một nguyên hàm của hàm số $M(t)$ trên đoạn $[0;%s]$ ' % T_days
                list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
                loigiai_nb_1 = 'Vì $M\'(t) = m(t)$ nên $M(t)$ là một nguyên hàm của hàm số $m(t)$.'

                # THÔNG HIỂU
                th_da_1_d = r'\True Công thức tính số ngày công đến hết ngày $t$ là $M(t) = %s$' % latex(M_t_func)
                th_da_1_s = r'Công thức tính số ngày công đến hết ngày $t$ là $M(t) = %s + %s$' % (latex(M_t_func), T_days)
                list_th_da_1 = [th_da_1_d, th_da_1_s]
                loigiai_th_1 = r'Ta có $M(t) = \int (%s) \text{d}t = %s + C$. Vì $M(0)=0 \Rightarrow C=0$. Vậy $M(t) = %s$.' % (latex(m_t), latex(M_t_func), latex(M_t_func))

                # VẬN DỤNG
                vd_da_1_d = r'\True Tổng số ngày công được tính đến khi hoàn thành công trình là %s' % M_T_val
                vd_da_1_s = r'Tổng số ngày công được tính đến khi hoàn thành công trình là %s' % (M_T_val + 1000)
                list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
                loigiai_vd_1 = r'Số ngày công tính đến ngày thứ %s là $M(%s) = %s \cdot %s - %s^2 = %s$.' % (T_days, T_days, a_val, T_days, T_days, M_T_val)

                # VẬN DỤNG CAO
                vdc_da_1_d = r'\True Chi phí nhân công lao động đến lúc hoàn thành là %s đồng' % total_cost
                vdc_da_1_s = r'Chi phí nhân công lao động đến lúc hoàn thành là %s đồng' % (M_T_val * unit_price * 1.1)
                list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
                loigiai_vdc_1 = r'Tổng chi phí = Đơn giá $\times$ Tổng số ngày công = %s $\times$ %s = %s (đồng).' % (unit_price, M_T_val, total_cost)

                # --- BƯỚC 4: LẶP ĐỂ CHỌN ĐÁP ÁN (1-3 ĐÚNG) ---
                def count_true_answers(answers):
                    return sum('\\True' in ans for ans in answers)

                while True:
                    nb_da = random.choice(list_nb_da_1)
                    th_da = random.choice(list_th_da_1)
                    vd_da = random.choice(list_vd_da_1)
                    vdc_da = random.choice(list_vdc_da_1)
                    answers = [nb_da, th_da, vd_da, vdc_da]
                    if 1 <= count_true_answers(answers) <= 3:
                        break

                # --- BƯỚC 5: XUẤT NỘI DUNG ---
                shuffled_answers = [nb_da, th_da, vd_da, vdc_da]
                shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

                content = ('\\begin{minipage}{\\textwidth} \n'
                           '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
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


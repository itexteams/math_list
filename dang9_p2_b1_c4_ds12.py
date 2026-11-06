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


def bt_dang9_p2_b1_c4_ds12(self):
            # Khai báo biến
            # Khai báo các hàm bổ trợ
            def nCr(n, r):
                f = math.factorial
                return f(n) // f(r) // f(n-r)

            # Hàm chuyển đổi dấu chấm thành dấu phẩy cho số thập phân
            def f_str(val):
                return str(val).replace('.', ',')

            # --- BƯỚC 1: NGẪU NHIÊN HÓA DỮ LIỆU ---
            rate = random.choice([60, 65, 70, 75, 80])
            p_val = rate / 100
            q_val = round(1 - p_val, 2)
            n_val = 3 

            # Tính toán các giá trị xác suất
            prob_a = round(p_val**3, 3)
            prob_b = round(1 - prob_a, 3)
            prob_c = round(nCr(3, 1) * (p_val**1) * (q_val**2), 3)
            prob_d = round(nCr(3, 2) * (p_val**2) * (q_val**1), 3)

            threshold_d = 0.45 

            # Chuyển đổi các giá trị sang định dạng dấu phẩy để hiển thị
            p_s = f_str(p_val)
            q_s = f_str(q_val)
            pa_s = f_str(prob_a)
            pb_s = f_str(prob_b)
            pc_s = f_str(prob_c)
            pd_s = f_str(prob_d)
            td_s = f_str(threshold_d)

            # --- BƯỚC 2: NỘI DUNG CÂU HỎI ---
            noidungcauhoi = ('''Một nghiên cứu tại một trường đại học cho biết tỉ lệ sinh viên dùng cà phê để duy trì tỉnh táo khi học vào ban đêm là %s\\%%. Giả sử chọn ngẫu nhiên %s sinh viên từ nhóm khảo sát trên để phỏng vấn.''' 
                             %(rate, n_val))

            ########################################################################
            # a) Nhận biết
            ########################################################################
            da_a_d = '\\True Xác suất để cả 3 sinh viên đều dùng cà phê để duy trì tỉnh táo là %s' %(pa_s)
            da_a_s = 'Xác suất để cả 3 sinh viên đều dùng cà phê để duy trì tỉnh táo là %s' %(f_str(round(prob_a + 0.012, 3)))
            list_a = [da_a_d, da_a_s]

            loigiai_nb_1 = ('''Xác suất thành công (sinh viên dùng cà phê): $p = %s\\%% = %s$. \\\\
            Xác suất thất bại (sinh viên không dùng cà phê): $q = 1 - %s = %s$. \\\\
            Gọi $X$ là số sinh viên dùng cà phê trong %s sinh viên được chọn. $X$ tuân theo phân phối nhị thức $B(n=%s, p=%s)$. \\\\
            Xác suất để cả 3 sinh viên đều dùng cà phê là trường hợp $X = 3$: \\\\
            $P(X=3) = C_{%s}^{%s} \\cdot p^{%s} \\cdot q^{%s-%s} = 1 \\cdot %s^{3} \\cdot %s^{0} = %s$.'''
                            %(rate, p_s, p_s, q_s, n_val, n_val, p_s, n_val, n_val, n_val, n_val, n_val, p_s, q_s, pa_s))

            ########################################################################
            # b) Thông hiểu
            ########################################################################
            da_b_d = '\\True Xác suất trong 3 sinh viên có ít nhất 1 sinh viên không dùng cà phê là %s' %(pb_s)
            da_b_s = 'Xác suất trong 3 sinh viên có ít nhất 1 sinh viên không dùng cà phê là %s' %(f_str(round(prob_b - 0.05, 3)))
            list_b = [da_b_d, da_b_s]

            loigiai_th_1 = ('''Biến cố "ít nhất 1 sinh viên không dùng cà phê" là biến cố đối của biến cố "cả 3 sinh viên đều dùng cà phê". \\\\
            Ta có: $P = 1 - P(X=3) = 1 - %s = %s$.'''
                            %(pa_s, pb_s))

            ########################################################################
            # c) Vận dụng
            ########################################################################
            da_c_d = '\\True Xác suất trong 3 sinh viên có đúng 1 sinh viên dùng cà phê là %s' %(pc_s)
            da_c_s = 'Xác suất trong 3 sinh viên có đúng 1 sinh viên dùng cà phê là %s' %(f_str(round(prob_c + 0.02, 3)))
            list_c = [da_c_d, da_c_s]

            loigiai_vd_1 = ('''Trường hợp này tương ứng với $X = 1$. Áp dụng công thức Bernoulli: \\\\
            $P(X=1) = C_{3}^{1} \\cdot p^{1} \\cdot q^{3-1} = 3 \\cdot %s^{1} \\cdot %s^{2} = %s$.'''
                            %(p_s, q_s, pc_s))

            ########################################################################
            # d) Vận dụng cao
            ########################################################################
            if prob_d > threshold_d:
                da_d_d = '\\True Xác suất trong 3 sinh viên có đúng 2 sinh viên dùng cà phê và 1 sinh viên không dùng cà phê lớn hơn %s' %(td_s)
                da_d_s = 'Xác suất trong 3 sinh viên có đúng 2 sinh viên dùng cà phê và 1 sinh viên không dùng cà phê nhỏ hơn %s' %(td_s)
            else:
                da_d_d = '\\True Xác suất trong 3 sinh viên có đúng 2 sinh viên dùng cà phê và 1 sinh viên không dùng cà phê nhỏ hơn %s' %(td_s)
                da_d_s = 'Xác suất trong 3 sinh viên có đúng 2 sinh viên dùng cà phê và 1 sinh viên không dùng cà phê lớn hơn %s' %(td_s)

            list_d = [da_d_d, da_d_s]
            so_sanh_latex = ">" if prob_d > threshold_d else "<"

            loigiai_vdc_1 = ('''Trường hợp này tương ứng với $X = 2$. Áp dụng công thức Bernoulli: \\\\
            $P(X=2) = C_{3}^{2} \\cdot p^{2} \\cdot q^{3-2} = 3 \\cdot %s^{2} \\cdot %s^{1} = %s$. \\\\
            So sánh với giá trị đề bài: $%s %s %s$.'''
                             %(p_s, q_s, pd_s, pd_s, so_sanh_latex, td_s))

            # --- BƯỚC 3: KIỂM TRA SỐ CÂU ĐÚNG VÀ XUẤT NỘI DUNG ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                dap_an_a = random.choice(list_a)
                dap_an_b = random.choice(list_b)
                dap_an_c = random.choice(list_c)
                dap_an_d = random.choice(list_d)
                current_answers = [dap_an_a, dap_an_b, dap_an_c, dap_an_d]
                if 1 <= count_true_answers(current_answers) <= 3:
                    break

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(dap_an_a) + '}\n'
                '{' + str(dap_an_b) + '}\n'
                '{' + str(dap_an_c) + '}\n'
                '{' + str(dap_an_d) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


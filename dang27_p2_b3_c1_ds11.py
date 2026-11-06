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


def bt_dang27_p2_b3_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            t = symbols('t')

            # Random các tham số cho bài toán thực tế tương đương
            A = random.choice([25, 30, 35])   # Chiều cao trục tâm vòng quay
            B = random.choice([15, 20, 25])   # Bán kính vòng quay
            M = random.choice([20, 25, 30])   # Tham số thời gian mẫu ở mẫu số góc (Chu kỳ quay sẽ là 2*M)

            chu_ky_dung = 2 * M
            chu_ky_sai = M

            max_h = A + B
            min_h = A - B

            # Các tính toán phục vụ ý c (Tính h(t) tại t = 175/6 khi M=25)
            # Tổng quát tính toán đồng bộ theo tham số ngẫu nhiên bằng SymPy
            t_c = Rational(7 * M, 1) if M != 25 else Rational(175, 6)
            # Tính góc phi = pi*t/M + pi/3
            goc_c = pi * t_c / M + pi / 3
            val_sin_c = sin(goc_c)
            h_c_val = A + B * val_sin_c

            # Tính toán cho ý d: Đạt độ cao H_d lần đầu tiên
            # Chọn độ cao H_d bằng đúng chiều cao trục quay A
            H_d = A 
            # h(t) = A + B*sin(pi*t/M + pi/3) = A <=> sin(pi*t/M + pi/3) = 0
            # Nghiệm đầu tiên t > 0 là pi*t/M + pi/3 = pi <=> pi*t/M = 2*pi/3 <=> t = 2*M/3
            t_d_dung = Rational(2 * M, 3)
            t_d_sai = Rational(1 * M, 2)

            # Định dạng hiển thị số thập phân cho chuỗi kết quả nếu là số bán nguyên
            t_d_dung_str = str(float(t_d_dung)).replace('.', ',') if t_d_dung.q == 2 else latex(t_d_dung)

            # Nội dung câu hỏi chính
            noidungcauhoi = ('''Chiều cao $h\\,(\\text{m})$ của một cabin trên vòng quay vào thời điểm $t$ giây sau khi bắt đầu chuyển động được cho bởi công thức $h(t) = %s + %s\\sin\\left( \\frac{\\pi t}{%s} + \\frac{\\pi}{3} \\right)$.''' 
                             %(latex(A), latex(B), latex(M)))

            ########################################################################
            # Nhận biết (Ý a) ############################################
            nb_da_1_d = '\\True Chu kỳ tuần hoàn của chuyển động là %s\\text{s}' %(latex(chu_ky_dung))
            nb_da_1_s = 'Chu kỳ tuần hoàn của chuyển động là %s\\text{s}' %(latex(chu_ky_sai))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = ('''Hàm số $y = \\sin(\\omega t + \\varphi)$ có chu kỳ tuần hoàn được tính theo công thức $T = \\frac{2\\pi}{\\omega}$.\\\\'''
                            '''Ở đây, hệ số góc $\\omega = \\frac{\\pi}{%s}$, do đó chu kỳ của chuyển động bằng: $T = \\frac{2\\pi}{\\frac{\\pi}{%s}} = %s\\,\\text{giây}$.'''
                            %(latex(M), latex(M), latex(chu_ky_dung)))

            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu (Ý b) ############################################
            th_da_1_d = '\\True Chiều cao lớn nhất của cabin là %s\\text{m}' %(latex(max_h))
            th_da_1_s = 'Chiều cao lớn nhất của cabin là %s\\text{m}' %(latex(A))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            loigiai_th_1 = ('''Vì ta luôn có $-1 \\le \\sin\\left( \\frac{\\pi t}{%s} + \\frac{\\pi}{3} \\right) \\le 1$ nên:\\\\'''
                            '''$h(t) \\le %s + %s \\cdot 1 = %s\\,\\text{m}$.\\\\'''
                            '''Dấu bằng xảy ra khi hàm $\\sin$ đạt giá trị bằng $1$. Do đó, chiều cao lớn nhất của cabin đạt được là %s\\text{m}.'''
                            %(latex(M), latex(A), latex(B), latex(max_h), latex(max_h)))

            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## 
            # Vận dụng (Ý c) ############################################
            h_c_str = str(float(h_c_val)).replace('.', ',').rstrip('0').rstrip(',') if h_c_val.is_Float else latex(h_c_val)
            vd_da_1_d = '\\True Tại thời điểm $t = %s$ giây thì chiều cao cabin bằng $%s\\text{m}$' %(latex(t_c), h_c_str)
            vd_da_1_s = 'Tại thời điểm $t = %s$ giây thì chiều cao cabin bằng $%s\\text{m}$' %(latex(t_c), latex(min_h))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = ('''Thay giá trị thời điểm $t = %s$ vào công thức hàm số lượng giác $h(t)$, ta có:\\\\'''
                            '''$h\\left( %s \\right) = %s + %s\\sin\\left( \\frac{\\pi \\cdot %s}{%s} + \\frac{\\pi}{3} \\right) = %s + %s\\sin\\left( %s \\right) = %s\\,\\text{m}$.'''
                            %(latex(t_c), latex(t_c), latex(A), latex(B), latex(t_c), latex(M), latex(A), latex(B), latex(goc_c), h_c_str))

            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## 
            # Vận dụng cao (Ý d) ############################################
            vdc_da_1_d = '\\True Sau $%s$ giây thì cabin đạt độ cao $%s\\,\\text{m}$ lần đầu tiên' %(latex(t_d_dung), latex(H_d))
            vdc_da_1_s = 'Sau $%s$ giây thì cabin đạt độ cao $%s\\,\\text{m}$ lần đầu tiên' %(latex(t_d_sai), latex(H_d))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = ('''Để tìm thời điểm đạt độ cao %s\\,m lần đầu tiên, ta giải phương trình $h(t) = %s$:\\\\'''
                             '''$%s + %s\\sin\\left( \\frac{\\pi t}{%s} + \\frac{\\pi}{3} \\right) = %s \\Leftrightarrow \\sin\\left( \\frac{\\pi t}{%s} + \\frac{\\pi}{3} \\right) = 0$\\\\'''
                             '''$\\Leftrightarrow \\frac{\\pi t}{%s} + \\frac{\\pi}{3} = k\\pi \\Leftrightarrow \\frac{\\pi t}{%s} = -\\frac{\\pi}{3} + k\\pi \\Leftrightarrow t = -\\frac{%s}{3} + k%s$ ($k \\in \\mathbb{Z}$).\\\\'''
                             '''Yêu cầu thời gian lần đầu tiên sau khi chuyển động nên ta tìm nghiệm dương $t$ nhỏ nhất.\\\\'''
                             '''Xét $k = 1 \\Rightarrow t = -\\frac{%s}{3} + %s = \\frac{2 \\cdot %s}{3} = %s\\,\\text{giây}$. Khẳng định thời gian này là đúng.'''
                             %(latex(H_d), latex(H_d), latex(A), latex(B), latex(M), latex(H_d), latex(M), latex(M), latex(M), latex(M), latex(M), latex(M), latex(M), latex(M), t_d_dung_str))

            list_vdc_2 = [loigiai_vdc_1]

            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Vòng lặp kiểm tra để đảm bảo số lượng đáp án đúng nằm trong khoảng từ 1 đến 3
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Thiết lập lại danh sách sau khi lọc thỏa mãn điều kiện
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

            # Xuất câu hỏi và lời giải chi tiết theo đúng định dạng mẫu khung chương trình đề ra
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
            str(noidungcauhoi)+ 
                '\\choiceTFn \n'
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


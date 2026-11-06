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


def bt_dang9_p2_b4_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Random tham số bài toán: Cho phương trình tan(2x + beta) = 1
            # Góc beta được chọn ngẫu nhiên để tạo ra nhiều câu hỏi khác nhau
            beta = random.choice([-30, -15, 15, 30])

            # Do tan(...) = 1 <=> góc trong bằng 45 + k*180
            # => 2x + beta = 45 + k*180 => 2x = (45 - beta) + k*180 => x = (45 - beta)/2 + k*90
            # Tính giá trị góc ban đầu cho nghiệm x
            goc_bandau = Rational(45 - beta, 2)

            # Tìm nghiệm âm lớn nhất và các nghiệm trong khoảng (-180; 90)
            # Duyệt k từ -5 đến 5 để lọc nghiệm
            nghiem_list = []
            for k_val in range(-5, 6):
                val_x = goc_bandau + k_val * 90
                nghiem_list.append(val_x)

            # 1. Nghiệm âm lớn nhất (các nghiệm < 0, chọn số lớn nhất)
            nghiem_am = [v for v in nghiem_list if v < 0]
            nghiem_am_lon_nhat = max(nghiem_am)

            # 2. Các nghiệm thuộc khoảng (-180; 90)
            nghiem_khoang = [v for v in nghiem_list if -180 < v < 90]
            tong_nghiem = sum(nghiem_khoang)
            nghiem_lon_nhat_khoang = max(nghiem_khoang)

            # Định dạng chuỗi hiển thị góc beta trong đề bài
            beta_str = '%s' % latex(2*x)
            if beta < 0:
                beta_str += ' - %s^\\circ' % latex(abs(beta))
            else:
                beta_str += ' + %s^\\circ' % latex(beta)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho phương trình lượng giác $\\tan\\left( %s \\right) = 1$ (*). ''' 
                             %(beta_str))

            ########################################################################
            # Nhận biết ############################################
            # Ý a: Phương trình (*) có họ nghiệm tổng quát
            nb_da_1_d = '\\True Phương trình (*) có nghiệm $x = %s^\\circ + k90^\\circ$ ($k \\in \\mathbb{Z}$)' %(latex(goc_bandau).replace('.', ','))
            nb_da_1_s = 'Phương trình (*) có nghiệm $x = 45^\\circ + k180^\\circ$ ($k \\in \\mathbb{Z}$)'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = ('''Ta có $\\tan\\left( %s \\right) = 1 \\Leftrightarrow 2x + %s^\\circ = 45^\\circ + k180^\\circ$\\\\'''
                            '''$\\Leftrightarrow 2x = %s^\\circ + k180^\\circ \\Leftrightarrow x = %s^\\circ + k90^\\circ$ ($k \\in \\mathbb{Z}$).'''
                            %(beta_str, latex(beta), latex(45 - beta), latex(goc_bandau).replace('.', ',')))

            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            # Ý b: Nghiệm âm lớn nhất của phương trình
            th_da_1_d = '\\True Phương trình có nghiệm âm lớn nhất bằng $%s^\\circ$' %(latex(nghiem_am_lon_nhat).replace('.', ','))
            th_da_1_s = 'Phương trình có nghiệm âm lớn nhất bằng $-45^\\circ$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            loigiai_th_1 = ('''Từ họ nghiệm $x = %s^\\circ + k90^\\circ$ ($k \\in \\mathbb{Z}$), xét điều kiện $x < 0$:\\\\'''
                            '''$%s^\\circ + k90^\\circ < 0 \\Leftrightarrow k < -\\frac{%s}{90}$.\\\\'''
                            '''Do $k \\in \\mathbb{Z}$ nên giá trị $k$ lớn nhất thỏa mãn là giá trị nguyên ngay trước đó.\\\\'''
                            '''Thay giá trị $k$ tương ứng vào ta tìm được nghiệm âm lớn nhất bằng $%s^\\circ$.'''
                            %(latex(goc_bandau).replace('.', ','), latex(goc_bandau).replace('.', ','), latex(goc_bandau).replace('.', ','), latex(nghiem_am_lon_nhat).replace('.', ',')))

            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## 
            # Vận dụng ############################################
            # Ý c: Tổng các nghiệm của phương trình trong khoảng (-180; 90)
            vd_da_1_d = '\\True Tổng các nghiệm của phương trình trong khoảng $(-180^\\circ; 90^\\circ)$ bằng $%s^\\circ$' %(latex(tong_nghiem).replace('.', ','))
            vd_da_1_s = 'Tổng các nghiệm của phương trình trong khoảng $(-180^\\circ; 90^\\circ)$ bằng $180^\\circ$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            # Biểu diễn các nghiệm cụ thể để chèn vào lời giải
            nghiem_str_list = [('%s^\\circ' % latex(v).replace('.', ',')) for v in nghiem_khoang]
            loigiai_vd_1 = ('''Xét các nghiệm thuộc khoảng $(-180^\\circ; 90^\\circ)$, ta có: $-180^\\circ < %s^\\circ + k90^\\circ < 90^\\circ$.\\\\'''
                            '''Giải bất phương trình trên với $k \\in \\mathbb{Z}$, ta tìm được các nghiệm cụ thể là: %s.\\\\'''
                            '''Tổng các nghiệm này bằng: $%s = %s^\\circ$.'''
                            %(latex(goc_bandau).replace('.', ','), ', '.join(['$%s$' % s for s in nghiem_str_list]), ' + '.join(['%s^\\circ' % latex(v).replace('.', ',') for v in nghiem_khoang]), latex(tong_nghiem).replace('.', ',')))

            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## 
            # Vận dụng cao ############################################
            # Ý d: Nghiệm lớn nhất trong khoảng (-180; 90)
            vdc_da_1_d = '\\True Trong khoảng $(-180^\\circ; 90^\\circ)$ phương trình có nghiệm lớn nhất bằng $%s^\\circ$' %(latex(nghiem_lon_nhat_khoang).replace('.', ','))
            vdc_da_1_s = 'Trong khoảng $(-180^\\circ; 90^\\circ)$ phương trình có nghiệm lớn nhất bằng $90^\\circ$'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = ('''Từ các nghiệm đã liệt kê trong khoảng $(-180^\\circ; 90^\\circ)$ ở bước trước,\\\\'''
                             '''ta so sánh và rút ra giá trị lớn nhất trong số các nghiệm đó.\\\\'''
                             '''Vậy nghiệm lớn nhất thỏa mãn yêu cầu bài toán bằng $%s^\\circ$.'''
                             %(latex(nghiem_lon_nhat_khoang).replace('.', ',')))

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


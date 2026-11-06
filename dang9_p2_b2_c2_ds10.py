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


def bt_dang9_p2_b2_c2_ds10(self):
            # Khai báo biến
            # Cấu hình sẵn các bộ thông số hợp lệ để đảm bảo bài toán luôn có nghiệm nguyên logic
            configs = [
                {
                    # Cấu hình 1: Giữ nguyên như đề gốc
                    'so_nguoi': 140, 'so_hang': 9, 'max_a': 10, 'max_b': 9,
                    'gia_a': 4, 'gia_b': 3, 'nguoi_a': 20, 'hang_a': "0{,}6", 'nguoi_b': 10, 'hang_b': "1{,}5",
                    'x_min': 5, 'y_min': 4, 't_min': 32,
                    'dinh_toa_do': 'A(10; 2); B(10; 9); C\\left(\\frac{5}{2}; 9\\right); D(5; 4)'
                },
                {
                    # Cấu hình 2: Đảo giá tiền thuê xe A và B (T = 3x + 4y)
                    'so_nguoi': 140, 'so_hang': 9, 'max_a': 10, 'max_b': 9,
                    'gia_a': 3, 'gia_b': 4, 'nguoi_a': 20, 'hang_a': "0{,}6", 'nguoi_b': 10, 'hang_b': "1{,}5",
                    'x_min': 5, 'y_min': 4, 't_min': 31,
                    'dinh_toa_do': 'A(10; 2); B(10; 9); C\\left(\\frac{5}{2}; 9\\right); D(5; 4)'
                },
                {
                    # Cấu hình 3: Nhân đôi quy mô bài toán (Nhu cầu gấp đôi, xe cấp gấp đôi)
                    'so_nguoi': 280, 'so_hang': 18, 'max_a': 20, 'max_b': 18,
                    'gia_a': 4, 'gia_b': 3, 'nguoi_a': 20, 'hang_a': "0{,}6", 'nguoi_b': 10, 'hang_b': "1{,}5",
                    'x_min': 10, 'y_min': 8, 't_min': 64,
                    'dinh_toa_do': 'A(20; 4); B(20; 18); C(5; 18); D(10; 8)'
                }
            ]

            # Random chọn 1 cấu hình từ ma trận
            cfg = random.choice(configs)

            so_nguoi = cfg['so_nguoi']
            so_hang = cfg['so_hang']
            max_a = cfg['max_a']
            max_b = cfg['max_b']
            gia_a = cfg['gia_a']
            gia_b = cfg['gia_b']
            nguoi_a = cfg['nguoi_a']
            hang_a = cfg['hang_a']
            nguoi_b = cfg['nguoi_b']
            hang_b = cfg['hang_b']
            x_min = cfg['x_min']
            y_min = cfg['y_min']
            t_min = cfg['t_min']
            dinh_toa_do = cfg['dinh_toa_do']

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một công ty TNHH trong một đợt quảng cáo và bán khuyến mãi hàng hóa (1 sản phẩm mới của công ty) cần thuê xe để chở trên %s người và trên %s tấn hàng. Nơi thuê chỉ có hai loại xe $A$ và $B$, trong đó xe loại $A$ có %s chiếc, xe loại $B$ có %s chiếc. Một chiếc xe loại $A$ cho thuê với giá %s triệu, loại $B$ giá %s triệu. Hỏi phải thuê bao nhiêu xe mỗi loại để chi phí vận chuyển là thấp nhất. Biết rằng xe $A$ chỉ chở tối đa %s người và %s tấn hàng. Xe $B$ chở tối đa %s người và %s tấn hàng. Gọi $x, y$ lần lượt là số xe loại $A, B$ được thuê.''' % (so_nguoi, so_hang, max_a, max_b, gia_a, gia_b, nguoi_a, hang_a, nguoi_b, hang_b))

            ######################################################################## Nhận biết ############################################

            # Các đáp án
            nb_da_1_d = '\\True Chi phí thuê xe theo $x, y$ là $T = %sx + %sy$' % (gia_a, gia_b)
            nb_da_1_s = 'Chi phí thuê xe theo $x, y$ là $T = %sx + %sy$' % (gia_b, gia_a)
            list_nb_da_1=[nb_da_1_d, nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Gọi $x$ là số xe loại $A(0 \\le x \\le %s; x \\in \\mathbb{N})$, $y$ là số xe loại $B(0 \\le y \\le %s; y \\in \\mathbb{N})$. Khi đó tổng chi phí thuê xe là $T = %sx + %sy$.''' % (max_a, max_b, gia_a, gia_b))
            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################

            # Các đáp án
            th_da_1_d = '\\True Tổng số người tối đa mà 2 xe chở được theo $x, y$ là $%sx + %sy$' % (nguoi_a, nguoi_b)
            th_da_1_s = 'Tổng số người tối đa mà 2 xe chở được theo $x, y$ là $%sx + %sy$' % (nguoi_b, nguoi_a)
            list_th_da_1=[th_da_1_d, th_da_1_s]
            th_da_1=random.choice(list_th_da_1)
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Xe $A$ chở tối đa %s người, xe $B$ chở tối đa %s người nên tổng số người 2 xe chở tối đa được là $%sx + %sy$.''' % (nguoi_a, nguoi_b, nguoi_a, nguoi_b))
            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################

            # Các đáp án
            vd_da_1_d = '\\True Tổng số tấn hàng tối đa mà 2 xe chở được theo $x, y$ là $%sx + %sy$' % (hang_a, hang_b)
            vd_da_1_s = 'Tổng số tấn hàng tối đa mà 2 xe chở được theo $x, y$ là $6x + 15y$'
            list_vd_da_1=[vd_da_1_d, vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Xe $A$ chở được %s tấn hàng, xe $B$ chở được %s tấn hàng nên tổng lượng hàng 2 xe chở được là $%sx + %sy$.''' % (hang_a, hang_b, hang_a, hang_b))
            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################

            # Các đáp án
            vdc_da_1_d = '\\True Để chi phí thuê xe là nhỏ nhất thì $\\begin{cases} x = %s \\\\ y = %s \\end{cases}$' % (x_min, y_min)
            vdc_da_1_s = 'Để chi phí thuê xe là nhỏ nhất thì $\\begin{cases} x = %s \\\\ y = %s \\end{cases}$' % (x_min + 1, y_min + 1)
            list_vdc_da_1=[vdc_da_1_d, vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Theo giả thiết, ta có $\\begin{cases} 0 \\le x \\le %s \\\\ 0 \\le y \\le %s \\\\ %sx + %sy \\ge %s \\\\ %sx + %sy \\ge %s \\end{cases} (*)$ \\\\
            Biểu diễn miền nghiệm của hệ bất phương trình $(*)$ là tứ giác $ABCD$ kể cả miền trong của tứ giác. \\\\
            Biểu thức $T = %sx + %sy$ đạt giá trị nhỏ nhất tại một trong các đỉnh của tứ giác $ABCD$. \\\\
            Tại các đỉnh $%s$, ta thấy $T$ đạt giá trị nhỏ nhất khi $\\begin{cases} x = %s \\\\ y = %s \\end{cases}$. \\\\
            Khi đó $T_{\\min} = %s$.''' % (max_a, max_b, nguoi_a, nguoi_b, so_nguoi, hang_a, hang_b, so_hang, gia_a, gia_b, dinh_toa_do, x_min, y_min, t_min))

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

            # Gán lại vào list
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
                str(noidungcauhoi)+ '\n'
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
                '\\end{ex}\n\\end{minipage}\n\n')
            return content


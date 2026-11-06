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


def bt_dang12_p2_b4_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Random tham số: Thay đổi hệ số của cos(x) từ 2 đến 4 (Bài gốc b = 3)
            b = randint(2, 4)

            # Tính toán giá trị chặn cho ý c: sin 2x + b*cos x = cos x * (2*sin x + b)
            # Giá trị lớn nhất của hàm số này luôn nhỏ hơn b + 1
            chan_tren = b + 1

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hàm số lượng giác $f(x) = \\sin 2x + %s\\cos x$.''' 
                             %(latex(b)))

            ########################################################################
            # Nhận biết ############################################
            # Ý a: Chu kỳ tuần hoàn của sin 2x là pi, của b*cos x là 2pi. Chu kỳ chung là 2pi
            nb_da_1_d = '\\True Hàm số đã cho có chu kỳ tuần hoàn $2\\pi$'
            nb_da_1_s = 'Hàm số đã cho có chu kỳ tuần hoàn $\\pi$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = ('''Thành phần $y = \\sin 2x$ tuần hoàn với chu kỳ $T_1 = \\frac{2\\pi}{2} = \\pi$.\\\\'''
                            '''Thành phần $y = %s\\cos x$ tuần hoàn với chu kỳ $T_2 = 2\\pi$.\\\\'''
                            '''Chu kỳ tuần hoàn nhỏ nhất của hàm số $f(x)$ là bội chung nhỏ nhất của $T_1$ và $T_2$, tức là $T = 2\\pi$. Khẳng định này đúng.'''
                            %(latex(b)))

            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            # Ý b: Hàm số biểu thị qua cos x và sin x là bậc hai: f(x) = 2 sin x cos x + b cos x (đây là bậc hai đối với sin x, cos x)
            th_da_1_d = 'Hàm số không thể biểu thị theo hàm số bậc hai của $\\cos x, \\sin x$'
            th_da_1_s = '\\True Hàm số có thể biểu thị theo hàm số bậc hai của $\\cos x, \\sin x$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            loigiai_th_1 = ('''Sử dụng công thức nhân đôi ta có: $\\sin 2x = 2\\sin x \\cos x$.\\\\'''
                            '''Biểu thức hàm số trở thành: $f(x) = 2\\sin x \\cos x + %s\\cos x$.\\\\'''
                            '''Đây là biểu thức bậc hai đối với các hàm số lượng giác $\\sin x$ và $\\cos x$. Do đó khẳng định không thể biểu thị theo hàm số bậc hai là khẳng định sai.'''
                            %(latex(b)))

            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## 
            # Vận dụng ############################################
            # Ý c: f(x) < b + 1, với mọi x (Bài gốc b = 3 nên f(x) < 4, \forall x)
            vd_da_1_d = '\\True $f(x) < %s, \\forall x$' %(latex(chan_tren))
            vd_da_1_s = '$f(x) \\ge %s, \\forall x$' %(latex(chan_tren))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = ('''Ta có $f(x) = \\cos x (2\\sin x + %s)$.\\\\'''
                            '''Áp dụng bất đẳng thức Bunhiacốpki hoặc đánh giá biên độ:\\\\'''
                            '''Ta luôn có $\\cos x \\le 1$ và $\\sin x \\le 1$, tuy nhiên dấu bằng của chúng không đồng thời xảy ra.\\\\'''
                            '''Cụ thể, giá trị lớn nhất của hàm số đạt được luôn luôn nhỏ hơn tuyệt đối $1 \\cdot (2 \\cdot 1 + %s) = %s$.\\\\'''
                            '''Do đó, khẳng định $f(x) < %s, \\forall x$ là khẳng định đúng.'''
                            %(latex(b), latex(b), latex(chan_tren), latex(chan_tren)))

            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## 
            # Vận dụng cao ############################################
            # Ý d: Phương trình f(x) = 0 <=> cos x (2 sin x + b) = 0. Vì b >= 2 nên 2 sin x + b = 0 vô nghiệm => cos x = 0 <=> x = pi/2 + k*pi
            # Trong khoảng (0; pi), nghiệm duy nhất là x = pi/2 -> Phương trình có đúng 1 nghiệm
            vdc_da_1_d = '\\True Phương trình $f(x) = 0$ có $1$ nghiệm trong khoảng $(0; \\pi)$'
            vdc_da_1_s = 'Phương trình $f(x) = 0$ có $2$ nghiệm trong khoảng $(0; \\pi)$'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = ('''Xét phương trình: $f(x) = 0 \\Leftrightarrow \\sin 2x + %s\\cos x = 0 \\Leftrightarrow 2\\sin x \\cos x + %s\\cos x = 0$\\\\'''
                             '''$\\Leftrightarrow \\cos x (2\\sin x + %s) = 0 \\Leftrightarrow \\left[ \\begin{aligned} &\\cos x = 0 \\\\ &\\sin x = -\\frac{%s}{2} \\end{aligned} \\right.$\\\\'''
                             '''Vì $%s \\ge 2$ nên $-\\frac{%s}{2} \\le -1$. Phương trình $\\sin x = -\\frac{%s}{2}$ vô nghiệm hoặc có nghiệm chạm biên nếu $%s = 2$.\\\\'''
                             '''Tuy nhiên trong khoảng mở $(0; \\pi)$, ta luôn có $\\sin x > 0$, nên phương trình dưới vô nghiệm hoàn toàn.\\\\'''
                             '''Xét phương trình $\\cos x = 0 \\Leftrightarrow x = \\frac{\\pi}{2} + k\\pi$ ($k \\in \\mathbb{Z}$).\\\\'''
                             '''Trong khoảng $(0; \\pi)$, ta chỉ nhận duy nhất một nghiệm $x = \\frac{\\pi}{2}$ (ứng với $k=0$).\\\\'''
                             '''Vậy phương trình có đúng $1$ nghiệm trong khoảng $(0; \\pi)$. Khẳng định này đúng.'''
                             %(latex(b), latex(b), latex(b), latex(b), latex(b), latex(b), latex(b), latex(b)))

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


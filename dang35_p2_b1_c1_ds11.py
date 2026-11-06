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


def bt_dang35_p2_b1_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            alpha = symbols('alpha')

            # B3-Suy nghĩ tìm cách random bài toán
            # Ta random khoảng của góc alpha giữa góc phần tư thứ I và thứ II
            # Case 1: 0 < alpha < pi/2 (Góc phần tư thứ I) -> sin alpha > 0, cos alpha > 0, tan alpha > 0
            # Case 2: pi/2 < alpha < pi (Góc phần tư thứ II) -> sin alpha > 0, cos alpha < 0, tan alpha < 0
            case_alpha = random.choice([1, 2])

            if case_alpha == 1:
                str_khoang = "0 < \\alpha < \\frac{\\pi}{2}"

                # a) A = cos(alpha + pi) = -cos(alpha) < 0 -> ĐÚNG
                nb_da_1_d = '\\True $A = \\cos(\\alpha + \\pi) < 0$'
                nb_da_1_s = '$A = \\cos(\\alpha + \\pi) > 0$'
                loigiai_nb_1 = ('''Vì $0 < \\alpha < \\frac{\\pi}{2}$ nên $\\cos \\alpha > 0$.\\\\
            Ta có $A = \\cos(\\alpha + \\pi) = -\\cos \\alpha$. Do $\\cos \\alpha > 0$ nên $-\\cos \\alpha < 0$.\\\\
            Vậy $A < 0$.''')

                # b) B = tan(alpha - pi) = tan(alpha) > 0 -> ĐÚNG
                th_da_1_d = '\\True $B = \\tan(\\alpha - \\pi) > 0$'
                th_da_1_s = '$B = \\tan(\\alpha - \\pi) < 0$'
                loigiai_th_1 = ('''Vì $0 < \\alpha < \\frac{\\pi}{2}$ nên $\\tan \\alpha > 0$.\\\\
            Ta có $B = \\tan(\\alpha - \\pi) = \\tan \\alpha$. Do $\\tan \\alpha > 0$ nên $B > 0$.''')

                # c) C = sin(alpha + 2pi/5) 
                # 0 < alpha < pi/2 => 2pi/5 < alpha + 2pi/5 < pi/2 + 2pi/5 = 9pi/10
                # Vì 2pi/5 và 9pi/10 đều thuộc khoảng (0; pi) nên sin(alpha + 2pi/5) > 0 -> ĐÚNG là > 0, trong ảnh ghi < 0 là SAI
                vd_da_1_s = '$C = \\sin\\left( \\alpha + \\frac{2\\pi}{5} \\right) < 0$'
                vd_da_1_d = '\\True $C = \\sin\\left( \\alpha + \\frac{2\\pi}{5} \\right) > 0$'
                loigiai_vd_1 = ('''Vì $0 < \\alpha < \\frac{\\pi}{2} \\Leftrightarrow \\frac{2\\pi}{5} < \\alpha + \\frac{2\\pi}{5} < \\frac{9\\pi}{10}$.\\\\
            Do khoảng $\\left( \\frac{2\\pi}{5}; \\frac{9\\pi}{10} \\right)$ nằm hoàn toàn trong góc phần tư thứ I và thứ II (khoảng $(0; \\pi)$), nên giá trị của sin luôn dương.\\\\
            Vậy $C = \\sin\\left( \\alpha + \\frac{2\\pi}{5} \\right) > 0$.''')

                # d) D = cos(alpha - 3pi/8)
                # 0 < alpha < pi/2 => -3pi/8 < alpha - 3pi/8 < pi/2 - 3pi/8 = pi/8
                # Khoảng (-3pi/8; pi/8) nằm trong (-pi/2; pi/2) nên cos luôn dương. Trong ảnh ghi < 0 là SAI
                vdc_da_1_s = '$D = \\cos\\left( \\alpha - \\frac{3\\pi}{8} \\right) < 0$'
                vdc_da_1_d = '\\True $D = \\cos\\left( \\alpha - \\frac{3\\pi}{8} \\right) > 0$'
                loigiai_vdc_1 = ('''Vì $0 < \\alpha < \\frac{\\pi}{2} \\Leftrightarrow -\\frac{3\\pi}{8} < \\alpha - \\frac{3\\pi}{8} < \\frac{\\pi}{8}$.\\\\
            Do khoảng $\\left( -\\frac{3\\pi}{8}; \\frac{\\pi}{8} \\right)$ nằm hoàn toàn trong cung $\\left( -\\frac{\\pi}{2}; \\frac{\\pi}{2} \\right)$ thuộc góc phần tư thứ IV và thứ I, nên giá trị của cos luôn dương.\\\\
            Vậy $D = \\cos\\left( \\alpha - \\frac{3\\pi}{8} \\right) > 0$.''')

            else:
                str_khoang = "\\frac{\\pi}{2} < \\alpha < \\pi"

                # a) A = cos(alpha + pi) = -cos(alpha) -> do cos alpha < 0 nên -cos alpha > 0
                nb_da_1_d = '\\True $A = \\cos(\\alpha + \\pi) > 0$'
                nb_da_1_s = '$A = \\cos(\\alpha + \\pi) < 0$'
                loigiai_nb_1 = ('''Vì $\\frac{\\pi}{2} < \\alpha < \\pi$ nên $\\cos \\alpha < 0$.\\\\
            Ta có $A = \\cos(\\alpha + \\pi) = -\\cos \\alpha$. Do $\\cos \\alpha < 0$ nên $-\\cos \\alpha > 0$.\\\\
            Vậy $A > 0$.''')

                # b) B = tan(alpha - pi) = tan(alpha) -> do tan alpha < 0 nên B < 0
                th_da_1_d = '\\True $B = \\tan(\\alpha - \\pi) < 0$'
                th_da_1_s = '$B = \\tan(\\alpha - \\pi) > 0$'
                loigiai_th_1 = ('''Vì $\\frac{\\pi}{2} < \\alpha < \\pi$ nên $\\tan \\alpha < 0$.\\\\
            Ta có $B = \\tan(\\alpha - \\pi) = \\tan \\alpha$. Do $\\tan \\alpha < 0$ nên $B < 0$.''')

                # c) C = sin(alpha + 2pi/5)
                # pi/2 < alpha < pi => pi/2 + 2pi/5 < alpha + 2pi/5 < pi + 2pi/5 <=> 9pi/10 < alpha + 2pi/5 < 14pi/10
                # Khoảng này đi qua pi nên dấu của sin có thể âm hoặc dương (chưa xác định dấu cố định trên cả khoảng), ta đổi sang biểu thức khác dễ xét hơn:
                # Để thuận tiện, đổi sang C = sin(alpha - pi/2) = -cos(alpha) > 0
                vd_da_1_d = '\\True $C = \\sin\\left( \\alpha - \\frac{\\pi}{2} \\right) > 0$'
                vd_da_1_s = '$C = \\sin\\left( \\alpha - \\frac{\\pi}{2} \\right) < 0$'
                loigiai_vd_1 = ('''Vì $\\frac{\\pi}{2} < \\alpha < \\pi$ nên $\\cos \\alpha < 0$.\\\\
            Áp dụng công thức biến đổi, ta có $C = \\sin\\left( \\alpha - \\frac{\\pi}{2} \\right) = -\\cos \\alpha$.\\\\
            Do $\\cos \\alpha < 0$ nên $-\\cos \\alpha > 0$. Vậy $C > 0$.''')

                # d) D = cos(alpha + pi/2) = -sin(alpha). Vì sin alpha > 0 nên -sin alpha < 0
                vdc_da_1_d = '\\True $D = \\cos\\left( \\alpha + \\frac{\\pi}{2} \\right) < 0$'
                vdc_da_1_s = '$D = \\cos\\left( \\alpha + \\frac{\\pi}{2} \\right) > 0$'
                loigiai_vdc_1 = ('''Vì $\\frac{\\pi}{2} < \\alpha < \\pi$ nên $\\sin \\alpha > 0$.\\\\
            Áp dụng công thức biến đổi cung hơn kém, ta có $D = \\cos\\left( \\alpha + \\frac{\\pi}{2} \\right) = -\\sin \\alpha$.\\\\
            Do $\\sin \\alpha > 0$ nên $-\\sin \\alpha < 0$. Vậy $D < 0$.''')

            # Đưa các đáp án ban đầu vào list lựa chọn ngẫu nhiên
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            # Nội dung câu hỏi sử dụng định dạng %s theo yêu cầu bắt buộc
            noidungcauhoi = ('''Cho $%s$. Xét tính đúng – sai của các mệnh đề sau:''' % (str_khoang))

            list_nb_1 = [random.choice(list_nb_da_1)]
            list_th_1 = [random.choice(list_th_da_1)]
            list_vd_1 = [random.choice(list_vd_da_1)]
            list_vdc_1 = [random.choice(list_vdc_da_1)]

            list_nb_2 = [loigiai_nb_1]
            list_th_2 = [loigiai_th_1]
            list_vd_2 = [loigiai_vd_1]
            list_vdc_2 = [loigiai_vdc_1]

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

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án tổng hợp có từ 1 đến 3 đúng
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán lại vào list sau khi thỏa mãn số lượng đáp án đúng
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

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn qua toán tử ép kiểu và nối chuỗi
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


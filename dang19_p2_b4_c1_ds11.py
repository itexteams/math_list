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


def bt_dang19_p2_b4_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            case = random.choice([1, 2])

            if case == 1:
                str_ve_phai = "-\\frac{\\sqrt{3}}{2}"
                alpha = Rational(-1, 3) # -pi/3
                str_alpha = "-\\frac{\\pi}{3}"
                # Họ nghiệm 1: 3x + pi/3 = -pi/3 + k2pi <=> 3x = -2pi/3 + k2pi <=> x = -2pi/9 + k2pi/3
                # Họ nghiệm 2: 3x + pi/3 = pi - (-pi/3) + k2pi <=> 3x = pi + k2pi <=> x = pi/3 + k2pi/3
                # (Trong ảnh gốc câu a họ nghiệm 1 ghi -pi/9 là SAI, họ nghiệm đúng phải là -2pi/9)
                str_nghiem_a_dung = "\\True Phương trình có nghiệm $\\left[\\begin{aligned} & x = -\\frac{2\\pi}{9} + k\\frac{2\\pi}{3} \\\\ & x = \\frac{\\pi}{3} + k\\frac{2\\pi}{3} \\end{aligned}\\right. (k \\in \\mathbb{Z})$"
                str_nghiem_a_sai = "Phương trình có nghiệm $\\left[\\begin{aligned} & x = -\\frac{\\pi}{9} + k\\frac{2\\pi}{3} \\\\ & x = \\frac{\\pi}{3} + k\\frac{2\\pi}{3} \\end{aligned}\\right. (k \\in \\mathbb{Z})$"

                # Nghiệm âm lớn nhất: Họ 1 với k=0 là -2pi/9. Họ 2 với k=0 là pi/3, k=-1 là -pi/3. Do -2pi/9 > -pi/3 nên max âm là -2pi/9
                str_max_am_dung = "\\True Phương trình có nghiệm âm lớn nhất bằng $-\\frac{2\\pi}{9}$"
                str_max_am_sai = "Phương trình có nghiệm âm lớn nhất bằng $-\\frac{\\pi}{9}$"

                # Xét nghiệm trên (0; pi/2)
                # Họ 1: 0 < -2/9 + 2k/3 < 1/2 <=> 2/9 < 2k/3 < 13/18 <=> 1/3 < k < 13/12 => k = 1 => x = 4pi/9
                # Họ 2: 0 < 1/3 + 2k/3 < 1/2 <=> -1/3 < 2k/3 < 1/6 <=> -1/2 < k < 1/4 => k = 0 => x = pi/3 = 3pi/9
                # Số nghiệm bằng 2
                str_so_nghiem_dung = "\\True Trên khoảng $\\left(0; \\frac{\\pi}{2}\\right)$ phương trình đã cho có $2$ nghiệm"
                str_so_nghiem_sai = "Trên khoảng $\\left(0; \\frac{\\pi}{2}\\right)$ phương trình đã cho có $3$ nghiệm"

                # Tổng các nghiệm: 4pi/9 + 3pi/9 = 7pi/9
                str_tong_nghiem_dung = "\\True Tổng các nghiệm của phương trình trong khoảng $\\left(0; \\frac{\\pi}{2}\\right)$ bằng $\\frac{7\\pi}{9}$"
                str_tong_nghiem_sai = "Tổng các nghiệm của phương trình trong khoảng $\\left(0; \\frac{\\pi}{2}\\right)$ bằng $\\frac{5\\pi}{9}$"

            else:
                str_ve_phai = "-\\frac{1}{2}"
                alpha = Rational(-1, 6) # -pi/6
                str_alpha = "-\\frac{\\pi}{6}"
                # Họ nghiệm 1: 3x + pi/3 = -pi/6 + k2pi <=> 3x = -pi/2 + k2pi <=> x = -pi/6 + k2pi/3
                # Họ nghiệm 2: 3x + pi/3 = pi - (-pi/6) + k2pi <=> 3x = 5pi/6 + k2pi <=> x = 5pi/18 + k2pi/3
                str_nghiem_a_dung = "\\True Phương trình có nghiệm $\\left[\\begin{aligned} & x = -\\frac{\\pi}{6} + k\\frac{2\\pi}{3} \\\\ & x = \\frac{5\\pi}{18} + k\\frac{2\\pi}{3} \\end{aligned}\\right. (k \\in \\mathbb{Z})$"
                str_nghiem_a_sai = "Phương trình có nghiệm $\\left[\\begin{aligned} & x = -\\frac{\\pi}{18} + k\\frac{2\\pi}{3} \\\\ & x = \\frac{5\\pi}{18} + k\\frac{2\\pi}{3} \\end{aligned}\\right. (k \\in \\mathbb{Z})$"

                # Nghiệm âm lớn nhất: Họ 1 k=0 là -pi/6. Họ 2 k=0 là 5pi/18, k=-1 là -7pi/18. Do -pi/6 = -3pi/18 > -7pi/18 nên max âm là -pi/6
                str_max_am_dung = "\\True Phương trình có nghiệm âm lớn nhất bằng $-\\frac{\\pi}{6}$"
                str_max_am_sai = "Phương trình có nghiệm âm lớn nhất bằng $-\\frac{\\pi}{18}$"

                # Xét nghiệm trên (0; pi/2)
                # Họ 1: 0 < -1/6 + 2k/3 < 1/2 <=> 1/6 < 2k/3 < 2/3 <=> 1/4 < k < 1 => k không có giá trị nguyên
                # Họ 2: 0 < 5/18 + 2k/3 < 1/2 <=> -5/18 < 2k/3 < 2/18 <=> -5/12 < k < 1/6 => k = 0 => x = 5pi/18
                # Số nghiệm bằng 1
                str_so_nghiem_dung = "\\True Trên khoảng $\\left(0; \\frac{\\pi}{2}\\right)$ phương trình đã cho có $1$ nghiệm"
                str_so_nghiem_sai = "Trên khoảng $\\left(0; \\frac{\\pi}{2}\\right)$ phương trình đã cho có $2$ nghiệm"

                # Tổng các nghiệm: 5pi/18
                str_tong_nghiem_dung = "\\True Tổng các nghiệm của phương trình trong khoảng $\\left(0; \\frac{\\pi}{2}\\right)$ bằng $\\frac{5\\pi}{18}$"
                str_tong_nghiem_sai = "Tổng các nghiệm của phương trình trong khoảng $\\left(0; \\frac{\\pi}{2}\\right)$ bằng $\\frac{7\\pi}{18}$"

            # Nội dung câu hỏi sử dụng định dạng %s theo yêu cầu bắt buộc
            noidungcauhoi = ('''Cho phương trình lượng giác $\\sin\\left( 3x + \\frac{\\pi}{3} \\right) = %s$.''' % (str_ve_phai))

            ########################################################################
            # Nhận biết ############################################
            list_nb_da_1 = [str_nghiem_a_dung, str_nghiem_a_sai]
            nb_da_1 = random.choice(list_nb_da_1)
            list_nb_1 = [nb_da_1]

            if case == 1:
                loigiai_nb_1 = ('''Ta có: $\\sin\\left( 3x + \\frac{\\pi}{3} \\right) = -\\frac{\\sqrt{3}}{2} \\Leftrightarrow \\sin\\left( 3x + \\frac{\\pi}{3} \\right) = \\sin\\left( -\\frac{\\pi}{3} \\right)$ \\\\
            $\\Leftrightarrow \\left[\\begin{aligned} & 3x + \\frac{\\pi}{3} = -\\frac{\\pi}{3} + k2\\pi \\\\ & 3x + \\frac{\\pi}{3} = \\pi - \\left( -\\frac{\\pi}{3} \\right) + k2\\pi \\end{aligned}\\right. \\Leftrightarrow \\left[\\begin{aligned} & 3x = -\\frac{2\\pi}{3} + k2\\pi \\\\ & 3x = \\pi + k2\\pi \\end{aligned}\\right. \\Leftrightarrow \\left[\\begin{aligned} & x = -\\frac{2\\pi}{9} + k\\frac{2\\pi}{3} \\\\ & x = \\frac{\\pi}{3} + k\\frac{2\\pi}{3} \\end{aligned}\\right. (k \\in \\mathbb{Z})$.''')
            else:
                loigiai_nb_1 = ('''Ta có: $\\sin\\left( 3x + \\frac{\\pi}{3} \\right) = -\\frac{1}{2} \\Leftrightarrow \\sin\\left( 3x + \\frac{\\pi}{3} \\right) = \\sin\\left( -\\frac{\\pi}{6} \\right)$ \\\\
            $\\Leftrightarrow \\left[\\begin{aligned} & 3x + \\frac{\\pi}{3} = -\\frac{\\pi}{6} + k2\\pi \\\\ & 3x + \\frac{\\pi}{3} = \\pi - \\left( -\\frac{\\pi}{6} \\right) + k2\\pi \\end{aligned}\\right. \\Leftrightarrow \\left[\\begin{aligned} & 3x = -\\frac{\\pi}{2} + k2\\pi \\\\ & 3x = \\frac{5\\pi}{6} + k2\\pi \\end{aligned}\\right. \\Leftrightarrow \\left[\\begin{aligned} & x = -\\frac{\\pi}{6} + k\\frac{2\\pi}{3} \\\\ & x = \\frac{5\\pi}{18} + k\\frac{2\\pi}{3} \\end{aligned}\\right. (k \\in \\mathbb{Z})$.''')

            list_nb_2 = [loigiai_nb_1]
            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            list_th_da_1 = [str_max_am_dung, str_max_am_sai]
            th_da_1 = random.choice(list_th_da_1)
            list_th_1 = [th_da_1]

            if case == 1:
                loigiai_th_1 = ('''Từ các họ nghiệm của phương trình, ta tìm các nghiệm âm lớn nhất: \\\\
            - Với họ nghiệm $x = -\\frac{2\\pi}{9} + k\\frac{2\\pi}{3}$, nghiệm âm lớn nhất ứng với $k=0$ là $x = -\\frac{2\\pi}{9}$. \\\\
            - Với họ nghiệm $x = \\frac{\\pi}{3} + k\\frac{2\\pi}{3}$, nghiệm âm lớn nhất ứng với $k=-1$ là $x = -\\frac{\\pi}{3}$. \\\\
            So sánh hai giá trị, ta thấy $-\\frac{2\\pi}{9} > -\\frac{\\pi}{3}$. Vậy nghiệm âm lớn nhất của phương trình là $-\\frac{2\\pi}{9}$.''')
            else:
                loigiai_th_1 = ('''Từ các họ nghiệm của phương trình, ta tìm các nghiệm âm lớn nhất: \\\\
            - Với họ nghiệm $x = -\\frac{\\pi}{6} + k\\frac{2\\pi}{3}$, nghiệm âm lớn nhất ứng với $k=0$ là $x = -\\frac{\\pi}{6}$. \\\\
            - Với họ nghiệm $x = \\frac{5\\pi}{18} + k\\frac{2\\pi}{3}$, nghiệm âm lớn nhất ứng với $k=-1$ là $x = -\\frac{7\\pi}{18}$. \\\\
            So sánh hai giá trị, ta thấy $-\\frac{\\pi}{6} > -\\frac{7\\pi}{18}$. Vậy nghiệm âm lớn nhất của phương trình là $-\\frac{\\pi}{6}$.''')

            list_th_2 = [loigiai_th_1]
            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng ############################################
            list_vd_da_1 = [str_so_nghiem_dung, str_so_nghiem_sai]
            vd_da_1 = random.choice(list_vd_da_1)
            list_vd_1 = [vd_da_1]

            if case == 1:
                loigiai_vd_1 = ('''Xét các nghiệm của phương trình nằm trong khoảng $\\left(0; \\frac{\\pi}{2}\\right)$: \\\\
            - Họ nghiệm thứ nhất: $0 < -\\frac{2\\pi}{9} + k\\frac{2\\pi}{3} < \\frac{\\pi}{2} \\Leftrightarrow \\frac{1}{3} < k < \\frac{13}{12}$. Vì $k \\in \\mathbb{Z}$ nên $k=1$, ta được nghiệm $x = \\frac{4\\pi}{9}$. \\\\
            - Họ nghiệm thứ hai: $0 < \\frac{\\pi}{3} + k\\frac{2\\pi}{3} < \\frac{\\pi}{2} \\Leftrightarrow -\\frac{1}{2} < k < \\frac{1}{4}$. Vì $k \\in \\mathbb{Z}$ nên $k=0$, ta được nghiệm $x = \\frac{\\pi}{3}$. \\\\
            Vậy phương trình đã cho có tất cả $2$ nghiệm trong khoảng đang xét.''')
            else:
                loigiai_vd_1 = ('''Xét các nghiệm của phương trình nằm trong khoảng $\\left(0; \\frac{\\pi}{2}\\right)$: \\\\
            - Họ nghiệm thứ nhất: $0 < -\\frac{\\pi}{6} + k\\frac{2\\pi}{3} < \\frac{\\pi}{2} \\Leftrightarrow \\frac{1}{4} < k < 1$. Vì $k \\in \\mathbb{Z}$ nên không có giá trị $k$ nào thỏa mãn. \\\\
            - Họ nghiệm thứ hai: $0 < \\frac{5\\pi}{18} + k\\frac{2\\pi}{3} < \\frac{\\pi}{2} \\Leftrightarrow -\\frac{5}{12} < k < \\frac{1}{6}$. Vì $k \\in \\mathbb{Z}$ nên $k=0$, ta được nghiệm $x = \\frac{5\\pi}{18}$. \\\\
            Vậy phương trình đã cho có duy nhất $1$ nghiệm trong khoảng đang xét.''')

            list_vd_2 = [loigiai_vd_1]
            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao ############################################
            list_vdc_da_1 = [str_tong_nghiem_dung, str_tong_nghiem_sai]
            vdc_da_1 = random.choice(list_vdc_da_1)
            list_vdc_1 = [vdc_da_1]

            if case == 1:
                loigiai_vdc_1 = ('''Các nghiệm nằm trong khoảng $\\left(0; \\frac{\\pi}{2}\\right)$ tìm được ở câu trước là $x_1 = \\frac{4\\pi}{9}$ và $x_2 = \\frac{\\pi}{3}$. \\\\
            Tổng các nghiệm này bằng: $S = \\frac{4\\pi}{9} + \\frac{\\pi}{3} = \\frac{7\\pi}{9}$.''')
            else:
                loigiai_vdc_1 = ('''Nghiệm duy nhất nằm trong khoảng $\\left(0; \\frac{\\pi}{2}\\right)$ tìm được ở câu trước là $x = \\frac{5\\pi}{18}$. \\\\
            Tổng các nghiệm này chính bằng: $S = \\frac{5\\pi}{18}$.''')

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

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn sử dụng định dạng %s
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


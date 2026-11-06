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


def bt_dang30_p2_b4_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # B3-Suy nghĩ tìm cách random bài toán
            # Ngẫu nhiên hóa góc pha ban đầu (Case 1: pi/3, Case 2: pi/4)
            case_goc = random.choice([1, 2])

            if case_goc == 1:
                str_goc = "\\frac{\\pi}{3}"
                str_x_a = "\\frac{\\pi}{6}"

                # Lời giải chi tiết cho từng câu tương ứng với góc pi/3
                loigiai_nb_1 = ('''Thay $x = \\frac{\\pi}{6}$ vào phương trình ta được:\\\\
            $2\\cos\\left(\\frac{\\pi}{6} + \\frac{\\pi}{3}\\right) - m + 1 = 0 \\Leftrightarrow 2\\cos\\left(\\frac{\\pi}{2}\\right) - m + 1 = 0 \\Leftrightarrow 2 \\cdot 0 - m + 1 = 0 \\Leftrightarrow m = 1$.''')

                th_da_1_d = '\\True Khi $m = 0$ phương trình có tập nghiệm là $\\left\\{ \\frac{\\pi}{3} + k2\\pi; -\\pi + k2\\pi \\mid k \\in \\mathbb{Z} \\right\\}$'
                th_da_1_s = 'Khi $m = 0$ phương trình có tập nghiệm là $\\left\\{ \\frac{\\pi}{6} + k2\\pi; -\\frac{5\\pi}{6} + k2\\pi \\mid k \\in \\mathbb{Z} \\right\\}$'
                loigiai_th_1 = ('''Khi $m = 0$, phương trình trở thành: $2\\cos\\left(x + \\frac{\\pi}{3}\\right) + 1 = 0 \\Leftrightarrow \\cos\\left(x + \\frac{\\pi}{3}\\right) = -\\frac{1}{2} = \\cos\\left(\\frac{2\\pi}{3}\\right)$\\\\
            $\\Leftrightarrow x + \\frac{\\pi}{3} = \\pm\\frac{2\\pi}{3} + k2\\pi \\Leftrightarrow \\left[\\begin{aligned} & x = \\frac{\\pi}{3} + k2\\pi \\\\ & x = -\\pi + k2\\pi \\end{aligned}\\right. (k \\in \\mathbb{Z})$.''')

                str_doan = "[0;6\\pi]"
                str_so_nghiem_d = "6"
                str_so_nghiem_s = "5"
                loigiai_vdc_1 = ('''Khi $m = 1$, phương trình tương đương với: $\\cos\\left(x + \\frac{\\pi}{3}\\right) = 0 \\Leftrightarrow x + \\frac{\\pi}{3} = \\frac{\\pi}{2} + k\\pi \\Leftrightarrow x = \\frac{\\pi}{6} + k\\pi$ ($k \\in \\mathbb{Z}$).\\\\
            Xét điều kiện nghiệm thuộc đoạn $[0; 6\\pi]$, ta có: $0 \\le \\frac{\\pi}{6} + k\\pi \\le 6\\pi \\Leftrightarrow -\\frac{1}{6} \\le k \\le \\frac{35}{6} \\approx 5,83$.\\\\
            Vì $k$ nguyên nên $k \\in \\{0; 1; 2; 3; 4; 5\\}$. Vậy phương trình có đúng $6$ nghiệm.''')

            else:
                str_goc = "\\frac{\\pi}{4}"
                str_x_a = "\\frac{\\pi}{4}"

                loigiai_nb_1 = ('''Thay $x = \\frac{\\pi}{4}$ vào phương trình ta được:\\\\
            $2\\cos\\left(\\frac{\\pi}{4} + \\frac{\\pi}{4}\\right) - m + 1 = 0 \\Leftrightarrow 2\\cos\\left(\\frac{\\pi}{2}\\right) - m + 1 = 0 \\Leftrightarrow 2 \\cdot 0 - m + 1 = 0 \\Leftrightarrow m = 1$.''')

                th_da_1_d = '\\True Khi $m = 0$ phương trình có tập nghiệm là $\\left\\{ \\frac{\\pi}{12} + k2\\pi; -\\frac{11\\pi}{12} + k2\\pi \\mid k \\in \\mathbb{Z} \\right\\}$'
                th_da_1_s = 'Khi $m = 0$ phương trình có tập nghiệm là $\\left\\{ \\frac{\\pi}{4} + k2\\pi; -\\frac{3\\pi}{4} + k2\\pi \\mid k \\in \\mathbb{Z} \\right\\}$'
                loigiai_th_1 = ('''Khi $m = 0$, phương trình trở thành: $2\\cos\\left(x + \\frac{\\pi}{4}\\right) + 1 = 0 \\Leftrightarrow \\cos\\left(x + \\frac{\\pi}{4}\\right) = -\\frac{1}{2} = \\cos\\left(\\frac{2\\pi}{3}\\right)$\\\\
            $\\Leftrightarrow x + \\frac{\\pi}{4} = \\pm\\frac{2\\pi}{3} + k2\\pi \\Leftrightarrow \\left[\\begin{aligned} & x = \\frac{5\\pi}{12} + k2\\pi \\\\ & x = -\\frac{11\\pi}{12} + k2\\pi \\end{aligned}\\right. (k \\in \\mathbb{Z})$.''')

                str_doan = "[0;4\\pi]"
                str_so_nghiem_d = "4"
                str_so_nghiem_s = "3"
                loigiai_vdc_1 = ('''Khi $m = 1$, phương trình tương đương với: $\\cos\\left(x + \\frac{\\pi}{4}\\right) = 0 \\Leftrightarrow x + \\frac{\\pi}{4} = \\frac{\\pi}{2} + k\\pi \\Leftrightarrow x = \\frac{\\pi}{4} + k\\pi$ ($k \\in \\mathbb{Z}$).\\\\
            Xét điều kiện nghiệm thuộc đoạn $[0; 4\\pi]$, ta có: $0 \\le \\frac{\\pi}{4} + k\\pi \\le 4\\pi \\Leftrightarrow -\\frac{1}{4} \\le k \\le \\frac{15}{4} = 3,75$.\\\\
            Vì $k$ nguyên nên $k \\in \\{0; 1; 2; 3\\}$. Vậy phương trình có đúng $4$ nghiệm.''')

            # Nội dung câu hỏi định dạng chuỗi %s
            noidungcauhoi = ('''Cho phương trình lượng giác $2\\cos\\left( x + %s \\right) - m + 1 = 0$, trong đó $m \\in \\mathbb{R}$ là tham số.''' % (str_goc))

            ########################################################################
            # Nhận biết ############################################
            nb_da_1_d = '\\True $%s$ là nghiệm của phương trình khi và chỉ khi $m = 1$' % (str_x_a)
            nb_da_1_s = '$%s$ là nghiệm của phương trình khi và chỉ khi $m = 0$' % (str_x_a)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)
            list_nb_1 = [nb_da_1]
            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)
            list_th_1 = [th_da_1]
            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng ############################################
            vd_da_1_s = 'Tập các giá trị của $m$ để phương trình có nghiệm là $[-1;1]$'
            vd_da_1_d = '\\True Tập các giá trị của $m$ để phương trình có nghiệm là $[-1;3]$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)
            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = ('''Phương trình tương đương với: $\\cos\\left(x + %s\\right) = \\frac{m-1}{2}$.\\\\
            Để phương trình lượng giác cơ bản có nghiệm, ta cần điều kiện:\\\\
            $-1 \\le \\frac{m-1}{2} \\le 1 \\Leftrightarrow -2 \\le m - 1 \\le 2 \\Leftrightarrow -1 \\le m \\le 3$.\\\\
            Vậy tập hợp các giá trị tham số $m$ cần tìm là $[-1;3]$. Khẳng định ghi $[-1;1]$ là sai.''' % (str_goc))
            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao ############################################
            vdc_da_1_d = '\\True Khi $m = 1$ phương trình có %s nghiệm trong đoạn $%s$' % (str_so_nghiem_d, str_doan)
            vdc_da_1_s = 'Khi $m = 1$ phương trình có %s nghiệm trong đoạn $%s$' % (str_so_nghiem_s, str_doan)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)
            list_vdc_1 = [vdc_da_1]
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

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn sử dụng cấu trúc %s
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


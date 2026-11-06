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


def bt_dang15_p2_b4_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Random cấu trúc bài toán lượng giác tương đương
            bo_so = random.choice([1, 2])

            if bo_so == 1:
                # Bài toán gốc
                bt_f_latex = '\\sqrt{3}\\cos 5x - 2\\sin 3x \\cdot \\cos 2x'
                chu_ky_latex = '2\\pi'
                chu_ky_sai_latex = '\\frac{2\\pi}{5}'
                gtln_val = 3
                gtln_latex = '3' # Số nguyên tố
                menh_de_c_dung = '\\True Hàm số đã cho có giá trị lớn nhất là một số nguyên tố'
                menh_de_c_sai = 'Hàm số đã cho có giá trị lớn nhất là một số hợp số'
                # Giải phương trình f(x) = sin x <=> 2cos(5x + pi/6) - sin x = sin x <=> cos(5x + pi/6) = sin x = cos(pi/2 - x)
                # => 5x + pi/6 = pi/2 - x + k2pi <=> 6x = pi/3 + k2pi <=> x = pi/18 + kpi/3
                # hoặc 5x + pi/6 = -pi/2 + x + k2pi <=> 4x = -2pi/3 + k2pi <=> x = -pi/6 + kpi/2
                # Nghiệm dương nhỏ nhất: pi/18. Nghiệm âm lớn nhất: -pi/6
                # Tổng = pi/18 - pi/6 = -2pi/18 = -pi/9
                tong_nghiem_d_latex = '-\\frac{\\pi}{9}'
                tong_nghiem_s_latex = '\\frac{\\pi}{9}'
                pt_d_latex = 'f(x) = \\sin x'
                loigiai_d_bo = ('''Phương trình $f(x) = \\sin x \\Leftrightarrow 2\\cos\\left(5x + \\frac{\\pi}{6}\\right) - \\sin x = \\sin x \\Leftrightarrow \\cos\\left(5x + \\frac{\\pi}{6}\\right) = \\sin x$\\\\'''
                                '''$\\Leftrightarrow \\cos\\left(5x + \\frac{\\pi}{6}\\right) = \\cos\\left(\\frac{\\pi}{2} - x\\right)$\\\\'''
                                '''Thứ nhất: $5x + \\frac{\\pi}{6} = \\frac{\\pi}{2} - x + k2\\pi \\Leftrightarrow 6x = \\frac{\\pi}{3} + k2\\pi \\Leftrightarrow x = \\frac{\\pi}{18} + k\\frac{\\pi}{3}$ ($k \\in \\mathbb{Z}$).\\\\'''
                                '''Thứ hai: $5x + \\frac{\\pi}{6} = -\\frac{\\pi}{2} + x + k2\\pi \\Leftrightarrow 4x = -\\frac{2\\pi}{3} + k2\\pi \\Leftrightarrow x = -\\frac{\\pi}{6} + k\\frac{\\pi}{2}$ ($k \\in \\mathbb{Z}$).\\\\'''
                                '''Từ hai họ nghiệm, ta tìm được nghiệm dương nhỏ nhất là $x = \\frac{\\pi}{18}$ (từ họ 1 với $k=0$) và nghiệm âm lớn nhất là $x = -\\frac{\\pi}{6}$ (từ họ 2 với $k=0$).\\\\'''
                                '''Tổng của nghiệm âm lớn nhất và nghiệm dương nhỏ nhất là: $-\\frac{\\pi}{6} + \\frac{\\pi}{18} = -\\frac{\\pi}{9}$.''')
            else:
                # Biến thể
                bt_f_latex = '\\sin 5x - 2\\sin 3x \\cdot \\cos 2x'
                # sin 5x - (sin 5x + sin x) = -sin x
                chu_ky_latex = '2\\pi'
                chu_ky_sai_latex = '\\pi'
                gtln_latex = '1' # Không phải số nguyên tố
                menh_de_c_dung = 'Hàm số đã cho có giá trị lớn nhất là một số nguyên tố'
                menh_de_c_sai = '\\True Hàm số đã cho có giá trị lớn nhất không phải là một số nguyên tố'
                # Giải phương trình f(x) = -\cos x <=> -sin x = -cos x <=> tan x = 1 <=> x = pi/4 + kpi
                # Nghiệm dương nhỏ nhất: pi/4. Nghiệm âm lớn nhất: -3pi/4
                # Tổng = pi/4 - 3pi/4 = -pi/2
                tong_nghiem_d_latex = '-\\frac{\\pi}{2}'
                tong_nghiem_s_latex = '-\\frac{\\pi}{4}'
                pt_d_latex = 'f(x) = -\\cos x'
                loigiai_d_bo = ('''Phương trình $f(x) = -\\cos x \\Leftrightarrow -\\sin x = -\\cos x \\Leftrightarrow \\tan x = 1 \\Leftrightarrow x = \\frac{\\pi}{4} + k\\pi$ ($k \\in \\mathbb{Z}$).\\\\'''
                                '''Nghiệm dương nhỏ nhất ứng với $k=0$ là $x = \\frac{\\pi}{4}$.\\\\'''
                                '''Nghiệm âm lớn nhất ứng với $k=-1$ là $x = -\\frac{3\\pi}{4}$.\\\\'''
                                '''Tổng của nghiệm âm lớn nhất và nghiệm dương nhỏ nhất là: $\\frac{\\pi}{4} + \\left(-\\frac{3\\pi}{4}\\right) = -\\frac{\\pi}{2}$.''')

            # Nội dung câu hỏi chính
            noidungcauhoi = ('''Cho hàm số $f(x) = %s$.''' %(bt_f_latex))

            ########################################################################
            # Nhận biết ############################################
            nb_da_1_d = '\\True Hàm số đã cho là hàm số lượng giác'
            nb_da_1_s = 'Hàm số đã cho là hàm số đa thức bậc cao'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = (sp.latex('''Hàm số $f(x)$ được cấu thành từ tổng và tích của các hàm số lượng giác cơ bản là sin và cos, do đó $f(x)$ là một hàm số lượng giác.''') if False else '''Hàm số $f(x)$ được cấu thành từ tổng và tích của các hàm số lượng giác cơ bản là sin và cos, do đó $f(x)$ là một hàm số lượng giác.''')

            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            th_da_1_d = 'Hàm số đã cho có chu kỳ tuần hoàn $T = %s$' %(chu_ky_sai_latex)
            th_da_1_s = '\\True Hàm số đã cho có chu kỳ tuần hoàn $T = %s$' %(chu_ky_latex)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            if bo_so == 1:
                loigiai_th_1 = ('''Ta biến đổi tích thành tổng: $2\\sin 3x \\cos 2x = \\sin 5x + \\sin x$.\\\\'''
                                '''Khi đó hàm số được viết gọn lại thành: $f(x) = \\sqrt{3}\\cos 5x - \\sin 5x - \\sin x = 2\\cos\\left(5x + \\frac{\\pi}{6}\\right) - \\sin x$.\\\\'''
                                '''Thành phần $\\cos\\left(5x + \\frac{\\pi}{6}\\right)$ tuần hoàn với chu kỳ $T_1 = \\frac{2\\pi}{5}$.\\\\'''
                                '''Thành phần $\\sin x$ tuần hoàn với chu kỳ $T_2 = 2\\pi$.\\\\'''
                                '''Chu kỳ tuần hoàn chung của hàm số là bội chung nhỏ nhất của $T_1$ và $T_2$, suy ra $T = 2\\pi$. Khẳng định chu kỳ bằng $\\frac{2\\pi}{5}$ là sai.''')
            else:
                loigiai_th_1 = ('''Ta biến đổi tích thành tổng: $2\\sin 3x \\cos 2x = \\sin 5x + \\sin x$.\\\\'''
                                '''Khi đó hàm số được viết gọn lại thành: $f(x) = \\sin 5x - (\\sin 5x + \\sin x) = -\\sin x$.\\\\'''
                                '''Hàm số $y = -\\sin x$ tuần hoàn với chu kỳ $T = 2\\pi$. Khẳng định chu kỳ khác $2\\pi$ là sai.''')

            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## 
            # Vận dụng ############################################
            vd_da_1_d = menh_de_c_dung
            vd_da_1_s = menh_de_c_sai
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            if bo_so == 1:
                loigiai_vd_1 = ('''Ta có $f(x) = 2\\cos\\left(5x + \\frac{\\pi}{6}\\right) - \\sin x$.\\\\'''
                                '''Sử dụng đánh giá trị lớn nhất: $f(x) \\le 2\\left|\\cos\\left(5x + \\frac{\\pi}{6}\\right)\\right| + |\\sin x| \\le 2 \\cdot 1 + 1 = 3$.\\\\'''
                                '''Dấu bằng xảy ra khi $\\cos\\left(5x + \\frac{\\pi}{6}\\right) = 1$ và $\\sin x = -1 \\Leftrightarrow x = -\\frac{\\pi}{2} + k2\\pi$, thay ngược lại thỏa mãn.\\\\'''
                                '''Vậy giá trị lớn nhất của hàm số bằng $3$. Vì $3$ là số nguyên tố nên khẳng định này đúng.''')
            else:
                loigiai_vd_1 = ('''Ta thu gọn được hàm số $f(x) = -\\sin x$.\\\\'''
                                '''Do $-1 \\le \\sin x \\le 1$ nên $-1 \\le -\\sin x \\le 1$. Giá trị lớn nhất của hàm số là $1$.\\\\'''
                                '''Số $1$ theo định nghĩa không phải là số nguyên tố và cũng không phải là hợp số.''')

            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## 
            # Vận dụng cao ############################################
            vdc_da_1_d = '\\True Tổng của nghiệm âm lớn nhất và nghiệm dương nhỏ nhất của phương trình $%s$ là $%s$' %(pt_d_latex, tong_nghiem_d_latex)
            vdc_da_1_s = 'Tổng của nghiệm âm lớn nhất và nghiệm dương nhỏ nhất của phương trình $%s$ là $%s$' %(pt_d_latex, tong_nghiem_s_latex)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = loigiai_d_bo

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


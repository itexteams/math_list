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


def bt_dang24_p2_b4_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # B3-Suy nghĩ tìm cách random bài toán
            # Random hệ số k của góc (kx) để sinh các bài toán tương tự
            k = random.choice([1, 2])

            if k == 1:
                str_f = "4\\cos^2 x - 3"
                str_g = "2\\sin x + 1"
                str_g_x = "2\\sin x + 1"
                str_f_x = "4\\cos^2 x - 3"
                str_diem_x = "\\frac{\\pi}{2}"
                str_diem_y = "3"
                str_chu_ky = "\\pi"
                str_chu_ky_sai = "2\\pi"
                str_khoang = "\\left( -\\frac{\\pi}{2}; \\frac{3\\pi}{2} \\right)"
                so_nghiem_chung = "2"
                so_nghiem_chung_sai = "4"
                loigiai_a = ('''Thay $x = \\frac{\\pi}{2}$ vào hàm số $g(x)$ ta được: $g\\left(\\frac{\\pi}{2}\\right) = 2\\sin\\left(\\frac{\\pi}{2}\\right) + 1 = 2 \\cdot 1 + 1 = 3$.\\\\ Do đó đồ thị hàm số $g(x)$ đi qua điểm $\\left( \\frac{\\pi}{2}; 3 \\right)$.''')
                loigiai_b = ('''Tập xác định $\\mathscr{D} = \\mathbb{R}$. Ta có $f(-x) = 4\\cos^2(-x) - 3 = 4\\cos^2 x - 3 = f(x)$ nên $f(x)$ là hàm số chẵn.\\\\ Hạ bậc hàm số $f(x) = 4 \\cdot \\frac{1 + \\cos 2x}{2} - 3 = 2\\cos 2x - 1$. Hàm số tuần hoàn với chu kỳ $T = \\frac{2\\pi}{2} = \\pi$.''')
                loigiai_d = ('''Phương trình $g(x) = 0 \\Leftrightarrow \\sin x = -\\frac{1}{2}$.\\\\ Phương trình $f(x) = 0 \\Leftrightarrow 4(1 - \\sin^2 x) - 3 = 0 \\Leftrightarrow \\sin^2 x = \\frac{1}{4} \\Leftrightarrow \\sin x = \\pm\\frac{1}{2}$.\\\\ Nghiệm chung của hai phương trình thỏa mãn $\\sin x = -\\frac{1}{2} \\Leftrightarrow x = -\\frac{\\pi}{6} + k2\\pi$ hoặc $x = \\frac{7\\pi}{6} + k2\\pi$.\\\\ Trên khoảng $\\left( -\\frac{\\pi}{2}; \\frac{3\\pi}{2} \\right)$, các nghiệm chung là $x = -\\frac{\\pi}{6}$ và $x = \\frac{7\\pi}{6}$. Vậy có đúng $2$ nghiệm chung.''')
            else:
                str_f = "4\\cos^2 2x - 3"
                str_g = "2\\sin 2x + 1"
                str_g_x = "2\\sin 2x + 1"
                str_f_x = "4\\cos^2 2x - 3"
                str_diem_x = "\\frac{\\pi}{4}"
                str_diem_y = "3"
                str_chu_ky = "\\frac{\\pi}{2}"
                str_chu_ky_sai = "\\pi"
                str_khoang = "\\left( -\\frac{\\pi}{4}; \\frac{3\\pi}{4} \\right)"
                so_nghiem_chung = "2"
                so_nghiem_chung_sai = "3"
                loigiai_a = ('''Thay $x = \\frac{\\pi}{4}$ vào hàm số $g(x)$ ta được: $g\\left(\\frac{\\pi}{4}\\right) = 2\\sin\\left(2 \\cdot \\frac{\\pi}{4}\\right) + 1 = 2 \\cdot 1 + 1 = 3$.\\\\ Do đó đồ thị hàm số $g(x)$ đi qua điểm $\\left( \\frac{\\pi}{4}; 3 \\right)$.''')
                loigiai_b = ('''Tập xác định $\\mathscr{D} = \\mathbb{R}$. Ta có $f(-x) = 4\\cos^2(-2x) - 3 = 4\\cos^2 2x - 3 = f(x)$ nên $f(x)$ là hàm số chẵn.\\\\ Hạ bậc hàm số $f(x) = 4 \\cdot \\frac{1 + \\cos 4x}{2} - 3 = 2\\cos 4x - 1$. Hàm số tuần hoàn với chu kỳ $T = \\frac{2\\pi}{4} = \\frac{\\pi}{2}$.''')
                loigiai_d = ('''Phương trình $g(x) = 0 \\Leftrightarrow \\sin 2x = -\\frac{1}{2}$.\\\\ Phương trình $f(x) = 0 \\Leftrightarrow 4(1 - \\sin^2 2x) - 3 = 0 \\Leftrightarrow \\sin^2 2x = \\frac{1}{4} \\Leftrightarrow \\sin 2x = \\pm\\frac{1}{2}$.\\\\ Nghiệm chung của hai phương trình thỏa mãn $\\sin 2x = -\\frac{1}{2} \\Leftrightarrow 2x = -\\frac{\\pi}{6} + k2\\pi$ hoặc $2x = \\frac{7\\pi}{6} + k2\\pi \\Leftrightarrow x = -\\frac{\\pi}{12} + k\\pi$ hoặc $x = \\frac{7\\pi}{12} + k\\pi$.\\\\ Trên khoảng $\\left( -\\frac{\\pi}{4}; \\frac{3\\pi}{4} \\right)$, các nghiệm chung là $x = -\\frac{\\pi}{12}$ và $x = \\frac{7\\pi}{12}$. Vậy có đúng $2$ nghiệm chung.''')

            # Nội dung câu hỏi
            noidungcauhoi = ('''Xét hai hàm số $f(x) = %s$; $g(x) = %s$.''' 
                             % (str_f, str_g))

            ########################################################################
            # Nhận biết ############################################
            nb_da_1_d = '\\True Đồ thị hàm số $g(x)$ đi qua điểm $\\left( %s; %s \\right)$' % (str_diem_x, str_diem_y)
            nb_da_1_s = 'Đồ thị hàm số $g(x)$ đi qua điểm $\\left( %s; 0 \\right)$' % (str_diem_x)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            list_nb_2 = [loigiai_a]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            th_da_1_d = '\\True Hàm số $f(x)$ là hàm số chẵn và có chu kỳ $T = %s$' % (str_chu_ky)
            th_da_1_s = 'Hàm số $f(x)$ là hàm số lẻ và có chu kỳ $T = %s$' % (str_chu_ky_sai)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            list_th_2 = [loigiai_b]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng ############################################
            vd_da_1_s = 'Giá trị lớn nhất của hàm số $f(x) + g(x)$ là một số nguyên'
            vd_da_1_d = '\\True Giá trị lớn nhất của hàm số $f(x) + g(x)$ bằng $2,25$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = ('''Ta có biểu thức tổng: $f(x) + g(x) = (4\\cos^2 %sx - 3) + (2\\sin %sx + 1) = 4(1 - \\sin^2 %sx) - 3 + 2\\sin %sx + 1 = -4\\sin^2 %sx + 2\\sin %sx + 2$.\\\\ Đặt $t = \\sin %sx$ với $t \\in [-1; 1]$, ta có hàm số bậc hai $h(t) = -4t^2 + 2t + 2$.\\\\ Tọa độ đỉnh của parabol là $t = -\\frac{2}{2 \\cdot (-4)} = \\frac{1}{4} \\in [-1; 1]$.\\\\ Giá trị lớn nhất của hàm số đạt được tại đỉnh: $\\max h(t) = h\\left(\\frac{1}{4}\\right) = -4\\left(\\frac{1}{16}\\right) + 2\\left(\\frac{1}{4}\\right) + 2 = \\frac{9}{4} = 2,25$.\\\\ Vì $2,25$ không phải là một số nguyên nên mệnh đề gốc phát biểu là sai.''' 
                            % (latex(k) if k != 1 else "", latex(k) if k != 1 else "", latex(k) if k != 1 else "", latex(k) if k != 1 else "", latex(k) if k != 1 else "", latex(k) if k != 1 else "", latex(k) if k != 1 else ""))

            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao ############################################
            vdc_da_1_d = '\\True Hai phương trình $f(x) = 0$; $g(x) = 0$ có $%s$ nghiệm chung trên khoảng $%s$' % (so_nghiem_chung, str_khoang)
            vdc_da_1_s = 'Hai phương trình $f(x) = 0$; $g(x) = 0$ có $%s$ nghiệm chung trên khoảng $%s$' % (so_nghiem_chung_sai, str_khoang)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            list_vdc_2 = [loigiai_d]

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


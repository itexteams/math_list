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


def bt_dang21_p2_b2_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            b = random.randint(1, 5)
            a = 2 * b
            f_prime_val = round(a * math.cos(-2) + b, 3)
            f_prime_str = str(f_prime_val).replace('.', ',')

            v1 = -b * sp.pi
            v2 = b * sp.sqrt(3)/2 - 2 * b * sp.pi / 3
            v3 = -b * sp.sqrt(3)/2 - b * sp.pi / 3
            v4 = b * sp.sqrt(3)/2 + b * sp.pi / 3
            v5 = -b * sp.sqrt(3)/2 + 2 * b * sp.pi / 3
            v6 = b * sp.pi
            f_pi_2 = b * sp.pi / 2

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hàm số $f(x)=%s \\sin x \\cos x + %s x$ trên $[-\\pi; \\pi]$.''' 
                             % (a, b))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Đạo hàm của hàm số đã cho là $f\'(x)=%s \\cos 2x + %s$' % (a, b)
            nb_da_1_s = 'Đạo hàm của hàm số đã cho là $f\'(x)=%s \\sin 2x + %s$' % (a, b)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Ta có: $f(x)=%s \\sin x \\cos x + %s x = %s \\sin 2x + %s x \\Rightarrow f'(x)=%s \\cos 2x + %s$.'''
                            % (a, b, b, b, a, b))

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Hàm số $y = f(x)$ có $4$ điểm cực trị thuộc $[-\\pi; \\pi]$'
            th_da_1_s = 'Hàm số $y = f(x)$ có $3$ điểm cực trị thuộc $[-\\pi; \\pi]$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Ta có $f'(x)=0 \\Leftrightarrow \\cos 2x = -\\frac{1}{2} \\Leftrightarrow \\left[ \\begin{array}{l} 2x = \\frac{2\\pi}{3} + k2\\pi \\\\ 2x = -\\frac{2\\pi}{3} + k2\\pi \\end{array} \\right. \\Leftrightarrow \\left[ \\begin{array}{l} x = \\frac{\\pi}{3} + k\\pi \\\\ x = -\\frac{\\pi}{3} + k\\pi \\end{array} \\right., k \\in \\mathbb{Z}$.\\\\
            Trên đoạn $[-\\pi; \\pi]$, $f'(x)=0 \\Leftrightarrow x \\in \\left\\{ \\frac{\\pi}{3}; -\\frac{\\pi}{3}; \\frac{2\\pi}{3}; -\\frac{2\\pi}{3} \\right\\}$.\\\\
            Vẽ bảng biến thiên của hàm số $y=f(x)$ trên đoạn $[-\\pi; \\pi]$:\\\\
            \\begin{center}
            \\begin{tikzpicture}[line width=1pt]
            \\tkzTabInit[espcl=1.5,lgt=1.5]
            {$x$ / 1, $f'(x)$ / 1, $f(x)$ / 2.5}
            {$-\\pi$, $-\\frac{2\\pi}{3}$, $-\\frac{\\pi}{3}$, $\\frac{\\pi}{3}$, $\\frac{2\\pi}{3}$, $\\pi$}
            \\tkzTabLine{, +, 0, -, 0, +, 0, -, 0, +, }
            \\tkzTabVar{-/ $%s$, +/ $%s$, -/ $%s$, +/ $%s$, -/ $%s$, +/ $%s$}
            \\end{tikzpicture}
            \\end{center}
            Từ bảng biến thiên ta thấy trên đoạn $[-\\pi; \\pi]$ hàm số có $4$ điểm cực trị.'''
                            % (latex(v1), latex(v2), latex(v3), latex(v4), latex(v5), latex(v6)))

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Hàm số $y = f(x)$ đồng biến trên khoảng $(-2; -1)$'
            vd_da_1_s = 'Hàm số $y = f(x)$ nghịch biến trên khoảng $(-2; -1)$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Do $-1 > -\\frac{\\pi}{3}$ nên khoảng $(-2; -1)$ không là tập con của khoảng $\\left(-\\frac{2\\pi}{3}; -\\frac{\\pi}{3}\\right)$.\\\\
            Tại $x=-1 \\in (-2; -1)$ có $f'(-1) = %s \\cos(-2) + %s = %s > 0$ do đó hàm số đã cho đồng biến trên $(-2; -1)$.'''
                            % (a, b, f_prime_str))

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Giá trị lớn nhất của $f(x)$ trên đoạn $\\left[0; \\frac{\\pi}{2}\\right]$ là $%s$' % latex(v4)
            vdc_da_1_s = 'Giá trị lớn nhất của $f(x)$ trên đoạn $\\left[0; \\frac{\\pi}{2}\\right]$ là $%s$' % latex(f_pi_2)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Ta có $f'(x)=0 \\Leftrightarrow \\cos 2x = -\\frac{1}{2} \\Leftrightarrow \\left[ \\begin{array}{l} 2x = \\frac{2\\pi}{3} + k2\\pi \\\\ 2x = -\\frac{2\\pi}{3} + k2\\pi \\end{array} \\right. \\Leftrightarrow \\left[ \\begin{array}{l} x = \\frac{\\pi}{3} + k\\pi \\\\ x = -\\frac{\\pi}{3} + k\\pi \\end{array} \\right., k \\in \\mathbb{Z}$.\\\\
            Trên $\\left[0; \\frac{\\pi}{2}\\right]$, $f'(x)=0 \\Leftrightarrow x = \\frac{\\pi}{3}$ và ta có $f(0)=0; f\\left(\\frac{\\pi}{2}\\right) = %s; f\\left(\\frac{\\pi}{3}\\right) = %s$.\\\\
            Giá trị lớn nhất của $f(x)$ trên đoạn $\\left[0; \\frac{\\pi}{2}\\right]$ là $%s$ đạt khi $x = \\frac{\\pi}{3}$.'''
                             % (latex(f_pi_2), latex(v4), latex(v4)))

            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vdc)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
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
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


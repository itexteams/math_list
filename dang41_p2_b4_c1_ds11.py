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


def bt_dang41_p2_b4_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            a = random.randint(1, 3)
            b = random.randint(2, 4)

            if a == 1:
                h_f = "\\sin x \\cos x"
                h_g = "\\sin x + \\cos x"
                val_c = "\\sqrt{2}"
                val_c_s = "2"
                chu_ky_d = "\\frac{\\pi}{2}"
                chu_ky_s = "\\frac{\\pi}{4}"

                loigiai_a = "Tập xác định $D=\\mathbb{R}$.\\\\ Có $g(-x) = \\sin(-x) + \\cos(-x) = -\\sin x + \\cos x \\neq g(x)$.\\\\ Và $-g(x) = -\\sin x - \\cos x \\neq g(-x)$.\\\\ Vậy hàm số $g(x)$ là hàm số không chẵn không lẻ."
                loigiai_b = "Ta có $f^2(x) = (\\sin x \\cos x)^2 = \\frac{1}{4} \\sin^2 2x = \\frac{1}{4} \\cdot \\frac{1-\\cos 4x}{2} = \\frac{1}{8} - \\frac{1}{8} \\cos 4x$.\\\\ Hàm số $y = \\cos 4x$ tuần hoàn với chu kỳ $T = \\frac{2\\pi}{4} = \\frac{\\pi}{2}$.\\\\ Vậy hàm số $f^2(x)$ có chu kỳ $T = \\frac{\\pi}{2}$."
                loigiai_c = "Ta có $g(x) = \\sin x + \\cos x = \\sqrt{2}\\sin\\left(x + \\frac{\\pi}{4}\\right)$.\\\\ Do $-1 \\le \\sin\\left(x + \\frac{\\pi}{4}\\right) \\le 1$ nên $-\\sqrt{2} \\le g(x) \\le \\sqrt{2}$.\\\\ Giá trị lớn nhất của hàm số $g(x)$ bằng $\\sqrt{2}$ khi $\\sin\\left(x + \\frac{\\pi}{4}\\right) = 1 \\Leftrightarrow x = \\frac{\\pi}{4} + k2\\pi$."

                loigiai_d = "Ta có $f(x) + 2g(x) = 2 \\Leftrightarrow \\sin x \\cos x + 2(\\sin x + \\cos x) = 2$.\\\\ Đặt $t = \\sin x + \\cos x$, điều kiện $t \\in [-\\sqrt{2}; \\sqrt{2}]$.\\\\ Suy ra $\\sin x \\cos x = \\frac{t^2 - 1}{2}$.\\\\ Phương trình trở thành $\\frac{t^2 - 1}{2} + 2t = 2 \\Leftrightarrow t^2 + 4t - 5 = 0 \\Leftrightarrow \\left[\\begin{aligned} & t = 1 \\text{ (nhận)} \\\\ & t = -5 \\text{ (loại)} \\end{aligned}\\right.$.\\\\ Với $t=1$, ta có $\\sin x + \\cos x = 1 \\Leftrightarrow \\sqrt{2}\\sin\\left(x + \\frac{\\pi}{4}\\right) = 1 \\Leftrightarrow \\sin\\left(x + \\frac{\\pi}{4}\\right) = \\frac{\\sqrt{2}}{2} \\Leftrightarrow \\left[\\begin{aligned} & x + \\frac{\\pi}{4} = \\frac{\\pi}{4} + k2\\pi \\\\ & x + \\frac{\\pi}{4} = \\frac{3\\pi}{4} + k2\\pi \\end{aligned}\\right. \\Leftrightarrow \\left[\\begin{aligned} & x = k2\\pi \\\\ & x = \\frac{\\pi}{2} + k2\\pi \\end{aligned}\\right.$.\\\\ Biểu diễn trên đường tròn lượng giác ta được $2$ điểm."
            else:
                h_f = "\\sin x \\cos x"
                h_g = "\\sin x + \\cos x"
                val_c = "\\sqrt{2}"
                val_c_s = "2"
                chu_ky_d = "\\frac{\\pi}{2}"
                chu_ky_s = "\\frac{\\pi}{4}"

                loigiai_a = "Tập xác định $D=\\mathbb{R}$.\\\\ Có $g(-x) = \\sin(-x) + \\cos(-x) = -\\sin x + \\cos x \\neq g(x)$.\\\\ Và $-g(x) = -\\sin x - \\cos x \\neq g(-x)$.\\\\ Vậy hàm số $g(x)$ là hàm số không chẵn không lẻ."
                loigiai_b = "Ta có $f^2(x) = (\\sin x \\cos x)^2 = \\frac{1}{4} \\sin^2 2x = \\frac{1}{4} \\cdot \\frac{1-\\cos 4x}{2} = \\frac{1}{8} - \\frac{1}{8} \\cos 4x$.\\\\ Hàm số $y = \\cos 4x$ tuần hoàn với chu kỳ $T = \\frac{2\\pi}{4} = \\frac{\\pi}{2}$.\\\\ Vậy hàm số $f^2(x)$ có chu kỳ $T = \\frac{\\pi}{2}$."
                loigiai_c = "Ta có $g(x) = \\sin x + \\cos x = \\sqrt{2}\\sin\\left(x + \\frac{\\pi}{4}\\right)$.\\\\ Do $-1 \\le \\sin\\left(x + \\frac{\\pi}{4}\\right) \\le 1$ nên $-\\sqrt{2} \\le g(x) \\le \\sqrt{2}$.\\\\ Giá trị lớn nhất của hàm số $g(x)$ bằng $\\sqrt{2}$ khi $\\sin\\left(x + \\frac{\\pi}{4}\\right) = 1 \\Leftrightarrow x = \\frac{\\pi}{4} + k2\\pi$."

                loigiai_d = "Ta có $f(x) + 2g(x) = 2 \\Leftrightarrow \\sin x \\cos x + 2(\\sin x + \\cos x) = 2$.\\\\ Đặt $t = \\sin x + \\cos x$, điều kiện $t \\in [-\\sqrt{2}; \\sqrt{2}]$.\\\\ Suy ra $\\sin x \\cos x = \\frac{t^2 - 1}{2}$.\\\\ Phương trình trở thành $\\frac{t^2 - 1}{2} + 2t = 2 \\Leftrightarrow t^2 + 4t - 5 = 0 \\Leftrightarrow \\left[\\begin{aligned} & t = 1 \\text{ (nhận)} \\\\ & t = -5 \\text{ (loại)} \\end{aligned}\\right.$.\\\\ Với $t=1$, ta có $\\sin x + \\cos x = 1 \\Leftrightarrow \\sqrt{2}\\sin\\left(x + \\frac{\\pi}{4}\\right) = 1 \\Leftrightarrow \\sin\\left(x + \\frac{\\pi}{4}\\right) = \\frac{\\sqrt{2}}{2} \\Leftrightarrow \\left[\\begin{aligned} & x + \\frac{\\pi}{4} = \\frac{\\pi}{4} + k2\\pi \\\\ & x + \\frac{\\pi}{4} = \\frac{3\\pi}{4} + k2\\pi \\end{aligned}\\right. \\Leftrightarrow \\left[\\begin{aligned} & x = k2\\pi \\\\ & x = \\frac{\\pi}{2} + k2\\pi \\end{aligned}\\right.$.\\\\ Biểu diễn trên đường tròn lượng giác ta được $2$ điểm."

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hai hàm số $f(x) = %s$; $g(x) = %s$. Xác định tính đúng sai của các mệnh đề sau:''' % (h_f, h_g))

            ########################################################################
            # Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Hàm số $g(x)$ là hàm số không chẵn không lẻ'
            nb_da_1_s = 'Hàm số $g(x)$ là hàm số chẵn'
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''%s''' % (loigiai_a))

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = 'Hàm số $f^2(x)$ có chu kỳ $T = %s$' % (chu_ky_s)
            th_da_1_s = '\\True Hàm số $f^2(x)$ có chu kỳ $T = %s$' % (chu_ky_d)
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''%s''' % (loigiai_b))

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận
            # dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Giá trị lớn nhất của hàm số $g(x)$ bằng $%s$' % (val_c)
            vd_da_1_s = 'Giá trị lớn nhất của hàm số $g(x)$ bằng $%s$' % (val_c_s)
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''%s''' % (loigiai_c))

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận
            # dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Phương trình $f(x) + 2g(x) = 2$ có 2 điểm biểu diễn nghiệm trên vòng tròn lượng giác'
            vdc_da_1_s = 'Phương trình $f(x) + 2g(x) = 2$ có 4 điểm biểu diễn nghiệm trên vòng tròn lượng giác'
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''%s''' % (loigiai_d))

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
            str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
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


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


def bt_dang24_p2_b3_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Random các tham số cho bài toán lượng giác tương đương
            # Ý a: y = tan(a1*x) + cot(b1*x)
            a1 = random.choice([1, 2])
            b1 = 2 if a1 == 1 else 3

            # Ý c: y = sqrt(c3 - sin^2 x) -> chọn c3 nguyên từ 2 đến 5 để biểu thức dưới căn luôn dương
            c3 = randint(2, 5)

            # Nội dung câu hỏi chính
            noidungcauhoi = ('''Các mệnh đề sau đúng hay sai?''')

            ########################################################################
            # Nhận biết (Ý a) ############################################
            # Hàm số y = tan(a1*x) + cot(b1*x) xác định khi cos(a1*x) != 0 và sin(b1*x) != 0
            nb_da_1_d = '\\True Hàm số $y = \\tan %s + \\cot %s$ xác định khi $\\begin{cases} \\cos %s \\ne 0 \\\\ \\sin %s \\ne 0 \\end{cases}$' %(latex(a1*x) if a1 != 1 else 'x', latex(b1*x), latex(a1*x) if a1 != 1 else 'x', latex(b1*x))
            nb_da_1_s = 'Hàm số $y = \\tan %s + \\cot %s$ xác định khi $\\cos %s \\ne 0$' %(latex(a1*x) if a1 != 1 else 'x', latex(b1*x), latex(a1*x) if a1 != 1 else 'x')
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = ('''Hàm số $y = \\tan %s + \\cot %s$ xác định khi và chỉ khi đồng thời:\\\\'''
                            '''$\\tan %s$ xác định $\\Leftrightarrow \\cos %s \\ne 0$.\\\\'''
                            '''$\\cot %s$ xác định $\\Leftrightarrow \\sin %s \\ne 0$.\\\\'''
                            '''Vậy điều kiện xác định là $\\begin{cases} \\cos %s \\ne 0 \\\\ \\sin %s \\ne 0 \\end{cases}$.'''
                            %(latex(a1*x) if a1 != 1 else 'x', latex(b1*x), latex(a1*x) if a1 != 1 else 'x', latex(a1*x) if a1 != 1 else 'x', latex(b1*x), latex(b1*x), latex(a1*x) if a1 != 1 else 'x', latex(b1*x)))

            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu (Ý b) ############################################
            # Hàm số y = sqrt(pi - cos x) có tập xác định D = R vì pi - cos x >= pi - 1 > 0 luôn đúng
            th_da_1_d = '\\True Hàm số $y = \\sqrt{\\pi - \\cos x}$ có tập xác định là $D = \\mathbb{R}$'
            th_da_1_s = 'Hàm số $y = \\sqrt{\\pi - \\cos x}$ có tập xác định là $D = [-1; 1]$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            loigiai_th_1 = ('''Hàm số $y = \\sqrt{\\pi - \\cos x}$ xác định khi và chỉ khi $\\pi - \\cos x \\ge 0 \\Leftrightarrow \\cos x \\le \\pi$.\\\\'''
                            '''Vì $-1 \\le \\cos x \\le 1$ với mọi $x \\in \\mathbb{R}$ và $\\pi \\approx 3,14 > 1$, nên bất phương trình $\\cos x \\le \\pi$ luôn đúng với mọi $x \\in \\mathbb{R}$.\\\\'''
                            '''Vậy tập xác định của hàm số là $D = \\mathbb{R}$.''')

            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## 
            # Vận dụng (Ý c) ############################################
            # Hàm số y = sqrt(c3 - sin^2 x) có tập xác định D = R vì c3 >= 2 và sin^2 x <= 1 => c3 - sin^2 x >= 1 > 0
            vd_da_1_d = '\\True Hàm số $y = \\sqrt{%s - \\sin^2 x}$ có tập xác định là $D = \\mathbb{R}$' %(latex(c3))
            vd_da_1_s = 'Hàm số $y = \\sqrt{%s - \\sin^2 x}$ có tập xác định là $D = [-%s; %s]$' %(latex(c3), latex(c3), latex(c3))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = ('''Hàm số $y = \\sqrt{%s - \\sin^2 x}$ xác định khi và chỉ khi $%s - \\sin^2 x \\ge 0 \\Leftrightarrow \\sin^2 x \\le %s$.\\\\'''
                            '''Vì $0 \\le \\sin^2 x \\le 1$ với mọi $x \\in \\mathbb{R}$ và $%s \\ge 2$, nên bất phương trình $\\sin^2 x \\le %s$ luôn đúng với mọi $x \\in \\mathbb{R}$.\\\\'''
                            '''Vậy tập xác định của hàm số là $D = \\mathbb{R}$'''
                            %(latex(c3), latex(c3), latex(c3), latex(c3), latex(c3)))

            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## 
            # Vận dụng cao (Ý d) ############################################
            # Hàm số y = sqrt(sin x - 1) + sqrt(cos x - 1) xác định khi sin x = 1 và cos x = 1 (vô nghiệm vì sin^2 x + cos^2 x = 2 != 1) -> TXĐ D = rỗng
            vdc_da_1_d = 'Hàm số $y = \\sqrt{\\sin x - 1} + \\sqrt{\\cos x - 1}$ có tập xác định là $D = \\mathbb{R}$'
            vdc_da_1_s = '\\True Hàm số $y = \\sqrt{\\sin x - 1} + \\sqrt{\\cos x - 1}$ có tập xác định là $D = \\varnothing$'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = ('''Hàm số $y = \\sqrt{\\sin x - 1} + \\sqrt{\\cos x - 1}$ xác định khi và chỉ khi:\\\\'''
                             '''$\\begin{cases} \\sin x - 1 \\ge 0 \\\\ \\cos x - 1 \\ge 0 \\end{cases} \\Leftrightarrow \\begin{cases} \\sin x \\ge 1 \\\\ \\cos x \\ge 1 \\end{cases} \\Leftrightarrow \\begin{cases} \\sin x = 1 \\\\ \\cos x = 1 \\end{cases}$.\\\\'''
                             '''Mặt khác, ta luôn có hệ thức $\\sin^2 x + \\cos^2 x = 1$. Nếu $\\sin x = 1$ và \\\\ $\\cos x = 1$ thì $1^2 + 1^2 = 2 \\ne 1$ (vô lý).\\\\'''
                             '''Do đó không tồn tại giá trị $x$ nào thỏa mãn điều kiện xác định.\\\\'''
                             '''Vậy tập xác định của hàm số là $D = \\varnothing$. Khẳng định $D = \\mathbb{R}$ là sai.''')

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


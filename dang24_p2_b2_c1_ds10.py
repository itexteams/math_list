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


def bt_dang24_p2_b2_c1_ds10(self):
            # Khai báo biến
            # Khai báo biến
            # Khởi tạo tham số ngẫu nhiên a (đóng vai trò của số 10 trong bài gốc)
            a_val = random.choice([8, 10, 12, 14, 16])
            m = symbols('m')

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho các tập hợp khác rỗng $A=[m; %s - m)$ và $B=(2m; 2m+1]$.''' % (a_val))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_true_val = a_val // 2 - 1
            nb_false_val = a_val // 2

            nb_da_1_d = '\\True Có %s giá trị nguyên dương của $m$ để hai tập hợp trên khác rỗng' % nb_true_val
            nb_da_1_s = 'Có %s giá trị nguyên dương của $m$ để hai tập hợp trên khác rỗng' % nb_false_val
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Điều kiện để tập $A$ khác rỗng: $m < %s - m \\Leftrightarrow 2m < %s \\Leftrightarrow m < %s$. \\\\
            Tập $B=(2m; 2m+1]$ luôn khác rỗng với mọi $m$. \\\\
            Vì $m$ là số nguyên dương nên $m \\in \\{1; 2; ... ; %s\\}$. \\\\
            Vậy có $%s$ giá trị nguyên dương của $m$.''' % (a_val, a_val, a_val // 2, nb_true_val, nb_true_val))

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
            th_max_m = (a_val - 2) // 3
            th_count = th_max_m + 1

            th_da_1_d = '\\True Có %s giá trị nguyên của $m$ để $B \\subset A$' % th_count
            th_da_1_s = 'Có vô số giá trị nguyên của $m$ để $B \\subset A$'
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            if th_max_m == 0:
                th_list_str = '0'
            elif th_max_m == 1:
                th_list_str = '0; 1'
            else:
                th_list_str = '0; 1; ... ; %s' % th_max_m

            fraction_str_th = '\\frac{%s}{3}' % (a_val - 1)

            loigiai_th_1 = ('''Để $B \\subset A$ thì $\\begin{cases} m \\le 2m \\\\ 2m+1 < %s-m \\end{cases} \\Leftrightarrow \\begin{cases} m \\ge 0 \\\\ 3m < %s \\end{cases} \\Leftrightarrow 0 \\le m < %s$. \\\\
            Vì $m$ là số nguyên nên $m \\in \\{%s\\}$. \\\\
            Vậy có $%s$ giá trị nguyên của $m$.''' % (a_val, a_val - 1, fraction_str_th, th_list_str, th_count))

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
            k_val = random.randint(1, a_val // 2 - 1)

            vd_da_1_d = '\\True Với $m=%s$ thì tập $A=[%s; %s)$' % (k_val, k_val, a_val - k_val)
            vd_da_1_s = 'Với $m=%s$ thì tập $A=[%s; %s]$' % (k_val, k_val, a_val - k_val)
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Thay $m=%s$ vào tập $A=[m; %s-m)$, ta được $A=[%s; %s-%s) = [%s; %s)$.''' % (k_val, a_val, k_val, a_val, k_val, k_val, a_val - k_val))

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
            upper_start = (a_val + 2) // 3
            upper_end = a_val // 2 - 1

            upper_list = []
            for i in range(upper_start, upper_end + 1):
                upper_list.append(str(i))
            upper_count = len(upper_list)

            vdc_count = 20 + upper_count

            vdc_da_1_d = '\\True Có %s giá trị nguyên của $m$ thuộc $[-20; 20]$ để $A \\subset C_{\\mathbb{R}}B$' % vdc_count
            vdc_da_1_s = 'Có %s giá trị nguyên của $m$ thuộc $[-20; 20]$ để $A \\subset C_{\\mathbb{R}}B$' % (vdc_count + 1)
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            fraction_str_vdc = '\\frac{%s}{3}' % a_val

            if upper_count == 0:
                upper_case_str = 'không có giá trị nguyên nào'
            elif upper_count == 1:
                upper_case_str = 'có $1$ giá trị là $m=%s$' % upper_list[0]
            else:
                upper_case_str = 'có $%s$ giá trị là $m \\in \\{%s\\}$' % (upper_count, '; '.join(upper_list))

            loigiai_vdc_1 = ('''Ta có $C_{\\mathbb{R}}B = (-\\infty; 2m] \\cup (2m+1; +\\infty)$. \\\\
            Để $A \\subset C_{\\mathbb{R}}B$ thì $\\left[\\begin{array}{l} %s-m \\le 2m \\\\ m \\ge 2m+1 \\end{array}\\right. \\Leftrightarrow \\left[\\begin{array}{l} 3m \\ge %s \\\\ m \\le -1 \\end{array}\\right. \\Leftrightarrow \\left[\\begin{array}{l} m \\ge %s \\\\ m \\le -1 \\end{array}\\right.$. \\\\
            Kết hợp điều kiện hai tập hợp khác rỗng là $m < %s$, ta được $m \\le -1$ hoặc $%s \\le m < %s$. \\\\
            Vì $m \\in \\mathbb{Z}$ và $m \\in [-20; 20]$ nên: \\\\
            Trường hợp 1: $m \\in \\{-20; -19; ... ; -1\\}$ có $20$ giá trị. \\\\
            Trường hợp 2: $%s \\le m < %s$, %s. \\\\
            Vậy tổng cộng có $20 + %s = %s$ giá trị nguyên của $m$.''' % (
                a_val, a_val, fraction_str_vdc, a_val // 2, fraction_str_vdc, a_val // 2, fraction_str_vdc, a_val // 2, upper_case_str, upper_count, vdc_count
            ))

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
                '\\end{ex}\n\\end{minipage}\n\n')
            return content


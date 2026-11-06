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


def bt_dang40_p2_b2_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Tạo x1, x2 là các số nguyên ngẫu nhiên sao cho x1 < x2 và x1 + x2 là số chẵn
            while True:
                x1 = random.randint(-4, 2)
                x2 = random.randint(x1 + 2, 5)
                if (x1 + x2) % 2 == 0:
                    break

            # Tính toán các hệ số để hàm số có điểm cực trị đẹp tại x1, x2
            # f'(x) = 3x^2 + 2bx + c. Để f'(x)=0 có nghiệm x1, x2 thì:
            b_val = -3 * (x1 + x2) // 2
            c_val = 3 * x1 * x2
            d_val = random.randint(-5, 5)

            f = x**3 + b_val*x**2 + c_val*x + d_val
            df = 3*x**2 + 2*b_val*x + c_val

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hàm số $y = f(x) = %s$.''' 
                             %(latex(f)))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Đạo hàm của hàm số đã cho là $f\'(x) = %s$' % (latex(df))
            # Tạo một đạo hàm sai
            df_sai = 3*x**2 - 2*b_val*x + c_val if b_val != 0 else 3*x**2 + 2*c_val*x - c_val
            nb_da_1_s = 'Đạo hàm của hàm số đã cho là $f\'(x) = %s$' % (latex(df_sai))

            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Ta có đạo hàm của hàm số là $f'(x) = %s$.''' % (latex(df)))

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
            th_da_1_d = '\\True Phương trình $f\'(x) = 0$ có tập nghiệm là $S = \\{%s; %s\\}$' % (x1, x2)
            th_da_1_s = 'Phương trình $f\'(x) = 0$ có tập nghiệm là $S = \\{%s; %s\\}$' % (-x1, -x2)

            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Ta có $f'(x) = 0 \\Leftrightarrow %s = 0 \\Leftrightarrow \\left[ \\begin{array}{l} x = %s \\\\ x = %s \\end{array} \\right.$. \\\\
            Vậy tập nghiệm của phương trình là $S = \\{%s; %s\\}$.''' % (latex(df), x1, x2, x1, x2))

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Tìm đoạn xét giá trị lớn nhất
            m1 = x2 - 1
            m2 = x2 + 1
            val_m1 = m1**3 + b_val*m1**2 + c_val*m1 + d_val
            val_x2 = x2**3 + b_val*x2**2 + c_val*x2 + d_val
            val_m2 = m2**3 + b_val*m2**2 + c_val*m2 + d_val

            # Tìm GTLN trên đoạn [m1; m2]
            max_val = max(val_m1, val_x2, val_m2)
            max_x = m1 if max_val == val_m1 else (x2 if max_val == val_x2 else m2)
            wrong_x = m1 if max_x != m1 else m2

            # Các đáp án
            vd_da_1_d = '\\True Hàm số đã cho đạt giá trị lớn nhất trên đoạn $[%s; %s]$ tại $x = %s$' % (m1, m2, max_x)
            vd_da_1_s = 'Hàm số đã cho đạt giá trị lớn nhất trên đoạn $[%s; %s]$ tại $x = %s$' % (m1, m2, wrong_x)

            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Xét hàm số trên đoạn $[%s; %s]$, ta có $f'(x) = 0 \\Leftrightarrow \\left[ \\begin{array}{l} x = %s \\text{ (loại)} \\\\ x = %s \\text{ (nhận)} \\end{array} \\right.$. \\\\
            Ta tính được các giá trị: $f(%s) = %s$, $f(%s) = %s$, $f(%s) = %s$. \\\\
            Vậy hàm số đạt giá trị lớn nhất trên đoạn $[%s; %s]$ tại $x = %s$.''' % 
            (m1, m2, x1, x2, m1, val_m1, x2, val_x2, m2, val_m2, m1, m2, max_x))

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Viết phương trình đường thẳng qua 2 điểm cực trị
            slope = Rational(2*c_val, 3) - Rational(2*b_val**2, 9)
            intercept = d_val - Rational(b_val*c_val, 9)

            # Phương trình đường thẳng
            line_eq = slope*x + intercept
            line_eq_sai = slope*x - intercept if intercept != 0 else -slope*x + 1

            # Các đáp án
            vdc_da_1_d = '\\True Gọi $x_1, x_2$ là hai điểm cực trị của hàm số $y = f(x)$. Khi đó, phương trình đường thẳng đi qua hai điểm $M_1(x_1; f(x_1))$ và $M_2(x_2; f(x_2))$ là $y = %s$' % (latex(line_eq))
            vdc_da_1_s = 'Gọi $x_1, x_2$ là hai điểm cực trị của hàm số $y = f(x)$. Khi đó, phương trình đường thẳng đi qua hai điểm $M_1(x_1; f(x_1))$ và $M_2(x_2; f(x_2))$ là $y = %s$' % (latex(line_eq_sai))

            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Ta thực hiện phép chia đa thức $f(x)$ cho $f'(x)$ ta được: \\\\
            $f(x) = f'(x) \\cdot \\left( \\frac{1}{3}x + %s \\right) + (%s)$. \\\\
            Do $x_1, x_2$ là các điểm cực trị nên $f'(x_1) = 0$ và $f'(x_2) = 0$. \\\\
            Suy ra $f(x_1) = %s$ và $f(x_2) = %s$. \\\\
            Vậy phương trình đường thẳng đi qua hai điểm cực trị là $y = %s$.''' % 
            (latex(Rational(b_val, 9)), latex(line_eq), latex(line_eq.subs(x, symbols('x_1'))), latex(line_eq.subs(x, symbols('x_2'))), latex(line_eq)))

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


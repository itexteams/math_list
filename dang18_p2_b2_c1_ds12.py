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


def bt_dang18_p2_b2_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Vòng lặp tìm bộ số ngẫu nhiên thỏa mãn yêu cầu bài toán
            while True:
                m = random.randint(3, 8)
                n = random.randint(15, 30) * 100
                A = random.randint(400, 500)
                B = random.randint(60, 70) * 1000
                C_val = 200000
                x1 = 10
                x2 = 50

                # Điều kiện để đạo hàm F'(x) và L'(x) có 2 nghiệm phân biệt
                if A**2 - 3*B <= 0: continue
                if (A+m)**2 - 3*(B-n) <= 0: continue

                # Nghiệm của F'(x) = 0
                xF1 = (A - math.sqrt(A**2 - 3*B)) / 3
                xF2 = (A + math.sqrt(A**2 - 3*B)) / 3

                # Nghiệm của L'(x) = 0
                xL1 = ((A+m) - math.sqrt((A+m)**2 - 3*(B-n))) / 3
                xL2 = ((A+m) + math.sqrt((A+m)**2 - 3*(B-n))) / 3

                # Giới hạn nghiệm cực đại nằm trong khoảng [10, 160] và nghiệm còn lại > 160 để bảng biến thiên gọn gàng
                if not (110 < xF1 < 140): continue
                if not (xF2 > 160): continue
                if not (100 < xL1 < 130): continue
                if not (xL2 > 160): continue

                # Hàm F(x) và L(x)
                def F_func(x_val): return x_val**3 - A*x_val**2 + B*x_val + C_val
                def L_func(x_val): return x_val**3 - (A+m)*x_val**2 + (B-n)*x_val

                # Kiểm tra giá trị Max của Doanh thu F(x)
                f_max_x = int(xF1)
                if F_func(f_max_x + 1) > F_func(f_max_x): 
                    f_max_x += 1
                if F_func(160) > F_func(f_max_x): continue

                # Kiểm tra giá trị Max của Lợi nhuận L(x)
                l_max_x = int(xL1)
                if L_func(l_max_x + 1) > L_func(l_max_x): 
                    l_max_x += 1
                if L_func(160) > L_func(l_max_x): continue

                # Tính chi phí mốc để sinh đề
                y1 = m * x1**2 + n * x1 + C_val
                y2 = 2 * m * x2 + n

                # Đảm bảo các giá trị chi phí đều dương
                if y1 < 0 or y2 < 0: continue

                break

            # Định dạng các số thập phân sử dụng dấu phẩy
            str_xF1 = f"{xF1:.2f}".replace('.', ',')
            str_xF2 = f"{xF2:.2f}".replace('.', ',')
            f_int1 = int(xF1)
            f_int2 = f_int1 + 1
            F_val1 = int(F_func(f_int1))
            F_val2 = int(F_func(f_int2))

            str_xL1 = f"{xL1:.2f}".replace('.', ',')
            str_xL2 = f"{xL2:.2f}".replace('.', ',')
            l_int1 = int(xL1)
            l_int2 = l_int1 + 1
            L_val1 = int(L_func(l_int1))
            L_val2 = int(L_func(l_int2))

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một doanh nghiệp sản xuất một loại linh kiện điện tử có hàm doanh thu được mô tả bởi công thức $F(x)=x^3 - %sx^2 + %sx + 200000$ (đồng) và hàm chi phí được mô tả bởi công thức $C(x)=mx^2 + nx + 200000$ (đồng), tính cho $x$ sản phẩm với điều kiện $10 \\le x \\le 160$. Biết rằng chi phí để sản xuất $10$ sản phẩm là $%s$ (đồng) và chi phí biên tại mức sản lượng $50$ sản phẩm là $%s$ (đồng). Giả sử các sản phẩm sản xuất ra đều bán hết.'''
                             % (A, B, y1, y2))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            val_a = 200 * m - n
            nb_da_1_d = '\\True $200m - n = %s$' % (val_a)
            nb_da_1_s = '$200m - n = %s$' % (val_a + random.choice([-1000, 1000, -500, 500]))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Chi phí sản xuất $10$ sản phẩm là $%s$ đồng nên ta có phương trình:
            $$C(10)=m \\cdot 10^2 + n \\cdot 10 + 200000 = %s \\Leftrightarrow 10m + n = %s \\, (1)$$
            Chi phí biên là đạo hàm của hàm chi phí: $C'(x)=2mx+n$ và tại mức sản lượng $50$ là $%s$ đồng nên ta có:
            $$C'(50)=2m \\cdot 50 + n = %s \\Leftrightarrow 100m + n = %s \\, (2)$$
            Giải hệ $\\begin{cases} 10m + n = %s \\\\ 100m + n = %s \\end{cases} \\Leftrightarrow \\begin{cases} m = %s \\\\ n = %s \\end{cases}$ suy ra $200m - n = %s$.'''
            % (y1, y1, (y1 - 200000)//10, y2, y2, y2, (y1 - 200000)//10, y2, m, n, val_a))

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Doanh thu lớn nhất đạt được khi sản xuất %s sản phẩm' % (f_max_x)
            th_da_1_s = 'Doanh thu lớn nhất đạt được khi sản xuất %s sản phẩm' % (f_max_x + random.choice([-1, 1, 2]))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Khi đó hàm chi phí: $C(x)=%sx^2 + %sx + 200000$ \\\\
            Hàm doanh thu: $F(x)=x^3 - %sx^2 + %sx + 200000$ có $F'(x)=3x^2 - %sx + %s = 0$ \\\\
            Giải $F'(x)=0 \\Leftrightarrow 3x^2 - %sx + %s = 0 \\Leftrightarrow \\left[ \\begin{array}{l} x \\approx %s \\\\ x \\approx %s \\end{array} \\right.$ và có bảng biến thiên:
            \\begin{center}
            \\begin{tikzpicture}[line width=1pt]
            \\tkzTabInit[espcl=3.5,lgt=1.5]
            {$x$/1,$F'(x)$/0.7,$F(x)$/2.1}
            {$10$,{$%s$},$160$}
            \\tkzTabLine{,+,0,-,}
            \\tkzTabVar{-/ $%s$ ,+/ $%s$ ,-/ $%s$ }
            \\end{tikzpicture}
            \\end{center}
            Xét $F(%s)=%s %s F(%s)=%s$ nên doanh thu lớn nhất đạt được khi sản xuất $%s$ sản phẩm.'''
            % (m, n, A, B, 2*A, B, 2*A, B, str_xF1, str_xF2, str_xF1, 
               int(F_func(10)), int(F_func(f_max_x)), int(F_func(160)),
               f_int1, F_val1, "<" if F_val1 < F_val2 else ">", f_int2, F_val2, f_max_x))

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            L10 = int(L_func(10))
            vd_da_1_d = '\\True Lợi nhuận khi sản xuất 10 sản phẩm là %s (đồng)' % (L10)
            vd_da_1_s = 'Lợi nhuận khi sản xuất 10 sản phẩm là %s (đồng)' % (L10 + random.choice([10000, -10000, 20000, -20000]))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Hàm lợi nhuận: $L(x)=F(x)-C(x)=x^3 - %sx^2 + %sx \\Rightarrow L(10)=%s$.'''
            % (A+m, B-n, L10))

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Lợi nhuận lớn nhất đạt được khi sản xuất %s sản phẩm' % (l_max_x)
            vdc_da_1_s = 'Lợi nhuận lớn nhất đạt được khi sản xuất %s sản phẩm' % (l_max_x + random.choice([-1, 1, 2]))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Ta có: $L'(x)=3x^2 - %sx + %s = 0 \\Leftrightarrow \\left[ \\begin{array}{l} x \\approx %s \\\\ x \\approx %s \\end{array} \\right.$ và ta có bảng biến thiên như sau:
            \\begin{center}
            \\begin{tikzpicture}[line width=1pt]
            \\tkzTabInit[espcl=3.5,lgt=1.5]
            {$x$/1,$L'(x)$/0.7,$L(x)$/2.1}
            {$10$,{$%s$},$160$}
            \\tkzTabLine{,+,0,-,}
            \\tkzTabVar{-/ $%s$ ,+/ $%s$ ,-/ $%s$ }
            \\end{tikzpicture}
            \\end{center}
            Xét $L(%s)=%s %s L(%s)=%s$ nên lợi nhuận lớn nhất đạt được khi sản xuất $%s$ sản phẩm.'''
            % (2*(A+m), B-n, str_xL1, str_xL2, str_xL1, 
               int(L_func(10)), int(L_func(l_max_x)), int(L_func(160)),
               l_int1, L_val1, "<" if L_val1 < L_val2 else ">", l_int2, L_val2, l_max_x))

            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
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
                str(noidungcauhoi)+ '\n' +
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
                '\\end{ex}\n \\end{minipage}\n\n')
            return content


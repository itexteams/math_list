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


def bt_dang13_p2_b2_c6_ds10(self):
            # Khai báo biến
            # Khai báo biến
            p_x = random.choice([60, 70, 80])
            p_y = 100 - p_x
            h_x = random.choice([3, 4, 5])
            h_y = random.choice([1, 2])
            k_val = random.choice([2, 3])

            if k_val == 2:
                p_d_num, p_d_den = 1, 2
                p_dbar_num, p_dbar_den = 1, 2
            else:
                p_d_num, p_d_den = 1, 3
                p_dbar_num, p_dbar_den = 2, 3

            def num_to_comma_str(num):
                if isinstance(num, float):
                    return f"{num:g}".replace('.', ',')
                return str(num).replace('.', ',')

            def frac_to_latex(f):
                if f.denominator == 1:
                    return str(f.numerator)
                return "\\frac{%s}{%s}" % (f.numerator, f.denominator)

            str_px = num_to_comma_str(p_x / 100)
            str_py = num_to_comma_str(p_y / 100)
            str_hx = num_to_comma_str(h_x / 100)
            str_hy = num_to_comma_str(h_y / 100)
            str_hx_bar = num_to_comma_str(1 - h_x / 100)
            str_hy_bar = num_to_comma_str(1 - h_y / 100)

            P_D = frac(p_d_num, p_d_den)
            P_Dbar = frac(p_dbar_num, p_dbar_den)

            P_B_frac = P_D * 1 + P_Dbar * frac(p_y, 100)
            P_B_A_frac = P_D * frac(h_y, 100) + P_Dbar * frac(p_y, 100) * frac(h_y, 100)
            P_Bbar_A_frac = P_Dbar * frac(p_x, 100) * frac(h_x, 100)
            P_A_frac = P_B_A_frac + P_Bbar_A_frac
            P_B_given_A_frac = P_B_A_frac / P_A_frac
            P_A_given_B_frac = frac(h_y, 100)

            val_B_given_A = frac_to_latex(P_B_given_A_frac)
            val_A_given_B = num_to_comma_str(float(P_A_given_B_frac))
            val_B = num_to_comma_str(float(P_B_frac))
            val_B_false = num_to_comma_str(p_y / 100)
            val_A = num_to_comma_str(float(P_A_frac))
            val_A_false = num_to_comma_str(float(P_B_A_frac))

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một hệ thống siêu thị nhập khẩu cam từ hai nông trại X và Y. Nông trại X cung cấp $%s\\%%$ tổng lượng cam và có tỉ lệ quả hỏng là $%s\\%%$. Nông trại Y cung cấp phần còn lại và có tỉ lệ quả hỏng là $%s\\%%$. Để kiểm tra chất lượng, nhân viên dùng một con xúc xắc cân đối đồng chất để gieo ngẫu nhiên. Nếu số chấm xuất hiện chia hết cho $%s$ thì nhân viên sẽ chọn một quả cam từ lô hàng của nông trại Y và nếu số chấm xuất hiện không chia hết cho $%s$ thì nhân viên sẽ chọn ngẫu nhiên một quả cam từ kho chung (đã trộn lẫn cam của cả hai nông trại). Gọi $A$ là biến cố chọn được quả cam bị hỏng và $B$ là biến cố chọn được quả cam có nguồn gốc từ nông trại Y.'''
                             % (p_x, h_x, h_y, k_val, k_val))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True $P(B|A)=%s$' % (val_B_given_A)
            nb_da_1_s = '$P(B|A)=%s$' % (val_A_given_B)
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Gieo một con xúc xắc nên số phần tử của không gian mẫu là: $n(\\Omega)=6$ cách. \\\\
            Gọi $D$ là biến cố "Số chấm chia hết cho $%s$" nên $P(D)=\\frac{%s}{%s}$ và có sơ đồ cây như sau: \\\\
            \\begin{center}
            \\begin{tikzpicture}[>=latex, scale=1, line width=1pt]
            \\node (O) at (0,0) [circle,fill,inner sep=1.5pt] {};
            \\node (D) at (2.5,1.5) {$D$};
            \\node (Dbar) at (2.5,-1.5) {$\\overline{D}$};
            \\draw[->] (O) -- (D) node[midway,above left] {$\\frac{%s}{%s}$};
            \\draw[->] (O) -- (Dbar) node[midway,below left] {$\\frac{%s}{%s}$};
            \\node (B1) at (5,1.5) {$B$};
            \\draw[->] (D) -- (B1);
            \\node (A1) at (7.5, 2.2) {$A$};
            \\node (A1bar) at (7.5, 0.8) {$\\overline{A}$};
            \\draw[->] (B1) -- (A1) node[midway,above] {$%s$};
            \\draw[->] (B1) -- (A1bar) node[midway,below] {$%s$};
            \\node (Bbar) at (5,-0.5) {$\\overline{B}$};
            \\node (B2) at (5,-2.5) {$B$};
            \\draw[->] (Dbar) -- (Bbar) node[midway,above left] {$%s$};
            \\draw[->] (Dbar) -- (B2) node[midway,below left] {$%s$};
            \\node (A2) at (7.5, 0.2) {$A$};
            \\node (A2bar) at (7.5, -1.2) {$\\overline{A}$};
            \\draw[->] (Bbar) -- (A2) node[midway,above] {$%s$};
            \\draw[->] (Bbar) -- (A2bar) node[midway,below] {$%s$};
            \\node (A3) at (7.5, -1.8) {$A$};
            \\node (A3bar) at (7.5, -3.2) {$\\overline{A}$};
            \\draw[->] (B2) -- (A3) node[midway,above] {$%s$};
            \\draw[->] (B2) -- (A3bar) node[midway,below] {$%s$};
            \\end{tikzpicture}
            \\end{center}
            Xét mệnh đề a) \\\\
            Ta có: \\\\
            $\\begin{cases} P(B \\cap A) = \\frac{%s}{%s} \\cdot %s + \\frac{%s}{%s} \\cdot %s \\cdot %s = %s \\\\ P(A) = \\frac{%s}{%s} \\cdot %s + \\frac{%s}{%s} \\cdot (%s \\cdot %s + %s \\cdot %s) = %s \\end{cases}$ \\\\
            suy ra $P(B|A) = \\frac{P(B \\cap A)}{P(A)} = %s$.''' % (
                k_val, p_d_num, p_d_den,
                p_d_num, p_d_den, p_dbar_num, p_dbar_den,
                str_hy, str_hy_bar,
                str_px, str_py,
                str_hx, str_hx_bar,
                str_hy, str_hy_bar,
                p_d_num, p_d_den, str_hy, p_dbar_num, p_dbar_den, str_py, str_hy, num_to_comma_str(float(P_B_A_frac)),
                p_d_num, p_d_den, str_hy, p_dbar_num, p_dbar_den, str_px, str_hx, str_py, str_hy, val_A,
                val_B_given_A
            ))

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
            th_da_1_d = '\\True $P(B)=%s$' % (val_B)
            th_da_1_s = '$P(B)=%s$' % (val_B_false)
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Xét mệnh đề b) \\\\
            Ta có: $P(B) = \\frac{%s}{%s} \\cdot 1 + \\frac{%s}{%s} \\cdot %s = %s$.''' % (
                p_d_num, p_d_den, p_dbar_num, p_dbar_den, str_py, val_B
            ))

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
            vd_da_1_d = '\\True $P(A)=%s$' % (val_A)
            vd_da_1_s = '$P(A)=%s$' % (val_A_false)
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Xét mệnh đề c) \\\\
            Ta có: $P(A) = \\frac{%s}{%s} \\cdot %s + \\frac{%s}{%s} \\cdot (%s \\cdot %s + %s \\cdot %s) = %s$.''' % (
                p_d_num, p_d_den, str_hy, p_dbar_num, p_dbar_den, str_px, str_hx, str_py, str_hy, val_A
            ))

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
            vdc_da_1_d = '\\True $P(A|B)=%s$' % (val_A_given_B)
            vdc_da_1_s = '$P(A|B)=%s$' % (val_B_given_A)
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Xét mệnh đề d) \\\\
            Ta có: $P(A|B) = \\frac{P(A \\cap B)}{P(B)} = \\frac{%s}{%s} = %s$.''' % (
                num_to_comma_str(float(P_B_A_frac)), val_B, val_A_given_B
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


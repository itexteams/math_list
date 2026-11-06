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


def bt_dang14_p2_b2_c2_ds10(self):
            # Khai báo biến
            # Khai báo biến
            # Random thời gian may 1 áo (t_1) và 1 quần (t_2), thường may áo nhanh hơn
            t_1 = random.randint(1, 3)
            t_2 = random.randint(2, 4)
            while t_1 >= t_2:
                t_1 = random.randint(1, 3)
                t_2 = random.randint(2, 4)

            # Tỉ lệ giữa quần và áo k (áo không vượt quá 1/k quần -> k*x <= y)
            k = random.choice([2, 3])
            frac_str = "một nửa" if k == 2 else "một phần ba"

            # Tính toán toạ độ đỉnh C (x_0, y_0) là điểm tối ưu
            # Chọn x_0 chia hết cho t_2 để t_max chia hết cho t_2 (điểm D trên trục Oy là số nguyên)
            x_0 = t_2 * random.randint(3, 5)
            y_0 = k * x_0

            # Tổng thời gian tối đa
            t_max = t_1 * x_0 + t_2 * y_0

            # Số lượng tối thiểu q_min
            q_min_mult = random.randint(2, x_0 - 1)
            q_min = (k + 1) * q_min_mult

            # Toạ độ các đỉnh của miền nghiệm
            # A(0, q_min)
            A_x, A_y = 0, q_min
            # B(B_x, B_y) là giao của x+y = q_min và y = kx
            B_x = q_min // (k + 1)
            B_y = k * B_x
            # C(x_0, y_0)
            C_x, C_y = x_0, y_0
            # D(0, D_y) là giao của t_1*x + t_2*y = t_max và x = 0
            D_x, D_y = 0, t_max // t_2

            # Random tiền công p_1, p_2 (nghìn đồng)
            # Đảm bảo đỉnh C luôn là lớn nhất: p_1/p_2 > t_1/t_2 => p_1*t_2 > p_2*t_1
            p_1 = random.randint(15, 30) * 10
            p_2 = random.randint(20, 40) * 10
            while p_1 * t_2 <= p_2 * t_1:
                p_1 += 10

            # Các giá trị hàm mục tiêu tại các đỉnh
            T_A = p_2 * A_y
            T_B = p_1 * B_x + p_2 * B_y
            T_C = p_1 * C_x + p_2 * C_y
            T_D = p_2 * D_y

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một người thợ may cần may một số áo và quần thể thao. Để may xong một cái áo người thợ mất %s giờ và để may xong một cái quần mất %s giờ. Người thợ may phải hoàn thành công việc trong thời gian không quá %s giờ. Tổng số lượng áo và quần mà người thợ cần may ít nhất là %s cái và số lượng áo không vượt quá %s số lượng quần. Biết tiền công may một cái áo là %s nghìn đồng, một cái quần là %s nghìn đồng. Gọi $x$ và $y$ ($x,y \\in \\mathbb{N}$) lần lượt là số áo và số quần mà người thợ may làm được.'''               
                             % (t_1, t_2, t_max, q_min, frac_str, p_1, p_2))

            ######################################################################## Nhận biết ############################################
            nb_da_1_d = '\\True Số tiền công người thợ may thu được là $T(x;y)=%sx+%sy$ nghìn đồng' % (p_1, p_2)
            nb_da_1_s = 'Số tiền công người thợ may thu được là $T(x;y)=%sx+%sy$ nghìn đồng' % (p_2, p_1)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)
            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = ('''Số tiền công người thợ thu được khi may $x$ cái áo và $y$ cái quần là $T(x;y)=%sx+%sy$ (nghìn đồng).'''
                            % (p_1, p_2))
            list_nb_2 = [loigiai_nb_1]

            ######################################################################## Thông hiểu ############################################
            th_da_1_d = '\\True $x+y \\ge %s$' % (q_min)
            th_da_1_s = '$x+y \\le %s$' % (q_min)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)
            list_th_1 = [th_da_1]

            loigiai_th_1 = ('''Tổng số lượng áo và quần người thợ cần may ít nhất là $%s$ cái, do đó ta có bất phương trình $x+y \\ge %s$.'''       
                       % (q_min, q_min))
            list_th_2 = [loigiai_th_1]

            ######################################################################## Vận dụng ############################################
            vd_da_1_d = '\\True $%sx+%sy \\le %s$' % (t_1, t_2, t_max)
            vd_da_1_s = '$%sx+%sy \\le %s$' % (t_2, t_1, t_max)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)
            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = ('''Thời gian may $x$ cái áo là $%sx$ (giờ), thời gian may $y$ cái quần là $%sy$ (giờ). \\\\
            Tổng thời gian may không quá $%s$ giờ nên ta có bất phương trình $%sx+%sy \\le %s$.'''  
                       % (t_1, t_2, t_max, t_1, t_2, t_max))
            list_vd_2 = [loigiai_vd_1]

            ######################################################################## Vận dụng cao ############################################

            # Cài đặt giới hạn đồ thị TikZ an toàn trong phạm vi nhìn thấy
            view_xmax = C_x + 8
            view_ymax = max(D_y, C_y) + 8

            scale_x = round(5.0 / view_xmax, 3)
            scale_y = round(5.0 / view_ymax, 3)

            # Tính toạ độ các đường thẳng trong phạm vi hiển thị
            line1_y_start = q_min + 2
            line1_y_end = q_min - view_xmax

            line2_y_start = (t_max + 2 * t_1) / t_2
            line2_y_end = (t_max - t_1 * view_xmax) / t_2

            line3_x_end = view_ymax / k

            vdc_da_1_d = '\\True Để thu được tiền công lớn nhất thì người thợ phải may $%s$ cái áo và $%s$ cái quần' % (C_x, C_y)
            vdc_da_1_s = 'Để thu được tiền công lớn nhất thì người thợ phải may $%s$ cái áo và $%s$ cái quần' % (D_x, D_y)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)
            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = ('''Từ giả thiết ta có hệ bất phương trình:
            $\\begin{cases} x \\ge 0, y \\ge 0 \\\\ x + y \\ge %s \\\\ %sx + %sy \\le %s \\\\ %sx - y \\le 0 \\end{cases}$. \\\\
            Miền nghiệm của hệ bất phương trình là miền tứ giác $ABCD$ (phần không bị gạch chéo, bao gồm cả biên). \\\\
            \\begin{center}
            \\begin{tikzpicture}[>=stealth, x=%scm, y=%scm, line width=1pt]
            \\draw[->] (-2,0) -- (%s,0) node[below] {$x$};
            \\draw[->] (0,-2) -- (0,%s) node[left] {$y$};
            \\node at (0,0) [below left] {$O$};
            \\begin{scope}
            \\clip (-2,-2) rectangle (%s,%s);
            \\fill[pattern=north east lines, pattern color=black!60] (-2,-2) rectangle (%s,%s);
            \\fill[white] (0,%s) -- (%s,%s) -- (%s,%s) -- (0,%s) -- cycle;
            \\draw[black] (-2, %s) -- (%s, %s);
            \\draw[black] (-2, %s) -- (%s, %s);
            \\draw[black] (-2, %s) -- (%s, %s);
            \\end{scope}
            \\coordinate (A) at (0,%s);
            \\coordinate (B) at (%s,%s);
            \\coordinate (C) at (%s,%s);
            \\coordinate (D) at (0,%s);
            \\node at (A) [left] {$A(0;%s)$};
            \\node at (B) [below] {$B(%s;%s)$};
            \\node at (C) [right] {$C(%s;%s)$};
            \\node at (D) [left] {$D(0;%s)$};
            \\fill (A) circle (1.5pt);
            \\fill (B) circle (1.5pt);
            \\fill (C) circle (1.5pt);
            \\fill (D) circle (1.5pt);
            \\end{tikzpicture}
            \\end{center}
            Ta tính giá trị của biểu thức $T(x;y)=%sx+%sy$ tại các đỉnh của tứ giác: \\\\
            Tại $A(0;%s) \\Rightarrow T = %s \\cdot 0 + %s \\cdot %s = %s$. \\\\
            Tại $B(%s;%s) \\Rightarrow T = %s \\cdot %s + %s \\cdot %s = %s$. \\\\
            Tại $C(%s;%s) \\Rightarrow T = %s \\cdot %s + %s \\cdot %s = %s$. \\\\
            Tại $D(0;%s) \\Rightarrow T = %s \\cdot 0 + %s \\cdot %s = %s$. \\\\
            Vậy số tiền công lớn nhất thu được là $%s$ nghìn đồng khi may $%s$ cái áo và $%s$ cái quần.'''
                       % (q_min, t_1, t_2, t_max, k, scale_x, scale_y, view_xmax, view_ymax,
                          view_xmax, view_ymax, view_xmax, view_ymax,
                          A_y, B_x, B_y, C_x, C_y, D_y,
                          line1_y_start, view_xmax, line1_y_end,
                          line2_y_start, view_xmax, line2_y_end,
                          -2 * k, line3_x_end, view_ymax,
                          A_y, B_x, B_y, C_x, C_y, D_y,
                          A_y, B_x, B_y, C_x, C_y, D_y,
                          p_1, p_2,
                          A_y, p_1, p_2, A_y, T_A,
                          B_x, B_y, p_1, B_x, p_2, B_y, T_B,
                          C_x, C_y, p_1, C_x, p_2, C_y, T_C,
                          D_y, p_1, p_2, D_y, T_D,
                          T_C, C_x, C_y))

            list_vdc_2 = [loigiai_vdc_1]

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
                '\\begin{ex}\n' +
                str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(shuffled_answers_nb[0]) + '}\n'
                '{' + str(shuffled_answers_th[0]) + '}\n'
                '{' + str(shuffled_answers_vd[0]) + '}\n'
                '{' + str(shuffled_answers_vdc[0]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(shuffled_solutions_nb[0]) + '\n'
                '\\item ' + str(shuffled_solutions_th[0]) + '\n'
                '\\item ' + str(shuffled_solutions_vd[0]) + '\n'
                '\\item ' + str(shuffled_solutions_vdc[0]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n\\end{minipage}\n\n')
            return content


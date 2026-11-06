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


def bt_dang18_p2_b2_c2_ds10(self):
            # Khai báo biến
            # Hàm hỗ trợ định dạng biểu thức bậc nhất ax + by + c
            def fmt_expr(a, b, c):
                res = ""
                if a == 1:
                    res += "x"
                elif a == -1:
                    res += "-x"
                elif a != 0:
                    res += "%sx" % a

                if b > 0:
                    if res != "":
                        res += " + "
                    if b == 1:
                        res += "y"
                    else:
                        res += "%sy" % b
                elif b < 0:
                    if res != "":
                        res += " - "
                    else:
                        res += "-"
                    if b == -1:
                        res += "y"
                    else:
                        res += "%sy" % (-b)

                if c > 0:
                    res += " + %s" % c
                elif c < 0:
                    res += " - %s" % (-c)

                return res

            # Định dạng phân số
            def format_frac(num):
                if num.denominator == 1:
                    return str(num.numerator)
                if num.numerator > 0:
                    return "\\frac{%s}{%s}" % (num.numerator, num.denominator)
                else:
                    return "-\\frac{%s}{%s}" % (-num.numerator, num.denominator)

            # Khai báo biến và tạo ngẫu nhiên
            # Đảm bảo tạo ra một hệ có miền nghiệm là tam giác
            while True:
                a1 = random.randint(1, 3)
                b1 = random.randint(1, 3)
                c1 = random.randint(-6, -2) # ax + by + c <= 0

                a2 = random.randint(1, 3)
                b2 = random.randint(-3, -1)
                c2 = random.randint(-4, -1) # ax - by + c <= 0

                D = a1 * b2 - a2 * b1
                if D == 0: continue

                # Giao điểm của d1 và d2
                xB = frac(-c1*b2 + c2*b1, D)
                yB = frac(-a1*c2 + a2*c1, D)

                if xB <= 0: continue

                # Giao điểm d1 với trục Oy
                yA = frac(-c1, b1)

                # Giao điểm d2 với trục Oy
                yC = frac(-c2, b2)

                if yA <= yC: continue
                break

            expr1 = fmt_expr(a1, b1, c1)
            expr2 = fmt_expr(a2, b2, c2)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hệ bất phương trình $\\begin{cases} %s \\le 0 \\\\ x \\ge 0 \\\\ %s \\le 0 \\end{cases}$.''' % (expr1, expr2))

            ######################################################################## Nhận biết ############################################
            nb_da_1_d = '\\True Hệ trên là hệ bất phương trình bậc nhất hai ẩn'
            nb_da_1_s = 'Hệ trên không phải là hệ bất phương trình bậc nhất hai ẩn'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = ('''Hệ gồm các bất phương trình bậc nhất hai ẩn $x$ và $y$ nên hệ trên là hệ bất phương trình bậc nhất hai ẩn.''')

            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            th_da_1_d = '\\True Hệ bất phương trình có nghiệm'
            th_da_1_s = 'Hệ bất phương trình vô nghiệm'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            v1 = a1 * 0 + b1 * float(yB) + c1
            v2 = a2 * 0 + b2 * float(yB) + c2
            is_M_sol = (0 >= 0) and (v1 <= 0) and (v2 <= 0)

            loigiai_th_1 = ('''Ta thấy tọa độ $(0; %s)$ thỏa mãn cả 3 bất phương trình của hệ: $0 \\ge 0$, $%s \\cdot 0 + %s \\cdot %s %s \\le 0$ và $%s \\cdot 0 + %s \\cdot %s %s \\le 0$. Vậy hệ bất phương trình có nghiệm.''' % (format_frac(yB), a1, b1, format_frac(yB), ("+ %s" % c1 if c1 > 0 else "- %s" % (-c1)), a2, b2, format_frac(yB), ("+ %s" % c2 if c2 > 0 else "- %s" % (-c2))))

            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Điểm M nằm trên trục Oy, ta chọn một điểm bất kỳ
            yM = yC
            xM = 0

            is_M_sol = (xM >= 0) and (a1*xM + b1*yM + c1 <= 0) and (a2*xM + b2*yM + c2 <= 0)

            if is_M_sol:
                vd_da_1_d = '\\True Điểm $M\\left(0; %s\\right)$ thuộc miền nghiệm hệ bất phương trình' % format_frac(yM)
                vd_da_1_s = 'Điểm $M\\left(0; %s\\right)$ không thuộc miền nghiệm hệ bất phương trình' % format_frac(yM)
            else:
                vd_da_1_d = '\\True Điểm $M\\left(0; %s\\right)$ không thuộc miền nghiệm hệ bất phương trình' % format_frac(yM)
                vd_da_1_s = 'Điểm $M\\left(0; %s\\right)$ thuộc miền nghiệm hệ bất phương trình' % format_frac(yM)

            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            str_thuoc = "thuộc" if is_M_sol else "không thuộc"
            loigiai_vd_1 = ('''Thay tọa độ điểm $M\\left(0; %s\\right)$ vào hệ ta thấy nó %s tất cả các bất phương trình nên $M$ %s miền nghiệm của hệ.''' % (format_frac(yM), "thỏa mãn" if is_M_sol else "không thỏa mãn", str_thuoc))

            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            vdc_da_1_d = '\\True Miền nghiệm của hệ bất phương trình là miền tam giác'
            vdc_da_1_s = 'Miền nghiệm của hệ bất phương trình không phải là miền tam giác'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = ('''Vẽ các đường thẳng $d_1: %s = 0$, $d_2: x = 0$ (trục tung), $d_3: %s = 0$ trên cùng một hệ trục tọa độ. \\\\
            Giao điểm của các đường thẳng là $A(0; %s)$, $B\\left(%s; %s\\right)$, $C(0; %s)$. \\\\
            Xác định các nửa mặt phẳng nghiệm, ta thấy miền nghiệm chung của hệ là phần mặt phẳng giới hạn bởi tam giác $ABC$ (kể cả biên). Vậy miền nghiệm của hệ là miền tam giác. \\\\
            \\begin{center}
            \\begin{tikzpicture}[>=stealth, scale=1, line width=1pt]
            \\node at (0,0) [below left] {$O$};
            \\clip (-2,-2) rectangle (4,4);
            \\fill[pattern=north east lines, pattern color=black] (-2,-2) rectangle (4,4);
            \\fill[white] (0, %s) -- (%s, %s) -- (0, %s) -- cycle;
            \\draw[black] (-2, %s) -- (4, %s);
            \\draw[black] (-2, %s) -- (4, %s);
            \\draw[black] (0, -2) -- (0, 4);
            \\draw[->] (-2, 0) -- (4, 0) node[below] {$x$};
            \\draw[->] (0, -2) -- (0, 4) node[left] {$y$};
            \\end{tikzpicture}
            \\end{center}''' % (expr1, expr2, format_frac(yA), format_frac(xB), format_frac(yB), format_frac(yC), float(yA), float(xB), float(yB), float(yC), float((-c1-a1*(-2))/b1), float((-c1-a1*4)/b1), float((-c2-a2*(-2))/b2), float((-c2-a2*4)/b2)))

            list_vdc_2 = [loigiai_vdc_1]

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


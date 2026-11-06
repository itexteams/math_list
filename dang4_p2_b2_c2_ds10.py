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


def bt_dang4_p2_b2_c2_ds10(self):
            # Khai báo biến
            # Hàm bổ trợ: Định dạng số theo chuẩn Việt Nam (chuyển dấu chấm thành dấu phẩy)
            def fmt_vn(val):
                if isinstance(val, sp.Rational):
                    if val.q == 1:
                        return str(val.p)
                    else:
                        return str(round(float(val), 2)).replace('.', ',')
                elif isinstance(val, (int, float)):
                    if int(val) == val:
                        return str(int(val))
                    return str(round(val, 2)).replace('.', ',')
                return str(val)

            # ------------------------------------------------------------------------
            # TẠO ĐỀ BÀI NGẪU NHIÊN VÀ TÍNH TOÁN TOÁN HỌC
            # ------------------------------------------------------------------------
            while True:
                # A: Diện tích đất, d1: công trồng rau, d2: công trồng dưa
                A = random.choice([4, 5, 6, 8, 10])
                d1 = random.choice([10, 15, 20])
                d2 = random.choice([20, 25, 30, 40])
                if d1 >= d2: 
                    continue # Phải đảm bảo công trồng dưa tốn hơn rau để tạo đa giác

                # D_months: số tháng hè. D: Tổng ngày công tối đa
                D_months = random.choice([2, 3, 4, 5])
                D = D_months * 30

                # Điều kiện để giao điểm 2 đường thẳng nằm trên hệ trục toạ độ dương
                if not (d1 * A < D < d2 * A): 
                    continue

                # p1, p2: Lợi nhuận mỗi ha rau và dưa (triệu đồng)
                p1 = random.randint(2, 6)
                p2 = random.randint(4, 9)

                # Tính toạ độ các đỉnh của tứ giác miền nghiệm OABC
                xB = sp.Rational(d2 * A - D, d2 - d1)
                yB = sp.Rational(D - d1 * A, d2 - d1)

                prof_O = 0
                prof_A = p1 * A
                prof_C = p2 * sp.Rational(D, d2)
                prof_B = p1 * xB + p2 * yB

                profits = [
                    (0, 0, prof_O, "O"),
                    (A, 0, prof_A, "A"),
                    (0, sp.Rational(D, d2), prof_C, "C"),
                    (xB, yB, prof_B, "B")
                ]

                max_prof_val = max(p[2] for p in profits)
                max_points = [p for p in profits if p[2] == max_prof_val]

                if len(max_points) == 1:
                    opt_x, opt_y, opt_prof, opt_name = max_points[0]
                    break

            # Nội dung câu hỏi
            noidungcauhoi = (f'''Dịp nghỉ hè, một gia đình thầy giáo dự định trồng $x$ (ha) rau và $y$ (ha) dưa leo trên một mảnh đất có diện tích ${A}$ ha. Nếu trồng 1 (ha) rau thì cần ${d1}$ ngày công và thu lợi ${p1}$ triệu. Nếu trồng 1 (ha) dưa leo thì cần ${d2}$ ngày công và thu lợi ${p2}$ triệu. Biết rằng, gia đình thầy chỉ có thể sử dụng ${D_months}$ tháng hè (tương đương không quá ${D}$ ngày công) để trồng rau và dưa leo.''')

            # ------------------------------------------------------------------------
            # Nhận biết (Mệnh đề a)
            # ------------------------------------------------------------------------
            sys_correct = f"\\begin{{cases}} x \\ge 0 \\\\ y \\ge 0 \\\\ x + y \\le {A} \\\\ {d1}x + {d2}y \\le {D} \\end{{cases}}"
            sys_wrong = f"\\begin{{cases}} x \\ge 0 \\\\ y \\ge 0 \\\\ x + y \\le {D} \\\\ {d1}x + {d2}y \\le {A} \\end{{cases}}"

            nb_da_1_d = f"\\True Hệ bất phương trình bậc nhất hai ẩn thể hiện mối quan hệ giữa $x$ và $y$ là ${sys_correct}$"
            nb_da_1_s = f"Hệ bất phương trình bậc nhất hai ẩn thể hiện mối quan hệ giữa $x$ và $y$ là ${sys_wrong}$"

            loigiai_nb_1_d = f"Đúng. Dựa vào điều kiện diện tích ($x+y \\le {A}$) và ngày công (${d1}x+{d2}y \\le {D}$), kết hợp điều kiện không âm của diện tích, ta có hệ bất phương trình: ${sys_correct}$."
            loigiai_nb_1_s = f"Sai. Dựa vào điều kiện diện tích ($x+y \\le {A}$) và ngày công (${d1}x+{d2}y \\le {D}$), kết hợp điều kiện không âm, hệ bất phương trình đúng phải là: ${sys_correct}$."

            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            # ------------------------------------------------------------------------
            # Thông hiểu (Mệnh đề b)
            # ------------------------------------------------------------------------
            while True:
                xt_d, yt_d = random.randint(1, A-1), random.randint(1, A-1)
                if (xt_d + yt_d <= A) and (d1*xt_d + d2*yt_d <= D):
                    break
            while True:
                xt_s, yt_s = random.randint(1, A+2), random.randint(1, A+2)
                if (xt_s + yt_s > A) or (d1*xt_s + d2*yt_s > D):
                    break

            th_da_1_d = f"\\True Gia đình thầy có thể trồng ${xt_d}$ (ha) rau và ${yt_d}$ (ha) dưa leo trên một mảnh đất này"
            th_da_1_s = f"Gia đình thầy có thể trồng ${xt_s}$ (ha) rau và ${yt_s}$ (ha) dưa leo trên một mảnh đất này"

            loigiai_th_1_d = f"Đúng. Vì số ngày công cần để trồng là ${d1} \\cdot {xt_d} + {d2} \\cdot {yt_d} = {d1*xt_d + d2*yt_d} \\le {D}$ (ngày), và tổng diện tích ${xt_d} + {yt_d} = {xt_d+yt_d} \\le {A}$ (ha) thỏa mãn điều kiện."
            if xt_s + yt_s > A:
                loigiai_th_1_s = f"Sai. Tổng diện tích trồng là ${xt_s} + {yt_s} = {xt_s+yt_s}$ (ha) $> {A}$ (ha), vượt quá diện tích tối đa của mảnh đất."
            else:
                loigiai_th_1_s = f"Sai. Số ngày công gia đình thầy cần để trồng ${xt_s}$ (ha) rau và ${yt_s}$ (ha) dưa leo là: ${d1} \\cdot {xt_s} + {d2} \\cdot {yt_s} = {d1*xt_s + d2*yt_s}$ (ngày), vượt quá số ngày công tối đa (${D}$ ngày)."

            list_th_da_1 = [th_da_1_d, th_da_1_s]

            # ------------------------------------------------------------------------
            # TẠO CODE TIKZ CHO MIỀN NGHIỆM (Sử dụng chuỗi raw r''' để tránh lỗi mất dấu \)
            # ------------------------------------------------------------------------
            x_b_tkz = round(float(xB), 2)
            y_b_tkz = round(float(yB), 2)
            y_c_tkz = round(float(D/d2), 2)

            x_min, y_min = -1.5, -1.5
            x_max = round(max(A, float(D/d1)) + 2.0, 2)
            y_max = round(max(A, float(D/d2)) + 2.0, 2)

            y_L1_start = round(A - x_min, 2)
            y_L1_end = round(A - x_max, 2)
            y_L2_start = round((D - d1*x_min)/d2, 2)
            y_L2_end = round((D - d1*x_max)/d2, 2)

            # Sử dụng r''' kết hợp format thủ công tránh xung đột cú pháp Python
            tikz_code = (
                "\\begin{center}\n"
                "\\begin{tikzpicture}[>=stealth, scale=0.4]\n"
                f"\\clip ({x_min-4}, {y_min}) rectangle ({x_max}, {y_max});\n"
                f"\\fill[pattern=north east lines, pattern color=black!40] ({x_min},{y_min}) rectangle (0, {y_max});\n"
                f"\\fill[pattern=north east lines, pattern color=black!40] ({x_min},{y_min}) rectangle ({x_max}, 0);\n"
                f"\\fill[pattern=north east lines, pattern color=black!40] ({x_min}, {y_L1_start}) -- ({x_max}, {y_L1_end}) -- ({x_max}, {y_max}) -- ({x_min}, {y_max}) -- cycle;\n"
                f"\\fill[pattern=north east lines, pattern color=black!40] ({x_min}, {y_L2_start}) -- ({x_max}, {y_L2_end}) -- ({x_max}, {y_max}) -- ({x_min}, {y_max}) -- cycle;\n"
                f"\\draw[->] (-1, 0) -- ({x_max - 0.5}, 0) node[below] {{$x$}};\n"
                f"\\draw[->] (0, -1) -- (0, {y_max - 0.5}) node[left] {{$y$}};\n"
                "\\node at (0,0) [below left] {{$O$}};\n"
                f"\\draw[thick] ({x_min}, {y_L1_start}) -- ({x_max}, {y_L1_end});\n"
                f"\\draw[thick] ({x_min}, {y_L2_start}) -- ({x_max}, {y_L2_end});\n"
                f"\\coordinate (A) at ({A}, 0);\n"
                f"\\coordinate (B) at ({x_b_tkz}, {y_b_tkz});\n"
                f"\\coordinate (C) at (0, {y_c_tkz});\n"
                f"\\fill (A) circle (1.5pt) node[below left] {{$A({fmt_vn(A)}; 0)$}};\n"
                f"\\fill (B) circle (1.5pt) node[above right] {{$B({fmt_vn(xB)}; {fmt_vn(yB)})$}};\n"
                f"\\fill (C) circle (1.5pt) node[below left] {{$C(0; {fmt_vn(sp.Rational(D, d2))})$}};\n"
                "\\end{tikzpicture}\n"
                "\\end{center}\n"
            )

            # ------------------------------------------------------------------------
            # Vận dụng (Mệnh đề c)
            # ------------------------------------------------------------------------
            other_vertices = [p for p in profits if p[3] != opt_name and p[3] != "O"]
            false_opt = random.choice(other_vertices)

            vd_da_1_d = f"\\True Gia đình thầy cần trồng ${fmt_vn(opt_x)}$ (ha) rau và ${fmt_vn(opt_y)}$ (ha) dưa leo trên mảnh đất này để thu được lợi nhuận lớn nhất"
            vd_da_1_s = f"Gia đình thầy cần trồng ${fmt_vn(false_opt[0])}$ (ha) rau và ${fmt_vn(false_opt[1])}$ (ha) dưa leo trên mảnh đất này để thu được lợi nhuận lớn nhất"

            sol_vd_base = (
                f"Miền nghiệm của hệ bất phương trình là tứ giác $OABC$ với $O(0;0)$, "
                f"$A({fmt_vn(A)};0)$, $B({fmt_vn(xB)};{fmt_vn(yB)})$, $C(0;{fmt_vn(sp.Rational(D, d2))})$.\n"
                f"{tikz_code}"
                f" Lợi nhuận thu được khi trồng $x$ (ha) rau và $y$ (ha) dưa leo là $P(x; y) = {p1}x + {p2}y$.\n"
                f" $P(0; 0) = 0$; $P({fmt_vn(A)}; 0) = {p1} \\cdot {fmt_vn(A)} + {p2} \\cdot 0 = {fmt_vn(prof_A)}$;\n"
                f" $P({fmt_vn(xB)}; {fmt_vn(yB)}) = {p1} \\cdot {fmt_vn(xB)} + {p2} \\cdot {fmt_vn(yB)} = {fmt_vn(prof_B)}$; "
                f"$P(0; {fmt_vn(sp.Rational(D, d2))}) = {p1} \\cdot 0 + {p2} \\cdot {fmt_vn(sp.Rational(D, d2))} = {fmt_vn(prof_C)}$.\n"
                f" Vậy gia đình cần trồng ${fmt_vn(opt_x)}$ (ha) rau và ${fmt_vn(opt_y)}$ (ha) dưa leo để thu được lợi nhuận lớn nhất."
            )

            loigiai_vd_1_d = f"Đúng. \n {sol_vd_base}"
            loigiai_vd_1_s = f"Sai. \n {sol_vd_base} Phương án đề bài đưa ra không phải là tối ưu."

            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            # ------------------------------------------------------------------------
            # Vận dụng cao (Mệnh đề d)
            # ------------------------------------------------------------------------
            vdc_da_1_d = f"\\True Lợi nhuận lớn nhất gia đình thầy có thể thu được khi trồng rau và dưa leo trên mảnh đất này là ${fmt_vn(opt_prof)}$ triệu đồng"
            vdc_da_1_s = f"Lợi nhuận lớn nhất gia đình thầy có thể thu được khi trồng rau và dưa leo trên mảnh đất này là ${fmt_vn(false_opt[2])}$ triệu đồng"

            loigiai_vdc_1_d = f"Đúng. Dựa vào bảng tính giá trị lợi nhuận $P(x; y)$ tại các đỉnh ở câu trên, ta thấy lợi nhuận lớn nhất đạt được là ${fmt_vn(opt_prof)}$ triệu đồng."
            loigiai_vdc_1_s = f"Sai. Dựa vào bảng tính giá trị lợi nhuận $P(x; y)$ tại các đỉnh ở câu trên, ta thấy lợi nhuận lớn nhất đạt được phải là ${fmt_vn(opt_prof)}$ triệu đồng, không phải ${fmt_vn(false_opt[2])}$ triệu đồng."

            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            # ------------------------------------------------------------------------
            # XỬ LÝ SỐ LƯỢNG ĐÁP ÁN ĐÚNG VÀ XUẤT LATEX
            # ------------------------------------------------------------------------
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                nb_index = list_nb_da_1.index(nb_da_1)

                th_da_1 = random.choice(list_th_da_1)
                th_index = list_th_da_1.index(th_da_1)

                vd_da_1 = random.choice(list_vd_da_1)
                vd_index = list_vd_da_1.index(vd_da_1)

                vdc_da_1 = random.choice(list_vdc_da_1)
                vdc_index = list_vdc_da_1.index(vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                if 1 <= count_true_answers(answers) <= 3:
                    break

            list_nb_1 = [nb_da_1]
            list_nb_2 = [[loigiai_nb_1_d, loigiai_nb_1_s][nb_index]]

            list_th_1 = [th_da_1]
            list_th_2 = [[loigiai_th_1_d, loigiai_th_1_s][th_index]]

            list_vd_1 = [vd_da_1]
            list_vd_2 = [[loigiai_vd_1_d, loigiai_vd_1_s][vd_index]]

            list_vdc_1 = [vdc_da_1]
            list_vdc_2 = [[loigiai_vdc_1_d, loigiai_vdc_1_s][vdc_index]]

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

            # Xuất kết quả
            content = (
                '\\begin{minipage}{\\textwidth}\n'
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
                '\\end{ex}\n'
                '\\end{minipage}\n\n')
            return content


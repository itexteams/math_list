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


def bt_dang5_p2_b2_c2_ds10(self):
            # Khai báo biến
            # CÁC HÀM BỔ TRỢ XỬ LÝ TOÁN HỌC VÀ FORMAT CHUỖI
            # ------------------------------------------------------------------------
            def format_eq(a, b):
                terms = []
                if a != 0:
                    if a == 1: terms.append("x")
                    elif a == -1: terms.append("-x")
                    else: terms.append(f"{a}x")

                if b != 0:
                    if b == 1:
                        terms.append("+y" if a != 0 else "y")
                    elif b == -1:
                        terms.append("-y")
                    else:
                        if b > 0 and a != 0:
                            terms.append(f"+{b}y")
                        else:
                            terms.append(f"{b}y")

                res = "".join(terms)
                res = res.replace("+-", "-")
                if res.startswith("+"): res = res[1:]
                return res if res else "0"

            def get_line_eq(p1, p2, p_inside):
                x1, y1 = p1
                x2, y2 = p2
                dx = x2 - x1
                dy = y2 - y1

                a = dy
                b = -dx
                c = dy * x1 - dx * y1

                g = math.gcd(abs(a), math.gcd(abs(b), abs(c)))
                a //= g
                b //= g
                c //= g

                if a < 0 or (a == 0 and b < 0):
                    a, b, c = -a, -b, -c

                val = a * p_inside[0] + b * p_inside[1]
                if val <= c:
                    sign = r'\le'
                    is_less = True
                else:
                    sign = r'\ge'
                    is_less = False

                return a, b, c, sign, is_less

            def get_giant_invalid_polygon(a, b, c, is_less):
                if b != 0:
                    x1, x2 = -50, 50
                    y1 = (c - a * x1) / b
                    y2 = (c - a * x2) / b
                else:
                    y1, y2 = -50, 50
                    x1 = c / a
                    x2 = c / a

                sgn = 1 if is_less else -1
                length = math.sqrt(a*a + b*b)
                nx = (a / length) * sgn * 100
                ny = (b / length) * sgn * 100

                p1 = (x1, y1)
                p2 = (x2, y2)
                p3 = (x2 + nx, y2 + ny)
                p4 = (x1 + nx, y1 + ny)

                return f"\\fill[pattern=north west lines, pattern color=black!40] ({p1[0]:.2f}, {p1[1]:.2f}) -- ({p2[0]:.2f}, {p2[1]:.2f}) -- ({p3[0]:.2f}, {p3[1]:.2f}) -- ({p4[0]:.2f}, {p4[1]:.2f}) -- cycle;"

            def get_line_path(a, b, c, xmin, xmax, ymin, ymax):
                pts = []
                if b != 0:
                    y1 = (c - a*xmin)/b
                    if ymin <= y1 <= ymax: pts.append((xmin, y1))
                    y2 = (c - a*xmax)/b
                    if ymin <= y2 <= ymax: pts.append((xmax, y2))
                if a != 0:
                    x1 = (c - b*ymin)/a
                    if xmin <= x1 <= xmax: pts.append((x1, ymin))
                    x2 = (c - b*ymax)/a
                    if xmin <= x2 <= xmax: pts.append((x2, ymax))

                unique_pts = []
                for p in pts:
                    if not any(math.isclose(p[0], up[0], abs_tol=1e-5) and math.isclose(p[1], up[1], abs_tol=1e-5) for up in unique_pts):
                        unique_pts.append(p)

                if len(unique_pts) >= 2:
                    return f"\\draw[thick] ({unique_pts[0][0]:.2f}, {unique_pts[0][1]:.2f}) -- ({unique_pts[1][0]:.2f}, {unique_pts[1][1]:.2f});"
                return ""

            # ------------------------------------------------------------------------
            # TẠO ĐỀ BÀI NGẪU NHIÊN 
            # ------------------------------------------------------------------------
            while True:
                xA, yA = random.randint(-4, -1), 0
                xD, yD = random.randint(0, 2), random.randint(2, 5)
                xC = random.randint(xD + 1, xD + 4)
                yC = random.randint(yD - 2, yD + 2)
                if yC <= 0: continue
                xB, yB = random.randint(xC + 1, xC + 5), 0

                mAD = (yD - yA) / (xD - xA) if xD != xA else 999
                mDC = (yC - yD) / (xC - xD) if xC != xD else 999
                mCB = (yB - yC) / (xB - xC) if xB != xC else -999

                if mAD > mDC > mCB:
                    break

            A, B, C, D = (xA, yA), (xB, yB), (xC, yC), (xD, yD)
            xM, yM = (xA + xB + xC + xD) / 4, (yA + yB + yC + yD) / 4
            M = (xM, yM)

            a1, b1, c1, sign1, is_less1 = get_line_eq(A, D, M)
            a2, b2, c2, sign2, is_less2 = get_line_eq(D, C, M)
            a3, b3, c3, sign3, is_less3 = get_line_eq(C, B, M)

            eq1_str = f"{format_eq(a1, b1)} {sign1} {c1}"
            eq2_str = f"{format_eq(a2, b2)} {sign2} {c2}"
            eq3_str = f"{format_eq(a3, b3)} {sign3} {c3}"

            while True:
                alpha, beta = random.randint(-3, 3), random.randint(-3, 3)
                if alpha != 0 or beta != 0:
                    F_A, F_B = alpha * xA + beta * yA, alpha * xB + beta * yB
                    F_C, F_D = alpha * xC + beta * yC, alpha * xD + beta * yD
                    min_F = min(F_A, F_B, F_C, F_D)
                    if -15 <= min_F <= 15:
                        break

            F_str = format_eq(alpha, beta)
            ans_count = min_F - (-20) + 1
            m_list_str = f"-20; -19; -18; \\dots; {min_F}" if ans_count > 6 else "; ".join(str(i) for i in range(-20, min_F + 1))
            latex_m_membership = "m \\in \\{" + m_list_str + "\\}"

            # TIKZ DRAWING CODE
            xmin, xmax = min(xA, xB, xC, xD) - 2, max(xA, xB, xC, xD) + 2
            ymin, ymax = -2, max(yA, yB, yC, yD) + 2

            fill1 = get_giant_invalid_polygon(a1, b1, c1, is_less1)
            fill2 = get_giant_invalid_polygon(a2, b2, c2, is_less2)
            fill3 = get_giant_invalid_polygon(a3, b3, c3, is_less3)
            fill_y = f"\\fill[pattern=north west lines, pattern color=black!40] ({xmin}, 0) -- ({xmax}, 0) -- ({xmax}, -50) -- ({xmin}, -50) -- cycle;"

            draw1 = get_line_path(a1, b1, c1, xmin, xmax, ymin, ymax)
            draw2 = get_line_path(a2, b2, c2, xmin, xmax, ymin, ymax)
            draw3 = get_line_path(a3, b3, c3, xmin, xmax, ymin, ymax)

            tikz_code = fr"""\begin{{center}}
            \begin{{tikzpicture}}[>=stealth, scale=0.6]
                \draw[step=1.0,gray!30,thin] ({xmin},{ymin}) grid ({xmax},{ymax});
                \begin{{scope}}
                    \clip ({xmin},{ymin}) rectangle ({xmax},{ymax});
                    {fill1} {fill2} {fill3} {fill_y}
                    {draw1} {draw2} {draw3}
                \end{{scope}}
                \draw[->, thick] ({xmin},0) -- ({xmax},0) node[below] {{$x$}};
                \draw[->, thick] (0,{ymin}) -- (0,{ymax}) node[left] {{$y$}};
                \node at (0.3, -0.3) {{$O$}};
                \fill ({xA}, {yA}) circle (1.5pt) node[below left] {{$A$}};
                \fill ({xB}, {yB}) circle (1.5pt) node[below right] {{$B$}};
                \fill ({xC}, {yC}) circle (1.5pt) node[above right] {{$C$}};
                \fill ({xD}, {yD}) circle (1.5pt) node[above left] {{$D$}};
            \end{{tikzpicture}}
            \end{{center}}"""

            noidungcauhoi = fr"Cho hệ bất phương trình $\begin{{cases}} {eq1_str} \\ {eq2_str} \\ {eq3_str} \\ y \ge 0 \end{{cases}}$."

            # ------------------------------------------------------------------------
            # LOGIC 4 MỆNH ĐỀ (Đúng / Sai)
            # ------------------------------------------------------------------------

            # Nhận biết
            x_P, y_P = random.choice([A, B, C, D])
            nb_da_1_d = fr"\True Điểm có tọa độ $({x_P}; {y_P})$ thuộc miền nghiệm của hệ bất phương trình"
            nb_da_1_s = fr"Điểm có tọa độ $({x_P}; {y_P})$ không thuộc miền nghiệm của hệ bất phương trình"
            loigiai_nb_d = fr"Đúng. Thay tọa độ $x = {x_P}, y = {y_P}$ vào hệ bất phương trình ta thấy thỏa mãn tất cả các bất phương trình."
            loigiai_nb_s = fr"Sai. Thay tọa độ $x = {x_P}, y = {y_P}$ vào hệ bất phương trình ta thấy thỏa mãn tất cả các bất phương trình."
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            # Thông hiểu
            th_da_1_d = r"\True Miền nghiệm của hệ bất phương trình là một tứ giác"
            th_da_1_s = r"Miền nghiệm của hệ bất phương trình là một tam giác"
            loigiai_th_d = fr"Đúng. Bằng cách vẽ các đường thẳng giới hạn, ta xác định được miền nghiệm của hệ là miền tứ giác $ABCD$ với $A({xA};{yA})$, $B({xB};{yB})$, $C({xC};{yC})$, $D({xD};{yD})$."
            loigiai_th_s = fr"Sai. Miền nghiệm của hệ bất phương trình phải là miền tứ giác $ABCD$ với $A({xA};{yA})$, $B({xB};{yB})$, $C({xC};{yC})$, $D({xD};{yD})$."
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            # Vận dụng
            vd_da_1_d = fr"\True Giá trị nhỏ nhất của biểu thức $F(x;y) = {F_str}$ trên miền nghiệm bằng ${min_F}$"
            vd_da_1_s = fr"Giá trị nhỏ nhất của biểu thức $F(x;y) = {F_str}$ trên miền nghiệm bằng ${min_F + random.choice([2, 3])}$"
            sol_vd_base = fr"""Miền nghiệm của hệ bất phương trình là miền tứ giác $ABCD$.
            {tikz_code}
            Ta tính giá trị của $F$ tại các đỉnh của tứ giác $ABCD$:
            \begin{{center}}
            \renewcommand{{\arraystretch}}{{1.5}}
            \begin{{tabular}}{{|c|c|c|c|c|}}
            \hline
            Đỉnh & $A({xA};{yA})$ & $B({xB};{yB})$ & $C({xC};{yC})$ & $D({xD};{yD})$ \\
            \hline
            $F = {F_str}$ & ${F_A}$ & ${F_B}$ & ${F_C}$ & ${F_D}$ \\
            \hline
            \end{{tabular}}
            \end{{center}}
            Từ bảng trên, ta thấy giá trị nhỏ nhất của $F(x;y)$ là $\min F = {min_F}$."""

            loigiai_vd_d = f"Đúng. \n{sol_vd_base}"
            loigiai_vd_s = f"Sai. \n{sol_vd_base}"
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            # Vận dụng cao
            vdc_da_1_d = fr"\True Có {ans_count} giá trị $m$ nguyên thuộc đoạn $[-20; 20]$ để $m \le {F_str}$ với mọi cặp số $(x;y)$ thoả mãn hệ"
            vdc_da_1_s = fr"Có {ans_count + random.choice([-1, 1, 2])} giá trị $m$ nguyên thuộc đoạn $[-20; 20]$ để $m \le {F_str}$ với mọi cặp số $(x;y)$ thoả mãn hệ"
            sol_vdc_base = fr"""Ta có: $m \le {F_str}$ với mọi cặp số $(x;y)$ thoả mãn hệ bất phương trình khi và chỉ khi
            $$ m \le \min F \Leftrightarrow m \le {min_F}. $$
            Do $m$ nguyên thuộc $[-20; 20]$ nên ${latex_m_membership}$. 
            Vậy có {ans_count} giá trị thỏa mãn."""

            loigiai_vdc_d = f"Đúng. \n{sol_vdc_base}"
            loigiai_vdc_s = f"Sai. \n{sol_vdc_base}"
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            # ------------------------------------------------------------------------
            # ĐẢM BẢO RANDOM 1-3 ĐÁP ÁN ĐÚNG
            # ------------------------------------------------------------------------
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_da = random.choice(list_nb_da_1)
                nb_idx = list_nb_da_1.index(nb_da)

                th_da = random.choice(list_th_da_1)
                th_idx = list_th_da_1.index(th_da)

                vd_da = random.choice(list_vd_da_1)
                vd_idx = list_vd_da_1.index(vd_da)

                vdc_da = random.choice(list_vdc_da_1)
                vdc_idx = list_vdc_da_1.index(vdc_da)

                answers = [nb_da, th_da, vd_da, vdc_da]
                if 1 <= count_true_answers(answers) <= 3:
                    break

            # Đóng gói và xáo trộn (Chỉ có 1 phần tử nên việc xáo trộn giữ nguyên cấu trúc chuẩn)
            list_nb_1 = [nb_da]; list_nb_2 = [[loigiai_nb_d, loigiai_nb_s][nb_idx]]
            list_th_1 = [th_da]; list_th_2 = [[loigiai_th_d, loigiai_th_s][th_idx]]
            list_vd_1 = [vd_da]; list_vd_2 = [[loigiai_vd_d, loigiai_vd_s][vd_idx]]
            list_vdc_1 = [vdc_da]; list_vdc_2 = [[loigiai_vdc_d, loigiai_vdc_s][vdc_idx]]

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


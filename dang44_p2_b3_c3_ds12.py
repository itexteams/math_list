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


def bt_dang44_p2_b3_c3_ds12(self):
            # --- BƯỚC 1: CHỌN THÔNG SỐ NGẪU NHIÊN ---
            # Khai báo biến
            t = symbols('t')
            x_sym = symbols('x')

            # Hàm định dạng số hiển thị dấu phẩy kiểu Việt Nam
            def fmt_num(val):
                s = str(val).replace('.', ',')
                if s.endswith(',0'):
                    s = s[:-2]
                return s

            # Random các tham số sao cho thời điểm t và thể tích đẹp
            while True:
                tA = random.randint(2, 4)
                tB = tA + random.choice([2, 4, 6])
                y0 = random.randint(3, 6)

                a_coeff = Rational(-y0, tA * tB)
                b_coeff = Rational(y0 * (tA + tB), tA * tB)
                t_max = tA + tB

                f_expr = a_coeff * t**2 + b_coeff * t
                V_expr = integrate(f_expr, t)

                # Tìm một thời điểm t_d (phân số tối giản) cho câu VD cao sao cho thể tích tại đó là số thập phân hữu hạn đẹp
                valid_t = []
                for den in [2, 4, 5, 8]:
                    for num in range(1, den * t_max):
                        if math.gcd(num, den) == 1:
                            t_val = Rational(num, den)
                            v_val = V_expr.subs(t, t_val)
                            # Kiểm tra xem mẫu số của v_val chỉ chứa thừa số nguyên tố 2 và 5 (để là số thập phân hữu hạn)
                            q = v_val.q
                            while q % 2 == 0: q //= 2
                            while q % 5 == 0: q //= 5
                            if q == 1:
                                valid_t.append(t_val)
                if len(valid_t) > 0:
                    t_d = random.choice(valid_t)
                    break

            # Vẽ đồ thị bằng TikZ
            tikz_code = (
            '''\\begin{center}
            \\begin{tikzpicture}[>=stealth, scale=0.8]
            \\draw[->] (-1,0) -- (%s,0) node[below] {$t$(giờ)};
            \\draw[->] (0,-1) -- (0,%s) node[right] {$y(\\text{m}^3/\\text{giờ})$};
            \\node at (0,0) [below left] {$O$};
            \\draw[line width=1pt, smooth, samples=100, domain=0:%s] plot(\\x, {%s*\\x*\\x + %s*\\x}) node[below] {$y=f(t)$};
            \\draw[dashed] (%s,0) node[below] {$%s$} -- (%s,%s) node[above left] {$A$} -- (0,%s) node[left] {$%s$};
            \\draw[dashed] (%s,0) node[below] {$%s$} -- (%s,%s) node[above right] {$B$} -- (0,%s);
            \\fill (0,0) circle (1.5pt);
            \\fill (%s,%s) circle (1.5pt);
            \\fill (%s,%s) circle (1.5pt);
            \\end{tikzpicture}
            \\end{center}''' % (t_max + 1.5, float(f_expr.subs(t, Rational(t_max, 2))) + 1.5, t_max, float(a_coeff), float(b_coeff), tA, tA, tA, y0, y0, y0, tB, tB, tB, y0, y0, tA, y0, tB, y0)
            )

            # Nội dung câu hỏi
            noidungcauhoi = ('''Người ta dùng một thiết bị bơm nước vào một bể không có nước. Tính từ lúc thiết bị bắt đầu hoạt động, tại thời điểm $t$ giờ với $0 \\le t \\le %s$, thiết bị đó có tốc độ bơm nước vào bể là $f(t)$ ($\\text{m}^3$/giờ). Biết rằng đồ thị của hàm số $y=f(t)$ là một phần đường parabol đi qua gốc tọa độ $O$ và hai điểm $A(%s; %s)$, $B(%s; %s)$ (xem hình minh họa bên dưới).
            %s''' % (t_max, tA, y0, tB, y0, tikz_code))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Với $0 \\le t \\le %s$ thì $f(t) = %s$ ($\\text{m}^3$/giờ)' % (t_max, latex(f_expr))
            nb_da_1_s = 'Với $0 \\le t \\le %s$ thì $f(t) = %s$ ($\\text{m}^3$/giờ)' % (t_max, latex(b_coeff * t**2 + a_coeff * t))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Gọi phương trình parabol là $y = f(t) = at^2 + bt + c$. \\\\ 
            Vì đồ thị đi qua gốc tọa độ $O(0;0)$ nên $c=0$. \\\\ 
            Đồ thị hàm số đi qua $A(%s; %s)$ và $B(%s; %s)$ nên ta có hệ phương trình: \\\\ 
            $\\begin{cases} %s^2 a + %s b = %s \\\\ %s^2 a + %s b = %s \\end{cases} \\Leftrightarrow \\begin{cases} a = %s \\\\ b = %s \\end{cases}$. \\\\ 
            Vậy $f(t) = %s$.''' % (tA, y0, tB, y0, tA, tA, y0, tB, tB, y0, latex(a_coeff), latex(b_coeff), latex(f_expr)))

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Tại thời điểm $t$ giờ ($0 \\le t \\le %s$) tính từ lúc thiết bị bắt đầu hoạt động, lượng nước trong bể là $V(t) = %s$ ($\\text{m}^3$)' % (t_max, latex(V_expr))
            th_da_1_s = 'Tại thời điểm $t$ giờ ($0 \\le t \\le %s$) tính từ lúc thiết bị bắt đầu hoạt động, lượng nước trong bể là $V(t) = %s$ ($\\text{m}^3$)' % (t_max, latex(a_coeff * t**2 + b_coeff * t))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Lượng nước trong bể tại thời điểm $t$ giờ là $V(t) = \\int_0^t f(x) \\mathrm{d}x = \\int_0^t \\left( %s \\right) \\mathrm{d}x = %s$.''' % (latex(f_expr.subs(t, x_sym)), latex(V_expr)))

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Tính V_max và so sánh
            t_S = Rational(tA + tB, 2)
            V_max = V_expr.subs(t, t_S)
            V_max_f = float(V_max)
            c_val_true = round(V_max_f - 0.2, 1)
            c_val_false = round(V_max_f + 0.2, 1)

            # Các đáp án
            vd_da_1_d = '\\True Tại thời điểm thiết bị có tốc độ bơm nước vào bể là lớn nhất, lượng nước trong bể lớn hơn $%s$ mét khối' % (fmt_num(c_val_true))
            vd_da_1_s = 'Tại thời điểm thiết bị có tốc độ bơm nước vào bể là lớn nhất, lượng nước trong bể lớn hơn $%s$ mét khối' % (fmt_num(c_val_false))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Tốc độ bơm lớn nhất đạt được tại đỉnh của parabol, tức là tại thời điểm $t = -\\frac{b}{2a} = %s$ (giờ). \\\\ 
            Khi đó, lượng nước trong bể là $V(%s) = %s \\approx %s$ mét khối. \\\\ 
            Đối chiếu với phương án để rút ra kết luận.''' % (latex(t_S), latex(t_S), latex(V_max), fmt_num(round(V_max_f, 2))))

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            v_d_val = V_expr.subs(t, t_d)
            v_d_str = fmt_num(float(v_d_val))
            ab_sum = t_d.p + t_d.q

            # Các đáp án
            vdc_da_1_d = '\\True Sau $\\frac{a}{b}$ giờ tính từ lúc thiết bị bắt đầu hoạt động (trong đó $\\frac{a}{b}$ là phân số tối giản và $b>0$), lượng nước trong bể là $%s$ mét khối. Khi đó, giá trị của $a+b$ là $%s$' % (v_d_str, ab_sum)
            vdc_da_1_s = 'Sau $\\frac{a}{b}$ giờ tính từ lúc thiết bị bắt đầu hoạt động (trong đó $\\frac{a}{b}$ là phân số tối giản và $b>0$), lượng nước trong bể là $%s$ mét khối. Khi đó, giá trị của $a+b$ là $%s$' % (v_d_str, ab_sum + random.randint(1, 4))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Ta có phương trình lượng nước: $V(t) = %s \\Leftrightarrow %s = %s$. \\\\ 
            Giải phương trình này với điều kiện $0 \\le t \\le %s$, ta thu được nghiệm $t = %s$ (giờ). \\\\ 
            Do đó, $a = %s$, $b = %s$. \\\\ 
            Suy ra $a+b = %s$.''' % (v_d_str, latex(V_expr), str(float(v_d_val)), t_max, latex(t_d), t_d.p, t_d.q, ab_sum))

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


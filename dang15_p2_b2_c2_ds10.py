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


def bt_dang15_p2_b2_c2_ds10(self):
            # Khai báo biến
            # Hàm hỗ trợ định dạng biểu thức bậc nhất ax + by
            def fmt_expr(a, b):
                def fmt_term(c, var, is_first):
                    if c == 0: return ""
                    if is_first:
                        if c == 1: return var
                        if c == -1: return "-" + var
                        return "%s%s" % (c, var)
                    else:
                        if c == 1: return "+ " + var
                        if c == -1: return "- " + var
                        if c > 0: return "+ %s%s" % (c, var)
                        return "- %s%s" % (-c, var)

                res = fmt_term(a, "x", True)
                if res == "":
                    res = fmt_term(b, "y", True)
                else:
                    res += " " + fmt_term(b, "y", False)
                return res

            # Hàm hỗ trợ định dạng phân số cho LaTeX
            def format_frac(num):
                if num.denominator == 1:
                    return str(num.numerator)
                if num.numerator > 0:
                    return "\\frac{%s}{%s}" % (num.numerator, num.denominator)
                else:
                    return "-\\frac{%s}{%s}" % (-num.numerator, num.denominator)

            # Random các thông số cho đến khi tạo thành một tam giác hợp lệ ở nửa mặt phẳng x >= 0
            while True:
                a = random.randint(1, 3)
                b = random.randint(1, 3)
                d = random.randint(1, 3)
                e = random.randint(-3, -1)

                c = random.randint(1, 6)
                f = random.randint(-3, 3)

                D = a*e - b*d
                if D == 0: continue

                xB = frac(c*e - b*f, D)
                yB = frac(a*f - c*d, D)

                if xB <= 0: continue

                yA = frac(c, b)
                yC = frac(f, e)

                if yA <= yC: continue

                break

            # Nội dung câu hỏi
            sys_tex = "\\begin{cases} %s \\le %s \\\\ x \\ge 0 \\\\ %s \\le %s \\end{cases}" % (fmt_expr(a, b), c, fmt_expr(d, e), f)
            noidungcauhoi = ('''Cho hệ bất phương trình $%s$.''' % sys_tex)

            ######################################################################## Nhận biết ############################################
            x1, y1 = random.randint(0, 3), random.randint(-2, 3)
            is_sol_A = (a*x1 + b*y1 <= c) and (x1 >= 0) and (d*x1 + e*y1 <= f)

            if is_sol_A:
                nb_da_1_d = '\\True Cặp số $(%s; %s)$ là nghiệm của hệ bất phương trình trên' % (x1, y1)
                nb_da_1_s = 'Cặp số $(%s; %s)$ không là nghiệm của hệ bất phương trình trên' % (x1, y1)
            else:
                nb_da_1_d = '\\True Cặp số $(%s; %s)$ không là nghiệm của hệ bất phương trình trên' % (x1, y1)
                nb_da_1_s = 'Cặp số $(%s; %s)$ là nghiệm của hệ bất phương trình trên' % (x1, y1)

            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            str_sol_A = "thỏa mãn cả 3 bất phương trình" if is_sol_A else "không thỏa mãn tất cả các bất phương trình"
            loigiai_nb_1 = ('''Thay $x=%s, y=%s$ vào hệ bất phương trình, ta thấy %s.''' % (x1, y1, str_sol_A))

            list_nb_2 = [loigiai_nb_1]
            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            O_in = (c >= 0) and (f >= 0)
            xM, yM = random.randint(-3, -1), random.randint(-2, 3) 
            B_true = O_in

            if B_true:
                th_da_1_d = '\\True Miền nghiệm của hệ bất phương trình trên chứa gốc tọa độ $O$ và không chứa điểm $M(%s; %s)$' % (xM, yM)
                th_da_1_s = 'Miền nghiệm của hệ bất phương trình trên không chứa gốc tọa độ $O$ hoặc chứa điểm $M(%s; %s)$' % (xM, yM)
            else:
                th_da_1_d = '\\True Miền nghiệm của hệ bất phương trình trên không chứa gốc tọa độ $O$ hoặc chứa điểm $M(%s; %s)$' % (xM, yM)
                th_da_1_s = 'Miền nghiệm của hệ bất phương trình trên chứa gốc tọa độ $O$ và không chứa điểm $M(%s; %s)$' % (xM, yM)

            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            str_O_in = "đúng" if O_in else "sai"
            loigiai_th_1 = ('''Kiểm tra $O(0;0)$: thay $x=0, y=0$ vào hệ ta thấy %s. Cùng với $M(%s; %s)$, do $x_M = %s < 0$ nên điểm $M$ không thuộc miền nghiệm.''' % (str_O_in, xM, yM, xM))

            list_th_2 = [loigiai_th_1]
            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            fake_xB = xB + frac(1, 2)
            is_C_true = random.choice([True, False])

            if is_C_true:
                vd_da_1_d = '\\True Miền nghiệm của hệ bất phương trình trên là miền tam giác $ABC$, với $A(0; %s), B\\left(%s; %s\\right)$ và $C(0; %s)$' % (format_frac(yA), format_frac(xB), format_frac(yB), format_frac(yC))
                vd_da_1_s = 'Miền nghiệm của hệ bất phương trình trên là miền tam giác $ABC$, với $A(0; %s), B\\left(%s; %s\\right)$ và $C(0; %s)$' % (format_frac(yA), format_frac(fake_xB), format_frac(yB), format_frac(yC))
            else:
                vd_da_1_d = '\\True Miền nghiệm của hệ bất phương trình trên không phải là miền tam giác $ABC$ với $A(0; %s), B\\left(%s; %s\\right)$ và $C(0; %s)$' % (format_frac(yA), format_frac(fake_xB), format_frac(yB), format_frac(yC))
                vd_da_1_s = 'Miền nghiệm của hệ bất phương trình trên là miền tam giác $ABC$, với $A(0; %s), B\\left(%s; %s\\right)$ và $C(0; %s)$' % (format_frac(yA), format_frac(fake_xB), format_frac(yB), format_frac(yC))

            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = ('''Miền nghiệm là tam giác tạo bởi các giao điểm của các đường thẳng $x=0$, $%s = %s$ và $%s = %s$. Giải các hệ phương trình ta được tọa độ các đỉnh là $A(0; %s), B\\left(%s; %s\\right)$ và $C(0; %s)$. Vẽ hình minh họa ta thấy miền nghiệm thỏa mãn là tam giác $ABC$. \\\\
            \\begin{center}
            \\begin{tikzpicture}[>=stealth, scale=1, line width=1pt]
            \\node at (0,0) [below left] {$O$};
            \\clip (-2,-2) rectangle (4,4);
            \\fill[pattern=north east lines, pattern color=black] (-2,-2) rectangle (4,4);
            \\fill[white] (0, %s) -- (%s, %s) -- (0, %s) -- cycle;
            \\draw[black] (-2, %s) -- (4, %s);
            \\draw[black] (-2, %s) -- (4, %s);
            \\draw[black] (0, -2) -- (0, 4);
            \\coordinate (A) at (0,%s);
            \\coordinate (B) at (%s,%s);
            \\coordinate (C) at (0,%s);
            \\node at (A) [left] {$A$};
            \\node at (B) [right] {$B$};
            \\node at (C) [left] {$C$};
            \\fill (A) circle (1.5pt);
            \\fill (B) circle (1.5pt);
            \\fill (C) circle (1.5pt);
            \\draw[->] (-2, 0) -- (4, 0) node[below] {$x$};
            \\draw[->] (0, -2) -- (0, 4) node[left] {$y$};
            \\end{tikzpicture}
            \\end{center}''' % (fmt_expr(a, b), c, fmt_expr(d, e), f, format_frac(yA), format_frac(xB), format_frac(yB), format_frac(yC), float(yA), float(xB), float(yB), float(yC), float((c-a*(-2))/b), float((c-a*4)/b), float((f-d*(-2))/e), float((f-d*4)/e), float(yA), float(xB), float(yB), float(yC)))

            list_vd_2 = [loigiai_vd_1]
            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            m = random.randint(1, 3)
            n = random.randint(-3, -1)
            F_expr = fmt_expr(m, n)

            FA = m*0 + n*yA
            FB = m*xB + n*yB
            FC = m*0 + n*yC

            F_min = min(FA, FB, FC)
            fake_F_min = F_min - 1

            is_D_true = random.choice([True, False])

            if is_D_true:
                vdc_da_1_d = '\\True Giá trị nhỏ nhất của biểu thức $F(x; y) = %s$ với $x, y$ thỏa mãn hệ bất phương trình trên bằng $%s$' % (F_expr, format_frac(F_min))
                vdc_da_1_s = 'Giá trị nhỏ nhất của biểu thức $F(x; y) = %s$ với $x, y$ thỏa mãn hệ bất phương trình trên bằng $%s$' % (F_expr, format_frac(fake_F_min))
            else:
                vdc_da_1_d = '\\True Giá trị nhỏ nhất của biểu thức $F(x; y) = %s$ với $x, y$ thỏa mãn hệ bất phương trình trên không bằng $%s$' % (F_expr, format_frac(fake_F_min))
                vdc_da_1_s = 'Giá trị nhỏ nhất của biểu thức $F(x; y) = %s$ với $x, y$ thỏa mãn hệ bất phương trình trên bằng $%s$' % (F_expr, format_frac(fake_F_min))

            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = ('''Ta tính giá trị biểu thức $F(x; y) = %s$ tại các đỉnh của tam giác $ABC$: \\\\
            - Tại $A\\left(0; %s\\right)$, $F = %s$. \\\\
            - Tại $B\\left(%s; %s\\right)$, $F = %s$. \\\\
            - Tại $C\\left(0; %s\\right)$, $F = %s$. \\\\
            Suy ra giá trị nhỏ nhất của $F(x; y)$ trên miền nghiệm là $%s$.''' % (F_expr, format_frac(yA), format_frac(FA), format_frac(xB), format_frac(yB), format_frac(FB), format_frac(yC), format_frac(FC), format_frac(F_min)))

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


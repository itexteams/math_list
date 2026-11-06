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


def bt_dang32_p2_b2_c2_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x, y = symbols('x y')

            # Sinh các hệ số ngẫu nhiên cho hệ bất phương trình
            a1 = randint(1, 3)
            c1 = randint(1, 3)
            a2 = randint(2, 4)
            c2_min = a2 * c1 + 1
            c2 = randint(c2_min, 12)

            # Sinh các hệ số cho biểu thức F(x, y) = mx - ny
            m = randint(1, 3)
            n = randint(1, 3)

            # Tính tọa độ điểm B (giao của hai đường thẳng x - a1*y = c1 và a2*x + y = c2)
            den = a1 * a2 + 1
            xB = Rational(c1 + a1 * c2, den)
            yB = Rational(c2 - a2 * c1, den)

            # Giá trị hàm F tại các đỉnh
            f_O = Rational(0, 1)
            f_A = Rational(m * c1, 1)
            f_B = m * xB - n * yB
            f_C = Rational(-n * c2, 1)

            vals = [f_O, f_A, f_B, f_C]
            max_val = max(vals)
            min_val = min(vals)

            # Biểu thức F(x,y)
            expr_F = ""
            if m == 1:
                expr_F = "x"
            else:
                expr_F = "%sx" % m
            if n == 1:
                expr_F += " - y"
            else:
                expr_F += " - %sy" % n

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hệ bất phương trình $\\begin{cases} x - %sy \\le %s \\\\ %sx + y \\le %s \\\\ x \\ge 0 \\\\ y \\ge 0 \\end{cases}$.'''
                             % (latex(a1), latex(c1), latex(a2), latex(c2)))

            ######################################################################## Nhận biết ############################################
            # Tạo điểm M thuộc và không thuộc miền nghiệm
            xm_T, ym_T = 1, 0
            xm_F, ym_F = c2, c2

            # Các đáp án
            nb_da_1_d = '\\True Miền nghiệm của hệ bất phương trình đã cho chứa điểm $M(%s;%s)$' % (xm_T, ym_T)
            nb_da_1_s = 'Miền nghiệm của hệ bất phương trình đã cho chứa điểm $M(%s;%s)$' % (xm_F, ym_F)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Thay tọa độ điểm $M(%s;%s)$ vào hệ bất phương trình ta thấy thỏa mãn nên điểm này thuộc miền nghiệm. \\\\
            Thay tọa độ điểm $M(%s;%s)$ vào bất phương trình thứ hai ta có $%s \\cdot %s + %s = %s > %s$ (không thỏa mãn) nên không thuộc miền nghiệm.'''
                            % (xm_T, ym_T, xm_F, ym_F, a2, xm_F, ym_F, a2 * xm_F + ym_F, c2))

            list_nb_2 = [loigiai_nb_1]
            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            yN = c2 - 1

            # Tính toán các tọa độ dải rộng cho TikZ
            def my_round(val):
                return round(float(val), 3)

            y1_start = (-2 - c1) / a1
            y1_end = (14 - c1) / a1
            y2_start = c2 - a2 * (-2)
            y2_end = c2 - a2 * (14)

            # Các đáp án
            th_da_1_d = '\\True Trên mặt phẳng tọa độ $Oxy$, biểu diễn miền nghiệm của hệ bất phương trình đã cho là miền tứ giác có chứa điểm $N(0;%s)$' % yN
            th_da_1_s = 'Trên mặt phẳng tọa độ $Oxy$, biểu diễn miền nghiệm của hệ bất phương trình đã cho là miền tam giác có chứa điểm $N(0;%s)$' % yN
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Miền nghiệm là tứ giác $OABC$ với $O(0;0)$, $A(%s;0)$, $B\\left(%s; %s\\right)$, $C(0;%s)$. \\\\
            Do đó miền nghiệm là một tứ giác. Điểm $N(0;%s)$ nằm trên đoạn $OC$ nên thuộc miền nghiệm.
            \\begin{center}
            \\begin{tikzpicture}[>=stealth, scale=0.4, line width=1pt]
            \\node at (0,0) [below left] {$O$};
            \\clip (-2,-2) rectangle (14,14);
            \\fill[pattern=north east lines, pattern color=black] (-2,-2) rectangle (14,14);
            \\fill[white] (0,0) -- (%s,0) -- (%s,%s) -- (0,%s) -- cycle;
            \\draw[black] (-2,%s) -- (14,%s);
            \\draw[black] (-2,%s) -- (14,%s);
            \\coordinate (A) at (%s,0);
            \\coordinate (B) at (%s,%s);
            \\coordinate (C) at (0,%s);
            \\fill (A) circle (3.5pt) node[above right] {$A$};
            \\fill (B) circle (3.5pt) node[above right] {$B$};
            \\fill (C) circle (3.5pt) node[right] {$C$};
            \\draw[->] (-2, 0) -- (14, 0) node[below] {$x$};
            \\draw[->] (0, -2) -- (0, 14) node[left] {$y$};
            \\end{tikzpicture}
            \\end{center}''' % (c1, latex(xB), latex(yB), c2, yN, c1, my_round(xB), my_round(yB), c2, my_round(y1_start), my_round(y1_end), my_round(y2_start), my_round(y2_end), c1, my_round(xB), my_round(yB), c2))

            list_th_2 = [loigiai_th_1]
            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            S_true = c1 + c2 + 1
            S_false = c1 + c2 - 1

            # Các đáp án
            vd_da_1_d = '\\True Miền nghiệm của hệ bất phương trình đã cho có $%s$ điểm có tọa độ nguyên nằm trên các trục tọa độ' % S_true
            vd_da_1_s = 'Miền nghiệm của hệ bất phương trình đã cho có $%s$ điểm có tọa độ nguyên nằm trên các trục tọa độ' % S_false
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Các điểm nằm trên trục $Ox$ thuộc miền nghiệm thỏa mãn: $\\begin{cases} y = 0 \\\\ 0 \\le x \\le %s \\end{cases}$. Vì $x \\in \\mathbb{Z}$ nên có $%s$ điểm. \\\\
            Các điểm nằm trên trục $Oy$ thuộc miền nghiệm thỏa mãn: $\\begin{cases} x = 0 \\\\ 0 \\le y \\le %s \\end{cases}$. Vì $y \\in \\mathbb{Z}$ nên có $%s$ điểm. \\\\
            Do điểm $O(0;0)$ được tính $2$ lần nên số điểm nguyên trên các trục tọa độ là: $%s + %s - 1 = %s$ điểm.'''
                            % (c1, c1 + 1, c2, c2 + 1, c1 + 1, c2 + 1, S_true))

            list_vd_2 = [loigiai_vd_1]
            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            p = den
            q = randint(1, 3)
            k = p * max_val + q * min_val
            k_false = k + randint(1, 5)

            # Các đáp án
            vdc_da_1_d = '\\True Giá trị lớn nhất và giá trị nhỏ nhất của biểu thức $F(x;y) = %s$, với $x$ và $y$ thỏa mãn hệ bất phương trình đã cho lần lượt là $a, b$. Giá trị $%sa + %sb = %s$' % (expr_F, p, q, latex(k))
            vdc_da_1_s = 'Giá trị lớn nhất và giá trị nhỏ nhất của biểu thức $F(x;y) = %s$, với $x$ và $y$ thỏa mãn hệ bất phương trình đã cho lần lượt là $a, b$. Giá trị $%sa + %sb = %s$' % (expr_F, p, q, latex(k_false))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Ta tính giá trị của $F(x;y)$ tại các đỉnh của miền nghiệm (tứ giác $OABC$): \\\\
            $F(O) = F(0;0) = 0$. \\\\
            $F(A) = F(%s;0) = %s$. \\\\
            $F(B) = F\\left(%s;%s\\right) = %s$. \\\\
            $F(C) = F(0;%s) = %s$. \\\\
            Do đó, giá trị lớn nhất $a = %s$, giá trị nhỏ nhất $b = %s$. \\\\
            Vậy $%sa + %sb = %s\\left(%s\\right) + %s\\left(%s\\right) = %s$.''' % (
                c1, latex(f_A),
                latex(xB), latex(yB), latex(f_B),
                c2, latex(f_C),
                latex(max_val), latex(min_val),
                p, q, p, latex(max_val), q, latex(min_val), latex(k)
            ))

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
                '\\begin{ex}\n' +
                str(noidungcauhoi) + '\n' +
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


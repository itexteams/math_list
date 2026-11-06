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


def bt_dang10_p2_b2_c3_hh10(self):
            # Khai báo biến
            # Khai báo các ký hiệu
            x, y = symbols('x y')

            # --- Bước 1: Khởi tạo dữ liệu ngẫu nhiên ---
            a_val = random.randint(1, 3)
            b_val = -1 
            c_val = random.randint(-3, 5)

            xA, yA = random.randint(-3, 3), random.randint(-3, 3)
            xB, yB = random.randint(1, 5), random.randint(-2, 2)

            # Đảm bảo A, B không trùng nhau và A không nằm trên d
            while (xA == xB and yA == yB) or (a_val*xA + b_val*yA + c_val == 0):
                xA, yA = random.randint(-3, 3), random.randint(-3, 3)

            noidungcauhoi = ('''Cho đường thẳng $d: %s = 0$ và hai điểm $A(%s; %s), B(%s; %s)$.''' 
                             % (latex(a_val*x + b_val*y + c_val), xA, yA, xB, yB))

            # --- Bước 2: Tính toán chính xác ---

            # a) Khoảng cách
            dist_A_d = Abs(a_val*xA + b_val*yA + c_val) / sqrt(a_val**2 + b_val**2)

            # b) Hình chiếu H
            h_x, h_y = symbols('h_x h_y')
            eq1 = a_val*h_x + b_val*h_y + c_val
            eq2 = -b_val*(h_x - xA) + a_val*(h_y - yA)
            sol_h = sp.solve((eq1, eq2), (h_x, h_y))
            Hx, Hy = sol_h[h_x], sol_h[h_y]

            # c) Tìm C(0; yC) để G thuộc d
            yC_sym = symbols('yC')
            Gx = Rational(xA + xB + 0, 3)
            Gy = (yA + yB + yC_sym) / Rational(3, 1)
            eq_G = a_val*Gx + b_val*Gy + c_val
            yC_val = sp.solve(eq_G, yC_sym)[0]

            # d) Diện tích theo phương pháp: Chiều cao * Đáy
            xC_val = 0
            # Độ dài cạnh đáy AB
            length_AB = sqrt((xB - xA)**2 + (yB - yA)**2)
            # Phương trình đường thẳng AB: (yA-yB)x + (xB-xA)y + xAyB - xByA = 0
            a_AB = yA - yB
            b_AB = xB - xA
            c_AB = xA*yB - xB*yA
            pt_AB = a_AB*x + b_AB*y + c_AB
            # Khoảng cách từ C đến AB (chiều cao h_C)
            h_C = Abs(a_AB*xC_val + b_AB*yC_val + c_AB) / sqrt(a_AB**2 + b_AB**2)
            # Diện tích
            area_ABC = Rational(1, 2) * length_AB * h_C

            ########################################################################
            # NHẬN BIẾT
            ########################################################################
            nb_da_1_d = '\\True Khoảng cách từ $A$ đến đường thẳng $d$ bằng $%s$' % (latex(dist_A_d))
            nb_da_1_s = 'Khoảng cách từ $A$ đến đường thẳng $d$ bằng $%s$' % (latex(dist_A_d + 1))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Khoảng cách từ $A(%s; %s)$ đến $d: %s=0$ là: \\\\
                            $d(A, d) = \\frac{|%s(%s) + (%s)(%s) + %s|}{\\sqrt{%s^2 + (%s)^2}} = %s$.''' 
                            % (xA, yA, latex(a_val*x + b_val*y + c_val), a_val, xA, b_val, yA, c_val, a_val, b_val, latex(dist_A_d)))

            ########################################################################
            # THÔNG HIỂU
            ########################################################################
            th_da_1_d = '\\True Tọa độ hình chiếu vuông góc của $A$ lên $d$ là $\\left(%s; %s\\right)$' % (latex(Hx), latex(Hy))
            th_da_1_s = 'Tọa độ hình chiếu vuông góc của $A$ lên $d$ là $\\left(%s; %s\\right)$' % (latex(Hx + 1), latex(Hy))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            pt_vg = -b_val*(x-xA) + a_val*(y-yA)
            loigiai_th_1 = ('''Gọi $H(x; y)$ là hình chiếu của $A$ lên $d$. Đường thẳng $\\Delta$ qua $A$ và vuông góc với $d$ có phương trình: \\\\
                            $%s = 0$. \\\\
                            Tọa độ $H$ là nghiệm của hệ: $\\begin{cases} %s = 0 \\\\ %s = 0 \\end{cases} \\Leftrightarrow \\begin{cases} x = %s \\\\ y = %s \\end{cases}$. \\\\
                            Vậy $H\\left(%s; %s\\right)$.''' 
                            % (latex(pt_vg), latex(a_val*x + b_val*y + c_val), latex(pt_vg), latex(Hx), latex(Hy), latex(Hx), latex(Hy)))

            ########################################################################
            # VẬN DỤNG
            ########################################################################
            vd_da_1_d = '\\True Điểm $C$ trên trục $Oy$ thỏa mãn trọng tâm tam giác $ABC$ thuộc $d$ có tọa độ $C(0; %s)$' % (latex(yC_val))
            vd_da_1_s = 'Điểm $C$ trên trục $Oy$ thỏa mãn trọng tâm tam giác $ABC$ thuộc $d$ có tọa độ $C(0; %s)$' % (latex(yC_val + 2))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Vì $C \\in Oy$ nên $C(0; y_C)$. Trọng tâm $G$ của $\\triangle ABC$ có tọa độ: \\\\
                            $x_G = \\frac{%s + %s + 0}{3} = %s$; $y_G = \\frac{%s + %s + y_C}{3} = \\frac{%s + y_C}{3}$. \\\\
                            Vì $G \\in d$ nên: $%s(%s) - \\frac{%s + y_C}{3} + %s = 0 \\Leftrightarrow y_C = %s$. \\\\
                            Vậy $C(0; %s)$.''' 
                            % (xA, xB, latex(Gx), yA, yB, yA+yB, a_val, latex(Gx), yA+yB, c_val, latex(yC_val), latex(yC_val)))

            ########################################################################
            # VẬN DỤNG CAO (Đã sửa theo yêu cầu)
            ########################################################################
            vdc_da_1_d = '\\True Diện tích tam giác $ABC$ với $C(0; %s)$ là $%s$ (đvdt)' % (latex(yC_val), latex(area_ABC))
            vdc_da_1_s = 'Diện tích tam giác $ABC$ với $C(0; %s)$ là $%s$ (đvdt)' % (latex(yC_val), latex(area_ABC + 5))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Để tính diện tích tam giác $ABC$, ta tính độ dài cạnh $AB$ và chiều cao từ $C$ đến $AB$: \\\\
                            - Độ dài cạnh đáy $AB = \\sqrt{(%s - (%s))^2 + (%s - %s)^2} = %s$. \\\\
                            - Đường thẳng $AB$ đi qua $A(%s; %s)$ và có vectơ chỉ phương $\\vec{AB} = (%s; %s)$ nên có phương trình: $%s = 0$. \\\\
                            - Chiều cao $h_C = d(C, AB) = \\frac{|%s(0) + (%s)(%s) + (%s)|}{\\sqrt{(%s)^2 + (%s)^2}} = %s$. \\\\
                            - Diện tích tam giác $ABC$ là: $S = \\frac{1}{2} \\cdot AB \\cdot h_C = \\frac{1}{2} \\cdot %s \\cdot %s = %s$.''' 
                            % (xB, xA, yB, yA, latex(length_AB), xA, yA, xB-xA, yB-yA, latex(pt_AB), 
                               a_AB, b_AB, latex(yC_val), c_AB, a_AB, b_AB, latex(h_C), latex(length_AB), latex(h_C), latex(area_ABC)))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_sel = random.choice(list_nb_da_1)
                th_sel = random.choice(list_th_da_1)
                vd_sel = random.choice(list_vd_da_1)
                vdc_sel = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([nb_sel, th_sel, vd_sel, vdc_sel]) <= 3:
                    break

            shuffled_answers = [nb_sel, th_sel, vd_sel, vdc_sel]
            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(shuffled_answers[0]) + '}\n'
                '{' + str(shuffled_answers[1]) + '}\n'
                '{' + str(shuffled_answers[2]) + '}\n'
                '{' + str(shuffled_answers[3]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(shuffled_solutions[0]) + '\n'
                '\\item ' + str(shuffled_solutions[1]) + '\n'
                '\\item ' + str(shuffled_solutions[2]) + '\n'
                '\\item ' + str(shuffled_solutions[3]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('+ -', '-').replace('- -', '+')
            return content   


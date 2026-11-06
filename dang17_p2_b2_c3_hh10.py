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


def bt_dang17_p2_b2_c3_hh10(self):
            # Khai báo biến
            # Chọn các bộ số Pitago để khoảng cách và độ dài cạnh là số nguyên cho đẹp
            pythagorean_triples = [(3, 4), (6, 8), (5, 12), (9, 12), (8, 15)]
            a_val, b_val = random.choice(pythagorean_triples)

            # Random tọa độ điểm C
            xc = random.randint(-3, 3)
            yc = random.randint(1, 5)

            # Random diện tích S cho câu d
            S_val = random.randint(2, 10)

            # Khai báo ký hiệu toán học
            x, y = symbols('x y')

            # 1. Phương trình đường thẳng Delta đi qua A(a, 0) và B(0, b)
            # bx + ay - ab = 0
            coeff_x = b_val
            coeff_y = a_val
            const = -a_val * b_val
            delta_eq = coeff_x*x + coeff_y*y + const

            # 2. Đường thẳng Delta1 qua A(a, 0) và vuông góc Delta
            # Vector pháp tuyến Delta là (b, a) -> VTCP là (a, -b) -> VTPT Delta1 là (a, -b)
            # a(x - a) - b(y - 0) = 0  => ax - by - a^2 = 0
            delta1_eq = a_val*x - b_val*y - a_val**2

            # 3. Khoảng cách từ C(xc, yc) đến Delta
            dist_num = abs(coeff_x*xc + coeff_y*yc + const)
            dist_den = sqrt(coeff_x**2 + coeff_y**2)
            dist_val = Rational(dist_num, dist_den)

            # 4. Điểm M trên Oy sao cho diện tích MAB = S
            # M(0, m). S = 1/2 * AB * d(M, Delta)
            # AB = sqrt(a^2 + b^2). d(M, Delta) = |a*m - ab| / sqrt(a^2 + b^2)
            # S = 1/2 * |a*m - ab| => |a*m - ab| = 2S => |m - b| = 2S/a
            # m = b + 2S/a hoặc m = b - 2S/a
            m1 = b_val + Rational(2*S_val, a_val)
            m2 = b_val - Rational(2*S_val, a_val)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Trong mặt phẳng tọa độ $\\left( Oxy \\right)$, cho ba điểm $A\\left( %s;0 \\right)$, $B\\left( 0;%s \\right)$ và $C\\left( %s;%s \\right)$. Gọi $\\Delta$ là đường thẳng đi qua $2$ điểm $A$ và $B$.''' 
                            % (latex(a_val), latex(b_val), latex(xc), latex(yc)))

            ########################################################################
            # Nhận biết - Câu a: Phương trình đường thẳng Delta
            ########################################################################
            nb_da_1_d = '\\True Phương trình đường thẳng $\\Delta$ là $%s=0$' % (latex(delta_eq))
            nb_da_1_s = 'Phương trình đường thẳng $\\Delta$ là $%s=0$' % (latex(delta_eq + random.randint(1,3)))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ('''Đường thẳng $\\Delta$ đi qua $A\\left( %s;0 \\right)$ và $B\\left( 0;%s \\right)$ có phương trình theo đoạn chắn là: \\\\
                            $\\frac{x}{%s} + \\frac{y}{%s} = 1 \\Leftrightarrow %s = 0$.''' 
                            % (latex(a_val), latex(b_val), latex(a_val), latex(b_val), latex(delta_eq)))

            ########################################################################
            # Thông hiểu - Câu b: Đường thẳng vuông góc
            ########################################################################
            th_da_1_d = '\\True Đường thẳng $\\Delta_1$ đi qua điểm $A$ và vuông góc với đường thẳng $\\Delta$ có phương trình $%s=0$' % (latex(delta1_eq))
            th_da_1_s = 'Đường thẳng $\\Delta_1$ đi qua điểm $A$ và vuông góc với đường thẳng $\\Delta$ có phương trình $%s=0$' % (latex(delta1_eq + x))
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ('''Đường thẳng $\\Delta$ có vectơ pháp tuyến $\\vec{n}_{\\Delta} = \\left( %s;%s \\right)$. \\\\
                            Vì $\\Delta_1 \\perp \\Delta$ nên $\\Delta_1$ có vectơ pháp tuyến $\\vec{n}_{\\Delta_1} = \\left( %s;-%s \\right)$. \\\\
                            Phương trình $\\Delta_1$ đi qua $A\\left( %s;0 \\right)$ là: $%s\\left( x-%s \\right) - %s\\left( y-0 \\right) = 0 \\Leftrightarrow %s = 0$.''' 
                            % (latex(coeff_x), latex(coeff_y), latex(a_val), latex(b_val), latex(a_val), latex(a_val), latex(a_val), latex(b_val), latex(delta1_eq)))

            ########################################################################
            # Vận dụng - Câu c: Khoảng cách
            ########################################################################
            wrong_dist = dist_val + 1
            vd_da_1_d = '\\True $d\\left( C, \\Delta \\right) = %s$' % (latex(dist_val))
            vd_da_1_s = '$d\\left( C, \\Delta \\right) = %s$' % (latex(wrong_dist))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ('''Khoảng cách từ điểm $C\\left( %s;%s \\right)$ đến đường thẳng $\\Delta: %s=0$ là: \\\\
                            $d\\left( C, \\Delta \\right) = \\frac{\\left| %s \\cdot \\left( %s \\right) + %s \\cdot %s %s \\right|}{\\sqrt{%s^2 + %s^2}} = %s$.''' 
                            % (latex(xc), latex(yc), latex(delta_eq), latex(coeff_x), latex(xc), latex(coeff_y), latex(yc), latex(const), latex(coeff_x), latex(coeff_y), latex(dist_val)))

            ########################################################################
            # Vận dụng cao - Câu d: Diện tích tam giác
            ########################################################################
            # Kiểm tra xem có điểm M nào tung độ dương không
            has_positive = (m1 > 0) or (m2 > 0)
            vdc_da_1_d = '\\True Điểm $M$ nằm trên trục $Oy$ ($M$ khác điểm $O$) sao cho diện tích tam giác $MAB$ bằng $%s$ có tung độ dương' % (latex(S_val))
            vdc_da_1_s = 'Điểm $M$ nằm trên trục $Oy$ ($M$ khác điểm $O$) sao cho diện tích tam giác $MAB$ bằng $%s$ không có tung độ dương' % (latex(S_val))

            # Điều chỉnh tính đúng sai thực tế dựa trên tham số random
            if has_positive:
                list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            else:
                # Nếu xui xẻo m1, m2 đều <= 0 (hiếm với bộ Pitago dương), ta đảo ngược nhãn
                vdc_da_1_d_fix = '\\True Điểm $M$ nằm trên trục $Oy$ ($M$ khác điểm $O$) sao cho diện tích tam giác $MAB$ bằng %s không có tung độ dương' % (latex(S_val))
                list_vdc_da_1 = [vdc_da_1_d_fix, vdc_da_1_s.replace('\\True', '')]

            loigiai_vdc_1 = ('''Gọi $M\\left( 0;m \\right) \\in Oy$ ($m \\neq 0$). Ta có $AB = \\sqrt{%s^2 + %s^2} = %s$. \\\\
                            Khoảng cách $d\\left( M, \\Delta \\right) = \\frac{\\left| %s \\cdot 0 + %s \\cdot m %s \\right|}{%s} = \\frac{\\left| %s m %s \\right|}{%s}$. \\\\
                            Diện tích $S_{\\triangle MAB} = \\frac{1}{2} AB \\cdot d\\left( M, \\Delta \\right) = \\frac{1}{2} \\cdot %s \\cdot \\frac{\\left| %s m %s \\right|}{%s} = %s \\Leftrightarrow \\left| %s m %s \\right| = %s$. \\\\
                            $\\Leftrightarrow \\left[ \\begin{aligned} & %s m %s = %s \\\\ & %s m %s = -%s \\end{aligned} \\right. \\Leftrightarrow \\left[ \\begin{aligned} & m = %s \\\\ & m = %s \\end{aligned} \\right.$. \\\\
                            Vậy tồn tại giá trị $m$ dương thỏa mãn yêu cầu.''' 
                            % (latex(a_val), latex(b_val), latex(int(sqrt(a_val**2+b_val**2))), latex(coeff_x), latex(coeff_y), latex(const), latex(int(sqrt(a_val**2+b_val**2))), latex(coeff_y), latex(const), latex(int(sqrt(a_val**2+b_val**2))),
                               latex(int(sqrt(a_val**2+b_val**2))), latex(coeff_y), latex(const), latex(int(sqrt(a_val**2+b_val**2))), latex(S_val), latex(coeff_y), latex(const), latex(2*S_val),
                               latex(coeff_y), latex(const), latex(2*S_val), latex(coeff_y), latex(const), latex(2*S_val), latex(m1), latex(m2)))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Vòng lặp chọn đáp án ngẫu nhiên sao cho có 1-3 câu đúng
            while True:
                ans_a = random.choice(list_nb_da_1)
                ans_b = random.choice(list_th_da_1)
                ans_c = random.choice(list_vd_da_1)
                ans_d = random.choice(list_vdc_da_1)

                current_answers = [ans_a, ans_b, ans_c, ans_d]
                if 1 <= count_true_answers(current_answers) <= 3:
                    break

            # Xuất nội dung theo định dạng mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(ans_a) + '}\n'
                '{' + str(ans_b) + '}\n'
                '{' + str(ans_c) + '}\n'
                '{' + str(ans_d) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content   


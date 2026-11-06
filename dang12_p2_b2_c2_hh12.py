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


def bt_dang12_p2_b2_c2_hh12(self):
            # Khai báo biến
            # THUẬT TOÁN RANDOM DỮ LIỆU BÀI TOÁN
            # ----------------------------------------------------------------------
            configs = [
                (8, 6, 4, 7, 5),    # Bài toán gốc
                (6, 8, 3, 6, 5),    
                (12, 5, 5, 1, 13),  
                (15, 8, 8, 2, 17),  
                (8, 15, 15, 9, 17), 
                (24, 7, 7, 1, 25)   
            ]

            xH, yH, z0, R, d_min = random.choice(configs)

            # Tìm vector chỉ phương u vuông góc với OH (trong mp Oxy)
            u1, u2 = yH, -xH
            g = math.gcd(abs(u1), abs(u2))
            u1, u2 = u1 // g, u2 // g

            if u1 < 0:
                u1, u2 = -u1, -u2

            # Sinh điểm M và N
            xM, yM = xH - u1, yH - u2
            xN, yN = xH + 2*u1, yH + 2*u2

            vec_MN_x, vec_MN_y = xN - xM, yN - yM

            R_thucte = R * 10
            d_min_thucte = d_min * 10

            # Tính toán các thông số phụ trợ cho Lời Giải chi tiết ý C
            OH_int = int(math.hypot(xH, yH))
            dist_PE_min = abs(OH_int - R)

            # Viết phương trình tổng quát đường thẳng M'N' (Ax + By + C = 0)
            A = -u2
            B = u1
            if A < 0 or (A == 0 and B < 0):
                A = -A
                B = -B
            C = -(A * xM + B * yM)

            str_B = f"+ {B}" if B >= 0 else f"- {abs(B)}"
            str_C = f"+ {C}" if C > 0 else (f"- {abs(C)}" if C < 0 else "")
            eq_line = f"{A}x {str_B}y {str_C} = 0"

            # ----------------------------------------------------------------------
            # NỘI DUNG CÂU HỎI
            # ----------------------------------------------------------------------
            noidungcauhoi = ('''Trong không gian xét hệ tọa độ $Oxyz$ có một đơn vị dài trên các trục tương ứng với 10 mét trên thực tế. Một mục tiêu cần được bảo vệ có vị trí ở gốc tọa độ $O$. Người ta thiết lập một vành đai bảo vệ quanh mục tiêu theo một đường tròn tâm $O$ có bán kính bằng $%d$ đơn vị (tương ứng $%d$ mét trên thực tế) nằm trong mặt phẳng $(Oxy)$. Một máy bay không người lái (được coi như một hạt) bay theo một đường thẳng từ vị trí $M(%d; %d; %d)$ đến vị trí $N(%d; %d; %d)$. Tại mỗi vị trí của máy bay, khoảng cách từ máy bay đến vành đai bảo vệ là độ dài ngắn nhất của các đoạn thẳng nối từ vị trí đó đến một điểm bất kì trên vành đai.''' 
                             % (R, R_thucte, xM, yM, z0, xN, yN, z0))

            # ============================ NHẬN BIẾT ============================
            nb_da_1_d = '\\True $\\overrightarrow{MN} = (%d; %d; 0)$' % (vec_MN_x, vec_MN_y)
            nb_da_1_s = '$\\overrightarrow{MN} = (%d; %d; 0)$' % (vec_MN_x + random.randint(1, 3), vec_MN_y - random.randint(1, 2))
            nb_da_1 = random.choice([nb_da_1_d, nb_da_1_s])

            loigiai_nb_1 = ('''Ta có $M(%d; %d; %d)$ và $N(%d; %d; %d)$ $\\Rightarrow \\overrightarrow{MN} = (%d; %d; 0)$.''' 
                            % (xM, yM, z0, xN, yN, z0, vec_MN_x, vec_MN_y))
            list_nb_2 = [loigiai_nb_1]

            # ============================ THÔNG HIỂU ============================
            th_da_1_d = '\\True Phương trình tham số của đường thẳng $MN$ là $\\left\\{\\begin{matrix} x = %d + %dt \\\\ y = %d %s %dt \\\\ z = %d \\end{matrix}\\right.$ với $t \\in \\mathbb{R}$' % (xM, u1, yM, '+' if u2>0 else '-', abs(u2), z0)
            th_da_1_s = 'Phương trình tham số của đường thẳng $MN$ là $\\left\\{\\begin{matrix} x = %d - %dt \\\\ y = %d %s %dt \\\\ z = %d \\end{matrix}\\right.$ với $t \\in \\mathbb{R}$' % (xM, u1, yM, '+' if u2>0 else '-', abs(u2), z0)
            th_da_1 = random.choice([th_da_1_d, th_da_1_s])

            loigiai_th_1 = ('''Đường thẳng $MN$ đi qua $M(%d; %d; %d)$ và có một vectơ chỉ phương $\\vec{u} = (%d; %d; 0)$ nên có phương trình tham số: $\\left\\{\\begin{matrix} x = %d + %dt \\\\ y = %d %s %dt \\\\ z = %d \\end{matrix}\\right. (t \\in \\mathbb{R})$.''' 
                            % (xM, yM, z0, u1, u2, xM, u1, yM, '+' if u2>0 else '-', abs(u2), z0))
            list_th_2 = [loigiai_th_1]

            # ============================ VẬN DỤNG ============================
            vd_da_1_d = '\\True Trong quá trình bay từ $M$ đến $N$, khoảng cách ngắn nhất từ máy bay đến vành đai bảo vệ là $%d$ mét' % (d_min_thucte)
            vd_da_1_s = 'Trong quá trình bay từ $M$ đến $N$, khoảng cách ngắn nhất từ máy bay đến vành đai bảo vệ là $%d$ mét' % (d_min_thucte + random.choice([10, 20, -10]))
            vd_da_1 = random.choice([vd_da_1_d, vd_da_1_s])

            # LỜI GIẢI CHI TIẾT CHO Ý C
            loigiai_vd_1 = ('''Gọi $P$ là vị trí bất kỳ của máy bay trên đoạn thẳng $MN$ và $P'$ là hình chiếu vuông góc của $P$ xuống mặt phẳng $(Oxy)$. \\\\
            Khi đó $P$ luôn có cao độ $z = %d$ nên độ dài $PP' = %d$. Tập hợp các điểm $P'$ là đoạn thẳng $M'N'$ trên mặt phẳng $(Oxy)$ với $M'(%d; %d; 0)$ và $N'(%d; %d; 0)$. \\\\
            Khoảng cách từ máy bay đến một điểm $E$ bất kỳ trên vành đai bảo vệ (đường tròn tâm $O$, bán kính $R = %d$) là: 
            $d = PE = \\sqrt{PP'^2 + P'E^2} = \\sqrt{%d^2 + P'E^2}$. \\\\
            Để $d$ nhỏ nhất thì $P'E$ phải nhỏ nhất. Theo tính chất hình học, khoảng cách ngắn nhất từ $P'$ đến đường tròn là $P'E_{\\min} = |OP' - R| = |OP' - %d|$. \\\\
            Để $|OP' - %d|$ nhỏ nhất, thì khoảng cách $OP'$ phải nhỏ nhất, tức là $P'$ trùng với hình chiếu vuông góc $H$ của $O$ lên đường thẳng $M'N'$. \\\\
            Đường thẳng $M'N'$ qua $M'(%d; %d)$, nhận $\\vec{u} = (%d; %d)$ làm vectơ chỉ phương nên có phương trình tổng quát: $%s$. \\\\
            Khoảng cách từ $O$ đến $M'N'$ là: $OH = \\frac{|%d \\cdot 0 %s \\cdot 0 %s|}{\\sqrt{%d^2 + %d^2}} = %d$. \\\\
            Suy ra $P'E_{\\min} = |%d - %d| = %d$. \\\\
            Vậy khoảng cách ngắn nhất từ máy bay đến vành đai là: $d_{\\min} = \\sqrt{%d^2 + %d^2} = %d$ (đơn vị). \\\\
            Vì $1$ đơn vị dài tương ứng với $10$ mét, nên khoảng cách ngắn nhất trên thực tế là $%d \\times 10 = %d$ (mét).''' 
            % (z0, z0, xM, yM, xN, yN, R, z0, R, R, xM, yM, u1, u2, eq_line, A, str_B, str_C, A, B, OH_int, OH_int, R, dist_PE_min, z0, dist_PE_min, d_min, d_min, d_min_thucte))
            list_vd_2 = [loigiai_vd_1]

            # ========================== VẬN DỤNG CAO ==========================
            vdc_da_1_d = '\\True Trong quá trình bay từ $M$ đến $N$, khoảng cách từ máy bay đến vành đai bảo vệ là ngắn nhất khi máy bay ở vị trí có tọa độ là $(%d; %d; %d)$' % (xH, yH, z0)
            vdc_da_1_s = 'Trong quá trình bay từ $M$ đến $N$, khoảng cách từ máy bay đến vành đai bảo vệ là ngắn nhất khi máy bay ở vị trí có tọa độ là $(%d; %d; %d)$' % (xM, yM, z0)
            vdc_da_1 = random.choice([vdc_da_1_d, vdc_da_1_s])

            loigiai_vdc_1 = ('''Dựa vào phân tích ở câu trên, hình chiếu vuông góc $H$ của $O$ lên đường thẳng $MN$ trong mặt phẳng $(Oxy)$ chính là điểm làm cho biểu thức $(OP' - R)^2$ đạt giá trị nhỏ nhất. \\\\
            Bằng cách giải hệ giữa phương trình $M'N'$ và đường thẳng qua $O$ vuông góc với $M'N'$, ta tìm được tọa độ điểm đó là $H(%d; %d; 0)$. \\\\
            Vậy vị trí của máy bay khi đạt khoảng cách ngắn nhất chính là điểm có cùng hoành độ và tung độ với $H$, tọa độ là $(%d; %d; %d)$.''' 
                             % (xH, yH, xH, yH, z0))
            list_vdc_2 = [loigiai_vdc_1]

            # ----------------------------------------------------------------------
            # TRỘN VÀ ĐẢM BẢO ĐIỀU KIỆN ĐÚNG/SAI
            # ----------------------------------------------------------------------
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_da_1 = random.choice([nb_da_1_d, nb_da_1_s])
                th_da_1 = random.choice([th_da_1_d, th_da_1_s])
                vd_da_1 = random.choice([vd_da_1_d, vd_da_1_s])
                vdc_da_1 = random.choice([vdc_da_1_d, vdc_da_1_s])

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)
                if 1 <= true_count <= 3:
                    break

            list_nb_1 = [nb_da_1]; list_th_1 = [th_da_1]; list_vd_1 = [vd_da_1]; list_vdc_1 = [vdc_da_1]

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

            # ----------------------------------------------------------------------
            # XUẤT NỘI DUNG MÃ LATEX
            # ----------------------------------------------------------------------
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi) + ' \n' +
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
                '\\end{ex}\n\\end{minipage}\n\n')
            return content 


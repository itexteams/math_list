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


def bt_dang6_p2_b1_c2_hh12(self):
            # Khai báo biến                               
            def generate_intercept_points():
                """Tạo ngẫu nhiên ba điểm trên ba trục tọa độ."""
                # Các đoạn chắn a, b, c. Đảm bảo khác 0
                a = randint(2, 5)
                b = randint(-5,-2)
                c = randint(-5,-3)     
                # Tọa độ ba điểm
                M_coords = (a, 0, 0)
                N_coords = (0, b, 0)
                P_coords = (0, 0, c)

                # Tính vectơ NM và NP
                vNM = (M_coords[0] - N_coords[0], M_coords[1] - N_coords[1], M_coords[2] - N_coords[2])
                vNP = (P_coords[0] - N_coords[0], P_coords[1] - N_coords[1], P_coords[2] - N_coords[2])

                # Phương trình tổng quát: BCNN(a, b, c) * (x/a + y/b + z/c) = 0
                # Rút gọn hệ số, đảm bảo A, B, C là các số nguyên nhỏ nhất
                # n_P = (bc, ac, ab) (Nếu tất cả đều dương)

                A_coeff = b * c
                B_coeff = a * c
                C_coeff = a * b
                D_coeff = -a * b * c

                # Rút gọn các hệ số A, B, C, D bằng cách chia cho ước chung lớn nhất
                gcd_val = math.gcd(A_coeff, math.gcd(B_coeff, math.gcd(C_coeff, D_coeff)))
                A_coeff, B_coeff, C_coeff, D_coeff = A_coeff // gcd_val, B_coeff // gcd_val, C_coeff // gcd_val, D_coeff // gcd_val

                # Điểm A (dùng cho câu c) - Tạo ngẫu nhiên và đảm bảo A không thuộc (MNP)
                xA, yA, zA = randint(-2, 2), randint(-2, 2), randint(-2, 2)
                while A_coeff * xA + B_coeff * yA + C_coeff * zA + D_coeff == 0:
                    xA += 1 # Thay đổi tọa độ để A không thuộc P

                return a, b, c, M_coords, N_coords, P_coords, A_coeff, B_coeff, C_coeff, D_coeff, vNM, vNP, (xA, yA, zA)

            # Thực hiện tạo dữ liệu
            a, b, c, M_coords, N_coords, P_coords, A_coeff, B_coeff, C_coeff, D_coeff, vNM, vNP, A_coords = generate_intercept_points()
            (xA, yA, zA) = A_coords

            # Biểu diễn LaTeX
            M_latex = '(%s; 0; 0)' % latex(a)
            N_latex = '(0; %s; 0)' % latex(b)
            P_latex = '(0; 0; %s)' % latex(c)
            A_latex = '(%s; %s; %s)' % (latex(xA), latex(yA), latex(zA))

            noidungcauhoi = (r'''Trong không gian $Oxyz$, cho ba điểm $M%s$, $N%s$ và $P%s$.''' 
                            % (M_latex, N_latex, P_latex))

            # Phương trình đoạn chắn
            ptdc_latex = r'\frac{x}{%s} + \frac{y}{%s} + \frac{z}{%s} = 1' % (latex(a), latex(b), latex(c))

            # vectơ pháp tuyến rút gọn
            nP_vectơ_latex = '(%s; %s; %s)' % (latex(A_coeff), latex(B_coeff), latex(C_coeff))

            # vectơ chỉ phương (ví dụ NM)
            vNM_latex = '(%s; %s; %s)' % (latex(vNM[0]), latex(vNM[1]), latex(vNM[2]))

            ########################################################################
            # Các câu hỏi
            ########################################################################

            # a) Nhận biết: Phương trình mặt phẳng đoạn chắn
            nb_da_1_d = r'\True Phương trình mặt phẳng $(MNP)$ có dạng $%s$' % ptdc_latex
            # Đáp án sai: Thay đổi dấu của một đoạn chắn
            ptdc_s_latex = r'\frac{x}{%s} + \frac{y}{%s} + \frac{z}{%s} = 1' % (latex(-a), latex(b), latex(c))
            nb_da_1_s = r'Phương trình mặt phẳng $(MNP)$ có dạng $%s$' % ptdc_s_latex
            list_nb_da_1=[nb_da_1_d, nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)
            loigiai_nb_1 = (r'''Mặt phẳng $(MNP)$ cắt ba trục tọa độ tại $M(a;0;0)$, $N(0;b;0)$, $P(0;0;c)$. \\
                            Phương trình mặt phẳng $(MNP)$ theo đoạn chắn là: $%s$.''' % ptdc_latex)

            # b) Thông hiểu: vectơ Pháp tuyến
            pt_tongquat_latex = r'%s x %s y %s z %s = 0' % (
                latex(A_coeff),
                '+'+latex(B_coeff) if B_coeff > 0 else latex(B_coeff),
                '+'+latex(C_coeff) if C_coeff > 0 else latex(C_coeff),
                '+'+latex(D_coeff) if D_coeff > 0 else latex(D_coeff)
            )
            th_da_1_d = r'\True Vectơ pháp tuyến của mặt phẳng $(MNP)$ là $\vec{n} = %s$' % nP_vectơ_latex
            # Đáp án sai: Đổi dấu
            nP_vectơ_s_latex = '(%s; %s; %s)' % (latex(-A_coeff), latex(B_coeff), latex(C_coeff))
            th_da_1_s = r'Vectơ pháp tuyến của mặt phẳng $(MNP)$ là $\vec{n} = %s$' % nP_vectơ_s_latex
            list_th_da_1=[th_da_1_d, th_da_1_s]
            th_da_1=random.choice(list_th_da_1)
            loigiai_th_1 = (r'''Từ phương trình đoạn chắn $%s$, ta quy đồng và rút gọn được phương trình tổng quát: $%s$. \\
                            Vậy vectơ pháp tuyến của $(MNP)$ là $\vec{n} = %s$.''' % (ptdc_latex, pt_tongquat_latex, nP_vectơ_latex))

            # c) Vận dụng: Điểm A thuộc (MNP)
            # Giá trị f(A) = A_coeff*xA + B_coeff*yA + C_coeff*zA + D_coeff
            value_A = A_coeff * (xA) + B_coeff * (yA) + C_coeff * (zA) + D_coeff
            value_A_latex = r'%s \cdot (%s) %s \cdot (%s) %s \cdot (%s) %s' % (
                latex(A_coeff), latex(xA), 
                '+'+latex(B_coeff) if B_coeff > 0 else latex(B_coeff), latex(yA),
                '+'+latex(C_coeff) if C_coeff > 0 else latex(C_coeff), latex(zA),
                '+'+latex(D_coeff) if D_coeff > 0 else latex(D_coeff)
            )

            vd_da_1_d = r'\True $A%s$ không thuộc mặt phẳng $(MNP)$' % A_latex
            # Đáp án sai: Khẳng định thuộc mặt phẳng
            vd_da_1_s = r'$A%s$ thuộc mặt phẳng $(MNP)$' % A_latex
            list_vd_da_1=[vd_da_1_d, vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)
            loigiai_vd_1 = (r'''Thay tọa độ điểm $A%s$ vào phương trình mặt phẳng $(MNP)$, ta có: \\
                            $%s = %s$. \\
                            Vì $%s \ne 0$ nên $A$ không thuộc $(MNP)$.''' 
                            % (A_latex, value_A_latex, latex(value_A), latex(value_A)))

            # d) Vận dụng cao: vectơ chỉ phương của mặt phẳng
            vdc_da_1_d = r'\True Một vectơ chỉ phương của mặt phẳng $(MNP)$ là $\vec{NM} = %s$' % vNM_latex
            # Đáp án sai: Lấy vectơ pháp tuyến
            vdc_da_1_s = r'Một vectơ chỉ phương của mặt phẳng $(MNP)$ là $\vec{n} = %s$' % nP_vectơ_latex
            list_vdc_da_1=[vdc_da_1_d, vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)
            loigiai_vdc_1 = (r'''Mặt phẳng $(MNP)$ có cặp vectơ chỉ phương là $\vec{NM}$ và $\vec{NP}$. \\
                            Ta có $\vec{NM} = (%s - 0; 0 - %s; 0 - 0) = %s$ là một vectơ chỉ phương của $(MNP)$.'''
                            % (latex(a), latex(b), vNM_latex))

            # --- Kết hợp và Xáo trộn ---
            list_nb_1 = [nb_da_1]
            list_th_1 = [th_da_1]
            list_vd_1 = [vd_da_1]
            list_vdc_1 = [vdc_da_1]

            list_nb_2 = [loigiai_nb_1]
            list_th_2 = [loigiai_th_1]
            list_vd_2 = [loigiai_vd_1]
            list_vdc_2 = [loigiai_vdc_1]

            # Đảm bảo số lượng đáp án True là 1, 2, hoặc 3
            def count_true_answers(answers):
                return sum(r'\True' in ans for ans in answers)

            # Lặp lại để chọn ngẫu nhiên đáp án đúng/sai sao cho số lượng đáp án Đúng là 1, 2, hoặc 3
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán lại vào list sau khi đã chọn ngẫu nhiên đáp án đúng/sai
            list_nb_1 = [nb_da_1]
            list_th_1 = [th_da_1]
            list_vd_1 = [vd_da_1]
            list_vdc_1 = [vdc_da_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            combined_th = list(zip(list_th_1, list_th_2))
            combined_vd = list(zip(list_vd_1, list_vd_2))
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            # Xáo trộn từng cặp (đáp án, lời giải)
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
            str(noidungcauhoi)+ 
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('- -', '+')
            return content


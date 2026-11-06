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


def bt_dang9_p2_b2_c3_hh10(self):
            # Khai báo biến
            # Khai báo biến
            x, y = symbols('x y')

            def get_line_eq(A, B):
                """Viết phương trình đường thẳng đi qua 2 điểm A(x1, y1) và B(x2, y2)"""
                x1, y1 = A
                x2, y2 = B
                a = y1 - y2
                b = x2 - x1
                c = x1*y2 - x2*y1
                # Tối giản hệ số
                common = gcd(gcd(a, b), c)
                return a//common, b//common, c//common

            def get_perp_line(point, line_coeffs):
                """Viết phương trình đường thẳng qua point và vuông góc với đường thẳng có hệ số line_coeffs (a, b, c)"""
                xp, yp = point
                a, b, c = line_coeffs
                # Đường thẳng vuông góc với ax + by + c = 0 có dạng bx - ay + m = 0
                new_a = b
                new_b = -a
                new_c = -(new_a * xp + new_b * yp)
                common = gcd(gcd(new_a, new_b), new_c)
                return new_a//common, new_b//common, new_c//common

            # 1. Sinh ngẫu nhiên tọa độ các đỉnh để bài toán đẹp (thường là số nguyên)
            while True:
                m_x, m_y = random.randint(-5, 5), random.randint(-5, 5)
                n_x, n_y = random.randint(-5, 5), random.randint(-5, 5)
                p_x, p_y = random.randint(-5, 5), random.randint(-5, 5)

                # Kiểm tra không thẳng hàng
                if (n_x - m_x) * (p_y - m_y) != (p_x - m_x) * (n_y - m_y):
                    break

            M = (m_x, m_y)
            N = (n_x, n_y)
            P = (p_x, p_y)

            # Tính toán các thông số đúng
            a1, b1, c1 = get_line_eq(M, N) # MN
            line_MN = a1*x + b1*y + c1

            # Đường cao MK vuông góc với NP
            coeffs_NP = get_line_eq(N, P)
            a_mk, b_mk, c_mk = get_perp_line(M, coeffs_NP)
            line_MK = a_mk*x + b_mk*y + c_mk

            # Đường cao NQ vuông góc với MP
            coeffs_MP = get_line_eq(M, P)
            a_nq, b_nq, c_nq = get_perp_line(N, coeffs_MP)
            line_NQ = a_nq*x + b_nq*y + c_nq

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho tam giác $MNP$ có phương trình đường thẳng chứa cạnh $MN$ là $%s=0$, phương trình đường cao $MK$ ($K \\in NP$) là $%s=0$, phương trình đường cao $NQ$ ($Q \\in MP$) là $%s=0$.''' 
                             %(latex(line_MN), latex(line_MK), latex(line_NQ)))

            ########################################################################
            # Nhận biết: Tọa độ điểm M
            m_coords_d = '\\True Điểm $M$ có tọa độ là $(%s;%s)$' % (m_x, m_y)
            m_coords_s = 'Điểm $M$ có tọa độ là $(%s;%s)$' % (m_x + random.choice([-1, 1]), m_y)
            list_nb_da_1 = [m_coords_d, m_coords_s]

            loigiai_nb_1 = ('''Tọa độ điểm $M$ là nghiệm của hệ phương trình gồm đường thẳng $MN$ và đường cao $MK$: \\\\
            $\\begin{cases} %s = 0 \\\\ %s = 0 \\end{cases} \\Leftrightarrow \\begin{cases} x = %s \\\\ y = %s \\end{cases}$. \\\\
            Vậy $M(%s;%s)$.''' % (latex(line_MN), latex(line_MK), m_x, m_y, m_x, m_y))

            ########################################################################
            # Thông hiểu: Tọa độ điểm N
            n_coords_d = '\\True Điểm $N$ có tọa độ là $(%s;%s)$' % (n_x, n_y)
            n_coords_s = 'Điểm $N$ có tọa độ là $(%s;%s)$' % (n_x, n_y + random.choice([-1, 1]))
            list_th_da_1 = [n_coords_d, n_coords_s]

            loigiai_th_1 = ('''Tọa độ điểm $N$ là nghiệm của hệ phương trình gồm đường thẳng $MN$ và đường cao $NQ$: \\\\
            $\\begin{cases} %s = 0 \\\\ %s = 0 \\end{cases} \\Leftrightarrow \\begin{cases} x = %s \\\\ y = %s \\end{cases}$. \\\\
            Vậy $N(%s;%s)$.''' % (latex(line_MN), latex(line_NQ), n_x, n_y, n_x, n_y))

            ########################################################################
            # Vận dụng: Phương trình đường thẳng NP
            np_eq_d = '\\True Phương trình đường thẳng $NP$ là $%s=0$' % (latex(coeffs_NP[0]*x + coeffs_NP[1]*y + coeffs_NP[2]))
            np_eq_s = 'Phương trình đường thẳng $NP$ là $%s=0$' % (latex(coeffs_NP[0]*x + coeffs_NP[1]*y + coeffs_NP[2] + random.randint(1, 3)))
            list_vd_da_1 = [np_eq_d, np_eq_s]

            loigiai_vd_1 = ('''Đường thẳng $NP$ đi qua điểm $N(%s;%s)$ và vuông góc với đường cao $MK$ ($%s=0$). \\\\
            Vectơ pháp tuyến của $MK$ là $\\vec{n}_{MK} = (%s; %s)$, suy ra vectơ chỉ phương của $MK$ là $\\vec{u}_{MK} = (%s; %s)$. \\\\
            Vì $NP \\perp MK$ nên $NP$ nhận $\\vec{u}_{MK}$ làm vectơ pháp tuyến. \\\\
            Phương trình $NP$: $%s(x - %s) + %s(y - %s) = 0 \\Leftrightarrow %s = 0$.''' 
                            % (n_x, n_y, latex(line_MK), a_mk, b_mk, b_mk, -a_mk, b_mk, n_x, -a_mk, n_y, latex(coeffs_NP[0]*x + coeffs_NP[1]*y + coeffs_NP[2])))

            ########################################################################
            # Vận dụng cao: Phương trình đường thẳng MP
            mp_eq_d = '\\True Phương trình đường thẳng $MP$ là $%s=0$' % (latex(coeffs_MP[0]*x + coeffs_MP[1]*y + coeffs_MP[2]))
            mp_eq_s = 'Phương trình đường thẳng $MP$ là $%s=0$' % (latex(coeffs_MP[0]*x + coeffs_MP[1]*y + coeffs_MP[2] - random.randint(1, 3)))
            list_vdc_da_1 = [mp_eq_d, mp_eq_s]

            loigiai_vdc_1 = ('''Đường thẳng $MP$ đi qua điểm $M(%s;%s)$ và vuông góc với đường cao $NQ$ ($%s=0$). \\\\
            Vectơ pháp tuyến của $NQ$ là $\\vec{n}_{NQ} = (%s; %s)$, suy ra vectơ chỉ phương của $NQ$ là $\\vec{u}_{NQ} = (%s; %s)$. \\\\
            Vì $MP \\perp NQ$ nên $MP$ nhận $\\vec{u}_{NQ}$ làm vectơ pháp tuyến. \\\\
            Phương trình $MP$: $%s(x - %s) + %s(y - %s) = 0 \\Leftrightarrow %s = 0$.''' 
                            % (m_x, m_y, latex(line_NQ), a_nq, b_nq, b_nq, -a_nq, b_nq, m_x, -a_nq, m_y, latex(coeffs_MP[0]*x + coeffs_MP[1]*y + coeffs_MP[2])))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 đúng
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)
                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                if 1 <= count_true_answers(answers) <= 3:
                    break

            # Gán lời giải tương ứng
            loigiai_list = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            # Xuất câu hỏi
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
                '{'+str(nb_da_1)+'}\n'
                '{'+str(th_da_1)+'}\n'
                '{'+str(vd_da_1)+'}\n'
                '{'+str(vdc_da_1)+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(loigiai_list[0])+'\n'
                '\\item '+str(loigiai_list[1])+'\n'
                '\\item '+str(loigiai_list[2])+'\n'
                '\\item '+str(loigiai_list[3])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('+ -', '-').replace('- -', '+')
            return content   


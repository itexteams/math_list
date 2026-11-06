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


def bt_dang7_p2_b1_c2_hh12(self):
            # Khai báo biến
            x, y, z = symbols('x y z')

            # CÁC BIẾN CỐ ĐỊNH (BASE CASE FROM THE IMAGE)
            # A(1, -3, 0), B(-5, 1, 2)
            ax, ay, az = randint(2,5), randint(-5,-2), randint(2,5)
            bx, by, bz = randint(-5,-2), randint(2,5), randint(2,5)
            # Điểm C(1, -3, 9) để tìm m=0 cho mặt phẳng (Q)
            cx, cy, cz = randint(2,5), randint(-5,-2), randint(2,8)

            # TÍNH TOÁN CÁC THÀNH PHẦN
            # 1. Vectơ AB (Pháp tuyến của P)
            v_AB_x = bx - ax
            v_AB_y = by - ay
            v_AB_z = bz - az
            # Vectơ pháp tuyến rút gọn n_P = (-3, 2, 1)
            n_P_x = v_AB_x // 2 # -6 // 2 = -3
            n_P_y = v_AB_y // 2 # 4 // 2 = 2
            n_P_z = v_AB_z // 2 # 2 // 2 = 1

            # 2. Trung điểm I
            I_x = Rational(ax + bx, 2) # -2
            I_y = Rational(ay + by, 2) # -1
            I_z = Rational(az + bz, 2) # 1

            # 3. Phương trình mặt phẳng (P): n_P_x(x - I_x) + n_P_y(y - I_y) + n_P_z(z - I_z) = 0
            # -3(x + 2) + 2(y + 1) + 1(z - 1) = 0  => -3x + 2y + z - 5 = 0
            D_P = -n_P_x * I_x - n_P_y * I_y - n_P_z * I_z # -(-3)(-2) - 2(-1) - 1(1) = -6 + 2 - 1 = -5

            # 4. Phương trình mặt phẳng (Q) song song (P): -3x + 2y + z + D_Q = 0
            # Q qua C(cx, cy, cz): -3(1) + 2(-3) + 1(9) + D_Q = 0 => -3 - 6 + 9 + D_Q = 0 => D_Q = 0
            D_Q = -n_P_x * cx - n_P_y * cy - n_P_z * cz # -(-3)(1) - 2(-3) - 1(9) = 3 + 6 - 9 = 0

            # Nội dung câu hỏi
            noidungcauhoi = ('''Trong không gian $Oxyz$, cho hai điểm $A(%s; %s; %s), B(%s; %s; %s)$. '''
                             '''Gọi $(P)$ là mặt phẳng trung trực của đoạn thẳng $AB$.'''
                             ''' Giả sử mặt phẳng $(Q)$ song song với $(P)$ và đi qua điểm $C(%s; %s; %s)$.'''
                             %(latex(ax), latex(ay), latex(az), latex(bx), latex(by), latex(bz),
                               latex(cx), latex(cy), latex(cz)
                               ))

            ########################################################################
            # Nhận biết (Vectơ AB)
            # Các đáp án
            nb_da_1_d = '\\True Vectơ $\\vec{AB}$ có tọa độ là $(%s; %s; %s)$' %(latex(v_AB_x), latex(v_AB_y), latex(v_AB_z))
            nb_da_1_s = 'Vectơ $\\vec{AB}$ có tọa độ là $(%s; %s; %s)$' %(latex(-v_AB_x), latex(-v_AB_y), latex(-v_AB_z))
            list_nb_da_1=[nb_da_1_d, nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            # Nội dung lời giải
            loigiai_nb_1 = ('''Vectơ $\\vec{AB}$ có tọa độ là $(%s; %s; %s)$.'''
                        %(latex(v_AB_x), latex(v_AB_y), latex(v_AB_z)))

            list_nb_1 = [nb_da_1]
            list_nb_2 = [loigiai_nb_1]
            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu (Trung điểm I)
            # Các đáp án
            th_da_1_d = '\\True Trung điểm $I$ của đoạn thẳng $AB$ có tọa độ là $ \\left(%s; %s; %s \\right)$' %(latex(I_x), latex(I_y), latex(I_z))
            th_da_1_s = 'Trung điểm $I$ của đoạn thẳng $AB$ có tọa độ là $\\left(%s; %s; %s \\right)$' %(latex(I_x), latex(I_y), latex(I_z + 1)) # Sai Z
            list_th_da_1=[th_da_1_d, th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            # Nội dung lời giải
            loigiai_th_1 = ('''Trung điểm $I$ của đoạn thẳng $AB$ có tọa độ là '''
                            '''$I\\left(\\frac{%s + %s}{2}; \\frac{%s + %s}{2}; \\frac{%s + %s}{2}\\right) = I \\left(%s; %s; %s \\right)$'''
                        %(latex(ax), latex(bx), latex(ay), latex(by), latex(az), latex(bz),
                          latex(I_x), latex(I_y), latex(I_z)))

            list_th_1 = [th_da_1]
            list_th_2 = [loigiai_th_1]
            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng (Mặt phẳng P)
            # Phương trình P: -3x + 2y + z - 5 = 0
            # Các đáp án
            vd_da_1_d = '\\True Phương trình mặt phẳng $(P)$ là $%s x + %s y + %s z + %s = 0$' %(latex(n_P_x), latex(n_P_y), latex(n_P_z), latex(D_P))
            vd_da_1_s = 'Phương trình mặt phẳng $(P)$ là $%s x + %s y + %s z + %s = 0$' %(latex(n_P_x), latex(n_P_y), latex(n_P_z), latex(D_P + 1)) # Sai D
            list_vd_da_1=[vd_da_1_d, vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            # Nội dung lời giải
            loigiai_vd_1 = ('''Mặt phẳng $(P)$ là mặt phẳng trung trực của $AB$ nên $(P)$ đi qua $I\\left(%s; %s; %s\\right)$ '''
                            '''và có VTPT $\\vec{n} = (%s; %s; %s)$. \\\\
                            Phương trình của $(P)$ là: $ %s \\left(x - %s \\right) + %s \\left(y - %s \\right) + %s \\left(z - %s \\right) = 0 $. \\\\
                            $\\Leftrightarrow %s x + %s y + %s z + %s = 0$.'''
                        %(latex(I_x), latex(I_y), latex(I_z), latex(n_P_x), latex(n_P_y), latex(n_P_z),
                          latex(n_P_x), latex(I_x), latex(n_P_y), latex(I_y), latex(n_P_z), latex(I_z),
                          latex(n_P_x), latex(n_P_y), latex(n_P_z), latex(D_P)))

            list_vd_1 = [vd_da_1]
            list_vd_2 = [loigiai_vd_1]
            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao (Mặt phẳng Q)
            # Phương trình Q: -3x + 2y + z + 0 = 0
            # Các đáp án
            vdc_da_1_d = '\\True Phương trình mặt phẳng $(Q)$ là $%s x + %s y + %s z = 0$' %(latex(n_P_x), latex(n_P_y), latex(n_P_z))
            vdc_da_1_s = 'Phương trình mặt phẳng $(Q)$ là $%s x + %s y + %s z + %s = 0$' %(latex(n_P_x), latex(n_P_y), latex(n_P_z), latex(D_P+1)) # D_Q khác D_P
            list_vdc_da_1=[vdc_da_1_d, vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Mặt phẳng $(Q)$ song song với $(P)$ nên có VTPT $\\vec{n} = (%s; %s; %s)$  \\\\'''
                             '''và có dạng $%s x + %s y + %s z + D = 0$. \\\\
                             $(Q)$ đi qua $C(%s; %s; %s)$ nên: $ %s \\cdot (%s) + %s \\cdot (%s) + %s \\cdot (%s) + D = 0 $ \\\\
                             $\\Leftrightarrow %s + D = 0 \\Leftrightarrow D = 0$. \\\\
                             Vậy phương trình mặt phẳng $(Q)$ là $%s x + %s y + %s z = 0$.'''
                        %(latex(n_P_x), latex(n_P_y), latex(n_P_z), latex(n_P_x), latex(n_P_y), latex(n_P_z),
                          latex(cx), latex(cy), latex(cz),
                          latex(n_P_x), latex(cx), latex(n_P_y), latex(cy), latex(n_P_z), latex(cz),
                          latex(D_Q), # Note: D_Q is 0, so the middle part simplifies to D=0.
                          latex(n_P_x), latex(n_P_y), latex(n_P_z)))


            list_vdc_1 = [vdc_da_1]
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('+ -', '-').replace('+ 0 z', '').replace('-1 z', '-z').replace('+ 1 z', '+z').replace('- -', '+')
            return content


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


def bt_dang8_p2_b2_c2_hh12(self):
            # Khai báo biến
            M_coords = (2, -2, -5)
            d1_point = (1, -2, -1)
            d1_direction = (3, 1, 2)
            d2_point = (1, -1, 0)
            d2_direction = (2, 1, -1)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Trong không gian $Oxyz$, cho điểm $M(%s;%s;%s)$ và hai đường thẳng \\begin{center} $d_1: \\begin{cases} x=%s+%st \\\\ y=%s+%st \\\\ z=%s+%st \\end{cases}$ và $d_2: \\frac{x-%s}{%s} = \\frac{y-%s}{%s} = \\frac{z-%s}{%s}$.\\end{center}'''
                             %(M_coords[0], M_coords[1], M_coords[2],
                               d1_point[0], d1_direction[0], d1_point[1], d1_direction[1], d1_point[2], d1_direction[2],
                               d2_point[0], d2_direction[0], d2_point[1], d2_direction[1], d2_point[2], d2_direction[2]
                                 ))

            ########################################################################Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Vectơ chỉ phương của đường thẳng $d_1$ là $\\vec{u_1}=(%s;%s;%s)$' %(d1_direction[0], d1_direction[1], d1_direction[2])
            nb_da_1_s = 'Vectơ chỉ phương của đường thẳng $d_1$ là $\\vec{u_1}=(%s;%s;%s)$' %(d1_direction[0], d1_direction[1], -d1_direction[2])
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Từ phương trình tham số của đường thẳng $d_1$, ta có vectơ chỉ phương là $\\vec{u_1}=(%s;%s;%s)$.'''
                         %(d1_direction[0], d1_direction[1], d1_direction[2])
                         )

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################Thông hiểu ############################################
            # Các đáp án
            u1 = sp.Matrix(d1_direction)
            u2 = sp.Matrix(d2_direction)
            u_cross = u1.cross(u2)
            u_false = u1.cross(u2) * -1
            th_da_1_d = '\\True Vectơ chỉ phương của đường thẳng vuông góc với cả hai đường thẳng $d_1, d_2$ là $\\vec{u}=(%s;%s;%s)$' %(u_cross[0], u_cross[1], u_cross[2])
            th_da_1_s = 'Vectơ chỉ phương của đường thẳng vuông góc với cả hai đường thẳng $d_1, d_2$ là $\\vec{u}=(%s;%s;%s)$' %(u_false[0], u_false[1], u_false[2])
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Vectơ chỉ phương của $d_1$ là $\\vec{u_1}=(%s;%s;%s)$. \\\\
                            Vectơ chỉ phương của $d_2$ là $\\vec{u_2}=(%s;%s;%s)$.\\\\
            Vectơ chỉ phương của đường thẳng vuông góc với cả hai đường thẳng $d_1, d_2$ là \\\\ $\\vec{u}=[\\vec{u_1}, \\vec{u_2}] = (%s;%s;%s)$.'''
                         %(d1_direction[0], d1_direction[1], d1_direction[2],
                           d2_direction[0], d2_direction[1], d2_direction[2],
                           u_cross[0], u_cross[1], u_cross[2])
                         )

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vậndụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Điểm $N$ thuộc đường thẳng $d_2$ có tọa độ dạng $(1+2t; -1+t; -t)$ với $t \\in \\mathbb{R}$'
            vd_da_1_s = 'Điểm $N$ thuộc đường thẳng $d_2$ có tọa độ dạng $(1+2t; 1+t; -t)$ với $t \\in \\mathbb{R}$'
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Từ phương trình chính tắc của đường thẳng $d_2$, ta có \\\\
                            Phương trình tham số của $d_2: \\begin{cases} x=1+2t \\\\ y=-1+t \\\\ z=0-t \\end{cases}$.\\\\
            Vậy tọa độ điểm $N$ thuộc đường thẳng $d_2$ có dạng $(1+2t; -1+t; -t)$ với $t \\in \\mathbb{R}$.'''
                         )

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vậndụng cao ############################################
            # Các đáp án
            N_t = (1 + 2*t, -1 + t, -t)
            MN_vec_t = (N_t[0] - M_coords[0], N_t[1] - M_coords[1], N_t[2] - M_coords[2])
            MN_sq = (MN_vec_t[0])**2 + (MN_vec_t[1])**2 + (MN_vec_t[2])**2
            dMN_sq_dt = diff(MN_sq, t)
            t_min = solve(dMN_sq_dt, t)[0]
            N_min = (N_t[0].subs(t, t_min), N_t[1].subs(t, t_min), N_t[2].subs(t, t_min))
            a_plus_b_plus_c = N_min[0] + N_min[1] + N_min[2]

            vdc_da_1_d = '\\True Khi khoảng cách $MN$ nhỏ nhất thì $a+b+c=%s$, với $N(a;b;c)$ là điểm thuộc $d_2$' %(latex(a_plus_b_plus_c))
            vdc_da_1_s = 'Khi khoảng cách $MN$ nhỏ nhất thì $a+b+c=%s$, với $N(a;b;c)$ là điểm thuộc $d_2$' %(latex(a_plus_b_plus_c + 2))
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Điểm $N$ thuộc $d_2$ có tọa độ dạng $N(1+2t; -1+t; -t)$. \\\\
            Ta có $M(%s;%s;%s)$. Khoảng cách $MN$ nhỏ nhất khi $MN^2$ nhỏ nhất. \\\\
            $MN^2 = (1+2t-2)^2+(-1+t-(-2))^2+(-t-(-5))^2$\\\\
            $MN^2 = (2t-1)^2+(t+1)^2+(-t+5)^2 = (4t^2-4t+1)+(t^2+2t+1)+(t^2-10t+25)$\\\\
            $MN^2 = 6t^2 - 12t + 27$. \\\\
            Để $MN^2$ nhỏ nhất, ta xét đạo hàm theo $t$:\\\\
            $(MN^2)' = 12t - 12$. Cho $(MN^2)' = 0 \\Rightarrow 12t - 12 = 0 \\Rightarrow t=1$.\\\\
            Với $t=1$, ta tìm được điểm $N$ có tọa độ là \\\\
            $N(1+2(1); -1+1; -1) \\Rightarrow N(3; 0; -1)$.\\\\
            Khi đó, $a+b+c = 3+0-1 = 2$.'''
                         %(M_coords[0], M_coords[1], M_coords[2])
                         )

            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vdc)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('+-', '-').replace('--', '+')
            return content   


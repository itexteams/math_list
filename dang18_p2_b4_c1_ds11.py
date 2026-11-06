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


def bt_dang18_p2_b4_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # B3-Suy nghĩ tìm cách random bài toán
            # Ta random tử số và mẫu số của góc pha ban đầu để tạo ra nhiều bài toán tương tự.
            # Trong hình mẫu là pi/4. Ta chọn ngẫu nhiên pha ban đầu alpha từ danh sách [pi/6, pi/4, pi/3]
            alpha_list = [Rational(1, 6), Rational(1, 4), Rational(1, 3)]
            alpha_frac = random.choice(alpha_list)

            # Tính toán các thông số dựa theo alpha_frac để đảm bảo tính chính xác cho các câu hỏi
            # Phương trình: sin(x + alpha) = sin(x)
            # <=> x + alpha = x + k2pi (vô nghiệm k) hoặc x + alpha = pi - x + k2pi
            # <=> 2x = pi - alpha + k2pi <=> x = (pi - alpha)/2 + kpi
            hoanh_do_dung_frac = Rational(1 - alpha_frac, 2) # Giá trị trước pi

            # Tạo phương án hoành độ sai
            hoanh_do_sai_frac = Rational(1 + alpha_frac, 2)

            # Đếm số nghiệm trong khoảng [0, 2pi]
            # 0 <= (1-alpha)/2 + k <= 2  <=> -hoanh_do_dung_frac <= k <= 2 - hoanh_do_dung_frac
            # Vì alpha_frac thuộc (0, 1) nên hoanh_do_dung_frac thuộc (0, 0.5)
            # k có thể nhận các giá trị nguyên là 0 và 1. Vậy luôn có hai giao điểm.
            so_giao_diem_dung = "hai điểm"
            so_giao_diem_sai = "ba điểm"

            # Tính tọa độ cụ thể cho hai nghiệm k = 0 và k = 1 để dùng cho câu d
            # k = 0: x1 = hoanh_do_dung_frac * pi
            x1_frac = hoanh_do_dung_frac
            # k = 1: x2 = (hoanh_do_dung_frac + 1) * pi
            x2_frac = hoanh_do_dung_frac + 1

            x1_sai_frac = hoanh_do_sai_frac
            x2_sai_frac = hoanh_do_sai_frac + 1

            # Tạo các chuỗi hiển thị latex sinh động theo tham số ngẫu nhiên
            str_alpha = latex(alpha_frac) + '\\pi' if alpha_frac != 1 else '\\pi'
            str_hoanh_do_dung = latex(hoanh_do_dung_frac) + '\\pi'
            str_hoanh_do_sai = latex(hoanh_do_sai_frac) + '\\pi'

            str_x1_d = latex(x1_frac) + '\\pi'
            str_x2_d = latex(x2_frac) + '\\pi'
            str_x1_s = latex(x1_sai_frac) + '\\pi'
            str_x2_s = latex(x2_sai_frac) + '\\pi'

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hai đồ thị hàm số $y = \\sin\\left( x + \\frac{%s}{1} \\right)$ và $y = \\sin x$, khi đó:''' 
                             % (str_alpha)) if alpha_frac.denominator == 1 else ('''Cho hai đồ thị hàm số $y = \\sin\\left( x + \\frac{\\pi}{%s} \\right)$ và $y = \\sin x$, khi đó:''' 
                             % (latex(alpha_frac.denominator)))

            ########################################################################
            # Nhận biết ############################################
            nb_da_1_d = '\\True Phương trình hoành độ giao điểm của hai đồ thị hàm số: $\\sin\\left( x + \\frac{\\pi}{%s} \\right) = \\sin x$' % (latex(alpha_frac.denominator))
            nb_da_1_s = 'Phương trình hoành độ giao điểm của hai đồ thị hàm số: $\\sin\\left( x + \\frac{\\pi}{%s} \\right) + \\sin x = 0$' % (latex(alpha_frac.denominator))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = ('''Phương trình hoành độ giao điểm của hai đồ thị hàm số được xác định bằng cách cho hai vế phải bằng nhau, ta được: $\\sin\\left( x + \\frac{\\pi}{%s} \\right) = \\sin x$.''' 
                            % (latex(alpha_frac.denominator)))

            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            th_da_1_d = '\\True Hoành độ giao điểm của hai đồ thị là $x = \\frac{%s}{%s}\\pi + k\\pi (k \\in \\mathbb{Z})$' % (latex(hoanh_do_dung_frac.numerator), latex(hoanh_do_dung_frac.denominator))
            th_da_1_s = 'Hoành độ giao điểm của hai đồ thị là $x = \\frac{%s}{%s}\\pi + k\\pi (k \\in \\mathbb{Z})$' % (latex(hoanh_do_sai_frac.numerator), latex(hoanh_do_sai_frac.denominator))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            loigiai_th_1 = ('''Giải phương trình hoành độ giao điểm:\\\\
            $\\sin\\left( x + \\frac{\\pi}{%s} \\right) = \\sin x \\Leftrightarrow \\left[\\begin{aligned} & x + \\frac{\\pi}{%s} = x + k2\\pi \\text{ (vô nghiệm)} \\\\ & x + \\frac{\\pi}{%s} = \\pi - x + k2\\pi \\end{aligned}\\right.$\\\\
            $\\Leftrightarrow 2x = \\pi - \\frac{\\pi}{%s} + k2\\pi \\Leftrightarrow 2x = \\frac{%s\\pi}{%s} + k2\\pi \\Leftrightarrow x = \\frac{%s}{%s}\\pi + k\\pi (k \\in \\mathbb{Z})$.''' 
                            % (latex(alpha_frac.denominator), latex(alpha_frac.denominator), latex(alpha_frac.denominator), latex(alpha_frac.denominator), latex((1-alpha_frac).numerator), latex((1-alpha_frac).denominator), latex(hoanh_do_dung_frac.numerator), latex(hoanh_do_dung_frac.denominator)))

            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng ############################################
            vd_da_1_d = '\\True Khi $x \\in [0;2\\pi]$ thì hai đồ thị hàm số cắt nhau tại %s' % (so_giao_diem_dung)
            vd_da_1_s = 'Khi $x \\in [0;2\\pi]$ thì hai đồ thị hàm số cắt nhau tại %s' % (so_giao_diem_sai)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = ('''Vì $x \\in [0;2\\pi]$ nên ta xét điều kiện cho họ nghiệm tìm được:\\\\
            $0 \\le \\frac{%s}{%s}\\pi + k\\pi \\le 2\\pi \\Leftrightarrow 0 \\le \\frac{%s}{%s} + k \\le 2 \\Leftrightarrow -\\frac{%s}{%s} \\le k \\le 2 - \\frac{%s}{%s}$.\\\\
            Do $k \\in \\mathbb{Z}$ nên ta chọn được $k = 0$ và $k = 1$.\\\\
            Vậy trong khoảng $[0;2\\pi]$, hai đồ thị hàm số cắt nhau tại hai điểm.''' 
                            % (latex(hoanh_do_dung_frac.numerator), latex(hoanh_do_dung_frac.denominator), latex(hoanh_do_dung_frac.numerator), latex(hoanh_do_dung_frac.denominator), latex(hoanh_do_dung_frac.numerator), latex(hoanh_do_dung_frac.denominator), latex(hoanh_do_dung_frac.numerator), latex(hoanh_do_dung_frac.denominator)))

            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao ############################################
            vdc_da_1_d = '\\True Khi $x \\in [0;2\\pi]$ thì tọa độ giao điểm của hai đồ thị hàm số là: $\\left( \\frac{%s}{%s}\\pi ; \\sin\\frac{%s\\pi}{%s} \\right), \\left( \\frac{%s}{%s}\\pi ; \\sin\\frac{%s\\pi}{%s} \\right)$' % (latex(x1_frac.numerator), latex(x1_frac.denominator), latex(x1_frac.numerator), latex(x1_frac.denominator), latex(x2_frac.numerator), latex(x2_frac.denominator), latex(x2_frac.numerator), latex(x2_frac.denominator))
            vdc_da_1_s = 'Khi $x \\in [0;2\\pi]$ thì tọa độ giao điểm của hai đồ thị hàm số là: $\\left( \\frac{%s}{%s}\\pi ; \\sin\\frac{%s\\pi}{%s} \\right), \\left( \\frac{%s}{%s}\\pi ; \\sin\\frac{%s\\pi}{%s} \\right)$' % (latex(x1_sai_frac.numerator), latex(x1_sai_frac.denominator), latex(x1_sai_frac.numerator), latex(x1_sai_frac.denominator), latex(x2_sai_frac.numerator), latex(x2_sai_frac.denominator), latex(x2_sai_frac.numerator), latex(x2_sai_frac.denominator))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = ('''Ứng với hai giá trị $k=0$ và $k=1$ tìm được ở câu trên, ta tính các hoành độ và tung độ giao điểm tương ứng:\\\\
            - Với $k=0 \\Rightarrow x = \\frac{%s}{%s}\\pi \\Rightarrow y = \\sin\\left(\\frac{%s}{%s}\\pi\\right)$. Ta được tọa độ giao điểm thứ nhất.\\\\
            - Với $k=1 \\Rightarrow x = \\frac{%s}{%s}\\pi + \\pi = \\frac{%s}{%s}\\pi \\Rightarrow y = \\sin\\left(\\frac{%s}{%s}\\pi\\right)$. Ta được tọa độ giao điểm thứ hai.\\\\
            Vậy tọa độ các giao điểm của hai đồ thị hàm số là $\\left( \\frac{%s}{%s}\\pi ; \\sin\\frac{%s\\pi}{%s} \\right)$ và $\\left( \\frac{%s}{%s}\\pi ; \\sin\\frac{%s\\pi}{%s} \\right)$.''' 
                             % (latex(x1_frac.numerator), latex(x1_frac.denominator), latex(x1_frac.numerator), latex(x1_frac.denominator), latex(x1_frac.numerator), latex(x1_frac.denominator), latex(x2_frac.numerator), latex(x2_frac.denominator), latex(x2_frac.numerator), latex(x2_frac.denominator), latex(x1_frac.numerator), latex(x1_frac.denominator), latex(x1_frac.numerator), latex(x1_frac.denominator), latex(x2_frac.numerator), latex(x2_frac.denominator), latex(x2_frac.numerator), latex(x2_frac.denominator)))

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
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


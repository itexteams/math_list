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


def bt_dang27_p2_b4_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # B3-Suy nghĩ tìm cách random bài toán
            # Random hệ số tự do c để sinh các số liệu bài toán khác nhau
            c_val = random.choice([0, 1, 2])

            # Tính toán các thông số theo c_val
            tung_do_b = 2 + c_val
            gtnn_t = Rational(-9, 8) + c_val
            gtln_t = 2 + c_val
            tong_max_min_dung = gtln_t + gtnn_t
            tong_max_min_sai = Rational(13, 8) + c_val

            # Chuỗi hiển thị latex động
            if c_val == 0:
                str_f_x = "\\cos 2x + \\cos x"
                str_pt_c = "[f(x) + 1]^3 = 0"
                str_pt_c_vp = "\\frac{\\cos x (8\\cos^3 x + 1)}{\\sqrt{3}\\cos x + 1} = 0"
                str_loigiai_c = ('''Phương trình $[f(x)+1]^3 = 0 \\Leftrightarrow \\cos 2x + \\cos x + 1 = 0 \\Leftrightarrow 2\\cos^2 x + \\cos x = 0 \\Leftrightarrow \\cos x(2\\cos x + 1) = 0$.\\\\ Phương trình vế phải có điều kiện xác định $\\sqrt{3}\\cos x + 1 \\neq 0 \\Leftrightarrow \\cos x \\neq -\\frac{1}{\\sqrt{3}}$. Do điều kiện làm thu hẹp tập nghiệm nên hai phương trình không tương đương.''')
            elif c_val == 1:
                str_f_x = "\\cos 2x + \\cos x + 1"
                str_pt_c = "[f(x)]^3 = 0"
                str_pt_c_vp = "\\frac{\\cos x (8\\cos^3 x + 1)}{\\sqrt{3}\\cos x + 1} = 0"
                str_loigiai_c = ('''Phương trình $[f(x)]^3 = 0 \\Leftrightarrow \\cos 2x + \\cos x + 1 = 0 \\Leftrightarrow 2\\cos^2 x + \\cos x = 0 \\Leftrightarrow \\cos x(2\\cos x + 1) = 0$.\\\\ Phương trình vế phải có điều kiện biến số mẫu thức khác không nên tập nghiệm không tương đương nhau.''')
            else:
                str_f_x = "\\cos 2x + \\cos x + 2"
                str_pt_c = "[f(x) - 1]^3 = 0"
                str_pt_c_vp = "\\frac{\\cos x (8\\cos^3 x + 1)}{\\sqrt{3}\\cos x + 1} = 0"
                str_loigiai_c = ('''Phương trình $[f(x)-1]^3 = 0 \\Leftrightarrow \\cos 2x + \\cos x + 1 = 0 \\Leftrightarrow 2\\cos^2 x + \\cos x = 0 \\Leftrightarrow \\cos x(2\\cos x + 1) = 0$.\\\\ Vế phải có điều kiện xác định đi kèm làm loại nghiệm nên không thể tương đương nhau.''')

            # Nội dung câu hỏi sử dụng định dạng %s theo yêu cầu bắt buộc
            noidungcauhoi = ('''Cho hàm số $f(x) = %s$.''' % (str_f_x))

            ########################################################################
            # Nhận biết ############################################
            nb_da_1_s = 'Hàm số đã cho là hàm số chẵn và có chu kỳ $T = \\pi$'
            nb_da_1_d = '\\True Hàm số đã cho là hàm số chẵn và có chu kỳ $T = 2\\pi$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = ('''Tập xác định của hàm số là $\\mathscr{D} = \\mathbb{R}$.\\\\ Ta có $f(-x) = \\cos(-2x) + \\cos(-x) %s = \\cos 2x + \\cos x %s = f(x)$ nên hàm số đã cho là hàm số chẵn.\\\\ Chu kỳ tuần hoàn của hàm số $y = \\cos 2x$ là $\\pi$, chu kỳ của $y = \\cos x$ là $2\\pi$. Chu kỳ chung nhỏ nhất của hàm số $f(x)$ phải là $2\\pi$.''' 
                            % (("+ " + str(c_val)) if c_val > 0 else "", ("+ " + str(c_val)) if c_val > 0 else ""))

            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            th_da_1_s = 'Đồ thị hàm số không đi qua điểm $(0;%s)$' % (latex(tung_do_b))
            th_da_1_d = '\\True Đồ thị hàm số đi qua điểm $(0;%s)$' % (latex(tung_do_b))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            loigiai_th_1 = ('''Thay giá trị hoành độ $x = 0$ vào hàm số, ta có:\\\\ $f(0) = \\cos 0 + \\cos 0 %s = 1 + 1 %s = %s$.\\\\ Do đó đồ thị hàm số luôn đi qua điểm có tọa độ là $(0;%s)$.''' 
                            % (("+ " + str(c_val)) if c_val > 0 else "", ("+ " + str(c_val)) if c_val > 0 else "", str(tung_do_b), str(tung_do_b)))

            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng ############################################
            vd_da_1_s = 'Phương trình $%s$ tương đương với phương trình $%s$' % (str_pt_c, str_pt_c_vp)
            vd_da_1_d = '\\True Phương trình $%s$ không tương đương với phương trình $%s$' % (str_pt_c, str_pt_c_vp)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            list_vd_2 = [str_loigiai_c]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao ############################################
            vdc_da_1_d = '\\True Tổng giá trị lớn nhất và giá trị nhỏ nhất của hàm số đã cho bằng $\\frac{%s}{%s}$' % (latex(tong_max_min_dung.numerator), latex(tong_max_min_dung.denominator))
            vdc_da_1_s = 'Tổng giá trị lớn nhất và giá trị nhỏ nhất của hàm số đã cho bằng $\\frac{%s}{%s}$' % (latex(tong_max_min_sai.numerator), latex(tong_max_min_sai.denominator))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = ('''Biến đổi hàm số về dạng tam thức bậc hai theo ẩn $\\cos x$:\\\\ $f(x) = (2\\cos^2 x - 1) + \\cos x %s = 2\\cos^2 x + \\cos x %s$.\\\\ Đặt $t = \\cos x$, điều kiện $t \\in [-1; 1]$. Hàm số trở thành $g(t) = 2t^2 + t %s$.\\\\ Parabol có tọa độ đỉnh tại hoành độ $t = -\\frac{1}{4} \\in [-1; 1]$.\\\\ Giá trị nhỏ nhất của hàm số đạt được tại đỉnh: $\\text{GTNN} = g\\left(-\\frac{1}{4}\\right) = %s$.\\\\ Tính giá trị biên tại hai đầu mút: $g(-1) = %s$, $g(1) = %s$.\\\\ Suy ra giá trị lớn nhất của hàm số là $\\text{GTLN} = %s$.\\\\ Tổng giá trị lớn nhất và giá trị nhỏ nhất bằng: $%s + \\left(%s\\right) = \\frac{%s}{%s}$''' 
                             % (("+ " + str(c_val)) if c_val > 0 else "", ("+ " + str(c_val - 1)) if (c_val - 1) != 0 else "", ("+ " + str(c_val - 1)) if (c_val - 1) != 0 else "", latex(gtnn_t), latex(c_val), latex(gtln_t), latex(gtln_t), latex(gtln_t), latex(gtnn_t), latex(tong_max_min_dung.numerator), latex(tong_max_min_dung.denominator)))

            list_vdc_2 = [loigiai_vdc_1]

            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)


            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án tổng hợp có từ 1 đến 3 đúng
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

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn qua định dạng %s
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


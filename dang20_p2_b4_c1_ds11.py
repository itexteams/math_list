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


def bt_dang20_p2_b4_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # B3-Suy nghĩ tìm cách random bài toán
            # Hàm số f(x) = sqrt(a*x - x^2)
            # Hàm số g(x) = cos(2x)
            # Ta random hệ số a lấy giá trị trong [3, 4] để bài toán có nghiệm đẹp và đa dạng.
            a_val = random.choice([3, 4])

            # Thiết lập các chuỗi và giá trị toán học động theo tham số a_val
            if a_val == 3:
                str_f = "\\sqrt{3x - x^2}"
                f_1_val = sqrt(2)
                str_f_1_dung = "\\sqrt{2}"
                str_f_1_sai = "2"
                # Tập xác định của f(x): 3x - x^2 >= 0 <=> x in [0, 3]
                # Giải phương trình f(x).g(x) = 0:
                # TH1: 3x - x^2 = 0 <=> x = 0 hoặc x = 3 (2 nghiệm thuộc [0, 3])
                # TH2: cos(2x) = 0 <=> 2x = pi/2 + k*pi <=> x = pi/4 + k*pi/2
                # Vì x in [0, 3], do pi/4 ≈ 0.785, 3pi/4 ≈ 2.356, 5pi/4 ≈ 3.927
                # Nên có 2 nghiệm lượng giác thuộc [0, 3] là pi/4 và 3pi/4.
                # Tổng cộng có 2 + 2 = 4 nghiệm thực.
                so_nghiem_dung = "4 nghiệm thực"
                so_nghiem_sai = "5 nghiệm thực"
                loigiai_d_chi_tiet = ('''Xét phương trình $f(x) \\cdot g(x) = 0 \\Leftrightarrow \\left[\\begin{aligned} & \\sqrt{3x - x^2} = 0 \\\\ & \\cos 2x = 0 \\end{aligned}\\right.$\\\\
            - Với $\\sqrt{3x - x^2} = 0 \\Leftrightarrow 3x - x^2 = 0 \\Leftrightarrow \\left[\\begin{aligned} & x = 0 \\\\ & x = 3 \\end{aligned}\\right.$ (thỏa mãn tập xác định $[0;3]$).\\\\
            - Với $\\cos 2x = 0 \\Leftrightarrow 2x = \\frac{\\pi}{2} + k\\pi \\Leftrightarrow x = \\frac{\\pi}{4} + k\\frac{\\pi}{2}$ ($k \\in \\mathbb{Z}$).\\\\
            Do $x \\in [0;3]$ nên ta tìm được các giá trị $k = 0 \\Rightarrow x = \\frac{\\pi}{4}$ và $k = 1 \\Rightarrow x = \\frac{3\\pi}{4}$.\\\\
            Vậy phương trình có tất cả $4$ nghiệm thực.''')
            else:
                str_f = "\\sqrt{4x - x^2}"
                f_1_val = sqrt(3)
                str_f_1_dung = "\\sqrt{3}"
                str_f_1_sai = "\\sqrt{2}"
                # Tập xác định của f(x): 4x - x^2 >= 0 <=> x in [0, 4]
                # Giải phương trình f(x).g(x) = 0:
                # TH1: x = 0 hoặc x = 4 (2 nghiệm thuộc [0, 4])
                # TH2: x = pi/4 + k*pi/2
                # Vì x in [0, 4], pi/4 ≈ 0.785, 3pi/4 ≈ 2.356, 5pi/4 ≈ 3.927
                # Nên có 3 nghiệm lượng giác thuộc [0, 4] là pi/4, 3pi/4, 5pi/4.
                # Tổng cộng có 2 + 3 = 5 nghiệm thực.
                so_nghiem_dung = "5 nghiệm thực"
                so_nghiem_sai = "4 nghiệm thực"
                loigiai_d_chi_tiet = ('''Xét phương trình $f(x) \\cdot g(x) = 0 \\Leftrightarrow \\left[\\begin{aligned} & \\sqrt{4x - x^2} = 0 \\\\ & \\cos 2x = 0 \\end{aligned}\\right.$\\\\
            - Với $\\sqrt{4x - x^2} = 0 \\Leftrightarrow 4x - x^2 = 0 \\Leftrightarrow \\left[\\begin{aligned} & x = 0 \\\\ & x = 4 \\end{aligned}\\right.$ (thỏa mãn tập xác định $[0;4]$).\\\\
            - Với $\\cos 2x = 0 \\Leftrightarrow 2x = \\frac{\\pi}{2} + k\\pi \\Leftrightarrow x = \\frac{\\pi}{4} + k\\frac{\\pi}{2}$ ($k \\in \\mathbb{Z}$).\\\\
            Do $x \\in [0;4]$ nên ta tìm được các giá trị $k = 0 \\Rightarrow x = \\frac{\\pi}{4}$, $k = 1 \\Rightarrow x = \\frac{3\\pi}{4}$ và $k = 2 \\Rightarrow x = \\frac{5\\pi}{4}$.\\\\
            Vậy phương trình có tất cả $5$ nghiệm thực.''')

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hai hàm số $f(x) = %s$; $g(x) = \\cos 2x$. Xét tính đúng – sai của các mệnh đề sau:''' % (str_f))

            ########################################################################
            # Nhận biết ############################################
            nb_da_1_d = '\\True Đồ thị hàm số $f(x)$ đi qua điểm $\\left( 1; %s \\right)$' % (str_f_1_dung)
            nb_da_1_s = 'Đồ thị hàm số $f(x)$ đi qua điểm $\\left( 1; %s \\right)$' % (str_f_1_sai)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = ('''Thay $x = 1$ vào biểu thức hàm số $f(x)$, ta được:\\\\
            $f(1) = \\sqrt{%s \\cdot 1 - 1^2} = %s$.\\\\
            Do đó, đồ thị hàm số $f(x)$ đi qua điểm $\\left( 1; %s \\right)$''' 
                            % (latex(a_val), str_f_1_dung, str_f_1_dung))

            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            th_da_1_d = '\\True Hàm số $g^2(x)$ có chu kỳ $T = \\frac{\\pi}{2}$'
            th_da_1_s = 'Hàm số $g^2(x)$ có chu kỳ $T = \\pi$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            loigiai_th_1 = ('''Sử dụng công thức hạ bậc đối với hàm số $g^2(x)$:\\\\
            $g^2(x) = \\cos^2 2x = \\frac{1 + \\cos 4x}{2} = \\frac{1}{2} + \\frac{1}{2}\\cos 4x$.\\\\
            Hàm số $y = \\cos 4x$ có chu kỳ tuần hoàn là $T = \\frac{2\\pi}{4} = \\frac{\\pi}{2}$.\\\\
            Do đó, hàm số $g^2(x)$ có chu kỳ $T = \\frac{\\pi}{2}$''')

            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng ############################################
            vd_da_1_d = '\\True Hàm số $g(x)$ có giá trị lớn nhất bằng $1$'
            vd_da_1_s = 'Hàm số $g(x)$ có giá trị lớn nhất bằng $2$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = ('''Với mọi số thực $x$, ta luôn có thuộc tính lượng giác cơ bản: $-1 \\le \\cos 2x \\le 1$.\\\\
            Do đó, giá trị lớn nhất của hàm số $g(x) = \\cos 2x$ bằng $1$, đạt được khi $2x = k2\\pi \\Leftrightarrow x = k\\pi$ ($k \\in \\mathbb{Z}$).''')

            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao ############################################
            vdc_da_1_d = '\\True Phương trình $f(x) \\cdot g(x) = 0$ có %s' % (so_nghiem_dung)
            vdc_da_1_s = 'Phương trình $f(x) \\cdot g(x) = 0$ có %s' % (so_nghiem_sai)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = ('''Hàm số $f(x) = %s$ xác định khi và chỉ khi $%sx - x^2 \\ge 0 \\Leftrightarrow x \\in [0; %s]$.\\\\
            %s''' % (str_f, latex(a_val), latex(a_val), loigiai_d_chi_tiet))

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


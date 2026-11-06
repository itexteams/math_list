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


def bt_dang13_p2_b3_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến và tạo bài toán ngẫu nhiên dạng y = (ax + b) / (cx + d)
            x = symbols('x')

            while True:
                c = random.choice([1, 2])
                x_0 = random.randint(-4, -1)  # Tiệm cận đứng x = x_0
                d = -c * x_0
                y_tcn = random.randint(1, 3)  # Tiệm cận ngang y = y_tcn
                a = c * y_tcn

                # Đảm bảo đạo hàm tử số ad - bc > 0 để hàm số luôn đồng biến
                max_b = (a * d) // c
                b = random.randint(max_b - 5, max_b - 1)

                if a * d - b * c > 0 and b != 0:
                    break

            # Các khoảng đồng biến ngẫu nhiên k_1 < x_0 và k_2 > x_0
            k_1 = x_0 - random.randint(5, 10)
            k_2 = x_0 + random.randint(5, 12)

            # Đoạn [alpha, beta] nằm hoàn toàn bên phải tiệm cận đứng để tính max, min
            alpha = random.randint(1, 3)
            beta = alpha + random.randint(2, 4)

            # Tính giá trị lớn nhất và nhỏ nhất trên đoạn [alpha, beta]
            y_min = Rational(a * alpha + b, c * alpha + d)
            y_max = Rational(a * beta + b, c * beta + d)

            # Tạo biểu thức phân thức dưới dạng LaTeX
            bt_tu = a * x + b
            bt_mau = c * x + d
            ham_so_latex = '\\frac{%s}{%s}' % (latex(bt_tu), latex(bt_mau))

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hàm số $y = %s$ có đồ thị là $(C)$.''' % (ham_so_latex))

            ########################################################################
            # Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Đường thẳng $y = %s$ là tiệm cận ngang của $(C)$' % (latex(y_tcn))
            nb_da_1_s = 'Đường thẳng $y = %s$ là tiệm cận ngang của $(C)$' % (latex(a if a != y_tcn else a + 1))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Ta có $\\lim_{x \\to +\\infty} y = \\lim_{x \\to +\\infty} \\frac{%s}{%s} = %s$ và $\\lim_{x \\to -\\infty} y = \\lim_{x \\to -\\infty} \\frac{%s}{%s} = %s$.\\\\
            Do đó, đường thẳng $y = %s$ là đường tiệm cận ngang của đồ thị hàm số $(C)$.''' 
                            % (latex(bt_tu), latex(bt_mau), latex(y_tcn), latex(bt_tu), latex(bt_mau), latex(y_tcn), latex(y_tcn)))

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Đường thẳng $x = %s$ là tiệm cận đứng của $(C)$' % (latex(x_0))
            th_da_1_s = 'Đường thẳng $x = %s$ là tiệm cận đứng của $(C)$' % (latex(-x_0))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Ta có mẫu số $%s = 0 \\Leftrightarrow x = %s$.\\\\
            Đồng thời $\\lim_{x \\to (%s)^+} y = +\\infty$ và $\\lim_{x \\to (%s)^-} y = -\\infty$.\\\\
            Do đó, đường thẳng $x = %s$ là đường tiệm cận đứng của đồ thị hàm số $(C)$.''' 
                            % (latex(bt_mau), latex(x_0), latex(x_0), latex(x_0), latex(x_0)))

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Hàm số đã cho đồng biến trên các khoảng $\\left(-\\infty; %s\\right)$ và $\\left(%s; +\\infty\\right)$' % (latex(k_1), latex(k_2))
            vd_da_1_s = 'Hàm số đã cho nghịch biến trên các khoảng $\\left(-\\infty; %s\\right)$ và $\\left(%s; +\\infty\\right)$' % (latex(k_1), latex(k_2))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Tập xác định của hàm số là $\\mathscr{D} = \\mathbb{R} \\setminus \\{%s\\}$.\\\\
            Ta có đạo hàm $y\' = \\frac{%s \\cdot %s - %s \\cdot %s}{(%s)^2} = \\frac{%s}{(%s)^2} > 0, \\forall x \\in \\mathscr{D}$.\\\\
            Do đó, hàm số đồng biến trên các khoảng $\\left(-\\infty; %s\\right)$ và $\\left(%s; +\\infty\\right)$.\\\\
            Vì các khoảng $\\left(-\\infty; %s\\right)$ và $\\left(%s; +\\infty\\right)$ lần lượt là tập con của $\\left(-\\infty; %s\\right)$ và $\\left(%s; +\\infty\\right)$ nên hàm số đã cho cũng đồng biến trên các khoảng đó.''' 
                            % (latex(x_0), latex(a), latex(d), latex(b), latex(c), latex(bt_mau), latex(a*d - b*c), latex(bt_mau), latex(x_0), latex(x_0), latex(k_1), latex(k_2), latex(x_0), latex(x_0)))

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Trên đoạn $\\left[%s; %s\\right]$, hàm số đã cho có giá trị lớn nhất bằng $%s$ và có giá trị nhỏ nhất bằng $%s$' % (latex(alpha), latex(beta), latex(y_max), latex(y_min))
            vdc_da_1_s = 'Trên đoạn $\\left[%s; %s\\right]$, hàm số đã cho có giá trị lớn nhất bằng $%s$ và có giá trị nhỏ nhất bằng $%s$' % (latex(alpha), latex(beta), latex(y_min), latex(y_max))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Vì đoạn $\\left[%s; %s\\right]$ nằm hoàn toàn trong khoảng xác định $\\left(%s; +\\infty\\right)$ và hàm số luôn đồng biến trên khoảng này, nên hàm số liên tục và đồng biến trên đoạn $\\left[%s; %s\\right]$.\\\\
            Do đó:\\\\
            - Giá trị nhỏ nhất của hàm số là $y(%s) = %s$.\\\\
            - Giá trị lớn nhất của hàm số là $y(%s) = %s$.''' 
                             % (latex(alpha), latex(beta), latex(x_0), latex(alpha), latex(beta), latex(alpha), latex(y_min), latex(beta), latex(y_max)))

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
                '\\begin{ex}\n' +
                str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(shuffled_answers_nb[0]) + '}\n'
                '{' + str(shuffled_answers_th[0]) + '}\n'
                '{' + str(shuffled_answers_vd[0]) + '}\n'
                '{' + str(shuffled_answers_vdc[0]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(shuffled_solutions_nb[0]) + '\n'
                '\\item ' + str(shuffled_solutions_th[0]) + '\n'
                '\\item ' + str(shuffled_solutions_vd[0]) + '\n'
                '\\item ' + str(shuffled_solutions_vdc[0]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


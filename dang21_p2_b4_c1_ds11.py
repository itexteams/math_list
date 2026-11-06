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


def bt_dang21_p2_b4_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # B3-Suy nghĩ tìm cách random bài toán
            # Đề bài gốc: f(x) = sqrt(-x^2 + 3x - 2) có nghiệm là 1 và 2. Tập xác định D = [1, 2].
            # Ta random cặp nghiệm (x1, x2) liên tiếp dạng (1, 2), (2, 3), (3, 4)
            x1 = random.choice([1, 2, 3])
            x2 = x1 + 1

            # Tam thức tương ứng: -(x - x1)(x - x2) = -x^2 + (x1+x2)x - x1*x2
            b_val = x1 + x2
            c_val = x1 * x2

            # Hàm số f(x) = sqrt(-x^2 + b_val*x - c_val)
            str_f = "-x^2 + %sx - %s" % (latex(b_val), latex(c_val))

            # Hoành độ kiểm tra ở câu a (gốc bằng 3 ứng với x1=1, x2=2, tức là x2 + 1)
            hoanh_do_a = x2 + 1

            # Tính số nghiệm cho câu d dựa trên tập xác định D = [x1, x2]
            # g(x) = sin(pi*(4x^2 + 2x)) = 0 <=> 4x^2 + 2x = k (k nguyên)
            # Xét hàm h(x) = 4x^2 + 2x trên đoạn [x1, x2]
            # h'(x) = 8x + 2 > 0 với mọi x >= 1, suy ra h(x) đồng biến trên [x1, x2]
            # h(x1) = 4*x1^2 + 2*x1
            # h(x2) = 4*x2^2 + 2*x2
            # Số nghiệm nguyên k chính là số nghiệm của phương trình g(x) = 0
            h_min = 4 * x1**2 + 2 * x1
            h_max = 4 * x2**2 + 2 * x2
            # Tổng số nghiệm thực của phương trình f(x).g(x) = 0 bao gồm x1, x2 và các nghiệm của g(x)=0 trong khoảng (x1, x2)
            # Do h(x) tăng liên tục từ h_min đến h_max, số nghiệm của g(x)=0 trên [x1, x2] là: (h_max - h_min + 1)
            # Do hai đầu mút x1, x2 đã làm f(x) = 0, tổng số nghiệm thực phân biệt của f(x).g(x) = 0 chính là (h_max - h_min + 1)
            so_nghiem_dung = h_max - h_min + 1
            so_nghiem_sai = so_nghiem_dung - 2

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hai hàm số $f(x) = \\sqrt{%s}$, $g(x) = \\sin \\pi (4x^2 + 2x)$. ''' % (str_f))

            ########################################################################
            # Nhận biết ############################################
            nb_da_1_d = '\\True Hàm số $f(x)$ không đi qua điểm nào có hoành độ bằng %s' % (latex(hoanh_do_a))
            nb_da_1_s = 'Hàm số $f(x)$ đi qua điểm có hoành độ bằng %s' % (latex(hoanh_do_a))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = ('''Điều kiện xác định của hàm số $f(x)$ là: $-x^2 + %sx - %s \\ge 0 \\Leftrightarrow %s \\le x \\le %s$.\\\\
            Do đó tập xác định của hàm số $f(x)$ là $\\mathscr{D}_1 = [%s; %s]$.\\\\
            Vì hoành độ $x = %s$ không thuộc tập xác định $\\mathscr{D}_1$, nên đồ thị hàm số $f(x)$ không đi qua điểm nào có hoành độ bằng %s.''' 
                            % (latex(b_val), latex(c_val), latex(x1), latex(x2), latex(x1), latex(x2), latex(hoanh_do_a), latex(hoanh_do_a)))

            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            th_da_1_d = '\\True Hàm số $g(x)$ có tập xác định $\\mathbb{R}$'
            th_da_1_s = 'Hàm số $g(x)$ có tập xác định $[0; +\\infty)$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            loigiai_th_1 = ('''Hàm số $g(x) = \\sin \\pi (4x^2 + 2x)$ là hàm số lượng giác dạng $\\sin(u(x))$.\\\\
            Biểu thức $u(x) = \\pi (4x^2 + 2x)$ là một đa thức bậc hai luôn xác định với mọi số thực $x \\in \\mathbb{R}$.\\\\
            Do đó, hàm số $g(x)$ có tập xác định là $\\mathbb{R}$.''')

            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng ############################################
            vd_da_1_d = '\\True Hàm số $g(x)$ có đồ thị nằm phía trên đường thẳng $y = -\\sqrt{2}$'
            vd_da_1_s = 'Hàm số $g(x)$ có đồ thị nằm phía dưới đường thẳng $y = -\\sqrt{2}$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = ('''Với mọi số thực $x$, ta luôn có giá trị của hàm số lượng giác nằm trong đoạn: $-1 \\le \\sin \\pi (4x^2 + 2x) \\le 1$.\\\\
            Mặt khác, ta có $-\\sqrt{2} \\approx -1,414 < -1$.\\\\
            Do đó, $g(x) \\ge -1 > -\\sqrt{2}$ với mọi $x \\in \\mathbb{R}$.\\\\
            Suy ra đồ thị hàm số $g(x)$ luôn nằm hoàn toàn phía trên đường thẳng $y = -\\sqrt{2}$.''')

            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao ############################################
            vdc_da_1_d = '\\True Phương trình $f(x) \\cdot g(x) = 0$ có %s nghiệm thực' % (latex(so_nghiem_dung))
            vdc_da_1_s = 'Phương trình $f(x) \\cdot g(x) = 0$ có %s nghiệm thực' % (latex(so_nghiem_sai))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = ('''Điều kiện để phương trình có nghĩa là $x \\in [%s; %s]$.\\\\
            Khi đó, phương trình $f(x) \\cdot g(x) = 0 \\Leftrightarrow \\left[\\begin{aligned} & f(x) = 0 \\\\ & g(x) = 0 \\end{aligned}\\right.$\\\\
            - Trường hợp 1: $f(x) = 0 \\Leftrightarrow -x^2 + %sx - %s = 0 \\Leftrightarrow x = %s$ hoặc $x = %s$.\\\\
            - Trường hợp 2: $g(x) = 0 \\Leftrightarrow \\sin \\pi (4x^2 + 2x) = 0 \\Leftrightarrow 4x^2 + 2x = k$ với $k \\in \\mathbb{Z}$.\\\\
            Xét hàm số $h(x) = 4x^2 + 2x$ trên đoạn $[%s; %s]$. Ta có $h'(x) = 8x + 2 > 0$ với mọi $x \\in [%s; %s]$, do đó hàm số đồng biến liên tục trên đoạn này.\\\\
            Giá trị nhỏ nhất là $h(%s) = %s$, giá trị lớn nhất là $h(%s) = %s$.\\\\
            Vì $h(x)$ tăng liên tục từ %s đến %s nên với mỗi giá trị nguyên $k$ thuộc đoạn $[%s; %s]$, phương trình $4x^2 + 2x = k$ có đúng $1$ nghiệm thực.\\\\
            Số lượng giá trị nguyên $k$ thỏa mãn là: %s - %s + 1 = %s giá trị.\\\\
            Do hai đầu mút ứng với $k = %s$ (tức $x = %s$) và $k = %s$ (tức $x = %s$) đã được tính, phương trình tích ban đầu có tất cả đúng %s nghiệm thực phân biệt.''' 
                             % (latex(x1), latex(x2), latex(b_val), latex(c_val), latex(x1), latex(x2), latex(x1), latex(x2), latex(x1), latex(x2), latex(x1), latex(h_min), latex(x2), latex(h_max), latex(h_min), latex(h_max), latex(h_min), latex(h_max), latex(h_max), latex(h_min), latex(so_nghiem_dung), latex(h_min), latex(x1), latex(h_max), latex(x2), latex(so_nghiem_dung)))

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


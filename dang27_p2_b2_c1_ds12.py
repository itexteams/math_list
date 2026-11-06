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


def bt_dang27_p2_b2_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Thiết lập ngẫu nhiên các thông số bài toán nuôi cá
            S = randint(35, 50)                      # Diện tích ao (m2)
            d0 = randint(12, 18)                     # Mật độ thả cá (con/m2)
            N0 = S * d0                              # Tổng số cá thả ban đầu (con)

            # Chọn khối lượng trung bình ban đầu m0 (ví dụ: 1.0, 1.1, 1.2, 1.3, 1.4, 1.5)
            m0 = random.choice([1.0, 1.1, 1.2, 1.3, 1.4, 1.5])
            M0_val = N0 * m0                         # Tổng sản lượng ban đầu (kg)

            k = randint(4, 8)                        # Số cá giảm đi mỗi lần
            w = random.choice([0.2, 0.3, 0.4, 0.5])  # Khối lượng tăng thêm của mỗi con (kg)

            # Chuyển đổi định dạng dấu phẩy cho hiển thị Tiếng Việt
            str_m0 = f"{m0:.1f}".replace('.', ',')
            str_M0_val = f"{M0_val:.1f}".replace('.', ',')
            str_w = f"{w:.1f}".replace('.', ',')

            # Các hệ số của hàm tổng khối lượng cá: M(x) = (N0 - k*x) * (m0 + w*x)
            # M(x) = - (k * w) * x^2 + (N0 * w - k * m0) * x + N0 * m0
            coef_a = - k * w
            coef_b = N0 * w - k * m0
            coef_c = M0_val

            str_coef_a = f"{coef_a:.1f}".replace('.', ',')
            str_coef_b = f"{coef_b:.1f}".replace('.', ',')
            str_coef_c = f"{coef_c:.1f}".replace('.', ',')

            # Đỉnh parabol x_opt = -b / (2a)
            x_opt = - coef_b / (2 * coef_a)
            str_x_opt_den = f"{2 * coef_a:.1f}".replace('.', ',')
            str_x_opt_num = f"{-coef_b:.1f}".replace('.', ',')
            str_x_opt = f"{x_opt:.1f}".replace('.', ',')

            # Vì x nguyên nên ta làm tròn x_opt để tìm giá trị thực tế tốt nhất
            x_best = round(x_opt)
            N_best = N0 - k * x_best

            # Giá trị sai lệch cho các phương án nhiễu
            N0_wrong = N0 + random.choice([-15, 15, 20])
            N_best_wrong = N_best + random.choice([-10, 10, 15])

            # Nội dung câu hỏi
            noidungcauhoi = ('''Bác Vinh có một cái ao có diện tích %s $m^2$ để nuôi cá. Vụ vừa qua bác nuôi với mật độ %s con/$m^2$ và thu được tất cả %s kg cá thành phẩm. Theo kinh nghiệm nuôi cá thu được, bác thấy cứ thả giảm đi %s con thì tương ứng sẽ có mỗi con cá thành phẩm thu được tăng thêm %s kg. Gọi $x$ là số lần giảm đi %s con.'''              
                             %(S, d0, str_M0_val, k, str_w, k))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = 'Số cá của vụ vừa qua mà bác Vinh thả là %s' % (N0_wrong)
            nb_da_1_s = '\\True Số cá của vụ vừa qua mà bác Vinh thả là %s' % (N0)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Số cá của vụ vừa qua mà bác Vinh thả là $%s \\cdot %s = %s$ con.'''
                        % (d0, S, N0))

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Sau $x$ lần giảm đi %s con thì số cá thả mới là $%s - %sx$' % (k, N0, k)  
            th_da_1_s = 'Sau $x$ lần giảm đi %s con thì số cá thả mới là $%s - %sx$' % (k, N0_wrong, k)   
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Với $x$ là số lần giảm đi %s con thì số cá thả mới là $%s - %sx$.'''       
                       % (k, N0, k))

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Sau $x$ lần giảm đi %s con và thả cá xuống ao thì đến khi thu hoạch khối lượng mỗi con cá là $(%s + %sx)$ kg' % (k, str_m0, str_w)  
            vd_da_1_s = 'Sau $x$ lần giảm đi %s con và thả cá xuống ao thì đến khi thu hoạch khối lượng mỗi con cá là $(%s + %sx)$ kg' % (k, str_m0, str_w)
            # (Chúng ta tạo ra một phương án sai bằng cách thay đổi hệ số khối lượng ban đầu)
            vd_da_1_s = 'Sau $x$ lần giảm đi %s con và thả cá xuống ao thì đến khi thu hoạch khối lượng mỗi con cá là $(%s + %sx)$ kg' % (k, f"{m0 + 0.5:.1f}".replace('.', ','), str_w)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Khối lượng trung bình của mỗi con cá vụ vừa qua là: \\\\
                           $\\frac{%s}{%s} = %s$ kg. \\\\
                           Sau $x$ lần giảm đi %s con và thả cá xuống ao thì đến khi thu hoạch khối lượng mỗi con cá là: \\\\
                           $(%s + %sx)$ kg.'''  
                       % (str_M0_val, N0, str_m0, k, str_m0, str_w))

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Để vụ tới bác Vinh thu được sản lượng cá lớn nhất thì số lượng cá bác cần thả là %s' % (N_best) 
            vdc_da_1_s = 'Để vụ tới bác Vinh thu được sản lượng cá lớn nhất thì số lượng cá bác cần thả là %s' % (N_best_wrong) 
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Số cá ban đầu: $%s \\cdot %s = %s$ con. \\\\
            Khối lượng trung bình mỗi con: $\\frac{%s}{%s} = %s$ kg. \\\\
            Gọi $x$ là số lần giảm cá, suy ra số cá giảm là: %sx con. \\\\
            Số cá thả mới: $N(x) = %s - %sx$. \\\\
            Mỗi con cá tăng thêm được: $m(x) = (%s + %sx)$ kg. \\\\
            Tổng khối lượng cá thu được: \\\\
            $M(x) = N(x) \\cdot m(x) = (%s - %sx) \\cdot (%s + %sx) = %sx^2 + %sx + %s$. \\\\
            Khối lượng cá đạt lớn nhất khi: $x = \\frac{%s}{%s} = %s$. \\\\
            Vì số cá nguyên nên $x = %s$. \\\\
            Số lượng cá cần thả: $N = %s - %s \\cdot %s = %s$ con.'''
                       % (d0, S, N0, str_M0_val, N0, str_m0, k, N0, k, str_m0, str_w, N0, k, str_m0, str_w, str_coef_a, str_coef_b, str_coef_c, str_x_opt_num, str_x_opt_den, str_x_opt, x_best, N0, k, x_best, N_best))

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
            str(noidungcauhoi) + 
                '\n\\choiceTFn \n'
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
                '\\end{ex}\n\\end{minipage}\n\n')
            return content


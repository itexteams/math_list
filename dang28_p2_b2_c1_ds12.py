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


def bt_dang28_p2_b2_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Tìm bộ số ngẫu nhiên sao cho x_opt là số nguyên dương đẹp
            while True:
                P0 = randint(120, 150)           # Giá bán ban đầu (nghìn đồng)
                L0 = randint(50, 70)             # Lãi ban đầu trên 1 áo (nghìn đồng)
                C_prod = P0 - L0                 # Chi phí sản xuất (nghìn đồng)

                dp = randint(2, 5)               # Mỗi lần tăng thêm dp nghìn đồng
                k_factor = randint(8, 15)        # Tỷ lệ giảm k = dq / dp
                dq = k_factor * dp               # Số lượng giảm tương ứng

                # Q0 phải lớn hơn k_factor * L0 để đạo hàm có nghiệm dương
                # Và (Q0 - k_factor * L0) phải chia hết cho (2 * k_factor) để x_opt nguyên
                Q0_min = k_factor * L0 + 10
                Q0_max = Q0_min + 500

                # Lọc ra các giá trị Q0 thỏa mãn chia hết cho 10 và tạo ra x_opt nguyên
                valid_Q0 = [q for q in range(Q0_min, Q0_max) if q % 10 == 0 and (q - k_factor * L0) % (2 * k_factor) == 0]

                if len(valid_Q0) > 0:
                    Q0 = random.choice(valid_Q0)
                    x_opt = (Q0 - k_factor * L0) // (2 * k_factor)
                    if 2 <= x_opt <= 15: # Đảm bảo x_opt nằm trong khoảng thực tế đẹp
                        break

            # Các giá trị dùng trong đề bài và đáp án (tính bằng đồng)
            P0_full = P0 * 1000
            C_full = C_prod * 1000
            L0_full = L0 * 1000
            dp_full = dp * 1000

            # Tạo hệ số nhiễu cho các đáp án sai
            L0_wrong = L0_full - randint(2, 5) * 1000
            k_wrong = k_factor + random.choice([-3, -2, 2, 3])
            x_opt_wrong = x_opt + random.choice([-2, -1, 1, 2])

            # Đổi định dạng hiển thị tiền sang chuỗi số nguyên dễ nhìn
            str_P0 = str(P0_full)
            str_C = str(C_full)
            str_L0 = str(L0_full)
            str_L0_wrong = str(L0_wrong)
            str_dp = str(dp_full)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một xưởng sản xuất bán áo thun với giá %s một chiếc, mỗi tháng bán trung bình %s chiếc. Khảo sát cho thấy nếu giá bán tăng thêm %s đồng thì số lượng tiêu thụ giảm %s chiếc. Biết chi phí sản xuất một chiếc áo là %s đồng. Gọi số tiền cần tăng giá mỗi chiếc áo là $x$ (nghìn đồng).'''              
                             %(str_P0, Q0, str_dp, dq, str_C))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Nếu bán với giá %s thì tiền lãi mỗi chiếc áo là %s (đồng)' % (str_P0, str_L0)
            nb_da_1_s = 'Nếu bán với giá %s thì tiền lãi mỗi chiếc áo là %s (đồng)' % (str_P0, str_L0_wrong)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Nếu bán với giá %s thì tiền lãi mỗi chiếc áo là: %s - %s = %s (đồng).'''
                        % (str_P0, str_P0, str_C, str_L0))

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
            th_da_1_d = '\\True Nếu tăng giá mỗi chiếc áo là $x$ (nghìn đồng) thì số lượng tiêu thụ giảm đi %sx chiếc áo' % (k_factor)  
            th_da_1_s = 'Nếu tăng giá mỗi chiếc áo là $x$ (nghìn đồng) thì số lượng tiêu thụ giảm đi %sx chiếc áo' % (k_wrong)   
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Vì cứ tăng giá thêm %s (nghìn đồng) thì cửa hàng bán ra giảm %s chiếc áo nên tăng $x$ (nghìn đồng) thì cửa hàng bị giảm đi bằng $\\frac{%sx}{%s} = %sx$ chiếc áo.'''       
                       % (dp, dq, dq, dp, k_factor))

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
            vd_da_1_d = '\\True Nếu tăng giá mỗi chiếc áo là $x$ (nghìn đồng) thì số lượng bán ra mỗi tháng là %s - %sx chiếc áo' % (Q0, k_factor)  
            vd_da_1_s = 'Nếu tăng giá mỗi chiếc áo là $x$ (nghìn đồng) thì số lượng bán ra mỗi tháng là %s - %sx chiếc áo' % (Q0, k_wrong)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Tăng $x$ (nghìn đồng) thì cửa hàng bị giảm đi %sx chiếc áo. \\\\
            Do đó tổng số chiếc áo bán ra mỗi tháng là: %s - %sx chiếc áo.'''  
                       % (k_factor, Q0, k_factor))

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
            vdc_da_1_d = '\\True Để lợi nhuận thu về cao nhất cần tăng thêm %s000 (đồng) mỗi chiếc áo' % (x_opt) 
            vdc_da_1_s = 'Để lợi nhuận thu về cao nhất cần tăng thêm %s000 (đồng) mỗi chiếc áo' % (x_opt_wrong) 
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            # Phục vụ cho tính toán biểu thức lợi nhuận f(x) = ax^2 + bx + c
            a_coef = -k_factor
            b_coef = Q0 - k_factor * L0
            c_coef = Q0 * L0
            loigiai_vdc_1 = ('''Gọi số tiền cần tăng giá mỗi chiếc áo là $x$ (nghìn đồng). \\\\
            Vì cứ tăng giá thêm %s (nghìn đồng) thì số lượng tiêu thụ %s chiếc nên tăng $x$ (nghìn đồng) thì số lượng tiêu thụ giảm đi là %sx. \\\\
            Do đó tổng số áo bán ra là: %s - %sx. \\\\
            Lúc đầu bán với giá %s (nghìn đồng), mỗi chiếc có lãi %s (nghìn đồng). \\\\
            Sau khi tăng giá, mỗi chiếc thu được số lãi là: %s + $x$ (nghìn đồng). \\\\
            Do đó tổng số lợi nhuận thu được sau khi tăng giá là: \\\\
            $f(x) = (%s - %sx)(%s + x) = %sx^2 + %sx + %s$. \\\\
            $f\'(x) = %s - %sx$. \\\\
            $f\'(x) = 0 \\Leftrightarrow %s - %sx = 0 \\Leftrightarrow x = %s$. \\\\
            Lập bảng biến thiên ta thấy $f(x)$ đạt giá trị lớn nhất khi $x = %s$. \\\\
            Vậy cần tăng thêm %s000 đồng cho mỗi chiếc áo để được lợi nhuận cao nhất.'''
                       % (dp, dq, k_factor, Q0, k_factor, P0, L0, L0, Q0, k_factor, L0, a_coef, b_coef, c_coef, b_coef, 2*k_factor, b_coef, 2*k_factor, x_opt, x_opt, x_opt))

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


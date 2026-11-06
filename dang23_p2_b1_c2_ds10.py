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


def bt_dang23_p2_b1_c2_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x, y = symbols('x y')

            # Sinh ngẫu nhiên các thông số của bài toán
            p1 = randint(6, 10) * 100   # Phí cố định từ thứ 2 đến thứ 6 (nghìn đồng/ngày)
            k1 = randint(5, 8)          # Phí quãng đường từ thứ 2 đến thứ 6 (nghìn đồng/km)
            p2 = randint(10, 15) * 100  # Phí cố định thứ 7 và Chủ nhật (nghìn đồng/ngày)
            k2 = randint(8, 12)         # Phí quãng đường thứ 7 và Chủ nhật (nghìn đồng/km)
            M = randint(10, 15)         # Tổng phí không quá M triệu đồng

            fixed_weekdays = 5 * p1
            fixed_weekend = 2 * p2
            fixed_total = fixed_weekdays + fixed_weekend

            target_ineq_const = M * 1000 - fixed_total

            km1_day = randint(15, 25)   # km mỗi ngày từ thứ 2 đến thứ 6
            km2_day = randint(25, 35)   # km mỗi ngày thứ 7 và Chủ nhật

            x_val = 5 * km1_day
            y_val = 2 * km2_day

            total_cost_nghin = fixed_total + k1 * x_val + k2 * y_val
            total_cost_trieu = total_cost_nghin / 1000.0

            # Định dạng số thập phân bằng dấu phẩy
            cost_str_correct = ("%.3f" % total_cost_trieu).rstrip('0').rstrip('.').replace('.', ',')
            cost_wrong_val = round(total_cost_trieu - 0.04, 1)
            cost_str_wrong = ("%.1f" % cost_wrong_val).replace('.', ',')

            # Nội dung câu hỏi
            noidungcauhoi = ('''Ông Hùng muốn thuê một chiếc xe ô tô trong một tuần. Giá thuê xe (đơn vị: nghìn đồng) được cho như trong bảng dưới đây: \\\\
            \\begin{center}
            \\begin{tabular}{|c|c|c|}
            \\hline
             & \\textbf{Phí cố định} & \\begin{tabular}[c]{@{}c@{}}\\textbf{Phí tính theo quãng}\\\\ \\textbf{đường di chuyển}\\end{tabular} \\\\
            \\hline
            \\begin{tabular}[c]{@{}c@{}}\\textbf{Từ thứ Hai đến thứ Sáu}\\end{tabular} & $%s$ & $%s$ \\\\
            \\hline
            \\begin{tabular}[c]{@{}c@{}}\\textbf{Thứ Bảy và Chủ nhật}\\end{tabular} & $%s$ & $%s$ \\\\
            \\hline
            \\end{tabular}
            \\end{center}
            Gọi $x$ ($x \\in \\mathbb{N}^*$) là tổng số kilômét ông Hùng đã đi trong các ngày từ thứ Hai đến thứ Sáu và $y$ ($y \\in \\mathbb{N}^*$) là tổng số kilômét ông Hùng đi trong hai ngày thứ Bảy và Chủ nhật.'''
                %(latex(p1), latex(k1), latex(p2), latex(k2))
            )

            ########################################################################
            # Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Số tiền ông Hùng phải trả khi đi $x$ km trong các ngày từ thứ Hai đến thứ Sáu là $%s + %s x$' %(latex(fixed_weekdays), latex(k1))
            nb_da_1_s = 'Số tiền ông Hùng phải trả khi đi $x$ km trong các ngày từ thứ Hai đến thứ Sáu là $%s + %s x$' %(latex(p1), latex(k1))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Từ thứ Hai đến thứ Sáu có $5$ ngày nên phí cố định là $5 \\cdot %s = %s$ (nghìn đồng). \\\\
            Số tiền trả theo quãng đường đi là $%s x$ (nghìn đồng). \\\\
            Do đó số tiền ông Hùng phải trả khi đi $x$ km trong các ngày từ thứ Hai đến thứ Sáu là $%s + %s x$ (nghìn đồng).'''
                %(latex(p1), latex(fixed_weekdays), latex(k1), latex(fixed_weekdays), latex(k1))
            )

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
            th_da_1_d = '\\True Số tiền ông Hùng phải trả khi đi $y$ km trong $2$ ngày cuối tuần là $%s \\cdot 2 + %s y$' %(latex(p2), latex(k2))
            th_da_1_s = 'Số tiền ông Hùng phải trả khi đi $y$ km trong $2$ ngày cuối tuần là $%s + %s y$' %(latex(p2), latex(k2))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Thứ Bảy và Chủ nhật có $2$ ngày nên phí cố định là $%s \\cdot 2 = %s$ (nghìn đồng). \\\\
            Số tiền trả theo quãng đường đi là $%s y$ (nghìn đồng). \\\\
            Do đó số tiền ông Hùng phải trả khi đi $y$ km trong $2$ ngày cuối tuần là $%s \\cdot 2 + %s y = %s + %s y$ (nghìn đồng).'''
                %(latex(p2), latex(fixed_weekend), latex(k2), latex(p2), latex(k2), latex(fixed_weekend), latex(k2))
            )

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
            vd_da_1_d = '\\True Để số tiền ông Hùng phải trả không quá $%s$ triệu đồng thì bất phương trình biểu thị mối liên hệ giữa $x, y$ là: $%s x + %s y \\le %s$' %(latex(M), latex(k1), latex(k2), latex(target_ineq_const))
            vd_da_1_s = 'Để số tiền ông Hùng phải trả không quá $%s$ triệu đồng thì bất phương trình biểu thị mối liên hệ giữa $x, y$ là: $%s x + %s y \\le %s$' %(latex(M), latex(k1), latex(k2), latex(target_ineq_const + fixed_weekdays))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Tổng số tiền ông Hùng phải trả trong một tuần là: \\\\
            $(%s + %s x) + (%s + %s y) = %s x + %s y + %s$ (nghìn đồng). \\\\
            Đổi $%s$ triệu đồng = $%s$ nghìn đồng. \\\\
            Để số tiền không quá $%s$ triệu đồng thì: \\\\
            $%s x + %s y + %s \\le %s \\Leftrightarrow %s x + %s y \\le %s$.'''
                %(latex(fixed_weekdays), latex(k1), latex(fixed_weekend), latex(k2), latex(k1), latex(k2), latex(fixed_total), latex(M), latex(M * 1000), latex(M), latex(k1), latex(k2), latex(fixed_total), latex(M * 1000), latex(k1), latex(k2), latex(target_ineq_const))
            )

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
            vdc_da_1_d = '\\True Từ thứ Hai đến thứ Sáu, mỗi ngày ông Hùng sử dụng xe $%s$ km, thứ Bảy và Chủ nhật mỗi ngày ông Hùng sử dụng xe $%s$ km thì số tiền ông phải trả cho tuần đó là $%s$ triệu đồng' %(latex(km1_day), latex(km2_day), cost_str_correct)
            vdc_da_1_s = 'Từ thứ Hai đến thứ Sáu, mỗi ngày ông Hùng sử dụng xe $%s$ km, thứ Bảy và Chủ nhật mỗi ngày ông Hùng sử dụng xe $%s$ km thì số tiền ông phải trả cho tuần đó là $%s$ triệu đồng' %(latex(km1_day), latex(km2_day), cost_str_wrong)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Số km đi từ thứ Hai đến thứ Sáu là: $x = 5 \\cdot %s = %s$ (km). \\\\
            Số km đi hai ngày cuối tuần là: $y = 2 \\cdot %s = %s$ (km). \\\\
            Số tiền ông Hùng phải trả cho tuần đó là: \\\\
            $%s \\cdot %s + %s \\cdot %s + %s = %s + %s + %s = %s$ (nghìn đồng) = $%s$ triệu đồng.'''
                %(latex(km1_day), latex(x_val), latex(km2_day), latex(y_val), latex(k1), latex(x_val), latex(k2), latex(y_val), latex(fixed_total), latex(k1 * x_val), latex(k2 * y_val), latex(fixed_total), latex(total_cost_nghin), cost_str_correct)
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
                '\\end{ex}\n \\end{minipage}\n\n')
            return content


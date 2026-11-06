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


def bt_dang35_p2_b2_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến và ngẫu nhiên hóa số liệu bài toán
            D = random.choice([12, 15, 18, 21, 24])    # Hiệu số giữa giá bán ban đầu và chi phí biến đổi (p0 - c1)
            c1 = random.choice([20, 25, 30, 35])        # Chi phí biến đổi cho mỗi tấn sản phẩm
            c0 = random.choice([50, 100, 150, 200])     # Chi phí cố định hàng tháng
            p0 = c1 + D                                 # Giá bán cơ bản ban đầu cho mỗi tấn sản phẩm

            # Tính toán các giá trị cho câu hỏi và đáp án
            cost_10_true = c0 + c1 * 10
            cost_10_false = cost_10_true + random.choice([-50, 50, 100])

            rev_10_true = 10 * p0 - 1
            rev_10_false = 10 * p0 + 50

            x_max_val = round(math.sqrt(D / 0.003), 1)
            x_max_str = str(x_max_val).replace('.', ',')
            x_max_wrong_val = round(x_max_val + random.choice([-12, 8, 12]), 1)
            x_max_wrong_str = str(x_max_wrong_val).replace('.', ',')

            # Nội dung câu hỏi
            noidungcauhoi = ('''Nhà máy $A$ chuyên sản xuất một loại sản phẩm cung cấp cho nhà máy $B$. Hai nhà máy thoả thuận rằng, hằng tháng $A$ cung cấp cho $B$ số lượng sản phẩm theo đơn đặt hàng của $B$ (tối đa $100$ tấn sản phẩm). Nếu số lượng đặt hàng là $x$ tấn sản phẩm thì giá bán cho mỗi tấn sản phẩm là $P(x) = %s - 0,001x^2$ (triệu đồng). Chi phí để $A$ sản xuất $x$ tấn sản phẩm trong một tháng là $C(x) = %s + %sx$ (triệu đồng) (gồm %s triệu đồng chi phí cố định và %s triệu đồng cho mỗi tấn sản phẩm).''') % (latex(p0), latex(c0), latex(c1), latex(c0), latex(c1))

            ########################################################################
            # Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Chi phí để $A$ sản xuất 10 tấn sản phẩm trong một tháng là %s triệu đồng' % (latex(cost_10_true))
            nb_da_1_s = 'Chi phí để $A$ sản xuất 10 tấn sản phẩm trong một tháng là %s triệu đồng' % (latex(cost_10_false))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Chi phí để nhà máy $A$ sản xuất $10$ tấn sản phẩm trong một tháng được tính bằng cách thay $x = 10$ vào công thức $C(x)$: \\\\ $C(10) = %s + %s \\cdot 10 = %s$ (triệu đồng).''') % (latex(c0), latex(c1), latex(cost_10_true))

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
            th_da_1_d = '\\True Số tiền $A$ thu được khi bán 10 tấn sản phẩm cho $B$ là %s triệu đồng' % (latex(rev_10_true))
            th_da_1_s = 'Số tiền $A$ thu được khi bán 10 tấn sản phẩm cho $B$ là %s triệu đồng' % (latex(rev_10_false))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Giá bán của mỗi tấn sản phẩm khi số lượng đặt hàng là $10$ tấn là: \\\\ $P(10) = %s - 0,001 \\cdot 10^2 = %s - 0,1 = %s$ (triệu đồng/tấn). \\\\ Số tiền nhà máy $A$ thu được khi bán $10$ tấn sản phẩm (doanh thu) là: \\\\ $R(10) = 10 \\cdot P(10) = 10 \\cdot %s = %s$ (triệu đồng).''') % (latex(p0), latex(p0), str(p0 - 0.1).replace('.', ','), str(p0 - 0.1).replace('.', ','), latex(rev_10_true))

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
            vd_da_1_d = '\\True Lợi nhuận mà $A$ thu được khi bán $x$ tấn sản phẩm ($0 \\le x \\le 100$) cho $B$ được biểu diễn bằng công thức $-0,001x^3 + %sx - %s$' % (latex(D), latex(c0))
            vd_da_1_s = 'Lợi nhuận mà $A$ thu được khi bán $x$ tấn sản phẩm ($0 \\le x \\le 100$) cho $B$ được biểu diễn bằng công thức $-0,01x^3 + %sx - %s$' % (latex(D), latex(c0))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Doanh thu khi bán $x$ tấn sản phẩm là: \\\\ $R(x) = x \\cdot P(x) = x \\cdot \\left(%s - 0,001x^2\\right) = %sx - 0,001x^3$ (triệu đồng). \\\\ Lợi nhuận mà nhà máy $A$ thu được là: \\\\ $L(x) = R(x) - C(x) = \\left(%sx - 0,001x^3\\right) - \\left(%s + %sx\\right) = -0,001x^3 + %sx - %s$ (triệu đồng).''') % (latex(p0), latex(p0), latex(p0), latex(c0), latex(c1), latex(D), latex(c0))

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
            vdc_da_1_d = '\\True $A$ bán cho $B$ khoảng %s tấn sản phẩm mỗi tháng thì thu được lợi nhuận lớn nhất' % (x_max_str)
            vdc_da_1_s = '$A$ bán cho $B$ khoảng %s tấn sản phẩm mỗi tháng thì thu được lợi nhuận lớn nhất' % (x_max_wrong_str)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Xét hàm số lợi nhuận $L(x) = -0,001x^3 + %sx - %s$ trên đoạn $\\left[0; 100\\right]$. \\\\ Ta có đạo hàm: $L\'(x) = -0,003x^2 + %s$. \\\\ Cho $L\'(x) = 0 \\Leftrightarrow -0,003x^2 + %s = 0 \\Leftrightarrow x^2 = %s \\Leftrightarrow x = \\sqrt{%s} \\approx %s$ (do $0 \\le x \\le 100$). \\\\ Lập bảng biến thiên hoặc tính các giá trị tại biên, ta thấy hàm số đạt giá trị lớn nhất tại $x \\approx %s$. \\\\ Vậy nhà máy $A$ bán cho $B$ khoảng %s tấn sản phẩm mỗi tháng thì thu được lợi nhuận lớn nhất.''') % (latex(D), latex(c0), latex(D), latex(D), latex(int(D / 0.003)), latex(int(D / 0.003)), x_max_str, x_max_str, x_max_str)

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
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


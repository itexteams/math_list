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


def bt_dang8_p2_b1_c1_ds11(self):
            # Khai báo biến
            # Định nghĩa các bộ ba số Pythagore đẹp (đối, kề, huyền) để tính lượng giác hữu tỉ
            pythagorean_triples = [(3, 4, 5), (4, 3, 5), (5, 12, 13), (12, 5, 13)]
            triple = random.choice(pythagorean_triples)

            # Chọn ngẫu nhiên góc phần tư để bài toán đa dạng hơn
            # Cấu hình 1: Góc phần tư thứ III: pi < x < 3pi/2 -> sin < 0, cos < 0, tan > 0, cot > 0
            # Cấu hình 2: Góc phần tư thứ II: pi/2 < x < pi -> sin > 0, cos < 0, tan < 0, cot < 0
            goc_phan_tu = random.choice([1, 2])

            if goc_phan_tu == 1:
                txt_range = '\\pi < x < \\frac{3\\pi}{2}'
                sign_sin = -1
                sign_cos = -1
                txt_cos_sign = '\\cos x < 0'
            else:
                txt_range = '\\frac{\\pi}{2} < x < \\pi'
                sign_sin = 1
                sign_cos = -1
                txt_cos_sign = '\\cos x < 0'

            # Tính giá trị chính xác của các hàm lượng giác bằng Rational SymPy
            val_sin = Rational(sign_sin * triple[0], triple[2])
            val_cos = Rational(sign_cos * triple[1], triple[2])
            val_tan = Rational(val_sin, val_cos)
            val_cot = Rational(val_cos, val_sin)

            # Nội dung câu hỏi tổng quát sử dụng định dạng %s
            noidungcauhoi = ('''Tính được các giá trị lượng giác còn lại của góc $x$, biết: $\\sin x = %s$ với $%s$. Khi đó:''' 
                             % (latex(val_sin), txt_range))

            ########################################################################
            # Nhận biết (Mệnh đề a: Xét dấu của cos x)
            if val_cos > 0:
                nb_da_1_d = '\\True $\\cos x > 0$'
                nb_da_1_s = '$\\cos x < 0$'
            else:
                nb_da_1_d = '\\True $\\cos x < 0$'
                nb_da_1_s = '$\\cos x > 0$'

            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải ý a)
            loigiai_nb_1 = ('''Do $%s$ nên $%s$.''' % (txt_range, txt_cos_sign))

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu (Mệnh đề b: Tính giá trị cos x)
            th_da_1_d = '\\True $\\cos x = %s$' % (latex(val_cos))
            th_da_1_s = '$\\cos x = %s$' % (latex(-val_cos))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải ý b)
            loigiai_th_1 = ('''Ta có: $\\sin^2 x + \\cos^2 x = 1 \\Rightarrow \\cos^2 x = 1 - \\sin^2 x = 1 - \\frac{%s}{%s} = \\frac{%s}{%s} \\Rightarrow \\cos x = %s$.''' 
                            % (latex(triple[0]**2), latex(triple[2]**2), latex(triple[1]**2), latex(triple[2]**2), latex(val_cos)))

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng (Mệnh đề c: Tính giá trị tan x)
            vd_da_1_d = '\\True $\\tan x = %s$' % (latex(val_tan))
            vd_da_1_s = '$\\tan x = %s$' % (latex(-val_tan))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải ý c)
            loigiai_vd_1 = ('''$\\tan x = \\frac{\\sin x}{\\cos x} = \\frac{%s}{%s} = %s$.''' 
                            % (latex(val_sin), latex(val_cos), latex(val_tan)))

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao (Mệnh đề d: Tính giá trị cot x)
            vdc_da_1_d = '\\True $\\cot x = %s$' % (latex(val_cot))
            vdc_da_1_s = '$\\cot x = %s$' % (latex(-val_cot))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải ý d)
            loigiai_vdc_1 = ('''$\\cot x = \\frac{\\cos x}{\\sin x} = \\frac{%s}{%s} = %s$.''' 
                             % (latex(val_cos), latex(val_sin), latex(val_cot)))

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


            # Vòng lặp đảm bảo số lượng phương án Đúng nằm trong khoảng [1, 3]
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán lại giá trị được chọn vào các danh sách xuất bản để đồng bộ hóa
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

            # Khởi tạo khối lời giải chi tiết phân bổ rõ ràng theo cấu trúc enumEX [a)]{1}
            loigiai = ('''\\begin{enumEX}[a)]{1} \n'''
                       '''\\item %s\n'''
                       '''\\item %s\n'''
                       '''\\item %s\n'''
                       '''\\item %s\n'''
                       '''\\end{enumEX}'''
                       % (shuffled_solutions_nb[0], shuffled_solutions_th[0], shuffled_solutions_vd[0], shuffled_solutions_vdc[0]))

            # Kết xuất cấu trúc chuỗi mẫu bằng định dạng %s thống nhất với khung chương trình
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' +
                str(noidungcauhoi) + 
                '\n\\choiceTFn \n'
                '{' + str(shuffled_answers_nb[0]) + '}\n'
                '{' + str(shuffled_answers_th[0]) + '}\n'
                '{' + str(shuffled_answers_vd[0]) + '}\n'
                '{' + str(shuffled_answers_vdc[0]) + '}\n'
                '\\loigiai{ \n'+
                loigiai+
                '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


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


def bt_dang10_p2_b1_c1_ds11(self):
            # Khai báo biến
            # Random số nguyên cho bài toán để tạo ra nhiều câu hỏi khác nhau
            val_tan = randint(-4, 4)
            while val_tan == 0 or val_tan == 1 or val_tan == -1:  # Tránh các giá trị đặc biệt gây suy biến mẫu số
                val_tan = randint(-4, 4)

            val_cot = Rational(1, val_tan)

            # Các hệ số trong biểu thức A1 và A2 được ngẫu nhiên hóa
            c1, c2 = randint(2, 6), randint(2, 6)
            c3, c4 = randint(2, 6), randint(2, 6)

            # Tính toán giá trị A1 và A2 chính xác bằng SymPy
            # A1 = (c1*cot(x) + c2*tan(x)) / (c1*cot(x) - c2*tan(x))
            # A2 = (c3*sin(x) + cos(x)) / (cos(x) - c4*sin(x)) = (c3*tan(x) + 1) / (1 - c4*tan(x))
            val_A1 = Rational(c1 * val_cot + c2 * val_tan, c1 * val_cot - c2 * val_tan)
            val_A2 = Rational(c3 * val_tan + 1, 1 - c4 * val_tan)

            # Nội dung câu hỏi sử dụng định dạng %s theo yêu cầu bắt buộc
            noidungcauhoi = ('''Cho $\\tan x = %s$. Tính được các biểu thức $A_1 = \\frac{%s\\cot x + %s\\tan x}{%s\\cot x - %s\\tan x}$, $A_2 = \\frac{%s\\sin x + \\cos x}{\\cos x - %s\\sin x}$, khi đó:''' 
                             % (latex(val_tan), latex(c1), latex(c2), latex(c1), latex(c2), latex(c3), latex(c4)))

            ########################################################################
            # Nhận biết (Mệnh đề a: Tính cot x)
            nb_da_1_d = '\\True $\\cot x = %s$' % (latex(val_cot))
            nb_da_1_s = '$\\cot x = %s$' % (latex(-val_cot))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]
            loigiai_nb_1 = ('''Ta có: $\\tan x = %s \\Rightarrow \\cot x = \\frac{1}{\\tan x} = %s$.''' % (latex(val_tan), latex(val_cot)))
            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu (Mệnh đề b: Điều kiện cos x)
            th_da_1_d = 'Vì $\\tan x = %s$ nên $\\cos x = 0$' % (latex(val_tan))
            th_da_1_s = '\\True Vì $\\tan x = %s$ nên $\\cos x \\neq 0$' % (latex(val_tan))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]
            loigiai_th_1 = ('''Vì $\\tan x = %s$ là một giá trị xác định nên $\\cos x \\neq 0$.''' % (latex(val_tan)))
            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng (Mệnh đề c: Tính giá trị biểu thức A1)
            vd_da_1_d = '\\True $A_1 = %s$' % (latex(val_A1))
            vd_da_1_s = '$A_1 = %s$' % (latex(val_A1 + 1))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]
            loigiai_vd_1 = ('''Thay $\\cot x = %s$ và $\\tan x = %s$ vào biểu thức $A_1$, ta được: \\\\ $A_1 = \\frac{%s \\cdot \\left(%s\\right) + %s \\cdot \\left(%s\\right)}{%s \\cdot \\left(%s\\right) - %s \\cdot \\left(%s\\right)} = %s$.''' 
                            % (latex(val_cot), latex(val_tan), latex(c1), latex(val_cot), latex(c2), latex(val_tan), latex(c1), latex(val_cot), latex(c2), latex(val_tan), latex(val_A1)))
            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao (Mệnh đề d: Tính giá trị biểu thức A2)
            vdc_da_1_d = '\\True $A_2 = %s$' % (latex(val_A2))
            vdc_da_1_s = '$A_2 = %s$' % (latex(-val_A2))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]
            loigiai_vdc_1 = ('''Chia cả tử và mẫu của biểu thức $A_2$ cho $\\cos x$, ta được: \\\\ $A_2 = \\frac{%s\\frac{\\sin x}{\\cos x} + \\frac{\\cos x}{\\cos x}}{\\frac{\\cos x}{\\cos x} - %s\\frac{\\sin x}{\\cos x}} = \\frac{%s\\tan x + 1}{1 - %s\\tan x} = \\frac{%s \\cdot \\left(%s\\right) + 1}{1 - %s \\cdot \\left(%s\\right)} = %s$.''' 
                             % (latex(c3), latex(c4), latex(c3), latex(c4), latex(c3), latex(val_tan), latex(c4), latex(val_tan), latex(val_A2)))
            list_vdc_2 = [loigiai_vdc_1]

            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
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

            # Đồng bộ hóa lại danh sách đáp án đã chọn sau vòng lặp
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

            # Khởi tạo khối lời giải chi tiết phân bổ rõ ràng từng ý bằng enumEX [a)]{1}
            loigiai = ('''\\begin{enumEX}[a)]{1} \n'''
                       '''\\item %s\n'''
                       '''\\item %s\n'''
                       '''\\item %s\n'''
                       '''\\item %s\n'''
                       '''\\end{enumEX}'''
                       % (shuffled_solutions_nb[0], shuffled_solutions_th[0], shuffled_solutions_vd[0], shuffled_solutions_vdc[0]))

            # Xuất câu hỏi theo đúng định dạng mẫu khung chương trình và định dạng %s
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' +
                str(noidungcauhoi) + 
                '\n\\choiceTFn \n'
                '{' + str(shuffled_answers_nb[0]) + '}\n'
                '{' + str(shuffled_answers_th[0]) + '}\n'
                '{' + str(shuffled_answers_vd[0]) + '}\n'
                '{' + str(shuffled_answers_vdc[0]) + '}\n'
                '\\loigiai{ \n'
                +loigiai+
                '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


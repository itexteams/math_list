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


def bt_dang13_p2_b2_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến và tạo số ngẫu nhiên cho bài toán
            # cot x = -sqrt(n)
            n_val = random.choice([2, 3, 5, 6, 7])
            cot_val = -sqrt(n_val)

            # Tính toán các giá trị lượng giác chính xác theo giả thiết 3pi/2 < x < 2pi
            # 1/sin^2(x) = 1 + cot^2(x)
            inv_sin2 = 1 + n_val
            sin_val = -1 / sqrt(inv_sin2) # Vì góc thuộc khoảng (3pi/2; 2pi) nên sin < 0
            cos_val = cot_val * sin_val
            tan_val = 1 / cot_val

            # Tính giá trị biểu thức câu c: sin(4pi/3 - x) = sin(4pi/3)cos(x) - cos(4pi/3)sin(x)
            sin_4pi3 = -sqrt(3)/2
            cos_4pi3 = -Rational(1, 2)
            sin_c_val = sin_4pi3 * cos_val - cos_4pi3 * sin_val
            sin_c_val = sp.simplify(sin_c_val)

            # Tính giá trị biểu thức câu d: tan(x + pi/3) = (tan(x) + tan(pi/3)) / (1 - tan(x)tan(pi/3))
            tan_pi3 = sqrt(3)
            tan_d_val = (tan_val + tan_pi3) / (1 - tan_val * tan_pi3)
            tan_d_val = sp.simplify(tan_d_val)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho $\\cot x = %s$, $\\frac{3\\pi}{2} < x < 2\\pi$. Khi đó:''' 
                             %(latex(cot_val)))

            ########################################################################
            # Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True $\\sin x = %s$' %(latex(sin_val))
            nb_da_1_s = '$\\sin x = %s$' %(latex(-sin_val))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''$\\cot x = %s, \\frac{3\\pi}{2} < x < 2\\pi$\\\\
            \\quad $\\frac{1}{\\sin^2 x} = 1 + \\cot^2 x = 1 + \\left(%s\\right)^2 = %s \\Rightarrow \\sin^2 x = \\frac{1}{%s} \\Rightarrow \\sin x = \\pm %s$\\\\
            \\quad Vì $\\frac{3\\pi}{2} < x < 2\\pi$ nên $\\sin x = %s$.'''
                            %(latex(cot_val), latex(cot_val), latex(inv_sin2), latex(inv_sin2), latex(-sin_val), latex(sin_val)))

            list_nb_2 = [loigiai_nb_1]
            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            # Các đáp án (Gốc cố tình cho phương án b Sai bằng cách mất dấu trừ hoặc đảo lộn số)
            th_da_1_d = '\\True $\\cos x = %s$' %(latex(cos_val))
            th_da_1_s = '$\\cos x = \\frac{\\sqrt{%s}}{%s}$' %(latex(n_val), latex(inv_sin2)) if n_val == 3 else '$\\cos x = %s$' %(latex(-cos_val))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''$\\cos x = \\cot x \\cdot \\sin x = \\left(%s\\right) \\cdot \\left(%s\\right) = %s$.'''
                            %(latex(cot_val), latex(sin_val), latex(cos_val)))

            list_th_2 = [loigiai_th_1]
            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True $\\sin\\left(\\frac{4\\pi}{3} - x\\right) = %s$' %(latex(sin_c_val))
            vd_da_1_s = '$\\sin\\left(\\frac{\\pi}{3} - x\\right) = %s$' %(latex(-sin_c_val))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''$\\sin\\left(\\frac{4\\pi}{3} - x\\right) = \\sin\\frac{4\\pi}{3}\\cos x - \\cos\\frac{4\\pi}{3}\\sin x = -\\frac{\\sqrt{3}}{2} \\cdot \\left(%s\\right) - \\frac{-1}{2} \\cdot \\left(%s\\right) = %s$.'''
                            %(latex(cos_val), latex(sin_val), latex(sin_c_val)))

            list_vd_2 = [loigiai_vd_1]
            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True $\\tan\\left(x + \\frac{\\pi}{3}\\right) = %s$' %(latex(tan_d_val))
            vdc_da_1_s = '$\\tan\\left(x + \\frac{\\pi}{3}\\right) = %s$' %(latex(-tan_d_val))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''$\\tan x = \\frac{1}{\\cot x} = %s$.\\\\
            $\\tan\\left(x + \\frac{\\pi}{3}\\right) = \\frac{\\tan x + \\tan\\frac{\\pi}{3}}{1 - \\tan x \\cdot \\tan\\frac{\\pi}{3}} = \\frac{%s + \\sqrt{3}}{1 - \\left(%s\\right) \\cdot \\sqrt{3}} = %s$.'''
                             %(latex(tan_val), latex(tan_val), latex(tan_val), latex(tan_d_val)))

            list_vdc_2 = [loigiai_vdc_1]
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi bộ đáp án tổng hợp có từ 1 đến 3 câu Đúng để phù hợp định dạng TN Đúng/Sai
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán lại vào danh sách sau khi đã chọn lọc số lượng Đúng/Sai thỏa mãn
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

            # Xuất câu hỏi với đáp án và lời giải đã được xử lý xáo trộn theo đúng cấu trúc khung chương trình mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
            str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
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


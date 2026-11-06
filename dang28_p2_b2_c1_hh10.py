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


def bt_dang28_p2_b2_c1_hh10(self):
    # Khai báo biến và random số liệu
    # Cho phần a, b
    a_val = random.randint(6, 12)
    b_val = random.randint(7, 13)
    c_val = random.randint(8, 15)
    # Ensure it forms a triangle
    while not (a_val + b_val > c_val and a_val + c_val > b_val and b_val + c_val > a_val):
        a_val = random.randint(6, 12)
        b_val = random.randint(7, 13)
        c_val = random.randint(8, 15)

    cosB = sp.Rational(a_val**2 + c_val**2 - b_val**2, 2 * a_val * c_val)
    B_deg = round(math.degrees(math.acos(float(cosB))))
    B_deg_false = B_deg + random.choice([-5, 5, -10, 10])

    cosC = sp.Rational(a_val**2 + b_val**2 - c_val**2, 2 * a_val * b_val)
    sinC = sp.simplify(sp.sqrt(1 - cosC**2))
    sinC_false = sp.simplify(sp.sqrt(1 - cosC**2) * sp.Rational(1, 2))

    # Cho phần c
    b_c = random.randint(2, 4)
    c_c = random.randint(3, 5)
    A_c = 60
    a_sq = b_c**2 + c_c**2 - 2 * b_c * c_c * sp.Rational(1, 2)
    # a = sqrt(ax + 1) -> ax + 1 = a_sq -> x = (a_sq - 1)/a_coeff
    a_coeff = random.choice([2, 3])
    while (a_sq - 1) % a_coeff != 0:
        b_c = random.randint(2, 4)
        c_c = random.randint(3, 5)
        a_sq = b_c**2 + c_c**2 - 2 * b_c * c_c * sp.Rational(1, 2)
    x_val = (a_sq - 1) // a_coeff
    x_val_false = x_val + random.choice([-1, 1, 2])

    # Cho phần d
    k_choices = [(1, 60), (sp.sqrt(3), 30), (sp.sqrt(2), 45)]
    k_val, BAC_deg = random.choice(k_choices)
    if k_val == 1:
        k_str = ''
        cosA_d = sp.Rational(1, 2)
    elif k_val == sp.sqrt(3):
        k_str = '\\sqrt{3}'
        cosA_d = sp.sqrt(3)/2
    else:
        k_str = '\\sqrt{2}'
        cosA_d = sp.sqrt(2)/2
    BAC_deg_false = BAC_deg + random.choice([15, -15, 30])


    # Nội dung câu hỏi
    noidungcauhoi = ('''Cho tam giác $ABC$ có $AB = c, BC = a, AC = b$.'''               
                     )

    ######################################################################## Nhận biết ############################################
    # Các đáp án
    nb_da_1_d = '\\True Cho $a = %scm, b = %scm, c = %scm$. Khi đó số đo góc $B \\approx %s^\\circ$.' % (a_val, b_val, c_val, B_deg)
    nb_da_1_s = 'Cho $a = %scm, b = %scm, c = %scm$. Khi đó số đo góc $B \\approx %s^\\circ$.' % (a_val, b_val, c_val, B_deg_false)
    list_nb_da_1=[nb_da_1_d,nb_da_1_s]
    nb_da_1=random.choice(list_nb_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]

    # Nội dung lời giải
    loigiai_nb_1 = ('''Áp dụng hệ quả định lý côsin ta có: \\\\
    $\\cos B = \\frac{a^2 + c^2 - b^2}{2ac} = \\frac{%s^2 + %s^2 - %s^2}{2 \\cdot %s \\cdot %s} = %s$. \\\\
    Suy ra $B \\approx %s^\\circ$.'''
                    %(a_val, c_val, b_val, a_val, c_val, sp.latex(cosB), B_deg))

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
    th_da_1_d = '\\True Nếu $a = %scm, b = %scm, c = %scm$ thì $\\sin C = %s$' % (a_val, b_val, c_val, sp.latex(sinC))  
    th_da_1_s = 'Nếu $a = %scm, b = %scm, c = %scm$ thì $\\sin C = %s$' % (a_val, b_val, c_val, sp.latex(sinC_false))   
    list_th_da_1=[th_da_1_d,th_da_1_s]
    th_da_1=random.choice(list_th_da_1)


    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]

    # Nội dung lời giải
    loigiai_th_1 = ('''Áp dụng hệ quả định lý côsin ta có: \\\\
    $\\cos C = \\frac{a^2 + b^2 - c^2}{2ab} = \\frac{%s^2 + %s^2 - %s^2}{2 \\cdot %s \\cdot %s} = %s$. \\\\
    Mà $\\sin^2 C + \\cos^2 C = 1$ và $\\sin C > 0$ nên $\\sin C = \\sqrt{1 - \\cos^2 C} = \\sqrt{1 - \\left(%s\\right)^2} = %s$.'''       
               %(a_val, b_val, c_val, a_val, b_val, sp.latex(cosC), sp.latex(cosC), sp.latex(sinC)))

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
    vd_da_1_d = '\\True Cho $a = \\sqrt{%sx + 1}, b = %s, c = %s, A = 60^\\circ$ thì $x = %s$.' % (a_coeff, b_c, c_c, x_val)  
    vd_da_1_s = 'Cho $a = \\sqrt{%sx + 1}, b = %s, c = %s, A = 60^\\circ$ thì $x = %s$.' % (a_coeff, b_c, c_c, x_val_false)  
    list_vd_da_1=[vd_da_1_d,vd_da_1_s]
    vd_da_1=random.choice(list_vd_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]

    # Nội dung lời giải
    loigiai_vd_1 = ('''Áp dụng định lý côsin ta có: \\\\
    $a^2 = b^2 + c^2 - 2bc \\cos A \\Leftrightarrow %sx + 1 = %s^2 + %s^2 - 2 \\cdot %s \\cdot %s \\cos 60^\\circ$. \\\\
    $\\Leftrightarrow %sx + 1 = %s \\Leftrightarrow %sx = %s \\Leftrightarrow x = %s$.'''  
               %(a_coeff, b_c, c_c, b_c, c_c, a_coeff, a_sq, a_coeff, a_sq - 1, x_val))

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
    vdc_da_1_d = '\\True Cho $b^2 + c^2 - a^2 = %s bc$ thì $\\widehat{BAC} = %s^\\circ$.' % (k_str, BAC_deg) 
    vdc_da_1_s = 'Cho $b^2 + c^2 - a^2 = %s bc$ thì $\\widehat{BAC} = %s^\\circ$.' % (k_str, BAC_deg_false) 
    list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
    vdc_da_1=random.choice(list_vdc_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]

    # Nội dung lời giải
    loigiai_vdc_1 = ('''Từ giả thiết $b^2 + c^2 - a^2 = %s bc$, ta có: \\\\
    $\\cos A = \\frac{b^2 + c^2 - a^2}{2bc} = \\frac{%s bc}{2bc} = %s$. \\\\
    Suy ra $\\widehat{BAC} = %s^\\circ$.'''
               %(k_str, k_str, sp.latex(cosA_d), BAC_deg))

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
    str(noidungcauhoi)+ '\n'+
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


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


def bt_dang16_p2_b2_c1_hh10(self):
    # Hàm hỗ trợ định dạng số thập phân sử dụng dấu phẩy
    def format_num(num):
        return str(num).replace('.', ',')

    # Sinh các biến ngẫu nhiên cho bài toán
    while True:
        c = random.randint(12, 18) # Cạnh AB
        b = random.randint(14, 22) # Cạnh AC
        alpha = random.randint(50, 70) # Góc A
        if b == c: 
            continue

        # Tính cạnh BC
        bc_exact_sq = c**2 + b**2 - 2 * c * b * math.cos(math.radians(alpha))
        bc_exact = math.sqrt(bc_exact_sq)
        bc_round = round(bc_exact, 1)

        # Tính góc B
        cos_B = (c**2 + bc_exact**2 - b**2) / (2 * c * bc_exact)
        B_rad = math.acos(cos_B)
        B_deg_total = math.degrees(B_rad)
        B_deg = int(B_deg_total)
        B_min = round((B_deg_total - B_deg) * 60)
        if B_min == 60:
            B_deg += 1
            B_min = 0

        # Tính điểm M
        c_half = c / 2.0
        x_c = b * math.cos(math.radians(alpha))
        y_c = b * math.sin(math.radians(alpha))

        max_m_sq = c_half**2 + y_c**2
        min_m_val = math.ceil(c_half) + 1
        max_m_val = int(math.sqrt(max_m_sq)) - 1

        if min_m_val >= max_m_val:
            continue

        m = random.randint(min_m_val, max_m_val)

        y_m_exact = math.sqrt(m**2 - c_half**2)
        mc_exact = math.sqrt((x_c - c_half)**2 + (y_c - y_m_exact)**2)
        mc_round = round(mc_exact, 1)
        break

    # Nội dung câu hỏi
    noidungcauhoi = ('''Cho tam giác $ABC$ có $AB = %s\\ cm; AC = %s\\ cm; A = %s^\\circ$.'''              
                     %(c, b, alpha))

    ########################################################################
    # Nhận biết ############################################
    # Các đáp án 
    nb_da_1_d = '\\True Ta có: $BC^2 = AB^2 + AC^2 - 2 \\cdot AB \\cdot AC \\cdot \\cos A$'
    nb_da_1_s = 'Ta có: $BC^2 = AB^2 + AC^2 - 2 \\cdot AB \\cdot AC \\cdot \\sin A$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]

    # Nội dung lời giải
    loigiai_nb_1 = ('''Theo định lý côsin trong tam giác $ABC$, ta có công thức đúng là: \\\\
    $BC^2 = AB^2 + AC^2 - 2 \\cdot AB \\cdot AC \\cdot \\cos A$.'''
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
    th_da_1_d = '\\True Cạnh $BC \\simeq %s\\ cm$' %(format_num(bc_round))  
    th_da_1_s = 'Cạnh $BC \\simeq %s\\ cm$' %(format_num(round(bc_exact + random.choice([1.2, -1.5, 2.1]), 1)))   
    list_th_da_1=[th_da_1_d,th_da_1_s]
    th_da_1=random.choice(list_th_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]

    # Nội dung lời giải
    loigiai_th_1 = ('''Áp dụng định lý côsin, ta có: \\\\
    $BC^2 = %s^2 + %s^2 - 2 \\cdot %s \\cdot %s \\cdot \\cos(%s^\\circ) \\approx %s$. \\\\
    Suy ra $BC \\approx %s\\ cm$.'''       
               %(c, b, c, b, alpha, format_num(round(bc_exact_sq, 2)), format_num(bc_round)))

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
    vd_da_1_d = '\\True Góc $B \\simeq %s^\\circ %s\'$' %(B_deg, B_min)  
    vd_da_1_s = 'Góc $B \\simeq %s^\\circ %s\'$' %(B_deg + random.choice([-2, -1, 1, 2]), B_min)  
    list_vd_da_1=[vd_da_1_d,vd_da_1_s]
    vd_da_1=random.choice(list_vd_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]

    # Nội dung lời giải
    loigiai_vd_1 = ('''Áp dụng hệ quả của định lý côsin, ta có: \\\\
    $\\cos B = \\frac{AB^2 + BC^2 - AC^2}{2 \\cdot AB \\cdot BC} \\approx \\frac{%s^2 + %s^2 - %s^2}{2 \\cdot %s \\cdot %s} \\approx %s$. \\\\
    Suy ra $\\widehat{B} \\approx %s^\\circ %s\'$.'''  
               %(c, format_num(bc_round), b, c, format_num(bc_round), format_num(round(cos_B, 4)), B_deg, B_min))

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
    vdc_da_1_d = '\\True Cho điểm $M$ nằm trong tam giác $ABC$ biết $MA = MB = %s\\ cm$. Khi đó cạnh $MC \\simeq %s\\ cm$' %(m, format_num(mc_round)) 
    vdc_da_1_s = 'Cho điểm $M$ nằm trong tam giác $ABC$ biết $MA = MB = %s\\ cm$. Khi đó cạnh $MC \\simeq %s\\ cm$' %(m, format_num(round(mc_exact + random.choice([-1.1, 1.3]), 1))) 
    list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
    vdc_da_1=random.choice(list_vdc_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]

    # Nội dung lời giải
    loigiai_vdc_1 = ('''Chọn hệ trục tọa độ sao cho $A$ trùng với gốc tọa độ, $B$ nằm trên tia $Ox$. \\\\
    Khi đó tọa độ các điểm là $A(0; 0)$ và $B(%s; 0)$. \\\\
    Tọa độ điểm $C(AC \\cdot \\cos A; AC \\cdot \\sin A) = (%s \\cdot \\cos %s^\\circ; %s \\cdot \\sin %s^\\circ) \\approx (%s; %s)$. \\\\
    Điểm $M$ thỏa mãn $MA = MB = %s$ nên $M$ nằm trên đường trung trực của $AB$. \\\\
    Phương trình đường trung trực của $AB$ là $x = %s$. \\\\
    Gọi $M(%s; y_M)$, ta có $MA = %s \\Rightarrow \\sqrt{%s^2 + y_M^2} = %s \\Rightarrow y_M = \\sqrt{%s^2 - %s^2} \\approx %s$ (do $M$ nằm trong tam giác nên $y_M > 0$). \\\\
    Vậy $M(%s; %s)$. Độ dài đoạn $MC = \\sqrt{(x_C - x_M)^2 + (y_C - y_M)^2} \\approx \\sqrt{(%s - %s)^2 + (%s - %s)^2} \\approx %s\\ cm$.'''
               %(c, b, alpha, b, alpha, format_num(round(x_c, 2)), format_num(round(y_c, 2)), m, format_num(c_half), format_num(c_half), m, format_num(c_half), m, m, format_num(c_half), format_num(round(y_m_exact, 2)), format_num(c_half), format_num(round(y_m_exact, 2)), format_num(round(x_c, 2)), format_num(c_half), format_num(round(y_c, 2)), format_num(round(y_m_exact, 2)), format_num(mc_round)))

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
        '\\end{ex}\n\\end{minipage}\n\n')
    return content


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


def bt_dang34_p2_b2_c1_hh10(self):
    # Khai báo biến
    # Các cấu hình tam giác tạo ra số liệu đẹp (a là số nguyên hoặc căn thức gọn)
    configs = [
        (sp.sympify('2*sqrt(3)'), sp.sympify('3'), sp.sympify('-sqrt(3)/9')), # Cấu hình gốc
        (sp.sympify('3'), sp.sympify('2*sqrt(3)'), sp.sympify('-sqrt(3)/9')),
        (sp.sympify('5'), sp.sympify('4*sqrt(2)'), sp.sympify('sqrt(2)/10')),
        (sp.sympify('4*sqrt(2)'), sp.sympify('5'), sp.sympify('sqrt(2)/10'))
    ]

    c_val, b_val, cos_A_val = random.choice(configs)

    # Tính toán các thông số
    a_val = sp.sqrt(sp.simplify(b_val**2 + c_val**2 - 2*b_val*c_val*cos_A_val))
    sin2_A_val = sp.simplify(1 - cos_A_val**2)
    sin_A_val = sp.sqrt(sin2_A_val)
    S_val = sp.simplify(sp.Rational(1, 2) * b_val * c_val * sin_A_val)
    AM_val = sp.simplify(b_val / 2)
    BM2_val = sp.simplify(c_val**2 + AM_val**2 - 2*c_val*AM_val*cos_A_val)
    BM_val = sp.sqrt(BM2_val)

    # Sắp xếp các cạnh để tìm góc nhỏ nhất
    sides = [
        (float(a_val.evalf()), 'BC', sp.latex(a_val), 'B', 'C'), # Góc đối diện BC là A (không dùng), nhưng ta lấy đỉnh
        (float(b_val.evalf()), 'AC', sp.latex(b_val), 'B', 'A'), # Góc đối diện AC là B
        (float(c_val.evalf()), 'AB', sp.latex(c_val), 'C', 'A')  # Góc đối diện AB là C
    ]
    # Gán lại góc đối diện cho chính xác
    sides_with_angles = [
        (float(a_val.evalf()), 'BC', sp.latex(a_val), 'A'),
        (float(b_val.evalf()), 'AC', sp.latex(b_val), 'B'),
        (float(c_val.evalf()), 'AB', sp.latex(c_val), 'C')
    ]
    sides_with_angles.sort(key=lambda x: x[0])

    min_side_name = sides_with_angles[0][1]
    min_side_latex = sides_with_angles[0][2]
    min_angle = sides_with_angles[0][3]

    inequality_str = f"{sides_with_angles[0][2]} < {sides_with_angles[1][2]} < {sides_with_angles[2][2]}"

    # Các giá trị sai cho phương án nhiễu
    false_angles = [a for a in ['A', 'B', 'C'] if a != min_angle]
    false_angle = random.choice(false_angles)

    a_false_val = a_val + 1 if a_val.is_integer else sp.sqrt(a_val**2 + 5)
    S_false_val = S_val * 2 if S_val.is_integer else sp.sqrt(S_val**2 + 5)

    try:
        bm2_float = float(BM2_val.evalf())
        BM_false_str = f"\\sqrt{{{int(bm2_float) - 1}}}" if int(bm2_float) > 1 else "\\sqrt{13}"
    except:
        BM_false_str = "\\sqrt{13}"

    if b_val == 3 and c_val == 2*sp.sqrt(3):
        BM_false_str = "\\sqrt{13}"

    # Nội dung câu hỏi
    noidungcauhoi = ('''Cho tam giác $ABC$ có $AB = %s, AC = %s$ và $\\cos A = %s$.'''                
                     %(sp.latex(c_val), sp.latex(b_val), sp.latex(cos_A_val)))

    ########################################################################
    # Nhận biết ############################################
    # Các đáp án
    nb_da_1_d = '\\True Góc nhỏ nhất trong tam giác là góc $\\widehat{%s}$' %(min_angle)
    nb_da_1_s = 'Góc nhỏ nhất trong tam giác là góc $\\widehat{%s}$' %(false_angle)
    list_nb_da_1=[nb_da_1_d,nb_da_1_s]
    nb_da_1=random.choice(list_nb_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]

    # Nội dung lời giải
    loigiai_nb_1 = ('''Ta có $BC^2 = AB^2 + AC^2 - 2 \\cdot AB \\cdot AC \\cdot \\cos A = (%s)^2 + (%s)^2 - 2 \\cdot %s \\cdot %s \\cdot \\left(%s\\right) = %s \\Rightarrow BC = %s$. \\\\
                       Ta thấy $AB = %s, AC = %s, BC = %s$. \\\\
                       Vì $%s$ nên cạnh $%s$ là cạnh nhỏ nhất trong tam giác. \\\\
                       Do đó góc nhỏ nhất là góc $\\widehat{%s}$.'''
                %(sp.latex(c_val), sp.latex(b_val), sp.latex(c_val), sp.latex(b_val), sp.latex(cos_A_val), sp.latex(a_val**2), sp.latex(a_val),
                  sp.latex(c_val), sp.latex(b_val), sp.latex(a_val),
                  inequality_str, min_side_name, min_angle))

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
    th_da_1_d = '\\True Độ dài cạnh $BC$ là $%s$' %(sp.latex(a_val))  
    th_da_1_s = 'Độ dài cạnh $BC$ là $%s$' %(sp.latex(a_false_val))   
    list_th_da_1=[th_da_1_d,th_da_1_s]
    th_da_1=random.choice(list_th_da_1)


    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]

    # Nội dung lời giải
    loigiai_th_1 = ('''Áp dụng định lí côsin trong tam giác $ABC$, ta có: \\\\
                       $BC^2 = AB^2 + AC^2 - 2 \\cdot AB \\cdot AC \\cdot \\cos A = (%s)^2 + (%s)^2 - 2 \\cdot %s \\cdot %s \\cdot \\left(%s\\right) = %s$. \\\\
                       Suy ra $BC = %s$.'''       
               %(sp.latex(c_val), sp.latex(b_val), sp.latex(c_val), sp.latex(b_val), sp.latex(cos_A_val), sp.latex(a_val**2), sp.latex(a_val)))

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
    vd_da_1_d = '\\True Gọi $M$ là trung điểm của cạnh $AC$. Độ dài cạnh $BM$ là $%s$' %(sp.latex(BM_val))  
    vd_da_1_s = 'Gọi $M$ là trung điểm của cạnh $AC$. Độ dài cạnh $BM$ là $%s$' %(BM_false_str)  
    list_vd_da_1=[vd_da_1_d,vd_da_1_s]
    vd_da_1=random.choice(list_vd_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]

    # Nội dung lời giải
    loigiai_vd_1 = ('''$M$ là trung điểm của $AC$ nên $AM = \\frac{AC}{2} = \\frac{%s}{2} = %s$. \\\\
                       Áp dụng định lí côsin trong tam giác $ABM$, ta có: \\\\
                       $BM^2 = AB^2 + AM^2 - 2 \\cdot AB \\cdot AM \\cdot \\cos A$ \\\\
                       $= (%s)^2 + \\left(%s\\right)^2 - 2 \\cdot %s \\cdot \\left(%s\\right) \\cdot \\left(%s\\right) = %s$. \\\\
                       Suy ra $BM = %s$.'''  
               %(sp.latex(b_val), sp.latex(AM_val),
                 sp.latex(c_val), sp.latex(AM_val), sp.latex(c_val), sp.latex(AM_val), sp.latex(cos_A_val), sp.latex(BM2_val), sp.latex(BM_val)))

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
    vdc_da_1_d = '\\True Diện tích của tam giác $ABC$ là $%s$' %(sp.latex(S_val)) 
    vdc_da_1_s = 'Diện tích của tam giác $ABC$ là $%s$' %(sp.latex(S_false_val)) 
    list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
    vdc_da_1=random.choice(list_vdc_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]

    # Nội dung lời giải
    loigiai_vdc_1 = ('''Ta có $\\sin^2 A = 1 - \\cos^2 A = 1 - \\left(%s\\right)^2 = %s$. \\\\
                        Vì $\\widehat{A}$ là một góc của tam giác nên $\\sin A > 0 \\Rightarrow \\sin A = %s$. \\\\
                        Diện tích tam giác $ABC$ là $S = \\frac{1}{2} \\cdot AB \\cdot AC \\cdot \\sin A = \\frac{1}{2} \\cdot %s \\cdot %s \\cdot %s = %s$.'''
               %(sp.latex(cos_A_val), sp.latex(sin2_A_val), sp.latex(sin_A_val),
                 sp.latex(c_val), sp.latex(b_val), sp.latex(sin_A_val), sp.latex(S_val)))

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


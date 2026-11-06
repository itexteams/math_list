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


def bt_dang25_p2_b2_c1_hh10(self):
    # Khai báo biến và random số liệu (chọn các bộ ba cạnh tam giác Heron để diện tích nguyên)
    heron_triangles = [
        (13, 14, 15),
        (9, 10, 17),
        (7, 15, 20),
        (10, 17, 21),
        (17, 25, 26),
        (13, 20, 21)
    ]
    sides = list(random.choice(heron_triangles))
    random.shuffle(sides)
    c, b, a = sides # AB = c, AC = b, BC = a

    # Tính toán các đại lượng chính xác
    p = sp.Rational(a + b + c, 2)
    S = sp.sqrt(p * (p - a) * (p - b) * (p - c))

    r_exact = sp.simplify(S / p)
    r_false = sp.simplify(r_exact * sp.Rational(1, 2))

    sinB_exact = sp.simplify(2 * S / (a * c))
    sinB_false = sp.simplify(S / (a * c))

    max_side = max(a, b, c)
    other_sides = [s for s in [a, b, c]]
    other_sides.remove(max_side)

    is_obtuse = max_side**2 > other_sides[0]**2 + other_sides[1]**2
    is_right = max_side**2 == other_sides[0]**2 + other_sides[1]**2

    # Nội dung câu hỏi
    noidungcauhoi = ('''Cho tam giác $ABC$ có $AB = %s, AC = %s, BC = %s$.'''               
                     %(c, b, a))

    ######################################################################## Nhận biết ############################################
    # Các đáp án
    if is_obtuse:
        nb_da_1_d = '\\True $\\Delta ABC$ có $1$ góc tù.'
        nb_da_1_s = '$\\Delta ABC$ là tam giác nhọn.'
        loigiai_nb = 'Ta có cạnh lớn nhất của tam giác là $%s$. Vì $%s^2 > %s^2 + %s^2$ nên tam giác $ABC$ có một góc tù.' % (max_side, max_side, other_sides[0], other_sides[1])
    elif is_right:
        nb_da_1_d = '\\True $\\Delta ABC$ là tam giác vuông.'
        nb_da_1_s = '$\\Delta ABC$ là tam giác nhọn.'
        loigiai_nb = 'Ta có cạnh lớn nhất của tam giác là $%s$. Vì $%s^2 = %s^2 + %s^2$ nên tam giác $ABC$ là tam giác vuông.' % (max_side, max_side, other_sides[0], other_sides[1])
    else:
        nb_da_1_d = '\\True $\\Delta ABC$ là tam giác nhọn.'
        nb_da_1_s = '$\\Delta ABC$ có $1$ góc tù.'
        loigiai_nb = 'Ta có cạnh lớn nhất của tam giác là $%s$. Vì $%s^2 < %s^2 + %s^2$ nên tam giác $ABC$ là tam giác nhọn.' % (max_side, max_side, other_sides[0], other_sides[1])

    list_nb_da_1=[nb_da_1_d,nb_da_1_s]
    nb_da_1=random.choice(list_nb_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]

    # Nội dung lời giải
    loigiai_nb_1 = (loigiai_nb)

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
    th_da_1_d = '\\True Diện tích tam giác $ABC$ bằng $%s$.' % (sp.latex(S))  
    th_da_1_s = 'Diện tích tam giác $ABC$ bằng $%s$.' % (sp.latex(S + random.choice([-10, -5, 5, 10])))   
    list_th_da_1=[th_da_1_d,th_da_1_s]
    th_da_1=random.choice(list_th_da_1)


    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]

    # Nội dung lời giải
    loigiai_th_1 = ('''Nửa chu vi tam giác $ABC$ là $p = \\frac{AB + AC + BC}{2} = \\frac{%s + %s + %s}{2} = %s$. \\\\
    Áp dụng công thức Heron, diện tích tam giác $ABC$ là: \\\\
    $S = \\sqrt{p(p-AB)(p-AC)(p-BC)} = \\sqrt{%s(%s-%s)(%s-%s)(%s-%s)} = %s$.'''       
               %(c, b, a, sp.latex(p), sp.latex(p), sp.latex(p), c, sp.latex(p), b, sp.latex(p), a, sp.latex(S)))

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
    vd_da_1_d = '\\True Bán kính đường tròn nội tiếp tam giác $ABC$ bằng $%s$.' % (sp.latex(r_exact))  
    vd_da_1_s = 'Bán kính đường tròn nội tiếp tam giác $ABC$ bằng $%s$.' % (sp.latex(r_false))  
    list_vd_da_1=[vd_da_1_d,vd_da_1_s]
    vd_da_1=random.choice(list_vd_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]

    # Nội dung lời giải
    loigiai_vd_1 = ('''Ta có $S = p \\cdot r \\Rightarrow r = \\frac{S}{p} = \\frac{%s}{%s} = %s$. \\\\
    Vậy bán kính đường tròn nội tiếp tam giác $ABC$ là $r = %s$.'''  
               %(sp.latex(S), sp.latex(p), sp.latex(r_exact), sp.latex(r_exact)))

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
    vdc_da_1_d = '\\True $\\sin B = %s$' % (sp.latex(sinB_exact)) 
    vdc_da_1_s = '$\\sin B = %s$' % (sp.latex(sinB_false)) 
    list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
    vdc_da_1=random.choice(list_vdc_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]

    # Nội dung lời giải
    loigiai_vdc_1 = ('''Ta có diện tích tam giác $S = \\frac{1}{2} \\cdot BA \\cdot BC \\cdot \\sin B$. \\\\
    Suy ra $\\sin B = \\frac{2S}{BA \\cdot BC} = \\frac{2 \\cdot %s}{%s \\cdot %s} = %s$.'''
               %(sp.latex(S), c, a, sp.latex(sinB_exact)))

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


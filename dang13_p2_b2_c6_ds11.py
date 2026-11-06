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


def bt_dang13_p2_b2_c6_ds11(self):
    # Chọn ngẫu nhiên số k chia hết cho biến cố A (ví dụ chọn trong khoảng 6 đến 9)
    k = random.choice([6, 7, 8, 9])

    # Tính toán các tập hợp và xác suất
    n_Omega = 90

    # Biến cố A: chia hết cho k
    A_set = [x for x in range(10, 100) if x % k == 0]
    n_A = len(A_set)
    p_A = Rational(n_A, n_Omega)

    # Biến cố B: hai chữ số giống nhau (bội của 11)
    B_set = [x for x in range(10, 100) if x % 11 == 0]
    n_B = len(B_set)  # 9 phần tử
    p_B = Rational(n_B, n_Omega)  # 1/10

    # Biến cố giao A cap B
    A_cap_B = [x for x in A_set if x % 11 == 0]
    n_A_cap_B = len(A_cap_B)

    # Biến cố hợp A cup B
    n_A_cup_B = n_A + n_B - n_A_cap_B
    p_A_cup_B = Rational(n_A_cup_B, n_Omega)

    # Định dạng chuỗi tập hợp cho LaTeX
    str_A_set = "\\{" + "; ".join(str(num) for num in A_set) + "\\}"
    str_A_cap_B = "\\{" + "; ".join(str(num) for num in A_cap_B) + "\\}" if n_A_cap_B > 0 else "\\emptyset"

    # Nội dung câu hỏi
    noidungcauhoi = ('''Xét phép thử chọn ngẫu nhiên một số tự nhiên có hai chữ số. Xét biến cố A: "Số được chọn là số chia hết cho %s" và biến cố B: "Số được chọn là số có hai chữ số giống nhau".'''
                     % (latex(k)))

    ########################################################################
    # Nhận biết ############################################
    # Các đáp án
    nb_da_1_d = '\\True Số phần tử của không gian mẫu là $n(\\Omega) = 90$'
    nb_da_1_s = 'Số phần tử của không gian mẫu là $n(\\Omega) = 89$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]

    # Nội dung lời giải
    loigiai_nb_1 = ('''Các số tự nhiên có hai chữ số là các số thuộc tập hợp $\\{10; 11; 12; \\dots; 99\\}$.\\\\
    Số phần tử của không gian mẫu là $n(\\Omega) = 99 - 10 + 1 = 90$.'''
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
    # Tạo phương án sai cho P(A)
    p_A_sai = Rational(n_A + 1, n_Omega) if n_A + 1 != n_Omega else Rational(n_A - 1, n_Omega)

    # Các đáp án
    th_da_1_d = '\\True Xác suất của biến cố A là $P(A) = %s$' % (latex(p_A))
    th_da_1_s = 'Xác suất của biến cố A là $P(A) = %s$' % (latex(p_A_sai))
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]

    # Nội dung lời giải
    loigiai_th_1 = ('''Các số tự nhiên có hai chữ số chia hết cho %s là: $%s$.\\\\
    Số kết quả thuận lợi cho biến cố A là $n(A) = %s$.\\\\
    Xác suất của biến cố A là $P(A) = \\frac{n(A)}{n(\\Omega)} = \\frac{%s}{90} = %s$.'''
                % (latex(k), str_A_set, latex(n_A), latex(n_A), latex(p_A)
                   ))

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
    vd_da_1_d = '\\True Xác suất của biến cố B là $P(B) = \\frac{1}{10}$'
    vd_da_1_s = 'Xác suất của biến cố B là $P(B) = \\frac{1}{9}$'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]

    # Nội dung lời giải
    loigiai_vd_1 = ('''Các số tự nhiên có hai chữ số giống nhau là: $\\{11; 22; 33; 44; 55; 66; 77; 88; 99\\}$.\\\\
    Số kết quả thuận lợi cho biến cố B là $n(B) = 9$.\\\\
    Xác suất của biến cố B là $P(B) = \\frac{n(B)}{n(\\Omega)} = \\frac{9}{90} = \\frac{1}{10}$.'''
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
    # Tạo phương án sai cho P(A cup B)
    p_A_cup_B_sai = Rational(n_A_cup_B + 1, n_Omega) if n_A_cup_B + 1 != n_Omega else Rational(n_A_cup_B - 1, n_Omega)

    # Các đáp án
    vdc_da_1_d = '\\True Xác suất của biến cố hợp $A \\cup B$ là $P(A \\cup B) = %s$' % (latex(p_A_cup_B))
    vdc_da_1_s = 'Xác suất của biến cố hợp $A \\cup B$ là $P(A \\cup B) = %s$' % (latex(p_A_cup_B_sai))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]

    # Nội dung lời giải
    loigiai_vdc_1 = ('''Biến cố $A \\cap B$ là biến cố "Số được chọn là số chia hết cho %s và có hai chữ số giống nhau".\\\\
    Tập hợp các số thuộc $A \\cap B$ là $%s$, do đó $n(A \\cap B) = %s$.\\\\
    Số phần tử của biến cố hợp $A \\cup B$ là:\\\\
    $n(A \\cup B) = n(A) + n(B) - n(A \\cap B) = %s + 9 - %s = %s$.\\\\
    Xác suất của biến cố hợp $A \\cup B$ là $P(A \\cup B) = \\frac{n(A \\cup B)}{n(\\Omega)} = \\frac{%s}{90} = %s$.'''
                % (latex(k), str_A_cap_B, latex(n_A_cap_B), latex(n_A), latex(n_A_cap_B), latex(n_A_cup_B), latex(n_A_cup_B), latex(p_A_cup_B)
                   ))

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
        ' \\choiceTFn \n'
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


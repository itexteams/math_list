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


def bt_dang14_p2_b3_c6_ds11(self):
    # Hàm chuyển đổi số thực thành chuỗi thập phân dùng dấu phẩy (VD: 0.15 -> 0,15)
    def format_num(val):
        s = "{:.6f}".format(val).rstrip('0').rstrip('.')
        return s.replace('.', ',')

    # Khai báo và random biến
    # Random xác suất sao cho tổng luôn nhỏ hơn hoặc bằng 1 và số tròn trịa
    p1 = random.choice([0.1, 0.15, 0.2])
    p2 = random.choice([0.2, 0.25, 0.3])
    p8 = random.choice([0.2, 0.25, 0.3])
    plt8 = round(1.0 - (p1 + p2 + p8), 2)

    # Tính toán các xác suất và trường hợp
    p3_10 = round(p1**3, 6)
    p910 = round(1 - p8 - plt8, 2)

    p29 = round(3 * p1**2 * p2, 6)
    wrong_p29 = round(p1**2 * p2, 6) # Đáp án nhiễu sai do quên nhân 3

    p30 = round(p1**3, 6)
    p10_9_9 = round(3 * p1 * p2**2, 6)
    p10_10_8 = round(3 * p1**2 * p8, 6)
    p28 = round(p30 + p29 + p10_9_9 + p10_10_8, 6)
    wrong_p28 = round(p30 + p29 + p10_10_8, 6) # Đáp án nhiễu sai do thiếu 1 trường hợp 28 điểm

    wrong_p1 = round(p1 + 0.05, 2)
    wrong_p2 = round(p2 - 0.05, 2)

    # Chuẩn bị chuỗi định dạng (dấu phẩy)
    p1_str = format_num(p1)
    p2_str = format_num(p2)
    p8_str = format_num(p8)
    plt8_str = format_num(plt8)
    p3_10_str = format_num(p3_10)
    p910_str = format_num(p910)
    p29_str = format_num(p29)
    wrong_p29_str = format_num(wrong_p29)
    p30_str = format_num(p30)
    p10_9_9_str = format_num(p10_9_9)
    p10_10_8_str = format_num(p10_10_8)
    p28_str = format_num(p28)
    wrong_p28_str = format_num(wrong_p28)
    wrong_p1_str = format_num(wrong_p1)
    wrong_p2_str = format_num(wrong_p2)

    # Hình vẽ bia ngắm bằng TikZ
    tikz_str = ''' \\begin{tikzpicture}[scale=0.35, line width=1pt]
    \\filldraw[fill=black] (0,0) circle (7);
    \\filldraw[fill=cyan!50] (0,0) circle (6.5);
    \\draw (0,0) circle (5.5);
    \\filldraw[fill=red!80] (0,0) circle (4.5);
    \\draw (0,0) circle (3.5);
    \\filldraw[fill=yellow!90] (0,0) circle (2.5);
    \\draw (0,0) circle (1.5);
    \\node at (0,0) {\\textbf{10}};
    \\node at (0,2) {\\textbf{9}}; \\node at (0,-2) {\\textbf{9}}; \\node at (2,0) {\\textbf{9}}; \\node at (-2,0) {\\textbf{9}};
    \\node at (0,3) {\\textbf{8}}; \\node at (0,-3) {\\textbf{8}}; \\node at (3,0) {\\textbf{8}}; \\node at (-3,0) {\\textbf{8}};
    \\node at (0,4) {\\textbf{7}}; \\node at (0,-4) {\\textbf{7}}; \\node at (4,0) {\\textbf{7}}; \\node at (-4,0) {\\textbf{7}};
    \\node at (0,5) {\\textbf{6}}; \\node at (0,-5) {\\textbf{6}}; \\node at (5,0) {\\textbf{6}}; \\node at (-5,0) {\\textbf{6}};
    \\node at (0,6) {\\textbf{5}}; \\node at (0,-6) {\\textbf{5}}; \\node at (6,0) {\\textbf{5}}; \\node at (-6,0) {\\textbf{5}};
    \\node[text=white] at (6.75,0) {\\textbf{L}}; \\node[text=white] at (-6.75,0) {\\textbf{L}};
    \\node[text=white] at (0,6.75) {\\textbf{L}}; \\node[text=white] at (0,-6.75) {\\textbf{L}};
    \\end{tikzpicture}'''

    # Nội dung câu hỏi
    noidungcauhoi = ('''\\immini{Một xạ thủ bắn bia, trên bia có các vòng tròn tính điểm (từ $5$ đến $10$) như hình vẽ. Mỗi lần bắn, xác suất xạ thủ đó bắn trúng vòng $8$ là $%s$; trúng vòng dưới $8$ (kể cả bắn trượt) là $%s$. Gọi $P_1$, $P_2$ lần lượt là xác suất xạ thủ đó bắn trúng vòng $10$ và vòng $9$ trong mỗi lần bắn. Biết rằng nếu xạ thủ đó bắn ba phát vào bia thì xác suất cả ba lần bắn trúng vòng $10$ là $%s$.} 
    {%s}''' % (p8_str, plt8_str, p3_10_str, tikz_str))

    ######################################################################## Nhận biết ############################################
    # Các đáp án
    nb_da_1_d = '\\True $P_1 = %s$' % (p1_str)
    nb_da_1_s = '$P_1 = %s$' % (wrong_p1_str)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]

    # Nội dung lời giải
    loigiai_nb_1 = ('''Ta có xác suất $3$ lần bắn trúng vòng $10$ là $P_1^3 = %s \\Rightarrow P_1 = \\sqrt[3]{%s} = %s$.''' % (p3_10_str, p3_10_str, p1_str))

    # Đưa các lời giải vào danh sách lời giải
    list_nb_2 = [loigiai_nb_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

    ######################################################################## Thông hiểu ############################################
    # Các đáp án
    th_da_1_d = '\\True $P_2 = %s$' % (p2_str)
    th_da_1_s = '$P_2 = %s$' % (wrong_p2_str)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]

    # Nội dung lời giải
    loigiai_th_1 = ('''Tổng xác suất các trường hợp điểm bắn là $1$. \\\\
    Xác suất bắn trúng vòng $9$ hoặc $10$ là: $1 - %s - %s = %s$. \\\\
    Do đó $P_1 + P_2 = %s \\Rightarrow P_2 = %s - P_1 = %s - %s = %s$.''' % (p8_str, plt8_str, p910_str, p910_str, p910_str, p910_str, p1_str, p2_str))

    # Đưa các lời giải vào danh sách lời giải
    list_th_2 = [loigiai_th_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

    ######################################################################## Vận dụng ############################################
    # Các đáp án
    vd_da_1_d = '\\True Nếu xạ thủ đó bắn ba phát thì xác suất đạt $29$ điểm là $%s$' % (p29_str)
    vd_da_1_s = 'Nếu xạ thủ đó bắn ba phát thì xác suất đạt $29$ điểm là $%s$' % (wrong_p29_str)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]

    # Nội dung lời giải
    loigiai_vd_1 = ('''Để đạt $29$ điểm trong $3$ phát bắn, xạ thủ phải bắn trúng hai phát vòng $10$ và một phát vòng $9$. Do có $3$ lượt bắn nên có $3$ cách đảo vị trí. \\\\
    Xác suất để xảy ra trường hợp này là $3 \\cdot P_1^2 \\cdot P_2 = 3 \\cdot (%s)^2 \\cdot %s = %s$.''' % (p1_str, p2_str, p29_str))

    # Đưa các lời giải vào danh sách lời giải
    list_vd_2 = [loigiai_vd_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

    ######################################################################## Vận dụng cao ############################################
    # Các đáp án
    vdc_da_1_d = '\\True Nếu xạ thủ đó bắn ba phát thì xác suất đạt ít nhất $28$ điểm là $%s$' % (p28_str)
    vdc_da_1_s = 'Nếu xạ thủ đó bắn ba phát thì xác suất đạt ít nhất $28$ điểm là $%s$' % (wrong_p28_str)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]

    # Nội dung lời giải
    loigiai_vdc_1 = ('''Các trường hợp đạt ít nhất $28$ điểm trong $3$ phát bắn gồm: \\\\
    - Đạt $30$ điểm ($3$ phát vòng $10$): Xác suất là $P_1^3 = (%s)^3 = %s$. \\\\
    - Đạt $29$ điểm ($2$ phát vòng $10$, $1$ phát vòng $9$): Xác suất là $3 \\cdot P_1^2 \\cdot P_2 = %s$. \\\\
    - Đạt $28$ điểm, gồm hai trường hợp: \\\\
    + $1$ phát vòng $10$, $2$ phát vòng $9$: Xác suất là $3 \\cdot P_1 \\cdot P_2^2 = 3 \\cdot %s \\cdot (%s)^2 = %s$. \\\\
    + $2$ phát vòng $10$, $1$ phát vòng $8$: Xác suất là $3 \\cdot P_1^2 \\cdot P_8 = 3 \\cdot (%s)^2 \\cdot %s = %s$. \\\\
    Xác suất đạt ít nhất $28$ điểm là: $%s + %s + %s + %s = %s$.''' % (p1_str, p30_str, p29_str, p1_str, p2_str, p10_9_9_str, p1_str, p8_str, p10_10_8_str, p30_str, p29_str, p10_9_9_str, p10_10_8_str, p28_str))

    # Đưa các lời giải vào danh sách lời giải
    list_vdc_2 = [loigiai_vdc_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))
    random.shuffle(combined_vdc)
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
        str(noidungcauhoi) + '\n' +
        '\\choiceTFn \n'
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
        '\\end{ex}\n\\end{minipage}\n\n')
    return content


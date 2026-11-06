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


def bt_dang19_p2_b2_c1_hh10(self):
    # Hàm định dạng số thực sang chuỗi có dấu phẩy cho số thập phân
    def fmt_num(val, decimals=1):
        s = f"{val:.{decimals}f}".replace('.', ',')
        if s.endswith(',0'):
            s = s[:-2]
        return s

    # Khai báo biến và tạo số ngẫu nhiên
    d = random.choice([20, 25, 30, 35, 40])        # Khoảng cách giữa 2 người (m)
    alpha = random.choice([25, 30, 35])            # Góc nhìn người A (độ)
    beta = random.choice([45, 50, 55])             # Góc nhìn người B (độ)

    # Tính toán các góc và độ dài
    angle_C = 180 - alpha - beta
    rad_alpha = math.radians(alpha)
    rad_beta = math.radians(beta)
    rad_C = math.radians(angle_C)

    # Khoảng cách AC (từ A đến nóc tòa nhà)
    AC_val = d * math.sin(rad_beta) / math.sin(rad_C)
    AC_str = fmt_num(AC_val, 1)

    # Chiều cao tòa nhà h = CH
    h_val = AC_val * math.sin(rad_alpha)
    h_str = fmt_num(h_val, 1)

    # Thông số xe cứu hỏa
    h_0 = 1.8
    h_0_str = fmt_num(h_0, 1)
    L_thang = 40

    # Khoảng cách xa nhất xe cứu hỏa đứng
    d_xe_val = math.sqrt(L_thang**2 - (h_val - h_0)**2)
    d_xe_str = fmt_num(d_xe_val, 1)

    # Các giá trị sai ngẫu nhiên phục vụ tạo phương án sai
    angle_C_sai = alpha
    AC_sai = fmt_num(AC_val * 1.88, 1)
    h_sai = fmt_num(d, 0)
    d_xe_sai = fmt_num(d_xe_val * 0.56, 1)

    # Nội dung câu hỏi
    noidungcauhoi = ('''Hai người dân đứng cách nhau $%sm$ cùng nhìn lên đỉnh của một tòa nhà theo góc nhìn lần lượt là $%s^\\circ$ và $%s^\\circ$.'''
                     % (d, alpha, beta))

    ########################################################################
    # Nhận biết ############################################
    # Các đáp án
    nb_da_1_d = '\\True Góc nhìn từ đỉnh tòa nhà về hai phía $A$ và $B$ nơi hai người dân đang đứng là góc $\\widehat{ACB}$ có số đo $%s^\\circ$' % (angle_C)
    nb_da_1_s = 'Góc nhìn từ đỉnh tòa nhà về hai phía $A$ và $B$ nơi hai người dân đang đứng là góc $\\widehat{ACB}$ có số đo $%s^\\circ$' % (angle_C_sai)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]

    # Nội dung lời giải
    loigiai_nb_1 = ('''Xét tam giác $ABC$, góc nhìn từ đỉnh tòa nhà về hai phía $A$ và $B$ là $\\widehat{ACB} = 180^\\circ - (%s^\\circ + %s^\\circ) = %s^\\circ$.'''
                    % (alpha, beta, angle_C))

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
    th_da_1_d = '\\True Khoảng cách từ vị trí người $A$ tới nóc của tòa nhà là $%sm$' % (AC_str)
    th_da_1_s = 'Khoảng cách từ vị trí người $A$ tới nóc của tòa nhà là $%sm$' % (AC_sai)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]

    # Nội dung lời giải
    loigiai_th_1 = ('''Áp dụng định lý sin trong tam giác $ABC$, ta có: \\\\
    $\\frac{AC}{\\sin \\widehat{B}} = \\frac{AB}{\\sin \\widehat{C}} \\Rightarrow AC = \\frac{AB \\cdot \\sin \\widehat{B}}{\\sin \\widehat{C}} = \\frac{%s \\cdot \\sin %s^\\circ}{\\sin %s^\\circ} \\approx %sm$.'''
                    % (d, beta, angle_C, AC_str))

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
    vd_da_1_d = '\\True Chiều cao của tòa nhà là khoảng $%sm$' % (h_str)
    vd_da_1_s = 'Chiều cao của tòa nhà là khoảng $%sm$' % (h_sai)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]

    # Nội dung lời giải
    loigiai_vd_1 = ('''Gọi $H$ là chân tòa nhà, tam giác $ACH$ vuông tại $H$. \\\\
    Chiều cao của tòa nhà là $CH = AC \\cdot \\sin \\widehat{A} \\approx %s \\cdot \\sin %s^\\circ \\approx %sm$.'''
                    % (AC_str, alpha, h_str))

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
    vdc_da_1_d = '\\True Vì gặp sự cố nên tầng trên cùng của tòa nhà đang bị cháy. Để cứu hộ đám cháy, một xe cứu hỏa đã tiếp cận dưới chân tòa nhà và chân thang đứng cách mặt đất $%sm$, chiều dài tối đa của thang xếp là $%sm$. Để tiếp cận được đám cháy thì xe cứu hỏa phải đứng cách chân tòa một khoảng xa nhất là $%sm$' % (h_0_str, L_thang, d_xe_str)
    vdc_da_1_s = 'Vì gặp sự cố nên tầng trên cùng của tòa nhà đang bị cháy. Để cứu hộ đám cháy, một xe cứu hỏa đã tiếp cận dưới chân tòa nhà và chân thang đứng cách mặt đất $%sm$, chiều dài tối đa của thang xếp là $%sm$. Để tiếp cận được đám cháy thì xe cứu hỏa phải đứng cách chân tòa một khoảng xa nhất là $%sm$' % (h_0_str, L_thang, d_xe_sai)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]

    # Nội dung lời giải
    loigiai_vdc_1 = ('''Chiều cao từ chân thang xếp đến đám cháy ở đỉnh tòa nhà là $%s - %s = %sm$. \\\\
    Khoảng cách xa nhất từ xe cứu hỏa đến chân tòa nhà để thang tiếp cận được đám cháy là: \\\\
    $d = \\sqrt{%s^2 - (%s - %s)^2} \\approx %sm$.'''
                     % (h_str, h_0_str, fmt_num(h_val - h_0, 1), L_thang, h_str, h_0_str, d_xe_str))

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


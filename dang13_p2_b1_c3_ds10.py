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


def bt_dang13_p2_b1_c3_ds10(self):
    # Khai báo biến
    # Danh sách các bộ số (x1, d1, x2, d2) đảm bảo tính toán đẹp ra số thập phân hữu hạn
    ds_bo_so = [
        (150, Decimal('0.6'), 80, Decimal('0.24')),
        (100, Decimal('0.4'), 50, Decimal('0.15')),
        (200, Decimal('0.8'), 120, Decimal('0.36')),
        (120, Decimal('0.6'), 60, Decimal('0.18')),
        (250, Decimal('1.0'), 100, Decimal('0.30')),
        (150, Decimal('0.45'), 80, Decimal('0.32')),
        (160, Decimal('0.8'), 90, Decimal('0.27'))
    ]
    x1, d1, x2, d2 = random.choice(ds_bo_so)
    
    dec_x1 = Decimal(str(x1))
    dec_x2 = Decimal(str(x2))
    
    # Tính sai số tương đối delta và phần trăm
    delta1 = d1 / dec_x1
    delta2 = d2 / dec_x2
    pct1 = delta1 * Decimal('100')
    pct2 = delta2 * Decimal('100')
    
    # Định dạng hiển thị dấu phẩy theo chuẩn Việt Nam
    str_x1 = str(x1)
    str_d1 = f"{d1}".replace('.', ',')
    str_delta1 = f"{delta1}".replace('.', ',')
    str_pct1 = f"{pct1}".replace('.', ',')
    
    str_x2 = str(x2)
    str_d2 = f"{d2}".replace('.', ',')
    str_delta2 = f"{delta2}".replace('.', ',')
    str_pct2 = f"{pct2}".replace('.', ',')
    
    # Giá trị gây nhiễu cho phần trăm
    str_pct1_sai = f"{pct1 * Decimal('2')}".replace('.', ',')
    str_pct2_sai = f"{pct2 * Decimal('2')}".replace('.', ',')
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Hai phương pháp đo cho kết quả $x_1 = %s \\pm %s, x_2 = %s \\pm %s$.'''
                     % (latex(x1), str_d1, latex(x2), str_d2)
                     )
    
    ######################################## Ý a ########################################
    # Ý a: Cận trên sai số tương đối của phương pháp thứ nhất
    a_da_d = '\\True Cận trên sai số tương đối của phương pháp thứ nhất là $%s\\%%$' % str_pct1
    a_da_s = 'Cận trên sai số tương đối của phương pháp thứ nhất là $%s\\%%$' % str_pct1_sai
    list_nb_da_1 = [a_da_d, a_da_s]
    
    loigiai_a_d = ('''Cận trên sai số tương đối của phương pháp thứ nhất là $\\delta_1 \\le \\frac{%s}{%s} = %s$, tức $%s\\%%$.'''
                   % (str_d1, latex(x1), str_delta1, str_pct1))
    loigiai_a_s = ('''Cận trên sai số tương đối của phương pháp thứ nhất là $\\delta_1 \\le \\frac{%s}{%s} = %s\\%%$, không phải $%s\\%%$.'''
                   % (str_d1, latex(x1), str_pct1, str_pct1_sai))
    list_a_lg = [loigiai_a_d, loigiai_a_s]
    
    ######################################## Ý b ########################################
    # Ý b: Cận trên sai số tương đối của phương pháp thứ hai
    b_da_d = '\\True Cận trên sai số tương đối của phương pháp thứ hai là $%s\\%%$' % str_pct2
    b_da_s = 'Cận trên sai số tương đối của phương pháp thứ hai là $%s\\%%$' % str_pct2_sai
    list_th_da_1 = [b_da_d, b_da_s]
    
    loigiai_b_d = ('''Cận trên sai số tương đối của phương pháp thứ hai là $\\delta_2 \\le \\frac{%s}{%s} = %s$, tức $%s\\%%$.'''
                   % (str_d2, latex(x2), str_delta2, str_pct2))
    loigiai_b_s = ('''Cận trên sai số tương đối của phương pháp thứ hai là $\\delta_2 \\le \\frac{%s}{%s} = %s\\%%$, không phải $%s\\%%$.'''
                   % (str_d2, latex(x2), str_pct2, str_pct2_sai))
    list_b_lg = [loigiai_b_d, loigiai_b_s]
    
    ######################################## Ý c ########################################
    # Ý c: Phương pháp nào chính xác hơn xét theo sai số tương đối
    if delta1 > delta2:
        c_da_d = '\\True Phương pháp thứ hai chính xác hơn xét theo sai số tương đối'
        c_da_s = 'Phương pháp thứ nhất chính xác hơn xét theo sai số tương đối'
        loigiai_c_d = ('''Vì $%s\\%% < %s\\%%$ nên phương pháp thứ hai có sai số tương đối nhỏ hơn, do đó chính xác hơn xét theo sai số tương đối.'''
                       % (str_pct2, str_pct1))
        loigiai_c_s = ('''Vì sai số tương đối của phương pháp thứ hai là $%s\\%%$ nhỏ hơn phương pháp thứ nhất là $%s\\%%$ nên phương pháp thứ hai mới là phương pháp chính xác hơn.'''
                       % (str_pct2, str_pct1))
    else:
        c_da_d = '\\True Phương pháp thứ nhất chính xác hơn xét theo sai số tương đối'
        c_da_s = 'Phương pháp thứ hai chính xác hơn xét theo sai số tương đối'
        loigiai_c_d = ('''Vì $%s\\%% < %s\\%%$ nên phương pháp thứ nhất có sai số tương đối nhỏ hơn, do đó chính xác hơn xét theo sai số tương đối.'''
                       % (str_pct1, str_pct2))
        loigiai_c_s = ('''Vì sai số tương đối của phương pháp thứ nhất là $%s\\%%$ nhỏ hơn phương pháp thứ hai là $%s\\%%$ nên phương pháp thứ nhất mới là phương pháp chính xác hơn.'''
                       % (str_pct1, str_pct2))
    
    list_vd_da_1 = [c_da_d, c_da_s]
    list_c_lg = [loigiai_c_d, loigiai_c_s]
    
    ######################################## Ý d ########################################
    # Ý d: So sánh theo sai số tuyệt đối khi hai đại lượng khác nhau (Sai)
    d_da_d = '\\True Không thể chỉ dựa vào so sánh $%s > %s$ để kết luận phương pháp thứ nhất chính xác hơn' % (str_d1, str_d2)
    d_da_s = 'Vì $%s > %s$ nên phương pháp thứ nhất chắc chắn chính xác hơn' % (str_d1, str_d2)
    list_vdc_da_1 = [d_da_s, d_da_d]
    
    loigiai_d_s = ('''Để so sánh độ chính xác của hai phép đo có quy mô giá trị đo khác nhau ($%s$ và $%s$), ta phải căn cứ vào sai số tương đối chứ không thể chỉ so sánh hai sai số tuyệt đối $%s$ và $%s$.'''
                   % (latex(x1), latex(x2), str_d1, str_d2))
    loigiai_d_d = ('''Để đánh giá độ chính xác của hai kết quả đo khác nhau, ta phải dùng sai số tương đối; sai số tuyệt đối không phản ánh được mức độ chính xác khi giá trị đo khác nhau.''' )
    list_d_lg = [loigiai_d_s, loigiai_d_d]
    
    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)
    
    # Lặp chọn để đảm bảo có từ 1 đến 3 khẳng định đúng
    while True:
        idx_a = random.choice([0, 1])
        idx_b = random.choice([0, 1])
        idx_c = random.choice([0, 1])
        idx_d = random.choice([0, 1])
    
        nb_da_1 = list_nb_da_1[idx_a]
        loigiai_nb_1 = list_a_lg[idx_a]
    
        th_da_1 = list_th_da_1[idx_b]
        loigiai_th_1 = list_b_lg[idx_b]
    
        vd_da_1 = list_vd_da_1[idx_c]
        loigiai_vd_1 = list_c_lg[idx_c]
    
        vdc_da_1 = list_vdc_da_1[idx_d]
        loigiai_vdc_1 = list_d_lg[idx_d]
    
        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        true_count = count_true_answers(answers)
        if 1 <= true_count <= 3:
            break
    
    # Gán vào danh sách
    shuffled_answers_nb = [nb_da_1]
    shuffled_solutions_nb = [loigiai_nb_1]
    
    shuffled_answers_th = [th_da_1]
    shuffled_solutions_th = [loigiai_th_1]
    
    shuffled_answers_vd = [vd_da_1]
    shuffled_solutions_vd = [loigiai_vd_1]
    
    shuffled_answers_vdc = [vdc_da_1]
    shuffled_solutions_vdc = [loigiai_vdc_1]
    
    # Xuất câu hỏi theo định dạng Đúng/Sai (choiceTF)
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
               '\\choiceTF \n'
               '{' + str(shuffled_answers_nb[0]) + '}\n'
               '{' + str(shuffled_answers_th[0]) + '}\n'
               '{' + str(shuffled_answers_vd[0]) + '}\n'
               '{' + str(shuffled_answers_vdc[0]) + '}\n'
               '\\loigiai{ \n'
               '\\begin{itemchoice} \n'
               '\\itemch ' + str(shuffled_solutions_nb[0]) + '\n'
               '\\itemch ' + str(shuffled_solutions_th[0]) + '\n'
               '\\itemch ' + str(shuffled_solutions_vd[0]) + '\n'
               '\\itemch ' + str(shuffled_solutions_vdc[0]) + '\n'
               '\\end{itemchoice}} \n'
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
    
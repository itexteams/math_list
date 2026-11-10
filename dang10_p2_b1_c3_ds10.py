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


def bt_dang10_p2_b1_c3_ds10(self):
    # Khai báo biến
    ds_bo_so = [
        (50, Decimal('0.5'), 200, Decimal('1')),
        (40, Decimal('0.4'), 160, Decimal('0.8')),
        (80, Decimal('0.8'), 240, Decimal('1.2')),
        (50, Decimal('0.25'), 100, Decimal('1')),
        (60, Decimal('0.6'), 300, Decimal('1.5')),
        (100, Decimal('1'), 400, Decimal('2')),
        (40, Decimal('0.2'), 200, Decimal('1'))
    ]
    a1, d1, a2, d2 = random.choice(ds_bo_so)
    
    dec_a1 = Decimal(str(a1))
    dec_a2 = Decimal(str(a2))
    
    # Tính sai số tương đối và phần trăm
    delta1 = d1 / dec_a1
    delta2 = d2 / dec_a2
    pct1 = delta1 * Decimal('100')
    pct2 = delta2 * Decimal('100')
    
    # Định dạng hiển thị dấu phẩy theo chuẩn Việt Nam
    str_a1 = str(a1)
    str_d1 = f"{d1}".replace('.', ',')
    str_pct1 = f"{pct1}".replace('.', ',')
    
    str_a2 = str(a2)
    str_d2 = f"{d2}".replace('.', ',')
    str_pct2 = f"{pct2}".replace('.', ',')
    
    # Giá trị sai số tương đối gây nhiễu
    str_pct1_sai = f"{pct1 * Decimal('2')}".replace('.', ',')
    str_pct2_sai = f"{pct2 * Decimal('2')}".replace('.', ',')
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Hai phép đo cho kết quả $a_1 = %s \\pm %s, a_2 = %s \\pm %s$.'''
                     % (latex(a1), str_d1, latex(a2), str_d2)
                     )
    
    ######################################## Ý a ########################################
    # Ý a: Cận trên sai số tương đối của phép đo thứ nhất
    a_da_d = '\\True Cận trên sai số tương đối của phép đo thứ nhất là $%s\\%%$' % str_pct1
    a_da_s = 'Cận trên sai số tương đối của phép đo thứ nhất là $%s\\%%$' % str_pct1_sai
    list_nb_da_1 = [a_da_d, a_da_s]
    
    loigiai_a_d = ('''Cận trên sai số tương đối của phép đo thứ nhất là $\\delta_1 \\le \\frac{%s}{%s} = %s\\%%$.'''
                   % (str_d1, latex(a1), str_pct1))
    loigiai_a_s = ('''Cận trên sai số tương đối của phép đo thứ nhất là $\\delta_1 \\le \\frac{%s}{%s} = %s\\%%$, không phải $%s\\%%$.'''
                   % (str_d1, latex(a1), str_pct1, str_pct1_sai))
    list_a_lg = [loigiai_a_d, loigiai_a_s]
    
    ######################################## Ý b ########################################
    # Ý b: Cận trên sai số tương đối của phép đo thứ hai
    b_da_d = '\\True Cận trên sai số tương đối của phép đo thứ hai là $%s\\%%$' % str_pct2
    b_da_s = 'Cận trên sai số tương đối của phép đo thứ hai là $%s\\%%$' % str_pct2_sai
    list_th_da_1 = [b_da_d, b_da_s]
    
    loigiai_b_d = ('''Cận trên sai số tương đối của phép đo thứ hai là $\\delta_2 \\le \\frac{%s}{%s} = %s\\%%$.'''
                   % (str_d2, latex(a2), str_pct2))
    loigiai_b_s = ('''Cận trên sai số tương đối của phép đo thứ hai là $\\delta_2 \\le \\frac{%s}{%s} = %s\\%%$, không phải $%s\\%%$.'''
                   % (str_d2, latex(a2), str_pct2, str_pct2_sai))
    list_b_lg = [loigiai_b_d, loigiai_b_s]
    
    ######################################## Ý c ########################################
    # Ý c: So sánh độ chính xác theo sai số tương đối (câu gốc: phép đo thứ nhất chính xác hơn là Sai)
    if delta1 > delta2:
        c_da_d = '\\True Phép đo thứ hai chính xác hơn xét theo sai số tương đối'
        c_da_s = 'Phép đo thứ nhất chính xác hơn xét theo sai số tương đối'
        loigiai_c_s = ('''Vì $\\delta_1 \\le %s\\%%$ và $\\delta_2 \\le %s\\%%$, do $%s\\%% < %s\\%%$ nên phép đo thứ hai chính xác hơn xét theo sai số tương đối.'''
                       % (str_pct1, str_pct2, str_pct2, str_pct1))
        loigiai_c_d = ('''Vì $%s\\%% < %s\\%%$ nên phép đo thứ hai có sai số tương đối nhỏ hơn, tức là cho kết quả chính xác hơn.'''
                       % (str_pct2, str_pct1))
    else:
        c_da_d = '\\True Phép đo thứ nhất chính xác hơn xét theo sai số tương đối'
        c_da_s = 'Phép đo thứ hai chính xác hơn xét theo sai số tương đối'
        loigiai_c_s = ('''Vì $\\delta_1 \\le %s\\%%$ và $\\delta_2 \\le %s\\%%$, do $%s\\%% < %s\\%%$ nên phép đo thứ nhất chính xác hơn xét theo sai số tương đối.'''
                       % (str_pct1, str_pct2, str_pct1, str_pct2))
        loigiai_c_d = ('''Vì $%s\\%% < %s\\%%$ nên phép đo thứ nhất có sai số tương đối nhỏ hơn, tức là cho kết quả chính xác hơn.'''
                       % (str_pct1, str_pct2))
    
    list_vd_da_1 = [c_da_s, c_da_d]
    list_c_lg = [loigiai_c_s, loigiai_c_d]
    
    ######################################## Ý d ########################################
    # Ý d: Sai số tuyệt đối của phép đo thứ hai lớn hơn phép đo thứ nhất (d2 > d1: Đúng)
    if d2 > d1:
        d_da_d = '\\True Độ chính xác (sai số tuyệt đối cận trên) của phép đo thứ hai lớn hơn phép đo thứ nhất'
        d_da_s = 'Độ chính xác (sai số tuyệt đối cận trên) của phép đo thứ hai nhỏ hơn phép đo thứ nhất'
        loigiai_d_d = ('''Sai số tuyệt đối của phép đo thứ hai có cận trên là $d_2 = %s$, còn phép đo thứ nhất có cận trên là $d_1 = %s$. Vì $%s > %s$ nên sai số tuyệt đối của phép đo thứ hai lớn hơn.'''
                       % (str_d2, str_d1, str_d2, str_d1))
        loigiai_d_s = ('''Vì $d_2 = %s > %s = d_1$ nên sai số tuyệt đối của phép đo thứ hai lớn hơn chứ không nhỏ hơn.'''
                       % (str_d2, str_d1))
    else:
        d_da_d = '\\True Độ chính xác (sai số tuyệt đối cận trên) của phép đo thứ hai nhỏ hơn phép đo thứ nhất'
        d_da_s = 'Độ chính xác (sai số tuyệt đối cận trên) của phép đo thứ hai lớn hơn phép đo thứ nhất'
        loigiai_d_d = ('''Sai số tuyệt đối của phép đo thứ hai có cận trên là $d_2 = %s$, còn phép đo thứ nhất có cận trên là $d_1 = %s$. Vì $%s < %s$ nên sai số tuyệt đối của phép đo thứ hai nhỏ hơn.'''
                       % (str_d2, str_d1, str_d2, str_d1))
        loigiai_d_s = ('''Vì $d_2 = %s < %s = d_1$ nên sai số tuyệt đối của phép đo thứ hai nhỏ hơn chứ không lớn hơn.'''
                       % (str_d2, str_d1))
    
    list_vdc_da_1 = [d_da_d, d_da_s]
    list_d_lg = [loigiai_d_d, loigiai_d_s]
    
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
    
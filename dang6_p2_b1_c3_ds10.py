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


def bt_dang6_p2_b1_c3_ds10(self):
    # Khai báo biến
    ds_so = [2, 3, 5, 6, 7, 8, 10, 11]
    n = random.choice(ds_so)
    
    val_sqrt = math.sqrt(n)
    dec_full = Decimal(str(val_sqrt))
    
    # Lấy biểu diễn xấp xỉ 5 chữ số thập phân trên máy tính
    str_5cs = f"{val_sqrt:.5f}"
    val_5cs_vn = str_5cs.replace('.', ',')
    
    # Làm tròn đến hàng phần trăm (2 chữ số thập phân)
    dec_phantram = dec_full.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    val_phantram_d = f"{dec_phantram:.2f}".replace('.', ',')
    # Giá trị sai cho hàng phần trăm
    val_phantram_s = f"{dec_phantram + Decimal('0.01'):.2f}".replace('.', ',')
    
    # Làm tròn đến hàng phần nghìn (3 chữ số thập phân)
    dec_phannghin = dec_full.quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)
    val_phannghin_d = f"{dec_phannghin:.3f}".replace('.', ',')
    # Giá trị sai cho hàng phần nghìn
    val_phannghin_s = f"{dec_phannghin + Decimal('0.001'):.3f}".replace('.', ',')
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Dùng máy tính với $\\sqrt{%s} \\approx %s$.'''
                     % (latex(n), val_5cs_vn)
                     )
    
    ######################################## Ý a ########################################
    # Làm tròn đến hàng phần trăm
    a_da_d = '\\True Làm tròn đến hàng phần trăm được $%s$' % val_phantram_d
    a_da_s = 'Làm tròn đến hàng phần trăm được $%s$' % val_phantram_s
    list_nb_da_1 = [a_da_d, a_da_s]
    
    loigiai_a_d = ('''Làm tròn $\\sqrt{%s} \\approx %s$ đến hàng phần trăm ta được $%s$.''' % (latex(n), val_5cs_vn, val_phantram_d))
    loigiai_a_s = ('''Làm tròn $\\sqrt{%s} \\approx %s$ đến hàng phần trăm phải được $%s$, không phải $%s$.''' % (latex(n), val_5cs_vn, val_phantram_d, val_phantram_s))
    list_a_lg = [loigiai_a_d, loigiai_a_s]
    
    ######################################## Ý b ########################################
    # Làm tròn đến hàng phần nghìn
    b_da_d = '\\True Làm tròn đến hàng phần nghìn được $%s$' % val_phannghin_d
    b_da_s = 'Làm tròn đến hàng phần nghìn được $%s$' % val_phannghin_s
    list_th_da_1 = [b_da_d, b_da_s]
    
    loigiai_b_d = ('''Làm tròn $\\sqrt{%s} \\approx %s$ đến hàng phần nghìn ta được $%s$.''' % (latex(n), val_5cs_vn, val_phannghin_d))
    loigiai_b_s = ('''Làm tròn $\\sqrt{%s} \\approx %s$ đến hàng phần nghìn phải được $%s$, không phải $%s$.''' % (latex(n), val_5cs_vn, val_phannghin_d, val_phannghin_s))
    list_b_lg = [loigiai_b_d, loigiai_b_s]
    
    ######################################## Ý c ########################################
    # Số hiển thị chỉ là giá trị gần đúng, không phải giá trị đúng (Mặc định câu gốc là Sai)
    c_da_d = '\\True Số $%s$ chỉ là một giá trị gần đúng của $\\sqrt{%s}$' % (val_5cs_vn, latex(n))
    c_da_s = 'Số $%s$ chắc chắn là giá trị đúng của $\\sqrt{%s}$' % (val_5cs_vn, latex(n))
    list_vd_da_1 = [c_da_s, c_da_d]
    
    loigiai_c_s = ('''Số $\\sqrt{%s}$ là số vô tỉ nên số thập phân $%s$ trên máy tính chỉ là một giá trị gần đúng, không phải là giá trị đúng.''' % (latex(n), val_5cs_vn))
    loigiai_c_d = ('''Số $\\sqrt{%s}$ là số vô tỉ, do đó kết quả $%s$ hiển thị trên máy tính chỉ là giá trị gần đúng.''' % (latex(n), val_5cs_vn))
    list_c_lg = [loigiai_c_s, loigiai_c_d]
    
    ######################################## Ý d ########################################
    # Số đã làm tròn là một số gần đúng của căn (Mặc định câu gốc là Đúng)
    d_da_d = '\\True Số $%s$ là một số gần đúng của $\\sqrt{%s}$' % (val_phantram_d, latex(n))
    d_da_s = 'Số $%s$ là giá trị đúng của $\\sqrt{%s}$' % (val_phantram_d, latex(n))
    list_vdc_da_1 = [d_da_d, d_da_s]
    
    loigiai_d_d = ('''Số $%s$ nhận được do làm tròn nên nó là một số gần đúng của $\\sqrt{%s}$.''' % (val_phantram_d, latex(n)))
    loigiai_d_s = ('''Số $%s$ chỉ là số gần đúng của $\\sqrt{%s}$, không phải là giá trị đúng.''' % (val_phantram_d, latex(n)))
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
    
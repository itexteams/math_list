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


def bt_dang11_p2_b1_c3_ds10(self):
    # Khai báo biến
    # Tạo số gần đúng có 5 chữ số với hàng chục d thuộc khoảng (10; 100] => làm tròn đến hàng trăm
    hang_nghin = random.randint(30, 85) # Ví dụ 58xxx
    hang_tram = random.randint(1, 9)    # Ví dụ 2
    hang_chuc = random.randint(1, 8)    # Ví dụ 4
    hang_don_vi = random.randint(1, 9)  # Ví dụ 1
    
    a = hang_nghin * 1000 + hang_tram * 100 + hang_chuc * 10 + hang_don_vi
    d = random.choice([30, 40, 50, 60, 70])
    
    # Làm tròn đến hàng trăm (quy tròn thích hợp vì 10 < d <= 100)
    dec_a = Decimal(str(a))
    so_quy_tron_tram = int(dec_a.quantize(Decimal('100'), rounding=ROUND_HALF_UP))
    so_quy_tron_chuc = int(dec_a.quantize(Decimal('10'), rounding=ROUND_HALF_UP))
    
    # Giá trị sai cho câu b
    so_quy_tron_tram_sai = so_quy_tron_tram + 100 if hang_chuc < 5 else so_quy_tron_tram - 100
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Cho số gần đúng $a = %s, d = %s$.'''
                     % (latex(a), latex(d))
                     )
    
    ######################################## Ý a ########################################
    # Ý a: Theo quy tắc của bài học, nên làm tròn a đến hàng trăm
    a_da_d = '\\True Theo quy tắc của bài học, nên làm tròn $a$ đến hàng trăm'
    a_da_s = 'Theo quy tắc của bài học, nên làm tròn $a$ đến hàng chục'
    list_nb_da_1 = [a_da_d, a_da_s]
    
    loigiai_a_d = ('''Vì độ chính xác $d = %s$ ở hàng chục ($10 < %s \\le 100$) nên theo quy tắc của bài học, ta làm tròn số gần đúng $a$ đến hàng trăm.'''
                   % (latex(d), latex(d)))
    loigiai_a_s = ('''Vì độ chính xác $d = %s$ ở hàng chục nên theo quy tắc ta phải làm tròn đến hàng trăm, không phải hàng chục.'''
                   % (latex(d)))
    list_a_lg = [loigiai_a_d, loigiai_a_s]
    
    ######################################## Ý b ########################################
    # Ý b: Số quy tròn thích hợp là ...
    b_da_d = '\\True Số quy tròn thích hợp là $%s$' % latex(so_quy_tron_tram)
    b_da_s = 'Số quy tròn thích hợp là $%s$' % latex(so_quy_tron_tram_sai)
    list_th_da_1 = [b_da_d, b_da_s]
    
    loigiai_b_d = ('''Làm tròn số $%s$ đến hàng trăm ta xét chữ số hàng chục là $%s$, do đó số quy tròn là $%s$.'''
                   % (latex(a), latex(hang_chuc), latex(so_quy_tron_tram)))
    loigiai_b_s = ('''Làm tròn $%s$ đến hàng trăm ta được số quy tròn là $%s$, không phải $%s$.'''
                   % (latex(a), latex(so_quy_tron_tram), latex(so_quy_tron_tram_sai)))
    list_b_lg = [loigiai_b_d, loigiai_b_s]
    
    ######################################## Ý c ########################################
    # Ý c: Làm tròn đến hàng chục được ...
    c_da_d = '\\True Làm tròn đến hàng chục được $%s$' % latex(so_quy_tron_chuc)
    c_da_s = 'Làm tròn đến hàng chục được $%s$' % latex(so_quy_tron_chuc + 10)
    list_vd_da_1 = [c_da_d, c_da_s]
    
    loigiai_c_d = ('''Chữ số ở hàng đơn vị là $%s$, nên khi làm tròn số $%s$ đến hàng chục ta được $%s$.'''
                   % (latex(hang_don_vi), latex(a), latex(so_quy_tron_chuc)))
    loigiai_c_s = ('''Khi làm tròn số $%s$ đến hàng chục ta được $%s$.'''
                   % (latex(a), latex(so_quy_tron_chuc)))
    list_c_lg = [loigiai_c_d, loigiai_c_s]
    
    ######################################## Ý d ########################################
    # Ý d: Theo độ chính xác đã cho, bắt buộc phải giữ nguyên tất cả chữ số của ... (Sai)
    d_da_d = '\\True Theo độ chính xác đã cho, không bắt buộc phải giữ nguyên tất cả chữ số của $%s$' % latex(a)
    d_da_s = 'Theo độ chính xác đã cho, bắt buộc phải giữ nguyên tất cả chữ số của $%s$' % latex(a)
    list_vdc_da_1 = [d_da_s, d_da_d]
    
    loigiai_d_s = ('''Vì độ chính xác là $d = %s$ nên các chữ số ở hàng đơn vị và hàng chục không còn đáng tin cậy hoàn toàn, ta nên làm tròn số đến hàng trăm chứ không bắt buộc phải giữ lại tất cả các chữ số.'''
                   % (latex(d)))
    loigiai_d_d = ('''Độ chính xác $d = %s$ cho phép quy tròn số đến hàng trăm để số liệu gọn gàng và phù hợp với độ tin cậy của phép đo.'''
                   % (latex(d)))
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
    
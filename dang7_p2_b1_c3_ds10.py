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


def bt_dang7_p2_b1_c3_ds10(self):
    # Khai báo biến
    phan_nguyen = random.randint(30, 85)
    phan_thap_phan = random.randint(1, 9)
    dec_a = Decimal(str(phan_nguyen)) + Decimal(str(phan_thap_phan)) / Decimal('10')
    
    # Chọn độ chính xác d có 1 chữ số thập phân
    dec_d = Decimal(str(random.choice([1, 2, 3, 4, 5]))) / Decimal('10')
    
    # Đầu mút của đoạn số đúng
    dec_trai = dec_a - dec_d
    dec_phai = dec_a + dec_d
    
    # Định dạng hiển thị dấu phẩy theo chuẩn Việt Nam
    str_a = f"{dec_a:.1f}".replace('.', ',')
    str_d = f"{dec_d:.1f}".replace('.', ',')
    str_trai = f"{dec_trai:.1f}".replace('.', ',')
    str_phai = f"{dec_phai:.1f}".replace('.', ',')
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Cho số gần đúng $a = %s \\pm %s$.'''
                     % (str_a, str_d)
                     )
    
    ######################################## Ý a ########################################
    # Ý a: Có thể lấy độ chính xác d
    a_da_d = '\\True Có thể lấy độ chính xác $d = %s$' % str_d
    a_da_s = 'Có thể lấy độ chính xác $d = %s$' % f"{dec_d + Decimal('0.1'):.1f}".replace('.', ',')
    list_nb_da_1 = [a_da_d, a_da_s]
    
    loigiai_a_d = ('''Kí hiệu $a = %s \\pm %s$ cho biết độ chính xác có thể lấy là $d = %s$.''' % (str_a, str_d, str_d))
    loigiai_a_s = ('''Từ kí hiệu $a = %s \\pm %s$, độ chính xác phải là $d = %s$.''' % (str_a, str_d, str_d))
    list_a_lg = [loigiai_a_d, loigiai_a_s]
    
    ######################################## Ý b ########################################
    # Ý b: Số đúng thuộc đoạn [a - d; a + d]
    b_da_d = '\\True Số đúng thuộc đoạn $[%s; %s]$' % (str_trai, str_phai)
    b_da_s = 'Số đúng thuộc đoạn $[%s; %s]$' % (str_a, str_phai)
    list_th_da_1 = [b_da_d, b_da_s]
    
    loigiai_b_d = ('''Số đúng $\\overline{a}$ thỏa mãn $|\\overline{a} - %s| \\le %s \\Leftrightarrow %s - %s \\le \\overline{a} \\le %s + %s \\Leftrightarrow %s \\le \\overline{a} \\le %s$. Do đó số đúng thuộc đoạn $[%s; %s]$.'''
                   % (str_a, str_d, str_a, str_d, str_a, str_d, str_trai, str_phai, str_trai, str_phai))
    loigiai_b_s = ('''Số đúng thuộc đoạn $[%s - %s; %s + %s] = [%s; %s]$, không phải đoạn $[%s; %s]$.'''
                   % (str_a, str_d, str_a, str_d, str_trai, str_phai, str_a, str_phai))
    list_b_lg = [loigiai_b_d, loigiai_b_s]
    
    ######################################## Ý c ########################################
    # Ý c: Sai số tuyệt đối chắc chắn bằng đúng d (Sai)
    c_da_d = '\\True Sai số tuyệt đối không nhất thiết phải bằng đúng $%s$' % str_d
    c_da_s = 'Sai số tuyệt đối chắc chắn bằng đúng $%s$' % str_d
    list_vd_da_1 = [c_da_s, c_da_d]
    
    loigiai_c_s = ('''Độ chính xác $d = %s$ là cận trên của sai số tuyệt đối (tức $\\Delta_a \\le %s$), không thể khẳng định sai số tuyệt đối chắc chắn bằng đúng $%s$.''' % (str_d, str_d, str_d))
    loigiai_c_d = ('''Sai số tuyệt đối thỏa mãn $\\Delta_a \\le %s$ chứ không bắt buộc phải bằng $%s$.''' % (str_d, str_d))
    list_c_lg = [loigiai_c_s, loigiai_c_d]
    
    ######################################## Ý d ########################################
    # Ý d: Sai số tuyệt đối không vượt quá d (Đúng)
    d_da_d = '\\True Sai số tuyệt đối không vượt quá $%s$' % str_d
    d_da_s = 'Sai số tuyệt đối lớn hơn $%s$' % str_d
    list_vdc_da_1 = [d_da_d, d_da_s]
    
    loigiai_d_d = ('''Theo định nghĩa độ chính xác, sai số tuyệt đối thỏa mãn $\\Delta_a \\le d = %s$, tức là không vượt quá $%s$.''' % (str_d, str_d))
    loigiai_d_s = ('''Sai số tuyệt đối phải thỏa mãn $\\Delta_a \\le %s$, nên không thể lớn hơn $%s$.''' % (str_d, str_d))
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
    
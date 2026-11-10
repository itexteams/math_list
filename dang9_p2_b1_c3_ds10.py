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


def bt_dang9_p2_b1_c3_ds10(self):
    # Khai báo biến
    ds_bo_so = [
        (400, 2),
        (500, 2),
        (200, 1),
        (250, 1),
        (500, 1),
        (800, 2),
        (400, 1),
        (250, 2)
    ]
    a, d = random.choice(ds_bo_so)
    
    dec_a = Decimal(str(a))
    dec_d = Decimal(str(d))
    val_tp = dec_d / dec_a
    val_pct = val_tp * Decimal('100')
    
    # Định dạng số thập phân dùng dấu phẩy
    str_tp = f"{val_tp}".replace('.', ',')
    str_pct = f"{val_pct}".replace('.', ',')
    str_pct_nham = f"{val_pct * Decimal('10')}".replace('.', ',')
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Cho số gần đúng $a = %s, \\Delta_a \\le %s$.'''
                     % (latex(a), latex(d))
                     )
    
    ######################################## Ý a ########################################
    # Ý a: Sai số tương đối không vượt quá ...
    a_da_d = '\\True Sai số tương đối không vượt quá $%s\\%%$' % str_pct
    a_da_s = 'Sai số tương đối có thể vượt quá $%s\\%%$' % str_pct
    list_nb_da_1 = [a_da_d, a_da_s]
    
    loigiai_a_d = ('''Ta có $\\delta_a = \\frac{\\Delta_a}{|a|} \\le \\frac{%s}{%s} = %s = %s\\%%$. Vậy sai số tương đối không vượt quá $%s\\%%$.'''
                   % (latex(d), latex(a), str_tp, str_pct, str_pct))
    loigiai_a_s = ('''Vì $\\delta_a \\le \\frac{%s}{%s} = %s\\%%$ nên sai số tương đối không thể vượt quá $%s\\%%$.'''
                   % (latex(d), latex(a), str_pct, str_pct))
    list_a_lg = [loigiai_a_d, loigiai_a_s]
    
    ######################################## Ý b ########################################
    # Ý b: Nếu sai số tuyệt đối thực tế bằng d thì sai số tương đối bằng ...
    b_da_d = '\\True Nếu sai số tuyệt đối thực tế bằng $%s$ thì sai số tương đối bằng $%s\\%%$' % (latex(d), str_pct)
    b_da_s = 'Nếu sai số tuyệt đối thực tế bằng $%s$ thì sai số tương đối bằng $%s\\%%$' % (latex(d), str_pct_nham)
    list_th_da_1 = [b_da_d, b_da_s]
    
    loigiai_b_d = ('''Khi $\\Delta_a = %s$, sai số tương đối là $\\delta_a = \\frac{%s}{%s} = %s\\%%$.'''
                   % (latex(d), latex(d), latex(a), str_pct))
    loigiai_b_s = ('''Khi $\\Delta_a = %s$, sai số tương đối là $\\delta_a = \\frac{%s}{%s} = %s\\%%$, không phải $%s\\%%$.'''
                   % (latex(d), latex(d), latex(a), str_pct, str_pct_nham))
    list_b_lg = [loigiai_b_d, loigiai_b_s]
    
    ######################################## Ý c ########################################
    # Ý c: Sai số tương đối luôn bằng ... (Sai) / không nhất thiết luôn bằng ... (Đúng)
    c_da_d = '\\True Sai số tương đối thực tế có thể nhỏ hơn $%s\\%%$' % str_pct
    c_da_s = 'Sai số tương đối chắc chắn luôn bằng $%s\\%%$' % str_pct
    list_vd_da_1 = [c_da_s, c_da_d]
    
    loigiai_c_s = ('''Do $\\Delta_a \\le %s$ nên sai số tuyệt đối thực tế có thể nhận giá trị nhỏ hơn $%s$, dẫn đến sai số tương đối không nhất thiết luôn bằng $%s\\%%$.'''
                   % (latex(d), latex(d), str_pct))
    loigiai_c_d = ('''Do $\\Delta_a \\le %s$ nên sai số tương đối thỏa mãn $\\delta_a \\le %s\\%%$, nghĩa là nó hoàn toàn có thể nhận giá trị nhỏ hơn $%s\\%%$.'''
                   % (latex(d), str_pct, str_pct))
    list_c_lg = [loigiai_c_s, loigiai_c_d]
    
    ######################################## Ý d ########################################
    # Ý d: Với cùng sai số tuyệt đối d, nếu số gần đúng lớn hơn a thì cận trên sai số tương đối sẽ nhỏ hơn
    d_da_d = '\\True Với cùng sai số tuyệt đối $%s$, nếu số gần đúng lớn hơn $%s$ thì cận trên của sai số tương đối sẽ nhỏ hơn' % (latex(d), latex(a))
    d_da_s = 'Với cùng sai số tuyệt đối $%s$, nếu số gần đúng lớn hơn $%s$ thì cận trên của sai số tương đối sẽ lớn hơn' % (latex(d), latex(a))
    list_vdc_da_1 = [d_da_d, d_da_s]
    
    loigiai_d_d = ('''Cận trên của sai số tương đối là $\\frac{%s}{|a|}$. Khi $|a|$ lớn hơn và tử số $%s$ giữ nguyên thì phân số có giá trị nhỏ hơn.'''
                   % (latex(d), latex(d)))
    loigiai_d_s = ('''Vì cận trên của sai số tương đối có dạng $\\frac{%s}{|a|}$, khi mẫu số $|a| > %s$ tăng lên thì phân số phải giảm đi, tức là nhỏ hơn chứ không thể lớn hơn.'''
                   % (latex(d), latex(a)))
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
    
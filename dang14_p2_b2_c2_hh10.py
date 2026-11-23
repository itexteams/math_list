
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


def bt_dang14_p2_b2_c2_hh10(self):
    k = random.randint(1, 6)
    canh = 'a' if k == 1 else '%sa' % k
    canh_bp = 'a^2' if k == 1 else '(%sa)^2' % k
    canh2_bp = '(2a)^2' if k == 1 else '(%sa)^2' % (2 * k)
    kq_2bp = '2a^2' if k == 1 else '%sa^2' % (2 * k ** 2)
    kq_5bp = '5a^2' if k == 1 else '%sa^2' % (5 * k ** 2)
    ac_val = 'a\\sqrt{2}' if k == 1 else '%sa\\sqrt{2}' % k
    ae_val = 'a\\sqrt{5}' if k == 1 else '%sa\\sqrt{5}' % k
    a3_val = 'a\\sqrt{3}' if k == 1 else '%sa\\sqrt{3}' % k
    a2_val = '2a' if k == 1 else '%sa' % (2 * k)
    ten_hv, A, B, C, D = random.choice([('ABCD', 'A', 'B', 'C', 'D'), ('ABCD', 'B', 'C', 'D', 'A'), ('ABCD', 'C', 'D', 'A', 'B'), ('ABCD', 'D', 'A', 'B', 'C'), ('MNPQ', 'M', 'N', 'P', 'Q'), ('MNPQ', 'N', 'P', 'Q', 'M')])
    E = random.choice(['E', 'I', 'K'])
    noidungcauhoi = 'Cho hình vuông $%s$ có cạnh bằng $%s$. Xét tính đúng sai của các khẳng định sau:' % (ten_hv, canh)
    nb_s_vec = random.choice([C + A, B + D, D + B])
    nb_da_1_d = '\\True $\\overrightarrow{%s%s} + \\overrightarrow{%s%s} = \\overrightarrow{%s%s}$' % (A, D, A, B, A, C)
    nb_da_1_s = '$\\overrightarrow{%s%s} + \\overrightarrow{%s%s} = \\overrightarrow{%s}$' % (A, D, A, B, nb_s_vec)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    list_nb_1 = [nb_da_1]
    loigiai_nb_1 = 'Theo quy tắc hình bình hành ta có $\\overrightarrow{%s%s} + \\overrightarrow{%s%s} = \\overrightarrow{%s%s}$.' % (A, D, A, B, A, C)
    list_nb_2 = [loigiai_nb_1]
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    hinh_sai = random.choice(['hình thang', 'hình thang vuông', 'hình chữ nhật', 'hình thoi'])
    th_da_1_d = '\\True Gọi $%s$ là điểm đối xứng với $%s$ qua $%s$. Khi đó $%s%s%s%s$ là hình bình hành.' % (E, B, C, A, D, E, C)
    th_da_1_s = 'Gọi $%s$ là điểm đối xứng với $%s$ qua $%s$. Khi đó $%s%s%s%s$ là %s.' % (E, B, C, A, D, E, C, hinh_sai)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    list_th_1 = [th_da_1]
    loigiai_th_1 = 'Gọi $%s$ là điểm đối xứng với $%s$ qua $%s$. Do $%s%s = %s%s = %s$, $%s%s \\parallel %s%s$ nên $%s%s%s%s$ là hình bình hành.' % (E, B, C, C, E, A, D, canh, C, E, A, D, A, D, E, C)
    list_th_2 = [loigiai_th_1]
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    vd_s_val = random.choice([a3_val, a2_val, ae_val])
    vd_da_1_d = '\\True $\\left|\\overrightarrow{%s%s} + \\overrightarrow{%s%s}\\right| = %s$' % (A, D, A, B, ac_val)
    vd_da_1_s = '$\\left|\\overrightarrow{%s%s} + \\overrightarrow{%s%s}\\right| = %s$' % (A, D, A, B, vd_s_val)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    list_vd_1 = [vd_da_1]
    loigiai_vd_1 = 'Theo định lí Pytago: $%s%s^2 = %s%s^2 + %s%s^2 = %s + %s = %s \\Rightarrow %s%s = %s$. Vậy $\\left|\\overrightarrow{%s%s} + \\overrightarrow{%s%s}\\right| = \\left|\\overrightarrow{%s%s}\\right| = %s%s = %s$.' % (A, C, A, B, B, C, canh_bp, canh_bp, kq_2bp, A, C, ac_val, A, D, A, B, A, C, A, C, ac_val)
    list_vd_2 = [loigiai_vd_1]
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    vdc_s_val = random.choice([a3_val, ac_val, a2_val])
    vdc_da_1_d = '\\True $\\left|\\overrightarrow{%s%s} + \\overrightarrow{%s%s}\\right| = %s$.' % (A, D, A, C, ae_val)
    vdc_da_1_s = '$\\left|\\overrightarrow{%s%s} + \\overrightarrow{%s%s}\\right| = %s$.' % (A, D, A, C, vdc_s_val)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    list_vdc_1 = [vdc_da_1]
    loigiai_vdc_1 = 'Ta có $\\overrightarrow{%s%s} + \\overrightarrow{%s%s} = \\overrightarrow{%s%s}$. Áp dụng định lí Pytago cho tam giác $%s%s%s$: $%s%s^2 = %s%s^2 + %s%s^2 = %s + %s = %s \\Rightarrow %s%s = %s$. Vậy $\\left|\\overrightarrow{%s%s} + \\overrightarrow{%s%s}\\right| = %s%s = %s$.' % (A, D, A, C, A, E, A, B, E, A, E, A, B, B, E, canh_bp, canh2_bp, kq_5bp, A, E, ae_val, A, D, A, C, A, E, ae_val)
    list_vdc_2 = [loigiai_vdc_1]
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))
    random.shuffle(combined_vdc)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)
    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)
    while True:
        nb_da_1 = random.choice(list_nb_da_1)
        th_da_1 = random.choice(list_th_da_1)
        vd_da_1 = random.choice(list_vd_da_1)
        vdc_da_1 = random.choice(list_vdc_da_1)
        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        true_count = count_true_answers(answers)
        if 1 <= true_count <= 3:
            break
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
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
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
        '\\end{ex}\n \\end{minipage}\n\n')
    return content


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


def bt_dang17_p2_b2_c2_hh10(self):
    bo_dinh = random.choice([('A', 'B', 'C', 'I', 'J', 'P', 'Q', 'R', 'S'), ('M', 'N', 'P', 'A', 'B', 'C', 'D', 'E', 'F'), ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'K'), ('D', 'E', 'F', 'A', 'B', 'G', 'H', 'X', 'Y')])
    A, B, C, I, J, P, Q, R, S = bo_dinh
    noidungcauhoi = 'Cho tam giác $%s%s%s$. Bên ngoài của tam giác vẽ các hình bình hành $%s%s%s%s, %s%s%s%s, %s%s%s%s$. Xét tính đúng sai của các khẳng định sau:' % (A, B, C, A, B, I, J, B, C, P, Q, C, A, R, S)
    chieu = random.choice([1, 2])
    if chieu == 1:
        v1, a1, b1, c1 = R + J, R + A, A + J, S + C
        v2, a2, b2, c2 = I + Q, I + B, B + Q, C + P
        v3, a3, b3, c3 = P + S, P + C, C + S, B + I
        s1_d, s2_d, s3_d = S + S, B + B, C + C
        g1_1, g1_2, g1_rep = a1, b3, c1
        g2_1, g2_2, g2_rep = b1, a2, c3
        g3_1, g3_2, g3_rep = b2, a3, c2
    else:
        v1, a1, b1, c1 = J + R, J + A, A + R, I + B
        v2, a2, b2, c2 = Q + I, Q + B, B + I, P + C
        v3, a3, b3, c3 = S + P, S + C, C + P, C + S
        s1_d, s2_d, s3_d = I + I, P + P, C + C
        g1_1, g1_2, g1_rep = a1, b2, c1
        g2_1, g2_2, g2_rep = a2, b3, c2
        g3_1, g3_2, g3_rep = b1, a3, c3
    nb_s_pair = random.choice([(a1, b1[::-1]), (a1[::-1], b1)])
    nb_da_1_d = '\\True $\\overrightarrow{%s} = \\overrightarrow{%s} + \\overrightarrow{%s}$' % (v1, a1, b1)
    nb_da_1_s = '$\\overrightarrow{%s} = \\overrightarrow{%s} + \\overrightarrow{%s}$' % (v1, nb_s_pair[0], nb_s_pair[1])
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    list_nb_1 = [nb_da_1]
    loigiai_nb_1 = 'Theo quy tắc ba điểm ta có $\\overrightarrow{%s} = \\overrightarrow{%s} + \\overrightarrow{%s}$.' % (v1, a1, b1)
    list_nb_2 = [loigiai_nb_1]
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    th_s_pair = random.choice([(a2, b2[::-1]), (a2[::-1], b2)])
    th_da_1_d = '\\True $\\overrightarrow{%s} = \\overrightarrow{%s} + \\overrightarrow{%s}$' % (v2, a2, b2)
    th_da_1_s = '$\\overrightarrow{%s} = \\overrightarrow{%s} + \\overrightarrow{%s}$' % (v2, th_s_pair[0], th_s_pair[1])
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    list_th_1 = [th_da_1]
    loigiai_th_1 = 'Theo quy tắc ba điểm ta có $\\overrightarrow{%s} = \\overrightarrow{%s} + \\overrightarrow{%s}$.' % (v2, a2, b2)
    list_th_2 = [loigiai_th_1]
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    vd_s_pair = random.choice([(a3, b3[::-1]), (a3[::-1], b3)])
    vd_da_1_d = '\\True $\\overrightarrow{%s} = \\overrightarrow{%s} + \\overrightarrow{%s}$' % (v3, a3, b3)
    vd_da_1_s = '$\\overrightarrow{%s} = \\overrightarrow{%s} + \\overrightarrow{%s}$' % (v3, vd_s_pair[0], vd_s_pair[1])
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    list_vd_1 = [vd_da_1]
    loigiai_vd_1 = 'Theo quy tắc ba điểm ta có $\\overrightarrow{%s} = \\overrightarrow{%s} + \\overrightarrow{%s}$.' % (v3, a3, b3)
    list_vd_2 = [loigiai_vd_1]
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    vp_sai = random.choice([A + B, B + C, C + A])
    vdc_da_1_d = '\\True $\\overrightarrow{%s} + \\overrightarrow{%s} + \\overrightarrow{%s} = \\overrightarrow{0}$' % (v1, v2, v3)
    vdc_da_1_s = '$\\overrightarrow{%s} + \\overrightarrow{%s} + \\overrightarrow{%s} = \\overrightarrow{%s}$' % (v1, v2, v3, vp_sai)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    list_vdc_1 = [vdc_da_1]
    loigiai_vdc_1 = 'Ta có: $\\overrightarrow{%s} + \\overrightarrow{%s} + \\overrightarrow{%s} = \\left(\\overrightarrow{%s} + \\overrightarrow{%s}\\right) + \\left(\\overrightarrow{%s} + \\overrightarrow{%s}\\right) + \\left(\\overrightarrow{%s} + \\overrightarrow{%s}\\right) = \\left(\\overrightarrow{%s} + \\overrightarrow{%s}\\right) + \\left(\\overrightarrow{%s} + \\overrightarrow{%s}\\right) + \\left(\\overrightarrow{%s} + \\overrightarrow{%s}\\right) = \\left(\\overrightarrow{%s} + \\overrightarrow{%s}\\right) + \\left(\\overrightarrow{%s} + \\overrightarrow{%s}\\right) + \\left(\\overrightarrow{%s} + \\overrightarrow{%s}\\right) = \\overrightarrow{%s} + \\overrightarrow{%s} + \\overrightarrow{%s} = \\overrightarrow{0}$. Vậy $\\overrightarrow{%s} + \\overrightarrow{%s} + \\overrightarrow{%s} = \\overrightarrow{0}$.' % (v1, v2, v3, a1, b1, a2, b2, a3, b3, g1_1, g1_2, g2_1, g2_2, g3_1, g3_2, g1_rep, g1_2, g2_rep, g2_2, g3_rep, g3_2, s1_d, s2_d, s3_d, v1, v2, v3)
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

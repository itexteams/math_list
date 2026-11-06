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


def bt_dang20_p2_b1_c1_hh11(self):
    # Khai báo biến ngẫu nhiên tên đỉnh
    danh_sach_dinh = [
        ('S', 'A', 'B', 'C', 'D', 'E', 'F', 'G'),
        ('S', 'M', 'N', 'P', 'Q', 'I', 'J', 'K'),
        ('P', 'A', 'B', 'C', 'D', 'E', 'F', 'H'),
        ('S', 'E', 'F', 'G', 'H', 'M', 'N', 'K')
    ]

    pt_S, pt_A, pt_B, pt_C, pt_D, pt_E, pt_F, pt_G = random.choice(danh_sach_dinh)

    # Nội dung câu hỏi
    noidungcauhoi = ('''Cho hình chóp $%s.%s%s%s%s$, biết $%s%s$ cắt $%s%s$ tại $%s$, $%s%s$ cắt $%s%s$ tại $%s$ trong mặt phẳng đáy.'''
                     % (pt_S, pt_A, pt_B, pt_C, pt_D, pt_A, pt_B, pt_C, pt_D, pt_E, pt_A, pt_C, pt_B, pt_D, pt_F))

    ########################################################################
    # Nhận biết ############################################
    # Các đáp án
    nb_da_1_d = '\\True Đường thẳng $%s%s$ nằm trong mặt phẳng $(%s%s%s%s)$' % (pt_E, pt_F, pt_A, pt_B, pt_C, pt_D)
    nb_da_1_s = 'Đường thẳng $%s%s$ không nằm trong mặt phẳng $(%s%s%s%s)$' % (pt_E, pt_F, pt_A, pt_B, pt_C, pt_D)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)

    list_nb_1 = [nb_da_1]

    k_nb = "đúng" if nb_da_1 == nb_da_1_d else "sai"
    loigiai_nb_1 = ('''Ta có: $%s = %s%s \\cap %s%s \\Rightarrow %s \\in (%s%s%s%s)$, $%s = %s%s \\cap %s%s \\Rightarrow %s \\in (%s%s%s%s)$.\\\\ Vậy $%s%s \\subset (%s%s%s%s)$ nên a %s.'''
                    % (pt_E, pt_A, pt_B, pt_C, pt_D, pt_E, pt_A, pt_B, pt_C, pt_D, pt_F, pt_A, pt_C, pt_B, pt_D, pt_F, pt_A, pt_B, pt_C, pt_D, pt_E, pt_F, pt_A, pt_B, pt_C, pt_D, k_nb))

    list_nb_2 = [loigiai_nb_1]
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

    ########################################################################
    # Thông hiểu ############################################
    # Các đáp án
    th_da_1_d = '\\True $%s%s$ là giao tuyến của hai mặt phẳng $(%s%s%s)$ và $(%s%s%s%s)$' % (pt_A, pt_B, pt_S, pt_A, pt_B, pt_A, pt_B, pt_C, pt_D)
    th_da_1_s = '$%s%s$ không phải là giao tuyến của hai mặt phẳng $(%s%s%s)$ và $(%s%s%s%s)$' % (pt_A, pt_B, pt_S, pt_A, pt_B, pt_A, pt_B, pt_C, pt_D)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)

    list_th_1 = [th_da_1]

    k_th = "đúng" if th_da_1 == th_da_1_d else "sai"
    loigiai_th_1 = ('''$%s$ và $%s$ là hai điểm chung của hai mặt phẳng $(%s%s%s)$ và $(%s%s%s%s)$.\\\\ Suy ra $%s%s = (%s%s%s) \\cap (%s%s%s%s)$ nên b %s.'''
                    % (pt_A, pt_B, pt_S, pt_A, pt_B, pt_A, pt_B, pt_C, pt_D, pt_A, pt_B, pt_S, pt_A, pt_B, pt_A, pt_B, pt_C, pt_D, k_th))

    list_th_2 = [loigiai_th_1]
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

    ########################################################################
    # Vận dụng ############################################
    # Các đáp án
    vd_da_1_d = '\\True $%s%s$ là giao tuyến của hai mặt phẳng $(%s%s%s)$ và $(%s%s%s)$, $%s%s$ là giao tuyến của hai mặt phẳng $(%s%s%s)$ và $(%s%s%s)$' % (pt_S, pt_E, pt_S, pt_A, pt_B, pt_S, pt_C, pt_D, pt_S, pt_F, pt_S, pt_A, pt_C, pt_S, pt_B, pt_D)
    vd_da_1_s = '$%s%s$ là giao tuyến của hai mặt phẳng $(%s%s%s)$ và $(%s%s%s)$, $%s%s$ không phải là giao tuyến của hai mặt phẳng $(%s%s%s)$ và $(%s%s%s)$' % (pt_S, pt_E, pt_S, pt_A, pt_B, pt_S, pt_C, pt_D, pt_S, pt_F, pt_S, pt_A, pt_C, pt_S, pt_B, pt_D)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)

    list_vd_1 = [vd_da_1]

    k_vd = "đúng" if vd_da_1 == vd_da_1_d else "sai"
    loigiai_vd_1 = ('''Dễ thấy $%s$ là điểm chung thứ nhất của $(%s%s%s)$ và $(%s%s%s)$.\\\\ Ta có $%s = %s%s \\cap %s%s \\Rightarrow %s \\in (%s%s%s) \\cap (%s%s%s) \\Rightarrow %s%s = (%s%s%s) \\cap (%s%s%s)$.\\\\ Tương tự $%s%s = (%s%s%s) \\cap (%s%s%s)$. Do đó c %s.'''
                    % (pt_S, pt_S, pt_A, pt_B, pt_S, pt_C, pt_D, pt_E, pt_A, pt_B, pt_C, pt_D, pt_E, pt_S, pt_A, pt_B, pt_S, pt_C, pt_D, pt_S, pt_E, pt_S, pt_A, pt_B, pt_S, pt_C, pt_D, pt_S, pt_F, pt_S, pt_A, pt_C, pt_S, pt_B, pt_D, k_vd))

    list_vd_2 = [loigiai_vd_1]
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

    ########################################################################
    # Vận dụng cao ############################################
    # Các đáp án
    vdc_da_1_d = '\\True Gọi $%s = %s%s \\cap %s%s$ khi đó, $%s%s$ là giao tuyến của mặt phẳng $(%s%s%s)$ và mặt phẳng $(%s%s%s)$' % (pt_G, pt_E, pt_F, pt_A, pt_D, pt_S, pt_G, pt_S, pt_E, pt_F, pt_S, pt_A, pt_D)
    vdc_da_1_s = 'Gọi $%s = %s%s \\cap %s%s$ khi đó, $%s%s$ không phải là giao tuyến của mặt phẳng $(%s%s%s)$ và mặt phẳng $(%s%s%s)$' % (pt_G, pt_E, pt_F, pt_A, pt_D, pt_S, pt_G, pt_S, pt_E, pt_F, pt_S, pt_A, pt_D)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)

    list_vdc_1 = [vdc_da_1]

    k_vdc = "đúng" if vdc_da_1 == vdc_da_1_d else "sai"
    loigiai_vdc_1 = ('''Dễ thấy $%s$ là điểm chung thứ nhất của $(%s%s%s)$ và $(%s%s%s)$.\\\\ Trong mặt phẳng đáy, gọi $%s = %s%s \\cap %s%s \\Rightarrow %s \\in (%s%s%s) \\cap (%s%s%s)$.\\\\ Vậy $%s%s = (%s%s%s) \\cap (%s%s%s)$ nên d %s.'''
                     % (pt_S, pt_S, pt_E, pt_F, pt_S, pt_A, pt_D, pt_G, pt_E, pt_F, pt_A, pt_D, pt_G, pt_S, pt_E, pt_F, pt_S, pt_A, pt_D, pt_S, pt_G, pt_S, pt_E, pt_F, pt_S, pt_A, pt_D, k_vdc))

    list_vdc_2 = [loigiai_vdc_1]
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

    k_nb = "đúng" if nb_da_1 == nb_da_1_d else "sai"
    k_th = "đúng" if th_da_1 == th_da_1_d else "sai"
    k_vd = "đúng" if vd_da_1 == vd_da_1_d else "sai"
    k_vdc = "đúng" if vdc_da_1 == vdc_da_1_d else "sai"

    loigiai_nb_1 = ('''Ta có: $%s = %s%s \\cap %s%s \\Rightarrow %s \\in (%s%s%s%s)$, $%s = %s%s \\cap %s%s \\Rightarrow %s \\in (%s%s%s%s)$.\\\\ Vậy $%s%s \\subset (%s%s%s%s)$ nên a %s.'''
                    % (pt_E, pt_A, pt_B, pt_C, pt_D, pt_E, pt_A, pt_B, pt_C, pt_D, pt_F, pt_A, pt_C, pt_B, pt_D, pt_F, pt_A, pt_B, pt_C, pt_D, pt_E, pt_F, pt_A, pt_B, pt_C, pt_D, k_nb))

    loigiai_th_1 = ('''$%s$ và $%s$ là hai điểm chung của hai mặt phẳng $(%s%s%s)$ và $(%s%s%s%s)$.\\\\ Suy ra $%s%s = (%s%s%s) \\cap (%s%s%s%s)$ nên b %s.'''
                    % (pt_A, pt_B, pt_S, pt_A, pt_B, pt_A, pt_B, pt_C, pt_D, pt_A, pt_B, pt_S, pt_A, pt_B, pt_A, pt_B, pt_C, pt_D, k_th))

    loigiai_vd_1 = ('''Dễ thấy $%s$ là điểm chung thứ nhất của $(%s%s%s)$ và $(%s%s%s)$.\\\\ Ta có $%s = %s%s \\cap %s%s \\Rightarrow %s \\in (%s%s%s) \\cap (%s%s%s) \\Rightarrow %s%s = (%s%s%s) \\cap (%s%s%s)$.\\\\ Tương tự $%s%s = (%s%s%s) \\cap (%s%s%s)$. Do đó c %s.'''
                    % (pt_S, pt_S, pt_A, pt_B, pt_S, pt_C, pt_D, pt_E, pt_A, pt_B, pt_C, pt_D, pt_E, pt_S, pt_A, pt_B, pt_S, pt_C, pt_D, pt_S, pt_E, pt_S, pt_A, pt_B, pt_S, pt_C, pt_D, pt_S, pt_F, pt_S, pt_A, pt_C, pt_S, pt_B, pt_D, k_vd))

    loigiai_vdc_1 = ('''Dễ thấy $%s$ là điểm chung thứ nhất của $(%s%s%s)$ và $(%s%s%s)$.\\\\ Trong mặt phẳng đáy, gọi $%s = %s%s \\cap %s%s \\Rightarrow %s \\in (%s%s%s) \\cap (%s%s%s)$.\\\\ Vậy $%s%s = (%s%s%s) \\cap (%s%s%s)$ nên d %s.'''
                     % (pt_S, pt_S, pt_E, pt_F, pt_S, pt_A, pt_D, pt_G, pt_E, pt_F, pt_A, pt_D, pt_G, pt_S, pt_E, pt_F, pt_S, pt_A, pt_D, pt_S, pt_G, pt_S, pt_E, pt_F, pt_S, pt_A, pt_D, k_vdc))

    list_nb_2 = [loigiai_nb_1]
    list_th_2 = [loigiai_th_1]
    list_vd_2 = [loigiai_vd_1]
    list_vdc_2 = [loigiai_vdc_1]

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

    # Mã hình TikZ chuẩn chính xác 100%
    tikz_fig = ('''\\begin{center}
    \\begin{tikzpicture}[line width=1pt, scale=0.9]
    \\coordinate (S) at (-0.5, 3.2);
    \\coordinate (A) at (-2.3, 0.4);
    \\coordinate (B) at (1.5, 0.4);
    \\coordinate (C) at (0.8, -0.5);
    \\coordinate (D) at (-1.2, -1.0);
    \\coordinate (E) at (4.5, 0.4);
    \\coordinate (F) at (0.12, -0.31);
    \\coordinate (G) at (-1.53, -0.58);
    \\coordinate (H) at (1.07, -0.16);
    \\draw[line width=1pt] (S)--(A) (S)--(D) (S)--(C) (S)--(B) (S)--(E);
    \\draw[line width=1pt] (A)--(D)--(C)--(E);
    \\draw[line width=1pt] (B)--(C);
    \\draw[line width=1pt] (B)--(E);
    \\draw[line width=1pt] (H)--(E);
    \\draw[line width=1pt, dashed] (A)--(B);
    \\draw[line width=1pt, dashed] (A)--(C);
    \\draw[line width=1pt, dashed] (B)--(D);
    \\draw[line width=1pt, dashed] (S)--(F);
    \\draw[line width=1pt, dashed] (G)--(H);
    \\fill (S) circle (1.5pt) node[above] {$%s$};
    \\fill (A) circle (1.5pt) node[left] {$%s$};
    \\fill (B) circle (1.5pt) node[above right] {$%s$};
    \\fill (C) circle (1.5pt) node[below right] {$%s$};
    \\fill (D) circle (1.5pt) node[below left] {$%s$};
    \\fill (E) circle (1.5pt) node[right] {$%s$};
    \\fill (F) circle (1.5pt) node[below] {$%s$};
    \\fill (G) circle (1.5pt) node[left] {$%s$};
    \\end{tikzpicture}
    \\end{center}''' % (pt_S, pt_A, pt_B, pt_C, pt_D, pt_E, pt_F, pt_G))

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n'
               '\\choiceTFn \n'
               '{' + str(shuffled_answers_nb[0]) + '}\n'
               '{' + str(shuffled_answers_th[0]) + '}\n'
               '{' + str(shuffled_answers_vd[0]) + '}\n'
               '{' + str(shuffled_answers_vdc[0]) + '}\n'
               '\\loigiai{ \n' +
               str(tikz_fig) + '\n'
               '\\begin{enumEX}[a)]{1} \n'
               '\\item ' + str(shuffled_solutions_nb[0]) + '\n'
               '\\item ' + str(shuffled_solutions_th[0]) + '\n'
               '\\item ' + str(shuffled_solutions_vd[0]) + '\n'
               '\\item ' + str(shuffled_solutions_vdc[0]) + '\n'
               '\\end{enumEX}} \n'
               '\\end{ex}\n \\end{minipage}\n\n')
    return content


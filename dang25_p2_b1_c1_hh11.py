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


def bt_dang25_p2_b1_c1_hh11(self):
    # Khai báo các điểm trong bài toán
    A, B, C, D, S, O, M, K, N = 'A', 'B', 'C', 'D', 'S', 'O', 'M', 'K', 'N'

    # Nội dung câu hỏi
    noidungcauhoi = ('''Cho tứ giác $%s%s%s%s$ có $%s%s$ và $%s%s$ giao nhau tại $%s$ và một điểm $%s$ không thuộc mặt phẳng $(%s%s%s%s)$. Trên đoạn $%s%s$ lấy một điểm $%s$ không trùng với $%s$ và $%s$, $%s = %s%s \\cap %s%s$.''' 
                     % (A, B, C, D, A, C, B, D, O, S, A, B, C, D, S, C, M, S, C, K, A, M, S, O))

    # Hình vẽ TikZ
    tikz_str = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,0);
    \\coordinate (B) at (1,-1.8);
    \\coordinate (C) at (4,-2.5);
    \\coordinate (D) at (6,-0.5);
    \\coordinate (S) at (2.5,3.5);
    \\coordinate (O) at (intersection of A--C and B--D);
    \\coordinate (M) at ($(S)!0.6!(C)$);
    \\coordinate (K) at (intersection of A--M and S--O);
    \\coordinate (N) at (intersection of B--K and S--D);
    \\draw[line width=1pt] (S)--(A) (S)--(B) (S)--(C) (S)--(D) (A)--(B) (B)--(C) (C)--(D)  (B)--(M);
    \\draw[line width=1pt, dashed] (A)--(D) (A)--(C) (B)--(D) (S)--(O) (B)--(N) (A)--(M);
    \\fill (A) circle (1pt) node[left] {$%s$};
    \\fill (B) circle (1pt) node[below left] {$%s$};
    \\fill (C) circle (1pt) node[below right] {$%s$};
    \\fill (D) circle (1pt) node[right] {$%s$};
    \\fill (S) circle (1pt) node[above] {$%s$};
    \\fill (O) circle (1pt) node[below] {$%s$};
    \\fill (M) circle (1pt) node[right] {$%s$};
    \\fill (K) circle (1pt) node[above left] {$%s$};
    \\fill (N) circle (1pt) node[above right] {$%s$};
    \\end{tikzpicture}
    \\end{center}''' % (A, B, C, D, S, O, M, K, N))

    ########################################################################
    # Nhận biết ############################################
    nb_da_1_d = '\\True $%s%s$ là giao tuyến của hai mặt phẳng $(%s%s%s)$ và $(%s%s%s)$' % (A, C, S, A, C, A, B, C)
    nb_da_1_s = '$%s%s$ là giao tuyến của hai mặt phẳng $(%s%s%s)$ và $(%s%s%s)$' % (S, O, S, A, C, A, B, C)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

    ########################################################################
    # Thông hiểu ############################################
    th_da_1_d = '\\True $%s%s$ là giao tuyến của hai mặt phẳng $(%s%s%s)$ và $(%s%s%s)$' % (S, O, S, A, C, S, B, D)
    th_da_1_s = '$%s%s$ là giao tuyến của hai mặt phẳng $(%s%s%s)$ và $(%s%s%s)$' % (A, C, S, A, C, S, B, D)
    list_th_da_1 = [th_da_1_d, th_da_1_s]

    ########################################################################
    # Vận dụng ############################################
    vd_da_1_d = '\\True Giao điểm của đường thẳng $%s%s$ với mặt phẳng $(%s%s%s)$ là điểm $%s$' % (S, O, A, B, M, K)
    vd_da_1_s = 'Giao điểm của đường thẳng $%s%s$ với mặt phẳng $(%s%s%s)$ là điểm $%s$' % (S, O, A, B, M, O)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

    ########################################################################
    # Vận dụng cao ############################################
    vdc_da_1_d = '\\True Giao điểm của đường thẳng $%s%s$ với mặt phẳng $(%s%s%s)$ là điểm $%s$ thuộc đường thẳng $%s%s$' % (S, D, A, B, M, N, B, K)
    vdc_da_1_s = 'Giao điểm của đường thẳng $%s%s$ với mặt phẳng $(%s%s%s)$ là điểm $%s$ thuộc đường thẳng $%s%s$' % (S, D, A, B, M, N, A, K)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

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

    # Lời giải chi tiết tương ứng với phương án được chọn
    if nb_da_1 == nb_da_1_d:
        loigiai_nb_1 = ('''Mệnh đề ĐÚNG.\\\\
    Giao tuyến của hai mặt phẳng $(%s%s%s)$ và $(%s%s%s)$ là đường thẳng $%s%s$.\\\\
    Ta có: $\\begin{cases} %s \\in (%s%s%s) \\cap (%s%s%s) \\\\ %s \\in (%s%s%s) \\cap (%s%s%s) \\end{cases} \\Rightarrow (%s%s%s) \\cap (%s%s%s) = %s%s$.'''
                        % (S, A, C, A, B, C, A, C,
                           A, S, A, C, A, B, C,
                           C, S, A, C, A, B, C,
                           S, A, C, A, B, C, A, C))
    else:
        loigiai_nb_1 = ('''Mệnh đề SAI.\\\\
    Giao tuyến của hai mặt phẳng $(%s%s%s)$ và $(%s%s%s)$ phải là đường thẳng $%s%s$ (không phải $%s%s$).\\\\
    Ta có: $\\begin{cases} %s \\in (%s%s%s) \\cap (%s%s%s) \\\\ %s \\in (%s%s%s) \\cap (%s%s%s) \\end{cases} \\Rightarrow (%s%s%s) \\cap (%s%s%s) = %s%s$.'''
                        % (S, A, C, A, B, C, A, C, S, O,
                           A, S, A, C, A, B, C,
                           C, S, A, C, A, B, C,
                           S, A, C, A, B, C, A, C))

    if th_da_1 == th_da_1_d:
        loigiai_th_1 = ('''Mệnh đề ĐÚNG.\\\\
    Giao tuyến của hai mặt phẳng $(%s%s%s)$ và $(%s%s%s)$ là đường thẳng $%s%s$.\\\\
    Trong mặt phẳng $(%s%s%s%s)$, gọi $%s = %s%s \\cap %s%s$.\\\\
    Ta có: $\\begin{cases} %s \\in (%s%s%s) \\cap (%s%s%s) \\\\ %s \\in %s%s \\subset (%s%s%s), %s \\in %s%s \\subset (%s%s%s) \\end{cases} \\Rightarrow (%s%s%s) \\cap (%s%s%s) = %s%s$.'''
                        % (S, A, C, S, B, D, S, O,
                           A, B, C, D, O, A, C, B, D,
                           S, S, A, C, S, B, D,
                           O, A, C, S, A, C,
                           O, B, D, S, B, D,
                           S, A, C, S, B, D, S, O))
    else:
        loigiai_th_1 = ('''Mệnh đề SAI.\\\\
    Giao tuyến của hai mặt phẳng $(%s%s%s)$ và $(%s%s%s)$ phải là đường thẳng $%s%s$ (không phải $%s%s$).\\\\
    Trong mặt phẳng $(%s%s%s%s)$, gọi $%s = %s%s \\cap %s%s$.\\\\
    Ta có: $\\begin{cases} %s \\in (%s%s%s) \\cap (%s%s%s) \\\\ %s \\in %s%s \\subset (%s%s%s), %s \\in %s%s \\subset (%s%s%s) \\end{cases} \\Rightarrow (%s%s%s) \\cap (%s%s%s) = %s%s$.'''
                        % (S, A, C, S, B, D, S, O, A, C,
                           A, B, C, D, O, A, C, B, D,
                           S, S, A, C, S, B, D,
                           O, A, C, S, A, C,
                           O, B, D, S, B, D,
                           S, A, C, S, B, D, S, O))

    if vd_da_1 == vd_da_1_d:
        loigiai_vd_1 = ('''Mệnh đề ĐÚNG.\\\\
    Tìm giao điểm của $%s%s$ và mặt phẳng $(%s%s%s)$:\\\\
    Trong mặt phẳng $(%s%s%s)$, gọi $%s = %s%s \\cap %s%s$.\\\\
    Vì $\\begin{cases} %s \\in %s%s, %s%s \\subset (%s%s%s) \\\\ %s \\in %s%s \\end{cases} \\Rightarrow %s = %s%s \\cap (%s%s%s)$.'''
                        % (S, O, A, B, M,
                           S, A, C, K, A, M, S, O,
                           K, A, M, A, M, A, B, M,
                           K, S, O,
                           K, S, O, A, B, M))
    else:
        loigiai_vd_1 = ('''Mệnh đề SAI.\\\\
    Giao điểm của đường thẳng $%s%s$ với mặt phẳng $(%s%s%s)$ là điểm $%s$ (không phải điểm $%s$).\\\\
    Trong mặt phẳng $(%s%s%s)$, gọi $%s = %s%s \\cap %s%s$.\\\\
    Vì $\\begin{cases} %s \\in %s%s, %s%s \\subset (%s%s%s) \\\\ %s \\in %s%s \\end{cases} \\Rightarrow %s = %s%s \\cap (%s%s%s)$.'''
                        % (S, O, A, B, M, K, O,
                           S, A, C, K, A, M, S, O,
                           K, A, M, A, M, A, B, M,
                           K, S, O,
                           K, S, O, A, B, M))

    if vdc_da_1 == vdc_da_1_d:
        loigiai_vdc_1 = ('''Mệnh đề ĐÚNG.\\\\
    Tìm giao điểm của $%s%s$ và mặt phẳng $(%s%s%s)$:\\\\
    Xét mặt phẳng phụ $(%s%s%s)$ chứa $%s%s$.\\\\
    Dễ thấy $%s$ là điểm chung của hai mặt phẳng $(%s%s%s)$ và $(%s%s%s)$.\\\\
    Ta có: $\\begin{cases} %s \\in %s%s, %s%s \\subset (%s%s%s) \\\\ %s \\in %s%s, %s%s \\subset (%s%s%s) \\end{cases} \\Rightarrow %s \\in (%s%s%s) \\cap (%s%s%s)$.\\\\
    Do đó $%s%s = (%s%s%s) \\cap (%s%s%s)$.\\\\
    Trong mặt phẳng $(%s%s%s)$, gọi $%s = %s%s \\cap %s%s$.\\\\
    Vì $\\begin{cases} %s \\in %s%s \\\\ %s \\in %s%s, %s%s \\subset (%s%s%s) \\end{cases} \\Rightarrow %s = %s%s \\cap (%s%s%s)$.\\\\
    Do đó điểm $%s$ thuộc đường thẳng $%s%s$.'''
                         % (S, D, A, B, M,
                            S, B, D, S, D,
                            B, S, B, D, A, B, M,
                            K, A, M, A, M, A, B, M,
                            K, S, O, S, O, S, B, D,
                            K, S, B, D, A, B, M,
                            B, K, S, B, D, A, B, M,
                            S, B, D, N, B, K, S, D,
                            N, S, D,
                            N, B, K, B, K, A, B, M,
                            N, S, D, A, B, M,
                            N, B, K))
    else:
        loigiai_vdc_1 = ('''Mệnh đề SAI.\\\\
    Tìm giao điểm của $%s%s$ và mặt phẳng $(%s%s%s)$:\\\\
    Xét mặt phẳng phụ $(%s%s%s)$ chứa $%s%s$.\\\\
    Dễ thấy $%s$ là điểm chung của hai mặt phẳng $(%s%s%s)$ và $(%s%s%s)$.\\\\
    Ta có: $\\begin{cases} %s \\in %s%s, %s%s \\subset (%s%s%s) \\\\ %s \\in %s%s, %s%s \\subset (%s%s%s) \\end{cases} \\Rightarrow %s \\in (%s%s%s) \\cap (%s%s%s)$.\\\\
    Do đó $%s%s = (%s%s%s) \\cap (%s%s%s)$.\\\\
    Trong mặt phẳng $(%s%s%s)$, gọi $%s = %s%s \\cap %s%s$.\\\\
    Vì $\\begin{cases} %s \\in %s%s \\\\ %s \\in %s%s, %s%s \\subset (%s%s%s) \\end{cases} \\Rightarrow %s = %s%s \\cap (%s%s%s)$.\\\\
    Do đó điểm $%s$ thuộc đường thẳng $%s%s$ (không thuộc đường thẳng $%s%s$).'''
                         % (S, D, A, B, M,
                            S, B, D, S, D,
                            B, S, B, D, A, B, M,
                            K, A, M, A, M, A, B, M,
                            K, S, O, S, O, S, B, D,
                            K, S, B, D, A, B, M,
                            B, K, S, B, D, A, B, M,
                            S, B, D, N, B, K, S, D,
                            N, S, D,
                            N, B, K, B, K, A, B, M,
                            N, S, D, A, B, M,
                            N, B, K, A, K))

    # Gán vào danh sách
    list_nb_1 = [nb_da_1]
    list_th_1 = [th_da_1]
    list_vd_1 = [vd_da_1]
    list_vdc_1 = [vdc_da_1]

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

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+
    str(noidungcauhoi)+ '\n'
        '\\choiceTFn \n'
       '{'+str(shuffled_answers_nb[0])+'}\n'
       '{'+str(shuffled_answers_th[0])+'}\n'
       '{'+str(shuffled_answers_vd[0])+'}\n'
       '{'+str(shuffled_answers_vdc[0])+'}\n'
        '\\loigiai{ \n' +
    str(tikz_str) + '\n' +
        '\\begin{enumEX}[a)]{1} \n'
        '\\item '+str(shuffled_solutions_nb[0])+'\n'
        '\\item '+str(shuffled_solutions_th[0])+'\n'
        '\\item '+str(shuffled_solutions_vd[0])+'\n'
        '\\item '+str(shuffled_solutions_vdc[0])+'\n'
        '\\end{enumEX}} \n'
        '\\end{ex}\n \\end{minipage}\n\n')
    return content


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


def bt_dang21_p2_b1_c1_hh11(self):
    # 1. Khai báo danh sách biến ngẫu nhiên đặt tên đỉnh
    danh_sach_dinh = [
        ('S', 'A', 'B', 'C', 'D', 'M', 'O', 'E', 'F'),
        ('S', 'M', 'N', 'P', 'Q', 'K', 'I', 'H', 'J'),
        ('P', 'A', 'B', 'C', 'D', 'E', 'O', 'X', 'Y'),
        ('S', 'E', 'F', 'G', 'H', 'N', 'K', 'U', 'V')
    ]

    pt_S, pt_A, pt_B, pt_C, pt_D, pt_M, pt_O, pt_E, pt_F = random.choice(danh_sach_dinh)

    # 2. Nội dung câu hỏi
    noidungcauhoi = ('''Cho hình chóp $%s.%s%s%s%s$, đáy là tứ giác lồi $%s%s%s%s$ có các cạnh đối không song song với nhau. Gọi $%s$ là điểm trên cạnh $%s%s$, $%s$ là giao điểm của $%s%s$ và $%s%s$.'''
                     % (pt_S, pt_A, pt_B, pt_C, pt_D, pt_A, pt_B, pt_C, pt_D, pt_M, pt_S, pt_A, pt_O, pt_A, pt_C, pt_B, pt_D))

    ########################################################################
    # Nhận biết 
    nb_da_1_d = '\\True Giao tuyến của $(%s%s%s)$ và $(%s%s%s)$ là $%s%s$' % (pt_S, pt_A, pt_C, pt_S, pt_B, pt_D, pt_S, pt_O)
    nb_da_1_s = 'Giao tuyến của $(%s%s%s)$ và $(%s%s%s)$ là $%s%s$' % (pt_S, pt_A, pt_C, pt_S, pt_B, pt_D, pt_S, pt_M)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

    ########################################################################
    # Thông hiểu 
    th_da_1_d = '\\True Giao tuyến của $(%s%s%s)$ và $(%s%s%s)$ là $%s%s$, $%s$ là giao điểm của $%s%s$ và $%s%s$' % (pt_S, pt_A, pt_B, pt_S, pt_C, pt_D, pt_S, pt_F, pt_F, pt_A, pt_B, pt_C, pt_D)
    th_da_1_s = 'Giao tuyến của $(%s%s%s)$ và $(%s%s%s)$ là $%s%s$, $%s$ là giao điểm của $%s%s$ và $%s%s$' % (pt_S, pt_A, pt_B, pt_S, pt_C, pt_D, pt_S, pt_E, pt_E, pt_A, pt_B, pt_C, pt_D)
    list_th_da_1 = [th_da_1_d, th_da_1_s]

    ########################################################################
    # Vận dụng 
    vd_da_1_d = '\\True Giao tuyến của $(%s%s%s)$ và $(%s%s%s)$ là $%s%s$' % (pt_B, pt_C, pt_M, pt_S, pt_A, pt_D, pt_M, pt_E)
    vd_da_1_s = 'Giao tuyến của $(%s%s%s)$ và $(%s%s%s)$ là $%s%s$' % (pt_B, pt_C, pt_M, pt_S, pt_A, pt_D, pt_S, pt_M)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

    ########################################################################
    # Vận dụng cao 
    vdc_da_1_d = '\\True Giao tuyến của $(%s%s%s)$ và $(%s%s%s)$ là $%s%s$' % (pt_C, pt_D, pt_M, pt_S, pt_A, pt_B, pt_M, pt_F)
    vdc_da_1_s = 'Giao tuyến của $(%s%s%s)$ và $(%s%s%s)$ là $%s%s$' % (pt_C, pt_D, pt_M, pt_S, pt_A, pt_B, pt_M, pt_E)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)

    # Lặp chọn ngẫu nhiên đến khi đáp án có từ 1 đến 3 câu đúng
    while True:
        nb_da_1 = random.choice(list_nb_da_1)
        th_da_1 = random.choice(list_th_da_1)
        vd_da_1 = random.choice(list_vd_da_1)
        vdc_da_1 = random.choice(list_vdc_da_1)

        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        true_count = count_true_answers(answers)

        if 1 <= true_count <= 3:
            break

    # Lời giải từng ý
    k_nb = "đúng" if nb_da_1 == nb_da_1_d else "sai"
    loigiai_nb_1 = ('''Trong mặt phẳng $(%s%s%s%s)$ có $%s%s \\cap %s%s = \\{%s\\}$.\\\\ Ta có $%s \\in %s%s \\subset (%s%s%s)$ và $%s \\in %s%s \\subset (%s%s%s) \\Rightarrow %s \\in (%s%s%s) \\cap (%s%s%s)$.\\\\ Mà $%s \\in (%s%s%s) \\cap (%s%s%s)$ nên $%s%s = (%s%s%s) \\cap (%s%s%s)$.\\\\ Vậy ý a %s.'''
                    % (pt_A, pt_B, pt_C, pt_D, pt_A, pt_C, pt_B, pt_D, pt_O, pt_O, pt_A, pt_C, pt_S, pt_A, pt_C, pt_O, pt_B, pt_D, pt_S, pt_B, pt_D, pt_O, pt_S, pt_A, pt_C, pt_S, pt_B, pt_D, pt_S, pt_S, pt_A, pt_C, pt_S, pt_B, pt_D, pt_S, pt_O, pt_S, pt_A, pt_C, pt_S, pt_B, pt_D, k_nb))

    k_th = "đúng" if th_da_1 == th_da_1_d else "sai"
    loigiai_th_1 = ('''Trong mặt phẳng $(%s%s%s%s)$ gọi $%s = %s%s \\cap %s%s$.\\\\ Ta có $%s \\in %s%s \\subset (%s%s%s)$ và $%s \\in %s%s \\subset (%s%s%s) \\Rightarrow %s \\in (%s%s%s) \\cap (%s%s%s)$.\\\\ Mà $%s \\in (%s%s%s) \\cap (%s%s%s)$ nên $%s%s = (%s%s%s) \\cap (%s%s%s)$.\\\\ Vậy ý b %s.'''
                    % (pt_A, pt_B, pt_C, pt_D, pt_F, pt_A, pt_B, pt_C, pt_D, pt_F, pt_A, pt_B, pt_S, pt_A, pt_B, pt_F, pt_C, pt_D, pt_S, pt_C, pt_D, pt_F, pt_S, pt_A, pt_B, pt_S, pt_C, pt_D, pt_S, pt_S, pt_A, pt_B, pt_S, pt_C, pt_D, pt_S, pt_F, pt_S, pt_A, pt_B, pt_S, pt_C, pt_D, k_th))

    k_vd = "đúng" if vd_da_1 == vd_da_1_d else "sai"
    loigiai_vd_1 = ('''Trong mặt phẳng $(%s%s%s%s)$ gọi $%s = %s%s \\cap %s%s$.\\\\ Ta có $%s \\in %s%s \\subset (%s%s%s)$ và $%s \\in %s%s \\subset (%s%s%s) \\Rightarrow %s \\in (%s%s%s) \\cap (%s%s%s)$.\\\\ Lại có $%s \\in %s%s \\subset (%s%s%s) \\Rightarrow %s \\in (%s%s%s) \\cap (%s%s%s)$.\\\\ Do đó giao tuyến của hai mặt phẳng $(%s%s%s)$ và $(%s%s%s)$ là $%s%s$.\\\\ Vậy ý c %s.'''
                    % (pt_A, pt_B, pt_C, pt_D, pt_E, pt_B, pt_C, pt_A, pt_D, pt_E, pt_B, pt_C, pt_B, pt_C, pt_M, pt_E, pt_A, pt_D, pt_S, pt_A, pt_D, pt_E, pt_B, pt_C, pt_M, pt_S, pt_A, pt_D, pt_M, pt_S, pt_A, pt_S, pt_A, pt_D, pt_M, pt_B, pt_C, pt_M, pt_S, pt_A, pt_D, pt_B, pt_C, pt_M, pt_S, pt_A, pt_D, pt_M, pt_E, k_vd))

    k_vdc = "đúng" if vdc_da_1 == vdc_da_1_d else "sai"
    loigiai_vdc_1 = ('''Trong mặt phẳng $(%s%s%s%s)$ gọi $%s = %s%s \\cap %s%s$.\\\\ Ta có $%s \\in %s%s \\subset (%s%s%s)$ và $%s \\in %s%s \\subset (%s%s%s) \\Rightarrow %s \\in (%s%s%s) \\cap (%s%s%s)$.\\\\ Lại có $%s \\in %s%s \\subset (%s%s%s) \\Rightarrow %s \\in (%s%s%s) \\cap (%s%s%s)$.\\\\ Do đó giao tuyến của hai mặt phẳng $(%s%s%s)$ và $(%s%s%s)$ là $%s%s$.\\\\ Vậy ý d %s.'''
                     % (pt_A, pt_B, pt_C, pt_D, pt_F, pt_C, pt_D, pt_A, pt_B, pt_F, pt_C, pt_D, pt_C, pt_D, pt_M, pt_F, pt_A, pt_B, pt_S, pt_A, pt_B, pt_F, pt_C, pt_D, pt_M, pt_S, pt_A, pt_B, pt_M, pt_S, pt_A, pt_S, pt_A, pt_B, pt_M, pt_C, pt_D, pt_M, pt_S, pt_A, pt_B, pt_C, pt_D, pt_M, pt_S, pt_A, pt_B, pt_M, pt_F, k_vdc))

    list_nb_1, list_th_1, list_vd_1, list_vdc_1 = [nb_da_1], [th_da_1], [vd_da_1], [vdc_da_1]
    list_nb_2, list_th_2, list_vd_2, list_vdc_2 = [loigiai_nb_1], [loigiai_th_1], [loigiai_vd_1], [loigiai_vdc_1]

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

    # Mã TikZ chuẩn xác 100% hình gốc, màu đen toàn bộ, tọa độ thẳng hàng
    tikz_fig = ('''\\begin{center}
    \\begin{tikzpicture}[line width=1pt, scale=1]
    \\coordinate (S) at (0, 3.5);
    \\coordinate (A) at (-3, 0.5);
    \\coordinate (D) at (1, 0.5);
    \\coordinate (E) at (4, 0.5);
    \\coordinate (B) at (-1.5, -1);
    \\coordinate (C) at (0.7, -0.4);
    \\coordinate (F) at (0, -2.5);
    \\coordinate (M) at (-1, 2.5);
    \\coordinate (O) at (-0.154, -0.192);
    \\draw (S)--(A) (S)--(B) (S)--(C) (S)--(E) (S)--(F);
    \\draw (A)--(B)--(F)--(C)--(E);
    \\draw (M)--(B) (M)--(C) (M)--(F);
    \\draw[dashed] (A)--(D)--(E) (D)--(C) (B)--(C);
    \\draw[dashed] (S)--(D) (M)--(D) (M)--(E);
    \\draw[dashed] (A)--(C) (B)--(D) (S)--(O) (M)--(O);
    \\fill[black] (S) circle (1.5pt) node[above] {$%s$};
    \\fill[black] (A) circle (1.5pt) node[left] {$%s$};
    \\fill[black] (B) circle (1.5pt) node[below left] {$%s$};
    \\fill[black] (C) circle (1.5pt) node[below right] {$%s$};
    \\fill[black] (D) circle (1.5pt) node[above right] {$%s$};
    \\fill[black] (M) circle (1.5pt) node[above left] {$%s$};
    \\fill[black] (O) circle (1.5pt) node[below] {$%s$};
    \\fill[black] (E) circle (1.5pt) node[right] {$%s$};
    \\fill[black] (F) circle (1.5pt) node[below] {$%s$};
    \\end{tikzpicture}
    \\end{center}''' % (pt_S, pt_A, pt_B, pt_C, pt_D, pt_M, pt_O, pt_E, pt_F))

    # Xuất câu hỏi
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


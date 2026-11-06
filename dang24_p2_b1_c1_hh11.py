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


def bt_dang24_p2_b1_c1_hh11(self):
    # Khai báo các điểm trong bài toán hình học
    A, B, C, D, S, M, N, O, I, J, P = 'A', 'B', 'C', 'D', 'S', 'M', 'N', 'O', 'I', 'J', 'P'

    # Nội dung câu hỏi
    noidungcauhoi = ('''Cho hình bình hành $%s%s%s%s$ và một điểm $%s$ không thuộc mặt phẳng $(%s%s%s%s)$, các điểm $%s,%s$ lần lượt là trung điểm của đoạn thẳng $%s%s,%s%s$. Gọi $%s = %s%s \\cap %s%s$.''' 
                     % (A, B, C, D, S, A, B, C, D, M, N, A, B, S, C, O, A, C, B, D))

    # Mã TikZ vẽ hình chính xác 100% theo ảnh cung cấp
    tikz_str = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,1);
    \\coordinate (B) at (1.5,-1.5);
    \\coordinate (C) at (5.5,-1.5);
    \\coordinate (D) at (4,1);
    \\coordinate (S) at (2.5,4);
    \\coordinate (M) at ($(A)!0.5!(B)$);
    \\coordinate (N) at ($(S)!0.5!(C)$);
    \\coordinate (O) at (intersection of A--C and B--D);
    \\coordinate (P) at (intersection of C--M and B--D);
    \\coordinate (I) at (intersection of S--O and A--N);
    \\coordinate (J) at (intersection of M--N and S--P);
    \\draw[line width=1pt] (S)--(A) (S)--(B) (S)--(C) (A)--(B) (B)--(C) (S)--(M);
    \\draw[line width=1pt, dashed] (A)--(D) (S)--(D) (C)--(D) (A)--(C) (B)--(D) (S)--(O) (A)--(N) (M)--(N) (C)--(M) (S)--(P);
    \\fill (A) circle (1pt) node[left] {$%s$};
    \\fill (B) circle (1pt) node[below left] {$%s$};
    \\fill (C) circle (1pt) node[below right] {$%s$};
    \\fill (D) circle (1pt) node[right] {$%s$};
    \\fill (S) circle (1pt) node[above] {$%s$};
    \\fill (M) circle (1pt) node[below left] {$%s$};
    \\fill (N) circle (1pt) node[right] {$%s$};
    \\fill (O) circle (1pt) node[below] {$%s$};
    \\fill (P) circle (1pt) node[below] {$%s$};
    \\fill (I) circle (1pt) node[right] {$%s$};
    \\fill (J) circle (1pt) node[left] {$%s$};
    \\end{tikzpicture}
    \\end{center}''' % (A, B, C, D, S, M, N, O, P, I, J))

    ######################################################################## Nhận biết ############################################
    # Các đáp án
    nb_da_1_d = '\\True $%s%s$ giao tuyến của hai mặt phẳng $(%s%s%s)$ và $(%s%s%s)$' % (S, O, S, A, C, S, B, D)
    nb_da_1_s = '$%s%s$ giao tuyến của hai mặt phẳng $(%s%s%s)$ và $(%s%s%s)$' % (S, D, S, A, C, S, B, D)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]

    # Nội dung lời giải
    loigiai_nb_1 = ('''$%s%s$ giao tuyến của hai mặt phẳng $(%s%s%s)$ và $(%s%s%s)$.\\\\
    Trong mặt phẳng $(%s%s%s%s)$, gọi $%s = %s%s \\cap %s%s$.\\\\
    Ta có: $\\begin{cases} %s \\in (%s%s%s) \\cap (%s%s%s) \\\\ %s \\in %s%s \\subset (%s%s%s), %s \\in %s%s \\subset (%s%s%s) \\end{cases} \\Rightarrow %s%s = (%s%s%s) \\cap (%s%s%s)$.'''
                    % (S, O, S, A, C, S, B, D,
                       A, B, C, D, O, A, C, B, D,
                       S, S, A, C, S, B, D, O, A, C, S, A, C, O, B, D, S, B, D, S, O, S, A, C, S, B, D))

    # Đưa các lời giải vào danh sách lời giải
    list_nb_2 = [loigiai_nb_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_nb = list(zip(list_nb_1, list_nb_2))

    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_nb)

    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

    ######################################################################## Thông hiểu ############################################
    # Các đáp án
    th_da_1_d = '\\True Giao điểm của $%s$ của đường thẳng $%s%s$ và mặt phẳng $(%s%s%s)$ là điểm nằm trên đường thẳng $%s%s$' % (I, A, N, S, B, D, S, O)
    th_da_1_s = 'Giao điểm của $%s$ của đường thẳng $%s%s$ và mặt phẳng $(%s%s%s)$ là điểm nằm trên đường thẳng $%s%s$' % (I, A, N, S, B, D, S, D)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]

    # Nội dung lời giải
    loigiai_th_1 = ('''Tìm giao điểm $%s$ của $%s%s$ và mặt phẳng $(%s%s%s)$:\\\\
    Trong mặt phẳng $(%s%s%s)$, gọi $%s = %s%s \\cap %s%s$.\\\\
    Ta có: $\\begin{cases} %s \\in %s%s \\\\ %s \\in %s%s, %s%s \\subset (%s%s%s) \\end{cases} \\Rightarrow %s = %s%s \\cap (%s%s%s)$.\\\\
    Do đó $%s$ nằm trên đường thẳng $%s%s$.'''
                    % (I, A, N, S, B, D,
                       S, A, C, I, S, O, A, N,
                       I, A, N, I, S, O, S, O, S, B, D, I, A, N, S, B, D,
                       I, S, O))

    # Đưa các lời giải vào danh sách lời giải
    list_th_2 = [loigiai_th_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_th = list(zip(list_th_1, list_th_2))

    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_th)

    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

    ######################################################################## Vận dụng ############################################
    # Các đáp án
    vd_da_1_d = '\\True Giao điểm của $%s$ của đường thẳng $%s%s$ và mặt phẳng $(%s%s%s)$ là điểm nằm trên đường thẳng $%s%s$' % (J, M, N, S, B, D, S, P)
    vd_da_1_s = 'Giao điểm của $%s$ của đường thẳng $%s%s$ và mặt phẳng $(%s%s%s)$ là điểm nằm trên đường thẳng $%s%s$' % (J, M, N, S, B, D, S, D)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]

    # Nội dung lời giải
    loigiai_vd_1 = ('''Tìm giao điểm $%s$ của $%s%s$ và mặt phẳng $(%s%s%s)$:\\\\
    Trong mặt phẳng $(%s%s%s%s)$, gọi $%s = %s%s \\cap %s%s$.\\\\
    Trong mặt phẳng $(%s%s%s)$, gọi $%s = %s%s \\cap %s%s$.\\\\
    Ta có: $\\begin{cases} %s \\in %s%s \\\\ %s \\in %s%s, %s%s \\subset (%s%s%s) \\end{cases} \\Rightarrow %s = %s%s \\cap (%s%s%s)$.\\\\
    Do đó $%s$ nằm trên đường thẳng $%s%s$ (không nằm trên đường thẳng $%s%s$).'''
                    % (J, M, N, S, B, D,
                       A, B, C, D, P, C, M, B, D,
                       S, C, M, J, M, N, S, P,
                       J, M, N, J, S, P, S, P, S, B, D, J, M, N, S, B, D,
                       J, S, P, S, D))

    # Đưa các lời giải vào danh sách lời giải
    list_vd_2 = [loigiai_vd_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_vd = list(zip(list_vd_1, list_vd_2))

    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_vd)

    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

    ######################################################################## Vận dụng cao ############################################
    # Các đáp án
    vdc_da_1_d = '\\True Ba điểm $%s, %s, %s$ thẳng hàng' % (I, J, B)
    vdc_da_1_s = 'Ba điểm $%s, %s, %s$ thẳng hàng' % (I, J, A)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]

    # Nội dung lời giải
    loigiai_vdc_1 = ('''Chứng minh $%s, %s, %s$ thẳng hàng:\\\\
    Dễ thấy $%s \\in (%s%s%s) \\cap (%s%s%s) \\quad (1)$.\\\\
    Ta có: $\\begin{cases} %s \\in %s%s, %s%s \\subset (%s%s%s) \\\\ %s \\in %s%s, %s%s \\subset (%s%s%s) \\end{cases} \\Rightarrow %s \\in (%s%s%s) \\cap (%s%s%s) \\quad (2)$.\\\\
    Tương tự: $\\begin{cases} %s \\in %s%s, %s%s \\subset (%s%s%s) \\\\ %s \\in %s%s, %s%s \\subset (%s%s%s) \\end{cases} \\Rightarrow %s \\in (%s%s%s) \\cap (%s%s%s) \\quad (3)$.\\\\
    Từ (1), (2), (3) suy ra $%s, %s, %s$ cùng thuộc giao tuyến của hai mặt phẳng $(%s%s%s)$ và $(%s%s%s)$ nên ba điểm này thẳng hàng.'''
                     % (I, J, B,
                        B, A, B, N, S, B, D,
                        I, A, N, A, N, A, B, N, I, S, O, S, O, S, B, D, I, A, B, N, S, B, D,
                        J, M, N, M, N, A, B, N, J, S, P, S, P, S, B, D, J, A, B, N, S, B, D,
                        B, I, J, A, B, N, S, B, D))

    # Đưa các lời giải vào danh sách lời giải
    list_vdc_2 = [loigiai_vdc_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))

    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_vdc)

    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
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
        '\\begin{ex}\n' +
        str(noidungcauhoi) + '\n' +
        '\\choiceTFn \n'
        '{' + str(shuffled_answers_nb[0]) + '}\n'
        '{' + str(shuffled_answers_th[0]) + '}\n'
        '{' + str(shuffled_answers_vd[0]) + '}\n'
        '{' + str(shuffled_answers_vdc[0]) + '}\n'
        '\\loigiai{ \n' +
        tikz_str + '\n'
        '\\begin{enumEX}[a)]{1} \n'
        '\\item ' + str(shuffled_solutions_nb[0]) + '\n'
        '\\item ' + str(shuffled_solutions_th[0]) + '\n'
        '\\item ' + str(shuffled_solutions_vd[0]) + '\n'
        '\\item ' + str(shuffled_solutions_vdc[0]) + '\n'
        '\\end{enumEX}} \n'
        '\\end{ex}\n\\end{minipage}\n\n')
    return content


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


def bt_dang9_p2_b2_c1_hh11(self):
    # Random các thông số của bài toán
    # Cho AB là số chẵn từ 4 đến 8
    AB_val = random.choice([4, 6, 8])
    DC_val = AB_val // 2
    h_val = random.choice([2, 3])
    canh_ben = AB_val

    # Tính toán các độ dài và diện tích thiết diện IJKN
    IJ_val = Rational(AB_val + DC_val, 2)
    NK_val = Rational(AB_val, 2)
    S_thiet_dien = Rational(IJ_val + NK_val, 2) * h_val

    def format_number(val):
        if isinstance(val, Rational):
            if val.q == 1:
                return str(val.p)
            f_val = float(val)
            if f_val.is_integer():
                return str(int(f_val))
            return str(f_val).replace('.', ',')
        elif isinstance(val, (int, float)):
            s = str(val)
            return s.replace('.', ',')
        return str(val)

    S_dung_str = format_number(S_thiet_dien)
    # Tạo giá trị sai cho câu d bằng cách cộng thêm 0.5 (hoặc 1)
    S_sai_val = S_thiet_dien + Rational(1, 2)
    S_sai_str = format_number(S_sai_val)

    IJ_str = format_number(IJ_val)
    NK_str = format_number(NK_val)

    # Hình vẽ TikZ vẽ chuẩn theo ảnh (đã bỏ lưới ô vuông, nét vẽ 1pt, điểm 1pt, màu đen)
    hinh_ve = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (S) at (2.4, 4.0);
    \\coordinate (A) at (0.2, 1.4);
    \\coordinate (B) at (4.2, 1.35);
    \\coordinate (D) at (1.3, -0.6);
    \\coordinate (C) at (3.5, -0.6);
    \\coordinate (O) at (2.3, 0.1);
    \\coordinate (I) at ($(A)!0.5!(D)$);
    \\coordinate (J) at ($(B)!0.5!(C)$);
    \\coordinate (K) at ($(S)!0.5!(B)$);
    \\coordinate (N) at ($(S)!0.5!(A)$);
    \\coordinate (x_left) at (-0.8, 4.0);
    \\coordinate (x_right) at (5.8, 4.0);
    \\draw[line width=1pt] (x_left)--(x_right);
    \\draw[line width=1pt] (S)--(A) (S)--(D) (S)--(C) (S)--(B);
    \\draw[line width=1pt] (A)--(D)--(C)--(B);
    \\draw[line width=1pt] (N)--(K);
    \\draw[line width=1pt, dashed] (A)--(B);
    \\draw[line width=1pt, dashed] (A)--(C) (B)--(D);
    \\draw[line width=1pt, dashed] (S)--(O);
    \\draw[line width=1pt, dashed] (I)--(K);
    \\draw[line width=1pt, dashed] (I)--(J);
    \\fill (S) circle (1pt) node[above right] {$S$};
    \\fill (A) circle (1pt) node[left] {$A$};
    \\fill (B) circle (1pt) node[right] {$B$};
    \\fill (C) circle (1pt) node[below right] {$C$};
    \\fill (D) circle (1pt) node[below] {$D$};
    \\fill (O) circle (1pt) node[below] {$O$};
    \\fill (I) circle (1pt) node[below left] {$I$};
    \\fill (J) circle (1pt) node[below right] {$J$};
    \\fill (K) circle (1pt) node[above right] {$K$};
    \\fill (N) circle (1pt) node[left] {$N$};
    \\end{tikzpicture}
    \\end{center}''')

    # Nội dung câu hỏi
    noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy là hình thang, đáy lớn $AB$. Gọi $I, J, K$ lần lượt là trung điểm của $AD, BC, SB$. Khi đó:''')

    ########################################################################
    # Nhận biết ############################################
    # Các đáp án
    nb_da_1_d = '\\True Giao tuyến của mặt phẳng $(IJK)$ với mặt phẳng $(SBC)$ là $JK$'
    nb_da_1_s = 'Giao tuyến của mặt phẳng $(IJK)$ với mặt phẳng $(SBC)$ là $IK$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]

    # Nội dung lời giải
    loigiai_nb_1 = ('''Ta có: \\\\
    $\\begin{cases} K \\in SB \\subset (SBC) \\\\ K \\in (IJK) \\end{cases} \\Rightarrow K$ là điểm chung thứ nhất. \\\\
    $\\begin{cases} J \\in BC \\subset (SBC) \\\\ J \\in (IJK) \\end{cases} \\Rightarrow J$ là điểm chung thứ hai. \\\\
    Vậy giao tuyến của mặt phẳng $(IJK)$ với mặt phẳng $(SBC)$ là $KJ$.''')

    # Đưa các lời giải vào danh sách lời giải
    list_nb_2 = [loigiai_nb_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

    ########################################################################
    # Thông hiểu ############################################
    # Các đáp án
    th_da_1_d = 'Giao tuyến của mặt phẳng $(SAB)$ và $(SCD)$ là $Sx$ thỏa mãn điều kiện song song với $AB$, song song với $BC$'
    th_da_1_s = '\\True Giao tuyến của mặt phẳng $(SAB)$ và $(SCD)$ là $Sx$ thỏa mãn điều kiện song song với $AB$, song song với $CD$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]

    # Nội dung lời giải
    loigiai_th_1 = ('''Ta có: \\\\
    $\\begin{cases} S \\in (SAB) \\\\ S \\in (SCD) \\end{cases} \\Rightarrow S$ là điểm chung thứ nhất. \\\\
    $\\begin{cases} AB \\subset (SAB) \\\\ DC \\subset (SDC) \\\\ AB // DC \\end{cases} \\Rightarrow$ Giao tuyến là $Sx // AB // CD$.''')

    # Đưa các lời giải vào danh sách lời giải
    list_th_2 = [loigiai_th_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

    ########################################################################
    # Vận dụng ############################################
    # Các đáp án
    vd_da_1_d = '\\True Giao điểm của $SA$ và $(IJK)$ là $N$, với $N$ là giao điểm của $Kx$ với $SA$ ($Kx // AB // DC$)'
    vd_da_1_s = 'Giao điểm của $SA$ và $(IJK)$ là $N$, với $N$ là trung điểm của $SD$'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]

    # Nội dung lời giải
    loigiai_vd_1 = ('''Ta có: \\\\
    - $SA$ nằm trong mặt phẳng $(SAB)$. \\\\
    - $(SAB) \\cap (IJK)$ theo giao tuyến là $Kx // AB // IJ // DC$. \\\\
    Kéo dài $Kx$ cắt $SA$ tại $N$. \\\\
    $\\Rightarrow N$ là giao điểm cần tìm.''')

    # Đưa các lời giải vào danh sách lời giải
    list_vd_2 = [loigiai_vd_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

    ########################################################################
    # Vận dụng cao ############################################
    # Các đáp án
    vdc_da_1_d = ('Diện tích thiết diện cắt bởi mặt phẳng $(IJK)$ và hình chóp là $%s$ (biết thiết diện có chiều cao bằng $%s$, $SA = SB = SC = SD = %s$, $AB = 2DC = %s$)'
                  % (S_sai_str, format_number(h_val), format_number(canh_ben), format_number(AB_val)))
    vdc_da_1_s = ('\\True Diện tích thiết diện cắt bởi mặt phẳng $(IJK)$ và hình chóp là $%s$ (biết thiết diện có chiều cao bằng $%s$, $SA = SB = SC = SD = %s$, $AB = 2DC = %s$)'
                  % (S_dung_str, format_number(h_val), format_number(canh_ben), format_number(AB_val)))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]

    # Nội dung lời giải
    loigiai_vdc_1 = ('''Ta có: $IJ = \\dfrac{AB + CD}{2} = \\dfrac{%s + %s}{2} = %s$, $NK = \\dfrac{1}{2} AB = %s$, $h = %s$. \\\\
    Thiết diện cắt bởi mp $(IJK)$ và hình chóp là hình thang $IJKN$ có diện tích là \\\\
    $S = \\dfrac{IJ + NK}{2} \\cdot h = \\dfrac{%s + %s}{2} \\cdot %s = %s$.'''
                     % (format_number(AB_val), format_number(DC_val), IJ_str, NK_str, format_number(h_val),
                        IJ_str, NK_str, format_number(h_val), S_dung_str))

    # Đưa các lời giải vào danh sách lời giải
    list_vdc_2 = [loigiai_vdc_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
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
        str(hinh_ve) + '\n'
        '\\begin{enumEX}[a)]{1} \n'
        '\\item ' + str(shuffled_solutions_nb[0]) + '\n'
        '\\item ' + str(shuffled_solutions_th[0]) + '\n'
        '\\item ' + str(shuffled_solutions_vd[0]) + '\n'
        '\\item ' + str(shuffled_solutions_vdc[0]) + '\n'
        '\\end{enumEX}} \n'
        '\\end{ex}\n \\end{minipage}\n\n')
    return content


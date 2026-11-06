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


def bt_dang10_p2_b2_c1_hh11(self):
    # Khai báo các đối tượng trong bài toán
    hinh_chop = "S.ABCD"
    hinh_day = "ABCD"
    tam_day = "O"

    # Khai báo biến ngẫu nhiên cho câu hỏi (random thứ tự hoặc tên gọi trung điểm giữ tính tổng quát)
    diem_1 = "SB"
    diem_2 = "SD"
    trung_diem_1 = "I"
    trung_diem_2 = "K"

    # Nội dung câu hỏi
    noidungcauhoi = ('''Cho hình chóp $%s$, có đáy $%s$ là một hình bình hành tâm $%s$. Gọi $%s,%s$ lần lượt là trung điểm của $%s$ và $%s$. Khi đó:'''
                     % (hinh_chop, hinh_day, tam_day, trung_diem_1, trung_diem_2, diem_1, diem_2))

    # Hình vẽ TikZ vẽ chuẩn 100% theo mẫu ảnh (nét vẽ 1pt, điểm 1pt, màu đen)
    hinh_ve = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (S) at (1.2, 4.3);
    \\coordinate (A) at (1.2, 0.8);
    \\coordinate (B) at (-0.3, -0.7);
    \\coordinate (C) at (4.5, -0.7);
    \\coordinate (D) at (6.0, 0.8);
    \\coordinate (O) at ($(A)!0.5!(C)$);
    \\coordinate (I) at ($(S)!0.5!(B)$);
    \\coordinate (K) at ($(S)!0.5!(D)$);
    \\coordinate (J) at ($(S)!0.5!(A)$);
    \\coordinate (x_end) at ($(K)+(1.2,0)$);
    \\coordinate (y_top) at ($(I)+(-0.6,0.9)$);
    \\coordinate (y_bot) at ($(C)+(0.6,-0.9)$);
    \\draw[line width=1pt] (y_top)--(I) (C)--(y_bot);
    \\draw[line width=1pt] (K)--(x_end) node[above left] {$x$};
    \\draw[line width=1pt] (S)--(B) (S)--(C) (S)--(D);
    \\draw[line width=1pt] (B)--(C)--(D);
    \\draw[line width=1pt] (K)--(C);
    \\draw[line width=1pt, dashed] (S)--(A) (A)--(B) (A)--(D);
    \\draw[line width=1pt, dashed] (A)--(C) (B)--(D) (S)--(O);
    \\draw[line width=1pt, dashed] (J)--(K) (I)--(J) (I)--(K);
    \\draw[line width=1pt, dashed] (I)--(O) (K)--(O) (O)--(J);
    \\draw[line width=1pt, dashed] (I)--(y_top) (I)--(C) (J)--(C);
    \\fill (S) circle (1pt) node[above] {$S$};
    \\fill (A) circle (1pt) node[left] {$A$};
    \\fill (B) circle (1pt) node[below left] {$B$};
    \\fill (C) circle (1pt) node[below] {$C$};
    \\fill (D) circle (1pt) node[right] {$D$};
    \\fill (O) circle (1pt) node[below] {$O$};
    \\fill (I) circle (1pt) node[left] {$I$};
    \\fill (K) circle (1pt) node[above right] {$K$};
    \\fill (J) circle (1pt) node[left] {$J$};
    \\node[above left] at (y_top) {$y$};
    \\end{tikzpicture}
    \\end{center}''')

    ########################################################################
    # Nhận biết ############################################
    # Các đáp án
    nb_da_1_d = '\\True $SO$ là giao tuyến của $(SAC)$ và $(SBD)$'
    nb_da_1_s = '$SI$ là giao tuyến của $(SAC)$ và $(SBD)$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]

    # Nội dung lời giải
    loigiai_nb_1 = ('''Ta có: \\\\
    $\\begin{cases} O \\in AC \\subset (SAC) \\\\ O \\in BD \\subset (SBD) \\end{cases} \\Rightarrow O \\in (SAC) \\cap (SBD)$. \\\\
    $S \\in (SAC) \\cap (SBD)$. \\\\
    $\\Rightarrow SO = (SAC) \\cap (SBD)$.''')

    # Đưa các lời giải vào danh sách lời giải
    list_nb_2 = [loigiai_nb_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

    ########################################################################
    # Thông hiểu ############################################
    # Các đáp án
    th_da_1_d = '\\True Giao điểm $J$ của $SA$ với $(CKB)$ thuộc đường thẳng đi qua $K$ và song song với $DC$'
    th_da_1_s = 'Giao điểm $J$ của $SA$ với $(CKB)$ thuộc đường thẳng đi qua $K$ và song song với $SD$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]

    # Nội dung lời giải
    loigiai_th_1 = ('''Tứ giác $ABCD$ là hình bình hành nên $AB // CD; AD // BC$. \\\\
    Ta có: $\\begin{cases} AD // CB \\\\ AD \\subset (SAD) \\\\ BC \\subset (KBC) \\\\ K \\in (KBC) \\cap (SAD) \\end{cases} \\Rightarrow \\begin{cases} Kx = (KBC) \\cap (SAD) \\\\ Kx // AD // BC \\end{cases}$. \\\\
    Trong $(SAD)$ gọi $J = Kx \\cap SA$, có $\\Rightarrow \\begin{cases} J \\in SA \\\\ J \\in Kx \\subset (BKC) \\end{cases} \\Rightarrow J = SA \\cap (BKC)$.''')

    # Đưa các lời giải vào danh sách lời giải
    list_th_2 = [loigiai_th_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

    ########################################################################
    # Vận dụng ############################################
    # Các đáp án
    vd_da_1_d = '\\True Giao tuyến của $(OIA)$ và $(SCD)$ là đường thẳng đi qua $C$ và song song với $SD$'
    vd_da_1_s = 'Giao tuyến của $(OIA)$ và $(SCD)$ là đường thẳng đi qua $C$ và song song với $SC$'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]

    # Nội dung lời giải
    loigiai_vd_1 = ('''Ta có $OI$ là đường trung bình của $\\Delta SBD \\Rightarrow OI // SD$. \\\\
    Ta có: $\\begin{cases} OI // SD \\\\ OI \\subset (OIA) \\\\ SD \\subset (SCD) \\\\ C \\in (OIA) \\cap (SCD) \\end{cases} \\Rightarrow \\begin{cases} Cy = (OIA) \\cap (SCD) \\\\ Cy // SD // OI \\end{cases}$.''')

    # Đưa các lời giải vào danh sách lời giải
    list_vd_2 = [loigiai_vd_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

    ########################################################################
    # Vận dụng cao ############################################
    # Các đáp án
    vdc_da_1_d = '\\True $CD // IJ$'
    vdc_da_1_s = '$CD$ cắt $IJ$'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]

    # Nội dung lời giải
    loigiai_vdc_1 = ('''Ta có: $IJ // AB$ ($IJ$ là đường trung bình của $\\Delta SAB$) \\\\
    $AB // CD$ (tứ giác $ABCD$ là hình bình hành) $\\Rightarrow CD // IJ$.''')

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


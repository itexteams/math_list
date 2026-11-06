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


def bt_dang7_p2_b2_c1_hh11(self):
    # Khai báo các đối tượng trong bài toán
    hinh_chop = "S.ABCD"
    day = "ABCD"

    # Nội dung câu hỏi
    noidungcauhoi = ('''Cho hình chóp $%s$ có đáy $%s$ là hình bình hành.'''
                     %(hinh_chop, day))

    # Hình vẽ TikZ dùng chung cho lời giải
    hinh_ve = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,0);
    \\coordinate (B) at (4,0);
    \\coordinate (D) at (-1.8,-1.8);
    \\coordinate (C) at (2.2,-1.8);
    \\coordinate (S) at (0,3.5);
    \\coordinate (M) at ($(S)!0.6!(C)$);
    \\coordinate (N) at ($(S)!0.55!(B)$);
    \\coordinate (x1) at ($(S)+(-1.8,0)$);
    \\coordinate (x2) at ($(S)+(3.5,0)$);
    \\coordinate (y1) at ($(S)+(-1.3,-1.3)$);
    \\coordinate (y2) at ($(S)+(1,1)$);
    \\coordinate (t1) at ($(M)+(-2.5,0)$);
    \\coordinate (t2) at ($(M)+(2.7,0)$);
    \\coordinate (z1) at ($(N)+(-3.8,0)$);
    \\coordinate (z2) at ($(N)+(1.5,0)$);
    \\draw[line width=1pt] (x1)--(x2) node[above left] {$x$};
    \\draw[line width=1pt] (y1)--(y2) node[above left] {$y$};
    \\draw[line width=1pt] (t1)--(t2) node[above left] {$t$};
    \\draw[line width=1pt] (N)--(z2) node[above left] {$z$};
    \\draw[line width=1pt, dashed] (z1)--(N);
    \\draw[line width=1pt] (S)--(D) (S)--(C) (S)--(B) (D)--(C)--(B) (M)--(B) (C)--(N);
    \\draw[line width=1pt, dashed] (S)--(A) (A)--(B) (A)--(D) (A)--(M) (D)--(N);
    \\fill (A) circle (1pt) node[left] {$A$};
    \\fill (B) circle (1pt) node[right] {$B$};
    \\fill (C) circle (1pt) node[below] {$C$};
    \\fill (D) circle (1pt) node[below left] {$D$};
    \\fill (S) circle (1pt) node[above left] {$S$};
    \\fill (M) circle (1pt) node[above right] {$M$};
    \\fill (N) circle (1pt) node[above right] {$N$};
    \\end{tikzpicture}
    \\end{center}''')

    ########################################################################
    # Nhận biết ############################################
    # Các đáp án
    nb_da_1_d = '\\True Giao tuyến của $(SAB)$ và $(SCD)$ là đường thẳng đi qua $S$ và song song với $AB$'
    nb_da_1_s = 'Giao tuyến của $(SAB)$ và $(SCD)$ là đường thẳng đi qua $S$ và song song với $AD$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]

    # Nội dung lời giải
    loigiai_nb_1 = ('''Ta có: $\\begin{cases} AB // CD \\\\ AB \\subset (SAB) \\\\ CD \\subset (SCD) \\\\ S \\in (SAB) \\cap (SCD) \\end{cases} \\Rightarrow \\begin{cases} Sx = (SAB) \\cap (SCD) \\\\ Sx // AB // CD \\end{cases}$''')

    # Đưa các lời giải vào danh sách lời giải
    list_nb_2 = [loigiai_nb_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

    ########################################################################
    # Thông hiểu ############################################
    # Các đáp án
    th_da_1_d = '\\True Giao tuyến của $(SAD)$ và $(SBC)$ là đường thẳng đi qua $S$ và song song với $AD$'
    th_da_1_s = 'Giao tuyến của $(SAD)$ và $(SBC)$ là đường thẳng đi qua $S$ và song song với $AB$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]

    # Nội dung lời giải
    loigiai_th_1 = ('''Ta có: $\\begin{cases} AD // BC \\\\ AD \\subset (SAD) \\\\ BC \\subset (SBC) \\\\ S \\in (SAD) \\cap (SBC) \\end{cases} \\Rightarrow \\begin{cases} Sy = (SAD) \\cap (SBC) \\\\ Sy // AD // BC \\end{cases}$''')

    # Đưa các lời giải vào danh sách lời giải
    list_th_2 = [loigiai_th_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

    ########################################################################
    # Vận dụng ############################################
    # Các đáp án
    vd_da_1_d = '\\True Gọi $M \\in SC$, giao tuyến của $(ABM)$ và $(SCD)$ là đường thẳng đi qua $M$ và song song với $AB$'
    vd_da_1_s = 'Gọi $M \\in SC$, giao tuyến của $(ABM)$ và $(SCD)$ là đường thẳng đi qua $M$ và song song với $SC$'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]

    # Nội dung lời giải
    loigiai_vd_1 = ('''Ta có: $\\begin{cases} AB // CD \\\\ AB \\subset (MAB) \\\\ CD \\subset (SCD) \\\\ M \\in (MAB) \\cap (SCD) \\end{cases} \\Rightarrow \\begin{cases} Mt = (MAB) \\cap (SCD) \\\\ Mt // AB // CD \\end{cases}$''')

    # Đưa các lời giải vào danh sách lời giải
    list_vd_2 = [loigiai_vd_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

    ########################################################################
    # Vận dụng cao ############################################
    # Các đáp án
    vdc_da_1_d = '\\True Gọi $N \\in SB$, giao tuyến của $(SAB)$ và $(NCD)$ là đường thẳng đi qua $N$ và song song với $AB$'
    vdc_da_1_s = 'Gọi $N \\in SB$, giao tuyến của $(SAB)$ và $(NCD)$ là đường thẳng đi qua $N$ và song song với $BC$'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]

    # Nội dung lời giải
    loigiai_vdc_1 = ('''Ta có: $\\begin{cases} AB // CD \\\\ AB \\subset (SAB) \\\\ CD \\subset (NCD) \\\\ N \\in (SAB) \\cap (NCD) \\end{cases} \\Rightarrow \\begin{cases} Nz = (SAB) \\cap (NCD) \\\\ Nz // AB // CD \\end{cases}$''')

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


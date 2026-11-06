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


def bt_dang12_p2_b2_c1_hh11(self):
    # Khai báo các đối tượng trong bài toán
    hinh_chop = "S.ABCD"
    hinh_day = "ABCD"
    diem_M = "M"
    diem_N = "N"
    canh_SA = "SA"
    canh_SB = "SB"
    giao_cheo = "O"

    # Random hệ số trong câu d (đẳng thức dạng SE = k * BC)
    k_val = random.choice([2, 3, 4])

    # Nội dung câu hỏi
    noidungcauhoi = ('''Cho hình chóp $%s$ có đáy $%s$ là hình bình hành. Gọi $%s, %s$ lần lượt là trung điểm của $%s, %s$, $%s$ là giao điểm của $AC$ và $BD$. Xét tính đúng sai các khẳng định sau:'''
                     % (hinh_chop, hinh_day, diem_M, diem_N, canh_SA, canh_SB, giao_cheo))

    # Hình vẽ TikZ chuẩn 100% như ảnh cung cấp (nét vẽ 1pt, điểm 1pt, màu đen)
    hinh_ve = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (S) at (2.2, 4.2);
    \\coordinate (A) at (3.0, 1.4);
    \\coordinate (B) at (1.4, -0.3);
    \\coordinate (C) at (5.5, -0.3);
    \\coordinate (D) at (7.1, 1.4);
    \\coordinate (O) at (intersection of A--C and B--D);
    \\coordinate (M) at ($(S)!0.5!(A)$);
    \\coordinate (N) at ($(S)!0.5!(B)$);
    \\coordinate (E) at (-1.8, 4.2);
    \\coordinate (y_end) at (7.5, 4.2);
    \\coordinate (left_ext) at (-2.0, 4.2);
    \\draw[line width=1pt] (left_ext)--(y_end) node[above left] {$y$};
    \\draw[line width=1pt] (E)--(M);
    \\draw[line width=1pt] (S)--(B) (S)--(C) (S)--(D);
    \\draw[line width=1pt] (B)--(C)--(D);
    \\draw[line width=1pt, dashed] (S)--(A) (A)--(B) (A)--(D);
    \\draw[line width=1pt, dashed] (A)--(C) (B)--(D);
    \\draw[line width=1pt, dashed] (S)--(O);
    \\draw[line width=1pt, dashed] (M)--(D) (M)--(N);
    \\fill (S) circle (1pt) node[above] {$S$};
    \\fill (A) circle (1pt) node[right] {$A$};
    \\fill (B) circle (1pt) node[below left] {$B$};
    \\fill (C) circle (1pt) node[below right] {$C$};
    \\fill (D) circle (1pt) node[above right] {$D$};
    \\fill (O) circle (1pt) node[below] {$O$};
    \\fill (M) circle (1pt) node[above right] {$M$};
    \\fill (N) circle (1pt) node[left] {$N$};
    \\fill (E) circle (1pt) node[above] {$E$};
    \\end{tikzpicture}
    \\end{center}''')

    ########################################################################
    # Nhận biết ############################################
    # Các đáp án
    nb_da_1_d = 'Giao điểm của đường thẳng $SA$ và $(ABCD)$ là điểm $D$'
    nb_da_1_s = '\\True Giao điểm của đường thẳng $SA$ và $(ABCD)$ là điểm $A$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]

    # Nội dung lời giải
    loigiai_nb_1 = ('''Giao điểm của đường thẳng $SA$ và $(ABCD)$ là điểm $A$. \\\\
    Ta có $SA \\cap (ABCD) = \\{A\\}$.''')

    # Đưa các lời giải vào danh sách lời giải
    list_nb_2 = [loigiai_nb_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

    ########################################################################
    # Thông hiểu ############################################
    # Các đáp án
    th_da_1_d = '\\True Giao điểm của đường thẳng $BD$ và $(SAC)$ là trung điểm của đoạn thẳng $AC$'
    th_da_1_s = 'Giao điểm của đường thẳng $BD$ và $(SAC)$ là trung điểm của đoạn thẳng $SA$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]

    # Nội dung lời giải
    loigiai_th_1 = ('''Giao điểm của đường thẳng $BD$ và $(SAC)$ là trung điểm của đoạn thẳng $AC$. \\\\
    Ta có: $\\begin{cases} O \\in BD \\\\ O \\in AC \\subset (SAC) \\end{cases} \\Rightarrow BD \\cap (SAC) = \\{O\\}$, với $O$ là trung điểm của $AC$.''')

    # Đưa các lời giải vào danh sách lời giải
    list_th_2 = [loigiai_th_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

    ########################################################################
    # Vận dụng ############################################
    # Các đáp án
    vd_da_1_d = 'Giao điểm của đường thẳng $SO$ và $(ABNM)$ là điểm $D$'
    vd_da_1_s = '\\True Giao điểm của đường thẳng $SO$ và $(ABNM)$ là điểm $S$'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]

    # Nội dung lời giải
    loigiai_vd_1 = ('''Giao điểm của đường thẳng $SO$ và $(ABNM)$ là điểm $S$. \\\\
    Ta có: $\\begin{cases} S \\in SO \\\\ S \\in AM \\subset (ABNM) \\end{cases} \\Rightarrow SO \\cap (ABNM) = \\{S\\}$.''')

    # Đưa các lời giải vào danh sách lời giải
    list_vd_2 = [loigiai_vd_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

    ########################################################################
    # Vận dụng cao ############################################
    # Các đáp án
    vdc_da_1_d = ('Gọi $E$ là giao điểm của $DM$ và mặt phẳng $(SBC)$. Khi đó $SE = %s BC$' % (str(k_val)))
    vdc_da_1_s = '\\True Gọi $E$ là giao điểm của $DM$ và mặt phẳng $(SBC)$. Khi đó $SE = BC$'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]

    # Nội dung lời giải
    loigiai_vdc_1 = ('''Gọi $E$ là giao điểm của $DM$ và mặt phẳng $(SBC)$. \\\\
    Ta có: $\\begin{cases} S \\in (SAD) \\cap (SBC) \\\\ AD // BC \\text{ ($ABCD$ là hình bình hành)} \\\\ AD \\subset (SAD) \\\\ BC \\subset (SBC) \\end{cases}$ \\\\
    $\\Rightarrow (SAD) \\cap (SBC) = Sy$ ($Sy // AD // BC$). \\\\
    Trong mặt phẳng $(SAD)$, gọi $E = Sy \\cap DM$. \\\\
    $\\begin{cases} E \\in Sy \\subset (SBC) \\\\ E \\in DM \\end{cases} \\Rightarrow E = DM \\cap (SBC)$. \\\\
    Vì $M$ là trung điểm của $SA$ và $SE // AD$ nên tứ giác $SEAD$ là hình bình hành. \\\\
    $\\Rightarrow SE = AD = BC$.''')

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


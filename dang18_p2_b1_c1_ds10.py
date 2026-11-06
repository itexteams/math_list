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


def bt_dang18_p2_b1_c1_ds10(self):
    # Khai báo biến
    # Tạo các tham số ngẫu nhiên
    # Câu a: Random tập hợp
    A_val = sorted(random.sample(range(0, 6), 4))
    B_val = sorted(random.sample(A_val, 3))
    str_A = "; ".join(map(str, A_val))
    str_B = "; ".join(map(str, B_val))

    # Câu b: Random số nguyên k
    k = random.randint(2, 5)

    # Câu d: Random bội số
    m1 = random.randint(2, 4)
    m2 = m1 * random.randint(2, 3)

    # Nội dung câu hỏi
    noidungcauhoi = ('Các câu sau là đúng hay sai?')

    ########################################################################
    # Nhận biết - Câu a: Tập hợp con
    # Kiểm tra A subset B (Thường là sai vì A có nhiều phần tử hơn)
    nb_da_1_d = '\\True Với hai tập $A = \\{%s\\}$ và $B = \\{%s\\}$, ta có $A \\subset B$' % (str_A, str_B)
    nb_da_1_s = 'Với hai tập $A = \\{%s\\}$ và $B = \\{%s\\}$, ta có $A \\not\\subset B$' % (str_A, str_B)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    loigiai_nb_1 = ('Ta có các phần tử của $A$ không phải đều thuộc $B$, nên $A \\not\\subset B$. Khẳng định $A \\subset B$ là sai.')

    ########################################################################
    # Thông hiểu - Câu b: Bằng nhau
    th_da_1_d = '\\True Với hai tập $C = \\{x \\in \\mathbb{R} | x^2 = %d^2\\}$ và $D = \\{x \\in \\mathbb{R} | |x| = %d\\}$, ta có $C = D$' % (k, k)
    th_da_1_s = 'Với hai tập $C = \\{x \\in \\mathbb{R} | x^2 = %d^2\\}$ và $D = \\{x \\in \\mathbb{R} | |x| = %d\\}$, ta có $C \\neq D$' % (k, k)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    loigiai_th_1 = ('Phương trình $x^2 = %d^2 \\Leftrightarrow x = \\pm %d$. Phương trình $|x| = %d \\Leftrightarrow x = \\pm %d$. Vậy $C = D = \\{-%d; %d\\}$.' % (k, k, k, k, k, k))

    ########################################################################
    # Vận dụng - Câu c: Tập hợp hình học
    vd_da_1_d = '\\True Với $E$ là tập các hình bình hành và $F$ là tập các tứ giác có hai cặp cạnh đối song song, ta có $E = F$'
    vd_da_1_s = 'Với $E$ là tập các hình bình hành và $F$ là tập các tứ giác có hai cặp cạnh đối song song, ta có $E \\neq F$'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    loigiai_vd_1 = ('Theo định nghĩa, hình bình hành là tứ giác có hai cặp cạnh đối song song. Vậy $E = F$.')

    ########################################################################
    # Vận dụng cao - Câu d: Bội số
    # G = bội của m1, H = bội của m2 (m2 là bội của m1 -> G không subset H)
    vdc_da_1_d = '\\True Với hai tập $G = \\{x \\in \\mathbb{N} | x \\text{ là bội của } %d\\}$ và $H = \\{x \\in \\mathbb{N} | x \\text{ là bội của } %d\\}$, ta có $G \\subset H$' % (m1, m2)
    vdc_da_1_s = 'Với hai tập $G = \\{x \\in \\mathbb{N} | x \\text{ là bội của } %d\\}$ và $H = \\{x \\in \\mathbb{N} | x \\text{ là bội của } %d\\}$, ta có $G \\not\\subset H$' % (m1, m2)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    loigiai_vdc_1 = ('Vì $%d$ là bội của $%d$ nên $G$ không thể là tập con của $H$. Ví dụ $%d \\in G$ nhưng $%d \\notin H$.' % (m2, m1, m1, m1))

    ########################################################################
    # Logic xử lý
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

    # Gán lại vào list để shuffle
    list_nb_1 = [nb_da_1]
    list_th_1 = [th_da_1]
    list_vd_1 = [vd_da_1]
    list_vdc_1 = [vdc_da_1]

    # Kết hợp
    combined_nb = list(zip(list_nb_1, [loigiai_nb_1]))
    combined_th = list(zip(list_th_1, [loigiai_th_1]))
    combined_vd = list(zip(list_vd_1, [loigiai_vd_1]))
    combined_vdc = list(zip(list_vdc_1, [loigiai_vdc_1]))

    # Xáo trộn
    random.shuffle(combined_nb)
    random.shuffle(combined_th)
    random.shuffle(combined_vd)
    random.shuffle(combined_vdc)

    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+
        str(noidungcauhoi)+ '\n'
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
        '\\end{ex}\n \\end{minipage} \n\n')
    return content


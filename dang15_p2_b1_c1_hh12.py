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


def bt_dang15_p2_b1_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Sinh ngẫu nhiên kích thước hình hộp chữ nhật ABCD.A'B'C'D'[cite: 26]
    # AB = a, AD = b, AA' = c đôi một khác nhau[cite: 26]
    while True:
        a_len = random.choice([1, 2, 3])
        b_len = random.choice([2, 3, 4])
        c_len = random.choice([3, 4, 5])
    
        if len({a_len, b_len, c_len}) == 3:
            break
    
    # 1. Khẳng định a: |BD| = sqrt(a^2 + b^2)[cite: 26]
    bd_sq = a_len**2 + b_len**2
    str_bd_true = latex(sp.sqrt(bd_sq))
    str_bd_false = latex(sp.sqrt(bd_sq + random.choice([-2, -1, 1, 2])))
    if str_bd_false == str_bd_true:
        str_bd_false = "\\sqrt{5}"[cite: 26]
    
    # 2. Khẳng định b: |BC'| = |AB'|[cite: 26]
    # |BC'|^2 = b^2 + c^2; |AB'|^2 = a^2 + c^2. Vì a != b nên |BC'| != |AB'| (luôn sai)[cite: 26]
    bc_prime_sq = b_len**2 + c_len**2
    ab_prime_sq = a_len**2 + c_len**2
    
    # 3. Khẳng định c: \vec{A'B} = \vec{C'D} (luôn sai vì \vec{A'B} = \vec{D'C} = -\vec{C'D})[cite: 26]
    
    # 4. Khẳng định d: Độ dài của véctơ AM với M là trung điểm CC'[cite: 26]
    # Gắn hệ tọa độ A(0;0;0): A(0;0;0), B(a;0;0), D(0;b;0), C(a;b;0), C'(a;b;c)[cite: 26]
    # M là trung điểm CC' => M(a; b; c/2)[cite: 26]
    # AM^2 = a^2 + b^2 + (c/2)^2 = a^2 + b^2 + c^2/4 = (4(a^2 + b^2) + c^2)/4[cite: 26]
    am_sq_num = 4 * (a_len**2 + b_len**2) + c_len**2
    str_am_true = "\\frac{\\sqrt{%s}}{2}" % (am_sq_num)
    str_am_false = "\\frac{\\sqrt{%s}}{2}" % (am_sq_num + random.choice([-3, -2, 2, 3]))
    if str_am_false == str_am_true:
        str_am_false = "\\frac{\\sqrt{29}}{2}"[cite: 26]
    
    # Nội dung câu hỏi[cite: 26]
    noidungcauhoi = (
        """Cho hình hộp chữ nhật $ABCD.A'B'C'D'$ có $AB = %s, AD = %s$ và $AA' = %s$. Gọi $M$ là trung điểm của $CC'$."""
        % (a_len, b_len, c_len)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: |BD| = ...[cite: 26]
    nb_da_1_d = "\\True $|\\vec{BD}| = %s$" % (str_bd_true)
    nb_da_1_s = "$|\\vec{BD}| = %s$" % (str_bd_false)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Đáy $ABCD$ của hình hộp chữ nhật là hình chữ nhật có $AB = %s, AD = %s$. \\\\ Tam giác $ABD$ vuông tại $A$, theo định lý Pythagore ta có: \\\\ $BD = \\sqrt{AB^2 + AD^2} = \\sqrt{(%s)^2 + (%s)^2} = \\sqrt{%s} = %s$. \\\\ Khi đó độ dài của vectơ $\\vec{BD}$ là: \\\\ $|\\vec{BD}| = BD = %s$."""
        % (
            a_len,
            b_len,
            a_len,
            b_len,
            bd_sq,
            str_bd_true,
            str_bd_true,
        )
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: |BC'| = |AB'|[cite: 26]
    th_da_1_d = "\\True $|\\vec{BC'}| \\neq |\\vec{AB'}|$"
    th_da_1_s = "$|\\vec{BC'}| = |\\vec{AB'}|$"
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Xét tam giác vuông $BCC'$ vuông tại $C$, ta có: \\\\ $|\\vec{BC'}| = BC' = \\sqrt{BC^2 + CC'^2} = \\sqrt{AD^2 + AA'^2} = \\sqrt{(%s)^2 + (%s)^2} = \\sqrt{%s}$. \\\\ Xét tam giác vuông $ABB'$ vuông tại $B$, ta có: \\\\ $|\\vec{AB'}| = AB' = \\sqrt{AB^2 + BB'^2} = \\sqrt{AB^2 + AA'^2} = \\sqrt{(%s)^2 + (%s)^2} = \\sqrt{%s}$. \\\\ Vì $AB \\neq AD$ ($%s \\neq %s$) nên $\\sqrt{%s} \\neq \\sqrt{%s}$, suy ra $|\\vec{BC'}| \\neq |\\vec{AB'}|$. \\\\ Do đó khẳng định là %s."""
        % (
            b_len,
            c_len,
            bc_prime_sq,
            a_len,
            c_len,
            ab_prime_sq,
            a_len,
            b_len,
            bc_prime_sq,
            ab_prime_sq,
            "đúng" if "\\True" in th_da_1 else "sai",
        )
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: \vec{A'B} = \vec{C'D}[cite: 26]
    vd_da_1_d = "\\True $\\vec{A'B} = \\vec{D'C}$"
    vd_da_1_s = "$\\vec{A'B} = \\vec{C'D}$"
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Trong hình hộp chữ nhật $ABCD.A'B'C'D'$, xét tứ giác $A'BCD'$ có: \\\\ $\\vec{A'D'} = \\vec{BC}$ và $A'D' // BC$. \\\\ Do đó tứ giác $A'BCD'$ là hình bình hành. \\\\ Suy ra $\\vec{A'B} = \\vec{D'C} = -\\vec{C'D}$. \\\\ Vì hai vectơ $\\vec{A'B}$ và $\\vec{C'D}$ có cùng độ dài nhưng ngược hướng nhau nên $\\vec{A'B} \\neq \\vec{C'D}$. \\\\ Do đó mệnh đề là %s."""
        % ("đúng" if "\\True" in vd_da_1 else "sai")
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: Độ dài của véctơ AM bằng ...[cite: 26]
    vdc_da_1_d = "\\True Độ dài của véctơ $\\vec{AM}$ bằng $%s$" % (str_am_true)
    vdc_da_1_s = "Độ dài của véctơ $\\vec{AM}$ bằng $%s$" % (str_am_false)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Chọn hệ trục tọa độ $Oxyz$ sao cho gốc tọa độ trùng với đỉnh $A$, tia $Ox$ chứa cạnh $AB$, tia $Oy$ chứa cạnh $AD$ và tia $Oz$ chứa cạnh $AA'$. \\\\ Khi đó tọa độ các đỉnh tương ứng là: \\\\ $A(0;0;0), B(%s;0;0), D(0;%s;0), C(%s;%s;0), C'(%s;%s;%s)$. \\\\ Vì $M$ là trung điểm của cạnh bên $CC'$ nên tọa độ của điểm $M$ là: \\\\ $M\\left(%s; %s; \\frac{%s}{2}\\right)$. \\\\ Khi đó vectơ $\\vec{AM}$ có tọa độ là: \\\\ $\\vec{AM} = \\left(%s; %s; \\frac{%s}{2}\\right)$. \\\\ Độ dài của véctơ $\\vec{AM}$ là: \\\\ $|\\vec{AM}| = \\sqrt{(%s)^2 + (%s)^2 + \\left(\\frac{%s}{2}\\right)^2} = \\sqrt{%s + %s + \\frac{%s}{4}} = \\sqrt{\\frac{%s}{4}} = %s$. \\\\ Do đó mệnh đề là %s."""
        % (
            a_len,
            b_len,
            a_len,
            b_len,
            a_len,
            b_len,
            c_len,
            a_len,
            b_len,
            c_len,
            a_len,
            b_len,
            c_len,
            a_len,
            b_len,
            c_len,
            a_len**2,
            b_len**2,
            c_len**2,
            am_sq_num,
            str_am_true,
            "đúng" if "\\True" in vdc_da_1 else "sai",
        )
    )
    
    list_vdc_2 = [loigiai_vdc_1]
    
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))
    random.shuffle(combined_vdc)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)
    
    
    def count_true_answers(answers):
        return sum("\\True" in ans for ans in answers)
    
    
    # Lặp đến khi đáp án có từ 1 đến 3 câu đúng
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
    content = (
        "\\begin{minipage}{\\textwidth} \n"
        "\\begin{ex}\n"
        + str(noidungcauhoi)
        + "\n"
        "\\choiceTFn \n"
        "{" + str(shuffled_answers_nb[0]) + "}\n"
        "{" + str(shuffled_answers_th[0]) + "}\n"
        "{" + str(shuffled_answers_vd[0]) + "}\n"
        "{" + str(shuffled_answers_vdc[0]) + "}\n"
        "\\loigiai{ \n"
        "\\begin{enumEX}[a)]{1} \n"
        "\\item " + str(shuffled_solutions_nb[0]) + "\n"
        "\\item " + str(shuffled_solutions_th[0]) + "\n"
        "\\item " + str(shuffled_solutions_vd[0]) + "\n"
        "\\item " + str(shuffled_solutions_vdc[0]) + "\n"
        "\\end{enumEX}} \n"
        "\\end{ex}\n \\end{minipage}\n\n" )
    return content
    
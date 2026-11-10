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


def bt_dang36_p2_b3_c1_hh12(self):
    # Sinh ngẫu nhiên hệ số k của cạnh bên: SA = SB = SC = SD = k*a[cite: 22]
    # k chọn trong tập {2, 3} để căn thức gọn đẹp[cite: 22]
    k_side = random.choice([2, 3])
    
    # Độ dài cạnh bên là k_side * a[cite: 22]
    str_side = "%sa" % (k_side) if k_side > 1 else "a"
    
    # Tính toán SO và độ dài |b + d| = 2*SO[cite: 22]
    # Đáy hình vuông cạnh a => BD = a*sqrt(2) => OB = a*sqrt(2)/2[cite: 22]
    # SO^2 = SB^2 - OB^2 = k_side^2 * a^2 - a^2 / 2 = ((2*k_side^2 - 1)/2) * a^2[cite: 22]
    # SO = a * sqrt(4*k_side^2 - 2) / 2[cite: 22]
    # |b + d| = 2*SO = a * sqrt(4*k_side^2 - 2)[cite: 22]
    val_inside_sqrt = 4 * k_side**2 - 2
    str_len_bd_vec_true = "a\\sqrt{%s}" % (val_inside_sqrt)
    str_len_bd_vec_false = "\\frac{a\\sqrt{%s}}{2}" % (val_inside_sqrt)
    
    # Hình vẽ TikZ cố định tọa độ theo chuẩn mẫu[cite: 22]
    tikz_figure = (
        "\\begin{center}\n"
        "\\begin{tikzpicture}[scale=0.9, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n"
        "    \\coordinate (A) at (1.2,1.2);\n"
        "    \\coordinate (B) at (0,0);\n"
        "    \\coordinate (C) at (3.2,-0.4);\n"
        "    \\coordinate (D) at (4.4,0.8);\n"
        "    \\coordinate (O) at ($(A)!0.5!(C)$);\n"
        "    \\coordinate (S) at (2.2,3.8);\n"
        "    \\draw[line width=1pt] (S)--(B) (S)--(C) (S)--(D) (B)--(C)--(D);\n"
        "    \\draw[line width=1pt, dashed] (S)--(A) (A)--(B) (A)--(D) (A)--(C) (B)--(D) (S)--(O);\n"
        "    \\fill (A) circle (1pt) node[left] {$A$};\n"
        "    \\fill (B) circle (1pt) node[below left] {$B$};\n"
        "    \\fill (C) circle (1pt) node[below right] {$C$};\n"
        "    \\fill (D) circle (1pt) node[right] {$D$};\n"
        "    \\fill (S) circle (1pt) node[above] {$S$};\n"
        "    \\fill (O) circle (1pt) node[below] {$O$};\n"
        "    \\path (S) -- (A) node[pos=0.45, right] {$\\vec{a}$};\n"
        "    \\path (S) -- (B) node[pos=0.45, left] {$\\vec{b}$};\n"
        "    \\path (S) -- (C) node[pos=0.55, left] {$\\vec{c}$};\n"
        "    \\path (S) -- (D) node[pos=0.45, right] {$\\vec{d}$};\n"
        "\\end{tikzpicture}\n"
        "\\end{center}"
    )
    
    # Nội dung câu hỏi[cite: 22]
    noidungcauhoi = (
        """Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình vuông cạnh $a$, các cạnh bên $SA = SB = SC = SD = %s$. Đặt $\\vec{SA} = \\vec{a}, \\vec{SB} = \\vec{b}, \\vec{SC} = \\vec{c}, \\vec{SD} = \\vec{d}$. Xét tính đúng, sai của các khẳng định sau: %s"""
        % (str_side, tikz_figure)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Khẳng định a: Các vectơ a, b, c, d có độ dài bằng nhau[cite: 22]
    nb_da_1_d = "\\True Các vectơ $\\vec{a}, \\vec{b}, \\vec{c}, \\vec{d}$ có độ dài bằng nhau"
    nb_da_1_s = "Các vectơ $\\vec{a}, \\vec{b}, \\vec{c}, \\vec{d}$ có độ dài đôi một khác nhau"
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Theo giả thiết, các cạnh bên của hình chóp đều bằng nhau: $SA = SB = SC = SD = %s$. \\\\ Do đó độ dài của các vectơ tương ứng là: \\\\ $|\\vec{a}| = |\\vec{b}| = |\\vec{c}| = |\\vec{d}| = %s$. \\\\ Vậy các vectơ $\\vec{a}, \\vec{b}, \\vec{c}, \\vec{d}$ có độ dài bằng nhau."""
        % (str_side, str_side)
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Khẳng định b: AC, BD cùng phương[cite: 22]
    th_da_1_d = "\\True Hai vectơ $\\vec{AC}, \\vec{BD}$ không cùng phương"
    th_da_1_s = "$\\vec{AC}, \\vec{BD}$ cùng phương"
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Vì $ABCD$ là hình vuông nên hai đường chéo $AC$ và $BD$ cắt nhau tại trung điểm $O$ của mỗi đường và vuông góc với nhau ($AC \\perp BD$). \\\\ Giá của hai vectơ $\\vec{AC}$ và $\\vec{BD}$ là hai đường thẳng cắt nhau nên hai vectơ $\\vec{AC}$ và $\\vec{BD}$ không cùng phương. \\\\ Do đó khẳng định $\\vec{AC}, \\vec{BD}$ cùng phương là sai."""
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Khẳng định c: Gọi O là giao điểm của AC, BD khi đó SO = 1/2 (b + d)[cite: 22]
    vd_da_1_d = (
        "\\True Gọi $O$ là giao điểm của $AC, BD$ khi đó $\\vec{SO} = \\frac{1}{2}(\\vec{b} + \\vec{d})$"
    )
    vd_da_1_s = (
        "Gọi $O$ là giao điểm của $AC, BD$ khi đó $\\vec{SO} = \\vec{b} + \\vec{d}$"
    )
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Vì tứ giác $ABCD$ là hình vuông nên giao điểm $O$ của hai đường chéo $AC$ và $BD$ là trung điểm của đoạn thẳng $BD$. \\\\ Áp dụng quy tắc trung điểm trong tam giác $SBD$, ta có: \\\\ $\\vec{SB} + \\vec{SD} = 2\\vec{SO} \\Leftrightarrow \\vec{SO} = \\frac{1}{2}(\\vec{SB} + \\vec{SD})$. \\\\ Vì $\\vec{SB} = \\vec{b}$ và $\\vec{SD} = \\vec{d}$ nên $\\vec{SO} = \\frac{1}{2}(\\vec{b} + \\vec{d})$."""
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Khẳng định d: Độ dài của b + d[cite: 22]
    vdc_da_1_d = "\\True Độ dài của $\\vec{b} + \\vec{d}$ bằng $%s$" % (
        str_len_bd_vec_true
    )
    vdc_da_1_s = "Độ dài của $\\vec{b} + \\vec{d}$ bằng $%s$" % (
        str_len_bd_vec_false
    )
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Ta có $\\vec{b} + \\vec{d} = \\vec{SB} + \\vec{SD} = 2\\vec{SO}$, do đó: \\\\ $|\\vec{b} + \\vec{d}| = |2\\vec{SO}| = 2 SO$. \\\\ Vì hình chóp $S.ABCD$ có các cạnh bên bằng nhau ($SA = SB = SC = SD$) và đáy $ABCD$ là hình vuông nên hình chiếu vuông góc của đỉnh $S$ lên mặt phẳng đáy trùng với tâm $O$ của đáy, tức là $SO \\perp (ABCD)$. \\\\ Xét hình vuông $ABCD$ cạnh $a$: \\\\ $BD = a\\sqrt{2} \\Rightarrow OB = \\frac{BD}{2} = \\frac{a\\sqrt{2}}{2}$. \\\\ Xét tam giác $SOB$ vuông tại $O$, ta có: \\\\ $SO = \\sqrt{SB^2 - OB^2} = \\sqrt{(%s)^2 - \\left(\\frac{a\\sqrt{2}}{2}\\right)^2} = \\sqrt{%sa^2 - \\frac{a^2}{2}} = \\sqrt{\\frac{%sa^2}{2}} = %s$. \\\\ Suy ra: \\\\ $|\\vec{b} + \\vec{d}| = 2 SO = 2 \\cdot %s = %s$."""
        % (
            str_side,
            k_side**2,
            2 * k_side**2 - 1,
            str_len_bd_vec_false,
            str_len_bd_vec_false,
            str_len_bd_vec_true,
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
    
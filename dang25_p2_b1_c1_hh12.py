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


def bt_dang25_p2_b1_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Mã vẽ TikZ hình lập phương ABCD.A'B'C'D' có tâm đáy O và các vectơ vẽ đúng 100% như ảnh[cite: 20]
    # Chú ý: Không chứa comment ký tự % trong khối chuỗi để tránh xung đột định dạng %s
    tikz_figure = """\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,0);
    \\coordinate (B) at (2.4,-0.5);
    \\coordinate (D) at (0.6,1.4);
    \\coordinate (C) at ($(B)+(D)-(A)$);
    \\coordinate (A') at (0.4,2.6);
    \\coordinate (B') at ($(B)+(A')-(A)$);
    \\coordinate (C') at ($(C)+(A')-(A)$);
    \\coordinate (D') at ($(D)+(A')-(A)$);
    \\coordinate (O) at ($(A)!0.5!(C)$);
    \\draw[line width=1pt] (A)--(B)--(C)--(C')--(D')--(A')--cycle;
    \\draw[line width=1pt] (A')--(B')--(C') (B)--(B');
    \\draw[line width=1pt, dashed] (A)--(D)--(C) (D)--(D');
    \\draw[line width=1pt, dashed] (A)--(C) (B)--(D);
    \\draw[line width=1pt, dashed, ->] (A)--(A');
    \\draw[line width=1pt, dashed, ->] (A)--(D);
    \\draw[line width=1pt, ->] (A)--(B);
    \\draw[line width=1pt, dashed, ->] (A')--(O);
    \\draw[line width=1pt, ->] (A')--(B);
    \\draw[line width=1pt, dashed, ->] (B')--(O);
    \\draw[line width=1pt, ->] (B')--(C);
    \\draw[line width=1pt, dashed, ->] (B')--(C');
    \\fill (A) circle (1pt) node[below left] {$A$};
    \\fill (B) circle (1pt) node[below] {$B$};
    \\fill (C) circle (1pt) node[right] {$C$};
    \\fill (D) circle (1pt) node[left] {$D$};
    \\fill (A') circle (1pt) node[above left] {$A'$};
    \\fill (B') circle (1pt) node[below right] {$B'$};
    \\fill (C') circle (1pt) node[above right] {$C'$};
    \\fill (D') circle (1pt) node[above] {$D'$};
    \\fill (O) circle (1pt) node[below] {$O$};
    \\end{tikzpicture}
    \\end{center}"""
    
    # Nội dung câu hỏi[cite: 20]
    noidungcauhoi = (
        """Trong không gian cho hình lập phương $ABCD.A'B'C'D'$ có độ dài cạnh là $a$. Gọi $O$ là giao điểm của $BD$ và $AC$. %s"""
        % (tikz_figure)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: Vectơ \vec{A'C} - \vec{A'A} = \vec{AB} + \vec{AD}[cite: 20]
    # Phân tích: \vec{A'C} - \vec{A'A} = \vec{AC}. Trong hình vuông ABCD, \vec{AC} = \vec{AB} + \vec{AD} (ĐÚNG)[cite: 20]
    nb_da_1_d = "\\True Vectơ $\\vec{A'C} - \\vec{A'A} = \\vec{AB} + \\vec{AD}$"
    nb_da_1_s = "Vectơ $\\vec{A'C} - \\vec{A'A} = \\vec{AB} - \\vec{AD}$"
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Áp dụng quy tắc hiệu hai vectơ chung gốc, ta có: \\\\ $\\vec{A'C} - \\vec{A'A} = \\vec{AC}$. \\\\ Xét mặt đáy $ABCD$ là hình vuông (cũng là hình bình hành), theo quy tắc hình bình hành ta có: \\\\ $\\vec{AC} = \\vec{AB} + \\vec{AD}$. \\\\ Từ đó suy ra: \\\\ $\\vec{A'C} - \\vec{A'A} = \\vec{AB} + \\vec{AD}$. \\\\ Do đó mệnh đề là %s."""
        % ("đúng" if "\\True" in nb_da_1 else "sai")
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: Vectơ \vec{BC'} = \vec{A'A} + \vec{B'C'}[cite: 20]
    # Phân tích: \vec{BC'} = \vec{BB'} + \vec{B'C'} = \vec{AA'} + \vec{B'C'} = -\vec{A'A} + \vec{B'C'}. Do đó \vec{A'A} + \vec{B'C'} là SAI[cite: 20]
    th_da_1_d = "\\True Vectơ $\\vec{BC'} = \\vec{AA'} + \\vec{B'C'}$"
    th_da_1_s = "Vectơ $\\vec{BC'} = \\vec{A'A} + \\vec{B'C'}$"
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Trong mặt bên $BCC'B'$ là hình vuông, áp dụng quy tắc hình bình hành hoặc quy tắc ba điểm, ta có: \\\\ $\\vec{BC'} = \\vec{BB'} + \\vec{B'C'}$. \\\\ Vì các cạnh bên của hình lập phương song song và bằng nhau, ta có $\\vec{BB'} = \\vec{AA'} = -\\vec{A'A}$. \\\\ Suy ra đẳng thức đúng là: \\\\ $\\vec{BC'} = \\vec{AA'} + \\vec{B'C'} = -\\vec{A'A} + \\vec{B'C'}$. \\\\ Đẳng thức $\\vec{BC'} = \\vec{A'A} + \\vec{B'C'}$ là sai do ngược hướng ở vectơ cạnh bên. \\\\ Do đó mệnh đề là %s."""
        % ("đúng" if "\\True" in th_da_1 else "sai")
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: Vectơ \vec{C'O} = \vec{C'A'} - \vec{OA'}[cite: 20]
    # Phân tích: \vec{C'A'} - \vec{OA'} = \vec{C'A'} + \vec{A'O} = \vec{C'O} (ĐÚNG)[cite: 20]
    vd_da_1_d = "\\True Vectơ $\\vec{C'O} = \\vec{C'A'} - \\vec{OA'}$"
    vd_da_1_s = "Vectơ $\\vec{C'O} = \\vec{C'A'} + \\vec{OA'}$"
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Ta xét vế phải của đẳng thức: \\\\ $\\vec{C'A'} - \\vec{OA'} = \\vec{C'A'} + (-\\vec{OA'}) = \\vec{C'A'} + \\vec{A'O}$. \\\\ Áp dụng quy tắc ba điểm cho phép cộng vectơ: \\\\ $\\vec{C'A'} + \\vec{A'O} = \\vec{C'O}$. \\\\ Do đó ta có $\\vec{C'O} = \\vec{C'A'} - \\vec{OA'}$. \\\\ Vậy mệnh đề là %s."""
        % ("đúng" if "\\True" in vd_da_1 else "sai")
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: \vec{A'D} \cdot \vec{A'B} = 0[cite: 20]
    # Phân tích: Tam giác A'BD có A'B = A'D = a\sqrt{2}, BD = a\sqrt{2} => tam giác A'BD đều => góc BA'D = 60°
    # => \vec{A'D} \cdot \vec{A'B} = a\sqrt{2} * a\sqrt{2} * cos(60°) = a^2 != 0 (Mệnh đề = 0 là SAI)[cite: 20]
    vdc_da_1_d = "\\True $\\vec{A'D} \\cdot \\vec{A'B} = a^2$"
    vdc_da_1_s = "$\\vec{A'D} \\cdot \\vec{A'B} = 0$"
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Xét tam giác $A'BD$, ta có: \\\\ $\\bullet$ $A'B$ là đường chéo của hình vuông $ABB'A'$ cạnh $a$, suy ra $A'B = a\\sqrt{2}$. \\\\ $\\bullet$ $A'D$ là đường chéo của hình vuông $ADD'A'$ cạnh $a$, suy ra $A'D = a\\sqrt{2}$. \\\\ $\\bullet$ $BD$ là đường chéo của hình vuông $ABCD$ cạnh $a$, suy ra $BD = a\\sqrt{2}$. \\\\ Do đó tam giác $A'BD$ là tam giác đều, suy ra góc $\\widehat{DA'B} = 60^\\circ$. \\\\ Tích vô hướng giữa hai vectơ $\\vec{A'D}$ và $\\vec{A'B}$ là: \\\\ $\\vec{A'D} \\cdot \\vec{A'B} = |\\vec{A'D}| \\cdot |\\vec{A'B}| \\cdot \\cos \\widehat{DA'B} = (a\\sqrt{2}) \\cdot (a\\sqrt{2}) \\cdot \\cos 60^\\circ = 2a^2 \\cdot \\frac{1}{2} = a^2 \\neq 0$. \\\\ Do đó mệnh đề $\\vec{A'D} \\cdot \\vec{A'B} = 0$ là sai. \\\\ Vì vậy mệnh đề là %s."""
        % ("đúng" if "\\True" in vdc_da_1 else "sai")
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
    
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


def bt_dang41_p2_b1_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Mã vẽ TikZ tứ diện S.ABC có các điểm M, I, E, K, G chuẩn 100% như ảnh[cite: 20]
    # Chú ý: Tuyệt đối không dùng ký hiệu % comment bên trong string để tránh lỗi format string
    tikz_figure = """\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,0);
    \\coordinate (B) at (1.2,-1.4);
    \\coordinate (C) at (3.6,0);
    \\coordinate (S) at (0.6,3.4);
    \\coordinate (M) at ($(S)!0.5!(A)$);
    \\coordinate (I) at ($(A)!0.5!(B)$);
    \\coordinate (E) at ($(S)!0.5!(I)$);
    \\coordinate (G) at ($(C)!0.66667!(I)$);
    \\coordinate (K) at ($(C)!0.5!(G)$);
    \\draw[line width=1pt] (S)--(A)--(B)--(C)--(S)--(B);
    \\draw[line width=1pt] (S)--(I);
    \\draw[line width=1pt, dashed] (A)--(C) (I)--(C) (S)--(G) (S)--(K);
    \\fill (A) circle (1pt) node[left] {$A$};
    \\fill (B) circle (1pt) node[below] {$B$};
    \\fill (C) circle (1pt) node[right] {$C$};
    \\fill (S) circle (1pt) node[above left] {$S$};
    \\fill (M) circle (1pt) node[left] {$M$};
    \\fill (I) circle (1pt) node[below left] {$I$};
    \\fill (E) circle (1pt) node[left] {$E$};
    \\fill (G) circle (1pt) node[below] {$G$};
    \\fill (K) circle (1pt) node[below] {$K$};
    \\end{tikzpicture}
    \\end{center}"""
    
    
    noidungcauhoi = (
        """Trong không gian cho tứ diện $S.ABC$, các điểm $M, I, E, K$ lần lượt là trung điểm của $SA, AB, SI, CG$ (với $G$ là trọng tâm tam giác $ABC$). %s"""
        % (tikz_figure)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: \vec{AS} - \vec{IB} = \vec{SI} (Sai vì bằng -\vec{SI} = \vec{IS})[cite: 20]
    nb_da_1_d = "\\True $\\vec{AS} - \\vec{IB} = -\\vec{SI}$"
    nb_da_1_s = "$\\vec{AS} - \\vec{IB} = \\vec{SI}$"
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Vì $I$ là trung điểm của đoạn thẳng $AB$ nên $\\vec{AI} = \\vec{IB}$. \\\\ Khi đó ta biến đổi vế trái: \\\\ $\\vec{AS} - \\vec{IB} = \\vec{AS} - \\vec{AI}$. \\\\ Theo quy tắc hiệu hai vectơ chung gốc $A$, ta có: \\\\ $\\vec{AS} - \\vec{AI} = \\vec{IS} = -\\vec{SI}$. \\\\ Vì $\\vec{IS} = -\\vec{SI} \\neq \\vec{SI}$ nên khẳng định $\\vec{AS} - \\vec{IB} = \\vec{SI}$ là sai do ngược hướng. \\\\ Do đó mệnh đề là %s."""
        % ("đúng" if "\\True" in nb_da_1 else "sai")
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: \vec{SG} = 1/3 (\vec{SA} + \vec{SB} + \vec{SC})[cite: 20]
    th_da_1_d = "\\True $\\vec{SG} = \\frac{1}{3}\\left(\\vec{SA} + \\vec{SB} + \\vec{SC}\\right)$"
    th_da_1_s = "$\\vec{SG} = \\frac{1}{2}\\left(\\vec{SA} + \\vec{SB} + \\vec{SC}\\right)$"
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Vì điểm $G$ là trọng tâm của tam giác $ABC$, theo tính chất trọng tâm tam giác ta có hệ thức vectơ: \\\\ $\\vec{GA} + \\vec{GB} + \\vec{GC} = \\vec{0}$. \\\\ Với điểm $S$ bất kỳ trong không gian, ta phân tích: \\\\ $\\vec{SA} + \\vec{SB} + \\vec{SC} = (\\vec{SG} + \\vec{GA}) + (\\vec{SG} + \\vec{GB}) + (\\vec{SG} + \\vec{GC}) = 3\\vec{SG} + (\\vec{GA} + \\vec{GB} + \\vec{GC}) = 3\\vec{SG}$. \\\\ Suy ra: \\\\ $\\vec{SG} = \\frac{1}{3}\\left(\\vec{SA} + \\vec{SB} + \\vec{SC}\\right)$. \\\\ Do đó mệnh đề là %s."""
        % ("đúng" if "\\True" in th_da_1 else "sai")
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: Phân tích vectơ \vec{MG} qua \vec{SA}, \vec{SB}, \vec{SC}[cite: 20]
    vd_da_1_d = "\\True $\\vec{MG} = -\\frac{1}{6}\\vec{SA} + \\frac{1}{3}\\vec{SB} + \\frac{1}{3}\\vec{SC}$"
    vd_da_1_s = "$\\vec{MG} = \\frac{1}{6}\\vec{SA} + \\frac{1}{3}\\vec{SB} + \\frac{1}{3}\\vec{SC}$"
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Biểu diễn vectơ $\\vec{MG}$ qua điểm gốc $S$: \\\\ $\\vec{MG} = \\vec{SG} - \\vec{SM}$. \\\\ Vì $M$ là trung điểm của cạnh $SA$ nên $\\vec{SM} = \\frac{1}{2}\\vec{SA}$. \\\\ Theo kết quả ở câu b, ta có $\\vec{SG} = \\frac{1}{3}\\vec{SA} + \\frac{1}{3}\\vec{SB} + \\frac{1}{3}\\vec{SC}$. \\\\ Khi đó: \\\\ $\\vec{MG} = \\left(\\frac{1}{3}\\vec{SA} + \\frac{1}{3}\\vec{SB} + \\frac{1}{3}\\vec{SC}\\right) - \\frac{1}{2}\\vec{SA} = \\left(\\frac{1}{3} - \\frac{1}{2}\\right)\\vec{SA} + \\frac{1}{3}\\vec{SB} + \\frac{1}{3}\\vec{SC}$ \\\\ $\\Leftrightarrow \\vec{MG} = -\\frac{1}{6}\\vec{SA} + \\frac{1}{3}\\vec{SB} + \\frac{1}{3}\\vec{SC}$. \\\\ Do đó mệnh đề là %s."""
        % ("đúng" if "\\True" in vd_da_1 else "sai")
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: Phân tích vectơ \vec{EK} qua \vec{SA}, \vec{SB}, \vec{SC}[cite: 20]
    vdc_da_1_d = "\\True $\\vec{EK} = -\\frac{1}{12}\\vec{SA} - \\frac{1}{12}\\vec{SB} + \\frac{2}{3}\\vec{SC}$"
    vdc_da_1_s = "$\\vec{EK} = \\frac{1}{12}\\vec{SA} + \\frac{1}{12}\\vec{SB} + \\frac{2}{3}\\vec{SC}$"
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Ta biểu diễn vectơ $\\vec{EK}$ thông qua điểm gốc $S$: \\\\ $\\vec{EK} = \\vec{SK} - \\vec{SE}$. \\\\ $\\bullet$ Do $E$ là trung điểm của đoạn thẳng $SI$ và $I$ là trung điểm của cạnh $AB$: \\\\ $\\vec{SI} = \\frac{1}{2}(\\vec{SA} + \\vec{SB}) \\Rightarrow \\vec{SE} = \\frac{1}{2}\\vec{SI} = \\frac{1}{4}\\vec{SA} + \\frac{1}{4}\\vec{SB}$. \\\\ $\\bullet$ Do $K$ là trung điểm của đoạn thẳng $CG$: \\\\ $\\vec{SK} = \\frac{1}{2}(\\vec{SC} + \\vec{SG}) = \\frac{1}{2}\\vec{SC} + \\frac{1}{2} \\cdot \\frac{1}{3}(\\vec{SA} + \\vec{SB} + \\vec{SC}) = \\frac{1}{6}\\vec{SA} + \\frac{1}{6}\\vec{SB} + \\left(\\frac{1}{2} + \\frac{1}{6}\\right)\\vec{SC} = \\frac{1}{6}\\vec{SA} + \\frac{1}{6}\\vec{SB} + \\frac{2}{3}\\vec{SC}$. \\\\ Khi đó: \\\\ $\\vec{EK} = \\vec{SK} - \\vec{SE} = \\left(\\frac{1}{6}\\vec{SA} + \\frac{1}{6}\\vec{SB} + \\frac{2}{3}\\vec{SC}\\right) - \\left(\\frac{1}{4}\\vec{SA} + \\frac{1}{4}\\vec{SB}\\right)$ \\\\ $= \\left(\\frac{1}{6} - \\frac{1}{4}\\right)\\vec{SA} + \\left(\\frac{1}{6} - \\frac{1}{4}\\right)\\vec{SB} + \\frac{2}{3}\\vec{SC} = -\\frac{1}{12}\\vec{SA} - \\frac{1}{12}\\vec{SB} + \\frac{2}{3}\\vec{SC}$. \\\\ Do đó mệnh đề là %s."""
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
    
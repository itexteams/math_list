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


def bt_dang19_p2_b1_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Mã vẽ TikZ tứ diện S.ABC có M là trung điểm BC chính xác 100% như ảnh[cite: 21]
    tikz_figure = """\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,0);
    \\coordinate (C) at (1.6,-1.7);
    \\coordinate (B) at (4.2,0);
    \\coordinate (S) at (1.9,3.0);
    \\coordinate (M) at ($(B)!0.5!(C)$);
    \\draw[line width=1pt] (S)--(A) node[midway, above left] {$a$};
    \\draw[line width=1pt] (S)--(C) node[midway, left] {$a$};
    \\draw[line width=1pt] (S)--(B) node[midway, above right] {$a$};
    \\draw[line width=1pt] (A)--(C) node[midway, below left] {$a$};
    \\draw[line width=1pt] (C)--(M) node[midway, below right] {$a$};
    \\draw[line width=1pt] (S)--(M);
    \\draw[line width=1pt, dashed] (A)--(B) node[midway, above] {$a$};
    \\draw[line width=1pt, dashed] (A)--(M);
    \\draw[line width=1pt] (M)--(B);
    \\fill (A) circle (1pt) node[below left] {$A$};
    \\fill (B) circle (1pt) node[below right] {$B$};
    \\fill (C) circle (1pt) node[below] {$C$};
    \\fill (S) circle (1pt) node[above] {$S$};
    \\fill (M) circle (1pt) node[below right] {$M$};
    \\end{tikzpicture}
    \\end{center}"""
    
    
    noidungcauhoi = (
        """Cho tứ diện đều $S.ABC$ cạnh $a$, $M$ là trung điểm của cạnh $BC$. %s"""
        % (tikz_figure)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Khẳng định a: (\vec{SA}, \vec{SB}) = 60^\circ[cite: 21]
    nb_da_1_d = "\\True $(\\vec{SA}, \\vec{SB}) = 60^\\circ$"
    nb_da_1_s = "$(\\vec{SA}, \\vec{SB}) = 120^\\circ$"
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Vì $S.ABC$ là tứ diện đều nên tam giác $SAB$ là tam giác đều. \\\\ Do đó $\\widehat{ASB} = 60^\\circ$. \\\\ Góc giữa hai vectơ $\\vec{SA}$ và $\\vec{SB}$ chính là góc $\\widehat{ASB}$: \\\\ $(\\vec{SA}, \\vec{SB}) = \\widehat{ASB} = 60^\\circ$. \\\\ Do đó khẳng định là %s."""
        % ("đúng" if "\\True" in nb_da_1 else "sai")
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Khẳng định b: \vec{SM} . \vec{BC} = a^2 (Sai)[cite: 21]
    th_da_1_d = "\\True $\\vec{SM} \\cdot \\vec{BC} = 0$"
    th_da_1_s = "$\\vec{SM} \\cdot \\vec{BC} = a^2$"
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Vì tứ diện $S.ABC$ đều nên mặt bên $SBC$ là tam giác đều. \\\\ Đoạn thẳng $SM$ là đường trung tuyến đồng thời là đường cao của tam giác $SBC$, suy ra $SM \\perp BC$. \\\\ Do đó hai vectơ $\\vec{SM}$ và $\\vec{BC}$ vuông góc với nhau: \\\\ $\\vec{SM} \\cdot \\vec{BC} = 0$. \\\\ Khẳng định $\\vec{SM} \\cdot \\vec{BC} = a^2$ là sai. \\\\ Vì vậy khẳng định là %s."""
        % ("đúng" if "\\True" in th_da_1 else "sai")
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Khẳng định c: \vec{SA} . \vec{SM} = a^2 / 2[cite: 21]
    vd_da_1_d = "\\True $\\vec{SA} \\cdot \\vec{SM} = \\frac{a^2}{2}$"
    vd_da_1_s = "$\\vec{SA} \\cdot \\vec{SM} = \\frac{a^2}{4}$"
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Vì $M$ là trung điểm của cạnh $BC$ nên với đỉnh $S$ ta có hệ thức vectơ: \\\\ $\\vec{SM} = \\frac{1}{2}\\left(\\vec{SB} + \\vec{SC}\\right)$. \\\\ Khi đó tích vô hướng giữa hai vectơ $\\vec{SA}$ và $\\vec{SM}$ là: \\\\ $\\vec{SA} \\cdot \\vec{SM} = \\vec{SA} \\cdot \\left[\\frac{1}{2}\\left(\\vec{SB} + \\vec{SC}\\right)\\right] = \\frac{1}{2}\\left(\\vec{SA} \\cdot \\vec{SB} + \\vec{SA} \\cdot \\vec{SC}\\right)$. \\\\ Vì các tam giác $SAB$ và $SAC$ là các tam giác đều cạnh $a$ nên: \\\\ $\\vec{SA} \\cdot \\vec{SB} = SA \\cdot SB \\cdot \\cos 60^\\circ = a \\cdot a \\cdot \\frac{1}{2} = \\frac{a^2}{2}$. \\\\ $\\vec{SA} \\cdot \\vec{SC} = SA \\cdot SC \\cdot \\cos 60^\\circ = a \\cdot a \\cdot \\frac{1}{2} = \\frac{a^2}{2}$. \\\\ Suy ra: \\\\ $\\vec{SA} \\cdot \\vec{SM} = \\frac{1}{2}\\left(\\frac{a^2}{2} + \\frac{a^2}{2}\\right) = \\frac{a^2}{2}$. \\\\ Do đó khẳng định là %s."""
        % ("đúng" if "\\True" in vd_da_1 else "sai")
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Khẳng định d: \cos(\vec{AM}, \vec{SB}) = -\frac{\sqrt{3}}{6} (đúng), \frac{\sqrt{3}}{6} (sai)[cite: 21]
    vdc_da_1_d = "\\True $\\cos(\\vec{AM}, \\vec{SB}) = -\\frac{\\sqrt{3}}{6}$"
    vdc_da_1_s = "$\\cos(\\vec{AM}, \\vec{SB}) = \\frac{\\sqrt{3}}{6}$"
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Ta tính độ dài của các vectơ: \\\\ $AM$ là đường cao trong tam giác đều $ABC$ cạnh $a$ nên $AM = |\\vec{AM}| = \\frac{a\\sqrt{3}}{2}$. \\\\ Cạnh của tứ diện đều là $SB = |\\vec{SB}| = a$. \\\\ Phân tích vectơ $\\vec{AM}$ theo hai vectơ cạnh: \\\\ $\\vec{AM} = \\vec{AB} + \\vec{BM} = \\vec{AB} + \\frac{1}{2}\\vec{BC}$. \\\\ Tích vô hướng của $\\vec{AM}$ và $\\vec{SB}$ là: \\\\ $\\vec{AM} \\cdot \\vec{SB} = \\left(\\vec{AB} + \\frac{1}{2}\\vec{BC}\\right) \\cdot \\vec{SB} = \\vec{AB} \\cdot \\vec{SB} + \\frac{1}{2}\\vec{BC} \\cdot \\vec{SB}$ \\\\ $= -\\vec{BA} \\cdot \\vec{SB} - \\frac{1}{2}\\vec{CB} \\cdot \\vec{SB}$ \\\\ $= -\\left(BA \\cdot SB \\cdot \\cos 60^\\circ\\right) - \\frac{1}{2}\\left(CB \\cdot SB \\cdot \\cos 60^\\circ\\right)$ \\\\ $= -\\left(a \\cdot a \\cdot \\frac{1}{2}\\right) - \\frac{1}{2}\\left(a \\cdot a \\cdot \\frac{1}{2}\\right) = -\\frac{a^2}{2} + \\frac{a^2}{4} = -\\frac{a^2}{4}$. \\\\ Áp dụng công thức tính côsin của góc giữa hai vectơ: \\\\ $\\cos(\\vec{AM}, \\vec{SB}) = \\frac{\\vec{AM} \\cdot \\vec{SB}}{|\\vec{AM}| \\cdot |\\vec{SB}|} = \\frac{-\\frac{a^2}{4}}{\\frac{a\\sqrt{3}}{2} \\cdot a} = -\\frac{1}{4} \\cdot \\frac{2}{\\sqrt{3}} = -\\frac{1}{2\\sqrt{3}} = -\\frac{\\sqrt{3}}{6}$. \\\\ Do giá trị mang dấu âm nên khẳng định $\\cos(\\vec{AM}, \\vec{SB}) = \\frac{\\sqrt{3}}{6}$ là sai. \\\\ Vì vậy mệnh đề là %s."""
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
    
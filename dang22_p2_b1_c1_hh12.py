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


def bt_dang22_p2_b1_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Mã vẽ TikZ hình chóp S.ABCD đều có đáy là hình vuông, M là trung điểm CD, O là tâm đáy, màu black, nét 1pt, điểm 1pt 100% như ảnh[cite: 21]
    tikz_figure = """\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,0);
    \\coordinate (B) at (-1.2,-1.2);
    \\coordinate (C) at (2.8,-1.2);
    \\coordinate (D) at (4,0);
    \\coordinate (O) at ($(A)!0.5!(C)$);
    \\coordinate (S) at ($(O)+(0,3.3)$);
    \\coordinate (M) at ($(C)!0.5!(D)$);
    \\draw[line width=1pt] (S)--(B)--(C)--(D)--(S)--(C);
    \\draw[line width=1pt] (S)--(M);
    \\draw[line width=1pt, dashed] (A)--(B) (A)--(D) (S)--(A) (A)--(C) (B)--(D) (S)--(O) (O)--(M);
    \\fill (A) circle (1pt) node[left] {$A$};
    \\fill (B) circle (1pt) node[below left] {$B$};
    \\fill (C) circle (1pt) node[below right] {$C$};
    \\fill (D) circle (1pt) node[right] {$D$};
    \\fill (O) circle (1pt) node[below] {$O$};
    \\fill (S) circle (1pt) node[above] {$S$};
    \\fill (M) circle (1pt) node[below right] {$M$};
    \\end{tikzpicture}
    \\end{center}"""
    
    
    noidungcauhoi = (
        """Cho hình chóp $S.ABCD$ có tất cả các cạnh bên và cạnh đáy đều bằng $a$ và $ABCD$ là hình vuông. Gọi $M$ là trung điểm của $CD$. %s"""
        % (tikz_figure)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: Góc giữa \vec{SO} và \vec{AC} bằng 90°[cite: 21]
    nb_da_1_d = "\\True Góc giữa $\\vec{SO}$ và $\\vec{AC}$ bằng $90^\\circ$"
    nb_da_1_s = "Góc giữa $\\vec{SO}$ và $\\vec{AC}$ bằng $45^\\circ$"
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Vì hình chóp $S.ABCD$ có các cạnh bên bằng nhau ($SA = SB = SC = SD = a$) và đáy $ABCD$ là hình vuông tâm $O$ nên $SO \\perp (ABCD)$. \\\\ Mặt khác $AC \\subset (ABCD)$, suy ra $SO \\perp AC$. \\\\ Do hai đường thẳng $SO$ và $AC$ vuông góc với nhau nên góc giữa hai vectơ $\\vec{SO}$ và $\\vec{AC}$ bằng $90^\\circ$. \\\\ Do đó mệnh đề là %s."""
        % ("đúng" if "\\True" in nb_da_1 else "sai")
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: Góc giữa \vec{BS} và \vec{CD} bằng 60°[cite: 21]
    th_da_1_d = "\\True Góc giữa $\\vec{BS}$ và $\\vec{CD}$ bằng $60^\\circ$"
    th_da_1_s = "Góc giữa $\\vec{BS}$ và $\\vec{CD}$ bằng $120^\\circ$"
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Vì $ABCD$ là hình vuông nên $\\vec{CD} = \\vec{BA}$. \\\\ Khi đó góc giữa hai vectơ $\\vec{BS}$ và $\\vec{CD}$ là: \\\\ $(\\vec{BS}, \\vec{CD}) = (\\vec{BS}, \\vec{BA}) = \\widehat{SBA}$. \\\\ Xét tam giác $SAB$ có $SA = SB = AB = a$, do đó tam giác $SAB$ là tam giác đều. \\\\ Suy ra góc $\\widehat{SBA} = 60^\\circ$, tức là $(\\vec{BS}, \\vec{CD}) = 60^\\circ$. \\\\ Do đó mệnh đề là %s."""
        % ("đúng" if "\\True" in th_da_1 else "sai")
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: \vec{AB} . \vec{CA} = -a^2 (đúng) hoặc = a^2 (sai)[cite: 21]
    vd_da_1_d = "\\True $\\vec{AB} \\cdot \\vec{CA} = -a^2$"
    vd_da_1_s = "$\\vec{AB} \\cdot \\vec{CA} = a^2$"
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Đáy $ABCD$ là hình vuông cạnh $a$ nên độ dài đường chéo là $CA = a\\sqrt{2}$ và góc $\\widehat{BAC} = 45^\\circ$. \\\\ Ta có: \\\\ $\\vec{AB} \\cdot \\vec{CA} = -\\vec{AB} \\cdot \\vec{AC} = -|\\vec{AB}| \\cdot |\\vec{AC}| \\cdot \\cos(\\vec{AB}, \\vec{AC})$ \\\\ $= -a \\cdot (a\\sqrt{2}) \\cdot \\cos 45^\\circ = -a^2\\sqrt{2} \\cdot \\frac{\\sqrt{2}}{2} = -a^2$. \\\\ Do đó mệnh đề $\\vec{AB} \\cdot \\vec{CA} = a^2$ là sai. \\\\ Vì vậy mệnh đề là %s."""
        % ("đúng" if "\\True" in vd_da_1 else "sai")
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: \vec{MS} . \vec{CB} = a^2 / 2[cite: 21]
    vdc_da_1_d = "\\True $\\vec{MS} \\cdot \\vec{CB} = \\frac{a^2}{2}$"
    vdc_da_1_s = "$\\vec{MS} \\cdot \\vec{CB} = -\\frac{a^2}{2}$"
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Chèn điểm $O$ vào vectơ $\\vec{MS}$, ta có $\\vec{MS} = \\vec{OS} - \\vec{OM}$. \\\\ Khi đó tích vô hướng: \\\\ $\\vec{MS} \\cdot \\vec{CB} = (\\vec{OS} - \\vec{OM}) \\cdot \\vec{CB} = \\vec{OS} \\cdot \\vec{CB} - \\vec{OM} \\cdot \\vec{CB}$. \\\\ Vì $SO \\perp (ABCD)$ mà $CB \\subset (ABCD)$ nên $SO \\perp CB$, suy ra $\\vec{OS} \\cdot \\vec{CB} = 0$. \\\\ Trong tam giác $BCD$, vì $O$ là trung điểm của $BD$ và $M$ là trung điểm của $CD$ nên $OM$ là đường trung bình của tam giác $BCD$, suy ra: \\\\ $\\vec{OM} = \\frac{1}{2}\\vec{BC} = -\\frac{1}{2}\\vec{CB}$. \\\\ Thay vào biểu thức tích vô hướng, ta được: \\\\ $\\vec{MS} \\cdot \\vec{CB} = 0 - \\left(-\\frac{1}{2}\\vec{CB}\\right) \\cdot \\vec{CB} = \\frac{1}{2}\\vec{CB}^2 = \\frac{1}{2}CB^2 = \\frac{a^2}{2}$. \\\\ Do đó mệnh đề là %s."""
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
    
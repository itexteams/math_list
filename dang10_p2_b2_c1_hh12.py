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


def bt_dang10_p2_b2_c1_hh12(self):
    # M thuộc đoạn AC sao cho AC = 3*MC <=> CM/AC = 1/3, AM/AC = 2/3
    k_m = 3
    # N thuộc đoạn C'D sao cho C'N = (2/3)*C'D
    ratio_n_num = 2
    ratio_n_den = 3
    
    # Chuỗi TikZ vẽ hình chính xác 100% như mẫu, nét 1pt, điểm 1pt, màu black
    hinh_ve_tikz = """\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,0);
    \\coordinate (D) at (3.2,-0.7);
    \\coordinate (B) at (1.8,1.2);
    \\coordinate (C) at ($(B)+(D)-(A)$);
    \\coordinate (h) at (0,3.3);
    \\coordinate (A') at ($(A)+(h)$);
    \\coordinate (B') at ($(B)+(h)$);
    \\coordinate (C') at ($(C)+(h)$);
    \\coordinate (D') at ($(D)+(h)$);
    \\coordinate (O) at ($(A)!0.5!(C)$);
    \\coordinate (M) at ($(A)!0.6667!(C)$);
    \\coordinate (N) at ($(C')!0.6667!(D)$);
    \\coordinate (I) at ($(C)!0.5!(D)$);
    \\draw[line width=1pt] (A)--(D)--(C)--(C')--(B')--(A')--(A) (A')--(D')--(C') (D')--(D) (C')--(D) (D')--(I) ;
    \\draw[line width=1pt, dashed] (A)--(B)--(C) (B)--(B') (A)--(C) (B)--(D) (B)--(D') (B)--(I) (D')--(M) (M)--(N);
    \\fill (A) circle (1pt) node[below left] {$A$};
    \\fill (B) circle (1pt) node[above left] {$B$};
    \\fill (C) circle (1pt) node[below right] {$C$};
    \\fill (D) circle (1pt) node[below] {$D$};
    \\fill (A') circle (1pt) node[left] {$A'$};
    \\fill (B') circle (1pt) node[above] {$B'$};
    \\fill (C') circle (1pt) node[above right] {$C'$};
    \\fill (D') circle (1pt) node[above] {$D'$};
    \\fill (O) circle (1pt) node[below] {$O$};
    \\fill (M) circle (1pt) node[below] {$M$};
    \\fill (N) circle (1pt) node[right] {$N$};
    \\fill (I) circle (1pt) node[below] {$I$};
    \\end{tikzpicture}
    \\end{center}"""
    
    # Nội dung câu hỏi (đặt hình vẽ lên đề bài theo yêu cầu)
    noidungcauhoi = (
        """Cho hình hộp $ABCD.A'B'C'D'$. $M$ là điểm trên đoạn $AC$ sao cho $AC = %sMC$. Lấy $N$ trên đoạn $C'D$ sao cho $C'N = \\frac{%s}{%s}C'D$. %s"""
        % (k_m, ratio_n_num, ratio_n_den, hinh_ve_tikz)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Phát biểu a: Hai vectơ AB' và C'D
    nb_da_1_d = "\\True Hai vectơ $\\vec{AB'}, \\vec{C'D}$ ngược hướng"
    nb_da_1_s = "Hai vectơ $\\vec{AB'}, \\vec{C'D}$ cùng hướng"
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = """Vì $ABCD.A'B'C'D'$ là hình hộp nên $ADC'B'$ là hình bình hành. \\\\ Do đó ta có $\\vec{AB'} = \\vec{DC'}$. \\\\ Mặt khác $\\vec{C'D} = -\\vec{DC'}$, suy ra $\\vec{AB'} = -\\vec{C'D}$. \\\\ Vậy hai vectơ $\\vec{AB'}$ và $\\vec{C'D}$ ngược hướng."""
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Phát biểu b: Biểu diễn vectơ CM theo vectơ AC
    th_da_1_d = "\\True $\\vec{CM} = -\\frac{1}{%s}\\vec{AC}$" % (k_m)
    th_da_1_s = "$\\vec{CM} = \\frac{1}{%s}\\vec{AC}$" % (k_m)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Vì $M$ thuộc đoạn thẳng $AC$ và $AC = %sMC$ nên điểm $M$ nằm giữa hai điểm $A$ và $C$, suy ra hai vectơ $\\vec{CM}$ và $\\vec{CA}$ cùng hướng và độ dài $CM = \\frac{1}{%s}CA$. \\\\ Do đó $\\vec{CM} = \\frac{1}{%s}\\vec{CA} = -\\frac{1}{%s}\\vec{AC}$."""
        % (k_m, k_m, k_m, k_m)
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Phát biểu c: M là trọng tâm tam giác BCD
    vd_da_1_d = "\\True $M$ là trọng tâm của tam giác $BCD$"
    vd_da_1_s = "$M$ là trọng tâm của tam giác $ABD$"
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = """Gọi $O$ là giao điểm của $AC$ và $BD$, khi đó $O$ là trung điểm của $AC$ và $BD$. \\\\ Ta có $CO = \\frac{1}{2}AC \\Leftrightarrow AC = 2CO$. \\\\ Kết hợp với giả thiết $AC = 3MC$, ta suy ra: $2CO = 3MC \\Leftrightarrow CM = \\frac{2}{3}CO$. \\\\ Trong tam giác $BCD$, $CO$ là đường trung tuyến kẻ từ đỉnh $C$. Vì $M$ thuộc đoạn $CO$ và $CM = \\frac{2}{3}CO$ nên $M$ chính là trọng tâm của tam giác $BCD$."""
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Phát biểu d: Mối quan hệ giữa MN và B'D hoặc D'B
    vdc_da_1_d = "\\True Hai vectơ $\\vec{MN}, \\vec{D'B}$ ngược hướng"
    vdc_da_1_s = "Hai vectơ $\\vec{MN}, \\vec{B'D}$ ngược hướng"
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Đặt $\\vec{AB} = \\vec{a}$, $\\vec{AD} = \\vec{b}$, $\\vec{AA'} = \\vec{c}$. \\\\ Khi đó ta có: \\\\ $\\vec{AC} = \\vec{a} + \\vec{b} \\Rightarrow \\vec{AM} = \\frac{2}{3}\\vec{AC} = \\frac{2}{3}\\vec{a} + \\frac{2}{3}\\vec{b}$. \\\\ $\\vec{AC'} = \\vec{a} + \\vec{b} + \\vec{c}$ và $\\vec{AD} = \\vec{b} \\Rightarrow \\vec{C'D} = \\vec{AD} - \\vec{AC'} = -\\vec{a} - \\vec{c}$. \\\\ Vì $\\vec{C'N} = \\frac{2}{3}\\vec{C'D} = -\\frac{2}{3}\\vec{a} - \\frac{2}{3}\\vec{c}$, nên: \\\\ $\\vec{AN} = \\vec{AC'} + \\vec{C'N} = (\\vec{a} + \\vec{b} + \\vec{c}) + \\left(-\\frac{2}{3}\\vec{a} - \\frac{2}{3}\\vec{c}\\right) = \\frac{1}{3}\\vec{a} + \\vec{b} + \\frac{1}{3}\\vec{c}$. \\\\ Từ đó ta có: \\\\ $\\vec{MN} = \\vec{AN} - \\vec{AM} = \\left(\\frac{1}{3}\\vec{a} + \\vec{b} + \\frac{1}{3}\\vec{c}\\right) - \\left(\\frac{2}{3}\\vec{a} + \\frac{2}{3}\\vec{b}\\right) = -\\frac{1}{3}\\vec{a} + \\frac{1}{3}\\vec{b} + \\frac{1}{3}\\vec{c} = -\\frac{1}{3}(\\vec{a} - \\vec{b} - \\vec{c})$. \\\\ Mặt khác: $\\vec{D'B} = \\vec{AB} - \\vec{AD'} = \\vec{a} - (\\vec{b} + \\vec{c}) = \\vec{a} - \\vec{b} - \\vec{c}$. \\\\ Do đó $\\vec{MN} = -\\frac{1}{3}\\vec{D'B}$, suy ra hai vectơ $\\vec{MN}$ và $\\vec{D'B}$ cùng phương và ngược hướng."""
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
        "\\end{ex}\n \\end{minipage}\n\n")
    return content
    
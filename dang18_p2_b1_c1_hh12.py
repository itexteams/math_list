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


def bt_dang18_p2_b1_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Mã vẽ TikZ hình hộp ABCD.A'B'C'D' có các điểm I, K chính xác 100% như ảnh[cite: 20]
    tikz_figure = """\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (B) at (0,0);
    \\coordinate (C) at (3.2,-0.5);
    \\coordinate (A) at (1.8,1.2);
    \\coordinate (D) at ($(A)+(C)-(B)$);
    \\coordinate (B') at (0.4,3.2);
    \\coordinate (A') at ($(A)+(B')-(B)$);
    \\coordinate (C') at ($(C)+(B')-(B)$);
    \\coordinate (D') at ($(D)+(B')-(B)$);
    \\coordinate (I) at ($(A')!0.5!(B)$);
    \\coordinate (K) at ($(B')!0.5!(C)$);
    \\draw[line width=1pt] (B)--(C)--(D)--(D')--(A')--(B')--cycle;
    \\draw[line width=1pt] (B')--(C')--(D') (C)--(C') (B')--(C) (A')--(C');
    \\draw[line width=1pt, dashed] (B)--(A)--(D) (A)--(A') (A)--(C) (B)--(D) (A')--(B) (A)--(B') (B)--(C') (A')--(D) (I)--(K);
    \\fill (B) circle (1pt) node[below left] {$B$};
    \\fill (C) circle (1pt) node[below] {$C$};
    \\fill (A) circle (1pt) node[above] {$A$};
    \\fill (D) circle (1pt) node[right] {$D$};
    \\fill (B') circle (1pt) node[above left] {$B'$};
    \\fill (A') circle (1pt) node[above] {$A'$};
    \\fill (C') circle (1pt) node[above right] {$C'$};
    \\fill (D') circle (1pt) node[above right] {$D'$};
    \\fill (I) circle (1pt) node[left] {$I$};
    \\fill (K) circle (1pt) node[above] {$K$};
    \\end{tikzpicture}
    \\end{center}"""
    
    # Nội dung câu hỏi[cite: 20]
    noidungcauhoi = (
        """Cho hình hộp $ABCD.A'B'C'D'$. Gọi $I$ và $K$ lần lượt là tâm của hình bình hành $ABB'A'$ và $BCC'B'$. Gọi $M$ là điểm trên cạnh $AC$ sao cho $AC = 3MC$. Lấy $N$ trên đoạn $C'D$ sao cho $C'N = xC'D$. %s"""
        % (tikz_figure)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: Vectơ AB = Vectơ D'C'[cite: 20]
    nb_da_1_d = "\\True $\\vec{AB} = \\vec{D'C'}$"
    nb_da_1_s = "$\\vec{AB} = \\vec{C'D'}$"
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Trong hình hộp $ABCD.A'B'C'D'$, mặt đáy $ABCD$ và mặt đáy $A'B'C'D'$ là các hình bình hành bằng nhau. \\\\ Do đó ta có các cặp vectơ cạnh đối song song và cùng hướng: \\\\ $\\vec{AB} = \\vec{DC}$ và $\\vec{DC} = \\vec{D'C'}$. \\\\ Từ đó suy ra $\\vec{AB} = \\vec{D'C'}$. \\\\ Mệnh đề $\\vec{AB} = \\vec{C'D'}$ là sai vì $\\vec{C'D'}$ ngược hướng với $\\vec{AB}$. \\\\ Do đó mệnh đề là %s."""
        % ("đúng" if "\\True" in nb_da_1 else "sai")
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: Quy tắc hình hộp xuất phát từ đỉnh B: \vec{BA} + \vec{BC} + \vec{BB'} = \vec{BD'}[cite: 20]
    th_da_1_d = "\\True $\\vec{BA} + \\vec{BC} + \\vec{BB'} = \\vec{BD'}$"
    th_da_1_s = "$\\vec{BA} + \\vec{BC} + \\vec{BB'} = \\vec{BC'}$"
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Áp dụng quy tắc hình bình hành cho đáy $ABCD$, ta có: \\\\ $\\vec{BA} + \\vec{BC} = \\vec{BD}$. \\\\ Khi đó: \\\\ $\\vec{BA} + \\vec{BC} + \\vec{BB'} = \\vec{BD} + \\vec{BB'}$. \\\\ Trong hình bình hành $BDD'B'$, theo quy tắc hình bình hành ta có: \\\\ $\\vec{BD} + \\vec{BB'} = \\vec{BD'}$. \\\\ Đây chính là quy tắc hình hộp xuất phát từ đỉnh $B$. \\\\ Vì $\\vec{BD'} \\neq \\vec{BC'}$ nên khẳng định $\\vec{BA} + \\vec{BC} + \\vec{BB'} = \\vec{BC'}$ là sai. \\\\ Do đó mệnh đề là %s."""
        % ("đúng" if "\\True" in th_da_1 else "sai")
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: BD + 2*IK = 2*BC (đúng) hoặc BD + 2*IK = BC (sai)[cite: 20]
    vd_da_1_d = "\\True $\\vec{BD} + 2\\vec{IK} = 2\\vec{BC}$"
    vd_da_1_s = "$\\vec{BD} + 2\\vec{IK} = \\vec{BC}$"
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Vì $I$ là tâm của hình bình hành $ABB'A'$ nên $I$ là trung điểm của đoạn thẳng $A'B$. \\\\ Vì $K$ là tâm của hình bình hành $BCC'B'$ nên $K$ là trung điểm của đoạn thẳng $BC'$. \\\\ Xét tam giác $BA'C'$, đoạn thẳng $IK$ là đường trung bình của tam giác ứng với cạnh $A'C'$, suy ra: \\\\ $\\vec{IK} = \\frac{1}{2}\\vec{A'C'} \\Leftrightarrow 2\\vec{IK} = \\vec{A'C'}$. \\\\ Mặt khác, vì tứ giác $ACC'A'$ là hình bình hành nên $\\vec{A'C'} = \\vec{AC}$. \\\\ Khi đó: \\\\ $\\vec{BD} + 2\\vec{IK} = \\vec{BD} + \\vec{AC} = (\\vec{BC} + \\vec{CD}) + (\\vec{AB} + \\vec{BC}) = (\\vec{CD} + \\vec{AB}) + 2\\vec{BC}$. \\\\ Vì $\\vec{CD}$ và $\\vec{AB}$ là hai vectơ đối nhau nên $\\vec{CD} + \\vec{AB} = \\vec{0}$. \\\\ Do đó: $\\vec{BD} + 2\\vec{IK} = 2\\vec{BC} \\neq \\vec{BC}$. \\\\ Vậy khẳng định $\\vec{BD} + 2\\vec{IK} = \\vec{BC}$ là sai. Mệnh đề là %s."""
        % ("đúng" if "\\True" in vd_da_1 else "sai")
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: Với x = 2/3 thì MN // BD' (đúng), với x = 1/3 thì MN // BD' (sai)[cite: 20]
    vdc_da_1_d = "\\True Với $x = \\frac{2}{3}$ thì $MN // BD'$"
    vdc_da_1_s = "Với $x = \\frac{1}{3}$ thì $MN // BD'$"
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Chọn ba vectơ không đồng phẳng làm cơ sở: $\\vec{a} = \\vec{BA}, \\vec{b} = \\vec{BC}, \\vec{c} = \\vec{BB'}$. \\\\ Khi đó theo quy tắc hình hộp, ta có: \\\\ $\\vec{BD'} = \\vec{BA} + \\vec{BC} + \\vec{BB'} = \\vec{a} + \\vec{b} + \\vec{c}$. \\\\ Điểm $M$ nằm trên cạnh $AC$ thỏa mãn $AC = 3MC$, suy ra: \\\\ $\\vec{BM} = \\vec{BA} + \\vec{AM} = \\vec{BA} + \\frac{2}{3}\\vec{AC} = \\vec{a} + \\frac{2}{3}(\\vec{BC} - \\vec{BA}) = \\frac{1}{3}\\vec{a} + \\frac{2}{3}\\vec{b}$. \\\\ Điểm $N$ nằm trên đoạn thẳng $C'D$ thỏa mãn $\\vec{C'N} = x\\vec{C'D}$, ta có: \\\\ $\\vec{BN} = \\vec{BC'} + \\vec{C'N} = (\\vec{b} + \\vec{c}) + x(\\vec{BD} - \\vec{BC'}) = (\\vec{b} + \\vec{c}) + x(\\vec{a} + \\vec{b} - \\vec{b} - \\vec{c}) = x\\vec{a} + \\vec{b} + (1 - x)\\vec{c}$. \\\\ Khi đó vectơ $\\vec{MN}$ được biểu diễn là: \\\\ $\\vec{MN} = \\vec{BN} - \\vec{BM} = \\left(x - \\frac{1}{3}\\right)\\vec{a} + \\frac{1}{3}\\vec{b} + (1 - x)\\vec{c}$. \\\\ Để $MN // BD'$ thì hai vectơ $\\vec{MN}$ và $\\vec{BD'}$ phải cùng phương, tức là tồn tại hệ số $k \\neq 0$ sao cho $\\vec{MN} = k\\vec{BD'}$. \\\\ Do $\\vec{BD'} = 1\\vec{a} + 1\\vec{b} + 1\\vec{c}$ và hệ số của $\\vec{b}$ trong $\\vec{MN}$ là $\\frac{1}{3}$, suy ra: \\\\ $k = \\frac{1}{3} \\Rightarrow \\begin{cases} x - \\frac{1}{3} = \\frac{1}{3} \\\\ 1 - x = \\frac{1}{3} \\end{cases} \\Leftrightarrow x = \\frac{2}{3}$. \\\\ Do đó điều kiện để $MN // BD'$ là $x = \\frac{2}{3}$, khẳng định $x = \\frac{1}{3}$ là sai. \\\\ Vì vậy mệnh đề là %s."""
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
    
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


def bt_dang23_p2_b1_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Mã vẽ TikZ tứ diện ABCD có M, N, G là trung điểm AB, CD, MN chính xác 100% như ảnh[cite: 20]
    tikz_figure = """\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,2.8);
    \\coordinate (B) at (-1.8,-0.2);
    \\coordinate (C) at (-0.4,-1.2);
    \\coordinate (D) at (1.8,-0.1);
    \\coordinate (M) at ($(A)!0.5!(B)$);
    \\coordinate (N) at ($(C)!0.5!(D)$);
    \\coordinate (G) at ($(M)!0.5!(N)$);
    \\draw[line width=1pt] (A)--(B)--(C)--(D)--(A)--(C);
    \\draw[line width=1pt, dashed] (B)--(D) (M)--(N);
    \\fill (A) circle (1pt) node[above] {$A$};
    \\fill (B) circle (1pt) node[left] {$B$};
    \\fill (C) circle (1pt) node[below] {$C$};
    \\fill (D) circle (1pt) node[right] {$D$};
    \\fill (M) circle (1pt) node[above left] {$M$};
    \\fill (N) circle (1pt) node[below right] {$N$};
    \\fill (G) circle (1pt) node[above right] {$G$};
    \\end{tikzpicture}
    \\end{center}"""
    
    # Nội dung câu hỏi[cite: 20]
    noidungcauhoi = (
        """Cho tứ diện $ABCD$. Gọi $M, N, G$ lần lượt là trung điểm của $AB, CD, MN$. %s"""
        % (tikz_figure)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: Vectơ đối nhau qua trung điểm M của AB[cite: 20]
    nb_da_1_d = "\\True $\\vec{MA} + \\vec{MB} = \\vec{0}$"
    nb_da_1_s = "$\\vec{MA} + \\vec{MB} = 2\\vec{AB}$"
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Vì $M$ là trung điểm của đoạn thẳng $AB$ nên hai vectơ $\\vec{MA}$ và $\\vec{MB}$ là hai vectơ có cùng độ dài nhưng ngược hướng nhau (hai vectơ đối nhau). \\\\ Do đó ta có hệ thức: \\\\ $\\vec{MA} + \\vec{MB} = \\vec{0}$. \\\\ Do đó khẳng định là %s."""
        % ("đúng" if "\\True" in nb_da_1 else "sai")
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: Quy tắc trung điểm N của đoạn thẳng CD với điểm M bất kỳ[cite: 20]
    th_da_1_d = "\\True $\\vec{MC} + \\vec{MD} = 2\\vec{MN}$"
    th_da_1_s = "$\\vec{MC} + \\vec{MD} = \\vec{MN}$"
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Vì $N$ là trung điểm của đoạn thẳng $CD$, với điểm $M$ bất kỳ ta có: \\\\ $\\vec{MC} + \\vec{MD} = (\\vec{MN} + \\vec{NC}) + (\\vec{MN} + \\vec{ND}) = 2\\vec{MN} + (\\vec{NC} + \\vec{ND})$. \\\\ Do $N$ là trung điểm của $CD$ nên $\\vec{NC} + \\vec{ND} = \\vec{0}$. \\\\ Suy ra: \\\\ $\\vec{MC} + \\vec{MD} = 2\\vec{MN}$. \\\\ Do đó khẳng định là %s."""
        % ("đúng" if "\\True" in th_da_1 else "sai")
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: Đẳng thức vectơ với trọng tâm G của tứ diện[cite: 20]
    vd_da_1_d = "\\True $\\vec{GA} + \\vec{GB} + \\vec{GC} + \\vec{GD} = \\vec{0}$"
    vd_da_1_s = "$\\vec{GA} + \\vec{GB} = \\vec{GC} + \\vec{GD}$"
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Vì $M$ là trung điểm của $AB$ và $N$ là trung điểm của $CD$ nên với điểm $G$ ta có: \\\\ $\\vec{GA} + \\vec{GB} = 2\\vec{GM}$. \\\\ $\\vec{GC} + \\vec{GD} = 2\\vec{GN}$. \\\\ Mặt khác, vì $G$ là trung điểm của đoạn thẳng $MN$ nên $\\vec{GM} + \\vec{GN} = \\vec{0} \\Leftrightarrow \\vec{GM} = -\\vec{GN}$. \\\\ Suy ra: \\\\ $\\vec{GA} + \\vec{GB} = 2\\vec{GM} = -2\\vec{GN} = -(\\vec{GC} + \\vec{GD})$ \\\\ $\\Leftrightarrow \\vec{GA} + \\vec{GB} + \\vec{GC} + \\vec{GD} = \\vec{0}$. \\\\ Do $\\vec{GA} + \\vec{GB} = -(\\vec{GC} + \\vec{GD})$ nên khẳng định $\\vec{GA} + \\vec{GB} = \\vec{GC} + \\vec{GD}$ là sai (chỉ xảy ra khi hai vế cùng bằng $\\vec{0}$, tức là $M \\equiv N$, vô lý trong tứ diện). \\\\ Do đó mệnh đề là %s."""
        % ("đúng" if "\\True" in vd_da_1 else "sai")
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: Biểu diễn tổng hai vectơ chéo nhau qua vectơ trung đoạn MN[cite: 20]
    vdc_da_1_d = "\\True $\\vec{AD} + \\vec{BC} = 2\\vec{MN}$"
    vdc_da_1_s = "$\\vec{AD} + \\vec{BC} = \\vec{MN}$"
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Chèn các điểm $M$ và $N$ vào hai vectơ $\\vec{AD}$ và $\\vec{BC}$, ta có: \\\\ $\\vec{AD} = \\vec{AM} + \\vec{MN} + \\vec{ND}$. \\\\ $\\vec{BC} = \\vec{BM} + \\vec{MN} + \\vec{NC}$. \\\\ Cộng vế theo vế hai đẳng thức trên, ta được: \\\\ $\\vec{AD} + \\vec{BC} = (\\vec{AM} + \\vec{BM}) + (\\vec{MN} + \\vec{MN}) + (\\vec{ND} + \\vec{NC})$. \\\\ Vì $M$ là trung điểm của $AB$ nên $\\vec{AM} + \\vec{BM} = \\vec{0}$. \\\\ Vì $N$ là trung điểm của $CD$ nên $\\vec{ND} + \\vec{NC} = \\vec{0}$. \\\\ Do đó: \\\\ $\\vec{AD} + \\vec{BC} = \\vec{0} + 2\\vec{MN} + \\vec{0} = 2\\vec{MN}$. \\\\ Do thiếu hệ số $2$ nên khẳng định $\\vec{AD} + \\vec{BC} = \\vec{MN}$ là sai. \\\\ Vì vậy mệnh đề là %s."""
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
    
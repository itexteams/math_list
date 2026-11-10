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


def bt_dang36_p2_b1_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Mã vẽ TikZ hình chóp S.ABCD đáy hình thoi tâm O, các điểm P, I chuẩn 100% như ảnh[cite: 20]
    # Chú ý: Không sử dụng ký tự % comment bên trong chuỗi để tránh lỗi format string
    tikz_figure = """\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (D) at (0,0);
    \\coordinate (C) at (2.2,-0.4);
    \\coordinate (A) at (1.2,0.8);
    \\coordinate (B) at ($(A)+(C)-(D)$);
    \\coordinate (O) at ($(A)!0.5!(C)$);
    \\coordinate (S) at ($(O)+(0,3.2)$);
    \\coordinate (P) at ($(B)!0.3333!(D)$);
    \\coordinate (I) at ($(B)!0.5!(C)$);
    \\draw[line width=1pt] (S)--(D)--(C)--(B)--(S)--(C);
    \\draw[line width=1pt] (S)--(I);
    \\draw[line width=1pt, dashed] (D)--(A)--(B) (S)--(A) (A)--(C) (B)--(D) (S)--(O) (S)--(P);
    \\fill (A) circle (1pt) node[left] {$A$};
    \\fill (B) circle (1pt) node[right] {$B$};
    \\fill (C) circle (1pt) node[below] {$C$};
    \\fill (D) circle (1pt) node[below left] {$D$};
    \\fill (O) circle (1pt) node[below left] {$O$};
    \\fill (S) circle (1pt) node[above] {$S$};
    \\fill (P) circle (1pt) node[above left] {$P$};
    \\fill (I) circle (1pt) node[below] {$I$};
    \\end{tikzpicture}
    \\end{center}"""
    
    
    
    # Nội dung câu hỏi[cite: 20]
    noidungcauhoi = (
        """Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình thoi tâm $O$, cạnh bằng $a$, $\\widehat{BAD} = 120^\\circ$, $SA = SC$, $SB = SD$ và $SO = \\frac{a\\sqrt{3}}{2}$. Gọi $P$ là điểm trên đường thẳng $BD$ sao cho $\\vec{BP} = \\frac{1}{3}\\vec{BD}$. %s"""
        % (tikz_figure)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: Tập hợp điểm M là mặt cầu tâm O bán kính a/2[cite: 20]
    nb_da_1_d = "\\True $|\\vec{MA} + \\vec{MB} + \\vec{MC} + \\vec{MD}| = |\\vec{MA} - \\vec{MB} - \\vec{MC} + \\vec{MD}| \\Leftrightarrow M$ thuộc mặt cầu tâm $O$ bán kính $\\frac{a}{2}$"
    nb_da_1_s = "$|\\vec{MA} + \\vec{MB} + \\vec{MC} + \\vec{MD}| = |\\vec{MA} - \\vec{MB} - \\vec{MC} + \\vec{MD}| \\Leftrightarrow M$ thuộc mặt cầu tâm $O$ bán kính $a$"
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Vì $O$ là giao điểm hai đường chéo của hình thoi $ABCD$ nên $O$ là trung điểm của cả $AC$ và $BD$, suy ra $\\vec{OA} + \\vec{OB} + \\vec{OC} + \\vec{OD} = \\vec{0}$. \\\\ Khi đó ta rút gọn hai vế của phương trình: \\\\ $\\bullet$ Vế trái: $\\vec{MA} + \\vec{MB} + \\vec{MC} + \\vec{MD} = 4\\vec{MO} + (\\vec{OA} + \\vec{OB} + \\vec{OC} + \\vec{OD}) = 4\\vec{MO}$. \\\\ $\\Rightarrow |\\vec{MA} + \\vec{MB} + \\vec{MC} + \\vec{MD}| = |4\\vec{MO}| = 4MO$. \\\\ $\\bullet$ Vế phải: $(\\vec{MA} - \\vec{MB}) + (\\vec{MD} - \\vec{MC}) = \\vec{BA} + \\vec{CD}$. \\\\ Vì $ABCD$ là hình thoi nên $\\vec{CD} = \\vec{BA}$, suy ra $\\vec{BA} + \\vec{CD} = 2\\vec{BA}$. \\\\ $\\Rightarrow |\\vec{MA} - \\vec{MB} - \\vec{MC} + \\vec{MD}| = |2\\vec{BA}| = 2AB = 2a$. \\\\ Từ phương trình đề bài cho, ta có: \\\\ $4MO = 2a \\Leftrightarrow MO = \\frac{a}{2}$. \\\\ Do đó tập hợp điểm $M$ là mặt cầu tâm $O$ bán kính $R = \\frac{a}{2}$. \\\\ Vì vậy mệnh đề là %s."""
        % ("đúng" if "\\True" in nb_da_1 else "sai")
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: (\vec{SB}, \vec{BO}) = 135°[cite: 20]
    th_da_1_d = "\\True $(\\vec{SB}, \\vec{BO}) = 135^\\circ$"
    th_da_1_s = "$(\\vec{SB}, \\vec{BO}) = 45^\\circ$"
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Vì tam giác $SAC$ cân tại $S$ ($SA = SC$) có $O$ là trung điểm $AC$ nên $SO \\perp AC$. \\\\ Vì tam giác $SBD$ cân tại $S$ ($SB = SD$) có $O$ là trung điểm $BD$ nên $SO \\perp BD$. \\\\ Suy ra $SO \\perp (ABCD)$ và tam giác $SOB$ vuông tại $O$. \\\\ Đáy $ABCD$ là hình thoi cạnh $a$ có $\\widehat{BAD} = 120^\\circ \\Rightarrow \\widehat{ABC} = 60^\\circ$. \\\\ Đường chéo $BD$ là tia phân giác của $\\widehat{ABC}$, suy ra $\\widehat{ABO} = 30^\\circ$. \\\\ Trong tam giác vuông $OAB$ tại $O$, ta có: \\\\ $OB = AB \\cdot \\cos \\widehat{ABO} = a \\cdot \\cos 30^\\circ = \\frac{a\\sqrt{3}}{2}$. \\\\ Xét tam giác vuông $SOB$ tại $O$, ta có $SO = \\frac{a\\sqrt{3}}{2}$ và $OB = \\frac{a\\sqrt{3}}{2}$. \\\\ Suy ra tam giác $SOB$ là tam giác vuông cân tại $O$, do đó góc $\\widehat{SBO} = 45^\\circ$. \\\\ Góc giữa hai vectơ $\\vec{SB}$ và $\\vec{BO}$ là: \\\\ $(\\vec{SB}, \\vec{BO}) = 180^\\circ - (\\vec{BS}, \\vec{BO}) = 180^\\circ - \\widehat{SBO} = 180^\\circ - 45^\\circ = 135^\\circ$. \\\\ Do đó mệnh đề là %s."""
        % ("đúng" if "\\True" in th_da_1 else "sai")
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: I là trung điểm BC, tích vô hướng \vec{SI} . \vec{BD}[cite: 20]
    vd_da_1_d = "\\True $I$ là trung điểm đoạn $BC$. Khi đó: $\\vec{SI} \\cdot \\vec{BD} = -\\frac{3a^2}{4}$"
    vd_da_1_s = "$I$ là trung điểm đoạn $BC$. Khi đó: $\\vec{SI} \\cdot \\vec{BD} = \\frac{3a^2}{4}$"
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Phân tích vectơ $\\vec{SI}$ qua điểm $O$: $\\vec{SI} = \\vec{SO} + \\vec{OI}$. \\\\ Khi đó tích vô hướng giữa $\\vec{SI}$ và $\\vec{BD}$ là: \\\\ $\\vec{SI} \\cdot \\vec{BD} = (\\vec{SO} + \\vec{OI}) \\cdot \\vec{BD} = \\vec{SO} \\cdot \\vec{BD} + \\vec{OI} \\cdot \\vec{BD}$. \\\\ Vì $SO \\perp (ABCD)$ mà $BD \\subset (ABCD)$ nên $SO \\perp BD$, suy ra $\\vec{SO} \\cdot \\vec{BD} = 0$. \\\\ Trong tam giác $ABC$, vì $O$ là trung điểm $AC$ và $I$ là trung điểm $BC$ nên $OI$ là đường trung bình, suy ra: \\\\ $\\vec{OI} = \\frac{1}{2}\\vec{AB}$. \\\\ Khi đó: \\\\ $\\vec{OI} \\cdot \\vec{BD} = \\frac{1}{2}\\vec{AB} \\cdot \\vec{BD} = -\\frac{1}{2}\\vec{BA} \\cdot \\vec{BD} = -\\frac{1}{2} BA \\cdot BD \\cdot \\cos(\\vec{BA}, \\vec{BD})$. \\\\ Ta có $BA = a$, $BD = 2OB = a\\sqrt{3}$, và $(\\vec{BA}, \\vec{BD}) = \\widehat{ABD} = 30^\\circ$. \\\\ Suy ra: \\\\ $\\vec{SI} \\cdot \\vec{BD} = 0 - \\frac{1}{2} \\cdot a \\cdot (a\\sqrt{3}) \\cdot \\cos 30^\\circ = -\\frac{a^2\\sqrt{3}}{2} \\cdot \\frac{\\sqrt{3}}{2} = -\\frac{3a^2}{4}$. \\\\ Khẳng định $\\vec{SI} \\cdot \\vec{BD} = \\frac{3a^2}{4}$ bị sai dấu. \\\\ Do đó mệnh đề là %s."""
        % ("đúng" if "\\True" in vd_da_1 else "sai")
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: Độ dài vectơ |\vec{SA} + \vec{SB} + \vec{SC}|[cite: 20]
    vdc_da_1_d = "\\True $|\\vec{SA} + \\vec{SB} + \\vec{SC}| = \\frac{a\\sqrt{30}}{2}$"
    vdc_da_1_s = "$|\\vec{SA} + \\vec{SB} + \\vec{SC}| = \\frac{a\\sqrt{6}}{2}$"
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Vì $O$ là trung điểm của đoạn thẳng $AC$ nên theo quy tắc trung điểm ta có: \\\\ $\\vec{SA} + \\vec{SC} = 2\\vec{SO}$. \\\\ Biểu diễn vectơ $\\vec{SB}$ qua đỉnh $O$: \\\\ $\\vec{SB} = \\vec{SO} + \\vec{OB}$. \\\\ Khi đó tổng ba vectơ là: \\\\ $\\vec{u} = \\vec{SA} + \\vec{SB} + \\vec{SC} = 2\\vec{SO} + (\\vec{SO} + \\vec{OB}) = 3\\vec{SO} + \\vec{OB}$. \\\\ Vì $SO \\perp (ABCD)$ và $OB \\subset (ABCD)$ nên $SO \\perp OB$, suy ra hai vectơ $\\vec{SO}$ và $\\vec{OB}$ vuông góc với nhau ($\\vec{SO} \\cdot \\vec{OB} = 0$). \\\\ Áp dụng định lý Pythagore cho bình phương độ dài của vectơ $\\vec{u}$: \\\\ $|\\vec{u}|^2 = |3\\vec{SO} + \\vec{OB}|^2 = 9|\\vec{SO}|^2 + |\\vec{OB}|^2 + 6\\vec{SO} \\cdot \\vec{OB} = 9SO^2 + OB^2$. \\\\ Thay số với $SO = \\frac{a\\sqrt{3}}{2}$ và $OB = \\frac{a\\sqrt{3}}{2}$: \\\\ $|\\vec{u}|^2 = 9 \\cdot \\left(\\frac{a\\sqrt{3}}{2}\\right)^2 + \\left(\\frac{a\\sqrt{3}}{2}\\right)^2 = 9 \\cdot \\frac{3a^2}{4} + \\frac{3a^2}{4} = 10 \\cdot \\frac{3a^2}{4} = \\frac{30a^2}{4}$. \\\\ Suy ra: \\\\ $|\\vec{SA} + \\vec{SB} + \\vec{SC}| = \\sqrt{\\frac{30a^2}{4}} = \\frac{a\\sqrt{30}}{2}$. \\\\ Khẳng định $|\\vec{SA} + \\vec{SB} + \\vec{SC}| = \\frac{a\\sqrt{6}}{2}$ là sai. \\\\ Do đó mệnh đề là %s."""
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
    
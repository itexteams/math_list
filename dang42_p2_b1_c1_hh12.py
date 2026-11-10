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


def bt_dang42_p2_b1_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Mã vẽ TikZ tứ diện OABC có OA, OB, OC đôi một vuông góc, M và N là trung điểm AB, OC chuẩn 100% như ảnh[cite: 20]
    # Chú ý: Tuyệt đối không dùng ký hiệu % comment bên trong chuỗi để tránh lỗi format string
    tikz_figure = """\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (O) at (0,0);
    \\coordinate (A) at (1.0,-0.8);
    \\coordinate (B) at (2.6,0.1);
    \\coordinate (C) at (0,2.6);
    \\coordinate (M) at ($(A)!0.5!(B)$);
    \\coordinate (N) at ($(O)!0.5!(C)$);
    \\draw[line width=1pt] (C)--(O)--(A)--(M)--(B)--(C)--(A) (C)--(M);
    \\draw[line width=1pt, dashed] (O)--(B) (O)--(M) (M)--(N);
    \\fill (O) circle (1pt) node[below left] {$O$};
    \\fill (A) circle (1pt) node[below] {$A$};
    \\fill (B) circle (1pt) node[right] {$B$};
    \\fill (C) circle (1pt) node[above] {$C$};
    \\fill (M) circle (1pt) node[below right] {$M$};
    \\fill (N) circle (1pt) node[left] {$N$};
    \\end{tikzpicture}
    \\end{center}"""
    
    
    
    # Nội dung câu hỏi[cite: 20]
    noidungcauhoi = (
        """Cho tứ diện $OABC$ có các cạnh $OA, OB, OC$ đôi một vuông góc và $OA = OB = OC = a$. Gọi $M, N$ lần lượt là trung điểm các cạnh $AB, OC$. %s"""
        % (tikz_figure)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: Biểu diễn vectơ \vec{MN} qua các vectơ cạnh[cite: 20]
    nb_da_1_d = "\\True $\\vec{MN} = \\frac{1}{2}\\left(\\vec{OC} - \\vec{OA} - \\vec{OB}\\right)$"
    nb_da_1_s = "$\\vec{MN} = \\frac{1}{2}\\left(\\vec{OA} + \\vec{BC}\\right)$"
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Biểu diễn vectơ $\\vec{MN}$ qua điểm gốc $O$, ta có: \\\\ $\\vec{MN} = \\vec{ON} - \\vec{OM}$. \\\\ Do $N$ là trung điểm của cạnh $OC$ nên $\\vec{ON} = \\frac{1}{2}\\vec{OC}$. \\\\ Do $M$ là trung điểm của cạnh $AB$ nên $\\vec{OM} = \\frac{1}{2}(\\vec{OA} + \\vec{OB})$. \\\\ Suy ra: \\\\ $\\vec{MN} = \\frac{1}{2}\\vec{OC} - \\frac{1}{2}(\\vec{OA} + \\vec{OB}) = \\frac{1}{2}\\left(\\vec{OC} - \\vec{OA} - \\vec{OB}\\right)$. \\\\ Mặt khác, xét biểu thức: \\\\ $\\frac{1}{2}(\\vec{OA} + \\vec{BC}) = \\frac{1}{2}(\\vec{OA} + \\vec{OC} - \\vec{OB}) \\neq \\vec{MN}$. \\\\ Do đó khẳng định $\\vec{MN} = \\frac{1}{2}(\\vec{OA} + \\vec{BC})$ là sai. \\\\ Vì vậy mệnh đề là %s."""
        % ("đúng" if "\\True" in nb_da_1 else "sai")
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: cos(\vec{OM}, \vec{CM}) = 1/\sqrt{3}[cite: 20]
    th_da_1_d = "\\True $\\cos(\\vec{OM}, \\vec{CM}) = \\frac{1}{\\sqrt{3}}$"
    th_da_1_s = "$\\cos(\\vec{OM}, \\vec{CM}) = \\frac{\\sqrt{2}}{3}$"
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Xét tam giác $OAB$ vuông tại $O$ có $OA = OB = a$, $M$ là trung điểm cạnh huyền $AB$: \\\\ $AB = \\sqrt{OA^2 + OB^2} = a\\sqrt{2} \\Rightarrow OM = \\frac{1}{2}AB = \\frac{a\\sqrt{2}}{2}$. \\\\ Vì $OC \\perp OA$ và $OC \\perp OB$ nên $OC \\perp (OAB) \\Rightarrow OC \\perp OM$, suy ra tam giác $OCM$ vuông tại $O$. \\\\ Áp dụng định lý Pythagore trong tam giác vuông $OCM$: \\\\ $CM = \\sqrt{OC^2 + OM^2} = \\sqrt{a^2 + \\left(\\frac{a\\sqrt{2}}{2}\\right)^2} = \\sqrt{a^2 + \\frac{a^2}{2}} = \\frac{a\\sqrt{6}}{2}$. \\\\ Ta có $\\vec{CM} = \\vec{OM} - \\vec{OC}$, suy ra tích vô hướng: \\\\ $\\vec{OM} \\cdot \\vec{CM} = \\vec{OM} \\cdot (\\vec{OM} - \\vec{OC}) = |\\vec{OM}|^2 - \\vec{OM} \\cdot \\vec{OC} = OM^2 - 0 = \\left(\\frac{a\\sqrt{2}}{2}\\right)^2 = \\frac{a^2}{2}$. \\\\ Khi đó: \\\\ $\\cos(\\vec{OM}, \\vec{CM}) = \\frac{\\vec{OM} \\cdot \\vec{CM}}{|\\vec{OM}| \\cdot |\\vec{CM}|} = \\frac{\\frac{a^2}{2}}{\\frac{a\\sqrt{2}}{2} \\cdot \\frac{a\\sqrt{6}}{2}} = \\frac{\\frac{a^2}{2}}{\\frac{a^2\\sqrt{12}}{4}} = \\frac{1}{2} \\cdot \\frac{4}{2\\sqrt{3}} = \\frac{1}{\\sqrt{3}}$. \\\\ Do đó mệnh đề là %s."""
        % ("đúng" if "\\True" in th_da_1 else "sai")
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: \vec{MN} \cdot \vec{OA} = -a^2/2[cite: 20]
    vd_da_1_d = "\\True $\\vec{MN} \\cdot \\vec{OA} = -\\frac{a^2}{2}$"
    vd_da_1_s = "$\\vec{MN} \\cdot \\vec{OA} = \\frac{a^2}{2}$"
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Theo kết quả phân tích ở câu a, ta có: \\\\ $\\vec{MN} = \\frac{1}{2}\\vec{OC} - \\frac{1}{2}\\vec{OA} - \\frac{1}{2}\\vec{OB}$. \\\\ Khi đó tích vô hướng của hai vectơ $\\vec{MN}$ và $\\vec{OA}$ là: \\\\ $\\vec{MN} \\cdot \\vec{OA} = \\left(\\frac{1}{2}\\vec{OC} - \\frac{1}{2}\\vec{OA} - \\frac{1}{2}\\vec{OB}\\right) \\cdot \\vec{OA}$ \\\\ $= \\frac{1}{2}\\vec{OC} \\cdot \\vec{OA} - \\frac{1}{2}\\vec{OA}^2 - \\frac{1}{2}\\vec{OB} \\cdot \\vec{OA}$. \\\\ Vì ba cạnh $OA, OB, OC$ đôi một vuông góc nên: \\\\ $\\vec{OC} \\cdot \\vec{OA} = 0$ và $\\vec{OB} \\cdot \\vec{OA} = 0$. \\\\ Hơn nữa $\\vec{OA}^2 = OA^2 = a^2$. \\\\ Suy ra: \\\\ $\\vec{MN} \\cdot \\vec{OA} = 0 - \\frac{1}{2}a^2 - 0 = -\\frac{a^2}{2}$. \\\\ Do đó mệnh đề là %s."""
        % ("đúng" if "\\True" in vd_da_1 else "sai")
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: |\vec{CB} + \vec{OA}| = a\sqrt{3} (đúng) hoặc a\sqrt{2} (sai)[cite: 20]
    vdc_da_1_d = "\\True $|\\vec{CB} + \\vec{OA}| = a\\sqrt{3}$"
    vdc_da_1_s = "$|\\vec{CB} + \\vec{OA}| = a\\sqrt{2}$"
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Ta biểu diễn vectơ tổng theo ba vectơ đôi một vuông góc xuất phát từ gốc $O$: \\\\ $\\vec{u} = \\vec{CB} + \\vec{OA} = (\\vec{OB} - \\vec{OC}) + \\vec{OA} = \\vec{OA} + \\vec{OB} - \\vec{OC}$. \\\\ Bình phương vô hướng của vectơ $\\vec{u}$, ta được: \\\\ $|\\vec{u}|^2 = (\\vec{OA} + \\vec{OB} - \\vec{OC})^2$ \\\\ $= \\vec{OA}^2 + \\vec{OB}^2 + \\vec{OC}^2 + 2(\\vec{OA} \\cdot \\vec{OB} - \\vec{OA} \\cdot \\vec{OC} - \\vec{OB} \\cdot \\vec{OC})$. \\\\ Vì các cạnh $OA, OB, OC$ đôi một vuông góc nên: \\\\ $\\vec{OA} \\cdot \\vec{OB} = 0, \\quad \\vec{OA} \\cdot \\vec{OC} = 0, \\quad \\vec{OB} \\cdot \\vec{OC} = 0$. \\\\ Và $OA = OB = OC = a$. Do đó: \\\\ $|\\vec{u}|^2 = a^2 + a^2 + a^2 + 0 = 3a^2$. \\\\ Suy ra độ dài của vectơ $\\vec{u}$ là: \\\\ $|\\vec{CB} + \\vec{OA}| = \\sqrt{3a^2} = a\\sqrt{3} \\neq a\\sqrt{2}$. \\\\ Vì vậy khẳng định $|\\vec{CB} + \\vec{OA}| = a\\sqrt{2}$ là sai. Mệnh đề là %s."""
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
    
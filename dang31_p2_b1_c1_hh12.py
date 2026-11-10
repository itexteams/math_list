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


def bt_dang31_p2_b1_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Mã vẽ TikZ hình lập phương ABCD.A'B'C'D' có đáy trên ABCD và đáy dưới A'B'C'D', giao điểm hai đáy I và I' chuẩn 100% như ảnh[cite: 20]
    # Chú ý: Tuyệt đối không dùng ký hiệu % comment bên trong string để tránh lỗi định dạng chuỗi
    tikz_figure = """\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,2.4);
    \\coordinate (B) at (1.4,3.1);
    \\coordinate (D) at (3.2,2.3);
    \\coordinate (C) at ($(B)+(D)-(A)$);
    \\coordinate (A') at (0,0);
    \\coordinate (B') at ($(B)+(A')-(A)$);
    \\coordinate (C') at ($(C)+(A')-(A)$);
    \\coordinate (D') at ($(D)+(A')-(A)$);
    \\coordinate (I) at ($(A)!0.5!(C)$);
    \\coordinate (I') at ($(A')!0.5!(C')$);
    \\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle;
    \\draw[line width=1pt] (A)--(C) (B)--(D);
    \\draw[line width=1pt] (A)--(A') (D)--(D') (C)--(C');
    \\draw[line width=1pt] (A')--(D')--(C');
    \\draw[line width=1pt, dashed] (B)--(B') (A')--(B')--(C');
    \\draw[line width=1pt, dashed] (A')--(C') (B')--(D');
    \\draw[line width=1pt, dashed] (I)--(I');
    \\fill (A) circle (1pt) node[left] {$A$};
    \\fill (B) circle (1pt) node[above] {$B$};
    \\fill (C) circle (1pt) node[above right] {$C$};
    \\fill (D) circle (1pt) node[below right] {$D$};
    \\fill (A') circle (1pt) node[below left] {$A'$};
    \\fill (B') circle (1pt) node[below left] {$B'$};
    \\fill (C') circle (1pt) node[below right] {$C'$};
    \\fill (D') circle (1pt) node[below right] {$D'$};
    \\fill (I) circle (1pt) node[above] {$I$};
    \\fill (I') circle (1pt) node[below] {$I'$};
    \\end{tikzpicture}
    \\end{center}"""
    
    
    
    # Nội dung câu hỏi[cite: 20]
    noidungcauhoi = (
        """Cho hình lập phương $ABCD.A'B'C'D'$ có cạnh bằng $a$. %s"""
        % (tikz_figure)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: \vec{AB} + \vec{AD} + \vec{AA'} = \vec{AC'} (Đúng theo quy tắc hình hộp)[cite: 20]
    nb_da_1_d = "\\True $\\vec{AB} + \\vec{AD} + \\vec{AA'} = \\vec{AC'}$"
    nb_da_1_s = "$\\vec{AB} + \\vec{AD} + \\vec{AA'} = \\vec{CA'}$"
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Áp dụng quy tắc hình bình hành cho mặt phẳng đáy $ABCD$, ta có: \\\\ $\\vec{AB} + \\vec{AD} = \\vec{AC}$. \\\\ Mặt khác, vì các cạnh bên của hình lập phương song song và bằng nhau nên $\\vec{AA'} = \\vec{CC'}$. \\\\ Khi đó: \\\\ $\\vec{AB} + \\vec{AD} + \\vec{AA'} = \\vec{AC} + \\vec{CC'} = \\vec{AC'}$. \\\\ Đây chính là quy tắc hình hộp xuất phát từ đỉnh $A$. \\\\ Do đó khẳng định là %s."""
        % ("đúng" if "\\True" in nb_da_1 else "sai")
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: (\vec{AC}, \vec{D'A'}) = 45° (Sai, vì bằng 135°)[cite: 20]
    th_da_1_d = "\\True $(\\vec{AC}, \\vec{D'A'}) = 135^\\circ$"
    th_da_1_s = "$(\\vec{AC}, \\vec{D'A'}) = 45^\\circ$"
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Trong hình lập phương $ABCD.A'B'C'D'$, mặt đáy $A'B'C'D'$ và $ABCD$ là hai hình vuông bằng nhau nên: \\\\ $\\vec{D'A'} = \\vec{C'B'} = \\vec{CB}$. \\\\ Khi đó góc giữa hai vectơ $\\vec{AC}$ và $\\vec{D'A'}$ là: \\\\ $(\\vec{AC}, \\vec{D'A'}) = (\\vec{AC}, \\vec{CB}) = 180^\\circ - (\\vec{CA}, \\vec{CB}) = 180^\\circ - \\widehat{ACB}$. \\\\ Vì $ABCD$ là hình vuông nên đường chéo $AC$ là tia phân giác của góc vuông $\\widehat{BCD}$, suy ra $\\widehat{ACB} = 45^\\circ$. \\\\ Do đó: \\\\ $(\\vec{AC}, \\vec{D'A'}) = 180^\\circ - 45^\\circ = 135^\\circ \\neq 45^\\circ$. \\\\ Vì vậy khẳng định $(\\vec{AC}, \\vec{D'A'}) = 45^\\circ$ là sai. Mệnh đề là %s."""
        % ("đúng" if "\\True" in th_da_1 else "sai")
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: \vec{BD} \cdot \vec{A'C'} = 0 (Đúng)[cite: 20]
    vd_da_1_d = "\\True $\\vec{BD} \\cdot \\vec{A'C'} = 0$"
    vd_da_1_s = "$\\vec{BD} \\cdot \\vec{A'C'} = a^2$"
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Vì tứ giác $A'B'C'D'$ và $ABCD$ song song và bằng nhau nên $\\vec{A'C'} = \\vec{AC}$. \\\\ Khi đó tích vô hướng: \\\\ $\\vec{BD} \\cdot \\vec{A'C'} = \\vec{BD} \\cdot \\vec{AC}$. \\\\ Xét hình vuông $ABCD$, hai đường chéo vuông góc với nhau, tức là $BD \\perp AC$. \\\\ Do đó hai vectơ $\\vec{BD}$ và $\\vec{AC}$ vuông góc với nhau, suy ra tích vô hướng: \\\\ $\\vec{BD} \\cdot \\vec{AC} = 0 \\Rightarrow \\vec{BD} \\cdot \\vec{A'C'} = 0$. \\\\ Do đó khẳng định là %s."""
        % ("đúng" if "\\True" in vd_da_1 else "sai")
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: \vec{AC'} \cdot \vec{AB} = a^2 (đúng) hoặc 3/2 a^2 (sai)[cite: 20]
    vdc_da_1_d = "\\True $\\vec{AC'} \\cdot \\vec{AB} = a^2$"
    vdc_da_1_s = "$\\vec{AC'} \\cdot \\vec{AB} = \\frac{3}{2}a^2$"
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Phân tích vectơ đường chéo $\\vec{AC'}$ theo ba vectơ cạnh xuất phát từ đỉnh $A$: \\\\ $\\vec{AC'} = \\vec{AB} + \\vec{AD} + \\vec{AA'}$. \\\\ Khi đó ta có: \\\\ $\\vec{AC'} \\cdot \\vec{AB} = (\\vec{AB} + \\vec{AD} + \\vec{AA'}) \\cdot \\vec{AB} = \\vec{AB}^2 + \\vec{AD} \\cdot \\vec{AB} + \\vec{AA'} \\cdot \\vec{AB}$. \\\\ Trong hình lập phương có ba cạnh $AB, AD, AA'$ đôi một vuông góc và có độ dài bằng $a$: \\\\ $\\bullet$ $\\vec{AB}^2 = AB^2 = a^2$. \\\\ $\\bullet$ $AD \\perp AB \\Rightarrow \\vec{AD} \\cdot \\vec{AB} = 0$. \\\\ $\\bullet$ $AA' \\perp AB \\Rightarrow \\vec{AA'} \\cdot \\vec{AB} = 0$. \\\\ Suy ra: \\\\ $\\vec{AC'} \\cdot \\vec{AB} = a^2 + 0 + 0 = a^2$. \\\\ Khẳng định $\\vec{AC'} \\cdot \\vec{AB} = \\frac{3}{2}a^2$ là sai. \\\\ Do đó mệnh đề là %s."""
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
    
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


def bt_dang35_p2_b1_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Mã vẽ TikZ hình lăng trụ tam giác ABC.A'B'C' chuẩn 100% như ảnh
    # Chú ý: Tuyệt đối không dùng ký hiệu % comment bên trong string để tránh lỗi định dạng chuỗi
    tikz_figure = """\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (B) at (0,0);
    \\coordinate (A) at (1.2,-1.0);
    \\coordinate (C) at (2.4,0);
    \\coordinate (B') at (-0.2,2.8);
    \\coordinate (A') at ($(A)+(B')-(B)$);
    \\coordinate (C') at ($(C)+(B')-(B)$);
    \\draw[line width=1pt] (B)--(A)--(C);
    \\draw[line width=1pt, dashed] (B)--(C);
    \\draw[line width=1pt] (B')--(A')--(C')--cycle;
    \\draw[line width=1pt] (B)--(B') (A)--(A') (C)--(C');
    \\fill (A) circle (1pt) node[below left] {$A$};
    \\fill (B) circle (1pt) node[left] {$B$};
    \\fill (C) circle (1pt) node[below right] {$C$};
    \\fill (A') circle (1pt) node[below] {$A'$};
    \\fill (B') circle (1pt) node[above left] {$B'$};
    \\fill (C') circle (1pt) node[above right] {$C'$};
    \\end{tikzpicture}
    \\end{center}"""
    
    
    #    Do \vec{CC'} = \vec{BB'} nên VT = \vec{BB'} + 2\vec{BB'} = 3\vec{BB'} = VP => ĐÚNG[cite: 19].
    
    # Nội dung câu hỏi
    noidungcauhoi = (
        """Cho hình lăng trụ tam giác $ABC.A'B'C'$. %s"""
        % (tikz_figure)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: \vec{AA'} + \vec{BB'} = 2\vec{CC'}[cite: 19]
    nb_da_1_d = "\\True $\\vec{AA'} + \\vec{BB'} = 2\\vec{CC'}$"
    nb_da_1_s = "$\\vec{AA'} + \\vec{BB'} = \\vec{CC'}$"
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Trong hình lăng trụ tam giác $ABC.A'B'C'$, các cạnh bên đôi một song song và bằng nhau, do đó: \\\\ $\\vec{AA'} = \\vec{BB'} = \\vec{CC'}$. \\\\ Thay vào vế trái của đẳng thức, ta được: \\\\ $\\vec{AA'} + \\vec{BB'} = \\vec{CC'} + \\vec{CC'} = 2\\vec{CC'}$. \\\\ Do đó mệnh đề là %s."""
        % ("đúng" if "\\True" in nb_da_1 else "sai")
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: \vec{AB} - \vec{CC'} - \vec{A'B'} = \vec{BB'}[cite: 19]
    th_da_1_d = "\\True $\\vec{AB} - \\vec{CC'} - \\vec{A'B'} = -\\vec{BB'}$"
    th_da_1_s = "$\\vec{AB} - \\vec{CC'} - \\vec{A'B'} = \\vec{BB'}$"
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Vì hai đáy $ABC$ và $A'B'C'$ là hai tam giác bằng nhau và song song nên $\\vec{A'B'} = \\vec{AB}$. \\\\ Khi đó ta rút gọn vế trái: \\\\ $\\vec{AB} - \\vec{CC'} - \\vec{A'B'} = (\\vec{AB} - \\vec{A'B'}) - \\vec{CC'} = \\vec{0} - \\vec{CC'} = -\\vec{CC'}$. \\\\ Mặt khác ta có $\\vec{CC'} = \\vec{BB'}$, suy ra: \\\\ $\\vec{AB} - \\vec{CC'} - \\vec{A'B'} = -\\vec{BB'} \\neq \\vec{BB'}$. \\\\ Đẳng thức $\\vec{AB} - \\vec{CC'} - \\vec{A'B'} = \\vec{BB'}$ bị ngược dấu nên là sai. \\\\ Vì vậy mệnh đề là %s."""
        % ("đúng" if "\\True" in th_da_1 else "sai")
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: \vec{BB'} + 2\vec{BC} + \vec{AA'} = 2\vec{BC'}[cite: 19]
    vd_da_1_d = "\\True $\\vec{BB'} + 2\\vec{BC} + \\vec{AA'} = 2\\vec{BC'}$"
    vd_da_1_s = "$\\vec{BB'} + 2\\vec{BC} + \\vec{AA'} = \\vec{BC'}$"
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Vì $\\vec{AA'} = \\vec{BB'}$ nên ta biến đổi vế trái: \\\\ $\\vec{BB'} + 2\\vec{BC} + \\vec{AA'} = \\vec{BB'} + 2\\vec{BC} + \\vec{BB'} = 2\\vec{BC} + 2\\vec{BB'} = 2\\left(\\vec{BC} + \\vec{BB'}\\right)$. \\\\ Trong hình bình hành $BCC'B'$, theo quy tắc tam giác hoặc hình bình hành ta có: \\\\ $\\vec{BC} + \\vec{BB'} = \\vec{BC'}$. \\\\ Do đó: \\\\ $\\vec{BB'} + 2\\vec{BC} + \\vec{AA'} = 2\\vec{BC'}$. \\\\ Vì vậy khẳng định là %s."""
        % ("đúng" if "\\True" in vd_da_1 else "sai")
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: \vec{AB'} + \vec{BA} + 2\vec{CC'} = 3\vec{BB'}[cite: 19]
    vdc_da_1_d = "\\True $\\vec{AB'} + \\vec{BA} + 2\\vec{CC'} = 3\\vec{BB'}$"
    vdc_da_1_s = "$\\vec{AB'} + \\vec{BA} + 2\\vec{CC'} = 2\\vec{BB'}$"
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Áp dụng tính chất giao hoán và quy tắc cộng vectơ cho hai số hạng đầu tiên: \\\\ $\\vec{AB'} + \\vec{BA} = \\vec{BA} + \\vec{AB'} = \\vec{BB'}$. \\\\ Mặt khác, vì các cạnh bên của hình lăng trụ song song và bằng nhau nên $\\vec{CC'} = \\vec{BB'}$. \\\\ Do đó vế trái trở thành: \\\\ $\\vec{AB'} + \\vec{BA} + 2\\vec{CC'} = \\vec{BB'} + 2\\vec{BB'} = 3\\vec{BB'}$. \\\\ Khẳng định $\\vec{AB'} + \\vec{BA} + 2\\vec{CC'} = 3\\vec{BB'}$ là hoàn toàn chính xác. \\\\ Do đó mệnh đề là %s."""
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
        "\\end{ex}\n \\end{minipage}\n\n")
    return content
    
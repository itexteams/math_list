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


def bt_dang33_p2_b1_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Mã vẽ TikZ tứ diện đều ABCD có trọng tâm G của BCD và điểm I trên AG chuẩn 100% như ảnh[cite: 20]
    # Chú ý: Không dùng ký hiệu % comment bên trong string để tránh lỗi định dạng chuỗi
    tikz_figure = """\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,2.6);
    \\coordinate (B) at (-1.8,0.2);
    \\coordinate (C) at (-0.6,-1.2);
    \\coordinate (D) at (2.2,0.2);
    \\coordinate (M) at ($(B)!0.5!(C)$);
    \\coordinate (N) at ($(B)!0.5!(D)$);
    \\coordinate (G) at (intersection of D--M and C--N);
    \\coordinate (I) at ($(A)!0.75!(G)$);
    \\draw[line width=1pt] (A)--(B)--(C)--(D)--(A)--(C);
    \\draw[line width=1pt, dashed] (B)--(D) (A)--(G) (C)--(G) (D)--(G) (D)--(M);
    \\fill (A) circle (1pt) node[above] {$A$};
    \\fill (B) circle (1pt) node[left] {$B$};
    \\fill (C) circle (1pt) node[below] {$C$};
    \\fill (D) circle (1pt) node[right] {$D$};
    \\fill (G) circle (1pt) node[below right] {$G$};
    \\fill (I) circle (1pt) node[right] {$I$};
    \\fill (M) circle (1pt);
    \\fill (N) circle (1pt);
    \\end{tikzpicture}
    \\end{center}"""
    
    
    noidungcauhoi = (
        """Cho tứ diện đều $ABCD$. Gọi $G$ là trọng tâm của tam giác $BCD$. %s"""
        % (tikz_figure)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: \vec{GB} + \vec{GC} + \vec{GD} = \vec{0}[cite: 20]
    nb_da_1_d = "\\True $\\vec{GB} + \\vec{GC} + \\vec{GD} = \\vec{0}$"
    nb_da_1_s = "$\\vec{GB} + \\vec{GC} + \\vec{GD} = 3\\vec{AG}$"
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Theo tính chất cơ bản của trọng tâm tam giác, với $G$ là trọng tâm của tam giác $BCD$, ta luôn có hệ thức vectơ: \\\\ $\\vec{GB} + \\vec{GC} + \\vec{GD} = \\vec{0}$. \\\\ Do đó mệnh đề là %s."""
        % ("đúng" if "\\True" in nb_da_1 else "sai")
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: \vec{AG} = 1/3 \vec{AB} + 2/3 \vec{AC} + 2/3 \vec{AD} (Sai, vì đúng phải là 1/3 \vec{AB} + 1/3 \vec{AC} + 1/3 \vec{AD})[cite: 20]
    th_da_1_d = "\\True $\\vec{AG} = \\frac{1}{3}\\vec{AB} + \\frac{1}{3}\\vec{AC} + \\frac{1}{3}\\vec{AD}$"
    th_da_1_s = "$\\vec{AG} = \\frac{1}{3}\\vec{AB} + \\frac{2}{3}\\vec{AC} + \\frac{2}{3}\\vec{AD}$"
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Với điểm $A$ bất kỳ và $G$ là trọng tâm tam giác $BCD$, ta có: \\\\ $\\vec{AB} + \\vec{AC} + \\vec{AD} = (\\vec{AG} + \\vec{GB}) + (\\vec{AG} + \\vec{GC}) + (\\vec{AG} + \\vec{GD}) = 3\\vec{AG} + (\\vec{GB} + \\vec{GC} + \\vec{GD})$. \\\\ Vì $\\vec{GB} + \\vec{GC} + \\vec{GD} = \\vec{0}$ nên: \\\\ $\\vec{AB} + \\vec{AC} + \\vec{AD} = 3\\vec{AG} \\Leftrightarrow \\vec{AG} = \\frac{1}{3}\\vec{AB} + \\frac{1}{3}\\vec{AC} + \\frac{1}{3}\\vec{AD}$. \\\\ Do đó khẳng định $\\vec{AG} = \\frac{1}{3}\\vec{AB} + \\frac{2}{3}\\vec{AC} + \\frac{2}{3}\\vec{AD}$ là sai. \\\\ Vì vậy mệnh đề là %s."""
        % ("đúng" if "\\True" in th_da_1 else "sai")
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: \vec{CG} = 1/3 \vec{AB} - 2/3 \vec{AC} + 1/3 \vec{AD}[cite: 20]
    vd_da_1_d = "\\True $\\vec{CG} = \\frac{1}{3}\\vec{AB} - \\frac{2}{3}\\vec{AC} + \\frac{1}{3}\\vec{AD}$"
    vd_da_1_s = "$\\vec{CG} = \\frac{1}{3}\\vec{AB} + \\frac{2}{3}\\vec{AC} + \\frac{1}{3}\\vec{AD}$"
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Áp dụng quy tắc hiệu hai vectơ và kết quả phân tích vectơ $\\vec{AG}$ theo $\\vec{AB}, \\vec{AC}, \\vec{AD}$, ta có: \\\\ $\\vec{CG} = \\vec{AG} - \\vec{AC} = \\left(\\frac{1}{3}\\vec{AB} + \\frac{1}{3}\\vec{AC} + \\frac{1}{3}\\vec{AD}\\right) - \\vec{AC}$ \\\\ $= \\frac{1}{3}\\vec{AB} + \\left(\\frac{1}{3}\\vec{AC} - \\vec{AC}\\right) + \\frac{1}{3}\\vec{AD} = \\frac{1}{3}\\vec{AB} - \\frac{2}{3}\\vec{AC} + \\frac{1}{3}\\vec{AD}$. \\\\ Do đó mệnh đề là %s."""
        % ("đúng" if "\\True" in vd_da_1 else "sai")
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: Gọi I là điểm thuộc đoạn AG và thỏa mãn AI = 3IG. Khi đó \vec{IA} + \vec{IB} + \vec{IC} + \vec{ID} = \vec{0}[cite: 20]
    vdc_da_1_d = (
        "\\True Gọi $I$ là điểm thuộc đoạn $AG$ và thỏa mãn $AI = 3IG$. Khi đó $\\vec{IA} + \\vec{IB} + \\vec{IC} + \\vec{ID} = \\vec{0}$"
    )
    vdc_da_1_s = (
        "Gọi $I$ là điểm thuộc đoạn $AG$ và thỏa mãn $AI = 3IG$. Khi đó $\\vec{IA} + \\vec{IB} + \\vec{IC} + \\vec{ID} = 4\\vec{AG}$"
    )
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Vì điểm $I$ thuộc đoạn thẳng $AG$ và thỏa mãn $AI = 3IG$ nên hai vectơ $\\vec{IA}$ và $\\vec{IG}$ ngược hướng nhau và có độ dài thỏa mãn $IA = 3IG$. \\\\ Do đó ta có hệ thức vectơ: \\\\ $\\vec{IA} = -3\\vec{IG} \\Leftrightarrow \\vec{IA} + 3\\vec{IG} = \\vec{0}$. \\\\ Mặt khác, vì $G$ là trọng tâm của tam giác $BCD$, với điểm $I$ bất kỳ ta có: \\\\ $\\vec{IB} + \\vec{IC} + \\vec{ID} = 3\\vec{IG}$. \\\\ Khi đó tổng bốn vectơ là: \\\\ $\\vec{IA} + \\vec{IB} + \\vec{IC} + \\vec{ID} = \\vec{IA} + (\\vec{IB} + \\vec{IC} + \\vec{ID}) = \\vec{IA} + 3\\vec{IG} = \\vec{0}$. \\\\ (Điều này chứng tỏ điểm $I$ chính là trọng tâm của tứ diện đều $ABCD$). \\\\ Do đó mệnh đề là %s."""
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
    
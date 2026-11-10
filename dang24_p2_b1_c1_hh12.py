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


def bt_dang24_p2_b1_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Mã vẽ TikZ hình chóp S.ABCD có đáy ABCD là hình vuông, SA vuông góc (ABCD)[cite: 19]
    # I, J là trung điểm SA, SC; O là tâm đáy; đường nét liền/đứt đúng 100% như ảnh[cite: 19]
    # Chú ý: Không để dấu % làm comment bên trong string để tránh lỗi format string
    tikz_figure = """\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,0);
    \\coordinate (B) at (-1.4,-1.4);
    \\coordinate (C) at (1.8,-1.4);
    \\coordinate (D) at ($(A)+(C)-(B)$);
    \\coordinate (S) at (0,2.8);
    \\coordinate (O) at ($(A)!0.5!(C)$);
    \\coordinate (I) at ($(S)!0.5!(A)$);
    \\coordinate (J) at ($(S)!0.5!(C)$);
    \\draw[line width=1pt] (S)--(B)--(C)--(D)--(S)--(C);
    \\draw[line width=1pt, dashed] (S)--(A)--(B) (A)--(D) (A)--(C) (B)--(D) (I)--(J);
    \\fill (A) circle (1pt) node[left] {$A$};
    \\fill (B) circle (1pt) node[below left] {$B$};
    \\fill (C) circle (1pt) node[below right] {$C$};
    \\fill (D) circle (1pt) node[right] {$D$};
    \\fill (S) circle (1pt) node[above left] {$S$};
    \\fill (O) circle (1pt) node[below] {$O$};
    \\fill (I) circle (1pt) node[left] {$I$};
    \\fill (J) circle (1pt) node[right] {$J$};
    \\end{tikzpicture}
    \\end{center}"""
    
    # Nội dung câu hỏi[cite: 19]
    noidungcauhoi = (
        """Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình vuông, $SA$ vuông góc với mặt phẳng $(ABCD)$. Gọi $I, J$ lần lượt là trung điểm của $SA, SC$. $G$ là trọng tâm tam giác $SBD$. %s"""
        % (tikz_figure)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: \vec{AC} - \vec{AB} = \vec{AD} (Đúng vì \vec{AC} - \vec{AB} = \vec{BC} = \vec{AD})[cite: 19]
    nb_da_1_d = "\\True $\\vec{AC} - \\vec{AB} = \\vec{AD}$"
    nb_da_1_s = "$\\vec{AC} - \\vec{AB} = \\vec{DA}$"
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Theo quy tắc hiệu hai vectơ chung gốc, ta có: \\\\ $\\vec{AC} - \\vec{AB} = \\vec{BC}$. \\\\ Vì tứ giác $ABCD$ là hình vuông nên $\\vec{BC} = \\vec{AD}$. \\\\ Do đó $\\vec{AC} - \\vec{AB} = \\vec{AD}$. \\\\ Vậy mệnh đề là %s."""
        % ("đúng" if "\\True" in nb_da_1 else "sai")
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: \vec{AS} + \vec{AB} + \vec{AD} = \vec{AG} (Sai vì G là trọng tâm tam giác SBD nên \vec{AS} + \vec{AB} + \vec{AD} = 3\vec{AG})[cite: 19]
    th_da_1_d = "\\True $\\vec{AS} + \\vec{AB} + \\vec{AD} = 3\\vec{AG}$"
    th_da_1_s = "$\\vec{AS} + \\vec{AB} + \\vec{AD} = \\vec{AG}$"
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Vì điểm $G$ là trọng tâm của tam giác $SBD$ nên với đỉnh $A$ bất kỳ, ta luôn có hệ thức trọng tâm: \\\\ $\\vec{AS} + \\vec{AB} + \\vec{AD} = 3\\vec{AG}$. \\\\ Do thiếu hệ số $3$ nên đẳng thức $\\vec{AS} + \\vec{AB} + \\vec{AD} = \\vec{AG}$ là sai. \\\\ Do đó khẳng định là %s."""
        % ("đúng" if "\\True" in th_da_1 else "sai")
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: \vec{IJ} . \vec{BD} = 0 (Sai về mặt ký hiệu vectơ không \vec{0}, hoặc đúng/sai về tích vô hướng)[cite: 19]
    # Tích vô hướng của hai vectơ là một SỐ thực: \vec{IJ} // AC mà AC vuông góc BD nên tích vô hướng bằng số 0, không phải vectơ không \vec{0}[cite: 19]
    vd_da_1_d = "\\True $\\vec{IJ} \\cdot \\vec{BD} = 0$"
    vd_da_1_s = "$\\vec{IJ} \\cdot \\vec{BD} = \\vec{0}$"
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Xét tam giác $SAC$, $I$ là trung điểm của $SA$ và $J$ là trung điểm của $SC$, suy ra $IJ$ là đường trung bình của tam giác $SAC$. \\\\ Do đó $\\vec{IJ} = \\frac{1}{2}\\vec{AC}$, hay giá của vectơ $\\vec{IJ}$ song song với đường thẳng $AC$. \\\\ Vì tứ giác $ABCD$ là hình vuông nên hai đường chéo vuông góc với nhau, tức là $AC \\perp BD$. \\\\ Suy ra hai vectơ $\\vec{IJ}$ và $\\vec{BD}$ vuông góc với nhau: \\\\ $\\vec{IJ} \\perp \\vec{BD} \\Rightarrow \\vec{IJ} \\cdot \\vec{BD} = 0$. \\\\ Chú ý rằng tích vô hướng của hai vectơ là một số thực ($0$), không phải là một vectơ-không ($\\vec{0}$). \\\\ Do đó mệnh đề $\\vec{IJ} \\cdot \\vec{BD} = \\vec{0}$ là sai. \\\\ Vì vậy mệnh đề là %s."""
        % ("đúng" if "\\True" in vd_da_1 else "sai")
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: \vec{AG}^2 = \vec{AS}^2 + \vec{AB}^2 + \vec{AD}^2 (Sai vì 3\vec{AG} = \vec{AS} + \vec{AB} + \vec{AD})[cite: 19]
    vdc_da_1_d = "\\True $9\\vec{AG}^2 = \\vec{AS}^2 + \\vec{AB}^2 + \\vec{AD}^2$"
    vdc_da_1_s = "$\\vec{AG}^2 = \\vec{AS}^2 + \\vec{AB}^2 + \\vec{AD}^2$"
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Theo tính chất trọng tâm ở câu b, ta có: \\\\ $3\\vec{AG} = \\vec{AS} + \\vec{AB} + \\vec{AD}$. \\\\ Bình phương vô hướng hai vế, ta được: \\\\ $9\\vec{AG}^2 = (\\vec{AS} + \\vec{AB} + \\vec{AD})^2 = \\vec{AS}^2 + \\vec{AB}^2 + \\vec{AD}^2 + 2(\\vec{AS} \\cdot \\vec{AB} + \\vec{AS} \\cdot \\vec{AD} + \\vec{AB} \\cdot \\vec{AD})$. \\\\ Vì $SA \\perp (ABCD)$ nên $SA \\perp AB$ và $SA \\perp AD$, suy ra $\\vec{AS} \\cdot \\vec{AB} = 0$ và $\\vec{AS} \\cdot \\vec{AD} = 0$. \\\\ Vì đáy $ABCD$ là hình vuông nên $AB \\perp AD$, suy ra $\\vec{AB} \\cdot \\vec{AD} = 0$. \\\\ Từ đó: \\\\ $9\\vec{AG}^2 = \\vec{AS}^2 + \\vec{AB}^2 + \\vec{AD}^2 \\Leftrightarrow \\vec{AG}^2 = \\frac{1}{9}\\left(\\vec{AS}^2 + \\vec{AB}^2 + \\vec{AD}^2\\right)$. \\\\ Do đó hệ thức $\\vec{AG}^2 = \\vec{AS}^2 + \\vec{AB}^2 + \\vec{AD}^2$ là sai vì thiếu hệ số $9$. \\\\ Vì vậy mệnh đề là %s."""
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
    
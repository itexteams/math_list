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


def bt_dang34_p2_b1_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Mã vẽ TikZ hình lăng trụ ABC.A'B'C' có G là trọng tâm tam giác A'B'C' chuẩn 100% như ảnh[cite: 20]
    # Chú ý: Tuyệt đối không dùng ký hiệu % comment bên trong string để tránh lỗi format string[cite: 20]
    tikz_figure = """\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,2.6);
    \\coordinate (B) at (1.1,1.8);
    \\coordinate (C) at (2.8,2.6);
    \\coordinate (A') at (0.4,0);
    \\coordinate (B') at ($(B)+(A')-(A)$);
    \\coordinate (C') at ($(C)+(A')-(A)$);
    \\coordinate (G) at ($(A')!0.33333!(B')!0.5!(C')$);
    \\draw[line width=1pt] (A)--(B)--(C)--cycle;
    \\draw[line width=1pt] (A)--(A') (B)--(B') (C)--(C');
    \\draw[line width=1pt] (A')--(B')--(C');
    \\draw[line width=1pt, dashed] (A')--(C') (A)--(G);
    \\fill (A) circle (1pt) node[above left] {$A$};
    \\fill (B) circle (1pt) node[below left] {$B$};
    \\fill (C) circle (1pt) node[above right] {$C$};
    \\fill (A') circle (1pt) node[left] {$A'$};
    \\fill (B') circle (1pt) node[below] {$B'$};
    \\fill (C') circle (1pt) node[right] {$C'$};
    \\fill (G) circle (1pt) node[below right] {$G$};
    \\end{tikzpicture}
    \\end{center}"""
    
    
    
    # Nội dung câu hỏi[cite: 20]
    noidungcauhoi = (
        """Cho hình lăng trụ $ABC.A'B'C'$ với $G$ là trọng tâm của tam giác $A'B'C'$. Đặt $\\vec{AA'} = \\vec{a}, \\vec{AB} = \\vec{b}, \\vec{AC} = \\vec{c}$. %s"""
        % (tikz_figure)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: \vec{AG} = 1/3 (\vec{AA'} + \vec{AB'} + \vec{AC'})[cite: 20]
    nb_da_1_d = (
        "\\True $\\vec{AG} = \\frac{1}{3}\\left(\\vec{AA'} + \\vec{AB'} +"
        " \\vec{AC'}\\right)$"
    )
    nb_da_1_s = (
        "$\\vec{AG} = \\frac{1}{2}\\left(\\vec{AA'} + \\vec{AB'} +"
        " \\vec{AC'}\\right)$"
    )
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Vì $G$ là trọng tâm của tam giác $A'B'C'$ nên với điểm $A$ bất kì trong không gian, theo tính chất trọng tâm tam giác ta có hệ thức vectơ: \\\\ $\\vec{AA'} + \\vec{AB'} + \\vec{AC'} = 3\\vec{AG} \\Leftrightarrow \\vec{AG} = \\frac{1}{3}\\left(\\vec{AA'} + \\vec{AB'} + \\vec{AC'}\\right)$. \\\\ Do đó mệnh đề là %s."""
        % ("đúng" if "\\True" in nb_da_1 else "sai")
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: \vec{AG} = \vec{a} + 1/3 (\vec{b} + \vec{c}) (đúng) hoặc \vec{a} + 1/3 (\vec{b} - \vec{c}) (sai)[cite: 20]
    th_da_1_d = (
        "\\True $\\vec{AG} = \\vec{a} + \\frac{1}{3}\\left(\\vec{b} +"
        " \\vec{c}\\right)$"
    )
    th_da_1_s = (
        "$\\vec{AG} = \\vec{a} + \\frac{1}{3}\\left(\\vec{b} - \\vec{c}\\right)$"
    )
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Trong hình lăng trụ tam giác $ABC.A'B'C'$, các cạnh bên song song và bằng nhau nên ta có $\\vec{BB'} = \\vec{CC'} = \\vec{AA'} = \\vec{a}$. \\\\ Áp dụng quy tắc cộng vectơ: \\\\ $\\bullet$ $\\vec{AB'} = \\vec{AB} + \\vec{BB'} = \\vec{b} + \\vec{a}$. \\\\ $\\bullet$ $\\vec{AC'} = \\vec{AC} + \\vec{CC'} = \\vec{c} + \\vec{a}$. \\\\ Thay vào biểu thức vectơ $\\vec{AG}$ ở câu a: \\\\ $\\vec{AG} = \\frac{1}{3}\\left(\\vec{AA'} + \\vec{AB'} + \\vec{AC'}\\right) = \\frac{1}{3}\\left[\\vec{a} + (\\vec{b} + \\vec{a}) + (\\vec{c} + \\vec{a})\\right]$ \\\\ $= \\frac{1}{3}\\left(3\\vec{a} + \\vec{b} + \\vec{c}\\right) = \\vec{a} + \\frac{1}{3}\\left(\\vec{b} + \\vec{c}\\right)$. \\\\ Do đó khẳng định $\\vec{AG} = \\vec{a} + \\frac{1}{3}\\left(\\vec{b} - \\vec{c}\\right)$ là sai. \\\\ Vì vậy mệnh đề là %s."""
        % ("đúng" if "\\True" in th_da_1 else "sai")
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: Phân tích vectơ \vec{CG}[cite: 20]
    # \vec{CG} = \vec{a} + 1/3 \vec{b} - 2/3 \vec{c} (đúng) hoặc \vec{a} - 1/3 \vec{b} + 2/3 \vec{c} (sai)[cite: 20]
    vd_da_1_d = (
        "\\True $\\vec{CG} = \\vec{a} + \\frac{1}{3}\\vec{b} -"
        " \\frac{2}{3}\\vec{c}$"
    )
    vd_da_1_s = (
        "$\\vec{CG} = \\vec{a} - \\frac{1}{3}\\vec{b} + \\frac{2}{3}\\vec{c}$"
    )
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Ta biểu diễn vectơ $\\vec{CG}$ thông qua điểm gốc $A$: \\\\ $\\vec{CG} = \\vec{AG} - \\vec{AC}$. \\\\ Theo kết quả phân tích vectơ $\\vec{AG}$ ở câu b: \\\\ $\\vec{AG} = \\vec{a} + \\frac{1}{3}\\vec{b} + \\frac{1}{3}\\vec{c}$. \\\\ Khi đó ta có: \\\\ $\\vec{CG} = \\left(\\vec{a} + \\frac{1}{3}\\vec{b} + \\frac{1}{3}\\vec{c}\\right) - \\vec{c} = \\vec{a} + \\frac{1}{3}\\vec{b} + \\left(\\frac{1}{3} - 1\\right)\\vec{c} = \\vec{a} + \\frac{1}{3}\\vec{b} - \\frac{2}{3}\\vec{c}$. \\\\ Khẳng định $\\vec{CG} = \\vec{a} - \\frac{1}{3}\\vec{b} + \\frac{2}{3}\\vec{c}$ bị sai dấu ở các hệ số của $\\vec{b}$ và $\\vec{c}$. \\\\ Do đó mệnh đề là %s."""
        % ("đúng" if "\\True" in vd_da_1 else "sai")
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: Phân tích vectơ \vec{BG}[cite: 20]
    # \vec{BG} = \vec{a} - 2/3 \vec{b} + 1/3 \vec{c} (đúng) hoặc \vec{a} + 2/3 \vec{b} + 1/3 \vec{c} (sai)[cite: 20]
    vdc_da_1_d = (
        "\\True $\\vec{BG} = \\vec{a} - \\frac{2}{3}\\vec{b} +"
        " \\frac{1}{3}\\vec{c}$"
    )
    vdc_da_1_s = (
        "$\\vec{BG} = \\vec{a} + \\frac{2}{3}\\vec{b} + \\frac{1}{3}\\vec{c}$"
    )
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Ta biểu diễn vectơ $\\vec{BG}$ qua điểm gốc $A$: \\\\ $\\vec{BG} = \\vec{AG} - \\vec{AB}$. \\\\ Thay $\\vec{AG} = \\vec{a} + \\frac{1}{3}\\vec{b} + \\frac{1}{3}\\vec{c}$ và $\\vec{AB} = \\vec{b}$ vào đẳng thức, ta được: \\\\ $\\vec{BG} = \\left(\\vec{a} + \\frac{1}{3}\\vec{b} + \\frac{1}{3}\\vec{c}\\right) - \\vec{b} = \\vec{a} + \\left(\\frac{1}{3} - 1\\right)\\vec{b} + \\frac{1}{3}\\vec{c} = \\vec{a} - \\frac{2}{3}\\vec{b} + \\frac{1}{3}\\vec{c}$. \\\\ Khẳng định $\\vec{BG} = \\vec{a} + \\frac{2}{3}\\vec{b} + \\frac{1}{3}\\vec{c}$ sai ở dấu của hệ số trước $\\vec{b}$. \\\\ Do đó mệnh đề là %s."""
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
        + str(noidungcauhoi)    + "\n"
        "\\choiceTFn \n"
        "{"    + str(shuffled_answers_nb[0])    + "}\n"
        "{"    + str(shuffled_answers_th[0])    + "}\n"
        "{"    + str(shuffled_answers_vd[0])    + "}\n"
        "{"    + str(shuffled_answers_vdc[0])    + "}\n"
        "\\loigiai{ \n"
        "\\begin{enumEX}[a)]{1} \n"
        "\\item "    + str(shuffled_solutions_nb[0])    + "\n"
        "\\item "    + str(shuffled_solutions_th[0])    + "\n"
        "\\item "    + str(shuffled_solutions_vd[0])    + "\n"
        "\\item "    + str(shuffled_solutions_vdc[0])    + "\n"
        "\\end{enumEX}} \n"
        "\\end{ex}\n \\end{minipage}\n\n")
    return content
    
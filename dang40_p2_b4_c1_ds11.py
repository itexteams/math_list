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


def bt_dang40_p2_b4_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            k = random.choice([1, 2]) # 1: y=sin(x), 2: y=cos(x) (để thay đổi bài toán)
            if k == 1:
                h_so = "\\sin x"

                nb_da_1_d = '\\True Đồ thị hàm số đi qua gốc tọa độ'
                nb_da_1_s = 'Đồ thị hàm số đi qua điểm $(0; 1)$'
                loigiai_nb_1 = '''Thay $x = 0$ vào hàm số ta được $y = \\sin 0 = 0$.\\\\ Vậy đồ thị hàm số đi qua gốc tọa độ $O(0;0)$.'''

                th_da_1_d = 'Hàm số nghịch biến trên $(-\\pi;0)$'
                th_da_1_s = '\\True Hàm số đồng biến trên $\\left(-\\frac{\\pi}{2}; \\frac{\\pi}{2}\\right)$'
                loigiai_th_1 = '''Dựa vào đồ thị hàm số $y = \\sin x$, ta thấy trên khoảng $\\left(-\\frac{\\pi}{2}; \\frac{\\pi}{2}\\right)$ đồ thị đi lên (từ trái qua phải) nên hàm số đồng biến.'''

                vd_da_1_d = '\\True Giá trị nhỏ nhất của hàm số trên $\\left[-\\frac{\\pi}{2}; -\\frac{\\pi}{5}\\right]$ bằng $-1$'
                vd_da_1_s = 'Giá trị nhỏ nhất của hàm số trên $\\left[-\\frac{\\pi}{2}; -\\frac{\\pi}{5}\\right]$ bằng $0$'
                loigiai_vd_1 = '''Hàm số $y = \\sin x$ đồng biến trên đoạn $\\left[-\\frac{\\pi}{2}; \\frac{\\pi}{2}\\right]$.\\\\ Do đó trên đoạn $\\left[-\\frac{\\pi}{2}; -\\frac{\\pi}{5}\\right]$, hàm số đạt giá trị nhỏ nhất tại $x = -\\frac{\\pi}{2}$.\\\\ Khi đó $\\min y = \\sin\\left(-\\frac{\\pi}{2}\\right) = -1$.'''

                # Cho pt f(x) = a có n nghiệm
                a_val = random.choice([1, 2, 3])
                k_pi = random.choice([2, 3, 4])
                so_nghiem = k_pi * 2 if k_pi % 2 == 0 else (k_pi//2)*2 + 2 # ví dụ [0; 2pi] có 2 ng, [0; 3pi] có 4 ng nếu 0<a<1

                vdc_da_1_d = 'Phương trình $f(x) = \\frac{%s}{4}$ có $6$ nghiệm trên $[0; %s\\pi]$' % (a_val, k_pi)
                vdc_da_1_s = '\\True Phương trình $f(x) = \\frac{%s}{4}$ có $%s$ nghiệm trên $[0; %s\\pi]$' % (a_val, so_nghiem, k_pi)

                loigiai_vdc_1 = '''Đường thẳng $y = \\frac{%s}{4}$ cắt đồ thị hàm số $y = \\sin x$ trên đoạn $[0; 2\\pi]$ tại $2$ điểm phân biệt.\\\\ Dựa vào tính tuần hoàn, trên đoạn $[0; %s\\pi]$ phương trình có $%s$ nghiệm phân biệt.''' % (a_val, k_pi, so_nghiem)

                tikz_fig = '''\\begin{tikzpicture}[>=stealth,x=1cm,y=1cm,scale=1]
            \\draw[->] (-3.5,0) -- (4,0) node[below] {$x$};
            \\draw[->] (0,-1.5) -- (0,2) node[right] {$y$};
            \\node[below right] at (0,0) {$O$};
            \\draw[thick, domain=-3.14:3.14, samples=100] plot (\\x, {sin(\\x r)});
            \\draw[dashed] (-1.57,0) node[above] {$-\\frac{\\pi}{2}$} -- (-1.57,-1) -- (0,-1) node[right] {$-1$};
            \\draw[dashed] (1.57,0) node[below] {$\\frac{\\pi}{2}$} -- (1.57,1) -- (0,1) node[left] {$1$};
            \\node[above left] at (-3.14,0) {$-\\pi$};
            \\node[below left] at (3.14,0) {$\\pi$};
            \\fill (-1.57,-1) circle (1.5pt);
            \\fill (1.57,1) circle (1.5pt);
            \\end{tikzpicture}'''

            else:
                h_so = "\\cos x"

                nb_da_1_d = '\\True Đồ thị hàm số đi qua điểm $(0; 1)$'
                nb_da_1_s = 'Đồ thị hàm số đi qua gốc tọa độ'
                loigiai_nb_1 = '''Thay $x = 0$ vào hàm số ta được $y = \\cos 0 = 1$.\\\\ Vậy đồ thị hàm số đi qua điểm $(0; 1)$.'''

                th_da_1_d = 'Hàm số đồng biến trên $(0; \\pi)$'
                th_da_1_s = '\\True Hàm số nghịch biến trên $(0; \\pi)$'
                loigiai_th_1 = '''Dựa vào đồ thị hàm số $y = \\cos x$, ta thấy trên khoảng $(0; \\pi)$ đồ thị đi xuống (từ trái qua phải) nên hàm số nghịch biến.'''

                vd_da_1_d = '\\True Giá trị lớn nhất của hàm số trên $\\left[-\\frac{\\pi}{3}; \\frac{\\pi}{3}\\right]$ bằng $1$'
                vd_da_1_s = 'Giá trị lớn nhất của hàm số trên $\\left[-\\frac{\\pi}{3}; \\frac{\\pi}{3}\\right]$ bằng $\\frac{1}{2}$'
                loigiai_vd_1 = '''Hàm số $y = \\cos x$ đạt giá trị lớn nhất bằng $1$ tại $x = 0$.\\\\ Vì $0 \\in \\left[-\\frac{\\pi}{3}; \\frac{\\pi}{3}\\right]$ nên giá trị lớn nhất của hàm số trên đoạn này bằng $1$.'''

                a_val = random.choice([1, 2, 3])
                k_pi = random.choice([2, 3, 4])
                so_nghiem = k_pi # Với cos(x) = a (0<a<1), số nghiệm trên [0, k*pi] thường là k.

                vdc_da_1_d = 'Phương trình $f(x) = \\frac{%s}{4}$ có $6$ nghiệm trên $[0; %s\\pi]$' % (a_val, k_pi)
                vdc_da_1_s = '\\True Phương trình $f(x) = \\frac{%s}{4}$ có $%s$ nghiệm trên $[0; %s\\pi]$' % (a_val, so_nghiem, k_pi)

                loigiai_vdc_1 = '''Đường thẳng $y = \\frac{%s}{4}$ cắt đồ thị hàm số $y = \\cos x$ trên đoạn $[0; 2\\pi]$ tại $2$ điểm phân biệt.\\\\ Dựa vào tính tuần hoàn, trên đoạn $[0; %s\\pi]$ phương trình có $%s$ nghiệm phân biệt.''' % (a_val, k_pi, so_nghiem)

                tikz_fig = '''\\begin{tikzpicture}[>=stealth,x=1cm,y=1cm,scale=1]
            \\draw[->] (-3.5,0) -- (4,0) node[below] {$x$};
            \\draw[->] (0,-1.5) -- (0,2) node[right] {$y$};
            \\node[below right] at (0,0) {$O$};
            \\draw[thick, domain=-3.14:3.14, samples=100] plot (\\x, {cos(\\x r)});
            \\draw[dashed] (-3.14,0) node[above right] {$-\\pi$} -- (-3.14,-1) -- (0,-1) node[right] {$-1$};
            \\draw[dashed] (3.14,0) node[above left] {$\\pi$} -- (3.14,-1) -- (0,-1);
            \\node[below left] at (-1.57,0) {$-\\frac{\\pi}{2}$};
            \\node[below right] at (1.57,0) {$\\frac{\\pi}{2}$};
            \\node[above left] at (0,1) {$1$};
            \\fill (-3.14,-1) circle (1.5pt);
            \\fill (3.14,-1) circle (1.5pt);
            \\fill (0,1) circle (1.5pt);
            \\end{tikzpicture}'''

            # Nội dung câu hỏi
            noidungcauhoi = ('''Trên miền $[-\\pi; \\pi]$ đồ thị hàm số $f(x) = %s$ như hình vẽ:
            \\begin{center}
            %s
            \\end{center}''' % (h_so, tikz_fig))

            ########################################################################
            # Nhận biết ############################################
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)
            list_nb_1 = [nb_da_1]
            list_nb_2 = [loigiai_nb_1]
            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)
            list_th_1 = [th_da_1]
            list_th_2 = [loigiai_th_1]
            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng ############################################
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)
            list_vd_1 = [vd_da_1]
            list_vd_2 = [loigiai_vd_1]
            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao ############################################
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)
            list_vdc_1 = [vdc_da_1]
            list_vdc_2 = [loigiai_vdc_1]
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 đúng
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
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
            str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
               '{'+str(shuffled_answers_nb[0])+'}\n'
               '{'+str(shuffled_answers_th[0])+'}\n'
               '{'+str(shuffled_answers_vd[0])+'}\n'
               '{'+str(shuffled_answers_vdc[0])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions_nb[0])+'\n'
                '\\item '+str(shuffled_solutions_th[0])+'\n'
                '\\item '+str(shuffled_solutions_vd[0])+'\n'
                '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


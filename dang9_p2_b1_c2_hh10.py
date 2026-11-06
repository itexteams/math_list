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


def bt_dang9_p2_b1_c2_hh10(self):
            # Khai báo biến
            # Ý tưởng Random: Xoay vòng cạnh đáy được xét (AB, BC hoặc CA)
            configs = [
                {
                    'edge': 'AB', 'mid_base': "C'", 'mid_1': "A'", 'mid_2': "B'",
                    'seg_eq': "BC' = C'A = A'B'", 'val': "\\frac{AB}{2}",
                    'vec1': "\\overrightarrow{BC'}", 'vec2': "\\overrightarrow{A'B'}", 'vec3': "\\overrightarrow{C'A}",
                    'vec4_left': "\\overrightarrow{B'C'}", 'vec4_right': "\\overrightarrow{CA'}",
                    'false_dir': "ngược hướng", 'true_dir': "cùng hướng"
                },
                {
                    'edge': 'BC', 'mid_base': "A'", 'mid_1': "B'", 'mid_2': "C'",
                    'seg_eq': "CA' = A'B = B'C'", 'val': "\\frac{BC}{2}",
                    'vec1': "\\overrightarrow{CA'}", 'vec2': "\\overrightarrow{B'C'}", 'vec3': "\\overrightarrow{A'B}",
                    'vec4_left': "\\overrightarrow{C'A'}", 'vec4_right': "\\overrightarrow{AB'}",
                    'false_dir': "ngược hướng", 'true_dir': "cùng hướng"
                },
                {
                    'edge': 'CA', 'mid_base': "B'", 'mid_1': "C'", 'mid_2': "A'",
                    'seg_eq': "AB' = B'C = C'A'", 'val': "\\frac{CA}{2}",
                    'vec1': "\\overrightarrow{AB'}", 'vec2': "\\overrightarrow{C'A'}", 'vec3': "\\overrightarrow{B'C}",
                    'vec4_left': "\\overrightarrow{A'B'}", 'vec4_right': "\\overrightarrow{BC'}",
                    'false_dir': "ngược hướng", 'true_dir': "cùng hướng"
                }
            ]

            cfg = random.choice(configs)

            # Nội dung câu hỏi
            noidungcauhoi = '''Cho $\\Delta ABC$ có $A', B', C'$ lần lượt là các trung điểm của các cạnh $BC, CA, AB$. Khi đó:'''

            # Code vẽ hình TikZ (dùng raw string để không lỗi dấu ngoặc nhọn)
            hinh_ve = r'''\begin{center}
            \begin{tikzpicture}[scale=0.9, font=\footnotesize, line join=round, line cap=round, >=stealth]
            \coordinate (A) at (1.5, 2.5);
            \coordinate (B) at (0, 0);
            \coordinate (C) at (4, 0);
            \coordinate (A') at ($(B)!0.5!(C)$);
            \coordinate (B') at ($(A)!0.5!(C)$);
            \coordinate (C') at ($(A)!0.5!(B)$);
            \draw (A)--(B)--(C)--cycle;
            \draw (A')--(B')--(C')--cycle;
            \node[above] at (A) {$A$};
            \node[left] at (B) {$B$};
            \node[right] at (C) {$C$};
            \node[below] at (A') {$A'$};
            \node[above right] at (B') {$B'$};
            \node[above left] at (C') {$C'$};
            \end{tikzpicture}
            \end{center}'''

            ######################################################################## Nhận biết ############################################

            # Các đáp án
            nb_da_1_d = f'\\True ${cfg["seg_eq"]} = {cfg["val"]}$'
            nb_da_1_s = f'${cfg["seg_eq"]} = {cfg["edge"]}$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = f'''Ta có ${cfg["mid_base"]}$ là trung điểm của ${cfg["edge"]}$ và ${cfg["mid_1"]}{cfg["mid_2"]}$ là đường trung bình của tam giác ứng với cạnh đáy ${cfg["edge"]}$ nên: ${cfg["seg_eq"]} = {cfg["val"]}$.'''
            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = f'\\True Hai vecto ${cfg["vec1"]}, {cfg["vec2"]}$ {cfg["true_dir"]}'
            th_da_1_s = f'Hai vecto ${cfg["vec1"]}, {cfg["vec2"]}$ {cfg["false_dir"]}'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = f'''Mặt khác, ba vecto ${cfg["vec1"]}, {cfg["vec3"]}, {cfg["vec2"]}$ cùng hướng.'''
            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = f'\\True ${cfg["vec1"]} = {cfg["vec3"]} = {cfg["vec2"]}$'
            vd_da_1_s = f'${cfg["vec1"]} = {cfg["vec3"]} = -{cfg["vec2"]}$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = f'''Do đó ${cfg["vec1"]} = {cfg["vec3"]} = {cfg["vec2"]}$.'''
            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = f'\\True ${cfg["vec4_left"]} = {cfg["vec4_right"]}$'
            vdc_da_1_s = f'${cfg["vec4_left"]} = -{cfg["vec4_right"]}$'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = f'''Ta xác định được hai vecto ${cfg["vec4_left"]}$ và ${cfg["vec4_right"]}$ cùng hướng và có độ dài bằng nhau nên ${cfg["vec4_left"]} = {cfg["vec4_right"]}$.'''
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
                str(noidungcauhoi)+ '\n' +
                '\\choiceTFn \n'
                '{'+str(shuffled_answers_nb[0])+'}\n'
                '{'+str(shuffled_answers_th[0])+'}\n'
                '{'+str(shuffled_answers_vd[0])+'}\n'
                '{'+str(shuffled_answers_vdc[0])+'}\n'
                '\\loigiai{ \n'
                + str(hinh_ve) + '\n' +
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions_nb[0])+'\n'
                '\\item '+str(shuffled_solutions_th[0])+'\n'
                '\\item '+str(shuffled_solutions_vd[0])+'\n'
                '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n\\end{minipage}\n\n')
            return content 


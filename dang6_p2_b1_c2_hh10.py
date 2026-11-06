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


def bt_dang6_p2_b1_c2_hh10(self):
            # Khai báo biến
            # Ý tưởng Random: Quay vòng các đỉnh của lục giác đều để tạo 3 bộ cấu hình tương đương
            hex_configs = [
                {
                    'v_oa': 'OA', 'v_od': 'OD', 'v_not_col': 'AB',
                    'list9': '\\overrightarrow{AO},\\overrightarrow{OD},\\overrightarrow{DO},\\overrightarrow{AD},\\overrightarrow{DA},\\overrightarrow{BC},\\overrightarrow{CB},\\overrightarrow{EF},\\overrightarrow{FE}',
                    'v_ab': 'AB', 'v_oc': 'OC',
                    'list4': '\\overrightarrow{FO},\\overrightarrow{OC},\\overrightarrow{FC},\\overrightarrow{ED}'
                },
                {
                    'v_oa': 'OB', 'v_od': 'OE', 'v_not_col': 'BC',
                    'list9': '\\overrightarrow{BO},\\overrightarrow{OE},\\overrightarrow{EO},\\overrightarrow{BE},\\overrightarrow{EB},\\overrightarrow{CD},\\overrightarrow{DC},\\overrightarrow{FA},\\overrightarrow{AF}',
                    'v_ab': 'BC', 'v_oc': 'OD',
                    'list4': '\\overrightarrow{AO},\\overrightarrow{OD},\\overrightarrow{AD},\\overrightarrow{FE}'
                },
                {
                    'v_oa': 'OC', 'v_od': 'OF', 'v_not_col': 'CD',
                    'list9': '\\overrightarrow{CO},\\overrightarrow{OF},\\overrightarrow{FO},\\overrightarrow{CF},\\overrightarrow{FC},\\overrightarrow{DE},\\overrightarrow{ED},\\overrightarrow{AB},\\overrightarrow{BA}',
                    'v_ab': 'CD', 'v_oc': 'OE',
                    'list4': '\\overrightarrow{BO},\\overrightarrow{OE},\\overrightarrow{BE},\\overrightarrow{AF}'
                }
            ]

            cfg = random.choice(hex_configs)

            # Nội dung câu hỏi
            noidungcauhoi = '''Cho lục giác đều $ABCDEF$ có tâm $O$. Khi đó:'''

            # Code vẽ hình TikZ
            hinh_ve = r'''\begin{center}
            \begin{tikzpicture}[scale=1, font=\footnotesize, line join=round, line cap=round, >=stealth]
            \def\R{1.5}
            \coordinate (O) at (0,0);
            \coordinate (C) at (0:\R);
            \coordinate (B) at (60:\R);
            \coordinate (A) at (120:\R);
            \coordinate (F) at (180:\R);
            \coordinate (E) at (240:\R);
            \coordinate (D) at (300:\R);
            \draw[thick, blue!80!black] (A)--(B)--(C)--(D)--(E)--(F)--cycle;
            \draw[thick, blue!80!black] (A)--(D) (B)--(E) (C)--(F);
            \fill[red] (O) circle (1.5pt) node[above right, black] {$O$};
            \fill[red] (A) circle (1.5pt) node[above left, black] {$A$};
            \fill[red] (B) circle (1.5pt) node[above right, black] {$B$};
            \fill[red] (C) circle (1.5pt) node[right, black] {$C$};
            \fill[red] (D) circle (1.5pt) node[below right, black] {$D$};
            \fill[red] (E) circle (1.5pt) node[below left, black] {$E$};
            \fill[red] (F) circle (1.5pt) node[left, black] {$F$};
            \end{tikzpicture}
            \end{center}'''

            ######################################################################## Nhận biết ############################################

            # Các đáp án
            nb_da_1_d = f'\\True Vecto $\\overrightarrow{{{cfg["v_oa"]}}}$ cùng phương với $\\overrightarrow{{{cfg["v_od"]}}}$'
            nb_da_1_s = f'Vecto $\\overrightarrow{{{cfg["v_oa"]}}}$ cùng phương với $\\overrightarrow{{{cfg["v_not_col"]}}}$'
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = f'''Vecto $\\overrightarrow{{{cfg["v_oa"]}}}$ cùng phương với $\\overrightarrow{{{cfg["v_od"]}}}$'''
            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = f'\\True Có 9 vecto khác vecto không và cùng phương với vecto $\\overrightarrow{{{cfg["v_oa"]}}}$'
            th_da_1_s = f'Có 8 vecto khác vecto không và cùng phương với vecto $\\overrightarrow{{{cfg["v_oa"]}}}$'
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = f'''Có 9 vecto khác vecto không và cùng phương với vecto $\\overrightarrow{{{cfg["v_oa"]}}}$:\\\\
            ${cfg["list9"]}$.'''
            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = f'\\True Vecto $\\overrightarrow{{{cfg["v_ab"]}}}$ cùng hướng $\\overrightarrow{{{cfg["v_oc"]}}}$'
            vd_da_1_s = f'Vecto $\\overrightarrow{{{cfg["v_ab"]}}}$ ngược hướng $\\overrightarrow{{{cfg["v_oc"]}}}$'
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = f'''Vecto $\\overrightarrow{{{cfg["v_ab"]}}}$ cùng hướng $\\overrightarrow{{{cfg["v_oc"]}}}$'''
            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = f'\\True Có 4 vecto khác vecto không và cùng hướng với vecto $\\overrightarrow{{{cfg["v_ab"]}}}$'
            vdc_da_1_s = f'Có 3 vecto khác vecto không và cùng hướng với vecto $\\overrightarrow{{{cfg["v_ab"]}}}$'
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = f'''Có 4 vecto khác vecto không và cùng hướng với vecto $\\overrightarrow{{{cfg["v_ab"]}}}$ là: ${cfg["list4"]}$.'''
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


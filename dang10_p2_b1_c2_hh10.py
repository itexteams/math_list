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


def bt_dang10_p2_b1_c2_hh10(self):
            # Khai báo biến
            # Ý tưởng Random: Chọn ngẫu nhiên đỉnh A, B hoặc C để lấy điểm đối xứng qua O
            configs = [
                { 
                    'V': 'B', 'Vp': "B'", 'V2': 'A', 'V3': 'C',
                    'Vp_V3': "B'C", 'V_V3': 'BC', 'V2_H': 'AH',
                    'Vp_V2': "AB'", 'V_V2': 'AB', 'V3_H': 'CH',
                    'para': "AB'CH",
                    'vec_V2H': '\\overrightarrow{AH}', 'vec_VpV3': "\\overrightarrow{B'C}",
                    'vec_V2Vp': "\\overrightarrow{AB'}", 'vec_HV3': '\\overrightarrow{HC}'
                },
                { 
                    'V': 'A', 'Vp': "A'", 'V2': 'B', 'V3': 'C',
                    'Vp_V3': "A'C", 'V_V3': 'AC', 'V2_H': 'BH',
                    'Vp_V2': "BA'", 'V_V2': 'AB', 'V3_H': 'CH', 
                    'para': "BA'CH",
                    'vec_V2H': '\\overrightarrow{BH}', 'vec_VpV3': "\\overrightarrow{A'C}",
                    'vec_V2Vp': "\\overrightarrow{BA'}", 'vec_HV3': '\\overrightarrow{HC}'
                },
                { 
                    'V': 'C', 'Vp': "C'", 'V2': 'A', 'V3': 'B',
                    'Vp_V3': "C'B", 'V_V3': 'BC', 'V2_H': 'AH',
                    'Vp_V2': "AC'", 'V_V2': 'AC', 'V3_H': 'BH',
                    'para': "AC'BH",
                    'vec_V2H': '\\overrightarrow{AH}', 'vec_VpV3': "\\overrightarrow{C'B}",
                    'vec_V2Vp': "\\overrightarrow{AC'}", 'vec_HV3': '\\overrightarrow{HB}'
                }
            ]

            cfg = random.choice(configs)

            # Nội dung câu hỏi
            noidungcauhoi = f'''Cho $\\Delta ABC$ có trực tâm $H$ và $O$ là tâm đường tròn ngoại tiếp tam giác. Gọi ${cfg["Vp"]}$ là điểm đối xứng của ${cfg["V"]}$ qua $O$. Khi đó:'''

            # Code vẽ hình TikZ tự động thích ứng với đỉnh được chọn
            hinh_ve = f'''\\begin{{center}}
            \\begin{{tikzpicture}}[scale=0.9, font=\\footnotesize, line join=round, line cap=round, >=stealth]
            \\coordinate (O) at (0,0);
            \\coordinate ({cfg["V"]}) at (-15:2.5);
            \\coordinate ({cfg["V3"]}) at (90:2.5);
            \\coordinate ({cfg["V2"]}) at (210:2.5);
            \\coordinate ({cfg["Vp"]}) at (165:2.5);
            \\coordinate (H) at ($({cfg["V2"]})+({cfg["V"]})+({cfg["V3"]})$);
            \\coordinate (footV2) at ($({cfg["V"]})!({cfg["V2"]})!({cfg["V3"]})$);
            \\coordinate (footV3) at ($({cfg["V2"]})!({cfg["V3"]})!({cfg["V"]})$);
            \\draw (O) circle (2.5);
            \\draw ({cfg["V2"]})--({cfg["V"]})--({cfg["V3"]})--cycle;
            \\draw ({cfg["V2"]})--({cfg["Vp"]})--({cfg["V3"]});
            \\draw ({cfg["V"]})--({cfg["Vp"]});
            \\draw ({cfg["V2"]})--(footV2);
            \\draw ({cfg["V3"]})--(footV3);
            \\tkzMarkRightAngle[size=0.25]({cfg["V2"]},footV2,{cfg["V3"]})
            \\tkzMarkRightAngle[size=0.25]({cfg["V3"]},footV3,{cfg["V"]})
            \\tkzMarkRightAngle[size=0.25]({cfg["V"]},{cfg["V3"]},{cfg["Vp"]})
            \\tkzMarkRightAngle[size=0.25]({cfg["Vp"]},{cfg["V2"]},{cfg["V"]})
            \\fill (O) circle (1.5pt) node[below] {{$O$}};
            \\fill (H) circle (1.5pt) node[left] {{$H$}};
            \\fill ({cfg["V2"]}) circle (1.5pt) node[below left] {{${cfg["V2"]}$}};
            \\fill ({cfg["V"]}) circle (1.5pt) node[right] {{${cfg["V"]}$}};
            \\fill ({cfg["V3"]}) circle (1.5pt) node[above] {{${cfg["V3"]}$}};
            \\fill ({cfg["Vp"]}) circle (1.5pt) node[left] {{${cfg["Vp"]}$}};
            \\end{{tikzpicture}}
            \\end{{center}}'''

            ######################################################################## Nhận biết ############################################

            # Các đáp án
            nb_da_1_d = f'\\True ${cfg["Vp_V3"]} \\perp {cfg["V_V3"]}$'
            nb_da_1_s = f'${cfg["Vp_V3"]} \\parallel {cfg["V_V3"]}$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = f'''Ta có ${cfg["V"]}{cfg["Vp"]}$ là đường kính đường tròn ngoại tiếp tam giác $ABC$ nên $\\widehat{{{cfg["V"]}{cfg["V3"]}{cfg["Vp"]}}} = 90^\\circ \\Rightarrow {cfg["Vp_V3"]} \\perp {cfg["V_V3"]}$.'''
            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = f'\\True ${cfg["Vp_V3"]} \\parallel {cfg["V2_H"]}$'
            th_da_1_s = f'${cfg["Vp_V3"]} \\parallel {cfg["V_V2"]}$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = f'''Mặt khác ${cfg["V2_H"]} \\perp {cfg["V_V3"]}$, suy ra ${cfg["Vp_V3"]} \\parallel {cfg["V2_H"]}$ (1).'''
            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = f'\\True Tứ giác ${cfg["para"]}$ là hình bình hành'
            vd_da_1_s = f'Tứ giác ${cfg["para"]}$ là hình chữ nhật'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = f'''Tương tự: $\\widehat{{{cfg["V"]}{cfg["V2"]}{cfg["Vp"]}}} = 90^\\circ$ hay ${cfg["Vp_V2"]} \\perp {cfg["V_V2"]}$ mà ${cfg["V3_H"]} \\perp {cfg["V_V2"]}$ nên ${cfg["V3_H"]} \\parallel {cfg["Vp_V2"]}$ (2).\\!\\! Từ (1) và (2) suy ra tứ giác ${cfg["para"]}$ là hình bình hành.'''
            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = f'\\True ${cfg["vec_V2H"]} = {cfg["vec_VpV3"]}; {cfg["vec_V2Vp"]} = {cfg["vec_HV3"]}$'
            vdc_da_1_s = f'${cfg["vec_V2H"]} = {cfg["vec_VpV3"]}; {cfg["vec_V2Vp"]} = \\overrightarrow{{{cfg["V3"]}H}}$'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = f'''Vì vậy: ${cfg["vec_V2H"]} = {cfg["vec_VpV3"]}; {cfg["vec_V2Vp"]} = {cfg["vec_HV3"]}$.'''
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


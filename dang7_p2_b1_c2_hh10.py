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


def bt_dang7_p2_b1_c2_hh10(self):
            # Khai báo biến
            # Ý tưởng Random: Xoay đỉnh focal (V) của tam giác đều
            configs = [
                {
                    'V': 'A', 'Vleft': 'C', 'Vright': 'B', 
                    'opp_edge': 'BC', 'left_edge': 'AC'
                },
                {
                    'V': 'B', 'Vleft': 'A', 'Vright': 'C', 
                    'opp_edge': 'AC', 'left_edge': 'AB'
                },
                {
                    'V': 'C', 'Vleft': 'B', 'Vright': 'A', 
                    'opp_edge': 'AB', 'left_edge': 'BC'
                }
            ]

            cfg = random.choice(configs)
            V = cfg['V']
            Vl = cfg['Vleft']
            Vr = cfg['Vright']
            opp = cfg['opp_edge']
            left = cfg['left_edge']

            # Nội dung câu hỏi
            noidungcauhoi = f'''Cho $\\Delta ABC$ đều cạnh $a$, trực tâm $H$. Khi đó:'''

            # Code vẽ hình TikZ
            hinh_ve = f'''\\begin{{center}}
            \\begin{{tikzpicture}}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
            \\coordinate (O) at (0,0);
            \\coordinate ({V}) at (90:2);
            \\coordinate ({Vl}) at (210:2);
            \\coordinate ({Vr}) at (330:2);
            \\coordinate (M) at ($({Vl})!0.5!({Vr})$);
            \\coordinate (N) at ($({Vl})!0.5!({V})$); 
            \\coordinate (H) at (0,0);
            \\draw (O) circle (2);
            \\draw ({V})--({Vl})--({Vr})--cycle;
            \\draw ({V})--(M);
            \\draw ({Vr})--(N);
            \\fill ({V}) circle (1.5pt) node[above] {{${V}$}};
            \\fill ({Vl}) circle (1.5pt) node[below left] {{${Vl}$}};
            \\fill ({Vr}) circle (1.5pt) node[below right] {{${Vr}$}};
            \\fill (M) circle (1.5pt) node[below] {{$M$}};
            \\fill (N) circle (1.5pt) node[above left] {{$N$}};
            \\fill (H) circle (1.5pt) node[below left] {{$H$}};
            \\end{{tikzpicture}}
            \\end{{center}}'''

            ######################################################################## Nhận biết ############################################

            # Các đáp án
            nb_da_1_d = f'\\True ${V}H \\perp {opp}$'
            nb_da_1_s = f'${V}H \\parallel {opp}$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = f'''$\\Delta ABC$ đều có trực tâm $H$ nên ${V}H \\perp {opp}$'''
            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = f'\\True ${V}M = \\frac{{a\\sqrt{{3}}}}{{2}}$'
            th_da_1_s = f'${V}M = \\frac{{a\\sqrt{{3}}}}{{3}}$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = f'''Gọi $M, N$ lần lượt là trung điểm cạnh ${opp}, {left}$.\\\\
            Do tam giác $ABC$ đều nên ${V}M, {Vr}N$ cũng là các đường cao của tam giác $ABC$;\\\\
            Vì vậy $H$ vừa là trực tâm vừa là trọng tâm tam giác này.\\\\
            Áp dụng định lí Py-tha-go cho $\\Delta {V}{Vr}M$, ta có: ${V}M^2 = {V}{Vr}^2 - {Vr}M^2 = a^2 - \\left(\\frac{{a}}{{2}}\\right)^2 = \\frac{{3a^2}}{{4}}$\\\\
            $\\Rightarrow {V}M = \\frac{{a\\sqrt{{3}}}}{{2}}$.'''
            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = f'\\True ${V}H = \\frac{{a\\sqrt{{3}}}}{{3}}$'
            vd_da_1_s = f'${V}H = \\frac{{a\\sqrt{{3}}}}{{4}}$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = f'''Theo tính chất trọng tâm, ta có: ${V}H = \\frac{{2}}{{3}}{V}M = \\frac{{2}}{{3}} \\cdot \\frac{{a\\sqrt{{3}}}}{{2}} = \\frac{{a\\sqrt{{3}}}}{{3}}$.'''
            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = f'\\True $\\left|\\overrightarrow{{HA}}\\right| = \\left|\\overrightarrow{{HB}}\\right| = \\left|\\overrightarrow{{HC}}\\right| = \\frac{{a\\sqrt{{3}}}}{{3}}$'
            vdc_da_1_s = f'$\\left|\\overrightarrow{{HA}}\\right| = \\left|\\overrightarrow{{HB}}\\right| = \\left|\\overrightarrow{{HC}}\\right| = \\frac{{a\\sqrt{{3}}}}{{4}}$'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = f'''Dễ thấy ba vecto $\\overrightarrow{{HA}}, \\overrightarrow{{HB}}, \\overrightarrow{{HC}}$ có độ dài bằng nhau: $\\left|\\overrightarrow{{HA}}\\right| = \\left|\\overrightarrow{{HB}}\\right| = \\left|\\overrightarrow{{HC}}\\right| = {V}H = \\frac{{a\\sqrt{{3}}}}{{3}}$.'''
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


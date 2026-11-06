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


def bt_dang37_p2_b4_c1_ds11(self):
            # Khai báo biến
            kieu_de = random.choice([1, 2])

            if kieu_de == 1:
                # f(x) = cos x + cos 2x + cos 3x
                # g(x) = cos 2x * (2 cos x + 1)
                str_f = "\\cos x + \\cos 2x + \\cos 3x"
                str_g = "\\cos 2x (2 \\cos x + 1)"
                loigiai_chan_le = '''Cả hai hàm số $f(x)$ và $g(x)$ đều có tập xác định là $\\mathscr{D} = \\mathbb{R}$.\\\\ Với mọi $x \\in \\mathbb{R}$ thì $-x \\in \\mathbb{R}$ và $f(-x) = \\cos(-x) + \\cos(-2x) + \\cos(-3x) = \\cos x + \\cos 2x + \\cos 3x = f(x)$.\\\\ Vậy các hàm số đã cho là các hàm số chẵn.'''
                loigiai_chu_ky = '''Hàm số $y = \\cos x$ và $y = \\cos 3x$ tuần hoàn với chu kỳ lần lượt là $2\\pi$ và $\\frac{2\\pi}{3}$.\\\\ Hàm số $y = \\cos 2x$ tuần hoàn với chu kỳ là $\\pi$.\\\\ Do đó chu kỳ tuần hoàn của hàm số đã cho là $T = 2\\pi$. Vì $2\\pi \\approx 6,28 > 5$ nên khẳng định đúng.'''
                loigiai_dong_nhat = '''Ta có $f(x) = (\\cos 3x + \\cos x) + \\cos 2x = 2 \\cos 2x \\cos x + \\cos 2x = \\cos 2x (2 \\cos x + 1) = g(x)$.\\\\ Vậy $f(x) \\equiv g(x)$.'''
                loigiai_nghiem = '''Phương trình $f(x) = 0 \\Leftrightarrow \\cos 2x (2 \\cos x + 1) = 0 \\Leftrightarrow \\left[\\begin{aligned} & \\cos 2x = 0 \\\\ & \\cos x = -\\frac{1}{2} \\end{aligned}\\right.$.\\\\ $\\bullet$ $\\cos 2x = 0 \\Leftrightarrow 2x = \\frac{\\pi}{2} + k\\pi \\Leftrightarrow x = \\frac{\\pi}{4} + \\frac{k\\pi}{2}$, họ nghiệm này có $4$ điểm biểu diễn trên đường tròn lượng giác.\\\\ $\\bullet$ $\\cos x = -\\frac{1}{2} \\Leftrightarrow x = \\pm \\frac{2\\pi}{3} + k2\\pi$, họ nghiệm này có $2$ điểm biểu diễn trên đường tròn lượng giác.\\\\ Các điểm biểu diễn này không trùng nhau. Vậy phương trình có tất cả $4 + 2 = 6$ điểm biểu diễn.'''
                val_ck_ss = 5
                ans_ck_true = "T"
                so_diem_bieu_dien = 6
            else:
                # f(x) = sin x + sin 2x + sin 3x
                # g(x) = sin 2x * (2 cos x + 1)
                str_f = "\\sin x + \\sin 2x + \\sin 3x"
                str_g = "\\sin 2x (2 \\cos x + 1)"
                loigiai_chan_le = '''Cả hai hàm số $f(x)$ và $g(x)$ đều có tập xác định là $\\mathscr{D} = \\mathbb{R}$.\\\\ Với mọi $x \\in \\mathbb{R}$ thì $-x \\in \\mathbb{R}$ và $f(-x) = \\sin(-x) + \\sin(-2x) + \\sin(-3x) = -\\sin x - \\sin 2x - \\sin 3x = -f(x)$.\\\\ Vậy các hàm số đã cho là các hàm số lẻ, không phải hàm số chẵn.'''
                loigiai_chu_ky = '''Hàm số $y = \\sin x$ và $y = \\sin 3x$ tuần hoàn với chu kỳ lần lượt là $2\\pi$ và $\\frac{2\\pi}{3}$.\\\\ Hàm số $y = \\sin 2x$ tuần hoàn với chu kỳ là $\\pi$.\\\\ Do đó chu kỳ tuần hoàn của hàm số đã cho là $T = 2\\pi$. Vì $2\\pi \\approx 6,28 > 5$ nên khẳng định đúng.'''
                loigiai_dong_nhat = '''Ta có $f(x) = (\\sin 3x + \\sin x) + \\sin 2x = 2 \\sin 2x \\cos x + \\sin 2x = \\sin 2x (2 \\cos x + 1) = g(x)$.\\\\ Vậy $f(x) \\equiv g(x)$.'''
                loigiai_nghiem = '''Phương trình $f(x) = 0 \\Leftrightarrow \\sin 2x (2 \\cos x + 1) = 0 \\Leftrightarrow \\left[\\begin{aligned} & \\sin 2x = 0 \\\\ & \\cos x = -\\frac{1}{2} \\end{aligned}\\right.$.\\\\ $\\bullet$ $\\sin 2x = 0 \\Leftrightarrow 2x = k\\pi \\Leftrightarrow x = \\frac{k\\pi}{2}$, họ nghiệm này có $4$ điểm biểu diễn trên đường tròn lượng giác (các điểm cực của trục hoành và trục tung).\\\\ $\\bullet$ $\\cos x = -\\frac{1}{2} \\Leftrightarrow x = \\pm \\frac{2\\pi}{3} + k2\\pi$, họ nghiệm này có $2$ điểm biểu diễn trên đường tròn lượng giác.\\\\ Các điểm biểu diễn này không trùng nhau. Vậy phương trình có tất cả $4 + 2 = 6$ điểm biểu diễn.'''
                val_ck_ss = 5
                ans_ck_true = "T"
                so_diem_bieu_dien = 6

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hai hàm số $f(x) = %s$ và $g(x) = %s$. Xét tính đúng, sai của các khẳng định sau:'''
                             % (str_f, str_g))

            ########################################################################
            # Nhận biết
            if kieu_de == 1:
                nb_da_1_d = '\\True Các hàm số đã cho là hàm số chẵn'
                nb_da_1_s = 'Các hàm số đã cho là hàm số lẻ'
            else:
                nb_da_1_d = 'Các hàm số đã cho là hàm số chẵn'
                nb_da_1_s = '\\True Các hàm số đã cho là hàm số lẻ'

            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)
            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = loigiai_chan_le
            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu
            th_da_1_d = '\\True Các hàm số đã cho có chu kỳ tuần hoàn $T > %s$' % val_ck_ss
            th_da_1_s = 'Các hàm số đã cho có chu kỳ tuần hoàn $T < 3$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)
            list_th_1 = [th_da_1]

            loigiai_th_1 = loigiai_chu_ky
            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng
            vd_da_1_d = '\\True $f(x) \\equiv g(x)$'
            vd_da_1_s = '$f(x) \\neq g(x)$ với mọi $x \\in \\mathbb{R}$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)
            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = loigiai_dong_nhat
            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao
            vdc_da_1_d = '\\True Phương trình $f(x) = 0$ có đúng %s điểm biểu diễn nghiệm trên vòng tròn lượng giác' % so_diem_bieu_dien
            vdc_da_1_s = 'Phương trình $f(x) = 0$ có đúng %s điểm biểu diễn nghiệm trên vòng tròn lượng giác' % (so_diem_bieu_dien - 2)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)
            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = loigiai_nghiem
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
                '\\choiceTFn \n'
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


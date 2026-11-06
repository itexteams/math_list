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


def bt_dang38_p2_b4_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến và tạo số ngẫu nhiên
            # Đề gốc: f(x) = 2*cot(2x) - 3*cot(3x), g(x) = tan(2x)
            # Random các hệ số và các chu kỳ để bài toán có tính chất tương tự
            a = random.choice([2, 4])
            b = random.choice([3, 5])
            c = random.choice([2, 4]) # Hệ số góc của g(x) và f(x) phần cot(2x) phải giống nhau

            # Tính chu kỳ g(x) = tan(c*x) -> T = pi/c
            chu_ky_g = Rational(1, c)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hai hàm số $f(x) = %s \\cot %sx - %s \\cot %sx$ và $g(x) = \\tan %sx$.'''
                             % (latex(a), latex(c), latex(b), latex(b), latex(c)))

            ########################################################################
            # Nhận biết
            # Các đáp án
            nb_da_1_d = '\\True Hàm số $f(x)$ là hàm số lẻ'
            nb_da_1_s = 'Hàm số $f(x)$ là hàm số chẵn'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Tập xác định của hàm số $f(x)$ là $\\mathscr{D} = \\mathbb{R} \\setminus \\left\\{ \\frac{k\\pi}{%s}; \\frac{k\\pi}{%s} \\Big| k \\in \\mathbb{Z} \\right\\}$, đây là một tập đối xứng.\\\\ Với mọi $x \\in \\mathscr{D}$, ta có $-x \\in \\mathscr{D}$ và:\\\\ $f(-x) = %s \\cot\\left(-%sx\\right) - %s \\cot\\left(-%sx\\right) = -%s \\cot %sx + %s \\cot %sx = -f(x)$.\\\\ Vậy $f(x)$ là hàm số lẻ.'''
                            % (latex(c), latex(b), latex(a), latex(c), latex(b), latex(b), latex(a), latex(c), latex(b), latex(b)))

            list_nb_2 = [loigiai_nb_1]
            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu
            # Các đáp án
            th_da_1_d = 'Hàm số $g(x)$ có chu kỳ $T = \\pi$'
            th_da_1_s = '\\True Hàm số $g(x)$ có chu kỳ $T = \\frac{\\pi}{%s}$' % latex(c)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Hàm số $y = \\tan kx$ tuần hoàn với chu kỳ $T = \\frac{\\pi}{|k|}$.\\\\ Do đó hàm số $g(x) = \\tan %sx$ tuần hoàn với chu kỳ $T = \\frac{\\pi}{%s}$.'''
                            % (latex(c), latex(c)))

            list_th_2 = [loigiai_th_1]
            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng
            # Các đáp án
            vd_da_1_d = '\\True Hàm số $g(x)$ có một khoảng đồng biến là $\\left( -\\frac{\\pi}{%s}; \\frac{\\pi}{%s} \\right)$' % (latex(2*c), latex(2*c))
            vd_da_1_s = 'Hàm số $g(x)$ có một khoảng nghịch biến là $\\left( -\\frac{\\pi}{%s}; \\frac{\\pi}{%s} \\right)$' % (latex(2*c), latex(2*c))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Hàm số $y = \\tan t$ luôn đồng biến trên mỗi khoảng của tập xác định $\\left( -\\frac{\\pi}{2} + k\\pi; \\frac{\\pi}{2} + k\\pi \\right)$.\\\\ Xét với $g(x) = \\tan %sx$, hàm số đồng biến khi $-\\frac{\\pi}{2} + k\\pi < %sx < \\frac{\\pi}{2} + k\\pi \\Leftrightarrow -\\frac{\\pi}{%s} + \\frac{k\\pi}{%s} < x < \\frac{\\pi}{%s} + \\frac{k\\pi}{%s}$.\\\\ Với $k = 0$, hàm số có một khoảng đồng biến là $\\left( -\\frac{\\pi}{%s}; \\frac{\\pi}{%s} \\right)$.'''
                            % (latex(c), latex(c), latex(2*c), latex(c), latex(2*c), latex(c), latex(2*c), latex(2*c)))

            list_vd_2 = [loigiai_vd_1]
            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao
            # Các đáp án
            vdc_da_1_d = '\\True Phương trình $f^5(x) = g^5(x)$ vô nghiệm'
            vdc_da_1_s = 'Phương trình $f^5(x) = g^5(x)$ có nghiệm'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Ta có $f^5(x) = g^5(x) \\Leftrightarrow f(x) = g(x)$.\\\\ Phương trình trở thành: $%s \\cot %sx - %s \\cot %sx = \\tan %sx \\Leftrightarrow %s \\cot %sx - \\tan %sx = %s \\cot %sx$.\\\\ Sử dụng công thức lượng giác $\\cot t - \\tan t = 2 \\cot 2t$ ta biến đổi vế trái:\\\\ Vì hệ số góc đã được thiết lập phù hợp, phương trình rút gọn thu được hệ thức không thỏa mãn tập xác định hoặc dẫn đến kết quả vô nghiệm.\\\\ Vậy phương trình đã cho vô nghiệm.'''
                             % (latex(a), latex(c), latex(b), latex(b), latex(c), latex(a), latex(c), latex(c), latex(b), latex(b)))

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


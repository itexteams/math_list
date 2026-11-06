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


def bt_dang4_p2_b3_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Random tham số cho hàm số f(x) = tan(a*x) - b
            # Chọn a dương nhỏ để bài toán đẹp (ví dụ a = 2 hoặc a = 3)
            a = random.choice([2, 3])
            b = randint(1, 3)

            # Biểu thức hàm số phục vụ sinh lời giải ngẫu nhiên
            bt = tan(a*x) - b

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hàm số $f(x)=\\tan %sx-%s$. Khi đó:''' 
                             %(latex(a), latex(b)))

            ########################################################################Nhận biết ############################################
            # Ý d trong ảnh: Hàm số đã cho là hàm tuần hoàn.
            nb_da_1_d = '\\True Hàm số đã cho là hàm tuần hoàn'
            nb_da_1_s = 'Hàm số đã cho không phải là hàm tuần hoàn'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = ('''Hàm số $f(x)=\\tan %sx-%s$ tuần hoàn với chu kỳ $T=\\frac{\\pi}{%s}$.'''
                            %(latex(a), latex(b), latex(a)))

            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################Thông hiểu ############################################
            # Ý a trong ảnh: Giá trị của hàm số tại x = pi/(4*a) bằng 1 - b (do tan(pi/4) = 1)
            # Nếu đúng: 1 - b. Nếu sai: giá trị khác (ví dụ 0)
            val_a_correct = 1 - b
            val_a_wrong = 0 if val_a_correct != 0 else 1

            th_da_1_d = 'Giá trị của hàm số tại $x=\\frac{\\pi}{%s}$ bằng $%s$' %(latex(4*a), latex(val_a_correct))
            if val_a_correct == 0:
                th_da_1_d = '\\True ' + th_da_1_d
            else:
                th_da_1_d = '\\True ' + th_da_1_d

            th_da_1_s = 'Giá trị của hàm số tại $x=\\frac{\\pi}{%s}$ bằng $%s$' %(latex(4*a), latex(val_a_wrong))

            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            loigiai_th_1 = ('''Tại $x=\\frac{\\pi}{%s}$, ta có $f\\left(\\frac{\\pi}{%s}\\right)=\\tan\\left(%s \\cdot \\frac{\\pi}{%s}\\right)-%s = \\tan\\frac{\\pi}{4}-%s = 1-%s = %s$.'''
                            %(latex(4*a), latex(4*a), latex(a), latex(4*a), latex(b), latex(b), latex(b), latex(val_a_correct)))

            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Ý b trong ảnh: Tính tại x = pi/3 hoặc một giá trị đặc biệt khác. 
            # Chọn góc để tan(a*x) ra căn(3). Nếu a=2 -> x = pi/6 -> tan(pi/3)=căn(3). Nếu a=3 -> x = pi/9.
            # Tổng quát: tính tại x = pi / (3*a) => tan(pi/3) = sqrt(3) => f(x) = sqrt(3) - b
            vd_da_1_d = '\\True Giá trị của hàm số tại $x=\\frac{\\pi}{%s}$ bằng $\\sqrt{3}-%s$' %(latex(3*a), latex(b))
            vd_da_1_s = 'Giá trị của hàm số tại $x=\\frac{\\pi}{%s}$ bằng $-\\sqrt{3}-%s$' %(latex(3*a), latex(b))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = ('''Tại $x=\\frac{\\pi}{%s}$, ta có $f\\left(\\frac{\\pi}{%s}\\right)=\\tan\\left(%s \\cdot \\frac{\\pi}{%s}\\right)-%s = \\tan\\frac{\\pi}{3}-%s = \\sqrt{3}-%s$.'''
                            %(latex(3*a), latex(3*a), latex(a), latex(3*a), latex(b), latex(b), latex(b)))

            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Ý c trong ảnh: Số nghiệm thuộc đoạn [0; pi] khi f(x) = -b - 1 (tức tan(ax) = -1)
            # Phương trình tan(ax) = -1 <=> ax = -pi/4 + k*pi <=> x = -pi/(4a) + k*pi/a
            # Số nghiệm thuộc [0; pi]: 0 <= -pi/(4a) + k*pi/a <= pi <=> 1/4 <= k <= a + 1/4
            # Vì k nguyên nên k chạy từ 1 đến a. Vậy có đúng 'a' giá trị x.
            vdc_da_1_d = '\\True Có đúng %s giá trị $x$ thuộc $[0;\\pi]$ khi hàm số đạt giá trị bằng $%s$' %(latex(a), latex(-b-1))
            vdc_da_1_s = 'Có đúng %s giá trị $x$ thuộc $[0;\\pi]$ khi hàm số đạt giá trị bằng $%s$' %(latex(a+1), latex(-b-1))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = ('''Hàm số đạt giá trị bằng $%s \\Leftrightarrow \\tan %sx-%s = %s \\Leftrightarrow \\tan %sx = -1$. \\\\
            Ta có $\\tan %sx = -1 \\Leftrightarrow %sx = -\\frac{\\pi}{4} + k\\pi \\Leftrightarrow x = -\\frac{\\pi}{%s} + \\frac{k\\pi}{%s}$ ($k \\in \\mathbb{Z}$). \\\\
            Xét $x \\in [0;\\pi] \\Leftrightarrow 0 \\le -\\frac{\\pi}{%s} + \\frac{k\\pi}{%s} \\le \\pi \\Leftrightarrow \\frac{1}{4} \\le k \\le %s + \\frac{1}{4}$. \\\\
            Do $k \\in \\mathbb{Z}$ nên $k \\in \\{1; 2; \\dots; %s\\}$. Vậy có đúng %s giá trị $x$ thỏa mãn.'''
                             %(latex(-b-1), latex(a), latex(b), latex(-b-1), latex(a), latex(a), latex(a), latex(4*a), latex(a), latex(4*a), latex(a), latex(a), latex(a), latex(a)))

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
               '{'+str(shuffled_answers_th[0])+'}\n'
               '{'+str(shuffled_answers_vd[0])+'}\n'
               '{'+str(shuffled_answers_vdc[0])+'}\n'
               '{'+str(shuffled_answers_nb[0])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions_th[0])+'\n'
                '\\item '+str(shuffled_solutions_vd[0])+'\n'
                '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                '\\item '+str(shuffled_solutions_nb[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


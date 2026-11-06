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


def bt_dang33_p2_b4_c1_ds11(self):
            # Khai báo biến
            # Để đơn giản và bài toán luôn đẹp, ta chọn cố định c = 1 và chọn ngẫu nhiên a, b, d sao cho có nghiệm đẹp.
            c = 1
            a = random.choice([2, 3])
            b = random.choice([1, -1])
            d = random.choice([2, 3, 4]) # Đảm bảo |d/c| > 1 để phương trình cos(x) = d/c vô nghiệm

            # Khai triển f(x) = (a*cos(x) - b)*(cos(x) - d)
            # = a*cos^2(x) - (a*d + b)*cos(x) + b*d
            # = (a/2)*cos(2x) - (a*d + b)*cos(x) + b*d + a/2
            coef_cos2x = Rational(a, 2)
            coef_cosx = a * d + b
            constant_term = b * d + Rational(a, 2)

            # Chuỗi LaTeX biểu diễn hàm số ban đầu
            if b > 0:
                factor1 = "%s \\cos x - %s" % (latex(a) if a != 1 else "", latex(b))
            else:
                factor1 = "%s \\cos x + %s" % (latex(a) if a != 1 else "", latex(-b))

            if d > 0:
                factor2 = "\\cos x - %s" % latex(d)
            else:
                factor2 = "\\cos x + %s" % latex(-d)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hàm số $f(x)=\\left(%s\\right)\\left(%s\\right)$.''' 
                             % (factor1, factor2))

            ########################################################################
            # Nhận biết
            # Các đáp án
            if coef_cosx > 0:
                sign_cosx = "- %s" % latex(coef_cosx)
            else:
                sign_cosx = "+ %s" % latex(-coef_cosx)

            if constant_term > 0:
                sign_const = "+ %s" % latex(constant_term)
            else:
                sign_const = "- %s" % latex(-constant_term)

            if coef_cos2x == 1:
                str_cos2x = "\\cos 2x"
            else:
                str_cos2x = "%s \\cos 2x" % latex(coef_cos2x)

            nb_da_1_d = '\\True Khai triển của hàm số là $f(x) = %s %s \\cos x %s$' % (str_cos2x, sign_cosx, sign_const)
            nb_da_1_s = 'Khai triển của hàm số là $f(x) = %s \\cos 2x %s \\cos x %s$' % (latex(a), sign_cosx, sign_const)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Ta có $f(x) = %s \\cos^2 x - %s \\cos x + %s = %s \\left(\\frac{1 + \\cos 2x}{2}\\right) - %s \\cos x + %s = %s %s \\cos x %s$.'''
                            % (latex(a), latex(a*d+b), latex(b*d), latex(a), latex(a*d+b), latex(b*d), str_cos2x, sign_cosx, sign_const))

            list_nb_2 = [loigiai_nb_1]
            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu
            # Các đáp án
            th_da_1_d = '\\True Hàm số đã cho là hàm số chẵn'
            th_da_1_s = 'Hàm số đã cho là hàm số lẻ'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Tập xác định của hàm số là $\\mathscr{D} = \\mathbb{R}$.\\\\ Với mọi $x \\in \\mathbb{R}$ thì $-x \\in \\mathbb{R}$ và $f(-x) = \\left(%s \\cos(-x) - %s\\right)\\left(\\cos(-x) - %s\\right) = \\left(%s \\cos x - %s\\right)\\left(\\cos x - %s\\right) = f(x)$.\\\\ Vậy hàm số đã cho là hàm số chẵn.'''
                            % (latex(a), latex(b), latex(d), latex(a), latex(b), latex(d)))

            list_th_2 = [loigiai_th_1]
            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng
            # Các đáp án
            vd_da_1_d = '\\True Hàm số đã cho tuần hoàn với chu kỳ $T = 2\\pi$'
            vd_da_1_s = 'Hàm số đã cho tuần hoàn với chu kỳ $T = \\pi$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Hàm số $y = \\cos 2x$ tuần hoàn với chu kỳ $T_1 = \\pi$, hàm số $y = \\cos x$ tuần hoàn với chu kỳ $T_2 = 2\\pi$.\\\\ Do đó hàm số $f(x)$ tuần hoàn với chu kỳ $T = \\text{BCNN}(\\pi, 2\\pi) = 2\\pi$.''')

            list_vd_2 = [loigiai_vd_1]
            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao
            # Các đáp án
            vdc_da_1_d = '\\True Phương trình $f(x) = 0$ có đúng 4 nghiệm thuộc đoạn $[-2\\pi; 2\\pi]$'
            vdc_da_1_s = 'Phương trình $f(x) = 0$ có đúng 2 nghiệm thuộc đoạn $[-2\\pi; 2\\pi]$'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Phương trình $f(x) = 0 \\Leftrightarrow \\left(%s\\right)\\left(%s\\right) = 0 \\Leftrightarrow \\left[\\begin{aligned} & \\cos x = %s \\\\ & \\cos x = %s \\end{aligned}\\right.$.\\\\ Vì $|%s| > 1$ nên phương trình $\\cos x = %s$ vô nghiệm.\\\\ Phương trình $\\cos x = %s$ có nghiệm $x = \\pm \\alpha + k2\\pi$. Trong đoạn $[-2\\pi; 2\\pi]$, phương trình này có đúng 4 nghiệm phân biệt.'''
                             % (factor1, factor2, latex(Rational(b, a)), latex(d), latex(d), latex(d), latex(Rational(b, a))))

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


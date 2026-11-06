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


def bt_dang6_p2_b3_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # B1: Nghiên cứu đề bài - Hàm số f(x) = (ax + b)^n
            # B2 & B3: Viết lại bài toán và thiết lập Random
            a = random.choice([2, 3, 4])
            b = random.choice([1, 3, 5, 7])
            n = random.choice([4, 5]) # Chọn n=4 hoặc 5 để đa dạng đạo hàm

            f = (a*x + b)**n
            f1 = diff(f, x) # f'(x)
            f2 = diff(f1, x) # f''(x)

            # Giá trị nghiệm câu a
            nghiem_a = -Rational(b, a)

            # Giá trị k cho câu b để có nghiệm đẹp
            # f''(x) = n*(n-1)*a^2 * (ax+b)^(n-2). Ta chọn k = n*(n-1)*a^2
            k_val = n * (n - 1) * a**2
            # Khi đó (ax+b)^(n-2) = 1.
            # Nếu n-2 lẻ (n=5): ax+b=1 => x = (1-b)/a
            # Nếu n-2 chẵn (n=4): ax+b = 1 hoặc -1 => x = (1-b)/a hoặc x = (-1-b)/a
            if (n-2) % 2 == 0:
                sol_b_set = "S = \\left\\{ %s; %s \\right\\}" % (latex(Rational(-1-b, a)), latex(Rational(1-b, a)))
                sol_b_wrong = "S = \\left\\{ %s \\right\\}" % (latex(Rational(1-b, a)))
            else:
                sol_b_set = "x = %s" % (latex(Rational(1-b, a)))
                sol_b_wrong = "x = %s" % (latex(Rational(-1-b, a)))

            # Câu d: f'(x) = f''(x) 
            # na(ax+b)^{n-1} = n(n-1)a^2(ax+b)^{n-2}
            # => ax+b = (n-1)a (với x != -b/a)
            nghiem_d_2 = Rational((n-1)*a - b, a)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hàm số $f \\left( x \\right) = \\left( %s x + %s \\right)^{%s}$.''' 
                             % (latex(a), latex(b), latex(n)))

            ########################################################################
            # Nhận biết (Câu a)
            nb_da_1_d = '\\True Phương trình $f\'\' \\left( x \\right) = 0$ có duy nhất một nghiệm $x = %s$' % (latex(nghiem_a))
            nb_da_1_s = 'Phương trình $f\'\' \\left( x \\right) = 0$ vô nghiệm'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ('''Ta có $f\' \\left( x \\right) = %s \\left( %s x + %s \\right)^{%s}$ \\\\
                            $f\'\' \\left( x \\right) = %s \\left( %s x + %s \\right)^{%s}$. \\\\
                            Phương trình $f\'\' \\left( x \\right) = 0 \\Leftrightarrow %s x + %s = 0 \\Leftrightarrow x = %s$.'''
                            % (latex(n*a), latex(a), latex(b), latex(n-1),
                               latex(n*(n-1)*a**2), latex(a), latex(b), latex(n-2),
                               latex(a), latex(b), latex(nghiem_a)))

            list_nb_1 = [random.choice(list_nb_da_1)]
            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # Thông hiểu (Câu b)
            th_da_1_d = '\\True Phương trình $f\'\' \\left( x \\right) = %s$ có tập nghiệm là $%s$' % (latex(k_val), sol_b_set)
            th_da_1_s = 'Phương trình $f\'\' \\left( x \\right) = %s$ có tập nghiệm là $%s$' % (latex(k_val), sol_b_wrong)
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ('''Phương trình $f\'\' \\left( x \\right) = %s \\Leftrightarrow %s \\left( %s x + %s \\right)^{%s} = %s$ \\\\
                            $\\Leftrightarrow \\left( %s x + %s \\right)^{%s} = 1$. \\\\
                            Suy ra nghiệm của phương trình là $%s$.'''
                            % (latex(k_val), latex(n*(n-1)*a**2), latex(a), latex(b), latex(n-2), latex(k_val),
                               latex(a), latex(b), latex(n-2), sol_b_set))

            list_th_1 = [random.choice(list_th_da_1)]
            list_th_2 = [loigiai_th_1]

            ########################################################################
            # Vận dụng (Câu c)
            vd_da_1_d = 'Phương trình $\\frac{f\'\' \\left( x \\right)}{\\left( %s x + %s \\right)^2} = 0$ có nghiệm $x = %s$' % (latex(a), latex(b), latex(nghiem_a))
            vd_da_1_s = '\\True Phương trình $\\frac{f\'\' \\left( x \\right)}{\\left( %s x + %s \\right)^2} = 0$ vô nghiệm'% (latex(a), latex(b))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ('''Xét phương trình $\\frac{f\'\' \\left( x \\right)}{\\left( %s x + %s \\right)^2} = 0$. Điều kiện xác định: $x \\neq %s$. \\\\
                            Khi đó phương trình trở thành $f\'\' \\left( x \\right) = 0 \\Leftrightarrow x = %s$ (không thỏa mãn điều kiện). \\\\
                            Vậy phương trình vô nghiệm.'''
                            % (latex(a), latex(b), latex(nghiem_a), latex(nghiem_a)))

            list_vd_1 = [random.choice(list_vd_da_1)]
            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # Vận dụng cao (Câu d)
            vdc_da_1_d = 'Phương trình $f\' \\left( x \\right) = f\'\' \\left( x \\right)$ có duy nhất một nghiệm $x = %s$' % (latex(nghiem_d_2))
            vdc_da_1_s = '\\True Phương trình $f\' \\left( x \\right) = f\'\' \\left( x \\right)$ có các nghiệm là $x = %s$ và $x = %s$' % (latex(nghiem_a), latex(nghiem_d_2))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = ('''Ta có $f\' \\left( x \\right) = f\'\' \\left( x \\right) \\Leftrightarrow %s \\left( %s x + %s \\right)^{%s} = %s \\left( %s x + %s \\right)^{%s}$ \\\\
                            $\\Leftrightarrow %s \\left( %s x + %s \\right)^{%s} \\left[ \\left( %s x + %s \\right) - %s \\right] = 0$ \\\\
                            $\\Leftrightarrow \\left[ \\begin{aligned} & %s x + %s = 0 \\\\ & %s x = %s \\end{aligned} \\right. \\Leftrightarrow \\left[ \\begin{aligned} & x = %s \\\\ & x = %s \\end{aligned} \\right.$.'''
                             % (latex(n*a), latex(a), latex(b), latex(n-1), latex(n*(n-1)*a**2), latex(a), latex(b), latex(n-2),
                                latex(n*a), latex(a), latex(b), latex(n-2), latex(a), latex(b), latex((n-1)*a),
                                latex(a), latex(b), latex(a), latex((n-1)*a - b),
                                latex(nghiem_a), latex(nghiem_d_2)))

            list_vdc_1 = [random.choice(list_vdc_da_1)]
            list_vdc_2 = [loigiai_vdc_1]

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 đúng
            while True:
                ans_nb = random.choice(list_nb_da_1)
                ans_th = random.choice(list_th_da_1)
                ans_vd = random.choice(list_vd_da_1)
                ans_vdc = random.choice(list_vdc_da_1)

                answers_list = [ans_nb, ans_th, ans_vd, ans_vdc]
                true_count = count_true_answers(answers_list)

                if 1 <= true_count <= 3:
                    break

            # Gán lại vào list để xử lý zip
            list_nb_1 = [ans_nb]
            list_th_1 = [ans_th]
            list_vd_1 = [ans_vd]
            list_vdc_1 = [ans_vdc]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            combined_th = list(zip(list_th_1, list_th_2))
            combined_vd = list(zip(list_vd_1, list_vd_2))
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # Xuất câu hỏi
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


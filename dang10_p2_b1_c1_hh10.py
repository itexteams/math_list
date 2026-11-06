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


def bt_dang10_p2_b1_c1_hh10(self):
            # Khai báo biến
            # Khai báo biến
            m = random.randint(2, 4) # nghiệm dương
            n = random.randint(1, 4) # trị tuyệt đối nghiệm âm
            while n == m:
                n = random.randint(1, 4)

            B = n - m
            C = -m * n

            if B == 1:
                str_B_tan = "+ \\tan \\alpha"
            elif B == -1:
                str_B_tan = "- \\tan \\alpha"
            elif B > 0:
                str_B_tan = "+ %s\\tan \\alpha" % B
            elif B < 0:
                str_B_tan = "- %s\\tan \\alpha" % (-B)

            str_eq = "\\tan^2 \\alpha %s - %s = 0" % (str_B_tan, -C)

            val_P = Rational((m**2 + 1)**2, m**2)
            val_P_wrong = val_P + Rational(random.choice([-1, 1, 3, -3]), m**2)
            if val_P_wrong <= 0:
                val_P_wrong = val_P + Rational(2, m**2)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho $%s, 0^\\circ < \\alpha < 90^\\circ$ và biểu thức $P = \\frac{1}{\\cos^2 \\alpha} + \\frac{1}{\\sin^2 \\alpha}$.'''
                             % (str_eq))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Với mọi góc $\\alpha$ thỏa mãn $0^\\circ < \\alpha < 90^\\circ$ thì $\\tan \\alpha > 0$'
            nb_da_1_s = 'Với mọi góc $\\alpha$ thỏa mãn $0^\\circ < \\alpha < 90^\\circ$ thì $\\tan \\alpha < 0$'
            list_nb_da_1=[nb_da_1_d, nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Vì $0^\\circ < \\alpha < 90^\\circ$ (góc thuộc góc phần tư thứ I) nên $\\sin \\alpha > 0$ và $\\cos \\alpha > 0$, suy ra $\\tan \\alpha = \\frac{\\sin \\alpha}{\\cos \\alpha} > 0$.''')

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True $%s$ được viết lại $(\\tan \\alpha - %s)(\\tan \\alpha + %s) = 0$' % (str_eq, m, n)
            th_da_1_s = '$%s$ được viết lại $(\\tan \\alpha - %s)(\\tan \\alpha - %s) = 0$' % (str_eq, m, n)
            list_th_da_1=[th_da_1_d, th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Ta có $%s \\Leftrightarrow \\tan^2 \\alpha - %s\\tan \\alpha + %s\\tan \\alpha - %s = 0 \\\\
            \\Leftrightarrow \\tan \\alpha (\\tan \\alpha - %s) + %s(\\tan \\alpha - %s) = 0 \\Leftrightarrow (\\tan \\alpha - %s)(\\tan \\alpha + %s) = 0$.'''
                            % (str_eq, m, n, m*n, m, n, m, m, n))

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]
            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Biểu thức $P$ được đưa về dạng $P = \\tan^2 \\alpha + \\cot^2 \\alpha + 2$'
            vd_da_1_s = 'Biểu thức $P$ được đưa về dạng $P = \\tan^2 \\alpha + \\cot^2 \\alpha + 1$'
            list_vd_da_1=[vd_da_1_d, vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Ta có $P = \\frac{1}{\\cos^2 \\alpha} + \\frac{1}{\\sin^2 \\alpha} = \\left(1 + \\tan^2 \\alpha\\right) + \\left(1 + \\cot^2 \\alpha\\right) = \\tan^2 \\alpha + \\cot^2 \\alpha + 2$.''')

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]
            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Giá trị của biểu thức $P$ bằng $%s$' % (latex(val_P))
            vdc_da_1_s = 'Giá trị của biểu thức $P$ bằng $%s$' % (latex(val_P_wrong))
            list_vdc_da_1=[vdc_da_1_d, vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Từ $(\\tan \\alpha - %s)(\\tan \\alpha + %s) = 0 \\Leftrightarrow \\left[ \\begin{array}{l} \\tan \\alpha = %s \\\\ \\tan \\alpha = -%s \\end{array} \\right.$. \\\\
            Do $0^\\circ < \\alpha < 90^\\circ$ nên $\\tan \\alpha > 0$, suy ra $\\tan \\alpha = %s \\Rightarrow \\cot \\alpha = \\frac{1}{%s}$. \\\\
            Thay vào $P$, ta được $P = %s^2 + \\left(\\frac{1}{%s}\\right)^2 + 2 = %s$.'''
                             % (m, n, m, n, m, m, m, m, latex(val_P)))

            # Đưa các lời giải vào danh sách lời giải
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
                '\\end{ex}\n \\end{minipage}\n\n')
            return content


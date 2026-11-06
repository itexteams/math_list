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


def bt_dang3_p2_b1_c1_ds11(self):
            # Khai báo biến
            # Khai báo và tính toán các hằng số bằng SymPy
            val_cos30 = Rational(1, 2) * sqrt(3)
            val_sin45 = Rational(1, 2) * sqrt(2)
            val_cot45 = Rational(1, 1)

            val_sin60 = Rational(1, 2) * sqrt(3)
            val_tan30 = Rational(1, 3) * sqrt(3)

            val_sin_pi6 = Rational(1, 2)
            val_cos_pi6 = Rational(1, 2) * sqrt(3)

            val_tan_pi4 = Rational(1, 1)
            val_cot_pi2 = Rational(0, 1)

            # Ngẫu nhiên hóa các hệ số trong bài toán để tạo các phương án khác nhau
            # Biểu thức A: k1/sqrt(3) * cos(30) - k2*sqrt(2) * sin(45) + k3 * cot(45)
            k1 = randint(1, 3)
            k2 = randint(1, 3)
            k3 = randint(1, 3)
            val_A = Rational(k1, 2) - k2 + k3

            # Biểu thức B: sin^2(60) + tan^2(30) - k4
            k4 = randint(1, 3)
            val_B = Rational(3, 4) + Rational(1, 3) - k4

            # Biểu thức C: k5 * sin(pi/6) + sqrt(3) * cos(pi/6)
            k5 = randint(1, 4)
            val_C = Rational(k5, 2) + Rational(3, 2)

            # Biểu thức D: (tan(pi/4) + 1) / (1/sqrt(k6) * cot(pi/2) - 2) -> mẫu bằng -2 vì cot(pi/2) = 0
            k6 = random.choice([2, 3, 5])
            val_D = Rational(2, -2) # Luôn bằng -1

            # Nội dung câu hỏi tổng quát
            noidungcauhoi = ('''Tính được giá trị các biểu thức. Khi đó:''')

            ########################################################################
            # Nhận biết (Biểu thức A)
            nb_da_1_d = '\\True $A = \\frac{%s}{\\sqrt{3}}\\cos 30^\\circ - %s\\sqrt{2}\\sin 45^\\circ + \\cot 45^\\circ = %s$' %(latex(k1), latex(k2) if k2 != 1 else '', latex(val_A))
            nb_da_1_s = '$A = \\frac{%s}{\\sqrt{3}}\\cos 30^\\circ - %s\\sqrt{2}\\sin 45^\\circ + \\cot 45^\\circ = %s$' %(latex(k1), latex(k2) if k2 != 1 else '', latex(val_A + 1))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]
            loigiai_nb_1 = ('''Ta có $A = \\frac{%s}{\\sqrt{3}}\\cdot\\frac{\\sqrt{3}}{2} - %s\\sqrt{2}\\cdot\\frac{\\sqrt{2}}{2} + 1 = \\frac{%s}{2} - %s + 1 = %s$.''' %(latex(k1), latex(k2) if k2 != 1 else '', latex(k1), latex(k2), latex(val_A)))
            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu (Biểu thức B)
            th_da_1_d = '\\True $B = \\sin^2 60^\\circ + \\tan^2 30^\\circ - %s = %s$' %(latex(k4), latex(val_B))
            th_da_1_s = '$B = \\sin^2 60^\\circ + \\tan^2 30^\\circ - %s = %s$' %(latex(k4), latex(val_B - 1))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]
            loigiai_th_1 = ('''Ta có $B = \\left(\\frac{\\sqrt{3}}{2}\\right)^2 + \\left(\\frac{1}{\\sqrt{3}}\\right)^2 - %s = \\frac{3}{4} + \\frac{1}{3} - %s = %s$.''' %(latex(k4), latex(k4), latex(val_B)))
            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng (Biểu thức C)
            vd_da_1_d = '\\True $C = %s\\sin\\frac{\\pi}{6} + \\sqrt{3}\\cos\\frac{\\pi}{6} = %s$' %(latex(k5) if k5 != 1 else '', latex(val_C))
            vd_da_1_s = '$C = %s\\sin\\frac{\\pi}{6} + \\sqrt{3}\\cos\\frac{\\pi}{6} = %s$' %(latex(k5) if k5 != 1 else '', latex(val_C + Rational(1,2)))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]
            loigiai_vd_1 = ('''Ta có $C = %s\\cdot\\frac{1}{2} + \\sqrt{3}\\cdot\\frac{\\sqrt{3}}{2} = %s$.''' %(latex(k5) if k5 != 1 else '1', latex(val_C)))
            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao (Biểu thức D)
            vdc_da_1_d = '\\True $D = \\frac{\\tan\\frac{\\pi}{4} + 1}{\\frac{1}{\\sqrt{%s}}\\cot\\frac{\\pi}{2} - 2} = %s$' %(latex(k6), latex(val_D))
            vdc_da_1_s = '$D = \\frac{\\tan\\frac{\\pi}{4} + 1}{\\frac{1}{\\sqrt{%s}}\\cot\\frac{\\pi}{2} - 2} = \\frac{6}{5}$' %(latex(k6))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]
            loigiai_vdc_1 = ('''Ta có $D = \\frac{1 + 1}{\\frac{1}{\\sqrt{%s}}\\cdot 0 - 2} = %s$.''' %(latex(k6), latex(val_D)))
            list_vdc_2 = [loigiai_vdc_1]

            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi số câu đúng từ 1 đến 3 câu đúng
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán lại vào danh sách kết xuất
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

            # Xuất câu hỏi theo định dạng mẫu mã nguồn
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
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


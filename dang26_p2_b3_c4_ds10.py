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


def bt_dang26_p2_b3_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # --- BƯỚC 1: SINH DỮ LIỆU NGẪU NHIÊN ---
            # Để bài toán có nghiệm đẹp: x1, x2 là 2 nghiệm của phương trình x^2 - px + S_min = 0
            # Ta chọn trước x1, x2 là các số nguyên.
            x1 = randint(6, 8)
            x2 = randint(12, 14)
            p = x1 + x2 # Nửa chu vi
            L = 2 * p   # Tổng chiều dài lưới (40 trong đề gốc)
            S_min = x1 * x2 # Diện tích tối thiểu (96 trong đề gốc)
            S_max = (p**2) / 4 # Diện tích cực đại (100 trong đề gốc)
            S_impossible = int(S_max + randint(2, 10)) # Một giá trị diện tích không thể đạt được (105 trong đề gốc)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Ông Tài có %s mét lưới và muốn dùng hết %s mét lưới đó để rào nuôi gà con, ông Tài có khu vườn rất rộng và cần một khu để chăm gà con hình chữ nhật có diện tích không nhỏ hơn %s mét vuông. Giả sử $x$ là một kích thước của hình chữ nhật.''' 
                             %(latex(L), latex(L), latex(S_min)))

            ########################################################################
            # a) Nhận biết: Kích thước còn lại ############################################
            nb_da_1_d = '\\True Kích thước còn lại của hình chữ nhật là $%s - x$' %(latex(p))
            nb_da_1_s = 'Kích thước còn lại của hình chữ nhật là $%s - x$' %(latex(L))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Gọi hai kích thước của hình chữ nhật là $x$ và $y$. \\\\
                            Chu vi của hình chữ nhật là $2(x+y) = %s \\Rightarrow x+y = %s \\Rightarrow y = %s - x$. \\\\
                            Vậy kích thước còn lại là $%s - x$.''' 
                            %(latex(L), latex(p), latex(p), latex(p)))

            list_nb_1 = [nb_da_1]
            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # b) Thông hiểu: Diện tích ############################################
            th_da_1_d = '\\True Diện tích của hình chữ nhật là $x(%s - x)$' %(latex(p))
            th_da_1_s = 'Diện tích của hình chữ nhật là $x(%s - x)$' %(latex(L))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Diện tích hình chữ nhật được tính theo công thức $S = x \\cdot y$. \\\\
                            Thay $y = %s - x$ vào ta được $S = x(%s - x)$.''' 
                            %(latex(p), latex(p)))

            list_th_1 = [th_da_1]
            list_th_2 = [loigiai_th_1]

            ########################################################################
            # c) Vận dụng: Diện tích không thể bằng... ############################################
            vd_da_1_d = '\\True Diện tích của hình chữ nhật không thể bằng $%s$ m$^2$' %(latex(S_impossible))
            vd_da_1_s = 'Diện tích của hình chữ nhật có thể bằng $%s$ m$^2$' %(latex(S_impossible))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Xét hàm diện tích $S(x) = x(%s - x) = -x^2 + %sx$. \\\\
                            Đây là hàm số bậc hai có giá trị lớn nhất tại $x = \\frac{-%s}{2(-1)} = %s$. \\\\
                            Giá trị lớn nhất $S_{max} = S(%s) = %s$. \\\\
                            Vì %s > %s nên diện tích không thể bằng %s m$^2$.''' 
                            %(latex(p), latex(p), latex(p), latex(p/2), latex(p/2), latex(int(S_max)), latex(S_impossible), latex(int(S_max)), latex(S_impossible)))

            list_vd_1 = [vd_da_1]
            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # d) Vận dụng cao: Tập nghiệm của x ############################################
            vdc_da_1_d = '\\True $%s \\le x \\le %s$' %(latex(x1), latex(x2))
            vdc_da_1_s = '$%s \\le x \\le %s$' %(latex(x1-1), latex(x2+1))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Theo đề bài, diện tích không nhỏ hơn %s m$^2$ nên: \\\\
                             $x(%s - x) \\ge %s \\Leftrightarrow -x^2 + %sx - %s \\ge 0$. \\\\
                             Xét phương trình $-x^2 + %sx - %s = 0$ có hai nghiệm $x = %s, x = %s$. \\\\
                             Dựa vào quy tắc xét dấu tam thức bậc hai, tập nghiệm của bất phương trình là $%s \\le x \\le %s$.''' 
                             %(latex(S_min), latex(p), latex(S_min), latex(p), latex(S_min), latex(p), latex(S_min), latex(x1), latex(x2), latex(x1), latex(x2)))

            list_vdc_1 = [vdc_da_1]
            list_vdc_2 = [loigiai_vdc_1]

            # --- BƯỚC 2: KIỂM TRA SỐ CÂU ĐÚNG ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)
                if 1 <= true_count <= 3:
                    break

            # Gán lại vào danh sách để xuất dữ liệu
            shuffled_answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            # --- BƯỚC 3: XUẤT NỘI DUNG ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(shuffled_answers[0]) + '}\n'
                '{' + str(shuffled_answers[1]) + '}\n'
                '{' + str(shuffled_answers[2]) + '}\n'
                '{' + str(shuffled_answers[3]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(shuffled_solutions[0]) + '\n'
                '\\item ' + str(shuffled_solutions[1]) + '\n'
                '\\item ' + str(shuffled_solutions[2]) + '\n'
                '\\item ' + str(shuffled_solutions[3]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('- -','+')
            return content


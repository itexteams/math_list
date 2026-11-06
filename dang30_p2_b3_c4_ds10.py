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


def bt_dang30_p2_b3_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x, m = symbols('x m')

            # Bước 1 & 3: Tạo các thông số ngẫu nhiên
            # Thay số 2023 bằng một số ngẫu nhiên K quanh năm hiện tại
            K = randint(2020, 2030)
            f_x = -x**2 + 2*x + m - K

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hàm số $f(x) = %s$.''' 
                             % (latex(f_x)))

            ########################################################################
            # a) Nhận biết: Tính f(1)
            ########################################################################
            val_f1 = m - (K - 1)
            nb_da_1_d = '\\True $f(1) = %s$' % (latex(val_f1))
            nb_da_1_s = '$f(1) = m - %s$' % (K) # Sai vì thiếu +1
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ('''Ta có $f(1) = -(1)^2 + 2(1) + m - %s = -1 + 2 + m - %s = m - %s$.''' 
                            % (K, K, K-1))

            ########################################################################
            # b) Thông hiểu: Tính chất hàm bậc hai
            ########################################################################
            th_da_1_d = '\\True Hàm số đã cho luôn là hàm số bậc hai'
            th_da_1_s = 'Hàm số đã cho là hàm số bậc hai khi $m \\neq %s$' % (K)
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ('''Hàm số $f(x) = -x^2 + 2x + m - %s$ có hệ số $a = -1 \\neq 0$ với mọi giá trị của tham số $m$. Do đó, đây luôn là hàm số bậc hai.''' 
                            % (K))

            ########################################################################
            # c) Vận dụng: Tam thức bậc hai âm với mọi x
            ########################################################################
            # f(x) < 0 <=> Delta' < 0 <=> 1 + m - K < 0 <=> m < K - 1
            cond_c = K - 1
            vd_da_1_d = '\\True Tam thức bậc hai $f(x)$ nhận giá trị âm $\\forall x \\in \\mathbb{R}$ khi $m < %s$' % (cond_c)
            vd_da_1_s = 'Tam thức bậc hai $f(x)$ nhận giá trị âm $\\forall x \\in \\mathbb{R}$ khi $m > %s$' % (cond_c)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ('''Tam thức bậc hai $f(x)$ có hệ số $a = -1 < 0$. \\\\
                            Để $f(x) < 0, \\forall x \\in \\mathbb{R}$ thì $\\Delta' < 0$. \\\\
                            Ta có $\\Delta' = 1^2 - (-1)(m - %s) = 1 + m - %s = m - %s$. \\\\
                            $\\Delta' < 0 \\Leftrightarrow m - %s < 0 \\Leftrightarrow m < %s$.''' 
                            % (K, K, K-1, K-1, K-1))

            ########################################################################
            # d) Vận dụng cao: Biến đổi biểu thức f(x+2)
            ########################################################################
            f_x_plus_2 = expand(f_x.subs(x, x + 2))
            vdc_da_1_d = '\\True $f(x+2) = %s$' % (latex(f_x_plus_2))
            vdc_da_1_s = '$f(x+2) = -x^2 - 2x + m - %s$' % (K - 8) # Tạo một giá trị sai khác
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = ('''Ta có $f(x+2) = -(x+2)^2 + 2(x+2) + m - %s$. \\\\
                             $= -(x^2 + 4x + 4) + 2x + 4 + m - %s$. \\\\
                             $= -x^2 - 4x - 4 + 2x + 4 + m - %s$. \\\\
                             $= %s$.''' 
                             % (K, K, K, latex(f_x_plus_2)))

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

            # Gán vào list để đồng bộ với phần xuất content
            shuffled_answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            # Xuất câu hỏi theo định dạng mẫu
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
                '\\end{ex}\n \\end{minipage}\n\n')
            return content


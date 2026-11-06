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


def bt_dang20_p2_b2_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # BƯỚC 1: Tạo các thông số ngẫu nhiên cho bài toán
            # Giả sử Parabol (C): y = x^2
            # Chọn 2 hoành độ giao điểm nguyên x1, x2 để đường thẳng (d) đẹp
            x1 = random.randint(-4, -1)
            x2 = random.randint(1, 4)
            y1 = x1**2
            y2 = x2**2

            # Phương trình đường thẳng d: y = ax + b đi qua A(x1, y1) và B(x2, y2)
            # a = (y2 - y1) / (x2 - x1)
            # b = y1 - a*x1
            a_val = (y2 - y1) // (x2 - x1)
            b_val = y1 - a_val * x1

            # Điểm M nằm trên (C) nhưng không nằm trên (d) để làm câu hỏi
            xM = random.choice([i for i in range(-3, 4) if i != x1 and i != x2 and i != 0])
            yM = xM**2

            # Điểm N là giao điểm của (d) với trục tung => N(0, b)
            # f(0) = 0, nếu b != 0 thì N không thuộc (C)
            n_tung_do = b_val

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hàm số $y = f(x) = x^2$ có đồ thị $(C)$ và hàm số $y = g(x) = %s x + %s$ có đồ thị là đường thẳng $(d)$.''' 
                             %(latex(a_val), latex(b_val)))

            ########################################################################
            # Nhận biết: Kiểm tra điểm thuộc đồ thị (C)
            nb_da_1_d = '\\True Ta có $f(%s) = %s$ nên $M(%s; %s) \\in (C)$' % (latex(xM), latex(yM), latex(xM), latex(yM))
            nb_da_1_s = 'Ta có $f(%s) = %s$ nên $M(%s; %s) \\notin (C)$' % (latex(xM), latex(yM), latex(xM), latex(yM))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)
            loigiai_nb_1 = ('Ta có $f(%s) = (%s)^2 = %s$ nên điểm $M(%s; %s)$ thuộc đồ thị $(C)$.' % (latex(xM), latex(xM), latex(yM), latex(xM), latex(yM)))

            ########################################################################
            # Thông hiểu: Sự biến thiên của hàm số bậc hai
            th_da_1_d = '\\True Hàm số $y = f(x) = x^2$ đồng biến trên $(0; +\\infty)$ và nghịch biến trên $(-\\infty; 0)$'
            th_da_1_s = 'Hàm số $y = f(x) = x^2$ nghịch biến trên $(0; +\\infty)$ và đồng biến trên $(-\\infty; 0)$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)
            loigiai_th_1 = ('Hàm số $y = x^2$ có hệ số $a=1>0$ nên đồng biến trên khoảng $(0; +\\infty)$ và nghịch biến trên khoảng $(-\\infty; 0)$.')

            ########################################################################
            # Vận dụng: Giao điểm với trục tung
            vd_da_1_d = '\\True Đường thẳng $(d)$ cắt trục tung tại điểm $N(0; %s)$ và $N \\notin (C)$' % (latex(n_tung_do))
            vd_da_1_s = '\\True Đường thẳng $(d)$ cắt trục tung tại điểm $N(0; %s)$ và $N \\in (C)$' % (latex(n_tung_do)) if n_tung_do == 0 else 'Đường thẳng $(d)$ cắt trục tung tại điểm $N(%s; 0)$' % (latex(n_tung_do))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)
            loigiai_vd_1 = ('Đường thẳng $(d)$ cắt trục tung tại điểm có hoành độ bằng $0$, suy ra $y = g(0) = %s$. Vậy $N(0; %s)$. Mặt khác $f(0) = 0$, vì $0 \\neq %s$ nên $N \\notin (C)$.' % (latex(n_tung_do), latex(n_tung_do), latex(n_tung_do)))

            ########################################################################
            # Vận dụng cao: Giao điểm của (C) và (d)
            vdc_da_1_d = '\\True Hai điểm $A(%s; %s)$ và $B(%s; %s)$ là giao điểm của $(C)$ và $(d)$' % (latex(x1), latex(y1), latex(x2), latex(y2))
            vdc_da_1_s = 'Chỉ có duy nhất điểm $A(%s; %s)$ là giao điểm của $(C)$ và $(d)$' % (latex(x1), latex(y1))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)
            loigiai_vdc_1 = ('Xét phương trình hoành độ giao điểm: $x^2 = %s x + %s \\Leftrightarrow x^2 - (%s)x - (%s) = 0$. Giải phương trình ta được $x = %s$ hoặc $x = %s$. Với $x=%s \\Rightarrow y=%s$; với $x=%s \\Rightarrow y=%s$. Vậy $A, B$ là hai giao điểm.' % (latex(a_val), latex(b_val), latex(a_val), latex(b_val), latex(x1), latex(x2), latex(x1), latex(y1), latex(x2), latex(y2)))

            # Lọc để đảm bảo số câu đúng từ 1 đến 3
            while True:
                ans_list = [random.choice(list_nb_da_1), random.choice(list_th_da_1), random.choice(list_vd_da_1), random.choice(list_vdc_da_1)]
                true_count = sum('\\True' in a for a in ans_list)
                if 1 <= true_count <= 3:
                    shuffled_answers = ans_list
                    break

            # Gán lời giải tương ứng (đơn giản hóa để khớp với đáp án đã chọn)
            final_solutions = []
            for i, ans in enumerate(shuffled_answers):
                if i == 0: final_solutions.append(loigiai_nb_1)
                elif i == 1: final_solutions.append(loigiai_th_1)
                elif i == 2: final_solutions.append(loigiai_vd_1)
                elif i == 3: final_solutions.append(loigiai_vdc_1)

            # Xuất nội dung theo mẫu
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
                '\\item ' + str(final_solutions[0]) + '\n'
                '\\item ' + str(final_solutions[1]) + '\n'
                '\\item ' + str(final_solutions[2]) + '\n'
                '\\item ' + str(final_solutions[3]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


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


def bt_dang39_p2_b3_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # BƯỚC 3: SUY NGHĨ TÌM CÁCH RANDOM BÀI TOÁN
            # Ta chọn 2 nghiệm nguyên x1, x2 sao cho x1 + x2 là số chẵn để L = 2(x1+x2) đẹp
            # Giả sử x1, x2 là khoảng cách từ cột đến tường để đạt diện tích M
            x1 = random.randint(3, 5)
            x2 = x1 + random.randint(2, 4)
            # Để tổng L/2 = x1 + x2 chẵn thì x1, x2 cùng tính chẵn lẻ hoặc... 
            # Tuy nhiên để tổng quát, ta chỉ cần L = 2*(x1 + x2) là số chẵn.
            L = 2 * (x1 + x2) 
            M = 2 * x1 * x2 # Diện tích mốc
            S_max = (L**2) // 8 # Diện tích cực đại
            K = S_max + random.randint(5, 15) # Một giá trị diện tích không thể đạt tới

            # Nội dung câu hỏi
            noidungcauhoi = ('''Bác Tuân có một tấm lưới dài $%s$m. Bác muốn dùng tấm lưới này rào chắn ba mặt áp bên bờ tường của khu vườn nhà mình thành một mảnh đất hình chữ nhật để trồng rau. Gọi $x(m)$, với $0 < x < %s$ là khoảng cách từ cột góc của hàng rào đến bờ tường.''' 
                             %(latex(L), latex(L//2)))

            ########################################################################
            # a) PQ = L - 2x
            nb_da_1_d = '\\True $PQ = %s - 2x$' % (latex(L))
            nb_da_1_s = '$PQ = %s - x$' % (latex(L))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Gọi $y$ là chiều dài cạnh $PQ$. Vì tổng chiều dài lưới là $%s$m nên ta có $2x + y = %s \\Rightarrow y = %s - 2x$. Vậy $PQ = %s - 2x$.''' 
                            % (latex(L), latex(L), latex(L), latex(L)))

            list_nb_1 = [nb_da_1]
            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # b) Diện tích S = -2x^2 + Lx
            th_da_1_d = '\\True Diện tích mảnh đất hình chữ nhật là $S = -2x^2 + %sx$' % (latex(L))
            th_da_1_s = 'Diện tích mảnh đất hình chữ nhật là $S = -x^2 + %sx$' % (latex(L))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Diện tích hình chữ nhật là $S = x \\cdot PQ = x(%s - 2x) = -2x^2 + %sx$.''' 
                            % (latex(L), latex(L)))

            list_th_1 = [th_da_1]
            list_th_2 = [loigiai_th_1]

            ########################################################################
            # c) Diện tích không thể bằng K (K > S_max)
            vd_da_1_d = '\\True Diện tích mảnh đất hình chữ nhật không thể bằng $%sm^2$' % (latex(K))
            vd_da_1_s = 'Diện tích mảnh đất hình chữ nhật có thể đạt bằng $%sm^2$' % (latex(K))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Xét hàm số $S(x) = -2x^2 + %sx$ với $0 < x < %s$. \\\\
                            Đồ thị là parabol có đỉnh tại $x = %s$, giá trị lớn nhất là $S(%s) = %s$. \\\\
                            Vì $%s > %s$ nên diện tích không thể bằng $%sm^2$.''' 
                            % (latex(L), latex(L//2), latex(Rational(L, 4)), latex(Rational(L, 4)), latex(S_max), latex(K), latex(S_max), latex(K)))

            list_vd_1 = [vd_da_1]
            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # d) S >= M thì x thuộc [x1, x2]
            vdc_da_1_d = '\\True Để diện tích mảnh đất được rào chắn của bác không nhỏ hơn $%sm^2$ thì $x \\in [%s;%s]m$' % (latex(M), latex(x1), latex(x2))
            vdc_da_1_s = 'Để diện tích mảnh đất được rào chắn của bác không nhỏ hơn $%sm^2$ thì $x \\in [0;%s]m$' % (latex(M), latex(x1))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Để diện tích không nhỏ hơn $%sm^2$, ta có bất phương trình: \\\\
                             $-2x^2 + %sx \\ge %s \\Leftrightarrow -2x^2 + %sx - %s \\ge 0 \\Leftrightarrow x^2 - %sx + %s \\le 0$. \\\\
                             Tam thức bậc hai có hai nghiệm $x = %s, x = %s$. \\\\
                             Vậy tập nghiệm là $x \\in [%s; %s]$.''' 
                             % (latex(M), latex(L), latex(M), latex(L), latex(M), latex(L//2), latex(M//2), latex(x1), latex(x2), latex(x1), latex(x2)))

            list_vdc_1 = [vdc_da_1]
            list_vdc_2 = [loigiai_vdc_1]

            ########################################################################
            # Phần logic xáo trộn và xuất nội dung
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                ans_a = random.choice(list_nb_da_1)
                ans_b = random.choice(list_th_da_1)
                ans_c = random.choice(list_vd_da_1)
                ans_d = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([ans_a, ans_b, ans_c, ans_d]) <= 3:
                    break

            # Gán vào list cuối cùng để khớp với template minipage
            shuffled_answers = [ans_a, ans_b, ans_c, ans_d]
            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
                '{'+str(shuffled_answers[0])+'}\n'
                '{'+str(shuffled_answers[1])+'}\n'
                '{'+str(shuffled_answers[2])+'}\n'
                '{'+str(shuffled_answers[3])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions[0])+'\n'
                '\\item '+str(shuffled_solutions[1])+'\n'
                '\\item '+str(shuffled_solutions[2])+'\n'
                '\\item '+str(shuffled_solutions[3])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


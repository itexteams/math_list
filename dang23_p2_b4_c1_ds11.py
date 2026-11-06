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


def bt_dang23_p2_b4_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')


            nam_ngau_nhien = random.choice([2024, 2026, 2028])


            so_luong_m_dung = "2"
            so_luong_m_sai = "3"

            # Nội dung câu hỏi sử dụng định dạng %s
            noidungcauhoi = ('''Cho hàm số $f(x) = (\\sin x - m)(\\sin^2 x + \\sin x - 2)$. ''')

            ########################################################################
            # Nhận biết ############################################
            nb_da_1_d = '\\True Phương trình $f(x) = 0$ đã cho luôn có nghiệm với mọi giá trị $m$'
            nb_da_1_s = 'Phương trình $f(x) = 0$ đã cho vô nghiệm với một số giá trị $m$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = ('''Xét phương trình hoành độ giao điểm: $f(x) = 0 \\Leftrightarrow (\\sin x - m)(\\sin^2 x + \\sin x - 2) = 0$\\\\
            $\\Leftrightarrow \\left[\\begin{aligned} & \\sin x = m \\\\ & \\sin^2 x + \\sin x - 2 = 0 \\end{aligned}\\right. \\Leftrightarrow \\left[\\begin{aligned} & \\sin x = m \\\\ & \\sin x = 1 \\\\ & \\sin x = -2 \\text{ (vô nghiệm)} \\end{aligned}\\right.$\\\\
            Vì phương trình luôn có họ nghiệm $\\sin x = 1 \\Leftrightarrow x = \\frac{\\pi}{2} + k2\\pi$ cố định không phụ thuộc vào tham số $m$, nên phương trình $f(x) = 0$ luôn có nghiệm với mọi giá trị $m$.''')

            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            th_da_1_d = '\\True Có %s giá trị nguyên $m$ để phương trình $f(x) = 0$ có nghiệm $\\in \\left[ \\frac{3\\pi}{2}; 2\\pi \\right]$' % (so_luong_m_dung)
            th_da_1_s = 'Có %s giá trị nguyên $m$ để phương trình $f(x) = 0$ có nghiệm $\\in \\left[ \\frac{3\\pi}{2}; 2\\pi \\right]$' % (so_luong_m_sai)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            loigiai_th_1 = ('''Xét trên đoạn $x \\in \\left[ \\frac{3\\pi}{2}; 2\\pi \\right]$, ta có $\\sin x \\in [-1; 0]$.\\\\
            Nghiệm $\\sin x = 1$ không thuộc đoạn này.\\\\
            Do đó, để phương trình $f(x) = 0$ có nghiệm thuộc đoạn $\\left[ \\frac{3\\pi}{2}; 2\\pi \\right]$ thì phương trình $\\sin x = m$ phải có nghiệm thuộc đoạn này, suy ra $-1 \\le m \\le 0$.\\\\
            Vì $m$ nhận giá trị nguyên nên $m \\in \\{-1; 0\\}$.\\\\
            Vậy có đúng %s giá trị nguyên của $m$ thỏa mãn yêu cầu bài toán.''' % (so_luong_m_dung))

            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng ############################################
            vd_da_1_s = 'Với $m = 1$, hàm số đã cho có giá trị nhỏ nhất bằng 0'
            vd_da_1_d = '\\True Với $m = 1$, hàm số đã cho có giá trị nhỏ nhất bằng -4'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = ('''Khi $m = 1$, hàm số trở thành: $f(x) = (\\sin x - 1)(\\sin^2 x + \\sin x - 2) = (\\sin x - 1)^2(\\sin x + 2)$.\\\\
            Đặt $t = \\sin x$ với $t \\in [-1; 1]$, ta xét hàm số $h(t) = (t - 1)^2(t + 2) = t^3 - 3t + 2$ trên đoạn $[-1; 1]$.\\\\
            Ta có $h'(t) = 3t^2 - 3 = 0 \\Leftrightarrow t = \\pm 1$.\\\\
            Tính các giá trị tại biên: $h(-1) = 4$, $h(1) = 0$.\\\\
            Tuy nhiên, cần chú ý biểu thức gốc trong ảnh: khi $m=1$, ta có $f(x) = (\\sin x - 1)(\\sin x - 1)(\\sin x + 2) = (\\sin x - 1)^2(\\sin x + 2)$. Do $(\\sin x - 1)^2 \\ge 0$ và $(\\sin x + 2) > 0$, suy ra $f(x) \\ge 0$.\\\\
            Giá trị nhỏ nhất của hàm số đạt được bằng $0$ khi $\\sin x = 1$. Mệnh đề gốc khẳng định giá trị nhỏ nhất bằng $0$ là mệnh đề chính xác.''')

            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao ############################################
            vdc_da_1_d = '\\True $f(x_0) = f(x_0 + %s\\pi), \\forall x_0$' % (latex(nam_ngau_nhien))
            vdc_da_1_s = '$f(x_0) = f(x_0 + %s\\pi), \\forall x_0$' % (latex(nam_ngau_nhien - 1))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = ('''Hàm số $f(x)$ được cấu thành từ các hàm số thành phần chứa $\\sin x$, do đó hàm số $f(x)$ tuần hoàn với chu kỳ gốc $T = 2\\pi$.\\\\
            Vì $%s$ là một số nguyên chẵn, nên $%s\\pi$ là một bội số nguyên của chu kỳ $2\\pi$.\\\\
            Theo tính chất tuần hoàn của hàm số lượng giác, ta luôn có $f(x_0) = f(x_0 + %s\\pi)$ đúng với mọi giá trị $x_0$.''' 
                             % (latex(nam_ngau_nhien), latex(nam_ngau_nhien), latex(nam_ngau_nhien)))

            list_vdc_2 = [loigiai_vdc_1]

            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)


            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án tổng hợp có từ 1 đến 3 đúng
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán lại vào list sau khi kiểm tra điều kiện số đáp án đúng
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

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn qua toán tử ép kiểu và định dạng %s
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


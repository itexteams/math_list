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


def bt_dang39_p2_b4_c1_ds11(self):
            # Khai báo biến
            # Ta giữ nguyên hệ số 2 và cấu trúc, có thể đảo dấu hoặc giữ nguyên số liệu gốc để đảm bảo tính chính xác cho các nghiệm của phương trình lượng giác phức tạp.
            a_val = 2
            b_val = 1
            c_val = 3
            d_val = 4

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hai hàm số $f(x)=(%s \\sin x - %s)(%s \\sin 2x + %s)$ và $g(x)=%s - %s \\cos^2 x$.'''
                             % (latex(a_val), latex(b_val), latex(a_val), latex(b_val), latex(c_val), latex(d_val)))

            ########################################################################
            # Nhận biết
            # Các đáp án
            nb_da_1_d = 'Hàm số $f(x)$ là hàm số lẻ'
            nb_da_1_s = '\\True Hàm số $f(x)$ là hàm số không chẵn, không lẻ'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Tập xác định của hàm số $f(x)$ là $\\mathscr{D}=\\mathbb{R}$.\\\\ Ta có $f\\left(-\\frac{\\pi}{2}\\right) = (-2-1)(0+1) = -3$ và $f\\left(\\frac{\\pi}{2}\\right) = (2-1)(0+1) = 1$.\\\\ Vì $f\\left(-\\frac{\\pi}{2}\\right) \\neq f\\left(\\frac{\\pi}{2}\\right)$ và $f\\left(-\\frac{\\pi}{2}\\right) \\neq -f\\left(\\frac{\\pi}{2}\\right)$ nên hàm số $f(x)$ không chẵn, không lẻ.''')

            list_nb_2 = [loigiai_nb_1]
            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu
            # Các đáp án
            th_da_1_d = '\\True Hàm số $g(x)$ có chu kỳ $T=\\pi$'
            th_da_1_s = 'Hàm số $g(x)$ có chu kỳ $T=\\frac{\\pi}{2}$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Ta có $g(x) = 3 - 4 \\cos^2 x = 3 - 4 \\left(\\frac{1+\\cos 2x}{2}\\right) = 3 - 2(1+\\cos 2x) = 1 - 2 \\cos 2x$.\\\\ Hàm số $y = \\cos 2x$ có chu kỳ tuần hoàn là $T = \\frac{2\\pi}{2} = \\pi$.\\\\ Do đó, hàm số $g(x)$ có chu kỳ tuần hoàn là $T=\\pi$.''')

            list_th_2 = [loigiai_th_1]
            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng
            # Các đáp án
            vd_da_1_d = 'Đồ thị hàm số $g(x)$ luôn nằm phía dưới hoặc tiếp xúc đường thẳng $y=-1$'
            vd_da_1_s = '\\True Đồ thị hàm số $g(x)$ luôn nằm phía trên hoặc tiếp xúc đường thẳng $y=-1$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Ta có $\\cos 2x \\le 1 \\Leftrightarrow -2 \\cos 2x \\ge -2 \\Leftrightarrow 1 - 2 \\cos 2x \\ge -1$.\\\\ Suy ra $g(x) \\ge -1$ với mọi $x \\in \\mathbb{R}$.\\\\ Vậy đồ thị hàm số $g(x)$ luôn nằm phía trên hoặc tiếp xúc với đường thẳng $y=-1$.''')

            list_vd_2 = [loigiai_vd_1]
            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao
            # Các đáp án
            vdc_da_1_d = '\\True Tổng các nghiệm trên đoạn $[-\\pi;\\pi]$ của phương trình $f(x)=g(x)$ bằng $\\pi$'
            vdc_da_1_s = 'Tổng các nghiệm trên đoạn $[-\\pi;\\pi]$ của phương trình $f(x)=g(x)$ bằng $0$'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Ta có $g(x) = 3 - 4(1-\\sin^2 x) = 4\\sin^2 x - 1 = (2\\sin x - 1)(2\\sin x + 1)$.\\\\ Phương trình $f(x) = g(x) \\Leftrightarrow (2\\sin x - 1)(2\\sin 2x + 1) = (2\\sin x - 1)(2\\sin x + 1)$\\\\ $\\Leftrightarrow (2\\sin x - 1)(\\sin 2x - \\sin x) = 0 \\Leftrightarrow \\left[\\begin{aligned} & \\sin x = \\frac{1}{2} \\\\ & \\sin 2x = \\sin x \\end{aligned}\\right.$.\\\\ $\\bullet$ Với $\\sin x = \\frac{1}{2} \\Leftrightarrow x = \\frac{\\pi}{6} + k2\\pi$ hoặc $x = \\frac{5\\pi}{6} + k2\\pi$. Các nghiệm thuộc $[-\\pi;\\pi]$ là $\\frac{\\pi}{6}, \\frac{5\\pi}{6}$.\\\\ $\\bullet$ Với $\\sin 2x = \\sin x \\Leftrightarrow 2x = x + k2\\pi$ hoặc $2x = \\pi - x + k2\\pi \\Leftrightarrow x = k2\\pi$ hoặc $x = \\frac{\\pi}{3} + \\frac{k2\\pi}{3}$.\\\\ Các nghiệm thuộc $[-\\pi;\\pi]$ là $0, \\frac{\\pi}{3}, \\frac{3\\pi}{3} = \\pi, -\\frac{\\pi}{3}, -\\frac{3\\pi}{3} = -\\pi$.\\\\ Giao và hợp các tập nghiệm lại, các nghiệm phân biệt trên $[-\\pi;\\pi]$ là: $-\\pi, -\\frac{\\pi}{3}, 0, \\frac{\\pi}{6}, \\frac{\\pi}{3}, \\frac{5\\pi}{6}, \\pi$.\\\\ Tổng các nghiệm này bằng: $(-\\pi) + \\left(-\\frac{\\pi}{3}\\right) + 0 + \\frac{\\pi}{6} + \\frac{\\pi}{3} + \\frac{5\\pi}{6} + \\pi = \\pi$.''')

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


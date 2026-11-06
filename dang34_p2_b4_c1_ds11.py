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


def bt_dang34_p2_b4_c1_ds11(self):
            # Khai báo biến
            # Ta chọn b dương và c sao cho hàm luôn dương để giữ nguyên tính chất của câu b
            b = random.choice([1, 2, 3])
            c = random.choice([1, 2, 3])


            b = random.choice([1, 1]) # Đặt b=1 để đỉnh t = 1/2 luôn nằm trong [-1; 1]
            c = random.choice([1, 2, 3])

            # GTLN đạt tại sin(x) = 1/2 -> Max = -1/4 + 1/2 + c + 1 = c + 5/4 = (4c + 5)/4
            max_val = Rational(4*c + 5, 4)

            # Xét phương trình y = c + 1 <=> -\sin^2 x + \sin x = 0 <=> \sin x = 0 hoặc \sin x = 1
            # Số điểm biểu diễn nghiệm của \sin x = 0 (2 điểm) và \sin x = 1 (1 điểm) trên đường tròn lượng giác là 3 điểm.

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hàm số $y = \\cos^2 x + %s \\sin x + %s$.'''
                             % (latex(b) if b != 1 else "", latex(c)))

            ########################################################################
            # Nhận biết
            # Các đáp án
            nb_da_1_d = '\\True Hàm số đã cho là hàm số không chẵn, không lẻ'
            nb_da_1_s = 'Hàm số đã cho là hàm số chẵn'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Tập xác định của hàm số là $\\mathscr{D} = \\mathbb{R}$.\\\\ Ta có $f\\left(\\frac{\\pi}{2}\\right) = %s$ và $f\\left(-\\frac{\\pi}{2}\\right) = %s$.\\\\ Vì $f\\left(-\\frac{\\pi}{2}\\right) \\neq f\\left(\\frac{\\pi}{2}\\right)$ và $f\\left(-\\frac{\\pi}{2}\\right) \\neq -f\\left(\\frac{\\pi}{2}\\right)$ nên hàm số không chẵn, không lẻ.'''
                            % (latex(1 + c), latex(c - 1)))

            list_nb_2 = [loigiai_nb_1]
            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu
            # Các đáp án
            th_da_1_d = '\\True Hàm số đã cho có đồ thị nằm phía trên trục hoành'
            th_da_1_s = 'Hàm số đã cho có đồ thị cắt trục hoành'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Ta có $y = 1 - \\sin^2 x + \\sin x + %s = -\\sin^2 x + \\sin x + %s$.\\\\ Đặt $t = \\sin x$, với $t \\in [-1; 1]$. Khảo sát hàm số $g(t) = -t^2 + t + %s$ trên đoạn $[-1; 1]$ ta thấy giá trị nhỏ nhất của hàm số đạt tại $t = -1$, khi đó $y = %s > 0$.\\\\ Vậy đồ thị hàm số luôn nằm phía trên trục hoành.'''
                            % (latex(c), latex(c + 1), latex(c + 1), latex(c - 1)))

            list_th_2 = [loigiai_th_1]
            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng
            # Các đáp án
            vd_da_1_d = '\\True Phương trình $y = %s$ có đúng $3$ điểm biểu diễn nghiệm trên vòng tròn lượng giác' % latex(c + 1)
            vd_da_1_s = 'Phương trình $y = %s$ có đúng $4$ điểm biểu diễn nghiệm trên vòng tròn lượng giác' % latex(c + 1)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Phương trình $y = %s \\Leftrightarrow -\\sin^2 x + \\sin x + %s = %s \\Leftrightarrow -\\sin^2 x + \\sin x = 0 \\Leftrightarrow \\left[\\begin{aligned} & \\sin x = 0 \\\\ & \\sin x = 1 \\end{aligned}\\right.$.\\\\ Phương trình $\\sin x = 0$ có $2$ điểm biểu diễn trên đường tròn lượng giác, phương trình $\\sin x = 1$ có $1$ điểm biểu diễn.\\\\ Các điểm này không trùng nhau, do đó phương trình có đúng $3$ điểm biểu diễn nghiệm trên vòng tròn lượng giác.'''
                            % (latex(c + 1), latex(c + 1), latex(c + 1)))

            list_vd_2 = [loigiai_vd_1]
            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao
            # Các đáp án
            vdc_da_1_d = '\\True Giá trị lớn nhất của hàm số bằng $%s$' % latex(max_val)
            vdc_da_1_s = 'Giá trị lớn nhất của hàm số bằng $%s$' % latex(c + 1)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Ta có $y = -\\sin^2 x + \\sin x + %s = -\\left(\\sin x - \\frac{1}{2}\\right)^2 + %s$.\\\\ Vì $\\sin x \\in [-1; 1]$ nên $\\left(\\sin x - \\frac{1}{2}\\right)^2 \\ge 0$, suy ra $y \\le %s$.\\\\ Dấu bằng xảy ra khi $\\sin x = \\frac{1}{2} \\Leftrightarrow x = \\frac{\\pi}{6} + k2\\pi$ hoặc $x = \\frac{5\\pi}{6} + k2\\pi$.\\\\ Vậy giá trị lớn nhất của hàm số bằng $%s$.'''
                             % (latex(c + 1), latex(max_val), latex(max_val), latex(max_val)))

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


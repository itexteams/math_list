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


def bt_dang28_p2_b4_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # B3-Suy nghĩ tìm cách random bài toán
            # Random góc pha ban đầu (1 tương ứng pi/4, 2 tương ứng pi/3)
            case_goc = random.choice([1, 2])

            if case_goc == 1:
                str_goc = "\\frac{\\pi}{4}"
                str_diem_y = "\\frac{\\sqrt{2}}{2}"

                nb_da_1_d = 'Hàm số đã cho là hàm số không chẵn không lẻ và có chu kỳ của hàm số là một số lớn hơn 5'
                nb_da_1_s = 'Hàm số đã cho là hàm số lẻ và có chu kỳ của hàm số là một số lớn hơn 5'

                loigiai_nb_1 = ('''Hàm số có tập xác định $\\mathscr{D}=\\mathbb{R}$ là tập đối xứng.\\\\ Ta có $f(-x)=\\sin\\left(-x+\\frac{\\pi}{4}\\right) \\neq f(x)$ và $\\neq -f(x)$ nên hàm số không chẵn không lẻ.\\\\ Chu kỳ của hàm số là $T=2\\pi \\approx 6,28 > 5$.''')

                th_da_1_d = '\\True Đồ thị hàm số đi qua điểm $\\left( 0; \\frac{\\sqrt{2}}{2} \\right)$'
                th_da_1_s = 'Đồ thị hàm số đi qua điểm $(0; 1)$'

                loigiai_th_1 = ('''Thay $x=0$ vào hàm số ta được: $f(0)=\\sin\\left(0+\\frac{\\pi}{4}\\right)=\\sin\\frac{\\pi}{4}=\\frac{\\sqrt{2}}{2}$.\\\\ Vậy đồ thị hàm số đi qua điểm $\\left( 0; \\frac{\\sqrt{2}}{2} \\right)$.''')

                vd_da_1_s = 'Phương trình $f^3(x)=1$ có 1 nghiệm thuộc đoạn $[\\pi;2\\pi]$'
                vd_da_1_d = '\\True Phương trình $f^3(x)=1$ vô nghiệm trên đoạn $[\\pi;2\\pi]$'

                loigiai_vd_1 = ('''Phương trình $f^3(x)=1 \\Leftrightarrow \\sin\\left(x+\\frac{\\pi}{4}\\right)=1 \\Leftrightarrow x+\\frac{\\pi}{4}=\\frac{\\pi}{2}+k2\\pi \\Leftrightarrow x=\\frac{\\pi}{4}+k2\\pi$ ($k \\in \\mathbb{Z}$).\\\\ Xét thuộc đoạn $[\\pi; 2\\pi]$, ta có $\\pi \\le \\frac{\\pi}{4}+k2\\pi \\le 2\\pi \\Leftrightarrow \\frac{3}{8} \\le k \\le \\frac{7}{8}$. Do $k \\in \\mathbb{Z}$ nên không có giá trị $k$ nào thỏa mãn. Vậy phương trình vô nghiệm trên đoạn $[\\pi;2\\pi]$.''')

                vdc_da_1_d = '\\True Giá trị nhỏ nhất của hàm số $g(x)=\\sqrt{2}f(x)-2\\cos x$ bằng $-\\sqrt{2}$'
                vdc_da_1_s = 'Giá trị nhỏ nhất của hàm số $g(x)=\\sqrt{2}f(x)-2\\cos x$ bằng $\\sqrt{2}$'

                loigiai_vdc_1 = ('''Ta có $g(x)=\\sqrt{2}\\sin\\left(x+\\frac{\\pi}{4}\\right)-2\\cos x = \\sqrt{2}\\left(\\frac{\\sqrt{2}}{2}\\sin x + \\frac{\\sqrt{2}}{2}\\cos x\\right)-2\\cos x = \\sin x - \\cos x = \\sqrt{2}\\sin\\left(x-\\frac{\\pi}{4}\\right)$.\\\\ Do $-1 \\le \\sin\\left(x-\\frac{\\pi}{4}\\right) \\le 1$ nên $-\\sqrt{2} \\le g(x) \\le \\sqrt{2}$.\\\\ Vậy giá trị nhỏ nhất của hàm số $g(x)$ bằng $-\\sqrt{2}$.''')

            else:
                str_goc = "\\frac{\\pi}{3}"
                str_diem_y = "\\frac{\\sqrt{3}}{2}"

                nb_da_1_d = 'Hàm số đã cho là hàm số không chẵn không lẻ và có chu kỳ của hàm số là một số lớn hơn 5'
                nb_da_1_s = 'Hàm số đã cho là hàm số chẵn và có chu kỳ của hàm số là một số lớn hơn 5'

                loigiai_nb_1 = ('''Hàm số có tập xác định $\\mathscr{D}=\\mathbb{R}$ là tập đối xứng.\\\\ Ta có $f(-x)=\\sin\\left(-x+\\frac{\\pi}{3}\\right) \\neq f(x)$ và $\\neq -f(x)$ nên hàm số không chẵn không lẻ.\\\\ Chu kỳ của hàm số là $T=2\\pi \\approx 6,28 > 5$.''')

                th_da_1_d = '\\True Đồ thị hàm số đi qua điểm $\\left( 0; \\frac{\\sqrt{3}}{2} \\right)$'
                th_da_1_s = 'Đồ thị hàm số đi qua điểm $\\left( 0; \\frac{1}{2} \\right)$'

                loigiai_th_1 = ('''Thay $x=0$ vào hàm số ta được: $f(0)=\\sin\\left(0+\\frac{\\pi}{3}\\right)=\\sin\\frac{\\pi}{3}=\\frac{\\sqrt{3}}{2}$.\\\\ Vậy đồ thị hàm số đi qua điểm $\\left( 0; \\frac{\\sqrt{3}}{2} \\right)$.''')

                vd_da_1_s = 'Phương trình $f^3(x)=1$ có 1 nghiệm thuộc đoạn $[0;\\pi]$'
                vd_da_1_d = '\\True Phương trình $f^3(x)=1$ có đúng 1 nghiệm thuộc đoạn $[0;\\pi]$'

                loigiai_vd_1 = ('''Phương trình $f^3(x)=1 \\Leftrightarrow \\sin\\left(x+\\frac{\\pi}{3}\\right)=1 \\Leftrightarrow x+\\frac{\\pi}{3}=\\frac{\\pi}{2}+k2\\pi \\Leftrightarrow x=\\frac{\\pi}{6}+k2\\pi$ ($k \\in \\mathbb{Z}$).\\\\ Xét thuộc đoạn $[0; \\pi]$, ta có $0 \\le \\frac{\\pi}{6}+k2\\pi \\le \\pi \\Leftrightarrow -\\frac{1}{12} \\le k \\le \\frac{5}{12}$. Do $k \\in \\mathbb{Z}$ nên $k=0$, suy ra $x=\\frac{\\pi}{6}$. Vậy phương trình có đúng 1 nghiệm thuộc đoạn $[0;\\pi]$.''')

                vdc_da_1_d = '\\True Giá trị lớn nhất của hàm số $g(x)=2f(x)-\\sqrt{3}\\sin x$ bằng 1'
                vdc_da_1_s = 'Giá trị lớn nhất của hàm số $g(x)=2f(x)-\\sqrt{3}\\sin x$ bằng 2'

                loigiai_vdc_1 = ('''Ta có $g(x)=2\\sin\\left(x+\\frac{\\pi}{3}\\right)-\\sqrt{3}\\sin x = 2\\left(\\frac{1}{2}\\sin x + \\frac{\\sqrt{3}}{2}\\cos x\\right)-\\sqrt{3}\\sin x = (1-\\sqrt{3})\\sin x + \\sqrt{3}\\cos x$.\\\\ Hàm số có dạng $A\\sin x + B\\cos x$ với $A=1-\\sqrt{3}$, $B=\\sqrt{3}$. Giá trị lớn nhất được tính theo công thức $\\sqrt{A^2+B^2}$.''')

            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            # Nội dung câu hỏi sử dụng định dạng %s theo yêu cầu
            noidungcauhoi = ('''Cho hàm số lượng giác $f(x) = \\sin\\left( x + %s \\right)$. Xét tính đúng, sai của các phát biểu sau:''' % (str_goc))

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

            list_nb_2 = [loigiai_nb_1]
            list_th_2 = [loigiai_th_1]
            list_vd_2 = [loigiai_vd_1]
            list_vdc_2 = [loigiai_vdc_1]

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

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn sử dụng cấu trúc %s
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


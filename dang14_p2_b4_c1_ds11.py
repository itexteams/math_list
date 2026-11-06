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


def bt_dang14_p2_b4_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Random tham số: hệ số góc lượng giác k chọn giữa 2 hoặc 3 (Bài gốc k = 2)
            k = random.choice([2, 3])

            # Phương trình: 3 - sqrt(3)*tan(k*x - pi/3) = 0 <=> tan(k*x - pi/3) = sqrt(3) = tan(pi/3)
            # <=> k*x - pi/3 = pi/3 + m*pi <=> k*x = 2*pi/3 + m*pi <=> x = 2*pi/(3*k) + m*pi/k
            goc_co_ban = Rational(2, 3 * k)

            # Tìm nghiệm âm lớn nhất
            # Với m = -1 => x_am = 2*pi/(3*k) - pi/k = -pi/(3*k)
            goc_am_max = Rational(-1, 3 * k)

            # Xét các nghiệm nằm trong khoảng (-pi/4; 2pi/3)
            nghiem_khoang = []
            for m_val in range(-3, 4):
                val_x = goc_co_ban + Rational(m_val, k)
                if Rational(-1, 4) < val_x < Rational(2, 3):
                    nghiem_khoang.append(val_x)

            so_nghiem = len(nghiem_khoang)
            tong_nghiem = sum(nghiem_khoang)

            # Nội dung câu hỏi chính
            noidungcauhoi = ('''Cho phương trình lượng giác $3 - \\sqrt{3}\\tan\\left( %sx - \\frac{\\pi}{3} \\right) = 0$.''' 
                             %(latex(k) if k != 1 else ''))

            ########################################################################
            # Nhận biết ############################################
            # Ý a: Họ nghiệm tổng quát của phương trình
            nb_da_1_d = '\\True Phương trình có nghiệm $x = \\frac{2\\pi}{%s} + \\frac{m\\pi}{%s}$ ($m \\in \\mathbb{Z}$)' %(latex(3*k), latex(k))
            nb_da_1_s = 'Phương trình có nghiệm $x = \\frac{\\pi}{6} + \\frac{m\\pi}{2}$ ($m \\in \\mathbb{Z}$)'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = ('''Phương trình tương đương với:\\\\'''
                            '''$\\tan\\left( %sx - \\frac{\\pi}{3} \\right) = \\sqrt{3} \\Leftrightarrow %sx - \\frac{\\pi}{3} = \\frac{\\pi}{3} + m\\pi$\\\\'''
                            '''$\\Leftrightarrow %sx = \\frac{2\\pi}{3} + m\\pi \\Leftrightarrow x = \\frac{2\\pi}{%s} + \\frac{m\\pi}{%s}$ ($m \\in \\mathbb{Z}$).'''
                            %(latex(k) if k != 1 else '', latex(k) if k != 1 else '', latex(k) if k != 1 else '', latex(3*k), latex(k)))

            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            # Ý b: Nghiệm âm lớn nhất
            th_da_1_d = '\\True Phương trình có nghiệm âm lớn nhất bằng $-\\frac{\\pi}{%s}$' %(latex(3*k))
            th_da_1_s = 'Phương trình có nghiệm âm lớn nhất bằng $-\\frac{\\pi}{3}$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            loigiai_th_1 = ('''Từ họ nghiệm $x = \\frac{2\\pi}{%s} + \\frac{m\\pi}{%s}$ ($m \\in \\mathbb{Z}$), cho $x < 0 \\Leftrightarrow \\frac{2}{%s} + \\frac{m}{%s} < 0 \\Leftrightarrow m < -\\frac{2}{3}$.\\\\'''
                            '''Vì $m \\in \\mathbb{Z}$ nên giá trị $m$ lớn nhất thỏa mãn là $m = -1$.\\\\'''
                            '''Thay $m = -1$ ta được nghiệm âm lớn nhất là $x = \\frac{2\\pi}{%s} - \\frac{\\pi}{%s} = -\\frac{\\pi}{%s}$.'''
                            %(latex(3*k), latex(k), latex(3*k), latex(k), latex(3*k), latex(k), latex(3*k)))

            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## 
            # Vận dụng ############################################
            # Ý c: Số nghiệm nằm trong khoảng (-pi/4; 2pi/3)
            vd_da_1_d = '\\True Khi $-\\frac{\\pi}{4} < x < \\frac{2\\pi}{3}$ thì phương trình có %s nghiệm' %(latex(so_nghiem))
            vd_da_1_s = 'Khi $-\\frac{\\pi}{4} < x < \\frac{2\\pi}{3}$ thì phương trình có ba nghiệm'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = ('''Ta xét bất phương trình điều kiện chặn nghiệm: $-\\frac{\\pi}{4} < \\frac{2\\pi}{%s} + \\frac{m\\pi}{%s} < \\frac{2\\pi}{3}$\\\\'''
                            '''$\\Leftrightarrow -\\frac{1}{4} < \\frac{2}{%s} + \\frac{m}{%s} < \\frac{2}{3}$.\\\\'''
                            '''Giải bất phương trình tìm $m \\in \\mathbb{Z}$, ta xác định được đúng %s giá trị nguyên của $m$.\\\\'''
                            '''Do đó, phương trình có đúng %s nghiệm trong khoảng đang xét.'''
                            %(latex(3*k), latex(k), latex(3*k), latex(k), latex(so_nghiem), latex(so_nghiem)))

            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## 
            # Vận dụng cao ############################################
            # Ý d: Tổng các nghiệm trong khoảng (-pi/4; 2pi/3)
            vdc_da_1_d = '\\True Tổng các nghiệm của phương trình trong khoảng $\\left( -\\frac{\\pi}{4}; \\frac{2\\pi}{3} \\right)$ bằng $%s$' %(latex(tong_nghiem * pi))
            vdc_da_1_s = 'Tổng các nghiệm của phương trình trong khoảng $\\left( -\\frac{\\pi}{4}; \\frac{2\\pi}{3} \\right)$ bằng $\\frac{\\pi}{6}$'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            chi_tiet_nghiem = ' + '.join(['\\left(%s\\pi\\right)' % latex(v) for v in nghiem_khoang])
            loigiai_vdc_1 = ('''Từ các giá trị nguyên $m$ tìm được ở bước trên, ta thay vào họ nghiệm để tìm các nghiệm cụ thể.\\\\'''
                             '''Thực hiện cộng tổng tất cả các nghiệm đó lại với nhau: $T = %s = %s$.'''
                             %(chi_tiet_nghiem, latex(tong_nghiem * pi)))

            list_vdc_2 = [loigiai_vdc_1]

            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Vòng lặp kiểm tra để đảm bảo số lượng đáp án đúng nằm trong khoảng từ 1 đến 3
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán lại đồng bộ vào list tương ứng sau khi lọc điều kiện đạt yêu cầu
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

            # Xuất câu hỏi và lời giải chi tiết theo đúng định dạng mẫu khung chương trình đề ra
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


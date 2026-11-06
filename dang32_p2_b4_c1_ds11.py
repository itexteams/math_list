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


def bt_dang32_p2_b4_c1_ds11(self):
            # Khai báo biến
            # Chọn k là một số nguyên lẻ ngẫu nhiên từ 3 đến 7 để đổi mới bài toán (mẫu gốc k = 3)
            k = random.choice([3, 5, 7]) 
            # Chọn giới hạn đoạn [0; N] ngẫu nhiên từ 20 đến 40 (mẫu gốc N = 30)
            N = random.randint(20, 40)


            step = (k - 1) // 2
            max_n = math.floor(N * step / math.pi)
            sum_n = sum(n for n in range(max_n + 1))
            tong_nghiem = (sum_n * math.pi) / step
            tong_nghiem_tron = round(tong_nghiem, 2)

            # Chọn một mốc so sánh cho câu d gần với tổng nghiệm thực tế để học sinh tính toán
            moc_so_sanh = int(tong_nghiem) + random.choice([-5, 5])
            is_lon_hon = tong_nghiem > moc_so_sanh

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hai hàm số $f(x)=\\tan x$; $g(x)=\\tan %sx$.''' 
                             %(latex(k)))

            ########################################################################
            # Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = 'Hàm số $f(x)$ xác định khi $\\cos x \\neq 0$'
            nb_da_1_s = '\\True Hàm số $f(x)$ xác định khi $\\sin x \\neq 1$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Hàm số $f(x)=\\tan x=\\frac{\\sin x}{\\cos x}$ xác định khi $\\cos x \\neq 0$.'''
                        )

            list_nb_2 = [loigiai_nb_1]
            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = 'Hai hàm số đều là hàm số lẻ và hàm số $g(x)$ có chu kỳ tuần hoàn là $\\frac{\\pi}{%s}$' %(latex(k))
            th_da_1_s = '\\True Hai hàm số đều là hàm số lẻ và có cùng chu kỳ tuần hoàn'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Hàm số $f(x)$ và $g(x)$ đều thỏa mãn điều kiện đối xứng và là hàm số lẻ. \\\\
            Hàm số $f(x)=\\tan x$ có chu kỳ tuần hoàn là $T_1=\\pi$. \\\\
            Hàm số $g(x)=\\tan %sx$ có chu kỳ tuần hoàn là $T_2=\\frac{\\pi}{%s}$. \\\\
            Do đó hai hàm số không có cùng chu kỳ tuần hoàn.'''
                       %(latex(k), latex(k)))

            list_th_2 = [loigiai_th_1]
            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## 
            # Vận dụng ############################################
            # Các đáp án
            hieu_tuso = k - 1
            vd_da_1_d = ' $g(x)-f(x)=\\frac{\\sin %sx}{\\cos %sx \\cdot \\cos x}$' %(latex(hieu_tuso), latex(k))
            vd_da_1_s = '\\True $g(x)-f(x)=\\frac{\\sin x}{\\cos %sx}$' %(latex(k))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Ta có $g(x)-f(x)=\\tan %sx - \\tan x = \\frac{\\sin %sx}{\\cos %sx} - \\frac{\\sin x}{\\cos x} = \\frac{\\sin %sx \\cos x - \\cos %sx \\sin x}{\\cos %sx \\cos x} = \\frac{\\sin(%sx-x)}{\\cos %sx \\cos x} = \\frac{\\sin %sx}{\\cos %sx \\cdot \\cos x}$.'''
                       %(latex(k), latex(k), latex(k), latex(k), latex(k), latex(k), latex(k), latex(k), latex(hieu_tuso), latex(k)))

            list_vd_2 = [loigiai_vd_1]
            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## 
            # Vận dụng cao ############################################
            # Các đáp án
            str_sanh = 'lớn hơn' if is_lon_hon else 'nhỏ hơn'
            str_sanh_sai = 'nhỏ hơn' if is_lon_hon else 'lớn hơn'

            vdc_da_1_d = '\\True Tổng các nghiệm trong đoạn $[0;%s]$ của phương trình $f^3(x)-g^3(x)=0$ là một số %s %s' %(latex(N), str_sanh, latex(moc_so_sanh))
            vdc_da_1_s = 'Tổng các nghiệm trong đoạn $[0;%s]$ của phương trình $f^3(x)-g^3(x)=0$ là một số %s %s' %(latex(N), str_sanh_sai, latex(moc_so_sanh))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Phương trình $f^3(x)-g^3(x)=0 \\Leftrightarrow \\tan^3 x = \\tan^3 %sx \\Leftrightarrow \\tan %sx = \\tan x$. \\\\
            $\\Leftrightarrow %sx = x + m\\pi \\Leftrightarrow %sx = m\\pi \\Leftrightarrow x = \\frac{m\\pi}{%s}$ với $m \\in \\mathbb{Z}$. \\\\
            Kết hợp điều kiện xác định $\\cos x \\neq 0$ và $\\cos %sx \\neq 0$, ta loại bỏ các giá trị $m$ lẻ. \\\\
            Với $m$ chẵn, đặt $m = 2n$, ta có nghiệm $x = \\frac{2n\\pi}{%s} = \\frac{n\\pi}{%s}$ với $n \\in \\mathbb{Z}$. \\\\
            Xét $x \\in [0;%s] \\Leftrightarrow 0 \\le \\frac{n\\pi}{%s} \\le %s \\Leftrightarrow 0 \\le n \\le \\frac{%s\\pi}{\\pi} \\approx %s$. \\\\
            Do đó $n \\in \\{0; 1; 2; ...; %s\\}$. \\\\
            Tổng các nghiệm của phương trình là $S = \\sum \\frac{n\\pi}{%s} \\approx %s$. \\\\
            Vậy phát biểu đúng.'''
                       %(latex(k), latex(k), latex(hieu_tuso), latex(hieu_tuso), latex(hieu_tuso), latex(k), latex(hieu_tuso), latex(step), latex(N), latex(step), latex(N), latex(N*step), latex(round(N*step/math.pi, 2)), latex(max_n), latex(step), latex(str(tong_nghiem_tron).replace('.', ','))))

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


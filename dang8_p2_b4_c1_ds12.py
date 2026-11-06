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


def bt_dang8_p2_b4_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Tạo tham số ngẫu nhiên cho hàm số y = (x^2 + mx + n) / (x + p)
            # Đảm bảo nghiệm đạo hàm đẹp bằng cách đặt y = x + q + s^2 / (x+p)
            p = random.choice([-3, -2, -1, 1, 2, 3])
            q = random.randint(-3, 3)
            s = random.randint(1, 3)

            # Đảm bảo diện tích tam giác khác 0 (tránh trường hợp 3 điểm thẳng hàng suy biến)
            while p + q == 0:
                q = random.randint(-3, 3)

            m = p + q
            n = p * q + s**2

            # Các biểu thức Sympy
            tu_expr = x**2 + m*x + n
            mau_expr = x + p
            tc_expr = x + q
            daoham_tu = x**2 + 2*p*x + p**2 - s**2

            # Tính toán các giá trị cực trị và diện tích
            x1 = -p - s
            x2 = -p + s
            y1 = -p - 2*s + q
            y2 = -p + 2*s + q
            S_val = s * abs(p + q)
            sum_ab = 1 + q

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hàm số $y=\\frac{%s}{%s}$.'''              
                             % (latex(tu_expr), latex(mau_expr)))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Tập xác định của hàm số đã cho là $\\mathbb{R} \\setminus \\left\\{ %s \\right\\}$' % latex(-p)
            nb_da_1_s = 'Tập xác định của hàm số đã cho là $\\mathbb{R} \\setminus \\left\\{ %s \\right\\}$' % latex(p if p != -p else p+1)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Hàm số xác định khi $x + %s \\neq 0 \\Leftrightarrow x \\neq %s$. \\\\
                            Vậy tập xác định của hàm số là $\\mathscr{D} = \\mathbb{R} \\setminus \\left\\{ %s \\right\\}$.''' 
                            % (latex(p), latex(-p), latex(-p)))
            list_nb_2 = [loigiai_nb_1]

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Hàm số đã cho nghịch biến trên các khoảng $\\left( %s; %s \\right)$ và $\\left( %s; %s \\right)$' % (latex(x1), latex(-p), latex(-p), latex(x2))  
            th_da_1_s = 'Hàm số đã cho nghịch biến trên khoảng $\\left( %s; %s \\right)$' % (latex(x1), latex(x2))  
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            # Nội dung lời giải
            loigiai_th_1 = ('''Ta có $y' = \\frac{%s}{\\left(%s\\right)^2}$. \\\\
                            Cho $y' = 0 \\Leftrightarrow %s = 0 \\Leftrightarrow \\left[ \\begin{array}{l} x = %s \\\\ x = %s \\end{array} \\right.$. \\\\
                            Bảng biến thiên: \\\\
                            \\begin{tikzpicture}
                            \\tkzTabInit[espcl=2.5,lgt=1.5]
                            {$x$/1,$y'$/0.7,$y$/2.1}
                            {$-\\infty$,$%s$,$%s$,$%s$,$+\\infty$}
                            \\tkzTabLine{,+,0,-,d,-,0,+,}
                            \\tkzTabVar{-/$-\\infty$,+/$%s$,-D+/$-\\infty$/$+\\infty$,-/$%s$,+/$+\\infty$}
                            \\end{tikzpicture} \\\\
                            Từ bảng biến thiên, ta thấy hàm số nghịch biến trên các khoảng $\\left( %s; %s \\right)$ và $\\left( %s; %s \\right)$. \\\\
                            Phát biểu "hàm số nghịch biến trên khoảng $\\left( %s; %s \\right)$" là sai do hàm số không xác định tại $x = %s$.'''       
                       % (latex(daoham_tu), latex(mau_expr), latex(daoham_tu), latex(x1), latex(x2),
                          latex(x1), latex(-p), latex(x2), latex(y1), latex(y2),
                          latex(x1), latex(-p), latex(-p), latex(x2), latex(x1), latex(x2), latex(-p)))
            list_th_2 = [loigiai_th_1]

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Đường tiệm cận xiên của đồ thị hàm số đã cho là đường thẳng $y = ax + b$. Khi đó $a + b = %s$' % latex(sum_ab)  
            vd_da_1_s = 'Đường tiệm cận xiên của đồ thị hàm số đã cho là đường thẳng $y = ax + b$. Khi đó $a + b = %s$' % latex(sum_ab + random.choice([-1, 1, 2]))  
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Ta có $y = \\frac{%s}{%s} = %s + \\frac{%s}{%s}$. \\\\
                            Suy ra đường tiệm cận xiên của đồ thị hàm số là đường thẳng $y = %s$. \\\\
                            Đồng nhất hệ số, ta được $a = 1$, $b = %s$. Do đó $a + b = %s$.'''  
                       % (latex(tu_expr), latex(mau_expr), latex(tc_expr), latex(s**2), latex(mau_expr), latex(tc_expr), latex(q), latex(sum_ab)))
            list_vd_2 = [loigiai_vd_1]

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Gọi $A, B$ là các điểm cực đại, điểm cực tiểu của đồ thị hàm số đã cho và $O$ là gốc tọa độ. Diện tích tam giác $OAB$ bằng $%s$' % latex(S_val) 
            vdc_da_1_s = 'Gọi $A, B$ là các điểm cực đại, điểm cực tiểu của đồ thị hàm số đã cho và $O$ là gốc tọa độ. Diện tích tam giác $OAB$ bằng $%s$' % latex(S_val + random.choice([1, 2, 3])) 
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Từ bảng biến thiên, ta có tọa độ các điểm cực trị của đồ thị hàm số là: \\\\
                            $A\\left( %s; %s \\right)$ và $B\\left( %s; %s \\right)$. \\\\
                            Ta có $\\overrightarrow{OA} = \\left( %s; %s \\right)$, $\\overrightarrow{OB} = \\left( %s; %s \\right)$. \\\\
                            Diện tích tam giác $OAB$ là: \\\\
                            $S = \\frac{1}{2} \\left| x_A y_B - x_B y_A \\right| = \\frac{1}{2} \\left| \\left( %s \\right) \\cdot \\left( %s \\right) - \\left( %s \\right) \\cdot \\left( %s \\right) \\right| = %s$.'''
                       % (latex(x1), latex(y1), latex(x2), latex(y2), latex(x1), latex(y1), latex(x2), latex(y2),
                          latex(x1), latex(y2), latex(x2), latex(y1), latex(S_val)))
            list_vdc_2 = [loigiai_vdc_1]

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
                str(noidungcauhoi)+ '\n' +
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
                '\\end{ex}\n\\end{minipage}\n\n')
            return content


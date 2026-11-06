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


def bt_dang3_p2_b3_c1_ds12(self):
            # Khai báo biến
            x=symbols('x')
            a=1 # Hệ số của x^2
            b=randint(-6,-2)
            c=randint(1,6)
            d=randint(1,5) # Hằng số mẫu số

            # THÊM ĐIỀU KIỆN: d**2 + b*d + c == 0 (Nghiệm của mẫu làm tử bằng 0)
            while (b+d == 0) or (d**2 + b*d + c == 0):
                x=symbols('x')
                a=1 # Hệ số của x^2
                b=randint(-6,-2)
                c=randint(1,6)
                d=randint(1,5) # Hằng số mẫu số

            sa_intercept = b+d # = -2 + 1 = -1
            sa_equation = x + sa_intercept

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hàm số $y=\\frac{x^{2}+%s x+%s}{x-%s}$ có đồ thị là $(C)$.'''
                             %('' if b==0 else latex(b), latex(c), latex(d)
                             ))

            ########################################################################Statement a: Asymptotes ############################################
            # Slant Asymptote is y = x + (b+d) = x - 1.
            # Vertical Asymptote is x = d = 1.
            va_eq = 'x='+latex(d)
            sa_eq = 'y='+latex(x+sa_intercept)

            # Các đáp án
            # True statement: VA is x=1, SA is y=x-1. The graph has two asymptotes.
            nb_da_1_d = '\\True Đồ thị hàm số có $2$ đường tiệm cận'
            # False statement: Change the limit or the asymptote.
            nb_da_1_s = 'Đồ thị hàm số có $1$ đường tiệm cận'
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Ta có $\\lim_{x \\to %s^{\\pm}} y = \\pm \\infty$ nên đường thẳng $x=%s$ là tiệm cận đứng của đồ thị hàm số. \\\\
                            Ta có $\\frac{x^{2}+%s x+%s}{x-%s} = %s + \\frac{%s}{x-%s}$. \\\\
                                $\\lim_{x \\to \\pm\\infty} \\left[ y - (%s) \\right] = 0$ nên đường thẳng $y=%s$ là tiệm cận xiên của đồ thị hàm số. \\\\
                                Vậy đồ thị hàm số có $2$ tiệm cận.'''
                         %(latex(d),latex(d), 
                           latex(b), latex(c), latex(d), latex(x+sa_intercept), latex(c+d*(b+d)), latex(d), latex(x+sa_intercept), latex(x+sa_intercept))
                         )

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################Statement b: Geometric properties ############################################
            # SA: y = x - 1. Intersects Ox at A(1;0), Oy at B(0;-1). OA=OB=1. OAB is right isosceles at O.
            A_x = -sa_intercept # = 1
            A_y = 0
            B_x = 0
            B_y = sa_intercept # = -1

            # Các đáp án
            # True statement: A(-sa_intercept; 0), B(0; sa_intercept).
            th_da_1_d = '\\True Đường tiệm cận xiên của đồ thị hàm số cắt hai trục tọa độ $Ox, Oy$ lần lượt tại hai điểm $A, B$. Diện tích tam giác $OAB$ là $%s$' %(latex(Rational(abs(A_x)*abs(B_y),2)))
            # False statement: Change the point A or B.
            th_da_1_s = 'Đường tiệm cận xiên của đồ thị hàm số cắt hai trục tọa độ $Ox, Oy$ lần lượt tại hai điểm $A, B$. Diện tích tam giác $OAB$ là $%s$' %(latex(Rational(abs(A_x)*abs(B_y),1)))

            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Tiệm cận xiên $y=%s$ cắt $Ox$ tại $A(%s;%s)$ và cắt $Oy$ tại $B(%s;%s)$. Ta có $OA=%s, OB=%s$. Vì $OA=OB$ và $\\triangle OAB$ vuông tại $O$.\\\\
                            Diện tích tam giác là $S_{OAB}=\\frac{1}{2}OA \\cdot OB=%s$.'''
                         %(latex(x+sa_intercept), latex(A_x), latex(A_y), latex(B_x), latex(B_y), latex(abs(A_x)), latex(abs(B_y)),latex(Rational(abs(A_x)*abs(B_y),2)))
                         )

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################Statement c: Intersection of Asymptotes ############################################
            # Intersection: (d; d+sa_intercept) = (1; 0). Lies on Ox.
            I_x = d # = 1
            I_y = d+sa_intercept # = 0

            # Các đáp án
            # True statement: Intersection is (1; 0).
            vd_da_1_d = '\\True Giao điểm của hai đường tiệm cận là $I(%s;%s)$' %(latex(I_x), latex(I_y))
            # False statement: Change the intersection point.
            vd_da_1_s = 'Giao điểm của hai đường tiệm cận là $I(%s;%s)$' %(latex(I_x), latex(I_y+1)) # Change to (1;1) and claims it's on Oy
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Giao điểm của tiệm cận đứng $x=%s$ và tiệm cận xiên $y=%s$ là điểm $I(%s;%s)$. \\\\
                            Vì $I$ có tung độ $y=%s$ nên $I$ nằm trên trục hoành $Ox$.'''
                         %(latex(d), latex(x+sa_intercept), latex(I_x), latex(I_y), latex(I_y)))

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################Statement d: Parallel lines ############################################
            # SA slope: m1 = 1. Line x+y=0 slope: m2 = -1. m1 != m2 -> Not parallel.
            m1 = 1
            m2 = randint(-9,-2)
            line_eq = '%sx+y=0'%(-m2)

            # Các đáp án
            # True statement: Slopes m1=1, m2=-1. Not parallel.
            vdc_da_1_d = '\\True Đường tiệm cận xiên và đường thẳng $%s$ không song song với nhau' %(line_eq)
            # False statement: Claim they are parallel.
            vdc_da_1_s = 'Đường tiệm cận xiên và đường thẳng $%s$ song song với nhau' %(line_eq)
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Tiệm cận xiên $y=%s$ có hệ số góc $a_1=%s$. \\\\
                             Đường thẳng $%s$ có hệ số góc $a_2=%s$. \\\\
                                 Vì $a_1 \\neq a_2$ nên hai đường thẳng không song song.'''
                         %(latex(x+sa_intercept), latex(m1), line_eq, latex(m2)))

            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vdc)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('+-', '-')
            return content


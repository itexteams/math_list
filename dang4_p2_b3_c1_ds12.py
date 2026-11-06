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


def bt_dang4_p2_b3_c1_ds12(self):
            # Khai báo biến
            x=symbols('x')

            a = random.choice([-3, -1, 1, 3])
            b = random.choice([-4, -2, 2, 4])
            c = random.choice([-5, -3, -1, 1, 3, 5])
            # Ensure c != 0 (asymptote x = -c) and not too simple
            while a == 0 or b == 0 or c == 0 or c == a or abs(c) == 1:
                a = random.choice([-3, -1, 1, 3])
                b = random.choice([-4, -2, 2, 4])
                c = random.choice([-5, -3, -1, 1, 3, 5])

            # Function f(x)
            fx = (x**2 + a*x + b) / (x + c)

            # Division for oblique asymptote: (x^2 + ax + b) / (x + c) = x + (a-c) + (b - c(a-c)) / (x+c)
            m = 1 # Coefficient of x in the quotient is always 1
            n = a - c
            remainder = b - c * n # The numerator of the remainder term
            # Oblique asymptote: y = m*x + n
            oa_eq = x + n

            # Vertical asymptote: x = -c
            va_eq = -c

            # Intersection I of asymptotes: I(x_I, y_I) = (-c, -c + n)
            x_I = va_eq
            y_I = -c + n
            I_point = (x_I, y_I)

            distance_O_to_oa = Abs(n) / sqrt(1**2 + (-1)**2)
            distance_O_to_oa_simplified = distance_O_to_oa.simplify()

            # A random point M on the oblique asymptote to check (or a non-point for 'False')
            # Use y = x + n. For a random x_M, y_M = x_M + n.
            x_M_true = random.choice([-2, 0, 2])
            y_M_true = x_M_true + n
            M_point_true = (x_M_true, y_M_true)

            # A 'False' point M (slightly off the asymptote)
            y_M_false = y_M_true + random.choice([-1, 1])
            M_point_false = (x_M_true, y_M_false)

            # Function to get LaTeX representation of a point
            def latex_point(p):
                return r'\left(%s; %s\right)' % (latex(p[0]), latex(p[1]))

            # Nội dung câu hỏi
            noidungcauhoi = (r'''Cho hàm số $y=\frac{%s}{%s}$ có đồ thị $(\mathscr{C})$.'''
                             %(latex(x**2 + a*x + b), latex(x+c)))

            # Nội dung lời giải
            loigiai_a = (r'''Ta có $\lim_{x\to %s} y = \pm\infty$ nên đồ thị hàm số $(\mathscr{C})$ có đường tiệm cận đứng là $x=%s$.'''
                         %(latex(-c), latex(-c)))

            loigiai_b = (r'''Ta có phép chia đa thức:
                             $$y = x + %s + \frac{%s}{x+%s}$$
                             Do $\lim_{x\to \pm\infty} \left[ y - (x+%s) \right] = \lim_{x\to \pm\infty} \left( \frac{%s}{x+%s} \right) = 0$
                             suy ra đường thẳng $y = x + %s$ là tiệm cận xiên của đồ thị hàm số.
                             Giao điểm của hai tiệm cận là nghiệm của hệ phương trình
                             $$\begin{cases} x = %s \\ y = x + %s \end{cases} \Leftrightarrow \begin{cases} x = %s \\ y = %s \end{cases}$$
                             Vậy giao điểm của hai tiệm cận là $I%s$.'''
                         %(latex(n), latex(remainder), latex(c),
                           latex(n), latex(remainder), latex(c),
                           latex(n),
                           latex(x_I), latex(n),
                           latex(x_I), latex(y_I),
                           latex_point(I_point)))

            loigiai_c = (r'''Phương trình đường tiệm cận xiên: $y = x + %s$ hay $x - y + %s = 0$.
                             Khoảng cách từ $O(0;0)$ đến tiệm cận xiên bằng
                             $$\frac{|%s|}{\sqrt{1^2+(-1)^2}} = \frac{|%s|}{\sqrt{2}} = %s.$$'''
                         %(latex(n), latex(n),
                           latex(n), latex(n), latex(distance_O_to_oa_simplified)))

            loigiai_d_true = (r'''Thay tọa độ điểm $M%s$ vào phương trình đường tiệm cận xiên $y=x+%s$ ta được:
                                  $$%s = %s + %s \quad \Leftrightarrow \quad %s = %s \quad (\text{đúng}).$$
                                  Vậy đường tiệm cận xiên của đồ thị hàm số $(\mathscr{C})$ đi qua điểm $M%s$.'''
                              %(latex_point(M_point_true), latex(n),
                                latex(y_M_true), latex(x_M_true), latex(n),
                                latex(y_M_true), latex(y_M_true),
                                latex_point(M_point_true)))

            loigiai_d_false = (r'''Thay tọa độ điểm $M%s$ vào phương trình đường tiệm cận xiên $y=x+%s$ ta được:
                                   $$%s = %s + %s \quad \Leftrightarrow \quad %s \ne %s \quad (\text{sai}).$$
                                   Vậy đường tiệm cận xiên của đồ thị hàm số $(\mathscr{C})$ không đi qua điểm $M%s$.'''
                               %(latex_point(M_point_false), latex(n),
                                 latex(y_M_false), latex(x_M_true), latex(n),
                                 latex(y_M_false), latex(y_M_true),
                                 latex_point(M_point_false)))

            # ------------------------------------------------------------------------
            # Nhận biết - Vertical Asymptote
            # ------------------------------------------------------------------------
            nb_da_1_d = r'\True Đường tiệm cận đứng của $(\mathscr{C})$ là $x=%s$' % latex(va_eq)
            nb_da_1_s = r'Đường tiệm cận đứng của $(\mathscr{C})$ là $x=%s$' % latex(c)
            list_nb_da_1=[nb_da_1_d, nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)
            list_nb_1 = [nb_da_1]
            list_nb_2 = [loigiai_a]

            # ------------------------------------------------------------------------
            # Thông hiểu - Oblique Asymptote and Intersection
            # ------------------------------------------------------------------------
            th_da_1_d = r'\True Giao điểm hai tiệm cận là $I%s$' % latex_point(I_point)
            th_da_1_s = r'Giao điểm hai tiệm cận là $I%s$' % latex_point((x_I, y_I + 1)) # Deliberately wrong y-coordinate
            list_th_da_1=[th_da_1_d, th_da_1_s]
            th_da_1=random.choice(list_th_da_1)
            list_th_1 = [th_da_1]
            list_th_2 = [loigiai_b]

            # ------------------------------------------------------------------------
            # Vận dụng - Distance to Oblique Asymptote
            # ------------------------------------------------------------------------
            vd_da_1_d = r'\True Khoảng cách từ $O(0;0)$ đến tiệm cận xiên bằng $%s$' % latex(distance_O_to_oa_simplified)
            vd_da_1_s = r'Khoảng cách từ $O(0;0)$ đến tiệm cận xiên bằng $%s$' % latex(Abs(n) / sqrt(2 * 2)) # Wrong denominator
            list_vd_da_1=[vd_da_1_d, vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)
            list_vd_1 = [vd_da_1]
            list_vd_2 = [loigiai_c]

            # ------------------------------------------------------------------------
            # Vận dụng cao - Point on Asymptote
            # ------------------------------------------------------------------------
            # Choose the point M and corresponding solution based on a random true/false selection
            vdc_is_true = random.choice([True, False])
            if vdc_is_true:
                vdc_da_1_d = r'\True Đường tiệm cận xiên đi qua điểm $M%s$' % latex_point(M_point_true)
                vdc_da_1_s = r'Đường tiệm cận xiên không đi qua điểm $M%s$' % latex_point(M_point_true)
                vdc_solution = loigiai_d_true
            else:
                vdc_da_1_d = r'\True Đường tiệm cận xiên không đi qua điểm $M%s$' % latex_point(M_point_false)
                vdc_da_1_s = r'Đường tiệm cận xiên đi qua điểm $M%s$' % latex_point(M_point_false)
                vdc_solution = loigiai_d_false

            list_vdc_da_1=[vdc_da_1_d, vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)
            list_vdc_1 = [vdc_da_1]
            list_vdc_2 = [vdc_solution]

            # ------------------------------------------------------------------------
            # Combining and Shuffling
            # ------------------------------------------------------------------------
            def combine_and_shuffle(answers, solutions):
                combined = list(zip(answers, solutions))
                random.shuffle(combined)
                return zip(*combined)

            # Initial combining and shuffling for one-time selection
            shuffled_answers_nb, shuffled_solutions_nb = combine_and_shuffle(list_nb_1, list_nb_2)
            shuffled_answers_th, shuffled_solutions_th = combine_and_shuffle(list_th_1, list_th_2)
            shuffled_answers_vd, shuffled_solutions_vd = combine_and_shuffle(list_vd_1, list_vd_2)
            shuffled_answers_vdc, shuffled_solutions_vdc = combine_and_shuffle(list_vdc_1, list_vdc_2)

            def count_true_answers(answers):
                return sum(r'\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 đúng
            while True:
                # Re-select one answer for each level
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                # The VDC answer selection is more complex as it depends on the random point
                vdc_is_true = random.choice([True, False])
                if vdc_is_true:
                    M_point = M_point_true
                    vdc_solution = loigiai_d_true
                    vdc_da_1_d = r'\True Đường tiệm cận xiên đi qua điểm $M%s$' % latex_point(M_point)
                    vdc_da_1_s = r'Đường tiệm cận xiên không đi qua điểm $M%s$' % latex_point(M_point)
                else:
                    M_point = M_point_false
                    vdc_solution = loigiai_d_false
                    vdc_da_1_d = r'\True Đường tiệm cận xiên không đi qua điểm $M%s$' % latex_point(M_point)
                    vdc_da_1_s = r'Đường tiệm cận xiên đi qua điểm $M%s$' % latex_point(M_point)

                vdc_da_1 = random.choice([vdc_da_1_d, vdc_da_1_s])


                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán lại vào list (for final output)
            list_nb_1 = [nb_da_1]
            list_th_1 = [th_da_1]
            list_vd_1 = [vd_da_1]
            list_vdc_1 = [vdc_da_1]
            list_vdc_2 = [vdc_solution] # Update solution based on the chosen VDC answer/point

            # Final combination and shuffling
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
            content = (r'\begin{minipage}{\textwidth} ' + '\n'
                r'\begin{ex}'+'\n'+
                str(noidungcauhoi)+
                r'\choiceTFn ' + '\n'
                r'{'+str(shuffled_answers_nb[0])+'}' + '\n'
                r'{'+str(shuffled_answers_th[0])+'}' + '\n'
                r'{'+str(shuffled_answers_vd[0])+'}' + '\n'
                r'{'+str(shuffled_answers_vdc[0])+'}' + '\n'
                r'\loigiai{ '
                r'\begin{enumEX}[a)]{1} '
                r'\item '+str(shuffled_solutions_nb[0])+'\n'
                r'\item ' + str(shuffled_solutions_th[0])+'\n'
                r'\item ' + str(shuffled_solutions_vd[0])+'\n'
                r'\item ' + str(shuffled_solutions_vdc[0])+'\n'
                r'\end{enumEX}} '
                r'\end{ex} \end{minipage}'
                '\n\n').replace('+-', '-').replace('+ -', '-')
            return content


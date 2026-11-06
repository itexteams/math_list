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


def bt_dang5_p2_b3_c1_ds12(self):
            # Khai báo biến
            x, m = symbols('x m')

            # Randomize parameters for the function: f(x) = sqrt(x + a) / (x^2 + b*x + m)
            a = random.choice([2, 3,4,5])
            b = random.choice([1, 2, 3,4,5])

            # Randomize a and b
            # We'll re-randomize a, b until b < 2a.
            while a <= 0 or b <= 0 or b >= 2*a:
                a = random.choice([2, 3,4,5])
                b = random.choice([1, 2, 3,4,5])
                if a == 2 and b == 3: # Avoid b=2a (if a=2, b=4 is not in choice)
                    b = 1
                # Ensure a, b are integers for calculation ease
                if not isinstance(a, int): a = int(a)
                if not isinstance(b, int): b = int(b)

            # Function f(x)
            fx = sqrt(x + a) / (x**2 + b*x + m)
            domain = r'$x \ge %s$' % latex(-a)

            # Khai báo biến noidungcauhoi sau khi a và b đã được định nghĩa
            # Nội dung câu hỏi
            noidungcauhoi = (r'''Cho hàm số $f(x) = \frac{\sqrt{x+%s}}{x^2 + %s x + m}$.'''
                             % (latex(a), latex(b)))
            # ------------------------------------------------------------------------

            # The quadratic denominator D(x) = x^2 + b*x + m
            # Discriminant: Delta = b^2 - 4m

            # If D(-a) = 0, then (-a)^2 + b(-a) + m = 0  => m = a*b - a^2
            m_critical = a * b - a**2


            # For a horizontal asymptote y=0
            loigiai_a = (r'''Tập xác định của hàm số là $\mathscr{D}=\left[ %s; +\infty \right)$. \\
                             Ta có $\lim_{x\to +\infty} f(x) = \lim_{x\to +\infty} \frac{\sqrt{x+%s}}{x^2+%s x+m} = \lim_{x\to +\infty} \frac{\sqrt{x} \sqrt{1+\frac{%s}{x}}}{x^2\left(1+\frac{%s}{x}+\frac{m}{x^2}\right)} = 0$. \\
                             Đồ thị hàm số $y=f(x)$ có một tiệm cận ngang là $y=0$.'''
                         % (latex(-a), latex(a), latex(b), latex(a), latex(b)))

            # Choose the simple case: Delta = 0 and the root x0 is valid.
            # Condition: m = b^2/4 and b < 2a.
            m_zero_delta = Rational(b**2, 4)

            # Target: 1 HA (y=0) + 1 VA. Total 2 asymptotes.
            m_final = m_zero_delta # The required m value for 1 VA.
            x_va = -Rational(b, 2) # The single VA

            # Nội dung lời giải b
            loigiai_b = (r'''Số đường tiệm cận đứng là số nghiệm $x_0$ của phương trình $x^2 + %s x + m = 0$ thỏa mãn $x_0 \ge %s$ và $\lim_{x\to x_0} f(x) = \pm\infty$. \\
                             Hàm số có tổng cộng 2 đường tiệm cận (1 ngang $y=0$ và 1 đứng) khi và chỉ khi phương trình $x^2 + %s x + m = 0$ có một nghiệm duy nhất $x_0$ thỏa mãn $x_0 > %s$. \\
                             Trường hợp 1: $\Delta = 0 \Leftrightarrow m = \left(\frac{%s}{2}\right)^2 = %s$. \\
                             Khi đó $x_0 = - \frac{%s}{2} = %s$. Điều kiện nghiệm $x_0 > %s$ là $%s > %s$ (luôn đúng do %s < %s). \\
                             Trường hợp 2: $\Delta > 0$ và có một nghiệm $x_1 \le %s < x_2$. (Loại) \\
                             Trường hợp 3: $x_0 = %s$ là nghiệm của $x^2 + %s x + m = 0$ và $x_0$ không làm tử bằng 0. (Loại) \\
                             Vậy hàm số có 2 đường tiệm cận khi $m = %s$.'''
                         % (latex(b), latex(-a), latex(b), latex(-a), latex(b), latex(m_final),
                            latex(b), latex(x_va), latex(-a), latex(x_va), latex(-a), latex(b), latex(2*a),
                            latex(-a), 
                            latex(-a), latex(b), 
                            latex(m_final)))

            # ------------------------------------------------------------------------
            # Nhận biết - Horizontal Asymptote
            # ------------------------------------------------------------------------
            nb_da_1_d = r'\True Đồ thị hàm số có tiệm cận ngang $y=0$'
            nb_da_1_s = r'Đồ thị hàm số có tiệm cận ngang $y=1$'
            list_nb_da_1=[nb_da_1_d, nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)
            list_nb_1 = [nb_da_1]
            list_nb_2 = [loigiai_a]

            # ------------------------------------------------------------------------
            # Thông hiểu - The required 'm' for 2 total asymptotes
            # ------------------------------------------------------------------------
            # The required m is m_final
            th_da_1_d = r'\True Hàm số có 2 đường tiệm cận (1 ngang, 1 đứng) khi $m = %s$' % latex(m_final)
            th_da_1_s = r'Hàm số có 2 đường tiệm cận (1 ngang, 1 đứng) khi $m = %s$' % latex(m_final + 1)
            list_th_da_1=[th_da_1_d, th_da_1_s]
            th_da_1=random.choice(list_th_da_1)
            list_th_1 = [th_da_1]
            list_th_2 = [loigiai_b]


            # ------------------------------------------------------------------------
            # Vận dụng - Analyze a case m=0
            # ------------------------------------------------------------------------
            m_case_0 = 0
            if b > 0: # Ensure $x=0$ is a VA
                D_0_roots = solve(x**2 + b*x + m_case_0, x) # 0 and -b
                if -b >= -a:
                    va_count_0 = 2 # x=0 and x=-b
                    da_vd_d = r'\True Khi $m=0$, đồ thị hàm số có 2 đường tiệm cận đứng là $x=0$ và $x=%s$' % latex(-b)
                    da_vd_s = r'Khi $m=0$, đồ thị hàm số có 1 đường tiệm cận đứng là $x=0$'
                    loigiai_c_0 = (r'''Khi $m=0$, ta có $f(x) = \frac{\sqrt{x+%s}}{x^2+%s x} = \frac{\sqrt{x+%s}}{x(x+%s)}$. \\
                                   Phương trình $x(x+%s)=0$ có hai nghiệm $x_1=0$ và $x_2=%s$. \\
                                   Với $x_1=0$: $\lim_{x\to 0^+} f(x) = \lim_{x\to 0^+} \frac{\sqrt{x+%s}}{x(x+%s)} = +\infty$. \\
                                   Với $x_2=%s$: $\lim_{x\to %s} f(x) = \lim_{x\to %s} \frac{\sqrt{x+%s}}{x(x+%s)} = \pm\infty$ (vì $x_2 \ge %s$). \\
                                   Vậy khi $m=0$, đồ thị hàm số có 2 đường tiệm cận đứng là $x=0$ và $x=%s$.'''
                                   % (latex(a), latex(b), latex(a), latex(b), latex(b), latex(-b),
                                      latex(a), latex(b), latex(-b), latex(-b), latex(-b), latex(a), latex(b), latex(-a), latex(-b)))
                else:
                    va_count_0 = 1 # only x=0
                    da_vd_d = r'\True Khi $m=0$, đồ thị hàm số có 1 đường tiệm cận đứng là $x=0$.'
                    da_vd_s = r'Khi $m=0$, đồ thị hàm số có 2 đường tiệm cận đứng là $x=0$ và $x=%s$.' % latex(-b)
                    loigiai_c_0 = (r'''Khi $m=0$, ta có $f(x) = \frac{\sqrt{x+%s}}{x^2+%s x} = \frac{\sqrt{x+%s}}{x(x+%s)}$. \\
                                   Phương trình $x(x+%s)=0$ có hai nghiệm $x_1=0$ và $x_2=%s$. \\
                                   $x_1=0$ thỏa mãn $x_1 \ge %s$ và $\lim_{x\to 0^+} f(x) = +\infty$. $\Rightarrow x=0$ là tiệm cận đứng. \\
                                   $x_2=%s$ không thỏa mãn $x_2 \ge %s$ (vì $%s < %s$). $\Rightarrow x=%s$ không là tiệm cận đứng. \\
                                   Vậy khi $m=0$, đồ thị hàm số có 1 đường tiệm cận đứng là $x=0$.'''
                                   % (latex(a), latex(b), latex(a), latex(b), latex(b), latex(-b),
                                      latex(-a), latex(-b), latex(-a), latex(-b), latex(-a), latex(-b)))
            else: # Should not happen based on randomization b>0, but for completeness
                va_count_0 = 0
                da_vd_d = r'\True Khi $m=0$, đồ thị hàm số không có tiệm cận đứng nào.'
                da_vd_s = r'Khi $m=0$, đồ thị hàm số có 1 tiệm cận đứng.'
                loigiai_c_0 = r'Không xét trường hợp này.'

            list_vd_da_1=[da_vd_d, da_vd_s]
            vd_da_1=random.choice(list_vd_da_1)
            list_vd_1 = [vd_da_1]
            list_vd_2 = [loigiai_c_0]

            # ------------------------------------------------------------------------
            # Vận dụng cao - Conclusion/Summary on total asymptotes
            # ------------------------------------------------------------------------
            # The main question is to find m such that there are 2 asymptotes (1 HA, 1 VA)
            vdc_da_1_d = r'\True Giá trị $m = %s$ làm cho hàm số có đúng 2 đường tiệm cận' % latex(m_final)
            vdc_da_1_s = r'Giá trị $m = %s$ làm cho hàm số có 2 đường tiệm cận' % latex(m_final-1)
            list_vdc_da_1=[vdc_da_1_d, vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            loigiai_d_vdc = (r'''Hàm số luôn có 1 tiệm cận ngang $y=0$. \\
                               Hàm số có đúng 2 đường tiệm cận khi có đúng 1 tiệm cận đứng. \\
                               Theo câu b), điều này xảy ra khi $m = %s$.'''
                             % latex(m_final))

            list_vdc_1 = [vdc_da_1]
            list_vdc_2 = [loigiai_d_vdc]

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
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán lại vào list (for final output)
            list_nb_1 = [nb_da_1]
            list_th_1 = [th_da_1]
            list_vd_1 = [vd_da_1]
            list_vdc_1 = [vdc_da_1]

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


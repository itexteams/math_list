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


def bt_dang20_p2_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Random các giá trị (m, n là tử và mẫu, a, b là cận)
            m = random.randint(1, 2)
            n = random.randint(1, 3)
            a = 2
            b = 6
            # Hàm số f(x) = m + n/x. Chú ý: Không dùng Rational(n, x) mà dùng n/x
            f = m + n/x
            ti_so_ba = Rational(b, a)

            # Nội dung câu hỏi
            noidungcauhoi = (r'''Cho hình phẳng $(H)$ giới hạn bởi đồ thị $(C)$ của hàm số $y=f(x)=\frac{%s x + %s}{x}$, trục hoành và hai đường thẳng $x=%s, x=%s$.''' 
                             %(latex(m), latex(n), latex(a), latex(b)))

            ########################################################################
            # Nhận biết ############################################
            s1_latex = latex(m*(b - a)) + " + " + latex(n) + r" \ln " + latex(ti_so_ba)
            s_sai = latex(n) + r" \ln " + latex(ti_so_ba)

            nb_da_1_d = r'\True Diện tích $S$ của hình phẳng $(H)$ là $S = %s$' % s1_latex
            nb_da_1_s = r'Diện tích $S$ của hình phẳng $(H)$ là $S = %s$' % s_sai
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]
            loigiai_nb_1 = (r'''Ta có $S = \int_{%s}^{%s} \left| \frac{%s x + %s}{x} \right| \text{d}x = \int_{%s}^{%s} \left( %s + \frac{%s}{x} \right) \text{d}x = \left( %s x + %s \ln x \right) \Big|_{%s}^{%s} = %s$.'''
                            %(latex(a), latex(b), latex(m), latex(n), latex(a), latex(b), latex(m), latex(n), latex(m), latex(n), latex(a), latex(b), s1_latex))
            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            th_da_1_d = r'\True Diện tích hình phẳng giới hạn bởi đồ thị $(C)$, đường thẳng $y = %s$ và hai đường thẳng $x = %s, x = %s$ là $S = %s$' % (latex(m), latex(a), latex(b), s_sai)
            th_da_1_s = r'Diện tích hình phẳng giới hạn bởi đồ thị $(C)$, đường thẳng $y = %s$ và hai đường thẳng $x = %s, x = %s$ là $S = %s$' % (latex(m), latex(a), latex(b), s1_latex)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]
            loigiai_th_1 = (r'''$S = \int_{%s}^{%s} \left| f(x) - %s \right| \text{d}x = \int_{%s}^{%s} \frac{%s}{x} \text{d}x = %s \ln x \Big|_{%s}^{%s} = %s$.'''
                            %(latex(a), latex(b), latex(m), latex(a), latex(b), latex(n), latex(n), latex(a), latex(b), s_sai))
            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## 
            # Vận dụng ############################################
            v1_tu = m**2*(b-a)*a*b + n**2*(b-a)
            v1_mau = a*b
            v1_latex = r"\frac{(%s + %s \ln %s)\pi}{%s}" % (latex(v1_tu), latex(2*m*n*a*b), latex(ti_so_ba), latex(v1_mau))

            vd_da_1_d = r'\True Thể tích khối tròn xoay tạo thành khi quay $(H)$ quanh trục $Ox$ là $V = %s$' % v1_latex
            vd_da_1_s = r'Thể tích khối tròn xoay tạo thành khi quay $(H)$ quanh trục $Ox$ là $V = %s$' % s1_latex
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]
            loigiai_vd_1 = (r'''$V = \pi \int_{%s}^{%s} f^2(x) \text{d}x = \pi \int_{%s}^{%s} \left( %s + \frac{%s}{x} + \frac{%s}{x^2} \right) \text{d}x = \pi \left( %s x + %s \ln x - \frac{%s}{x} \right) \Big|_{%s}^{%s} = %s$.'''
                            %(latex(a), latex(b), latex(a), latex(b), latex(m**2), latex(2*m*n), latex(n**2), latex(m**2), latex(2*m*n), latex(n**2), latex(a), latex(b), v1_latex))
            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## 
            # Vận dụng cao ############################################
            v2_tu = n**2*(b-a)
            v2_latex = r"\frac{(%s + %s \ln %s)\pi}{%s}" % (latex(v2_tu), latex(2*m*n*a*b), latex(ti_so_ba), latex(v1_mau))

            vdc_da_1_d = r'\True Thể tích khối tròn xoay khi quay hình phẳng giới hạn bởi $(C)$ và $y=%s, x=%s, x=%s$ quanh $Ox$ là $V = %s$' % (latex(m), latex(a), latex(b), v2_latex)
            vdc_da_1_s = r'Thể tích khối tròn xoay khi quay hình phẳng giới hạn bởi $(C)$ và $y=%s, x=%s, x=%s$ quanh $Ox$ là $V = %s$' % (latex(m), latex(a), latex(b), v1_latex)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]
            loigiai_vdc_1 = (r'''$V = \pi \int_{%s}^{%s} [f^2(x) - %s^2] \text{d}x = \pi \int_{%s}^{%s} \left( \frac{%s}{x} + \frac{%s}{x^2} \right) \text{d}x = \pi \left( %s \ln x - \frac{%s}{x} \right) \Big|_{%s}^{%s} = %s$.'''
                             %(latex(a), latex(b), latex(m), latex(a), latex(b), latex(2*m*n), latex(n**2), latex(2*m*n), latex(n**2), latex(a), latex(b), v2_latex))
            list_vdc_2 = [loigiai_vdc_1]

            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 đúng theo yêu cầu mẫu
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)
                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)
                if 1 <= true_count <= 3:
                    break

            # Gán lại vào list để xuất nội dung
            list_nb_1 = [nb_da_1]
            list_th_1 = [th_da_1]
            list_vd_1 = [vd_da_1]
            list_vdc_1 = [vdc_da_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            combined_th = list(zip(list_th_1, list_th_2))
            combined_vd = list(zip(list_vd_1, list_vd_2))
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # Xuất câu hỏi
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
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


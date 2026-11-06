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


def bt_dang7_p2_b2_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Random các hệ số cho hàm số f(x) = (x - a)/(x + b)
            # Chọn a, b sao cho đạo hàm đẹp và các giá trị tính toán không quá phức tạp
            a = random.randint(2, 5)
            b = random.randint(1, 4)
            x0 = -1 # Điểm tính đạo hàm f'
            x1 = sp.E # Điểm tính đạo hàm g' (thường dùng e để ln(e) = 1)

            # Định nghĩa hàm số
            f = (x - a)/(x + b)
            g = x * log(x)

            # Tính đạo hàm
            df = diff(f, x)
            dg = diff(g, x)

            # Tính các giá trị cụ thể cho câu (c)
            val_f_prime = df.subs(x, x0)
            val_g_prime = dg.subs(x, x1)
            diff_val = val_f_prime - val_g_prime

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hàm số $f(x)=\\frac{x-%s}{x+%s}$ và $g(x)=x \\ln x$.''' 
                             % (latex(a), latex(b)))

            ########################################################################
            # Nhận biết - Kiểm tra đạo hàm f(x)
            ########################################################################
            # Tính tử số của f'(x): (x+b) - (x-a) = b+a
            tu_so_f = b + a
            nb_da_1_d = '\\True Hàm số $f(x)$ có đạo hàm là $f\'(x)=\\frac{%s}{\\left( x+%s \\right)^2}$' % (latex(tu_so_f), latex(b))
            nb_da_1_s = 'Hàm số $f(x)$ có đạo hàm là $f\'(x)=\\frac{%s}{\\left( x+%s \\right)^2}$' % (latex(tu_so_f - 1), latex(b))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ('''Ta có $f(x)=\\frac{x-%s}{x+%s} \\Rightarrow f'(x)=\\frac{1 \\cdot %s - 1 \\cdot \\left( -%s \\right)}{\\left( x+%s \\right)^2} = \\frac{%s}{\\left( x+%s \\right)^2}$.''' 
                            % (latex(a), latex(b), latex(b), latex(a), latex(b), latex(tu_so_f), latex(b)))
            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # Thông hiểu - Kiểm tra đạo hàm g(x)
            ########################################################################
            th_da_1_d = '\\True Hàm số $g(x)$ có đạo hàm là $g\'(x)=\\ln x+1$'
            th_da_1_s = 'Hàm số $g(x)$ có đạo hàm là $g\'(x)=\\ln x-1$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ('''Ta có $g(x)=x \\ln x \\Rightarrow g'(x)=(x)' \\ln x + x (\\ln x)' = \\ln x + x \\cdot \\frac{1}{x} = \\ln x+1$.''')
            list_th_2 = [loigiai_th_1]

            ########################################################################
            # Vận dụng - Tính toán giá trị biểu thức
            ########################################################################
            # Tạo đáp án đúng và sai cho f'(x0) - g'(x1)
            # f'(-1) = (b+a)/(b-1)^2. g'(e) = ln(e)+1 = 2
            res_c = val_f_prime - 2
            vd_da_1_d = '\\True $f\'(%s)-g\'(e)=%s$' % (latex(x0), latex(res_c))
            vd_da_1_s = '$f\'(%s)-g\'(e)=%s$' % (latex(x0), latex(res_c + 1))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ('''Ta có $f'(%s)=\\frac{%s}{\\left( %s+%s \\right)^2}=%s$. \\\\
                            Mặt khác $g'(e)=\\ln e+1=2$. \\\\
                            Vậy $f'(%s)-g'(e)=%s-2=%s$.''' 
                            % (latex(x0), latex(tu_so_f), latex(x0), latex(b), latex(val_f_prime), latex(x0), latex(val_f_prime), latex(res_c)))
            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # Vận dụng cao - Giải phương trình
            ########################################################################
            # Phương trình (x+b)^2 * f'(x) = g'(x) 
            # <=> tu_so_f = ln x + 1 <=> ln x = tu_so_f - 1 <=> x = e^(tu_so_f - 1)
            # Phương trình này luôn có duy nhất 1 nghiệm dương.
            vdc_da_1_d = '\\True Phương trình $\\left( x+%s \\right)^2 f\'(x)=g\'(x)$ có một nghiệm' % (latex(b))
            vdc_da_1_s = 'Phương trình $\\left( x+%s \\right)^2 f\'(x)=g\'(x)$ có hai nghiệm' % (latex(b))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = ('''Phương trình tương đương: \\\\
                             $\\left( x+%s \\right)^2 \\cdot \\frac{%s}{\\left( x+%s \\right)^2} = \\ln x+1$ \\\\
                             $\\Leftrightarrow %s = \\ln x+1 \\Leftrightarrow \\ln x = %s \\Leftrightarrow x = e^{%s}$. \\\\
                             Vậy phương trình đã cho có duy nhất một nghiệm.''' 
                             % (latex(b), latex(tu_so_f), latex(b), latex(tu_so_f), latex(tu_so_f-1), latex(tu_so_f-1)))
            list_vdc_2 = [loigiai_vdc_1]

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Vòng lặp đảm bảo số lượng câu đúng từ 1 đến 3
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                if 1 <= count_true_answers(answers) <= 3:
                    break

            # Gán và xáo trộn theo cặp (đáp án, lời giải) để đảm bảo lời giải khớp với đáp án đã chọn
            combined_nb = list(zip([nb_da_1], list_nb_2))
            combined_th = list(zip([th_da_1], list_th_2))
            combined_vd = list(zip([vd_da_1], list_vd_2))
            combined_vdc = list(zip([vdc_da_1], list_vdc_2))

            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # Xuất nội dung theo định dạng yêu cầu
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


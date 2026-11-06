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


def bt_dang13_p2_b3_c5_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Random số mũ n từ 3 đến 6 để đảm bảo tính toán vừa phải và thú vị
            n = random.randint(3, 6)
            expr = (1 + x + x**2)**n
            expanded_expr = expand(expr)

            # 1. Số hạng tự do
            constant_term = expanded_expr.subs(x, 0)

            # 2. Số hạng tử trong khai triển
            # Đa thức (1+x+x^2)^n có bậc cao nhất là 2n, thấp nhất là 0. 
            # Tổng số hạng tử là 2n + 1
            num_terms = 2 * n + 1

            # 3. Số hạng chính giữa
            # Vì có 2n+1 hạng tử (lẻ), hạng tử chính giữa là hạng tử chứa x^n
            middle_coeff = expanded_expr.coeff(x, n)

            # 4. Tổng các hệ số
            sum_coefficients = expanded_expr.subs(x, 1)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Xét khai triển biểu thức $\\left( 1+x+x^2 \\right)^{%s}$ (sắp xếp theo thứ tự mũ giảm dần).''' 
                             % (latex(n)))

            ########################################################################
            # Nhận biết ############################################
            nb_da_1_d = '\\True Số hạng tự do trong khai triển bằng $%s$' % (latex(constant_term))
            nb_da_1_s = 'Số hạng tự do trong khai triển bằng $%s$' % (latex(num_terms))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Số hạng tự do trong khai triển tương ứng với giá trị của đa thức khi $x=0$.\\\\
                            Thay $x=0$ vào biểu thức, ta được $f\\left( 0 \\right) = \\left( 1+0+0^2 \\right)^{%s} = 1$.''' % (latex(n)))

            ########################################################################
            # Thông hiểu ############################################
            th_da_1_d = '\\True Trong khai triển có $%s$ hạng tử' % (latex(num_terms))
            th_da_1_s = 'Trong khai triển có $%s$ hạng tử' % (latex(n + 1))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Biểu thức có dạng $\\left( 1+x+x^2 \\right)^{%s}$. Khi khai triển, bậc cao nhất của $x$ là $2 \\cdot %s = %s$ và bậc thấp nhất là $0$.\\\\
                            Do đó, số hạng tử của khai triển là $%s - 0 + 1 = %s$ hạng tử.''' % (latex(n), latex(n), latex(2*n), latex(2*n), latex(num_terms)))

            ########################################################################
            # Vận dụng ############################################
            vd_da_1_d = '\\True Tổng các hệ số trong khai triển bằng $%s$' % (latex(sum_coefficients))
            vd_da_1_s = 'Tổng các hệ số trong khai triển bằng $%s$' % (latex(2**n))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Tổng các hệ số trong khai triển của một đa thức $P(x)$ chính là giá trị của đa thức đó khi $x=1$.\\\\
                            Ta có $P(1) = \\left( 1+1+1^2 \\right)^{%s} = 3^{%s} = %s$.''' % (latex(n), latex(n), latex(sum_coefficients)))

            ########################################################################
            # Vận dụng cao ############################################
            vdc_da_1_d = '\\True Số hạng chính giữa trong khai triển là $%s x^{%s}$' % (latex(middle_coeff), latex(n))
            vdc_da_1_s = 'Số hạng chính giữa trong khai triển là $%s x^{%s}$' % (latex(middle_coeff + 2), latex(n))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Khai triển có $%s$ hạng tử, do đó hạng tử chính giữa là hạng tử thứ $%s$, ứng với số mũ $x^{%s}$.\\\\
                             Hệ số của $x^{%s}$ trong khai triển $\\left( 1+x+x^2 \\right)^{%s}$ được tính toán là $%s$.\\\\
                             Vậy số hạng chính giữa là $%s x^{%s}$.''' 
                             % (latex(num_terms), latex(n + 1), latex(n), latex(n), latex(n), latex(middle_coeff), latex(middle_coeff), latex(n)))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 đúng
            while True:
                nb_sel = random.choice(list_nb_da_1)
                th_sel = random.choice(list_th_da_1)
                vd_sel = random.choice(list_vd_da_1)
                vdc_sel = random.choice(list_vdc_da_1)

                answers = [nb_sel, th_sel, vd_sel, vdc_sel]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán kết quả cuối cùng
            shuffled_answers = [nb_sel, th_sel, vd_sel, vdc_sel]
            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            # Xuất câu hỏi
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\\choiceTFn \n'
                '{'+str(shuffled_answers[0])+'}\n'
                '{'+str(shuffled_answers[1])+'}\n'
                '{'+str(shuffled_answers[2])+'}\n'
                '{'+str(shuffled_answers[3])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions[0])+'\n'
                '\\item '+str(shuffled_solutions[1])+'\n'
                '\\item '+str(shuffled_solutions[2])+'\n'
                '\\item '+str(shuffled_solutions[3])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


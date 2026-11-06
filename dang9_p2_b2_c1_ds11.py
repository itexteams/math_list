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


def bt_dang9_p2_b2_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến và tạo dữ liệu ngẫu nhiên từ bộ ba số Pythagore
            # Danh sách chứa các bộ ba Pythagore (đối, kề, huyền)
            pythagorean_triplets = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (20, 21, 29)]

            # Chọn ngẫu nhiên bộ ba Pythagore cho góc a và góc b (đảm bảo khác nhau để bài toán phong phú)
            triplet_a = random.choice(pythagorean_triplets)
            remaining_triplets = [t for t in pythagorean_triplets if t != triplet_a]
            triplet_b = random.choice(remaining_triplets)

            # Góc a: sin(a) = doi_a / huyen_a
            doi_a, ke_a, huyen_a = triplet_a[0], triplet_a[1], triplet_a[2]
            # Có thể hoán đổi ngẫu nhiên đối và kề của góc a
            if random.choice([True, False]):
                doi_a, ke_a = ke_a, doi_a

            sin_a = Rational(doi_a, huyen_a)
            cos_a = Rational(ke_a, huyen_a)
            tan_a = Rational(doi_a, ke_a)

            # Góc b: tan(b) = doi_b / ke_b
            doi_b, ke_b, huyen_b = triplet_b[0], triplet_b[1], triplet_b[2]
            if random.choice([True, False]):
                doi_b, ke_b = ke_b, doi_b

            tan_b = Rational(doi_b, ke_b)
            cos_b = Rational(ke_b, huyen_b)
            sin_b = Rational(doi_b, huyen_b)

            # Tính toán các giá trị biểu thức chính xác
            sin_am_b = sin_a * cos_b - cos_a * sin_b
            cos_ap_b = cos_a * cos_b - sin_a * sin_b
            tan_ap_b = (tan_a + tan_b) / (1 - tan_a * tan_b)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Biết $\\sin a = %s$, $\\tan b = %s$ và $a, b$ là các góc nhọn. Khi đó:''' 
                             %(latex(sin_a), latex(tan_b)))

            ########################################################################
            # Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True $\\tan a = %s$' %(latex(tan_a))
            nb_da_1_s = '$\\tan a = %s$' %(latex(1 / tan_a))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Vì $a, b$ là các góc nhọn nên $\\cos a > 0, \\cos b > 0$.\\\\
            Ta có: $\\cos a = \\sqrt{1 - \\sin^2 a} = %s \\Rightarrow \\tan a = \\frac{\\sin a}{\\cos a} = %s$;'''
                            %(latex(cos_a), latex(tan_a)))

            list_nb_2 = [loigiai_nb_1]
            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True $\\sin(a - b) = %s$' %(latex(sin_am_b))
            th_da_1_s = '$\\sin(a - b) = %s$' %(latex(-sin_am_b))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''$\\cos b = \\sqrt{\\frac{1}{1 + \\tan^2 b}} = %s \\Rightarrow \\sin b = \\cos b \\cdot \\tan b = %s$. Khi đó:\\\\
            $\\sin(a - b) = \\sin a \\cdot \\cos b - \\cos a \\cdot \\sin b = %s \\cdot %s - %s \\cdot %s = %s$.'''
                            %(latex(cos_b), latex(sin_b), latex(sin_a), latex(cos_b), latex(cos_a), latex(sin_b), latex(sin_am_b)))

            list_th_2 = [loigiai_th_1]
            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng ############################################
            # Các đáp án (Gốc cố tình cho phương án c Sai bằng cách rút gọn mẫu số sai hoặc viết sai số)
            sai_cos_ap_b = Rational(14, 22) if triplet_a == (8, 15, 17) and triplet_b == (5, 12, 13) else cos_ap_b / 2
            vd_da_1_d = '$\\cos(a + b) = %s$' %(latex(sai_cos_ap_b))
            vd_da_1_s = '\\True $\\cos(a + b) = %s$' %(latex(cos_ap_b))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''$\\cos(a + b) = \\cos a \\cdot \\cos b - \\sin a \\cdot \\sin b = %s \\cdot %s - %s \\cdot %s = %s$.'''
                            %(latex(cos_a), latex(cos_b), latex(sin_a), latex(sin_b), latex(cos_ap_b)))

            list_vd_2 = [loigiai_vd_1]
            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao ############################################
            # Các đáp án (Gốc cố tình cho phương án d Sai bằng việc đảo ngược phân số hoặc viết nhầm số)
            sai_tan_ap_b = Rational(17, 14) if triplet_a == (8, 15, 17) and triplet_b == (5, 12, 13) else 1 / tan_ap_b
            vdc_da_1_d = '$\\tan(a + b) = %s$' %(latex(sai_tan_ap_b))
            vdc_da_1_s = '\\True $\\tan(a + b) = %s$' %(latex(tan_ap_b))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''$\\tan(a + b) = \\frac{\\tan a + \\tan b}{1 - \\tan a \\cdot \\tan b} = \\frac{%s + %s}{1 - %s \\cdot %s} = %s$.'''
                             %(latex(tan_a), latex(tan_b), latex(tan_a), latex(tan_b), latex(tan_ap_b)))

            list_vdc_2 = [loigiai_vdc_1]
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án tổng hợp có từ 1 đến 3 đúng để đảm bảo tính ngẫu nhiên True/False đúng định dạng mẫu
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán lại vào list sau khi lọc điều kiện thỏa mãn
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

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn theo khung chương trình mẫu
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


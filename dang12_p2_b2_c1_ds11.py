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


def bt_dang12_p2_b2_c1_ds11(self):
            # Khai báo biến
            # Chọn ngẫu nhiên sin(alpha) = tu / mau sao cho 0 < sin < 1
            mau = random.choice([3, 4, 5, 7])
            tu = random.randint(1, mau - 1)
            sin_val = Rational(tu, mau)

            # Tính toán các giá trị chính xác bằng SymPy theo giả thiết góc thuộc khoảng (pi/2; pi)
            cos2_val = 1 - sin_val**2
            cos_val = -sqrt(cos2_val) # Vì pi/2 < alpha < pi nên cos < 0
            tan_val = sin_val / cos_val

            # Tính giá trị câu c: cos(pi/3 + alpha) = cos(pi/3)cos(alpha) - sin(pi/3)sin(alpha)
            cos_pi3 = Rational(1, 2)
            sin_pi3 = sqrt(3)/2
            cos_c_val = cos_pi3 * cos_val - sin_pi3 * sin_val
            cos_c_val = sp.simplify(cos_c_val)

            # Tính giá trị câu d: cos(pi/4 - alpha) = cos(pi/4)cos(alpha) + sin(pi/4)sin(alpha)
            cos_pi4 = sqrt(2)/2
            sin_pi4 = sqrt(2)/2
            cos_d_val = cos_pi4 * cos_val + sin_pi4 * sin_val
            cos_d_val = sp.simplify(cos_d_val)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho $\\sin\\alpha = %s$, $\\frac{\\pi}{2} < \\alpha < \\pi$. Khi đó:''' 
                             %(latex(sin_val)))

            ########################################################################
            # Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True $\\cos\\alpha = %s$' %(latex(cos_val))
            nb_da_1_s = '$\\cos\\alpha = %s$' %(latex(-cos_val))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''$\\sin\\alpha = %s$, $\\frac{\\pi}{2} < \\alpha < \\pi$\\\\
            Ta có: $\\cos^2\\alpha = 1 - \\sin^2\\alpha = 1 - \\left(%s\\right)^2 = %s \\Rightarrow \\cos\\alpha = \\pm %s$\\\\
            Vì $\\frac{\\pi}{2} < \\alpha < \\pi$ nên $\\cos\\alpha = %s$.'''
                            %(latex(sin_val), latex(sin_val), latex(cos2_val), latex(-cos_val), latex(cos_val)))

            list_nb_2 = [loigiai_nb_1]
            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True $\\tan\\alpha = %s$' %(latex(tan_val))
            th_da_1_s = '$\\tan\\alpha = %s$' %(latex(-tan_val))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''$\\tan\\alpha = \\frac{\\sin\\alpha}{\\cos\\alpha} = %s$.''' %(latex(tan_val)))

            list_th_2 = [loigiai_th_1]
            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng ############################################
            # Các đáp án (Gốc cố tình cho phương án c Sai bằng việc biến đổi nhầm dấu)
            sai_cos_c_val = cos_pi3 * (-cos_val) - sin_pi3 * sin_val if tu == 2 and mau == 3 else -cos_c_val
            vd_da_1_d = '$\\cos\\left(\\frac{\\pi}{3} + \\alpha\\right) = %s$' %(latex(sai_cos_c_val))
            vd_da_1_s = '\\True $\\cos\\left(\\frac{\\pi}{3} + \\alpha\\right) = %s$' %(latex(cos_c_val))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''$\\cos\\left(\\frac{\\pi}{3} + \\alpha\\right) = \\cos\\frac{\\pi}{3}\\cos\\alpha - \\sin\\frac{\\pi}{3}\\sin\\alpha = \\frac{1}{2} \\cdot \\left(%s\\right) - \\frac{\\sqrt{3}}{2} \\cdot %s = %s$.'''
                            %(latex(cos_val), latex(sin_val), latex(cos_c_val)))

            list_vd_2 = [loigiai_vd_1]
            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao ############################################
            # Các đáp án (Gốc cố tình cho phương án d Sai bằng việc biến đổi nhầm dấu)
            sai_cos_d_val = cos_pi4 * (-cos_val) + sin_pi4 * sin_val if tu == 2 and mau == 3 else -cos_d_val
            vdc_da_1_d = '$\\cos\\left(\\frac{\\pi}{4} - \\alpha\\right) = %s$' %(latex(sai_cos_d_val))
            vdc_da_1_s = '\\True $\\cos\\left(\\frac{\\pi}{4} - \\alpha\\right) = %s$' %(latex(cos_d_val))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''$\\cos\\left(\\frac{\\pi}{4} - \\alpha\\right) = \\cos\\frac{\\pi}{4}\\cos\\alpha + \\sin\\frac{\\pi}{4}\\sin\\alpha = \\frac{\\sqrt{2}}{2} \\cdot \\left(%s\\right) + \\frac{\\sqrt{2}}{2} \\cdot %s = %s$.'''
                             %(latex(cos_val), latex(sin_val), latex(cos_d_val)))

            list_vdc_2 = [loigiai_vdc_1]
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án tổng hợp thỏa mãn có từ 1 đến 3 câu Đúng
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán lại vào danh sách sau khi đã kiểm duyệt số lượng câu Đúng/Sai thích hợp
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

            # Xuất câu hỏi với đáp án và lời giải đã được xử lý đồng bộ theo đúng cấu trúc khung chương trình mẫu
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


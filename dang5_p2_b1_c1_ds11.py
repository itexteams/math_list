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


def bt_dang5_p2_b1_c1_ds11(self):
            # Khai báo biến
            # Danh sách các góc cơ sở và định dạng LaTeX tương ứng (được chọn ngẫu nhiên)
            goc_data = [
                {"val": -pi/4, "latex": "-\\frac{\\pi}{4}", "abs_latex": "\\frac{\\pi}{4}"},
                {"val": -pi/3, "latex": "-\\frac{\\pi}{3}", "abs_latex": "\\frac{\\pi}{3}"},
                {"val": -pi/6, "latex": "-\\frac{\\pi}{6}", "abs_latex": "\\frac{\\pi}{6}"},
                {"val": pi/4, "latex": "\\frac{\\pi}{4}", "abs_latex": "\\frac{\\pi}{4}"},
                {"val": pi/3, "latex": "\\frac{\\pi}{3}", "abs_latex": "\\frac{\\pi}{3}"},
                {"val": pi/6, "latex": "\\frac{\\pi}{6}", "abs_latex": "\\frac{\\pi}{6}"}
            ]

            goc_chon = random.choice(goc_data)
            goc_val = goc_chon["val"]
            goc_latex = goc_chon["latex"]
            goc_abs_latex = goc_chon["abs_latex"]

            # Biến đổi góc: alpha = goc_val + (2k+1)*pi = goc_val + 2k*pi + pi = (goc_val + pi) + k2pi
            # Các giá trị lượng giác thực tế của alpha chính là lượng giác của (goc_val + pi)
            val_sin = sin(goc_val + pi)
            val_cos = cos(goc_val + pi)
            val_tan = tan(goc_val + pi)
            val_cot = cot(goc_val + pi)

            # Biến đổi lượng giác để phục vụ phần lời giải chi tiết từng bước như hình ảnh gốc
            val_sin_goc = sin(goc_val)
            val_cos_goc = cos(goc_val)
            val_tan_goc = tan(goc_val)
            val_cot_goc = cot(goc_val)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Tính được các giá trị lượng giác của góc $\\alpha = %s + (2k+1)\\pi$ (biết $k \\in \\mathbb{Z}$). Khi đó:''' % (goc_latex))

            ########################################################################
            # Nhận biết (Biểu thức sin alpha)
            nb_da_1_d = '\\True $\\sin \\alpha = %s$' % (latex(val_sin))
            nb_da_1_s = '$\\sin \\alpha = %s$' % (latex(-val_sin))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            # Chuỗi biến đổi chi tiết cho sin alpha dựa trên dấu của góc cơ sở ban đầu
            if goc_val < 0:
                loigiai_nb_1 = ('''$\\sin \\left[ %s + (2k+1)\\pi \\right] = \\sin \\left( %s + 2k\\pi + \\pi \\right) = \\sin \\left( %s + \\pi \\right) = -\\sin \\left( %s \\right) = \\sin %s = %s$''' 
                                % (goc_latex, goc_latex, goc_latex, goc_latex, goc_abs_latex, latex(val_sin)))
            else:
                loigiai_nb_1 = ('''$\\sin \\left[ %s + (2k+1)\\pi \\right] = \\sin \\left( %s + 2k\\pi + \\pi \\right) = \\sin \\left( %s + \\pi \\right) = -\\sin %s = %s$''' 
                                % (goc_latex, goc_latex, goc_latex, goc_latex, latex(val_sin)))

            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu (Biểu thức cos alpha)
            th_da_1_d = '\\True $\\cos \\alpha = %s$' % (latex(val_cos))
            th_da_1_s = '$\\cos \\alpha = %s$' % (latex(-val_cos))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            if goc_val < 0:
                loigiai_th_1 = ('''$\\cos \\left[ %s + (2k+1)\\pi \\right] = \\cos \\left( %s + 2k\\pi + \\pi \\right) = \\cos \\left( %s + \\pi \\right) = -\\cos \\left( %s \\right) = -\\cos %s = %s$''' 
                                % (goc_latex, goc_latex, goc_latex, goc_latex, goc_abs_latex, latex(val_cos)))
            else:
                loigiai_th_1 = ('''$\\cos \\left[ %s + (2k+1)\\pi \\right] = \\cos \\left( %s + 2k\\pi + \\pi \\right) = \\cos \\left( %s + \\pi \\right) = -\\cos %s = %s$''' 
                                % (goc_latex, goc_latex, goc_latex, goc_latex, latex(val_cos)))

            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng (Biểu thức tan alpha)
            vd_da_1_d = '\\True $\\tan \\alpha = %s$' % (latex(val_tan))
            vd_da_1_s = '$\\tan \\alpha = %s$' % (latex(-val_tan))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            if goc_val < 0:
                loigiai_vd_1 = ('''$\\tan \\left[ %s + (2k+1)\\pi \\right] = \\tan \\left( %s \\right) = -\\tan %s = %s$''' 
                                % (goc_latex, goc_latex, goc_abs_latex, latex(val_tan)))
            else:
                loigiai_vd_1 = ('''$\\tan \\left[ %s + (2k+1)\\pi \\right] = \\tan %s = %s$''' 
                                % (goc_latex, goc_latex, latex(val_tan)))

            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao (Biểu thức cot alpha)
            vdc_da_1_d = '\\True $\\cot \\alpha = %s$' % (latex(val_cot))
            vdc_da_1_s = '$\\cot \\alpha = %s$' % (latex(-val_cot))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            if goc_val < 0:
                loigiai_vdc_1 = ('''$\\cot \\left[ %s + (2k+1)\\pi \\right] = \\cot \\left( %s \\right) = -\\cot %s = %s$''' 
                                 % (goc_latex, goc_latex, goc_abs_latex, latex(val_cot)))
            else:
                loigiai_vdc_1 = ('''$\\cot \\left[ %s + (2k+1)\\pi \\right] = \\cot %s = %s$''' 
                                 % (goc_latex, goc_latex, latex(val_cot)))

            list_vdc_2 = [loigiai_vdc_1]

            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)


            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)


            # Vòng lặp đảm bảo số lượng phương án Đúng nằm trong khoảng từ 1 đến 3 câu
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán lại vào cấu trúc danh sách
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

            # Xuất câu hỏi với định dạng mẫu mã nguồn theo cấu trúc đề thi trắc nghiệm Đúng-Sai mẫu
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


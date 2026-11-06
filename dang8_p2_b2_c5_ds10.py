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


def bt_dang8_p2_b2_c5_ds10(self):
            # Khai báo biến
            # Khai báo các thông số của bài toán
            nA = randint(10,15)
            nB = randint(8,12)
            nC = randint(5,6)
            k_tong = randint(15,20)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Từ một nhóm %s học sinh lớp 12 gồm %s học sinh khối $A$, %s học sinh khối $B$ và %s học sinh khối $C$, cần chọn ra %s học sinh.''' 
                             %(latex(nA + nB + nC), latex(nA), latex(nB), latex(nC), latex(k_tong)))

            ########################################################################
            # Nhận biết ############################################
            # Tính toán số cách chọn mỗi khối bằng nhau (mỗi khối 5 em)
            val_a = binomial(nA, 5) * binomial(nB, 5) * binomial(nC, 5)

            nb_da_1_d = '\\True Số cách chọn để học sinh mỗi khối là bằng nhau là %s' %(latex(val_a))
            nb_da_1_s = 'Số cách chọn để học sinh mỗi khối là bằng nhau là 252252'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Để chọn mỗi khối có số học sinh bằng nhau, ta chọn mỗi khối $%s: %s = 5$ học sinh. \\\\
                            Số cách chọn là $C_{%s}^{5} \\cdot C_{%s}^{5} \\cdot C_{%s}^{5} = %s \\cdot %s \\cdot %s = %s$.''' 
                            %(latex(k_tong), latex(3), latex(nA), latex(nB), latex(nC), 
                              latex(binomial(nA, 5)), latex(binomial(nB, 5)), latex(binomial(nC, 5)), latex(val_a)))

            list_nb_1 = [nb_da_1]
            list_nb_2 = [loigiai_nb_1]
            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            # Chọn 2 học sinh khối C và 13 học sinh khối B hoặc A (tổng A+B là 25)
            val_b_formula = 'C_{%s}^{2}C_{%s}^{13}' %(latex(nC), latex(nA + nB))

            th_da_1_d = '\\True Số cách chọn để có 2 học sinh khối $C$, 13 học sinh khối $B$ hoặc khối $A$: có $%s$ cách' %(val_b_formula)
            th_da_1_s = 'Số cách chọn để có 2 học sinh khối $C$, 13 học sinh khối $B$ hoặc khối $A$: có $C_{5}^{2}C_{15}^{13}$ cách'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Chọn 2 học sinh từ %s học sinh khối $C$ có $C_{%s}^{2}$ cách. \\\\
                            Chọn 13 học sinh còn lại từ nhóm khối $A$ và $B$ (tổng $%s + %s = 25$ học sinh) có $C_{25}^{13}$ cách. \\\\
                            Vậy số cách chọn là $C_{%s}^{2}C_{25}^{13}$.''' 
                            %(latex(nC), latex(nC), latex(nA), latex(nB), latex(nC)))

            list_th_1 = [th_da_1]
            list_th_2 = [loigiai_th_1]
            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng ############################################
            # Chọn 2C, 10B, 3A
            val_c_calc = binomial(nC, 2) * binomial(nB, 10) * binomial(nA, 3)

            vd_da_1_d = '\\True Số cách chọn để có 2 học sinh khối $C$, 10 học sinh khối $B$ và 3 học sinh khối $A$ có $C_{5}^{2}C_{10}^{10}C_{15}^{3}$ cách'
            vd_da_1_s = 'Số cách chọn để có 2 học sinh khối $C$, 10 học sinh khối $B$ và 3 học sinh khối $A$ có $C_{5}^{2}C_{10}^{1}C_{15}^{3}$ cách'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Số cách chọn 2 học sinh khối $C$ là $C_{%s}^{2}$. \\\\
                            Số cách chọn 10 học sinh khối $B$ là $C_{%s}^{10}$. \\\\
                            Số cách chọn 3 học sinh khối $A$ là $C_{%s}^{3}$. \\\\
                            Tổng số cách chọn là $C_{%s}^{2} \\cdot C_{%s}^{10} \\cdot C_{%s}^{3} = %s$ cách.''' 
                            %(latex(nC), latex(nB), latex(nA), latex(nC), latex(nB), latex(nA), latex(val_c_calc)))

            list_vd_1 = [vd_da_1]
            list_vd_2 = [loigiai_vd_1]
            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao ############################################
            # Đúng 2C và ít nhất 5A. 
            # Tổng chọn từ A+B là 13. B tối đa có 10 em.
            # Các trường hợp vi phạm (ít hơn 5A): A=3, B=10 hoặc A=4, B=9.
            total_AB_13 = binomial(nA + nB, 13)
            case_A3 = binomial(nA, 3) * binomial(nB, 10)
            case_A4 = binomial(nA, 4) * binomial(nB, 9)
            val_d_final = binomial(nC, 2) * (total_AB_13 - case_A3 - case_A4)

            vdc_da_1_d = '\\True Số cách chọn để có ít nhất 5 học sinh khối $A$ và có đúng 2 học sinh khối $C$ là %s' %(latex(val_d_final))
            vdc_da_1_s = 'Số cách chọn để có ít nhất 5 học sinh khối $A$ và có đúng 2 học sinh khối $C$ là 5186195'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Số cách chọn đúng 2 học sinh khối $C$ là $C_{5}^{2} = 10$. \\\\
                            Cần chọn 13 học sinh còn lại từ khối $A$ (%s em) và khối $B$ (%s em) sao cho có ít nhất 5 học sinh khối $A$. \\\\
                            Tổng số cách chọn 13 em từ 25 em (A và B) là $C_{25}^{13} = %s$. \\\\
                            Do khối $B$ chỉ có 10 em nên số học sinh khối $A$ tối thiểu phải là $13 - 10 = 3$. \\\\
                            Các trường hợp không thỏa mãn (ít hơn 5 em khối $A$): \\\\
                            - Trường hợp 3 học sinh khối $A$, 10 học sinh khối $B$: $C_{15}^{3} \\cdot C_{10}^{10} = %s$. \\\\
                            - Trường hợp 4 học sinh khối $A$, 9 học sinh khối $B$: $C_{15}^{4} \\cdot C_{10}^{9} = %s$. \\\\
                            Số cách chọn 13 em thỏa mãn là: $%s - %s - %s = %s$. \\\\
                            Vậy tổng số cách chọn là: $10 \\cdot %s = %s$.''' 
                            %(latex(nA), latex(nB), latex(total_AB_13), latex(case_A3), latex(case_A4), 
                              latex(total_AB_13), latex(case_A3), latex(case_A4), latex(total_AB_13 - case_A3 - case_A4),
                              latex(total_AB_13 - case_A3 - case_A4), latex(val_d_final)))

            list_vdc_1 = [vdc_da_1]
            list_vdc_2 = [loigiai_vdc_1]
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)
                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                if 1 <= count_true_answers(answers) <= 3:
                    break

            list_nb_1, list_th_1, list_vd_1, list_vdc_1 = [nb_da_1], [th_da_1], [vd_da_1], [vdc_da_1]
            shuffled_answers_nb, shuffled_solutions_nb = nb_da_1, loigiai_nb_1
            shuffled_answers_th, shuffled_solutions_th = th_da_1, loigiai_th_1
            shuffled_answers_vd, shuffled_solutions_vd = vd_da_1, loigiai_vd_1
            shuffled_answers_vdc, shuffled_solutions_vdc = vdc_da_1, loigiai_vdc_1

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
                '{'+str(shuffled_answers_nb)+'}\n'
                '{'+str(shuffled_answers_th)+'}\n'
                '{'+str(shuffled_answers_vd)+'}\n'
                '{'+str(shuffled_answers_vdc)+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions_nb)+'\n'
                '\\item '+str(shuffled_solutions_th)+'\n'
                '\\item '+str(shuffled_solutions_vd)+'\n'
                '\\item '+str(shuffled_solutions_vdc)+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


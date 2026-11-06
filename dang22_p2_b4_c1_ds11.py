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


def bt_dang22_p2_b4_c1_ds11(self):
            # Khai báo biến
            x = symbols('x')              
            case_d = random.choice([1, 2])

            if case_d == 1:
                str_val_d = "\\sqrt{3}"
                so_diem_dung = "1 điểm biểu diễn nghiệm trên vòng tròn lượng giác"
                so_diem_sai = "5 điểm biểu diễn nghiệm trên vòng tròn lượng giác"
                loigiai_d_chi_tiet = ('''Xét phương trình $f(x) = \\sqrt{3}$ với điều kiện xác định.\\\\
            Phương trình tương đương với:\\\\
            $\\frac{\\cos x}{\\sin x + 1} = \\sqrt{3} \\Leftrightarrow \\cos x = \\sqrt{3}\\sin x + \\sqrt{3} \\Leftrightarrow \\cos x - \\sqrt{3}\\sin x = \\sqrt{3}$\\\\
            $\\Leftrightarrow \\frac{1}{2}\\cos x - \\frac{\\sqrt{3}}{2}\\sin x = \\frac{\\sqrt{3}}{2} \\Leftrightarrow \\cos\\left( x + \\frac{\\pi}{3} \\right) = \\cos\\frac{\\pi}{6}$\\\\
            $\\Leftrightarrow \\left[\\begin{aligned} & x + \\frac{\\pi}{3} = \\frac{\\pi}{6} + k2\\pi \\\\ & x + \\frac{\\pi}{3} = -\\frac{\\pi}{6} + k2\\pi \\end{aligned}\\right. \\Leftrightarrow \\left[\\begin{aligned} & x = -\\frac{\\pi}{6} + k2\\pi \\text{ (thỏa mãn)} \\\\ & x = -\\frac{\\pi}{2} + k2\\pi \\text{ (loại vì làm } \\sin x = -1) \\end{aligned}\\right.$\\\\
            Vậy phương trình có duy nhất $1$ điểm biểu diễn nghiệm trên vòng tròn lượng giác.''')
            else:
                str_val_d = "\\frac{\\sqrt{3}}{3}"
                so_diem_dung = "0 điểm biểu diễn nghiệm trên vòng tròn lượng giác"
                so_diem_sai = "3 điểm biểu diễn nghiệm trên vòng tròn lượng giác"
                loigiai_d_chi_tiet = ('''Xét phương trình $f(x) = \\frac{\\sqrt{3}}{3}$ với điều kiện xác định.\\\\
            Phương trình tương đương với:\\\\
            $\\frac{\\cos x}{\\sin x + 1} = \\frac{\\sqrt{3}}{3} \\Leftrightarrow 3\\cos x = \\sqrt{3}\\sin x + \\sqrt{3} \\Leftrightarrow \\sqrt{3}\\cos x - \\sin x = 1$\\\\
            $\\Leftrightarrow \\frac{\\sqrt{3}}{2}\\cos x - \\frac{1}{2}\\sin x = \\frac{1}{2} \\Leftrightarrow \\cos\\left( x + \\frac{\\pi}{6} \\right) = \\cos\\frac{\\pi}{3}$\\\\
            $\\Leftrightarrow \\left[\\begin{aligned} & x + \\frac{\\pi}{6} = \\frac{\\pi}{3} + k2\\pi \\\\ & x + \\frac{\\pi}{6} = -\\frac{\\pi}{3} + k2\\pi \\end{aligned}\\right. \\Leftrightarrow \\left[\\begin{aligned} & x = \\frac{\\pi}{6} + k2\\pi \\text{ (loại vì làm } 1 - 2\\sin x = 0) \\\\ & x = -\\frac{\\pi}{2} + k2\\pi \\text{ (loại vì làm } \\sin x = -1) \\end{aligned}\\right.$\\\\
            Vậy phương trình vô nghiệm, tức là có $0$ điểm biểu diễn nghiệm trên vòng tròn lượng giác.''')

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hàm số $f(x) = \\frac{\\cos x (1 - 2\\sin x)}{2\\cos^2 x - \\sin x - 1}$. Xét tính đúng – sai của các mệnh đề sau:''')

            ########################################################################
            # Nhận biết ############################################
            nb_da_1_d = '\\True $f(x) = \\frac{\\cos x}{\\sin x + 1}$'
            nb_da_1_s = '$f(x) = \\frac{\\cos x}{\\sin x - 1}$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = ('''Ta biến đổi mẫu số của hàm số $f(x)$:\\\\
            $2\\cos^2 x - \\sin x - 1 = 2(1 - \\sin^2 x) - \\sin x - 1 = -2\\sin^2 x - \\sin x + 1 = (1 - 2\\sin x)(\\sin x + 1)$.\\\\
            Khi đó biểu thức hàm số trở thành:\\\\
            $f(x) = \\frac{\\cos x (1 - 2\\sin x)}{(1 - 2\\sin x)(\\sin x + 1)} = \\frac{\\cos x}{\\sin x + 1}$.''')

            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            th_da_1_d = '\\True Đồ thị hàm số đi qua điểm $(0;1)$'
            th_da_1_s = 'Đồ thị hàm số đi qua điểm $(0;0)$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            loigiai_th_1 = ('''Thay tọa độ điểm hoành độ $x = 0$ vào hàm số đã rút gọn ta được:\\\\
            $f(0) = \\frac{\\cos 0}{\\sin 0 + 1} = \\frac{1}{0 + 1} = 1$.\\\\
            Do đó đồ thị hàm số đi qua điểm $(0;1)$.''')

            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng ############################################
            vd_da_1_s = 'Hàm số đã cho là hàm số chẵn'
            vd_da_1_d = '\\True Hàm số đã cho không phải là hàm số chẵn cũng không phải là hàm số lẻ'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = ('''Xét biểu thức rút gọn $f(x) = \\frac{\\cos x}{\\sin x + 1}$.\\\\
            Ta có $f(-x) = \\frac{\\cos(-x)}{\\sin(-x) + 1} = \\frac{\\cos x}{-\\sin x + 1}$.\\\\
            Nhận thấy $f(-x) \\neq f(x)$ và $f(-x) \\neq -f(x)$.\\\\
            Vậy hàm số đã cho không phải là hàm số chẵn cũng không phải là hàm số lẻ.''')

            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao ############################################
            vdc_da_1_d = '\\True Phương trình $f(x) = %s$ có %s' % (str_val_d, so_diem_dung)
            vdc_da_1_s = 'Phương trình $f(x) = %s$ có %s' % (str_val_d, so_diem_sai)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = ('''Điều kiện xác định của hàm số là: $\\left\\{\\begin{aligned} & 1 - 2\\sin x \\neq 0 \\\\ & \\sin x + 1 \\neq 0 \\end{aligned}\\right. \\Leftrightarrow \\left\\{\\begin{aligned} & \\sin x \\neq \\frac{1}{2} \\\\ & \\sin x \\neq -1 \\end{aligned}\\right.$\\\\
            %s''' % (loigiai_d_chi_tiet))

            list_vdc_2 = [loigiai_vdc_1]

            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
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
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


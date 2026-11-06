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


def bt_dang10_p2_b4_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Random tham số số hạng hằng số tự do c (trong bài gốc c = 4)
            c = randint(2, 6)

            # Các giá trị tính toán đồng bộ theo c
            c_cong_nua = Rational(2*c + 1, 2)
            c_hangso_habac = c_cong_nua

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hàm số lượng giác $f(x) = \\sin^2 x + %s$.''' 
                             %(latex(c)))

            ########################################################################
            # Nhận biết ############################################
            # Ý a: Biến đổi f(x) qua công thức hạ bậc: sin^2 x = (1 - cos 2x)/2 => f(x) = c + 1/2 - 1/2*cos 2x = c_hangso_habac - 1/2*cos 2x
            # Mệnh đề gốc ghi 5 - cos 2x (sai hệ số), ta tổng quát mệnh đề sai và mệnh đề đúng
            nb_da_1_d = 'Hàm số $f(x) = %s - \\cos 2x$' %(latex(c + 1))
            nb_da_1_s = '\\True Hàm số $f(x) = %s - \\frac{1}{2}\\cos 2x$' %(latex(c_cong_nua).replace('.', ','))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = ('''Sử dụng công thức hạ bậc ta có: $\\sin^2 x = \\frac{1 - \\cos 2x}{2} = \\frac{1}{2} - \\frac{1}{2}\\cos 2x$.\\\\'''
                            '''Thay vào biểu thức hàm số: $f(x) = \\frac{1}{2} - \\frac{1}{2}\\cos 2x + %s = %s - \\frac{1}{2}\\cos 2x$.'''
                            %(latex(c), latex(c_cong_nua).replace('.', ',')))

            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            # Ý b: Hàm số đã cho là hàm số chẵn và có chu kỳ bằng \pi
            th_da_1_d = '\\True Hàm số đã cho là hàm số chẵn và có chu kỳ bằng $\\pi$'
            th_da_1_s = 'Hàm số đã cho là hàm số lẻ và có chu kỳ bằng $2\\pi$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            loigiai_th_1 = ('''Xét tính chẵn lẻ: $f(-x) = \\sin^2(-x) + %s = (-\\sin x)^2 + %s = \\sin^2 x + %s = f(x)$, do đó hàm số là hàm số chẵn.\\\\'''
                            '''Xét tính tuần hoàn: Hàm số $y = \\cos 2x$ tuần hoàn với chu kỳ $T = \\frac{2\\pi}{2} = \\pi$. Do đó hàm số $f(x)$ tuần hoàn với chu kỳ $\\pi$. Khẳng định này đúng.'''
                            %(latex(c), latex(c), latex(c)))

            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## 
            # Vận dụng ############################################
            # Ý c: Đồ thị hàm số luôn nằm trong khoảng giữa hai đường thẳng cách nhau một khoảng bằng 1
            # Vì 0 <= sin^2 x <= 1 => c <= f(x) <= c + 1. Đồ thị luôn nằm giữa y = c và y = c + 1, khoảng cách giữa hai đường này là (c+1) - c = 1
            vd_da_1_d = '\\True Đồ thị hàm số đã cho luôn nằm trong khoảng giữa hai đường thẳng cách nhau một khoảng bằng $1$'
            vd_da_1_s = 'Đồ thị hàm số đã cho luôn nằm trong khoảng giữa hai đường thẳng cách nhau một khoảng bằng %s' %(latex(c))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = ('''Ta luôn có điều kiện: $0 \\le \\sin^2 x \\le 1 \\Leftrightarrow 0 + %s \\le \\sin^2 x + %s \\le 1 + %s \\Leftrightarrow %s \\le f(x) \\le %s$.\\\\'''
                            '''Như vậy, đồ thị của hàm số luôn luôn nằm giới hạn giữa hai đường thẳng nằm ngang là $y = %s$ và $y = %s$.\\\\'''
                            '''Khoảng cách giữa hai đường thẳng song song này bằng: $%s - %s = 1$. Do đó khẳng định này đúng.'''
                            %(latex(c), latex(c), latex(c), latex(c), latex(c + 1), latex(c), latex(c + 1), latex(c + 1), latex(c)))

            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## 
            # Vận dụng cao ############################################
            # Ý d: Phương trình f(x) = 5 sin x <=> sin^2 x - 5 sin x + c = 0
            # Với c = 4: sin^2 x - 5 sin x + 4 = 0 <=> sin x = 1 hoặc sin x = 4 (loại) => sin x = 1 có 1 điểm biểu diễn trên đường tròn lượng giác (Đúng)
            # Nếu c chọn ngẫu nhiên khác 4, ta đổi vế phải thành (c + 1) * sin x để đưa về dạng sin^2 x - (c+1) sin x + c = 0 <=> sin x = 1 hoặc sin x = c (loại)
            vế_phải_sin = c + 1
            vdc_da_1_d = '\\True Phương trình $f(x) = %s\\sin x$ có $1$ điểm biểu diễn trên vòng tròn lượng giác' %(latex(vế_phải_sin))
            vdc_da_1_s = 'Phương trình $f(x) = %s\\sin x$ có $2$ điểm biểu diễn trên vòng tròn lượng giác' %(latex(vế_phải_sin))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = ('''Ta xét phương trình: $f(x) = %s\\sin x \\Leftrightarrow \\sin^2 x + %s = %s\\sin x \\Leftrightarrow \\sin^2 x - %s\\sin x + %s = 0$.\\\\'''
                             '''Đặt $t = \\sin x$ với điều kiện $-1 \\le t \\le 1$, phương trình trở thành: $t^2 - %st + %s = 0 \\Leftrightarrow \\left[ \\begin{aligned} &t = 1 \\text{ (thỏa mãn)} \\\\ &t = %s \\text{ (loại vì } %s > 1) \\end{aligned} \\right.$\\\\'''
                             '''Với $t = 1 \\Leftrightarrow \\sin x = 1 \\Leftrightarrow x = \\frac{\\pi}{2} + k2\\pi$ ($k \\in \\mathbb{Z}$).\\\\'''
                             '''Họ nghiệm này chỉ được biểu diễn bởi duy nhất $1$ điểm cuối nằm trên trục tung của vòng tròn lượng giác. Khẳng định trên là đúng.'''
                             %(latex(vế_phải_sin), latex(c), latex(vế_phải_sin), latex(vế_phải_sin), latex(c), latex(vế_phải_sin), latex(c), latex(c), latex(c)))

            list_vdc_2 = [loigiai_vdc_1]

            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Vòng lặp kiểm tra để đảm bảo số lượng đáp án đúng nằm trong khoảng từ 1 đến 3
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Thiết lập lại danh sách sau khi lọc thỏa mãn điều kiện
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

            # Xuất câu hỏi và lời giải chi tiết theo đúng định dạng mẫu khung chương trình đề ra
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


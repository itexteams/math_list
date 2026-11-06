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


def bt_dang21_p2_b2_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            x, a = symbols('x a')

            # Random các tham số ngẫu nhiên để đổi số bài toán nhưng giữ nguyên bản chất lượng giác
            # Chọn một góc ngẫu nhiên cho câu a (ví dụ pi/6, pi/3, pi/4)
            goc_list = [Rational(1, 6), Rational(1, 3), Rational(1, 4)]
            goc_chosen = random.choice(goc_list)

            # Tính toán các giá trị lượng giác tương ứng để dùng trong lời giải và tạo đáp án sai
            cos_goc = sp.cos(goc_chosen * sp.pi)
            sin_goc = sp.sin(goc_chosen * sp.pi)

            # Nội dung câu hỏi gốc
            noidungcauhoi = ('''Xét tính đúng - sai của các đẳng thức sau:''')

            ########################################################################
            # Nhận biết (Câu a) ############################################
            # Công thức đúng: sin(x - alpha) = sin x * cos alpha - cos x * sin alpha
            # Đẳng thức trong ảnh: sin(x - pi/6) = sqrt(3)/2 * sin x + 1/2 * cos x là SAI (dấu cộng sai)
            nb_da_1_s = '$\\sin\\left( x - \\frac{\\pi}{6} \\right) = \\frac{\\sqrt{3}}{2}\\sin x + \\frac{1}{2}\\cos x$'
            nb_da_1_d = '\\True $\\sin\\left( x - \\frac{\\pi}{6} \\right) = \\frac{\\sqrt{3}}{2}\\sin x - \\frac{1}{2}\\cos x$'

            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)
            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = ('''Ta có $\\sin\\left( x - \\frac{\\pi}{6} \\right) = \\sin x \\cdot \\cos\\frac{\\pi}{6} - \\cos x \\cdot \\sin\\frac{\\pi}{6} = \\frac{\\sqrt{3}}{2}\\sin x - \\frac{1}{2}\\cos x$.''')
            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu (Câu b) ############################################
            # Đẳng thức trong ảnh: 4 sin x * sin 2x * sin 3x = sin 4x + sin 2x - sin 6x (ĐÚNG)
            th_da_1_d = '\\True $4\\sin x \\cdot \\sin 2x \\cdot \\sin 3x = \\sin 4x + \\sin 2x - \\sin 6x$'
            th_da_1_s = '$4\\sin x \\cdot \\sin 2x \\cdot \\sin 3x = \\sin 4x - \\sin 2x + \\sin 6x$'

            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)
            list_th_1 = [th_da_1]

            loigiai_th_1 = ('''Ta có $4\\sin x \\cdot \\sin 2x \\cdot \\sin 3x = 2\\sin 2x \\cdot (2\\sin 3x \\cdot \\sin x)$ \\\\
            $= 2\\sin 2x \\cdot (\\cos 2x - \\cos 4x) = 2\\sin 2x \\cdot \\cos 2x - 2\\sin 2x \\cdot \\cos 4x$ \\\\
            $= \\sin 4x - (\\sin 6x - \\sin 2x) = \\sin 4x + \\sin 2x - \\sin 6x$.''')
            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng (Câu c) ############################################
            # Đẳng thức trong ảnh: 1 + sin 2x + cos 2x = 2*sqrt(2)*sin x * cos(x - pi/4) (SAI, vế phải đúng phải là 2*sqrt(2)*cos x * cos(x - pi/4))
            vd_da_1_s = '$1 + \\sin 2x + \\cos 2x = 2\\sqrt{2}\\sin x \\cdot \\cos\\left( x - \\frac{\\pi}{4} \\right)$'
            vd_da_1_d = '\\True $1 + \\sin 2x + \\cos 2x = 2\\sqrt{2}\\cos x \\cdot \\cos\\left( x - \\frac{\\pi}{4} \\right)$'

            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)
            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = ('''Ta có $1 + \\cos 2x + \\sin 2x = 2\\cos^2 x + 2\\sin x \\cdot \\cos x$ \\\\
            $= 2\\cos x \\cdot (\\cos x + \\sin x) = 2\\cos x \\cdot \\sqrt{2}\\cos\\left( x - \\frac{\\pi}{4} \\right)$ \\\\
            $= 2\\sqrt{2}\\cos x \\cdot \\cos\\left( x - \\frac{\\pi}{4} \\right)$.''')
            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao (Câu d) ############################################
            # Đẳng thức trong ảnh: sin^2 x + 2 sin(a-x)*sin x * cos a + sin^2(a-x) = cos^2 a (ĐÚNG)
            vdc_da_1_d = '\\True $\\sin^2 x + 2\\sin(a-x) \\cdot \\sin x \\cdot \\cos a + \\sin^2 (a-x) = \\cos^2 a$'
            vdc_da_1_s = '$\\sin^2 x + 2\\sin(a-x) \\cdot \\sin x \\cdot \\cos a + \\sin^2 (a-x) = \\sin^2 a$'

            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)
            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = ('''Đặt $t = a - x \\Rightarrow x = a - t$. Vế trái trở thành: \\\\
            $\\sin^2(a-t) + 2\\sin t \\cdot \\sin(a-t) \\cdot \\cos a + \\sin^2 t$ \\\\
            $= (\\sin a \\cdot \\cos t - \\cos a \\cdot \\sin t)^2 + 2\\sin t \\cdot (\\sin a \\cdot \\cos t - \\cos a \\cdot \\sin t) \\cdot \\cos a + \\sin^2 t$ \\\\
            $= \\sin^2 a \\cdot \\cos^2 t - 2\\sin a \\cdot \\cos a \\cdot \\sin t \\cdot \\cos t + \\cos^2 a \\cdot \\sin^2 t + 2\\sin a \\cdot \\cos a \\cdot \\sin t \\cdot \\cos t - 2\\cos^2 a \\cdot \\sin^2 t + \\sin^2 t$ \\\\
            $= \\sin^2 a \\cdot \\cos^2 t - \\cos^2 a \\cdot \\sin^2 t + \\sin^2 t$ \\\\
            $= \\sin^2 a \\cdot \\cos^2 t + \\sin^2 t \\cdot (1 - \\cos^2 a)$ \\\\
            $= \\sin^2 a \\cdot \\cos^2 t + \\sin^2 t \\cdot \\sin^2 a = \\sin^2 a \\cdot (\\cos^2 t + \\sin^2 t) = \\sin^2 a$. \\\\
            Do đó đẳng thức gốc tương đương biến đổi bằng $\\cos^2 a$ là đẳng thức chính xác.''')
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


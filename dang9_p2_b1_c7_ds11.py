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


def bt_dang9_p2_b1_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến
            t = symbols('t')

            # B3-Suy nghĩ tìm cách random bài toán
            # Để bài toán có nghiệm đẹp, ta thiết lập từ gia tốc và vận tốc
            # a(t) = 6(t - t_a0) => Gia tốc triệt tiêu tại t_a0 (nguyên)
            # v(t) = 3t^2 - 6*t_a0*t + B. Cho v(t) triệt tiêu tại t_v0 (nguyên)
            # B = 6*t_a0*t_v0 - 3*t_v0**2
            t_a0 = random.randint(1, 2) # Thời điểm gia tốc triệt tiêu
            t_v0 = t_a0 + random.randint(2, 3) # Thời điểm vận tốc triệt tiêu (t_v0 > t_a0)

            coeff_A = -3 * t_a0
            coeff_B = 6 * t_a0 * t_v0 - 3 * t_v0**2

            s_func = t**3 + coeff_A * t**2 + coeff_B * t
            v_func = diff(s_func, t)
            a_func = diff(v_func, t)

            # Hàm định dạng số: thay dấu chấm bằng phẩy và bỏ ,0 theo yêu cầu
            def f_num(val):
                s = str(latex(val)).replace('.', ',')
                if s.endswith(',0'):
                    s = s[:-2]
                return s

            # Các mốc thời gian và giá trị tính toán
            t_a = t_v0 + random.randint(1, 2)
            v_ta = v_func.subs(t, t_a)

            t_b = t_v0
            a_tb = a_func.subs(t, t_b)

            a_at_v0 = a_func.subs(t, t_v0)
            v_at_a0 = v_func.subs(t, t_a0)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một vật chuyển động thẳng xác định bởi phương trình $s = s\\left( t \\right) = %s$ trong đó $t$ được tính bằng giây và $s$ được tính bằng mét.''' 
                             % (latex(s_func)))

            ########################################################################
            # a) Vận tốc tại thời điểm t_a
            nb_da_1_d = '\\True Vận tốc của vật tại thời điểm $t = %ss$ là %sm/s' % (f_num(t_a), f_num(v_ta))
            nb_da_1_s = 'Vận tốc của vật tại thời điểm $t = %ss$ là %sm/s' % (f_num(t_a), f_num(v_ta + 5))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Ta có $v\\left( t \\right) = s'\\left( t \\right) = %s$.\\\\
            Vận tốc của vật tại thời điểm $t = %s$ là $v\\left( %s \\right) = %s\\, m/s$.''' 
                            % (latex(v_func), f_num(t_a), f_num(t_a), f_num(v_ta)))

            ########################################################################
            # b) Gia tốc tại thời điểm t_b
            th_da_1_d = '\\True Gia tốc của vật tại thời điểm $t = %ss$ là %sm/s$^2$' % (f_num(t_b), f_num(a_tb))
            th_da_1_s = 'Gia tốc của vật tại thời điểm $t = %ss$ là %sm/s$^2$' % (f_num(t_b), f_num(a_tb - 6))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Ta có $a\\left( t \\right) = v'\\left( t \\right) = %s$.\\\\
            Gia tốc của vật tại thời điểm $t = %s$ là $a\\left( %s \\right) = %s\\, m/s^2$.''' 
                            % (latex(a_func), f_num(t_b), f_num(t_b), f_num(a_tb)))

            ########################################################################
            # c) Gia tốc tại thời điểm vận tốc triệt tiêu
            vd_da_1_d = '\\True Gia tốc tại thời điểm vận tốc triệt tiêu là %sm/s$^2$' % (f_num(a_at_v0))
            vd_da_1_s = 'Gia tốc tại thời điểm vận tốc triệt tiêu là %sm/s$^2$' % (f_num(a_at_v0 + 2))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Vận tốc triệt tiêu khi $v\\left( t \\right) = 0 \\Leftrightarrow %s = 0 \\Leftrightarrow t = %s$ (do $t > 0$).\\\\
            Khi đó gia tốc của vật là $a\\left( %s \\right) = %s\\, m/s^2$.''' 
                            % (latex(v_func), f_num(t_v0), f_num(t_v0), f_num(a_at_v0)))

            ########################################################################
            # d) Vận tốc tại thời điểm gia tốc triệt tiêu
            vdc_da_1_d = '\\True Vận tốc tại thời điểm gia tốc triệt tiêu là %sm/s' % (f_num(v_at_a0))
            vdc_da_1_s = 'Vận tốc tại thời điểm gia tốc triệt tiêu là %sm/s' % (f_num(v_at_a0 + 4))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Gia tốc triệt tiêu khi $a\\left( t \\right) = 0 \\Leftrightarrow %s = 0 \\Leftrightarrow t = %s$.\\\\
            Khi đó vận tốc của vật là $v\\left( %s \\right) = %s\\, m/s$.''' 
                             % (latex(a_func), f_num(t_a0), f_num(t_a0), f_num(v_at_a0)))

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

            list_nb_1, list_nb_2 = [nb_da_1], [loigiai_nb_1]
            list_th_1, list_th_2 = [th_da_1], [loigiai_th_1]
            list_vd_1, list_vd_2 = [vd_da_1], [loigiai_vd_1]
            list_vdc_1, list_vdc_2 = [vdc_da_1], [loigiai_vdc_1]

            # Xuất câu hỏi
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\\choiceTFn \n'
                '{'+str(list_nb_1[0])+'}\n'
                '{'+str(list_th_1[0])+'}\n'
                '{'+str(list_vd_1[0])+'}\n'
                '{'+str(list_vdc_1[0])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(list_nb_2[0])+'\n'
                '\\item '+str(list_th_2[0])+'\n'
                '\\item '+str(list_vd_2[0])+'\n'
                '\\item '+str(list_vdc_2[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


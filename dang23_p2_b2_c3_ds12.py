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


def bt_dang23_p2_b2_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            t = symbols('t')

            # B3: Random bài toán bằng cách thay đổi hệ số k của gia tốc a(t) = k*cos(t)
            k = randint(2, 8) 
            at = k * cos(t)
            vt = k * sin(t) # Vì v(0) = 0 nên C = 0

            # Nội dung câu hỏi
            noidungcauhoi = (r'''Một vật chuyển động với gia tốc $a(t) = %s \cos t \text{ (m/s}^2)$.''' 
                             % (latex(k)))

            ########################################################################
            # Nhận biết: Xác định công thức vận tốc v(t)
            ########################################################################
            nb_da_1_d = r'\True Công thức vận tốc của vật là $v(t) = %s \sin t$' % (latex(k))
            nb_da_1_s = r'Công thức vận tốc của vật là $v(t) = -%s \sin t$' % (latex(k))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = (r'''Ta có $v(t) = \int a(t) \text{d}t = \int %s \cos t \text{d}t = %s \sin t + C$. \\
                            Mà tại thời điểm bắt đầu chuyển động, vật có vận tốc bằng $0$ nên $v(0)=0 \Rightarrow C=0$. \\
                            Vậy $v(t) = %s \sin t$.''' % (latex(k), latex(k), latex(k)))

            list_nb_1 = [nb_da_1]
            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # Thông hiểu: Tính vận tốc tại t = pi/2
            ########################################################################
            t_th = pi/2
            v_th_val = vt.subs(t, t_th)

            th_da_1_d = r'\True Vận tốc của vật tại thời điểm $t = \frac{\pi}{2}$ là $v\left(\frac{\pi}{2}\right) = %s \text{ (m/s)}$' % (latex(v_th_val))
            th_da_1_s = r'Vận tốc của vật tại thời điểm $t = \frac{\pi}{2}$ là $v\left(\frac{\pi}{2}\right) = 0 \text{ (m/s)}$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = (r'''Vận tốc của vật tại thời điểm $t = \frac{\pi}{2}$ là $v\left(\frac{\pi}{2}\right) = %s \sin \frac{\pi}{2} = %s \text{ (m/s)}$.''' 
                            % (latex(k), latex(v_th_val)))

            list_th_1 = [th_da_1]
            list_th_2 = [loigiai_th_1]

            ########################################################################
            # Vận dụng: Quãng đường từ t=0 đến t=pi
            ########################################################################
            s_vd = integrate(vt, (t, 0, pi))

            vd_da_1_d = r'\True Quãng đường vật đi được từ $t=0\text{ (s)}$ đến $t=\pi\text{ (s)}$ là $%s\text{ (m)}$' % (latex(s_vd))
            vd_da_1_s = r'Quãng đường vật đi được từ $t=0\text{ (s)}$ đến $t=\pi\text{ (s)}$ là $0\text{ (m)}$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = (r'''Quãng đường vật đi được từ thời điểm $t=0\text{ (s)}$ đến $t=\pi\text{ (s)}$ là: \\
                            $\int_{0}^{\pi} v(t) \text{d}t = \int_{0}^{\pi} %s \sin t \text{d}t = -%s \cos t \big|_0^{\pi} = -%s \cos \pi - (-%s \cos 0) = %s\text{ (m)}$.''' 
                            % (latex(k), latex(k), latex(k), latex(k), latex(s_vd)))

            list_vd_1 = [vd_da_1]
            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # Vận dụng cao: Quãng đường từ t=pi/2 đến t=3pi/4
            ########################################################################
            t_start = pi/2
            t_end = 3*pi/4
            s_vdc = integrate(vt, (t, t_start, t_end))

            vdc_da_1_d = r'\True Quãng đường vật đi được từ $t=\frac{\pi}{2}\text{ (s)}$ đến $t=\frac{3\pi}{4}\text{ (s)}$ là $%s\text{ (m)}$' % (latex(s_vdc))
            vdc_da_1_s = r'Quãng đường vật đi được từ $t=\frac{\pi}{2}\text{ (s)}$ đến $t=\frac{3\pi}{4}\text{ (s)}$ là $%s\text{ (m)}$' % (latex(2*s_vdc))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = (r'''Quãng đường vật đi được từ thời điểm $t=\frac{\pi}{2}\text{ (s)}$ đến $t=\frac{3\pi}{4}\text{ (s)}$ là: \\
                             $\int_{\frac{\pi}{2}}^{\frac{3\pi}{4}} v(t) \text{d}t = \int_{\frac{\pi}{2}}^{\frac{3\pi}{4}} %s \sin t \text{d}t = -%s \cos t \big|_{\frac{\pi}{2}}^{\frac{3\pi}{4}} = -%s \cos \frac{3\pi}{4} - (-%s \cos \frac{\pi}{2}) = %s\text{ (m)}$.''' 
                             % (latex(k), latex(k), latex(k), latex(k), latex(s_vdc)))

            list_vdc_1 = [vdc_da_1]
            list_vdc_2 = [loigiai_vdc_1]

            # --- Xử lý xáo trộn và xuất kết quả tương tự mẫu ---

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                ans_nb = random.choice(list_nb_da_1)
                ans_th = random.choice(list_th_da_1)
                ans_vd = random.choice(list_vd_da_1)
                ans_vdc = random.choice(list_vdc_da_1)

                current_answers = [ans_nb, ans_th, ans_vd, ans_vdc]
                if 1 <= count_true_answers(current_answers) <= 3:
                    break

            # Đóng gói và in kết quả
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(ans_nb) + '}\n'
                '{' + str(ans_th) + '}\n'
                '{' + str(ans_vd) + '}\n'
                '{' + str(ans_vdc) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


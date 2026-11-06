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


def bt_dang10_p2_b2_c7_ds11(self):
            # Khai báo biến
            # Khai báo biến
            t = symbols('t')

            # Random tham số cho hàm s(t) = -t^3 + 3kt^2 + (9k^2)t + d
            # Để v(t) = -3t^2 + 6kt + 9k^2 có nghiệm đẹp là -k và 3k
            k = randint(1, 3)
            d = randint(2, 5)

            s_func = -t**3 + 3*k*t**2 + 9*k**2*t + d
            v_func = diff(s_func, t)
            a_func = diff(v_func, t)

            # Các giá trị tính toán
            t_vmax = k
            v_max = v_func.subs(t, t_vmax)
            t_dung = 3*k
            s_dung = s_func.subs(t, t_dung) - s_func.subs(t, 0)
            t_check = 2*k
            v_check = v_func.subs(t, t_check)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một vật chuyển động trên đường thẳng được xác định bởi công thức $s\\left( t \\right)=%s$, trong đó $t>0$ và tính bằng giây và $s$ là quãng đường chuyển động được của vật trong $t$ giây tính bằng mét.''' 
                             %(latex(s_func)))

            ########################################################################
            # Nhận biết (Vận tốc tại thời điểm cụ thể)
            nb_da_1_d = '\\True Vận tốc tức thời của vật tại thời điểm $t = %s$ là $%s$ (m/s)' %(latex(t_check), latex(v_check))
            nb_da_1_s = 'Vận tốc tức thời của vật tại thời điểm $t = %s$ là $%s$ (m/s)' %(latex(t_check), latex(v_check + randint(1, 3)))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ('''Vận tốc của vật là $v\\left( t \\right)=s\'\\left( t \\right)=%s$. \\\\ Tại thời điểm $t=%s$, vận tốc của vật là $v\\left( %s \\right)=%s$ (m/s).''' 
                            %(latex(v_func), latex(t_check), latex(t_check), latex(v_check)))

            ########################################################################
            # Thông hiểu (Vận tốc cực đại)
            th_da_1_d = '\\True Vận tốc cực đại của chuyển động là %s (m/s)' %(latex(v_max))
            th_da_1_s = 'Vận tốc cực đại của chuyển động là %s (m/s)' %(latex(v_max + randint(2, 5)))
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ('''Ta có $v\'\\left( t \\right)=a\\left( t \\right)=%s$. \\\\ $v\'\\left( t \\right)=0 \\Leftrightarrow t=%s$. \\\\ Vận tốc cực đại của vật là $v\\left( %s \\right)=%s$ (m/s).''' 
                            %(latex(a_func), latex(t_vmax), latex(t_vmax), latex(v_max)))

            ########################################################################
            # Vận dụng (Quãng đường cho đến khi dừng)
            vd_da_1_d = '\\True Quãng đường của vật đi được từ thời điểm bắt đầu chuyển động cho đến lúc dừng lại là %s (m)' %(latex(s_dung))
            vd_da_1_s = 'Quãng đường của vật đi được từ thời điểm bắt đầu chuyển động cho đến lúc dừng lại là %s (m)' %(latex(s_dung + randint(1, 5)))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ('''Vật dừng lại khi $v\\left( t \\right)=0 \\Leftrightarrow %s=0 \\Leftrightarrow t=%s$ (vì $t>0$). \\\\ Quãng đường vật đi được là $s\\left( %s \\right)-s\\left( 0 \\right)=%s-%s=%s$ (m).''' 
                            %(latex(v_func), latex(t_dung), latex(t_dung), latex(s_func.subs(t, t_dung)), latex(d), latex(s_dung)))

            ########################################################################
            # Vận dụng cao (Gia tốc tại thời điểm v max)
            vdc_da_1_d = '\\True Gia tốc của vật khi vận tốc đạt cực đại bằng 0'
            vdc_da_1_s = 'Gia tốc của vật khi vận tốc đạt cực đại bằng %s' %(latex(randint(1, 5)))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = ('''Vận tốc đạt cực đại tại $t=%s$. \\\\ Khi đó gia tốc của vật là $a\\left( %s \\right)=%s$.''' 
                             %(latex(t_vmax), latex(t_vmax), latex(a_func.subs(t, t_vmax))))

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

            # Gán lại vào list và xáo trộn lời giải tương ứng
            list_nb_1, list_nb_2 = [nb_da_1], [loigiai_nb_1]
            list_th_1, list_th_2 = [th_da_1], [loigiai_th_1]
            list_vd_1, list_vd_2 = [vd_da_1], [loigiai_vd_1]
            list_vdc_1, list_vdc_2 = [vdc_da_1], [loigiai_vdc_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            combined_th = list(zip(list_th_1, list_th_2))
            combined_vd = list(zip(list_vd_1, list_vd_2))
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # Xuất nội dung
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


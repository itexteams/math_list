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


def bt_dang14_p2_b3_c1_hh12(self):
    while True:
        vt_AC_x = random.randint(-4, 4)
        vt_AC_y = random.randint(-4, 4)
        vt_AC_z = random.randint(-4, 4)
        vt_BC_x = random.randint(-4, 4)
        vt_BC_y = random.randint(-4, 4)
        vt_BC_z = random.randint(-4, 4)
        if (vt_AC_x*vt_BC_x + vt_AC_y*vt_BC_y + vt_AC_z*vt_BC_z == 0) and (vt_AC_x!=0 or vt_AC_y!=0 or vt_AC_z!=0) and (vt_BC_x!=0 or vt_BC_y!=0 or vt_BC_z!=0) and vt_BC_y != 0:
            x_C = random.randint(-3, 3)
            y_C = random.randint(-3, 3)
            z_C = random.randint(-3, 3)
            x_A = x_C - vt_AC_x
            y_A = y_C - vt_AC_y
            z_A = z_C - vt_AC_z
            x_B = x_C - vt_BC_x
            y_B = y_C - vt_BC_y
            z_B = z_C - vt_BC_z
            k_val = Rational(-y_B, vt_BC_y)
            c_val = z_B + k_val * vt_BC_z
            if c_val != 0:
                break
    vt_AB_x = x_B - x_A
    vt_AB_y = y_B - y_A
    vt_AB_z = z_B - z_A
    AC_sq = vt_AC_x**2 + vt_AC_y**2 + vt_AC_z**2
    BC_sq = vt_BC_x**2 + vt_BC_y**2 + vt_BC_z**2
    S_val = sp.sqrt(AC_sq * BC_sq) / 2
    dot_AB_AC = vt_AB_x * vt_AC_x + vt_AB_y * vt_AC_y + vt_AB_z * vt_AC_z
    x_G = Rational(x_A + x_B + x_C, 3)
    y_G = Rational(y_A + y_B + y_C, 3)
    z_G = Rational(z_A + z_B + z_C, 3)
    a_val = x_B + k_val * vt_BC_x
    expr_val = 2 * a_val / c_val
    noidungcauhoi = ('''Trong không gian $Oxyz$, cho tam giác $ABC$ với $A(%s;%s;%s)$, $B(%s;%s;%s)$ và $C(%s;%s;%s)$.'''%(latex(x_A), latex(y_A), latex(z_A), latex(x_B), latex(y_B), latex(z_B), latex(x_C), latex(y_C), latex(z_C)))
    nb_da_1_d = '\\True Diện tích của tam giác $ABC$ bằng $%s$' %(latex(S_val))
    nb_da_1_s = 'Diện tích của tam giác $ABC$ bằng $%s$' %(latex(S_val / 2))
    list_nb_da_1=[nb_da_1_d,nb_da_1_s]
    nb_da_1=random.choice(list_nb_da_1)
    list_nb_1 = [nb_da_1]
    loigiai_nb_1 = ('''Ta có: $\\overrightarrow{AC}=(%s;%s;%s)$, $\\overrightarrow{BC}=(%s;%s;%s)$.\\\\ Khi đó $\\overrightarrow{AC}.\\overrightarrow{BC}=0 \\Rightarrow AC \\perp BC \\Rightarrow S_{\\Delta ABC} = \\frac{1}{2}AC.BC = %s$.'''%(latex(vt_AC_x), latex(vt_AC_y), latex(vt_AC_z), latex(vt_BC_x), latex(vt_BC_y), latex(vt_BC_z), latex(S_val)))
    list_nb_2 = [loigiai_nb_1]
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    th_da_1_d = '\\True $\\overrightarrow{AB}.\\overrightarrow{AC} = %s$' %(latex(dot_AB_AC))
    th_da_1_s = '$\\overrightarrow{AB}.\\overrightarrow{AC} = %s$' %(latex(dot_AB_AC + random.choice([-2, 2, 3])))
    list_th_da_1=[th_da_1_d,th_da_1_s]
    th_da_1=random.choice(list_th_da_1)
    list_th_1 = [th_da_1]
    loigiai_th_1 = ('''Ta có $\\overrightarrow{AB}=(%s;%s;%s)$, $\\overrightarrow{AC}=(%s;%s;%s) \\Rightarrow \\overrightarrow{AB}.\\overrightarrow{AC} = %s$.'''%(latex(vt_AB_x), latex(vt_AB_y), latex(vt_AB_z), latex(vt_AC_x), latex(vt_AC_y), latex(vt_AC_z), latex(dot_AB_AC)))
    list_th_2 = [loigiai_th_1]
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    vd_da_1_d = '\\True Tọa độ trọng tâm tam giác $ABC$ là $G\\left(%s;%s;%s\\right)$' %(latex(x_G), latex(y_G), latex(z_G))
    vd_da_1_s = 'Tọa độ trọng tâm tam giác $ABC$ là $G\\left(%s;%s;%s\\right)$' %(latex(x_G), latex(y_G + 1), latex(z_G))
    list_vd_da_1=[vd_da_1_d,vd_da_1_s]
    vd_da_1=random.choice(list_vd_da_1)
    list_vd_1 = [vd_da_1]
    loigiai_vd_1 = ('''Tọa độ trọng tâm $G$ của tam giác $ABC$ được xác định bởi: $\\begin{cases} x_G = \\frac{x_A+x_B+x_C}{3} = %s \\\\ y_G = \\frac{y_A+y_B+y_C}{3} = %s \\\\ z_G = \\frac{z_A+z_B+z_C}{3} = %s \\end{cases}$.'''%(latex(x_G), latex(y_G), latex(z_G)))
    list_vd_2 = [loigiai_vd_1]
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    vdc_da_1_d = '\\True Gọi điểm $E(a;b;c)$ là giao điểm của đường thẳng $BC$ với mặt phẳng tọa độ $(Oxz)$, khi đó $\\frac{2a}{c} + b = %s$' %(latex(expr_val))
    vdc_da_1_s = 'Gọi điểm $E(a;b;c)$ là giao điểm của đường thẳng $BC$ với mặt phẳng tọa độ $(Oxz)$, khi đó $\\frac{2a}{c} + b = %s$' %(latex(expr_val + Rational(1,2)))
    list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
    vdc_da_1=random.choice(list_vdc_da_1)
    list_vdc_1 = [vdc_da_1]
    loigiai_vdc_1 = ('''Vì $E(a;b;c) \\in (Oxz) \\Rightarrow b=0$. Ta có $\\overrightarrow{BC}=(%s;%s;%s)$, $\\overrightarrow{BE}=(a-(%s);%s;c-(%s))$.\\\\ Vì $B, C, E$ thẳng hàng nên: $k.\\overrightarrow{BC} = \\overrightarrow{BE} \\Rightarrow \\begin{cases} %sk = a-(%s) \\\\ %sk = %s \\\\ %sk = c-(%s) \\end{cases} \\Leftrightarrow \\begin{cases} k = %s \\\\ a = %s \\\\ c = %s \\end{cases}$.\\\\ Suy ra: $\\frac{2a}{c} + b = %s$.'''%(latex(vt_BC_x), latex(vt_BC_y), latex(vt_BC_z), latex(x_B), latex(-y_B), latex(z_B), latex(vt_BC_x), latex(x_B), latex(vt_BC_y), latex(-y_B), latex(vt_BC_z), latex(z_B), latex(k_val), latex(a_val), latex(c_val), latex(expr_val)))
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
        true_count = count_true_answers(answers)
        if 1 <= true_count <= 3:
            break
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
    content = ('\\begin{minipage}{\\textwidth} \n''\\begin{ex}\n'+str(noidungcauhoi)+ '\n''\\choiceTFn \n''{'+str(shuffled_answers_nb[0])+'}\n''{'+str(shuffled_answers_th[0])+'}\n''{'+str(shuffled_answers_vd[0])+'}\n''{'+str(shuffled_answers_vdc[0])+'}\n''\\loigiai{ \n''\\begin{enumEX}[a)]{1} \n''\\item '+str(shuffled_solutions_nb[0])+'\n''\\item '+str(shuffled_solutions_th[0])+'\n''\\item '+str(shuffled_solutions_vd[0])+'\n''\\item '+str(shuffled_solutions_vdc[0])+'\n''\\end{enumEX}} \n''\\end{ex}\n \\end{minipage}\n\n')
    return content


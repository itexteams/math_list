
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


def bt_dang15_p2_b2_c2_hh10(self):
    k = 2 * random.randint(1, 5)
    m = k // 2
    canh = '%sa' % k
    ad2 = '%sa^2' % (k ** 2)
    de2 = 'a^2' if m == 1 else '%sa^2' % (m ** 2)
    noidungcauhoi = 'Cho hình vuông $ABCD$ có cạnh bằng $%s$. Xét tính đúng sai của các khẳng định sau:' % canh
    nb_v1, nb_v2, nb_kq_d, nb_kq_s = random.choice([('AB', 'BC', 'AC', 'CA'), ('AD', 'DC', 'AC', 'CA'), ('BA', 'AD', 'BD', 'DB'), ('BC', 'CD', 'BD', 'DB')])
    nb_da_1_d = '\\True $\\overrightarrow{%s} + \\overrightarrow{%s} = \\overrightarrow{%s}$' % (nb_v1, nb_v2, nb_kq_d)
    nb_da_1_s = '$\\overrightarrow{%s} + \\overrightarrow{%s} = \\overrightarrow{%s}$' % (nb_v1, nb_v2, nb_kq_s)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    list_nb_1 = [nb_da_1]
    loigiai_nb_1 = 'Ta có theo quy tắc ba điểm: $\\overrightarrow{%s} + \\overrightarrow{%s} = \\overrightarrow{%s}$.' % (nb_v1, nb_v2, nb_kq_d)
    list_nb_2 = [loigiai_nb_1]
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    th_v1, th_v2, th_kq = random.choice([('AB', 'AC', 'CB'), ('AD', 'AC', 'CD'), ('BA', 'BD', 'DA'), ('BC', 'BD', 'DC'), ('DA', 'DB', 'BA'), ('DC', 'DB', 'BC')])
    th_s_val = random.choice(['%sa\\sqrt{2}' % k, '%sa' % (2 * k)])
    th_da_1_d = '\\True $\\left|\\overrightarrow{%s} - \\overrightarrow{%s}\\right| = %s$' % (th_v1, th_v2, canh)
    th_da_1_s = '$\\left|\\overrightarrow{%s} - \\overrightarrow{%s}\\right| = %s$' % (th_v1, th_v2, th_s_val)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    list_th_1 = [th_da_1]
    loigiai_th_1 = 'Ta có theo quy tắc trừ: $\\left|\\overrightarrow{%s} - \\overrightarrow{%s}\\right| = \\left|\\overrightarrow{%s}\\right| = %s = %s$.' % (th_v1, th_v2, th_kq, th_kq, canh)
    list_th_2 = [loigiai_th_1]
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    vd_v1, vd_v2 = random.choice([('AB', 'CD'), ('BA', 'DC'), ('AD', 'CB'), ('DA', 'BC')])
    vd_s_val = random.choice([canh, '%sa' % (2 * k)])
    vd_da_1_d = '\\True $\\left|\\overrightarrow{%s} + \\overrightarrow{%s}\\right| = 0$' % (vd_v1, vd_v2)
    vd_da_1_s = '$\\left|\\overrightarrow{%s} + \\overrightarrow{%s}\\right| = %s$' % (vd_v1, vd_v2, vd_s_val)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    list_vd_1 = [vd_da_1]
    loigiai_vd_1 = 'Ta có $\\left|\\overrightarrow{%s} + \\overrightarrow{%s}\\right| = \\left|\\overrightarrow{%s} - \\overrightarrow{%s}\\right| = \\left|\\overrightarrow{0}\\right| = 0$.' % (vd_v1, vd_v2, vd_v1, vd_v1)
    list_vd_2 = [loigiai_vd_1]
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    vdc_v1, vdc_v2, vdc_doan, vdc_goc, vdc_nua = random.choice([('AD', 'AC', 'CD', 'A', 'DE'), ('AB', 'AC', 'BC', 'A', 'BE'), ('BA', 'BD', 'AD', 'B', 'AE'), ('BC', 'BD', 'CD', 'B', 'CE'), ('CB', 'CA', 'AB', 'C', 'BE'), ('CD', 'CA', 'AD', 'C', 'DE')])
    vdc_s_val = random.choice(['%sa\\sqrt{3}' % k, '%sa\\sqrt{2}' % k])
    vdc_da_1_d = '\\True $\\left|\\overrightarrow{%s} + \\overrightarrow{%s}\\right| = %sa\\sqrt{5}$' % (vdc_v1, vdc_v2, k)
    vdc_da_1_s = '$\\left|\\overrightarrow{%s} + \\overrightarrow{%s}\\right| = %s$' % (vdc_v1, vdc_v2, vdc_s_val)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    list_vdc_1 = [vdc_da_1]
    loigiai_vdc_1 = 'Gọi $E$ là trung điểm của $%s$, theo tính chất trung điểm đoạn thẳng ta có: $\\left|\\overrightarrow{%s} + \\overrightarrow{%s}\\right| = 2\\left|\\overrightarrow{%sE}\\right| = 2\\sqrt{%s^2 + %s^2} = 2\\sqrt{%s + %s} = %sa\\sqrt{5}$.' % (vdc_doan, vdc_v1, vdc_v2, vdc_goc, vdc_v1, vdc_nua, ad2, de2, k)
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
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
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
        '\\end{ex}\n \\end{minipage}\n\n')
    return content

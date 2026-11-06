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


def bt_dang5_p2_b5_c1_hh11(self):
    # Khai báo và random tỉ lệ m : n
    # Đề bài gốc: m:n = 2:1 => AD:DB = AE:EC = m:n
    pair = random.choice([(2, 1), (3, 1), (3, 2), (4, 1), (2, 3), (1, 2)])
    m_val, n_val = pair

    # Tỉ lệ AD/DB
    frac_ad_db_d = Rational(m_val, n_val)
    latex_ad_db_d = latex(frac_ad_db_d)
    frac_ad_db_s = Rational(n_val, m_val)
    latex_ad_db_s = latex(frac_ad_db_s)

    # Tỉ lệ DE/BC = AD/AB = m / (m + n)
    frac_de_bc_d = Rational(m_val, m_val + n_val)
    latex_de_bc_d = latex(frac_de_bc_d)
    # Phương án sai cho DE/BC
    wrong_frac_list = [Rational(n_val, m_val + n_val), Rational(n_val, m_val), Rational(1, 2)]
    wrong_frac_list = [f for f in wrong_frac_list if f != frac_de_bc_d]
    frac_de_bc_s = random.choice(wrong_frac_list)
    latex_de_bc_s = latex(frac_de_bc_s)

    # Nội dung câu hỏi
    noidungcauhoi = ('''Trong tam giác $ABC$, lấy $D \\in AB$, $E \\in AC$ sao cho $AD : DB = AE : EC = %s : %s$. Một phép chiếu song song biến các điểm $A, B, C, D, E$ lần lượt thành $A', B', C', D', E'$.''' % (m_val, n_val))

    ###################################################################### Nhận biết ######################################################
    # Mệnh đề a: D' in A'B'
    nb_da_1_d = '\\True $D\' \\in A\'B\'$'
    nb_da_1_s = '$D\' \\notin A\'B\'$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)

    list_nb_1 = [nb_da_1]

    loigiai_nb_1 = ('''Phép chiếu song song bảo toàn tính thẳng hàng và thứ tự của các điểm thẳng hàng. Vì điểm $D$ thuộc đoạn thẳng $AB$ nên hình chiếu $D'$ của $D$ cũng thuộc đoạn thẳng $A'B'$, do đó $D' \\in A'B'$.''')

    list_nb_2 = [loigiai_nb_1]

    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

    ###################################################################### Thông hiểu ######################################################
    # Mệnh đề b: Tỉ số A'D' / D'B'
    th_da_1_s = '$\\dfrac{A\'D\'}{D\'B\'} = %s$' % (latex_ad_db_s)
    th_da_1_d = '\\True $\\dfrac{A\'D\'}{D\'B\'} = %s$' % (latex_ad_db_d)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)

    list_th_1 = [th_da_1]

    loigiai_th_1 = ('''Phép chiếu song song bảo toàn tỉ số độ dài của hai đoạn thẳng cùng nằm trên một đường thẳng. Vì vậy $\\dfrac{A\'D\'}{D\'B\'} = \\dfrac{AD}{DB} = %s$.''' % (latex_ad_db_d))

    list_th_2 = [loigiai_th_1]

    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

    ###################################################################### Vận dụng ######################################################
    # Mệnh đề c: D'E' // B'C' hoặc D'E' cắt B'C'
    vd_da_1_d = '\\True $D\'E\' // B\'C\'$ (hoặc $D\'E\'$ trùng $B\'C\'$)'
    vd_da_1_s = '$D\'E\'$ luôn cắt $B\'C\'$'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)

    list_vd_1 = [vd_da_1]

    loigiai_vd_1 = ('''Trong tam giác $ABC$, do $\\dfrac{AD}{DB} = \\dfrac{AE}{EC} = %s : %s$ nên theo định lí Thales đảo, ta có $DE // BC$. Phép chiếu song song biến hai đường thẳng song song thành hai đường thẳng song song hoặc trùng nhau, do đó $D\'E\' // B\'C\'$ (hoặc trùng nhau nếu mặt phẳng chứa tam giác song song với phương chiếu).''' % (m_val, n_val))

    list_vd_2 = [loigiai_vd_1]

    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

    ###################################################################### Vận dụng cao ######################################################
    # Mệnh đề d: Tỉ số D'E' / B'C'
    vdc_da_1_s = '$\\dfrac{D\'E\'}{B\'C\'} = %s$' % (latex_de_bc_s)
    vdc_da_1_d = '\\True $\\dfrac{D\'E\'}{B\'C\'} = %s$' % (latex_de_bc_d)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)

    list_vdc_1 = [vdc_da_1]

    loigiai_vdc_1 = ('''Do $DE // BC$ nên theo hệ quả định lí Thales trong tam giác $ABC$, ta có $\\dfrac{DE}{BC} = \\dfrac{AD}{AB} = \\dfrac{AD}{AD + DB} = \\dfrac{%s}{%s + %s} = %s$. Phép chiếu song song bảo toàn tỉ số độ dài của hai đoạn thẳng nằm trên hai đường thẳng song song, do đó $\\dfrac{D\'E\'}{B\'C\'} = \\dfrac{DE}{BC} = %s$.''' % (m_val, m_val, n_val, latex_de_bc_d, latex_de_bc_d))

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
    '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
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


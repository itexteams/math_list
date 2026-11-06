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


def bt_dang3_p2_b5_c1_hh11(self):
    # Khai báo các tên đối tượng ngẫu nhiên để tạo nhiều đề bài khác nhau
    list_mat_phang = ['(P)', '(Q)', '(\\alpha)', '(\\beta)']
    list_duong_thang = ['\\Delta', 'd', '\\Delta_0']
    list_diem = ['X', 'M', 'A', 'B']
    list_hinh = ['\\mathcal{H}', '(H)', '\\mathbf{H}']
    list_duong_l = ['\\ell', 'd\'', '\\Delta\'']

    P_plane = random.choice(list_mat_phang)
    Delta_line = random.choice(list_duong_thang)
    X_pt = random.choice(list_diem)
    H_fig = random.choice(list_hinh)
    l_line = random.choice(list_duong_l)

    # Nội dung câu hỏi
    noidungcauhoi = ('''Xét phép chiếu song song lên mặt phẳng $%s$ theo phương $%s$, trong đó $%s$ cắt $%s$.''' % (P_plane, Delta_line, Delta_line, P_plane))

    ###################################################################### Nhận biết ######################################################
    # Mệnh đề a: Mặt phẳng chiếu
    nb_da_1_d = '\\True Mặt phẳng $%s$ được gọi là mặt phẳng chiếu' % (P_plane)
    nb_da_1_s = 'Mặt phẳng $%s$ được gọi là phương chiếu' % (P_plane)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)

    list_nb_1 = [nb_da_1]

    loigiai_nb_1 = ('''Mặt phẳng $%s$ được gọi là mặt phẳng chiếu, phương của đường thẳng $%s$ gọi là phương chiếu.''' % (P_plane, Delta_line))

    list_nb_2 = [loigiai_nb_1]

    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

    ###################################################################### Thông hiểu ######################################################
    # Mệnh đề b: Điểm thuộc mặt phẳng chiếu
    th_da_1_d = '\\True Nếu $%s \\in %s$ thì hình chiếu của $%s$ là chính $%s$' % (X_pt, P_plane, X_pt, X_pt)
    th_da_1_s = 'Nếu $%s \\in %s$ thì hình chiếu của $%s$ không trùng với $%s$' % (X_pt, P_plane, X_pt, X_pt)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)

    list_th_1 = [th_da_1]

    loigiai_th_1 = ('''Với mọi điểm $%s \\in %s$, đường thẳng đi qua $%s$ và song song hoặc trùng với phương chiếu $%s$ cắt $%s$ tại chính $%s$, do đó hình chiếu của $%s$ là chính nó.''' % (X_pt, P_plane, X_pt, Delta_line, P_plane, X_pt, X_pt))

    list_th_2 = [loigiai_th_1]

    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

    ###################################################################### Vận dụng ######################################################
    # Mệnh đề c: Hình chiếu của đường thẳng song song với phương chiếu
    vd_da_1_s = 'Nếu đường thẳng $%s // %s$ và $%s$ cắt $%s$ thì hình chiếu của $%s$ là một đường thẳng nằm trong $%s$' % (l_line, Delta_line, l_line, P_plane, l_line, P_plane)
    vd_da_1_d = '\\True Nếu đường thẳng $%s // %s$ và $%s$ cắt $%s$ thì hình chiếu của $%s$ là một điểm thuộc $%s$' % (l_line, Delta_line, l_line, P_plane, l_line, P_plane)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)

    list_vd_1 = [vd_da_1]

    loigiai_vd_1 = ('''Vì đường thẳng $%s // %s$ nên phương chiếu song song với $%s$. Mọi điểm thuộc $%s$ đều có hình chiếu trùng với giao điểm của $%s$ và $%s$. Do đó, hình chiếu của $%s$ là một điểm thuộc $%s$ chứ không phải là một đường thẳng.''' % (l_line, Delta_line, l_line, l_line, l_line, P_plane, l_line, P_plane))

    list_vd_2 = [loigiai_vd_1]

    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

    ###################################################################### Vận dụng cao ######################################################
    # Mệnh đề d: Định nghĩa hình chiếu của một hình
    vdc_da_1_d = '\\True Hình chiếu của một hình $%s$ là tập hợp hình chiếu của tất cả các điểm thuộc $%s$' % (H_fig, H_fig)
    vdc_da_1_s = 'Hình chiếu của một hình $%s$ là hình đồng dạng với hình $%s$' % (H_fig, H_fig)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)

    list_vdc_1 = [vdc_da_1]

    loigiai_vdc_1 = ('''Theo định nghĩa phép chiếu song song, hình chiếu của một hình $%s$ là tập hợp hình chiếu của tất cả các điểm thuộc $%s$.''' % (H_fig, H_fig))

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


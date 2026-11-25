
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


def bt_dang12_p2_b4_c2_hh10(self):
    def fmt_coord(u, v):
        ru, rv = Rational(u), Rational(v)
        su = latex(ru).replace('\\frac', '\\dfrac')
        sv = latex(rv).replace('\\frac', '\\dfrac')
        if ru.q != 1 or rv.q != 1:
            return f'\\left({su};{sv}\\right)'
        return f'({su};{sv})'
    vals = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]
    while True:
        xA, yA = random.choice(vals), random.choice(vals)
        xB, yB = random.choice(vals), random.choice(vals)
        xC, yC = random.choice(vals), random.choice(vals)
        ab1, ab2 = xB - xA, yB - yA
        ac1, ac2 = xC - xA, yC - yA
        if ab1 == 0 or ab2 == 0 or ac1 == 0 or ac2 == 0:
            continue
        if ab1 * ac2 == ab2 * ac1:
            continue
        if xA + xC == 0 or yA + yC == 0:
            continue
        if xA + xB + xC == 0 or yA + yB + yC == 0:
            continue
        break
    xM, yM = Rational(xA + xC, 2), Rational(yA + yC, 2)
    xG, yG = Rational(xA + xB + xC, 3), Rational(yA + yB + yC, 3)
    M_str = fmt_coord(xM, yM)
    G_str = fmt_coord(xG, yG)
    xM_tex = latex(xM).replace('\\frac', '\\dfrac')
    yM_tex = latex(yM).replace('\\frac', '\\dfrac')
    xG_tex = latex(xG).replace('\\frac', '\\dfrac')
    yG_tex = latex(yG).replace('\\frac', '\\dfrac')
    noidungcauhoi = f'Trong mặt phẳng tọa độ $Oxy$, cho $A({xA};{yA})$, $B({xB};{yB})$, $C({xC};{yC})$. Xét tính đúng sai của các khẳng định sau:\n'
    wrong_M = random.choice([p for p in [(-xM, yM), (xM, -yM), (yM, xM), (xM + 1, yM), (xM, yM + 1)] if p != (xM, yM)])
    wM_str = fmt_coord(wrong_M[0], wrong_M[1])
    nb_da_1_d = f'\\True Tọa độ trung điểm của đoạn thẳng $AC$ là $M{M_str}$'
    nb_da_1_s = f'Tọa độ trung điểm của đoạn thẳng $AC$ là $M{wM_str}$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    wrong_ab_ac = random.choice([p for p in [((-ab1, ab2), (ac1, ac2)), ((ab1, -ab2), (ac1, ac2)), ((ab1, ab2), (-ac1, ac2)), ((ab1, ab2), (ac1, -ac2)), ((ab1 + 1, ab2), (ac1, ac2))] if p != ((ab1, ab2), (ac1, ac2))])
    th_da_1_d = f'\\True $\\overrightarrow{{AB}}=({ab1};{ab2}), \\overrightarrow{{AC}}=({ac1};{ac2})$'
    th_da_1_s = f'$\\overrightarrow{{AB}}=({wrong_ab_ac[0][0]};{wrong_ab_ac[0][1]}), \\overrightarrow{{AC}}=({wrong_ab_ac[1][0]};{wrong_ab_ac[1][1]})$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    vd_da_1_d = '\\True Ba điểm $A, B, C$ không thẳng hàng'
    vd_da_1_s = 'Ba điểm $A, B, C$ thẳng hàng'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    wrong_G = random.choice([p for p in [(-xG, yG), (xG, -yG), (yG, xG), (xG + 1, yG), (xG, yG + 1)] if p != (xG, yG)])
    wG_str = fmt_coord(wrong_G[0], wrong_G[1])
    vdc_da_1_d = f'\\True Tọa độ trọng tâm tam giác $ABC$ là $G{G_str}$'
    vdc_da_1_s = f'Tọa độ trọng tâm tam giác $ABC$ là $G{wG_str}$'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
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
    tt_nb = 'Đúng' if '\\True' in nb_da_1 else 'Sai'
    tt_th = 'Đúng' if '\\True' in th_da_1 else 'Sai'
    tt_vd = 'Đúng' if '\\True' in vd_da_1 else 'Sai'
    tt_vdc = 'Đúng' if '\\True' in vdc_da_1 else 'Sai'
    num_xM = f'{xA}+{xC}'.replace('+-', '-').replace('--', '+')
    num_yM = f'{yA}+{yC}'.replace('+-', '-').replace('--', '+')
    num_xG = f'{xA}+{xB}+{xC}'.replace('+-', '-').replace('--', '+')
    num_yG = f'{yA}+{yB}+{yC}'.replace('+-', '-').replace('--', '+')
    loigiai_nb_1 = f'{tt_nb}: Gọi $M$ là trung điểm $AC \\Rightarrow \\begin{{cases}} x_M=\\dfrac{{{num_xM}}}{{2}}={xM_tex} \\\\ y_M=\\dfrac{{{num_yM}}}{{2}}={yM_tex} \\end{{cases}} \\Rightarrow M{M_str}$.'
    loigiai_th_1 = f'{tt_th}: Tính được $\\overrightarrow{{AB}}=({ab1};{ab2}), \\overrightarrow{{AC}}=({ac1};{ac2})$ dẫn đến hai vectơ đó không cùng phương.'
    loigiai_vd_1 = f'{tt_vd}: Vì hai vectơ $\\overrightarrow{{AB}}, \\overrightarrow{{AC}}$ không cùng phương nên ba điểm $A, B, C$ không thẳng hàng (nói cách khác ba điểm $A, B, C$ tạo thành một tam giác).'
    loigiai_vdc_1 = f'{tt_vdc}: Gọi $G$ là trọng tâm tam giác $ABC \\Rightarrow \\begin{{cases}} x_G=\\dfrac{{{num_xG}}}{{3}}={xG_tex} \\\\ y_G=\\dfrac{{{num_yG}}}{{3}}={yG_tex} \\end{{cases}} \\Rightarrow G{G_str}$.'
    list_nb_1 = [nb_da_1]
    list_th_1 = [th_da_1]
    list_vd_1 = [vd_da_1]
    list_vdc_1 = [vdc_da_1]
    list_nb_2 = [loigiai_nb_1]
    list_th_2 = [loigiai_th_1]
    list_vd_2 = [loigiai_vd_1]
    list_vdc_2 = [loigiai_vdc_1]
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
        '\\end{ex}\n \\end{minipage} \n\n')
    return content

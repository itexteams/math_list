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


def bt_dang17_p2_b3_c1_hh12(self):
    # Khai báo biến và random tọa độ 4 điểm
    xA, yA, zA = [randint(-5, 5) for _ in range(3)]
    xB, yB, zB = [randint(-5, 5) for _ in range(3)]
    xC, yC, zC = [randint(-5, 5) for _ in range(3)]
    xDp, yDp, zDp = [randint(-5, 5) for _ in range(3)]

    # Tính toán các kết quả đúng
    # Ý a: vector BA = A - B
    vBA_x, vBA_y, vBA_z = xA - xB, yA - yB, zA - zB
    # Ý c: Tâm hình hộp I là trung điểm của BD'
    xI = Rational(xB + xDp, 2)
    yI = Rational(yB + yDp, 2)
    zI = Rational(zB + zDp, 2)
    # Ý d: Tọa độ B'
    # Tâm O của mặt đáy là trung điểm AC
    xO, yO, zO = Rational(xA + xC, 2), Rational(yA + yC, 2), Rational(zA + zC, 2)
    # D sao cho O là trung điểm BD
    xD = xA + xC - xB
    yD = yA + yC - yB
    zD = zA + zC - zB
    # Véc tơ DD'
    vDDp_x, vDDp_y, vDDp_z = xDp - xD, yDp - yD, zDp - zD
    # B' = B + DD'
    xBp = xB + vDDp_x
    yBp = yB + vDDp_y
    zBp = zB + vDDp_z

    # Nội dung câu hỏi
    noidungcauhoi = ('''Trong không gian $Oxyz$, cho hình hộp $ABCD.A'B'C'D'$. Biết $A(%s; %s; %s)$, $B(%s; %s; %s)$, $C(%s; %s; %s)$ và $D'(%s; %s; %s)$.''' 
                     % (xA, yA, zA, xB, yB, zB, xC, yC, zC, xDp, yDp, zDp))

    ######################################################################## Nhận biết ############################################

    # Các đáp án
    nb_da_1_d = '\\True $\\overrightarrow{BA} = (%s; %s; %s)$' % (vBA_x, vBA_y, vBA_z)
    nb_da_1_s = '$\\overrightarrow{BA} = (%s; %s; %s)$' % (-vBA_x, -vBA_y, -vBA_z) # Sai dấu (thành AB)
    list_nb_da_1=[nb_da_1_d,nb_da_1_s]
    nb_da_1=random.choice(list_nb_da_1)
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]

    # Nội dung lời giải
    loigiai_nb_1 = ('''Ta có $\\overrightarrow{BA} = (x_A - x_B; y_A - y_B; z_A - z_B) = (%s; %s; %s)$.''' % (vBA_x, vBA_y, vBA_z))
    # Đưa các lời giải vào danh sách lời giải
    list_nb_2 = [loigiai_nb_1]

    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

    ########################################################################Thông hiểu ############################################
    # Các đáp án
    th_da_1_d = '\\True Tọa độ hình chiếu vuông góc của điểm $C$ xuống trục hoành là $(%s; 0; 0)$' % (xC)
    th_da_1_s = 'Tọa độ hình chiếu vuông góc của điểm $C$ xuống trục hoành là $(0; %s; 0)$' % (yC)
    list_th_da_1=[th_da_1_d,th_da_1_s]
    th_da_1=random.choice(list_th_da_1)
    list_th_1 = [th_da_1]

    # Nội dung lời giải
    loigiai_th_1 = ('''Hình chiếu vuông góc của điểm $C(%s; %s; %s)$ xuống trục hoành ($Ox$) có tung độ và cao độ bằng $0$, hoành độ giữ nguyên. Vậy tọa độ hình chiếu là $(%s; 0; 0)$.''' % (xC, yC, zC, xC))

    list_th_2 = [loigiai_th_1]
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

    ######################################################################## Vận dụng ############################################
    # Các đáp án
    vd_da_1_d = '\\True Tọa độ của tâm hình hộp $ABCD.A\'B\'C\'D\'$ là $\\left(%s; %s; %s\\right)$' % (latex(xI), latex(yI), latex(zI))
    vd_da_1_s = 'Tọa độ của tâm hình hộp $ABCD.A\'B\'C\'D\'$ là $\\left(%s; %s; %s\\right)$' % (latex(xI + 1), latex(yI - 1), latex(zI))
    list_vd_da_1=[vd_da_1_d,vd_da_1_s]
    vd_da_1=random.choice(list_vd_da_1)
    list_vd_1 = [vd_da_1]

    # Nội dung lời giải
    loigiai_vd_1 = ('''Giả sử $I(x; y; z)$ là tâm hình hộp, ta có $I$ là trung điểm của đường chéo $BD'$. \\\\
    Suy ra $\\begin{cases} x = \\dfrac{x_B + x_{D'}}{2} = %s \\\\[4pt] y = \\dfrac{y_B + y_{D'}}{2} = %s \\\\[4pt] z = \\dfrac{z_B + z_{D'}}{2} = %s \\end{cases}$. \\\\
    Vậy tâm hình hộp là $I\\left(%s; %s; %s\\right)$.''' % (latex(xI), latex(yI), latex(zI), latex(xI), latex(yI), latex(zI)))

    list_vd_2 = [loigiai_vd_1]
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

    ######################################################################## Vận dụng cao ############################################
    # Các đáp án
    vdc_da_1_d = '\\True Tọa độ của điểm $B\'(%s; %s; %s)$' % (xBp, yBp, zBp)
    vdc_da_1_s = 'Tọa độ của điểm $B\'(%s; %s; %s)$' % (xBp + 2, yBp - 1, zBp)
    list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
    vdc_da_1=random.choice(list_vdc_da_1)
    list_vdc_1 = [vdc_da_1]

    # Nội dung lời giải
    loigiai_vdc_1 = ('''Gọi $O = AC \\cap BD \\Rightarrow O$ là trung điểm $AC \\Rightarrow O\\left(%s; %s; %s\\right)$. \\\\
    Vì $O$ cũng là trung điểm của $BD$ nên $\\begin{cases} x_D = 2x_O - x_B = %s \\\\ y_D = 2y_O - y_B = %s \\\\ z_D = 2z_O - z_B = %s \\end{cases} \\Rightarrow D(%s; %s; %s)$. \\\\
    Ta có $\\overrightarrow{DD'} = (%s; %s; %s)$. Do $ABCD.A'B'C'D'$ là hình hộp nên $\\overrightarrow{BB'} = \\overrightarrow{DD'}$. \\\\
    Gọi $B'(a'; b'; c')$, ta có $\\overrightarrow{BB'} = (a' - (%s); b' - (%s); c' - (%s))$. \\\\
    Suy ra $\\begin{cases} a' - (%s) = %s \\\\ b' - (%s) = %s \\\\ c' - (%s) = %s \\end{cases} \\Rightarrow \\begin{cases} a' = %s \\\\ b' = %s \\\\ c' = %s \\end{cases}$. \\\\
    Vậy $B'(%s; %s; %s)$.''' 
    % (latex(xO), latex(yO), latex(zO), xD, yD, zD, xD, yD, zD, vDDp_x, vDDp_y, vDDp_z, 
       xB, yB, zB, xB, vDDp_x, yB, vDDp_y, zB, vDDp_z, xBp, yBp, zBp, xBp, yBp, zBp))

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
        str(noidungcauhoi)+ '\n'+
        '\\choiceTF \n'
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
        '\\end{ex}\n\\end{minipage}\n\n')
    return content


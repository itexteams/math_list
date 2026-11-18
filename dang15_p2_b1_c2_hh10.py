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


def bt_dang15_p2_b1_c2_hh10(self):
    # Khai báo biến và sinh ngẫu nhiên tọa độ các điểm trên mặt phẳng Oxy
    xA = random.randint(-3, 3)
    yA = random.randint(-3, 3)
    L = random.randint(2, 6)
    
    # Điểm B nằm bên phải A trên cùng đường thẳng y = yA
    xB, yB = xA + L, yA
    
    # Điểm D không nằm trên đường thẳng AB và độ dài AD khác L
    while True:
        dx = random.choice([-2, -1, 1, 2])
        dy = random.randint(2, 5)
        if dx**2 + dy**2 != L**2:
            break
    
    xD, yD = xA + dx, yA + dy
    # Điểm C sao cho vectơ DC = vectơ AB (tứ giác ABCD là hình bình hành)
    xC, yC = xD + L, yD
    
    # Điểm M nằm trên đường thẳng DC sao cho C nằm giữa D và M
    k_M = random.randint(2, 5)
    xM, yM = xC + k_M, yD
    
    # Điểm N thỏa mãn vectơ CN = vectơ AD (tứ giác ACND là hình bình hành)
    xN, yN = xC + dx, yC + dy
    len_AN = sp.sqrt((xN - xA)**2 + (yN - yA)**2)
    wrong_len_AN = sp.sqrt((xC - xA)**2 + (yC - yA)**2)
    if len_AN == wrong_len_AN:
        wrong_len_AN = len_AN + 1
    
    # Định dạng hiển thị số âm trong phép trừ
    xA_str = f"({xA})" if xA < 0 else f"{xA}"
    yA_str = f"({yA})" if yA < 0 else f"{yA}"
    xD_str = f"({xD})" if xD < 0 else f"{xD}"
    xN_minus_xA_str = f"({xN - xA})" if (xN - xA) < 0 else f"{xN - xA}"
    yN_minus_yA_str = f"({yN - yA})" if (yN - yA) < 0 else f"{yN - yA}"
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Trên mặt phẳng tọa độ $Oxy$, cho năm điểm $A(%s; %s)$, $B(%s; %s)$, $C(%s; %s)$, $D(%s; %s)$ và $M(%s; %s)$. Xét tính đúng, sai của các khẳng định sau:''' % (xA, yA, xB, yB, xC, yC, xD, yD, xM, yM))
    
    ######################################################################## Nhận biết ############################################
    # Các đáp án
    nb_da_1_d = '\\True Hai vectơ $\\overrightarrow{AB}$ và $\\overrightarrow{DC}$ bằng nhau và có độ dài bằng $%s$' % (L)
    nb_da_1_s = 'Hai vectơ $\\overrightarrow{AB}$ và $\\overrightarrow{DC}$ bằng nhau và có độ dài bằng $%s$' % (L + 1)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]
    
    # Nội dung lời giải
    loigiai_nb_1 = ('''Hai điểm $A(%s; %s)$ và $B(%s; %s)$ có cùng tung độ bằng $%s$ nên giá của $\\overrightarrow{AB}$ là đường thẳng $y = %s$, chiều từ $A$ đến $B$ hướng từ trái sang phải (theo chiều dương trục $Ox$) và độ dài $|\\overrightarrow{AB}| = AB = %s - %s = %s$. \\\\ Tương tự, hai điểm $D(%s; %s)$ và $C(%s; %s)$ có cùng tung độ bằng $%s$ nên giá của $\\overrightarrow{DC}$ là đường thẳng $y = %s$ song song với đường thẳng $y = %s$, chiều từ $D$ đến $C$ cũng hướng từ trái sang phải và độ dài $|\\overrightarrow{DC}| = DC = %s - %s = %s$. \\\\ Vì $\\overrightarrow{AB}$ và $\\overrightarrow{DC}$ cùng hướng và có cùng độ dài bằng $%s$ nên $\\overrightarrow{AB} = \\overrightarrow{DC}$ và $|\\overrightarrow{AB}| = |\\overrightarrow{DC}| = %s$.''' % (xA, yA, xB, yB, yA, yA, xB, xA_str, L, xD, yD, xC, yC, yD, yD, yA, xC, xD_str, L, L, L))
    
    # Đưa các lời giải vào danh sách lời giải
    list_nb_2 = [loigiai_nb_1]
    
    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_nb = list(zip(list_nb_1, list_nb_2))
    
    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_nb)
    
    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ######################################################################## Thông hiểu ############################################
    # Các đáp án
    th_da_1_d = '\\True Hai vectơ $\\overrightarrow{AD}$ và $\\overrightarrow{CB}$ ngược hướng với nhau'
    th_da_1_s = 'Hai vectơ $\\overrightarrow{AD}$ và $\\overrightarrow{CB}$ cùng hướng với nhau'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]
    
    # Nội dung lời giải
    loigiai_th_1 = ('''Tứ giác $ABCD$ có $\\overrightarrow{AB} = \\overrightarrow{DC}$ và ba điểm $A, B, D$ không thẳng hàng nên $ABCD$ là hình bình hành. \\\\ Do đó hai cạnh đối $AD$ và $BC$ song song và bằng nhau, suy ra hai vectơ $\\overrightarrow{AD}$ và $\\overrightarrow{BC}$ cùng hướng (cùng hướng từ dưới lên trên do $y_D = %s > y_A = %s$). \\\\ Mặt khác, hai vectơ $\\overrightarrow{CB}$ và $\\overrightarrow{BC}$ có chung giá là đường thẳng $BC$ và ngược hướng nhau. Vì vậy, hai vectơ $\\overrightarrow{AD}$ và $\\overrightarrow{CB}$ cùng phương nhưng ngược hướng với nhau.''' % (yD, yA))
    
    # Đưa các lời giải vào danh sách lời giải
    list_th_2 = [loigiai_th_1]
    
    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_th = list(zip(list_th_1, list_th_2))
    
    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_th)
    
    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ######################################################################## Vận dụng ############################################
    # Các đáp án
    vd_da_1_d = '\\True Ba điểm $D, C, M$ thẳng hàng và hai vectơ $\\overrightarrow{CD}, \\overrightarrow{CM}$ ngược hướng nhau'
    vd_da_1_s = 'Ba điểm $D, C, M$ thẳng hàng và hai vectơ $\\overrightarrow{CD}, \\overrightarrow{CM}$ cùng hướng với nhau'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]
    
    # Nội dung lời giải
    loigiai_vd_1 = ('''Ba điểm $D(%s; %s)$, $C(%s; %s)$ và $M(%s; %s)$ có cùng tung độ bằng $%s$ nên cùng nằm trên đường thẳng $y = %s$, tức là ba điểm $D, C, M$ thẳng hàng (hai vectơ $\\overrightarrow{CD}$ và $\\overrightarrow{CM}$ có chung giá nên cùng phương). \\\\ Trên đường thẳng $y = %s$, hoành độ các điểm thỏa mãn $x_D = %s < x_C = %s < x_M = %s$ nên điểm $C$ nằm giữa hai điểm $D$ và $M$. Do đó hai vectơ $\\overrightarrow{CD}$ (hướng sang trái) và $\\overrightarrow{CM}$ (hướng sang phải) ngược hướng với nhau.''' % (xD, yD, xC, yC, xM, yM, yD, yD, yD, xD, xC, xM))
    
    # Đưa các lời giải vào danh sách lời giải
    list_vd_2 = [loigiai_vd_1]
    
    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_vd = list(zip(list_vd_1, list_vd_2))
    
    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_vd)
    
    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ######################################################################## Vận dụng cao ############################################
    # Các đáp án
    vdc_da_1_d = '\\True Gọi $N$ là điểm thỏa mãn $\\overrightarrow{CN} = \\overrightarrow{AD}$. Khi đó tứ giác $ACND$ là hình bình hành và $|\\overrightarrow{AN}| = %s$' % (latex(len_AN))
    vdc_da_1_s = 'Gọi $N$ là điểm thỏa mãn $\\overrightarrow{CN} = \\overrightarrow{AD}$. Khi đó tứ giác $ACND$ là hình bình hành và $|\\overrightarrow{AN}| = %s$' % (latex(wrong_len_AN))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]
    
    # Nội dung lời giải
    loigiai_vdc_1 = ('''Vì $\\overrightarrow{CN} = \\overrightarrow{AD}$ và ba điểm $A, C, D$ không thẳng hàng nên tứ giác $ACND$ là hình bình hành. \\\\ Từ $A(%s; %s)$ đến $D(%s; %s)$, hoành độ thay đổi một lượng là $%s - %s = %s$ và tung độ tăng thêm $%s - %s = %s$. Vì $\\overrightarrow{CN} = \\overrightarrow{AD}$ nên từ $C(%s; %s)$ ta suy ra tọa độ điểm $N(%s; %s)$. \\\\ Do đó độ dài vectơ $\\overrightarrow{AN}$ là $|\\overrightarrow{AN}| = AN = \\sqrt{%s^2 + %s^2} = %s$.''' % (xA, yA, xD, yD, xD, xA_str, dx, yD, yA_str, dy, xC, yC, xN, yN, xN_minus_xA_str, yN_minus_yA_str, latex(len_AN)))
    
    # Đưa các lời giải vào danh sách lời giải
    list_vdc_2 = [loigiai_vdc_1]
    
    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))
    
    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_vdc)
    
    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
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


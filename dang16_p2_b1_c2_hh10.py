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


def bt_dang16_p2_b1_c2_hh10(self):
    vn = random.choice([3, 4, 5])
    s_scale = vn
    k_B = random.choice([2, 4])
    ratio_AB = random.choice([2, 3])
    
    # Vận tốc thực tế và vận tốc riêng của hai ca nô A, B (km/h)
    v_B = k_B * vn
    v_B0 = v_B + vn
    v_A = ratio_AB * v_B
    v_A0 = v_A - vn
    
    # Độ dài vectơ vận tốc thực tế của ca nô A trên bản đồ (cm)
    len_vA_cm = v_A // s_scale
    wrong_len_vA_cm = v_A0 // s_scale
    
    # Thời điểm xuất phát, thời điểm xét (sau 1,5 giờ) và quãng đường đi được (km)
    h_start = random.choice([7, 8])
    h_end = h_start + 1
    OM = (v_A * 3) // 2
    ON = (v_B * 3) // 2
    MN_true = OM + ON
    MN_wrong = abs(OM - ON)
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Một khúc sông thẳng có dòng nước chảy đều từ hướng Tây sang hướng Đông với vận tốc $\\overrightarrow{v_n}$ có độ lớn $%s\\text{ km/h}$. Lúc $%s\\text{ giờ sáng}$, hai ca nô $A$ và $B$ cùng xuất phát từ bến $O$: ca nô $A$ chạy xuôi dòng về hướng Đông với vận tốc riêng $%s\\text{ km/h}$, ca nô $B$ chạy ngược dòng về hướng Tây với vận tốc riêng $%s\\text{ km/h}$. Trên bản đồ quy ước tỉ lệ xích: cứ $1\\text{ cm}$ độ dài vectơ biểu diễn vận tốc có độ lớn $%s\\text{ km/h}$. Gọi $\\overrightarrow{v_A}, \\overrightarrow{v_B}$ lần lượt là vectơ vận tốc thực tế của ca nô $A$ và ca nô $B$. Xét tính đúng, sai của các khẳng định sau:''' % (vn, h_start, v_A0, v_B0, s_scale))
    
    ######################################################################## Nhận biết ############################################
    # Các đáp án
    nb_da_1_d = '\\True Ba vectơ $\\overrightarrow{v_n}, \\overrightarrow{v_A}, \\overrightarrow{v_B}$ cùng phương với nhau, trong đó $\\overrightarrow{v_A}$ và $\\overrightarrow{v_B}$ ngược hướng nhau'
    nb_da_1_s = 'Ba vectơ $\\overrightarrow{v_n}, \\overrightarrow{v_A}, \\overrightarrow{v_B}$ cùng phương với nhau, trong đó $\\overrightarrow{v_A}$ và $\\overrightarrow{v_B}$ cùng hướng với nhau'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]
    
    # Nội dung lời giải
    loigiai_nb_1 = ('''Dòng nước và hai ca nô đều chuyển động dọc theo khúc sông thẳng theo phương Đông -- Tây nên giá của ba vectơ $\\overrightarrow{v_n}, \\overrightarrow{v_A}, \\overrightarrow{v_B}$ song song hoặc trùng nhau, do đó ba vectơ này cùng phương. \\\\ Vì ca nô $A$ chạy về hướng Đông còn ca nô $B$ chạy về hướng Tây nên hai vectơ $\\overrightarrow{v_A}$ và $\\overrightarrow{v_B}$ ngược hướng nhau.''')
    
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
    th_da_1_d = '\\True Trên bản đồ tỉ lệ xích đã cho, vectơ biểu diễn vận tốc thực tế $\\overrightarrow{v_A}$ có độ dài bằng $%s\\text{ cm}$' % (len_vA_cm)
    th_da_1_s = 'Trên bản đồ tỉ lệ xích đã cho, vectơ biểu diễn vận tốc thực tế $\\overrightarrow{v_A}$ có độ dài bằng $%s\\text{ cm}$' % (wrong_len_vA_cm)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]
    
    # Nội dung lời giải
    loigiai_th_1 = ('''Ca nô $A$ chạy xuôi dòng nên độ lớn vận tốc thực tế của ca nô $A$ là $v_A = %s + %s = %s\\text{ km/h}$. \\\\ Với quy ước tỉ lệ xích $1\\text{ cm}$ ứng với $%s\\text{ km/h}$, độ dài vectơ biểu diễn $\\overrightarrow{v_A}$ trên bản đồ là $\\dfrac{%s}{%s} = %s\\text{ cm}$.''' % (v_A0, vn, v_A, s_scale, v_A, s_scale, len_vA_cm))
    
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
    vd_da_1_d = '\\True Độ dài vectơ vận tốc thực tế của ca nô $A$ gấp $%s$ lần độ dài vectơ vận tốc thực tế của ca nô $B$' % (ratio_AB)
    vd_da_1_s = 'Độ dài vectơ vận tốc thực tế của ca nô $A$ gấp $%s$ lần độ dài vectơ vận tốc thực tế của ca nô $B$' % (ratio_AB + 1)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]
    
    # Nội dung lời giải
    loigiai_vd_1 = ('''Ca nô $B$ chạy ngược dòng nên độ lớn vận tốc thực tế của ca nô $B$ là $v_B = %s - %s = %s\\text{ km/h}$. Trong khi đó độ lớn vận tốc thực tế của ca nô $A$ là $v_A = %s\\text{ km/h}$. \\\\ Vì độ dài vectơ tỉ lệ thuận với độ lớn vận tốc nên $\\dfrac{|\\overrightarrow{v_A}|}{|\\overrightarrow{v_B}|} = \\dfrac{%s}{%s} = %s$, tức là độ dài vectơ $\\overrightarrow{v_A}$ gấp $%s$ lần độ dài vectơ $\\overrightarrow{v_B}$.''' % (v_B0, vn, v_B, v_A, v_A, v_B, ratio_AB, ratio_AB))
    
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
    vdc_da_1_d = '\\True Lúc $%s\\text{ giờ } 30\\text{ phút}$ cùng ngày, gọi $M$ và $N$ lần lượt là vị trí của ca nô $A$ và ca nô $B$. Khi đó hai vectơ $\\overrightarrow{OM}$ và $\\overrightarrow{ON}$ ngược hướng và $|\\overrightarrow{MN}| = %s\\text{ km}$' % (h_end, MN_true)
    vdc_da_1_s = 'Lúc $%s\\text{ giờ } 30\\text{ phút}$ cùng ngày, gọi $M$ và $N$ lần lượt là vị trí của ca nô $A$ và ca nô $B$. Khi đó hai vectơ $\\overrightarrow{OM}$ và $\\overrightarrow{ON}$ cùng hướng và $|\\overrightarrow{MN}| = %s\\text{ km}$' % (h_end, MN_wrong)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]
    
    # Nội dung lời giải
    loigiai_vdc_1 = ('''Thời gian hai ca nô di chuyển từ $%s\\text{ giờ}$ đến $%s\\text{ giờ } 30\\text{ phút}$ là $1,5\\text{ giờ}$. \\\\ Ca nô $A$ đi về hướng Đông được quãng đường $OM = %s \\times 1,5 = %s\\text{ km}$; ca nô $B$ đi về hướng Tây được quãng đường $ON = %s \\times 1,5 = %s\\text{ km}$. \\\\ Vì hai ca nô đi về hai hướng ngược nhau từ bến $O$ nên điểm $O$ nằm giữa hai điểm $M$ và $N$. Suy ra hai vectơ $\\overrightarrow{OM}$ và $\\overrightarrow{ON}$ ngược hướng và $|\\overrightarrow{MN}| = MN = OM + ON = %s + %s = %s\\text{ km}$.''' % (h_start, h_end, v_A, OM, v_B, ON, OM, ON, MN_true))
    
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


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


def bt_dang3_p2_b1_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            n = symbols('n')
            a = randint(-5, -1)
            b = randint(1, 5)
            un = a*n / (n+b)
            un_expr = latex(un)

            # Các giá trị để tính
            k1 = 10
            k2 = 100
            k3_val_n = 85
            k3_wrong_n = 86
            k4_val_n = 99
            k4_wrong_d = 101

            # Tính giá trị các số hạng
            u1 = a * 1 / (1 + b)
            u2 = a * 2 / (2 + b)
            u3 = a * 3 / (3 + b)
            u4 = a * 4 / (4 + b)
            u5 = a * 5 / (5 + b)

            u10 = a * 10 / (10 + b)
            u100 = a * 100 / (100 + b)

            u85 = a * k3_val_n / (k3_val_n + b)
            u85_wrong_n = k3_wrong_n
            u85_wrong = a * u85_wrong_n / (u85_wrong_n + b)

            u99 = a * k4_val_n / (k4_val_n + b)
            u99_wrong_d = k4_wrong_d
            u99_wrong = Rational(a * k4_val_n, k4_wrong_d)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho dãy số $(u_n)$, biết $u_n=%s$.'''                 
                             %(un_expr))

            ######################################################################### Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True $u_1=%s; u_2=%s; u_3=%s; u_4=%s; u_5=%s$' % (latex(Rational(a*1, 1+b)), latex(Rational(a*2, 2+b)), latex(Rational(a*3, 3+b)), latex(Rational(a*4, 4+b)), latex(Rational(a*5, 5+b)))
            nb_da_1_s = 'Năm số hạng đầu tiên của dãy số là $u_1=%s; u_2=%s; u_3=%s; u_4=%s; u_5=%s$' % (latex(Rational(a*1, 1+b)), latex(Rational(a*2, 2+b)), latex(Rational(a*3, 3+b)), latex(Rational(a*5, 5+b)), latex(Rational(a*4, 4+b)))
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Thay $n=1, 2, 3, 4, 5$ vào công thức $u_n=%s$, ta được năm số hạng đầu tiên là \\\\ $u_1=%s; u_2=%s; u_3=%s; u_4=%s; u_5=%s$.'''
                        %(un_expr, latex(Rational(a*1, 1+b)), latex(Rational(a*2, 2+b)), latex(Rational(a*3, 3+b)), latex(Rational(a*4, 4+b)), latex(Rational(a*5, 5+b))))

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################### Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Số hạng $u_{%s}, u_{%s}$ lần lượt là $%s; %s$' %(k1, k2, latex(Rational(a*k1, k1+b)), latex(Rational(a*k2, k2+b)))  
            th_da_1_s = 'Số hạng $u_{%s}, u_{%s}$ lần lượt là $%s; %s$' %(k1, k2, latex(Rational(a*k2, k2+b)), latex(Rational(a*k1, k1+b)))   
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Thay $n=%s$ và $n=%s$ vào công thức $u_n=%s$, ta được $u_{%s}=%s$ và $u_{%s}=%s$.'''       
                       %(k1, k2, un_expr, k1, latex(Rational(a*k1, k1+b)), k2, latex(Rational(a*k2, k2+b))))

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################### Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True $%s$ là số hạng thứ $%s$ của dãy số $(u_n)$' %(latex(Rational(a*k3_val_n, k3_val_n+b)), k3_val_n)  
            vd_da_1_s = '$%s$ là số hạng thứ $%s$ của dãy số $(u_n)$' %(latex(Rational(a*k3_val_n, k3_val_n+b)), k3_wrong_n)  
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            hang_tu_tu_do = a*k3_val_n*b
            dau_hang_tu = f"+ {hang_tu_tu_do}" if hang_tu_tu_do > 0 else f"- {abs(hang_tu_tu_do)}"

            loigiai_vd_1 = ('''Ta xét phương trình: $u_n = %s \\Leftrightarrow %s = %s \\Leftrightarrow %sn = %s(n+%s) \\Leftrightarrow %sn = %sn %s \\Leftrightarrow %sn = %s \\Leftrightarrow n = %s$. \\\\
                              Vậy $%s$ là số hạng thứ $%s$ của dãy số.'''  
                       %(latex(Rational(a*k3_val_n, k3_val_n+b)), un_expr, latex(Rational(a*k3_val_n, k3_val_n+b)), 
                         a*(k3_val_n+b), a*k3_val_n, b, 
                         a*(k3_val_n+b), a*k3_val_n, dau_hang_tu, 
                         a*(k3_val_n+b) - a*k3_val_n, a*k3_val_n*b, 
                         k3_val_n, 
                         latex(Rational(a*k3_val_n, k3_val_n+b)), k3_val_n))

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## # Vận dụng cao ############################################
            # Các đáp án
            # Tính toán một số hạng không thuộc dãy
            val_khong_thuoc_day = Rational(a * k4_val_n, k4_wrong_d)
            vdc_da_1_s = '\\True $%s$ không là một số hạng của dãy số $(u_n)$' %(latex(Rational(a*k4_val_n, k4_val_n+b))) 
            vdc_da_1_d = '$%s$ là số hạng của dãy số $(u_n)$' %(latex(val_khong_thuoc_day)) 
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            hang_tu_tu_do_vdc = a*k4_val_n*b
            dau_hang_tu_vdc = f"+ {hang_tu_tu_do_vdc}" if hang_tu_tu_do_vdc > 0 else f"- {abs(hang_tu_tu_do_vdc)}"

            loigiai_vdc_1 = ('''Giả sử $%s$ là một số hạng của dãy số. Ta có: \\\\
                            $u_n = %s \\Leftrightarrow %s = %s \\Leftrightarrow %sn = %s(n+%s) \\Leftrightarrow %sn = %sn %s \\Leftrightarrow %sn = %s \\Leftrightarrow n = %s$. \\\\
                            Vì $n = %s$ không phải là số nguyên dương nên mệnh đề trên đúng/sai tùy thuộc vào giá trị $n$ tìm được. Trong trường hợp đáp án sai, $n$ tìm được không phải là số nguyên dương.'''
                       %(latex(val_khong_thuoc_day), 
                         latex(val_khong_thuoc_day), un_expr, latex(val_khong_thuoc_day), 
                         a*k4_wrong_d, a*k4_val_n, b, 
                         a*k4_wrong_d, a*k4_val_n, dau_hang_tu_vdc, 
                         a*k4_wrong_d - a*k4_val_n, a*k4_val_n*b, 
                         latex(Rational(a*k4_val_n*b, a*k4_wrong_d - a*k4_val_n)),
                         latex(Rational(a*k4_val_n*b, a*k4_wrong_d - a*k4_val_n))))

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


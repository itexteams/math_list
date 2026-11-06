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


def bt_dang4_p2_b2_c2_ds11(self):
            # Khai báo biến
            n=symbols('n', integer=True)

            # ⭐️ KHU VỰC RANDOM THAM SỐ ⭐️
            T_start = randint(5, 20)      # Thời gian bơi ngày đầu (T1): 5 đến 20 phút
            d = randint(1, 5)             # Thời gian tăng thêm mỗi ngày (công sai): 1 đến 5 phút
            N_target = randint(15, 40)    # Chọn ngày đạt mục tiêu ngẫu nhiên: Ngày thứ 15 đến 40

            # Tính ngược T_target để đảm bảo N_target là số nguyên
            # T_target = T_start + (N_target - 1) * d
            T_target = T_start + (N_target - 1) * d 
            # ⭐️ KẾT THÚC KHU VỰC RANDOM ⭐️

            # Công thức tổng quát Tn = T_start + (n-1)*d
            Tn = T_start + (n-1)*d
            Tn_expanded = expand(Tn) # Ví dụ: 8 + 2n

            # Nội dung câu hỏi
            noidungcauhoi = ('''Bác Hưng quyết định tham gia một chương trình bơi lội để duy trì sức khỏe. 
            Bác bắt đầu bằng cách bơi %s phút vào ngày đầu tiên, sau đó thêm %s phút mỗi ngày sau đó.'''
                             %(latex(T_start), latex(d)
                                ))

            ########################################################################Mệnh đề A (Truy hồi) ############################################
            # Các đáp án
            nb_da_1_d = '\\True Gọi $T_n$ là số phút mà bác Hưng bơi vào ngày thứ $n$. Ta có hệ thức truy hồi $T_1 = %s, T_{n+1} = T_n + %s, \\forall n \\ge 1$.' %(latex(T_start), latex(d))
            nb_da_1_s = 'Gọi $T_n$ là số phút mà bác Hưng bơi vào ngày thứ $n$. Ta có hệ thức truy hồi $T_1 = %s, T_{n+1} = T_n + %s, \\forall n \\ge 1$.' %(latex(T_start+randint(1,2)), latex(d)) # Sai T1
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Do bác bắt đầu cách bơi %s phút vào ngày đầu tiên, sau đó thêm %s phút mỗi ngày sau đó nên ta có hệ thức truy hồi $T_1 = %s, T_{n+1} = T_n + %s, \\forall n \\ge 1$.'''
                            %(latex(T_start), latex(d), latex(T_start), latex(d)
                            ))

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################Mệnh đề B (Các số hạng đầu) ############################################
            T2 = T_start + d
            T3 = T_start + 2*d
            T4 = T_start + 3*d
            T5 = T_start + 4*d
            T6 = T_start + 5*d

            # Các đáp án
            th_da_1_d = '\\True Sáu số hạng đầu của dãy số là $T_1 = %s; T_2 = %s; T_3 = %s; T_4 = %s; T_5 = %s; T_6 = %s$.' \
                        %(latex(T_start), latex(T2), latex(T3), latex(T4), latex(T5), latex(T6)) 
            th_da_1_s = 'Sáu số hạng đầu của dãy số là $T_1 = %s; T_2 = %s; T_3 = %s; T_4 = %s; T_5 = %s; T_6 = %s$.' \
                        %(latex(T_start), latex(T2-d + randint(1,2)), latex(T3), latex(T4), latex(T5), latex(T6)) # Sai T2
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Sáu số hạng đầu của dãy số là $T_1 = %s; T_2 = %s; T_3 = %s; T_4 = %s; T_5 = %s; T_6 = %s$.'''
                        %(latex(T_start), latex(T2), latex(T3), latex(T4), latex(T5), latex(T6)
                            ))

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Mệnh đề C (Công thức tổng quát) ############################################
            # Các đáp án
            vd_da_1_d = '\\True Theo định nghĩa dãy số $T_n$ là cấp số cộng có $T_1 = %s$ và công sai $d = %s$. Suy ra, công thức tổng quát của dãy số là $T_n = %s, \\forall n \\ge 1$.' \
                        %(latex(T_start), latex(d), latex(Tn_expanded))  
            vd_da_1_s = 'Theo định nghĩa dãy số $T_n$ là cấp số cộng có $T_1 = %s$ và công sai $d = %s$. Suy ra, công thức tổng quát của dãy số là $T_n = %s, \\forall n \\ge 1$.' \
                        %(latex(T_start), latex(d), latex(Tn_expanded + randint(1,2))) # Sai công thức tổng quát
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Theo định nghĩa dãy số $T_n$ là cấp số cộng có $T_1 = %s$ và công sai $d = %s$. \\\\
            Suy ra, công thức tổng quát của dãy số là $T_n = T_1 + (n-1)d = %s + (n-1)%s = %s, \\forall n \\ge 1$.'''
                        %(latex(T_start), latex(d), latex(T_start), latex(d), latex(Tn_expanded)
                            ))

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Mệnh đề D (Mục tiêu) ############################################
            # Ngày đạt mục tiêu
            # N_target đã được tính ở trên: T_target = T_start + (N_target - 1) * d 

            # Các đáp án
            vdc_da_1_d = '\\True Ta có $T_n \\ge %s \\Leftrightarrow n \\ge %s$. Vậy bác Hưng đạt được mục tiêu bơi ít nhất %s phút mỗi ngày vào ngày thứ %s của chương trình.' \
                        %(latex(T_target), latex(N_target), latex(T_target), latex(N_target)) 
            vdc_da_1_s = 'Ta có $T_n \\ge %s \\Leftrightarrow n \\ge %s$. Vậy bác Hưng đạt được mục tiêu bơi ít nhất %s phút mỗi ngày vào ngày thứ %s của chương trình.' \
                        %(latex(T_target), latex(N_target + 1), latex(T_target), latex(N_target + 1)) # Sai ngày đạt mục tiêu
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Ta có $T_n \\ge %s \\Leftrightarrow %s \\ge %s \\Leftrightarrow %s \\ge %s \\Leftrightarrow n \\ge %s$. \\\\
            Vậy bác Hưng đạt được mục tiêu bơi ít nhất %s phút mỗi ngày vào ngày thứ %s của chương trình.'''
                        %(latex(T_target), latex(Tn_expanded), latex(T_target), latex(d*n), latex(T_target - (T_start - d)), latex(N_target),
                         latex(T_target), latex(N_target)
                            ))

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
                # Chọn lại đáp án ngẫu nhiên
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán lại vào list (để đảm bảo đáp án và lời giải khớp)
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


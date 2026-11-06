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


def bt_dang14_p2_b2_c1_ds10(self):
            # Khai báo biến
            # Để đảm bảo nghiệm nguyên, ta tạo ngược từ đáp án
            y_val = randint(2, 6) # Số học sinh chỉ giỏi Văn
            B_val = randint(3, 8) # Số học sinh giỏi cả 2 môn
            # Vì Số HS giỏi Toán = 2 * Số HS giỏi Văn => (x + B) = 2(y + B) => x = 2y + B
            x_val = 2 * y_val + B_val # Số học sinh chỉ giỏi Toán
            N_val = randint(8, 15) # Số học sinh không giỏi môn nào
            T_val = x_val + y_val + B_val + N_val # Tổng số học sinh

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một lớp học có $%s$ học sinh trong đó gồm có $%s$ học sinh giỏi cả hai môn Văn và Toán, $%s$ học sinh không giỏi môn nào trong cả hai môn Văn và Toán, số học sinh giỏi Toán bằng hai lần số học sinh giỏi Văn.'''
                             %(T_val, B_val, N_val))

            ######################################################################## Nhận biết ############################################
            # Xét quan hệ lớn hơn/nhỏ hơn giữa số HS giỏi cả 2 môn (B) và không giỏi môn nào (N)
            word_d = 'nhỏ hơn' if B_val < N_val else 'lớn hơn'
            word_s = 'lớn hơn' if B_val < N_val else 'nhỏ hơn'

            # Các đáp án
            nb_da_1_d = '\\True Số học sinh giỏi cả Văn và Toán %s số học sinh không giỏi môn nào trong cả hai môn Văn và Toán' % (word_d)
            nb_da_1_s = 'Số học sinh giỏi cả Văn và Toán %s số học sinh không giỏi môn nào trong cả hai môn Văn và Toán' % (word_s)
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Ta có số học sinh giỏi cả Văn và Toán là $%s$, số học sinh không giỏi môn nào là $%s$. \\\\
            Vì $%s %s %s$ nên số học sinh giỏi cả Văn và Toán %s số học sinh không giỏi môn nào.''' 
                            %(B_val, N_val, B_val, '<' if B_val < N_val else '>', N_val, word_d))

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            sum_xy = x_val + y_val
            sum_xy_s = sum_xy + randint(1, 3) * random.choice([-1, 1])

            # Các đáp án
            th_da_1_d = '\\True Nếu gọi $x$ là số học sinh chỉ giỏi Toán và $y$ là số học sinh chỉ giỏi Văn thì $x + y = %s$' %(sum_xy)
            th_da_1_s = 'Nếu gọi $x$ là số học sinh chỉ giỏi Toán và $y$ là số học sinh chỉ giỏi Văn thì $x + y = %s$' %(sum_xy_s)
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Số học sinh ít nhất giỏi một trong hai môn Văn hoặc Toán là: $%s - %s = %s$. \\\\
            Khi đó tổng số học sinh chỉ giỏi Toán và chỉ giỏi Văn là: $%s - %s = %s$. \\\\
            Vậy $x + y = %s$.'''
                            %(T_val, N_val, T_val - N_val, T_val - N_val, B_val, sum_xy, sum_xy))

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            diff_xy = B_val # x - 2y = B_val
            diff_xy_s = diff_xy + randint(1, 3) * random.choice([-1, 1])

            # Các đáp án
            vd_da_1_d = '\\True Nếu gọi $x$ là số học sinh chỉ giỏi Toán và $y$ là số học sinh chỉ giỏi Văn thì $x - 2y = %s$' %(diff_xy)
            vd_da_1_s = 'Nếu gọi $x$ là số học sinh chỉ giỏi Toán và $y$ là số học sinh chỉ giỏi Văn thì $x - 2y = %s$' %(diff_xy_s)
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Số học sinh giỏi Toán là $x + %s$. Số học sinh giỏi Văn là $y + %s$. \\\\
            Theo bài ra, số học sinh giỏi Toán bằng hai lần số học sinh giỏi Văn nên ta có: \\\\
            $x + %s = 2(y + %s) \\Leftrightarrow x + %s = 2y + %s \\Leftrightarrow x - 2y = %s$.''' 
                            %(B_val, B_val, B_val, B_val, B_val, 2*B_val, diff_xy))

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            x_s = x_val + randint(1, 3) * random.choice([-1, 1])

            # Các đáp án
            vdc_da_1_d = '\\True Số học sinh chỉ giỏi Toán là $%s$' %(x_val)
            vdc_da_1_s = 'Số học sinh chỉ giỏi Toán là $%s$' %(x_s)
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Từ các ý trên ta có hệ phương trình: \\\\
            $\\begin{cases} x + y = %s \\\\ x - 2y = %s \\end{cases} \\Leftrightarrow \\begin{cases} 3y = %s \\\\ x = %s + 2y \\end{cases} \\Leftrightarrow \\begin{cases} y = %s \\\\ x = %s \\end{cases}$. \\\\
            Vậy số học sinh chỉ giỏi Toán là $%s$.''' 
                             %(sum_xy, B_val, sum_xy - B_val, B_val, y_val, x_val, x_val))

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

